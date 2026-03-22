# TODO_03 — Active Roadmap

Summary of completed work: [TODO_Summary.md](TODO_Summary.md)
Previous roadmaps: [TODO_01.md](TODO_01.md) (Parts 1–41) | [TODO_02.md](TODO_02.md) (Parts 42–76)

---

## Methodology

Before starting any new problem, follow the Problem-Solving Protocol:

1. Read `docs/Methodology.md` and select relevant checklist items
2. Write out a short plan: which strategies to try, in which order, and why
3. Present the plan to the user before starting work
4. Only proceed after the plan is agreed

For deep/fundamental problems where 3+ approaches have failed, escalate to a
**Forced Checklist Check (FCC)** — see CLAUDE.md for full protocol.

**Strategy for free parameters:** See `docs/Methodology.md` section 8 for the full
expand/contract/reframe checklist (including re-examine negatives, two-phase extension,
emergent quantity, and independent Lagrangian strategies).

---

## Rules

- One Part at a time to stay within session/token limits
- Every new equation: Sudoku consistency check (10+ tests, SM compatibility, two-phase check)
- Every PDTP Original result: SymPy verification before acceptance
- Every research .md: complete derivation (show your work — see CLAUDE.md)
- Python: no Unicode, save output to `simulations/solver/outputs/`, cite all sources
- Commit after each completed Part; user approves before push
- **All open problems MUST be tracked in TODO files** — research docs and scripts
  may contain details, but the TODO file is the single source of truth for status

---

## Current Status (as of Part 76)

**What works:**
- Three Lagrangians (U(1), two-phase, SU(3)) — internally consistent
- Einstein equation recovery via SU(3) emergent metric + Sakharov mechanism
- QCD string tension within 4% from first principles (strong-coupling formula)
- 12 falsifiable predictions ranked by testability
- 76 parts of systematic derivation; comprehensive solver with 46 phases

**Free parameters:** m_cond, Lambda, alpha_EM, sin^2(theta_W), v_EW, theta_0

---

## Open Problems — Master Registry

Every open problem in PDTP is tracked here. Status tags:
- **OPEN** — unsolved, actively on the roadmap
- **NEGATIVE** — attempted and failed; re-examine with FCC when new findings arise
- **PARTIAL** — structure derived but value/magnitude underdetermined
- **RESOLVED** — solved in a later Part (reference given)

---

### Category A — Free Parameters (expand/contract strategy)

These are values PDTP cannot currently derive. Strategy: find an independent
equation that produces the value without using PDTP/GR/QED as input, or reframe
as pointing to deeper physics.

#### [ ] A1. m_cond = m_P underdetermined — OPEN (BLOCKING)

**Problem:** G = hc/m_cond^2 is exact, but m_cond = m_P is not derived.
**Prior research:**
- Part 29: All 8 substitution chains circular (algebraically proven)
- Part 30: Sakharov route gives G = a^2/(N_eff pi hbar c); breathing gap ~ 69 GeV
- Part 33: Vortex winding n = m_cond/m [DERIVED]; G = hc/m_cond^2 [G-free given m_cond]
- Part 34: Condensate self-consistent for ANY m_cond (one-parameter family)
- Part 35: Dimensional transmutation NEGATIVE (beta > 0, IR free)
- Scripts: `vortex_winding.py`, `condensate_selfconsist.py`, `dim_transmutation.py`, `brute_force_runner.py`
- Docs: `vortex_winding_derivation.md`, `condensate_selfconsist.md`, `dimensional_transmutation.md`
**Status:** All perturbative paths exhausted (Parts 29-35). m_cond analogous to Lambda in GR.
**FCC trigger:** Yes — fundamental problem, 5+ approaches failed.
**New findings since last attempt:** SU(3) extension (Parts 37-41), two-phase (61-63),
Einstein recovery (72-76), graviton validation (76). SU(3) may provide non-perturbative path.
**RESULTS:** [ ]

