---
{layout: reader, title: "λ-partition and the magnitude of a YIG drive-toggle response"}
---
# λ-partition and the magnitude of a YIG drive-toggle response

**Final public research edition — 2026-11-11. Outcome class: CONDITIONAL.**

The useful question is quantitative: **what fractional change in support weight, $$\lvert\Delta w/w\rvert$$, would switching a YIG drive on and off produce through the Appendix-5 variable-G channel?** The proposed intervention holds the static preparation fixed and introduces a bounded cone of collective orientation. The calculation separates the loss of aligned-twist projection from a possible orbital-winding contribution. Its largest unknown is one coefficient, the price assigned to aligned twist, **$$K_s$$**.

The consequence is practical. No price supported by current commitments reaches the build threshold for the microwave toggle on a 0.01 mg balance. A drive-off reversal, with qualified controls, can first bound or calibrate the conditional static coefficient. The accompanying [static-gate protocol](static-gate-protocol.html) freezes that test and the consequences of a null, a contrast or an ambiguous record.

This is a research-record derivation and a prospective program decision, not a measurement. No physical experiment, support contrast or bound is reported here. Source and numerical authority: **program research record, 2026-11-11**, including the independent **PASS-WITH-FINDINGS** re-review; its numerical corrections and interpretation limits govern this edition.

## 1. The source construction and its comparator

Pope's *Einstein's Lost Legacy*, Appendix 5, places intrinsic spin in the variable-G channel and points to Osborne and Pope (2007), chapters 6–7, for the quantitative construction. Equations (6.16)–(6.19) and (7.11)–(7.21) compose **kinetic energies**, not an undifferentiated sum of angular momenta:

$$
\begin{gathered}
F = \frac{m M (\mathcal{G}-G')}{R^2}, \qquad G' = \frac{R V^2}{M} \\
\frac{\mathcal{G}}{G} = \left(\frac{\mathcal{K}}{K_0}\right)^{1/2} \\
\mathcal{K}^2 = K_0^2 + K_s^2 + 2 K_0 K_s \cos\beta \\
L_o = m V R, \qquad v_0 = \frac{G M}{V R}, \qquad r_0 = \frac{V R}{v_0} \\
K_0 = \frac12 m v_0^2, \qquad \omega_0 = \frac{v_0}{r_0}, \qquad K_0 = \frac12 L_o \omega_0 \\
a = \frac{r_0}{R} = \frac{G'}{G}, \qquad \Gamma = \frac{1}{1-a}, \qquad \rho = \frac{K_s}{K_0}
\end{gathered}
$$

Here F is the support force in the source's held-path construction; w denotes its baseline weight. R is the Earth reference radius, V the equatorial surface speed, M the Earth mass, and β the angle between spin and the declared orbital angular-momentum axis.

**$$K_0$$ is the test body's hypothetical natural spinless Earth-orbit kinetic energy**, carrying the same angular momentum as its constrained daily Earth-rotation path. It is neither the Earth's own energy nor the sphere's roughly 293 J held-path kinetic energy. The approximately 22 km natural radius is a point-concentrated-Earth idealization in the source, not a measured trajectory inside the Earth.

At weak spin, $$\rho \ll 1$$, expansion gives the two response columns:

Intrinsic-twist projection:

$$
\frac{\delta w}{w} = +\Gamma \left[\frac{K_s}{2K_0}\right]\cos\beta + O(\rho^2)
$$

Orbital-numerator addition, to first order in $$\Delta L/L_o$$:

$$
\frac{\delta w}{w} = -2\Gamma a\frac{\Delta L}{L_o}
$$

Co-sense intrinsic twist is heavier in this construction. A co-sense orbital-numerator increment is lighter. These are different columns and different prices; naming angular momentum alone does not fix the support response.

## 2. The nominal spin store, by two routes

The adopted nominal specimen is a 1 cm YIG sphere of density 5.17 g/cm³, normalized to $$4\pi M_s = 1780\ \mathrm{G}$$. These are calculation inputs, not measurements of a selected article. The imported material census and constants were not independently replayed against primary external tables in the research record.

### Route 1 — magnetization

$$
\begin{aligned}
V_{\mathrm{sphere}} &= \frac{\pi d^3}{6} = 5.23598775598\times10^{-7}\ \mathrm{m^3} \\
m &= \rho_{\mathrm{material}} V_{\mathrm{sphere}} = 2.707005669843205\ldots\times10^{-3}\ \mathrm{kg} \\
M_s &= 1.41647899352\times10^5\ \mathrm{A/m} \\
\mu_{\mathrm{sat}} &= M_s V_{\mathrm{sphere}} = 0.0741666666666667\ \mathrm{A}\cdot\mathrm{m^2} \\
\lvert\gamma\rvert &= \frac{2\mu_B}{\hbar} = 1.75882001077\times10^{11}\ \mathrm{rad}\cdot\mathrm{s^{-1}}\cdot\mathrm{T^{-1}} \quad (g=2) \\
S &= \frac{\mu_{\mathrm{sat}}}{\lvert\gamma\rvert} = 4.21684232681124\times10^{-13}\ \mathrm{J}\cdot\mathrm{s}
\end{aligned}
$$

### Route 2 — normalized constituent census

The imported Y₃Fe₅O₁₂ formula mass is 737.930514 g/mol. This gives 2.20914691460×10²¹ formula units. The conventional ferrimagnetic census assigns 5 $$\mu_B$$ per formula unit at 0 K; its nominal magnetization is 2458.52 G. Normalizing it to the same adopted 1780 G multiplies it by 0.7240133832:

$$
\begin{aligned}
S &= 5 N_{\mathrm{formula}}\frac{\hbar}{2}\times0.7240133832 \\
&= 4.21684232681124\times10^{-13}\ \mathrm{J}\cdot\mathrm{s} \approx 4.2168\times10^{-13}\ \mathrm{J}\cdot\mathrm{s}
\end{aligned}
$$

The agreement is an algebraic identity after normalization: $$\mu/\gamma = (\mu/\mu_B)(\hbar/2)$$. It checks units and factors of 2π; it is **not two independent mechanical receipts**. Both routes yield a magnetic proxy. Converting that proxy to physical angular momentum requires the separate reaction/reciprocity receipt in the [program protocol](protocol.html). Magnetization and angular momentum are not interchangeable observations.

The electron-spin sign also matters operationally: angular momentum is antiparallel to magnetization. A physical co/anti mapping must be frozen, not inferred from the names of bias polarities.

## 3. What switching the drive changes

For a fixed-magnitude, uniform circular cone of half-angle θ about the bias axis, the time-averaged axial projection is multiplied by $$\cos\theta$$. The geometrical solid angle is $$2\pi(1-\cos\theta)$$, and the proposed axial displacement is $$S(1-\cos\theta)$$.

The calculation adopts **unchanged $$K_s$$ during tipping**. Drive-on therefore removes $$(1-\cos\theta)$$ of the drive-off twist projection. If, additionally, the coning displacement is physical writhe and can be posted to the Earth-orbital numerator, it supplies the second, much smaller term. That posting has no independent receipt and is retained only as a conditional ceiling. Internal winding is not automatically center-of-mass orbital motion.

This is a **bounded state held by a flow**. More elapsed RF cycles do not accumulate additional instantaneous S. A pulsed drive reduces the time-averaged response by its duty factor under the stated steady-state approximation.

## 4. Closed form and fixed constants

**Validity beside the formula:** equatorial reference geometry; weak spin $$K_s/K_0 \ll 1$$; first-order orbital increment; fixed-magnitude uniform coning; fixed $$K_s$$ on tipping; the adopted source support law. At the equator, $$g_{\mathrm{eq}}=\lvert\cos\beta\rvert$$ is only the bias-axis projection, with $$g_{\mathrm{eq}}=1$$ in the co-sense reference. It is not a general-latitude multiplier for both terms.

$$
\begin{aligned}
\left\lvert\frac{\Delta w}{w}\right\rvert &= (1-\cos\theta)\,g_{\mathrm{eq}}\,\Gamma\left[\frac{K_s}{2K_0}+2\frac{r_0}{R}\frac{S}{L_o}\right] \\
&= (1-\cos\theta)\,g_{\mathrm{eq}}\,\Gamma\frac{S}{L_o}\left[\frac{\Omega_s}{\omega_0}+\frac{2r_0}{R}\right]
\end{aligned}
$$

$$
\Omega_s \equiv \frac{K_s}{S}
$$

(mean price, not a differential preparation-path rate)

For the nominal specimen and modern WGS84 inputs substituted into the source equations:

| Quantity | Fixed reference value | Role |
|---|---:|---|
| $$K_0$$ | 24,437,249.848418309… J | Natural spinless-orbit energy comparator |
| $$L_o$$ | 8,030,273.952013946… J·s | Constrained equatorial Earth-rotation angular momentum |
| $$r_0$$ | 22,077.2317394063… m | Source-model natural radius |
| $$r_0/R$$ | 0.00346139189851305… | Held-path to natural-orbit ratio |
| $$\Gamma$$ | 1.0034734147481825853… | Support normalization |
| $$\omega_0$$ | 6.08628049166108… rad/s | Natural-orbit angular rate |
| S | 4.21684232681124×10⁻¹³ J·s | Conditional magnetic proxy from either normalized route |
| $$S/L_o$$ | 5.251181157716×10⁻²⁰ | Dimensionless store ratio |
| **$$K_s$$** | **Unfixed** | **Aligned-state energy price in the variable-G column** |

The dominant term is most clearly written $$K_s/(2K_0)$$: it does not require substituting $$\mu/\gamma$$ for S. Rewriting it with $$\Omega_s$$ does not earn that conversion. For a rigid rotor, $$K_s/S = \omega/2$$ while $$dK_s/dS = \omega$$; the mean price and differential conjugate rate must remain distinct.

### Latitude restriction

The original common-factor expression is not the source-state-function result at general latitude. If $$L_\phi = f L_e$$, the source construction gives $$K_{0,\phi}=K_{0,e}/f^2$$, $$a_\phi=a_e f^2$$ and $$\Gamma_\phi=(1-a_e f^2)^{-1}$$. With a separately specified axis projection p, the twist term scales with $$\Gamma_\phi f^2p$$, while the deposit scales with $$\Gamma_\phi fp$$. A common equatorial $$\Gamma g$$ factor cannot represent both.

For the reviewed hybrid vertical illustration at 30.3° N, the corrected **deposit-only, $$\theta=90^\circ$$ ceiling is 1.587649329213×10⁻²²**, not the value from a shared latitude factor. The headline and price table below are restricted to the equator. The static protocol separately declares its frozen, leading-order north–south geometry convention; those bounds are conditional coefficients under that convention, not an exact general-latitude law.

## 5. One unfixed price; approximately 25 orders of candidate span

No current commitment fixes **$$K_s$$** for saturated aligned YIG. The rotor relation $$K_s=\tfrac12 I\omega^2$$ applies to bulk rotation; it does not price an aligned ferrimagnet. The proposed conjugate-action relation $$K_s=\int\Omega\,dJ=\int B_{\mathrm{eff}}\,d\mu$$ remains conditional until direct work and the reaction account support it. Assigning $$hcR_\infty$$ to each net aligned Bohr magneton is explicitly unsupported without an independent alignment-energy bridge.

The candidate anchors expose the scale freedom; none is adopted here:

| Candidate price | $$K_s$$, approximately | Standing |
|---|---:|---|
| Rigid-equivalent rotation $$S^2/(2I)$$ | 3.28×10⁻¹⁸ J | Lower comparison anchor, not an aligned-state law |
| Selected natural-orbit rate, $$\Omega_s=\omega_0(1-3r_0/R)$$ | 2.539837651306×10⁻¹² J | Algebraic choice reproducing the naive ratio |
| Conjugate-action preparation model, 59.3 mT | 0.004400555556 J | Open preparation-price proposal |
| Same proposal, 0.180 T | 0.01335 J | Open preparation-price proposal |
| $$hcR_\infty$$ per net aligned $$\mu_B$$ | 17,433.00529283 J | Unsupported alignment price; comparison only |
| Compton-rate comparison, $$K_s=S\omega_C/2$$ | 1.64×10⁸ J | Upper comparison anchor, not a commitment |

The corresponding exact source-model static shifts at the end anchors run from about 6.7×10⁻²⁶ to 1.78: approximately **25 orders of magnitude**. This is a candidate span, not an uncertainty interval or a physical bound. The upper anchor is outside weak spin and is not evaluated with the first-order toggle formula. Once the state and axis hypothesis are specified, **$$K_s$$ is the single unfixed magnitude coefficient**; θ is a preparation parameter and the axis remains a separate declared geometry assumption.

## 6. Price table: reviewed ceilings and common per-watt normalization

All entries are conditional fractional weight changes. Ceilings use $$\theta=90^\circ$$ and $$g_{\mathrm{eq}}=1$$; they bound the formula, not an attainable operating point. Every per-watt entry uses the **same** normalization: $$B_{\mathrm{res}}=0.180\ \mathrm{T}$$ and linewidth $$\Delta H=0.5\ \mathrm{Oe}$$.

| Price or contribution | $$K_s$$ (J) | Ceiling, equator | Per absorbed watt, equator (W⁻¹) |
|---|---:|---:|---:|
| Orbital deposit only | 0 | 3.647906015718×10⁻²² | 3.107212622913×10⁻²⁷ |
| Selected naive price | 2.539837651306×10⁻¹² | 5.251181157716×10⁻²⁰ | 4.472849987953×10⁻²⁵ |
| Preparation price $$\mu_{\mathrm{sat}} B_{\mathrm{eff}}$$ at 59.3 mT | 0.004400555556 | 9.035060282011×10⁻¹¹ | **7.695881756843×10⁻¹⁶** |
| Preparation price $$\mu_{\mathrm{sat}} B_{\mathrm{eff}}$$ at 0.180 T | 0.01335 | 2.740973343973×10⁻¹⁰ | 2.334705701508×10⁻¹⁵ |
| Unsupported $$hcR_\infty$$ alignment price | 17,433.00529283 | 3.579281109583×10⁻⁴ | 3.048759314722×10⁻⁹ |

The per-watt conversion is imported Gilbert/FMR phenomenology, not a measured power–cone relation for this sphere:

$$
P_{\mathrm{abs}} = \frac{(\lvert\gamma\rvert\,\Delta H)(\mu_{\mathrm{sat}} B_{\mathrm{res}})\sin^2\theta}{2}
$$

Small angle:

$$
\frac{1-\cos\theta}{P_{\mathrm{abs}}} = 8.517797907964\times10^{-6}\ \mathrm{W^{-1}}
$$

Its arithmetic gives 1 W → 0.2364844° and a 10° cone → 1770.040210678 W absorbed continuously at the stated field and linewidth. It supplies a normalization only, not an operating specification. In particular, changing the price to the minimum-field value does not change the common RF normalization field in that table row.

## 7. Reproducing the 1.09×10⁻²¹ limiting case

The reference quotient is:

$$
\frac{6.9\times10^{-13}}{6.35\times10^8} = 1.08661417322835\times10^{-21} \approx 1.09\times10^{-21}
$$

Those inputs describe the research record's brass-gyroscope example, not the YIG sphere. The unrounded quotient is 1.08407233031432×10⁻²¹; the corresponding nominal YIG quotient is 6.97986577181208×10⁻²⁰.

Set $$\theta=90^\circ$$, $$g_{\mathrm{eq}}=1$$ and choose:

$$
\begin{gathered}
\Omega_s^* = \omega_0\left(1-\frac{3r_0}{R}\right) = 6.02307948570334\ \mathrm{rad/s} \\
\Gamma\left[\frac{\Omega_s^*}{\omega_0}+\frac{2r_0}{R}\right] = 1
\end{gathered}
$$

Therefore

$$
\left\lvert\frac{\Delta w}{w}\right\rvert = \frac{S}{L_o}.
$$

Substitution of the reference input pair reproduces 1.09×10⁻²¹. This is a deliberately selected algebraic price, not a price forced by the source or a universal physical limit. Under the nominal equatorial YIG inputs the same selection returns 5.251181157716×10⁻²⁰.

## 8. Threshold verdict and the static test

The program's build threshold is $$\lvert\Delta w/w\rvert \ge 1.3\times10^{-4}$$. **No supported price reaches it. The microwave toggle is not buildable as a discriminating weight experiment on current commitments.** This conclusion is specific to the proposed channel, observable and balance; it does not substitute for a measurement.

Even the larger open preparation-price proposal gives only 2.740973343973×10⁻¹⁰ at the idealized ceiling, a shortfall of about 5.7 orders. First-order threshold requirements are 6331.692366940 J at 90° in the best geometry, or 416771.289462871 J at 10°. These correspond to 4.941607132376 and 325.271642591568 eV per net aligned $$\mu_B$$/spin-½ equivalent. They are conditional requirements, not achievable energy assignments. The unsupported $$hcR_\infty$$ price crosses the threshold only at large cones; its presence in the table is not a build premise.

For the same state and geometry, the dominant toggle term is $$(1-\cos\theta)$$ times the static half-contrast:

$$
\begin{aligned}
C_{\mathrm{static}} &= \frac{w_{\mathrm{co}}-w_{\mathrm{anti}}}{2w} = \Gamma g_{\mathrm{static}}\frac{K_s}{2K_0} \\
\text{Full reversal} &= \frac{w_{\mathrm{co}}-w_{\mathrm{anti}}}{w} = 2 C_{\mathrm{static}}
\end{aligned}
$$

To reach the build threshold at 10° would require a **full reversal of 1.7113992%**. The 0.8556996% value is the half-contrast, not the reversal.

The static protocol adopts Convention A: two 0.01 mg increments bound the half-contrast, so the raw pair-difference threshold is 0.04 mg. For the receipt-exact nominal mass, one increment is 3.694118601746 ppm, not the 66.7 ppm belonging to a separate 150 mg example. A qualified north–south null would give **$$K_s < 482.7226\text{–}750.0121\ \mathrm{J}$$**, with the bound selected by the declared axis hypothesis, and exclude the unsupported $$hcR_\infty$$ alignment price by **×23.2436–36.1139** within that conditional model. It would bound the same-state 10° toggle by **1.122439243998×10⁻⁷** (reported as 1.1224×10⁻⁷), with the negligible deposit neglected. These are prospective consequences; none is an existing experimental bound.

A contrast would instead calibrate a **conditional effective-support coefficient in $$K_s$$-equivalent joules**. It earns a static directed-order candidate only. A separate same-transition state/reaction/work receipt remains necessary for spin-energy or twist interpretation.

## 9. Reading the partition: the narrowed insight

The conditional projection term explains why the sign alone cannot identify the channel. In an additional-assumption countermodel, let the driven twist energy be $$K_s+\Omega_d S(1-\cos\theta)$$, projected with $$\cos\theta$$. Then, at the equatorial reference:

Twist reading:

$$
\frac{\Delta w}{w} = (1-\cos\theta)\,g_{\mathrm{eq}}\,\Gamma\frac{S}{L_o}\frac{\Omega_d\cos\theta-\Omega_s}{\omega_0}
$$

This is lighter when $$\Omega_s>\Omega_d\cos\theta$$; $$\Omega_s>\Omega_d$$ is sufficient. Thus both a proposed writhe reading and this extra-assumption twist reading can give “lighter.” The countermodel is algebra, not a demonstrated YIG channel law, and has not passed the program's matched-static-state or separate channel/reaction/work requirements.

**For this proposed calibration route, a qualified static measurement or sufficient static bound is a prerequisite to reading the partition through the toggle.** This is a consistent sharpening of the tightened GROUNDING §4 standard: drive-toggle comparison **plus** field-gradient imitation controls, matched delivered/absorbed energy, and complete apparatus accounting; sign alone is necessary, not sufficient. It is not a challenge to that standard or a claim that static weighing is universally necessary. An independently specified constitutive price or a separate channel receipt could support another route. Without those qualifications the outcome remains channel-unassigned.

## 10. EARNED and UNEARNED: what the derivation establishes

**EARNED-BY** identifies definitions, arithmetic, geometry, declared imported tools or the named source construction at their stated level. It never promotes a source postulate into an observation. **UNEARNED** identifies a physical conversion not established by current commitments; any result depending on it remains conditional.

Three UNEARNED conversions stand upstream of the dominant term:

| Research-record tag | Unearned conversion | Consequence |
|---|---|---|
| T18 | Variable-G state → measured support force through $$F=mM(\mathcal{G}-G^{\prime})/R^2$$ | The source support law is adopted conditionally, not an established YIG response law |
| T23 | Prepared spin direction → the operative containing-circulation projection axis | The axis must be declared and tested; different axis hypotheses are not noise to average away |
| T24 | Saturated aligned magnetic state → the twist-column energy price $$K_s$$ | No current commitment fixes the coefficient; static support calibration is not independent spin energy |

The nominal mass calculation is an earned arithmetic dependency upstream of $$K_0$$. The magnetic proxy conversion, coning-to-writhe assignment and internal-displacement-to-orbital-numerator posting add separate UNEARNED dependencies to the small deposit term. Dimension checks and arithmetic replay test equations and software, not these physical premises.

The public program therefore carries two instructive results of paper work: a **conditional derivation** that identifies the missing price and a **decisive preregistered protocol** that says what each outcome will teach. A null would bound the coefficient, a contrast would calibrate it within the adopted form, and an ambiguous record would require a named repeat or stopping disposition. None is anticipated as a performed result.

## References and next step

- Pope, *Einstein's Lost Legacy*, Appendix 5; Osborne and Pope (2007), chapters 6–7, equations (6.16)–(6.19) and (7.11)–(7.21): source construction, not a YIG measurement.
- **Program research record, 2026-11-11:** final magnitude derivation, independent re-review and corrected arithmetic; nominal inputs and imported relations retain the limits stated above.
- [Static-gate preregistration and bench runbook](static-gate-protocol.html): locked convention, controls, decision table and executable reduction.
- [Program protocol](protocol.html) and [data schema](data-schema.html): qualification, independent state/reaction/work requirements and raw-record custody.

Publication precedes the physical experiment. It supplies neither an experimental result nor construction or operating authority; the completed run annex and separate bench authorization remain necessary.
