## Prompt 1 — Dvali-Gomez Criticality (T55) — highest value

PDTP physics framework. Context and task below.

PDTP Lagrangian: L = ½(∂φ)² + Σ½(∂ψᵢ)² + Σg cos(ψᵢ−φ)
Key result: G = ℏc/m_cond² (exact). Problem: m_cond is a free parameter.
All perturbative paths to fix m_cond are exhausted (circularity proven algebraically).

NEW HYPOTHESIS (T55): Dvali-Gomez (2011, arXiv:1106.3548) showed that a
self-gravitating condensate of N gravitons saturates when α_gr = N·G/R²·ℏc = 1.
This criticality condition is a fixed point — systems drift toward it.
If the PDTP spacetime condensate self-tunes to this criticality, m_cond = m_P
emerges from dynamics rather than being a fitting parameter.

KEY QUESTION: Is α_gr = 1 an attractor fixed point of the PDTP condensate dynamics?
Specifically:
1. Write down the PDTP condensate energy as a function of m_cond (= ℏω_gap/c²).
2. Compute dE/d(m_cond) and show whether the minimum is at m_cond = m_P.
3. Check: does the Jeans instability eigenvalue λ = +2√2·g (Part 61, two-phase)
   give a preferred scale when combined with the criticality condition?
4. Dvali-Gomez criticality: N·ℏ = M·R·c (for a BH of mass M, radius R).
   What is N for the spacetime condensate with m_cond? Does N=1 force m_cond = m_P?

CODING STANDARDS:
- Every returned dict value must be COMPUTED, not hardcoded.
- All equations tagged [ASSUMED], [DERIVED], [SPECULATIVE], or [VERIFIED].
- PDTP Original results must be SymPy-verified (residual = 0).
- No Unicode in Python; plain ASCII only.
- Run 10+ Sudoku consistency checks substituting result into known equations.

FILES TO CREATE/UPDATE:
1. Script: simulations/solver/t55_dvali_gomez.py  (new)
2. Research doc: docs/research/hierarchy_problem_reframe.md  (add T55 section)
3. TODO_05.md: update T55 status line to [DONE/PARTIAL] with Sudoku score

Related context: docs/research/extremal_condensate.md (Part 78 results),
docs/research/vortex_winding_derivation.md (n = m_cond/m derivation).

---
## Prompt 2 — Lambda Causal-Sync (T50) — cheap, high impact

PDTP physics framework. Context and task below.

Two-phase Lagrangian (Part 61): L = +g cos(ψ−φ_b) − g cos(ψ−φ_s)
phi_minus = (phi_b − phi_s)/2 is a surface mode.
Part 119 result: phi_minus = pi/2 is the true vacuum; thawing EOS w = −1+2ε.
G_eff = 2·G_bare (derived from Lagrangian symmetry, Part 61).
omega_gap = g = m_P·c²/ℏ ≈ 1.855×10⁴³ rad/s.

CAUSAL-SYNC ANSATZ (T50, SPECULATIVE):
phi_minus_vac ~ H / omega_gap
Lambda ~ (H₀ / omega_gap)²

TASK: Numerically verify this ansatz.
1. Compute Lambda_obs = 3·Omega_Lambda·(H₀/c)² using Planck 2018 values.
2. Compute Lambda_naive = 1/l_P² (Planck-scale prediction).
3. Compute ratio: Lambda_obs / Lambda_naive.
4. Compute (H₀ / omega_gap)².
5. Compare — do they match within one order of magnitude?
6. Identify the O(1) coefficient. Check whether it equals 2 (from G_eff = 2·G_bare),
   4, or 4π. A clean match is a Sudoku PASS of high value.
7. Dimensional check: confirm (H₀/omega_gap)² is dimensionless.
8. Two-phase check: G_eff = 2·G_bare shifts omega_gap by √2; does the ratio still match?

CODING STANDARDS:
- Every numerical result must come from arithmetic expressions using the input constants.
- No hardcoded return values matching the expected answer.
- Tag all equations [DERIVED], [SPECULATIVE], or [VERIFIED].
- No Unicode in Python.
- Minimum 5 Sudoku tests.

Note: H₀ is an external cosmological input, NOT derived from PDTP.
This does NOT violate the Part 115 no-go theorem (which blocks internal circular
derivations only). Using H₀ ties Lambda to expansion history — genuinely external.

FILES TO CREATE/UPDATE:
1. Script: simulations/solver/t50_lambda_causal_sync.py  (new)
2. Research doc: docs/research/lambda_locking_fossil.md  (add T50 section at bottom)
3. TODO_05.md: update T50 status line to [DONE/PARTIAL] with Sudoku score

---
## Prompt 3 — CP Violation Quantitative (B4) — fixes known gap

PDTP physics framework. Context and task below.

Two-phase Lagrangian (Part 61): L = +g cos(ψ−φ_b) − g cos(ψ−φ_s)
Part 85 established the CP violation mechanism:
- L4 (U(1)+sin): FAKE — removable by field redefinition
- L5 (two-phase + ε·sin(2·phi_minus)): REAL — shifts vacuum, Sakharov cond. 2 derived
- L6 (SU(3) + Im[Tr]): REAL — is the QCD theta-term

The mechanism is known. The MAGNITUDE has never been computed.

TASK: Full quantitative CP violation calculation for L5.
1. Define CP transformation rules for ψ, φ_b, φ_s explicitly (show under CP:
   phi_b → −phi_b, phi_s → −phi_s, ψ → −ψ and verify L5 is CP-odd).
2. Verify L4 is removable: SymPy identity cos(x)+ε·sin(x) = A·cos(x+δ),
   find A and δ, confirm the sin term is absorbed by phase redefinition.
3. Full potential V(phi_minus) with −ε·sin(2·phi_minus) term:
   V = −2g·Phi·sin(phi_minus) − ε·sin(2·phi_minus)
   Find shifted vacuum phi_minus* = π/2 − δ; solve for δ(ε) to leading order.
4. Check Sakharov condition 2: V(delta*) ≠ V(−delta*) when ε ≠ 0. [DERIVE]
5. Estimate baryon asymmetry: use Sakharov (1967) formula
   η = n_B/n_γ ~ (ε/g) × (ΔΓ/Γ) × (1/g_*^(1/2))
   Target: η_obs ~ 6×10⁻¹⁰.
   What ε/g ratio is required? Is it physically reasonable?
6. Strong CP: for L6, why is theta ~ 0? Is there a PDTP analog of the Peccei-Quinn
   mechanism (axion)? Or does topological cancellation work?

CODING STANDARDS:
- Every returned dict value must be computed from arithmetic, not hardcoded.
- SymPy verification for every algebraic identity (residual must = 0 symbolically).
- Tag all results [DERIVED], [SPECULATIVE], or [VERIFIED].
- No Unicode in Python.
- Run 10+ Sudoku checks; check L5/L6 still pass all 16 two-phase re-derivation tests.

FILES TO CREATE/UPDATE:
1. Script: simulations/solver/cp_violation_quantitative.py  (new, extends Phase 55)
2. Research doc: docs/research/cp_violation.md  (add quantitative B4 section)
3. TODO_03.md: mark B4 subtasks [x] as completed; update B4 status