#### [ ] A2. alpha_EM = 1/137.036 not derived — OPEN (CRITICAL)

**Problem:** EM coupling constant value has no derivation in SM or PDTP.
**Prior research:**
- Part 5: alpha = Z_0/(2R_K) is exact structural identity (circular, contains h and e)
- Part 27: Beta functions derived from group theory; initial values alpha_EM, alpha_S free
- Part 55: Two-channel model gives alpha ~ K_0^2 ~ 1/158 (13.2% off)
- Part 56: RG running K_0 -> alpha_EM FAILED (wrong direction, 3 models tested)
- Part 57: Dispersion model FAILED (4 fatal problems)
- Scripts: `coupling_constants.py`, `rg_alpha_em.py`
- Docs: `coupling_constants.md`, `fine_structure_derivation.md`
**Status:** Structure derived (why it exists, why mass-independent), value not.
**FCC trigger:** Yes — 3+ approaches failed (Parts 55, 56, 57).
**New findings since last attempt:** SU(3) emergent metric (Part 75) changes DOF counting;
graviton validation (Part 76) constrains spin-2 sector.
**RESULTS:** [ ]

#### [ ] A3. Cosmological constant Lambda — OPEN (CRITICAL)

**Problem:** Lambda is a second free parameter alongside G. Cannot be derived.
**Prior research:**
- Part 17: Scalar sector filters vacuum; tensor sector inherits GR's Lambda problem
- Part 54: FCC done; three paths converge on rho_Lambda ~ rho_Planck x (l_P/L_H)^2
- Part 68: Two-phase FCC; Omega_beat = 2/3 (2.6% off observed); beat freq rejected
- Part 69: Scale selection; all scales ~ l_P; H_0 confirmed as 2nd free parameter
- Scripts: `cosmo_constant.py`, `cosmo_constant_v2.py`, `scale_selection.py`
- Docs: `cosmological_constant_fcc.md`, `cosmo_constant_two_phase.md`, `scale_selection_mechanism.md`
**Status:** Lambda analogous to G — both free parameters of condensate initial conditions.
**FCC trigger:** Yes — multiple approaches failed.
**New findings since last attempt:** Two-phase phi_- + Einstein recovery may constrain.
**RESULTS:** [ ]

#### [ ] A4. Koide theta_0 = 2/9 underdetermined — OPEN (MEDIUM)

**Problem:** Lepton mass angular parameter has no SU(3) derivation.
**Prior research:**
- Part 4: Koide Q = 2/3 <=> delta = sqrt(2); Z_3 phase geometry
- Part 32: 0/8 non-circular candidates; Koide = structure theorem, not scale theorem
- Part 53: Z3 geometry + equal partition derives delta = sqrt(2); theta_0 remains free
- Scripts: `koide_z3.py`, `koide_lattice_analysis.py`
- Docs: `koide_z3_derivation.md`, `koide_lattice_analysis.md`
**Status:** 3 lepton masses reduced to 2 free params (M_0, theta_0); delta eliminated.
**FCC trigger:** Not yet — only 2 approaches tried.
**New findings:** Xi_cc baryon (Part 70) provides new mass constraint; SU(3) geometry may fix angle.
**RESULTS:** [ ]

#### [ ] A5. sin^2(theta_W) and v_EW = 246 GeV — OPEN (MEDIUM)

**Problem:** Weak mixing angle and EW condensate scale are free parameters.
**Prior research:**
- Part 27: Structure derived (ratio of condensate stiffnesses); value not derived
- Docs: `coupling_constants.md`
**Status:** No derivation attempted beyond structure. Requires EW condensate model.
**FCC trigger:** Not yet — minimal investigation so far.
**RESULTS:** [ ]

#### [ ] A6. Coupling constant g (Lagrangian) — OPEN (HIGH)

