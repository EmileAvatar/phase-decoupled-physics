# TODO_05 — Lambda-Locking Deep Dive and Multi-Medium Framework

**Type:** Extended investigation — Lambda mechanism + multi-condensate structure
**Date opened:** 2026-07-04
**Source notes:** `docs/fable_notes/` (Fable session notes + DESI update, 2026-07-02/04)
**Previous roadmaps:** [TODO_01.md](TODO_01.md) (Parts 1-41) |
[TODO_02.md](TODO_02.md) (Parts 42-76) | [TODO_03.md](TODO_03.md) (Parts 77-83+) |
[TODO_04.md](TODO_04.md) (Parts 84-120+)

---

## Overview

Two investigation threads opened by Fable session notes (2026-07-02) and DESI
DR2 data analysis (2026-07-04):

**Thread A — Lambda-Locking Deep Dive (T46 extended)**
T46 (Part 119) proved phi_- = pi/2 is the true vacuum and derived the thawing EOS
w = -1+2*eps. The magnitude problem remains: the causal-sync ansatz
phi_minus_vac ~ H/omega_gap predicts (H_0/omega_gap)^2 ~ 1.4e-122, matching the
observed Lambda ratio within factor ~2. DESI DR2 adds empirical targets:
w_0 ~ -0.7, w_a ~ -1 (contested), dark energy peak at z ~ 0.5.

**Thread B — Multi-Medium Framework**
PDTP has at least three interpenetrating condensates (gravitational, EM, QCD).
The stiffness ratios between them are hard predictions, not free parameters.
Key open questions: Dvali-Gomez criticality as an attractor, QCD stiffness
cross-check, cross-medium coupling Sudoku, and weak-force placement.

---

## Open Items — Quick Reference

New additions go on top. One line per item. Full details below.

- T59 — Weak force placement: SU(2) extension vs riding existing condensate; even deferred answer must be tracked per Open Problem Tracking Rule [PENDING, SPEC, LOW PRIORITY]
- T58 — EM condensate quantum mass: locate or derive m_cond_EM giving the 1e36 grav/EM ratio; add to term_glossary.md if missing [PENDING, LOW PRIORITY, one-row addition]
- T57 — Cross-medium coupling Sudoku: verify PDTP reproduces "EM energy gravitates" (GR requirement); explain what suppresses condensate-condensate direct locking [PENDING, MEDIUM; 5+ Sudoku tests]
- T56 — QCD/gravitational stiffness ratio: compute ratio from same formula structure as m_cond_QCD = 367 MeV (Part 37); investigate M_0 ~ m_p/3 ~ m_cond_QCD coincidence; link to hierarchy problem [PENDING, HIGH]
- T55 — Dvali-Gomez criticality as attractor: formalize alpha_gr=1 as stability fixed point of condensate dynamics; if attractor, m_cond=m_P is derived not fitted; link to Part 110 laser-threshold critical exponents [PENDING, HIGHEST VALUE]
- T54 — Prior art section: cite Zel'dovich, running vacuum, holographic DE; state what PDTP adds (mechanism + freeze-out); needed to survive peer review [PENDING, MEDIUM; research doc section]
- T53 — Phantom crossing derivation: derive effective w(z) of partially-locked phi_minus INCLUDING energy exchange with matter sector; check w < -1 without ghost instability; SymPy + Sudoku [PENDING, HIGH; Task 4b from DESI update]
- T52 — Kuramoto expanding-lattice simulation: 2D Kuramoto grid with shrinking coupling range mimicking H(t); measure <phi_minus^2> vs H/K; extract beta(z); triple Sudoku chain (EDE + Lambda + w_0/w_a) [PENDING, HIGH; jackpot sim]
- T51 — Dimensional audit: Lambda = g * phi_minus_vac^2 SymPy dimensional check tracking every factor of c and hbar; tag the corrected relation [PENDING, MEDIUM; prerequisite for T52]
- T50 — Lambda causal-sync numerical check: compute (H_0/omega_gap)^2 ~ 1.4e-122 and Lambda_obs/Lambda_naive ~ 2.9e-122; check O(1) coefficient against 2 and 4*pi [PENDING, HIGH; cheap first step]

**Natural first picks:** T50 (cheap, anchors Thread A); T55 (highest scientific value in Thread B).

---

## Rules

