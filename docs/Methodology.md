# Methodology — How We Work

## What Methodology Are We Using?

### The Sudoku Consistency Check

The core internal tool is the **Sudoku consistency check**: take a new candidate
value or equation, substitute it into 10+ known established equations, and score
each result as a ratio. Ratios within 1% = MATCH; anything else = contradiction.

This is not a custom invention — it is standard scientific practice under several
names:

- **Overdetermined system testing** — more equations than unknowns, so consistency
  across all of them is a strong signal the candidate is right
- **Proof by contradiction** — if the candidate is wrong, contradictions appear;
  find them and they tell you *where* the assumption breaks, not just *that* it does
- **Regression residuals** — how wrong is the model across many independent tests?

The "Sudoku" framing is our label for the methodology. The logic is universal.

**Reference implementation:** `simulations/sudoku_consistency_check.py`

---

### Historical Parallels

These are examples of scientists using the same core strategies we use.
Each one is a template for a class of problem-solving move.

#### Maxwell's Displacement Current — Scaffolding That Became Real

Maxwell noticed Ampere's law violated charge conservation inside a capacitor.
He added a term `∂E/∂t` to *fix the mathematical inconsistency*, not because he
observed it. That term predicted radio waves — confirmed 20 years later by Hertz.

**The move:** Introduce a new term demanded by internal consistency. Treat it as
real and derive its consequences. Let experiment confirm or deny it.

**PDTP parallel:** The `+cos(ψ−φ)` coupling was chosen because it gives stable
phase-locking (the pendulum test), not observed directly. The breathing mode
prediction follows from it — testable later.

---

#### Dirac's Equation — Forced Consequences

Dirac demanded his equation be both relativistic AND quantum mechanical. The math
forced him to accept negative-energy solutions he did not want — which turned out
to be antiparticles, discovered two years later.

**The move:** Apply multiple simultaneous constraints. Accept what the math gives
you, even if it is unexpected. The surprise is the prediction.

**PDTP parallel:** The SU(3) extension was the natural generalisation of U(1).
Z₃ vortices (quarks) and 8 gluons fell out of the algebra automatically — not
assumed, derived from symmetry.

---

#### Einstein's Equivalence Principle — Postulate and Derive

Not derived — *postulated* as a guiding constraint: inertial mass equals
gravitational mass. Used to derive everything else. Chosen because it was the
simplest assumption consistent with known facts.

**The move:** When you cannot derive something from first principles, postulate it
clearly, mark it as a postulate, and see how far it carries you.

**PDTP parallel:** The phase-locking hypothesis is our equivalence principle.
Gravity is emergent phase coherence between matter-waves and spacetime-waves.
We are deriving consequences, not proving it from scratch.

---

#### Landau's Order Parameter — Symmetry Before Microscopy

Landau said: near a phase transition there must be some field φ that is zero in
one phase and nonzero in another. He did not know what φ was physically. He used
symmetry to constrain its form. Ginzburg-Landau theory came first; the BCS
microscopic explanation came 10 years later.

**The move:** Write down the most general field consistent with the symmetry of
the problem. The microscopic origin can come later. The macroscopic structure
is already predictive.

**PDTP parallel:** Our φ (spacetime condensate phase) is a Landau order parameter
for gravitational phase-locking. We do not yet know the "atoms" of the condensate.

---

#### Wilson's Lattice QCD — Scaffolding as Numerical Tool

Wilson could not solve QCD analytically in the strong-coupling regime. He put
spacetime on a discrete lattice and computed numerically. The lattice is not
physical — it is scaffolding that lets you extract real numbers (string tension,
hadron masses) which then match experiment.

**The move:** When the continuum theory is intractable, discretise it, compute,
and then take the continuum limit. The scaffold comes down; the result remains.

**PDTP parallel:** Exactly what Parts 38–41 are doing with `su3_lattice.py`.
The lattice is the tool, not the theory.

---

### Where PDTP Sits on the Methodology Spectrum

| Stage | Description | PDTP status |
|---|---|---|
| Analogy | Map new phenomenon to known one | Done (wave optics, BEC, QCD) |
| Lagrangian | Write down symmetry-constrained action | Done (U(1), SU(3)) |
| Consistency | Sudoku check — no internal contradictions | Ongoing |
| Prediction | Derive falsifiable, testable numbers | Done (6 predictions) |
| Scaffolding becomes real | Predicted phenomena observed | Not yet — needs experiment |

We are in the middle phase — the same place Maxwell was when he had the equations
but had not yet seen radio waves.

---

---

## Problem-Solving Checklist

A generic checklist to work through when stuck on a hard problem.
Not every item applies to every problem — treat it as a menu, not a procedure.
Check off what you have tried. Untried items are where the answer may be hiding.

---

### 1. Reframe the Problem

- [ ] **Change the field or lens** — how would a condensed matter physicist see this?
  A topologist? An engineer? An information theorist?
- [ ] **What-if scenario** — swap one assumption and re-derive. What changes?
- [ ] **Invert the problem** — solve for what you do *not* want, then negate it
- [ ] **Zoom in** — strip to the simplest non-trivial toy model (1D, 2-particle, etc.)
- [ ] **Zoom out** — does the problem look different at a larger scale or longer time?
- [ ] **Rename everything** — give variables neutral names to remove preconceptions
  about what they "should" be
- [ ] **State the problem in one sentence** — if you cannot, the problem is not
  yet well-defined

---

### 2. Introduce Something New (Maxwell-Style Scaffolding)

- [ ] **Add a new term to the equation** — what term, if added, would make the
  inconsistency disappear? Is it physical? Can it be tested?
