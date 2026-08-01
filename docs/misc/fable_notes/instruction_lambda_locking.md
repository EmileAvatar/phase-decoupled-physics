# Instruction: Lambda from Locking History (T46 Attack Plan)

**Purpose:** Hand-off document for Claude Code. Proposes a mechanism that ties the
cosmological constant Lambda to the locking history beta(z), potentially collapsing
the 10^122 fine-tuning problem to an O(1) coefficient. Contains the core ansatz,
a numerical check already performed, candidate beta(z) forms, kill tests, and a
task list including a Kuramoto simulation spec.

**Status:** [SPECULATIVE] throughout. Nothing here is derived yet. This document
was produced in a claude.ai session using ONLY `term_glossary.md`, `CLAUDE.md`,
and `electricity_phase_terms.md`. Verify every claim against the full repo
(especially Parts 87, 102, 110, 115, 116, 117 and T46 in TODO_04.md) before
accepting anything.

**Project rules apply:** Sudoku consistency check, SymPy verification, equation
tags, step-by-step derivations in research .md, compute-only Python, ASCII-only
Python source, log outputs to `simulations/solver/outputs/`, user approval before
commit/push.

---

## 1. The Narrowing Insight: Lambda and beta(z) Are One Problem

Description: Stop treating Lambda as a constant of nature. Given Lambda =
g*phi_minus_vac^2 (Part 87 reframe) and phi_minus controlled by the locking
history, Lambda becomes a RELIC of beta(z) — the frozen leftover of how the
universe synced. Solving beta(z) makes Lambda's value a historical outcome, not
a free parameter.

* No-go compatibility (Part 115): the theorem blocks internal derivations because
  every internal observable rescales uniformly with m_cond.
    * beta(z) depends on H(z), the expansion history — an EXTERNAL initial
      condition, not an internal PDTP quantity.
    * Tying Lambda to expansion history therefore evades the no-go theorem.
      This must be stated and defended explicitly in the research doc.

---

## 2. Core Ansatz: The Causal Sync Limit [SPECULATIVE]

Description: Apply the project's own logic (current flow IS Kuramoto
synchronization, Part T49; gravity IS phase-locking) at cosmological scale.
Principle: clocks cannot sync with regions they cannot see.

* Two competing rates in an expanding universe
    * Sync rate: omega_gap = g_cond = m_P*c^2/hbar approx 1.86e43 rad/s
      (glossary value) — the condensate's natural frequency.
    * Desync injection rate: H(z) — expansion stretches phases apart and hides
      regions behind the causal horizon.
* The ansatz
    * phi_minus_vac ~ H / omega_gap   [SPECULATIVE — to be derived or refuted]
    * Plain English: the universe syncs almost perfectly, but expansion
      guarantees a floor of leftover desync. That floor is dark energy.

---

## 3. Numerical Check Already Performed (Reproduce and Audit)

Description: Order-of-magnitude check done in the claude.ai session using only
glossary values. No fitting. Claude Code should reproduce this in a compute-only
script as step 1 (it is cheap and anchors everything else).

* Observed gap (the "worst fine-tuning problem")
    * Lambda_obs = 3*Omega_Lambda*(H_0/c)^2 approx 1.1e-52 m^-2
    * Lambda_naive = 1/l_P^2 approx 3.8e69 m^-2
    * Ratio: Lambda_obs/Lambda_naive approx 2.9e-122
* Ansatz prediction
    * H_0/omega_gap = 2.18e-18 / 1.86e43 approx 1.17e-61
    * Squared (Lambda proportional to phi_minus_vac^2):
      (H_0/omega_gap)^2 approx 1.4e-122
* Result
    * Match to the observed ratio within a factor of approx 2.
    * The 122-order gap collapses to an O(1) coefficient, forced by the causal
      sync bound. The huge omega_gap (i.e. the Planck-mass "absurdity") does
      the suppression work, mirroring its role in the hierarchy problem.
* Audit note on the factor of approx 2
    * The framework already contains a derived factor of 2
      (G_eff = 2*G_bare, Part 61). Check whether the O(1) coefficient is
      exactly that 2. If it is, that is a Sudoku MATCH of high value. 4*pi
      would also be acceptable. An arbitrary large number would be a problem.

