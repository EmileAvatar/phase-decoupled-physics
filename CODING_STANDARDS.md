# PDTP Coding Standards & Mathematical Rigor

This document defines the coding standards, mathematical rigor requirements,
and separation of concerns for all Python scripts and research documents in
the PDTP project.

**Purpose:** Every derivation, equation, and claim must survive scrutiny from
mathematicians and physicists. Incorrect math will break the project.
This document is the single reference for how to achieve that.

---

## 1. Script Structure

Every Python script must clearly state its purpose and scope at the top.

### 1.1 Required Header

Every script must begin with a docstring containing:

```python
"""
script_name.py -- [Short description]
=============================================

GOAL:
    What this script computes or tests. One paragraph max.

EQUATIONS USED:
    List every equation used, with source citations.
    Example:
        Eq 1: L = (1/2)(d_mu phi)(d^mu phi) + g cos(psi - phi)
               Source: PDTP Lagrangian (CLAUDE.md)
        Eq 2: E-L equation: d/dt(dL/d(phi_dot)) - dL/d(phi) = 0
               Source: Goldstein, Classical Mechanics, Eq 2.3

ASSUMPTIONS:
    List every assumption explicitly. Nothing implicit.
    Example:
        [A1] Spatially uniform fields: phi = phi(t) only, no spatial gradients.
             Justification: Standard first step in scalar field theory
             (Peskin & Schroeder sec 2.2, Goldstein sec 2.1).
        [A2] Small-amplitude oscillations for linearization.
             Justification: Required for eigenvalue analysis near equilibrium.

OUTPUT:
    What this script produces (data, not interpretation).
    Example:
        - Euler-Lagrange equations (symbolic)
        - Eigenvalues of coupled system matrix
        - Sudoku consistency scores (N/M pass)
"""
```

### 1.2 Function Naming Convention

Scripts must use these prefixes to separate concerns:

| Prefix | Purpose | Returns |
|--------|---------|---------|
| `derive_*()` | Pure symbolic math derivation | SymPy expressions |
| `verify_*()` | Independent re-derivation to cross-check | bool (pass/fail) |
| `compute_*()` | Numerical evaluation of derived formulas | Numbers with units |
| `run_sudoku_checks()` | Consistency tests against known physics | Scorecard |

**No interpretation in derivation functions.** A `derive_*()` function must
not contain print statements with physics interpretation. It returns symbolic
results. Period.

### 1.3 No Analysis in Code

Python scripts must output **data only**:
- Symbolic expressions
- Numerical values with units
- Pass/fail results
- Ratios and error metrics

**All interpretation belongs in research documents** (`.md` files in `docs/research/`).

The reporting layer (`print_utils.py`, `ReportWriter`) handles formatting
output to log files. Scripts call `rw.print()`, `rw.key_value()`, `rw.table()`
to output data — not to explain what the data means physically.

**Allowed in scripts:** "Eigenvalue lambda_1 = 2*sqrt(2)*g > 0 (unstable mode)"
**Not allowed in scripts:** "This unstable mode represents gravitational collapse,
suggesting that gravity emerges from..."

---

## 2. Mathematical Rigor

### 2.1 Every Equation Must Be Labeled

Use these tags in both code comments and documentation:

| Tag | Meaning | Requirement |
|-----|---------|-------------|
| `[ASSUMED]` | Taken as given, not derived here | Must cite source or state as axiom |
| `[DERIVED]` | Follows from assumptions via explicit steps | Must show all steps |
| `[VERIFIED]` | Independently confirmed by SymPy or numerical check | Must reference the verification |
| `[SPECULATIVE]` | Interpretation beyond what the math proves | Must be in a separate section |
| `[NEGATIVE]` | Tried and shown not to work | Must document why it fails |

### 2.2 Step-by-Step Derivations

Every derivation must show every step. No shortcuts.

**Bad:**
```
# It can be shown that the field equation is:
# box(phi) = g * sin(psi - phi)
```

**Good:**
```
# Start: L = (1/2)(phi_dot)^2 + g*cos(psi - phi)   [ASSUMED: PDTP Lagrangian]
# Step 1: dL/d(phi_dot) = phi_dot                    [partial derivative]
# Step 2: d/dt(dL/d(phi_dot)) = phi_ddot             [time derivative of Step 1]
# Step 3: dL/d(phi) = -g*sin(psi - phi)*(-1)         [chain rule on cos]
#        = g*sin(psi - phi)
# Step 4: E-L equation: phi_ddot - g*sin(psi - phi) = 0   [Step 2 - Step 3 = 0]
# Result: phi_ddot = g*sin(psi - phi)                [DERIVED]
# Verify: SymPy EL derivation matches                [VERIFIED: S1 PASS]
```

### 2.3 Sign Conventions

State sign conventions at the top of every derivation:

