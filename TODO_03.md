# TODO_03 — Active Roadmap

Summary of completed work: [TODO_Summary.md](TODO_Summary.md)
Previous roadmaps: [TODO_01.md](TODO_01.md) (Parts 1–41) | [TODO_02.md](TODO_02.md) (Parts 42–76)

---

## Methodology

Before starting any new problem, follow the Problem-Solving Protocol:

1. Read `docs/Methodology.md` and select relevant checklist items
2. Read `docs/wave_effects_extension.md` — the wave effects checklist
3. Write out a short plan: which strategies to try, in which order, and why
4. Present the plan to the user before starting work
5. Only proceed after the plan is agreed

For deep/fundamental problems where 3+ approaches have failed, escalate to a
**Forced Checklist Check (FCC)** — see CLAUDE.md for full protocol.

**Strategy for free parameters:** See `docs/Methodology.md` section 8 for the full
expand/contract/reframe checklist (including re-examine negatives, two-phase extension,
emergent quantity, and independent Lagrangian strategies).

**Wave effects reference:** See `docs/wave_effects_extension.md` — unified checklist
of all wave types (55), emergent phenomena (25), physical condensate layers (3+boundaries),
and governing variables (28). Use alongside Methodology.md to verify PDTP covers all
known wave physics. Cross-reference with `docs/research/wave_effects_pdtp.md` (Part 28c)
for existing PDTP mappings of effects 1-50.

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
- **Part 77: SU(3) dimensional transmutation — FCC completed (see below)**
- **Part 78: Extremal condensate — 4 remaining paths all NEGATIVE (see below)**
- Scripts: `vortex_winding.py`, `condensate_selfconsist.py`, `dim_transmutation.py`,
  `brute_force_runner.py`, `su3_dim_transmutation.py`, `extremal_condensate.py`
- Docs: `vortex_winding_derivation.md`, `condensate_selfconsist.md`,
  `dimensional_transmutation.md`, `su3_dim_transmutation.md`, `extremal_condensate.md`
**Status:** All paths exhausted (11 independent, Parts 29-35, 77-78). m_cond = m_P confirmed as free parameter.
**FCC trigger:** COMPLETED (Parts 77-78). Full Methodology.md checklist evaluated.

**FCC Results (Part 77, 2026-03-22):**
Seven previously untried Methodology.md items investigated:

| # | Item | Result |
|---|------|--------|
| 1 | SU(3) dimensional transmutation (6.8) | **NEGATIVE** — alpha_s = 2.0 (strong coupling); exp(-pi/11) = 0.75 (no hierarchy) |
| 2 | BCS gap equation (4.1/4.3) | **NEGATIVE** — UV cutoff = m_cond (circular) |
| 3 | Proof by contradiction (6.2) | **NEGATIVE** — framework consistent for ANY m_cond |
| 4 | Stability bounds / invert problem (1.3) | **POSITIVE** — m_cond <= O(m_P) from BH consistency; m_P SATURATES bound |
| 5 | N_eff overcounting (3.5) | Not resolved (needs separate investigation) |
| 6 | Conserved quantity (6.3) | Not identified |
| 7 | Independent Lagrangian (8.7) | Not yet attempted |

**New positive findings:**
- m_cond_QCD = 0.236 GeV from measured string tension (reverse chain, G-free) [PDTP Original]
- m_cond = m_P saturates BH consistency bound (extremal condensate) [PDTP Original]
- Extremal condensate hypothesis: deeper principle forces m_cond to max [SPECULATIVE]

**Remaining untried paths (Part 78 — all investigated, all NEGATIVE):**
- [x] Entropy maximization / holographic bound — S_Bek = 2*pi*k_B (m_cond-free); S_holo = pi (tautology); G = dual of eta
- [x] Dvali N-species bound — N = 1 (one condensate field); consistent, not a derivation
- [x] Independent Lagrangian for m_cond — VEV rho_0 = 3/pi (structure, not scale)
- [x] Topological invariant — S_inst = pi exactly; exp(-pi) = 0.0432; 10^15x QCD

**RESULTS (Parts 77-78 combined):** SU(3) AF fails (strong coupling). BCS circular.
m_P not unique. BH bound saturated (m_cond <= m_P). QCD sector: m_cond_QCD = 0.236 GeV.
Part 78: all 4 remaining paths NEGATIVE. 9 dimensionless quantities determined by K_NAT.
Fundamental barrier: PDTP determines dimensionless structure, not dimensional scale.
Sudoku 8/8 (Part 77) + 9/9 (Part 78) pass. **Status: CONFIRMED FREE PARAMETER — CLOSED.**

#### [ ] A2. alpha_EM = 1/137.036 not derived — OPEN (CONFIRMED FREE PARAMETER)

**Problem:** EM coupling constant value has no derivation in SM or PDTP.
**Prior research:**
- Part 5: alpha = Z_0/(2R_K) is exact structural identity (circular, contains h and e)
- Part 27: Beta functions derived from group theory; initial values alpha_EM, alpha_S free
- Part 55: Two-channel model gives alpha ~ K_0^2 ~ 1/158 (13.2% off)
- Part 56: RG running K_0 -> alpha_EM FAILED (wrong direction, 3 models tested)
- Part 57: Dispersion model FAILED (4 fatal problems)
- **Part 79: FCC completed — 5 paths all NEGATIVE (see below)**
- Scripts: `coupling_constants.py`, `rg_alpha_em.py`, `alpha_em_fcc.py`
- Docs: `coupling_constants.md`, `fine_structure_derivation.md`, `alpha_em_fcc.md`
**Status:** All paths exhausted (8 approaches, Parts 52, 55-57, 79). alpha_EM confirmed as free parameter.
**FCC trigger:** COMPLETED (Part 79). Full Methodology.md checklist evaluated.

**FCC Results (Part 79, 2026-03-22):**
Five untried Methodology.md paths investigated:

| # | Path | Result |
|---|------|--------|
| 1 | SU(3)-U(1) coupling (item 8.4) | **NEGATIVE** — SU(3) AF gives Lambda_QCD, not alpha_GUT; K_NAT^2 RG -> 1/231 (not 137) |
| 2 | Emergent impedance from SU(3) metric (item 8.6) | **NEGATIVE** — metric (spin-2) and gauge (spin-1) independent DOF |
| 3 | Topological winding in EM sector (items 6.5, 8.2) | **NEGATIVE** — Dirac constrains e*g_m, not e alone; Chern = integers; alpha irrational |
| 4 | Coupling ratios (item 7.4) | **NEGATIVE** — ratios depend on alpha_GUT and M_GUT (both free) |
| 5 | Two-phase extension (item 8.5) | **NEGATIVE** — phi_- is spin-0 (not photon); same K_NAT, no new number |

**New positive findings:**
- alpha_EM(M_P) = 1/64 needed for 1/137 at m_e via QED RG [Eq. 79.1]
- Impedance duality: g_m/e = 1/(2*alpha) = R_K/Z_0 = 68.5 [Eq. 79.5]
- sin^2(theta_W) = 3/8 at GUT scale [DERIVED, group theory, Eq. 79.7]
- Wyler's formula: 0.6 ppm accuracy from O(4,2) conformal geometry [Eq. 79.6]

**RESULTS:** All 5 FCC paths NEGATIVE. alpha_EM confirmed as free parameter
after 8 independent approaches. Same barrier as m_cond (Part 78): PDTP determines
dimensionless structure, not coupling values. Sudoku 9/10 pass.
Most promising future: Wyler's conformal geometry (O(4,2)). **Status: CONFIRMED FREE PARAMETER — CLOSED.**

#### [x] A3. Cosmological constant Lambda — CONFIRMED FREE PARAMETER — CLOSED (Part 87)

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
**RESULTS (Part 87, 2026-03-29):**
- Approach A (Induced Lambda): NEGATIVE -- N_bose=8 gluons; no SUSY cancellation; Planck scale
- Approach B (Entropy-corrected): rho_vac_PDTP = rho_Planck/(4*ln(2))^2 [PDTP Original]
  Still ~10^121 x rho_Lambda -- hierarchy not closed
- Approach C (phi_- reframe): Lambda = g*phi_-_vac^2 [PDTP Original, REFRAME]
  phi_-_vac = sqrt(rho_Lambda/g_phys) ~ 10^-70 rad [tiny but consistent]
  Lambda is the large-scale phi_- phase offset of the condensate
  Lambda is DYNAMIC in PDTP: phi_-_vac(t) evolves -> w(z) != -1 [SPECULATIVE, PDTP Original]
  DESI 2024 w_0~-0.7 is consistent with phi_- quintessence [SPECULATIVE]
- 12/12 Sudoku PASS
- Scripts: `cosmo_constant_a3.py` (Phase 57); Docs: `cosmo_constant_a3.md`
**Status change:** OPEN (CRITICAL) --> CONFIRMED FREE PARAMETER -- CLOSED
**Same as A1 (m_cond) and A2 (alpha_EM): PDTP gives physical meaning but not value.**

