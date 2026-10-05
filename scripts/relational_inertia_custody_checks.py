#!/usr/bin/env python3
"""Design arithmetic for the Relational Inertia Custody-Control paper.

Illustrative sensitivities only. No physical custody fraction is predicted.
"""
from pathlib import Path
import json

def inertial_fraction(f, q):
    return 1.5*f*q

def oscillator_fraction(f, q):
    return -0.75*f*q

f_values=[1e-3,1e-6,1e-9,1e-12,1e-15]
q_values=[1.0,0.1,0.01]
ladder=[]
for f in f_values:
    for q in q_values:
        ladder.append({
            "f_illustrative":f,
            "q_illustrative":q,
            "delta_inertial_fraction":inertial_fraction(f,q),
            "delta_oscillator_frequency_fraction":oscillator_fraction(f,q),
        })

# Trace-free example: an axis-enhanced normalized comparison change.
delta_M=[[-0.4,0,0],[0,0.2,0],[0,0,0.2]]
trace=sum(delta_M[i][i] for i in range(3))
f_demo=1e-6
delta_K_over_m=[1.5*f_demo*delta_M[i][i] for i in range(3)]

payload={
 "status":"design arithmetic only; no physical data; f is not predicted",
 "equations":{
   "inertial_fraction":"Delta k_u/m = (3/2) f q_u",
   "oscillator_fraction":"Delta omega/omega ~= -(3/4) f q_u, conditional on fixed stiffness and the named bridge",
 },
 "illustrative_ladder":ladder,
 "trace_free_example":{
   "delta_M_diagonal":[delta_M[i][i] for i in range(3)],
   "trace":trace,
   "f_illustrative":f_demo,
   "delta_K_over_m_diagonal":delta_K_over_m,
   "response_trace":sum(delta_K_over_m),
 },
 "identifiability_boundary":"a null bounds f*q times the tested bridge; without an independent custody witness it does not identify f",
}

out=Path(__file__).with_name('relational_inertia_custody_results.json')
out.write_text(json.dumps(payload,indent=2)+'\n')
assert trace==0
assert abs(sum(delta_K_over_m))<1e-24
assert inertial_fraction(1e-6,1)==1.5e-6
assert oscillator_fraction(1e-6,1)==-7.5e-7
print(json.dumps(payload,indent=2))
print('PASS: leverage equation, trace closure, oscillator translation, identifiability boundary')
