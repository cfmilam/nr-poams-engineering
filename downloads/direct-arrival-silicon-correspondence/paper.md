# A Silicon Correspondence for Coupled Ledgers

Technical paper · Public edition 1.1 · 20 October 2026

## Abstract

A coupled ledger becomes a physical construction when its state variables, exchange rule and conserved account have explicit counterparts in an apparatus. This paper supplies that correspondence for the twelve-node, two-ledger model accompanying *Direct Arrival*. Coherent optical modes represent the complex state; integrated packet energies represent the ledger balances; and matched coupling sections implement the model's finite two-mode rotation. An ordered network reproduces the complete graph evolution, with derived phase response, inverse operations, loss accounts and error bounds.

The connected mechanism has an independent experimental precedent. Silicon directional couplers and programmable coherent transformations have been investigated experimentally for optical communications and computing, independently of this proposal. Those results support the physical component class and connected operations used here. The present contribution is the explicit correspondence to our ledger model and its complete accounting requirements. The distinctive Direct Arrival question remains what happens after the ordinary physical connection is removed.

**Result:** an energy-normalized, connected silicon-photonic construction, with reported external experimental support for its building blocks and eleven reproducible mathematical checks of the correspondence.

### Two accounts of one construction

This paper follows each principal operation from its engineering description to its POAMS reading, then states the observable consequence they share. The engineering account specifies modes, phases, transfer matrices and port energies. POAMS reads the source, silicon structure, supports and receiver as organizations of one angular-momentum substance, with completed exchanges recorded at their participating ends. The mathematical description remains usable without making a traveling object its ontology.

The POAMS passages below are an interpretation of the declared connected model. Its calibrated optical transfer laws remain adopted inputs; their derivation from a specified circulation organization is the further construction identified in §8. All comparisons retain the same apparatus settings, finite timing and energy records. A change of account does not remove a connection's measured delay.

## Independent experimental support

We need not begin by inventing an unobserved connected interaction. Two independently motivated experimental programs already address the relevant silicon operations:

| Experimental work | Reported result relevant here | Supported claim |
| --- | --- | --- |
| Ahmed H. El-Saeed and colleagues, *Low-Loss Silicon Directional Coupler with Arbitrary Coupling Ratios* (2024) | Fabricated silicon couplers with measured through/cross power behavior and several coupling ratios | Silicon structures can physically redistribute optical power between connected ports; symmetry, mismatch and loss matter |
| José Roberto Rausell-Campo, Daniel Pérez-López and José Capmany, *Programming universal unitary transformations on a general-purpose silicon photonic platform* (2025; preprint 2024) | Programmed and tested coherent 3×3 and 4×4 transformations on an integrated photonic processor | Physical networks of calibrated couplers and phase controls can implement coherent linear transformations |