```python
# SIGN CONVENTIONS:
# - Metric signature: (+,-,-,-)
# - Lagrangian: L = T - V (kinetic minus potential)
# - Coupling: +cos (attractive/stable), -cos (repulsive/unstable)
# - Euler-Lagrange: d/dt(dL/d(q_dot)) - dL/d(q) = 0
```

### 2.4 Dimensional Analysis

Every new equation must pass dimensional analysis:

```python
# Dimensional check:
# [phi] = radians (dimensionless)
# [g] = rad/s^2 (angular frequency squared)
# [phi_ddot] = rad/s^2
# LHS: [phi_ddot] = rad/s^2    CHECK
# RHS: [g*sin(psi-phi)] = rad/s^2 * dimensionless = rad/s^2    CHECK
```

### 2.5 Trig Identities Must Be Explicit

Never use a trig identity without stating it:

```python
# Identity used: cos(A) - cos(B) = -2*sin((A+B)/2)*sin((A-B)/2)
# Source: standard trig (Abramowitz & Stegun 4.3.37)
# Applied with A = psi - phi_b, B = psi - phi_s:
#   (A+B)/2 = psi - (phi_b+phi_s)/2 = psi - phi_+
#   (A-B)/2 = -(phi_b-phi_s)/2 = -phi_-
# Result: cos(psi-phi_b) - cos(psi-phi_s) = 2*sin(psi-phi_+)*sin(phi_-)
```

---

## 3. Independent Verification

### 3.1 SymPy Verification Is Independent

SymPy verification must **re-derive from scratch**, not just confirm the answer.

**Bad (circular verification):**
```python
def verify_field_equation():
    # Just check that our stored result equals itself
    eq = phi_ddot - g * sp.sin(psi - phi)
    assert eq == 0  # This proves nothing
```

**Good (independent re-derivation):**
```python
def verify_field_equation():
    # Re-derive from the Lagrangian using SymPy's EL machinery
    L = Rational(1,2)*phi_dot**2 + g*sp.cos(psi - phi)
    # Compute dL/d(phi_dot)
    dL_dphidot = sp.diff(L, phi_dot)
    # Compute d/dt of that (via chain rule through phi_dot -> phi_ddot)
    ddt_term = sp.diff(dL_dphidot, phi) * phi_dot + sp.diff(dL_dphidot, phi_dot) * phi_ddot
    # Compute dL/d(phi)
    dL_dphi = sp.diff(L, phi)
    # E-L equation
    el_eq = ddt_term - dL_dphi
    # Solve for phi_ddot
    result = sp.solve(el_eq, phi_ddot)[0]
    expected = g * sp.sin(psi - phi)
    return sp.simplify(result - expected) == 0
```

### 3.2 Standard Model Compatibility Check

Every new prediction or equation must be tested for compatibility with the
Standard Model. PDTP must EXPLAIN the Standard Model, not contradict it.

**Check each of these:**

1. **Gauge invariance:** Does the new result preserve SU(3) x SU(2) x U(1)?
2. **Particle content:** Does it give the correct particles (quarks, leptons,
   gauge bosons, Higgs)? Does it accidentally predict new particles?
3. **Higgs mechanism:** Is it compatible with the Higgs field, electroweak
   symmetry breaking, and the measured Higgs mass (125 GeV)?
4. **Conservation laws:** Does it preserve baryon number, lepton number,
   electric charge, color charge?
5. **Known masses and couplings:** Does it reproduce (or at least not
   contradict) measured particle masses and coupling constants?
6. **Established experimental results:** Is it consistent with precision
   electroweak data, QCD lattice results, neutrino oscillations?

If a PDTP result contradicts any of the above, this must be:
- Explicitly documented as a TENSION
- Investigated to determine if it is a bug in the derivation or a genuine
  new prediction that differs from SM
- If genuine, added to `falsifiable_predictions.md` as a testable difference

### 3.3 Numerical Cross-Checks

Where possible, verify symbolic results numerically:

```python
# Symbolic result: eigenvalue = 2*sqrt(2)*g
# Numerical check at g = 1.0:
#   lambda = 2*sqrt(2)*1.0 = 2.8284...
#   Direct matrix eigenvalue: numpy.linalg.eigvals([[0,4],[2,0]])
#   = [+2.8284, -2.8284]   CHECK
```

### 3.3 No Hardcoded Assumptions Without Proof

Every physical constant substitution must be justified:

**Bad:**
```python
g = 1.22e19  # Planck mass in GeV
```

**Good:**
```python
# g coupling constant [ASSUMED: set to Planck scale for dimensional analysis]
# Justification: natural scale in quantum gravity; value not derived in PDTP
# This is a FREE PARAMETER of the theory (see Part 35, dim_transmutation.py)
g = M_P * C**2 / HBAR  # [rad/s^2], from m_cond = m_P
```

