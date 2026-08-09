# The Madelung Closure Theorem
## Closure + Self-Duality + Coulomb Eye ⟹ 720° ⟹ the (n+l) Families

**Status: conditional theorem** — proved from stated hypotheses (H1–H5 below), with the
Abel-inversion step computed end-to-end and every imported tool attributed. Companion to
the published exhibit `aufbau-as-closure.html` (empirical leg) and the audit trail in
`memory/poams-audit/` (charter, recon dossiers, instruments, run logs). 2026-08-09.

---

## 1 · Statement

**Theorem.** Let $V(r)$ be a central attractive potential and $G(r) \equiv -2r^2V(r)$.
Assume:

- **(H1)** regularity: $V$ continuous on $(0,\infty)$; $G > 0$ on some interval.
- **(H2)** *single ledger annulus:* $G$ is single-peaked — strictly increasing then
  strictly decreasing — with $G \to 0$ as $r \to 0$ and $r \to \infty$.
- **(H3)** *self-duality:* $G(r) = G(R^2/r)$ for some $R > 0$.
- **(H4)** *frontier closure:* every bounded zero-energy orbit has the same apsidal
  (pericenter→apocenter) angle $\Phi$, for all admissible angular momenta
  $J \in (0, \sqrt{f_0})$, $f_0 = \max G$.
- **(H5)** *Coulomb eye:* $V(r) \sim -Z/r$ as $r \to 0$.

Then $\Phi = 2\pi$ — the zero-energy orbits close after exactly two turns, 720° — and

$$V(r) = U_{1/2}(r) = -\frac{2v}{rR\,(r+R)^2}$$

exactly (the Demkov–Ostrovsky potential), whose zero-energy bound thresholds group by
$N = n + l$. The semiclassical degeneracy families are $n_r + 2l$: **the Madelung
families.** If (H4) holds only approximately — the physical case — the frontier slope
satisfies $k = \Phi/\pi < 2$ strictly, which is precisely the Madelung tie-break clause
("lower $n$ first").

## 2 · Proof

**Step 1 (mechanics → cylinder).** At $E=0$, energy conservation gives
$d\varphi/d\theta = J/\sqrt{f(\theta) - J^2}$ exactly, where $\theta = \ln(r/R)$,
$f(\theta) = G(Re^\theta)$, $J = L$. No metric normalization enters; this is one line of
algebra from $\tfrac12(\dot r^2 + r^2\dot\varphi^2) + V = 0$.

**Step 2 (self-duality = evenness).** (H3) says $f(-\theta) = f(\theta)$: the ledger reads
the same from the inside face and the outside face. By (H2), $f$ is even, single-peaked at
$\theta = 0$ (the peak sits at $r = R$ automatically), $f \to 0$ at both ends.

**Step 3 (closure → Abel equation).** With $\Theta(u)$ the positive half-width of
$\{f \ge u\}$ and $W = -\Theta' \ge 0$:
$$\Delta\varphi(J) = 2J\int_{J^2}^{f_0} \frac{W(u)\,du}{\sqrt{u - J^2}} \equiv \Phi
\quad \text{for all } J \in (0,\sqrt{f_0}).$$

**Step 4 (inversion — uniqueness computed).** The finite-interval Abel operator is
injective on locally integrable $W$ (explicit inversion formula; standard). Inverting the
constant function:
$$W(u) = \frac{\Phi}{\pi}\cdot\frac{\sqrt{f_0}}{2u\sqrt{f_0 - u}}
\;\Longrightarrow\;
\Theta(u) = \frac{\Phi}{\pi}\,\mathrm{arccosh}\sqrt{f_0/u}
\;\Longrightarrow\;
\boxed{f(\theta) = f_0\,\mathrm{sech}^2(\pi\theta/\Phi)}$$
— the unique even single-peaked solution. (Cross-check: $U_\mu$ gives
$f \propto \mathrm{sech}^2(\mu\theta)$ and $\Delta\varphi = \pi/\mu$ analytically, via
$s = \tanh\mu\theta$; the formulas match with $\mu = \pi/\Phi$.)