Same as TODO_04:
- One Part at a time
- Every new equation: Sudoku consistency check (10+ tests)
- Every PDTP Original result: SymPy verification
- Every research .md: complete derivation (show your work)
- Python: no Unicode, save output to `simulations/solver/outputs/`
- Plain English explanations for every key result
- Commit after user approval

---

## Group A — Lambda-Locking Deep Dive (T46 Extended)

**Context:** T46 (Part 119, Phase 87) established the Lambda-locking mechanism:
phi_- = pi/2 is the true vacuum; freeze condition eps < 1/9 [Eq 119.2]; thawing
EOS w = -1+2*eps [Eq 119.3]; mechanism consistent; magnitude of phi_minus_vac
remains open. The causal-sync ansatz from the Fable session proposes the resolution.

### T50 — Lambda Causal-Sync Numerical Check [HIGH, cheap first step]

**Status:** PENDING
**Estimated effort:** ~2 hours (one short script; no new theory)
**Source:** `docs/fable_notes/instruction_lambda_locking.md` Section 3

**What:**
Reproduce the order-of-magnitude check from the Fable session using only known
constants. No fitting. Script must be compute-only with no hardcoded return values.

**Core ansatz [SPECULATIVE]:**
phi_minus_vac ~ H / omega_gap
Lambda ~ (H_0 / omega_gap)^2

**Compute targets:**
- Lambda_obs = 3 * Omega_Lambda * (H_0/c)^2 ~ 1.1e-52 m^-2  [Planck 2018]
- Lambda_naive = 1/l_P^2 ~ 3.8e69 m^-2
- Ratio: Lambda_obs / Lambda_naive ~ 2.9e-122
- omega_gap = m_P*c^2/hbar ~ 1.86e43 rad/s  [G-free: uses m_P from calibration]
- Ansatz: (H_0 / omega_gap)^2 ~ 1.4e-122

**Key Sudoku check:**
Is the O(1) coefficient exactly 2 (from G_eff = 2*G_bare, Part 61)?
Or 4*pi? Or 4? Any of these is a Sudoku MATCH of high value. An arbitrary
large number is a problem.

**No-go compatibility note (must be stated in the doc):**
H_0 is an external cosmological input, not an internal PDTP quantity. Using it
does NOT violate the Part 115 no-go theorem (which blocks internal circular
derivations only). The ansatz ties Lambda to expansion history -- genuinely external.

**Sudoku (5 minimum for a cheap check):**
- S1: Lambda_obs / Lambda_naive matches (H_0/omega_gap)^2 within 1 OoM
- S2: omega_gap formula is G-free (verify: omega_gap = m_P*c^2/hbar uses only hbar, c, m_P)
- S3: ratio is dimensionless (dimensional check)
- S4: O(1) coefficient identified and checked against 2, 4, 4*pi
- S5: two-phase check -- G_eff = 2*G_bare shifts prediction by factor sqrt(2); still within OoM

**Deliverables:**
- Script: `simulations/solver/t50_lambda_causal_sync.py`
- Result added as a section to `docs/research/lambda_locking_fossil.md` (extend T46 doc, not new file)

---

### T51 — Dimensional Audit: Lambda = g * phi_minus_vac^2 [MEDIUM]

**Status:** PENDING
**Estimated effort:** half-day (SymPy dimensional analysis)
**Source:** `docs/fable_notes/instruction_lambda_locking.md` Section 6 kill tests
**Prerequisite:** T50 (need numerical values before auditing the formula)

**What:**
The formula Lambda = g * phi_minus_vac^2 was cited from Part 87 in the Fable
notes. T46 used ratio form to sidestep dimensional issues. A full derivation
cannot. Track every factor of c and hbar from the Lagrangian coupling g [rad/s]
to Lambda [m^-2].

**Key questions:**
- Exact SI units of phi_minus_vac in the two-phase Lagrangian (Part 61)?
- Correct formula: Lambda = g/c^2 * phi_minus_vac^2, or involves hbar?
- Does biharmonic dispersion (Part 61) contribute additional factors?

**Deliverables:**
- SymPy script with dimensional chain verification
- Updated section in lambda_locking_fossil.md with corrected relation tagged [DERIVED] or [SPECULATIVE]

---

### T52 — Kuramoto Expanding-Lattice Simulation [HIGH, large task]

**Status:** PENDING
**Estimated effort:** several days (build + run + analysis)
**Source:** `docs/fable_notes/instruction_lambda_locking.md` Section 7

