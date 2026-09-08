# ARCHIVE — Running-Law Separability Test

> **Current disposition (ratified 2026-09-07): superseded research design, not a current prediction.** The running law it was designed to separate was never quantitatively established and is now carried as an open question. Preserve this document as a record of the proposed falsification programme, not as a live theorem. Current status: [The Alpha Problem — An Open Front](https://cfmilam.github.io/nr-poams-exhibits/alpha-fine-structure-derivation.html).

Companion to `poams-engineering-public/proofs/ALPHA-RUNNING-LAW.md` (the conditional theorem:
bare-vortex fine-structure running is **multiplicative**, natural realization
α⁻¹(ℓ) ∝ √( ln(ℓ_ref/ℓ) ); log form excluded by the two pillars; coefficient **open**).

**Mandate.** Find and rank regimes/observables where the bare-vortex √-of-log law *separates
observably* from conventional (log) QED running. Firewall: the coefficient **k stays symbolic**;
nothing is fitted to a running curve. A null design that names the precision required to see or
kill the effect is a SUCCESS.

---

## Symbols & normalization (fixed once, used throughout)

- Depth variable: t ≡ ln(ℓ_ref/ℓ) = ln(Q/Q_ref). Finer probe ⇒ larger t ⇒ deeper in the winding.
- Bare-vortex (BV) law:  α⁻¹_BV(t) = C − k·√t ,  slope  d(α⁻¹)/dt = −k/(2√t)  (falls with depth).
- Conventional single-species QED (well above one threshold, charge q, colour N_c):
  α⁻¹_QED(t) = C − s·t ,  s = (2/3π)·N_c·q²  (CONSTANT slope). For one lepton s = 2/3π = 0.2122.
- Forced-magnitude anchor (used only to set the NATURAL SCALE of k, never as a fit):
  the theorem forces Δα⁻¹ ≈ 1 unit across the bare vortex's W ≈ 5.6-e-fold window [r_s, r_orb].
  ⇒ k·√5.6 ≈ 1 ⇒ **k ~ 0.42 (order-unity)**. Reported deviations scale linearly in k.
- Physical window of a bare electron vortex: r_s = ħ/2m_e c (half reduced Compton), 
  r_orb = ħ/m_e βc = (reduced Compton)/β, β = √(2/N) ≈ 0.09 ⇒ span ln(r_orb/r_s) = ln(2/β) ≈ 5.6 e-folds.
  **Key geometric fact:** the window lives from ~½ Compton down to ~5.6 e-folds finer — i.e. AT and
  BELOW the Compton scale. Atomic ORBITAL scales (Bohr = Compton/α ≈ 137× Compton) are far OUTSIDE
  (coarser than) the window. So orbital observables do NOT probe the window; only contact/self-energy/
  hyperfine/g-2 class observables (which sample the Compton region) do. This governs which tests qualify.

---

## Ledger (verdicts; detail in appendices)

| # | Candidate class | Observable | e-folds Δt | Signal (units α⁻¹) | Needed precision | Verdict |
|---|---|---|---|---|---|---|
| a | Between-threshold curvature | running-α, m_e→m_μ (e+e−, spectroscopy) | ~5.3 | ~0.1–0.2·(k/0.42) curvature on ~1 unit drop | δα⁻¹ ≲ 0.01 across MeV Q | MARGINAL |
| b1| Below-floor, two depths | α from e g−2 vs μ g−2 (Compton-scale probes) | 5.33 | ~1·(k/0.42) IF both sit in window | δα⁻¹/α⁻¹ ~1e−9 (already have) | DECISIVE* |
| b2| Below-floor, one system | μH vs eH Lamb/hyperfine α-consistency | ~2–5 | ~0.5·(k/0.42) IF inside window | δα⁻¹ ~1e−4…1e−6 | DECISIVE* |
| c | Pure curvature over e-folds | d(α⁻¹)/dt slope-fall, wide range | ≥6 needed | shape only; tower-contaminated | δ(slope) ~1e−2 & tower model | DEAD (standalone) |
| d | Single-species (tower-suppressed) | positronium / muonium spectroscopy | ~2–3 | ~0.3·(k/0.42) if window reached | δα⁻¹ ~1e−5 | MARGINAL |

*DECISIVE conditional on establishing the probe sits INSIDE [r_s, r_orb]; see appendices for the
crux (the "does-it-probe-the-window" gate) — this is where the design earns or loses its teeth.

---

## Appendix A — Between-threshold precision (m_e → m_μ)  [MARGINAL]

**Setup.** Between two well-separated charged-species thresholds only ONE species loop is active, so
conventional QED running is *exactly* log with an *exactly known* slope s = 2/3π = 0.2122 per e-fold
(single lepton). Between m_e = 0.511 MeV and m_μ = 105.66 MeV the available span is
Δt = ln(m_μ/m_e) = ln(206.8) = 5.33 e-folds. Conventional drop over the window (fully-on limit):
Δα⁻¹_QED ≈ 0.2122 × 5.33 ≈ **1.13 units** (the real Uehling turn-on is softened near each end,
but the interior slope is the clean, known constant).

**BV signature = curvature, not offset.** A superposed bare-vortex term subtracts k√t on top of the
known −s·t. The offset is unobservable (absorbed into C / the low-energy anchor); the *shape* is not.
Deviation of α⁻¹_BV+QED from the best-fit straight line across [t1,t2] is a coefficient-scaled,
shape-fixed concavity. For the m_e→m_μ window measured from the electron onset (t1≈0.3, t2≈5.6),
the max departure of k√t from its chord is Δ_curv ≈ k·[√t_mid − chord] ≈ 0.13·(k/0.42) units on a
~1-unit total drop — i.e. a **~12% curvature of the running**, or Δα⁻¹ ≈ 0.13 absolute.

**Sharpest sub-feature — the onset cusp.** d(α⁻¹)/dt = −k/(2√t) DIVERGES as t→0. Just above the
electron threshold the BV law predicts an anomalously STEEP initial fall relative to QED's finite
Uehling onset. Concentrating measurement points in the first e-fold above m_e maximizes contrast.

**Precision reality.** To resolve a 0.13-unit concavity one needs α⁻¹(Q) mapped at ≥3 points across
Q ~ 1–100 MeV with δα⁻¹ ≲ 0.01 each. Direct spacelike/timelike running-α at these low Q is coarse:
e+e− running-α extractions (KLOE, BaBar, OPAL) operate at Q ≳ 0.2–90 GeV; the sub-GeV region is
dominated by hadronic uncertainty and has no clean per-point δα⁻¹ ~ 0.01 at MeV scale today.
Lamb-shift-class spectroscopy fixes α at essentially Q→0 (one point, not a curve). g-2 supplies α at
the Compton scale (one point). **No current programme maps the MeV running curve at 0.01 resolution.**

**Systematics.** Hadronic vacuum polarization onset (2m_π ≈ 280 MeV) sits just above the window —
its low-energy tail plus π⁰/η contributions contaminate the upper e-fold; muon-loop turn-on at t2.
**Verdict: MARGINAL.** Signal shape is clean and coefficient-robust (concavity is there for any k>0),
but the required MeV-scale running-α cartography at δα⁻¹~0.01 does not exist and is not foreseeable
near-term. Good as a design target for a dedicated low-Q running-α programme; not decisive today.

---

## Appendix B — Below-the-floor regime (Q < m_e)  [DECISIVE, gated]

**Why this is the prize.** Below the lightest charged species there are no lighter loops, so
conventional vacuum-polarization running **STOPS**: s_QED = 0. The background slope is exactly zero.
Therefore, in this regime, **any residual scale dependence of α is the bare-vortex term alone** — the
√-log has no log competitor to hide behind. Separation is not a curvature-vs-line contest (App. A);
it is signal-vs-flat-null. This is the cleanest possible discriminator.

**Does POAMS predict running below the QED floor?** Yes, conditionally: the theorem's scale
dependence is intrinsic to the single bare vortex's own window [r_s, r_orb] and does not require
lighter species — it is holonomy accrued per traversal, independent of the loop tower. So inside that
window POAMS predicts α runs while QED says it is frozen. The whole test therefore reduces to ONE
physical question (the GATE):

  **GATE — does the observable probe two DISTINCT effective resolutions ℓ inside [r_s, r_orb]?**

  Recall the window is ~½Compton down to 5.6 e-folds finer. Orbital/Bohr-scale observables are
  OUTSIDE (coarser) and see the frozen, integrated α — no signal. Only Compton-region probes
  (self-energy / g-2 / contact-density / inner-shell) sample inside.

**b1 — electron g−2 vs muon g−2 as α-determinations.** Each g−2 samples the lepton's own Compton
scale; the muon's is 207× finer ⇒ 5.33 e-folds deeper. If BOTH sit inside a (shared, species-blind)
bare-vortex window, POAMS predicts the α extracted from μ g−2 differs from e g−2 by
  Δα⁻¹ = k[√(t_μ) − √(t_e)] ≈ k·√5.33 ≈ 0.97·(k/0.42) units  (if t_e≈0),
a **~0.7% shift** — colossal. QED predicts ZERO (α is universal). The EXPERIMENTAL FACT: α from
electron g−2 (0.13 ppb) and independent determinations agree with muon-sector inputs at the
~1e−9 level; α is universal to ppb across systems. **This null already bounds k√(Δt) ≲ 1e−7**, i.e.
**k ≲ 1e−7 / √5.33 ≈ 4e−8 IF the two g−2's probe distinct depths inside the window.** That is 7
orders below the natural k~0.42 — an apparent gross exclusion. The escape (and the honest reading):
the g−2 Compton-scale probes may both lie at the SAME edge of the window (both "just inside"),
giving Δt_effective ≪ 5.33, or the window's species-blindness may fail (each lepton carries its own
window that co-moves with its Compton scale, so μ and e each sit at the same *relative* depth t and
see the SAME α — Δ=0 structurally). **This structural co-motion is the physically natural POAMS
reading and it PREDICTS the observed universality** — turning the apparent catastrophe into a
consistency. Decisive power then requires a probe of TWO depths WITHIN ONE species' window.