#### [x] A4. Koide theta_0 = 2/9 — CONFIRMED FREE PARAMETER — CLOSED (Part 91)

**Problem:** Lepton mass angular parameter has no SU(3) derivation.
**Prior research:**
- Part 4: Koide Q = 2/3 <=> delta = sqrt(2); Z_3 phase geometry
- Part 32: 0/8 non-circular candidates; Koide = structure theorem, not scale theorem
- Part 53: Z3 geometry + equal partition derives delta = sqrt(2); theta_0 remains free
- Part 82: D4 re-examine; 0/5 new constraints; theta_0 ~ theta_C excluded by m_e precision
- Part 91: A4 FCC; SU(5) NEGATIVE; reverse scan NEGATIVE; cross-sector pattern SPECULATIVE
- Scripts: `koide_z3.py`, `koide_lattice_analysis.py`, `koide_reexamine.py`, `koide_theta0.py`
- Docs: `koide_z3_derivation.md`, `koide_lattice_analysis.md`, `koide_reexamine.md`, `koide_theta0.md`
**RESULTS (Part 91, 2026-04-03):**
- Cross-sector Brannen: theta_0(lep)=2/9, theta_0(up)~2/27, theta_0(dn)~1/9
  Pattern 2/3^n is suggestive but unconfirmed (quark mass uncertainty ~5%)
  Q=2/3 holds ONLY for leptons (Z3-neutral); quarks (Z3-charged) give Q_up=0.849, Q_dn=0.732 [DERIVED]
- SU(5) GUT center: Z5 phases all >20% off theta_0 [NEGATIVE]
- Reverse scan: closest PDTP angle 4.5% off (C2_fund/2pi) [NEGATIVE]
- NEW RESULT: Neutrino mass prediction from Koide + oscillation data [PDTP Original]
  Sum(m_nu) = 58.6 meV (NO), 59.4 meV (IO) -- testable by CMB-S4/Euclid (~2030)
  m_nu1 < 1 meV (nearly massless); lightest nu in SIGNED Brannen regime (Q_nu=0.52 not 2/3)
- 12/12 Sudoku PASS
**Status change:** OPEN (MEDIUM) --> CONFIRMED FREE PARAMETER -- CLOSED
**Same pattern as A1, A2, A3: PDTP gives structure (delta=sqrt(2), Q=2/3, 120-deg spacing)
but not the value theta_0. The neutrino mass prediction is the new falsifiable output.**

#### [x] A5. sin^2(theta_W) and v_EW = 246 GeV — PARTIAL DERIVATION + FREE PARAM — CLOSED (Part 92)

**Problem:** Weak mixing angle and EW condensate scale are free parameters.
**Prior research:**
- Part 27: Structure derived (ratio of condensate stiffnesses); value not derived
- Part 49: W/Z boson masses structural (m_W = g_2*v/2, m_Z = m_W/cos(theta_W))
- Part 52: coupling constants running derived (beta functions); values free
- Docs: `coupling_constants.md`, `wz_boson_masses.md`
**Status:** FCC complete (Part 92). Two distinct results.
**RESULTS:**
- sin^2(theta_W)(M_GUT) = 3/8: DERIVED from SU(5) group normalization [EXACT, group theory]
  - g_1 = sqrt(5/3)*g_Y [SU(5) normalization]; at GUT g_1=g_2=g_GUT; => sin2w = 3/8 [PDTP Original]
- sin^2(theta_W)(m_Z) ~ 0.210: PARTIAL from one-loop RG (9% off measured 0.231)
  - Gap = well-known non-SUSY SU(5) failure; SUSY-SU(5) gives 0.232 (closes gap)
- SM non-unification confirmed: alpha_1(M_GUT) / alpha_GUT ~ 1.30 ≠ 1 in SM [NEGATIVE for unification]
- v = 246.22 GeV: CONFIRMED FREE PARAMETER (C3 condensate density; EW hierarchy v/m_P ~ 2e-17)
  - Same pattern as A1 (m_cond), A2 (alpha_EM), A3 (Lambda): free condensate scale
- Topological scan: no PDTP topology within 4% of sin2w(m_Z) = 0.231 [NEGATIVE]
- 12/12 Sudoku PASS
**UNIQUE in A-series: sin^2(theta_W) has structural GROUP THEORY origin (SU(5) fixes it at M_GUT).**
**Unlike A1-A4 (fully free), sin^2(theta_W) is PARTIALLY DERIVED. v = 246 GeV remains free.**
**Status change:** OPEN (MEDIUM) --> PARTIAL + FREE -- CLOSED

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

#### [ ] A7. Speed of light c — is it emergent? — OPEN (HIGH)

**Problem:** c is treated as a fundamental constant in PDTP, but it may be emergent from the
condensate lattice. If the spacetime condensate has a lattice spacing l_0 and a natural
oscillation frequency omega_0, then c = omega_0 x l_0 — same as how sound speed in a crystal
emerges from frequency x lattice spacing. Under this view c is NOT fundamental; it is the
phonon dispersion speed of the spacetime condensate, which could in principle vary.

**Key questions:**
1. Does c = omega_0 x l_0 reduce to c_s = c (Part 34) or is it an independent statement?
2. If l_0 = l_P and omega_0 = c/l_P (Planck frequency), is this circular or confirmatory?
3. If the condensate has a background oscillation phi = phi_0 cos(omega_0 t), the coupling
   is renormalized: g_eff = g x J_0(phi_0) (Bessel function). What sets phi_0?
4. Could c vary locally? (Variable Speed of Light theories — VSL). If the condensate
   density n or lattice spacing l_0 varies (near black holes, in early universe), c varies.
5. Is there a dispersion relation for c itself? c(omega) — frequency-dependent speed of light?
6. Connection to dark energy: if c changes cosmologically, H_0 and the Hubble tension may shift.
7. Why do photons travel at c? In PDTP, what IS a photon and why does it move at c_s?
8. Slow-light experiments: Lene Hau (1999) slowed light to 17 m/s in a BEC, then stopped it
   completely. What does this mean for PDTP? If c = c_s of the spacetime condensate, then
   slowing light in an atomic BEC is exactly analogous to what would happen if the spacetime
   condensate density were locally reduced. Does the Hau mechanism have a PDTP counterpart?

**Prior research:**
- Part 34 (condensate_selfconsist.py): c_s = c EXACTLY derived — sound speed of condensate = c
- Part 29 (orbital_scanner.py): c/l_P = Planck frequency = omega_gap_C1
- Part 89 (condensate_layer_optics.py): n_eff formula uses c as fixed; what if c = c(layer)?
- CLAUDE.md key equation: c_s = sqrt(g_GP x n / m_cond) = c [always, any m_cond]

**Experimental analog — Slow Light (Hau 1999):**
Lene Hau slowed photons to 17 m/s (later 0 m/s) by passing them through a BEC of sodium
atoms cooled near absolute zero. The mechanism: Electromagnetically Induced Transparency (EIT)
creates a coupled photon-matter quasiparticle (dark-state polariton) whose group velocity
is c_s of the atomic BEC, which can be made arbitrarily small by tuning n and g_GP.
This is the EXACT same formula as Part 34: c_s = sqrt(g_GP x n / m_atom).
PDTP interpretation: normal vacuum is a BEC at maximum density (n = n_Planck, c_s = c).
Slow light = reduced local condensate density = same physics, different condensate.
Key check: does PDTP predict a mechanism to locally reduce n of the spacetime condensate?
If yes: this is a route to local c reduction — directly relevant to Goal 2 (phase decoupling).
If light can be stopped in a lab BEC by reducing c_s to zero, can spacetime c be similarly
reduced in a region of controlled condensate density? What energy/mechanism is required?

**Why photons travel at c — PDTP answer to derive:**
In standard QED, c is postulated (Lorentz invariance). In PDTP the question becomes:
what IS a photon in the condensate picture? Candidates:
(a) Photon = massless phonon of the C1 condensate (gravity sector) — travels at c_s = c
(b) Photon = massless Goldstone boson of the U(1) phase symmetry — dispersion ω = ck
(c) Photon = transverse wave in C3 condensate (EW sector, spin-1) — group velocity = c
Option (a) is most natural: Part 34 shows c_s = c for C1; massless phonons travel at c_s.
This gives a first-principles reason: photons travel at c BECAUSE they are the massless
excitations of the same condensate whose sound speed is c. Not a postulate — a result.
Cross-check: massive particles (matter) travel at v < c because they are VORTEX excitations
(Part 33), not phonons. Phonons are massless; vortices have rest energy m_cond c^2.

