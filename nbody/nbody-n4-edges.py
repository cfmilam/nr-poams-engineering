#!/usr/bin/env python3
# N4a/b edge extraction — procedure as REGISTERED 2026-08-11 01:40 (ledger 42e5511).
# Pull JPL SBDB numbered asteroids (a,e,H), 2.30-3.50 AU, H<=15 superset (local ladder).
import json, math, os, subprocess, statistics, sys

CACHE = "data/nbody-n4-sbdb.json"
os.makedirs("data", exist_ok=True)
if not os.path.exists(CACHE) or os.path.getsize(CACHE) < 1000:
    cmd = ["curl", "-sS", "-G", "https://ssd-api.jpl.nasa.gov/sbdb_query.api",
           "--data-urlencode", "fields=a,e,H",
           "--data-urlencode", "sb-kind=a",
           "--data-urlencode", "sb-ns=n",
           "--data-urlencode", 'sb-cdata={"AND":["a|GE|2.30","a|LE|3.50","H|LE|15"]}',
           "-o", CACHE]
    subprocess.run(cmd, check=True, timeout=150)
with open(CACHE) as f: J = json.load(f)
if "data" not in J:
    print("API ERROR:", str(J)[:500]); sys.exit(1)
rows = []
for r in J["data"]:
    try: rows.append((float(r[0]), float(r[1]), float(r[2])))
    except (TypeError, ValueError): pass
print(f"pulled rows (H<=15, 2.30-3.50): {len(rows)}   [count field: {J.get('count')}]")

A0, A1, BW = 2.30, 3.50, 0.005
NB = round((A1-A0)/BW)
def hist(sample):
    h = [0]*NB
    for a,_,_ in sample:
        i = int((a-A0)/BW)
        if 0 <= i < NB: h[i] += 1
    return h
def wbins(lo,hi):  # bins fully inside [lo,hi]
    return [i for i in range(NB) if A0+i*BW >= lo-1e-9 and A0+(i+1)*BW <= hi+1e-9]

GAPS = [  # name, computed center, flanks [(lo,hi),...], one_sided, comp dA, factor(None=report-only)
    ("3:1", 2.502, [(2.36,2.46),(2.54,2.64)], False, 0.0144, 3.0),
    ("5:2", 2.825, [(2.72,2.79),(2.86,2.91)], False, 0.0183, None),
    ("7:3", 2.958, [(2.88,2.93),(2.99,3.02)], False, 0.0160, None),
    ("2:1", 3.279, [(3.10,3.22)],             True,  0.0785, 2.0),
]

# Fallback ladder on PRIMARY sample flank medians (registered floor 20/bin)
Hcut = None
for hc in (13.0, 14.0, 15.0):
    prim = [(a,e,H) for a,e,H in rows if H <= hc and 0.10 <= e <= 0.20]
    h = hist(prim)
    meds = [statistics.median([h[i] for fl in flanks for i in wbins(*fl)])
            for _,_,flanks,_,_,_ in GAPS]
    if min(meds) >= 20: Hcut = hc; break
if Hcut is None: Hcut = 15.0; prim = [(a,e,H) for a,e,H in rows if 0.10 <= e <= 0.20]
h = hist(prim)
alle = hist([(a,e,H) for a,e,H in rows if H <= Hcut])
print(f"H cut used (ladder): H<={Hcut}   primary sample (e in [0.10,0.20]): {len(prim)}")

def extract(h, name, c, flanks, one_sided, tag):
    fb = [h[i] for fl in flanks for i in wbins(*fl)]
    nbg = statistics.median(fb); thr = 0.5*nbg
    # recenter to min-count bin within +-0.02 AU
    cand = [i for i in range(NB) if abs(A0+(i+0.5)*BW - c) <= 0.02+1e-9]
    ic = min(cand, key=lambda i: (h[i], abs(A0+(i+0.5)*BW - c)))
    cc = A0+(ic+0.5)*BW
    if h[ic] >= thr:
        print(f"  {tag} {name}: NO sub-threshold run (bin@{cc:.3f}={h[ic]}, thr={thr:.1f}) -> REGISTERED NULL (osculating smear)")
        return None
    iL = ic
    while iL-1 >= 0 and h[iL-1] < thr: iL -= 1
    iR = ic
    while iR+1 < NB and h[iR+1] < thr: iR += 1
    aL, aR = A0+iL*BW, A0+(iR+1)*BW
    da = (cc - aL) if one_sided else (aR-aL)/2
    print(f"  {tag} {name}: N_bg={nbg:.0f} thr={thr:.1f} center@{cc:.3f} run [{aL:.3f},{aR:.3f}]"
          f"{' ONE-SIDED' if one_sided else ''}  half-width = {da:.4f} AU")
    return da

print("\n-- PRIMARY (e in [0.10,0.20], H<=%.0f) --" % Hcut)
res = {}
for name,c,flanks,os_,comp,fac in GAPS:
    res[name] = extract(h, name, c, flanks, os_, "P")
print("\n-- SECONDARY all-e (report-only) --")
for name,c,flanks,os_,comp,fac in GAPS:
    extract(alle, name, c, flanks, os_, "S")

print("\n-- VERDICTS (registered criteria) --")
for name,c,flanks,os_,comp,fac in GAPS:
    meas = res[name]
    if meas is None:
        print(f"  {name}: NULL (named handoff to proper elements)"); continue
    f = max(comp/meas, meas/comp)
    line = f"  {name}: computed {comp:.4f} vs measured {meas:.4f} AU -> factor {f:.2f}"
    if fac: line += f"  [{'PASS' if f <= fac else 'FAIL'} vs registered factor {fac:.0f}]"
    else:   line += "  [report-only]"
    print(line)
