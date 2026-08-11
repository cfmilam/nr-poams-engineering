#!/usr/bin/env python3
# Swing 14 — capacity-packing enumeration. Registration: ledger fdcf31e (pre-run).
import numpy as np, math

RHO = 0.138; CORE = 1.72; ZC = 4.78
HB2M = 41.47; RQ = 0.86
DP = HB2M/(4*RQ*RQ)                       # 14.02
C3 = HB2M*0.75/(18*RQ*RQ)                 # 2.336
C4 = HB2M*0.5/(32*RQ*RQ)                  # 0.876
H  = 0.84
BOOKS = 35.85

def lattice(kind):
    """return (points array in one conventional cell, cell vectors scaled to rho0, label)"""
    if kind == "sc":   basis = [[0,0,0]]; npc = 1
    elif kind == "bcc": basis = [[0,0,0],[.5,.5,.5]]; npc = 2
    elif kind == "fcc": basis = [[0,0,0],[.5,.5,0],[.5,0,.5],[0,.5,.5]]; npc = 4
    elif kind == "diamond":
        basis = [[0,0,0],[.5,.5,0],[.5,0,.5],[0,.5,.5],
                 [.25,.25,.25],[.75,.75,.25],[.75,.25,.75],[.25,.75,.75]]; npc = 8
    elif kind == "A15":
        basis = [[0,0,0],[.5,.5,.5],
                 [.25,0,.5],[.75,0,.5],[.5,.25,0],[.5,.75,0],[0,.5,.25],[0,.5,.75]]; npc = 8
    else: raise ValueError(kind)
    a = (npc/RHO)**(1/3.0)
    return np.array(basis, float), a

def periodic_census(basis, a, reach, reps=5):
    """census on periodic lattice via minimum-image over reps^3 supercell"""
    pts = []
    for i in range(reps):
        for j in range(reps):
            for k in range(reps):
                for b in basis:
                    pts.append(((np.array([i,j,k]) + b) * a))
    pts = np.array(pts); Lbox = reps*a
    N = len(pts)
    d = pts[:,None,:] - pts[None,:,:]
    d -= Lbox*np.round(d/Lbox)
    d2 = np.einsum('ijk,ijk->ij', d, d)
    np.fill_diagonal(d2, 1e9)
    dmin = math.sqrt(d2.min())
    A = d2 <= reach*reach
    deg = A.sum(1)
    nbrs = [np.flatnonzero(A[i]) for i in range(N)]
    # census on central-cell bonds only (all equivalent by symmetry; sample subset)
    bonds = [(i,j) for i in range(min(N, 4*len(basis))) for j in nbrs[i] if j > i]
    if not bonds:
        return dmin, deg.mean(), 0.0, 0.0, 0
    P2s, P3s = [], []
    for (i,j) in bonds:
        Ni, Nj = set(nbrs[i]), set(nbrs[j])
        P2s.append(len((Ni & Nj) - {i,j}))
        c3 = 0
        for x in Nj - {i}:
            for y in (set(nbrs[x]) & Ni) - {i,j}:
                if x != y: c3 += 1
        P3s.append(c3)
    return dmin, deg.mean(), float(np.mean(P2s)), float(np.mean(P3s)), len(bonds)

def compose(z, p2, p3):
    if z <= 0: return 0.0
    per_bond = DP + H + C3*max(0.0, p2-1) + C4*p3
    return (z/2.0)*min(1.0, ZC/z)*per_bond

print("candidate | reach | d_min | z | P2 | P3 | G/quantum | notes")
rows = {}
for kind in ("sc","bcc","fcc","diamond","A15"):
    basis, a = lattice(kind)
    for reach in (2.06, 2.14, 2.22):
        dmin, z, p2, p3, nb = periodic_census(basis, a, reach)
        feas = "CORE-VIOLATION" if dmin < CORE else ("no-bonds" if z == 0 else "")
        G = compose(z, p2, p3) if dmin >= CORE else 0.0
        rows[(kind, reach)] = (dmin, z, p2, p3, G, feas)
        print("%-8s | %.2f | %.3f | %5.2f | %5.2f | %6.2f | %6.2f | %s"
              % (kind, reach, dmin, z, p2, p3, G, feas))

# hcp via explicit points (finite slab, central sample)
a = (2.0/(RHO*math.sqrt(2)))**(1/3.0); c = a*math.sqrt(8.0/3.0)
pts = []
R = 4
for i in range(-R,R+1):
    for j in range(-R,R+1):
        for k in range(-R,R+1):
            o = np.array([ (i + 0.5*j)*a, j*a*math.sqrt(3)/2, k*c ])
            pts.append(o)
            pts.append(o + np.array([0.5*a, a/(2*math.sqrt(3)), c/2]))