**What:**
The decisive numerical experiment for the lambda-locking mechanism. Turns the
ansatz phi_minus_vac ~ H/omega_gap into measured data instead of guesswork.

**Setup:**
- 2D Kuramoto oscillator grid (extend to 3D if 2D shows clear signal)
- Mimic expansion: dilute coupling strength K(t) per an H(t) schedule
  (matter + Lambda + radiation phases)
- Sweep H/K over several decades (H/omega_gap from 1e-60 to 1e-40)

**Measurements:**
- D1: residual phase variance <phi_minus^2> vs H/K
  -- confirm or refute phi_minus_vac ~ H/g; extract O(1) coefficient
- D2: order parameter r(t) -- compute beta(z) = arccos(r) directly from data
- D3: freeze-out verdict -- sharp (laser-threshold like) or gradual?

**Triple Sudoku chain (jackpot structure -- 3 observables, 1 simulation):**
- Feed measured beta(z) into lambda_4 = 2g^2 sin^2(beta)/(3 kbar^2) [Part 117]
  -- predict EDE amplitude; check <= 10% bound
- Feed phi_minus_vac into Lambda = g*phi_minus_vac^2 [Part 87]
  -- predict Lambda today; compare to 1.1e-52 m^-2
- Feed beta(z) into Part 102 loss tangent
  -- predict w_0/w_a; compare to DESI targets (CONTESTED; see T53)

**Candidate B preference:**
Kuramoto critical dynamics gives sharp recent lock -- matches freeze-out story and
Part 110 laser-threshold critical exponents (beta=1, nu=1/2). Start with Candidate B.

**LCDM branch requirement (from DESI update):**
Report which H/K regions give sharp freeze-out (DESI branch) vs early gradual lock
(pure LCDM branch). Do NOT assume the DESI w_a hint is real.

**Script:** `simulations/solver/t52_kuramoto_expansion.py`
**Doc:** new `docs/research/kuramoto_expansion.md`

---

### T53 — Phantom Crossing Derivation [HIGH, new from DESI update]

**Status:** PENDING
**Estimated effort:** half-day to 1 day
**Source:** `docs/fable_notes/desi_update_lambda_locking_amendments.md` Section 4

**What:**
DESI best-fit: w ~ -1.7 at high z, crossing to w > -1 today. Ordinary scalar
fields cannot cross w = -1 without ghost instabilities. PDTP candidate (Task 4b):
the dark energy sector is NOT closed during active locking (alpha = cos(Delta)
evolving means energy flows between matter and condensate), so effective w < -1
may be possible without real ghosts.

**Required derivation:**
1. Derive effective w(z) of partially-locked phi_minus INCLUDING energy exchange
   with matter sector (Part 61 two-phase equations as starting point)
2. Determine if phantom-to-quintessence crossing at lock completion is generic
   or requires tuning
3. Verify ghost-freedom (kinetic term positive definite in the two-phase Lagrangian)

**Sudoku:**
- S1: w(z_lock) = -1 exactly (phi_minus frozen -> pure cosmological constant)
- S2: w at z >> z_lock -- compatible with matter domination (dark energy subdominant)
- S3: ghost check -- kinetic term positive definite throughout
- S4: two-phase check -- consistent with Part 61 equations
- S5: DESI target -- can w_0 ~ -0.7, w_a ~ -1 be reproduced without tuning?

**If ghost-free crossing derived:** major result; full Sudoku suite + SymPy.
**If it fails:** document as NEGATIVE (ghost instability, requires new mechanism);
the failure tells us where DESI signal cannot come from.

**Script:** `simulations/solver/t53_phantom_crossing.py`
**Doc:** section appended to `docs/research/lambda_locking_fossil.md`

---

### T54 — Prior Art Section [MEDIUM, research doc]

**Status:** PENDING
**Estimated effort:** ~2 hours (literature review + writing)
**Source:** `docs/fable_notes/instruction_lambda_locking.md` Section 6

**What:**
Lambda ~ H_0^2 proposals have a long history. The PDTP doc must cite prior art
and state precisely what PDTP adds (mechanism + freeze-out), not just the number.

**Prior art to cite:**
- Zel'dovich (1968): Lambda ~ (G*m_p^2/hbar*c)^6 * m_p^2*c/hbar^3 -- numerology
- Running vacuum models: Shapiro & Sola -- Lambda running as H^2
- Holographic dark energy: Li (2004) -- L = c^2/L_H^2 from causal horizon
- Cohen-Kaplan-Nelson (CKN) bound (already in T46 doc)

