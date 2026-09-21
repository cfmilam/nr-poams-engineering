# EXP-S3 — Gyro Spin–Orbit Exchange Protocol

**Status:** preregistered engineering protocol; no positive effect is claimed by this document<br>
**Date:** 2026-09-20<br>
**Framework:** Normal Realism / Pope–Osborne Angular Momentum Synthesis (NR-POAMS)<br>
**Authors:** Star Lord, Parzival<br>
**Public theory boundary:** [`spin-orbit-settlement-ledger.html`](https://cfmilam.github.io/nr-poams-exhibits/spin-orbit-settlement-ledger.html)<br>
**Method boundary:** [`translation-ledger.html`](https://cfmilam.github.io/nr-poams-exhibits/translation-ledger.html)

*This protocol is an extrapolation of the foundational work of N. Vivian “Viv” Pope and Dr. Anthony D. Osborne, PhD. It converts reported mechanical-gyro behavior into measurements, controls, and promotion gates. The reports motivate the test; they are not evidence that an anomalous exchange exists.*

---

## 0. Registered question and status boundary

**Question.** After ordinary bearing, drive, support, magnetic, electrical, aerodynamic, thermal, acoustic, and vibration accounts are measured, does a mechanical gyro exhibit a reproducible torque or power component that is odd under reversal of the local spin/orbit sense?

The primary sense variable is

$$
\sigma=\operatorname{sgn}(\mathbf S_{\mathrm{rotor}}\!\cdot\!\mathbf L_{\mathrm{containing}}),
$$

where $\mathbf L_{\mathrm{containing}}$ is the preregistered platform-orbit component about the declared local centre. It is one typed component of the complete apparatus ledger in §1, not a synonym for every non-rotor angular-momentum stock. **Co-sense** $(\sigma=+1)$ and **anti-sense** $(\sigma=-1)$ are prepared at matched magnitudes and trajectories.

This protocol preserves four public boundaries:

1. **GROUNDING §4.0 supplies orientation order only.** Where spin and its immediate containing orbit are dynamically coupled, anti-sense is the higher organization and an available path settles toward co-sense. Section 4.0 does **not** supply a universal energy gap, torque, coupling coefficient, transfer fraction, terminal angle, latency, relaxation time, orbit shift, or apparatus magnitude.
2. **C1 remains a named constitutive premise in a declared unresolved regime.** Conservation proves that an aggregate internal angular momentum exists; it does not prove that a parent exchange sees only that aggregate. Any C1 use must state what the parent cannot resolve and must pass the regrouping test in §11. Directly resolved rotor/platform measurements do not need C1.
3. **The numerical origin of $\alpha$ remains open.** Measured $\alpha$ may be used only as a disclosed calibration where relevant. This protocol creates no Machian/global-rate route and no constant derivation.
4. **Venus remains a quantitative falsification/scaling gate, not an explanation.** No bench coefficient may be transferred to Venus, a galaxy, or any other scale until a preregistered scale law survives the laboratory matrix in §10.

A null result is valid. A loud or violent result without closed books is not.

---

## 1. Complete angular-momentum boundary

Freeze one exposure cut $\mathcal B$ before data collection. Everything is assigned exactly once: either it is a stock inside $\mathcal B$, or it exchanges angular momentum across the boundary. The minimum inside account is

$$
\boxed{\mathbf J_{\mathcal B}=\mathbf S_{\mathrm{rotor}}+\mathbf L_{\mathrm{platform}}},
\qquad
\boxed{\Delta\mathbf J_{\mathcal B}=\int_{t_0}^{t_1}\!\mathbf N_{\partial\mathcal B}^{\mathrm{in}}(t)\,dt}.
$$

- $\mathbf S_{\mathrm{rotor}}=I_r\boldsymbol\omega_r$: **only** the test rotor's intrinsic spin about its centre of mass.
- $\mathbf L_{\mathrm{platform}}$: every other angular-momentum stock inside $\mathcal B$, counted once. It includes the test rotor centre-of-mass orbit, tray/platform motion, gimbals, bearings, onboard motor/brake rotors, and other moving in-boundary parts, including both orbital and intrinsic contributions where applicable. It excludes $\mathbf S_{\mathrm{rotor}}$.
- $\mathbf N_{\partial\mathcal B}^{\mathrm{in}}$: net torque exerted on the inside by everything outside $\mathcal B$, measured at mounts, shafts, cables, hoses, electrical feedthroughs, air/chamber interfaces, operator contacts, floor, and Earth as applicable.

The complementary support/Earth reservoir posting is a **derived boundary flux**, not a second list of the same apparatus parts. Denote it by $\Delta\mathbf J_R$:

$$
\Delta\mathbf J_R
\equiv-\int_{t_0}^{t_1}\!\mathbf N_{\partial\mathcal B}^{\mathrm{in}}(t)\,dt.
$$

$$
\Delta\mathbf S_{\mathrm{rotor}}+\Delta\mathbf L_{\mathrm{platform}}+\Delta\mathbf J_R=0.
$$

A motor, gimbal, bearing, frame, or cable physically inside $\mathcal B$ belongs only to $\mathbf L_{\mathrm{platform}}$; the same object may not also be entered in $\mathbf J_R$. Moving the exposure cut between campaigns is allowed only if every stock and boundary flux is redefined and the analysis is repeated.

### 1.1 Required vector postings

For every event window report, in a common inertial or explicitly transformed frame,

$$
\Delta\mathbf S_{\mathrm{rotor}},\qquad
\Delta\mathbf L_{\mathrm{platform}},\qquad
\int\!\mathbf N_{\partial\mathcal B}^{\mathrm{in}}\,dt,
$$

and the closure residual

$$
\boldsymbol\epsilon_J=
\Delta\mathbf S_{\mathrm{rotor}}+\Delta\mathbf L_{\mathrm{platform}}
-\int\!\mathbf N_{\partial\mathcal B}^{\mathrm{in}}\,dt.
$$

The uncertainty budget for $\boldsymbol\epsilon_J$ is part of the result. A scalar RPM trace is insufficient where the axis moves.

---

## 2. Complete energy/source/recipient account

Use the same frozen boundary $\mathcal B$. Stocks retained inside and fluxes crossing $\partial\mathcal B$ are mutually exclusive. Define the total stored-energy change as

$$
\begin{aligned}
\Delta E_{\mathcal B}^{\mathrm{stored}}
&\equiv\Delta K_{\mathrm{rotor}}+\Delta K_{\mathrm{platform}}+\Delta E_{\mathrm{elastic}}\\
&\quad+\Delta U_{\mathrm{internal}}+\Delta E_{\mathrm{other,stored}}.
\end{aligned}
$$

The closure equation is then

$$
\boxed{W_{\partial\mathcal B}^{\mathrm{in}}-W_{\partial\mathcal B}^{\mathrm{out}}
=\Delta E_{\mathcal B}^{\mathrm{stored}}}.
$$

- $K_{\mathrm{rotor}}$ is only the test rotor's intrinsic spin kinetic energy.
- $K_{\mathrm{platform}}$ contains every other in-boundary kinetic store counted once: rotor centre-of-mass orbit, tray/platform, gimbals, bearings, onboard drive rotors, and other moving parts.
- $\Delta U_{\mathrm{internal}}$ contains energy retained inside $\mathcal B$ at the endpoint as heat, unresolved internal vibration, deformation, or other internal modes.
- $W_{\partial\mathcal B}^{\mathrm{in/out}}$ are signed transfers across the boundary: electrical/mechanical drive work, exported or imported shaft work, heat crossing the boundary, radiated/exported acoustic or vibration energy, aerodynamic work, and any recovered energy.

A joule is posted once. For example, vibration retained inside at $t_1$ belongs to $\Delta U_{\mathrm{internal}}$; vibration exported through mounts belongs to $W_{\partial\mathcal B}^{\mathrm{out}}$; vibration later thermalized inside is not entered again as both vibration and heat. Likewise an onboard motor belongs to the kinetic/internal stocks, while electrical energy entering through its feedthrough is a boundary flux.

| Exclusive account | Required measurement or bound | Posting rule |
|---|---|---|
| Test-rotor spin stock | $I_r$, $\boldsymbol\omega_r(t)$, $K_r(t)=\tfrac12\boldsymbol\omega_r^TI_r\boldsymbol\omega_r$ | Intrinsic rotor energy only |
| Other in-boundary kinetic stocks | inertias/rates/trajectory of platform, gimbals, drives, and rotor COM | Each moving part once; excludes test-rotor spin |
| Elastic/internal stocks | strain, calibrated temperatures/heat capacity, bounded modal energy | Endpoint energy still inside $\mathcal B$ |
| Electrical/mechanical boundary work | synchronized voltage/current and boundary force/torque × velocity/rate | Signed flux into or out of $\mathcal B$ |
| Exported heat | calibrated heat-flow across $\partial\mathcal B$ | Outward flux; not retained internal heat |
| Exported vibration/acoustics | boundary accelerometry/force or calibrated acoustic intensity | Outward flux; not later counted again as heat |
| Aerodynamic/pressure work | pressure, gas composition, flow/drag model and controls | Boundary flux and ordinary confound |
| Recovered work | regeneration or measured work returned across $\partial\mathcal B$ | Outward flux, explicitly signed |

Energy closure is evaluated over the same registered windows as angular impulse. Do not infer power from sound level, motor current alone, or endpoint RPM alone.

---

## 3. Endpoint/path distinction — mandatory reading rule

For a fixed-magnitude reversal about a measured principal axis with axial moment $I_{\mathrm{axis}}$,

$$
\mathbf S_f=-\mathbf S_i,
\qquad
|\Delta\mathbf S|=2|\mathbf S|=2I_{\mathrm{axis}}|\omega_r|,
\qquad
\Delta K_{\mathrm{spin}}=0.
$$

The equal endpoint kinetic energies do **not** imply zero angular impulse, zero gross path work, or zero dissipation. The path may require large positive and negative work exchanges while ending with the same $K_{\mathrm{spin}}$; bearings, supports, motors, brakes, sound, vibration, and heat can receive energy throughout it.

Therefore every reversal report must include both:

- endpoint state functions: $\mathbf S_i,\mathbf S_f,K_i,K_f$;
- path quantities: $\int\mathbf N\,dt$, signed and gross work, heat, vibration/acoustics, trajectory, and duration.

---

## 4. Apparatus and synchronized instrumentation

### 4.1 Minimum apparatus

1. Rotor with measured mass properties and replaceable rotor bodies/inertias.
2. Three-axis gimbal capable of a documented **free-axis** state and a mechanically documented **locked-gimbal** state.
3. Driven platform/tray capable of straight translation, controlled local orbit, orbit reversal, and orbit stop with the same payload.
4. Instrumented platform drive/brake and support reactions.
5. Rotor tachometry plus full axis attitude tracking; optical tracking is preferred as an independent channel.
6. Common-clock acquisition for torque, attitude, trajectory, rate, electrical power, temperatures, pressure, accelerometers, and acoustics.

### 4.2 Minimum timing discipline

All channels share one clock or carry a measured clock offset and drift correction. Register:

- sampling rate and anti-alias filtering;
- trigger definitions;
- sensor latency and timestamp uncertainty;
- the slowest channel that limits the event timing claim.

If response onset is indistinguishable from orbit onset within resolution $\delta t$, report **“latency not resolved; bounded by $\delta t$”**. Never report “instantaneous,” “zero-time,” or an infinite/undefined coupling coefficient.

---

## 5. Matched preparation matrix

The core design is a matched $2\times2$ preparation:

| Local sense | Free-axis path | Locked-gimbal path |
|---|---|---|
| Co-sense, $\mathbf S\cdot\mathbf L>0$ | `CO-FREE` | `CO-LOCK` |
| Anti-sense, $\mathbf S\cdot\mathbf L<0$ | `ANTI-FREE` | `ANTI-LOCK` |

Match or model-correct, before unblinding:

- $|\mathbf S|$, rotor temperature, run age after spin-up;
- $|\boldsymbol\Omega_c|$, orbit radius, acceleration, and trajectory profile;
- platform mass/inertia and payload placement;
- reversal jerk and duration;
- bearing preload/lubrication and gimbal friction;
- cable routing, magnetic environment, pressure, and thermal state.

Randomize run order in balanced blocks. Use coded sense labels during primary reduction where practical. Predeclare exclusion rules; do not remove “ugly” grinding runs after seeing the sign.

---

## 6. Five preregistered apparatus gates

These gates test preparation specificity and branch structure. Passing a gate is **not** by itself evidence for a new coupling; the odd-under-sense, closure, control, and scaling requirements in §§7–13 still apply.

### G1 — Translation-null

**Preparation:** Move the spinning, free-gimbal apparatus through registered straight paths, including direction changes and changes of distance from candidate local centres, while matching linear speed and acceleration to the orbit runs as closely as the apparatus permits.

**Pass condition:** No reproducible axis-flip, odd torque/power, or settled-axis response above the preregistered sensitivity follows translation alone.

**Purpose:** Distinguish angular winding about a named centre from translation, start/stop impulse, cable drag, or generic acceleration.

### G2 — Orbit-onset

**Preparation:** Transition from the translation control into a local orbit with declared centre, radius, plane normal, and containing rate $\boldsymbol\Omega_c$, without changing rotor preparation.

**Pass condition:** A candidate response begins reproducibly only after the orbit account becomes nonzero and follows the predeclared onset statistic. Timing is reported at instrument resolution only.

**Failure/alternative:** A response during matched translation or before orbit onset identifies an ordinary motion/startup coupling or falsifies the claimed preparation specificity.

### G3 — Plane-tracking

**Preparation:** With the gimbal free, vary the local orbital plane through at least three registered orientations while holding $|\mathbf S|$, $|\boldsymbol\Omega_c|$, radius, and support geometry fixed as closely as possible.

**Pass condition:** The settled rotor-axis relation tracks the local orbital plane/normal with the registered sign and angular uncertainty, rather than the bench normal, camera frame, magnetic axis, or a fixed bearing bias.

**Required output:** Full attitude trajectory, terminal angle distribution, and lag bound—not a video-only judgment.

### G4 — Orbit-off hierarchy-switch

**Preparation:** After a free-axis local-orbit run, stop the local orbit while leaving the gimbal free. Continue attitude recording long enough to resolve the next stable orientation or place a bound on it.

**Registered hypothesis:** If the reported immediate-edge hierarchy is physical, the former local-plane preference should disappear after orbit-off and the next candidate containing circulation for this bench is Earth's rotation, giving a preregistered latitude-dependent direction. A null, a fixed apparatus direction, or a different reproducible direction is retained as a valid outcome.

**Pass condition:** The measured post-stop direction distribution discriminates the registered Earth-axis hypothesis from the null and apparatus-fixed alternatives at the preregistered uncertainty; no outcome is relabeled after unblinding.

**Boundary:** This gate tests a specific immediate-edge hypothesis. It does not assume or prove a universal hierarchy law, C1, an Earth coupling magnitude, or zero latency.

### G5 — Locked-gimbal branch

**Preparation:** Repeat the matched anti-sense local-orbit run with the geometric reorientation path mechanically locked; include matched co-sense locked controls.

**Pass condition:** Relative to the free-axis branch, the locked branch shows a quantitatively closed redistribution through rotor spin-down and/or support/platform impulse, work, heat, vibration, and acoustics. Any threshold at which the rotor “no longer matters” must be stated in sensor units.

**Failure/alternative:** Grinding or rapid spin-down fully explained by ordinary lock friction, misalignment, bearing load, or drive control is not anomalous and must be reported as such.

---

## 7. Primary observables

Report raw time series, calibration, uncertainty, and registered reduction code for:

1. **Rotor vector AM:** $\mathbf S(t)=I_r\boldsymbol\omega_r(t)$.
2. **Containing orbit:** $\boldsymbol\Omega_c(t)$, declared orbit centre, radius/acceleration, plane normal, and platform trajectory $\mathbf x(t)$.
3. **Torque:** vector support/drive torque $\mathbf N(t)$ at every instrumented boundary.
4. **Angular impulse:**
   $$
   \mathbf I_J=\int_{t_0}^{t_1}\mathbf N(t)\,dt.
   $$
5. **Power/work:** synchronized mechanical and electrical power; signed work and gross positive work over the event window.
6. **Energy recipients:** heat, structural vibration, airborne/structure-borne acoustics, bearing temperature, and recovered mechanical energy.
7. **Attitude response:** rotor-axis trajectory, terminal angle, reorientation rate, overshoot, ring-down, and event duration.
8. **Environment:** pressure/vacuum, gas temperature, magnetic field, electrical leakage/ground currents, ambient vibration, and apparatus temperature map.

### 7.1 Odd-under-sense observables

Before data collection choose a signed torque projection $q$ in a declared coordinate frame and a specific measured boundary-power channel. For matched anti-sense and co-sense runs reduced with the same pipeline,

$$
\boxed{N_{\mathrm{odd},q}(t)=\frac{N_{\mathrm{anti},q}(t)-N_{\mathrm{co},q}(t)}{2}}.
$$

$$
\boxed{P_{\mathrm{odd}}(t)=\frac{P_{\mathrm{anti}}(t)-P_{\mathrm{co}}(t)}{2}}.
$$

Also report vector/even torque components and even power; an ordinary loss may be large and sense-even. The power estimand is measured independently from the exclusive boundary-energy ledger. For any proposed torque-work channel, calculate separately

$$
P_N(t)=\mathbf N_{\partial\mathcal B}^{\mathrm{in}}(t)\!\cdot\!\boldsymbol\omega_{\mathrm{rel}}(t)
$$

and test whether its odd component agrees with the independently measured $P_{\mathrm{odd}}$. Do not infer total odd power by multiplying an odd torque from one run pair by an unmatched or absolute angular rate.

Integrated primary estimands are

$$
I_{\mathrm{odd},q}=\int N_{\mathrm{odd},q}(t)\,dt,
\qquad
W_{\mathrm{odd}}=\int P_{\mathrm{odd}}(t)\,dt.
$$

A claimed sign reversal must be present in independent torque/impulse and energy channels, not manufactured by subtracting unmatched trajectories.

---

## 8. Mandatory controls

Each control is run in the same balanced/randomized structure as the primary preparation.

1. **Sham reversal:** execute the command sequence and platform profile without reversing the physical spin/orbit sense; include coded false reversals.
2. **Rotor-off / low-spin sham:** same platform trajectory with $|\mathbf S|$ below a registered threshold.
3. **Bearing control:** dummy rotor or matched inertia with ordinary bearing/gimbal loads; independently map friction versus orientation, speed, preload, and temperature.
4. **Magnetic control:** map ambient and motor fields; repeat with nonmagnetic hardware where feasible and with equivalent field changes but no sense reversal.
5. **Electrical control:** monitor ground current, cable torque, slip-ring drag, motor-controller asymmetry, regeneration, and sensor pickup; swap drive channels/polarity without changing mechanics.
6. **Aerodynamic control:** repeat across pressure levels, including vacuum where feasible; model windage and convection from measured pressure and temperature.
7. **Thermal control:** matched heater runs reproducing the measured temperature history without rotor/orbit reversal.
8. **Pressure/vacuum control:** document chamber pressure, pump vibration, outgassing, and feedthrough forces throughout each event.
9. **Support-geometry control:** rotate, mirror, stiffen, and relocate support paths while preserving the intended $\mathbf S$ and $\mathbf L$ preparation.
10. **Trajectory control:** match linear acceleration/jerk and platform motor commands without closing an orbit.

A candidate survives a control only if the preregistered odd estimand remains while the control transfer function is too small to account for it.

---

## 9. Analysis and uncertainty registration

Before the first confirmatory run, freeze:

- event windows and baseline windows;
- torque/power sign conventions and coordinate transforms;
- filters, downsampling, drift correction, and sensor fusion;
- latency estimator and onset threshold;
- outlier/exclusion rules;
- minimum run count and stopping rule;
- uncertainty propagation and closure-residual thresholds;
- confirmatory statistic and effect-size interval;
- labels for exploratory analyses.

Exploratory findings may generate a later registered campaign; they do not retroactively become confirmatory.

---

## 10. Preregistered scaling matrix

One apparatus point cannot establish a transferable law. Before confirmatory data, register at least three levels where feasible for each factor:

| Factor | Required registration | Why it matters |
|---|---|---|
| Rotor $|S|$ | inertia/rate combinations, not RPM alone | Tests dependence on the actual spin account |
| Containing rate $|\Omega_c|$ | signed rate levels including zero | Tests orbit-rate dependence and translation/orbit distinction |
| Radius / centripetal acceleration | vary radius at matched rate and acceleration where possible | Separates winding rate, geometry, and ordinary load |
| Rotor size/mass | geometrically similar and deliberately non-similar rotors | Tests extensivity and hidden bearing/aero scaling |
| Reversal rate | multiple durations/jerks with matched endpoints | Separates endpoint sense from path forcing |
| Support geometry | at least two materially different load paths | Tests whether the response is an apparatus mode |
| Pressure | air/intermediate/vacuum where feasible | Bounds windage, convection, and acoustic transfer |

### 10.1 Candidate scale laws to test—not assume

A first torque candidate for the preregistered projection $q$ may be

$$
\boxed{N_{\mathrm{odd},q}=\chi_N|\mathbf S||\boldsymbol\Omega_c|},
\qquad
\chi_N=\frac{N_{\mathrm{odd},q}}{|\mathbf S||\boldsymbol\Omega_c|}.
$$

A separate power candidate may be

$$
\boxed{P_{\mathrm{odd}}=\chi_P|\mathbf S||\boldsymbol\Omega_c||\omega_{\mathrm{rel},q}|},
\qquad
\chi_P=\frac{P_{\mathrm{odd}}}{|\mathbf S||\boldsymbol\Omega_c||\omega_{\mathrm{rel},q}|}.
$$

Both coefficients are signed empirical normalizations under the declared $q$ convention. Evaluate the ratios only for nonzero $|\mathbf S|$, $|\boldsymbol\Omega_c|$, and—where used—$|\omega_{\mathrm{rel},q}|$; the zero levels are null controls, not divisions. The coefficients are not assumed equal. If one physical torque-work channel is proposed, preregister and test the additional relation

$$
P_{\mathrm{odd}}\stackrel{?}{=}N_{\mathrm{odd},q}\,\omega_{\mathrm{rel},q}
$$

against the independently measured boundary-power ledger; do not build that equality into data reduction.

These are **candidate empirical normalizations**, not POAMS theorems or planetary coefficients. Register in advance which interval of factors is claimed to leave $\chi_N$ or $\chi_P$ invariant. If radius, acceleration, size, reversal rate, pressure, or support geometry changes either coefficient, the law must be expanded and independently retested; it may not be averaged into a universal constant.

At least one preregistered scaling law must survive an out-of-sample apparatus configuration before promotion.

---

## 11. C1 regrouping gate, if invoked

C1—exterior-interface sufficiency—is allowed only in a named unresolved regime. If a claim treats a compound rotor assembly as one effective parent-visible spin:

1. state which internal phases, separations, multipoles, spectra, and dissipation channels the parent instrument cannot resolve;
2. calculate the response once from resolved subaccounts and once from the declared aggregate $\mathbf J_{\mathrm{int}}$;
3. regroup the same primitives in at least two legitimate ways;
4. require agreement within the preregistered uncertainty.

Failure means the aggregate is insufficient in that regime. It does not violate AM conservation; it rejects that C1 application.

---

## 12. Promotion criteria

EXP-S3 advances from **reported behavior** to a **candidate measured spin–orbit exchange** only if all are satisfied:

1. **Sense reversal:** the primary response reverses with $\mathbf S_{\mathrm{rotor}}\cdot\mathbf L_{\mathrm{containing}}$ in matched co/anti preparations.
2. **Closed AM books:** $\Delta\mathbf S_{\mathrm{rotor}}+\Delta\mathbf L_{\mathrm{platform}}-\int\mathbf N_{\partial\mathcal B}^{\mathrm{in}}dt=0$ within the registered uncertainty, using one frozen exposure cut.
3. **Closed energy books:** $W_{\partial\mathcal B}^{\mathrm{in}}-W_{\partial\mathcal B}^{\mathrm{out}}$ reconciles the mutually exclusive in-boundary kinetic, elastic, internal, and other stored-energy changes within uncertainty; no packet is posted both as a retained stock and an exported recipient.
4. **Control survival:** sham reversal plus bearing, magnetic, electrical, aerodynamic, thermal, pressure/vacuum, trajectory, and support-geometry controls are too small to explain the odd component.
5. **Branch prediction:** free-axis and locked-gimbal outcomes differ in the registered direction and both close their books.
6. **At least one preregistered scaling law survives** factor variation and an out-of-sample apparatus configuration.
7. **Independent replication:** a separately built apparatus reproduces the registered sign and scale behavior before any universal or cross-scale claim.

Passing only the five apparatus gates is apparatus characterization, not promotion.

---

## 13. Explicit prohibitions

The following are not sufficient evidence and must not appear in a success claim:

- loud grinding, violent movement, a felt reaction, or a dramatic video without calibrated torque, angular impulse, work, and closure;
- near-zero observed latency restated as “instantaneous”;
- endpoint $\Delta K_{\mathrm{spin}}=0$ restated as zero impulse, zero gross work, or zero dissipation;
- a sign-blind excess treated as spin/orbit exchange;
- topology $Lk=Tw+Wr$ treated as a torque, energy, or coefficient;
- C1 treated as a theorem or universal premise;
- §4.0 treated as a universal $-K\mathbf S\cdot\mathbf L$ potential, torque law, timescale, exact-alignment law, or transfer fraction;
- one bench coefficient transferred to Venus, a galaxy, an atom, or another apparatus without a surviving scale law;
- Venusian climate, volcanism, or atmosphere treated as evidence for the laboratory effect;
- measured $\alpha$, a fitted constant, or a Machian/global-rate hypothesis inserted into the apparatus result.

---

## 14. Outcome language

Use one of these final grades:

- **NULL:** no odd-under-sense response above the registered sensitivity; report the excluded region for the tested scale law.
- **ORDINARY APPARATUS RESPONSE:** a signal exists but is closed by bearing, drive, support, magnetic, electrical, aerodynamic, thermal, pressure, or trajectory controls.
- **UNRESOLVED CANDIDATE:** an odd response survives some controls but AM/energy closure, branch behavior, or scaling is incomplete.
- **PROMOTED CANDIDATE EXCHANGE:** all §12 criteria except independent replication are satisfied.
- **REPLICATED EXCHANGE:** an independent apparatus satisfies the registered sign, closure, controls, branch, and scaling gates.

No grade by itself licenses a Venus, galaxy, atomic, propulsion, or universal-coupling claim.

---

## 15. Run-registration block

Copy and freeze this block before each confirmatory campaign:

```text
Campaign ID / date:
Apparatus revision and photographs:
Frozen exposure cut B and inventory of in-boundary stocks:
Boundary AM-flux sensors/interfaces:
Boundary energy-flux sensors/interfaces:
Exclusive retained/exported heat-vibration-acoustic posting rules:
Rotor mass/inertia tensor and spin levels:
Platform inertia, centre, radius, plane, rate levels:
Free/locked implementation and measured friction:
CO/ANTI sign convention, L_containing definition, and coordinate frame:
Randomized run order / blinding code:
Five gate definitions and pass thresholds:
Primary N_odd,q, P_odd, I_odd,q, W_odd channels:
Event/baseline windows and filters:
Latency resolution and estimator:
AM closure threshold:
Energy closure threshold:
Control matrix:
Scaling factors, levels, and candidate law:
Stopping/exclusion rules:
Confirmatory statistic and uncertainty method:
Raw-data, calibration, code, and checksum locations:
```

The registration is append-only. Corrections after data acquisition are labeled exploratory and dated.
