---
{layout: reader, title: "YIG static-gate protocol"}
---
# YIG static-gate protocol

**Final public preregistration — 2026-11-11. Decision table LOCKED under Convention A before any sphere data.**

Reverse a saturated YIG sphere's static bias sense, with the microwave drive absent, and compare its support readings. A qualified contrast would calibrate the coefficient needed to size a later drive-toggle experiment; a qualified null would bound that coefficient before microwave hardware is considered. The [partition-magnitude derivation](partition-magnitude-derivation.html) supplies the conditional connection.

**Objective:** bound or measure $$K_s$$, the single unfixed aligned-state price in the proposed variable-G support term. Operationally, this means a bound or a **conditional effective-support coefficient in $$K_s$$-equivalent joules**, not an independently measured microscopic spin energy. A contrast earns **static directed-order candidate only**, subject to the program's separate same-transition state/reaction/work requirements.

> **Binding interpretive rule — verbatim:** the static calibration must not become an independent spin-energy receipt.

This publishes a protocol, not a result. No physical measurement, $$K_s$$ value or experimental bound exists in this package. The calculation and software checks are not observations. Publication before the experiment was authorized on 2026-11-11 at 03:29 CST; execution still requires the run-specific annex, qualification records and separate bench authorization.

## 1. Convention A and the locked numerical basis

The two-increment threshold applies to the **half-contrast**, not the full reversal:

$$
C_{\mathrm{static}} = \frac{w_{\mathrm{co}}-w_{\mathrm{anti}}}{2w}
$$

| Quantity | Locked value or definition |
|---|---|
| One balance increment | 0.01 mg |
| $$W$$ | 2707.0056698432051738086443819258383185498942991282 mg |
| Receipt-exact nominal input for $$W$$ | $$1000\times5.17\times\pi/6\ \mathrm{mg}$$ |
| $$C_{\mathrm{thr}}$$ | $$0.02\ \mathrm{mg}/W = 7.38823720349224\times10^{-6}$$ |
| $$D_{\mathrm{thr}}$$ | $$2 W C_{\mathrm{thr}} = 0.04\ \mathrm{mg}$$ |

W is the nominal specimen's mass-equivalent balance reading; “2707.0 mg” is display-only. One increment is 3.694118601746 ppm of W (display 3.69 ppm). A raw north-minus-south difference D is compared with 0.04 mg. Freeze the mapping of the physical N/S bias senses to co/anti in the run annex; the magnitude decision uses $$\lvert D\rvert$$, while the signed readings and mapping remain part of the record.

**OWNER OVERRIDE FLAG:** the owner may choose the full-difference reading instead. Any override must be recorded here as a **dated revision before any sphere datum exists**, with revised consequences and re-verification. That alternative would halve the $$K_s$$ limits; it is not the operative convention in this edition. No threshold, criterion or consequence may move after data.

The receipt-exact constants used by the reduction are:

| Quantity | Locked value |
|---|---|
| Sphere | Nominal 2.707 g YIG; operative W as above |
| Readability | 0.01 mg; not by itself a statistical detection threshold |
| Static half-contrast threshold | $$C_{\mathrm{thr}}=0.02/W=7.38823720349224\times10^{-6}$$ |
| Raw pair-difference threshold | $$D_{\mathrm{thr}}=0.04\ \mathrm{mg}$$ |
| $$K_0$$ | 24437249.848418309006512168499783362205747730377583 J |
| $$\Gamma$$ | 1.0034734147481825853397496237992791448191139223730 |
| North–south geometry, high endpoint | $$g_{\mathrm{hi}}=0.7454518768075703$$ (display 0.75) |
| North–south geometry, low endpoint | $$g_{\mathrm{lo}}=0.4797876129279153$$ (display 0.48) |
| Excluded geometry | Vertical bias; $$g_{\mathrm{geo}}=0\text{–}0.38$$ in the stated hypotheses |
| Designed orientation-null family | Horizontal east–west |
| Required pre/post gradient magnitude | $$\le 1\ \mathrm{\mu T/m}$$, relevant axial-field component with full field map |
| Gradient imitating two half-contrast increments | About 2.6 µT/m; reviewed value 2.640939132302 µT/m |
| Full reversal required for the build-threshold toggle at 10° | 1.7113992% |

The exact constants reproduce **482.7226438282 / 750.0120701809 J** at the threshold. Reporting uses **482.7226–750.0121 J**. Do not substitute rounded $$g_{\mathrm{geo}}$$, $$\Gamma$$, $$K_0$$ or W into the operative calculation.

## 2. LOCKED decision table

