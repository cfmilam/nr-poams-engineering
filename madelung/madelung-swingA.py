#!/usr/bin/env python3
# Madelung swing M-A consistency instrument. Registration: b4ad780 (pre-run).
# Autonomous census system: t' = t + t^2 - sigma, sigma' = sigma(3-t)/2, p' = 1 - t.
# Launch from TF series at x0 = 1e-6 (Baker B1); stop s = 8 (pre-divergence guard).
import numpy as np, math

B1 = 1.5880710226113753
X0 = 1e-6
S_END = 8.0
N = 60000

# series launch: chi = 1 - B1 x + (4/3)x^{3/2} - (2B1/5)x^{5/2} + (1/3)x^3
x = X0
chi = 1 - B1*x + (4/3)*x**1.5 - (2*B1/5)*x**2.5 + (1/3)*x**3
chip = -B1 + 2*math.sqrt(x) - B1*x**1.5 + x*x
t0 = -x*chip/chi
sg0 = x**1.5*math.sqrt(chi)
p0 = math.log(x*chi)

s0 = math.log(X0)
h = (S_END - s0)/N

def F(y):
    t, sg, p = y
    return np.array([t + t*t - sg, sg*(3.0 - t)*0.5, 1.0 - t])

ys = np.empty((N+1, 3))
ys[0] = (t0, sg0, p0)
y = ys[0].copy()
for i in range(N):
    k1 = F(y); k2 = F(y + 0.5*h*k1); k3 = F(y + 0.5*h*k2); k4 = F(y + h*k3)
    y = y + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    ys[i+1] = y
T = ys[:, 0]; SG = ys[:, 1]; P = ys[:, 2]
svals = s0 + h*np.arange(N+1)

# GUARD ENFORCEMENT (registered): truncate at first non-monotone/nan index
# (saddle float-divergence); all data used must lie strictly before it.
bad = np.where(~(np.diff(T) > 0) | ~np.isfinite(T[1:]) | (T[1:] >= 3.0))[0]
cut = int(bad[0]) if len(bad) else N
T = T[:cut]; SG = SG[:cut]; P = P[:cut]; svals = svals[:cut]
print("guard: divergence at s = %.3f (t = %.4f) -> truncated; t monotone on kept range %s | t_max %.6f"
      % (svals[-1], T[-1], bool(np.all(np.diff(T) > 0)), float(T.max())))

# S at t = 1 (cubic interpolation on the monotone grid)
i1 = int(np.searchsorted(T, 1.0))
sl = slice(max(0, i1-2), i1+2)
S_dip = float(np.interp(1.0, T[sl], SG[sl]))
p_pk = float(np.interp(1.0, T[sl], P[sl]))
print("S = sigma(t=1) = %.9f  (booked 1.467319754, dS = %+.2e)" % (S_dip, S_dip - 1.467319754))
m0 = 2.0 - S_dip
anchor = 1.0/math.sqrt(2.0*m0)
print("peak anchor 1/sqrt(2(2-S)) = %.6f  (booked M2 worst ratio 0.9687)" % anchor)

V = np.exp(P - p_pk)
# outer branch arrays (t > 1): v strictly decreasing
out = T > 1.0
T_o = T[out]; V_o = V[out]

def pair(v):
    # find tau on outer branch with V_o = v (V_o decreasing)
    j = int(np.searchsorted(-V_o, -v))
    j = min(max(j, 1), len(V_o)-1)
    w = (v - V_o[j]) / (V_o[j-1] - V_o[j])
    return float(T_o[j] + w*(T_o[j-1] - T_o[j]))

print("\n%-6s %-9s %-9s %-10s %-10s %-9s" % ("t_in", "v", "tau", "Psi", "ratio", "1-ratio"))
grid = [0.005, 0.01, 0.02] + [round(0.06 + 0.04*i, 2) for i in range(24)]  # 0.005/0.01 = DIAGNOSTIC rows (unregistered, report-only)
worstPsi = -1e9; rows = []
for t_in in grid:
    i = int(np.searchsorted(T, t_in))
    v = float(np.interp(t_in, T[i-2:i+2], V[i-2:i+2]))
    tau = pair(v)
    b_in = 1.0 - t_in; b_out = tau - 1.0
    Psi = 1.0/b_in + 1.0/b_out - 2.0/math.sqrt(1.0 - v)
    ratio = math.sqrt(1.0 - v)*(1.0/b_in + 1.0/b_out)/2.0   # sigma*/sigma_hat
    rows.append((t_in, v, tau, Psi, ratio))
    worstPsi = max(worstPsi, Psi)
    print("%-6.2f %-9.5f %-9.5f %-10.5f %-9.5f %-9.5f" % (t_in, v, tau, Psi, ratio, 1-ratio))

# gates
gA2 = worstPsi < 0
print("\nG-A2 Psi < 0 on full grid:", "PASS (max Psi = %.5f)" % worstPsi if gA2 else "FAIL (max %.5f)" % worstPsi)
gA3s = abs(S_dip - 1.467319754) < 1e-6
r95 = [r for r in rows if r[0] == 0.94][0][4]; r98 = [r for r in rows if r[0] == 0.98][0][4]
r_extrap = r98 + (r98 - r95)/(0.98 - 0.94)*(1.0 - 0.98)
gA3r = abs(r_extrap - 0.9687) <= 0.002
print("G-A3 S reproduction: %s | peak-ratio extrapolation %.4f vs 0.9687: %s"
      % ("PASS" if gA3s else "FAIL", r_extrap, "PASS" if gA3r else "FAIL"))
psi_eye = [r for r in rows if r[0] == 0.02][0][3]
gA4 = abs(psi_eye - (-0.5)) <= 0.03
print("G-A4 eye limit: Psi(0.02) = %.4f vs -0.5 +- 0.03:" % psi_eye, "PASS" if gA4 else "FAIL")
print("   diagnostic (report-only): Psi(0.01) = %.4f, Psi(0.005) = %.4f — approach to -1/2 is"
      % ([r for r in rows if r[0]==0.01][0][3], [r for r in rows if r[0]==0.005][0][3]))
print("   O(x_out^-0.772): the Sommerfeld saddle eigenvalue (sqrt(73)-7)/2 = %.4f controls the eye margin"
      % ((math.sqrt(73)-7)/2))
ratios = [r[4] for r in rows]
i_max = ratios.index(max(ratios))
print("G-A5 report: ratio profile max at t_in = %.2f (ratio %.4f); ratio at v=0.75 row:" % (rows[i_max][0], rows[i_max][4]))
for r in rows:
    if abs(r[1] - 0.75) < 0.04:
        print("   t_in %.2f v %.3f ratio %.4f (M2 booked min margin 0.230 at v=0.75 — margin metric 1-ratio = %.3f)"
              % (r[0], r[1], r[4], 1 - r[4]))