**Verdict b1: DECISIVE as a null already passed** — universality of α to ppb is exactly what
co-moving windows predict and what a species-blind absolute window would have grossly violated. It
kills the "single shared absolute window" realization at k≳4e−8. It does NOT yet probe intra-window
running (that needs b2).

**b2 — two depths inside ONE species' window (the real decisive test).** Probe α at two distinct ℓ
*within the same electron's* [r_s, r_orb] window and look for a nonzero Δα⁻¹ where QED demands zero.
Candidate paired observables on hydrogenic electron systems, ordered by depth (finest = deepest t):
  • hyperfine / contact density (samples the electron AT the nucleus — finest, deepest in window);
  • electron self-energy / Lamb shift Uehling piece (Compton-region — mid window);
  • fine-structure / spin-orbit (coarser — window edge or just outside).
Extract α_eff from each channel of the SAME atom via QED-corrected theory; conventional QED forces
one universal α to all channels. A statistically significant channel-to-channel Δα⁻¹ beyond QED
error = bare-vortex running. Predicted size for a within-window depth split Δt ~ 1–2 e-folds at
mid-window t~3: Δα⁻¹ = k[√(t+Δt) − √t] ≈ k·Δt/(2√t) ≈ 0.42·1.5/(2·1.7) ≈ **0.18·(k/0.42) units**,
i.e. Δα⁻¹/α⁻¹ ~ 1.3e−3. Hydrogen α-consistency across channels currently holds at the ~1e−6…1e−8
level (bounded by proton-structure/QED uncertainties, not by α). A 1e−3 channel split would have
been seen ⇒ this ALSO bounds the intra-window k, unless the accessible channels all cluster at the
same effective depth (the likely loophole — hydrogen channels may not span ≥1 e-fold inside [r_s,r_orb]).