No threshold moves after data. The interval statistics and control tests are defined in §6. “Qualified” includes all ten controls, valid ABBA pairing, the required pre/post gradient surveys and the run-record checks; a software label alone does not supply them.

| <span style="white-space:nowrap">Outcome</span> | Preregistered criterion | Locked consequence |
|---|---|---|
| <strong style="white-space:nowrap">NULL</strong> | Point estimate and 95% upper edge of the magnitude of D are both $$<0.04\ \mathrm{mg}$$; CI half-width $$\le 0.02\ \mathrm{mg}$$; Step-0 is present and main pair count meets its required N; gradient surveys $$\le 1\ \mathrm{\mu T/m}$$; east–west and all controls clean | Conditional **$$K_s<482.7226\text{–}750.0121\ \mathrm{J}$$**, with $$g_{\mathrm{hi}}$$ giving the lower bound and $$g_{\mathrm{lo}}$$ the upper. The unsupported $$hcR_\infty$$ alignment price is excluded by **×23.2436–36.1139** under the adopted form. Same-state, same-geometry microwave-toggle ceiling at 10°: **1.1224×10⁻⁷**, using Convention A and the full-reversal normalization (**1.7113992%**, not the half-contrast value). A null is a successful measurement that fixes an upper bound. |
| <strong style="white-space:nowrap">CONTRAST</strong> | 95% lower edge of the magnitude of D is $$\ge0.04\ \mathrm{mg}$$; gradient surveys $$\le 1\ \mathrm{\mu T/m}$$; east–west and all controls clean; valid ABBA pairing and remount consistency | Report a **conditional effective-support coefficient in $$K_s$$-equivalent joules**, $$K_{\text{s-equiv}}=2K_0\cdot\operatorname{abs}(C)/(\Gamma g_{\mathrm{geo}})$$, with the 0.48–0.75 geometry range carried as systematic. **Static directed-order candidate only**: not independently measured $$K_s$$ or twist, not an independent spin-energy receipt, and not evidence establishing a larger claim. It sizes the instrument for a possible future toggle test. |
| <strong style="white-space:nowrap">AMBIGUOUS</strong> | Anything else: interval straddles threshold, unresolved or insufficient-N null, missing/dirty controls, missing or excessive gradient survey, invalid timing/pairing, remount disagreement, or another qualification failure | **RE-SURVEY** and repeat; **INCREASE N** under the preregistered rule; or **STOP** and report ambiguous. Name the reason and disposition. A gradient or Gate-0 failure blocks interpretation: it is not a POAMS null. |

The reducer's **GATE0_FAIL** label is an operational qualification failure within the ambiguous/no-interpretation disposition, not a fourth scientific outcome. The nominal readability and a near-zero display do not establish a statistical null.

## 3. Apparatus, geometry and environment

Use the static Gate 0–1 subset of the [program protocol](protocol.html): a 0.01 mg-readability analytical balance, the nominal 2.707 g sphere, nonmagnetic low-creep pan furniture, a reversible saturating DC bias assembly, vector field/gradient mapping, a roughly 2.7 g nonmagnetic dummy and the empty mount. Verify the saturated preparation and both physical bias senses using independent state readout. Record article, mount and instrument identities in the annex. There is **no microwave chain** in this experiment.

### Measurement and null axes

- **North–south horizontal bias:** measurement family. The three enumerated Earth-rotation-axis hypotheses give $$g_{\mathrm{geo}}\approx0.48\text{–}0.75$$. Carry that spread as a systematic hypothesis range; it cannot be averaged away.
- **East–west horizontal bias:** designed first-order null family under those same three hypotheses. Use the same cadence and support apparatus.
- **Vertical bias: excluded.** Its factor ranges from zero to about 0.38 and is exactly first-order null under the source's literal center-referenced latitude reading. A vertical null could therefore provide no useful coefficient bound.

These are the three declared source-model axis readings, not every possible containing circulation. A distinct Earth-orbit-normal hypothesis is outside this protocol's stated geometry.

### Equatorial-validity restriction

The underlying closed toggle form is established only at the **equatorial, weak-spin, first-order reference**. This preregistration retains the reviewed leading-order north–south geometry convention for its locked coefficient conversion, with the exact endpoints above. The general-latitude common-factor formula is not an exact law and awaits its scoped correction; the table must not be presented as a precision general-latitude prediction. State the actual site and chosen axis hypothesis in the annex before acquisition. The geometry uncertainty remains part of every reported $$K_s$$-equivalent interval.

### Relevant gradient and map