**What PDTP adds (explicit statement required):**
1. MECHANISM: causal sync limit from cos(psi-phi) coupling -- not numerology
2. FREEZE-OUT history: explains structure formation, coincidence problem, DESI hint
3. Falsifiable output: beta(z) shape from T52 simulation

**Deliverables:**
- Section "Prior Art and Comparison" appended to `docs/research/lambda_locking_fossil.md`
- All URLs verified (run check_urls.py)

---

## Group B — Multi-Medium Framework

**Context:** PDTP has (at minimum) three interpenetrating condensates: gravitational
(m_P), EM (m_cond_EM unknown), QCD (~367 MeV, Part 37). Same Lagrangian structure;
only stiffness differs. Stiffness ratios are hard predictions (not free parameters).
Session source: `docs/fable_notes/session_summary_dm_mcond_unification.md`

### T55 — Dvali-Gomez Criticality as Attractor [HIGHEST VALUE]

**Status:** PENDING
**Estimated effort:** 1-2 days (stability analysis + Part 110 link)
**Source:** `docs/fable_notes/session_summary_dm_mcond_unification.md` TC1

**What:**
Part 115 proved the no-go theorem: m_cond is externally underdetermined. But Part 115
also found Dvali-Gomez criticality (alpha_gr = 1, every condensate grain is marginally
its own black hole) is satisfied at EXACTLY m_cond = m_P with ALL bounds simultaneously
saturated. The question: is alpha_gr = 1 an ATTRACTOR of condensate dynamics (not
an assumed input)?

If yes, m_cond = m_P is the stable fixed point of the self-organization dynamics --
the only no-go-compatible route to "derive" m_cond.

**Derivation strategy:**
1. Write condensate self-energy as a function of m_cond (Lagrangian structure fixed,
   grain mass varied)
2. Compute d(alpha_gr)/d(m_cond); find fixed points
3. Check stability: d^2E/d(m_cond)^2 > 0 at alpha_gr = 1? (energy minimum = attractor)
4. Link to Part 110 laser-threshold universality class (beta=1, nu=1/2) -- same class?

**No-go compatibility (must be stated explicitly):**
The no-go theorem blocks internal ALGEBRAIC ratios pinning m_cond. An attractor
argument derives m_cond from DYNAMICS (energy minimization), not from algebra. These
are different: one is circular substitution, the other is a stability condition.

**Sudoku (if attractor confirmed):**
- S1: alpha_gr computed FROM m_cond = m_P (not assumed); verify = 1.000
- S2: r_S = 2*a_0 (Schwarzschild = 2*Compton) at the fixed point
- S3: G = hbar*c/m_cond^2 gives G_pred = G_known at the fixed point
- S4: all Part 115 bounds saturated simultaneously at the fixed point

**Script:** `simulations/solver/t55_dvali_gomez_attractor.py`
**Doc:** `docs/research/dvali_gomez_attractor.md`

---

### T56 — QCD/Gravitational Stiffness Ratio [HIGH]

**Status:** PENDING
**Estimated effort:** 1 day (analytical + Sudoku)
**Source:** `docs/fable_notes/session_summary_dm_mcond_unification.md` TC2

**What:**
m_cond_QCD ~ 367 MeV (Part 37) and M_0 ~ 313.84 MeV ~ m_p/3 (Part 32, 0.3%)
arise from the same Lagrangian structure. If the formula giving m_cond_QCD extends
to the gravitational condensate, the stiffness ratio m_P / m_cond_QCD might be
computable from QCD running couplings -- giving m_cond_grav from measured QCD data.

**Key quantities:**
- m_cond_QCD ~ Lambda_QCD ~ 200 MeV (Part 37: 367 MeV from sigma fit)
- m_P = sqrt(hbar*c/G) ~ 2.176e-8 kg
- Ratio: m_P / m_cond_QCD ~ 3.6e19
- Candidate derivation: does this ratio = exp(8*pi^2/g_s^2) or similar from
  the QCD running coupling? (SU(3) beta function is negative -- asymptotically
  free; U(1) PDTP beta function is positive -- IR free. Different structure.)