**b2′ — muonic vs electronic hydrogen (the depth lever).** The muon orbit sits 207× deeper; muonic
hydrogen samples the proton/self-energy region at ℓ smaller by 5.33 e-folds than electronic H. If the
bare-vortex law is species-blind at the STRUCK charge (the orbiting lepton), μH probes 5.33 e-folds
deeper into the SAME window and POAMS predicts α_eff(μH) − α_eff(eH) = k[√(t+5.33) − √t] ~ 0.5–1 unit
— grossly visible. μH Lamb shift is measured to ~ppm and is CONSISTENT with eH under a common α once
the proton radius is fixed (the "proton radius puzzle" resolved 2019–2021 at this level). That
consistency again favors co-moving windows (Δ=0) over an absolute window. **The decisive residual:**
is there a channel pair — e.g. μH 2S hyperfine (deep, contact) vs μH Lamb shift (Uehling, dominated
by e⁺e⁻ vac-pol at ~electron Compton) — that samples two DIFFERENT depths for the SAME muon? The μH
Lamb shift is ~99% electron-loop Uehling: it literally probes the electron Compton scale, while μH
hyperfine probes the muon-contact scale. Those two DIFFER by ~5 e-folds within one bound system.
**This is the lever.** Required precision to see k~0.42 over Δt~5 at t~1: Δα⁻¹ ~ k(√6−√1) ≈ 0.6 unit
— already excluded ⇒ k≲1e−6; to probe the *natural* co-moving residual (a log-of-log softening term,
~k'·ln t) needs δα⁻¹ ~ 1e−6 in cross-channel α, at the edge of next-gen μH/μD spectroscopy (CREMA,
muonic-atom programs). **Verdict b2/b2′: DECISIVE** — zero QED background makes any cross-channel
α split a pure bare-vortex readout; current data already sets k ≲ 1e−6 on absolute-window
realizations, and next-gen muonic spectroscopy at δα⁻¹~1e−7 tests the co-moving softening residue.