Survey the **vertical derivative of the bias-axis field component** at the sample: for north–south bias, **$$\partial B_N/\partial z$$**, not merely $$\partial B_z/\partial z$$. Its absolute magnitude must be **$$\le 1\ \mathrm{\mu T/m}$$ before and after the session**. Supply the vector field and gradient map over the sample/support region for each bias state; endpoint numbers alone are not a field map. The gradient input to the reducer is a finite, nonnegative magnitude in µT/m.

Imported dipole-force arithmetic gives 2.640939132302 µT/m as the ambient gradient imitating two 0.01 mg half-contrast increments; the sealed design line is “2.6 µT/m imitates two increments.” A 1 µT/m allocation is about 0.379 of that threshold. This is a design allocation, not an achieved uncertainty or a replacement for measured transfer controls. Calibrate gradient imitation with applied gradients of both signs under the program protocol.

## 4. Ten required controls

Gate-0 discipline remains applicable. RF-chain maps are explicitly not applicable because no RF chain is present; the other field, force/wrench, thermal, mechanical, timing, nuisance, blinding and boundary requirements remain. Keep the qualification records with the raw data. Dummy, empty, remount and east–west are CSV run types; the other controls require the accompanying survey and session records.

1. **Gradient survey.** Pre- and post-session magnitude $$\le 1\ \mathrm{\mu T/m}$$ for the component specified in §3, with the full field/gradient map and bias-state records. Purpose: bound polarity-odd magnetic-force imitation.
2. **Wrench/six-axis check.** Record mount torque states and the applicable calibrated force/wrench response. Purpose: exclude mechanical settling or exported apparatus reaction masquerading as sphere contrast.
3. **Timing protocol.** Freeze the settle time after each bias command; log timestamps and actual order. Purpose: preserve the ABBA drift symmetry and identify timing violations.
4. **Thermal control.** Log the ambient and relevant apparatus temperatures; no HVAC transitions within a block; retain the applicable thermal-transfer qualification. Purpose: bound buoyancy and expansion drift.
5. **Mechanical isolation.** No bench contact during reads; document the applicable vibration, tilt and other mechanical nuisance checks. Purpose: exclude mechanical bias in the support channel.
6. **Blinding and randomization.** Preassign the randomized block schedule and ABBA/mirrored-ABBA choices before acquisition. Hide bias-sense labels from the reader where feasible and preserve the blinded mapping through reduction. Document any unavoidable unblinding. Purpose: prevent observer and order bias without breaking balanced drift cancellation.
7. **Dummy-mass runs.** Run the full flip sequence on the nonmagnetic mass, including the pre-sphere repeatability stage. Purpose: detect bias-source or field-on-balance artifacts.
8. **Empty-mount runs.** Use the same cadence on the mount alone. Purpose: detect mount–field interactions.
9. **Remount runs.** Remove and replace the sphere, then repeat. Purpose: seating reproducibility. A real contrast should reproduce; the criterion is consistency with the main estimate, not disappearance.
10. **Boundary items.** Record start/end reference weighings and the applicable B1/B2 boundary/reaction accounts. Purpose: bracket long drift and retain the complete support accounting required by the program protocol.

Failure of any required control blocks interpretation and enters the ambiguous disposition. No control failure can be reported as a null.

## 5. Acquisition sequence

1. **Survey and qualify.** Record the pre-session gradient and map; confirm geometry, saturation, instrument range, settling cadence and the ten-control checklist.
2. **Step-0 repeatability, before any sphere data.** Perform at least 20 alternating bias flips on the dummy and retain every raw reading. Determine $$\sigma_{\mathrm{single}}$$ and the required main-run pair count N by §6. Freeze that result and the acquisition plan in the annex. Repeatability may use alternating N,S,N,S; the main contrast requires balanced quads.
3. **Opening reference.** Record the sphere's bias-off reference weighing and boundary state.
4. **Main run.** Use complete **ABBA quads: N,S,S,N**, or the mirror S,N,N,S, with fixed settle time after each command. Randomize the preassigned choice of complete quads/blocks while retaining equal opposing pair orientations. Acquire at least N adjacent pairs. Simple fixed-order N,S,N,S is not an acceptable main sequence.
5. **Interleaved east–west null blocks.** Use the equivalent E,W,W,E cadence or its mirror. Acquire at least one east–west pair for every three main pairs, and meet the minimum control count below.
6. **Control blocks.** Acquire dummy, empty-mount and sphere-remount runs at the same cadence; each must meet the minimum control count. Do not replace the pre-sphere repeatability record with an after-the-fact estimate chosen after seeing the sphere.
7. **Closing references.** Record the closing reference weighing, boundary state, post-session gradient and map qualification.
8. **Freeze raw records before reduction.** Preserve the chronological CSV, independent state records, survey, nuisance records, randomization/blinding map and all exclusions under the [data-custody schema](data-schema.html). Apply only the preregistered reduction after that freeze.