**Problem:** g in L = g cos(psi - phi) is not determined from first principles.
**Prior research:**
- Part 1: g introduced as coupling; determines omega_gap, G_eff, breathing amplitude
- Part 62: phi_- mass m^2 = 2g*Phi — connects g to measurable mass
- Part 75b: Breathing mode mass depends on g
- Docs: `mathematical_formalization.md`
**Status:** g determines all physical scales but is itself underdetermined. Related to A1 (m_cond).
**FCC trigger:** Linked to A1; if m_cond determined, g follows.
**RESULTS:** [ ]

---

### Category B — Structural Gaps (derive from within PDTP)

These are missing derivations where the answer should come from the framework.

#### [ ] B1. N_eff = 6pi gap in Sakharov formula — OPEN (CRITICAL)

**Problem:** Sakharov 1-loop gives G_ind = 2.36 x G (need N_eff ~ 18.85 but get ~3).
**Prior research:**
- Part 30: Sakharov route identified; breathing gap ~ 69 GeV
- Part 75b: G_ind = 2.36G with 8 gluon fields; auto-Lorenz gauge DERIVED
- Part 76a: Graviton validation confirms Fierz-Pauli structure
- Scripts: `su3_einstein_recovery.py`, `su3_graviton_validation.py`
- Docs: `einstein_recovery.md`, `einstein_from_pdtp.md`
**Status:** Factor 2.36 gap. Shared limitation with ALL induced gravity approaches.
**FCC trigger:** Yes — specific number needed (6pi); graviton validation (Part 76) constrains DOF.
**New findings:** Part 76 Fierz-Pauli + Isaacson may restrict which fields contribute to N_eff.
**RESULTS:** [ ]

#### [ ] B2. Full nonlinear Einstein equation — OPEN (HIGH)

**Problem:** Sakharov gives 1-loop only; full nonlinear GR requires all-loop or exact mechanism.
**Prior research:**
- Part 74: Three routes (Sakharov, Jacobson, frustration); all partial
- Part 76g: O(epsilon^4) SU(3) corrections via f^{abc}; derivative order differs from GR
- Scripts: `einstein_from_pdtp.py`, `su3_graviton_validation.py`
- Docs: `einstein_from_pdtp.md`
**Status:** Linearized Einstein recovered; nonlinear regime open.
**FCC trigger:** Yes — 3 routes attempted, all partial.
**RESULTS:** [ ]

#### [ ] B3. Condensate tetrad structure — OPEN (HIGH)

**Problem:** Need tensor (vierbein) degrees of freedom for full GW polarization.
**Prior research:**
- Part 12: Phi = sqrt(rho_0) e^{i*phi} e^a_mu; Einstein eq derived; frame-dragging recovered
- Part 3b: kappa = -2 is coordinate-dependent (not universal PPN)
- Docs: `tetrad_extension.md`, `hard_problems.md` section 1.10
**Status:** Partial — tetrad postulated in Part 12, not derived from Lagrangian.
Spin connection not yet derived from lattice curvature.
**FCC trigger:** Yes — SU(3) emergent metric (Part 75) may REPLACE the need for
explicit tetrad (g_mu_nu = Tr(dU^dag dU) provides metric directly).
**New findings:** Part 75 metric has 2 TT modes without tetrad. May resolve this gap.
**RESULTS:** [ ]

#### [ ] B4. CP violation absent — OPEN (HIGH)

**Problem:** PDTP Lagrangian is C, P, T invariant. No CP violation = no baryogenesis.
**Prior research:**
- Part 22: Antiparticle = vortex winding -1; CPT verified; CP violation absent
- Part 50: Chirality = Z_2 winding; maximal parity violation automatic
- Part 65: Condensate birefringence; chirality from refractive index
- Scripts: `antimatter_topological_defects.py`, `chirality_parity.py`
- Docs: `antimatter_topological_defects.md`, `chirality_parity_violation.md`
**Status:** PDTP explains WHY parity breaks (Z_2 topology) but not WHICH hand (left vs right).
Sakharov baryogenesis blocked without CP violation.
**FCC trigger:** Yes — two-phase phi_- may break vacuum symmetry.
**RESULTS:** [ ]

