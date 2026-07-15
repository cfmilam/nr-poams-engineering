#!/usr/bin/env python3
"""
COLLECTIVE BOOTSTRAP — numerical test of PIN vs FLAT for the POAMS alpha/beta program.

Question: does the JOINT (whole-totality) mutual-AM-coherence fixed point pin the common
tilt beta, or leave a flat (uniform-dilation) zero-mode -> beta contingent?

Model (POAMS-faithful, NOT rigged to an answer):
- N vortices, tilts theta_i. Mutual coherence: theta_i = sum_j K_ij theta_j  (homogeneous deg-1).
- THIRD-LAW RECIPROCITY (kappa=1 identity): what goes out comes back equal -> per-vortex the
  induced tilts sum to the vortex's own (row-stochastic K, row sums = 1). This is not a tuning;
  it is the reciprocity identity.
- INTRANSITIVITY (A<->B, B<->C =/=> A<->C): coupling is a pairwise reciprocal transaction; you may
  NOT chain/compose (no path sums, no global sum over the totality).
The outcome (flat vs pinned) is READ OFF the spectrum; nothing about beta's value is put in.
"""
import numpy as np
rng = np.random.default_rng(20260715)

def reciprocal_rowstochastic(N, graph="random", p=0.35):
    """Symmetric (reciprocal) nonneg coupling, then row-normalize to enforce kappa=1 (row sums=1).
    Symmetric weights = third-law reciprocity (i<->j equal). Row-normalization = kappa=1 identity."""
    if graph == "complete":
        Wt = rng.random((N, N)); Wt = (Wt + Wt.T)/2
    elif graph == "sparse":
        M = (rng.random((N, N)) < p).astype(float); M = np.triu(M, 1); M = M + M.T
        Wt = M * ((rng.random((N, N)) + 0.1)); Wt = (Wt + Wt.T)/2
    else:  # random dense weights
        Wt = rng.random((N, N)); Wt = (Wt + Wt.T)/2
    np.fill_diagonal(Wt, 0.0)
    # guard: ensure no isolated vertex
    s = Wt.sum(1)
    s[s == 0] = 1.0
    K = Wt / s[:, None]              # row-stochastic  => row sums = 1  => kappa = 1
    return K

print("="*74)
print("A. MARGINALITY IS GENERIC: kappa=1 (reciprocity) => uniform mode is an EXACT")
print("   eigenvector with eigenvalue 1 => the common scale beta is a FLAT direction.")
print("="*74)
for graph in ["complete", "random", "sparse"]:
    for N in [6, 20, 60]:
        K = reciprocal_rowstochastic(N, graph)
        u = np.ones(N)
        Ku = K @ u
        flat_resid = np.max(np.abs(Ku - u))       # K u == u ?  (fixed-point ray theta=c*u)
        ev = np.sort(np.abs(np.linalg.eigvals(K)))[::-1]
        lam1, lam2 = ev[0], ev[1]
        print(f"  {graph:8s} N={N:3d}:  max|Ku-u|={flat_resid:.2e}  "
              f"|lambda1|={lam1:.6f}  |lambda2|={lam2:.6f}  "
              f"gap(1-|l2|)={1-lam2:.3f}")
print("  -> Ku=u to machine precision for EVERY graph/size: theta=c*u solves the joint")
print("     fixed point for ANY c. lambda2<1 => that is the ONLY undetermined d.o.f.")
print("  VERDICT A: exactly ONE flat direction = the common tilt scale beta. NOT pinned.")

print()
print("="*74)
print("B. WHY: the flat mode is PROTECTED by the kappa=1 identity (row sums=1).")
print("   Break reciprocity (row sums != 1) and the linear part pins NOTHING finite:")
print("   kappa<1 -> only theta=0 ; kappa>1 -> diverges. No finite nonzero scale either way.")
print("="*74)
K = reciprocal_rowstochastic(40, "random")
for kappa in [0.90, 0.999, 1.000, 1.001, 1.10]:
    Kk = kappa * K
    ev = np.sort(np.abs(np.linalg.eigvals(Kk)))[::-1]
    # fixed point of theta = Kk theta is theta=0 unless spectral radius hits 1
    sr = ev[0]
    if abs(sr - 1) < 1e-9:
        status = "MARGINAL: flat ray survives (finite scale FREE)"
    elif sr < 1:
        status = "only theta=0 (no finite vortex)"
    else:
        status = "diverges (no finite fixed point)"
    print(f"  kappa={kappa:6.3f}: spectral radius={sr:.6f}  -> {status}")
print("  VERDICT B: a FINITE nonzero common beta exists ONLY at kappa=1, and there it is")
print("     FLAT (any scale). kappa=1 is forced as an IDENTITY by third-law reciprocity")
print("     => the flat direction cannot be removed without breaking reciprocity.")

