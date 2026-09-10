# The n-Centre Closure Derivation

Ratified theorem record — 2026-09-09. P1–P5, the ephemeris, belt, and history
instruments, and the resulting claim boundaries are ratified. This document answers
the four open items named
by *The Solar System*: the general orbital Hamiltonian, the radial law, channel
widths, and capture selection. It is deliberately stricter than the 2026-08-10 T3
note: no bracketed three-body width is promoted to a derivation.

## 0. Verdict at a glance

1. **General n-centre orbital Hamiltonian: derived on ratified P1–P5.** In the
   relational Euclidean chart and point-centre orbital tier,
   the exact all-centre Hamiltonian is

   \[
   \boxed{\mathcal H=\sum_{i=1}^{N}\frac{|\boldsymbol\pi_i|^2}{2w_i}
   -\Gamma\sum_{i<j}\frac{w_iw_j}{r_{ij}}},\qquad
   r_{ij}=|\mathbf q_i-\mathbf q_j|.
   \]

   Here \(w_i>0\), \(\sum_iw_i=1\), is the measured share of the joint momentum
   ledger and \(\Gamma\) is the measured system circulation scale. Neither mass nor
   \(G\) occurs. This is an exact reparameterization of the point-centre inverse-square
   dynamics, not a claimed closed-form solution of its trajectories.

2. **Radial law: derived on the ratified zero-remainder joint.** POAMS whole-turn closure plus Bertrand's
   theorem leaves the Kepler and isotropic-oscillator branches. The latter is removed
   by the **zero-remainder boundary lemma**: when the relational overlap of a pair is
   removed, that pair's booked term must tend to zero, not grow without bound. This
   lemma is physically native to a two-ended transaction and was ratified with P1–P5
   by Star Lord on 2026-09-09. It remains printed because it is load-bearing, not
   because its status is provisional.

3. **Channel widths: derived as a general computation, not one universal scalar
   formula.** Every isolated primitive integer channel has a Fourier coefficient
   obtained directly from the Hamiltonian and a resonant normal form. At leading
   single-harmonic order its beat-rate half-width is

   \[
   \boxed{W_{\mathbf k}=2\sqrt{|A_{\mathbf k}C_{\mathbf k}|}},\qquad
   A_{\mathbf k}=\mathbf k^T D^2\!\mathcal H_0\,\mathbf k.
   \]

   Higher-order coefficients are computed recursively. In an overlapping
   multi-resonance domain, a unique scalar width does not exist; the honest object is
   the connected resonant domain on a surface of section.

4. **Why this system captured these locks: conditional probabilities are derivable;
   a unique history is not.** An autonomous Hamiltonian preserves phase-space volume
   and has no attracting resonance. Capture requires additional ledger centres—disc,
   tide, spin, impact, or loss channels—which make the orbital subsystem nonautonomous.
   The present orbital census does not contain their initial conditions. This is an
   information boundary, not a missing algebraic trick.

## 1. Primitive ledger statements

Only the following are used.

- **P1 — relational centres.** Positions are chart coordinates; only differences
  \(\mathbf q_i-\mathbf q_j\) enter. Translation and rotation of the whole chart
  cannot change the books.
- **P2 — additive shares.** A centre carries a positive measured ledger share \(w_i\).
  Splitting one resolved centre into co-moving subcentres adds their shares. Normalize
  \(\sum_iw_i=1\).
- **P3 — two-ended, intransitive settlement.** A primitive transaction is co-signed by
  exactly two centres. Therefore the primitive interaction book is a sum over pairs;
  there is no primitive three-centre term. Effective three-centre channels may still
  arise by composition in the dynamics, but no A-to-C transaction is inserted merely
  because A-B and B-C exist.
- **P4 — whole-turn persistence.** Every stable bounded natural orbit in the ideal
  isolated two-centre family closes without secular phase leakage. This deliberately
  strong statement is the exact hypothesis Bertrand's theorem needs; real precession
  is then booked to additional centres or additional channels. If POAMS licenses only
  selected closed orbits, Bertrand cannot determine the radial law.
- **P5 — zero-remainder boundary (ratified 2026-09-09).** If a pair's relational overlap is
  removed, its pair term tends to zero. Removing a possible transaction may not leave
  an infinite bill. This is the only added POAMS joint in the radial derivation.