**Step 5 (the eye forces 720°).** (H5) gives $f = -2r^2V \sim 2ZRe^{\theta}$ as
$\theta \to -\infty$, while $\mathrm{sech}^2(\pi\theta/\Phi) \sim 4e^{2\pi\theta/\Phi}$.
Matching exponents: $2\pi/\Phi = 1$, i.e. $\Phi = 2\pi$, $\mu = \tfrac12$, $k = 2$.
Evenness then fixes the conjugate tail $V \sim -2f_0R/r^3$ — the inversion image of the
Coulomb eye (and indeed $U_{1/2} \sim -2v/r^3$). ∎

**Lemma (zero-energy criticality; used in the deformation theory of the physical case).**
On every bounded $E=0$ orbit in *any* central ledger,
$$\frac{1}{\Phi}\oint t\,d\varphi \equiv 1, \qquad t = -\frac{d\ln\chi}{d\ln r},$$
by the explicit antiderivative $\int dG/(G\sqrt{G-J^2}) = (2/J)\arctan(\sqrt{G-J^2}/J)$,
whose two legs (peri→peak, peak→apo) cancel. Zero-energy orbits self-average any
screening profile to the marginal exponent; $k$ is a functional of the *fluctuation
profile* of $t$ about 1 (magnitude alone insufficient — the $U_{1/2}$ family holds
$k = 2$ across a wide fluctuation range while the TF family orders monotonically in it).

## 3 · Attribution (what is cited, what is new)

**Cited — the machinery is classical:**
- Abel/width inversion — the period-type functional determines only the *width* of a
  well; an infinity of asymmetric wells share it; **symmetry makes the well unique**:
  Landau & Lifshitz, *Mechanics* §12 (the classical statement); Firsov 1953; Luneburg
  1944; modern Abel form: Saa & Venegeroles (arXiv:2110.01953).
- The focusing family and its $k=2$ zero-energy closure — Demkov & Ostrovsky, *Sov. Phys.
  JETP* 35:66 (1972); the family's construction and — decisively — its documented
  **non-uniqueness** ("a whole family of potentials with given focusing properties"):
  Demkov, Ostrovskii & Berezina, *Sov. Phys. JETP* 33:867 (1971); fish-eye group theory:
  Demkov & Ostrovskii, *Sov. Phys. JETP* 33:1083 (1971). Quantum zero-energy states track
  the closed orbits: Makowski, *PRA* 86:042117 (2012).
- The differential-geometric mirror — rotationally symmetric metrics with all geodesics
  closed are parameterized by an **odd** deformation function, the round metric at
  $h \equiv 0$ (Zoll 1903; Besse, *Manifolds all of whose Geodesics are Closed*, ch. 4
  §4.B; Guillemin 1976). Evenness kills the deformation: our Step 2+4 is the mechanical
  shadow of that statement. Constant apsidal angle ⇔ closure families in the relativistic
  setting: Perlick, *Class. Quantum Grav.* 9:1009 (1992) — whose Type-I conformal factor
  in the log coordinate is literally a sech² profile (via Ballesteros et al.,
  arXiv:0803.3430; Perlick read via secondary sources — flagged).

**New here (as far as the searchable record shows; recon dossiers on file):**
1. **The selection principle.** Closure alone leaves the shear freedom (documented by
   D–O–Berezina themselves; general uniqueness declared open in both 1971 papers).
   *Inversion self-duality — the eye's hole and wall as inside and outside faces of one
   ledger — is exactly the condition that kills the shear* and selects the
   $\mathrm{sech}^2$ member. That physical premise doing that mathematical work appears
   nowhere in the prior corpus.
2. **The eye forcing the count.** $\Phi = 2\pi$ — the 720° — derived by exponent-matching
   the Coulomb eye against the self-dual profile, rather than assumed or fitted.
