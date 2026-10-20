"""Independent numerical checks of a conditional silicon-photonic correspondence.

No instrument measurements, network access, or public/audio mutations.
Uses NumPy spectral propagation, independent of the published real-pair update.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import numpy as np

HERE = Path(__file__).resolve().parent
CORE = HERE / 'direct-arrival-model-core.js'
OUT = HERE / 'verification.json'
checks = []
rng = np.random.default_rng(20261019)


def check(name, condition, **metrics):
    checks.append({'name': name, 'status': 'PASS' if condition else 'FAIL', **metrics})
    if not condition:
        raise AssertionError(name)


def propagator(h, length=1.0):
    w, v = np.linalg.eigh(h)
    return (v * np.exp(-1j * length * w)) @ v.conj().T


def pair(theta):
    return propagator(np.array([[0, theta], [theta, 0]], dtype=complex))


def layer(u, v, theta, n=12):
    h = np.zeros((n, n), dtype=complex)
    h[u, v] = h[v, u] = theta
    return propagator(h)


def schedule(coupled=True, scale=1.0):
    local = [(6*g+j, 6*g+(j+1) % 6, .035*scale)
             for g in range(2) for j in range(6)]
    return local + [(0, 6, (.085 if coupled else 0)*scale)] + list(reversed(local))


def circuit(coupled=True, scale=1.0):
    u = np.eye(12, dtype=complex)
    for a, b, angle in schedule(coupled, scale):
        u = layer(a, b, angle) @ u
    return u


def q_b(x):
    return float(np.vdot(x[6:], x[6:]).real)


def main():
    # Pairwise finite scattering is derived from two supermode phases.
    max_error = 0.0
    split = np.array([[1, 1], [1, -1]], complex) / np.sqrt(2)
    for theta in [0, .035, .085, -.085, np.pi/4, np.pi/2, 1.123]:
        modes = split @ np.diag(np.exp(-1j*np.array([theta, -theta]))) @ split.T
        exact = np.cos(theta)*np.eye(2) - 1j*np.sin(theta)*np.array([[0, 1], [1, 0]])
        max_error = max(max_error, float(np.max(np.abs(modes - exact))))
    check('Supermode finite propagation gives the published pair exchange', max_error < 2e-14,
          maximum_component_error=max_error)

    # Get real outputs of the deployed core. No Python recurrence copied from it.
    node = r"""