P1–P5 were ratified by Star Lord on 2026-09-09. Ratification fixes the premises; it
does not convert imported mathematics into POAMS work or excuse a failed confrontation.

The canonical/action-angle machinery below is a named mathematical representation.
It does not introduce a second physical substance.

## 2. The coefficient theorem

Let \(B(x,y)\) be the amplitude assigned to a primitive pair whose endpoint shares
are \(x\) and \(y\). Endpoint symmetry gives \(B(x,y)=B(y,x)\). Ledger additivity gives

\[
B(x_1+x_2,y)=B(x_1,y)+B(x_2,y)
\]

and the same relation in the second argument. Positivity/continuity removes pathological
Cauchy solutions. Every continuous symmetric bi-additive map on the positive reals is

\[
\boxed{B(x,y)=\Gamma xy}.
\]

Thus the familiar product is not a mass postulate here. It is the only coefficient
that respects endpoint co-signing and ledger splitting. \(\Gamma\) sets the measured
scale of the whole system.

Define the individual measured circulation strengths

\[
\gamma_i\equiv\Gamma w_i.
\]

For an isolated pair, the relative-orbit invariant is then

\[
\boxed{\mu_{ij}=\gamma_i+\gamma_j=\Gamma(w_i+w_j)}.
\]

For any three distinct centres,

\[
\boxed{\gamma_i=\tfrac12(\mu_{ij}+\mu_{ik}-\mu_{jk})}.
\]

With \(N\ge3\), complete pair-invariant data therefore reconstruct every \(\gamma_i\),
then \(\Gamma=\sum_i\gamma_i\) and \(w_i=\gamma_i/\Gamma\). Independence of the chosen
pair \((j,k)\) is an overdetermined closure test. For \(N=2\), \(\mu_{12}=\Gamma\) and
one barycentric partition datum is necessarily required, exactly as found in T1.

### 2.1 The absolute-scale boundary is a theorem, not unfinished algebra

Integer closures and share ratios are dimensionless. They cannot select a dimensional
system scale. Under

\[
\mathbf q\mapsto a\mathbf q,\qquad t\mapsto b t,\qquad
\Gamma\mapsto \frac{a^3}{b^2}\Gamma,
\]

the equations keep the same dimensionless trajectories and every integer phase
closure is unchanged. Therefore no argument built only from closure integers can
derive a numerical \(\Gamma\) in length\(^3\)/time\(^2\). One measured rod–clock
calibration is logically necessary. Once a pair invariant and one barycentric
partition are measured, its two endpoint strengths follow:

\[
\gamma_i=f_i\mu_{ij},\qquad \gamma_j=(1-f_i)\mu_{ij}.
\]

The remaining solar-system strengths are then overdetermined by other pair invariants
and perturbations. Thus the **form and identifiability** of the scale are derived; its
numerical value is contingent measurement, not an open POAMS constant awaiting
numerology.

## 3. The radial theorem

P1 and P3 make a primitive pair term rotationally invariant:

\[
V_{ij}=B(w_i,w_j)\,U(r_{ij}).
\]

The isolated relative problem is central, so orbital angular momentum is conserved.
P4 now supplies the nontrivial condition: every stable bounded orbit in the ideal
two-centre family closes. Bertrand's theorem permits only

\[
U_K(r)=-\frac1r
\quad\text{or}\quad
U_H(r)=\frac12\omega_*^2r^2.
\]

P5 excludes \(U_H\), because it grows rather than vanishes when the pair relation is
removed. Fixing the irrelevant additive constant by \(U(\infty)=0\) leaves

\[
\boxed{U(r)=-1/r},\qquad
\boxed{-\nabla U=-\frac{\mathbf r}{r^3}}.
\]

This is the inverse-square **radial bookkeeping rate** in the relational chart—not a
force or carrier crossing a void. Without P4 there are infinitely many central laws;
without P5 Bertrand leaves two. Angular-momentum conservation alone never fixes the
radial power.

The measured sky independently discriminates the two Bertrand branches. For circular
members the Kepler branch keeps \(n^2a^3\) approximately constant within a host ledger;
the oscillator branch keeps \(n^2\) constant. The JPL major-moon census gives normalized
ranges:

