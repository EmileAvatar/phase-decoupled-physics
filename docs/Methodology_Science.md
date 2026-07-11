# Methodology (Science) — How Scientists Solve Problems

**Type:** General reference / grounding document (not PDTP-specific).
**Companion to:** `Methodology.md` (PDTP's own condensed, practical checklist) and
`Methodology_Math.md` (the mathematical-methodology counterpart to this document).
**Purpose:** `Methodology.md` already uses real scientific-method concepts — most
directly, Section 7's "what would falsify this? — if nothing would, the claim is
not physics, it is philosophy," which is Popper's falsifiability criterion, stated
without naming it. This document collects the established, citable methodology
those ideas come from. Nothing here is PDTP-specific — no Sudoku checks, no SymPy
verification, no equation tags apply. It is background reading, and also the
lens used when evaluating outside claims (see the review of an external paper
that prompted this document's creation, 2026-07-11).

---

## Table of Contents

1. [The Scientific Method Cycle](#1-the-scientific-method-cycle)
2. [Falsifiability (Popper)](#2-falsifiability-popper)
3. [Paradigms and Normal vs. Revolutionary Science (Kuhn)](#3-paradigms-and-normal-vs-revolutionary-science-kuhn)
4. [Occam's Razor](#4-occams-razor)
5. [Feynman: Cargo Cult Science](#5-feynman-cargo-cult-science)
6. [Model-Building Methodology](#6-model-building-methodology)
7. [Quick Reference Summary](#7-quick-reference-summary)
8. [References](#8-references)

---

## 1. The Scientific Method Cycle

The standard modern synthesis of scientific method, as actually practiced (not the
oversimplified single-line-diagram version taught in school):

1. **Observation.** Notice a phenomenon, a gap, or an anomaly relative to current
   understanding.
2. **Hypothesis.** Propose a testable explanation — a mechanism, not just a
   description.
3. **Prediction.** Derive specific, quantitative consequences the hypothesis
   implies, ideally ones that distinguish it from competing explanations.
4. **Test / experiment.** Attempt to observe those consequences under controlled
   conditions.
5. **Analysis.** Compare prediction to result. Does it match, within stated
   uncertainty?
6. **Revision or acceptance.** If it fails, revise the hypothesis (or discard it)
   and document *how* it failed, not just *that* it failed. If it succeeds,
   the hypothesis survives — provisionally, never proven, only not-yet-falsified.
7. **Replication and peer review.** Independent groups attempt to reproduce the
   result before it is treated as established. This step is social/institutional,
   not logical, but it is where most bad results actually get caught.

**Source:** this is a composite of the Baconian empirical tradition (Francis
Bacon, *Novum Organum*, 1620) and the hypothetico-deductive model formalized in
20th-century philosophy of science (see Popper, below). No single canonical
citation exists because the method evolved over centuries; see
[Scientific method — Wikipedia](https://en.wikipedia.org/wiki/Scientific_method)
for the full historical development.

**Why this matters for PDTP:** the project's own stated Goal 1 milestones
("reproduce known GR predictions," "identify predictions that differ from GR,"
"provide specific testable numbers") are steps 2–3 of this cycle. Step 7
(replication/peer review) is the step PDTP has *not* yet passed through — worth
being explicit about that, rather than treating internal Sudoku consistency as a
substitute for external replication. They check different things: Sudoku checks
internal consistency; peer review and experiment check correspondence to reality.

---

## 2. Falsifiability (Popper)

**Source:** Popper, K. (1959), *The Logic of Scientific Discovery* (English
translation of *Logik der Forschung*, 1934), Hutchinson & Co.

Popper's demarcation criterion: a theory is scientific only if it makes
predictions that could, in principle, be shown false by some possible observation.
A theory compatible with *every* conceivable outcome explains nothing — it has no
empirical content. Popper contrasted physics (which forbids certain outcomes and
is refutable) with theories he considered pseudoscientific *not* because they were
wrong, but because they could absorb any result and claim consistency regardless.

Key consequences of this view:
- Theories are never *proven* true by evidence — they are corroborated (survived
  attempts to falsify them) or falsified. Confirmation is weaker than most
  intuition suggests; a thousand consistent observations don't prove a theory,
  one clean counterexample can kill it.
- A good theory is a *risky* one — it forbids more, and is therefore easier to
  falsify, than a vague one. Risk is a virtue, not a liability.
- "Unfalsifiable" is not automatically "wrong" — it means "not currently doing the
  job a scientific theory needs to do." An unfalsifiable claim can still be true;
  it just isn't testable science until it's sharpened into a falsifiable form.

**Why this matters for PDTP:** this is the direct citation for `Methodology.md`
Section 7's checklist item. It's also the standard the project's own
`falsifiable_predictions.md` document is explicitly organized around — every entry
there is required to state a test method and an expected value, i.e. a way it
could fail. It is also the sharpest tool for evaluating outside claims: a theory
that "explains" any experimental result after the fact, or that treats critics'
objections as evidence of bias rather than engaging them technically, is behaving
in the way Popper flagged as the hallmark of non-science — independent of whether
its author is right or wrong on the physics.

---

## 3. Paradigms and Normal vs. Revolutionary Science (Kuhn)

**Source:** Kuhn, T. (1962), *The Structure of Scientific Revolutions*, University
of Chicago Press.

Kuhn argued that science does not progress by smooth accumulation of facts.
Instead:

- **Normal science** operates within a "paradigm" — a shared framework of theory,
  method, and standard problems ("puzzles") the community agrees are worth
  solving and knows how to evaluate. Most scientific work is normal science:
  solving puzzles within an accepted framework, not questioning the framework
  itself.
- **Anomalies** accumulate — results the paradigm cannot easily explain. Most are
  initially set aside or patched over, not treated as immediately fatal (this is
  rational, not a failure of science — most anomalies turn out to be errors or
  minor corrections, not paradigm-breakers).
- **Crisis** occurs when anomalies accumulate past a threshold and confidence in
  the paradigm erodes.
- **Revolution** — a new paradigm is proposed that resolves the anomalies (often
  by reframing what counts as a legitimate question, not just by adding an
  equation). The transition is not purely logical; Kuhn described paradigms as
  partially "incommensurable" — the new framework can reinterpret old data in ways
  the old framework's practitioners initially find hard to even parse.

**Why this matters for PDTP:** two-sided relevance, both worth holding at once.
(a) Extraordinary, paradigm-challenging claims correctly face high scrutiny and
slow acceptance — this is normal, healthy science, not "establishment bias," and
framing legitimate technical pushback as bias (a pattern the paper reviewed
2026-07-11 exhibited explicitly) is itself a red flag, not a sign of being
ahead of one's time. (b) At the same time, Kuhn's framework is also a caution
against dismissing new approaches purely because they're unfamiliar — the
question is always whether the specific technical claims hold up, not whether the
framework is mainstream. The discipline is in applying the *same* standard of
scrutiny to PDTP's own claims that would be applied to anyone else's.

---

## 4. Occam's Razor

**Source:** attributed to William of Ockham (14th century); modern formulation via
the principle of parsimony in statistics and model selection (e.g. the Akaike
Information Criterion, Akaike 1974, which formalizes a mathematical trade-off
between fit quality and model complexity).

Among competing explanations that fit the evidence equally well, prefer the one
with fewer assumptions / free parameters / new entities. Not a claim that
simpler theories are automatically *true* — nature is not obligated to be simple —
but a methodological default: extra unmotivated machinery needs to earn its place
by explaining something the simpler version cannot.

**Why this matters for PDTP:** this is the standard PDTP's own coding rules
already apply informally — "don't add abstractions beyond what the task requires"
— extended to physics content: every free parameter or new postulate should be
explicitly flagged (as the project's own Sudoku/tagging system already requires),
and its necessity should be demonstrable, not assumed. It's also the standard by
which the paper reviewed 2026-07-11 fell short in the opposite direction — needed
angles were picked *after the fact* to match target numbers, which is the reverse
of parsimony: complexity (an unmotivated specific angle) introduced solely to fit
a known answer.

---

## 5. Feynman: Cargo Cult Science

**Source:** Feynman, R. (1974), Caltech commencement address, published as
"Cargo Cult Science" in *Surely You're Joking, Mr. Feynman!* (1985) and
separately in *Engineering and Science* magazine.

Feynman's central claim: "The first principle is that you must not fool
yourself — and you are the easiest person to fool." He describes "cargo cult
science" as work that has all the *superficial* trappings of real science —
following procedures, publishing results, using technical language — while
missing the substance: rigorous self-checking, honest reporting of everything
that *doesn't* work (not just what does), and genuine vulnerability to being
proven wrong.

Specific practices Feynman called out:
- Report all the data, including results that complicate or contradict your own
  hypothesis — not a filtered subset.
- Detail everything that could invalidate your result, even (especially) things a
  reader might not think to ask about.
- Be your own harshest critic before anyone else has the chance to be.

**Why this matters for PDTP:** this is the direct grounding for the project's
own "RECHECK" protocol — the explicit rule that a function returning a hardcoded
value matching the expected answer "is a lie to the reader," and that reviewers
"will look for exactly this failure mode." That rule is Feynman's cargo-cult
warning applied specifically to code. The broader lesson generalizes: honest
science requires actively hunting for the ways you might be fooling yourself, not
just presenting results that survived whatever checks you happened to think of.

---

## 6. Model-Building Methodology

Physics rarely works with the "true" theory directly — it works with models valid
in some regime, and treats that limitation as a feature, not a defect.

- **Effective field theory.** A theory need not be valid at all energy scales to
  be useful or correct within its domain. Newtonian gravity is not "wrong" — it's
  the correct effective theory in the weak-field, low-velocity limit of GR.
  Knowing a theory's domain of validity is as important as the theory itself.
- **Toy models.** Deliberately simplified systems (1D, 2-particle, single
  symmetry) used to isolate one mechanism at a time before tackling the full
  problem. A toy model that fails to reproduce a known result cheaply reveals
  a wrong assumption before expensive machinery is built on top of it.
- **Scale separation.** Identify the natural length/time/energy scale of the
  problem and work at that scale; physics at very different scales is often
  effectively decoupled (renormalization group intuition), which is why particle
  physics can proceed without solving quantum gravity first.
- **"All models are wrong, some are useful."** — George Box (1976). No model is a
  perfect map of reality; the operative question is always whether a model is
  useful for the questions being asked of it, not whether it's metaphysically
  "true."

**Why this matters for PDTP:** the project's own explicit acknowledgment that
G and Λ are free parameters (not derived) is a model-scope statement in this
sense — PDTP is not claimed to be a final theory, but an effective framework whose
domain of validity and open parameters are stated honestly, which is exactly the
standard this section describes.

---

## 7. Quick Reference Summary

| Concept | One-line description | Source |
|---|---|---|
| Scientific method cycle | Observe → hypothesize → predict → test → revise → replicate | Composite, Bacon/20th c. |
| Falsifiability | A theory must forbid some possible outcome to be scientific | Popper 1959 |
| Normal vs. revolutionary science | Puzzle-solving within a paradigm vs. paradigm change after crisis | Kuhn 1962 |
| Occam's Razor | Prefer fewer assumptions among equally-fitting explanations | Ockham; Akaike 1974 |
| Cargo cult science | Don't fool yourself; report everything that could be wrong | Feynman 1974 |
| Effective field theory | A model can be correct within a domain without being universal | Standard QFT practice |
| Toy models | Isolate one mechanism cheaply before building the full system | Standard physics practice |
| "All models are wrong, some are useful" | Usefulness, not metaphysical truth, is the operative test | Box 1976 |

---

## 8. References

1. Bacon, F. (1620), *Novum Organum*.
2. Popper, K. (1959), *The Logic of Scientific Discovery*, Hutchinson & Co.
   (English translation of *Logik der Forschung*, 1934).
3. Kuhn, T. (1962), *The Structure of Scientific Revolutions*, University of
   Chicago Press.
4. Akaike, H. (1974), "A new look at the statistical model identification,"
   *IEEE Transactions on Automatic Control*, 19(6), 716–723.
5. Feynman, R. (1974), "Cargo Cult Science," Caltech commencement address;
   reprinted in *Surely You're Joking, Mr. Feynman!* (1985).
6. Box, G. E. P. (1976), "Science and Statistics," *Journal of the American
   Statistical Association*, 71(356), 791–799.
7. [Scientific method — Wikipedia](https://en.wikipedia.org/wiki/Scientific_method)
8. [Falsifiability — Wikipedia](https://en.wikipedia.org/wiki/Falsifiability)
9. [The Structure of Scientific Revolutions — Wikipedia](https://en.wikipedia.org/wiki/The_Structure_of_Scientific_Revolutions)
10. [Occam's razor — Wikipedia](https://en.wikipedia.org/wiki/Occam%27s_razor)
11. [Cargo cult science — Wikipedia](https://en.wikipedia.org/wiki/Cargo_cult_science)

---

*Compiled 2026-07-11. See also `Methodology.md` (PDTP's practical checklist,
which draws on several of these concepts) and `Methodology_Math.md` (the
mathematical-methodology counterpart).*
