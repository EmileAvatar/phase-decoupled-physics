# PDTP — Phase-Decoupled Transport Physics

## Project Summary
Speculative physics framework: gravity as emergent phase-locking between
matter-waves and spacetime-waves. Not experimentally validated.

## Repository Structure
- `docs/core_concepts/` — Framework overview, particle reframing
- `docs/technical/` — Glossary, Einstein comparison, term mappings
- `docs/research/` — Math status, formalization, quantum gravity, mysteries
- `docs/applications/` — Interpretive applications
- `simulations/` — Python emulator
- `assets/images/` — Diagrams (SVG, GIF)
- `Elastic_Universe/` — SEPARATE: External elastic-universe.org review (speculative, not PDTP)
- `TODO_04.md` — Active roadmap (tan investigation, Parts 84-120+)
- `TODO_05.md` — Active roadmap (Lambda-locking deep dive + multi-medium framework, 2026-07-04+)
- `TODO_03.md` — Previous roadmap (Parts 77–96+, archive)
- `TODO_02.md` — Previous roadmap (Parts 42–76, archive)
- `TODO_Summary.md` — Completed work at a glance (< 200 lines)
- `TODO_01.md` — Full archive (Parts 1–41, do not edit)
- `CODING_STANDARDS.md` — Math rigor, coding standards, separation of concerns

## Key Equations

### U(1) Lagrangian — current form (gravitational condensate)
- Lagrangian: L = ½(∂μφ)(∂^μφ) + Σᵢ ½(∂μψᵢ)(∂^μψᵢ) + Σᵢ gᵢ cos(ψᵢ − φ)
- Field equation: □φ = Σᵢ gᵢ sin(ψᵢ − φ)
- Coupling: α = cos(ψ − φ), where α=1 is normal gravity, α→0 is decoupled
- φ ∈ ℝ (single phase angle; U(1) symmetry)

### Two-Phase Lagrangian — Part 61 (TESTED: 16/16 PASS, Part 63)
**PDTP Original.** Adding surface tension (-cos) alongside gravity (+cos):
- Lagrangian: L = +g cos(ψ − φ_b) − g cos(ψ − φ_s)
- φ_b = bulk phase (+cos, gravity); φ_s = surface phase (−cos, surface tension)
- Change of variables: φ_+ = (φ_b + φ_s)/2 (gravity mode); φ_- = (φ_b − φ_s)/2 (surface mode)
- Product coupling: cos(ψ−φ_b) − cos(ψ−φ_s) = 2 sin(ψ−φ_+) sin(φ_-)
- Newton's 3rd law DERIVED: ψ̈ = −2φ̈_+ (exact; factor 2 consistent with G_eff = 2G_bare)
- Jeans instability: eigenvalue +2√2 g > 0 (gravitational collapse from Lagrangian) [DERIVED]
- Biharmonic gravity: ∇⁴Φ + 4g²Φ = source (4th order, not Poisson) [DERIVED]
- phi_- = reversed Higgs: massless in vacuum, massive near matter (m² = 2gΦ) [DERIVED]
- **STATUS: 16/16 re-derivation tests PASS (Part 63). All single-phase results reproduced.
  Key mechanism: χ = φ_+ + π/2 maps two-phase to single-phase exactly.
  Correction: Newton's 3rd law factor is 2, not 1 (psi_ddot = -2*phi_+_ddot).**
- Induced EDE quartic: λ₄ = 2g²sin²(β)/(3k̄²) > 0 at partial lock (ψ−φ₊ = π/2−β);
  EFFECTIVE term from the SAME Lagrangian (no new fundamental term); vanishes
  identically at β=0 → transient Early Dark Energy, w=−1 today automatic [DERIVED, Part 117]
- DM winding selection: n=1 (vortex stability + Kibble-Zurek) → m_DM = m_P
  ("Planck vortex relic"); kill test = CMB tensor modes (LiteBIRD/CMB-S4) [DERIVED, Part 116]