| Host | Bodies | range of \(n^2a^3\)/mean | range of \(n\)/mean |
|---|---:|---:|---:|
| Jupiter | 4 | 1.52% | 193% |
| Saturn | 7 | 0.972% | 246% |
| Uranus | 5 | 0.0378% | 206% |
| Neptune | 2 | 0.149% | 136% |

The residual Kepler-branch spread is expected because these are fitted mean elements
inside genuinely many-centre, oblate-primary systems. The branch separation is still
orders of magnitude.

## 4. The exact n-centre orbital book

The kinetic term is fixed inside the relational Euclidean chart as follows. Isotropy
makes a one-centre free term a function of \(|\dot{\mathbf q}|^2\); Galilean change of
chart may alter the action only by a total time derivative, which forces that function
to be affine in \(|\dot{\mathbf q}|^2\). The irrelevant constant drops out. Additivity
under ledger splitting then makes the coefficient proportional to \(w_i\), and the
choice of time/length units fixes the common factor to \(1/2\). Thus the quadratic
kinetic chart is not an additional fitted law.

With P1-P5, the per-unit-total-ledger Lagrangian and its Hamiltonian are

\[
\mathcal L=\frac12\sum_iw_i|\dot{\mathbf q}_i|^2
+\Gamma\sum_{i<j}\frac{w_iw_j}{r_{ij}},
\]

\[
\boxed{\mathcal H=\sum_i\frac{|\boldsymbol\pi_i|^2}{2w_i}
-\Gamma\sum_{i<j}\frac{w_iw_j}{r_{ij}}},\qquad
\boldsymbol\pi_i=w_i\dot{\mathbf q}_i.
\]

Hamilton's equations give every centre simultaneously:

\[
\ddot{\mathbf q}_i=-\Gamma\sum_{j\ne i}w_j
\frac{\mathbf q_i-\mathbf q_j}{r_{ij}^3}.
\]

No patched conics and no time-dependent pair invariant are required. The pair
invariants are projections of the one fixed set \(\{\gamma_i\}\); apparent variation
of an osculating two-body \(\mu\) is the omitted-centre remainder.

The scope of “exact” is precise: exact for the point-centre orbital Hamiltonian with
the derived pair kernel. Finite-size, oblateness, tides, intrinsic spin, relativistic
anholonomy, and unresolved centres are additional named terms—not errors hidden in a
fitted \(\mu_{ij}(t)\).

### 4.1 Discreteum propagator

Split \(\mathcal H=T+V\) and use kick-drift-kick:

\[
\begin{aligned}
\boldsymbol\pi_i^{m+1/2}&=\boldsymbol\pi_i^m-\tfrac12\Delta t\,\nabla_iV(\mathbf q^m),\\
\mathbf q_i^{m+1}&=\mathbf q_i^m+\Delta t\,\boldsymbol\pi_i^{m+1/2}/w_i,\\
\boldsymbol\pi_i^{m+1}&=\boldsymbol\pi_i^{m+1/2}-\tfrac12\Delta t\,\nabla_iV(\mathbf q^{m+1}).
\end{aligned}
\]

Each pair kick is equal and opposite, so \(\sum_i\boldsymbol\pi_i\) is unchanged.
Each kick is central, so pair torque vanishes. Each drift is parallel to its own
momentum, so \(\sum_i\mathbf q_i\times\boldsymbol\pi_i\) is unchanged. Total linear
and angular momentum are therefore conserved by construction at every discrete step,
apart from arithmetic roundoff. This is the fundamental propagator; the differential
Hamiltonian is its smooth chart.

## 5. Every isolated channel, from the same Hamiltonian

Choose any hierarchical action-angle chart \((\mathbf J,\boldsymbol\theta)\) for the
uncoupled part \(\mathcal H_0\). The remaining exact pair book has the torus expansion

\[
\mathcal H_1(\mathbf J,\boldsymbol\theta)
=\sum_{\mathbf k\in\mathbb Z^d}C_{\mathbf k}(\mathbf J)
\cos(\mathbf k\!\cdot\!\boldsymbol\theta+\psi_{\mathbf k}),
\]

with coefficients defined without a Laplace-table import:

\[
\boxed{C_{\mathbf k}e^{i\psi_{\mathbf k}}=
\frac{1}{(2\pi)^d}\int_{\mathbb T^d}\mathcal H_1
e^{-i\mathbf k\cdot\boldsymbol\theta}\,d^d\theta}.
\]

Rotational invariance enforces the d'Alembert selection rule. Multiples of a vector
name the same angle, so candidates are primitive integer vectors only.

For a primitive \(\mathbf k\), choose an integer unimodular canonical transformation
whose first angle is \(\phi=\mathbf k\cdot\boldsymbol\theta\) and first action is
\(I\). At a root \(\mathbf k\cdot\boldsymbol\omega(\mathbf J_*)=0\), the isolated
single-harmonic normal form is

\[
K=K_*+\delta I+\frac12A_{\mathbf k}I^2
-|C_{\mathbf k}|\cos\phi+\mathcal R,
\qquad
A_{\mathbf k}=\mathbf k^TD^2\!\mathcal H_0(\mathbf J_*)\mathbf k.
\]

Dropping only the explicitly bounded remainder \(\mathcal R\), the separatrix energy
gives

\[
\Delta I=2\sqrt{\left|\frac{C_{\mathbf k}}{A_{\mathbf k}}\right|},\qquad
\omega_{\rm lib}=\sqrt{|A_{\mathbf k}C_{\mathbf k}|},\qquad
\boxed{W_{\mathbf k}=2\omega_{\rm lib}}.
\]

Thus “\(\dot\Phi\approx0\)” acquires a computed meaning:

\[
|\mathbf k\cdot\boldsymbol\omega|<W_{\mathbf k},
\]

followed by the empirical requirement of bounded libration. For higher accuracy, retain
additional Fourier terms and determine the saddle/centre contours of the averaged
Hamiltonian numerically. A claimed width is released with the normal-form remainder
bound. Where two separatrices overlap, no invariant single-channel width exists; the
whole connected resonant domain must be propagated.

### 5.1 The missing three-body coefficient is no longer guessed

Because P3 permits only primitive pair terms, a harmonic whose integer vector has
support on three centres is absent at first order. It appears at second order through
two pair harmonics sharing a centre.

Write \(\mathcal H=\mathcal H_0+\epsilon\mathcal H_1\). Let \(\chi_1\) solve the
homological equation

\[
\{\chi_1,\mathcal H_0\}=-(\mathcal H_1-\langle\mathcal H_1\rangle),
\qquad
(\chi_1)_{\mathbf u}=
\frac{(\mathcal H_1)_{\mathbf u}}{i\,\mathbf u\cdot\boldsymbol\omega}
\quad(\mathbf u\cdot\boldsymbol\omega\ne0).
\]

The leading coefficient of a genuine three-centre angle \(\mathbf k\) is the
\(\mathbf k\)-Fourier component of the second-order Lie term

\[
\boxed{C^{(2)}_{\mathbf k}=\left[
\tfrac12\{\chi_1,\mathcal H_1-\langle\mathcal H_1\rangle\}
+\{\chi_1,\langle\mathcal H_1\rangle\}
\right]_{\mathbf k}}.
\]