---

## 4. Separation of Concerns

### 4.1 File Organization

```
simulations/solver/
    # Derivation scripts (pure math, data output only)
    two_phase_lagrangian.py     # derives EL equations, eigenvalues, etc.
    reversed_higgs.py           # derives environment-dependent mass
    ...

    # Infrastructure (shared utilities)
    print_utils.py              # ReportWriter for formatted output
    sudoku_engine.py            # consistency check engine + constants
    sympy_checks.py             # SymPy verification library

    # Entry point
    main.py                     # orchestrates all phases, writes report

    # Output (generated, not tracked)
    outputs/                    # timestamped report files

docs/research/
    # Analysis and interpretation (separate from code)
    two_phase_analysis.md       # what the two-phase results MEAN
    falsifiable_predictions.md  # testable predictions (kept updated)
    ...
```

### 4.2 What Goes Where

| Content | Location | Example |
|---------|----------|---------|
| Symbolic derivation | `.py` script | `derive_euler_lagrange()` |
| Numerical computation | `.py` script | `compute_eigenvalues()` |
| Pass/fail verification | `.py` script | `run_sudoku_checks()` |
| Physical interpretation | `.md` research doc | "This eigenvalue implies..." |
| Speculative claims | `.md` research doc | "This may represent gravity..." |
| Falsifiable predictions | `falsifiable_predictions.md` | "Prediction 7: ..." |

### 4.3 Research Document Structure

Every research document should follow this structure:

```markdown
# Title

## Summary
One paragraph: what was done, what was found.

## Equations and Derivations
Step-by-step math with [ASSUMED]/[DERIVED]/[VERIFIED] tags.
Reference the Python script that verifies each result.

## Results (Data)
Numerical values, ratios, pass/fail scores.
No interpretation here — just the numbers.

## Analysis [SPECULATIVE]
Physical interpretation of the results.
Clearly marked as speculative where applicable.

## Predictions
Any new falsifiable predictions arising from this work.
Must also be added to falsifiable_predictions.md.

## Status
What is proven, what is open, what failed.
```

---

## 5. Falsifiable Predictions

### 5.1 Living Document

`docs/research/falsifiable_predictions.md` is a living document that must be
updated whenever new testable predictions are found.

**Rule:** Always plan before updating `falsifiable_predictions.md`.
Write out what predictions to add and get user approval first.

### 5.2 Prediction Format

Each prediction must include:

```markdown
### Prediction N: [Short name]

**Statement:** [Precise, testable claim]
**Derived from:** [Which Part/equation]
**Assumptions:** [What must be true for this prediction to hold]
**Test:** [How to test it — what experiment, what measurement]
**Expected value:** [Number with units and uncertainty estimate]
**Current status:** [Untested / Consistent with data / In tension / Ruled out]
**Distinguishes from:** [What competing theory gives a different answer]
```

### 5.3 Math Must Be Correct

Every prediction's derivation must be:
1. Step-by-step (no hand-waving)
2. SymPy verified (or explanation of why not)
3. Dimensionally consistent
4. Clearly labeled [ASSUMED] vs [DERIVED]

---

## 6. Long-Term Scientific Goals

The PDTP project aims to determine whether the phase-locking Lagrangian can produce:

1. **Effective spacetime geometry** — metric structure from condensate dynamics
2. **Particle-like wave solutions** — solitons, vortices, stable localized modes
3. **Long-range attractive forces** — 1/r^2 law from phase coupling
4. **Emergent gravitational behavior** — Newtonian limit, GR corrections

**Ultimate objective:** Connect matter-wave and spacetime-wave dynamics into a
framework capable of describing Standard Model interactions, gravity, and
spacetime structure — or clearly identify where and why it fails.

**This project is exploratory.** All interpretations must be clearly separated
from mathematical derivations. The math must stand on its own regardless of
whether the physical interpretation is correct.

---

## 7. Review Checklist

Before any script or document is committed, verify:

- [ ] Script header has GOAL, EQUATIONS USED, ASSUMPTIONS, OUTPUT
- [ ] Every equation tagged [ASSUMED], [DERIVED], [VERIFIED], or [SPECULATIVE]
- [ ] Sign conventions stated
- [ ] Dimensional analysis performed on new equations
- [ ] Trig identities stated explicitly (not used silently)
- [ ] SymPy verification re-derives independently (not circular)
- [ ] No physical interpretation in Python code (data output only)
- [ ] Interpretation in `.md` docs, clearly marked [SPECULATIVE] where needed
- [ ] Standard Model compatibility check performed (gauge invariance, particles, Higgs, conservation laws)
- [ ] New predictions added to `falsifiable_predictions.md` (with plan approval)
- [ ] No non-ASCII characters in `.py` files
- [ ] All URLs verified to be real, working links