**Sudoku:**
- S1: m_cond_QCD from formula within 10% of Part 37 value (367 MeV)
- S2: stiffness ratio dimensionless (dimensional check)
- S3: ratio from QCD running coupling -- does it match 3.6e19?
- S4: if ratio derivable, compute m_P prediction; verify vs known value

**Script:** `simulations/solver/t56_stiffness_ratio.py`
**Doc:** `docs/research/stiffness_ratio.md`

---

### T57 — Cross-Medium Coupling Sudoku [MEDIUM]

**Status:** PENDING
**Estimated effort:** half-day (Sudoku checks; no new derivation required)
**Source:** `docs/fable_notes/session_summary_dm_mcond_unification.md` TC3

**What:**
GR requires: EM field energy gravitates. PDTP must reproduce this. In PDTP, psi_EM
locks to phi_grav (like any matter), so photon energy does gravitate. But: what
prevents phi_grav from directly phase-locking to A_mu (the EM condensate field)?

**Sudoku tests:**
- S1: photon gravitational lensing -- psi_photon locking gives 1.75" deflection
  (Part 112 GR recovery); verify it comes from psi-phi coupling, not condensate-condensate
- S2: Shapiro delay for light -- consistent with GR gamma=1 (Part 112)?
- S3: EM stress-energy source -- does PDTP's picture produce the GR T_mu_nu^EM source term?
- S4: condensate-condensate coupling amplitude -- what suppresses phi_grav locking to A_mu?
  (Expected suppression: the coupling constant ratio m_cond_grav/m_cond_EM ~ sqrt(1e36))
- S5: Lorentz invariance -- EM condensate must not introduce a preferred frame;
  c_s = c must hold independently (Part 34)

**Doc:** section in new `docs/research/multi_medium_framework.md`

---

### T58 — EM Condensate Quantum Mass [LOW PRIORITY]

**Status:** PENDING
**Estimated effort:** ~1 hour (one glossary row or short scoping note)
**Source:** `docs/fable_notes/session_summary_dm_mcond_unification.md` TC4

**What:**
The 1e36 grav/EM ratio is stated in PDTP but no explicit m_cond_EM appears in
the current docs. Either locate it in the repo (Parts 22, 28b, 36) or compute it:

If G_EM analogue = k_e = 1/(4*pi*eps_0), then by G = hbar*c/m_cond^2:
m_cond_EM = sqrt(hbar*c*4*pi*eps_0) -- compute and add to term_glossary.md.

**Cross-check:**
- m_P / m_cond_EM should equal sqrt(k_e/G) = sqrt(alpha * m_P^2/m_e^2) -- verify
- Is m_cond_EM related to m_e (electron mass) or the fine structure constant?

**Deliverable:** one row in term_glossary.md + one sentence in multi_medium_framework.md

---

### T59 — Weak Force Placement Note [LOW PRIORITY]

**Status:** PENDING
**Estimated effort:** ~1 hour (scoping doc; deferred answer acceptable)
**Source:** `docs/fable_notes/session_summary_dm_mcond_unification.md` TC5

**What:**
No SU(2) extension or fourth condensate appears in current PDTP docs. The weak
force must go somewhere. Two candidate routes:
(a) SU(2) condensate with its own m_cond_weak (analogous to the SU(3) extension, Part 37)
(b) Weak force rides an existing condensate with Higgs-like symmetry breaking from
    phi_minus (phi_minus is a "reversed Higgs", Part 62)

Per the Open Problem Tracking Rule, even "not yet investigated" must be recorded.

**Deliverables:**
- `docs/research/weak_force_placement.md` (< 1 page; scoping only)
- Add as OPEN question to equation_reference.md

---

## Previously Open — Now Resolved

*(None yet -- resolved items will be moved here)*

---

## Assets

**HTML Visualizations (Gemini, 2026-07-04):**
- `assets/visualizations/gemini-code-1783012329313.html` -- Planck Vortex Relic (n=1) animation
- `assets/visualizations/pdtp_spacetime_and_matter.html` -- Spacetime phase-locking animation
Open in any browser.

**Source notes (Fable sessions):**
- `docs/fable_notes/session_summary_dm_mcond_unification.md` -- DM/m_cond session (2026-07-02)
- `docs/fable_notes/instruction_lambda_locking.md` -- T46 attack plan (2026-07-02)
- `docs/fable_notes/desi_update_lambda_locking_amendments.md` -- DESI DR2 update (2026-07-04)