**Approach (in order):**
1. Reframe Part 34 result: c_s = c is NOT a coincidence — it IS the definition of c in PDTP
2. Show c = omega_0 x l_0 in condensate notation; identify omega_0 and l_0 explicitly
3. Derive photon = massless phonon of C1; show ω = ck follows from condensate dispersion
4. Map Hau EIT mechanism onto PDTP: c_s formula identical; identify PDTP analog of coupling
5. Derive what happens to c_s if n or l_0 changes (early universe, near singularity)
6. Bessel renormalization: compute g_eff = g x J_0(phi_0); what observable does phi_0 set?
7. VSL prediction: does c(z) at high redshift differ from c_0? Consistent with CMB/BBN?
8. Sudoku: 10+ tests substituting c -> c(n, l_0) into known equations; check contradictions
9. SM compatibility: variable c must not break gauge invariance or alter particle masses
10. Two-phase check: does c_s = c hold separately for phi_+ and phi_- modes?

**Expected outcome:** c is the condensate phonon speed (c_s = c, Part 34) — this is the
derivation, not a coincidence. The Planck frequency sets omega_0; l_P sets l_0; c emerges.
If correct: c is to PDTP as c_s is to BEC — a derived material property, not a postulate.
This would make G, Lambda, AND c all emergent from the same condensate (m_cond, n, l_0).
Photons travel at c because they are the massless phonons of that condensate.
Massive particles travel at v < c because they are vortex excitations with rest energy.

**VSL implication (SPECULATIVE):** Near a black hole or in the early universe, if n varies,
c varies. May connect to Mach-effect theories and UAP phase-decoupling (Goal 2).
Slow-light analog suggests: if spacetime condensate density can be locally reduced
(e.g. by driving phi_- to large values, as in Part 71 Leidenfrost screening), c_local < c.
This is a concrete mechanism for phase decoupling (Goal 2) that doesn't require exotic energy.

**Status:** Not yet investigated. Partially hinted at in Part 34 (c_s = c) and Part 89 (n_eff).
**FCC trigger:** Not yet — first pass needed.
**Linked problems:** A1 (m_cond), A6 (g), C3 (why this Lagrangian)
**RESULTS:** [ ]

---

### Category B — Structural Gaps (derive from within PDTP)

These are missing derivations where the answer should come from the framework.

#### [x] B1. N_eff = 6pi gap in Sakharov formula — PARTIAL (Part 83)

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
**RESULTS (Part 83):**
- G_ind = (6pi/N_eff) * hbar*c/m_cond^2; with N_s=8: G_ind/G = 3pi/4 = 2.356 [VERIFIED]
- SM signed helicity sum = -62 (fermion-dominated; known issue, not PDTP-specific)
- PDTP N_eff range: minimal=8, two-phase=10, with matter=34; target 6pi~18.85 between 10-34
- Near-miss: 8 + (4/3)*8 = 18.67 (Casimir enhancement, 1% off)
- 6pi is geometric (4D heat kernel), not field-content; non-integer = no exact field content
- Gap is UNIVERSAL — shared by all induced gravity approaches
- Open: which matter species contribute how much? Lattice regularization may shift prefactor
- **NEW CANDIDATE (Part 84 observation):** Y-junction rotational modes — the baryon
  Y-vertex has 2 bosonic rotational DOF not counted in the 8-gluon N_eff. Bosonic =
  positive sign (right direction). A fractional coupling could provide the missing 0.18
  needed to close 18.67 → 18.85. Also: flux tube transverse vibrations (check double-counting
  with gluons). Quark spin (fermions) contributes NEGATIVELY — wrong sign, do not include.
- Script: `neff_sakharov.py` (Phase 53); Doc: `neff_sakharov.md`; Sudoku: 10/10 PASS

#### [x] B2. Full nonlinear Einstein equation — PARTIALLY RESOLVED (Part 86)

**Problem:** Sakharov gives 1-loop only; full nonlinear GR requires all-loop or exact mechanism.
**Prior research:**
- Part 74: Three routes (Sakharov, Jacobson, frustration); all partial
- Part 76g: O(epsilon^4) SU(3) corrections via f^{abc}; derivative order differs from GR
- Scripts: `einstein_from_pdtp.py`, `su3_graviton_validation.py`
- Docs: `einstein_from_pdtp.md`
**Status:** Linearized Einstein recovered; nonlinear regime open.
**FCC trigger:** Yes — 3 routes attempted, all partial.
**RESULTS (Part 86, 2026-03-29):**
- Strategy 1 (O(eps^4) sigma model): NEGATIVE — chi^2*(d chi)^2 ≠ (d h)^2 of GR; sigma
  model field eq d_mu(U_dag d^mu U)=0 is structurally different from G_mu_nu=8*pi*G T_mu_nu
- Strategy 2 (PDTP microscopic entropy): S_PDTP = k_B*ln(2)*A/a_0^2 [PDTP Original, DERIVED]
  Entropy-area law holds if a_0 = 2*sqrt(ln(2))*l_P = 1.665*l_P [PDTP Original]
- Strategy 3 (Jacobson + S_PDTP): PARTIAL — full GR via Clausius at corrected a_0 = 1.665*l_P
- Strategy 4 (Biharmonic Part 61): CONSISTENT — nabla^4+4g^2 reduces to Newtonian at r >> l_P
- Gap convergence: entropy gap 4*ln(2)=2.773 and Sakharov gap 3*pi/4=2.356 are both ~2-3
  independently, pointing at same microstate counting uncertainty [PDTP Original]
- 12/12 Sudoku PASS
- Scripts: `nonlinear_einstein.py` (Phase 56); Docs: `nonlinear_einstein.md`
**Remaining open:** WHY a_0 = 1.665 l_P (not l_P)? Closing this = closing B1 (N_eff) simultaneously.

#### [x] B3. Condensate tetrad structure — PARTIALLY RESOLVED (Part 84)

**Problem:** Need tensor (vierbein) degrees of freedom for full GW polarization.
**Prior research:**
- Part 12: Phi = sqrt(rho_0) e^{i*phi} e^a_mu; Einstein eq derived; frame-dragging recovered
- Part 3b: kappa = -2 is coordinate-dependent (not universal PPN)
- Docs: `tetrad_extension.md`, `hard_problems.md` section 1.10
**Resolution (Part 84):** SU(3) emergent metric (Part 75) REPLACES explicit tetrad
for linearized/weak-field gravity. Head-to-head: Part 75 wins 6, Part 12 wins 4, 7 ties.
- 2 TT modes DERIVED (not postulated) from 8 gluon fields
- Lorenz gauge automatic, Fierz-Pauli emergent, pure gauge escaped
- Two-phase compatible (all 4 checks pass)
- 12/12 Sudoku PASS
**Remaining gaps:** Strong-field (2-DOF deficit: 8 fields vs 10 metric), N_eff gap (B1).
Part 12 needed ONLY for black hole interiors / mergers / extreme curvature.
**Status change:** HIGH → LOW (residual gap is non-blocking for observable physics).
**Docs:** `tetrad_resolution.md`; Script: Phase 54 `tetrad_resolution.py`
**RESULTS:** [PARTIALLY RESOLVED — SU(3) replaces tetrad for linearized gravity]

#### [x] B4. CP violation — PARTIALLY RESOLVED (Part 85)

**Problem:** PDTP Lagrangian is C, P, T invariant. No CP violation = no baryogenesis.
**Prior research:**
- Part 22: Antiparticle = vortex winding -1; CPT verified; CP violation absent
- Part 50: Chirality = Z_2 winding; maximal parity violation automatic
- Part 65: Condensate birefringence; chirality from refractive index
- Scripts: `antimatter_topological_defects.py`, `chirality_parity.py`
- Docs: `antimatter_topological_defects.md`, `chirality_parity_violation.md`
**Resolution (Part 85):** Three mechanisms analyzed. L5 (two-phase + sin(2*phi_-))
provides REAL, non-removable CP violation:
- L4 (U(1)+sin): FAKE — absorbed by field redefinition cos+sin=shifted cos [DERIVED]
- L5 (two-phase + eps*sin(2*phi_-)): REAL — 3-field system, sin invariant under redefinitions
- L6 (SU(3) + Im[Tr]): REAL — IS the QCD theta-term [IDENTIFIED]
- Vacuum shifts: delta = -eps/g (small eps approx) [PDTP Original]
- Sakharov condition 2 (CP): V(delta) != V(-delta) when eps != 0 [DERIVED]
- Baryon asymmetry: eps/g ~ 3e-7 gives eta ~ 6e-10 [ESTIMATED]
- Two-phase tests: all preserved at O(eps^2) corrections [CONSISTENT]
- 12/12 Sudoku PASS
**Remaining open:** B violation rate (vortex nucleation), non-equilibrium transition,
WHY eps << g (PDTP version of Strong CP Problem), CKM phase from SU(3).
**Docs:** `cp_violation.md`; Script: Phase 55 `cp_violation.py`
**RESULTS:** [PARTIALLY RESOLVED — CP mechanism identified; Sakharov cond. 2 derived]

