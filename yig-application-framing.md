# YIG Phase-Rotation — Application Framing
## The Experiment Restated in Claims Language (a Skeleton, Not a Filing)

*Date: 2026-08-12 · Framework: Normal Realism / POAMS · Authors: Star Lord, Parzival*
*Companion to `yig-levitation-experiment.md` (v7.0). Purpose: focus the program's minds on
application terms — what would be claimed, how it would be defined, what counts as the effect,
and what the prior-art landscape looks like — in anticipation of, not as, a filing. Nothing here
is legal advice.*

---

## 0 · Posture (read this first)

**This repository is a defensive publication.** Every revision of the experiment spec is public
with a commit date. That cuts both ways, and the trade should be held consciously:

- **Shield:** the published record is prior art against anyone else attempting to patent the
  same method/apparatus later. The mechanism, the materials selection logic, the pulsed
  protocol, the sign-reversal readout, and the λ-partition discriminant are all on the record
  with dates.
- **Cost:** public disclosure starts the novelty clock on ourselves. In the U.S. a 12-month
  grace period runs from first public disclosure; most foreign jurisdictions have **no** grace
  period — anything already published here is already unpatentable abroad as-is. Concretely:
  the March 2026 revisions' disclosed content has a U.S. filing window closing on the order of
  **March 2027**; material first disclosed in later revisions runs from its own date.
- **The live option:** improvements *not yet disclosed* (specific feedback laws, cavity/array
  geometries, materials treatments, control firmware, application-specific integrations) remain
  fresh subject matter. If patent value is ever intended, the discipline is: **decide before
  publishing each new increment** whether it goes in the public spec (shield) or in a filing
  first (sword). To date everything has gone to the shield — a defensible default for a
  foundational program; this document exists so that choice is made with eyes open.

**Why claims language at all, if not filing:** a claim is a falsifiable, operational statement
stripped of ontology — the same discipline as a registered gate. Drafting the experiment in
claims form forces exactly the application-grade questions: what is *operationally* done, what
is *measurably* produced, what is the *minimum* structure that produces it, and what would a
competitor change to design around it.

## 1 · The invention, in one sentence each

**Method.** Controllably altering the measured weight of a body by (a) aligning the intrinsic
circulation senses of its constituents with a static field, and (b) coherently advancing the
collective phase of the aligned population with a resonant electromagnetic drive, the weight
change being selectable in sign by the alignment sense and readable as a differential signal.

**Apparatus.** An insulating single-crystal ferrimagnetic test mass in a tuned microwave cavity
under a uniform static alignment field, driven by a pulsed, frequency-locked source, on a force
sensor, with controls and readouts arranged so the direction-dependent component of the force is
isolated from thermal, radiative, and gyroscopic artifacts.

Claims must stay **operational and mechanism-free** (steps and measurables, not ontology): the
claim recites *what is done and what is measured*; the specification carries the teaching (the
POAMS reading — weight as constraint force against the natural orbital radius; the twist/writhe
channel structure). This is standard patent craft and also good epistemics: the claim skeleton
below would survive even if the theoretical reading were revised, so long as the effect is real.

## 2 · Claims skeleton (prophetic; drafted in anticipation of reduction to practice)

**Independent — method:**

1. A method of altering the measured weight of a test body, comprising:
   (a) providing a test body comprising an electrically insulating, magnetically ordered
   crystalline material having a net uncompensated internal circulation (extant label: net
   electronic spin moment);
   (b) applying a substantially uniform static alignment field to said body along a selected
   axis, of magnitude at or above the material's saturation value;
   (c) applying an oscillating electromagnetic drive to said body at a frequency substantially
   equal to the material's precession resonance (extant label: ferromagnetic resonance) under
   said alignment field, whereby the aligned population is driven in phase-coherent precession;
   (d) measuring a change in the force required to support said body relative to the undriven
   state; and
   (e) selecting the sign of said change by selecting the sense of the alignment field relative
   to a reference rotation axis.

**Independent — apparatus:**

2. Apparatus for controllably altering the measured weight of a test mass, comprising: a
   single-crystal ferrimagnetic test mass; a resonant cavity enclosing said mass and tuned to
   its precession resonance; alignment coils arranged to produce a uniform, reversible static
   field across said mass; a drive source frequency-locked to the absorption resonance of said
   mass; a force sensor supporting the assembly; and a controller configured to execute a
   differential measurement protocol in which drive state and alignment sense are toggled and
   the direction-dependent force component is extracted.

**Dependent (the design-around surface — each is a real degree of freedom):**

3. The method of claim 1, wherein the drive is pulsed with pulse width 0.1–10 μs and repetition
   rate 50 Hz–1 MHz, the repetition rate being swept to maximize the measured change (the
   pump-and-relax protocol; Alzofon-informed, discovery parameter).