#### [ ] B5. Three generations — why exactly 3? — PARTIAL (MEDIUM)

**Problem:** SM has 3 generations; PDTP maps to radial vortex modes but doesn't prove only 3 stable.
**Prior research:**
- Part 51: 3 generations = radial modes n_r = 0, 1, 2; lepton universality DERIVED
- Part 53: Z3 phase spacing = Y-junction 120 deg geometry
- Scripts: `three_generations.py`, `koide_z3.py`
- Docs: `three_generations.md`, `koide_z3_derivation.md`
**Status:** Structure explained (radial modes); need decay width Gamma(n_r >= 3) to prove instability.
**FCC trigger:** Not yet — needs specific calculation of higher-mode lifetimes.
**RESULTS:** [ ]

#### [ ] B6. Spin-statistics connection — PARTIAL (MEDIUM)

**Problem:** Need to derive fermion exclusion from vortex topology, not just assume it.
**Prior research:**
- Part 40: Wilson fermions; Clifford algebra {gamma_mu, gamma_nu} = 2*delta_mu_nu exact
- Part 50: Chirality = Z_2 winding (+1/2 or -1/2); maximal parity violation automatic
- Scripts: `su3_fermion.py`, `chirality_parity.py`
- Docs: `su3_fermion.md`, `chirality_parity_violation.md`
**Status:** Vortex winding number W <-> fermion chirality established. Full topological proof
of spin-statistics theorem (why half-integer spin = Fermi-Dirac) not yet completed.
**FCC trigger:** Not yet — theoretical proof needed, not numerical.
**RESULTS:** [ ]

---

### Category C — Reframe (may point to deeper physics)

Problems where the failure itself is informative — may require physics beyond any current framework.

#### [ ] C1. Hubble tension — 9 orders too small — OPEN (HIGH)

**Problem:** PDTP predicts two mechanisms for H_0 tension; both ~9 orders too small.
**Prior research:**
- Part 16: Dark energy drift + early-time acceleration both fail
- Docs: `hubble_tension_analysis.md`
**Status:** Genuinely open; requires new physics beyond PDTP (and possibly beyond GR).
**FCC trigger:** Yes — re-examine with all findings from Parts 17-76.
**New findings:** Two-phase (Part 61), phi_- dark energy (Part 68-69), Einstein recovery (Parts 72-76).
**RESULTS:** [ ]

#### [ ] C2. Hierarchy problem — why m_P >> m_e — FUNDAMENTAL

**Problem:** The ratio m_P/m_e ~ 10^22 has no explanation in any framework.
**Prior research:**
- Parts 29-35: All substitution chains circular; equivalent to A1
- Part 33: Reframed as "why is vortex winding n so large?"
- Part 35: Dimensional transmutation cannot generate the scale
- Scripts: `brute_force_runner.py`, `orbital_scanner.py`
- Docs: `substitution_chain_analysis.md`, `vortex_winding_derivation.md`
**Status:** = A1 at deepest level. May require physics beyond PDTP/GR/QED entirely.
If solved, cascades to A1, A6, and most other free parameters.
**RESULTS:** [ ]

#### [ ] C3. Why THIS Lagrangian? — FUNDAMENTAL

**Problem:** L = (1/2)(d phi)^2 + g cos(psi - phi) is postulated, not derived from deeper principle.
**Prior research:**
- Part 1: Lagrangian postulated by analogy to Kuramoto model / BEC physics
- Part 37: SU(3) extension is the most general form compatible with gauge symmetry
- Docs: `mathematical_formalization.md`
**Status:** SM Lagrangian is also postulated. But an information-theoretic or topological
argument forcing this specific form would be a major advance.
**FCC trigger:** Not yet — philosophical/foundational, not computational.
**RESULTS:** [ ]

---

### Category D — Negative Results (re-examine with FCC)

These were attempted and failed. Re-examine because new findings (Parts 37-76) may
open paths that didn't exist when the original attempt was made.