---

## Appendix C — Derivative / curvature signature over many e-folds  [DEAD standalone]

**Signature.** d(α⁻¹)/dt = −k/(2√t) FALLS as ~t^(−1/2) with depth, whereas summed-tower log running
gives a piecewise-CONSTANT slope (stepping up at each threshold). Measuring the slope at two widely
separated depths and showing it *decreases within a single-species plateau* would isolate √-log.

**e-folds needed.** To see slope fall by a detectable factor √(t2/t1)=2 needs t2/t1=4, i.e. ≥1.4
e-folds of *pure single-species* running plus an accurate baseline — realistically ≥6 e-folds of
clean plateau to bracket it. The only clean single-species plateau is m_e→m_μ (App. A), 5.3 e-folds.
**Fatal problem:** across the FULL measured 137→128 curve the species TOWER dominates (log-like, ~8
units / ~12 e-folds); the bare-vortex slope-fall is buried under threshold steps and hadronic VP.
Distinguishing the intrinsic 1/√t slope-fall from the tower requires a validated tower model to
subtract — reintroducing model dependence the firewall forbids. **Verdict: DEAD** as a standalone
discriminator; it is merely the differential restatement of App. A and inherits App. A's precision
wall without adding a null background. Keep only as a cross-check on a b-class detection.

---

## Appendix D — Single-species (tower-suppressed) systems  [MARGINAL]