4. The method of claim 1, wherein the drive frequency is servo-locked to the absorption minimum
   through a directional coupler (temperature-drift tracking; the EPR/FMR lock).
5. The method of claim 1, further comprising toggling the drive at fixed alignment and recording
   the sign of the resulting change, thereby reading which internal channel receives the driven
   angular momentum (**the λ-partition readout** — the experiment's own discriminant claimed as
   a measurement method in its own right).
6. The method of claim 1, wherein the measured relaxation time of the force change upon drive
   termination exceeds the material's electronic coherence time, indicating storage in a channel
   other than the driven precession (the relaxation-curve diagnostic).
7. The apparatus of claim 2, wherein the cavity is a TM₀₁₀ cylinder with unloaded Q ≥ 10⁴ and
   the test mass is a polished sphere of diameter 2–15 mm (uniform demagnetization ⇒ single
   sharp resonance).
8. The apparatus of claim 2, comprising a plurality of test masses in a common or coupled
   cavity array driven phase-coherently (the scaling claim).
9. The method of claim 1, wherein the material is selected from the class of insulating
   crystals bearing net alignable circulation: iron garnets (YIG and substituted variants),
   doped corundum (ruby, sapphire class), olivine class (the materials envelope — the
   operational technology's own class per the engineering analysis).
10. The apparatus of claim 2, further comprising a vertical RF-transparent guide above the
    cavity and a distributed drive structure maintaining resonant illumination of the test mass
    through vertical travel (the levitation-containment claim, Rev 5).
11. A method of trimming the effective weight of a payload element comprising mounting thereto
    a body per claim 1 and operating the drive to produce a selected weight offset (the use
    claim — actuation/trim; deliberately modest).

**Definiteness note.** Claim 1(d)'s "change" must be operationally bounded to be a claim at
all — the spec's own numbers do the work: detection threshold 7 ppm of a 150 mg mass on a
0.01 mg balance (Rev 1); effect declared only on the **differential** signal (ON−OFF, UP−DOWN)
exceeding 3σ of baseline; controls (non-magnetic mass; off-resonance drive) reciting zero.

## 3 · Definitions (patent-style "as used herein," liturgy-clean)

- **Circulation quantum / accumulator:** the persistent angular-momentum organization
  constituting a constituent of the body (extant comparative labels: atom, ion moment). Its
  intrinsic circulation is constitutive — not addable — per the Rev 3 correction.
- **Alignment:** ordering of the circulation senses toward a common axis by a static field;
  quantified by the polarized fraction (order unity at saturation for ferrimagnets — the reason
  this class and not Barnett-level bulk rotation, factor ~10¹⁰, Laithwaite's missing lever).
- **Coherent phase advance:** driven, in-lockstep advance of the aligned population's
  collective orientation phase at the precession resonance; operationally certified by the
  absorption lock (reflected-power minimum). The micro-equivalent of bulk rotation without the
  fracture limit — GHz winding vs ~170 Hz mechanical.
- **Weight:** the support force at the constraint (what the load cell reads) — operationally
  the only definition a claim needs; the specification may add: the constraint bill for
  standing off the natural orbital radius (POAMS reading, GROUNDING §3).
- **Sign / channel structure (specification teaching, kept out of the claims):** driven angular
  momentum can land in the intrinsic-alignment channel (twist → effective-coupling route →
  co-sense **heavier**; the settled brass-gyroscope anchor) or the orbital-winding channel
  (writhe → angular-momentum-numerator route → co-sense **lighter**); the **λ-partition** —
  which channel the resonant drive feeds — is precisely what claim 5's readout measures. Either
  sign is a positive result; the differential protocol is sign-agnostic by design.

## 4 · What counts as the effect (the go/no-go, restated as acceptance criteria)

| Acceptance test | Pass condition | Artifact excluded |
|---|---|---|
| A1 directional signature | differential weight change reverses sign under alignment reversal at fixed drive | heating, radiation pressure, magnetostriction (sign-blind) |
| A2 resonance specificity | effect present at FMR lock, absent ≥500 MHz off-resonance at equal power | broadband RF/thermal coupling |
| A3 material specificity | zero effect on matched non-magnetic mass under full protocol | balance/RF interaction, convection |
| A4 λ-readout | drive-toggle at fixed alignment yields a definite, repeatable sign | — (this one is a measurement, not a control) |
| A5 relaxation diagnostic | force relaxation time ≠ electronic T₂* class | pure FMR ring-down |
| A6 channel separation (Rev 7) | effect reads on the constraint force, not on motional statistics; body has net twist to align | gyroscopic stiffening (channel 1), churn (channel 2) |

Reduction to practice = A1 ∧ A2 ∧ A3 at 3σ. Everything else is characterization.

## 5 · Prior art landscape (named, dated, distinguished)

- **Alzofon 1981 (AIAA-81-1608), Dynamic Nuclear Orientation.** Closest art. Same drive class
  (pulsed GHz at resonance under static alignment), same claim target (gravitational
  modification). Distinguished by: working channel (electronic vs nuclear orientation — ~10³
  moment advantage, ~10⁵ shorter coherence; different regime), materials (insulating
  single-crystal ferrimagnet vs Al+Fe composite), coherence architecture (tuned cavity enforcing
  spatial phase), and protocol (feedback-locked, differential, sign-resolving). His framing
  (virtual-particle energy removal) is not adopted; his parameters informed the pulse protocol.
- **Hathaway/AGNUE (Toronto).** Partial experimental verification of the Alzofon program
  ("anomalous motion of a test mass"); no theoretical frame, no sign protocol. Witnessed by
  Star Lord with H. Puthoff.
- **Wallace patents (US 3,626,605 / 3,626,606, 1971).** The extant patent record's spin-force
  claims ("kinemassic field"): force-field generation by aligned nuclear spin in rotating
  bodies. Prior art to acknowledge and distinguish: mechanical rotation of half-integer-spin
  material bodies vs stationary bulk with electromagnetic collective phase advance; no resonant
  drive, no cavity, no sign-reversal readout. Their existence is also the cautionary tale: filed,
  granted, never reduced to accepted practice — claims without the differential discipline.
- **Einstein–de Haas / Barnett (1915).** The established alignment⇄rotation ledger both ways —
  cited as the anchor that alignment IS mechanical angular momentum at the constituent level.
  Not a weight claim.
- **Laithwaite (1974 RI discourse).** The right instinct on the wrong lever (bulk rotation,
  Barnett-level alignment ~10⁻¹⁰); static weight-loss claim did not survive careful weighing.
  Our design is his lever inverted: order-unity alignment first, then electromagnetic winding.
- **St Andrews levitated rotor ("600 MRPM sphere cooling").** The modern decoy, analyzed in the
  spec (Rev 7): diamagnetic body (no twist to align), motional statistic (not constraint force),
  channel-1 gyroscopics. Excluded by the acceptance criteria's own terms (A6).
- **Standard FMR/EPR instrumentation.** All drive/lock components are stock art; no novelty
  claimed in the microwave chain — novelty lives in (i) the *purpose-composition* (weight
  modulation), (ii) the differential sign-resolving protocol, (iii) the λ-readout.

## 6 · The application ladder (kept honest)

| Rung | Condition | Application class |
|---|---|---|
| 0 (now) | pre-detection | The experiment itself is the product: a decisive, cheap (~$1–2k) discriminating instrument |
| 1 | A1–A3 pass at mg scale | Metrology: a new force-modulation standard; the λ-partition as a laboratory observable; publication + replication kit |
| 2 | effect ≥ 0.1% of test-mass weight, controllable | Mass trim / ballast-free attitude actuation (satellite reaction control without propellant or wheels — trim class, not lift class) |
| 3 | effect approaches unity at engineering power | Lift/launch assist; the Rev 5 architecture (containment, feedback, distributed drive) becomes the product skeleton |

Rung 2 is the first commercially meaningful claim and it is *modest*: a body whose effective
weight is electrically adjustable by parts-per-thousand is already a spacecraft actuator. The
ladder deliberately does not lead with levitation.

## 7 · What this exercise changes about the program (the mind-focusing)

1. **Claims are registered gates wearing a suit.** Operational steps, measurable outcomes,
   pre-declared acceptance criteria, artifacts named and excluded — the program already runs at
   patent discipline; this document only changes the notation.
2. **The λ-partition is not a complication — it is a second invention.** A method of *measuring
   which channel driven angular momentum enters* stands on its own (claim 5) regardless of the
   weight effect's magnitude, and it is the piece with no prior art at all.
3. **The disclosure clock is the one strategic decision.** Everything disclosed to date is
   shield. The next genuinely new increments — control laws, array geometry, materials
   treatments — should each pass through the publish-or-file decision consciously (§0).
4. **Mechanism-free claim language is an honesty instrument.** Writing the effect without POAMS
   vocabulary and without extant vocabulary (no "gravity shielding," no force-field) leaves
   exactly what a balance would certify — which is the same standard the research ledger already
   holds every swing to.

---

*Cross-references: `yig-levitation-experiment.md` (full spec, Revs 1–7); the λ-partition record
`memory/poams-audit/directional-sign-2026-07-19.md` and `LAMBDA-SWAMP-forward-opus.md` (research
workspace); Alzofon AIAA-81-1608 (`Alzofon-1981-AIAA.pdf`, this repo); GROUNDING §3–§4 (weight
as constraint bill; spin-orbit channel structure).*