- DM self-interaction: σ/m = 4πG²m_DM/v⁴ (Part 118 erratum — NOT G/c⁴ as Part 89 had)
- Research: Part 61 `two_phase_lagrangian.py`; Part 62 `reversed_higgs.py`; Part 63 `two_phase_rederivation.py`;
  Part 116 `dm_winding_selection.py`; Part 117 `phi_minus_quartic.py`; Part 118 `sigma_m_erratum.py`

### SU(3) Extension — Part 37 (QCD condensate; in development)
**PDTP Original.** Replacing φ with a 3×3 SU(3) matrix field U(x) generalises the
Lagrangian to produce Z₃ fractional vortices (quarks) and 8 gluons:
- Lagrangian: L = K Tr[(∂μU†)(∂^μU)] + Σᵢ Kᵢ Tr[(∂μΨᵢ†)(∂^μΨᵢ)] + Σᵢ gᵢ Re[Tr(Ψᵢ†U)] / 3
- U(x) ∈ SU(3) — spacetime condensate field (3×3 unitary, det=1)
- Ψᵢ(x) ∈ SU(3) — matter field for particle i
- The coupling Re[Tr(Ψ†U)]/N is the Wilson loop action (Wilson 1974)
- U(1) limit: Re[Tr(Ψ†U)]/1 = cos(ψ−φ) — recovers the U(1) Lagrangian exactly
- 8 gluons from N²−1 = 8 SU(3) generators; Z₃ vortices (winding 1/3) = quarks
- κ_GL = √2 (Type II) for any m_cond — Abrikosov flux tubes form in both condensates
- String tension: σ_SU(3) = (4/3)×σ_U(1) [Casimir factor; Part 37]; full value needs lattice (Part 38)
- Research: `docs/research/su3_condensate_extension.md`; simulation: `simulations/solver/su3_condensate.py`

## Coding Standards & Mathematical Rigor

**Full standards:** See `CODING_STANDARDS.md` in the repo root.

Key rules (enforced in all Python scripts and research docs):
- Every established formula MUST cite its source (Wikipedia or paper)
- New/original results MUST be marked: **PDTP Original**
- All derivations must be step-by-step, not hand-waved
- Sign conventions must be verified (the +cos coupling is required for stability)
- Numerical predictions must include units and order-of-magnitude estimates
- Every equation must be tagged: `[ASSUMED]`, `[DERIVED]`, `[VERIFIED]`, or `[SPECULATIVE]`
- Python scripts output DATA only — no physical interpretation in code
- All interpretation belongs in `.md` research docs, clearly marked `[SPECULATIVE]` where needed
- SymPy verification must re-derive independently (not just confirm stored results)
- Separate derivation (`derive_*`), verification (`verify_*`), and computation (`compute_*`) functions

### ABSOLUTE REQUIREMENT: Show Your Work in Research Docs
**Every research `.md` file MUST show the complete derivation for every result.**
This is non-negotiable. Mathematicians and physicists will demand it.

For every scorecard item, test, or claimed result, the `.md` file must contain:
1. **Starting point** — what is assumed, with source citation and equation tag
2. **Every intermediate step** — every substitution, every simplification, every
   trig identity, written out as numbered equations. No skipping steps.
3. **SymPy verification** — state what was checked and the residual (e.g., "residual = 0")
4. **Numerical values** — where applicable, show the computed number with units
5. **Result** — final equation with `[DERIVED]` / `[VERIFIED]` / `[ASSUMED]` tag
6. **Independence argument** — if the result must hold under a new extension
   (e.g., two-phase), explain WHY it still holds, not just THAT it holds

The Python script is NOT the documentation. The `.md` file must be **self-contained**:
a reader who never opens the `.py` file must be able to follow every step of every
derivation. The script comments can and should be mirrored in the research doc.