Equivalently it is a sum over \(\mathbf u+\mathbf v=\mathbf k\) of cross-brackets of
pair coefficients and their action derivatives, divided by the nonresonant pair beats.
For the Galilean vector \((1,-3,2)\), the decomposition
\((1,-2,0)+(0,-1,2)=(1,-3,2)\) shows the source directly. The previously bracketed
\(f'^2\)-to-first-order “width” is retired as a derivation; the coefficient must be
computed by this cross-bracket before a quantitative width is claimed.

This is the exact algebraic form of the leading effective three-body term for a chosen
Hamiltonian split. An “exact one-degree-of-freedom three-body Hamiltonian” at all
orders generally does not exist: fast and overlapping angles cannot be removed
globally in a nonintegrable system. The exact object is the full n-centre Hamiltonian
above; channel Hamiltonians are controlled normal forms.

The audit evaluates the published direct, circular, second-order specialization for
Io–Europa–Ganymede, normalized to \(a_{Europa}=n_{Europa}=1\), using the measured
ledger-share ratios already registered in N3. For \(\mathbf k=(1,-3,2)\):

\[
C_{\mathbf k}^{(2)}=4.55333\times10^{-13},\quad
A_{\mathbf k}=-1.28919\times10^6,\quad
W_{\mathbf k}/n_E=1.53233\times10^{-3}.
\]

The observed beat is \(3.40770\times10^{-8}n_E\), hence

\[
\boxed{|\dot\Phi|/W=2.224\times10^{-5}}
\]

or about **44,970 times inside** that isolated leading normal form. This replaces the
former guessed bracket with an evaluated coefficient, but the number is **not** a
precision physical width for the real Galilean chain. The real system is a connected
two-resonance domain, so indirect terms, eccentric harmonics, Jupiter's figure, and
neighboring angles cannot be gathered into one invariant scalar remainder.

The ephemeris-grade audit therefore tests the correct object. It reads the integrated
JPL JUP365 solution directly over 2000–2030 without re-propagating osculating elements.
The Laplace angle remains centred at 180°, spans only 0.844°, and retains that bounded
cluster in both 15-year halves and at 1/2/4/8-day cadences. Of the four first-order
2:1 eccentricity arguments, exactly three librate and the Ganymede-pericentre argument
circulates. Their dominant slow period is 476.48 days. This 3-of-4 topology is the
connected-channel signature; it also demonstrates why the isolated coefficient is an
identification calculation rather than the system's precision width.

The same preregistered instrument now tests the other named locks instead of relying
on period ratios. Node-bearing satellite arguments are evaluated in Horizons'
central-body equator-and-node-of-date frame; using the J2000 ecliptic for these angles
is a coordinate error. Over 2000–2030, Mimas–Tethys spans 155.30°, Enceladus–Dione
42.88°, Titan–Hyperion 105.91°, and Naiad–Thalassa 106.78°; every argument remains
bounded in both 15-year halves. Janus–Epimetheus is retained as a report-only
horseshoe exchange control because its co-orbital angle is not a single semicircular
cluster.

The long-period planetary test uses the DE441 Neptune and Pluto barycentres directly
from 9000 BC through AD 9000. The resonant argument
(3\lambda_P-2\lambda_N-\varpi_P) spans 159.68° and remains bounded in both
9,000-year halves. Horizons rejected the preregistered 100-day request under its row
ceiling; the recorded 400-day instrument cadence is still orders finer than the
millennial libration. The strongest FFT bin is window-limited at 18,000 years, so the
audit claims bounded libration—not a precision libration period.

No claim in the present exhibit depends on an unbounded normal-form remainder. The
Galilean chain is released on its directly observed connected-angle topology, not on
the isolated scalar estimate. The four main-belt widths are explicitly leading-order
predictions and are released only with their preregistered population comparisons.
Higher-order accuracy remains a case-by-case calculation under the general algorithm;
it is not a missing universal term in the n-centre Hamiltonian.

### 5.2 A closure can store or clear a population

The integer vector \(\mathbf k\) identifies a candidate channel; it does not determine
the channel's fate. A libration island can confine trajectories. A separatrix that
reaches a planet-crossing boundary, or overlaps neighboring channels, can instead
produce chaotic diffusion and remove trajectories from a region. “Destructive” means
loss from the chosen orbital census—not destruction of the conserved substance.

The main asteroid belt is the population-level control. Its major Kirkwood gaps occur
at asteroid–Jupiter mean-motion closures, while the Saturn-linked \(\nu_6\) apsidal
closure helps bound the belt near 2.1 AU. Yet Jupiter's 3:2 Hilda resonance contains a
stable concentration. Therefore no rule of the form “integer resonance implies
clearing” is licensed. The sign and geometry of the evaluated coefficient, channel
overlap, and access to an escape boundary must be computed from the full Hamiltonian.
The observed gaps are empirical evidence for those destructive channels; they are not
deduced from the integers alone.

The registered N4 population audit now closes the leading forward test. The pair
kernel predicts the 3:1, 5:2, 7:3, and 2:1 centres to within 0.014%. After correcting
an old conversion error—\(W_\phi\) contains \(q\), but
\(\delta n=W_\phi/q\)—the predicted half-widths at \(e=0.15\) are 0.01436,
0.00917, 0.00535, and 0.07848 AU. JPL SBDB population gaps differ by factors 2.09,
1.64, 2.14, and 1.36, all inside the registered factor-three gate. The independent
1.25-million-body synthetic proper-orbit catalog gives 0.00500 AU for 7:3, only a
factor 1.07 from the prediction.

The same widened population pull supplies the storage control: numbered \(H\le15\)
asteroids within 0.05 AU of the 3:2 Hilda centre are 339 times denser per AU than
the registered equal-width sidebands. Destructive channels also have a calculable
escape target. From the derived centre \(a\), Mars crossing begins at
\(e>1-Q_{Mars}/a\): 0.334, 0.410, 0.437, and 0.492 for the four gaps. Thus the
forward result is not “an integer makes a hole.” The coefficient fixes a local
channel; eccentricity growth and access to the crossing boundary decide removal.

## 6. Capture: what can and cannot be derived

For the pendulum normal form the libration-island area is

\[
\mathcal A_{\rm lib}=16\sqrt{|C_{\mathbf k}/A_{\mathbf k}|}.
\]

An autonomous Hamiltonian flow is symplectic and preserves phase-space volume. It
cannot make this island an attractor. Therefore permanent capture requires a changing
detuning or channel coefficient produced by additional booked centres. After those
centres are included and then projected out, define

\[
\eta_{\mathbf k}=\frac{|\dot\delta|}{\omega_{\rm lib}^2},
\qquad \delta(t)=\mathbf k\cdot\boldsymbol\omega(t).
\]

- \(\eta\ll1\): adiabatic separatrix encounter; capture is possible, and can become
  certain in restricted low-action regimes.
- \(\eta\gtrsim1\): fast crossing; capture probability falls and must be integrated
  from the actual phase ensemble.
- A shrinking \(\mathcal A_{\rm lib}\) cannot acquire phase volume; a growing island
  can. The probability is the captured phase-volume flux divided by the incident
  flux, computed from the extended model—not assigned from a period ratio.

The required inputs are the time histories of \(\delta\), \(C_{\mathbf k}\), damping,
and the incoming action/phase distribution. The present JPL state supplies none of
those histories by itself, but the wider published record supplies important
constraints: astrometric migration and dissipation rates, thermal and geological
states, formation calculations, and the resonant/non-resonant populations surrounding
some locks. These data define **measurement-constrained ensembles of admissible
histories**. They are not one uniquely recoverable trajectory.

Consequently POAMS can derive conditional capture and survival maps over a registered
historical ensemble. Competing reservoirs are then compared by whether they jointly
reproduce the lock, neighboring non-locks, and independent thermal or population
evidence. Time reversal, chaotic branching, and incomplete initial data still forbid
claiming one unique reason for today's architecture from the endpoints alone.

### 6.1 The published history ensemble has been executed

The history audit registers eight model families without pooling incompatible priors.
It preserves each reservoir, initial-condition family, sample size, reported frequency,
and failed outcome. Three results are sharp:

1. **Some reservoir classes are selected.** Sixteen Neptune-migration experiments
   (twelve grainy, four smooth, one million test bodies each) favor outward grainy
   migration when the resonant/non-resonant population and libration amplitudes are
   scored together. A 67-system 2026 update independently favors a jumping/grainy
   family while retaining named failures. The asteroid belt's registered exterior
   depletion ratios likewise select sweeping Jupiter–Saturn channels over present-
   architecture erosion alone.
2. **Conditional probabilities stay conditional.** The reported 6.0–6.6% Mimas–Tethys
   and 100% Titan–Hyperion values belong to Luan's single-resonance, slow-convergence
   assumptions. Past three-body captures lasting at least 10 Myr invalidate a unique
   two-body-only Saturn history.
3. **Ambiguity and failure are data.** Primordial disc convergence and later tidal
   expansion remain distinct viable routes to the present Galilean endpoint. Pluto's
   four-moon resonant-transport route fails when the actual figure and finite moon
   shares are retained.

This closes the former “run an ensemble” open at the published-record grade. It does
not manufacture a posterior where the papers use incompatible initial ensembles. The
non-identifiability proof survives because at least two distinct reservoirs reach the
same Galilean endpoint.

## 7. Claim ledger

| Claim | Grade |
|---|---|
| Bilinear pair coefficient from additive two-ended shares | Derived |
| Pair-strength reconstruction from \(\mu_{ij}\) | Derived |
| Inverse-square radial law | Derived on ratified P4 + P5 |
| General point-centre n-body Hamiltonian | Derived on ratified radial theorem |
| Exact stepwise conservation of total \(P\) and \(L\) | Derived |
| Absolute numerical system scale from closure integers alone | Proven non-identifiable by scale symmetry; one measured rod–clock calibration required |
| Isolated-channel leading width | Derived normal form; convergence/remainder required for each released isolated case |
| Three-body leading coefficient | Derived algorithm; Galilean leading-order value run |
| One scalar width inside overlap | Not well-defined |
| Galilean present lock | JPL JUP365 bounded-libration test passed; connected 3-of-4 first-order topology established |
| Other displayed present locks | Direct Horizons bounded-angle gates pass for Mimas–Tethys, Enceladus–Dione, Titan–Hyperion, Naiad–Thalassa, and the 18-kyr Neptune–Pluto interval; Janus–Epimetheus retained as horseshoe control |
| Stable versus destructive outcome from the integer ratio alone | Not derivable; coefficient, topology, and escape boundary are now separately computed |
| Main-belt centres and leading widths | Registered 4/4 centre and 4/4 factor-three width gates pass; proper-orbit 7:3 control differs by factor 1.07 |
| Conditional capture criterion | Derived; eight-family published history ensemble registered and audited |
| Unique historical reason for today's locks from current census | Proven underdetermined |

## 8. Primary-source checks for imported mathematics

- Bertrand branch theorem: M. A. Reynolds & M. T. Shouppe, *Closed,
  spirograph-like orbits in power law central potentials*, arXiv:1008.0559.
- Three-body coefficient by second-order canonical transformation: A. C. Quillen,
  *Three-body resonance overlap in closely spaced multiple-planet systems*, MNRAS
  418 (2011) 1043–1054.
- Capture normal forms and migration-rate dependence: A. J. Mustill & M. C. Wyatt,
  *A general model of resonance capture in planetary systems*, MNRAS 413 (2011)
  554–572; K. Batygin, *Capture of planets into mean-motion resonances*, MNRAS 451
  (2015) 2589–2609.
- Representative historical constraints used by *The Solar System*: V. Lainey et al.,
  *Nature* 459 (2009) 957–959 (Io/Jupiter dissipation); S. J. Peale & M. H. Lee,
  *Science* 298 (2002) 593–597 (primordial Galilean-disc route); V. Lainey et al.,
  *Nature Astronomy* 4 (2020) 1053–1058 (Titan migration); R. Malhotra, *Nature* 365
  (1993) 819–821 and D. Nesvorný & D. Vokrouhlický, *ApJ* 825 (2016) 94
  (Neptune–Pluto and grainy migration); W. H. Cheng, S. J. Peale & M. H. Lee,
  *Icarus* 241 (2014) 180–189 (failed full Pluto-moon resonant transport).
- Asteroid-belt controls: J. Wisdom, *Icarus* 56 (1983) 51–74 (chaotic 3:1
  Kirkwood gap); T. Kiang, *Nature* 273 (1978) 734–736 (stable 3:2 Hildas versus
  unstable 2:1 gap); D. A. Minton & R. Malhotra, *Nature* 457 (2009) 1109–1111
  (migration scars and \(\nu_6\) sweeping); R. Deienno et al., *ApJ* 864 (2018) 50
  (instability-driven excitation and model-conditioned depletion).
- Direct angle and population instruments: NASA/JPL Horizons API and DE441/JUP365/
  SAT441L/NEP098 integrated solutions; NASA/JPL SBDB Query API; D. Nesvorný et al.,
  *Catalog of Proper Orbits for 1.25 Million Main Belt Asteroids*, arXiv:2407.18221.
- Extended migration constraint: D. Nesvorný et al., *The Dynamical History of the
  Kuiper Belt*, arXiv:2602.16999 (67 registered outer-system histories).

The source theorems are imported mathematics. The coefficient factorization, the
zero-remainder selection, the ledger-share reconstruction, and their POAMS reading are
the work of this derivation.