3. **The criticality lemma** ($\langle t\rangle_\angle \equiv 1$ at $E=0$) — not located in
   the literature; distinct from the (time-averaged, homogeneity-based) virial theorem.
4. **The empirical leg** (companion exhibit): the zero-energy apsidal slope $k(Z,l)$ of
   the actual Thomas–Fermi ledger computed with zero adjustable parameters — $k \in
   (1.60, 1.94)$, strictly under 2, inside the razor window $(5/3, 2)$ that is *equivalent*
   to the full Madelung rule; the emergent aufbau with declared ties at the real anomaly
   boundaries; and, at TFD fidelity, the d-collapse appearing at exactly $Z = 21$ when the
   statistical exchange (pairing) hole is added (Slater coefficient; radius collapse in
   both classic conventions; convention-sensitivity named).

## 4 · The physical reading (the POAMS layer)

- **(H4) is the ontology, not a convenience.** A quantum is a completed turn; the census
  grows at the zero-binding frontier; what does not close there does not persist. Standard
  mechanics has no reason to impose closure on zero-energy orbits — the license is
  Normal-Realist. This is the hypothesis that turns geometry into a filling rule.
- **(H3) is GROUNDING §3.** The vortex's hole and wall are one ledger's two faces; at the
  census edge the books must balance read from either side. Its mathematical shadow is
  evenness on the cylinder — and evenness is precisely what uniqueness needs.
- **(H2)'s failure mode is the anomaly layer.** Single-peaked $G$ = one classically
  allowed annulus per winding = the smooth census. Where the discrete census breaks it —
  the double well — is exactly where the d-collapse and the ~20 anomalous configurations
  live, and the computed near-ties + exchange-hole instrument take over there. The
  theorem's hypothesis boundary and the exception catalogue coincide; the rule and its
  exceptions get one geometry.
- **(H5) is the established POAMS interior** (the bare fundamental's $1/r$ ledger), and
  the real ledger's $r^{-4}$ far field (vs the self-dual $r^{-3}$ image) is part of the
  physical *discount* that keeps $k < 2$ strict — the tie-break as over-screened outer
  face.

## 5 · Open (named, not hidden)

1. **The fixed point.** Why does the self-consistent census hold its frontier *near* the
   self-dual point (the computed $k \in (1.60, 1.94)$)? The criticality lemma pins the
   mean; the D–O counterexample shows the fluctuation *profile*, not magnitude, is what
   matters; the conjecture is that closure stacking drives the profile toward the sech²
   family with a finite discount. Not yet proved.
2. **Native pairing ledger.** The statistical $\rho^{1/3}$ hole stands in for same-sense
   quanta being unable to double-file. Building the sense-bookkeeping term natively (and
   deriving the anomaly catalogue from it) is the discrete tier.
3. **POAMS-native census.** Thomas–Fermi is the standard self-consistent stand-in for the
   census's net ledger; deriving the screening shape from closure stacking directly
   remains open.
4. **Rigor residue.** Abel injectivity hypotheses stated as (H1–H2) (endpoint behavior,
   single-valued width); Besse ch. 4 exact theorem numbering verified only to section
   level; Perlick via secondary sources; pre-1990 Russian-language literature not
   exhaustively searched.

## 6 · Firewall record

Razor window derived from the empirical sequence *before* any computation; no Madelung
input, no α, no fitted constant anywhere in the chain; registered prediction (d-collapse
flip at $Z \approx 21$) logged before the instrument that found it, with two failed
fidelities (point-shells, Hartree-only) honestly recorded first; prior-art recon run
*before* claiming the razor (caught D–O 1972 — cited, not claimed) and before claiming
the theorem (caught LL §12 + D–O–B non-uniqueness — cited; selection step confirmed
unclaimed). The 720°/spin-double-cover resonance (M2) remains quarantined: the pairing
*ledger* owns the collapse; the resonance owns nothing until it computes.
