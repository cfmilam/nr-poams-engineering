# Generation-1 Mechanical Rotor

## Status

**Conditional protocol complete / instrument prototype only.** No anomalous support response has been observed. No rotor procurement, fabrication, or spin is authorized by this page.

This branch tests the conditional Appendix-5 support-response law after its laboratory geometry is made explicit. For a surface-fixed article, the center-referenced orbital-angular-momentum direction is local geocentric north. The first-order signed response is therefore assigned to a north–south rotor axis; vertical and east–west reversals are null controls.

## Frozen two-site discriminator

For retained rotor energy `K`, the conditional first-order odd estimator is

`D_NS(K) = [Y_+N(K) - Y_-N(K)] / 2 = g_G K cos²(lambda) / v_0,eq²`.

Using nominal city latitudes, the frozen amplitude ratio is

`Austin / Palo Alto = 1.183318`.

Palo Alto must reproduce the Austin sign at about 84.51% of its matched-energy amplitude. A response fixed to local vertical, equally odd on every axis, or incompatible with this ratio is not the registered Appendix-5 result. Exact building coordinates, elevations and local surveys are required before a confirmatory run.

## Metrology sequence

1. **P0 — static qualification:** loaded drift, spectrum and Allan deviation; blind force recovery; direct tilt, thermal, pressure, cable, magnetic and vibration injections.
2. **P1 — powered dummy:** reproduce mass, center of mass, thermal capacity and plumbing without retained rotor energy.
3. **P2 — low-energy transfer map:** zero plus at least three energy plateaus; north/south primary states; up/down and east/west odd nulls; heater, sham, remount and dummy controls.
4. **P3 — frozen confirmation:** lock the analysis and exclusions, acquire blinded randomized blocks, repeat with a second rotor/remount, then transfer the frozen protocol to Palo Alto.

The primary standard uncertainty must be no larger than one fifth of the conditional target. Each reversal-correlated nuisance must be below 0.1 target; combined nuisance uncertainty must be below 0.25 target; each perpendicular odd control must be bounded below 0.2 target. An occurrence claim also requires the registered sign and energy scaling, at least familywise five-sigma significance, all hostile controls, and the two-site ratio. Significance alone cannot rescue a failed physical discriminator.

## Selected instrument candidate

A direct commercial mass comparator and ordinary load cell are rejected as the primary architecture. The selected prototype candidate is a **counterbalanced flexure/null balance**:

- the complete test pod sits on one arm and a matched dead load on the other;
- an optical displacement channel observes the error coordinate;
- an electrostatic actuator holds the balance near null;
- a dissimilar second force reference cross-checks calibration;
- the weighed inner containment stays with the pod;
- a separate fixed outer guard provides redundant personnel protection without touching the pod.

The immediate build target is an **inert full-mass dummy pod**. It must blindly recover 10, 40, 100 and 400 nN injections, reach loaded-stage `u(D) <= 8 nN`, survive hostile artifact injections, agree across two dissimilar force references, and repeat after remount and 180-degree reversal.

## Decision envelope

- **Green:** `u <= 8 nN`; the metrology supports an independently engineered 100 J study, beginning far below that ceiling.
- **Amber:** `8 nN < u <= 40 nN`; improve isolation and readout before considering the higher containment burden.
- **Red:** `u > 40 nN`, unstable correction, or a force path dependent on contact/cabling; redesign or stop. Do not buy sensitivity by escalating rotor energy.

At matched `K`, different inertia/speed combinations provide a strong discriminator: the conditional law scales with energy, while ordinary Earth-rate gyroscopic reactions generally scale with angular momentum `J = sqrt(2 I K)`.

## Safety boundary

No rotor may spin until an independent qualified mechanical engineer signs the rotor stress/fatigue, hub/shaft/bearing/fastener failure analysis, independent overspeed protection, maximum credible energy, fragment trajectories, validated inner containment, fixed outer guard, remote operation, pressure-vessel compliance where applicable, safe rundown, exclusion zone and emergency procedure.

Containment is sized from credible failure modes and fragment geometry, not ideal hoop stress or nominal kinetic energy alone. Personnel protection is not part of the measurement optimization.

## Package

- [Frozen protocol](programs/generation-1-mechanical-rotor/protocol.html)
- [Instrument and containment envelope](programs/generation-1-mechanical-rotor/instrument-and-containment.html)
- Parent program: [Mechanically Ordered Angular Momentum](mechanically-ordered-angular-momentum.html)

## Primary sources and status receipts

- NIST, [Electrostatic force method to determine flexure stiffness with integrated fiber-optic displacement interferometer](https://www.nist.gov/publications/electrostatic-force-method-determine-flexure-stiffness-integrated-fiber-optic)
- NIST, [Comparison of electrostatic and photon pressure force references at the nanonewton level](https://www.nist.gov/publications/comparison-electrostatic-and-photon-pressure-force-references-nanonewton-level)
- NIST, [Flexures for Kibble balances: Minimizing the effects of anelastic relaxation](https://www.nist.gov/publications/flexures-kibble-balances-minimizing-effects-anelastic-relaxation)
- NASA, [High Energy Flywheel Containment Evaluation](https://ntrs.nasa.gov/citations/20000120215)
- NASA, [Evaluation and Implementation of a Water Containment System to Support Aerospace Flywheel Testing](https://ntrs.nasa.gov/citations/20020081257)

The cited work establishes small-force metrology and containment discipline. It does not establish the conditional POAMS response or prove nanonewton performance under a live kilogram-scale rotor.