---

## 4. Freeze-Out Story: Why Lambda ~ H_0^2 Without Killing Galaxies

Description: Naive Lambda proportional to H(z)^2 at ALL times is ruled out
(dark energy would dominate forever; no structure forms). The two-phase locking
history fixes this: phi_minus_vac stays dynamical while beta != 0, then FREEZES
at the moment of full lock, retaining the value ~H(z_lock)/omega_gap.

* If z_lock is O(0.3 to 1), then H(z_lock) ~ H_0, giving Lambda ~ H_0^2
  automatically — consistent with the Section 3 numbers.
* Bonus 1 — coincidence problem: "why does dark energy dominate NOW?"
  Answer: full lock just completed; Lambda is stamped with the locking epoch.
* Bonus 2 — DESI: before freeze-out (beta != 0), w != -1. DESI's hint of
  evolving dark energy at higher z is what a recent freeze-out predicts.
  Part 102 loss tangent should fix the w_0/w_a shape.
* Bonus 3 — EDE: lambda_4 proportional to sin^2(beta(z)) (Part 117), and beta
  was larger early, giving a natural EDE bump before recombination that decays
  as locking proceeds. Qualitatively matches Part 117 with nothing added.

---

## 5. Candidate Functional Forms for beta(z)

Description: Three ansaetze for T46, ordered by physical motivation. Each must
be tested against the triple constraint: EDE amplitude + Lambda today +
DESI w_0/w_a.

* Candidate A — Steady-state balance
    * sin(beta(z)) approx H(z)/g_eff — desync injection balanced against sync pull.
    * Problem to resolve: if g_eff = g_cond, beta ~ 1e-61 at all times — too
      small for visible EDE or DESI signal.
    * Key question raised: what is the EFFECTIVE coupling at horizon scales?
      Check whether the biharmonic dispersion (nabla^4 + 4g^2) naturally
      softens g at low k (large wavelengths). This is a concrete derivation
      target with existing machinery (Part 61).
* Candidate B — Kuramoto critical dynamics (preferred physical picture)
    * Treat cosmic locking as a Kuramoto transition: order parameter r(z),
      beta = arccos(r).
    * Near threshold: r ~ sqrt(1 - K_c/K(z)), with K(z) growing as the causal
      horizon grows.
    * Gives a sharp, recent lock completion — matches the freeze-out story and
      the Part 110 laser-threshold critical exponents (beta=1, nu=1/2) already
      derived for the Leidenfrost transition.
* Candidate C — Pure phenomenology (fallback)
    * beta(z) = beta_r * tanh((z - z_lock)/Delta_z).
    * Fit z_lock and Delta_z to DESI + EDE, then reverse-engineer what dynamics
      produces that shape.

---

## 6. Kill Tests and Honest Objections (Referee List)

Description: Where this dies if it is wrong. Every item must be addressed in the
research doc before the result can carry a [DERIVED] tag anywhere.

* Prior art: Lambda ~ H_0^2 proposals are old (Zel'dovich-era numerology,
  running vacuum models, holographic dark energy). The PDTP contribution must
  be (a) the MECHANISM (causal sync limit from the cos coupling) and (b) the
  FREEZE-OUT history (which addresses the structure-formation and coincidence
  objections that killed naive versions). Cite prior art explicitly.
* Structure formation: rho_Lambda must be negligible during matter domination.
  Freeze-out handles this ONLY IF beta's contribution to expansion pre-lock was
  subdominant — the EDE bump must stay at or below roughly 10 percent (which is
  also what Hubble-tension fits want). One constraint, two jobs: compute
  whether it threads the needle. If not, the idea dies here.
* Unit bookkeeping: Lambda = g*phi_minus_vac^2 needs a careful dimensional
  audit (g in rad/s, Lambda in m^-2; track every factor of c). The Section 3
  check used ratio form to avoid this; the SymPy version cannot.
* No-go theorem consistency: write the explicit argument for why an
  H(z)-dependent result is external and therefore allowed by Part 115.