#### [ ] D1. Dimensional transmutation — NEGATIVE (Part 35) — RE-EXAMINE

**Original failure:** beta(K) = +K^2/(8pi^2) > 0 (IR free); no scale generation.
**Why re-examine:** SU(3) extension (Parts 37-41) changes the gauge group. SU(3) has
negative beta (asymptotically free). Does the SU(3) PDTP Lagrangian inherit this?
If beta_SU3(K) < 0, dimensional transmutation could generate m_cond dynamically.
**Prior scripts:** `dim_transmutation.py`
**Prior docs:** `dimensional_transmutation.md`
**RESULTS:** [ ]

#### [ ] D2. RG running K_0 -> alpha_EM — NEGATIVE (Part 56) — RE-EXAMINE

**Original failure:** 3 models tested; all run wrong direction or miss by 60%.
**Why re-examine:** SU(3) emergent metric (Part 75) provides a new geometric object.
Running of coupling ON the emergent metric (not flat spacetime) could differ.
Also: graviton validation (Part 76) constrains which modes propagate.
**Prior scripts:** `rg_alpha_em.py`, `coupling_constants.py`
**Prior docs:** `coupling_constants.md`
**RESULTS:** [ ]

#### [ ] D3. Dispersion model — NEGATIVE (Part 57) — RE-EXAMINE

**Original failure:** 4 fatal problems (hard cutoff, no dispersion for massless, wrong
direction for strong force, GUT scale 3 orders off).
**Why re-examine:** Two-phase phi_- has environment-dependent mass (Part 62). This IS
dispersion — different environments = different propagation. The original model assumed
a single scalar; two-phase provides the missing ingredient.
**Prior scripts:** `gravity_em_truth_table.py` (investigation notes)
**Prior docs:** TODO_02.md Ideas section
**RESULTS:** [ ]

#### [ ] D4. Koide circularity for G — NEGATIVE (Part 32) — RE-EXAMINE

**Original failure:** 0/8 non-circular candidates; Koide is structure theorem not scale theorem.
**Why re-examine:** Z3 geometry (Part 53) + Xi_cc baryon (Part 70, 0.02% match) provide
new mass constraints. If M_0 = 313.84 MeV is identified with m_cond_QCD (Part 37: 367 MeV),
the ratio M_0/m_cond_QCD = 0.86 might have topological meaning.
**Prior scripts:** `koide_lattice_analysis.py`, `koide_z3.py`
**Prior docs:** `koide_lattice_analysis.md`, `koide_z3_derivation.md`
**RESULTS:** [ ]

---

### Previously "Open" — Now RESOLVED

These were listed as open in earlier TODOs but have been resolved by later work.
Kept here for traceability.

| Problem | Was Open In | Resolved By | Resolution |
|---------|-------------|-------------|------------|
| PPN kappa = -2 | hard_problems | Parts 3b, 75b | Coordinate-dependent, not universal PPN; auto-Lorenz gauge derived |
| Strong-field 2-DOF deficit | Part 76e | Parts 73-74 | Extra scalar (breathing), not deficit; 2 TT + 1 scalar = 3 DOF |
| phi_- surface mode role | Part 62 | Parts 61-63 | 16/16 re-derivation PASS; reversed Higgs [DERIVED]; hollow shell test proposed |
| RG beta function structure | Part 27 | Part 27 | Beta_0 derived from group theory exactly; initial values remain free |
| K_0 = 1/(4pi) origin | Part 35 | Part 35 | IS the dimensionless natural value; connecting to alpha_EM is problem A2 |
| Scalar charge (double pulsar) | Part 13 | Part 13 | alpha_A = 0 from U(1) symmetry; P_dot_PDTP = P_dot_GR exactly |

---

## FCC Queue — Proposed Order

Each problem gets a Forced Checklist Check against ALL items in `docs/Methodology.md`.
Order: most constrained first (most equations to cross-check).