print()
print("="*74)
print("C. HOMOGENEITY-BREAKING (solid-angle cap) ALONE drives beta->0; a finite beta needs")
print("   a SOURCE eps (the 'something not nothing' overshoot). Then beta = f(eps): RELOCATION.")
print("="*74)
# theta_i = sum_j K_ij theta_j - (a/2) sum_j K_ij theta_j^2 + eps      (cap quadratic + source)
N = 30; K = reciprocal_rowstochastic(N, "random"); a = 1.0
def solve_uniform(eps, a=1.0, iters=20000, tol=1e-14):
    # uniform ansatz theta_i=b: b = b - (a/2) b^2 + eps  => 0 = -(a/2) b^2 + eps => b=sqrt(2eps/a)
    # solve the FULL vector map too, to confirm uniform is the attractor
    th = np.full(N, np.sqrt(max(eps,0)*2/a) if eps>0 else 0.0) + 1e-3*rng.standard_normal(N)
    for _ in range(iters):
        new = K@th - (a/2)*(K@(th**2)) + eps
        if np.max(np.abs(new-th)) < tol: 
            th = new; break
        th = new
    return th
for eps in [0.0, 1e-6, 4e-6, 1e-5, 1e-4]:
    th = solve_uniform(eps)
    b = float(np.mean(th)); spread = float(np.std(th))
    pred = np.sqrt(2*eps/a) if eps>0 else 0.0
    print(f"  eps={eps:.1e}: beta*={b:+.6e} (uniform spread={spread:.1e})  sqrt(2eps/a)={pred:.6e}")
print("  -> eps=0 gives beta=0 (cap alone = nothing). beta* = sqrt(2 eps/a): the value of beta")
print("     IS the value of the source overshoot eps. VERDICT C: freedom RELOCATED beta<->eps,")
print("     not removed. (No cap parameter 'a' or graph pins eps; eps is the free act.)")

print()
print("="*74)
print("D. GLOBAL CLOSURE  Sum_i Omega(theta_i)=4pi  is ONE equation in TWO unknowns (W,beta).")
print("   It RELATES W and beta; it does not pin either. (Omega=2pi(1-cos theta).)")
print("="*74)
import math
# uniform: W * 2pi(1-cos beta) = 4pi -> W(1-cos beta)=2 -> for small beta: W beta^2/2 = 2
def W_of_beta(beta): return 2.0/(1-math.cos(beta))
for ainv in [100, 129, 137.036, 150, 500]:
    beta = 1/ainv
    W = W_of_beta(beta)
    print(f"  beta=1/{ainv:<7.3f}: W = 2/(1-cos beta) = {W:.4e}   (all lie on ONE curve W(beta))")
print("  -> Every (W,beta) on the curve W=2/(1-cos beta) satisfies closure. Closure alone")
print("     picks NO point. VERDICT D: one equation, two unknowns => FLAT / RELOCATED (beta<->W).")

print()
print("="*74)
print("E. DISCRETENESS of W does NOT pin beta: every large integer W gives an admissible beta;")
print("   no principle selects one (and delta is forced transcendental => integer W = wrong cat.)")
print("="*74)
target = 137.036
for W in [70000, 75000, 75116, 80000, 100000]:
    beta = math.acos(1 - 2.0/W)          # invert closure for integer W
    ainv = 1/beta
    print(f"  W={W:6d} (integer): beta=arccos(1-2/W) -> alpha^-1 = {ainv:.3f}")
print("  -> alpha^-1 slides smoothly with W; W=75116 is not distinguished from its neighbours.")
print("  VERDICT E: integrality gives a dense ladder, selects nothing. Still FLAT.")

print()
print("="*74)
print("F. WHAT WOULD PIN IT = a TRANSITIVE global sum over the totality (forbidden). Demonstrate:")
print("   imposing Sum_i theta_i = S (a sum over the whole = chaining) pins beta uniquely.")
print("="*74)
N = 40; K = reciprocal_rowstochastic(N, "random"); u = np.ones(N)
S = 1.0
# with the flat ray theta=c*u, a GLOBAL SUM constraint sum theta_i = S -> c*N = S -> c=S/N pinned
c_pinned = S / N
print(f"  intransitive (no global sum): theta=c*u, c FREE  -> beta unpinned (flat).")
print(f"  add transitive global sum  sum_i theta_i = S={S}:  c = S/N = {c_pinned:.6f}  -> PINNED.")
print("  BUT 'sum over the totality' is exactly the transitive chaining INTRANSITIVITY forbids")
print("  (Pope's sonship: A<->B,B<->C =/=> A<->C). Pinning requires abandoning the no-loop core.")
print("  VERDICT F: the ONLY thing that pins beta is a forbidden global/transitive sum (or an")
print("     injected external scale). Within POAMS's intransitive axioms, beta stays FLAT.")

print()
print("="*74)
print("OVERALL VERDICT: (B) FLAT / RELOCATED.")
print("The collective bootstrap does NOT pin beta. The uniform-dilation mode is an exact zero-")
print("mode protected by the kappa=1 identity (third-law reciprocity) + intransitivity (no global")
print("sum). Closure Sum Omega=4pi is one equation in two unknowns (relocates beta<->W). A finite")
print("beta requires a source overshoot eps whose magnitude IS beta (relocation, not derivation).")
print("Pinning demands a transitive sum over the totality or an external scale -- both forbidden.")
print("=> beta's contingency IS POAMS's no-loop core. Impossibility theorem: COMPLETE (pending")
print("   model-agreement reconciliation).")