* Standard Model / GR compatibility: run the full Sudoku suite per CLAUDE.md
  (10+ equations, SM check, two-phase check, Newton's laws check, scorecard).

---

## 7. Simulation Spec: Kuramoto on an Expanding Lattice

Description: The decisive numerical experiment. Turns the whole proposal into
measured data instead of guesswork. Fits the project's compute-only standards.

* Setup
    * Oscillator grid (2D first, 3D if 2D shows signal) with Kuramoto coupling.
    * Mimic expansion by shrinking the coupling range in comoving coordinates
      (or equivalently diluting coupling strength K(t) per an H(t) schedule).
    * Sweep H/K over several decades.
* Measurements
    * Residual phase variance <phi_minus^2> as a function of H/K.
    * Order parameter r(t) — extract beta(z) = arccos(r) directly from data.
    * Sharpness of lock completion: freeze-out (sharp) vs gradual.
* Deliverables
    * D1: confirm or refute the scaling phi_minus_vac proportional to H/g, and
      extract the O(1) coefficient (compare against 2 and 4*pi).
    * D2: measured beta(z) curve — data-driven input for Candidates A/B/C.
    * D3: freeze-out verdict (supports or kills Section 4).
* Sudoku chain (mandatory)
    * Feed measured beta(z) into lambda_4 = 2g^2 sin^2(beta)/(3 k_bar^2)
      (Part 117) — predict EDE amplitude; check against the <=10 percent bound.
    * Feed phi_minus_vac into Lambda = g*phi_minus_vac^2 (Part 87) — predict
      today's Lambda; compare to 1.1e-52 m^-2.
    * Feed beta(z) into the Part 102 loss tangent — predict w_0/w_a; compare
      to DESI.
    * Three independent observables from one simulation — this is the T46
      jackpot structure. Score per the standard scorecard.
* Coding standards reminders
    * ASCII-only source, separate derive_/verify_/compute_ functions, no
      hardcoded return values (RECHECK checklist), tee output to
      simulations/solver/outputs/, data only — interpretation goes in the
      research .md.

---

## 8. Task List

Description: Ordered tasks. One point at a time per project rules. User approves
before anything is committed or added to TODO_04.md.

* Task 1: Reproduce the Section 3 numerical check
    * Script: compute Lambda_obs/Lambda_naive and (H_0/omega_gap)^2 from
      constants; report the ratio and the O(1) coefficient. Cite sources for
      H_0, Omega_Lambda used.
* Task 2: Dimensional audit of Lambda = g*phi_minus_vac^2
    * SymPy dimensional check; write out every factor of c and hbar. Tag the
      corrected relation.
* Task 3: No-go compatibility note
    * Short section in the research doc: why H(z)-dependence is external to
      the Part 115 theorem. Have it reviewed against the original Part 115
      derivation in the repo.
* Task 4: Effective coupling at horizon scales (Candidate A rescue)
    * Derive the k-dependence of the effective g from the biharmonic dispersion
      (Part 61). Determine whether g_eff(k -> horizon) is suppressed enough to
      make Candidate A viable. SymPy verification required.
* Task 5: Kuramoto expanding-lattice simulation (Section 7 spec)
    * Build, run, log. Extract D1, D2, D3.
* Task 6: Triple Sudoku check
    * Run the Section 7 Sudoku chain with measured beta(z). Produce scorecard:
      N matches, M contradictions out of T tests.
* Task 7: Prior art section
    * Cite Zel'dovich, running vacuum, holographic DE; state precisely what
      PDTP adds (mechanism + freeze-out). Needed to survive review.
* Task 8: Verdict and TODO update
    * If the chain passes: draft the research doc with full step-by-step
      derivations and propose T46 status change (user approval required).
    * If it fails: document the negative result and WHERE the contradiction
      appeared (per project rules, contradictions are findings).

---

## 9. One-Line Summary

Lambda stops being a fine-tuned constant if it is the frozen residue of cosmic
synchronization: the causal sync limit predicts (H_0/omega_gap)^2 approx 1e-122
— the observed value within a factor of approx 2 — and a recent locking
freeze-out would simultaneously explain why dark energy dominates now and why
DESI sees w drifting.

---

*Generated 2026-07-02 from a claude.ai session. [SPECULATIVE] until it survives
the Sudoku suite. Verify against the full repository before acting.*
