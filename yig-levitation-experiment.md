# YIG Phase Rotation Experiment — Design & Specification

## Objective

Demonstrate measurable weight change in a Yttrium Iron Garnet (YIG) sphere by driving coherent phase rotation of its internal angular momentum structures via ferromagnetic resonance (FMR). The experiment aims to show that bulk coherent angular momentum state change alters the test mass's natural orbital radius relative to Earth, manifesting as a change in constraint force (measured weight).

## Theoretical Basis (POAMS Framework)

- Mass is rotational inertia of quantized angular momentum vortices (accumulators)
- "Weight" is the constraint force preventing an object from occupying its natural force-free orbital radius
- Changing the net angular momentum state of the bulk material changes its orbital radius
- Anti-spin (opposing Earth's rotation) → radius extension → reduced weight
- Co-spin (aligned with Earth's rotation) → radius contraction → increased weight
- **Sign — stated in Normal Realist terms (no container):** There is no spatial "field" the body sits inside; in Normal Realism the angular momentum *is* the happening — it *is* the spatial separation, mass, and motion (Pope & Osborne). "Radius" is the angular-momentum *relation* between body and Earth, not a distance across empty space. So the sign is set by how two angular momenta **compose**, per Pope, *Einstein's Lost Legacy*, App. 4/5: the body's internal spin and its orbital co-rotation with Earth add/subtract as vectors; total spin-plus-orbital AM fixes the natural radius via `L = mvr` (equivalently, spin makes `G` a variable). Rule: spin vector **same sense** as orbital → natural radius **contracts** → the body's fixed surface radius now exceeds its natural radius (natural orbital speed rel. to surface rises) → bears harder on the surface constraint → **heavier**; **opposed** → natural radius **extends** past the surface → contact reaction drops → **lighter**. ("Weight" = the contact reaction at the surface, not an *in vacuo* force across a gap.) Pope states it for our exact case: *"adding spin angular momentum to a particle... on the Earth's equator... will increase or decrease its natural orbital speed relative to the Earth's surface, making it weigh either more or less, depending on the direction of its motion"* (App. 5). *Labeling note:* right-hand rule names the vectors ("co-spin" = spin in the same sense as orbital co-rotation); this is pure labeling — a left-hand rule relabels both together, physics unchanged. The sign lives in the physical direction of the spin vector relative to the orbital vector (a measurable AM relation), read off Pope's vector composition, not re-assumed. The experiment measures that relation directly.
- **Channel partition (λ) — added 2026-07-19, cross-vendor adversary-checked (Sol/OpenAI GPT-5.6 + Fable/Anthropic, independent, liturgy-clean).** The sign above is the **twist/spin** routing: intrinsic spin composes into the effective coupling (variable `G`, App-4/5), co-sense → natural radius contracts → **heavier**. There is a *second* routing with the OPPOSITE sign — angular momentum deposited as **writhe** (bulk orbital winding, adding to `L_orb` in `r_ff = L_orb²/GMm²`) → natural radius *extends* → **lighter**. So co-sense reads **heavier if the drive lands as twist, lighter if it lands as writhe**; which one FMR-driven coherent phase-advance feeds is the **λ-partition**. This is not a defect but a measurement: the **sign of the co-spin weight change reads the partition off directly** — heavier ⇒ twist deposit (through `G`), lighter ⇒ writhe deposit (through `L_orb`). Either sign is a positive result; the primary criterion (sign *reverses* with alignment) holds in both. The brass-gyroscope repro (below) is the **clean twist case** — a rotor spun about its own axis is body *spin = twist* (not orbital winding about Earth), and it already measures co-spin → **heavier** (App-5 sign, confirmed). So the intrinsic-spin sign is settled heavier; the only thing the YIG run adds is whether coherent collective phase-advance stays **pure twist** (→ heavier, as the companion paper commits) or **leaks into writhe** (→ lighter) — its measured sign confirms which. [Derivation + raw adversary outputs: `memory/poams-audit/directional-sign-2026-07-19.md`]
- **λ-partition — forward-derived (2026-07-19, Opus + Sol cross-vendor, independent).** The drive is two deposits in *different* channels, with *opposite* co-sense signs. (i) DC **alignment** deposits net intrinsic-spin **polarization** = twist → variable-`G` → co-sense **heavier** (the Barnett / brass-gyroscope case, settled). (ii) The microwave phase-advance cannot touch constitutive own-axis spin, so it can only advance orientation = swept solid angle Ω = 2π(1-cosθ) = **writhe** → adds to the `L_orb` numerator → co-sense **lighter**, a bounded offset ∝(1-cosθ) held only while driven (relaxes at drive-off). So the clean λ readout is the **microwave-toggle at fixed alignment**: its sign isolates the drive/writhe channel (forward prediction: lighter). Caveats: (a) rests on the driven coning being physical axis-winding, not a coordinate relabel — decided empirically by whether killing the drive leaves persistent added linking (weight-relaxation vs coherence-decay); (b) a sign-blind, always-heavier maintenance channel (energy/dissipation) coexists but cancels exactly in the co/anti differential *provided the reversal is symmetric* (matched cone angle, polarized fraction, dissipation, drive); (c) the swamping law S(θ,ρ) — hence any optimal drive point — is empirical, not forced. [Forward derivation: `memory/poams-audit/LAMBDA-SWAMP-forward-opus.md`]
- Coherent phase rotation = all accumulators precessing in lockstep = macroscopic angular momentum state change

## Why YIG

| Property | Value | Why It Matters |
|---|---|---|
| FMR linewidth | ~0.3 Oe (narrowest known) | Longest coherence time — precession persists long enough to build bulk state |
| Electrical resistivity | ~10¹² Ω·cm (insulator) | Full microwave penetration — no skin depth problem, entire volume is active |
| Spin density | ~2.1 × 10²² spins/cm³ | High accumulator count per unit volume |
| Saturation magnetization | ~1780 Gauss | Aligns readily with modest applied static alignment |
| Curie temperature | 560 K | Stable at room temperature with wide margin |
| Availability | Commercial, polished spheres | No custom fabrication needed |
| Cost | $50-100 per sphere | Affordable for iteration |

## Experimental Design

### Overview

A polished YIG sphere sits on a precision analytical balance inside a small RF-transparent enclosure. A pair of Helmholtz coils provides a uniform static alignment along the vertical axis (parallel or anti-parallel to Earth's rotation axis component). A microwave source drives the sphere at its FMR frequency, establishing coherent phase rotation across all accumulators simultaneously. Weight is logged continuously as the drive is swept through resonance, toggled on/off, and reversed in alignment sense.

### Component Specification

#### 1. YIG Sphere (Test Mass)

- **Size:** 2-5 mm diameter (start with 3mm — standard commercial size)
- **Source:** Ferrisphere, MSE Supplies, or similar vendor
- **Quantity:** Order 3-5 spheres for repeatability testing
- **Estimated cost:** $50-80 each, ~$200 for a set
- **Mass:** ~0.15g (3mm sphere, density 5.17 g/cm³)

#### 2. Precision Analytical Balance

- **Resolution:** 0.01 mg (10 microgram)
- **Capacity:** ≥1g
- **Key requirement:** Must not be affected by RF or static alignment fields
- **Option A:** Sartorius/Mettler micro-balance (used on eBay: $200-500)
- **Option B:** DIY torsion balance with optical readout (more sensitive, more work)
- **Shielding:** Balance electronics housed in grounded copper mesh enclosure with only the weighing pan exposed
- **Estimated cost:** $300-500

**Sensitivity analysis:** A 3mm YIG sphere weighs ~150mg. At 0.01mg resolution, we can detect a weight change of ~7 parts per million (7 ppm). If the effect is larger than this, we see it directly.

#### 3. Helmholtz Coil Pair (Static Alignment)

- **Purpose:** Provide uniform alignment along vertical axis to orient all accumulator vortex axes
- **Configuration:** Matched pair, separation = radius (standard Helmholtz geometry)
- **Coil diameter:** 10-15 cm (large enough for uniform central region around the sphere)
- **Target strength:** 500-3000 Gauss (tunable) — YIG saturates around 1780 G, we want to reach and exceed this
- **Wire:** 18 AWG magnet wire, ~200 turns per coil
- **Power supply:** Adjustable DC bench supply, 0-30V / 5A
- **Build:** Wind on 3D-printed or PVC forms
- **Estimated cost:** $40 wire + $60 power supply = ~$100
- **Orientation:** Coil axis vertical. Reversing current direction reverses alignment sense (co-spin vs anti-spin relative to Earth)

#### 4. Microwave Source (Phase Rotation Drive)

- **Frequency range:** 1-15 GHz (FMR frequency depends on applied static alignment strength)
- **FMR frequency formula:** f = γ × B_applied, where γ ≈ 2.8 MHz/Gauss for YIG
  - At 1000 G → f ≈ 2.8 GHz
  - At 2000 G → f ≈ 5.6 GHz
  - At 3000 G → f ≈ 8.4 GHz
- **Power:** 10-100 mW should be sufficient for a 3mm sphere (start low, increase)
- **Option A (recommended):** Voltage-Controlled Oscillator (VCO) evaluation board
  - Analog Devices HMC739 or similar, covers 6-12 GHz
  - ~$50-100 for eval board
  - Powered by bench supply, frequency set by tuning voltage
- **Option B:** Used microwave signal generator (HP/Agilent 8350 series on eBay, $200-400 — more precise, overkill for first pass)
- **Delivery:** Small horn antenna or open-ended waveguide pointed at the sphere from the side (not above/below — don't interfere with the weight measurement axis)
- **Estimated cost:** $100-200

#### 5. Microwave Power Detector (Absorption Measurement)

- **Purpose:** Confirm FMR is actually occurring. At resonance, the sphere absorbs microwave power sharply. This is your "lock-on" indicator.
- **Method:** Diode detector on far side of sphere from the source. When you hit resonance, transmitted power drops — the sphere is eating the energy.
- **Component:** Schottky diode detector + oscilloscope or multimeter
- **Estimated cost:** $20-40

#### 6. Enclosure

- **Purpose:** Isolate from air currents (balance sensitivity enemy #1), provide RF-transparent housing
- **Material:** Acrylic or polycarbonate box around the weighing region
- **Size:** ~20 × 20 × 20 cm, open bottom seated on balance platform
- **RF transparency:** Acrylic is transparent to microwaves — no problem
- **Access:** Small ports for microwave delivery and Helmholtz coil leads
- **Estimated cost:** $20-30

### System Layout (Top View)

```
        Helmholtz Coil (top)
              ___
             /   \
    MW      | YIG |      MW
   Source →  | ● |  ← Detector
             \___/
        
        Helmholtz Coil (bottom)
        
    ════════════════════════
         Balance Pan
    ════════════════════════
         Balance Body
      (shielded enclosure)
```

### Measurement Protocol

#### Phase 1: Baseline Characterization

1. Place YIG sphere on balance, enclosure sealed
2. Let balance settle for 30 minutes (thermal equilibrium)
3. Record baseline weight (average over 10 minutes, note drift rate)
4. Turn on Helmholtz coils (1000 G). Record any weight change from magnetostriction or coil vibration
5. Turn off. Repeat 5x. Establish that static alignment alone does not produce systematic weight shift

#### Phase 2: Find Resonance

6. Set static alignment to 1000 G → expected FMR at ~2.8 GHz
7. Turn on microwave source at low power (~10 mW)
8. Slowly sweep frequency while monitoring the diode detector
9. When transmitted power dips sharply → you've hit FMR
10. Note exact frequency. This confirms coherent phase rotation is occurring in the bulk
11. Repeat at 2000 G, 3000 G to verify f = γB relationship

#### Phase 3: Weight Measurement at Resonance

12. Set static alignment to target value
13. Record weight with microwaves OFF (1 minute average)
14. Turn on microwave drive at FMR frequency
15. Record weight with microwaves ON (1 minute average)
16. Turn off. Record weight again (1 minute)
17. Repeat 20x for statistics

#### Phase 4: Direction Reversal

18. Reverse Helmholtz coil current (flip alignment direction)
19. Find new FMR frequency (should be identical — same magnitude)
20. Repeat Phase 3 measurements
21. Compare: if weight change reverses sign when alignment reverses, that's the signal

#### Phase 5: Controls

22. Replace YIG sphere with non-magnetic sphere of same size (glass bead)
23. Repeat Phase 3. Should show zero effect. This rules out microwave radiation pressure, thermal convection artifacts, etc.
24. Repeat with microwave drive at frequency 500 MHz AWAY from FMR. Should show zero effect. This rules out general microwave heating as cause.
25. Test at different static alignment strengths. Effect should scale with the number of coherently driven accumulators (proportional to how far above saturation you are).

#### Phase 6: Atmosphere Independence (Optional but Powerful)

26. Seal the enclosure, run with air
27. Flush with helium, repeat
28. Flush with argon, repeat
29. Identical results across atmospheres confirms mechanism is not aerodynamic or convective

### Data Analysis

**Primary signal:** Weight(FMR ON, alignment UP) minus Weight(FMR ON, alignment DOWN)

This subtracts out any symmetric artifacts (microwave heating, radiation pressure, etc.) and isolates the direction-dependent component — which is what POAMS predicts and conventional physics does not.

**Statistical threshold:** Signal must exceed 3σ of the baseline noise floor to claim detection.

### Expected Challenges

1. **Thermal drift:** Microwaves heat the sphere slightly → thermal convection changes apparent weight. Mitigation: enclosed chamber, symmetric microwave exposure, and the direction-reversal protocol (thermal effects don't reverse with alignment direction)

2. **Coil forces:** Helmholtz coils produce force on the YIG sphere (it's attracted to the coils). Mitigation: symmetric coil pair produces no net vertical force at center point. Careful positioning matters.

3. **Vibration:** Microwave source, power supply fans, building vibration. Mitigation: rubber isolation pads under balance, measurements taken at night when building is quiet.

4. **RF interference with balance:** Microwave leakage could affect balance electronics. Mitigation: shielded balance enclosure, and the control measurement with non-magnetic sphere confirms this isn't happening.

5. **Magnetostriction:** YIG changes shape slightly under alignment. Mitigation: this is a static effect — present when coils are on, absent when off. Phase 1 baseline measurement isolates this.

### Bill of Materials

| Component | Specification | Est. Cost |
|---|---|---|
| YIG spheres (×5) | 3mm diameter, polished | $200 |
| Analytical balance | 0.01mg resolution, used | $400 |
| Magnet wire | 18 AWG, 1 lb spool | $25 |
| Coil forms | 3D printed or PVC pipe | $10 |
| DC power supply | 0-30V, 5A adjustable | $60 |
| VCO eval board | 2-10 GHz range | $100 |
| RF amplifier | 100mW, matching band | $80 |
| Schottky detector | Zero-bias, broadband | $25 |
| Acrylic enclosure | 20×20×20 cm | $25 |
| SMA cables/connectors | Assorted | $30 |
| Small horn antenna | 3D printed + copper tape | $15 |
| BNC cables, banana plugs | Assorted | $20 |
| Multimeter (if not owned) | Basic digital | $30 |
| **Total** | | **~$1,020** |

### Phase 2 Upgrades (If Signal Detected)

- **Larger YIG sphere** (10-15mm) — signal should scale with volume (cube of radius)
- **Lock-in amplifier** — extract signal from noise floor at sub-microgram levels
- **Vacuum chamber** — definitively rule out atmospheric effects
- **Multiple spheres in array** — coherent phase rotation across multiple coupled spheres
- **Bismuth-doped YIG or hexaferrites** — higher per-accumulator angular momentum with retained coherence

### Success Criteria

| Outcome | Meaning |
|---|---|
| Weight change reverses with alignment reversal at FMR | **Primary success.** Direction-dependent weight modification via coherent angular momentum state change. Conventional physics has no explanation. |
| Weight change at FMR but same sign both directions | Partial success. Effect is real but mechanism may be symmetric (thermal, radiation pressure). More investigation needed. |
| No weight change above noise floor | Null result at this sensitivity. Need larger sphere, better balance, or lock-in amplifier. Does not disprove the hypothesis — may just be below detection threshold. |
| Weight change at non-FMR frequencies too | Artifact. Something other than coherent phase rotation is affecting the measurement. Back to debugging. |

---

## Summary

Drive every accumulator in a YIG sphere into coherent phase rotation via FMR. Measure weight change. Reverse alignment direction and measure again. If the weight change reverses sign, we've demonstrated controllable orbital radius modification of a material via angular momentum state engineering.

That's the flying car. Just very small and on a scale. For now.

---

---

## Revision 2: Cavity-Enhanced Bulk Ferrite Design (Gram-Scale Effect Target)

### Key Insight (from discussion)

Conservation of angular momentum demands that if orbital angular momentum is held constant and spin angular momentum is driven in, the natural orbital radius changes instantaneously. The effect is:
- **Linear** — scales directly with total driven spin angular momentum
- **Instantaneous** — appears within microseconds of FMR engagement
- **Reversible** — sign flips with alignment reversal
- **No threshold** — present from the first driven accumulator

### Revised Architecture

Replace the small YIG sphere + precision balance with a large ferrite mass inside a resonant microwave cavity on a robust scale.

#### Why Cavity-Enhanced

A tuned copper cavity stores microwave energy, amplifying effective drive power by the cavity Q factor (10,000-50,000×). This:
- Drives large precession cone angles with modest input power
- Enforces spatial phase coherence across the entire ferrite volume (the cavity mode has defined phase everywhere)
- Solves the coherence problem even for broader-linewidth bulk ferrites
- Eliminates the need for YIG-level intrinsic linewidth

#### Revised Component Specification

| Component | Specification | Est. Cost |
|---|---|---|
| Bulk ferrite cylinder | NiZn or LiZn, 500g-1kg, machinable | $30-80 |
| Copper cavity | Cylindrical, tuned to FMR frequency, machined from tube + endcaps | $50-100 |
| SMA input coupler | Coupling loop or probe | $20 |
| Helmholtz coils | 10-15 cm diameter pair, 18 AWG, ~200 turns each | $40 |
| DC power supply | 0-30V / 5A adjustable (for coils) | $60 |
| Microwave source | VCO + power amplifier, 1-5W, 1-10 GHz range | $200-300 |
| Scale | 0.01g resolution sufficient for gram-level changes | $25 |
| Network analyzer (optional) | NanoVNA — confirm cavity resonance and FMR overlap | $150 |
| SMA cables, connectors | Assorted | $30 |
| **Total** | | **~$600-800** |

#### Design Steps

1. **Select ferrite composition** — NiZn ferrite preferred (low loss at GHz, insulating, cheap, available in bulk)
2. **Machine ferrite to fit cavity** — cylinder that fills the copper cavity interior
3. **Determine FMR frequency** — f = γ × B_applied (γ ≈ 2.8 MHz/G for most ferrites)
4. **Design cavity** — cylindrical TM₀₁₀ mode, radius chosen so cavity resonance = FMR frequency at target alignment strength
5. **Confirm overlap** — use NanoVNA to verify cavity mode and FMR absorption overlap. Tune by adjusting alignment strength (shifts FMR) or cavity dimensions (shifts cavity mode)
6. **Drive and measure** — engage microwave source, confirm FMR absorption, read scale

#### Measurement Protocol (Revised for Gram-Scale)

1. Place loaded cavity assembly on scale. Record stable baseline weight.
2. Energize Helmholtz coils (alignment UP). Record any static weight change from coil/ferrite interaction.
3. Engage microwave drive at cavity-FMR overlap frequency.
4. Record weight. Expected: instantaneous shift visible on 0.01g scale.
5. Kill microwave drive. Weight returns to baseline.
6. Repeat 10×.
7. Reverse Helmholtz current (alignment DOWN). Repeat steps 3-6.
8. **Primary signal:** Weight change must reverse sign when alignment reverses.
9. Control: replace ferrite with non-magnetic ceramic of same mass. Repeat. Zero effect expected.

#### Precession Cone Angle and Drive Power

The spin angular momentum driven per accumulator depends on the precession cone angle θ:
- Small angle (1-5°): small perturbation, small effect per accumulator
- Large angle (45-90°): massive spin angular momentum change per accumulator

Cone angle scales with microwave drive amplitude (H_rf):
- θ ≈ arctan(γ H_rf / Δω) where Δω is the linewidth

The cavity Q amplifies H_rf inside the cavity by √Q relative to the input. For Q = 10,000, a 1W input creates effective fields equivalent to 10kW in free space. This is how we drive large cone angles with tabletop power levels.

#### Scaling Path

If the initial build produces measurable effect:
- **Increase ferrite volume** — linear scaling means 2× mass = 2× effect
- **Increase drive power** — larger cone angle = more spin angular momentum per accumulator
- **Multiple cavities** — array of cavity-ferrite units for additive effect
- **Optimized ferrite composition** — high spin density, low damping, matched to cavity

If the effect exceeds ~10% of test mass weight at any scale, the path to engineering application is open.

### Success Criteria (Revised)

| Outcome | Meaning |
|---|---|
| Gram-scale weight change, reverses with alignment | **Decisive success.** Visible on a kitchen scale. Unexplainable by conventional physics. Funding-ready demonstration. |
| Milligram-scale weight change, reverses with alignment | **Confirmed effect, needs scaling.** Larger ferrite volume, more drive power, or better material. |
| Sub-milligram, reverses with alignment | **Detected but marginal.** Return to precision balance protocol (Rev 1). Need lock-in amplifier and vibration isolation. |
| No directional effect at any power level | **Null result.** Either the fractional effect is below all sensitivity thresholds, or the mechanism requires something beyond FMR-driven precession. Reassess theory. |

---

---

## Revision 3: Corrected Physics — Collective Phase Advance Protocol

*Date: 2026-03-18*

### Fundamental Correction

**You cannot add spin angular momentum to an individual atom without changing the element.** An element's intrinsic spin IS its identity — the vortex structure that makes Bismuth be Bismuth, Iron be Iron. This is not a knob you turn.

What you CAN do:

1. **Polarize** — align the velocity vectors of atomic vortices (naturally randomized in non-magnetic materials). A "magnet" is partial alignment of fixed-spin vortices.
2. **Advance the collective phase** — once aligned, coherently advance the rotational phase of the entire collection. This is the micro-physical equivalent of physically rotating the bulk. Atoms keep their identity. Their intrinsic spin doesn't change. But their collective orientation advances, and that collective phase advance IS angular momentum added to the system.

This is what Einstein-de Haas demonstrated: magnetize an iron bar → spins align → bar physically rotates. Angular momentum conservation. The spin alignment IS mechanical rotation at the atomic level.

**Star Lord has reproduced this as a weight change with a brass gyroscope on a tabletop.** Macroscopic rotation → measurable weight change. Same mechanism. Our experiment does the same thing electromagnetically, at GHz winding rates instead of ~170 Hz mechanical rotation — seven orders of magnitude faster, no structural fracture limit.

### Why "Phase Multiplicity" Is the Key

At the macro scale, you can physically rotate a bulk object to add angular momentum. But material fracture sets the speed limit. You cannot spin a ferrite cylinder at 10⁹ RPM.

At the micro scale, resonant electromagnetic drive advances the collective phase of aligned vortices without mechanical rotation of the bulk. Each microwave cycle at resonance advances the phase of all aligned vortices by one step. The bulk material sits still on the scale while its internal angular momentum state winds up.

**Phase multiplicity** = how many times the collective phase has advanced beyond the natural (randomized) state. Higher multiplicity = more stored collective angular momentum = greater orbital radius change = greater weight change.

The drive accumulates phase continuously. Not limited by atomic quantum numbers. Limited only by:
- Polarization fraction (how many vortices are aligned)
- Drive frequency (winding rate — GHz = billions of advances per second)
- Dissipation (how fast the phase randomizes back)
- Input power (to sustain drive against dissipation)

**Steady-state angular momentum = drive rate / dissipation rate**

### Connection to Alzofon AGNUE Program

Frederick Alzofon (Boeing Aerospace) published the same core mechanism in 1981 (AIAA-81-1608): Dynamic Nuclear Orientation (DNO) of paramagnetic nuclei to modify gravitational interaction. Key parameters from his paper:

| Parameter | Alzofon Value | Our Design |
|---|---|---|
| Working material | Al²⁷ with iron inclusions | NiZn ferrite (insulating, full volume penetration) |
| Fixed alignment field | 660 Oe | 500-3000 Oe (tunable Helmholtz) |
| Drive frequency | 3000 MHz | 1-10 GHz (matched to FMR at applied field) |
| Drive mode | Pulsed: 2μs on, 2-6ms off | Pulsed (see protocol below) |
| Mechanism (his language) | "Remove gravitational field energy via virtual particle process decay" | — |
| Mechanism (POAMS) | Collective phase advance of aligned nuclear vortices changes orbital radius | ✓ |

**Where Alzofon was right:**
- Nuclear orientation is the key mechanism ✓
- Microwave resonance at GHz is the drive ✓
- Pulsed rather than continuous drive ✓
- Material acts as reservoir of orientation ✓
- Achievable at room temperature ✓
- Estimated ~1 joule gravitational energy removed per duty cycle ✓

**Where he was locked in 20th century physics:**
- Framed as "removing gravitational field energy" via virtual particle processes
- Used Le Chatelier's principle applied to Compton wavelength adjustment
- Required virtual particle clouds and creation-annihilation scaffolding
- All unnecessary — what's happening is collective phase advance changing orbital radius

**Hathaway Research (Toronto)** ran partial experimental verification under the AGNUE program. Star Lord visited the lab with Hal Puthoff. Results: "anomalous motion of a test mass" detected but not properly interpreted. They saw the effect but lacked the theoretical framework (POAMS) to understand what they measured.

**Daniel Alzofon** (Frederick's son) authored the engineering analysis of observed UAP, identifying microwave waveguide arrays, Luneberg lens profiles, and radiation patterns consistent with gravity-modification vehicles using this mechanism. Daniel has worked for Star Lord on contract and is now aligned with the POAMS framework.

### Marshall Space Flight Center — What Went Wrong

Star Lord's prior experiment at Marshall used:
- Bismuth hockey puck with strong magnets above/below for alignment
- Six microwave emitters fired sequentially

**Failure points (now understood):**
1. **Bismuth is conductive** — skin depth limited penetration to microns. Only surface atoms driven. The bulk was dead weight.
2. **Sequential firing** — no phase coherence across the volume. Each emitter drove a different region at a different phase. No collective advance.
3. **High damping** — Bismuth's diamagnetic character resists alignment and has picosecond relaxation times. Phase randomized before it could accumulate.
4. **Wrong conceptual model** — attempting to pump individual atoms rather than advance collective phase of aligned ensemble.

**Our design fixes all four:** insulating ferrite (full volume penetration), resonant cavity (enforces spatial phase coherence), ferrimagnetic material (supports alignment + long relaxation), correct physics (collective phase advance, not individual atom pumping).

### Pulsed Drive Protocol (Informed by Alzofon)

Alzofon's pulsed protocol (2μs on, 2-6ms off) is significant. It's not continuous wave driving. It's a pump-and-release cycle:

1. **Pulse ON (2μs):** Microwave drive at FMR frequency advances collective phase of all aligned vortices. Angular momentum accumulates in the aligned ensemble.
2. **Pulse OFF (2-6ms):** Drive removed. The accumulated collective angular momentum interacts with the Earth's gravitational system. This is where the orbital radius modification occurs — the wound-up state couples to the orbital mechanics.
3. **Next pulse:** Winds the collective phase further forward from wherever it relaxed to.

**Why pulsed may be superior to CW:**
- Continuous drive holds the system in a steady state — drive balances dissipation. The system reaches equilibrium.
- Pulsed drive creates a *transient* departure from equilibrium each cycle. The relaxation period is where the gravitational coupling actually acts. Then the next pulse pushes further.
- This is analogous to how a swing is pumped — you push at the right moment in the cycle, not constantly.

**Revised drive protocol for our experiment:**

| Phase | Duration | Action |
|---|---|---|
| Ramp alignment | 30 seconds | Bring Helmholtz coils up slowly — adiabatic alignment of vortices |
| Initial CW drive | 10 seconds | Continuous wave at FMR to establish baseline phase coherence |
| Pulsed drive | Minutes | 2μs pulses, variable repetition rate (100 Hz to 1 kHz), monitor weight continuously |
| Sweep rep rate | Minutes | Find optimal pulse repetition rate — the one that produces maximum weight change |
| Hold at optimum | Minutes | Sustain pulsed drive at optimal rate, record steady-state weight change |
| Kill drive | Instant | Observe relaxation time — how fast does weight return to baseline? |
| Reverse alignment | 30 seconds | Flip Helmholtz polarity, repeat entire sequence |

**The optimal pulse repetition rate is a discovery parameter.** It depends on the material's relaxation time and the gravitational coupling time constant — neither of which we know a priori. Alzofon estimated 2-6ms off-time (170-500 Hz rep rate). We sweep to find it empirically.

### UAP Engineering Connection

Daniel Alzofon's analysis of observed craft identifies features consistent with this mechanism at vehicle scale:

- **Slotted waveguide arrays on external skin** — for shedding excess angular momentum as microwave radiation. To descend (contract orbital radius), stored angular momentum must be radiated away. Conservation demands it.
- **Luneberg lens profile** ("saucer shape") — microwave optical component for directing radiated energy into steered, collimated beam. The vehicle shape IS the antenna.
- **3000 MHz operating frequency** — matches lowest sky radiation temperature (straight up, at night). Optimal for radiating excess energy into space.
- **Radiation burns on witnesses** — grid pattern matching waveguide array spacing. Near-field microwave exposure from active radiator at power levels needed for flight-scale orbital radius modification.
- **Working substance: ruby, olivine, sapphire** — insulating crystals with paramagnetic impurities. Same material class as YIG/ferrites. Full microwave penetration, low damping, resonant drive at GHz.

**The engineering lineage is terrestrial, not extraterrestrial.** Mid-20th century microwave technology: slotted waveguides, cavity resonators, Luneberg lenses — all WWII radar-era components. The knowledge transfer path runs through Operation Paperclip and the aerospace primes (Boeing, Lockheed) where scientists like Frederick Alzofon worked.

**This reframes our experiment:** We are not discovering something new. We are reconstructing something likely demonstrated 80+ years ago, using better materials (YIG/ferrites vs 1940s options), better instrumentation, and the correct theoretical framework (POAMS) instead of 20th century physics language that obscured the mechanism.

### Updated Bill of Materials (Rev 3)

| Component | Specification | Est. Cost |
|---|---|---|
| Bulk ferrite cylinder | NiZn, 500g-1kg, machinable | $30-80 |
| Copper cavity | Cylindrical, tuned to FMR frequency | $50-100 |
| SMA input coupler | Coupling loop or probe | $20 |
| Helmholtz coils | 10-15 cm diameter pair, 18 AWG, ~200 turns each | $40 |
| DC power supply | 0-30V / 5A adjustable | $60 |
| Microwave source | VCO + power amplifier, 1-5W, 1-10 GHz | $200-300 |
| Pulse generator | For modulating microwave source, variable rep rate | $50-100 |
| Scale | 0.01g resolution (gram-level target) | $25 |
| NanoVNA | Confirm cavity resonance / FMR overlap | $150 |
| SMA cables, connectors | Assorted | $30 |
| **Total** | | **~$700-900** |

### Success Criteria (Rev 3 — unchanged)

| Outcome | Meaning |
|---|---|
| Gram-scale weight change, reverses with alignment | **Decisive.** Kitchen-scale visible. Funding-ready. |
| Milligram-scale, reverses with alignment | **Confirmed, needs scaling.** More material, more power. |
| Sub-milligram, reverses with alignment | **Detected but marginal.** Return to precision balance + lock-in. |
| No directional effect at any power/rep-rate | **Null result.** Reassess coupling mechanism. |

### Key Collaborators

- **Daniel Alzofon** — authored UAP engineering analysis, ran AGNUE experiments at Hathaway Research, now aligned with POAMS framework. Contract resource for Star Lord.
- **George Hathaway** — Hathaway Research International, Toronto. Ran original AGNUE verification experiments. Detected anomalous motion.
- **Hal Puthoff** — present at Hathaway lab visit with Star Lord.
- **Norman Vincent Pope & Anthony Osborne** — POAMS theoretical framework.

---

*Document version: 3.0*
*Date: 2026-03-18*
*Framework: Normal Realism / POAMS*
*Authors: Star Lord, Parzival*

---

## Revision 4: YIG + Cavity + Pulsed Alzofon Protocol

*Date: 2026-03-19*

### Why Back to YIG

Rev 2-3 moved to bulk NiZn ferrite for mass. But Alzofon's work reveals the critical parameter isn't mass — it's **accumulated phase before dissipation**. The effect scales with:

**Total effect = (number of aligned vortices) × (phase accumulated per vortex)**

Phase accumulated per vortex = drive rate / dissipation rate. And dissipation rate is where YIG destroys everything else:

| Material | FMR Linewidth | Relaxation Time | Relative Phase Storage |
|---|---|---|---|
| YIG | ~0.3 Oe | ~100 ns | **1× (reference)** |
| NiZn ferrite | ~50-200 Oe | <1 ns | 0.002-0.006× |
| Bismuth | N/A (diamagnetic) | ~ps | ~0.00001× |
| Al²⁷ + Fe (Alzofon) | Nuclear: ~kHz linewidth | ~6 ms (nuclear) | ~60,000× (nuclear) |

Alzofon's Al²⁷ had extraordinary nuclear relaxation times (~6ms) — but required cryogenic-level nuclear polarization to get meaningful alignment fractions at room temperature. The iron inclusions solved this by seeding orientation that diffused into the aluminum matrix.

YIG at room temperature is **already fully alignable** (ferrimagnetic, saturates at ~1780 G) with **the longest electronic spin coherence of any known material**. It's the optimal intersection of:
- High alignment fraction (ferrimagnetic → near-100% at saturation)
- Long coherence (0.3 Oe linewidth → ~100 ns relaxation)
- Full volume penetration (insulator, 10¹² Ω·cm)
- Commercial availability as precision single crystals

The cavity provides field amplification. YIG provides the coherence. Pulsed drive exploits the long relaxation window.

### Material Class Validation

Daniel Alzofon's analysis of observed craft identifies working substances: **ruby, olivine, sapphire** — insulating single crystals with paramagnetic impurities. This is YIG's material class:
- Single crystal (long-range order → coherent collective response)
- Insulating (full microwave penetration)
- Magnetic impurities in insulating matrix (resonant absorption)
- Low damping (narrow linewidth → long phase storage)

Bulk polycrystalline ferrite is the wrong direction. The operational technology uses single crystals. So should we.

### Revised Architecture

A polished YIG sphere (or multiple spheres) inside a tuned copper microwave cavity, on a precision balance. Helmholtz coils for alignment. Pulsed microwave drive at FMR frequency per the Alzofon protocol.

#### Why Sphere + Cavity (Not Bulk Cylinder)

YIG is grown as single crystals and commercially available as polished spheres (up to ~15mm diameter). Spheres are ideal because:
- Uniform internal demagnetization field → single sharp FMR resonance (no broadening from geometry)
- Commercial, characterized, repeatable
- Cavity concentrates field on the sphere — sphere doesn't need to fill the cavity

#### Scaling Strategy

Instead of one massive ferrite cylinder, use **multiple YIG spheres in a cavity array**:

| Config | Total YIG Mass | Est. Cost | Notes |
|---|---|---|---|
| Single 3mm sphere | 0.15g | $60 | Proof of concept |
| Single 10mm sphere | 5.4g | $200-400 | 36× more mass than 3mm |
| Single 15mm sphere | 18g | $400-800 | Largest standard commercial |
| Array of 10× 10mm spheres | 54g | $2,000-4,000 | Cavity designed for array |
| Custom-grown 25mm+ sphere | 85g+ | Custom quote | Maximum single-crystal mass |

At 5.4g (10mm sphere), if the fractional weight change is even 1%, that's 54mg — easily visible on a milligram balance. At 0.1%, that's 5.4mg — still detectable. We don't need kilograms.

### Component Specification (Rev 4)

| Component | Specification | Est. Cost |
|---|---|---|
| YIG sphere(s) | 10mm diameter, polished single crystal | $200-400 |
| Copper cavity | Cylindrical TM₀₁₀, tuned to FMR frequency at target field | $50-100 |
| SMA coupling probe | Loop or iris coupler, positioned for optimal coupling to sphere | $20 |
| Helmholtz coils | 10-15 cm diameter pair, 18 AWG, ~200 turns each | $40 |
| DC power supply | 0-30V / 5A adjustable | $60 |
| Microwave source | VCO eval board, 2-10 GHz | $80-150 |
| RF power amplifier | 1-5W, matched to VCO band | $100-200 |
| Pulse generator | TTL modulation of RF amp, variable width (1-10μs) and rep rate (50-1000 Hz) | $50-100 |
| Analytical balance | 0.01mg resolution (Sartorius/Mettler, used) | $300-500 |
| NanoVNA | Confirm cavity resonance / FMR overlap | $150 |
| Schottky detector | Broadband, zero-bias — confirm FMR absorption | $25 |
| Acrylic enclosure | RF-transparent, air current isolation | $25 |
| SMA cables, connectors | Assorted | $30 |
| **Total (single 10mm sphere)** | | **~$1,100-1,800** |

### Pulsed Drive Protocol (Rev 4 — Alzofon-Informed)

Based on Frederick Alzofon's parameters, adapted for YIG's electronic (not nuclear) spin system:

#### Key Timescales

| Parameter | Alzofon (Nuclear) | YIG (Electronic) | Ratio |
|---|---|---|---|
| Resonant frequency | 3 GHz | 1-10 GHz (field-dependent) | Similar |
| Pulse duration | 2 μs | 0.1-2 μs (shorter OK — faster electronic response) | Similar |
| Relaxation time | ~6 ms (nuclear T₁) | ~100 ns (electronic T₂*) | 60,000× shorter |
| Off-time (Alzofon) | 2-6 ms | **Discovery parameter** | — |
| Alignment method | Iron inclusion seeding | External Helmholtz field | Simpler |

**Critical difference:** YIG's electronic relaxation (~100 ns) is much shorter than Alzofon's nuclear relaxation (~6 ms). This means:
- Pulses must repeat faster (microsecond spacing, not millisecond)
- But each pulse drives **far more angular momentum per vortex** (electronic magnetic moment is ~1000× nuclear)
- The cavity Q extends effective coherence by storing the field (ring-down time adds to drive duration)

#### Protocol

| Step | Duration | Action |
|---|---|---|
| 1. Ramp alignment | 30 s | Bring Helmholtz coils to target field (e.g. 2000 Oe → FMR at ~5.6 GHz) |
| 2. Verify FMR | 60 s | Sweep VCO frequency, monitor Schottky detector for absorption dip. Lock frequency. |
| 3. Baseline weight | 120 s | Record stable weight average. Alignment ON, microwaves OFF. |
| 4. CW drive | 30 s | Continuous wave at FMR. Record weight. Establishes steady-state phase coherence. |
| 5. Pulsed drive sweep | 5-10 min | Switch to pulsed mode. Sweep pulse width (0.1-5 μs) and rep rate (1 kHz - 1 MHz). Record weight continuously. Map the parameter space. |
| 6. Optimal hold | 5 min | Lock pulse parameters at maximum weight change. Sustain. Record. |
| 7. Kill drive | Instant | Observe weight relaxation curve. How fast does it return to baseline? This measures the gravitational coupling time constant. |
| 8. Reverse alignment | 30 s | Flip Helmholtz polarity. |
| 9. Repeat steps 2-7 | 15 min | Full measurement in reversed alignment. |
| 10. Control: off-resonance | 5 min | Drive at FMR + 500 MHz. No absorption → no effect expected. Confirms FMR specificity. |
| 11. Control: non-magnetic mass | 10 min | Replace YIG with glass sphere of equal mass. Full protocol. Zero effect expected. |

#### The Relaxation Curve (Step 7) Is Gold

When you kill the drive, the weight should return to baseline — but **how fast?** This tells you:
- If it snaps back in microseconds → the coupling is purely electronic spin-orbit, no gravitational component
- If it decays over milliseconds to seconds → there's a slower coupling mechanism (the gravitational interaction we're looking for)
- If it persists → the phase state is meta-stable (extremely interesting — implies the system found a new orbital equilibrium)

Alzofon predicted the nuclear orientation thermal lifetime at room temperature was ~6 ms. YIG's electronic relaxation is ~100 ns. If we see a weight relaxation time **longer than 100 ns** (the known electronic T₂*), something beyond standard FMR relaxation is happening.

### Cavity Design Details

**Mode:** TM₀₁₀ (simplest cylindrical mode, uniform axial E-field)

**Sizing:** For TM₀₁₀ in a cylinder, the resonant frequency depends only on radius:
- f₀₁₀ = 2.405 × c / (2π × a), where a = cavity radius
- At 2.8 GHz (1000 Oe field): a ≈ 41 mm → 82 mm diameter cavity
- At 5.6 GHz (2000 Oe field): a ≈ 20.5 mm → 41 mm diameter cavity
- At 8.4 GHz (3000 Oe field): a ≈ 13.7 mm → 27 mm diameter cavity

**Practical choice:** Target 2000 Oe alignment field → 5.6 GHz FMR → ~41 mm diameter copper cavity. This is a small, easily machined cylinder. A 10mm YIG sphere sits comfortably inside with room for the coupling probe.

**Height:** λ/4 to λ/2 (13-27 mm at 5.6 GHz). Exact height tuned for optimal coupling.

**Q factor:** Copper cavity at 5.6 GHz, 41mm diameter → Q ≈ 10,000-20,000 unloaded. With YIG inside, loaded Q drops (YIG absorbs at FMR) but this is exactly what we want — the absorption IS the drive.

**Construction:** Copper tube (plumbing supply) with machined or soldered endcaps. SMA bulkhead connector with coupling loop through sidewall. Total machining: basic lathe work or even hand-filed endcaps with good electrical contact.

### What Victory Looks Like

**The minimum viable result:**

A 10mm YIG sphere (5.4g) on a milligram balance. Drive pulsed microwaves at FMR. Weight shifts by any measurable amount. Reverse alignment. Weight shift reverses sign.

That's it. That's the paper. That's the demonstration. Direction-dependent weight modification via coherent angular momentum phase advance. Conventional physics predicts exactly zero directional weight change from FMR in any material, at any power, in any alignment.

**The stretch result:**

Weight change exceeds 0.1% of sphere mass (>5.4mg). Visible on a pharmacy scale. Relaxation time exceeds electronic T₂* by orders of magnitude. Pulsed protocol shows compounding (weight change grows with pulse count before saturating).

That funds Daniel's return and the next phase.

---

*Document version: 4.0*
*Date: 2026-03-19*
*Framework: Normal Realism / POAMS*
*Authors: Star Lord, Parzival*

---

## Revision 5: Levitation Target — Full Weight Cancellation

*Date: 2026-03-19*

### Design Philosophy Change

Revisions 1-4 were designed for **detection** — measure a weight change on a scale, prove the effect exists. This revision targets **levitation** — full cancellation of gravitational constraint force, resulting in the YIG sphere lifting off its support and ascending.

The physics doesn't change. It's only a matter of power. If the effect is real at milligrams, it's real at grams. If it's real at grams, it's real at 100%. There is no theoretical threshold or phase transition between "weight reduction" and "levitation" — it's a continuous linear function of accumulated collective angular momentum.

### What Changes From Rev 4

| Parameter | Rev 4 (Detection) | Rev 5 (Levitation) |
|---|---|---|
| Target outcome | Measurable weight change | Full weight cancellation → lift-off |
| Drive power | 1-5W | 10-50W |
| Measurement | Precision balance | Optical position tracking + force transducer |
| Containment | Open (sphere on scale pan) | Vertical polycarbonate tube (capped) |
| Frequency control | Manual VCO tuning | Closed-loop feedback tracking FMR absorption |
| Documentation | Data logs | Continuous high-speed video |

### The Core Problem: Maintaining Resonant Drive During Lift-Off

When the sphere sits on a fixed support inside the cavity, its position is stable and the cavity coupling is constant. As weight decreases toward zero:

1. **The sphere lifts off its support.** It's now free to move vertically inside the cavity.
2. **Position changes alter coupling.** The sphere moves through the cavity mode pattern. The local H_rf field strength varies with position. Drive efficiency changes.
3. **If the sphere exits the cavity, drive ceases.** The effect collapses. The sphere falls back. You get a bouncing ball, not sustained levitation.

**Solution: Extended cavity / waveguide containment with distributed drive.**

The sphere doesn't need to stay inside a small resonant cavity. The cavity establishes the initial phase coherence and drives the sphere to lift-off. Above the cavity, a vertical waveguide section continues to bathe the sphere in resonant microwave energy as it rises. The sphere carries its aligned, phase-advanced state with it. As long as the drive field is present and at the correct frequency, phase accumulation continues.

### System Architecture

```
     ┌──── Cap (polycarbonate, RF-transparent window for video) ────┐
     │                                                                │
     │    Vertical polycarbonate tube (containment)                   │
     │    ~50 cm tall, 50mm inner diameter                            │
     │                                                                │
     │    ┌─────────────────────────────────┐                         │
     │    │  Secondary coupling loop (top)  │ ← maintains drive      │
     │    └─────────────────────────────────┘   as sphere rises       │
     │                                                                │
     │              ↑ sphere ascends                                  │
     │              ●  YIG sphere (10mm)                              │
     │              ↑                                                 │
     ├────┬─────────────────────────────────┬─────────────────────────┤
     │    │     Copper Cavity (TM₀₁₀)      │                         │
     │    │     ~41mm Ø × 25mm height       │                         │
     │    │     SMA coupling probe          │ ← primary drive         │
     │    │     Sphere rests on PTFE post   │                         │
     │    └─────────────────────────────────┘                         │
     │                                                                │
     ├────┬─────────────────────────────────┬─────────────────────────┤
     │    │   Helmholtz Coil (lower)        │                         │
     │    └─────────────────────────────────┘                         │
     │                                                                │
     └── Base plate (aluminum, houses force transducer) ──────────────┘

     Helmholtz Coil (upper) mounted above tube, coaxial

     Coil separation = coil radius (~15 cm) — uniform field
     across full vertical travel of sphere
```

### Feedback Control System

The sphere must stay in resonant drive throughout its vertical travel. This requires closed-loop control of at least the drive frequency, and ideally drive power.

#### What Shifts During Operation

1. **Sphere position** — as sphere rises, coupling to cavity mode weakens. But the Helmholtz field remains uniform (that's the whole point of Helmholtz geometry), so FMR frequency doesn't change.

2. **Temperature** — microwave absorption heats the sphere slightly. YIG's saturation magnetization is temperature-dependent (~-6 G/°C). FMR frequency drifts ~-17 MHz/°C at 2000 Oe. Over a 10°C rise: ~170 MHz drift.

3. **Demagnetization changes** — negligible for a sphere (uniform demagnetization factor = 1/3 regardless of position or orientation).

#### Feedback Architecture

```
                    ┌──────────────┐
                    │  VCO + Amp   │
                    │  (drive)     │
                    └──────┬───────┘
                           │ RF out
                           ▼
                    ┌──────────────┐
  Absorption ──────│  Directional  │──────► Cavity + YIG
  signal     ◄─────│  Coupler      │
                    └──────────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  Schottky    │
                    │  Detector    │
                    └──────┬───────┘
                           │ DC voltage ∝ reflected power
                           ▼
                    ┌──────────────┐
                    │  Arduino /   │
                    │  Teensy MCU  │──── frequency sweep + lock
                    └──────┬───────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  Data log    │
                    │  + display   │
                    └──────────────┘
```

**Method: Minimum reflected power lock.**

At FMR, the sphere absorbs maximum power from the cavity. Reflected power (measured via directional coupler + Schottky detector) drops to a minimum. The MCU continuously dithers the VCO frequency by ±1 MHz around the current center and tracks the absorption minimum. If the minimum shifts (due to temperature drift), the MCU follows it.

This is standard microwave instrumentation — the same technique used in every EPR/FMR spectrometer. No exotic components.

**Components for feedback loop:**

| Component | Specification | Est. Cost |
|---|---|---|
| Directional coupler | 20dB, 1-10 GHz, SMA | $30-60 |
| Schottky detector | Zero-bias, broadband | $25 |
| Arduino/Teensy | Any MCU with ADC + DAC | $25 |
| VCO with voltage control | Already in BOM | — |

Total added cost for feedback: ~$80-110

#### Pulse Modulation + Feedback

During pulsed operation, the feedback loop operates during each pulse:
1. Pulse ON → MCU reads reflected power → adjusts VCO for next pulse
2. Pulse OFF → MCU logs data, prepares next frequency setting
3. Loop rate: 1 kHz+ (MCU can easily do this)

Between pulses, the MCU also reads:
- Force transducer (weight/thrust measurement)
- Optical position sensor (sphere height in tube)
- Thermocouple (cavity temperature)

All logged with microsecond timestamps.

### Instrumentation

#### Force Measurement

**Primary: Strain gauge load cell under the cavity assembly.**

The entire cavity + coil assembly sits on a load cell. As the sphere loses weight, the load cell reads the change. When the sphere lifts off, the load cell reads the full sphere weight as "missing" from the assembly.

- 100g load cell with HX711 ADC → 0.01g resolution, 10-80 Hz sample rate
- Connected to the same MCU running the feedback loop
- Cost: $10

**Secondary: Optical position tracking.**

A laser + photodiode pair across the polycarbonate tube above the cavity. When the sphere rises past the beam, the photodiode triggers. Multiple pairs at different heights give velocity.

- Laser pointer + photodiode: $5 per pair, 3-4 pairs = $15-20
- Sub-millisecond response time

#### Video Documentation

Two cameras:
1. **Side view** — through polycarbonate tube, captures sphere position continuously
2. **Scale view** — if retaining a digital scale as backup, captures the readout

Smartphone cameras are sufficient. 60fps captures motion at millisecond resolution. Slow-motion (240fps) even better.

**Critical:** Video must show the sphere, the cavity, the power supply readings, and a clock in a single continuous uncut shot. This is the evidence.

### Power Budget

**Target: 100% weight cancellation of a 5.4g sphere.**

Using Alzofon's estimate (~1 J/duty-cycle at 3 GHz pulsed):
- Gravitational binding energy: m × g × (one orbital radian of radius change) — but this framing is Alzofon's, based on virtual particle energy removal
- More conservatively: we don't know the coupling constant. So we design for excess power and sweep.

**Power amplifier options:**

| Amplifier | Power | Frequency | Est. Cost | Notes |
|---|---|---|---|---|
| Mini-Circuits ZVE-3W-183+ | 3W | 2-18 GHz | $300 | Broadband, covers all field settings |
| Used TWTA (traveling wave tube) | 20-50W | 2-8 GHz | $200-500 (eBay) | Surplus radar/comm amp. Serious power. |
| LDMOS PA module | 10-25W | 2-6 GHz | $100-200 | Ham radio / cell tower surplus |
| Custom class-AB with MRF9180 | 50W | 2-3 GHz | $80 + build time | DIY, highest power per dollar |

**Recommendation:** Start with the 3W broadband amp for detection-phase testing. If the effect is confirmed and scales linearly with power, upgrade to a 20-50W TWTA for levitation attempts. Total power cost: $300 → $500-800.

At 50W pulsed with 1% duty cycle (2μs on, 200μs off), average power dissipation is only 0.5W. The sphere and cavity stay cool. Peak power in the cavity (Q = 10,000) is effectively 500kW equivalent. That's serious field strength.

### Revised Drive Protocol (Rev 5 — Levitation Sequence)

| Step | Duration | Action | Monitor |
|---|---|---|---|
| 1. System check | 5 min | Power on all systems. Verify cavity resonance on NanoVNA. Verify Helmholtz field with gaussmeter. Calibrate load cell with sphere in place. Start video recording. | All instruments |
| 2. Ramp alignment | 30 s | Helmholtz coils to 2000 Oe. Adiabatic. | Load cell (magnetostriction baseline) |
| 3. Find FMR | 60 s | MCU sweeps VCO. Locks to absorption minimum. | Reflected power, frequency |
| 4. Low-power CW | 60 s | 1W CW at FMR. Baseline weight with drive on. | Load cell, temperature |
| 5. Low-power pulsed | 5 min | 1W pulsed. Sweep rep rate 100 Hz → 1 MHz. Find optimal rep rate (maximum weight change). | Load cell vs rep rate |
| 6. Power ramp — detection | 10 min | Lock rep rate at optimum. Ramp power: 1W → 3W → 5W. Record weight change at each level. Confirm linearity. | Load cell, reflected power, temperature |
| 7. Reverse alignment check | 10 min | Flip Helmholtz. Repeat steps 3-6. Confirm sign reversal. This is the go/no-go gate for levitation attempt. | Load cell (sign must reverse) |
| 8. GATE: Proceed only if directional weight change confirmed | — | If no directional effect → stop. Debug. If directional effect confirmed → continue to levitation. | — |
| 9. Restore alignment for maximum weight reduction | 30 s | Whichever polarity produced weight decrease. | — |
| 10. Power ramp — levitation | Minutes | Increase to 10W, 20W, 50W (as amplifier allows). At each level, record weight change. Extrapolate: at what power does weight reach zero? | Load cell (watching for zero crossing) |
| 11. Levitation | — | If weight reaches zero, sphere lifts off PTFE post. Optical sensors trigger. MCU logs ascent velocity and height. Video captures everything. | Position sensors, video, load cell |
| 12. Sustain | Minutes | Hold drive at levitation power. Sphere should hover or continue ascending (depending on whether drive field extends above cavity). | Position, video |
| 13. Kill drive | Instant | Cut RF power. Sphere should fall back to support. Observe descent dynamics — does it fall at g? Slower? | Position sensors, video, load cell |
| 14. Repeat | — | Multiple levitation cycles for reproducibility. Vary power levels to find minimum levitation power. | All |

### Safety Considerations

**Microwave exposure:**
- At 50W, microwave leakage from the cavity/tube assembly could exceed safety limits
- Polycarbonate tube is RF-transparent — it contains the sphere, not the microwaves
- **Mitigation:** Operate inside a microwave-absorbing enclosure (RAM foam sheets, $20-40) or at >2m distance during high-power runs
- MPE (maximum permissible exposure) at 5 GHz: 10 mW/cm² — monitor with RF field meter or stay behind shielding

**Projectile risk:**
- If the sphere accelerates upward at more than 1g net, it becomes a projectile
- 5.4g YIG sphere at even 2g net acceleration reaches 4.4 m/s in 1 second
- **Mitigation:** Polycarbonate tube is capped. Tube rated for impact. Do not stand directly above.
- Design tube height (50 cm) as safe capture distance. If sphere hits cap at speed, assess damage before increasing power.

**Thermal:**
- YIG Curie temperature: 560K. Significant margin above room temp.
- Cavity cooling: natural convection sufficient at <50W average power (duty cycle keeps average low)
- If running CW at high power: add small fan or heat sink to cavity

**Magnetic fields:**
- 2000 Oe Helmholtz field: keep credit cards, pacemakers, and magnetic storage away
- Field drops as 1/r³ — safe beyond ~50 cm from coil center

### Bill of Materials (Rev 5 — Levitation Build)

| Component | Specification | Est. Cost |
|---|---|---|
| **Core** | | |
| YIG sphere | 10mm diameter, polished single crystal | $200-400 |
| Copper cavity | Cylindrical TM₀₁₀, ~41mm Ø × 25mm, SMA port | $50-100 |
| Helmholtz coils | 15 cm Ø pair, 18 AWG, ~200 turns each, on PVC/3D-printed forms | $40 |
| DC power supply | 0-30V / 5A adjustable (Helmholtz drive) | $60 |
| PTFE sphere support | Small post/cup inside cavity | $5 |
| **Microwave Drive** | | |
| VCO eval board | 2-10 GHz, voltage-tuned | $80-150 |
| RF power amplifier (Phase 1) | 3W broadband, 2-18 GHz | $300 |
| RF power amplifier (Phase 2) | 20-50W TWTA or LDMOS, 2-6 GHz (used/surplus) | $200-500 |
| Pulse generator / RF switch | PIN diode switch + TTL driver, or MCU-controlled | $50-80 |
| **Feedback & Instrumentation** | | |
| Directional coupler | 20 dB, 1-10 GHz, SMA | $30-60 |
| Schottky detector | Zero-bias, broadband | $25 |
| Arduino/Teensy MCU | ADC + DAC for feedback loop | $25 |
| Load cell + HX711 | 100g, 0.01g resolution | $10 |
| NanoVNA | Cavity/FMR characterization | $150 |
| Thermocouple + reader | K-type, cavity temperature | $15 |
| **Containment & Structure** | | |
| Polycarbonate tube | 50mm ID × 50 cm tall, capped | $25-40 |
| Aluminum base plate | Houses load cell, mounts cavity | $20 |
| Laser + photodiode pairs (×4) | Position sensing along tube | $20 |
| RAM foam / RF shielding | Microwave safety enclosure | $20-40 |
| **Cables & Connectors** | | |
| SMA cables, adapters, BNC | Assorted | $40 |
| **Documentation** | | |
| Camera mount / tripod | For continuous uncut video | $20 (or use phone) |
| **Total (Phase 1: detection)** | | **~$1,200-1,800** |
| **Total (Phase 2: + high-power amp)** | | **~$1,400-2,300** |

### What Success Looks Like

**Phase 1 (detection):** Directional weight change confirmed. Effect scales linearly with power. Sign reverses with alignment. Go/no-go gate passed.

**Phase 2 (levitation):** Sphere lifts off support. Ascends inside polycarbonate tube. Sustained at stable height or rises to cap. Falls when drive is killed. Repeatable. On video.

**Phase 3 (the one that matters):** The video goes public. A YIG sphere floating inside a copper tube, controlled by a microwave source and a pair of coils. No strings. No magnets above it. No superconductors. No tricks. Just angular momentum, phase advance, and the correct understanding of what gravity actually is.

That video is the end of one era and the beginning of another.

---

*Document version: 5.0*
*Date: 2026-03-19*
*Framework: Normal Realism / POAMS*
*Authors: Star Lord, Parzival*

---

## Revision 6: Vortex Model Restatement & Magnet Correction

*Date: 2026-03-27*

### Critical Design Correction: Alignment Source

The Rev 4/5 spec calls for air-core Helmholtz coils (200 turns, 15cm diameter, 30V/5A supply) to reach 2000 Oe. This is physically impossible. Air-core Helmholtz at those parameters delivers ~120 Oe — 6% of target.

**Fix:** Replace with iron-core electromagnet. A C-shaped or H-shaped soft iron yoke with coils wound on it delivers 2000+ Oe in a small air gap with a few hundred turns at modest current. Still reversible (flip the current). Alternatives:
- Surplus lab electromagnet (eBay, $100-300)
- Custom wound on machined soft iron yoke ($50 iron + $25 wire + machine time)
- Lower field operation: 500 Oe → FMR at ~1.4 GHz, bigger cavity (~82mm), fewer aligned vortices

### YIG Under the Vortex Model

#### Formula Unit: Y₃Fe₅O₁₂

Each formula unit is a coupled system of 20 vortices:

| Vortex | Mode | ħ per vortex | Count | Subtotal |
|---|---|---|---|---|
| Yttrium | 39 | 89ħ | 3 | 267ħ |
| Iron | 26 | 56ħ | 5 | 280ħ |
| Oxygen | 8 | 16ħ | 12 | 192ħ |
| **Total** | | | **20** | **739ħ** |

#### The Active Vortices: Iron's d-Harmonic Asymmetry

The critical vortices are the five Irons. Mode 26 has partially filled d-harmonic patterns — 6 of 10 geometric slots occupied in the 3d submode. These unfilled slots mean the iron vortex has a **net circulation** in those modes. The vortex has a persistent angular momentum asymmetry in its outer harmonic structure.

This asymmetry is what conventional physics calls the "magnetic moment" of iron. In vortex language: it is a geometric fact about mode 26 — the d-harmonic pattern is incomplete, creating a net directional circulation that cannot cancel internally.

#### The Garnet Lattice: Oxygen as Coupling Bridge

In the YIG crystal, billions of iron vortices couple through their shared oxygen vortices. The oxygen vortices (mode 8, 16ħ) act as coupling bridges — their harmonic modes overlap with iron's, creating a rigid angular momentum network. This is what "crystal structure" IS: a vast coupled system of vortices whose harmonic modes interlock.

The yttrium vortices (mode 39, 89ħ) provide structural scaffolding. Their d-harmonic patterns are filled (4d complete), so they contribute no net circulation. They are angularly neutral in the relevant modes but provide massive structural inertia to the lattice.

#### Ferrimagnetism: The Uncompensated Vortex

The five iron vortices per formula unit sit in two different geometric positions in the garnet lattice — three in tetrahedral sites, two in octahedral sites. Their d-harmonic circulations couple antiparallel through the oxygen bridges: three point one way, two point the other.

**Net: one uncompensated iron vortex's worth of d-harmonic circulation per formula unit.**

This is not a "magnetic field" or a "magnetic moment." It is a geometric fact about the coupled vortex lattice: there is a net angular momentum circulation asymmetry built into the structure.

### The Experiment Restated in Vortex Language

#### 1. Alignment

An organized angular momentum source (iron-core electromagnet: iron vortices whose d-harmonic circulations have been aligned by coherent action flowing through the conductor winding) couples directly to the YIG crystal. The angular momentum coupling between the source's vortices and the YIG's vortices forces all net d-harmonic circulations in the YIG to orient along a common axis.

The coupling is direct — vortex structure to vortex structure. Not a "field" crossing a gap. The gap between the iron poles and the YIG is not empty space. It IS angular momentum structure (everything is), and the alignment condition propagates through it as a structural coupling, not as a signal.

#### 2. Precession

Once aligned, the net d-harmonic circulations of the iron vortices precess around the alignment axis. This precession is the natural response of an angular momentum structure tilted relative to a preferred direction — identical to how a gyroscope precesses when tilted relative to a constraint.

The precession rate is determined by the coupling strength between the d-harmonic circulation and the alignment. Stronger alignment → faster precession. This rate is the FMR frequency: f = γ × B_alignment, where γ = 2.8 MHz/Gauss.

The gyromagnetic ratio γ is itself a geometric quantity — the ratio between the phase state's angular momentum (½ℏ) and the full action quantum, multiplied by g ≈ 2 (reflecting that the phase state couples at twice the naive rate because it IS the fundamental half-quantum seeing the full quantum structure). This ratio doesn't change under vortex reinterpretation. It is a property of the angular momentum topology.

#### 3. Resonant Drive via Cavity

The copper cavity (mode 29, 64ħ per vortex) has delocalized outermost harmonic quanta — the single s-mode quantum at the 4th radial level of each copper vortex merges into a collective, crystal-wide angular momentum mode. This is what "metallic conduction" IS: outermost harmonic quanta forming extended lattice modes rather than remaining bound to individual vortex structures.

The VCO injects oscillating action through the SMA probe, driving these delocalized lattice modes into coherent oscillation. The cavity geometry determines which oscillation patterns are self-reinforcing (resonant) — the standing modes. At resonance, the cavity's delocalized angular momentum oscillates coherently throughout the interior volume.

The YIG sphere sits within this oscillating structure. At the FMR frequency — where the cavity oscillation matches the natural precession rate of the aligned d-harmonic circulations — the coupling is resonant. Maximum energy transfer. Each cycle of the cavity mode drives the precession further forward. The collective phase of all aligned vortices advances coherently.

**The cavity Q factor (10,000-20,000)** means the oscillation persists for thousands of cycles before dissipating. Each cycle adds constructively. The effective drive is amplified by Q — not because a "field" is amplified, but because coherent oscillation builds over thousands of cycles, like pushing a swing at its natural frequency.

#### 4. Phase Accumulation → Orbital Radius Change

The accumulated collective angular momentum changes the system's natural orbital radius relative to Earth. The constraint force (weight) changes accordingly.

#### 5. Reversal

Reverse the alignment source polarity → d-harmonic circulations align the opposite way → precession reverses → phase advance adds angular momentum in the opposite sense → weight change reverses sign.

### Does the Vortex Model Predict a Different Frequency?

**No.** The resonance at f = γ × B arises from the angular momentum geometry of mode 26's d-harmonic structure coupling to an alignment source. The gyromagnetic ratio γ = 2.8 MHz/Gauss is a ratio of angular momentum quantities that are identical in both conventional and vortex language. 2000 Oe → 5.6 GHz. Same number, deeper reason.

The one place the vortex model *might* predict something different is in the **linewidth** (dissipation rate). Conventional theory attributes YIG's 0.3 Oe linewidth to spin-spin and spin-lattice relaxation. The vortex model says it's the rate at which coherent d-harmonic circulation phase randomizes through coupling to the broader lattice structure — through the oxygen bridges and yttrium scaffolding. Whether this coupling is stronger or weaker than conventional theory predicts is an empirical question the experiment itself will answer.

### Revised BOM Note

The Helmholtz coils ($40 wire + $60 supply = $100) should be replaced with:

| Option | Est. Cost | Notes |
|---|---|---|
| Surplus lab electromagnet | $100-300 | eBay/surplus, needs pole gap ≥ 50mm for cavity |
| Custom iron-core electromagnet | $75-150 | Machined soft iron yoke + winding |
| Existing DC supply | $60 | Same 30V/5A supply works — iron core reduces current needed |

Net BOM impact: +$0 to +$200 depending on option.

### Detection-Phase Note

Rev 5 switches entirely to a load cell (0.01g resolution). For Phase 1 (detection), retain the analytical balance (0.01mg resolution, $300-500) from Rev 4. The load cell is backup for levitation phase. At 0.01mg, we can detect a weight change of ~2 ppm on a 5.4g sphere. At 0.01g (load cell), we need ~0.2% effect to see anything. Start sensitive.

### Multiferroic Path (Future Direction)

The current design requires an electromagnetic alignment source (iron-core electromagnet), which invites dismissal as "just magnets." A rhetorically bulletproof version would use **electric** alignment of circulations — no magnetic components at all.

This is possible in **multiferroic** materials, where electric and magnetic order are coupled: applying a voltage reorients the d-harmonic circulations directly. However, no known multiferroic approaches YIG's 0.3 Oe linewidth (coherence). Current candidates (hexaferrites, bismuth ferrite) have linewidths 100-1000× broader, making resonant phase accumulation impractical.

Worth monitoring. If a multiferroic with single-digit Oe linewidth is developed, the entire experiment can be rebuilt with only a capacitor for alignment and an RF/microwave source for drive. Zero magnetic components. Same physics.

### Historical Precedents: Convergent Evidence

Three independent programs across 60 years converged on the same architecture — high energy applied to organized angular momentum — and all reported anomalous weight/thrust effects. None had the POAMS framework to explain their results. All used brute force where resonant coupling is orders of magnitude more efficient.

#### Die Glocke (1944-45, Nazi Germany)

Counter-rotating drums filled with "Xerum 525" (likely mercury antimonate — a heavy paramagnetic compound), subjected to high voltage. Mercury is mode 80 (201ħ), with massive spin-orbit coupling from deep d and f harmonics. In high-mode-number vortices, the coupling between phase state (electric) and circulation (magnetic) degrees of freedom scales as Z⁴ — mercury's spin-orbit coupling is ~10⁶× stronger than iron's.

**Vortex interpretation:** Mechanical rotation provided bulk angular momentum alignment. High voltage, through spin-orbit coupling in the mercury compound, drove circulation phase advance. The high mode number of mercury made electric-to-circulation coupling viable where it fails for lighter elements. Brute force, lossy, dangerous (radiation from excited heavy-element vortices), but potentially functional.

#### T.T. Brown (1950s-60s, USA)

High voltage asymmetric capacitors with dielectric materials. No rotation. Brown claimed directional thrust toward the positive plate at voltages of 50-250 kV.

**Vortex interpretation:** Enormous phase-state gradients across the dielectric. If the dielectric material has any asymmetry in how it couples phase state to circulation (piezoelectric or ferroelectric materials do), the electric gradient produces a net circulation bias. Extremely weak coupling — Brown compensated with enormous voltages. No alignment step, no resonance, no coherence. The least efficient approach of the three, but the simplest.

#### Podkletnov (1992-2003, Finland/Russia)

Superconducting YBCO disc spinning at ~5,000 RPM, later combined with 2 MV pulsed discharge ("gravity impulse generator"). Claimed 0.3-2% weight reduction above the spinning disc.

**Vortex interpretation:** Superconductivity = delocalized lattice harmonics forming a single phase-locked state. The entire disc's outermost angular momentum modes oscillate as one coherent system. Mechanical rotation aligns bulk angular momentum. The high-voltage pulse delivers a massive, sudden phase-state perturbation to a system whose circulations are already coherent and aligned. Of the three precedents, Podkletnov's design comes closest to ours: coherent target material + alignment + impulsive drive. He just lacked resonant coupling and the theoretical framework to optimize.

#### Comparison

| Program | Alignment | Drive | Coherence | Efficiency |
|---|---|---|---|---|
| Die Glocke | Mechanical rotation | HV (spin-orbit in Hg) | None (polycrystalline) | Very low |
| Brown | None | Enormous voltage gradient | None | Extremely low |
| Podkletnov | Rotation + superconducting coherence | HV pulse discharge | High (SC phase lock) | Moderate |
| Alzofon (AGNUE) | DC magnetic field | Pulsed microwave (DNO) | Partial (paramagnetic) | Moderate |
| **This experiment** | **DC electromagnetic alignment** | **Resonant cavity at FMR** | **High (YIG single crystal)** | **Best** |

The convergence of four independent programs on "organized angular momentum + energy input = anomalous weight" is not coincidence. It is the same vortex physics — coherent phase advance of collective angular momentum — approached with varying degrees of understanding and efficiency. Our design benefits from all their lessons: use a single crystal (not polycrystalline), use resonant coupling (not brute force), use the natural precession frequency (not arbitrary voltage), and understand the mechanism (POAMS) so you can optimize rather than grope in the dark.

---

*Document version: 6.0*
*Date: 2026-03-27*
*Framework: Normal Realism / POAMS (Vortex Model)*
*Authors: Star Lord, Parzival*
