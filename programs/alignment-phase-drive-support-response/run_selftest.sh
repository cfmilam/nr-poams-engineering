#!/bin/bash
# run_selftest.sh — four synthetic cases through static_gate_reduce.py
set -e
cd "$(dirname "$0")"
python3 - <<'GEN'
import csv, random
def abba_block(wr, rt, a, b, base, diff, quads, sig):
    for i in range(quads):  # A B B A
        wr.writerow([f"t{rt}{i}a", rt, a, f"{base + diff/2 + random.gauss(0,sig):.4f}"])
        wr.writerow([f"t{rt}{i}b", rt, b, f"{base - diff/2 + random.gauss(0,sig):.4f}"])
        wr.writerow([f"t{rt}{i}c", rt, b, f"{base - diff/2 + random.gauss(0,sig):.4f}"])
        wr.writerow([f"t{rt}{i}d", rt, a, f"{base + diff/2 + random.gauss(0,sig):.4f}"])
def make(name, main_diff, remount_diff, include_remount=True, seed=7):
    random.seed(seed)
    with open(name, "w", newline="") as f:
        wr = csv.writer(f); wr.writerow(["timestamp","run_type","bias_state","reading_mg"])
        abba_block(wr, "dummy",   "N","S", 2700.0, 0.000, 13, 0.004)
        abba_block(wr, "main",    "N","S", 2707.0, main_diff, 25, 0.004)
        abba_block(wr, "ew_null", "E","W", 2707.0, 0.000, 8, 0.004)
        abba_block(wr, "empty",   "N","S",  120.0, 0.000, 4, 0.004)
        if include_remount:
            abba_block(wr, "remount", "N","S", 2707.0, remount_diff, 4, 0.004)
make("selftest_null.csv", 0.004, 0.004, seed=7)
make("selftest_contrast.csv", 0.100, 0.100, seed=11)      # contrast REPRODUCES after remount
make("selftest_missing_remount.csv", 0.004, 0.0, include_remount=False, seed=13)
GEN
V1=$(python3 static_gate_reduce.py selftest_null.csv --gradient-pre 0.8 --gradient-post 0.9 | python3 -c "import sys,json; print(json.load(sys.stdin)['verdict'])")
V2=$(python3 static_gate_reduce.py selftest_contrast.csv --gradient-pre 0.8 --gradient-post 0.9 | python3 -c "import sys,json; print(json.load(sys.stdin)['verdict'])")
V3=$(python3 static_gate_reduce.py selftest_missing_remount.csv --gradient-pre 0.8 --gradient-post 0.9 | python3 -c "import sys,json; print(json.load(sys.stdin)['verdict'])")
V4=$(python3 static_gate_reduce.py selftest_null.csv --gradient-pre 1.5 --gradient-post 0.9 | python3 -c "import sys,json; print(json.load(sys.stdin)['verdict'])")
echo "null:$V1 contrast:$V2 missing_remount:$V3 gradient_fail:$V4"
[ "$V1" = "NULL" ] && [ "$V2" = "CONTRAST" ] && [ "$V3" = "GATE0_FAIL" ] && [ "$V4" = "GATE0_FAIL" ] && echo "SELFTEST: PASS" || { echo "SELFTEST: FAIL"; exit 1; }
