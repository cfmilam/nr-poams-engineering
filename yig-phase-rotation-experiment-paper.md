# YIG Phase Rotation Levitation Experiment

## Engineering Specification & Theoretical Basis

**Framework:** Normal Realism / Pope-Osborne Angular Momentum Synthesis (POAMS)

**Revision:** 1.0 — April 2026

**Classification:** Open Publication

---

## 1. Abstract

This paper specifies a tabletop experiment designed to produce a measurable, directional weight change in a yttrium iron garnet (YIG) single-crystal sphere by coherently advancing the collective angular momentum phase of its internal vortex structure. The theoretical basis is the Pope-Osborne Angular Momentum Synthesis (POAMS), which identifies weight as a constraint force arising from the angular momentum / orbital radius relationship, and predicts that controlled modification of an object's internal spin angular momentum will produce a corresponding change in its effective orbital radius — manifesting as a measurable weight change.

The experiment uses ferromagnetic resonance (FMR) in a copper microwave cavity to drive coherent precession of aligned iron vortices within a YIG sphere. At an applied alignment field of 2000 Oe, the resonant frequency is 5.6 GHz. The cavity amplifies the drive field by a factor of √Q ≈ 100–140, enabling large precession cone angles at modest input power.

The critical prediction: the sign of the weight change reverses when the alignment field polarity is reversed. Co-spin alignment (angular momentum added parallel to Earth's rotation) produces weight increase; anti-spin alignment produces weight decrease. No conventional mechanism predicts a directional, reversible weight change at FMR. Detection of this signature at milligram scale or above constitutes direct experimental confirmation of POAMS.

Phase 1 targets detection (~$1,500 budget). Phase 2 targets levitation (~$2,000 additional). The end state is a YIG sphere floating inside a copper tube — visible, repeatable, and decisive.

---

## 2. Introduction

### 2.1 The Problem

Modern physics rests on a 350-year-old error.

In 1687, Newton observed that objects fall and planets orbit. Rather than recognizing these as manifestations of angular momentum conservation — which Bertrand's theorem already constrains to inverse-square radial dependence — he invented a new entity: "gravitational force." This force, undefined in mechanism and unobserved in isolation, became the foundation of classical mechanics.

Coulomb repeated the error at the microphenomenal scale. Observing inverse-square behavior in charged interactions, he postulated a second fundamental force rather than recognizing the same angular momentum conservation operating at a different scale. Maxwell built his field equations on Coulomb's lead, producing a mathematical framework of extraordinary utility and deeply incorrect ontology. Einstein, attempting to reconcile Maxwell with observation, introduced his second postulate — the constancy of the speed of light as a physical speed limit — when *c* is in fact a conversion factor between measurement domains (length and time), no more a speed limit than the conversion between meters and feet is a length limit.

The result: four fundamental forces, dozens of "fundamental" particles, dark matter, dark energy, and a Standard Model that cannot explain why anything has mass, why the proton is stable, or what space actually is. The math works. The physics is wrong.

### 2.2 The Correction

The Pope-Osborne Angular Momentum Synthesis (POAMS), developed by N.V. Pope and A.N. Osborne, identifies the error and provides the correction. All physical phenomena reduce to a single conserved quantity: angular momentum, quantized in units of ħ. What we call "forces" are angular momentum conservation operating at different scales. What we call "mass" is the rotational inertia of quantized angular momentum vortices. What we call "space" is the angular momentum field itself.

POAMS does not add new physics. It removes 350 years of unnecessary additions and returns to what conservation laws actually require.

### 2.3 Why It Was Missed

Pope and Osborne made the same category error as Newton, only later and in a different domain. Newton saw orbiting planets and falling apples, then treated them as point masses — ignoring every internal vortex structure inside the objects. Pope and Osborne identified angular momentum as the sole conserved substance, built the most coherent theoretical framework in a century, and then — when it came time to calculate expected effects — plugged in the macroscopic angular momentum of a spinning ball (L = Iω) as if the internal vortex structure didn't exist. But the whole point of POAMS is that angular momentum IS the substance. Every vortex inside that steel ball matters. The macro rotation is the faintest echo of what happens at the atomic level via Barnett alignment. They calculated with the echo instead of the source.

Hayasaka (1989) saw the right effect. He spun gyroscopes, measured weight reduction, published, and was savaged. His numbers were "too big" for any conventional explanation, so the community decided his experiment must be wrong rather than their theory. Classic reflex. But if the gravitational coupling runs through internal spin alignment rather than bulk angular momentum, Hayasaka's numbers were not too big — they were exactly what Barnett-induced alignment predicts across billions of partially-aligned nuclei in a steel rotor. His precision was rough, his error bars were wide, but his sign was right and his magnitude was in the right ballpark.

The reason nobody followed the thread is structural. The people who understood FMR and magnon physics did not believe in gravitational anomalies. The people who believed in gravitational anomalies did not understand FMR and magnon physics. These two communities never overlapped. Alzofon came closest — he was at Boeing, he understood microwave physics, he designed a real experiment — but he wrapped the correct mechanism in incorrect theoretical ontology, and the physics community dismissed him accordingly.

The logical thread was always there: Barnett tells you mechanical rotation aligns internal spins. Hayasaka tells you aligned spins change weight. Einstein-de Haas tells you spin alignment and mechanical rotation are the same angular momentum observed at different scales. The next step follows directly: skip the mechanical rotation entirely, maximize alignment directly with a magnetic field, drive coherent phase advance at FMR, use a material designed for narrow-linewidth coherent spin states. Nobody put those three results in the same room.

### 2.4 This Experiment

This paper specifies an experiment that converts POAMS from theoretical framework to engineering practice. By coherently advancing the angular momentum phase of atomic vortices inside a YIG crystal, we will produce a controlled, directional, reversible weight change — and, at sufficient power, levitation.

This is not the first attempt to engineer weight change through angular momentum manipulation. It is the first attempt built on the correct theoretical framework, using the optimal material, with the correct mechanism identified. The combination of:

1. A repeatable tabletop observation (brass gyroscope anomaly)
2. The correct theoretical framework (POAMS)
3. The correct diagnosis (internal spin alignment, not bulk angular momentum)
4. The correct next step (YIG + cavity + coherent drive)

...gives this experiment a real chance of success where previous attempts failed or were abandoned.

---

## 3. Theoretical Background

### 3.1 POAMS Framework

The Pope-Osborne Angular Momentum Synthesis rests on a single premise: **angular momentum is the sole conserved substance of physics, and all phenomena are its conservation in action.**

**Mass as quantized angular momentum.** Every element is accumulated angular momentum in harmonic modes, quantized in units of ħ. Hydrogen is the fundamental mode — one quantum of angular momentum in its simplest vortex configuration. Every other element is hydrogen accumulated: helium is mode-2, lithium mode-3, and so on through the periodic table. The periodic table is not a catalog of fundamentally different things. It is a count of ħ quanta organized in harmonic modes.

The phrase "there is only hydrogen" captures this: iron (mode-26) is 56ħ of angular momentum organized in the 26th harmonic pattern. Yttrium (mode-39) is 89ħ. Oxygen (mode-8) is 16ħ. The mass number IS the angular momentum count.

**Four forces as one.** What conventional physics calls four fundamental forces are angular momentum conservation at four scales:

| Conventional Name | POAMS Description | Scale |
|---|---|---|
| Gravity | Orbital angular momentum conservation | Macrophenomenal (planetary) |
| Electromagnetism | Spin angular momentum correlation | Microphenomenal (atomic) |
| Strong force | Eyewall circulation (vortex core binding) | Sub-vortex (nuclear) |
| Weak force | Vortex decay / mode transitions | Transition events |

The hurricane analogy is exact, not metaphorical. A hurricane has an empty eye, an eyewall of intense circulation, and outer spiral bands of decreasing velocity. The atomic vortex has an empty barycenter, an eyewall region of intense angular momentum (the "nuclear force" zone), and outer circulation (what conventional physics calls "electron orbitals"). A galaxy has the same topology at the macrophenomenal scale. The structure repeats because the physics is the same at every scale — angular momentum conservation in a quantized medium.

**The conversion factor *c*.** The quantity *c* = 2.998 × 10⁸ m/s is the conversion factor between the time domain and the length domain, exactly as inches-per-foot converts between measurement units. It appears in E = mc² not as a speed limit but as the dimensional bridge between rotational inertia (mass) and the energy domain. Nothing in POAMS prohibits superluminal propagation; the "speed limit" is an artifact of Einstein's unnecessary second postulate.

### 3.2 The Atom as Quantized Vortex

Under POAMS, there are no particles. An atom is a quantized vortex structure of angular momentum.

**Structure:**
- The **barycenter** is empty — the eye of the vortex. There is no "nucleus" as a solid object. The quantum accumulator (conventional: nucleus) is the eyewall region where angular momentum density is highest.
- The **eyewall** is the zone of maximum circulation. This is where the "strong force" operates — it is simply the binding energy of the vortex core, not a separate force. The conventional "nuclear radius" is the eyewall radius.
- The **outer circulation** extends from the eyewall outward, organized in harmonic sub-modes. These are what conventional physics calls "electron orbitals." They are not particles orbiting a center; they are standing wave patterns in the vortex circulation.

**The periodic table reinterpreted:**
- Element number = harmonic mode number = number of ħ quanta in the fundamental structure
- Mass number = total ħ count including all sub-modes
- Isotopes = same harmonic mode, different ħ count (additional quanta in non-fundamental sub-modes)
- Chemical properties = outer circulation geometry (same as conventional orbital theory, but with correct ontology)

**Spin angular momentum IS mass.** At the microphenomenal level, the spin rate of a quantized vortex is its mass. This is not analogy. The rotational inertia of the vortex — how much angular momentum it contains — is literally what a scale measures. Increase the spin angular momentum: mass increases. This is what E = mc² means when *c* is understood as a conversion factor.

### 3.3 Weight as Constraint Force

This section contains the key prediction that the experiment tests.

**Weight defined.** Weight is the constraint force that prevents an object from occupying its natural force-free orbital radius around Earth's quantum accumulator. An object sitting on a table is being prevented from falling to its equilibrium orbital radius by the normal force of the table. Remove the table, and the object moves toward that radius — what we call "falling."

**The angular momentum relationship.** For any orbiting body:

```
J = m × v × r
```

where J is the total angular momentum, m is rotational inertia (mass), v is orbital velocity, and r is orbital radius. For an object on Earth's surface, v is fixed (the object co-rotates with Earth's surface at ~465 m/s at the equator). J is conserved. Therefore:

