# Supportive Bench Experiments — Exhibit-Verification Track

*Established 2026-08-16 (Star Lord directive: "simple supportive work when we get into the lab"). This track is **secondary and opportunistic**: the program's primary experiment remains the YIG phase-rotation spec (`yig-levitation-experiment.md`, v7.0). Entries here are cheap bench items that support the public exhibit corpus by putting modern instrumentation on claims the published record states but the extant literature has not re-run. Shield-side discipline applies throughout: nothing below is claimable apparatus; both entries test the published Pope record.*

---

## EXP-S1 — Dead-Circuit Transient Audit

**Supports:** POAMS & Electricity exhibit §2 (the dead circuit). **Record basis:** Pope, *Why the Constant c Cannot Be a Speed* series (the demonstration "any electrician can run").

**Working position (the record's, adopted):** with the far-end switch open, the circuit is completely dead at the source — no entry, no start-up transient, *including* the variant with a large capacitor fitted just before the open switch. Dead until it's not; then it's not. Energization on closure is whole-circuit, with settling that reads as L/c.

**Contrast class (extant expectation):** transmission-line theory predicts brief connection transients — the line charging at its characteristic impedance, settling over round trips. The two pictures agree on DC steady state; they differ on the first microseconds. Nobody appears to have published a sensitive modern look specifically framed on this question.

**Apparatus (all commodity):** bench DC source with clean switching; line pairs — coax spools (100 m and ~1 km) plus an open-wire variant; far-end switch; series-capacitor variant; source-side sensing: fast current probe into a GHz-class scope, plus an integrating charge/electrometer bound for the "no entry" claim.

**Protocol:**
1. Source connected, far end open — record source-side entry with statistical bounds (probe artifacts and displacement-current accounting audited; shielded and unshielded runs).
2. Capacitor-before-the-open-switch variant — the record's sharpest version.
3. Closure events — energization timing against L/c across line lengths.
4. Far-end Morse keying — timing audit against the projection reading.
5. Controls: dummy loads, probe-only runs, geometry swaps.

**Outcome handling:** every outcome is informative. A clean null at modern sensitivity is a strong supportive result for the exhibit and the program's credibility. A measured transient gets fully characterized and the exhibit revisited against the record per the corpus replacement policy. Cost class: trivial (cable spools + borrowed scope time).

---

## EXP-S2 — Teleblocking Containment Bound (Pope–Hopton Retry)

**Supports:** POAMS & Telecommunications exhibit §4 (retrograde signalling, the record's own limits). **Record basis:** *Faster than Radar* series; *Refraction in Optic Fibres* out-take fn. 3 — Pope and Dr. John Hopton's 1970s optical trials, inconclusive **specifically on containment** (the "loose-knit fisherman's sock" leakage).

**Object:** measure, not presume. The record names sink-exclusivity as the open engineering condition for its retrograde channel. This experiment **bounds the leakage** for a real guided channel and looks for any source-side signature of far-end receptivity modulation under progressively better containment.

**Simple first version (RF, not optics):** high-Q shielded cavity/waveguide link; uniquely matched narrowband sink; far-end receptivity keyed (detune / load-switch) at a lock-in reference rate; source-side monitoring of emission and loading signatures (source current, reflected power, cavity loading), phase-locked to the keying.

**Honest discriminator, stated up front:** ordinary reflection/SWR responses to far-end changes propagate at the projection rate and will produce source-side signatures at s/c delay — that is extant engineering, not the effect. Any candidate positive must be separated by **timing at distance** (long-baseline variant) before it is called anything. The record itself prices all conventional readings at s/c; the purpose here is the leakage bound and the containment engineering, not a communications claim.

**Status:** design-later; lab phase. Cost class: low (bench RF + shielding).

---

*Both entries: no claimable device matter; the patent family map explicitly excludes FTL communications — EXP-S2 is a bound-measurement on the published record, not a comms device. Exhibit cross-links: `poams-electricity.html` §2, `poams-telecommunications.html` §4.*