**Idea.** In systems where the multi-species tower is physically absent, the measured running should
approach the bare-vortex form. Pure-leptonic bound states — positronium (e⁺e⁻) and muonium (μ⁺e⁻) —
have no hadronic VP and a single active leptonic loop, so their internal running is the cleanest
single-species case. Positronium 1S–2S and hyperfine, and muonium 1S–2S / hyperfine, are measured to
~ppb–ppt fractional.

**Signal.** These systems still probe scales set by their (large) Bohr radii — OUTSIDE the bare-vortex
window (GATE fails for the gross orbital observables). The window is reached only by their contact/
hyperfine/annihilation channels (which sample the Compton region). Positronium hyperfine and the
annihilation rate probe the e⁺e⁻ contact ~Compton scale — inside the window edge. A within-system
split between the coarse 1S–2S interval (outside) and hyperfine/annihilation (inside) yields
Δα⁻¹ ~ k[√t_in − √t_out]; with t_out≈0 (window edge) and t_in~1, Δα⁻¹ ~ k·1 ≈ 0.4·(k/0.42) — but
t_out at the edge means √t_out→0 and the "outside" channel carries the frozen integrated α, so the
contrast is set by how deep the contact channel reaches: realistically Δα⁻¹ ~ 0.1–0.3·(k/0.42).
**Precision.** Positronium theory/experiment agreement on hyperfine is at ~1e−5 (a long-standing
few-σ discrepancy exists ~1e−4!). Muonium hyperfine (MuSEUM) targets ~1e−7. Extracting a
cross-channel α split at δα⁻¹ ~1e−5 is feasible but the theory error (higher-order QED, recoil)
is the wall, not statistics. **Verdict: MARGINAL** — clean of hadronic/tower systematics and thus a
valuable *corroborating* system, but the accessible depth split is small and QED-theory-limited;
the persistent positronium-hyperfine discrepancy is worth a dedicated bare-vortex re-analysis (flag).

---

## Appendix E — Ranked shortlist & the single decisive test

**Ranking (best separation first).**
1. **b2′ — muonic-hydrogen cross-channel α-consistency** (Lamb/Uehling depth vs hyperfine/contact
   depth within one μH atom, ~5 e-fold internal lever). DECISIVE: zero QED running background ⇒ any
   cross-channel Δα⁻¹ is a pure bare-vortex readout.
2. **b1 — e g−2 vs μ g−2 universality** (already-passed null): kills the absolute-shared-window
   realization at k ≲ 4e−8; confirms co-moving windows. DECISIVE but retrospective.
3. **b2 — electronic-hydrogen cross-channel α split** (hyperfine vs Lamb vs fine-structure).
4. **a — dedicated MeV-scale running-α curvature** (m_e→m_μ onset cusp). MARGINAL; needs new programme.
5. **d — positronium/muonium contact-channel** corroborator (flag: Ps HFS discrepancy).
6. **c — many-e-fold slope-fall.** DEAD standalone (tower-contaminated; firewall-violating to subtract).

**THE single decisive test (named precisely):**

