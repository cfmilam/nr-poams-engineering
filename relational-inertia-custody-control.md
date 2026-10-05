# Relational Inertia Custody-Control Program

**Status:** foundational engineering paper — design analysis only; no physical run, no M0/M1 evidence, no apparatus or fabrication authorization  
**Date:** 4 October 2026  
**Theory source:** [Inertia — The Felt and the Seen](https://cfmilam.github.io/nr-poams-exhibits/inertia.html)  
**Governing principle:** No-Orphan Inertial Response (NOIR), adopted 4 October 2026

> This paper begins an engineering program. It does not report inertial modification, weight change, propulsion, time-rate control, or a measured custody fraction. Its job is to expose the consequence deeply enough that nature can reject it.

## 1. Engineering question

Can a deliberately prepared external angular-action organization change the **constitutive relational custody account** of a retained test body, producing the trace-preserving inertial-tensor change required by NOIR?

The program separates three propositions:

1. **Geometry:** a declared custody measure defines a transverse comparison tensor. This is mathematical.
2. **Participation:** an engineered preparation changes the test body's ontic custody measure rather than merely changing detector illumination, heat, fields, stress or information. This is open.
3. **Readout:** the changed tensor appears in a named inertial observable through a declared translation map. This is open.

A result at one level does not establish the next.

## 2. Theory input

For the complete ontic custody measure \(\nu_*\),

\[
\mathcal M_*=\int_{S^2}
\left(I-\hat{\boldsymbol n}\hat{\boldsymbol n}^{\mathsf T}\right)
\,d\nu_*(\hat{\boldsymbol n}),
\qquad
\operatorname{tr}\mathcal M_*=2.
\]

NOIR fixes the candidate inertial tensor to

\[
\mathsf K=\frac{3m}{2}\mathcal M_*.
\]

For a baseline account \(\nu_0\) and prepared account \(\nu_d\), define the custody participation fraction \(f\) by

\[
\nu_*'=(1-f)\nu_0+f\nu_d.
\]

Then

\[
\boxed{
\Delta\mathsf K=\frac{3m}{2}f(\mathcal M_d-\mathcal M_0).
}
\]

No additional response coefficient remains after NOIR. The unknown is whether the preparation participates at all and, if so, the value of \(f\).

## 3. The participation firewall

The following are not interchangeable:

- source energy;
- received optical or RF power;
- photon/event count;
- material polarization or aligned fraction;
- detector exposure;
- inferred astronomical mass;
- custody participation fraction \(f\).

An apparatus can change every quantity in the first six while leaving \(f=0\). A source becomes constitutive only through an independently defined and tested relation to the retained organization's complete external account.

No source-side measurement alone identifies \(f\). Inferring \(f\) from the same inertial shift used to claim the effect is circular. Promotion requires either:

1. an independent custody witness calibrated before the inertial comparison; or
2. a multi-amplitude response family whose common \(f\)-law predicts held-out tensor states without refitting.

## 4. Translation hypotheses

The program keeps three readout bridges distinct.

### RI-R — rotational response

A prepared change in \(\mathsf K\) changes the angular impulse or rotational susceptibility of a retained body along the same principal axes.

### RI-T — translational response

A prepared change in \(\mathsf K\) changes the effective translational inertial coefficient along a named laboratory axis.

### RI-C — clock/rate response

A prepared change in custody changes a local phase or rate observable in the tensor pattern predicted by the same preparation.

NOIR alone does not prove that all three bridges exist or share magnitude. Each requires its own raw observable and falsification gate. A response in one lane does not authorize claims in the others.

## 5. Lowest-order signatures

For a unit sensor axis \(\hat u\),

\[
\frac{\Delta k_{\hat u}}{m}
=\frac32f\,\hat u^{\mathsf T}(\mathcal M_d-\mathcal M_0)\hat u.
\]

For a rotated uniaxial quadrupole this becomes a second angular harmonic,

\[
\frac{\Delta k}{m}=C_0+C_c\cos2\theta+C_s\sin2\theta,
\]

with the trace rule requiring the sum over three orthogonal principal responses to vanish:

\[
\Delta k_x+Delta k_y+Delta k_z=0.
\]

That trace-free three-axis closure is more discriminating than a single periodic signal.

For an oscillator with independently calibrated stiffness \(s\) and effective inertial coefficient \(k_u\), the imported engineering identity \(\omega^2=s/k_u\) gives, to first order,

\[
\frac{\Delta\omega}{\omega}
=-\frac12\frac{\Delta k_u}{k_u}
\approx-\frac34f\,
\hat u^{\mathsf T}(\mathcal M_d-\mathcal M_0)\hat u.
\]

This last equation is conditional on RI-R or RI-T and on measured stiffness constancy. It is not a POAMS derivation of oscillator mechanics.

## 6. Why the source, detector and hardware must rotate independently

The synthetic design study found that locked source/hardware rotation allows a pure hardware quadrupole to appear as a 75-sigma source-following response. Repetition does not cure structural aliasing.

The minimum architecture therefore has three independently indexed frames:

1. **P-frame:** prepared action/custody candidate tensor;
2. **D-frame:** detector or inertial-sensor axis;
3. **H-frame:** support, cabling, shielding and source hardware.

The schedule must span a randomized factorial set of \((\theta_P,\theta_D,\theta_H)\). If any two are mechanically locked, their harmonics are not separately identifiable.

## 7. Reference apparatus architecture

This is a design reference, not a procurement authorization.

### 7.1 Prepared-source shell

A symmetric shell carries independently addressable source modules. The same modules generate:

- isotropic action-matched state;
- uniaxial/quadrupolar state;
- axis-permuted state;
- detuned state;
- dummy state with matched heat, power, mass motion and timing;
- source-absent schedule replay.

Total measured source action and ordinary emissions are held constant as closely as practicable while tensor geometry changes.

### 7.2 Crossed inertial sensors

At least three orthogonal sensor channels share one central test article. Candidate instrument classes include crossed torsional resonators, orthogonal flexural resonators, interferometric inertial oscillators or gyroscopic phase sensors. The first build should optimize artifact observability and calibration access—not claimed sensitivity to new physics.

### 7.3 Independent rotations

The source pattern is electronically permuted without rotating the shell where possible. The sensor triad can be physically indexed independently. The support frame has a third indexing schedule or remains fixed while source and detector permutations span the necessary design matrix.

## 8. Required states

Every confirmatory run includes:

1. baseline isotropic source state;
2. quadrupole states along each of three orthogonal axes;
3. equal-total-action geometry reversals;
4. detuned source state;
5. action-matched isotropic clone;
6. inert dummy with matched thermal/electrical/mechanical load;
7. source absent;
8. detector-axis permutations;
9. hardware orientation permutations;
10. blinded injected synthetic signals and null injections.

## 9. Direct artifact characterization

Before a physical search, inject and measure transfer functions for:

- temperature, gradients and radiative heating;
- magnetic field and three-axis gradient;
- electric field, leakage, grounding and cable forces;
- vibration, tilt, acoustic drive and bearing harmonics;
- gas flow, pressure and buoyancy;
- optical/RF radiation pressure and momentum transfer;
- mechanical creep, stiffness, damping and resonance shifts;
- timing skew, digitizer crosstalk and analysis leakage;
- source-state classification errors.

Calculated conventional expectations do not replace these injections.

## 10. Preregistered hypothesis family

- **H0 — no participation:** the prepared source changes measured environment and detector estimator but \(f=0\); calibrated nuisance paths explain all sensor changes.
- **HP — participation candidate:** a source-state term follows the independently witnessed P-frame tensor, survives D/H permutations and controls, and closes the trace-free three-axis sum.
- **HL — local ordinary coupling:** a real effect follows source geometry but is fully explained by measured electromagnetic, thermal, mechanical, optical or timing transfer.
- **HB — bridge-specific response:** one of RI-R, RI-T or RI-C survives while the others do not; claims remain confined to that lane.
- **HA — adverse NOIR result:** an independently established custody-tensor change fails the frozen proportionality, eigenvector or trace rule.
- **HX — structurally inconclusive:** rank, custody, stability, calibration or control coverage is insufficient.

## 11. Stage gates

### Stage 0 — metrology and alias rejection

Build no exotic source. Demonstrate that independent P/D/H labels are recoverable, blinded tensor injections are estimated without leakage, locked-axis counterfeit signals are correctly rejected, and three-axis trace closure is measurable.

### Stage 1 — source-state qualification

Establish repeatable isotropic, quadrupolar, reversed, detuned, dummy and absent source states with immutable raw records. Show matched totals and independently measured residual differences. This stage earns only a prepared-source tensor—not custody participation.

### Stage 2 — bounded coupling search

Run the randomized factorial schedule against one preselected sensor lane. Use the frozen nuisance model and decision rule. A null sets an upper bound on the product of custody participation and that bridge's response; absent an independent custody witness it does not separately bound \(f\).

### Stage 3 — independent custody and bridge separation

Only after a Stage-2 candidate: introduce an independent custody witness or held-out multi-amplitude law; repeat after remount and source substitution; test RI-R, RI-T and RI-C separately.

### Stage 4 — replication

Transfer the frozen protocol and analysis to an independent apparatus and team. No technology claim precedes this gate.

## 12. Sensitivity arithmetic—not a performance forecast

Let

\[
q_u=\hat u^{\mathsf T}(\mathcal M_d-\mathcal M_0)\hat u.
\]

Then

\[
\left|\frac{\Delta k_u}{m}\right|=\frac32|f q_u|,
\qquad
\left|\frac{\Delta\omega}{\omega}\right|\approx\frac34|f q_u|.
\]

These equations convert an instrument's registered fractional sensitivity into a bound on \(|fq_u|\). They do not predict \(f\). The companion executable emits illustrative ladders only and labels them accordingly.

## 13. Acceptance rule

A custody-control candidate requires all of the following:

1. correct P-frame tensor harmonic and sign;
2. independence from H-frame and D-frame nuisance harmonics;
3. three-axis trace closure;
4. survival of matched isotropic, dummy, detuned and absent controls;
5. survival of direct artifact-transfer subtraction with uncertainty;
6. repeat after shutdown, remount and fresh randomization;
7. a noncircular custody witness or held-out response family;
8. bridge-specific replication.

Failure of any item prevents promotion. A beautiful \(2\theta\) signal alone is insufficient.

## 14. Kill and narrowing gates

- A qualified change in the complete custody tensor with absent predicted response kills the tested NOIR realization.
- A response that follows hardware rather than the P-frame kills the custody interpretation.
- A nonzero three-axis trace after calibrated ordinary transfers kills the minimal redistribution law.
- Different inferred \(f\) values across tensor geometries under one preparation narrow or kill the affine-mixture model.
- Failure to construct an independent custody witness leaves the program at an effective-coupling result, never a measurement of \(f\).
- A response confined to one bridge narrows the theory to that bridge and forbids broader inertia, weight, clock or propulsion claims.

## 15. Data custody

Raw records are append-only and hash-sealed. Preserve:

- source-module currents, voltages, phases, temperatures and state witnesses;
- P/D/H indices and encoder records;
- all inertial-sensor raw channels;
- environmental sensors and direct-injection calibrations;
- synchronization markers and latency calibrations;
- complete randomized schedule commitment;
- all failed, excluded and interrupted trials with reason codes;
- software, firmware, geometry surveys, wiring photographs and analysis environment.

Derived tables must regenerate from immutable manifests by versioned code.

## 16. Present disposition

The consequence is important enough to surface and disciplined enough to test, but no build is yet authorized. The immediate work is Stage 0: instrument and analysis architecture, counterfeit rejection, and custody-witness design.

If the program fails, the failure will be published as a narrowing result. If it succeeds, the first earned claim will be a tensorial response in one named bridge—not propulsion, weight cancellation, or control of inertia in general.

## Reproducibility

- [Executable sensitivity and tensor-closure checks](scripts/relational_inertia_custody_checks.py)
- [Machine-readable results](scripts/relational_inertia_custody_results.json)