| Priority | Problem(s) | Strategy | Expected Part # | Status |
|----------|-----------|----------|-----------------|--------|
| 1 | [ ] D1-D4 (negative re-examination) | FCC with new Parts 37-76 findings | 77-80 | PENDING |
| 2 | [ ] B1 (N_eff = 6pi gap) | Contract — DOF counting from graviton sector | 81 | PENDING |
| 3 | [ ] B3 (tetrad from SU(3)) | Contract — does Part 75 metric replace tetrad? | 82 | PENDING |
| 4 | [ ] A1 + C2 (m_cond / hierarchy) | Expand — independent Lagrangian for m_cond | 83 | PENDING |
| 5 | [ ] B4 (CP violation) | Contract — two-phase vacuum symmetry breaking? | 84 | PENDING |
| 6 | [ ] A2 (alpha_EM) | Expand — after D2 re-examination | 85 | PENDING |
| 7 | [ ] B2 (nonlinear Einstein) | Contract — SU(3) structure constants at O(e^4) | 86 | PENDING |
| 8 | [ ] A3 (Lambda) | Reframe — deepest problem, last | 87 | PENDING |
| 9 | [ ] C1 (Hubble tension) | Reframe — after Lambda understood | 88 | PENDING |
| 10 | [ ] B5, B6, A4, A5 (structural) | Mixed — as needed | 89+ | PENDING |

---

## Three Lagrangians — Multiple Forms

Each Lagrangian can be written in equivalent mathematical forms. Different forms
expose different structure — like Maxwell's equations in integral vs differential
vs tensor form. Use all forms when testing; things may "fall out" in one form
that are hidden in another.

| Form | U(1) | Two-Phase | SU(3) |
|------|------|-----------|-------|
| **Lagrangian density** | L = 1/2(d phi)^2 + Sum g_i cos(psi_i - phi) | L = +g cos(psi - phi_b) - g cos(psi - phi_s) | L = K Tr(dU^dag dU) + Sum g_i Re[Tr(Psi_i^dag U)]/3 |
| **Action integral** | S = int [1/2(d phi)^2 + Sum g_i cos(psi_i - phi)] d^4x | S = int g[cos(psi - phi_b) - cos(psi - phi_s)] d^4x | S = int {K Tr(dU^dag dU) + Sum g_i Re[Tr(Psi_i^dag U)]/3} d^4x |
| **Field equation** (EL) | box phi = Sum g_i sin(psi_i - phi) | box phi_+ = g sin(psi - phi_+) cos(phi_-) | K d_mu(U^dag d^mu U) = Sum g_i Psi_i^dag/(6i) + h.c. |
| **Quadratic** (small osc.) | L ~ 1/2(d phi)^2 - 1/2 g(psi - phi)^2 | L ~ 2g(psi - phi_+) phi_- | L ~ K Tr(d chi)^2 + Sum g_i(1 - Tr(chi^2)/6) |
| **Product form** | -- | 2g sin(psi - phi_+) sin(phi_-) | Wilson: -K Re[Tr(U_plaq)]/3 |
| **Emergent metric** | g_mu_nu from acoustic analogy | g_mu_nu from phi_+ sector | g_mu_nu = Tr(d_mu U^dag d_nu U) [DERIVED] |
| **Newton limit** | nabla^2 Phi = 4 pi G rho (Poisson) | nabla^4 Phi + 4g^2 Phi = source (biharmonic) | Same as U(1) + corrections O(chi^2) |
| **Symmetry** | U(1) shift: phi -> phi + c | U(1) x U(1) | SU(3) gauge: U -> V U W^dag |
| **DOF count** | 1 scalar | 2 scalars (phi_+, phi_-) | 8 (N^2 - 1 generators) |

**TODO:** [ ] Output all 3 Lagrangians in each form as a reference sheet for systematic testing.
Each form is a different lens — quadratic for perturbation theory, product for coupling analysis,
field equation for dynamics, emergent metric for GR recovery. Cross-check results across forms.

---

## Next Parts

*(To be filled as each FCC is completed and approved)*

---
