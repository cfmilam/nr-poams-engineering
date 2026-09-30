# Generation-1 mechanical-rotor protocol

## Registered question

Does a fully characterized retained-energy state produce the conditional north/south odd support response, while up/down and east/west odd contrasts remain null, and does the result reproduce at Austin and Palo Alto in the frozen ratio `1.183318`?

## State and estimator

At zero and at least three nonzero retained-energy plateaus, acquire equal valid dwell in `+N`, `-N`, `+U`, `-U`, `+E`, and `-E`, with dummy, matched-heater, powered-sham, remount and calibrated-injection blocks.

Primary estimators:

- `D_NS(K) = [Y_+N(K)-Y_-N(K)]/2`
- `D_UD(K) = [Y_+U(K)-Y_-U(K)]/2`
- `D_EW(K) = [Y_+E(K)-Y_-E(K)]/2`

The conditional first-order prediction is `D_NS = g_G K cos²(lambda)/v_0,eq²`; the perpendicular odd estimators are zero. Fit the north/south energy law through the qualified zero. Preserve raw and corrected results together.

## Sequence

1. **P0:** inert loaded-stage force qualification and direct nuisance injections.
2. **P1:** powered nonrotating dummy/plumbing map.
3. **P2:** low-energy spinning transfer map below an independently approved containment ceiling; characterization only.
4. **P3:** new randomized schedule after code, exclusions and nuisance model are frozen; decode labels only after lock; second rotor/remount; then Palo Alto replication.

## Raw custody minimum

Preserve native support force, encoder angle/rate/direction, independently calibrated inertia, orientation survey, motor electrical and torque/loss channels, bearing state, six-axis motion, tilt, strain/reaction, acoustic pressure, chamber/air/coolant state, temperatures, magnetic field/gradient, cable/hose reaction, controller telemetry, common-clock timestamps, block codes and all exclusions.

The nuisance model may use only P0 injections, P1 dummy blocks, a declared P2 training portion and predeclared environmental channels. It may not use the physics label or a deterministic proxy.

## Advancement gates

- blind recovery at 0.5, 1 and 2 times target;
- `u(D_NS) <= target/5`;
- each correlated nuisance below `0.1 target`, combined nuisance uncertainty below `0.25 target`;
- each perpendicular odd bound below `0.2 target`;
- correct sign, registered energy scaling and familywise significance of at least five sigma;
- survival of dummy, heater, sham, remount and second-rotor controls;
- Palo Alto replication compatible with the `1.183318` ratio.

Stop before P3 for unclosed containment, failed blind injection, unmatched reversal state, label-dependent correction, perpendicular reproduction, motor-command rather than retained-state tracking, or discretionary window dependence.

**Status:** protocol specification, not a physical result and not a spin authorization.