> **Cross-channel fine-structure-constant consistency in muonic hydrogen.** Extract α_eff
> independently from (i) the μH 2S–2P Lamb shift — whose value is ~99% set by electron-loop Uehling
> vacuum polarization sampled at the electron Compton scale (deep) — and (ii) a μH observable sampling
> the muon-contact/hyperfine scale (~5 e-folds shallower or deeper depending on channel), holding the
> proton radius fixed from the resolved (2019+) puzzle. Conventional QED demands **identical α** in
> both channels (running is frozen below m_e: s_QED = 0). The bare-vortex law predicts a nonzero
> Δα⁻¹ = k[√t_deep − √t_shallow]. **Required precision:** absolute-window realizations are already
> excluded at k ≲ 1e−6 by present μH/eH agreement; testing the *natural co-moving softening residue*
> (a ~k'·ln t term surviving window co-motion) demands cross-channel δα⁻¹ ~ 1e−7, the target of
> next-generation CREMA-class muonic-atom spectroscopy. A confirmed null at 1e−7 with a stated k-bound
> is a full success under the firewall; a nonzero split is a clean detection with NO log competitor.

**Firewall compliance.** k held symbolic throughout; every signal quoted as ·(k/0.42) with the 0.42
used only to state a natural scale, never fitted. All quantitative verdicts are precision-requirement
statements (null designs), satisfying the mandate.

---

## Appendix F — The GATE physics: absolute vs co-moving windows (the decision fork)

Every b-class verdict pivots on one unresolved structural choice about the bare-vortex window. State
it explicitly, because it converts "gross exclusion" into "sharp prediction" and defines what the
decisive test actually measures.

**(F1) Absolute window.** There is ONE window [r_s, r_orb] fixed in laboratory length units,
shared by all species. Then a heavier lepton (finer Compton) sits deeper in it and reads a different
α than a lighter one: Δα⁻¹(μ vs e) = k[√t_μ − √t_e] ~ 0.97·(k/0.42). PREDICTION: α is NOT universal.
EXPERIMENT: α is universal to ~1e−9 (e g−2, μ inputs, Rydberg, recoil). ⇒ absolute window is
**EXCLUDED** for k ≳ 4e−8 — seven orders below natural scale. If POAMS insisted on the absolute
window, the running law would be dead. It does not.

**(F2) Co-moving window (physically natural in POAMS).** Each vortex carries its OWN window scaled to
its Compton length: r_s ∝ ħ/mc. A μ and an e each sit at the SAME *relative* depth t within their own
windows ⇒ read the SAME α at corresponding channels ⇒ universality is PREDICTED, not fitted. This is
the reading the pillars favor (the window is intrinsic to the strand's own coil, not to lab length).
**Consequence for tests:** cross-SPECIES comparisons (b1) become null by construction — they test F1
vs F2, and the data has already chosen F2. To see running you must compare TWO DEPTHS WITHIN ONE
vortex's own window — exactly what the μH cross-channel test (b2′) does. This is why b2′, not b1, is
the decisive live test: it is the only design that survives the F2 selection with nonzero predicted
signal.

**(F3) What co-motion leaves observable.** Under F2 the leading √t offset co-moves away, but the
*curvature within a single window* does not: two channels of one atom sampling depths t and t+Δt
still differ by k[√(t+Δt)−√t]. If even this cancels (fully rigid co-motion of all channels), the
surviving signal is the theorem's declared **log-of-log softening** — a residual ~k'·ln t term that
cannot be gauged away because it is the second-order shape, not the offset. That residue is the
ultimate target: δα⁻¹ ~ 1e−7 cross-channel. Naming this precision IS the deliverable.

**Threshold ladder (for App. A / C bookkeeping), single-lepton slope s=2/3π per e-fold:**
  m_e 0.511 MeV · m_μ 105.7 MeV (Δt 5.33) · 2m_π≈280 MeV (hadronic on) · m_τ 1777 MeV.
  Only [m_e, 2m_π] is a clean single-species QED plateau; usable clean span ≈ ln(280/0.511·)≈ up to
  m_μ then muon+ onset — effective clean window ~5 e-folds, matching App. A.

**Systematics common to all b-tests.** (1) Proton/nuclear structure — neutralized by fixing r_p from
the resolved puzzle and by using structure-insensitive channel ratios. (2) Higher-order QED theory
error — the true wall below ~1e−6; drives the need for improved μH/muonium theory. (3) Nuclear
polarizability in μH (few percent of Lamb shift) — mitigated by muonic-deuterium/helium cross-checks.
(4) Definition of "effective depth t" per channel — requires a POAMS map from observable→ℓ; this is
model input but NOT a coefficient fit (it sets Δt, not k), so it stays firewall-clean if pre-registered.
