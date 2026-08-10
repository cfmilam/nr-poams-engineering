#!/usr/bin/env python3
"""nbody-n1 — T1 two-centre engine vs Pluto-Charon (N1a) and Earth-Moon (N1b).
Registration: NBODY-FORWARD.md §2 (committed 88acc0a BEFORE data pull).
DATA (retrieved 2026-08-10, en.wikipedia.org, provenance noted per value):
  Pluto-Charon (infobox 'Charon (moon)', citing Brozovic et al. 2024 / Buie 2006):
    r_p = 19592.61 km, r_a = 19598.92 km (periapsis/apoapsis, epoch 2452600.5)
    a_sep = 19595.764 km (planetocentric), e = 0.000161, T = 6.387221 d
    a2(Charon, barycentric) = 17181.0 km   [SUSPECT — tested below]
    comparison-only: GM ratio from masses M_C=1.5897e21 kg, '12.2% of Pluto'
  Earth-Moon (infobox+text 'Orbit of the Moon'):
    r_p = 363300 km (avg perigee), r_a = 405507 km (avg apogee)
    a1(Earth about barycentre) = 4670 km; vbar2(Moon, barycentric) = 1.022 km/s
    sidereal month = 27.322 d (comparison)
DECLARED INPUT DEVIATIONS from the registration (data availability, named):
  N1a: no precise published apsidal SPEED exists (infobox '0.21 km/s' is a 2-s.f.
       calculated note) -> the period T is used as the precision input instead
       (input-swap declared); partition datum = a2 as published (registered type).
  N1b: no published apsidal speed pair -> the Moon's published MEAN barycentric
       speed 1.022 km/s is the speed datum; mean-speed ellipse relation used
       (no T, no G): vbar = sqrt(mu/a)*(1 - e^2/4 - 3 e^4/64).
ENGINE RULE: G and masses appear NOWHERE in engine arithmetic. The pair invariant
mu_rel is a measured quantity (= h*v0 identically for an ellipse; = 4pi^2 a^3/T^2)."""
import math
D = 86400.0

print("="*78)
print("nbody-n1 — the two-centre momentum-ledger engine, no G, no masses")
print("="*78)

# ---------------- N1a: Pluto-Charon ----------------
rp, ra = 19592.61, 19598.92
T = 6.387221*D
a2_pub = 17181.0
a = 0.5*(rp+ra)
e = (ra-rp)/(ra+rp)
v_rel = 2*math.pi*a/T * (1 + e*e/4)     # mean relative speed (e^2 ~ 1e-8, negligible)
mu = (2*math.pi)**2 * a**3 / T**2       # pair invariant, measured (km^3/s^2)
print("\n-- N1a: Pluto-Charon --")
print(f"  geometry from (r_p, r_a): a_sep = {a:.3f} km  e = {e:.6f}  [pub: 19595.764, 0.000161]")
print(f"  pair invariant mu_rel = 4pi^2 a^3/T^2 = {mu:.1f} km^3/s^2  (no G, no masses)")
print(f"  [comparison only, NOT engine input: GM_P+GM_C (Brozovic 2024) ~ 975.5 -> {100*abs(mu-975.5)/975.5:.2f}% agreement]")
print(f"  v_rel (mean) = {v_rel*1000:.2f} m/s")
# partition with the published a2 (registered-type input)
a1_pred = a - a2_pub
v2 = v_rel*a2_pub/a; v1 = v_rel*a1_pred/a
print(f"  PARTITION using published a2 = {a2_pub} km:")
print(f"    predict a1(Pluto) = {a1_pred:.1f} km ; v2(Charon) = {v2*1000:.1f} m/s ; v1(Pluto) = {v1*1000:.1f} m/s")
# adjudication: same infobox's mass ratio (comparison data)
q = 0.12205   # M_C/M_P from the same source's masses (comparison only)
a1_alt = a*q/(1+q); a2_alt = a - a1_alt
print(f"  ADJUDICATION (comparison data, same source's mass ratio q = {q}):")
print(f"    a1 = {a1_alt:.1f} km, a2 = {a2_alt:.1f} km  ->  published a2 = 17181.0 is {100*(a2_alt-a2_pub)/a2_alt:.2f}% LOW")
print(f"    verdict: the two data in ONE infobox are mutually inconsistent; the engine's")
print(f"    partition arithmetic exposes it. Independent GMs side AGAINST 17181.0.")
print(f"    (infobox '0.21 km/s' matches neither partition: {v2*1000:.0f} or {v_rel*a2_alt/a*1000:.0f} m/s — 2 s.f. note, too coarse.)")

# ---------------- N1b: Earth-Moon ----------------
rp, ra = 363300.0, 405507.0
a1 = 4670.0
vbar2 = 1.022  # km/s, Moon about barycentre (published mean)
a = 0.5*(rp+ra)
e = (ra-rp)/(ra+rp)
a2 = a - a1
f2 = a2/a
vbar_rel = vbar2/f2
mu = (vbar_rel/(1 - e*e/4 - 3*e**4/64))**2 * a     # mean-speed relation: no T, no G
T_pred = 2*math.pi*math.sqrt(a**3/mu)/D
print("\n-- N1b: Earth-Moon --")
print(f"  geometry: a_sep = {a:.1f} km  e = {e:.5f}  [pub mean e: 0.0549]")
print(f"  partition from a1 = {a1} km: f2 = {f2:.5f}, a2(Moon) = {a2:.0f} km")
print(f"  mu_rel from mean-speed relation = {mu:.0f} km^3/s^2  (no G, no T input)")
print(f"  [comparison only: GM_E+GM_M ~ 403503]")
print(f"  (i) PREDICT period T = {T_pred:.3f} d  vs sidereal 27.322 d  -> {100*abs(T_pred-27.322)/27.322:.2f}%  "
      f"{'PASS (<=1.5%)' if abs(T_pred-27.322)/27.322 <= 0.015 else 'FAIL'}")
print(f"  (ii) PREDICT Moon barycentric apsides: {f2*rp:.0f} / {f2*ra:.0f} km (perigee/apogee about barycentre)")
print(f"       Earth speed amplitude v1 = {vbar2*a1/a2*1000:.1f} m/s (the Earth's monthly wobble)")
print(f"  (iii) apsidal speed ratio v_p/v_a = r_a/r_p = {ra/rp:.5f} — pure AM conservation (engine identity;")
print(f"        no independent published apsidal-speed pair in the consulted source — noted, not scored)")
print(f"  residual reading: the {100*abs(T_pred-27.322)/27.322:.2f}% period miss direction and size are the")
print(f"  registered THREE-BODY HANDOFF (solar perturbation) if >~0.5%; below that, data-grade agreement.")