The coupler study reports device measurements and the effects of asymmetry; it does not establish that every splitter has the ideal symmetric phase relation. [El-Saeed et al., full paper](https://arxiv.org/html/2404.06117v1)

The transformation study's preprint describes 1,500 random matrices per size/architecture combination. Its reported comparison normalizes the measured output powers, so that comparison supports transformation behavior, not an independent absolute energy-closure test. [Rausell-Campo et al., experimental procedure](https://arxiv.org/html/2407.03235v1#S4)

These experiments predate this ledger construction and were performed for other purposes. Their independence gives a useful external check; our correspondence is retrospective, not a prediction those experiments were designed to confirm. Neither study tested this exact twelve-node schedule or exchange after physical disconnection. Their published results are used as reported experimental support; raw instrument records have not been independently replayed here.

The separation is productive: the connected physical mechanism has an experimental basis, the complete ledger mapping is developed below, and **retained adjacency after disconnect remains the new physical question**.

## 1. The question and the distinction it requires

Silicon's physical energetic transfers can supply a connection between represented states. The stronger construction identifies the *particular conserved account and exchange law* with physical quantities and interactions. That distinction separates ordinary physical computation from an apparatus whose own dynamics perform the proposed exchange.

For an ordinary computer, let a decoding map D take a valid hardware state p to a numerical model state ψ. A running implementation has the approximate correspondence

\[
D(F(p))\approx U D(p)
\]

where F includes actual processor, memory and control operations. The approximation includes floating-point arithmetic. This does **not** imply that hardware energy has the form

\[
E_{\mathrm{hardware}}(p)=E_*\lVert D(p)\rVert^2
\]

Encoding changes, unused storage, clock activity and different instruction sequences can preserve the decoded calculation while changing hardware activity and energy cost. The memory representing 1.25 need not contain more physical energy than memory representing 0.75. Moreover, the program reads and writes both endpoints during exchange. “No scripted outcome” does not mean “no programmed update.”

The model's disconnected control proves independence of its represented B state from a fresh A intervention under that code. It does not physically isolate two parts of the computer from shared power, heat, clocks or other hardware paths.

### Candidate selection

| Candidate | What is physically represented | Correspondence established here |
| --- | --- | --- |
| Existing CPU / digital memory | Binary encodings of complex numbers | Physical execution of the numerical rule; no energy identification |
| Digital FPGA implementation | Register encodings and hardware arithmetic | Could remove a software execution layer, but encoding is still not an energy account |
| Coupled electrical/optical storage resonators | Retained oscillatory states | Relevant to storage, but switching work, interaction energy and mode normalization need their own branch |
| **Finite silicon-photonic network** | **Coherent optical port amplitudes and calibrated pulse energies** | **Selected: explicit finite exchange and full-network energy correspondence** |

Silicon directional couplers and programmable interferometer networks are established component classes in the literature. The independent reports support these connected component classes; they did not test our particular twelve-mode network. [El-Saeed et al.](https://arxiv.org/abs/2404.06117), [Rausell-Campo, Pérez-López and Capmany](https://doi.org/10.1063/5.0235712)

## 2. Exact scope of the candidate

The candidate is a finite-depth, connected, feed-forward optical network on a silicon photonic platform. Its twelve labeled channels represent A0–A5 and B0–B5 at successive reference planes. A graph step is a prescribed sequence of physical coupling sections, **not elapsed time in twelve permanently interconnected resonators**.

The adopted assumptions are:

1. Power-normalized, mutually orthogonal input/output port modes with a common carrier frequency and specified polarization. Arbitrary overlapping fields cannot be assigned additive energies just by naming them separate nodes.
2. Linear, passive, time-independent sections during each packet's passage; negligible unwanted reflections and unmodeled mode conversion in the ideal case.
3. Sufficiently narrow-band packets and matched channel delays that a common envelope factors out. All remaining relative propagation phases are explicitly included or compensated.
4. Prepared input amplitudes and phases are independent of the eventual receiver measurement. The source intervention changes only A0 at its designated reference plane.
5. Every nonzero A–B coupling is an ordinary admitted physical path. The branch contains no post-disconnection interaction.

These are operational assumptions imported from classical photonic circuit modeling. They are not derived from the one-substance ontology. In particular, orthogonal coupled-mode formulas have a limited domain; cross-power terms matter for unsuitable modal bases. [Huang, coupled-mode scope and normalization](https://doi.org/10.1364/JOSAA.11.000963)

### State, energy and phase mapping

Let the dimensionless published state be ψ ∈ C¹². Let f(t) be a common packet envelope with ∫|f(t)|² dt = 1, and let E_* > 0 be an independently specified energy scale. Define the physical port amplitude

\[
x_j(t)=\sqrt{E_*}\,\psi_j f(t)
\]

Here |x_j|² is power in watts, f has units \(\mathrm{s}^{-1/2}\), and

\[
E_j=\int |x_j(t)|^2\,dt=E_*|\psi_j|^2
\]

Thus \(E_A=E_*\sum_{j\in A}|\psi_j|^2\) and \(E_B=E_*\sum_{j\in B}|\psi_j|^2\). The model's seed is \([\sqrt{0.6},\sqrt{0.08},\sqrt{0.08},\sqrt{0.08},\sqrt{0.08},\sqrt{0.08}]\) in each group, so each input group carries E_* and the two carry 2E_*. These are **packet energies crossing reference planes**, not a claim about energy stored permanently at the displayed vertices.

Relative optical phase supplies the model phase. A static, source-local phase section multiplies A0 by exp(iφ), leaving its packet energy unchanged in the ideal model. It is set before that packet arrives; arbitrary choices between packets are possible. This is not a claim that a time-varying phase kick on already stored motion costs zero work. Preparation, actuator setting and thermal stabilization belong to the apparatus account.

#### Preparation and guidance: the two accounts

**Engineering account.** A prepared coherent packet has specified amplitudes and relative phases in twelve optical ports. Waveguide geometry constrains the supported modes and their transfer between reference planes.

**POAMS account.** The source and silicon are participants in the physical organization, not a launcher and a passive container for a second substance. The mode labels distinguish operational alternatives within that prepared connection. The complex entries summarize its phase-sensitive response; the waveguide supplies material constraints on the permitted exchange. Reference planes mark where that account is compared, rather than places where twelve tiny occupants must be imagined.

**Shared observable consequence.** The same preparation must yield the specified port-energy balances, relative-phase response and finite timing records.

## 3. Deriving the pair exchange from physical mode propagation

For a matched symmetric two-port coupling section, adopt normalized even/odd supermodes. Their finite propagation factors are exp(-iβ₊ℓ) and exp(-iβ₋ℓ). With

\[
H_2=\frac{1}{\sqrt 2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
\]

transforming to the supermodes, propagating, and transforming back gives

\[
\begin{aligned}S&=H_2\operatorname{diag}(e^{-i\beta_+\ell},e^{-i\beta_-\ell})H_2\\&=e^{-i\bar\beta\ell}\begin{pmatrix}\cos\theta&-i\sin\theta\\-i\sin\theta&\cos\theta\end{pmatrix}\end{aligned}
\]

where \(\bar\beta=(\beta_++\beta_-)/2\) and \(\theta=(\beta_+-\beta_-)\ell/2\).

After accounting for the common propagation reference, this is precisely the published pair rule:

\[
\begin{aligned}a^\prime&=\cos\theta\,a-i\sin\theta\,b\\b^\prime&=\cos\theta\,b-i\sin\theta\,a\end{aligned}
\]

The matrix is unitary; therefore the sum of the **port packet energies** is conserved under the declared encoding. Optical propagation and coupling perform the operation without a processor calculating the new amplitudes from the old ones.

**Phase-reference obligation:** a phase common to the two participating modes is not necessarily common to all twelve modes. It cannot silently be discarded at each section. Matched bypass paths or explicitly tracked phase sections must make the complete twelve-mode matrix equal to the target, up to one genuinely global phase and common delay. Published silicon meshes likewise require path-phase calibration; intensity splitting ratios alone do not establish the required complex matrix. [Rausell-Campo et al., calibration and coherent transformations](https://arxiv.org/html/2407.03235v1)

**Coupler qualification:** not every device sold as a 2×2 splitter has this exact phase law. Asymmetric/bent couplers can change relative phase and the maximum coupling. We use the symmetric idealization and an explicitly calibrated complex transfer matrix, not a generic device label. [El-Saeed et al., symmetry and phase dependence](https://arxiv.org/html/2404.06117v1)

#### Pair coupling: the two accounts

**Engineering account.** A matched coupling section coherently mixes two modal amplitudes by the derived two-mode matrix, preserving their summed packet energy in the ideal case.

**POAMS account.** The two entries are coordinates of one connected account. The coupling section changes their coherent combination and hence the distribution of energy that can be registered at the outputs. On this reading the silicon constrains an exchange relationship; it is not merely a place where independently existing couriers trade cargo. The angle θ specifies the adopted transfer rule, not an already established mechanical rotation of the material's angular momentum.

**Shared observable consequence.** Both output energies and the relative phase must agree with the same complex matrix; matching only a splitting ratio is insufficient.

## 4. Full graph correspondence and resource scaling

The accompanying JavaScript executes, in order:

1. Six internal ring edges of A, then six internal ring edges of B, each at θ=0.035.
2. A0–B0 at θ=0.085 when enabled, or zero when disabled.
3. The twelve internal edges again in reverse order at θ=0.035.

There are **25 pair sections per enabled step**. If the temporal sequence of section matrices is L₁,…,L₂₅, then the transfer is \(U_{\mathrm{step}}=L_{25}\cdots L_1\). Each L is the pair matrix embedded into a twelve-mode identity, with all required bypass phases included. A source intervention is \(P_0(\varphi)=\operatorname{diag}(e^{i\varphi},1,\ldots,1)\).

For n steps after one source intervention:

\[
\psi_{\mathrm{out}}=U_{\mathrm{step}}^n P_0(\varphi)\psi_{\mathrm{in}}
\]

The finite spatial network can implement this ordered product. Its direct, unoptimized representation requires 25n coupling sections plus input preparation, phase/bypass/routing sections and output access. Ten steps correspond to 250 pair sections, **not a demonstrated chip footprint or a statement that every optical route crosses all 250 couplers**. The actual phase/loss/depth budget depends on routing. Alternative compilation into a smaller net transformation would need its own correspondence if intermediate graph states are to remain inspectable.

Other finite, prescribed histories are compositions of the same sections and source-local phase factors at specified reference planes. This does not implement the browser's indefinite Pause/Run/Undo interface as persistent optical memory. Adaptive intervention on a packet already in the device, repeated circulation, or stopping and retaining its state would require an additional storage/control branch. No detector is assumed to read out a complex state nondestructively between every section.

It is not enough to fabricate twelve resonators with all edges continuously active. Neighboring edge generators generally do not commute. The always-on map \(\exp(-i\sum_e\theta_e X_e)\) differs from the ordered product. Numerically, the one-step operator-norm difference is 1.74434×10⁻⁴ at the published angles. Halving all angles reduces the discrepancy by approximately eight, as expected for the symmetric sequence's leading cubic error. A controlled approximation is possible, but it is not identity.

This is a theoretical correspondence in the stated modal model, not a full-wave semiconductor/material calculation or a fabrication design. Packet passage has ordinary finite delay. A spatial reference-plane map does not supply instantaneous action or remove the physical propagation path.

#### The ordered network: the two accounts

**Engineering account.** Successive connected coupling sections implement an ordered product of transfer matrices, including the phases of the bypass paths.

**POAMS account.** The calculation composes changes to a coherent account under successive apparatus constraints. Its intermediate reference planes are mathematical comparison boundaries, not claims that a detector event or a completed photum occurs at every step. Order matters because one constraint changes the preparation on which the next acts.

**Shared observable consequence.** The final port records must follow the prescribed ordered product, including its ordinary delay; an always-on network is a different construction.

## 5. Derived predictions, without fitting the response

### Two populated modes

For \(a=\sqrt{E_0}e^{i\varphi}\) and \(b=\sqrt{E_0}\) in energy-normalized units, direct expansion gives

\[
\Delta E_B=E_0\sin(2\theta)\sin\varphi,\qquad\Delta E_A=-\Delta E_B
\]

For general input amplitudes:

\[
\begin{aligned}\Delta E_B={}&\sin^2\theta\,(|a|^2-|b|^2)\\&+2\sin\theta\cos\theta\,\operatorname{Im}(ab^*)\end{aligned}
\]

If b=0, then \(E_B^\prime=E_A\sin^2\theta\), independent of A's global phase. Phase response needs a relative-phase reference, not merely a source label. If both inputs receive the same phase, no port energy changes. For symmetric equal seeding, uniform random relative phase removes the mean signed interference term but does not remove the physical coupling.

#### Phase control: the two accounts

**Engineering account.** Changing one populated input's phase changes interference at the outputs. A common phase on both inputs changes neither output energy.

**POAMS account.** Relative phase belongs to the prepared relationship between alternatives. In the adopted coherent description, changing it changes how those alternatives combine into possible terminal records. The intervention reorganizes the distribution of the existing account; it does not create an extra energy supply. Its physical setting and stabilization still belong to the apparatus balance.

**Shared observable consequence.** The simple pair retains the derived sine response and equal, opposite energy changes. The full network retains its separately derived cosine-plus-sine response.

### The actual twelve-mode graph

The simple pair's opposite-phase equal magnitudes do **not** generally survive the full network. This can be derived without fitting or appeal to numerical noise.

Set \(U=U_{\mathrm{step}}^n\), \(p=\psi_{\mathrm{in},0}e_0\), \(x=P_B U p\), and \(y=P_B U(\psi_{\mathrm{in}}-p)\). Here P_B selects the six receiver outputs. Define \(C=y^\dagger x\). Compared with the same circuit and no source phase operation,

\[
\frac{R_B(\varphi)}{E_*}=A(\cos\varphi-1)+B\sin\varphi
\]

where \(A=2\operatorname{Re}C\) and \(B=-2\operatorname{Im}C\). Both coefficients are computed from the frozen graph and seed, not adjusted to the phase scan.

At the published angles and n=10:

| Quantity | Prediction |
| --- | ---: |
| A | 0.0783177175757793 |
| B | 0.3293143476848204 |
| +π/2 source phase: R_B/E_* | +0.250996630109041 |
| −π/2 source phase: R_B/E_* | −0.407632065260600 |
| Maximum over phase | +0.260181328918237 |
| Minimum over phase | −0.416816764069796 |
| Phase of maximum | atan2(B,A) ≈ 76.6224° |

For the energy-normalized optical implementation, multiply these by the independently established E_*. For the existing CPU implementation, they remain dimensionless numbers; that conversion has not been made physically.

### Cutting the bridge

With every A–B coupling removed, the admitted transfer becomes block diagonal: \(U_{\mathrm{off}}=\operatorname{diag}(U_A,U_B)\). Therefore for a fresh source-local phase P_A,

\[
P_B U_{\mathrm{off}}(P_A\oplus I)\psi=U_B\psi_B
\]

The new source operation cannot affect B under this candidate, even when ψ contains changes left by an earlier connected history. Retained energy/state is not retained ability to transmit a new choice. This explicitly separates a physically connected analogue from Direct Arrival's proposed retained-adjacency extension.

#### Disconnection: the two accounts

**Engineering account.** Removing every cross-coupling makes the transfer block diagonal. A fresh phase choice at A then leaves the B output unchanged.

**POAMS account.** Earlier exchanges may have changed the preparations at both ends. Those changes are not themselves a continuing permission for a new joint exchange. One substance and a shared history do not imply perpetual addressability. Retained adjacency would require an additional physical state and exchange law beyond this connected candidate.

**Shared observable consequence.** After removal of all admitted A–B paths, a newly selected A intervention produces no B response under the present model.

### Inverse operation

For a pair, \(S(-\theta)=Z S(\theta)Z\), with \(Z=\operatorname{diag}(1,-1)\). Thus an ideal inverse can use the same positive-coupling section and π phase shifts. For a network, reverse the order and invert every phase/coupling operation. The coherent output must be routed into this inverse network; a photograph or detected intensity list does not contain the full state.

Passing backwards through an ordinary reciprocal coupler is not automatically this algebraic inverse for arbitrary complex input. Reciprocity and inversion must not be conflated.

With one-pass intensity transmission T and otherwise ideal propagation, a lossy forward circuit followed by an equally lossy inverse returns only T² of the input signal energy. The numerical Undo button does not reverse heat or erase the apparatus history. Reset physically requires discharge/output routing and preparation of a new input; it is not free.

#### Inversion: the two accounts

**Engineering account.** A coherent inverse reverses the sequence and each operation; passive losses remain. Detection does not preserve a complete complex input for later inversion.

**POAMS account.** Reversing the reversible part of the account is not making a completed occurrence unhappen. Receiver absorption, apparatus changes and discarded outputs remain in the physical history. Reset is a new preparation with its own transfers, not deletion of the old ledger.

**Shared observable consequence.** Recovery concerns the surviving coherent amplitude and phase, with the stated attenuation and reset costs—not recovery of numbers alone.

## 6. Mismatch, loss, error and complete accounts

### Phase mismatch

As an explicitly adopted nonideal two-mode model, use the Hermitian propagation generator

\[
K=\begin{pmatrix}\delta/2&g\\g&-\delta/2\end{pmatrix},\quad\Omega=\sqrt{g^2+(\delta/2)^2}
\]

The finite section is \(S=\cos(\Omega\ell)I-i\sin(\Omega\ell)K/\Omega\). Put \(c=\cos(\Omega\ell)\), \(s=\sin(\Omega\ell)\), \(r=g/\Omega\), and \(d=\delta/(2\Omega)\). For equal populated inputs as above,

\[
\frac{E_B^\prime-E_0}{E_0}=2rsc\sin\varphi-2rds^2\cos\varphi
\]

Against the φ=0 reference the cosine term becomes \(-2rds^2(\cos\varphi-1)\). An unseeded receiver satisfies \(E_B^\prime/E_A\le g^2/[g^2+(\delta/2)^2]\). The resonant pair law follows at δ=0. g, δ and ℓ have defined roles and must be determined independently; they are not unrestricted fitted response functions.

### Loss and outputs

In a common-loss section, an intensity attenuation exp(-αℓ) multiplies all ideal output energies. Unequal loss cannot generally be removed by a single normalization. An adopted local model is

\[
\frac{dx}{dz}=\left(-iK-\frac{\Gamma}{2}\right)x,\qquad K=K^\dagger,\quad\Gamma\succeq0
\]

giving \(\frac{d(x^\dagger x)}{dz}=-x^\dagger\Gamma x\). Integrating the right-hand side supplies the loss account. For a general passive port transfer T, \(T^\dagger T\le I\), and

\[
E_{\mathrm{missing}}=E_*\psi^\dagger(I-T^\dagger T)\psi\ge0
\]

Missing monitored-port energy can include separately routed ports, readout taps, reflection, radiation and absorption. It must not all be labeled heat without distinguishing these channels. Signal amplification, nonlinear saturation, time modulation and gain are outside the frozen passive candidate; admitting any of them requires an explicit source account and revised dynamics.

For a network boundary excluding the source and detectors, integrate a complete packet and retain any internal residual:

\[
\begin{aligned}E_{\mathrm{signal,in}}+W_{\mathrm{control\to signal}}={}&E_{\mathrm{signal,out}}+E_{\mathrm{other\ ports}}\\&+Q_{\mathrm{absorbed}}+\Delta E_{\mathrm{retained}}\end{aligned}
\]

For static, passive settings in the ideal branch, \(W_{\mathrm{control\to signal}}=0\), and after complete passage \(\Delta E_{\mathrm{retained}}=0\). Electrical heater/control consumption is not thereby zero. It enters a separate apparatus balance. A larger boundary including preparation, electronics and detectors has

\[
\begin{aligned}E_{\mathrm{initial}}+W_{\mathrm{supplies}}+E_{\mathrm{other,in}}\\=E_{\mathrm{final}}+Q_{\mathrm{exported}}+E_{\mathrm{other,out}}\end{aligned}
\]

Optical energy absorbed inside that larger boundary is an internal transfer, not a second external output. This avoids double-counting detector heat and the optical packet that produced it. Source preparation, receiver absorption, intentionally discarded encoding ports, reset and environmental outlets all have a place; none is silently folded into “ledger conservation.”

#### Loss: the two accounts

**Engineering account.** Energy absent from the monitored ports can appear in other ports, reflection, radiation, absorption or retained internal excitation. Control supplies have their own balance.

**POAMS account.** An entry missing from one selected account has not vanished from the physical organization. Its destination belongs in another participating account, including the apparatus and its environment. Moving the bookkeeping boundary changes which transfers count as internal; it does not permit counting an absorbed packet and the heat it produces as two independent exports.

**Shared observable consequence.** Close the same complete energy balance with separately identified outlets. Calling every deficit heat, or normalizing it away, does not close the account.

### Stability and error propagation

The ideal network preserves norm and has no amplitude gain. For per-section operator errors ε_k, unitary ideal sections and contractive actual sections give the telescoping bound \(\lVert T_{\mathrm{actual}}-U\rVert\le\sum_k\varepsilon_k\). A pair angle error Δθ has exact operator error \(2|\sin(\Delta\theta/2)|\). A phase-setting error Δφ at A0 gives state error \(2|\psi_0|\,|\sin(\Delta\varphi/2)|\), preserved by subsequent ideal propagation.

If the ideal output is y and its actual deviation is d, any receiver-energy error obeys

\[
\frac{|\delta E_B|}{E_*}\le2\lVert y\rVert\lVert d\rVert+\lVert d\rVert^2
\]

This gives a finite uncertainty budget before inspecting the phase-response data. Bandwidth, differential delay, phase drift, undesired coupling and calibrated readout errors must enter that budget or make the candidate inapplicable. For lossless but dispersive S(ω), total spectral energy can remain conserved while the single-envelope, single-matrix representation fails. Neither renormalizing every result nor fitting a separate matrix to each trial repairs that failure.

## 7. Operational readout and failure conditions

The prospective raw records are port-detector current traces and acquisition times, source/phase settings and independent calibration records—not the browser's state vector. For a specified linear readout with independently calibrated responsivity ρ_j and dark trace i_dark,j,

\[
\widehat E_j=\frac1{\rho_j}\int[i_j(t)-i_{\mathrm{dark},j}(t)]\,dt
\]

This is a proposed operational reduction, not data collected here. Collection must cover the packet, account for gain, loading and unmonitored paths, and preserve raw records. The reduction specifies what a future measurement would mean; sensor selection and apparatus qualification follow a defined physical target.

#### Readout: the two accounts

**Engineering account.** A detector produces a current trace; the independently calibrated reduction gives an estimate of energy received at its port.

**POAMS account.** The receiver is a participant in a completed exchange, not a spectator watching an unseen traveler. A photum names an individual completed two-ended exchange in the POAMS account. This paper's optical packet and integrated current can summarize many exchanges; neither is automatically one photum. The trace is the instrument occurrence, while its source–receiver interpretation and microscopic angular-momentum allocation are distinct identifications.

**Shared observable consequence.** Preserve the same raw current, timing, settings and calibration records. A current trace alone does not establish a path or resolve individual exchanges.

The frozen target is the declared complex transfer, phase curve and complete energy balance within an **independently determined** uncertainty bound. Port intensities alone do not establish all phases or certify inverse state recovery. Phase-sensitive records or an explicitly sufficient set of coherent input comparisons would be required for that stronger claim.

| Candidate consequence | What would fail it within its admitted domain |
| --- | --- |
| Full matrix equals the prescribed ordered exchange product | Independently characterized complex transfer lies outside the predeclared error budget |
| Predicted phase curve and source/receiver balance | Raw reduced records disagree with frozen coefficients beyond calibration uncertainty |
| Fresh A changes do not reach B when all admitted cross-coupling is absent | A repeatable source-dependent B record not explained by independently bounded ordinary paths |
| Passive signal account closes | Unaccounted output or loss beyond uncertainty, or hidden gain/control work needed to force agreement |
| Ideal inverse recovers coherent signal, with known passive attenuation | State mismatch inconsistent with independently characterized phase/loss errors |

These are theoretical failure conditions, not a completed experimental protocol. Alternative explanations requiring explicit characterization include control-heater feedthrough, electrical/readout crosstalk, source-power changes correlated with phase setting, residual optical paths, nonorthogonal-mode accounting, detector gain changes and nonlinear response. Software synthesis of output numbers or feedback based on measured input is also a countermodel for an allegedly autonomous transfer device. Documentation of the actual circuit and causal controls matters; one matched curve alone cannot identify its mechanism.

## 8. Angular momentum, storage and residual unknowns

The energy-normalized optical account is not automatically a net angular-momentum account. In particular, do not assign \(J=E/\omega\) to an arbitrary guided or standing mode. Polarization, spatial mode, support torque and outlet angular momentum must be specified and independently linked to records before that stronger identification. The present branch uses imported operational photonic mathematics; it does not supply the native circulation/closure derivation demanded for a POAMS-native claim.

### What the ontological bridge supplies

The paired accounts locate the participants, controls, boundaries and terminal records of the connected construction in POAMS language. They also locate the remaining native task: construct the relevant circulation organization, its permitted exchange operation and its coupling to the supports and outlets, so that the optical transfer is obtained with a specified angular-momentum account.

POAMS already admits finite complex alternative states and norm-preserving reversible controls through its adopted Coherent Completion Kernel. That supplies a compatible mathematical vocabulary, not a selection of these silicon modes or their coupling constants. Here the squared modal norm is an energy account under the stated classical-optical normalization; it is not being promoted to a count of photums or a single-quantum outcome probability. A microscopic completion mapping would be additional work.

| Remaining item | Kind and status |
| --- | --- |
| E_*, coupler phases/angles, mismatch, loss, delay, bandwidth and readout gain | Empirical calibrations with defined roles, independent characterization routes and derived consequences; not yet measured here |
| Particular waveguide geometry, material stack and component count after routing | Device design and full-wave/material work, outside this finite-network correspondence |
| Persistent stored A/B states with arbitrary in-time operations | Different candidate; interaction energy, switching work, retention and reset must be closed before adopting it |
| Net angular momentum and native POAMS mechanism | Open physical/ontological correspondence; energy and optical phase alone do not close it |
| Continued exchange after ordinary paths are removed | Additional retained-adjacency hypothesis; not supplied by this construction |

The bounded finite-network correspondence is closed on paper under its declared assumptions. **The gate to a native POAMS mechanism, a stored-endpoint machine, or an experimental build is not cleared by this result.** The next paper branch, if pursued, must specify the retained physical state and its full source/support/exchange account. The connected construction supplies a baseline for that further work.

## 9. Verification and evidence status

`verify.py` performs independent NumPy eigenmode propagation and compares it with the unchanged accompanying JavaScript implementation. It also evaluates the derived phase and mismatch laws, block-diagonal independence, inverse/loss behavior, error bounds and an independently integrated unequal-loss account.

**11/11 mathematical checks passed.** The 24 full-graph comparisons differ by at most 1.70×10⁻¹⁴ per complex component. The phase curve's maximum sampled discrepancy is 5.0×10⁻¹⁶. Unequal-loss state evolution plus its integrated loss account closes to 1.84×10⁻¹⁴ in synthetic model units. The schedule-versus-always-on countermodel fails identity as predicted; it is preserved rather than normalized away.

These checks establish consistency of the conditional mathematical correspondence. They are not measurements of silicon. The external experimental support and its scope are set out at the beginning of the paper. The numerical checks reported here are separate mathematical evidence, not additional instrument measurements.


### Reproduce the mathematical checks

The [verification download](https://cfmilam.github.io/nr-poams-engineering/downloads/direct-arrival-silicon-correspondence/README.txt) contains a standalone checker, the unchanged model core and its recorded results. Python with NumPy and Node.js are required; no instrument connection or external service is used.

- [Checker](https://cfmilam.github.io/nr-poams-engineering/downloads/direct-arrival-silicon-correspondence/verify.py)
- [Recorded mathematical results](https://cfmilam.github.io/nr-poams-engineering/downloads/direct-arrival-silicon-correspondence/verification.json)
- [Model core](https://cfmilam.github.io/nr-poams-engineering/downloads/direct-arrival-silicon-correspondence/direct-arrival-model-core.js)
- [Readable paper source](https://cfmilam.github.io/nr-poams-engineering/downloads/direct-arrival-silicon-correspondence/paper.md)

## 10. Conclusion

**The ledger dynamics have a concrete connected silicon counterpart.** Coherent optical amplitudes carry the state, packet energies carry the account, and a prescribed sequence of physical couplers performs the same exchange as the model. Independent experiments undertaken for other purposes already support the connected component class and coherent transformations on which this construction rests.

The full correspondence makes the next question sharper. A state can persist after a connection is removed without preserving the ability to exchange a newly chosen intervention. The connected construction predicts no such new influence once its cross-coupling is absent. Whether a suitably prepared pair retains an additional interaction is the distinctive Direct Arrival question, addressed by the [retained-adjacency research program](https://cfmilam.github.io/nr-poams-engineering/direct-arrival-research.html).

The bridge is therefore operationally specific: the same connected apparatus can be described by optical transfer and interpreted as constrained relational bookkeeping, without changing its predicted records. Deriving that transfer from an explicit microscopic circulation construction remains a distinct, well-defined next step.

### References

1. A. H. El-Saeed et al., *Low-Loss Silicon Directional Coupler with Arbitrary Coupling Ratios for Broadband Wavelength Operation Based on Bent Waveguides*, arXiv:2404.06117 (2024). [Paper](https://arxiv.org/abs/2404.06117)
2. J. R. Rausell-Campo, D. Pérez-López and J. Capmany, *Programming universal unitary transformations on a general-purpose silicon photonic platform*, **APL Photonics 10**, 026102 (2025). [Published article](https://doi.org/10.1063/5.0235712) · [Open preprint and experimental procedure](https://arxiv.org/abs/2407.03235)
3. W.-P. Huang, *Coupled-mode theory for optical waveguides: an overview*, **Journal of the Optical Society of America A 11**, 963–983 (1994). [Article](https://doi.org/10.1364/JOSAA.11.000963)