pts = np.array(pts)
center = pts[np.argmin(np.einsum('ij,ij->i', pts, pts))]
d2all = np.einsum('ij,ij->i', pts-center, pts-center)
sel = pts[d2all <= (6*a)**2]
N = len(sel)
d2 = np.einsum('ijk,ijk->ij', sel[:,None,:]-sel[None,:,:], sel[:,None,:]-sel[None,:,:])
np.fill_diagonal(d2, 1e9)
for reach in (2.06, 2.14, 2.22):
    A = d2 <= reach*reach
    nbrs = [np.flatnonzero(A[i]) for i in range(N)]
    interior = [i for i in range(N) if np.sqrt(((sel[i]-center)**2).sum()) < 3*a]
    zbar = np.mean([len(nbrs[i]) for i in interior])
    bonds = [(i,j) for i in interior for j in nbrs[i] if j > i]
    if bonds:
        P2s, P3s = [], []
        for (i,j) in bonds:
            Ni, Nj = set(nbrs[i]), set(nbrs[j])
            P2s.append(len((Ni & Nj)-{i,j}))
            c3 = 0
            for x in Nj-{i}:
                for y in (set(nbrs[x]) & Ni)-{i,j}:
                    if x != y: c3 += 1
            P3s.append(c3)
        p2, p3 = float(np.mean(P2s)), float(np.mean(P3s))
    else: p2 = p3 = 0.0
    dmin = math.sqrt(d2.min())
    G = compose(zbar, p2, p3) if dmin >= CORE else 0.0
    print("%-8s | %.2f | %.3f | %5.2f | %5.2f | %6.2f | %6.2f | %s"
          % ("hcp", reach, dmin, zbar, p2, p3, G, "" if zbar>0 else "no-bonds"))

# finite contact-order references (local census, homogeneity caveat)
def finite_census(pts, reach, label):
    pts = np.array(pts); N = len(pts)
    d2 = np.einsum('ijk,ijk->ij', pts[:,None,:]-pts[None,:,:], pts[:,None,:]-pts[None,:,:])
    np.fill_diagonal(d2, 1e9)
    A = d2 <= reach*reach
    nbrs = [np.flatnonzero(A[i]) for i in range(N)]
    # interior = max-degree third
    deg = A.sum(1)
    thresh = np.quantile(deg, 0.5)
    interior = [i for i in range(N) if deg[i] >= thresh]
    bonds = [(i,j) for i in interior for j in nbrs[i] if j > i]
    P2s, P3s = [], []
    for (i,j) in bonds:
        Ni, Nj = set(nbrs[i]), set(nbrs[j])
        P2s.append(len((Ni & Nj)-{i,j}))
        c3 = 0
        for x in Nj-{i}:
            for y in (set(nbrs[x]) & Ni)-{i,j}:
                if x != y: c3 += 1
        P3s.append(c3)
    z = float(np.mean([len(nbrs[i]) for i in interior]))
    p2 = float(np.mean(P2s)) if P2s else 0.0
    p3 = float(np.mean(P3s)) if P3s else 0.0
    # local density: N inside a sphere of radius = max dist of interior pts + core/2
    print("%-8s | %.2f | %.3f | %5.2f | %5.2f | %6.2f | %6.2f | local ref (not at rho0)"
          % (label, reach, math.sqrt(d2.min()), z, p2, p3, compose(z, p2, p3)))

# tetrahelix (Boerdijk-Coxeter) at contact edge = CORE*1.02
edge = CORE*1.02
th = []
r = 3*math.sqrt(3)/10*edge; hstep = edge/math.sqrt(10); theta = math.acos(-2/3.0)
for n in range(40):
    th.append([r*math.cos(n*theta), r*math.sin(n*theta), n*hstep])
finite_census(th, 2.14, "tetrahx")

# icosahedron-13 at center-vertex = CORE*1.02
cv = CORE*1.02
phi_g = (1+math.sqrt(5))/2
ico = [[0,0,0]]
raw = []
for s1 in (1,-1):
    for s2 in (1,-1):
        raw += [[0, s1, s2*phi_g],[s1, s2*phi_g, 0],[s2*phi_g, 0, s1]]
nrm = math.sqrt(1+phi_g**2)
for v in raw: ico.append([cv*x/nrm for x in v])
finite_census(ico, 2.14, "icos13")

print("\nBooks target C = %.2f, window [32, 40]" % BOOKS)