### Plain English Explanations
Every research doc and results section MUST include a **plain English explanation**
of the key findings. The user is not a math person — technical results need to be
translated into intuitive language. This applies to:
- Each major result or equation (what does it MEAN physically?)
- Technical terms on first use (what IS a Casimir factor? a heat kernel?)
- Why a result matters (so what? what does this tell us?)
- Negative results (what did we learn from the failure?)
Even a single-line summary like "This means gravity is 2.4x too strong with only
gluons" counts. The goal: someone who skips all the math can still understand the
findings by reading only the plain English sections.

### Sudoku Consistency Check
Apply whenever a new equation, variable, or value is introduced to the framework:

1. **Assume** the new value/equation is correct
2. **Substitute** it into 10+ known, established physics equations (use the
   full test suite in `simulations/sudoku_consistency_check.py` as a template)
3. **Standard Model compatibility check:** verify the new prediction is compatible
   with the Standard Model Lagrangian — particles, fields, Higgs mechanism,
   gauge symmetries SU(3)xSU(2)xU(1). PDTP must EXPLAIN the SM, not contradict it.
   Check: does it break gauge invariance? Does it give wrong particle masses?
   Does it conflict with known Higgs phenomenology? Does it violate conservation laws?
4. **Two-phase Lagrangian check:** verify the result is consistent with the
   two-phase system (Part 61). New results must be tested with BOTH single-phase
   (+cos only) AND two-phase (+cos/-cos) Lagrangians. Specifically check:
   - Does it still hold when phi_- is present?
   - Does the biharmonic field equation (nabla^4 + 4g^2) reduce correctly?
   - Is Newton's 3rd law (psi_ddot = -phi_+_ddot) preserved?
   - Does the Jeans instability eigenvalue remain positive?
   Previous single-phase results (Newton's laws, GR recovery, Hawking, PPN, etc.)
   must ALL be re-derived in the two-phase framework to confirm compatibility.
5. **Newton's laws check:** verify ALL Newton's laws are derivable (not assumed):
   - 1st law (inertia): free particle maintains phase → constant velocity
   - 2nd law (F=ma): phase-gradient force = coupling × phase mismatch
   - 3rd law: psi_ddot = -phi_+_ddot (DERIVED in Part 61 from Lagrangian symmetry)
6. **Score** each result: ratio ≈ 1.00 (within 1%) = MATCH; anything else = contradiction
7. **Explain** every contradiction — it must be accounted for or the value is rejected
8. **Report** the scorecard: `N matches, M contradictions out of T tests`

The contradictions are the finding, not a failure. They tell you WHERE the
assumption breaks down, not just THAT it does — like a wrong number in Sudoku
creating cascading conflicts that pinpoint the error.

**What to do with results:**
- All pass → value is internally consistent (may still be circular — note this)
- All fail → value is wrong; identify the correction factor
- Some pass, some fail → identify which sub-group of equations contradicts it
  and what physical assumption they share

**Reference implementation:** `simulations/sudoku_consistency_check.py`

**Example (Part 30a):** K = ℏ/(4πc) with a = electron Compton wavelength → 0/10
passes; correction factor = (m_e/m_Planck)² exactly → the failure IS the
hierarchy problem, not a calculation error.

## Equation Reference
All PDTP equations with status tags in one place:
`docs/research/equation_reference.md`
**Update that file whenever a new equation is derived or status changes.**

## Term and Symbol Glossary
Every symbol, variable, and named concept used in PDTP in one place:
`docs/technical/term_glossary.md`
**Update that file whenever a new symbol or named mechanism is introduced to the framework.**
Companion to `docs/technical/glossary.md` (plain-English concepts) and
`docs/research/equation_reference.md` (equations with status tags).

## Citation Format
```
**Source:** [Title](URL)
**Source:** Author (Year), "Paper title"
**PDTP Original:** Description of new result
```

## External AI Reviews (ChatGPT, DeepSeek, etc.)
When the user shares output from ChatGPT, DeepSeek, or other LLMs:
- **They have VERY LIMITED scope on PDTP.** They only see what the user pasted
  into them. They do NOT have access to our full project history, TODO files,
  past Parts, negative results, or proven theorems.
- **Do NOT judge their output against our full project knowledge.** Evaluate
  what they say on its own merits given the limited context they received.
- **The user's PROMPTS to the external AI are the user's ideas** — not the
  AI's claims about PDTP. Distinguish user hypotheses (4a, 4b, 4c, 4d etc.)
  from the AI's analysis of those hypotheses.
- **Look for useful insights** that survive scrutiny, not just errors.
- **When cross-checking:** note which of our results the external AI could not
  have known about, rather than treating ignorance as error.

## Project Goals (in order)

### Goal 1 — Confirm gravity as emergent phase-locking (CURRENT)
Prove (with falsifiable, testable predictions) that gravity is emergent
phase-locking between matter-waves and spacetime-waves. This is the
foundation — without confirming this, nothing else follows.

Key milestones:
- Reproduce all standard GR predictions from the phase-locking Lagrangian
- Identify predictions that DIFFER from GR (breathing mode, birefringence)
- Provide specific numbers that experimentalists can test or rule out
- See `docs/research/falsifiable_predictions.md` for the full list

### Long-Term Scientific Goals
Determine whether the phase-locking Lagrangian can produce:
- Effective spacetime geometry from condensate dynamics
- Particle-like wave solutions (solitons, vortices, stable localized modes)
- Long-range attractive forces (1/r^2 law from phase coupling)
- Emergent gravitational behavior (Newtonian limit, GR corrections)

Ultimate objective: connect matter-wave and spacetime-wave dynamics into a
framework capable of describing Standard Model interactions, gravity, and
spacetime structure — or clearly identify where and why it fails.

### Goal 2 — Phase decoupling (FUTURE — depends on Goal 1)
Once phase-locking is confirmed, investigate how to decouple matter from
spacetime: α = cos(ψ − φ) → 0. This would mean zero gravitational
interaction — the engineering basis for UAP/platform-like characteristics.

Requires:
- Knowing the lattice coupling constant K (Part 29)
- Understanding the energy cost of decoupling (ΔV = g per oscillator)
- Finding a mechanism for sustained decoupling (metastable state or
  continuous energy input)
- This goal is speculative and depends entirely on Goal 1 being validated

## Falsifiable Predictions

`docs/research/falsifiable_predictions.md` is a living document. Rules:
- Update it whenever a new testable prediction is found in any Part
- **Always plan before updating** — list proposed additions, get user approval first
- Every prediction must include: statement, derivation source, assumptions,
  test method, expected value, current status, and what it distinguishes from
- The math behind every prediction must be 100% correct (SymPy verified)
- See `CODING_STANDARDS.md` section 5 for the full prediction format

## Interpretations vs Derivations

This is exploratory physics. Interpretations must be clearly separated from
mathematical derivations at all times:
- Mathematical derivations: step-by-step, SymPy verified, tagged [DERIVED]
- Physical interpretations: separate section, tagged [SPECULATIVE]
- All physics claims must be supported by: symbolic derivation, numerical
  verification, and stability analysis
- No assumptions may be hardcoded without proof

## Status
Mathematically inspired, formalization in progress.
Conceptual framework — not experimentally validated.

## GitHub
Repository: EmileAvatar/phase-decoupled-physics

## URL Rules — CRITICAL
All URLs in documents must be real, working links. Users will click them.

**Before adding any URL:**
1. Verify the page actually exists — do not assume a Wikipedia article exists for every named concept
2. Wikipedia often has NO standalone article for a specific concept (e.g. "Healing length",
   "Landau criterion", "Superfluid density") — in that case, link to the broader article where
   the concept is discussed (e.g. Gross-Pitaevskii equation, Superfluidity)
3. Never generate a Wikipedia URL by guessing — verify it resolves to the correct page
4. If a concept is a section within a broader article, use an anchor link (#section-name)
5. After creating or editing documents, run `check_urls.py` to verify all URLs

**Replacing broken URLs:**
- Find the Wikipedia/external article that actually covers the concept
- Update both the source document AND the glossary_sources.md entry
- Update the link text if it no longer matches the target article

## User and glossary_sources.md
Claude to ask user to download wiki sources if claude can't download it.
make a list of required sources and keep it updated.
create and update a glossary_sources.md with links to the various sources cited so we have it all in one place

## Python Code Rules

### No non-ASCII characters in Python files
Never use Unicode/non-ASCII characters or emojis in Python source files (.py).
This causes UnicodeEncodeError on Windows (cp1252 encoding) when the script prints output.
Use ASCII equivalents instead:
- Greek letters: alpha, beta, sigma, pi, Delta, omega, lambda, mu, nu, hbar
- Math symbols: *, ^2, ^3, /, ->, <-, ~, !=, <=, >=, dag (for dagger)
- Arrows/dashes: ->, <-, --, ---
- Subscripts/superscripts: write as _mu, ^2, etc.

Non-ASCII is fine in .md documentation files.

### Save script output to log files
When running Python scripts (standalone or as part of the solver), always save
the output to a log file in `simulations/solver/outputs/` so the user can review.
Use `tee` or redirect: `python script.py 2>&1 | tee outputs/script_name.txt`

### Chunk large file creation into smaller subtasks
When creating large Python scripts or long markdown files, break the work into
chunks of ~100 lines per Edit/Write call. This avoids hitting the 32,000 output
token limit. Plan the sections first, then write each section separately.

### RECHECK functions -- no hand-waving code results
**CRITICAL: Never hand-wave a computation.** A function that prints
narrative conclusions and returns hardcoded constants (e.g.
`return {'consistent': True, 'spin_OK': True, 'proton_charge': 1.0}`)
is a lie to the reader and will invalidate the whole project if caught.

**Before finalising any derivation / verification script, RECHECK every
step function using this checklist:**

1. **Does the function actually compute its return values?**
   Every numeric field in the returned dict must come from an arithmetic
   expression that uses inputs -- not a hardcoded literal that matches the
   expected answer. If the "expected" value is typed directly into the return
   statement, the function is not verifying anything.

2. **Is the print output backed by the computation?**
   If the function prints "E_H / E_Y = 2 pi", the ratio printed must be a
   COMPUTED variable (e.g. `ratio = E_H / E_Y`), not the string "2 pi".
   The same applies to tables: each row value must be derived from the
   inputs, not copied from a textbook answer.

3. **Does the Sudoku check exercise the computed value?**
   The consistency check MUST read the computed value from the step's
   return dict (e.g. `r3['B_baryon']`, `r5['ratio']`) and compare it to
   the expected physics constant. If the Sudoku check recomputes the
   answer inline (`Q_U + Q_U + Q_D`) without consulting the step, then
   bugs in the step are invisible to the test.

4. **If the function returns booleans, are they computed?**
   `'match': abs(B_calc - B_std) < 1e-12` is fine.
   `'match': True` (hardcoded) is NOT fine -- it is a lie.

5. **Trace path requirement:**
   For every result you claim in the final verdict, there must be a
   traceable chain:
     inputs -> arithmetic in step_k -> returned value -> Sudoku check.
   If any link in this chain is hardcoded, the chain is broken.

**When in doubt, ADD MORE Sudoku checks** that read from the step return
dicts. This is how we catch hand-waving: if the step was lying, the
check will fail against the true physics value.

**Applies to:** every PDTP derivation / verification / investigation script.
Reviewers (mathematicians, physicists, peer referees) will look for
exactly this failure mode. Hand-waved code invalidates the result; a
single hardcoded-return function can poison an entire paper.

## Problem-Solving Protocol

When we hit a problem — a mathematical gap, a failed derivation, a dead end,
an unexpected result — **stop and plan before doing any code, research, or math**.

**Steps (in order):**
1. Read `docs/Methodology.md` and select relevant checklist items for this problem (muliple if needed)
2. Write out a short plan: which strategies to try, in which order, and why
3. Present the plan to the user before starting work
4. Only proceed after the plan is agreed

The goal is to avoid going in circles. The checklist in `docs/Methodology.md`
is the menu — pick from it deliberately, not by instinct.

### Forced Checklist Check (escalation for deep problems)

When normal selected-checklist iterations have failed on a **fundamental** problem
(deriving G, the Λ problem, chirality, three fermion generations, etc.) and 3 or
more standard approaches have produced no progress, escalate to a Forced Checklist Check:

1. Open `docs/Methodology.md` and go through **every single item** in the checklist
2. For each item, answer explicitly: "Have we tried this? What was the result?"
3. Nothing is skipped — even items that seem irrelevant often produce unexpected insights
4. Document all responses in writing before forming a new plan
5. Only THEN write a new plan based on the untried items

This is the "nuclear option" — slow but guaranteed to surface untried paths.
Call it a Forced Checklist Check explicitly when invoking it.

## SymPy Math Verification

All **PDTP Original** analytical results must be verified using
`simulations/solver/sympy_checks.py` before being accepted:

- New field equations → `verify_pdtp_field_equation()`
- New T_μν / stress-energy formulas → `hamiltonian_density()` + `pressure_uniform()`
- Shift / symmetry claims → `check_shift_symmetry()`
- EOS results (w = p/ρ) → `check_eos()`
- Sign claims → `check_sign()`
- Any algebraic identity → `check_equal()`

If SymPy **cannot** verify a result (e.g., it is non-algebraic or numerical), document
why explicitly. No PDTP Original equation may be accepted without either a SymPy
verification or a written explanation of why SymPy verification is inapplicable.

## TODO
Work from TODO_04.md or TODO_05.md (both active). Do it 1 point at a time to avoid the run and token limits of claude sessions.
- TODO_04.md — tan investigation series (T10-T15 remain; T1-T9 done)
- TODO_05.md — Lambda-locking deep dive + multi-medium framework (T50-T59; opened 2026-07-04)
TODO_03.md is now archived (Parts 77–96+). Do not add new items to it.
TODO_02.md is now archived (Parts 42–76). Do not add new items to it.
User to approve the new updates before being commited and pushed to github.

### Elastic Universe (SEPARATE from PDTP)
The `Elastic_Universe/` folder contains a speculative investigation of the
elastic-universe.org framework. This is COMPLETELY SEPARATE from PDTP:
- Tracked in `Elastic_Universe/TODO_Elastic.md` (NOT in TODO_03/04)
- No results flow into PDTP docs/simulations without explicit Sudoku validation
- All content tagged [EXTERNAL] or [SPECULATIVE]
- Purpose: extract useful thinking, analogies, and visualization code
- NEVER mix Elastic Universe claims with PDTP derivations

### Open Problem Tracking Rule
**All open problems MUST be tracked in TODO files** — not just in research docs or Python scripts.
Research docs and scripts contain the details, but the TODO file is the **single source of truth**
for what is open, resolved, negative, or partial. When a problem's status changes:
1. Update the TODO file FIRST (status tag + resolution reference)
2. Then update the research doc and script
3. If a problem is resolved by a later Part, move it to the "Previously Open — Now RESOLVED" table

### Strategy for Free Parameters
See `docs/Methodology.md` section 8 for the full expand/contract/reframe strategy
and related checklist items (re-examine negatives, two-phase extension, emergent quantity, etc.).