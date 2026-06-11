# PDTP — Phase-Decoupled Transport Physics

## Project Summary
Speculative physics framework:
gravity emerges from phase-locking between matter-waves and spacetime-waves.

Status:
- Exploratory
- Not experimentally validated
- Formalization in progress

Repository:
EmileAvatar/phase-decoupled-physics

---

# Active Goals

## Goal 1 — Emergent Gravity
Primary objective:
derive gravity as emergent phase-locking behavior from the PDTP Lagrangian.

Requirements:
- Recover Newtonian gravity
- Recover GR approximations where possible
- Produce falsifiable predictions
- Verify mathematical consistency

## Goal 2 — Phase Decoupling (Future)
Investigate:
alpha = cos(psi - phi) -> 0

This depends entirely on Goal 1 succeeding.

---

# Core Equations

## U(1) Phase-Locking Lagrangian
L = 1/2(d_mu phi)(d^mu phi)
  + SUM_i 1/2(d_mu psi_i)(d^mu psi_i)
  + SUM_i g_i cos(psi_i - phi)

Field equation:
box(phi) = SUM_i g_i sin(psi_i - phi)

Coupling:
alpha = cos(psi - phi)

---

## Two-Phase Extension
L = +g cos(psi - phi_b)
    - g cos(psi - phi_s)

Definitions:
- phi_b = bulk phase
- phi_s = surface phase

Known derived behavior:
- Newton 3rd law behavior
- Biharmonic gravity structure
- Jeans instability

Status:
16/16 re-derivation tests passed.

---

# Repository Structure

docs/
    core_concepts/
    technical/
    research/
    applications/

simulations/
assets/images/

Elastic_Universe/
    Separate speculative project

TODO_04.md
    Active work only

---

# Critical Coding Rules

## Python
- ASCII only in .py files
- Save outputs to log files
- No hardcoded verification outputs
- Separate:
    derive_*
    verify_*
    compute_*

## Verification
Every important result must:
- show derivation
- include SymPy verification where applicable
- distinguish:
    [ASSUMED]
    [DERIVED]
    [VERIFIED]
    [SPECULATIVE]

## Research Docs
Must include:
- derivation
- intermediate steps
- numerical values
- plain English explanation

---

# SymPy Verification

Use:
simulations/solver/sympy_checks.py

Required for:
- field equations
- EOS claims
- symmetry claims
- algebraic identities

---

# Problem Solving Protocol

Before deep investigations:
1. Read docs/Methodology.md
2. Create a plan
3. Present plan
4. Then proceed

---

# TODO Rules

Use:
TODO_04.md

Do:
- one task at a time
- small scoped updates
- modular work

Avoid:
- loading old TODO archives unless required

---

# External AI Reviews

When reviewing ChatGPT/DeepSeek/etc:
- evaluate ideas on their own merits
- remember they lack full project context
- distinguish user hypotheses from AI analysis

---

# Context Optimization Rules

Keep active context small:
- current task only
- relevant files only
- avoid archive loading

Exclude:
- outputs/
- logs/
- old TODOs
- generated assets
- large archives

---

# Elastic Universe

Elastic_Universe/ is separate from PDTP.

Rules:
- no automatic crossover into PDTP
- all claims remain speculative
- validate independently before reuse

---

# URL Rules

All URLs must:
- be real
- verified
- checked before commit

Use:
check_urls.py

---

# Status

Speculative framework.
Research and formalization in progress.