- [ ] **Add a new variable** — what hidden quantity, if it exists, would close the gap?
- [ ] **Add a constraint** — demand self-consistency, conservation, or symmetry,
  and see what it forces
- [ ] **Change the symmetry group** — if U(1) is stuck, try SU(2) or SU(3).
  If ℝ is stuck, try a compact space. Generalise the symmetry.
- [ ] **Postulate and derive** — if derivation fails, state it as a postulate,
  mark it clearly, and derive consequences. Let the consequences be tested.
- [ ] **Introduce a scale** — does the problem have a natural length, time, or
  energy scale you have not used? What sets it?
- [ ] **Introduce an order parameter** — is there a field that is zero in one
  regime and nonzero in another? What symmetry does it break?

---

### 3. Consistency Checks

- [ ] **Sudoku check** — substitute the candidate into 10+ known equations.
  Score ratios. Contradictions tell you where the assumption breaks.
- [ ] **Limiting cases** — does the result reduce to known physics in the
  appropriate limits? (weak field, low energy, large N, etc.)
- [ ] **Dimensional analysis** — check every term has the right units.
  If not, a factor is missing.
- [ ] **Sign and direction conventions** — verify signs by checking a known
  stable solution (the pendulum test: does the equilibrium attract or repel?)
- [ ] **Overcounting check** — are you counting the same thing twice under
  different names?
- [ ] **Circular reasoning check** — trace every input back to its source.
  Does G appear on both sides? Does the result depend on what it is trying to prove?
- [ ] **Order-of-magnitude check** — is the number in the right ballpark?
  If off by more than 10×, a fundamental assumption is wrong.

---

### 4. Use Analogies

- [ ] **Find the analogue in another field** — what well-understood system
  behaves the same way? (superconductor, rip current, optical polariser, etc.)
- [ ] **Map phenomena to a catalog** — list all known phenomena in the analogous
  system and check which ones have PDTP counterparts
- [ ] **Use the analogy to predict** — what does the analogous system predict
  that you have not yet derived? Derive it.
- [ ] **Check where the analogy breaks** — every analogy fails somewhere.
  Finding where it breaks is itself a result.

---

### 5. Handle Negative Results Properly

- [ ] **Document what fails, not just that it fails** — record the exact
  contradiction and what assumption it traces back to
- [ ] **Find the correction factor** — if all tests fail by the same ratio,
  that ratio is the clue (see: hierarchy problem as G correction factor)
- [ ] **Find the sub-group** — which subset of tests fails? What physical
  assumption do they share? That assumption is wrong.
- [ ] **Declare exhaustion explicitly** — state "all perturbative paths tried,
  moving to non-perturbative" rather than circling back
- [ ] **Reframe the negative result as a positive finding** — "we cannot derive
  G algebraically" = "G is to PDTP as Λ is to GR — a free parameter"

---

### 6. Mathematical Strategies

- [ ] **Work backwards** — assume the desired result and derive what inputs
  it requires. Are those inputs physically reasonable?
- [ ] **Proof by contradiction** — assume the opposite of what you want to prove.
  Derive a contradiction. Conclude the original claim.
- [ ] **Find invariants** — what quantity is conserved or unchanged under the
  relevant transformation? Build around it.
- [ ] **Change coordinates or basis** — the problem may be trivial in a different
  frame (momentum space, eigenbasis, polar coordinates, etc.)
- [ ] **Symmetry argument** — what is the most general expression consistent
  with all the symmetries? Write that down first.
- [ ] **Topological argument** — is the result protected by topology (winding
  number, Chern class, index)? If so, it is exact and perturbation-independent.
- [ ] **Perturbation theory** — if the exact answer is inaccessible, expand in
  a small parameter. Check at each order.
- [ ] **Dimensional transmutation** — can a dimensionless coupling generate
  a mass scale non-perturbatively? (Coleman-Weinberg mechanism)

---

### 7. When Completely Stuck

- [ ] **List every assumption and question each one** — which assumptions have
  you verified? Which are inherited from elsewhere without checking?
- [ ] **Ask: what would have to be true for this to work?** — then check
  whether that thing is true
- [ ] **Ask: what would falsify this?** — if nothing would falsify it, the
  claim is not physics, it is philosophy
- [ ] **Look for the free parameter** — every framework has something it cannot
  fix internally. Identify it explicitly rather than hiding it.
- [ ] **Change the question** — sometimes the question is malformed.
  "What is K?" may be unanswerable; "what does K predict?" may not be.
- [ ] **Find the simplest system that has the same problem** — solve that first.
- [ ] **Sleep on it / return with fresh eyes** — not a joke. Pattern recognition
  works differently after a break.

---

## Quick Reference Summary

| Strategy | One-line description | Historical example |
|---|---|---|
| Scaffolding term | Add a term to fix inconsistency; test it | Maxwell displacement current |
| Forced consequence | Apply constraints; accept surprising outputs | Dirac antiparticles |
| Postulate + derive | State clearly; derive all consequences | Einstein equivalence principle |
| Order parameter | Write general field from symmetry; fill in microscopy later | Landau GL theory |
| Numerical scaffold | Discretise; compute; take continuum limit | Wilson lattice QCD |
| Sudoku check | Substitute into 10+ equations; score ratios | PDTP internal tool |
| Analogy catalog | Map all phenomena from analogous field | PDTP wave catalog (Part 28c) |
| Negative = finding | Failure pinpoints the broken assumption | Part 29 circularity |
| Symmetry generalise | U(1) → SU(3); allow the algebra to speak | Part 37 SU(3) extension |
| Topological derivation | Winding number fixes what algebra cannot | Part 33 vortex winding |