**Preliminary investigation (2026-03-22, quick check):**
Adding a -sin term to each Lagrangian as CP-violating extension:

| # | Name | Lagrangian | CP violation? |
|---|------|-----------|---------------|
| L4 | U(1) - sin | +g cos(psi-phi) - eps sin(psi-phi) | FAKE — removable by field redefinition (trig identity: cos+sin = shifted cos) |
| L5 | Two-Phase - sin | L2 - eps sin(phi_b - phi_s) | REAL — sin(2*phi_-) tilts vacuum, not removable |
| L6 | SU(3) - sin | g Re[Tr(Psi^dag U)]/3 - eps Im[Tr(Psi^dag U)]/3 | REAL — IS the QCD theta-term |

Key findings from quick check:
- U(1) CANNOT break CP (sin absorbed by phase redefinition phi' = phi + delta)
- Two-Phase CAN: eps sin(2*phi_-) shifts vacuum from pi/2 to pi/2 - delta → matter preferred
- SU(3) CAN: eps Im[Tr] = QCD theta-term; experiment bounds theta < 10^-10 (Strong CP Problem)
- The Strong CP Problem (why theta ~ 0) lands naturally in PDTP's SU(3) extension

**Refined understanding (CP mechanism):**
- **What creates CP violation:** sin / imaginary terms (these are CP-odd under CP transformation)
- **What the sign does:** +eps vs -eps selects the DIRECTION of asymmetry (matter vs antimatter)
- **cos terms shape the potential** (symmetric wells); **sin terms tilt the potential** (break symmetry)
- The sign does NOT create CP violation — it picks which vacuum wins
- Under CP: sin(theta) -> -sin(theta), cos(theta) -> cos(theta); this is the actual mechanism
- Practical approach: simulate BOTH +eps and -eps, measure matter vs antimatter production,
  pick the sign matching observation (matter-dominated universe)

**TODO for full investigation:**
- [ ] Define CP transformation rules for psi, phi_b, phi_s explicitly
- [ ] Verify L4 is removable (SymPy: cos + sin = shifted cos)
- [ ] Derive full potential V(phi_-) with -eps sin(2*phi_-) term
- [ ] Find shifted vacuum: phi_- = pi/2 - delta, solve for delta(eps)
- [ ] Check: does shifted vacuum break Sakharov condition 2 (CP)?
- [ ] Compute matter vs antimatter production rate asymmetry
- [ ] For SU(3): verify -eps Im[Tr(Psi^dag U)]/3 matches QCD theta-term on lattice
- [ ] Check experimental constraint: what eps (= theta) gives observed baryon asymmetry?
- [ ] Sudoku consistency: do L5/L6 still pass all 16 two-phase re-derivation tests?
- [ ] If theta ~ 0 in SU(3), can PDTP explain WHY? (axion mechanism? topological cancellation?)
- [ ] Simulate L5 with BOTH +eps and -eps; determine which sign gives matter dominance
- [ ] Estimate baryon asymmetry: does eps produce observed ratio eta ~ 6x10^-10?

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

#### [ ] B7. Condensate layer optics — TIR, dark matter, evanescent waves — OPEN (HIGH)

**Problem:** The three condensate layers (C1 grav, C2 QCD, C3 EW) are defined in
`wave_effects_extension.md` Section 3a, but the WAVE PHYSICS at the boundaries has
never been derived: no refractive indices, no Snell's law, no critical angles, no
evanescent penetration depths. The boundaries are where the most interesting physics
happens — confinement, dark matter, and cross-layer coupling all live here.

**Motivation (2026-03-29):** Interference fringe image (8.2.2.2 water waves) shows that
two condensate "poles" at a boundary naturally produce constructive/destructive zones.
The destructive zones may be where dark-matter-like excitations reside — trapped by
total internal reflection (TIR) at B1 rather than being separate particle species.

**Key questions:**
1. What is n_eff(omega) for each condensate layer?
   - Massless phonons (C1 grav): n_eff = 1 everywhere?
   - Massive modes (C2 QCD gap ~ 200 MeV, C3 EW gap ~ 80 GeV): n_eff < 1 (plasma-like)?
2. What is the critical angle at B1 (grav/QCD) and B2 (QCD/EW)?
   - sin(theta_c) = n_lower/n_upper at each boundary
3. Which excitations are totally internally reflected at B1?
   - Low-energy C1 modes (E << Lambda_QCD): cannot propagate in C2 → dark matter candidates?
   - Quarks (SU(3) winding 1/3): incompatible modes → confinement alternative explanation?
4. What is the evanescent penetration depth at each boundary?
   - lambda_evan ~ hbar/(Delta_m * c) — connection to virtual photon exchange range?
5. Does the two-source interference fringe spacing predict any observable scale?
   - Dark matter clustering? BAO scale? Void sizes?

**Connection to existing work:**
- Part 28b: spacetime birefringence (E24) — PDTP already predicts n depends on polarization
- Part 65: condensate birefringence from chirality — two polarizations see different n
- Part 67: White comparison; healing length xi ~ l_P/sqrt(2) as penetration depth candidate
- Section 3a wave_effects_extension.md: three layers + boundaries defined (conceptual only)
- E2 (wave_effects_extension.md): TIR listed as emergent effect — never computed for PDTP

**FCC trigger:** YES — full Methodology.md check + full wave_effects_extension.md cross-check.
**Wave Effects Check:** YES — specifically items 50 (evanescent), 52 (TIR), E2, E3, E10
(Anderson localization), E16 (horizon as TIR — already identified, now extend to all boundaries).
**Status:** First quantitative investigation complete (Part 89).
**Script:** `simulations/solver/condensate_layer_optics.py` (Phase 59)
**Docs:** `docs/research/condensate_layer_optics.md`
**Sudoku:** 12/12 PASS
**RESULTS (Part 89, 2026-03-29):**
- n_eff hierarchy: n_C1=1 > n_C2(E) > n_C3(E) for E < m_W*c^2 [DERIVED]
- lambda_evan(B1) = hbar/(Lambda_QCD*c) = 0.987 fm [QCD confinement scale, DERIVED]
- lambda_evan(B2) = hbar/(m_W*c) = 0.00245 fm [weak force range, DERIVED]
- Force ranges = evanescent depths at layer boundaries [PDTP Original, DERIVED]
- Dark matter as mode-mismatch U(1) vortex: gravity-only, Bullet Cluster safe [SPECULATIVE]
- Critical angle at B1 (proton) = 77.7 deg [DERIVED]
- Two dual origins of quark confinement: string tension (Part 38) + evanescent depth (Part 89) [PDTP Original]
**Full FCC + wave effects check:** Still pending (Priority 12).

---

### Category C — Reframe (may point to deeper physics)

Problems where the failure itself is informative — may require physics beyond any current framework.

#### [x] C1. Hubble tension — NEGATIVE (confirmed) — CLOSED (Part 88)

**Problem:** PDTP predicts two mechanisms for H_0 tension; both ~9 orders too small.
**Prior research:**
- Part 16: Dark energy drift + early-time acceleration both fail
- Docs: `hubble_tension_analysis.md`
**FCC Result (Part 88):** All 5 mechanisms tested. All NEGATIVE:
- phi_- EDE: frozen (w=-1, m=0 in vacuum) AND 9.4 orders too weak
- phi_- -> G variation: G is constant; phi_- not coupled to m_cond
- Biharmonic correction: 118 orders too small (sub-Planck only)
**New PDTP Original results:**
- phi_-_vac_EDE = 5.41e-66 rad needed (4.7 orders > observed)
- Missing physics identified: phi_-^4 quartic term (positive, higher-order correction)
- Falsifiable: DESI w(z) distinguishes systematics vs real physics
**Script:** `simulations/solver/hubble_tension_c1.py` (Phase 58)
**Docs:** `docs/research/hubble_tension_c1.md`
**Sudoku:** 12/12 PASS
**RESULTS:** NEGATIVE (confirmed) — CLOSED

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

#### [x] D1. Dimensional transmutation — RE-EXAMINED (Part 77) — STILL NEGATIVE

**Original failure:** beta(K) = +K^2/(8pi^2) > 0 (IR free); no scale generation.
**Re-examination:** Part 77 tested SU(3) AF: alpha_s(PDTP) = 2.0 (strong coupling);
exp(-pi/11) = 0.75 (no hierarchy). SU(3) IS AF but PDTP K_NAT is at strong coupling.
**RESULTS:** NEGATIVE confirmed. SU(3) AF does not generate m_cond. See `su3_dim_transmutation.md`.

#### [x] D2. RG running K_0 -> alpha_EM — RE-EXAMINED (Part 79) — STILL NEGATIVE

**Original failure:** 3 models tested; all run wrong direction or miss by 60%.
**Re-examination:** Part 79 Path 1 tested with SU(3) findings: K_NAT^2 at M_P, QED RG
gives 1/alpha = 231 (not 137). Backward solve: alpha(M_P) = 1/64 needed.
SU(3) metric (spin-2) independent of gauge field (spin-1).
**RESULTS:** NEGATIVE confirmed. See `alpha_em_fcc.md` Path 1.

#### [x] D3. Dispersion model — NEGATIVE (Part 57) — RE-EXAMINED (Part 80) — STILL NEGATIVE

**Original failure:** 4 fatal problems (hard cutoff, no dispersion for massless, wrong
direction for strong force, GUT scale 3 orders off).
**Why re-examine:** Two-phase phi_- has environment-dependent mass (Part 62). This IS
dispersion — different environments = different propagation.
**Re-examination (Part 80):** 4 checks against 4 fatal problems:
- F1 (hard cutoff): IMPROVED — gap varies with Phi, smooth in space. But still step in energy.
- F2 (massless modes): UNCHANGED — phi_- (spin-0) does not couple to spin-1 carriers.
- F3 (AF direction): UNCHANGED — AF is quantum loops; dispersion is classical.
- F4 (GUT scale): REFRAMED — gap now ~MeV at BH (was E_Planck). Direction reversed, neither matches GUT.
**Root cause:** coupling running = quantum (vacuum polarization); dispersion = classical. Unbridgeable.
**RESULTS:** NEGATIVE CONFIRMED. 10/10 Sudoku. See `dispersion_two_phase.md`.

#### [x] D4. Koide circularity for G — NEGATIVE (Part 32) — RE-EXAMINED (Part 82) — STILL NEGATIVE

**Original failure:** 0/8 non-circular candidates; Koide is structure theorem not scale theorem.
**Why re-examine:** Z3 geometry (Part 53) + Xi_cc baryon (Part 70, 0.02% match) provide
new mass constraints. If M_0 = 313.84 MeV is identified with m_cond_QCD (Part 37: 367 MeV),
the ratio M_0/m_cond_QCD = 0.86 might have topological meaning.
**Re-examination (Part 82):** 4 new findings checked (two-phase, emergent metric, Sakharov,
Xi_cc), all NEGATIVE for constraining M_0. M_0/m_cond_QCD ratio does NOT match clean SU(3)
group number. Yukawa screening from reversed Higgs gives r ~ 10^-18 m (too short, consistent).
theta_0 ~ theta_C at 2.2% (excluded by m_e precision). M_0 ~ m_p/3 at 0.3% is structural.
**Prior scripts:** `koide_lattice_analysis.py`, `koide_z3.py`, `koide_reexamine.py`
**Prior docs:** `koide_lattice_analysis.md`, `koide_z3_derivation.md`, `koide_reexamine.md`
**RESULTS:** STILL NEGATIVE. Koide = structure, not scale. 7/10 Sudoku. See Part 82.

---

### Category E — Living Reference Documents (ongoing, not problems)

These are documents that must be created and kept continuously updated as new
Parts are completed. They are not "problems" to solve — they are running records.

#### [ ] E1. dark_matter_energy.md — Dark Matter and Dark Energy Living Reference

**Purpose:** Single source of truth for ALL dark matter (DM) and dark energy (DE)
findings in PDTP, alongside current science. Updated after every relevant Part.

**Why it's needed:**
- DM and DE appear in many separate Parts (22, 25, 28b, 29, 33, 54, 68, 69, 87, 88, 89...)
- No single document currently summarises what PDTP says about either
- Future Parts (B7 FCC, dark matter FCC) need this as a baseline reference
- Allows direct comparison: current science observation vs PDTP prediction/mechanism

**Contents to compile (first pass):**
- Section 1: Dark matter — observed properties (Planck 2020, rotation curves, CMB, lensing)
- Section 2: Dark matter — PDTP candidates (all Parts surveyed):
  - Mode-mismatch U(1)-only vortex in C1 (Part 89) [SPECULATIVE]
  - TIR confinement at B1 for sub-gap excitations (Part 89) [SPECULATIVE]
  - Antimatter as topological defects — does not explain DM (Part 22) [NEGATIVE]
  - Vortex winding candidates from Part 33
- Section 3: Dark energy — observed properties (w(z), DESI 2024, acceleration)
- Section 4: Dark energy — PDTP mechanisms (all Parts surveyed):
  - Lambda = g*phi_-_vac^2 (Part 87) — confirmed free parameter
  - Beats between phi and psi fields (Part 25, 68) — w(z) ≠ -1 [SPECULATIVE]
  - phi_- quintessence — frozen w=-1 (Part 88) [NEGATIVE for H_0]
  - phi_-^4 missing term (Part 88) — EDE candidate [SPECULATIVE]
  - phi_-_vac ~ 10^-70 rad; rho_vac = rho_Planck/7.68 (Part 87)
- Section 5: Neutrino detectability (Part 89) — evanescent/propagating transition
- Section 6: Open questions and PDTP predictions (falsifiable)
- Section 7: What PDTP does NOT explain (honest negative results)

**Sources to survey before writing:**
Parts 22, 25, 28b, 28c, 29, 33, 54, 61, 62, 68, 69, 71, 87, 88, 89
Docs: hubble_tension_c1.md, cosmo_constant_a3.md, cosmo_constant_v2.md,
      condensate_layer_optics.md, falsifiable_predictions.md, wave_effects_extension.md

**Update rule:** Any Part that produces a DM or DE finding (positive or negative)
must add an entry to dark_matter_energy.md in the same session before commit.

**Expected Part #:** 90 (creation); then living update each relevant Part thereafter
**Status:** [ ] TO CREATE
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
| 1 | [x] D1-D2 (negative re-examination) | D1: Part 77 (SU(3) AF still neg); D2: Part 79 Path 1 (RG still neg) | 77, 79 | DONE |
| 2 | D3 [x] D4 [x] (remaining negatives) | D3: DONE (Part 80); D4: DONE (Part 82, still neg; chameleon; theta_0~theta_C) | 80, 82 | DONE |
| 2.5 | [x] Wave Effects Audit — G focus | Systematic: check all 55 wave effects + 28 vars against Lagrangian; G as combination? | 81 | DONE |
| 3 | [x] B1 (N_eff = 6pi gap) | PARTIAL: N_eff range 10-34, target 6pi~18.85 between; Casimir near-miss 1%; universal gap | 83 | DONE |
| 4 | [x] B3 (tetrad from SU(3)) | PARTIALLY RESOLVED: SU(3) replaces tetrad for linearized gravity; 2-DOF deficit for strong-field | 84 | DONE |
| 5 | [x] A1 FCC (m_cond / hierarchy) | SU(3) AF + BCS + bounds — all negative; m_P saturates BH bound | 77-78 | DONE |
| 6 | [x] B4 (CP violation) | PARTIALLY RESOLVED: L5 sin(2phi_-) real CP; delta=-eps/g; eta~6e-10 | 85 | DONE |
| 7 | [x] A2 (alpha_EM) | FCC 5 paths — all negative; confirmed free parameter | 79 | DONE |
| 8 | [x] B2 (nonlinear Einstein) | PARTIALLY RESOLVED: sigma model NEGATIVE; entropy+Jacobson PARTIAL (a_0=1.665*l_P) | 86 | DONE |
| 9 | [x] A3 (Lambda) | CONFIRMED FREE PARAM: Lambda=g*phi_-_vac^2; rho_vac=rho_P/7.68; DESI w(z) | 87 | DONE |
| 10 | [x] C1 (Hubble tension) | NEGATIVE: phi_- frozen; missing phi_-^4; DESI test | 88 | DONE |
| 11 | [ ] B5, B6, A5 (structural); [x] A4 DONE | Mixed — as needed | 91+ | **NEXT (A4 done)** |
| 12 | [ ] B7 (condensate layer optics) | FCC + Wave Effects Check: n_eff, TIR, dark matter, evanescent | 90+ | PENDING |
| 13 | [ ] E1 (dark_matter_energy.md living doc) | Compile all DM/DE findings from all Parts into one file | 90+ | PENDING |
| 14 | [ ] A7 (emergent c) | c = omega_0 x l_0; c_s=c reframe; Bessel renorm; VSL; Sudoku | 91+ | PENDING |

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

## CP-Violating Extensions (L4-L6) — Preliminary

Adding sin terms to each Lagrangian to investigate CP violation (see B4 above).
**Mechanism:** sin is CP-odd (sin(theta) -> -sin(theta) under CP), so ANY sin term breaks CP symmetry.
The sign (+eps or -eps) does not create CP violation — it selects the direction of asymmetry
(matter vs antimatter dominance). cos shapes the potential; sin tilts it.

| # | Lagrangian | CP violation? | Notes |
|---|-----------|---------------|-------|
| L4 | +g cos(psi-phi) +/- eps sin(psi-phi) | FAKE | = sqrt(g^2+eps^2) cos(psi-phi-delta); removable by phi' = phi + delta |
| L5 | L2 +/- eps sin(phi_b - phi_s) | REAL | sin(2*phi_-) tilts vacuum; sign selects matter vs antimatter |
| L6 | g Re[Tr(Psi^dag U)]/3 +/- eps Im[Tr(Psi^dag U)]/3 | REAL | = QCD theta-term; experiment: theta < 10^-10 |

L5 in multiple forms:

| Form | L5: Two-Phase - sin |
|------|-------------------|
| **Lagrangian** | +g cos(psi-phi_b) - g cos(psi-phi_s) +/- eps sin(phi_b - phi_s) |
| **phi_+/phi_- variables** | 2g sin(psi-phi_+) sin(phi_-) +/- eps sin(2*phi_-) |
| **Field eq (phi_-)** | box phi_- = -g cos(psi-phi_+) sin(phi_-) -/+ 2*eps cos(2*phi_-) |
| **Quadratic** | L2_quad +/- 2*eps*phi_- (linear tilt — breaks phi_- <-> -phi_- symmetry) |
| **Vacuum shift** | phi_- = pi/2 - delta where delta ~ eps/g for small eps; sign of delta = sign of eps |
| **CP test** | Under CP: sin(2*phi_-) -> -sin(2*phi_-); L5 NOT invariant -> CP broken |

L6 in multiple forms:

| Form | L6: SU(3) - sin |
|------|-----------------|
| **Lagrangian** | g Re[Tr(Psi^dag U)]/3 +/- eps Im[Tr(Psi^dag U)]/3 |
| **Complex form** | Re[(g -/+ i*eps) Tr(Psi^dag U)/3] = |g_eff| Re[Tr(Psi^dag U) e^{+/-i*delta}]/3 |
| **Lattice form** | Wilson: -K Re[Tr(U_plaq)]/3 +/- eps_lat Im[Tr(U_plaq)]/3 |
| **QCD match** | eps_lat = theta/(32*pi^2) in continuum limit |
| **Experimental** | Neutron EDM bounds theta < 10^-10 |
| **CP test** | Under CP: Im[Tr] -> -Im[Tr]; L6 NOT invariant -> CP broken |

**Key question for B4:** Can PDTP explain WHY eps (= theta) is so small?
If yes → solves Strong CP Problem (major prediction).
If no → eps is another free parameter (A7).

**TODO:** [ ] Full investigation of L5 and L6 as part of B4 FCC.
**Simulation plan:**
- [ ] Simulate L5 with +eps and -eps; measure matter vs antimatter production rates
- [ ] Pick sign matching observed matter-dominated universe
- [ ] Derive how CP term feeds into baryon asymmetry equations (Sakharov condition 2)
- [ ] Estimate whether eps can realistically produce observed baryon-to-photon ratio (~6x10^-10)

---

## Next Parts

### Part 77 — SU(3) Dimensional Transmutation (A1 FCC) — DONE
- Phase 47 in solver; `su3_dim_transmutation.py`
- FCC for A1: 7 untried Methodology.md items investigated
- SU(3) AF FAILS (alpha_s = 2.0, strong coupling, no hierarchy)
- BCS gap FAILS (circular); proof by contradiction FAILS (any m_cond works)
- **Positive:** m_cond <= m_P from BH bound (saturated); m_cond_QCD = 0.236 GeV from sigma
- Sudoku 8/8; research doc: `su3_dim_transmutation.md`

### Part 78 — Extremal Condensate: 4 Remaining Paths for A1 — DONE (2026-03-22)
- Phase 48 in solver; `extremal_condensate.py`; doc: `extremal_condensate.md`
- Investigated all 4 untried paths from Part 77's FCC. **All 4 NEGATIVE for fixing m_cond.**
- **Key conclusion:** PDTP determines dimensionless structure but not dimensional scale.
- 9/9 Sudoku pass. 9 dimensionless quantities determined by K_NAT = 1/(4*pi).

**Path 1: Entropy maximization / holographic bound** — NEGATIVE
- S_Bek = 2*pi*k_B per cell (m_cond cancels); S_holo = pi (l_P=a_0 tautology)
- Mode counting: entropy monotonically increasing with m_cond; no non-circular upper bound
- **POSITIVE:** G = thermodynamic dual of entropy density eta = 1/(4*a_0^2) (Jacobson)

**Path 2: Dvali N-species bound** — NEGATIVE
- N = (m_P/m_cond)^2 = 1 for m_cond = m_P — one gravitational species
- Natural (one condensate field) but assumption, not derivation

**Path 3: Independent Lagrangian (Higgs analogy)** — NEGATIVE
- VEV rho_0 = 12*K_NAT = 3/pi = 0.955 (pure number from cosine expansion)
- Structure (symmetry breaking shape) not scale (physical mass); same as SM Higgs problem

**Path 4: Topological invariant (SU(3) instantons)** — NEGATIVE
- S_inst = 8*pi^2/g^2 = pi exactly (no free parameters)
- exp(-pi) = 0.0432 — 10^15x stronger than QCD; instantons NOT suppressed
- Instanton-generated mass still needs external reference scale mu

**Final status:** m_cond = m_P confirmed as PDTP's fundamental free parameter after 11 paths.
Analogous to Lambda_QCD in QCD, v_EW in SM, Lambda in GR.

---

### Part 79 — Alpha_EM FCC: Fine-Structure Constant Derivation — DONE (2026-03-22)
- Phase 49 in solver; `alpha_em_fcc.py`; doc: `alpha_em_fcc.md`
- **FCC completed:** Full Methodology.md checklist (42 items evaluated; 16 untried -> 5 paths)
- **All 5 paths NEGATIVE.** alpha_EM confirmed as free parameter after 8 approaches.
- 9/10 Sudoku pass. 11 derived quantities cataloged.

**Path 1: SU(3)-U(1) coupling** (item 8.4) — NEGATIVE
- K_NAT^2 at M_P -> QED RG gives 1/alpha = 231 (not 137); wrong direction
- Backward solve: alpha_EM(M_P) = 1/64 needed [Eq. 79.1]

**Path 2: Emergent impedance** (item 8.6) — NEGATIVE
- Metric (spin-2) and gauge (spin-1) are independent sectors; c_s = c is not enough

**Path 3: Topological winding** (items 6.5, 8.2) — NEGATIVE
- Dirac: constrains e*g_m, not e alone; Chern = integers; alpha irrational
- **POSITIVE:** g_m/e = 1/(2*alpha) = R_K/Z_0 [impedance duality, Eq. 79.5]
- **POSITIVE:** Wyler's formula 0.6 ppm [Eq. 79.6]

**Path 4: Coupling ratios** (item 7.4) — NEGATIVE
- Ratios depend on alpha_GUT and M_GUT (both free)
- **POSITIVE:** sin^2(theta_W) = 3/8 at GUT scale [Eq. 79.7]

**Path 5: Two-phase extension** (item 8.5) — NEGATIVE
- phi_- is spin-0 (not photon); same K_NAT; no new dimensionless number

**Future:** Wyler's conformal geometry (O(4,2)) — most promising unexplored direction

---

### Part 80 — Dispersion Model Re-examination with Two-Phase phi_- — DONE (2026-03-24)
- Phase 50 in solver; `dispersion_two_phase.py`; doc: `dispersion_two_phase.md`
- **D3 re-examination:** Part 57 had 4 fatal problems; re-examined with two-phase phi_-
- **NEGATIVE CONFIRMED:** 2 improved (F1 gradual gap, F4 direction reversed), 2 unchanged (F2, F3)
- 10/10 Sudoku pass. 4 equations (80.1-80.4).

**Key results:**
- F1: Gap is now E_gap = hbar*sqrt(2*g*Phi) — continuous across space, not fixed at E_P [Eq. 80.1]
- F2: phi_- (spin-0) does not couple to A_mu or gluons (spin-1) [Eq. 80.2]
- F3: b0_QCD = 7 unchanged by phi_- — AF is quantum loops [Eq. 80.3]
- F4: BH max gap ~ 2.8 MeV (was E_Planck); mismatch reverses direction [Eq. 80.4]
- Root cause: coupling running = quantum (vacuum polarization) != classical dispersion

---

### Part 81 — Wave Effects Audit: G as Combination Effect — DONE (2026-03-25)

**Phase:** 51 in solver; `wave_audit_g.py`; doc: `wave_audit_g.md`
**Reference:** `docs/wave_effects_extension.md` (55 effects, 25 emergent, 28 variables)
**Motivation:** All 11 paths to derive m_cond (and thus G) have failed (Parts 29-35, 77-78).
Every attempt treated G as a single parameter. But emergent phenomena (SOFAR, solitons,
photonic band gaps) show that measurable "constants" can arise from COMBINATIONS of
simpler wave effects. What if G is like SOFAR — not one knob, but a combination?

**Core question:** Does the wave effects checklist reveal missing Lagrangian terms that
could collectively determine G (or m_cond) without any single term doing it alone?

#### Step 1: Lagrangian Coverage Audit

Go through all 55 wave effects (Section 1) + 28 variables (Section 4) and for each:
- Is this effect/variable represented by a term in the Lagrangian?
- If YES: which term? (kinetic, cos coupling, two-phase, SU(3))
- If NO: what term would produce it? Write the candidate term explicitly.

**Preliminary audit (from initial scan):**

| Wave Effect | In Lagrangian? | Which Term / What's Missing |
|-------------|:-:|----|
| Traveling waves (#10) | YES | Kinetic terms -> wave equation |
| Standing waves (#9) | YES | Boundary conditions on kinetic |
| Interference (#14,15) | YES | cos(psi-phi) IS interference |
| Phase locking (#41) | YES | cos coupling directly |
| Dispersion/mass gap (#23) | YES | cos -> Bogoliubov dispersion |
| Resonance (#17) | YES | Natural frequency from cos |
| Surface tension | YES | Two-phase -cos term |
| Beats (#18) | PARTIAL | Phase drift (Part 25) but no explicit 2nd frequency source |
| **Damping (#22,43)** | **NO** | No dissipation term (gamma * d_t phi) |
| **Scattering (#21,45)** | **NO** | No disorder/inhomogeneity term |
| **Decoherence (#48)** | **NO** | No environment/bath coupling |
| **Higher-order dispersion** | **NO** | No (nabla^2 phi)^2 beyond two-phase biharmonic |
| **Anisotropy/Birefringence (#29)** | **NO** | Scalar = isotropic; needs tensor extension |
| **Cross-layer coupling** | **NO** | No phi*U or U*Phi_H terms |
| **Gradient coupling** | **NO** | No d_mu(phi) * d_mu(psi) term |
| **Guided waves (#51)** | **NO** | No geometry/boundary terms |
| **Wave mixing (#39)** | **WEAK** | Only through cos -> phi^4 expansion |
| **Temperature (#26)** | **NO** | No thermal/statistical terms |
| **Impedance variation (#24)** | **IMPLICIT** | kappa/rho ratio but not spatially varying |

#### Step 2: Candidate Missing Terms

For each "NO" above, write the explicit Lagrangian term and check what it produces:

| # | Candidate Term | Mathematical Form | What It Produces | Could Affect G? |
|---|---------------|-------------------|-----------------|:-:|
| T1 | Damping | gamma * d_t(phi) | Attenuation, decoherence, coherence length | Indirectly — sets range |
| T2 | Biharmonic (already in two-phase) | (nabla^2 phi)^2 | Modified short-wavelength dispersion | YES — changes effective stiffness |
| T3 | Derivative coupling | d_mu(phi) * d_mu(psi) | Velocity-dependent force; frame-dragging | YES — modifies how matter feels condensate |
| T4 | Disorder/noise | eta(x) * phi | Scattering, Anderson localization, vacuum fluct. | YES — could renormalize G |
| T5 | Anisotropy tensor | kappa_ij * d_i(phi) * d_j(phi) | Direction-dependent speed; birefringence | Maybe — directional G |
| T6 | Cross-quadratic | phi^2 * psi^2 | Wave mixing, parametric amplification | YES — nonlinear coupling changes effective g |
| T7 | Boundary/interface terms | delta(x - x_B) * sigma | Guided modes, confinement, surface waves | YES — G could depend on boundary conditions |

#### Step 3: G as Combination Effect (the key test)

Currently: G = hbar*c / m_cond^2, and m_cond is free.
From the lattice: G = c^2 / (4*pi*kappa), where c^2 = kappa/rho.

**SOFAR analogy:** SOFAR channel is not caused by any single parameter. It requires:
- Temperature gradient (sets speed profile)
- Pressure gradient (modifies speed at depth)
- Refraction (bends wavefronts)
- Geometry (ocean boundaries)

No single one creates SOFAR. The combination does.

**G combination hypothesis:** What if G emerges from:
- Coupling strength g (the cos term) — sets phase-locking force
- Lattice geometry (number of neighbors, dimension) — sets stiffness
- Angular forces (Part 28) — needed for c_T = c
- Layer boundary conditions (Section 3a) — B1, B2 interfaces
- Quantum corrections (vacuum polarization) — renormalize g

Each of these is represented (or missing!) in the Lagrangian. If G is fixed by
requiring ALL of them to be self-consistent simultaneously, then m_cond might
not be free — it could be the ONLY value where all ingredients balance.

**Test:** For each candidate term T1-T7:
1. Add it to the Lagrangian
2. Derive the modified G (or modified equation for G)
3. Check: does the new term introduce a constraint that pins m_cond?
4. Sudoku: does the modified Lagrangian still pass all existing tests?

#### Step 4: Remaining Free Parameters

After G audit, the same method applies to:
- Lambda (could be a combination of boundary + thermal + decoherence effects?)
- alpha_EM (could impedance matching + layer structure fix it?)
- sin^2(theta_W) (could cross-layer coupling at B2 determine it?)

These are future Parts (82+). Part 81 focuses on G only.

#### Expected Outcomes

| Outcome | What It Means |
|---------|---------------|
| All terms already present | G truly is a free parameter; nothing missing from Lagrangian |
| Missing term pins m_cond | BREAKTHROUGH — G derived from wave physics |
| Missing terms exist but don't pin m_cond | New physics identified but hierarchy problem persists |
| Combination effect works | G is emergent (like SOFAR); specific combination recipe identified |

#### Step 5: Forced Checklist Check (FCC) — Combined Wave + Methodology Audit

Due to the importance of this investigation (touches A1, A6, C2, C3 simultaneously),
Part 81 includes a **full FCC** run in conjunction with the wave checklist:

1. Open `docs/Methodology.md` — go through **every item** in the checklist
2. For each Methodology item, cross-reference against the wave effects checklist:
   - Does this strategy suggest a missing wave effect or Lagrangian term?
   - Has a wave-based version of this strategy been tried?
   - Could combining this strategy WITH a missing wave term open a new path?
3. Document all responses before forming the final plan
4. Special attention to items that were previously marked "not applicable" —
   the wave checklist may reveal they ARE applicable when viewed as wave physics

**Why both checklists together:** Methodology.md asks "what mathematical/physical
strategies exist?" Wave_effects_extension.md asks "what wave phenomena exist?"
Crossing them creates a 2D matrix: (strategy) x (wave effect) = new paths.
Previous FCCs used Methodology alone — this is the first to use both.

**Example cross-reference:**
- Methodology item 4.1 (BCS gap equation) was NEGATIVE for G (circular)
- Wave effect #17 (resonance) + #23 (dispersion) + #9 (standing waves)
- Cross: BCS gap IS a resonance + standing wave combination. Did we check whether
  the COMBINATION of lattice geometry + angular forces + resonance condition gives
  a BCS-like equation where the gap is NOT circular?
- This specific cross was never tested.

**Script:** `wave_audit_g.py` (Phase 51)
- Reads wave_effects_extension.md checklist programmatically
- For each of 55 effects: YES/NO/PARTIAL coverage in Lagrangian
- For each "NO": tests candidate term's effect on G
- FCC: cross-reference each Methodology.md item with wave effects
- Sudoku check for each modification
- Summary: which terms, if any, could constrain m_cond

**Touches A1, A6, C2, C3** — if G is a combination effect, it partially addresses
the hierarchy problem (C2) and explains why THIS Lagrangian (C3).

#### Step 6: DeepSeek Cross-Check (external AI verification)

DeepSeek AI was given the 3 PDTP Lagrangians and attempted to derive G and the
Einstein equations. Its response contained both useful directions and significant errors.
Part 81 must address these systematically:

**What DeepSeek got right (confirm/verify):**
- Two-phase Newton's 3rd law: psi_ddot = -2*phi_+_ddot (already Part 61)
- Biharmonic gravity: nabla^4 + 4g^2 (already Part 61)
- Emergent metric from SU(3): g_uv = Tr(d_u U^dag d_v U) (already Part 75)
- Direction: SU(3) condensate -> emergent metric -> gravity (correct path)

**What DeepSeek got wrong (must NOT reproduce):**
1. **EOM normalization error:** Wrote Box(phi_+) = -2g cos(...) sin(...)
   Correct: Box(phi_+) = -g cos(...) sin(...) (factor 2 from kinetic normalization)
2. **G_bare = g/(4*pi) — unjustified:** No derivation; actual PDTP relation is
   G = hbar*c/m_cond^2 with g = m_cond*c^2/hbar. DeepSeek's formula has wrong dimensions.
3. **Classical kinetic term -> Einstein-Hilbert — WRONG MECHANISM:** The Ricci scalar R
   has 2nd derivatives of g_uv = 3rd/4th derivatives of U. The kinetic term K Tr[(dU)^2]
   has only 2nd derivatives of U. Cannot get R from classical expansion. Requires
   Sakharov one-loop mechanism (quantum effect, not classical rewriting).
4. **Casimir factor applied to G — WRONG:** sigma_SU(3) = (4/3)*sigma_U(1) is for
   string tension (confinement), NOT gravitational coupling. Different physics.
5. **G = 1/(16*pi*K) dimensional mismatch:** K_NAT = 1/(4*pi) is dimensionless in
   natural units. 1/(16*pi*K_NAT) = 1/4 (dimensionless). But G = l_P^2 has dimensions.
   m_cond is completely absent from DeepSeek's formula.

**Key question for Part 81:** DeepSeek's path (SU(3) kinetic -> metric -> Sakharov -> G)
is REAL but requires 4 ingredients working together:
1. SU(3) kinetic term (emergent metric — Part 75)
2. Sakharov one-loop (quantum correction generates Einstein-Hilbert)
3. Two-phase boundary conditions (normalization of G_eff = 2*G_bare)
4. Lattice angular forces (c_T = c condition — Part 28)

Does requiring ALL FOUR simultaneously pin m_cond? This is a specific instance of
the "G as combination effect" hypothesis from Step 3.

#### Part 81 Results (2026-03-25)

**Coverage:** 30/55 YES, 13 PARTIAL/WEAK/IMPLICIT, 12 NO (missing from Lagrangian)
**Terms:** 9 candidates (T1-T9); 2 MAYBE (T6 Sakharov, T7 boundary), 7 NO
**SOFAR hypothesis: REJECTED.** All G ingredients scale as m_cond^(-2); no cross-constraint.
**FCC cross-ref:** 11 untried (Methodology x Wave) paths; all add free params or circular
**DeepSeek:** 6 claims checked, ALL have errors (factors, dimensions, mechanism)
**Sudoku:** 10/10 PASS

**Key equations:**
- Eq. 81.1: 1/(16*pi*G) = N_eff * Lambda^2 / (192*pi^2) [ASSUMED, Sakharov/Visser]
- Eq. 81.2: N_eff = 12*pi ~ 37.7 (PDTP-Sakharov consistency) [DERIVED, PDTP Original]
- Eq. 81.3: G = hbar*c * m_cond^(-2); no cross-constraint from wave audit [DERIVED]
- Eq. 81.4: Box(phi_+) = -g*cos(psi-phi_+)*sin(phi_-) (corrected EOM) [VERIFIED]

**Open paths:**
1. Sakharov one-loop + PDTP layer confinement: N_eff = 12*pi required; grav DOF = 23-29;
   gap 1.3-1.6x; sign problem (N_bos - N_ferm = -7) needs PDTP confinement resolution
2. Boundary terms for OTHER params (alpha_EM, theta_W) — not G
3. DeepSeek corrected path = path #1
4. **Yukawa screening length from reversed Higgs** (from ChatGPT cross-check, 2026-03-26):
   Integrating out massive phi_- gives screened Poisson: nabla^2 Phi - mu^2 Phi = rho,
   where mu^2 = 8g^2/m^2. PDTP already has phi_- mass: m^2 = 2g*Phi (reversed Higgs, Part 62).
   Substituting: mu^2 = 8g^2/(2g*Phi) = 4g/Phi. This gives a **field-dependent Yukawa range**
   r_Yukawa = 1/mu = sqrt(Phi/(4g)). Concrete number needed — compare to fifth-force experiments
   (torsion balance, Casimir force). The algebra in ChatGPT's derivation checks out for the
   screened Poisson step; the errors are in: (a) constant mass instead of field-dependent,
   (b) external rho added by hand (circular), (c) G still free, (d) dropping nabla^4 assumes answer.
   **Check with D4** — fold into Part 82 as additional Sudoku test.

---

### Part 82 — Koide Circularity Re-examination (D4) — DONE (2026-03-27)

**Phase:** 52 in solver; `koide_reexamine.py`; doc: `koide_reexamine.md`
**Motivation:** Re-examine Part 32 NEGATIVE (0/8 non-circular G from Koide) with
findings from Parts 37-81. Also check Yukawa screening from reversed Higgs.

**Steps:**
1. Ratio analysis: M_0 vs m_cond_QCD and SU(3) group numbers
2. New constraints: two-phase, emergent metric, Sakharov, Xi_cc — all NEGATIVE
3. Yukawa screening: r = sqrt(hbar*Phi/(4*m_P)) ~ 10^-18 m at Earth
4. FCC: 13 Methodology items, 5 new — all NEGATIVE or numerology
5. theta_0 = 2/9 investigation: ~ Cabibbo angle at 2.2% (excluded by m_e)
6. Sudoku: 7/10 PASS (3 expected failures: S5 ratio, S6 hierarchy, S7 Yukawa range)

**Key results:**
- D4 VERDICT: STILL NEGATIVE. Koide = structure theorem, not scale theorem.
- M_0/m_cond_QCD(P37) = 0.855 ~ sqrt(3)/2 (1.3%) — suggestive, not derived
- M_0/m_cond_QCD(P77) = 1.330 ~ C2_fund = 4/3 (0.3%) — suggestive, not derived
- M_0 ~ m_p/3 at 0.3% CONFIRMED — constituent quark mass = Koide base mass
- phi_- reversed Higgs = CHAMELEON MECHANISM (derived, not postulated) [PDTP Original]
- Yukawa range field-dependent: r = sqrt(hbar*Phi/(4*m_P)) [Eq. 82.1, DERIVED]
- At Earth surface: r ~ 10^-18 m (consistent with no fifth force detected)
- theta_0 ~ theta_C (Cabibbo) at 2.2% [SPECULATIVE] — excluded as exact by m_e

**Key equations:**
- Eq. 82.1: r_Yukawa = sqrt(hbar * Phi / (4 * m_P))  [DERIVED, PDTP Original]
- Eq. 82.2: M_0 = 313.84 MeV ~ m_p/3  [CONFIRMED, 0.3%]
- Eq. 82.3: theta_0 ~ theta_C = arcsin(V_us)  [SPECULATIVE, 2.2%]
- Eq. 82.4: G(M_0)/G = (m_P/M_0)^2 ~ 3.6e38  [CONFIRMED, hierarchy wall]

**Open paths:**
1. theta_0 = theta_C (quark-lepton unification — needs GUT)
2. Chameleon predictions (fifth-force at sub-fm sensitivity — future)
3. Unified condensate hypothesis (blocked by hierarchy)

---

### Part 83 — N_eff = 6pi Gap in Sakharov Formula (B1 FCC) — PARTIAL (2026-03-28)

**Phase:** 53 in solver; `neff_sakharov.py`; doc: `neff_sakharov.md`
**Motivation:** FCC item B1 — Sakharov 1-loop with 8 SU(3) gluons gives G_ind = 2.356*G.
Need N_eff = 6pi ~ 18.85 for exact match. Systematic DOF audit.

**Steps:**
1. Gap reproduction: G_ind/G = 3pi/4 = 2.356 [VERIFIED, matches Part 75b]
2. SM DOF counting: signed helicity sum = -62 (fermion-dominated, known issue)
3. PDTP DOF audit: minimal=8, two-phase=10, with matter=34; target 6pi between 10-34
4. Decomposition: 6pi is geometric (heat kernel); near-miss 8+(4/3)*8=18.67 (1% off)
5. Sudoku: 10/10 PASS; verdict: PARTIAL (universal gap, not PDTP-specific)

**Key results:**
- G_ind = (6pi/N_eff) * hbar*c/m_cond^2 confirmed [VERIFIED]
- phi_+ (breathing) and phi_- (chameleon) each add +1 DOF -> N_eff(two-phase) = 10
- 24 matter vortex phases (if they contribute) push to N_eff = 34 -> undershoots
- Crossover at 6pi ~ 18.85 is physically reasonable (between 10 and 34)
- SM signed counting = -62 (negative = repulsive gravity -> known subtlety)
- Casimir near-miss: 8 + (4/3)*8 = 18.67, G_ind/G = 1.0098 (1% off)
- Gap is UNIVERSAL — shared by ALL induced gravity approaches

**Key equations:**
- Eq. 83.1: G_ind = (6pi/N_eff) * hbar*c/m_cond^2  [VERIFIED]
- Eq. 83.2: N_eff = sum_i epsilon_i * nu_i  [STANDARD]
- Eq. 83.3: N_eff(PDTP, minimal) = 8  [DERIVED]
- Eq. 83.4: N_eff(PDTP, two-phase) = 10  [DERIVED]
- Eq. 83.5: N_eff(PDTP, +matter) = 34  [ESTIMATED]
- Eq. 83.6: G_ind/G = 6pi/N_eff  [DERIVED, scheme-independent]

**Open paths:**
1. Matter vortex contribution: how much does each species contribute? (scalar phase vs spinor)
2. PDTP lattice regularization: may shift the geometric prefactor (6pi -> different number)
3. Casimir mechanism: can SU(3) structure amplify gluon DOF by 4/3? Would close gap to 1%

---