The acquisition record must establish complete, balanced ABBA quads and valid timing. The frozen reducer checks that both main pair orientations occur; that check alone does not certify the full acquisition schedule or any physical control.

## 6. Preregistered reduction and interval criteria

### Pair estimator

For each adjacent N/S pair, orient the difference as north minus south regardless of which was read first:

$$
\begin{aligned}
d_i &= \mathrm{reading}_N-\mathrm{reading}_S \\
D &= \operatorname{mean}(d_i) \\
\sigma_D &= \frac{\operatorname{stdev}(d_i)}{\sqrt{n_{\mathrm{pairs}}}} \\
h &= 1.96\,\sigma_D \\
95\%\text{ interval} &= [D-h,D+h] \\
C &= \frac{D}{2W} \\
\text{Magnitude upper edge }U &= \lvert D\rvert+h \\
\text{Magnitude lower decision edge }L &= \lvert D\rvert-h
\end{aligned}
$$

For east–west, use E minus W. A negative L simply cannot satisfy the positive contrast threshold. Preserve the sign of D in the record; $$K_s$$-equivalent magnitudes are reported using $$\lvert C\rvert$$ and the frozen physical co/anti mapping.

A single fixed-order pair **does not cancel linear drift**. Equal-cadence ABBA quads give opposing pair-order drift terms whose mean cancels a linear drift. Missing or imbalanced quads and timing violations require the ambiguous disposition; do not silently repair the chronology after seeing results.

### Step-0 N rule

$$
\begin{gathered}
\sigma_d = \sqrt{2}\,\sigma_{\mathrm{single}} \\
n_{\mathrm{required}} = \max\left(1,\left\lceil\left[\frac{1.96\,\sigma_d}{D_{\mathrm{thr}}/2}\right]^2\right\rceil\right) \\
D_{\mathrm{thr}}/2 = 0.02\ \mathrm{mg}
\end{gathered}
$$

The dummy pair-difference standard deviation supplies $$\sigma_d$$; equivalently, $$\sigma_{\mathrm{single}}=\operatorname{stdev}(\text{dummy pair differences})/\sqrt{2}$$ in the frozen reducer. Determine and freeze N before sphere acquisition. The reducer recomputes it from the supplied dummy pairs; the pre-sphere timing and frozen N remain run-record requirements. Do not discard the original repeatability data.

A **NULL additionally requires** Step-0 present, achieved main $$n_{\mathrm{pairs}}\ge n_{\mathrm{required}}$$, and achieved $$h\le0.02\ \mathrm{mg}$$. If N is short, the result cannot be NULL; it can only satisfy the separate CONTRAST rule or remain AMBIGUOUS. A preregistered increase in N must follow the noise-based rule, not a changed effect threshold.

### Required control estimates

All four control run types — **dummy, empty, remount, ew_null** — are required with **at least 3 pairs each**. The additional acquisition requirements, including Step-0's $$\ge20$$ flips and interleaved east–west coverage, still apply.

| Control | Clean criterion |
|---|---|
| Dummy | Absolute pair-difference mean $$<0.02\ \mathrm{mg}$$ |
| Empty mount | Absolute pair-difference mean $$<0.02\ \mathrm{mg}$$ |
| East–west | Absolute $$E-W$$ pair-difference mean $$<0.02\ \mathrm{mg}$$ |
| Remount | Absolute difference between remount and main D $$<0.02\ \mathrm{mg}$$ |

The inequalities are strict: equality at 0.02 mg is not clean. For dummy/empty/east–west this is a zero band, not a “CI includes zero” rule. For remount it is **consistency-with-main**. A reproducing contrast is evidence; requiring remount to read zero would reject the very response being tested.

Missing/underpopulated control runs or excessive gradient generate GATE0_FAIL. Remount disagreement generates AMBIGUOUS. In either case, interpretation is blocked. A repeat may address the named failure, but no threshold or exclusion rule may move.

### Coefficient and toggle consequences

$$
\begin{gathered}
K_{\text{s-equiv}} = \frac{2K_0\lvert C\rvert}{\Gamma g_{\mathrm{geo}}} \\
g_{\mathrm{geo}}\in\{0.7454518768075703,\ 0.4797876129279153\}
\end{gathered}
$$

At $$C_{\mathrm{thr}}$$:

$$
\begin{aligned}
K_s\text{ limit}(g_{\mathrm{hi}}) &= 482.7226438282\ \mathrm{J} \\
K_s\text{ limit}(g_{\mathrm{lo}}) &= 750.0120701809\ \mathrm{J}
\end{aligned}
$$

These are conditional effective-support coefficients under the adopted source form and geometry convention. The single global range is not a claim that both endpoints are simultaneous limits: report which axis hypothesis supplies each bound.

For a qualified NULL, the projection relation gives $$(1-\cos10^\circ)C_{\mathrm{thr}}=$$ **1.122439243998×10⁻⁷**, reported as **1.1224×10⁻⁷**, for a future same-state/same-geometry toggle with the negligible deposit omitted. The build-threshold comparison uses the **full reversal $$2C=1.7113992\%$$ at 10°**; 0.86% is a half-contrast and is not a full reversal. There is no new spin-energy receipt in either calculation.

## 7. Executable reduction and raw-file contract

The byte-frozen [static_gate_reduce.py](static_gate_reduce.py) and [run_selftest.sh](run_selftest.sh) ship beside this file. They require Python 3 and a shell; no additional Python package is needed. The script's historical `STATIC-GATE-PREREG.md` references identify the source preregistration represented by this public edition; a second file by that name is not required.

The reducer reads a CSV with these columns:

```text
timestamp,run_type,bias_state,reading_mg
```

Allowed run_type values are `main`, `dummy`, `empty`, `remount`, `ew_null`. Use N/S states for the first four and E/W for `ew_null`. Supply chronological, finite numerical readings, both finite nonnegative gradient magnitudes, and the accompanying qualification records. Preserve raw records before any format or label reduction. The CSV is the balance stream, not the entire apparatus receipt.

Run from the directory containing the scripts:

```sh
python3 static_gate_reduce.py run.csv --gradient-pre 0.8 --gradient-post 0.9 > reduction.json
```

The gradient arguments shown are **usage examples**, not measured survey values. Use the actual pre/post survey magnitudes. JSON records the inputs, constants, main/control estimates, required N, verdict and conditional consequences; exact-geometry formula cross-checks accompany the governed reporting values.

The four-case synthetic self-test exercises a null, a contrast with a reproducing remount, a missing-remount failure and a gradient failure:

```sh
bash run_selftest.sh
```

It writes synthetic CSV files beside the scripts. Run it in a separate copy of the script directory, away from physical-run records. Passing synthetic cases checks the software paths only. Timing, complete ABBA balance, pre-sphere Step-0, maps, blinding and the ten-control qualification are operator/reviewer checks, not inferred from the JSON verdict.

## 8. Short bench runbook

1. Map the field/gradient at the sample and support; record the relevant component and verify $$\le 1\ \mathrm{\mu T/m}$$.
2. With the **dummy**, log $$\ge20$$ alternating flips; determine and freeze the required N before the sphere run.
3. Record the opening bias-off sphere reference and boundary state.
4. Run the sphere in the preassigned **ABBA or mirrored-ABBA** sequence with fixed settling; acquire at least N pairs.
5. Interleave east–west null blocks; retain at least one-third as many pairs as in the main run.
6. Run dummy, empty mount and remounted sphere controls. A sphere contrast should reproduce after remount.
7. Record closing reference and gradient survey; preserve the field map, timing, nuisance and qualification records.
8. Freeze the raw CSV and supporting records, then run the shipped reduction and report the locked outcome with its sign, uncertainty, geometry and control disposition.

**What each outcome teaches:** a qualified null fixes an upper bound and retains the microwave no-build decision under the current form; a qualified contrast gives a conditional coefficient for instrument sizing and motivates the separate physical interpretation receipts; ambiguity identifies the re-survey, additional-N or stopping action. Every outcome is instructive without relabeling it after acquisition.

## 9. Provenance and claim boundary

**Program research record, 2026-11-11** is the numerical and procedural source: final static-gate preregistration and bench runbook, byte-frozen reducer/self-test, commission rulings, and independent magnitude re-review. Reviewer-governed values are 482.7226–750.0121 J, ×23.2436–36.1139, 1.1224×10⁻⁷ at 10°, and 1.7113992% full reversal. Source-model constants and nominal inputs retain the equatorial/first-order and geometry qualifications above. The reference gradient arithmetic is imported dipole accounting; the control transfer must be characterized directly.

A support contrast or null can calibrate or bound an effective coefficient under an adopted form. It does not independently establish spin kinetic energy, physical twist, a general variable-G law or a larger POAMS claim. The separate state, reaction and direct-work requirements in the [program protocol](protocol.html) remain in force. **No physical experiment is reported as performed.**
