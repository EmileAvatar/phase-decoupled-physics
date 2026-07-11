# Methodology (Math) — How Mathematicians Solve Problems

**Type:** General reference / grounding document (not PDTP-specific).
**Companion to:** `Methodology.md` (PDTP's own condensed, practical checklist) and
`Methodology_Science.md` (the scientific-method counterpart to this document).
**Purpose:** `Methodology.md` already uses real mathematical problem-solving
techniques (proof by contradiction, working backwards, invariants, symmetry
arguments) without always naming or citing their source. This document collects
the established, citable methodology those techniques come from, so PDTP work can
point to a real framework instead of reinventing one. Nothing in this document is
PDTP-specific — no Sudoku checks, no SymPy verification, no equation tags apply
here. It is background reading.

---

## Table of Contents

1. [Pólya's Four-Phase Framework](#1-pólyas-four-phase-framework)
2. [Core Proof Techniques](#2-core-proof-techniques)
3. [Heuristics for Discovery](#3-heuristics-for-discovery)
4. [Lakatos: Proofs and Refutations](#4-lakatos-proofs-and-refutations)
5. [Quick Reference Summary](#5-quick-reference-summary)
6. [References](#6-references)

---

## 1. Pólya's Four-Phase Framework

**Source:** Pólya, G. (1945), *How to Solve It*, Princeton University Press.

The canonical reference for mathematical problem-solving methodology. Pólya breaks
problem-solving into four phases, each with its own guiding questions:

**Phase 1 — Understand the problem.**
What is the unknown? What are the data? What is the condition? Is it possible to
satisfy the condition? Draw a figure. Introduce suitable notation.

**Phase 2 — Devise a plan.**
Have you seen this problem before, or one like it? Do you know a related problem?
Look at the unknown and try to think of a familiar problem with the same or a
similar unknown. Can you restate the problem? Can you solve a part of the problem?

**Phase 3 — Carry out the plan.**
Check each step. Can you see clearly that each step is correct? Can you prove it?

**Phase 4 — Look back.**
Can you check the result? Can you check the argument? Can you derive the result
differently? Can you use the result, or the method, for some other problem?

**Why this matters for PDTP:** `Methodology.md`'s entire problem-solving checklist
is effectively an expanded, physics-flavored version of Pólya's Phase 2 ("devise a
plan") — reframe the problem, introduce something new, use analogies, try
mathematical strategies. Phase 4 ("look back") maps directly onto the Sudoku
consistency check: after deriving a result, test it against everything else known
and see whether the method generalizes.

---

## 2. Core Proof Techniques

Standard techniques from mathematical logic and proof theory. Every mathematician's
basic toolkit; listed here so PDTP work can name the technique it is using rather
than describing it from scratch each time.

**Direct proof.** Start from premises, apply valid inference steps, arrive at the
conclusion. The default when it works.

**Proof by contradiction (reductio ad absurdum).** Assume the negation of what you
want to prove; derive a logical contradiction; conclude the original statement must
be true. **Source:** classical logic, formalized in Aristotle's *Organon*; used
throughout modern mathematics (e.g. the irrationality of √2).

**Proof by contrapositive.** To prove "if P then Q," prove the logically equivalent
"if not Q then not P." Useful when the direct implication is hard to establish but
its contrapositive is easier to reason about.

**Proof by induction.** Establish a base case, then show that truth at step n
implies truth at step n+1 (or, in strong induction, that truth for all steps up to
n implies truth at n+1). The standard tool for statements indexed by the natural
numbers. **Source:** formalized by Peano's axioms (1889).

**Proof by construction.** Prove existence by explicitly building the object in
question. Stronger than a non-constructive existence proof because it also gives
you the object.

**Proof by exhaustion.** Break the problem into a finite number of cases and verify
each one. Valid but often seen as inelegant; sometimes unavoidable (e.g. the Four
Color Theorem, Appel & Haken 1976, required computer-assisted case-checking of
1,936 configurations).

**Pigeonhole principle.** If n items are placed into fewer than n containers, at
least one container holds more than one item. A simple counting argument that
proves existence without construction — widely underused because it looks too
simple to be powerful.

**Extremal principle.** Among all objects satisfying some condition, consider the
one that maximizes or minimizes some quantity. Properties of the extremal object
often force the general result. A workhorse technique in combinatorics and
optimization.

**Non-constructive vs. constructive proofs.** A non-constructive proof shows
something must exist (often via contradiction or a counting argument) without
producing it; a constructive proof builds it. The distinction matters practically:
a non-constructive existence proof tells you a solution exists but not how to find
one.

---

## 3. Heuristics for Discovery

These are not proof techniques but strategies for *finding* the right approach —
the "devise a plan" phase in practice. PDTP's `Methodology.md` Section 6
("Mathematical Strategies") is a condensed, physics-flavored version of several of
these; this section is the fuller, general-purpose form they are drawn from.

- **Specialization.** Try the smallest, simplest non-trivial case. Solve that
  first; the general pattern often becomes visible.
- **Generalization.** Once a specific case is solved, ask whether the same argument
  works for a broader class of objects. Generalizing sometimes makes a problem
  *easier* by revealing which details were actually load-bearing.
- **Analogy.** Map the problem onto a structurally similar, better-understood
  problem. Pólya devotes a large part of *How to Solve It* to this move.
- **Working backwards.** Start from the desired conclusion and ask what would have
  to be true immediately before it, then work backward step by step to something
  already known.
- **Auxiliary constructions.** Introduce a new object (a line, a variable, a
  function) not present in the original problem statement, purely because it makes
  the structure visible. Common in Euclidean geometry proofs (auxiliary lines) and
  algebra (substitutions).
- **Symmetry.** If the problem has a symmetry, the answer usually respects it. Use
  symmetry to rule out asymmetric solutions before searching, or to reduce the
  search space.
- **Invariants.** Find a quantity that stays fixed under the allowed operations.
  Invariants are one of the most powerful tools for proving something is
  *impossible* (if the invariant differs between the start and target states, no
  sequence of allowed moves can connect them).

---

## 4. Lakatos: Proofs and Refutations

**Source:** Lakatos, I. (1976), *Proofs and Refutations: The Logic of Mathematical
Discovery*, Cambridge University Press.

Lakatos studied how mathematical concepts and theorems actually evolve historically
(using Euler's polyhedron formula V − E + F = 2 as his central case study), and
found that they rarely spring into existence fully correct. Instead:

1. A conjecture is proposed with an informal proof.
2. A counterexample ("monster") is found that the proof doesn't handle.
3. Mathematicians respond in one of several ways:
   - **Monster-barring** — redefine terms to exclude the counterexample (e.g.
     restrict "polyhedron" to exclude the pathological case).
   - **Monster-adjusting** — reinterpret the counterexample so it actually
     confirms a modified version of the theorem.
   - **Exception-barring** — accept the theorem only for a restricted domain that
     excludes the counterexample.
   - **Proof-and-refutation, properly** — use the counterexample to locate exactly
     which step ("lemma") in the proof is false, then repair that step, refining
     both the theorem's statement and its proof simultaneously.
4. The theorem and its proof co-evolve through this process until they stabilize.

**Why this matters for PDTP:** this is a direct, citable grounding for the
project's own stated practice that "contradictions are the finding, not a
failure" and that negative results should be documented, not discarded. A Sudoku
check that fails is a Lakatosian counterexample — it tells you exactly which
assumption ("lemma") in the derivation needs repair, not merely that the whole
result is wrong. The project's Part 29 circularity result and the Part 30a
hierarchy-problem correction factor are both examples of proof-and-refutation in
Lakatos's sense: the counterexample (G cannot be derived; the correction factor is
off by (m_e/m_P)²) pinpointed exactly where the assumption broke.

---

## 5. Quick Reference Summary

| Technique | One-line description | Source |
|---|---|---|
| Pólya 4 phases | Understand → plan → execute → look back | Pólya 1945 |
| Direct proof | Premises → valid steps → conclusion | Classical logic |
| Contradiction | Assume the negation; derive absurdity | Aristotle's *Organon* |
| Contrapositive | Prove "not Q ⇒ not P" instead of "P ⇒ Q" | Classical logic |
| Induction | Base case + step n ⇒ step n+1 | Peano axioms, 1889 |
| Construction | Prove existence by building the object | — |
| Exhaustion | Finite case-check covers all possibilities | Four Color Theorem, 1976 |
| Pigeonhole | n items, fewer than n boxes ⇒ a collision | Dirichlet |
| Extremal principle | Consider the max/min object; its properties force the result | — |
| Specialization | Solve the simplest case first | Pólya |
| Generalization | Broaden the case; find what was load-bearing | Pólya |
| Working backwards | Start from the goal; find what precedes it | Pólya |
| Invariants | Find a fixed quantity; use it to prove impossibility | — |
| Proof-and-refutation | Counterexample locates the false lemma, not just "wrong" | Lakatos 1976 |

---

## 6. References

1. Pólya, G. (1945), *How to Solve It: A New Aspect of Mathematical Method*,
   Princeton University Press.
2. Lakatos, I. (1976), *Proofs and Refutations: The Logic of Mathematical
   Discovery*, Cambridge University Press.
3. Peano, G. (1889), *Arithmetices principia, nova methodo exposita* (Peano
   axioms).
4. Appel, K. & Haken, W. (1976), "Every Planar Map is Four Colorable,"
   *Illinois Journal of Mathematics*, 21, 429–567.
5. [Mathematical proof — Wikipedia](https://en.wikipedia.org/wiki/Mathematical_proof)
6. [Pólya's How to Solve It — Wikipedia](https://en.wikipedia.org/wiki/How_to_Solve_It)
7. [Proofs and Refutations — Wikipedia](https://en.wikipedia.org/wiki/Proofs_and_Refutations)

---

*Compiled 2026-07-11. See also `Methodology.md` (PDTP's practical checklist,
which draws on several of these techniques) and `Methodology_Science.md` (the
scientific-method counterpart).*