const M = require(process.argv[1]);
const results=[];
for (const phi of [0,Math.PI/2,-Math.PI/2,0.37]) {
  for (const coupled of [true,false]) {
    const x=M.seed(); M.phase(x,0,phi);
    for (let n=1;n<=37;n++) {
      M.step(x,M.schedule(coupled));
      if ([1,10,37].includes(n)) results.push({phi,coupled,n,x:M.copy(x)});
    }
  }
}
process.stdout.write(JSON.stringify(results));
"""
    observed = json.loads(subprocess.check_output(['node', '-e', node, str(CORE)], text=True))
    seed = np.sqrt(np.array([.6,.08,.08,.08,.08,.08]*2, float)).astype(complex)
    matrices = {True: circuit(True), False: circuit(False)}
    max_error = 0.0
    for record in observed:
        x = seed.copy()
        x[0] *= np.exp(1j*record['phi'])
        expected = np.linalg.matrix_power(matrices[record['coupled']], record['n']) @ x
        actual = np.array([complex(*z) for z in record['x']])
        max_error = max(max_error, float(np.max(np.abs(actual - expected))))
    check('Ordered 25-section optical matrix agrees with current JavaScript core', max_error < 2e-12,
          cases=len(observed), maximum_component_error=max_error)

    # Full 12-mode phase scan: coefficients are predicted, never fitted to samples.
    u = np.linalg.matrix_power(matrices[True], 10)
    one = np.zeros(12, complex)
    one[0] = seed[0]
    xb, yb = (u @ one)[6:], (u @ (seed-one))[6:]
    cross = np.vdot(yb, xb)
    ac, bs = 2*cross.real, -2*cross.imag
    baseline = q_b(u @ seed)
    max_error = 0.0
    for phi in np.linspace(-np.pi, np.pi, 97):
        x = seed.copy(); x[0] *= np.exp(1j*phi)
        response = q_b(u @ x)-baseline
        prediction = ac*(np.cos(phi)-1)+bs*np.sin(phi)
        max_error = max(max_error, abs(response-prediction))
    positive, negative = float(-ac+bs), float(-ac-bs)
    check('Entire graph obeys derived phase curve including unequal signed responses',
          max_error < 2e-13 and positive > 0 and negative < 0 and abs(positive+negative) > .1,
          cosine_coefficient=float(ac), sine_coefficient=float(bs),
          positive_quarter_turn_response=positive, negative_quarter_turn_response=negative,
          maximum_phase_curve_error=float(max_error))

    # Conservation applies to physical pulse energies only under declared encoding.
    max_norm_error = 0.0
    for _ in range(30):
        x = rng.normal(size=12)+1j*rng.normal(size=12)
        x *= np.sqrt(2)/np.linalg.norm(x)
        out = u @ x
        max_norm_error = max(max_norm_error, abs(np.vdot(out,out).real-2))
    unitarity_error = float(np.linalg.norm(u.conj().T@u-np.eye(12), 2))
    check('All-state norm conservation of the ideal full graph', max_norm_error < 2e-12,
          maximum_norm_error=float(max_norm_error), spectral_unitarity_error=unitarity_error)

    # Reset-and-cut and cut-after-history both forbid new source influence.
    off = np.linalg.matrix_power(matrices[False], 17)
    x = u @ seed
    reference = off @ x
    x[0] *= np.exp(1j*.734)
    response = np.max(np.abs((off @ x)[6:]-reference[6:]))
    block_error = np.max(np.abs(off[6:,:6]))
    check('Cut bridge blocks fresh source influence even after a connected history',
          response < 2e-13 and block_error < 2e-13,
          receiver_component_error=float(response), off_block_norm=float(block_error))

    # An inverse device reconstructs the signal in the ideal case; not lost heat.
    z = np.diag([1,-1])
    inverse_pair_error = np.max(np.abs(z@pair(.085)@z-pair(-.085)))
    restored = u.conj().T @ (u @ seed)
    inverse_error = np.max(np.abs(restored-seed))
    transmission = .81  # illustrative intensity transmission, not component data
    lossy_restored = (np.sqrt(transmission)*u.conj().T) @ (np.sqrt(transmission)*u@seed)
    restored_fraction = np.vdot(lossy_restored,lossy_restored).real / np.vdot(seed,seed).real
    check('Inverse phases work ideally but passive loss is not undone',
          inverse_pair_error < 2e-14 and inverse_error < 2e-12 and abs(restored_fraction-transmission**2) < 2e-12,
          pair_inverse_error=float(inverse_pair_error), full_inverse_error=float(inverse_error),
          illustrative_one_pass_intensity_transmission=transmission,
          illustrative_round_trip_energy_fraction=float(restored_fraction))

    # Phase mismatch gives a precise bounded departure, not a free efficiency fit.
    max_mismatch_error = 0.0
    g, delta, length = .8, 1.3, .7
    h = np.array([[delta/2, g],[g, -delta/2]], complex)
    omega = np.sqrt(g*g+(delta/2)**2)
    c, s, r, d = np.cos(omega*length), np.sin(omega*length), g/omega, delta/(2*omega)
    for phi in np.linspace(-np.pi,np.pi,41):
        inp = np.array([np.exp(1j*phi),1])
        out = propagator(h,length)@inp
        prediction = 2*r*s*c*np.sin(phi)-2*r*d*s*s*np.cos(phi)
        max_mismatch_error = max(max_mismatch_error, abs((abs(out[1])**2-1)-prediction))
    unseeded = propagator(h,length)@np.array([1,0],complex)
    bound = g*g/(g*g+(delta/2)**2)
    check('Detuning law and maximum unseeded-transfer bound',
          max_mismatch_error < 2e-13 and abs(unseeded[1])**2 <= bound+1e-13,
          maximum_formula_error=float(max_mismatch_error), transfer_upper_bound=float(bound))

    # Unequal loss: integrate state and physical loss account with independent RK4.
    gamma = np.diag([.13,.41])
    gen = -1j*h - gamma/2
    x0 = np.array([np.exp(.71j),.83], complex)
    def integrate(n):
        dt = 2.0/n
        y = np.r_[x0, 0j]
        def f(state):
            x = state[:2]
            return np.r_[gen@x, np.vdot(x,gamma@x).real]
        for _ in range(n):
            k1=f(y); k2=f(y+dt*k1/2); k3=f(y+dt*k2/2); k4=f(y+dt*k3)
            y += dt*(k1+2*k2+2*k3+k4)/6
        return y
    y1, y2 = integrate(1000), integrate(2000)
    defect = abs(np.vdot(x0,x0).real-np.vdot(y2[:2],y2[:2]).real-y2[2].real)
    check('Unequal-loss differential account closes without hidden normalization',
          defect < 2e-11 and np.max(np.abs(y1-y2)) < 2e-10 and y2[2].real > 0,
          energy_balance_defect=float(defect), refinement_difference=float(np.max(np.abs(y1-y2))),
          lost_account=float(y2[2].real))

    # Continuous all-edges-on hardware is a different map from the specified schedule.
    errors=[]
    for scale in [1,.5,.25]:
        hsum=np.zeros((12,12),complex)
        for a,b,t in schedule(True,scale):
            hsum[a,b]+=t; hsum[b,a]+=t
        errors.append(float(np.linalg.norm(circuit(True,scale)-propagator(hsum),2)))
    ratios=[errors[i]/errors[i+1] for i in range(2)]
    check('Simultaneous coupling countermodel differs with cubic split-step error',
          errors[0] > 1e-6 and all(7.7 < r < 8.3 for r in ratios),
          spectral_differences=errors, halving_ratios=ratios)

    # Contraction gives a passive loss budget for an arbitrary independently encoded state.
    attenuation=np.diag(np.sqrt(np.linspace(.7,.95,12)))
    t=attenuation@u
    x=seed*np.exp(1j*np.linspace(0,.9,12))
    missing=float(np.vdot(x,(np.eye(12)-t.conj().T@t)@x).real)
    direct=float(np.vdot(x,x).real-np.vdot(t@x,t@x).real)
    check('General passive port-energy deficit is nonnegative and accounted',
          missing >= 0 and abs(missing-direct) < 2e-13,
          missing_account=missing, identity_error=abs(missing-direct))

    # Source phase-setting error, no unknown fitted functions.
    eps=.01
    bound=2*abs(seed[0])*abs(np.sin(eps/2))
    x=seed.copy(); x[0]*=np.exp(1j*eps)
    actual=float(np.linalg.norm(u@x-u@seed))
    check('Source phase-error bound is preserved through the ideal circuit',
          abs(actual-bound)<2e-13, illustrative_phase_error=eps,
          state_error=actual, analytic_bound=float(bound))

    receipt={'status':'PASS','evidence':'synthetic mathematical verification; no physical measurements',
             'timestamp_utc':datetime.now(timezone.utc).isoformat(),
             'model_core_sha256':hashlib.sha256(CORE.read_bytes()).hexdigest(),
             'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'numpy_version':np.__version__,'checks':checks}
    OUT.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':
    main()