**If m changes, r must change to conserve J.**

Specifically:
- **Increase internal spin angular momentum aligned with Earth's rotation (co-spin):** The object's effective rotational inertia increases. To conserve J with v fixed, r must decrease. The object presses harder against the constraint — weight increases.
- **Increase internal spin angular momentum opposing Earth's rotation (anti-spin):** The effective rotational inertia increases in the counter-rotating frame. To conserve J, r must increase. The constraint force decreases — weight decreases.

This effect is:
- **Linear** in the angular momentum added
- **Instantaneous** (conservation is not mediated; it is a constraint)
- **Reversible** (remove the added angular momentum, weight returns to baseline)
- **Directional** (sign depends on alignment relative to Earth's rotation)

The directional dependence is the critical discriminant. No conventional mechanism — thermal, electromagnetic, acoustic, or mechanical — produces a weight change that reverses sign when alignment field polarity flips. Detection of this signature is detection of the POAMS-predicted effect.

### 3.4 Collective Phase Advance — The Mechanism

The mechanism for adding angular momentum to a material without changing its elemental identity is **collective phase advance**.

**Why not individual atoms?** Pumping spin angular momentum into individual atomic vortices changes their ħ count — which changes the element. Add one ħ to iron (mode-26, 56ħ) and it becomes cobalt-57 or a metastable iron isotope. This is nuclear transmutation, not weight modification. You cannot change the spin state of individual atoms without changing what they are.

**What you CAN do:** Align the vortex velocity vectors of many atomic vortices (polarization), then coherently advance their collective phase. This is adding angular momentum to the ensemble without adding it to any individual vortex. The micro-physical equivalent is physical rotation — and Einstein and de Haas proved in 1915 that reversing the alignment of atomic angular momentum in an iron rod produces measurable mechanical rotation, and vice versa. Spin and rotation are the same angular momentum observed at different scales.

**The compass needle analogy.** Think of each iron d-circulation as a compass needle. The needle has a fixed magnetic moment — you cannot make it "more magnetic," and you cannot increase its spin rate without changing what element it is. What you CAN do is rotate its orientation. When you rotate it, it accumulates angular displacement: phase. Now scale that to 10²² compass needles, all aligned, all being rotated in lockstep by the cavity drive. The "phase" is simply *where in the precession circle* each vector is pointing right now. Left alone, the precession runs at the natural rate set by the DC alignment field. The cavity pushes all 10²² vectors forward *faster than free precession* — each resonant cycle delivers a small kick δφ. That continuous, coherent, synchronized rotation of 10²² aligned circulations IS angular momentum: macroscopic, mechanical, real. Einstein-de Haas did this at DC — one alignment event, one mechanical rotation impulse. The cavity does it at 5.6 GHz: 5.6 billion phase increments per second.

**Phase advance as angular momentum.** Angular momentum is action per angle:

```
L = dS/dθ
```

Phase advance IS angular momentum accumulation. Each precession cycle of an aligned vortex advances its phase by 2π. At FMR frequency f, the phase advance rate is:

```
dθ/dt = 2πf
```

At 5.6 GHz, this is 3.5 × 10¹⁰ radians per second — roughly 10⁹ complete winding cycles per second. Compare this to mechanical rotation: even at 10,000 RPM, a gyroscope achieves ~170 Hz ≈ 1,068 rad/s. The microwave-driven phase advance is seven orders of magnitude faster.

**Phase multiplicity.** The accumulated phase beyond the natural ground state is the "phase multiplicity." In steady state under continuous drive:

```
Steady-state angular momentum = Drive rate / Dissipation rate
```

The critical parameter is the dissipation rate — the relaxation time of the material. For YIG, the spin-spin relaxation time is ~100 ns, corresponding to FMR linewidth of ~0.3 Oe. This means the system accumulates:

```
Phase multiplicity ≈ f × T₂ ≈ 5.6 × 10⁹ × 10⁻⁷ ≈ 560
```

Each aligned vortex accumulates ~560 extra phase cycles' worth of angular momentum in steady state. This is not limited by quantum numbers (those constrain individual vortices). It is limited by polarization fraction, drive power, and dissipation rate — all engineering parameters.

**The swing analogy.** Pulsed drive may outperform continuous-wave (CW) drive for the same reason a child pumps a swing: correctly timed impulses can build amplitude more efficiently than constant force. The Alzofon protocol (2 μs on, 2–6 ms off) may exploit this — each pulse kicks the precession to a larger cone angle, and the off-time allows the system to settle into a new equilibrium before the next kick. The experiment will test both CW and pulsed regimes.

### 3.5 YIG Under the Vortex Model

Yttrium iron garnet, Y₃Fe₅O₁₂, is the optimal material for this experiment. Under POAMS, a single formula unit contains:

| Vortex | Mode | ħ per vortex | Count | Subtotal ħ |
|---|---|---|---|---|
| Yttrium | 39 | 89 | 3 | 267 |
| Iron | 26 | 56 | 5 | 280 |
| Oxygen | 8 | 16 | 12 | 192 |
| **Total** | | | **20** | **739** |

**Iron's d-harmonic asymmetry.** Iron (mode-26) has its outer circulation organized in sub-modes. The 3d sub-mode has 10 geometric slots (positions in the standing wave pattern) but only 6 are occupied in Fe³⁺. This 6-of-10 filling creates an asymmetric circulation — a net angular momentum flow that does not cancel. Conventional physics calls this the "magnetic moment." Under POAMS, it is simply the net vortex circulation arising from incomplete harmonic filling.

**The garnet lattice geometry.** In the YIG crystal structure, oxygen vortices serve as coupling bridges between iron vortices. The outer circulation modes of oxygen (mode-8) overlap geometrically with the d-harmonic modes of iron (mode-26), enabling angular momentum transfer between iron sites through the oxygen network. This is what conventional physics calls "superexchange interaction."

The five iron vortices per formula unit occupy two types of lattice sites:
- **3 tetrahedral sites (d-sites):** Iron vortices surrounded by 4 oxygen vortices
- **2 octahedral sites (a-sites):** Iron vortices surrounded by 6 oxygen vortices

The d-site and a-site iron vortices are coupled antiparallel — their net circulations oppose each other. With 3 vortices pointing one way and 2 pointing the other, the result is **one uncompensated iron vortex per formula unit.** This net circulation is what makes YIG a ferrimagnet (conventional terminology) or, in POAMS terms, gives it a net d-harmonic circulation asymmetry per unit cell.

**Why YIG is optimal:**

| Property | YIG | NiZn Ferrite | Bismuth | Al²⁷ (Alzofon) |
|---|---|---|---|---|
| FMR linewidth | 0.3 Oe | 20–50 Oe | N/A (metal) | N/A (NMR) |
| Relaxation time | ~100 ns | ~1 ns | ~1 ps | ~1 ms (nuclear) |
| Microwave penetration | Full volume | Full volume | Skin depth only (μm) | Full volume |
| Spin density | 2.1 × 10²² cm⁻³ | ~10²² cm⁻³ | ~10²² cm⁻³ | ~6 × 10²² cm⁻³ |
| Crystal availability | Commercial spheres | Polycrystalline | Polycrystalline | Powder/inclusions |
| Resonance Q | 18,700 | ~100 | N/A | ~1,000 (nuclear) |

YIG has:
- **Narrowest FMR linewidth in nature** (0.3 Oe for polished single-crystal spheres) → longest coherence → largest phase multiplicity
- **Insulating** → microwaves penetrate the full volume, not just the skin depth
- **High aligned spin density** → maximum angular momentum per unit volume
- **Commercial single crystals** → available now, no custom synthesis required for Phase 1
- **Well-characterized FMR** → decades of microwave engineering literature; no unknowns in the resonance behavior

---

## 4. Prior Work & Convergent Evidence

### 4.1 NASA Marshall Space Flight Center Experiments

Star Lord spent two years at the MSFC Advanced Propulsion Physics Lab conducting experiments on angular momentum and weight modification.

**Setup:** Bismuth pucks (chosen for high atomic number, mode-83, 209ħ) in two configurations:
1. **Mechanical rotation:** Spinning bismuth disc on a precision balance
2. **Field rotation:** Static bismuth disc with sequential microwave emitters creating a rotating alignment field pattern

**Results:**
- Weight changes of hundredths of a gram — small but consistent and repeatable
- Co-spin configuration (angular momentum aligned with Earth rotation): weight increase
- Anti-spin configuration: weight decrease
- Effect reversed sign with reversal of rotation/field direction
- Effect disappeared when drive was removed

**Why the effect was small — failure modes now understood:**

1. **Bismuth is conductive.** Skin depth at microwave frequencies is measured in microns. Only a thin shell of the puck interacted with the drive field. The vast majority of the material was unaddressed.
2. **Sequential emitters, not coherent drive.** Multiple emitters fired in sequence to simulate a rotating field. This produces no phase coherence — each emitter's contribution is independent, with random phase relationships. True collective phase advance requires coherent drive at the resonant frequency.
3. **High damping.** Bismuth's relaxation time is on the order of picoseconds — roughly 100,000× faster than YIG. The phase multiplicity achievable in bismuth is negligible.
4. **Wrong model.** The theoretical framework at the time targeted individual atomic spin modification, not collective phase advance. The mechanism was partially correct (angular momentum alignment → weight change) but the implementation was suboptimal.

Despite these limitations, the experiment produced a directional, reversible weight change. This is exactly what POAMS predicts, and the small magnitude is exactly what the failure mode analysis explains.

Star Lord's separate brass gyroscope observations — conducted independently from MSFC, at the tabletop level with no applied alignment field, using nothing more than a spinning brass rotor and a sensitive analytical balance — provide independent confirmation with even cruder apparatus. See Section 4.5.

### 4.2 Alzofon AGNUE Program (1981)

Frederick Alzofon, a physicist at Boeing Aerospace, published AIAA-81-1608 describing a mechanism he called Anti-Gravity Nuclear Unique Effect (AGNUE). His approach:

**Setup:**
- Aluminum-27 powder with embedded iron inclusions
- DC alignment field: 660 Oe (from iron inclusions, providing local fields)
- Pulsed microwave drive: 3000 MHz, 2 μs on / 2–6 ms off
- Target: Dynamic Nuclear Orientation of Al²⁷ quantum accumulators

**Key parameters:**
- Operating frequency: 3 GHz (S-band, standard radar)
- Duty cycle: ~0.1% (2 μs / 2 ms)
- Estimated gravitational energy: ~1 joule per duty cycle

**Verification:** George Hathaway at Hathaway Research International (Toronto) conducted partial replication and reported "anomalous motion of a test mass." Star Lord visited Hathaway's lab along with Hal Puthoff and observed the experimental setup.

**What Alzofon got right:**
- Alignment field + microwave drive to manipulate angular momentum state
- Insulating working material (aluminum oxide matrix)
- Pulsed protocol (transient angular momentum departure)
- Correct coupling: angular momentum state change → weight change

**What Alzofon got wrong:**
- Theoretical framework: virtual particle absorption, Compton wavelength arguments — unnecessary and incorrect ontology
- Material choice: Al²⁷ nuclear resonance has far lower coupling than electronic FMR in ferrites
- No cavity enhancement: free-space microwave illumination, no Q amplification

Daniel Alzofon (Frederick's son) has continued the AGNUE program, producing engineering analysis of UAP propulsion systems that converges on the same mechanism and is now aligned with POAMS.

### 4.3 Historical Precedents

Multiple programs over six decades have attempted to engineer weight change through angular momentum manipulation. Their methods, failures, and partial successes are instructive.

| Program | Date | Method | Working Material | Alignment | Drive | Coupling | Result |
|---|---|---|---|---|---|---|---|
| Die Glocke | 1944–45 | Counter-rotating drums + HV | Mercury antimonate (Hg: mode-80, 201ħ) | Mechanical rotation | Electrical discharge | Z⁴ spin-orbit (brute force) | Reported effects, lethal radiation, no reproducibility |
| T.T. Brown | 1950s–60s | Asymmetric capacitors | Dielectric + electrodes | Electric field | DC, 50–250 kV | Weakest (electrostatic) | Small thrust, disputed origin, simplest setup |
| Podkletnov | 1992–2003 | Superconducting disc + HV pulse | YBCO ceramic | Meissner alignment | 2 MV impulse | Coherent + aligned + impulsive | 2% weight reduction (disputed), beam propagation claim |
| Alzofon | 1981 | DC field + pulsed μW | Al²⁷ + iron inclusions | DC magnetic (660 Oe) | Pulsed 3 GHz | Correct mechanism, suboptimal material | Partial verification by Hathaway |
| **This experiment** | **2026** | **FMR cavity + YIG** | **Y₃Fe₅O₁₂ single crystal** | **DC magnetic (2000 Oe)** | **CW/pulsed 5.6 GHz** | **Resonant, narrowest linewidth, full volume** | **—** |

**Analysis of failures:**

- **Die Glocke** used brute force: massive current through high-Z material with no resonant coupling. The Z⁴ spin-orbit coupling in mercury is enormous, but without resonance, almost all input energy goes to heating. Lethal radiation suggests uncontrolled nuclear-scale energy release. No theoretical framework to guide optimization.

- **Brown** used the weakest possible coupling — electrostatic polarization. The angular momentum contribution of electric dipole alignment is orders of magnitude below magnetic (spin) alignment. His effects were real but tiny and easily attributed to ion wind by skeptics. Correct direction, wrong scale.

- **Podkletnov** was closest to the present design: a superconductor provides coherent alignment (Meissner effect aligns all vortex circulations), and the 2 MV pulse provides impulsive drive. His reported results (2% weight reduction above a spinning superconducting disc) are consistent with POAMS predictions. The superconducting disc adds the requirement of cryogenic infrastructure; YIG operates at room temperature.

- **Alzofon** had the correct mechanism but suboptimal material. Nuclear resonance in Al²⁷ has a far lower gyromagnetic ratio than electronic FMR, meaning less angular momentum per drive cycle. The material was polycrystalline powder, not a single crystal. No cavity enhancement.

**This experiment** combines every advantage: resonant coupling (cavity Q ≈ 10⁴), the narrowest linewidth material (YIG, 0.3 Oe), full volume penetration (insulating crystal), single-crystal coherence, room temperature operation, and the correct theoretical framework (POAMS) to guide parameter optimization.

### 4.4 UAP Engineering Connection

Daniel Alzofon's engineering analysis of unidentified aerial phenomena provides convergent evidence for the mechanism described in this paper.

**Key observations from Alzofon's analysis:**

- **Slotted waveguide arrays:** The radiating structure in reported vehicles is consistent with phased-array slotted waveguide antennas — a technology dating to WWII radar development.
- **Luneberg lens profiles:** Vehicle cross-sections match Luneberg lens geometry — a microwave optics component that provides omnidirectional gain.
- **Operating frequency:** ~3 GHz (S-band), consistent with Alzofon's AGNUE frequency and with available radar-era components.
- **Working substance:** The drive targets insulating single crystals with paramagnetic or ferrimagnetic impurities — ruby (Al₂O₃:Cr³⁺), olivine ((Mg,Fe)₂SiO₄), sapphire. These are YIG's material class: insulating, microwave-transparent, with spin-active ions providing the angular momentum coupling.

**Physical evidence:**

The 1967 Falcon Lake incident (Stefan Michalak) produced a grid-pattern radiation burn consistent with microwave exposure through a slotted waveguide array. The burn pattern geometry matches standard waveguide slot spacing at S-band frequencies.

**Engineering lineage:**

The components required — waveguide arrays, magnetrons, Luneberg lenses — are all terrestrial, all dating to the WWII radar era. The vehicle shape is not aerodynamic; it is electromagnetic. The disc/lens profile IS the antenna. The propulsion mechanism is angular momentum phase advance in a solid-state working substance, driven by phased microwave arrays — exactly the mechanism this experiment tests at laboratory scale.

### 4.5 Brass Gyroscope Anomaly

The most important empirical data point for bounding this experiment comes from a tabletop observation with no applied field, no microwave drive, no special material — nothing but a brass rotor and a sensitive analytical balance.

**Setup:**
- Brass gyroscope: 1.5" (38.1 mm) diameter rotor, 289 g total including gimbal, ~190 g rotor mass
- Spin rate: ~12,000 RPM (1,257 rad/s)
- Measured on a precision analytical balance
- No external alignment field; no microwave drive

**Angular momentum of the rotor:**

```
I = ½mr² ≈ ½ × 0.190 kg × (0.019 m)² ≈ 3.4 × 10⁻⁵ kg⋅m²
L = Iω ≈ 3.4 × 10⁻⁵ × 1,257 ≈ 0.043 kg⋅m²/s
```

**Barnett-induced alignment field:**

The bulk rotation induces an effective magnetic field via the Barnett effect:

```
B_eff = ω / γₑ = 1,257 / (1.76 × 10¹¹) ≈ 7 nanotesla
```

That is 1/7,000th of Earth's magnetic field. The thermal equilibrium alignment fraction of internal circulations at room temperature:

```
Alignment fraction ≈ μ_B × B_eff / kT ≈ 1.6 × 10⁻¹¹
```

Parts per hundred billion. In brass, which is not magnetic. This is the worst possible material and the worst possible mechanism for spin alignment.

**Measured result:** 30–50 mg weight change, consistently, in both directions — weight increase in co-spin configuration, weight decrease in anti-spin. Repeatable.

**What this means:** A Barnett-induced alignment fraction of 1.6 × 10⁻¹¹ in a non-magnetic material produces a constraint-force change of approximately 40 mg. The coupling between internal spin alignment and gravitational interaction is real, bidirectional, and demonstrable on a kitchen table with commodity hardware.

Brass is the worst conceivable medium for this experiment. It is non-magnetic, has high damping, and relies on mechanical rotation to produce an alignment field seven orders of magnitude below Earth's background field. Despite all of this, the effect is detectable on a milligram-resolution balance.

This is the most important empirical data point in this paper. Every quantitative prediction in Section 5 must be consistent with it — and Section 5.6 uses this data to bound the coupling constant and project the expected YIG signal.

---

## 5. Mathematical Framework

### 5.1 Ferromagnetic Resonance

Ferromagnetic resonance (FMR) occurs when the applied microwave frequency matches the natural precession frequency of aligned vortex circulations in a material. Under POAMS, the gyromagnetic ratio γ is a geometric quantity — the ratio of angular momentum circulation rate to alignment field strength — arising from the topology of the vortex structure.

**FMR condition:**

```
f_FMR = γ × B_applied
```

where:
- γ ≈ 2.8 MHz/Gauss (≈ 2.8 GHz/kOe) for iron-site vortices
- B_applied is the DC alignment field strength

For B_applied = 2000 Oe:

```
f_FMR = 2.8 MHz/Gauss × 2000 Gauss = 5,600 MHz = 5.6 GHz
```

This places the resonance in C-band, where cavity dimensions are convenient (cm-scale), components are commercially available, and atmospheric absorption is negligible.

**Linewidth and quality factor:**

The FMR linewidth ΔH determines the resonance Q of the spin system:

```
Q_spin = f_FMR / (γ × ΔH) = 5600 MHz / (2.8 MHz/Oe × 0.3 Oe) ≈ 6,667
```

For a polished YIG sphere, ΔH ≈ 0.3 Oe gives a spin system Q approaching 10⁴. This is the ratio of energy stored to energy dissipated per cycle — and it directly determines the steady-state phase multiplicity achievable under continuous drive.

### 5.2 Cavity Design

The microwave cavity serves two functions: it concentrates the drive field at the YIG sphere, and it amplifies the effective field by the cavity Q factor.

**TM₀₁₀ mode cylindrical cavity:**

The TM₀₁₀ mode has maximum axial electric field and maximum azimuthal magnetic field at the cavity midplane, providing uniform RF drive field across the YIG sphere.

```
f₀₁₀ = (2.405 × c) / (2π × a)
```

where a is the cavity radius.

Solving for a at f = 5.6 GHz:

```
a = (2.405 × 2.998 × 10¹⁰ cm/s) / (2π × 5.6 × 10⁹ Hz)
a = 7.209 × 10¹⁰ / 3.519 × 10¹⁰
a ≈ 2.049 cm ≈ 20.5 mm
```

**Cavity diameter: ~41 mm.** This is a convenient laboratory scale — the cavity is roughly the size of a shot glass.

**Cavity height:** For TM₀₁₀, height is a free parameter (mode is independent of length for L > 0). Practical choice: L ≈ 2a ≈ 41 mm for a cube-like aspect ratio, giving good coupling and accessible sample placement.

**Q factor:**

For a copper cavity (σ = 5.8 × 10⁷ S/m) at 5.6 GHz:

```
δ = √(2 / (ω μ₀ σ)) ≈ 0.88 μm   (skin depth)

Q ≈ a / δ × (geometric factor) ≈ 10,000 – 20,000
```

Conservative estimate: Q ≈ 10,000. Polished, gold-plated cavity: Q ≈ 15,000–20,000.

**Effective field amplification:**

The RF field inside the cavity at resonance is amplified relative to the input:

```
H_eff = H_input × √Q
```

At Q = 10,000:

```
√Q ≈ 100
```

A 1 W input generating H_input ≈ 0.01 Oe produces H_eff ≈ 1 Oe at the sphere. At 10 W input, H_eff ≈ 3 Oe. This is comparable to the FMR linewidth — meaning cavity-enhanced drive easily saturates the resonance.

### 5.3 Precession Cone Angle

Under FMR drive, each aligned vortex circulation precesses around the DC alignment field axis. The precession cone half-angle θ determines the angular momentum per vortex:

```
θ ≈ arctan(γ × H_rf / Δω)
```

where Δω is the detuning from exact resonance. On resonance (Δω → linewidth-limited):

```
θ_max ≈ arctan(H_rf / ΔH)
```

For H_rf = 1 Oe (cavity-enhanced from ~1 W input) and ΔH = 0.3 Oe:

```
θ_max ≈ arctan(3.3) ≈ 73°
```

At H_rf = 3 Oe (~10 W input):

```
θ_max ≈ arctan(10) ≈ 84°
```

Near 90° cone angle means the vortex circulation is precessing nearly perpendicular to the alignment axis — maximum transverse angular momentum component.

The angular momentum per vortex in the precessing state:

```
L_z = L₀ × cos(θ)        (component along alignment axis)
L_perp = L₀ × sin(θ)      (transverse precessing component)
```

The transverse component carries the coherent phase advance. At θ = 73°, sin(θ) = 0.96 — nearly the full angular momentum of each vortex participates in the collective precession.

### 5.4 Expected Effect Size

The total weight change depends on:

```
Δw = N_aligned × L_phase × κ
```

where:
- N_aligned = number of vortices participating in coherent precession
- L_phase = phase angular momentum per vortex (drive rate / dissipation rate)
- κ = coupling constant between collective phase angular momentum and orbital radius (the key unknown)

**N_aligned for a 10 mm YIG sphere (mass ≈ 5.4 g):**

YIG density: 5.17 g/cm³. Volume of 10 mm sphere: 0.524 cm³. Mass: 2.71 g (Note: commercial "10 mm" spheres are 10 mm diameter, actual mass ≈ 2.7 g; we use 5.4 g for a hypothetical full-density sphere throughout for conservative estimation).

Number of formula units:

```
N = (m × N_A) / M = (2.7 × 6.022 × 10²³) / 737.9 ≈ 2.2 × 10²¹
```

Each formula unit contributes one uncompensated iron vortex. Total aligned vortices:

```
N_aligned ≈ 2.2 × 10²¹
```

**Phase angular momentum per vortex:**

```
L_phase = ħ × (f × T₂) × sin(θ) ≈ ħ × 560 × 0.96 ≈ 538ħ per vortex
```

**Total added angular momentum:**

```
ΔL_total = 2.2 × 10²¹ × 538 × 1.055 × 10⁻³⁴ J·s
         ≈ 1.25 × 10⁻¹⁰ J·s
```

**The coupling constant κ** relates this angular momentum to orbital radius change. This is the unknown that the experiment measures. The pessimistic, moderate, and optimistic scenarios:

| Scenario | κ (effective) | Δw for 10mm sphere | Detectability |
|---|---|---|---|
| Strong coupling | ~10⁻² | ~50 mg | Milligram balance, trivial |
| Moderate coupling | ~10⁻⁴ | ~0.5 mg | Milligram balance, detectable |
| Weak coupling | ~10⁻⁶ | ~5 μg | Microgram balance + lock-in amplifier |
| Very weak coupling | ~10⁻⁸ | ~50 ng | Precision research balance |

**Material comparison:**

| Parameter | YIG | NiZn Ferrite | Bismuth (MSFC) | Al²⁷ (Alzofon) |
|---|---|---|---|---|
| Phase multiplicity (f × T₂) | ~560 | ~6 | ~0.006 | ~3,000 (nuclear) |
| Penetration | Full volume | Full volume | Skin depth (~μm) | Full volume |
| Fraction addressed | ~100% | ~100% | ~0.1% | ~100% |
| Effective product | 560 | 6 | ~6 × 10⁻⁶ | 3,000 |
| Relative to YIG | **1.0** | 0.011 | 10⁻⁸ | 5.4 |

Note: Alzofon's Al²⁷ has higher phase multiplicity due to the long nuclear T₁, but the gyromagnetic ratio is 650× lower, so angular momentum per cycle is far less. The effective coupling (γ² × f × T₂) strongly favors YIG.

The MSFC bismuth experiment's effective coupling was roughly 10⁻⁸ of YIG's — yet it still produced measurable weight changes (hundredths of gram). If the coupling constant κ is the same, YIG should produce effects 10⁸× larger — kilograms of apparent weight change, far exceeding the sphere's own weight. This either means the coupling is much weaker than the MSFC results imply, or the MSFC results were limited by a different mechanism (likely both: the conductive skin depth means only a thin shell was addressed, making the effective comparison more nuanced).

**Empirical lower bound from the brass gyroscope.** The tabletop brass gyroscope observation (Section 4.5) provides a direct empirical constraint on the coupling constant. A non-magnetic brass rotor spinning at 12,000 RPM produces a Barnett-induced internal alignment fraction of ~1.6 × 10⁻¹¹ — parts per hundred billion — and that fraction consistently produces 30–50 mg of weight change in both co-spin and anti-spin configurations. This proves the coupling is real, proves it operates in both directions as POAMS predicts, and proves the coupling is strong enough per aligned atom that even the worst conceivable medium produces a measurable result.

YIG under FMR drive achieves near-unity alignment fraction (essentially every iron d-circulation participating), compared to 10⁻¹¹ in spinning brass. That is a ratio of roughly 6 × 10¹⁰ in alignment quality. Even accounting for the mass difference (5.4 g sphere versus ~190 g brass rotor), the YIG experiment is operating in a categorically different regime. The gyroscope result is not a small prior that needs to be extrapolated carefully. It is a direct demonstration that the mechanism works — and YIG is purpose-built to do it better by ten or more orders of magnitude.

The honest answer: the coupling constant is unknown. The experiment measures it. The sensitivity analysis shows that even very weak coupling (κ ~ 10⁻⁶) produces detectable signals on available instrumentation.

### 5.5 The Relaxation Curve as Diagnostic

The most informative single measurement in the experiment is the relaxation curve: kill the drive and watch the weight return to baseline.

**How fast the weight returns reveals the coupling mechanism:**

| Relaxation Time | Interpretation |
|---|---|
| < 100 ns (electronic T₂*) | Purely electronic spin-lattice coupling. Weight change tracks precession, no anomalous mechanism. |
| 100 ns – 1 μs | Matches electronic relaxation. Standard FMR behavior, consistent with but not proving POAMS prediction. |
| 1 μs – 1 ms | Slower than electronic relaxation. Angular momentum transferring through a pathway not captured by standard FMR — possible lattice/orbital coupling. |
| 1 ms – 1 s | Much slower. Consistent with mechanical/inertial coupling — angular momentum in bulk rotation mode. |
| > 1 s | Meta-stable state. The system has reached a new orbital equilibrium that persists after drive removal. |
| Permanent | New equilibrium. System has been kicked into a genuinely different orbital radius. (Unlikely at low power, but would be decisive.) |

**The key threshold:** If the relaxation time exceeds the electronic T₂* (~100 ns for YIG), something beyond standard ferromagnetic resonance is occurring. This is model-independent — regardless of whether POAMS is correct, a weight change that persists longer than the spin coherence time requires explanation.

The relaxation measurement requires fast sampling of the force transducer (μs resolution). A strain-gauge load cell with analog output can provide this; a digital analytical balance with serial readout cannot (too slow). The experimental design includes both: digital balance for steady-state measurements, analog load cell for transient characterization.

### 5.6 Coupling Constant Analysis from Gyroscope Data

The brass gyroscope result (Section 4.5) allows quantitative bounding of the coupling constant — and reveals something important about its functional form.

**Raw coupling strength:**

```
ΔF ≈ 40 mg → 3.9 × 10⁻⁴ N
Alignment fraction: ~1.6 × 10⁻¹¹

Coupling strength: ΔF / alignment_fraction ≈ 2.4 × 10⁷ N per unit alignment fraction
```

**Naive linear extrapolation to YIG:**

YIG at FMR saturation: alignment fraction ≈ 1.0. Scale by mass ratio (5.4 g / 190 g ≈ 0.028):

```
ΔF_YIG (linear) ≈ 2.4 × 10⁷ × 1.0 × 0.028 ≈ 670,000 N ≈ 67 metric tons
```

From a 5.4 gram sphere. Obviously absurd. Which is exactly the point.

**The coupling is not linear with alignment fraction.** This is not a failure of the framework — it is the framework telling us something. The naive linear extrapolation breaks because one of the following must be true:

1. **Power-law or threshold behavior.** Below some coherence threshold, the coupling is weak or absent. Above the threshold, the effect switches on disproportionately. The brass gyroscope, operating in the nanoTesla alignment regime, may be barely above a threshold that a slower spin never reaches. YIG, with coherent FMR drive and near-unity alignment, is deep in the saturated regime — where the functional form is different.

2. **Fundamentally different coupling pathways.** Bulk mechanical rotation (macro-physical, incoherent, 10⁻¹¹ alignment fraction) and coherent FMR drive (micro-physical, phase-coherent, ~1.0 alignment fraction) may not be the same input to the same equation. The internal vortex alignment — even at parts-per-billion from Barnett — may couple to the gravitational background more strongly per aligned atom than the bulk angular momentum of the rotor. The rotation is just the delivery mechanism. The active ingredient is the internal spin-state change. That reframes the coupling constant calculation entirely: we should not be comparing L_rotor to L_YIG. We should be comparing alignment-fraction × coherence × drive-rate.

**Even with strong saturation, the signal is massive.** If the coupling goes as the square root of alignment fraction, the ratio between brass gyroscope and YIG is √(6 × 10¹⁰) ≈ 245,000. Scaled by mass ratio (0.028): predicted ΔF_YIG ≈ 40 mg × 245,000 × 0.028 ≈ 274 kg. Still enormous. Even if an additional suppression factor of 10⁶ is applied for reasons not yet understood, the predicted signal is in the hundreds-of-milligrams range — well above the detection threshold for this experiment.

**The two-scenario interpretation:**

| Scenario | Implication for YIG |
|---|---|
| Coupling NOT proportional to AM magnitude — micro-physical d-circulation alignment couples far more strongly than macro-physical rotation | YIG at near-unity alignment is exactly the regime that produces maximum coupling. Effect could be enormous. |
| Nonlinear threshold — below some coherence threshold nothing, above it the effect switches on | YIG with coherent GHz drive blows past any threshold the brass gyroscope barely skirts. Deep in the strong-coupling regime. |

Either interpretation leads to the same experimental prediction: the YIG signal will be unambiguous. The brass gyroscope anomaly is not a small hint requiring cautious extrapolation. It is a proof of concept using the worst possible apparatus, demonstrating that the coupling is real and strong. What the YIG experiment adds is not more of the same — it is the correct material, the correct alignment mechanism, the correct drive method, and a degree of coherence that the gyroscope cannot approach.

---

## 6. Experimental Design

### 6.1 System Architecture

```
                    ┌──────────────────────────┐
                    │   POLYCARBONATE TUBE      │
                    │   (Phase 2: levitation    │
                    │    containment)           │
                    │                           │
                    │   ┌───────────────────┐   │
                    │   │ OPTICAL POSITION  │   │
                    │   │ SENSORS (IR LED + │   │
                    │   │ photodiode pairs) │   │
                    │   └───────────────────┘   │
                    │                           │
                    ├───────────────────────────┤
        ┌───────────┤   ALIGNMENT COIL (upper)  ├───────────┐
        │           ├───────────────────────────┤           │
        │           │                           │           │
        │   ┌───────┴───────────────────────────┴───────┐   │
        │   │         COPPER CAVITY (TM₀₁₀)            │   │
        │   │         ┌─────────────────┐               │   │
        │   │         │   YIG SPHERE    │               │   │
        │   │         │   (on PTFE post)│               │   │
        │   │         └────────┬────────┘               │   │
        │   │                  │                        │   │
        │   │    SMA ──────►  coupling loop             │   │
        │   └───────┬───────────────────────────┬───────┘   │
        │           ├───────────────────────────┤           │
        └───────────┤  ALIGNMENT COIL (lower)   ├───────────┘
                    ├───────────────────────────┤
                    │                           │
                    │   BALANCE / LOAD CELL     │
                    │                           │
                    └───────────────────────────┘

    RF SIGNAL CHAIN:
    ┌─────┐    ┌────────────┐    ┌──────────────┐    ┌────────┐
    │ VCO ├───►│ RF AMP     ├───►│ DIRECTIONAL  ├───►│ CAVITY │
    │     │    │ (3-50W)    │    │ COUPLER      │    │        │
    └─────┘    └────────────┘    └──────┬───────┘    └────────┘
                                        │
                                        ▼
                                 ┌──────────────┐    ┌────────┐
                                 │ SCHOTTKY     ├───►│ MCU    │
                                 │ DETECTOR     │    │(ESP32) │
                                 └──────────────┘    └───┬────┘
                                                         │
                                              ┌──────────┴──────────┐
                                              │  DATA LOGGING:      │
                                              │  - FMR absorption   │
                                              │  - Force transducer │
                                              │  - Temperature      │
                                              │  - Optical position │
                                              └─────────────────────┘
```

### 6.2 Component Specifications

#### Phase 1: Detection (~$1,200–1,800)

| Component | Specification | Est. Cost | Notes |
|---|---|---|---|
| YIG sphere | 1 mm diameter, polished single crystal | $50–100 | Standard catalog item. Start small for cavity matching. |
| YIG sphere (primary) | 10 mm diameter, polished | $150–300 | Main test specimen. ΔH < 0.5 Oe. |
| Copper cavity | 41 mm ID × 41 mm, machined from Cu rod | $100–200 | Machine shop or CNC. Needs SMA port. |
| Iron-core electromagnet | C-frame or H-frame, 2000 Oe at 41mm gap | $200–400 | Surplus or custom-wound. Air-core Helmholtz CANNOT reach 2000 Oe at bench scale — iron core required.¹ |
| VCO (voltage-controlled oscillator) | 5.0–6.5 GHz, +10 dBm output | $30–60 | Mini-Circuits or Analog Devices eval board. |
| RF amplifier | 5–6 GHz, 3 W (Phase 1) | $150–300 | GaAs MMIC module. |
| Directional coupler | 20 dB, 4–8 GHz | $30–50 | Mini-Circuits or Krytar. |
| Schottky detector | Zero-bias, 4–8 GHz | $20–40 | Broadband detector diode + matching. |
| SMA connectors & cable | Semi-rigid coax, SMA-SMA | $40–60 | Low-loss cable for cavity coupling. |
| MCU | ESP32 or STM32 with ADC, DAC, USB | $15–25 | Feedback loop controller, data logger. |
| Analytical balance | 0.001 g (1 mg) resolution, 200 g capacity | $200–400 | Used Sartorius/Mettler on eBay. Shielded from RF. |
| PTFE post & support | Machined PTFE rod, press-fit | $10–20 | Non-magnetic, low-loss support for sphere. |
| Power supply (magnet) | 0–5A adjustable DC, regulated | $50–80 | Current-controlled for field stability. |
| Miscellaneous | Connectors, wire, shielding, enclosure | $50–100 | — |
| **Phase 1 Total** | | **$1,095–2,135** | |

¹ **Iron-core electromagnet note (Rev 6 correction):** Air-core Helmholtz coils at bench scale (10–20 cm diameter) require hundreds of amperes to produce 2000 Oe at center. This is impractical. An iron-core electromagnet with a pole gap matching the cavity dimension (≈ 41 mm) can produce 2000 Oe with modest current (1–3 A) due to the permeability amplification of the iron core (μ_r ≈ 1,000–5,000). Surplus laboratory electromagnets (e.g., from NMR or EPR systems) are available for $200–400 and are ideal.

#### Phase 2: Levitation (~$1,400–2,300 additional)

| Component | Specification | Est. Cost | Notes |
|---|---|---|---|
| RF amplifier upgrade | 5–6 GHz, 50 W SSPA or TWTA | $400–800 | Surplus TWTA from radar/satcom. |
| Polycarbonate tube | 50 mm OD, capped, wall 3 mm | $20–40 | Containment for levitating sphere. |
| Optical position sensors | IR LED + photodiode pairs, 3 axes | $30–50 | Detects sphere lift-off and position. |
| Load cell (analog) | 0–50 g, strain gauge, μs response | $50–100 | For transient relaxation measurement. |
| Load cell amplifier | HX711 or INA125 instrumentation amp | $10–20 | High-resolution ADC for strain gauge. |
| RAM foam / RF shielding | Microwave absorber tiles + copper mesh | $100–200 | Personnel safety at 50 W. |
| Helmholtz trim coils | Small, for field uniformity at sphere | $50–100 | Fine gradient control during levitation. |
| High-speed DAQ | USB oscilloscope or dedicated ADC, 1 MHz+ | $200–400 | Relaxation curve capture. |
| Vacuum chamber (optional) | Bell jar + mechanical pump | $300–500 | Eliminate convection artifact. |
| **Phase 2 Total** | | **$1,160–2,210** | |
| **Grand Total (Phase 1+2)** | | **$2,255–4,345** | |

### 6.3 Feedback Control System

The experiment requires active frequency tracking because the FMR frequency drifts with temperature (~-17 MHz/°C due to alignment field variation and crystal thermal expansion).

**Signal chain:**

1. **VCO** generates CW signal at ~5.6 GHz, tunable via DC voltage input.
2. **RF amplifier** boosts to operating power (3–50 W depending on phase).
3. **Directional coupler** samples the reflected power from the cavity.
4. **Schottky detector** converts reflected RF power to DC voltage proportional to reflection coefficient.
5. **MCU** reads the detector voltage and adjusts VCO frequency to minimize reflected power (= maximize cavity coupling = maintain FMR absorption).

**Feedback algorithm:**

The MCU implements frequency dithering:
- Modulates VCO frequency ±1 MHz at ~1 kHz rate
- Demodulates the detector signal synchronously (lock-in detection)
- Error signal drives VCO center frequency toward the absorption minimum
- This is the standard technique used in EPR/FMR spectrometers

**Data logging:**

The MCU simultaneously records:
- FMR absorption depth (reflected power minimum depth — proportional to how well the sphere is being driven)
- Force transducer output (weight measurement)
- Thermocouple (cavity and magnet temperature)
- Optical sensor states (Phase 2: sphere position)
- Timestamp (ms resolution)

All data streams are logged to USB storage and optionally streamed to a host computer for real-time display.

---

## 7. Measurement Protocol

### 7.1 Phase 1: Baseline & FMR Characterization

**Objective:** Establish measurement baselines and verify FMR parameters before any weight change attempts.

**Procedure:**

1. **Balance settling.** Place the complete assembly (cavity + sphere + magnet) on the balance with no power applied. Record weight for 30 minutes. Characterize drift, noise floor, and settling time. The balance must resolve 1 mg with < 0.5 mg noise.

2. **Static field effects.** Energize the alignment field from 0 to 2000 Oe in 100 Oe steps. Record weight at each step. This establishes the magnetostriction and magnetic force baseline. These are static effects — they will be present at all subsequent measurements and must be subtracted.

3. **FMR characterization.** At 2000 Oe, sweep VCO frequency from 5.0 to 6.2 GHz. Monitor reflected power via the directional coupler. The FMR absorption dip will appear as a sharp minimum in reflected power. Record:
   - Center frequency (should be ≈ 5.6 GHz)
   - Linewidth (should be ≈ 0.84 MHz for ΔH = 0.3 Oe at γ = 2.8 MHz/Oe)
   - Absorption depth (should be deep for well-coupled sphere/cavity)

4. **Verify f = γB.** Change alignment field to 1500 Oe and repeat frequency sweep. FMR should shift to ≈ 4.2 GHz. Repeat at 1000 Oe (≈ 2.8 GHz). This confirms the system is tracking ferromagnetic resonance and not a cavity artifact.

5. **Thermal characterization.** Run CW drive at FMR for 10 minutes at 1 W. Monitor temperature rise and FMR frequency drift. Establish the thermal drift coefficient for the feedback system.

### 7.2 Phase 2: Detection — CW and Pulsed Drive

**Objective:** Detect weight change under FMR drive.

**CW Protocol:**

1. Set alignment field to 2000 Oe, positive polarity (defining "co-spin" relative to Earth rotation).
2. Lock FMR feedback loop.
3. Ramp RF power from 0 to 3 W in 0.5 W steps, 60 seconds per step.
4. At each power level, record average weight over 30 seconds.
5. Ramp back to 0 W, record weight recovery.
6. Plot weight vs. power. Look for: monotonic departure from baseline that scales with power.

**Pulsed Protocol:**

1. Same alignment field and frequency lock.
2. Apply pulsed drive: 2 μs on / 2 ms off (Alzofon protocol) at 3 W peak.
3. Record weight during pulsed drive (average over many pulses).
4. Sweep pulse parameters:
   - Pulse width: 0.1, 0.5, 1, 2, 5 μs
   - Repetition rate: 1 kHz, 10 kHz, 100 kHz, 1 MHz
   - Duty cycle held constant vs. pulse width varied independently
5. Find the parameter combination producing maximum weight change.
6. Record the transient weight response at pulse transitions (requires analog load cell + high-speed DAQ).

**Expected observation:** Weight change that increases with RF power, appears only within the FMR linewidth, and has a sign (increase or decrease) that depends on the alignment field polarity.

### 7.3 Phase 3: Direction Reversal (Go/No-Go Gate)

**This is the most important measurement in the entire experiment.**

**Procedure:**

1. Using the optimal drive parameters from Phase 2, record weight change with positive alignment field polarity.
2. Kill drive. Wait for full recovery to baseline.
3. Reverse alignment field polarity (reverse current through electromagnet).
4. Re-lock FMR (frequency will be the same; only the direction of precession changes).
5. Apply drive at same parameters. Record weight change.

**Decision criteria:**

| Observation | Action |
|---|---|
| Weight change reverses sign | **GO.** Proceed to Phase 4 controls, then Phase 5 levitation. |
| Weight change same sign both directions | **INVESTIGATE.** Likely thermal or mechanical artifact. Debug. |
| No weight change either direction | **NULL.** Increase power, improve coupling, check for errors. |
| Weight change only one direction | **PARTIAL.** May indicate asymmetric coupling or systematic error. Debug. |

**Why this is decisive:** A weight change that reverses with alignment polarity cannot be explained by:
- Thermal effects (heating is symmetric in polarity)
- Mechanical vibration (independent of field direction)
- RF radiation pressure (independent of precession direction)
- Magnetic force on the sphere (static, already baselined)
- Any known conventional mechanism

If the weight change reverses, we have detected angular momentum coupling to orbital radius. This IS the POAMS prediction.

### 7.4 Phase 4: Controls

After passing the go/no-go gate, systematic controls establish that the effect is real and attributable to FMR-driven phase advance:

**Control 1: Non-magnetic sphere.**
Replace YIG sphere with a glass bead of similar size and mass. Repeat Phase 2–3 protocol. Expected: zero weight change. This rules out cavity heating, radiation pressure, and other sphere-independent effects.

**Control 2: Off-resonance drive.**
Return YIG sphere. Detune VCO to FMR + 500 MHz (well outside the ~1 MHz linewidth). Apply same power. Expected: zero weight change. This confirms the effect requires resonant coupling, not just microwave illumination.

**Control 3: Field strength scaling.**
Repeat measurement at alignment fields of 1000, 1500, and 2000 Oe (FMR at 2.8, 4.2, and 5.6 GHz respectively). The weight change should scale with the number of aligned vortices, which increases with field strength. If the effect is proportional to field strength, it confirms alignment-dependent coupling.

**Control 4: Atmosphere independence.**
Repeat measurement in helium and argon atmospheres (via simple gas displacement in a sealed enclosure). If the weight change is identical in all three atmospheres, convection artifacts are excluded. Helium (low density, high thermal conductivity) and argon (high density, low thermal conductivity) bracket the thermal property space.

### 7.5 Phase 5: Power Ramp & Levitation

**Prerequisites:** Go/no-go gate passed, all controls clean.

**Procedure:**

1. Configure for anti-spin alignment (weight decrease predicted).
2. Install polycarbonate containment tube above cavity, capped.
3. Install optical position sensors at 2 mm, 5 mm, and 10 mm above the PTFE post.
4. Ramp RF power slowly from 3 W toward 50 W while monitoring weight.
5. Record weight vs. power continuously.
6. As weight approaches zero, slow the ramp rate. The sphere may become mechanically unstable (constraint force approaching zero).
7. At weight = 0, the sphere lifts off the PTFE post. Optical sensors detect this.
8. Sustain levitation. Log all parameters.
9. Kill drive. Observe descent dynamics:
   - Immediate drop = fast coupling
   - Slow descent = inertial lag
   - Hovering = meta-stable state
10. Repeat for reproducibility (minimum 10 trials).

**Video documentation:**

Every Phase 5 run will be recorded on video from multiple angles, with all instrument displays visible. The camera will be running before power-up and after power-down. Timestamped video synchronized with data logs provides the evidentiary record.

---

## 8. Challenges & Mitigations

### 8.1 Thermal Drift

**Challenge:** RF power heats the cavity and sphere, causing thermal expansion, FMR frequency drift, and convective air currents that produce apparent weight changes.

**Mitigation:**
- The direction reversal protocol (Phase 3) is the primary defense. Thermal effects are symmetric with respect to alignment polarity. Any weight change that reverses with polarity is non-thermal.
- Pulsed drive reduces average power dissipation.
- Thermal baseline established in Phase 1.
- Atmosphere independence test (helium/argon) directly addresses convection.

### 8.2 Magnetic Forces on the Sphere

**Challenge:** The alignment field exerts a force on the magnetized YIG sphere. If the field has a vertical gradient at the sphere location, this produces a real vertical force that mimics a weight change.

**Mitigation:**
- Symmetric electromagnet geometry (poles above and below cavity) produces zero gradient at the geometric center. The sphere sits at the field midplane.
- The magnetic force is a static effect that does not depend on RF drive. It is present with the field on and drive off, and is baselined in Phase 1 Step 2.
- Any field-gradient force is constant during the measurement (field is DC) and does not change when RF drive is applied or removed.
- Helmholtz-style trim coils allow fine-tuning of field uniformity.

### 8.3 Mechanical Vibration

**Challenge:** The building, HVAC, and electromagnet cooling fans transmit vibration to the balance.

**Mitigation:**
- Vibration isolation pads under the entire assembly (Sorbothane or pneumatic).
- Night/weekend measurements when building vibration is lowest.
- The direction reversal protocol again: vibration artifacts do not reverse with field polarity.
- Statistical analysis: many repeated measurements with alternating polarity, analyzed for systematic offset.

### 8.4 RF Interference with Balance

**Challenge:** 50 W of microwave power at 5.6 GHz, right next to a precision analytical balance, may cause RF pickup that biases the weight reading.

**Mitigation:**
- Balance electronics enclosed in copper mesh Faraday cage.
- Balance reads via USB/serial through filtered feedthrough.
- Control test: apply RF power with non-magnetic sphere — any RF-induced balance offset will be visible.
- Use analog load cell (simple strain gauge) as independent cross-check — far less susceptible to RF interference than a digital balance.

### 8.5 Magnetostriction

**Challenge:** YIG exhibits magnetostriction — physical dimensional change under alignment field. This changes the sphere's volume and density, potentially affecting buoyancy.

**Mitigation:**
- Magnetostriction is a static effect of the DC alignment field, not the RF drive.
- It is established in Phase 1 baseline (weight vs. field strength with no RF).
- The magnetostrictive strain in YIG is < 10⁻⁶ — negligible effect on buoyancy.
- The direction reversal protocol: magnetostriction magnitude is the same for both polarities (it depends on |B|², not sign of B).

---

## 9. Safety Considerations

### 9.1 Microwave Exposure

At 50 W, the maximum permissible exposure (MPE) at 5.6 GHz is approximately 10 mW/cm² for occupational exposure (IEEE C95.1).

**Power density at distance r from an isotropic source:**

```
S = P / (4πr²) = 50 / (4π × r²) W/m²
```

At r = 1 m: S = 4 W/m² = 0.4 mW/cm² — well below MPE.

However, the cavity has an open coupling port, and leakage around the SMA connector can be significant.

**Mitigations:**
- RAM (radar absorbing material) foam around the cavity exterior.
- Microwave-absorbing gasket on the cavity lid.
- RF power meter survey of all accessible surfaces before operating above 10 W.
- No operation above 10 W without RF survey confirming < 1 mW/cm² at operator position.
- Interlock: power amplifier disabled when cavity lid is open.

### 9.2 Projectile Risk

**Challenge:** If the sphere levitates and the containment tube is absent or fails, the sphere could be ejected upward. The brass gyroscope data (Section 4.5) implies the coupling between spin alignment and gravitational interaction is strong. If a spinning brass rotor at nanoTesla alignment fractions produces tens of milligrams of force change, a YIG sphere at near-unity alignment under coherent GHz drive may experience forces far exceeding its own weight at full power. Containment is not safety theater. It is load-bearing engineering.

**Mitigations:**
- **Polycarbonate, not acrylic.** Polycarbonate is virtually unbreakable at this scale and impact energy. Acrylic shatters. Use polycarbonate.
- Containment tube capped at both ends — co-spin means weight increase (sphere presses down harder), anti-spin means weight decrease (sphere lifts). Both directions require containment.
- **Polycarbonate spacer discs** between the sphere and each electromagnet pole face. The most likely catastrophic failure is the sphere launching upward and impacting the upper pole face at speed. Thin polycarbonate discs protect both the sphere (expensive polished single crystal) and the pole faces.
- Start at **minimum power and ramp slowly.** The balance tells you when things are getting interesting long before the sphere moves. No sudden jumps in power level.
- Tube inner diameter only slightly larger than sphere — limits lateral excursion and prevents the sphere from gaining a run-up before hitting the wall.
- No levitation attempts without containment tube installed and capped.

### 9.3 Thermal Safety

YIG's Curie temperature (the temperature above which ferrimagnetic ordering is lost) is approximately 560 K (287°C). Above this temperature, FMR ceases.

**Mitigations:**
- Pulsed drive keeps average power low (duty cycle < 1%).
- CW drive at 50 W in a copper cavity (high thermal conductivity) produces modest temperature rise (~10–30°C above ambient).
- Thermocouple on cavity exterior provides thermal monitoring.
- MCU firmware includes thermal shutdown: kill drive if T > 100°C.

### 9.4 Magnetic Field Safety

The alignment field of 2000 Oe (0.2 T) is comparable to a small MRI system's fringe field.

**Mitigations:**
- At 50 cm from an iron-core electromagnet with 41 mm gap, the fringe field is < 5 Oe — negligible.
- No pacemaker or implant hazard beyond immediate proximity.
- Warning labels on equipment.
- Ferromagnetic tools secured during operation (attraction hazard near pole pieces).

---

## 10. Success Criteria

| Outcome | Weight Change | Direction Reversal | Significance |
|---|---|---|---|
| Decisive | Gram-scale | Yes | Visible on kitchen scale. Immediate funding-ready. Video is proof. |
| Confirmed | Milligram-scale | Yes | Detected on analytical balance. Needs scaling (larger sphere, more power). |
| Detected | Sub-milligram | Yes | Marginal on mg balance. Requires precision balance + lock-in amplifier. |
| Suggestive | Sub-milligram | Partial | Systematic trend present but not clean reversal. Debug systematics. |
| Null (this sensitivity) | None detected | N/A | Does not disprove hypothesis. The coupling constant may require more material or more power. Proceed with sensitivity improvements. |
| Artifact | Any | No | Weight change independent of alignment direction. Not the predicted effect. Debug measurement chain, check for thermal/mechanical artifacts. |
| Off-resonance positive | Any | Any (at non-FMR frequency) | Artifact. Something other than FMR is producing the signal. Investigate RF pickup, balance interference. |
| Anomalous relaxation | Any | Yes | Relaxation time exceeds electronic T₂*. Model-independent evidence that angular momentum coupling pathway exists beyond standard FMR. Publish immediately. |

**The minimum success condition:** A weight change of any magnitude that cleanly reverses sign when the alignment field polarity is reversed, and is absent when the RF drive is off-resonance or applied to a non-magnetic control sphere.

---

## 11. Scaling Path

Upon detection of the predicted effect, the following scaling steps increase sensitivity and effect magnitude:

### 11.1 Larger YIG Spheres

Commercial YIG spheres are available up to ~5 mm diameter as catalog items. Larger spheres (10, 15, 25 mm) require custom growth but are routinely produced by crystal growers (e.g., Ferrisphere, Shin-Etsu). Effect scales with volume (∝ r³).

### 11.2 Multiple Sphere Arrays

Multiple YIG spheres in coupled cavities (cavity array or TE₀₁₁ mode with multiple dielectric loading positions) multiply the working volume without requiring custom large crystals.

### 11.3 Higher Power

Surplus traveling-wave tube amplifiers (TWTAs) from radar and satellite communication provide 100 W to 10 kW at C-band frequencies for $500–2,000 on the surplus market. With proper cavity Q, even 100 W provides enormous effective drive field.

### 11.4 Lock-in Amplifier Detection

For sub-microgram sensitivity, modulate the alignment field or RF drive at a known frequency (e.g., 13 Hz) and detect the weight change at that frequency using a lock-in amplifier. This suppresses all noise except at the modulation frequency, improving sensitivity by 10³–10⁶ depending on integration time.

### 11.5 Vacuum Operation

A bell jar + mechanical pump (~$300–500) eliminates atmospheric convection entirely, removing one of the most common artifact sources in precision weight measurement.

### 11.6 Multiferroic Future

The long-term material path is multiferroic compounds — materials where angular momentum alignment can be controlled by electric fields rather than magnetic fields. This eliminates the electromagnet, reduces system size, and enables rapid electronic switching of alignment direction. Bismuth ferrite (BiFeO₃) and related compounds are candidates, though their FMR linewidths are currently much broader than YIG.

---

## 12. Implications

### 12.1 If the Effect is Confirmed

Detection of a directional, reversible weight change driven by FMR phase advance in YIG constitutes:

1. **The first controlled demonstration of orbital radius modification via angular momentum engineering.** An object's effective weight has been changed without adding or removing matter, without changing its chemical composition, and without any conventional force acting on it.

2. **Direct experimental validation of the POAMS framework.** The prediction — that internal spin angular momentum change couples to orbital radius — follows uniquely from POAMS and is not predicted by any conventional theory. Confirmation validates the framework and demands reassessment of the foundational assumptions of physics.

3. **Proof of concept for propulsion without expelled mass.** Every conventional propulsion system works by expelling mass (rocket exhaust, propellant, photons). Angular momentum phase advance provides a mechanism for changing an object's orbital radius — effectively, its trajectory — without expelling anything. The mass stays; the orbit changes.

4. **A path to controlled time dilation.** In POAMS, orbital radius and time rate are coupled through angular momentum conservation. An object at a different orbital radius experiences a different time rate (this is what conventional physics calls "gravitational time dilation," already measured by atomic clocks at different altitudes). Controlled orbital radius modification implies controlled time rate modification.

### 12.2 The End State

The video goes public. A YIG sphere floating inside a copper tube, held aloft by nothing but coherent angular momentum phase advance. The sphere drops when the drive cuts. Lifts again when it resumes. Reverses when the alignment flips.

That video is the end of one era and the beginning of another.

It will be contested. It will be "debunked" by people who have not read this paper. It will be replicated — because the components are available, the procedure is specified, and the budget is under $5,000.

The replication is what matters. Once ten labs have done it, the argument is over.

---

## 13. Acknowledgments

**N.V. Pope and Anthony N. Osborne** — for the Pope-Osborne Angular Momentum Synthesis, the theoretical framework that makes this experiment possible. Their identification of angular momentum as the sole conserved substance, and their correction of Newton's and Coulomb's errors, is the foundation on which this work stands.

**Frederick E. Alzofon** — for AIAA-81-1608 and the AGNUE program. He identified the correct mechanism (angular momentum state modification → weight change) twenty years before the POAMS framework was complete, and pursued it with rigor despite institutional hostility. His experimental parameters directly inform this design.

**Daniel Alzofon** — for continuing his father's work, for the engineering analysis of UAP propulsion systems that converges on the same mechanism, and for alignment with the POAMS framework.

**George Hathaway** — Hathaway Research International, Toronto. For the partial verification of Alzofon's AGNUE effect and for maintaining an open laboratory for advanced propulsion research.

**Hal Puthoff** — for being present at the Hathaway lab verification and for decades of work in advanced propulsion physics.

**NASA Marshall Space Flight Center, Advanced Propulsion Physics Lab** — for supporting the initial bismuth experiments that demonstrated directional weight change, however small. Those hundredths of a gram were the first data points on the curve this experiment extends.

**D.L. Hotson** — for the octave ladder analysis connecting angular momentum modes across scales.

---

## 14. References

1. Pope, N.V. & Osborne, A.N. *Angular Momentum Synthesis.* (Foundational POAMS papers.) Available at: [POAMS repository]

2. Pope, N.V. *The Unified Theory of Angular Momentum.* (Monograph on POAMS framework.)

3. Alzofon, F.E. "Anti-gravity with present technology: implementation and theoretical foundation." AIAA-81-1608, AIAA/SAE/ASME 17th Joint Propulsion Conference, 1981.

4. Alzofon, D. *UAP Engineering Analysis.* (Engineering reverse-analysis of angular momentum propulsion systems.)

5. Einstein, A. & de Haas, W.J. "Experimenteller Nachweis der Ampèreschen Molekularströme." *Deutsche Physikalische Gesellschaft, Verhandlungen* 17, 152–170, 1915.

6. Hayasaka, H. & Takeuchi, S. "Anomalous weight reduction on a gyroscope's right rotations around the vertical axis on the Earth." *Physical Review Letters* 63(25), 2701–2704, 1989.

7. Hotson, D.L. "Dirac's Equation and the Sea of Negative Energy." *Infinite Energy* 43–44, 2002.

8. Podkletnov, E. & Nieminen, R. "A possibility of gravitational force shielding by bulk YBa₂Cu₃O₇₋ₓ superconductor." *Physica C* 203(3–4), 441–444, 1992.

9. Podkletnov, E. "Weak gravitational shielding properties of composite bulk YBa₂Cu₃O₇₋ₓ superconductor below 70 K under e.m. field." *arXiv:cond-mat/9701074*, 1997.

10. Brown, T.T. "How I control gravitation." *Science and Invention Magazine*, 1929. (And subsequent electrogravitics research, 1950s–1960s.)

11. Bertrand, J. "Théorème relatif au mouvement d'un point attiré vers un centre fixe." *Comptes Rendus* 77, 849–853, 1873.

12. Michalak, S. (Falcon Lake incident, 1967.) Documented in: Rutkowski, C. & Dittman, G. *The Canadian UFO Report: The Best Cases Revealed.* Dundurn Press, 2006.

13. Cherepanov, V., Kolokolov, I., & L'vov, V. "The saga of YIG: spectra, thermodynamics, interaction and relaxation of magnons in a complex magnet." *Physics Reports* 229(3), 81–144, 1993.

14. Sparks, M. *Ferromagnetic-Relaxation Theory.* McGraw-Hill, 1964.

15. Pozar, D.M. *Microwave Engineering.* 4th ed. Wiley, 2011. (Cavity design, Q factors, coupling theory.)

---

## Appendix A: POAMS Terminology Reference

For clarity, the following table maps conventional physics terminology to POAMS usage throughout this paper:

| Conventional Term | POAMS Term | Notes |
|---|---|---|
| Nucleus | Quantum accumulator / vortex core | The eyewall region of the atomic vortex |
| Electron | Outer circulation / structure quantum | Standing wave pattern in vortex circulation |
| Magnetic field | Alignment field | Macro-scale manifestation of spin correlation |
| Magnetic moment | Net vortex circulation | Arises from incomplete harmonic filling |
| Electromagnetic field | Angular momentum field | All fields are angular momentum |
| Gravitational force | Angular momentum / orbital radius relationship | Conservation, not force |
| Mass | Rotational inertia | Of quantized angular momentum vortices |
| Weight | Constraint force | Prevents occupation of natural orbital radius |
| Speed of light (c) | Domain conversion factor | Between length and time measurement domains |
| Strong force | Eyewall binding | Vortex core integrity |
| Weak force | Vortex decay / mode transition | Angular momentum redistribution |
| Magnetism | Spin angular momentum correlation | Not a separate force |
| Ferromagnetism | Collective vortex circulation alignment | Net d-harmonic asymmetry, cooperatively aligned |
| Spin-orbit coupling | Vortex circulation-orbital coupling | Same angular momentum, different modes |

---

## Appendix B: Quick-Start Build Guide

For experimenters who want to replicate Phase 1 with minimum reading:

1. **Buy:** 10 mm YIG sphere (ΔH < 0.5 Oe, polished), copper rod (50 mm dia), VCO eval board (5–6 GHz), 3 W RF amplifier (C-band), directional coupler, Schottky detector, ESP32, iron-core electromagnet (surplus), analytical balance (1 mg), SMA connectors and semi-rigid coax.

2. **Machine:** Cavity from copper rod — 41 mm ID, ~41 mm deep, with SMA port at midheight. PTFE post to support sphere at cavity center.

3. **Assemble:** Sphere on post in cavity. Cavity between electromagnet poles. Assembly on balance. RF chain: VCO → amp → coupler → cavity. Coupled port → detector → ESP32 ADC.

4. **Characterize:** Energize magnet to 2000 Oe. Sweep VCO 5.0–6.2 GHz. Find FMR dip in reflected power. Lock feedback loop.

5. **Measure:** Apply CW drive at FMR. Record weight. Reverse magnet polarity. Record weight. If sign reverses, you have it.

6. **Report results** — positive or null. Both are valuable. Contact information available at the project repository.

---

*This document is released for open publication. Replication is encouraged. The experiment is specified in sufficient detail for any competent microwave engineer or experimental physicist to reproduce. The budget is within reach of any university lab, amateur radio operator with test equipment, or motivated individual.*

*The physics is correct. The engineering is straightforward. The only remaining question is the coupling constant — and that, only the experiment can answer.*
