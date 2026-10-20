Direct Arrival: A Silicon Correspondence for Coupled Ledgers
Public edition 1.0 — 19 October 2026

Read the HTML paper or downloads/direct-arrival-silicon-correspondence.pdf.
The source paper is paper.md. Equations in the HTML use native MathML.

To reproduce the mathematical checks:
  Install Python 3.11+ and Node.js 20+.
  Download verify.py, direct-arrival-model-core.js and requirements.txt into one folder.
  python3 -m venv .venv
  .venv/bin/python -m pip install -r requirements.txt
  .venv/bin/python verify.py

The checker writes verification.json beside itself. Its timestamp is run-specific.
The model-core and verifier hashes identify the tested source. No network access,
instrument connection, production audio or paid service is used by the checks.
The checks concern the conditional mathematics, not physical measurements.
