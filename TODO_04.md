# TODO_04 — Tangent Function Investigation

**Type:** Full FCC + Wave Check
**Initial investigation:** `docs/research/tan_initial_investigation.md`
**Date opened:** 2026-03-28
**Previous roadmaps:** [TODO_01.md](TODO_01.md) (Parts 1-41) |
[TODO_02.md](TODO_02.md) (Parts 42-76) | [TODO_03.md](TODO_03.md) (Parts 77-83+)

---

## Open Items — Quick Reference

New additions go on top. One line per item. Full details below.

- T78 — De Broglie double-solution pilot-wave comparison (Darrow & Bush 2024, *Symmetry*, arXiv:2408.06972 -- real, open-access, peer-reviewed): Lorentz-covariant two-way-coupled pilot-wave framework with Compton-scale oscillations satisfying the de Broglie relation; compare against PDTP's own matter-wave (psi) treatment, same spirit as the Elastic Universe review (T27) [PENDING, MEDIUM]
- T77 — Timeflow Gravity comparison (Trofimov 2026, *Class. Quantum Grav.* 43, DOI 10.1088/1361-6382/ae811d -- real, peer-reviewed, PDF now in hand at assets/pdfs/Trofimov_2026_Class._Quantum_Grav._43_135020.pdf): strikingly close core thesis (1D circle/U(1) state space, entropic gravity via the SAME Jacobson Clausius-relation argument as PDTP's Part 86, MOND-like dynamics from phase coherence, DM/DE as phase-space projections) -- needs a careful, honest side-by-side now that the paper is available [PENDING, HIGH]
- T76 — Topological dark-matter candidate: ring-on-chain linking [SPECULATIVE, user-original idea, NOT a citable paper]: could a "gets tangled without extra energy cost" topological mechanism (ring-dropped-over-a-2-line-chain trick; canal tow-rope "roving bridge" analogy) be a genuine additional DM candidate -- matter acquiring DM-like behavior via topology alone rather than needing exotic energy? Must be checked against the already-mature candidate roster in dark_matter_energy.md Part 2 (esp. Mechanism 2 / winding-number n=1, Part 116) and cross-referenced with T30 (Hopf-link coherence protection) before being treated as new. Rubik's-cube/Cayley-graph state-space idea folded in as a second, weaker topological analogy, also SPECULATIVE [PENDING, LOW-MEDIUM]
- T75 — TeVeS structural comparison [scoping]: TeVeS (Bekenstein's tensor-vector-scalar relativistic completion of MOND) is one of GW170817's casualties (arXiv:1710.06168); PDTP has no true vector field anywhere in its Lagrangian (confirmed T70/Part 140) -- worth understanding what TeVeS's vector field buys it, both for the DM/MOND question and the still-open "no U(1) EM vector field" gap flagged in docs/research/polarization_analogy.md [PENDING, MEDIUM]
- T74 — GW170817 constraint on PDTP's own GW structure [DONE, Part 142, 2026-09-10 -- PASS (tensor sector) + CONSTRUCTIVE NEGATIVE (scalar sector): tensor sector (phi_+/SU(3), the actual LIGO signal) has c_s=c EXACT (Part 3/63 S8), trivially inside the computed GW170817 speed bound (4.13e-16, computed here from the paper's own Delta t=1.7s/d=40Mpc, not quoted from memory) -- PASS by pre-existing PPN-gamma=1 design requirement, not coincidence; phi_- (scalar/breathing mode) is NOT what GW170817's timing measures -- shown evanescent (non-propagating) at LIGO-band frequencies for EVERY physically realized potential incl. emptiest cosmic voids (77 orders of margin, Sachs-Wolfe LSS scale vs. propagation threshold) -- no possible phi_- signal existed for GW170817 to constrain; 11/12 Sudoku; byproduct: found+fixed a 22-orders-of-magnitude numerical erratum in two_phase_rederivation.md (Part 63) Section S7, unrelated to T68's bug but same genre; see docs/research/gw170817_dispersion_check.md]
- T73 — Glueball mass test vs X(2370) (BESIII arXiv:2607.20366) [DONE, Part 141, 2026-09-10 -- CONSTRUCTIVE (mass scale) + NEGATIVE (quantum numbers): Mechanism A (closed flux-tube loop, Parts 36-37's own sigma/xi_QCD) brackets X(2370)'s 2376 MeV at minimal radius (1.18-4.01 GeV) and stays within x5 across R=1-3*xi_QCD (10/12 Sudoku); Mechanism B (Part 114's chi^a contact vertex reapplied at QCD layer) is 4.7x too weak, E_break_QCD=507 MeV -- clean negative, distinguishes the two mechanisms; J^PC=0-+ quantum numbers NOT derivable by either (chi^a are NLSM scalars per T70/Part 140, no vector-gluon content to build 0-+ from) -- mass-scale coincidence, not a derivation; see docs/research/glueball_x2370_test.md]
- T71 — Audit the CKN "factor 12" formula discrepancy (Part 54): cosmological_constant_fcc.md gives rho_CKN = hbar*c/(l_P^2*L_H^2), TODO_02.md/equation_reference.md give rho_CKN = c^2/(G*L_H^2) -- these did not look dimensionally equivalent on a quick check (2026-09-06, found while searching the repo for qwen's "factor 12" claim); need to determine which is correct, reconcile the "factor 12" number, and only then judge whether qwen's Suggestion 4 (GHY boundary term / Padmanabhan bulk-surface equipartition) is worth pursuing [PENDING]
- T70 — N_eff via spin-weighted Seeley-DeWitt a_2 heat-kernel coefficient [DONE, Part 140, 2026-09-06 -- CONSTRUCTIVE NEGATIVE: formula unverifiable (2 targeted lit searches found no source for N_v + 11/2*N_f + 1/6*N_s); more decisive, PDTP's own Lagrangian (U(1), SU(3), two-phase) has N_v=0, N_f=0 identically -- "gluons"/"quarks" are nonlinear-sigma-model scalars (confirmed via Part 114's independent classification + Weinberg ChPT anchor), not real gauge bosons/spinors; Part 40's Wilson fermions are a borrowed lattice-QCD scaffold, not PDTP's own matter field; computed anyway for completeness -- QCD-analogy reading gives G_ind/G=0.13-0.18 (worse than Part 83's existing range), scalar-only 1/6-weighted reading gives 3.3-14.1 (also worse); Part 83's characterization stands unchanged; 10/10 Sudoku]
- T69 — Dark matter doc audit + two current external events [DONE, Parts 138-139, 2026-09-02 -- audit found+fixed TWO real 1000x unit-conversion bugs (Bullet Cluster bound: 44.3->47.3 OoM margin; KM3 neutrino E/m_W: 2737->2.7e6), both baked into code not just prose, neither changing any verdict; LZ 2.6-sigma event matches NEITHER PDTP DM candidate (16-17 OoM too heavy for n=1 wimpzilla, 1000x too light for ~200 MeV candidate) -- honest fork flagged for future data, not resolved; Roman's lensing/substructure capability tests NOTHING PDTP-specific (biharmonic-gravity route already dead by 20 OoM, DM test needs CMB not optical); Roman's real PDTP connection is the already-on-record w(z) Prediction 5, whose stale "Launch ~2027" note was corrected]
- T49 — Kuramoto connection: PDTP field equation IS relativistic Kuramoto model; Arnold tongues = Leidenfrost boundary; stiffness = m_cond = hierarchy problem; two proposed calculations: (1) winding amplification g_eff ~ g*n closes 43-OoM locking gap, (2) Arnold tongue width vs Part 110 critical exponents [SPECULATIVE, LOW PRIORITY; see docs/research/hierarchy_problem_reframe.md Section 8]
- T48 — Hierarchy problem reframe: 5 reframings + 5 PDTP candidate paths (C1 ratio derivation, C2 cosmological winding, C3 locking fossil, C4 Dvali-Gomez self-reference, C5 anthropic window); revisit after T46 + two-condensate ratio work [SPECULATIVE, LOW PRIORITY until T46 done; see docs/research/hierarchy_problem_reframe.md]
- T46 — Lambda as locking fossil: true vacuum phi_- = pi/2 derived; m/H = 3*sqrt(eps) [Eq 119.1]; freeze condition eps < 1/9 [Eq 119.2]; thawing w = -1+2*eps [Eq 119.3]; mechanism consistent; beta(z) OPEN for magnitude [DONE PARTIAL, Part 119, Phase 87; 12/12 Sudoku; see docs/research/lambda_locking_fossil.md]
- T47 — m_cond consequence scanner: 30-row lookup table scans 10^0 to 10^28 eV/c^2 (one decade per row); 10 individual quantity functions (Newtons, BreathingMode, LatticeSpacing, WindingNumber, DarkMatterMass, CondensateDensity, HealingLength, GPInteractionConstant, BiharmonicScreeningScale, GLParameter); kappa_GL=sqrt(2) self-check in every row; reference rows at m_e, m_p, Lambda_QCD, Higgs, m_P [DONE, Part 120, Phase 88; 12/12 Sudoku; see simulations/solver/t47_mcond_scanner.py]
- T45 — Cleanup: Eq 89.17 erratum (sigma/m = 4 pi G^2 m_DM/v^4 replaces G/c^4) + check_urls.py fixes [DONE, Part 118, Phase 86; 7/7 Sudoku; Bullet margin 47.3 OoM (corrected T69/Part 138, was misstated 44.3 -- separate 1000x Bullet-bound unit error); verdicts unchanged]
- T43 — DM winding selection: n=1 via stability + Kibble-Zurek -> m_DM = m_P [DONE, Part 116, Phase 84; 12/12 Sudoku; KZ relic abundance NEGATIVE (50 OoM); kill test = CMB tensor modes]
- T44 — Positive phi_-^4 quartic: induced lambda_4 = 2g^2 sin^2(beta)/(3 kbar^2) at partial lock [DONE, Part 117, Phase 85; 10/10 Sudoku; tree + zero-point NEGATIVE; self-switching transient EDE; beta(z) OPEN]
- T40 — Nuclear geometry from Y-junction packing [DONE (conceptual), Part 137, 2026-08-30 -- NEGATIVE, resolved together with T28: no Z_3-network counting rule reproduces the magic numbers; E_Y/E_H (Part 37/106) overshoot the ~11 MeV target by 249x/1566x; implementation steps 4-8 (pdtp_topology_correction, Sudoku re-run) not executed -- no surviving formula to wire in]
- T38 — WCT regularizer Theta[psi] as UV-cure candidate in PDTP (from Wave Confinement Theory review, May 2026) [SPEC, low priority]
- T39 — WCT effective metric cross-check vs PDTP acoustic metric (Part 73) and SU(3) metric (Part 75-76) [SPEC, low priority]
- T36 — Three-component Hopf link as baryon structure (3 interlinked quark loops instead of Y-junction flux tube) [DONE, Part 106, Phase 74; E_H/E_Y=2pi; 20/20 Sudoku]
- T37 — Isotope stability mini-project (SEMF baseline + decay rates; validate vs known isotopes; scan Z=115 for Lazar gap) [DONE PARTIAL, Part 107, Phase 75; 6/15 Sudoku; Z=115 longest=11s; Lazar gap ~29 OoM ~ 10 MeV; baseline for T28/T40]
- T28 — Mc-299 / Element 115 topological closure lens [DONE, Part 137, 2026-08-30 -- NEGATIVE: magic numbers 2,8,20,28,50,82,126 NOT Z_3-generated (differences fail divisibility by 3 from 3rd gap); FCC/cuboctahedral shells (Part 54's own lattice type) give ZERO matches; PDTP vortex energy (E_Y/E_H) 1800-11000x too large for shell-gap scale; resolved together with T40; see docs/research/magic_number_topology.md]
- T29 — Phase self-locking mechanism (when does psi lock to internal omega_nuc instead of phi?) [SPEC, Goal 2]
- T30 — Hopf-link topology protection for phase coherence (interlinked vortex loops, decoherence immunity) [SPEC, Goal 2]
- T31 — Nonlinear converging horn / amplitude concentration -> high-harmonic generation in cos coupling [SPEC, Goal 2]
- T32 — Soliton compression / supercontinuum in PDTP (Kerr chi3 from cos expansion, frequency comb) [SPEC, Goal 2]
- T33 — Geometric blueshift via condensate infall flow (analog horizon as frequency pump) [SPEC, Goal 2]
- T34 — Fractal Z_3 cascade (self-similar vortex subdivision, frequency ladder 3^n) [SPEC, Goal 2]
- T35 — Analog-horizon Hawking emission test (device should emit T_H phase noise if T33 works) [SPEC, testable]
- T4 — Gravitational Brewster angle for GWs (breathing vs tensor mode reflection) [DONE, Part 108, Phase 76, 2026-05-09]
- T5 — Multi-layer phase stacks (air/water/oil decoupling, transfer matrix) [DONE, Part 109, Phase 77, 2026-05-09]
- T6 — Leidenfrost + tan phase transition (critical exponents, universality class) [DONE, Part 110, Phase 78, 2026-05-09]
- T7 — Hawking temperature with n_PDTP = 1/alpha (modify surface gravity kappa?) [DONE, Part 111, Phase 79, 2026-05-17]
- T8 — PPN parameters with tan corrections (must keep gamma=1, beta=1) [DONE, Part 112, Phase 80, 2026-05-17]
- T9 — Two-phase tan: Delta_+ and Delta_- diagnostics [DONE, Part 113, Phase 81; 12/12 Sudoku; L_res=2g at Leidenfrost; phi_-=breathing mode at horizon]
- T10 — SU(3) group manifold tan [DONE, Part 121, Phase 89; 10/10 Sudoku; Z3 critical angle=60deg tan=sqrt(3); C2=1/sin^2(60)=4/3; see docs/research/su3_tan_geometry.md]
- T11 — Koide angle and tan (theta_0 = 2/9, Z_3 geometry) [DONE, Part 122, Phase 90; 10/10 Sudoku; master formula delta=sqrt(2)*tan(theta_v) PDTP Original; theta_v(leptons)=45deg=U1 critical; quark sqrt(3) NEGATIVE; theta_0 NEGATIVE; see docs/research/koide_tan.md]
- T12 — N_eff and heat kernel tan (does n_PDTP modify 6*pi factor?) [DONE, Part 129, 2026-08-09; 12/12 Sudoku; NEGATIVE -- n_PDTP is M-sourced, identically 1 in the M=0 vacuum where the Sakharov cutoff lives; N_eff gap (Part 83) unchanged; see docs/research/neff_sakharov.md Section 10]
- T13 — Update falsifiable_predictions.md with new testable items from T1-T6 [DONE, 2026-08-09; added Prediction 15 (Brewster angle, Part 108) + Prediction 16 (Leidenfrost critical exponents, Part 110) + Prediction 10 horizon refinement (Part 113)]
- T14 — Update equation_reference.md with all new T-equations [DONE, 2026-08-09; found Parts 121 (T10) and 122 (T11) missing entirely, added both; flagged Parts 119/120 (T46/T47, Lambda thread) as also missing but out of T14's scope]
- T15 — Final verdict and summary (did tan reveal new physics?) [DONE, 2026-08-09; VERDICT: genuine new structure (U(1)/SU(3) geometric unification, surprising Koide-45deg connection, 2 new falsifiable predictions), but does NOT constrain m_cond/G -- tan investigation CLOSED as productive]
- T66 — Rotation-field / tetrad promotion (Cosserat-continua analogy) [DONE, Part 136, 2026-08-30 -- literal SO(2) proposal is an information-free relabeling of phi(x) (dim SO(2)=1, same as U(1)); all 4 Key Questions resolved; 11/12 Sudoku (1 informative contradiction: violates Cosserat's independence requirement by construction); genuine SO(3)/decoupled-field extension flagged, NOT adopted; see docs/research/rotation_field_gate_check.md]
- T65 — Backfill mathematical_formalization.md: doc stops before Part 37 (SU(3)) and Part 61 (two-phase); add both as new sections with full step-by-step derivations [integration, LARGE, filed 2026-07-11]
- M3 — Moire band spacing vs evanescent depth (Part 89 cross-check) [SPEC] [DONE, 2026-08-30 -- DEGENERATE as posed: a=lambda_evan is forced by definition (same Compton-wavelength formula), so theta=60 deg drops out independent of which boundary/scale is checked; not a genuine physics cross-check, though 60 deg does coincide with Part 121's independently-derived SU(3) angle]
- M4 — Moire min displacement {s,r} vs vortex winding (quark n=73 Pythagorean?) [SPEC] [DONE, 2026-08-30 -- NEGATIVE: the (37,36) pair is a mathematical inevitability for ANY odd number (SymPy-proved for general odd N) and, since 73 is prime, is also the UNIQUE possible pair -- not small, not special, no evidence either way]
- T17 — n=sqrt(2) observable near compact objects (VLBI/EHT lensing signature) [priority 17] [DONE, Part 130, 2026-08-09 -- no isolable signature at n=sqrt2 itself; positive byproduct: EHT shadow radius matches GR exactly even in scalar theory]
- T18 — Two-phase Delta_- crossover inside dense matter (neutron star f/g-modes) [priority 18] [DONE, Part 131, 2026-08-09 -- NO pi/4 crossover for Delta_- (structurally different from Delta_+); independently re-derives Part 119's phi_-=pi/2 true vacuum; NS mode-frequency sub-question OPEN, filed as TODO_05 T68]
- T19 — L_4 SymPy verification + b quark check (all L_4 results currently unverified) [priority 19] [DONE, Part 132, 2026-08-09 -- found+fixed a real sign error (FE1-FE3) and a real numerical error (eigenvalues failed trace check); b-quark "4% match" downgraded to open question, doc's own cited analogy actually favors a different rule that does NOT match]
- T20 — L_4 Goldstone mode: what is it? (graviton? phi_-? Higgs eater?) [priority 20] [DONE, Part 133, 2026-08-09 -- genuine independent massless scalar; NOT graviton (spin), NOT phi_- (field content), not currently eaten (no gauge field)]
- T25 — String theory and PDTP (Regge slope, graviton, extra dims, landscape) [priority 25, low] [DONE, Part 134, 2026-08-30 -- graviton/landscape structurally analogous only; Regge slope CANNOT constrain m_cond (different condensate layers, NEGATIVE for a structural reason); T/S-duality vs phi+/phi- NEGATIVE (superficial resemblance only); no PDTP moduli]
- T26 — Bob Lazar truth table (decoupling phenomenology, 5 scenarios) [priority 26, low] [DONE, Part 135, 2026-08-30 -- "amplifier" claim structurally impossible (cos bounded, alpha<=1); 3-emitter geometry EXACTLY matches Part 71's Z3 cancellation (re-verified, coincidence not evidence); energy budget NEGATIVE by ~7 OoM beyond universe mass-energy (boundary-layer) / dozens of OoM (practical device); payoff = T35 Hawking test, independent of Lazar]
- T27 — Elastic Universe review (shear modes, liquid crystal, visualizations) [priority 27, low] [DONE, 2026-08-30 -- all 3 phases complete (E1-E16, J1-J3); site DOES have a Lagrangian now (updates earlier "no Lagrangian" finding), still no EFE/Schwarzschild/charge-quantization; JSFiddle library ~150-220 unique demos, 6-fiddle shortlist extracted (Hopf, FCC+tensor, Liquid Crystal = good rendering candidates; "Cosserat Charge" = NEGATIVE, does not implement Cosserat theory despite name -- relevant to T66); author = Chantal Roth (PhD Sci. Computing, not physics)]

**Natural next pick:** T12 (N_eff and heat kernel tan -- does n_PDTP modify the 6*pi factor?)
or T13/T14 (update falsifiable_predictions + equation_reference).
T48/T49 remain low priority (speculative).
**See also:** TODO_05.md (Lambda-locking deep dive + multi-medium framework; T50-T59).

---

## Motivation

PDTP uses cos(psi - phi) for coupling and sin(psi - phi) for force, but the
tangent function tan = sin/cos has never been systematically investigated.

Initial investigation (2026-03-28) found that tan(psi - phi) is a physically
meaningful **diagnostic ratio** that:
1. Defines a **critical transition point** at Delta = 45 degrees (tan = 1)
2. Gives a **PDTP refractive index** n = 1/alpha = 1/cos(Delta)
3. Predicts a **gravitational Brewster angle** for GW polarization splitting
4. Provides a **loss tangent** framework for the dark energy transition
5. Connects Leidenfrost decoupling (tan → infinity) to phase transition physics
6. Extends to multi-layer (air/water/oil) decoupling models

**Goal:** Systematically check every tan-related result against the full PDTP
framework (FCC + Wave check), derive new predictions, and verify consistency
with all previous Parts.

**Our overarching goal:** Fix and prove the Lagrangian works mathematically
until observations can approve or disprove. Deriving G from the framework
(without using G as input) remains the big milestone.

---

## Rules

Same as TODO_03:
- One Part at a time
- Every new equation: Sudoku consistency check (10+ tests)
- Every PDTP Original result: SymPy verification
- Every research .md: complete derivation (show your work)
- Python: no Unicode, save output to `simulations/solver/outputs/`
- Plain English explanations for every key result
- Commit after user approval

---

## Investigation Queue

### Phase 1 — Foundations (verify tan framework)

#### [x] T1. PDTP Refractive Index — PRIORITY 1 — DONE (Part 98, 2026-04-04)

**Part:** 98
**Script:** `simulations/solver/pdtp_refractive_index.py` (Phase 66)
**Doc:** `docs/research/pdtp_refractive_index.md`
**Sudoku:** 10/10 PASS

**RESULTS:**
- n_PDTP = 1/alpha = 1/cos(Delta) DERIVED from acoustic metric g_tt = -alpha^2*c^2 [Eq 98.1]
- alpha = sqrt(-g_tt/c^2) = sqrt(1-2GM/(rc^2)) [Eq 98.2, PDTP-Schwarzschild identification]
- Weak-field: n ~ 1 + GM/(rc^2) [Eq 98.3] -- HALF of GR isotropic (1 + 2GM/(rc^2)) [Eq 98.4]
- Factor-of-2 gap [Eq 98.5, PDTP Original]: PDTP scalar captures g_tt only; full GR captures g_tt + g_ij
  - PDTP U(1) scalar deflection: 0.875" [Eq 98.6] -- Newtonian; RULED OUT by Eddington 1919
  - PDTP SU(3) / GR tensor deflection: 1.75" [Eq 98.7] -- confirmed; needs Part 75 metric
  - SPECULATIVE: two-phase G_eff = 2*G_bare (Part 61) may close the gap without SU(3)
- TIR at horizon: n -> inf as r -> r_S [Eq 98.8, PDTP Original, DERIVED]
- Two-phase: n_+ = 1/cos(Delta_+), n_- = 1/cos(Delta_-); n_- ~ 1 (negligible) [Eq 98.10]
- Two n-types in PDTP: n_grav = 1/alpha (lensing) vs n_plasma = sqrt(1-omega_gap^2/omega^2) (layers)
- SymPy: 1/cos(x) Taylor = 1 + x^2/2 + 5x^4/24 + ...; n ~ 1+GM/(rc^2) confirmed

#### [x] T2. Critical Point at tan = 1 (45 degrees) — DONE (Part 99, 2026-04-06)

**Part:** 99
**Script:** `simulations/solver/tan_critical_point.py` (Phase 67)
**Doc:** `docs/research/tan_critical_point.md`
**Sudoku:** 10/10 PASS

**RESULTS:**
- Field eq: ddot(Delta) = -2g sin(Delta); V(Delta) = -2g cos(Delta) [Eq 99.1-2, DERIVED]
- Fixed points: Delta=0 (stable, omega^2=2g), Delta=pi (unstable). pi/4 is NOT a fixed point.
- tan(Delta)=1 is a FORCE-COUPLING CROSSOVER, not a bifurcation [Eq 99.3, PDTP Original]
- Regime: tan<1 = coupling dominates; tan>1 = force dominates (sizzling onset) [Eq 99.4]
- alpha_c = 1/sqrt(2), n_c = sqrt(2) (universal -- independent of g, m_cond) [Eq 99.5, PDTP Original]
- Energy fraction = 1-1/sqrt(2) approx 0.293 (29.3% to reach sizzling onset) [Eq 99.6, PDTP Original]
- Two-phase: n_+ = sqrt(2) at Delta_+=pi/4; phi_- correction O(Delta_-^2) negligible in vacuum
- SymPy: all 6 checks PASS (residuals = 0)

#### [x] T3. Gravitational Loss Tangent and Dark Energy — PRIORITY 3 -- DONE (PARTIAL)

**Part:** 102 (Phase 70) -- `simulations/solver/t3_loss_tangent.py`
**Doc:** `docs/research/loss_tangent_dark_energy.md`
**Verdict:** PARTIAL -- structural mapping works, no new z-scale, no w_a resolution.
**Results:**
- eps(Delta, H) = g(1 + cos Delta)/(9 H^2) [Eq 102.1, PDTP Original]
  Generalises Part 25 harmonic epsilon to the FULL nonlinear pendulum.
- Harmonic limit: g_eff = 2g exactly [Eq 102.2, DERIVED]
  -- confirms Part 99 EOM factor 2 is consistent with Part 25.
- V(Delta)/V(pi/2) = 1 - cos Delta [Eq 102.3]; f_c = 1 - 1/sqrt(2) [Eq 102.4]
- DESI w_0 = -0.827 => eps_0 = 0.0947 [Part 25 Eq 5.1 confirmed]
- Case A (Delta_0 = pi/4 today) => g ~ 2.4e-36 s^-2, g_eff ~ 4.8e-36 s^-2
  -- within 10% of Part 25's independent g_eff = 4.4e-36 s^-2 [CONSISTENT]
- Case B (use Part 25 g_eff) => Delta_0 ~ 25 deg (not at the crossover)
- w_a (T3, constant g) = -6 eps_0 Omega_m/(eps_0+1)^2 = -0.149 [Eq 102.5]
  Algebraically IDENTICAL to Part 25 m=0 [SymPy verified identity]
- Coincidence: f_c = 0.293 vs Omega_m,0 = 0.315 (within 7%) [SPECULATIVE]
  NOT a derivation -- V/V_max and Omega_m are structurally different quantities.
**Negative findings:**
- Slow-roll attractor damps Delta -> 0 (not growing toward pi/2).
  Naive "rising drift" picture is WRONG. Omega_DE grows because matter
  dilutes, not because Delta grows.
- w_a = -0.149 is factor-5 too small vs DESI w_a = -0.75.
  Same as Part 25 m=0. Part 25 m=3 is still required to fit DESI.
- PDTP provides NO new z-scale for the dark energy transition.
  Delta = pi/4 is a PHASE-SPACE threshold, not a REDSHIFT threshold.
- The Part 99 tan(Delta) = 1 crossover is DIAGNOSTIC (about force/coupling
  balance), not a cosmological phase transition.
**What T3 resolves:**
- Part 99 and Part 25 are the same physics: Part 25 = harmonic limit of Part 99.
- g_eff = 2g exactly (was previously only implied).
- The negative sign of dot(Delta) kills the "rising drift" narrative cleanly.
**Open:** Why Omega_m ~ 30%; why m ~ 3 for g_eff(a); selection of Delta_0.
**Sudoku:** 10/10 PASS. SymPy: 6/6 residuals = 0.

---

### Phase 2 — New Predictions (derive and test)

#### [x] T4. Gravitational Brewster Angle — DONE (Part 108, Phase 76, 2026-05-09)

**Part:** 108
**Script:** `simulations/solver/t4_brewster_gw.py` (Phase 76)
**Doc:** `docs/research/brewster_gw.md`
**Sudoku:** 12/12 PASS | **SymPy:** 5/5 PASS
**Verdict:** PRODUCTIVE — new testable prediction derived.

**RESULTS:**
- n = 1/alpha = 1/cos(Delta) (Part 98) used as GW refractive index [Eq 108.1]
- + polarization (TE-equivalent): no Brewster angle; always partially reflects [Eq 108.6, DERIVED]
- x polarization (TM-equivalent): Brewster angle tan(theta_B) = n2/n1 = alpha1/alpha2 [Eq 108.5, DERIVED, SymPy VERIFIED]
- theta_B (galaxy cluster): 45.000286 deg (deviation 5.0 urad = 1 arcsec)
- theta_B (NS surface r=4r_S): 49.1 deg (deviation 4.1 deg — detectable with GW polarimetry)
- Breathing mode: n_b = sqrt(1-omega_gap^2/omega^2) < 1 in dense regions (opposite to tensor) [Eq 108.7]
- Breathing mode has no Brewster angle (scalar/TE-form) but has TIR [Eqs 108.6, 108.8]
- Mode splitting delta_theta_B = theta_B_tensor - theta_B_breath; up to 12.4 deg near omega_gap [Eq 108.10, PDTP Original]
- GR prediction: no Brewster angle (GR has no GW refractive index); splitting = 0

**New prediction [PDTP Original]:**
  At theta_B, the x (cross) GW polarization has R=0; reflected beam at theta_B is
  pure + polarization. Absent in GR. Observable via GW polarimetry at NS boundaries
  (degree-scale deviation from 45 deg).

**Open:**
- Full spin-2 boundary condition derivation to confirm TE/TM assignment (currently [SPECULATIVE])
- Breathing mode TIR → evanescent wave → testable phase noise (link to T35)
- Two-phase phi_- correction to n near dense matter

**Part:** Next after T3
**What:** Full derivation of reflection/transmission coefficients for gravitational
waves (breathing mode + tensor mode) at a step potential boundary.
Calculate the Brewster angle where one mode has zero reflection.
**Key questions:**
- What are the Fresnel-equivalent equations for GWs in PDTP?
- Does the breathing mode (scalar, massive) reflect differently from tensor (massless)?
- At what galaxy cluster density contrast does Brewster splitting become detectable?
**Cross-check with:**
- Part 28b (LIGO as polarization filter, breathing mode)
- Part 65 (chirality from birefringence — two n values, two Brewster angles?)
- Part 76 (SU(3) graviton — spin-2 vs spin-0 mode behaviour)
**Sudoku:** Verify reflection coefficients reduce to known GR result when breathing mode = 0
**Wave check:** Effects 1 (reflection), 2 (refraction), 11 (polarization), 32 (Brewster)

#### [x] T5. Multi-Layer Phase Stacks (Air/Water/Oil Model) — DONE (Part 109, Phase 77, 2026-05-09)

**Part:** 109
**Script:** `simulations/solver/t5_phase_stack.py` (Phase 77)
**Doc:** `docs/research/phase_stack.md`
**Sudoku:** 12/12 PASS | **SymPy:** 3/3 PASS
**Verdict:** PRODUCTIVE + one key NEGATIVE result.

**RESULTS:**
- TMM (Born & Wolf S1.6) implemented for N layers with PDTP n_j = 1/alpha_j [Eqs 109.1-109.4]
- N=0 recovery: TMM == Fresnel (T4) to 10^-16 [VERIFIED]
- N=1 Fabry-Perot: TMM == r_FP formula (Eq 109.7, SymPy + numeric VERIFIED)
- Decoupled limit [DERIVED]: alpha->0 => R->1; perfect gravitational mirror [Eq 109.5]
  Physical: GW (propagating in phi) cannot enter a region where phi is decoupled from psi.
  Meissner analogy from Part 36.
- Quarter-wave AR [DERIVED]: d_QW = c*alpha/(4*f), alpha_AR = sqrt(alpha_out) [Eq 109.6]
  Example: 650 km layer at 100 Hz reduces R from 0.020 to 10^-33
- Photonic bandgap [PDTP Original]: f_gap = c*alpha_oil/(2*d) [Eq 109.8]
  5-period stack at alpha=0.8, d=300km: R_max=0.64 at ~220 Hz (predicted 400 Hz; N too small)
- NEGATIVE [key]: Leidenfrost layer (d~lP~1e-35 m) has R~0 at all GW detector frequencies.
  alpha_crit(LIGO 100Hz) = 1.52e-41 [Eq 109.10, PDTP Original].
  Layer must be km-scale for resonant shielding effect.

**Open:**
- Full N->inf bandgap structure (Bloch waves, band edges)
- TM vs TE bandgap differences
- Link to T6: does ξ diverge at Leidenfrost transition (making layer thicker)?

**Part:** Next after T4
**What:** Quantitative treatment of multiple phase-incoherent layers.
Transfer matrix method for gravitational wave propagation through
stacked regions with different alpha values.
**Key questions:**
- Air layer: thin region with alpha ~ 0 (phase-incoherent). How thin must it be?
- Water layer: bulk region with alpha ~ 1 (coupled). Standard propagation.
- Oil layer: region with intermediate alpha. Partial coupling.
- Does a single fully decoupled layer (alpha = 0) block ALL gravitational coupling?
- Multi-layer interference: can stacked thin films create frequency-selective shielding?
**Cross-check with:**
- Part 71 (Leidenfrost: boundary layer thickness = healing length)
- Part 36 (flux tubes: Meissner screening in condensate)
- Part 34 (healing length xi = l_P/sqrt(2))
**Analogies to verify:**
- Thin-film optics (anti-reflection coatings)
- Acoustic impedance matching (sonar, ultrasound)
- Thermal insulation (air gaps, vacuum flasks)
**Wave check:** Effects 3 (diffraction), 8 (interference), 15 (thin-film), 44 (impedance)

#### [x] T6. Leidenfrost + Tan: Phase Transition Analysis — DONE (Part 110, Phase 78, 2026-05-09)

**Part:** 110
**Script:** `simulations/solver/t6_leidenfrost_tan.py` (Phase 78)
**Doc:** `docs/research/leidenfrost_tan.md`
**Sudoku:** 12/12 PASS | **SymPy:** 6/6 PASS
**Verdict:** PRODUCTIVE — critical exponents derived; universality class classified.

**RESULTS:**
- Critical point: V''(pi/2) = 0 (phase stiffness vanishes) [Eq 110.4, DERIVED, SymPy S1]
- Order parameter: alpha = cos(Delta) ~ eps, beta = 1 [Eq 110.5, DERIVED]
- Correlation length: xi_phi = 1/sqrt(g cos(Delta)) ~ eps^{-1/2}, nu = 1/2 [Eq 110.6]
- GW noise susceptibility: S ~ 1/(g*alpha) ~ eps^{-1}, gamma = 1 [Eq 110.8, testable]
- Energy gap: Delta_V = g per oscillator exactly [Eq 110.9, matches Part 29/71]
- Universality: (beta,nu,gamma)=(1,1/2,1) = NON-EQUILIBRIUM CROSSOVER [Eq 110.10, PDTP Original]
  Matches laser-threshold universality, NOT Ising/XY/BKT equilibrium transitions.
  NOT a spontaneous symmetry breaking -- always requires sustained drive.
- T2 connection: tan=1 crossover at Delta=pi/4 is the exact midpoint of the tan->inf divergence.
- T5 connection: perfect GW mirror condition (R->1, n->inf) = same critical point as V''=0 here.
- Observable: GW phase noise diverges as alpha^{-1} near Leidenfrost decoupling.

**Open:**
- Fluctuation corrections beyond mean-field (RG calculation)
- Two-phase (T9): does phi_- mass cutoff the noise divergence?
- Hysteresis: approach from Delta<pi/2 vs Delta>pi/2

**Part:** Next after T5
**What:** Re-examine Part 71 Leidenfrost decoupling using tan framework.
Does the tan divergence at pi/2 change the energy budget? Is the
decoupling a true second-order phase transition?
**Key questions:**
- Critical exponents: what universality class does the decoupling transition belong to?
- Divergent susceptibility (tan → inf): does this produce anomalous gravitational noise?
- Leidenfrost "temperature" in phase space: what energy density triggers the transition?
- Connection to condensate healing length (Part 34): does xi diverge at decoupling?
**Cross-check with:**
- Part 71 (Leidenfrost energy budget: single oscillator, boundary layer, power)
- Part 34 (healing length, condensate self-consistency)
- Part 62 (reversed Higgs: phi_- mass near matter)
**Wave check:** Effects 26 (phase transitions), 46 (critical phenomena)

---

### Phase 3 — Cross-Checks (verify against all previous results)

#### [x] T7. Hawking Temperature with n_PDTP — DONE (Part 111, Phase 79, 2026-05-17)

**Part:** 111
**Script:** `simulations/solver/t7_hawking_n_pdtp.py` (Phase 79)
**Doc:** `docs/research/hawking_n_pdtp.md`
**Sudoku:** 12/12 PASS | **SymPy:** 5/5 PASS
**Verdict:** CONSTRUCTIVE NEGATIVE + one PDTP Original.

**RESULTS:**
- T_H^PDTP = T_H^GR = hbar c^3/(8pi G M k_B)  [DERIVED, Eq 111.5]
  n_PDTP does NOT modify T_H.
- kappa = c^2/(2r_S) from three routes: lapse gradient (Eq 111.3), n^{-2} gradient (Eq 111.4), acoustic (Unruh 1981). All agree.
- New PDTP Original: kappa = (c^2/2)|d(1/n^2)/dr|_{r_S}  [Eq 111.4]
  "Surface gravity = gradient of n^{-2} at the horizon"
- Physical reason n doesn't change T_H: n=1/alpha slows PHASE velocity c_phase=c/n.
  Hawking T depends on GROUP velocity c_group=c_s=c (Part 34) -- unchanged.
  kappa_acoustic = (1/2)|d(c_s^2 - v^2)/dr| uses c_s=c, not c_phase.
- Breathing mode: T_H unchanged; emission cut off below omega_gap=sqrt(2g)~2.2e-18 rad/s.
  T_cutoff/T_H ~ 1e-22 for stellar BHs -- completely negligible.
- Two-phase (Part 61): G_eff=2G_bare but G_N=G_eff -> T_H unchanged in terms of G_N.
- Birefringence (T4): + and x modes have same T_H (share same alpha(r) profile).

**Open:**
- PG infall v(r) not derived from PDTP Lagrangian (Part 101 gap)
- Breathing mode greybody factor modification (luminosity, not temperature)
- Two-phase phi_- mass correction to kappa (T9)

**What:** Does the refractive index n = 1/alpha modify the Hawking radiation
derivation (Part 24)? The surface gravity kappa involves the gradient of the
metric — which is related to the gradient of alpha (and therefore of n).
**Cross-check with:** Part 24 (Hawking: T_H = hbar*c^3/(8*pi*G*M*k_B))

#### [x] T8. PPN Parameters with Tan Corrections — DONE (Part 112, Phase 80, 2026-05-17)

**Part:** 112
**Script:** `simulations/solver/t8_ppn_tan.py` (Phase 80)
**Doc:** `docs/research/ppn_tan.md`
**Sudoku:** 12/12 PASS | **SymPy:** 5/5 PASS
**Verdict:** PRODUCTIVE — gamma=1 derived from optical metric; beta=1 from Schwarzschild; tan corrections negligible.

**RESULTS:**
- gamma_scalar(U(1)) = 0  [Part 103, ESTABLISHED]  -- FAILS Cassini / Eddington 1919
- gamma_acoustic = 1/2   [Part 101, ESTABLISHED]  -- FAILS Cassini
- gamma_optical = 1      [Eq 112.4, DERIVED]  -- PASSES Cassini
  g_ij = n^2 delta_ij = (1/alpha^2) delta_ij;  n^2 ~ 1+2u at 1PN -> gamma=1
  Physical: optical metric is standard for medium with refractive index n; n=1/alpha is PDTP-natural.
- Tan correction at 2PN: Delta_gamma_2PN = 4*(U/c^2) ~ 1e-7 at Cassini perihelion [Eq 112.5]
  0.4% of Cassini bound -- NEGLIGIBLE
- beta = 1 from Schwarzschild isotropic coordinates [Eq 112.6, DERIVED]
  areal-coord beta=0 is a gauge artifact; PPN uses isotropic gauge -> beta=1 (PASSES LLR)
- beta=1 inherited from Part 73 GR recovery

**Open:**
- Derive optical metric g_ij=n^2 delta_ij from the PDTP Lagrangian (currently a motivated prescription)
- Connection to SU(3) metric g_ij=(1/3)Tr(dU^dag dU) from Part 103 -- are they equivalent?
- 2PN tan correction potentially measurable by LISA/BepiColombo radio science

**What:** Do the PPN parameters gamma and beta acquire tan-dependent corrections
at post-Newtonian order? PDTP must maintain gamma = 1, beta = 1 to match
solar system tests.
**Cross-check with:** Part 12 (tetrad extension), Part 73 (Einstein recovery)

#### [x] T9. Two-Phase Tan: Delta_+ and Delta_- — DONE (Part 113, Phase 81, 2026-05-24)

**Part:** 113
**Script:** `simulations/solver/t9_two_phase_tan.py` (Phase 81)
**Doc:** `docs/research/two_phase_tan.md`
**Sudoku:** 12/12 PASS | **SymPy:** 5/5 PASS
**Verdict:** PRODUCTIVE — product coupling in tan language; ratio diagnostic derived;
T6 and T7 open questions resolved; two new PDTP Original results.

**RESULTS:**
- D+ = psi - phi_+  (gravity coupling gap); D- = phi_-  (surface mode) [Eq 113.1, DEFINED]
- L = 2g*sin(D+)*sin(D-)  [Eq 113.2, DERIVED, SymPy S1]
- L = 2g*alpha_+*alpha_-*tan(D+)*tan(D-)  [Eq 113.3, DERIVED, SymPy S2]
- tan(D-)/tan(D+) = sin(D-)cos(D+)/(cos(D-)sin(D+))  [Eq 113.4, DERIVED, SymPy S3]
- m^2(phi_-) = 2g*sin(D+) = 2g*alpha_+*tan(D+)  [Eq 113.5, DERIVED, SymPy S4]
- T6: phi_- does NOT cutoff phi_+ noise divergence (separate sectors)  [Eq 113.6, VERIFIED]
- T7: kappa unchanged; m^2(phi_-)=2g at horizon = omega_gap^2  [Eq 113.7, VERIFIED]
  NEW: phi_- mode = breathing mode at event horizon [PDTP Original, Eq 113.7b]
- Full decoupling: BOTH D+->pi/2 AND D-->0 required  [Eq 113.8, PDTP Original]
- L_residual = 2g at D+=pi/2, D-=pi/2 (MAXIMUM!) -- closing phi_+ opens phi_-  [Eq 113.9, PDTP Original]
- D- = pi/2 -> single-phase recovery via chi = phi_+ + pi/2  [Eq 113.10, VERIFIED, SymPy S5]

**KEY FINDING:** Two-phase Leidenfrost (D+ = pi/2) is NOT decoupled!
Closing the gravity channel opens the surface channel maximally (L_res = 2g).
Full decoupling requires phi_- to be in vacuum (D- = 0), impossible near any gravity source.

**Open:**
- Can condition (B) D- -> 0 be achieved by screening Phi locally? (T29 connection)
- Does tan(D-)/tan(D+) ratio appear as GW polarisation asymmetry?
- Derive horizon coincidence m^2(phi_-)=omega_gap^2 from symmetry argument

#### [x] T10. SU(3) Tan: Group Manifold Geometry — DONE (Part 121, Phase 89, 2026-07-06)

**Part:** 121
**Script:** `simulations/solver/t10_su3_tan.py` (Phase 89)
**Doc:** `docs/research/su3_tan_geometry.md`
**Sudoku:** 10/10 PASS | **SymPy:** 3/3 PASS (residuals = 0)
**Verdict:** PRODUCTIVE — Z3 critical angle derived; Casimir identity found.

**RESULTS:**
- U(1) critical angle (T2): 45 deg, tan = 1  [reproduced]
- SU(3) Z3 critical angle: 60 deg, tan = sqrt(3)  [PDTP Original, DERIVED, Eq 121.5]
  Derivation: cos(Delta) = cos(Delta - 2*pi/3) -> Delta = pi/3 (SymPy residual = 0)
  Physical: quark equidistant between two Z3 vacua; equal opposing forces; no escape direction
- SU(2) critical angle: 90 deg, tan -> inf  [degenerate: Z2 midpoint = Leidenfrost angle]
- Generator arctan catalog: unique values {30.0, 45.0, 49.1 deg}  [VERIFIED]
  30 deg from lam_8 entry 1/sqrt(3); 45 deg from all off-diagonal lam_1..7; 49 deg from lam_8 entry 2/sqrt(3)
  60 deg appears in root vectors (global), NOT in individual generator entries
- Casimir identity: C2(fund) = 1/sin^2(60 deg) = 4/3  [PDTP Original numerological, SymPy residual=0]
  Holds ONLY for N=3; does not generalize to SU(2) or SU(N>=4)
- String tension: sigma_SU3/sigma_U1 = 1/sin^2(Delta_crit) = 4/3  [Part 37 reproduced]
- Root system: 6 roots at 60 deg intervals (hexagonal); tan(60)=sqrt(3) in root directions
- Confinement sketch [SPECULATIVE]: Z3 geometry prevents quark Leidenfrost; every path to Leidenfrost
  passes through 60 deg equidistance point; quark redirected to next vacuum, not to escape

**Cross-check:** Part 37 (SU(3) condensate, Casimir 4/3 reproduced exactly)

#### [x] T11. Koide Angle and Tan — DONE (Part 122, Phase 90, 2026-07-06)

**Part:** 122 | **Phase:** 90
**Script:** `simulations/solver/t11_koide_tan.py`
**Doc:** `docs/research/koide_tan.md`
**Sudoku:** 10/10 PASS | **SymPy:** 6/6 PASS

**RESULTS:**
- Master formula [PDTP Original, DERIVED, SymPy VERIFIED]: delta = sqrt(2)*tan(theta_v)
  where theta_v = arccos(1/sqrt(3*Q)) is the flavor-vector partition angle.
- theta_v(leptons) = 45.000 deg -- exact match to U(1) critical angle (T2/Part 99).
  Connects delta=sqrt(2) [Part 53] to tan=1 [T2] via the master formula. [EXACT]
- Up quarks: delta_up = 1.759 ~ sqrt(3) = 1.732 (1.54% off pole mass; 1.15% off MS-bar).
  theta_v(up) = 51.2 deg, NOT 60 deg. NEGATIVE: T10's 60 deg gives delta=sqrt(6)~2.45.
- theta_0 = 2/9: no T10 angle within 4%. NEGATIVE -- confirms Part 91.

**What:** Koide formula has theta_0 = 2/9. Is tan(2/9) or arctan related to
Z_3 geometry? The Koide angle lives on the flavor circle -- does Brewster's
angle appear there?
**Cross-check with:** Part 53 (Z3-Koide derivation)

#### [x] T12. N_eff and Heat Kernel Tan — DONE (Part 129, 2026-08-09)

**What:** The Sakharov formula heat kernel a_1 coefficient involves curvature
integrals. Does n_PDTP = 1/alpha enter the heat kernel expansion? Could this
modify the 6*pi factor?
**Cross-check with:** Part 83 (N_eff = 6pi gap)

**Result [NEGATIVE, 12/12 Sudoku]:** No. n_PDTP = 1/alpha (Part 98) is sourced
by a gravitating mass M and is identically 1 when M=0. The Sakharov cutoff
Lambda = m_cond*c/hbar (Part 74b/83) has no M dependence, and the calculation
that fixes N_eff is conducted entirely in that M=0 vacuum -- there is no term
for a refractive-index correction to attach to. The N_eff gap (Part 83, range
[8,34], target 6*pi ~ 18.85) is exactly as open as before. Structurally
distinct from T7/Part 111's negative result (group vs phase velocity) --
recorded separately to avoid conflating the two mechanisms.
**Script:** `simulations/solver/t12_neff_refractive_index.py`
**Doc:** `docs/research/neff_sakharov.md` Section 10

---

### Phase 4 — Integration

#### [x] T13. Update Falsifiable Predictions — DONE (2026-08-09)

**What:** After T1-T6, update `docs/research/falsifiable_predictions.md` with
any new testable predictions (Brewster angle, transition redshift, etc.).

**Result:** Reviewed all of T1-T12 against the existing 14 predictions (plan
presented and approved first, per this file's "always plan before updating"
rule). Two genuinely new, non-redundant predictions added:
- **Prediction 15 — Gravitational Brewster Angle** (T4/Part 108): polarization-
  selective total transmission at tan(theta_B)=alpha1/alpha2 for the breathing
  mode; no analogous angle for tensor modes. Neutron-star-surface deviation
  ~4.1 deg (large, in-principle resolvable).
- **Prediction 16 — Leidenfrost Critical Exponents** (T6/Part 110): (beta,nu,
  gamma)=(1,1/2,1), a non-equilibrium laser-threshold universality class for
  the decoupling transition; testable via lab BEC/superfluid/Josephson analogs.
- **Prediction 10 refined** (T9/Part 113): exact horizon result m^2(phi_-)=
  omega_gap^2=2g -- phi_- and the breathing mode become the SAME excitation
  at a black hole horizon (not just another weak-field data point).

Everything else from T1-T12 correctly excluded as out-of-scope (internal
consistency checks / negative results / non-discriminating from GR) --
T1 (scalar-tensor deflection, resolved by SU(3)), T7 (Hawking T unchanged),
T8 (PPN matches GR), T2/T10/T11/T12 (geometry/mass-relation/theory results,
not observational discriminators).

#### [x] T14. Update Equation Reference — DONE (2026-08-09)

**What:** Add all new equations (T.1-T.14 and any derived during Parts) to
`docs/research/equation_reference.md`.

**Result:** Audited all T1-T12 Parts against equation_reference.md. Found
Parts 121 (T10, SU(3) group manifold tan) and 122 (T11, Koide angle and tan)
were missing ENTIRELY -- added both with full equation tables (Eqs 121.1-121.6,
122.1-122.5). All other tan-series Parts (98-113, 129) were already present
and correct. Also flagged (but did not fix, out of T14's tan-series scope):
Parts 119 (T46) and 120 (T47) from the separate Lambda-locking thread are
ALSO missing from equation_reference.md -- noted in the changelog for a
future pass.

#### [x] T15. Final Verdict and Summary — DONE (2026-08-09)

**What:** Write up the overall findings. Did tan reveal new physics?
Which predictions survived the full FCC + Wave check?
Does any tan result help constrain m_cond or derive G?

**VERDICT: tan revealed genuine new structure, but not a new mechanism or
a free-parameter resolution.** Specifically:

1. **A coherent geometric language unifying separate sectors.** The U(1)
   critical angle (45 deg, T2/Part99) and SU(3) critical angle (60 deg,
   T10/Part121) are the SAME diagnostic (phase mismatch where restoring
   force balances coupling force) applied to different gauge groups. The
   SU(3) angle independently reproduces the ALREADY-KNOWN Casimir factor
   4/3 = 1/sin^2(60deg) (Part 37) -- a nontrivial cross-check the tan lens
   did not have to pass, but did.
2. **One genuinely surprising cross-domain connection.** T11/Part122 found
   the Koide lepton mass formula's partition angle is EXACTLY 45 deg -- the
   identical U(1) gravitational critical angle from T2, despite Koide's
   formula living entirely in the particle-mass sector. This was not
   assumed or fitted; it fell out of the master formula delta=sqrt(2)*
   tan(theta_v). The quark sector and theta_0 did NOT show a matching
   connection (confirmed NEGATIVE, Part 122.4-122.5) -- so this is a real,
   specific, falsifiable-in-hindsight structural fact about leptons, not a
   general pattern being overfit everywhere.
3. **Two new falsifiable predictions** (T13, Predictions 15-16): the
   gravitational Brewster angle (polarization-selective GW transmission at
   a density interface) and the Leidenfrost critical exponents
   (beta,nu,gamma)=(1,1/2,1) for the decoupling transition -- both did not
   exist before this investigation.
4. **Three honest negative/confirming results** (T7, T8, T12): PPN
   parameters, Hawking temperature, and the Sakharov N_eff gap are all
   UNCHANGED by n_PDTP. This is valuable precisely because it was not
   guaranteed -- a wrong theory could easily have broken one of these
   well-tested GR results, and none did.

**Does tan constrain m_cond or derive G? NO.** Every tan result operates at
the level of geometric/critical-angle structure (dimensionless ratios,
angles, exponents) -- none of T1-T12 touch the m_cond hierarchy problem.
m_cond remains PDTP's one free parameter (A1, all perturbative paths
exhausted per Parts 29-35), exactly as before this investigation. T48/T49
(hierarchy reframe, Kuramoto connection) remain the open threads for that
separate problem, still low-priority/speculative pending T46 follow-up.

**Which predictions survived the full FCC + Wave check?** All 6 productive
Parts (T4, T6, T9, T10, T11, plus T13's integration) passed their own
Sudoku suites (10/10 to 12/12 each) and remain standing. No tan-derived
result was later found to contradict an established PDTP result.

**Summary table (T1-T12, T15 recomputed from the Status Summary table above):**
DONE productive: T4, T5, T6, T9(via T113 refinement), T10, T11 (6).
DONE constructive-negative/confirming: T1, T2, T3, T7, T8 (5).
DONE negative-but-informative: T12 (1).
Net: 0 physics reversals, 2 new falsifiable predictions, 1 unexpected
cross-domain connection (Koide/T2), 1 gap fully characterized (N_eff,
unaffected by tan). The tan investigation is CLOSED as productive.

#### [ ] T65. Backfill mathematical_formalization.md

**Status:** PENDING. Filed 2026-07-11 alongside a new CLAUDE.md rule requiring this
doc to be kept current going forward (see CLAUDE.md "Mathematical Formalization"
section).

**What:** `docs/research/mathematical_formalization.md` is the narrative,
step-by-step foundations document (distinct from the terse `equation_reference.md`
log, which has been kept current). It currently covers only the single-phase U(1)
Lagrangian (Euler-Lagrange for fields, Noether's theorem, sine-Gordon/Kuramoto
connections, weak-field Newtonian recovery, energy cost of decoupling) — roughly
Parts 1-20s. It stops **before** two of the framework's largest structural results:

- **Part 37 — SU(3) extension:** matrix field U(x), Z₃ vortices as quarks, 8 gluons
  from generators, the Wilson-loop coupling Re[Tr(Ψ†U)]/N, U(1) limit recovery.
- **Part 61 — Two-phase Lagrangian:** φ₊/φ₋ split, product coupling
  2g·sin(ψ−φ₊)·sin(φ₋), Newton's 3rd law derivation, biharmonic gravity, the
  reversed-Higgs φ₋ mode.

Both need full step-by-step derivation sections added, matching the existing
document's standard (every step shown, every established result cited, every new
result tagged PDTP Original, SymPy verification referenced where applicable —
per CODING_STANDARDS.md and the "Show Your Work" requirement in CLAUDE.md).

**Scope note:** this is a documentation-currency task, not new physics — the
derivations already exist (Parts 37, 61, and their many follow-ups) and are already
correct; this is about making the foundations document narratively complete and
pedagogically walkable end-to-end, the way Sections 1-9 currently are for the
single-phase case.

**Suggested approach (plan before starting, per the Problem-Solving Protocol):**
1. Add Section 12 (SU(3) extension) following the existing document's structure
   (prerequisites → Lagrangian → field equations → key results), citing Parts
   37-41.
2. Add Section 13 (Two-phase Lagrangian) similarly, citing Parts 61-63 and the
   16/16 re-derivation.
3. Decide whether later structural results (DM winding Part 116, Lambda-locking
   Part 119, CP violation Part 85/125) warrant their own sections too, or whether
   the doc should stay scoped to "foundations" with those left in their own
   research docs and only cross-linked.
4. Update the Table of Contents and Summary of Results (Sections 10-11) to match.

**Estimated effort:** LARGE — likely its own multi-session task given the chunking
rule (~100 lines per Edit/Write call) and the amount of material to backfill.
Do not start without a plan approved by the user first.

---

## Connection to the G Derivation Goal

The tan investigation connects to the G derivation in several ways:

1. **n_PDTP = 1/alpha:** If we can measure the refractive index of spacetime
   independently (e.g., via gravitational lensing precision), we get alpha,
   which constrains the coupling g, which constrains m_cond.

2. **Brewster angle:** If GW polarization splitting is observed, it gives the
   RATIO alpha_1/alpha_2 at a known density boundary — independent constraint
   on the coupling.

3. **Dark energy transition:** If tan = 1 at z ~ 0.7 is confirmed by DESI,
   it fixes the phase drift rate, which constrains g/H^2, which constrains g.

4. **Multi-layer model:** If frequency-selective gravitational shielding is
   possible (even in principle), it constrains the condensate's impedance
   properties, which constrain K and therefore m_cond.

None of these individually derive G, but they are **independent constraints**
on the coupling constant g and therefore m_cond = sqrt(hbar*c/G). Multiple
independent constraints may overdetermine the system — and that IS how you
derive a free parameter (Strategy A from Parts 29-35).

---

### Phase 4 — Moire Pattern Extension [SPECULATION] (2026-04-04)

**References:**
- Wolfram NKS Notes 10-7: https://www.wolframscience.com/nks/notes-10-7--moire-patterns/
- Wikipedia: https://en.wikipedia.org/wiki/Moir%C3%A9_pattern
- Local PDF: `assets/pdfs/moire pattern Note (b) for Visual Perception...pdf`

**Key Wolfram formulas relevant to tan investigation:**
```
Band spacing  = (1/2) * csc(theta/2) ~ 1/theta         (small angles)
Exact repeat  : tan(theta) = u/v   where GCD(u,v) = 1   (Pythagorean condition)
Minimum shift : {s, r} = {s, r} from u = r^2 - s^2, v = 2*r*s
```

**Critical connection to TODO_04:**
The Wolfram condition tan(theta) = u/v for exact moire periodicity gives a
PHYSICAL MEANING to the tan investigation:

- **T2 (tan=1 critical point):** tan(theta)=1 means u=v, i.e. GCD(u,v)=u >= 2
  -> NOT a primitive Pythagorean triple -> the moire pattern at tan=1 is
  NOT exactly periodic. It is at the boundary of lock-in vs drift.
  This makes tan(Delta)=1 (Delta=45 deg) the LOCK-IN THRESHOLD:
  below it (tan < 1), moire can lock to small-integer rational; above it,
  larger integers needed, harder to lock.

- **T11 (Koide angle):** Koide Q=2/3 from three Z_3 lattices. Three-grid
  moire exact repeat requires tan(theta_12)=u/v AND tan(theta_23)=p/q
  simultaneously. For 120 deg spacing: tan(120)=-sqrt(3) is irrational
  -> the three-grid moire is QUASIPERIODIC unless viewed mod Z_3.
  The Koide formula Q=2/3 may be the quasiperiodic average of the three-grid
  moire visibility function.

**New moire-specific tan items [ALL SPECULATION]:**

#### [x] M1. Pythagorean lock-in of alpha_EM [SPECULATION] -- DONE (2026-04-04)

**Result:** QUASIPERIODIC. No small-integer lock-in.
- tan(arccos(sqrt(alpha_EM))) = 11.663
- Smallest primitive pair: (23,2) -> 1/alpha = 133.25 (1.4% off -- not alpha_EM)
- Best accurate small pair: (35,3) -> 1/alpha = 137.11 (0.03% off; u=35 is NOT small)
- Conclusion: alpha_EM requires large integers to match. No Pythagorean lock-in.
- G1 in TODO_03 stays SPECULATION -- does NOT move to ACTIVE.
- Script output: `simulations/solver/outputs/moire_quick_checks.txt`

#### [x] M2. tan(theta_W) = u/v for Weinberg angle [SPECULATION] -- DONE (2026-04-04)

**Result:** INCONCLUSIVE / NOT NEEDED.
- tan(theta_W) = 0.5484; best small pair: (5,9) -> sin2=0.2358 (1.3% off)
- Most accurate compact pair: (17,31) -> sin2=0.2312 (0.006% off) -- but not small
- GUT angle sqrt(3/5) is already DERIVED from SU(5) group theory (Part 92, exact)
- Moire framing adds no predictive power beyond group theory result
- Script output: `simulations/solver/outputs/moire_quick_checks.txt`

#### [x] M3. Band spacing formula and PDTP condensate layers [SPECULATION] -- DONE (2026-08-30)

**Formula:** lambda_moire = (1/2) * csc(theta/2) * a  (a = lattice spacing)
  For C1/C2 boundary: theta = angle between gravitational and QCD condensate lattices
  lambda_moire = ? -- if this equals the evanescent depth from Part 89, that
  would be a non-trivial cross-check.
  Part 89: lambda_evan(C2) = 0.00245 fm; lambda_evan(C1) = 0.987 fm
  Can these be expressed as moire band spacings of two misaligned condensates?

**RESULT: DEGENERATE as posed, not a genuine cross-check.** Part 96's own
condensate lattice-spacing table (`condensate_layer_optics.md` Eq 96.1)
states its own starting point plainly: "Condensate lattice spacing = Compton
wavelength of gap mass" -- i.e. a = hbar*c/E_gap. Part 89's evanescent depth
(Eq 89.13) is lambda_evan = hbar/(m_gap*c), the SAME formula. So a = lambda_evan
**by construction**, at every boundary, not as a result to be tested -- they
are one formula wearing two names in two different sections of the project.
Given that, setting lambda_moire = (1/2)*csc(theta/2)*a equal to a and solving
for theta gives theta = 60 deg **exactly**, and (SymPy-verified) this solution
does not depend on the numeric value of a at all -- it would come out the
same at ANY boundary, any mass scale, because a cancels algebraically out of
the equation before theta is solved for. So this "check" cannot discriminate
between different physics; it was never capable of confirming or refuting
anything about QCD vs EW scales specifically.

**One genuinely separate observation, held to the same skepticism:** the
forced theta=60 deg happens to match Part 121/T10's INDEPENDENTLY-derived
SU(3) critical angle (tan(theta)=sqrt(3), reproducing the already-known 4/3
Casimir factor from Part 37 -- a completely different calculation, sharing no
formula with this one). Whether that is meaningful or coincidental is not
resolved here -- flagged for anyone revisiting this, but NOT claimed as a
finding, since the M3 side of the "coincidence" was mathematically forced
and therefore carries no evidential weight on its own.
**Script:** `simulations/solver/moire_quick_checks_m3_m4.py`. Log:
`simulations/solver/outputs/moire_quick_checks_m3_m4.txt`. 9/9 sanity checks PASS.
**Connection:** T5 (multi-layer stacks) -- each layer boundary has a moire
  angle; the evanescent depth may equal the moire band spacing.

#### [x] M4. Minimum displacement {s,r} and vortex winding [SPECULATION] -- DONE (2026-08-30)

**Wolfram:** Minimum displacement = {s, r} where u=r^2-s^2, v=2rs (Pythagorean generator)
  This {s,r} pair is the smallest lattice vector that leaves the moire unchanged.
  In PDTP: winding number n = m_cond/m_particle (Part 33).
  Is n = r - s or r + s for some Pythagorean generator pair?
  For electron: n = m_P/m_e ~ 2.4e22 -- too large for small integers.
  For QCD condensate: n = m_cond_QCD/m_quark ~ 367MeV/5MeV ~ 73 -- small!
  Check: is 73 = r^2 - s^2 for small integers? 73 = 37^2 - 36^2 = (37-36)(37+36) = 1*73.
  Primitive pair: (r,s) = (37,36), u=73, v=2*37*36=2664. GCD(73,2664) = 1. YES.
  This means quark winding n=73 MAY correspond to a primitive Pythagorean moire.

**RESULT: NEGATIVE.** The (37,36) pair is not a hit, it is a mathematical
inevitability. SymPy-proved for GENERAL odd N (not just checked at 73): the
pair (r,s) = ((N+1)/2, (N-1)/2) always satisfies r^2-s^2=N, and since r-s=1
identically, gcd(r,s)=1 always too -- ANY odd number produces a "primitive
Pythagorean pair" this way, automatically, with zero physics content. Worse
for the hypothesis: since 73 is prime (confirmed, not assumed), u=r^2-s^2=
(r-s)(r+s)=73 has only ONE integer factorization (1x73), so (37,36) is not
just an inevitable pair, it is the UNIQUE possible pair (brute-force search
confirmed no other pair exists for r up to 200) -- and by M1/M2's own
established standard for what counts as "small" (their smallest confirmed
hits used pairs with values in the 2-30 range), (37,36) is not small. No
evidence either way survives this check; consistent with M1/M2's own
already-negative pattern.
**Script:** `simulations/solver/moire_quick_checks_m3_m4.py`. Log:
`simulations/solver/outputs/moire_quick_checks_m3_m4.txt`. 9/9 sanity checks PASS.

**NOTE:** M1-M4 are all SPECULATIVE. Before investigating as full Parts,
run the simple numerical checks (marked **Compute:** above) to see if the
moire angle hypothesis survives first contact with numbers. These are
10-minute calculations, not full Parts. Do them first.

**First priority check (5 min):**
  arccos(sqrt(alpha_EM)) = ?  Is tan of this angle a small rational number?
  If yes: G1/M1 moves to ACTIVE. If no: moire is probably coincidental for alpha_EM.

---

### Phase 5 — Open Questions from Parts 98-99 and L4/Tensor Work (2026-04-06)

#### [x] T16. Two-Phase Factor-of-2 Lensing Check — DONE (Part 100, 2026-04-06)

**Part:** 100
**Script:** `simulations/solver/two_phase_lensing.py` (Phase 68)
**Doc:** `docs/research/two_phase_lensing.md`
**Sudoku:** 9/10 PASS

**RESULTS (NEGATIVE):**
- Two independent factor-of-2s identified [Eq 100.1, DERIVED, PDTP Original]:
  (A) G_eff = 2*G_bare (Part 61): acts on MATTER FORCE (Newton's 2nd law); already in G_N
  (B) Lensing gap: PDTP scalar missing g_ij (spatial curvature); acts on PHOTON PATH
- theta_GR/theta_PDTP = 2, invariant under any G rescaling [Eq 100.2, SymPy VERIFIED]
  - Case 1 (G_bare=G_N/2): 0.4375" vs 0.875", ratio=2 (gap worse)
  - Case 2 (G_eff=2*G_N): 1.75" vs 3.50", ratio=2 (GR also doubled)
  - Case 3 (standard G_N=G_eff, correct): 0.875" vs 1.75", ratio=2
- Bergmann-Wagoner theorem: any scalar field (including phi_+) gives PPN gamma=0
  => lensing factor = 1+gamma = 1 (not 2); measured gamma = 1+/-2e-5 (Cassini 2003)
- Fix requires SU(3) spatial metric (Part 75): g_ij from Tr(dU_dag dU) [SPECULATIVE]

#### [x] T17. n = sqrt(2) Observable Signature — PRIORITY 17 — DONE (Part 130, 2026-08-09)
**Source:** Part 99 open question 2; tan_critical_point.md Sec 10.2
**What:** Near a compact object where Delta_+ approaches pi/4, n_PDTP = sqrt(2) = 1.414.
Is this distinguishable from standard GR lensing at that density?

**RESULT:** The original note's own math above was WRONG -- it used u=1-alpha
(should be u=(1-alpha^2)/2) and got r=0.293*r_S "inside the Schwarzschild
radius." The correct, exact answer is **r = 2 r_S** (SymPy solve, Eq 130.1),
well outside the horizon and inside the EHT-probed range (1.5-6 r_S) as
originally hoped. BUT: a general GR fact (turning-point b(r0)=r0/sqrt(g_tt(r0)),
independent of g_rr, Wald 1984) means PDTP's scalar n_PDTP(r)*r is algebraically
IDENTICAL to the true GR turning-point formula (Eq 130.4) -- so the photon
sphere (1.5 r_S) and EHT shadow radius (b_crit=3*sqrt(3)GM/c^2) match GR
EXACTLY, even in the unmodified scalar theory (Eq 130.6-130.7). The n=sqrt(2)
point itself (r=2 r_S) is not a turning point or shadow boundary -- it carries
no EHT-isolable signature. Independently re-derived Part 98's known weak-field
factor-of-2 via orbit-equation perturbation theory (Eq 130.8-130.10), confirming
it (not new, but now derived by a second method). Neutron stars (typical
compactness C~0.17-0.19) fall well short of the C=0.25 needed for n=sqrt(2);
the Buchdahl bound (C=0.444) permits it in principle for unusually compact NS.
**Verdict: NEGATIVE for T17's original premise (no new signature at n=sqrt2),
but a genuine new POSITIVE byproduct (EHT shadow-size prediction survives
exactly in the pure scalar theory).** 16/16 Sudoku PASS.
**Script:** `simulations/solver/t17_photon_sphere_signature.py`.
**Doc:** `docs/research/pdtp_refractive_index.md` Section 12.
**Not touched:** falsifiable_predictions.md -- no NEW falsifiable difference
from GR was found (the result is "matches GR", not "differs from GR"), so no
new numbered Prediction was added; the existing factor-of-2 discussion in
Part 98 Sec 5.3 already covers the weak-field side of this.

**Key questions (original, now answered above):**
- At what mass density does Delta reach pi/4? Use alpha = 1/sqrt(2) => GM/(rc^2) = 1 - 1/sqrt(2) ~ 0.293.
  => r = GM/(0.293 * c^2) = 0.293 * r_S (inside the Schwarzschild radius!) -- probably not observable.
  **[CORRECTED, Part 130: this arithmetic was wrong; correct answer is r=2 r_S, see above.]**
- For neutron stars (r ~ 3 r_S): Delta_+ is small but nonzero. What is n there?
- Could the n=sqrt(2) signature appear in gravitational lensing of light near black holes?
  VLBI/EHT images of M87* and Sgr A* probe r ~ 1.5-6 r_S.
**Cross-check with:** Part 98 (TIR table: n=3.3 at r=1.1*r_S), Part 73 (Kerr metric PDTP;
NOT re-derived here -- Kerr spin flagged as future work, Sec 12.11)
**Effort:** Medium (need to map density to Delta; VLBI data comparison).

#### [x] T18. Two-Phase Delta_- Crossover Near Dense Matter — PRIORITY 18 — DONE (Part 131, 2026-08-09)
**Source:** Part 99 open question 3; tan_critical_point.md Sec 10.3
**What:** The reversed Higgs (Part 62) gives phi_- a mass near matter: m^2 = 2g*Phi.
Does Delta_- ever reach pi/4 inside a neutron star or white dwarf?

**RESULT:** Re-deriving Part 61's own product-form potential directly
(V_eff = -2g*sin(Delta_+)*sin(phi_-)) and extremizing it shows the TRUE
minimum is at phi_- = pi/2 for ANY Delta_+ > 0 -- independently reproducing
Part 119's cosmological "true vacuum at pi/2" result via a much simpler,
purely static argument (no beta parametrization or Part 117 quartic needed).
This also reconciles Part 62's original mass claim: its "V''(0)" was
evaluated at phi_-=0, which is NOT a stationary point once Delta_+>0 (dV/dphi_-
there is nonzero) -- that quantity describes the initial tachyonic push
rate, not a stable particle mass. The correct stable mass is
m^2(Delta_+)=2g*sin(Delta_+) at phi_-=pi/2. **Delta_- = pi/2 - phi_- has NO
pi/4 crossover** -- checked directly (dV/dphi_- at phi_-=pi/4 is nonzero for
Delta_+>0) and explained structurally: Delta_+'s pi/4 crossover (Part 99)
is a regime boundary within a monotonic "how decoupled" dial; Delta_- is a
displacement from a single stable equilibrium, a different kind of variable
in a differently-shaped potential -- no analogous feature exists.
**Key Questions (a) and (c) answered: NO stable crossover; NOT the same
kind of state as the pi/2 equilibrium.**
While scoping Key Question (b) (NS f/g-mode comparison), found Part 62's
g=omega_gap uses the same units shortcut T51/Part128 already flagged and
fixed elsewhere (forced [g]=1/s^2, not 1/s); two "corrected" candidates
(omega_gap^2 vs Part 119's own g_dyn) differ by ~60 orders of magnitude for
a NS-scale calculation -- reported as OPEN rather than guessed at, and
**filed as new TODO_05 T68** (a project-wide g-units audit, out of T18's
scope). 13/13 Sudoku PASS.
**Script:** `simulations/solver/t18_delta_minus_crossover.py`.
**Doc:** `docs/research/phi_minus_local_mass_and_crossover.md` (new).

**Key questions (original, now answered above):**
- Delta_- equation of motion: involves phi_- mass term from Part 62.
  Is there a stable crossover state Delta_- = pi/4 inside dense objects?
  **[ANSWERED: NO, see above.]**
- If Delta_- = pi/4 inside a neutron star: n_- = sqrt(2). Would this affect
  neutron star oscillation modes (f-modes, g-modes)? **[OPEN, blocked on TODO_05 T68.]**
- Connection: reversed Higgs at equilibrium phi_- = pi/2 (Part 62) vs crossover pi/4.
  Are these the same thing or different states? **[ANSWERED: different kinds of concept
  entirely; pi/2 is the potential's genuine minimum, pi/4 is not special at all.]**
**Cross-check with:** Part 61-62 (two-phase, reversed Higgs), Part 99 (crossover analysis)
**Effort:** Medium (extend Part 62 to solve for Delta_- profile inside dense star).

#### [x] T19. L_4 SymPy Verification and b Quark Check — PRIORITY 19 — DONE (Part 132, 2026-08-09)
**Source:** pdtp_lagrangian4.md -- all results currently [SPECULATIVE, unverified]
**What:** L_4 = L_kinetic + L_self + L_cross adds J_{ab} cos(phi_a - phi_b) inter-layer coupling.
Verify ALL results with SymPy before accepting any as [DERIVED].

**RESULT:** Two independent errors found and corrected in the previously-
unverified document. (1) FE1-FE3 had a sign error on the J-coupling terms
(direct SymPy differentiation of L_4 disagrees; validated first against
FE4, which the doc got right and SymPy reproduces exactly). The doc's
separately-stated mass matrix was, despite this, already correct -- now
confirmed independently, and generalized: the mass matrix is exactly a
weighted graph Laplacian (standard graph theory), proving the "exact zero
eigenvalue + positive rest" claim in general, for any number of condensate
layers. (2) The doc's stated full-3x3 eigenvalues (34 TeV/178 TeV) failed a
basic trace(M^2) sanity check by 10 orders of magnitude -- recomputed
correctly (~1.35e9 GeV / ~3.13e10 GeV). Also found the doc's own
"conservation law" claim was a tautology as literally stated; the real,
stronger, previously-unstated result is FE1+FE2+FE3+FE4=0 identically (the
Goldstone equation of motion across all 4 fields, not just 3).
Task 4 (product rule vs geometric mean): the doc's own cited analogy
(Lorentz-Berthelot) actually supports the geometric mean, sqrt(g_a*g_b)/2,
not the product rule g_a*g_b/2 it adopted -- using the geometric mean gives
m_23=2.00 GeV (52% off the b quark) vs the product rule's 4.01 GeV (4% off).
Since both are equally valid dimensionally, this means the product rule
looks like it was picked BECAUSE it gives an appealing number, not derived
independently -- the headline "4% match" is downgraded from finding to open
question. Task 5 (what is the C2-C3 mode) is now lower priority given this.
15/18 Sudoku PASS (3 expected fails documenting the sign-error finding).
**Script:** `simulations/solver/lagrangian4.py`.
**Doc:** `docs/research/pdtp_lagrangian4.md` (status upgraded to PARTIALLY VERIFIED).

**Tasks (in order, now answered above):**
1. SymPy: Euler-Lagrange equations for all 4 fields (phi_1, phi_2, phi_3, psi) from L_4.
   Verify signs, symmetry, conservation law sum_a FE_a. **[DONE -- sign error found+fixed.]**
2. SymPy: Mass matrix M^2 eigenvalues (3x3 Laplacian). Verify zero eigenvalue (Goldstone) exact.
   **[DONE -- confirmed exact, generalized to n condensates via graph Laplacian.]**
3. SymPy: Isolated C2-C3 mode mass = sqrt(g_2 * g_3) with J_{23} = g_2*g_3/2.
   Numerical: sqrt(0.200 GeV * 80.4 GeV) = 4.010 GeV vs m_b = 4.18 GeV (4% off).
   **[DONE -- confirmed numerically, and self-consistent with the full 3x3 limit.]**
4. Physical argument: why does J_{ab} = g_a*g_b/2 (product rule) rather than sqrt(g_a*g_b)/2
   (geometric mean rule)? Is there a symmetry or dimensional argument?
   **[ANSWERED: no such argument found; doc's own analogy favors the OTHER rule. OPEN.]**
5. What IS the C2-C3 mode physically? It has no colour charge, no spin-1/2.
   Candidates: scalar meson near 4 GeV? Chi_c(1P) charmonium at 3.51 GeV? B meson (5.28 GeV)?
   **[DEFERRED -- lower priority given (4)'s finding weakens the motivation.]**
**Cross-check with:** L_1/L_2/L_3; Part 37 (SU(3) condensate); Part 53 (Koide Z3)
**Effort:** Medium-High (new script needed: lagrangian4.py)

#### [x] T20. L_4 Goldstone Mode — What Is It? — PRIORITY 20 — DONE (Part 133, 2026-08-09)
**Source:** pdtp_lagrangian4.md Sec "Goldstone mode"
**What:** L_4 has a global U(1) symmetry phi_a -> phi_a + c for all a simultaneously.
This guarantees one massless Goldstone mode. What is this mode physically?

**RESULT:** chi = (phi_1+phi_2+phi_3+psi)/2 (extending T19/Part132's exact
FE1+FE2+FE3+FE4=0 result to the field level) is a genuine, independent,
freely-propagating massless scalar: canonical kinetic term, no mixing with
the other 3 shape degrees of freedom, and dV/dchi=0 proven EXACTLY (not
just linearized/near-vacuum) since every L_4 potential term is a
cos(DIFFERENCE), so the chi-shift cancels algebraically at all orders.
**NOT the graviton** -- pure representation theory (Goldstone theorem gives
spin-0 for scalar fields; graviton is spin-2), no dynamics needed to settle
this. **NOT Part 61's phi_-** -- different field content (chi spans 4
fields across 3 condensate layers + matter; phi_- spans only 2 fields
within C1's bulk/surface split) -- though the SAME underlying mechanism
(any cos-difference Lagrangian has an automatic center-of-mass zero mode)
recurs at both levels, a nice structural unification even though the modes
themselves differ. **Higgs mechanism not applicable** to L_4 as currently
written -- the symmetry is global (constant c), no gauge field exists in
L_4 for chi to be eaten by; would need a distinct future gauging extension.
11/11 Sudoku PASS.
**Script:** `simulations/solver/t20_goldstone_identification.py`.
**Doc:** `docs/research/pdtp_lagrangian4.md`, "Physical meaning of the Goldstone mode" section.

**Key questions (original, now answered above):**
- Is this the graviton? **[NO -- spin-0 vs spin-2, representation theory.]**
- Is this phi_- from Part 61? **[NO -- different field content, though same recurring mechanism.]**
- Is the Goldstone eaten by a gauge field? **[NOT APPLICABLE -- L_4 has no gauge field, symmetry is global.]**
**Cross-check with:** Part 61 (phi_- as surface Goldstone), Part 62 (reversed Higgs mass)
**Effort:** Low-Medium (mostly conceptual; SymPy eigenvalue check is fast)

#### [x] T21. Condensate Compression as Spatial Curvature — DONE (Part 101, 2026-04-06)

**Part:** 101
**Script:** `simulations/solver/condensate_compression.py` (Phase 69)
**Doc:** TBD (research doc not yet written)
**Sudoku:** 9/10 PASS

**RESULTS (MIXED):**
- omega_eff^2 = g*alpha: condensate slows near matter [Eq 101.1, DERIVED, SymPy PASS]
- n(r)/n_0 = 1+u: density increases (Thomas-Fermi compression) [Eq 101.2, DERIVED]
- **NEGATIVE:** Static condensate -> conformally flat metric -> n_eff = 1 -> ZERO lensing [Eq 101.3]
  Both g_00 and g_ij scale as (1+u) -> ratio = 1 -> no refraction
- **KEY INSIGHT:** Lensing requires FLOW, not just compression [Eq 101.4]
  PG flow (v=sqrt(2GM/r)) breaks conformal symmetry -> full GR lensing
  Linearized PDTP velocity 12 orders too small -> flow NOT derived from PDTP EOM
- Black hole unification: alpha->0, omega->0, n->inf = TIR = frozen condensate [Eq 101.5]
- **OPEN PROBLEM:** Does PDTP condensate flow at v=sqrt(2GM/r) near a star?
  If yes: gamma=1, lensing=1.75". If no: need SU(3) or another mechanism.

**Source:** User notes 2026-04-06; Part 100 (lensing gap NEGATIVE)

**Core idea (user):** Matter coupling to the condensate SLOWS the condensate oscillation.
The slowed oscillation forces the condensate density to increase (compress) to maintain
c_s = c. The increased density creates a non-flat spatial metric: g_ij != delta_ij.
This is the spatial curvature missing from PDTP scalar lensing -- and it comes for free
from the SAME mechanism that gives gravitational time dilation.

**Mechanism chain [to be DERIVED]:**
  (1) Matter couples: psi-phi = Delta > 0, so alpha = cos(Delta) < 1
  (2) Condensate oscillation slows: omega_eff^2 = g*cos(Delta) = g*alpha  [linearize phi EOM]
      Near equilibrium: Box(delta_phi) = -g*alpha*delta_phi => omega_eff = sqrt(g*alpha)
  (3) Part 34: c_s = c always. c_s^2 = g_eff*rho/m = c^2 = const.
      If g_eff = g*alpha decreases, rho must increase: rho(r) = rho_0/alpha(r)
  (4) Acoustic metric spatial part [Unruh 1981]: g_ij = (rho/c_s)*delta_ij
      => g_ij = (rho_0/c)*(1/alpha)*delta_ij
      Weak field [1/alpha ~ 1+u, u=GM/(rc^2)]: g_ij ~ (1+u)*delta_ij
  (5) PPN spatial metric g_ij = (1 + 2*gamma*u)*delta_ij => gamma_PDTP = 1/2
      (Not 1 yet -- but massively better than gamma=0 from Part 100)
  (6) Black hole limit: alpha->0, omega_eff->0 (frozen), rho->inf, n->inf => TIR [Part 98]
      The condensate FREEZES at the horizon. Time stops = oscillation stops. Same thing.

**Key questions:**
1. Confirm omega_eff^2 = g*alpha from linearized EOM (SymPy, straightforward).
2. Confirm rho = rho_0/alpha from Part 34 c_s=c + g_eff = g*alpha (check self-consistency).
3. Derive g_ij = (rho_0/c)*(1/alpha)*delta_ij from Unruh acoustic metric + rho(r).
4. Compute PPN gamma: g_ij = (1+2*gamma*u)*delta_ij => what is gamma?
   Expected: gamma = 1/2 from single-phase. Does two-phase (Part 61 factor-2) give gamma=1?
5. What closes the gamma=1/2 -> 1 gap?
   - Two-phase: phi_+ and phi_- both compress? Does phi_+ alone give gamma=1/2, both give gamma=1?
   - Connection to Part 61 G_eff=2*G_bare: same factor of 2?
6. Black hole check: at r=r_S, alpha=0, omega_eff=0, rho->inf. Is this consistent with
   TIR (n->inf, Part 98) and the acoustic horizon (Part 73)?
   All three descriptions (TIR, frozen condensate, infinite density) should be EQUIVALENT.
**Cross-check with:** Part 34 (c_s=c, rho self-consistency), Part 73 (acoustic metric),
Part 98 (n=1/alpha, TIR), Part 100 (Bergmann-Wagoner), Part 61 (G_eff=2*G_bare factor-2)
**Outcome if gamma=1/2 confirmed and factor-2 closes to gamma=1:**
  Lensing gap CLOSED in U(1)/two-phase PDTP without SU(3).
  Mechanism: matter coupling slows oscillation -> density increase -> spatial curvature.
  Bergmann-Wagoner evaded: g_ij is NOT delta_ij (density-dependent correction).
  Black hole = frozen condensate = total internal reflection. Three views, one object.
**Outcome if gamma=1/2 and factor-2 does NOT close to 1:**
  SU(3) (Part 75) still required for full lensing. But gamma=1/2 is already new physics --
  intermediate between scalar (0) and GR (1), potentially measurable.
**Effort:** Low-Medium (mostly algebra + SymPy; no new Lagrangian needed).

---

### Phase 5 — Three-Lens Exploration for Missing PDTP Terms (2026-04-07)

**Source:** User request 2026-04-07 after T3 PARTIAL verdict.
**Motivation:** T3 (Part 102) confirmed that the current PDTP Lagrangian
L = (1/2)(d phi)^2 + sum_i (1/2)(d psi_i)^2 + sum_i g_i cos(psi_i - phi)
is structurally complete for the harmonic limit but does NOT predict:
- the matter density fraction Omega_m,0 ~ 0.31
- the dark energy w_a ~ -0.75 (factor 5 too small at m=0)
- a redshift z-scale for the dark energy transition
- the Initial value Delta_0 (no selection principle)
- the lensing factor of 2 (Part 100 NEGATIVE: scalar -> gamma=0)

The hypothesis is that the Lagrangian is **missing one or more terms**.
T22-T24 use three different lenses to identify candidate missing terms.

#### [x] T22. Platonic Solids Lens — Topology / Discrete Symmetry — DONE (PARTIAL)

**Part:** 105 (Phase 73)
**Script:** `simulations/solver/t22_platonic_lens.py`
**Doc:** `docs/research/platonic_solids_lens.md`
**Sudoku:** 10/10 PASS | **SymPy:** 8/8 VERIFIED
**Verdict:** PARTIAL — 1 DERIVED (textbook), 3 NEGATIVE, 1 CATALOG

**Results:**
- Euler formula V-E+F=2 verified for all 5 solids; 3 distinct non-A/D groups
  (tetrahedral A_4, octahedral S_4, icosahedral A_5) [Eq 105.1, DERIVED]
- McKay: SU(2) finite subgroups <-> ADE Dynkin; 3 exceptional E groups
  (E_6/E_7/E_8) <-> 3 non-cyclic/non-dihedral Platonic [Eq 105.2, CATALOG]
- **N_c = 3 DERIVED from Z_3 center of SU(3)** [Eq 105.3, textbook]:
  Baryon psi1*psi2*psi3 is Z_3-invariant -> exactly 3 quarks per baryon
- Y-junction n=3 is selected by Z_3 center, NOT by planar force balance
  (any n>=3 works) or energy (E(n)=1/n monotone decreasing) [Eq 105.4, DERIVED]
- **N_gen = 3 NOT derivable from Platonic arithmetic** [Eq 105.7, NEGATIVE]:
  No ratio of Platonic group orders gives 3 (S_4/A_4=2, A_5/A_4=5, A_5/S_4=2.5)
- **K_0 = 1/(4 pi) NOT a lattice coordination** [Eq 105.5, NEGATIVE]:
  4 pi irrational; Z integer; FCC best gap 4.5%. K_0 origin = 3D solid angle
- **Lambda/M_P^4 ~ 10^-122 NOT phi^n for natural n** [Eq 105.6, NEGATIVE]:
  Natural candidates (|A_5|, dim(E_8), |2I|, 2*dim(E_8)) all fail by >19 decades

**Key reframe:** N_c = 3 (Z_3 structural, DERIVED) and N_gen = 3 (empirical,
OPEN) are DIFFERENT QUESTIONS. The "three" in each has a different origin.
Platonic lens makes this distinction clean.

**Outcome:** Confirms Part 37 (N_c from Z_3) and Part 54 (Lambda free parameter).
No new free parameter fixed. Expected going in (most speculative of T22-T24).
**Open:** N_gen = 3 needs non-discrete-symmetry input (topology of compactified
extra dimensions, Koide-generalisation, or anomaly-cancellation UV completion).

#### [x] T23. Hilbert Space Lens — sin^2 Second Fourier Harmonic — DONE (PRODUCTIVE)

**Part:** 104 (Phase 72)
**Script:** `simulations/solver/t23_sin2_term.py`
**Doc:** `docs/research/sin2_hilbert_term.md`
**Sudoku:** 10/10 PASS | **SymPy:** 9/9 VERIFIED
**Verdict:** PRODUCTIVE — new physics, new prediction, w_a NOT resolved

**Results:**
- Fourier analysis: V(Delta) = sum a_n cos(n*Delta); sin^2 is the n=2 harmonic [Eq 104.6]
- Field equations: Box(phi) = g sin(D) - lambda sin(2D); momentum conserved exactly [Eq 104.2]
- **PITCHFORK BIFURCATION:** At lambda = g/2, ground state shifts from D=0 to
  D* = arccos(g/(2*lambda)). This is PERMANENT PARTIAL DECOUPLING. [Eq 104.3-104.4]
  - alpha* = g/(2*lambda) < 1 when lambda > g/2
  - Phase diagram: standard PDTP (lam<g/2) vs partially decoupled (lam>g/2)
- **w_a: CANNOT REACH -0.75.** Best w_a = -0.075 (factor 10 off). Slow-roll is the
  bottleneck, not the potential shape. Same structural limit as T3. [Eq 104.5]
- Physical meaning: sin^2(D) = |Im<psi|phi>|^2 = cross-polarization intensity
- Two-phase: compatible; adds -lambda sin(2*Sigma) sin(2*phi_-) [vanishes in vacuum]
- Natural origin: phi_- fluctuations at 1-loop generate this harmonic
- **NEW PREDICTION:** If lambda >= g/2, G_eff = G*alpha*. Testable via lunar laser ranging.
**Open:** lambda undetermined (new free parameter); density-matrix and U(2) promotion deferred.

#### [x] T24. Backward GR -> PDTP Lagrangian — Reverse Engineering — DONE (CONSTRUCTIVE NEGATIVE)

**Part:** 103 (Phase 71)
**Script:** `simulations/solver/t24_gr_reverse.py`
**Doc:** `docs/research/gr_reverse_pdtp.md`
**Sudoku:** 10/10 PASS | **SymPy:** 8/8 VERIFIED
**Verdict:** CONSTRUCTIVE NEGATIVE

**Results:**
- phi_PG(r) = -(4/3)(m_cond/hbar)*sqrt(2GM*r) [Eq 103.1]: PG phase field ~ r^(1/2)
- Lap(phi_PG) != 0 in vacuum [Eq 103.2]: condensate flows inward (not field-free)
- Delta_gamma = 1 [Eq 103.3]: scalar gives gamma=0, GR gives gamma=1
- theta_GR/theta_scalar = 2 exactly [Eq 103.4]: the lensing factor-of-2
- R_acoustic contains (d^2 phi)^2 higher-derivative structure [Eq 103.5]
  -- higher-derivative scalar CAN fix g_00 but CANNOT fix g_ij
- DOF counting [Eq 103.6]: g_ij needs 6 DOF; SU(3) has 8 (minimal group)
- Minimum fix = Part 75: g_mu_nu = (1/3)Tr(dU^dag dU) [Eq 103.7]
- Three alternatives REJECTED: (A) Brans-Dicke (circular), (B) higher-derivative
  scalar (DOF counting), (C) Nordstrom (gamma=-1)
- ADM orphan: lapse N and shift N^i mapped by phi; g_ij = FLAT (the gap)
- Architecture: L_full = L_PDTP_U1(time sector) + L_SU3(space sector)
**Priority:** High (most concrete path to closing Part 100 lensing gap).

#### Connection table for T22-T24

| Open issue | T22 (Platonic) | T23 (Hilbert / sin^2) | T24 (GR reverse) |
|------------|----------------|------------------------|-------------------|
| w_a tension (T3) | low | medium | low |
| No z-scale (T3)  | low | medium | low |
| Omega_m ~ 30%    | medium | low | low |
| 3 generations    | high | medium | low |
| gamma=1 lensing  | low | low | **high** |
| Hierarchy problem | low | medium | low |

**Proposed execution order (subject to user choice):**
1. T24 first -- most concrete, addresses a known NEGATIVE (Part 100)
2. T23 second -- can add a verifiable Lagrangian term
3. T22 third -- most speculative, only after T23/T24 reveal the symmetry needed

**Common deliverable per task:**
- Plan first (already in this TODO entry)
- Research doc with Plain English + step-by-step derivation
- SymPy verification of any new equations
- Sudoku consistency check (10 tests)
- TODO_04 + equation_reference updates

---

### Phase 6 — Cross-Framework Investigations (2026-04-11)

#### [x] T25. String Theory and PDTP — Graviton Comparison — DONE (Part 134, 2026-08-30)

**RESULT:** Comparison doc written (`docs/research/string_theory_comparison.md`).
Key Question 1 (graviton): structurally analogous (both force spin-2 from an
internal-consistency requirement on a more fundamental object -- string
worldsheet Weyl-anomaly cancellation vs. SU(3) condensate fluctuations,
Part 75) but not mechanistically transferable; PDTP's own path to full
nonlinear GR recovery (Part 86) has to be walked on its own terms.
Key Question 2 (Regge slope constraining m_cond): computed cleanly,
**NEGATIVE for a structural reason, not a numerical one** -- PDTP's own
sigma_SU(3)=0.173 GeV^2 (Part 38) and the resulting alpha'=0.920 GeV^-2 both
belong entirely to the QCD condensate layer (tied to m_cond_QCD=367 MeV,
Part 37), which has NO established relationship anywhere in the framework to
the gravity layer's m_cond=m_Planck (ratio 3.3e19) -- the Regge slope relation
was never wired to the quantity in question, regardless of what number comes
out. Key Question 3 (extra dims/moduli): no meaningful parallel -- PDTP has
no compactification geometry behind m_cond/Lambda. Key Question 4 (landscape):
same philosophical shape (internal consistency doesn't guarantee uniqueness)
but PDTP's "landscape" is 2 free parameters, not ~10^500+ -- string theory's
scale comes specifically from flux combinatorics PDTP has no analogue of.
Key Question 5 (T/S-duality vs phi_+/phi_-): **NEGATIVE** -- T/S-duality are
exact equivalences BETWEEN two distinct theory descriptions; phi_+/phi_- is
a linear change of variables WITHIN one Lagrangian (Part 61) -- superficial
resemblance only, does not hold up.
**Script:** `simulations/solver/t25_string_theory_comparison.py` (the one
quantitative piece, Key Question 2; rest is sourced literature comparison
per the task's own "Medium effort, mostly literature review" scope).
**Doc:** `docs/research/string_theory_comparison.md`.

**Part:** 134
**What:** Investigate how string theory derives general relativity (graviton as
massless spin-2 closed string excitation; Weyl anomaly cancellation forces
Einstein equations). Compare the mechanism to PDTP's SU(3) graviton (Part 75-76).
Identify whether string theory tools can fix or constrain PDTP's open gaps.

**Key questions:**
1. Graviton comparison: string theory spin-2 from worldsheet consistency vs
   PDTP spin-2 from SU(3) condensate fluctuations. Same logic (consistency
   forces GR) — how deep does the parallel go?
2. Regge slope: string tension sigma = 1/(2*pi*alpha') relates string tension
   to graviton spectrum. Compare to PDTP sigma_SU(3) = 0.173 GeV^2 (Part 38).
   Does the Regge trajectory formula constrain m_cond?
3. Extra dimensions: string theory requires D=10 (or 11 for M-theory).
   Compactification on Calabi-Yau gives moduli = free parameters.
   Parallel: PDTP's free parameters (m_cond, Lambda) — are they analogous
   to string moduli? Does this mean PDTP also needs compactification?
4. Landscape problem: string theory has ~10^500 vacua (no unique prediction).
   PDTP has the same issue: G = hbar*c/m_cond^2 with m_cond free (Part 35).
   Is this a universal feature of any framework that derives GR?
5. Can string theory's T-duality or S-duality inform PDTP's two-phase
   system (+cos/-cos)? The phi_+ / phi_- duality (Part 61) resembles
   strong/weak duality.

**Expected effort:** Medium. Mostly literature review + comparison tables.
**Likely outcome:** Comparison doc showing parallels and divergences.
Possible [DERIVED] Regge slope constraint on m_cond. Likely conclusion:
string theory and PDTP solve the same problem (derive GR) via different
routes, with the same unsolved landscape issue.
**Priority:** Low (depends on T24 completing first; no immediate gap it closes).

#### [x] T26. Bob Lazar Truth Table — Decoupling Phenomenology — DONE (Part 135, 2026-08-30)

**RESULT:** Full truth-table doc: `docs/research/lazar_truth_table.md`.
Script: `simulations/solver/t26_lazar_truth_table.py`. Key findings:
(1) "Gravity amplification" (C3) has no home in the current Lagrangian —
alpha=cos(psi-phi) is bounded to <=1, so literal amplification beyond
normal coupling is structurally impossible; the closer-fitting mechanism
is local phase-gradient steering + decoupling (matches Lazar's own "not
propulsion, geometry" description, C5). (2) The "three emitters at the
base" claim (C4) has an EXACT, independently re-verified structural
match: Part 71 Sec 5.1-5.2's Z3 three-source cancellation gives phi-
independent zero coupling at the centre of three 120-degree-spaced
sources -- re-checked numerically here across 12 phi values (max
|<alpha>| = 1.0e-16) -- flagged explicitly as a topological coincidence,
not evidence, since 3-fold symmetry is also the mundane engineering
default. (3) Energy budget (Key Q3) is NEGATIVE, decisively: the stale
10 kW/ton (Part 28b) figure is superseded; Part 71's boundary-layer
mechanism costs E_layer = 9.04e76 J for a 1 kg object (computed here for
the first time as an explicit number) -- ~7 orders of magnitude beyond
the ENTIRE OBSERVABLE UNIVERSE's mass-energy, and dozens of orders of
magnitude beyond any practical device budget; bulk decoupling alone
costs ~35% of rest-mass energy. Frequency gap re-derived independently:
f_gap = 2.95e42 Hz vs current tech ~1e15 Hz -> ratio 2.95e27 (confirms
Phase 7's rounded "~10^27" figure). (4) Element 115 gap (Key Q2/4):
confirmed 29 OoM half-life gap / 9-15 MeV binding needed (Part 107,
unchanged, not re-derived, cited only) -- remains open, belongs to
T28/T40. (5) Structural ranking of "most likely distortion" (Key Q4):
energy/power claims least consistent; geometric/"falls into distortion"
description most structurally natural. (6) S1-vs-S2 distinguishing
observable identified (Key Q5): craft's own gravitational pull on nearby
test masses during operation (increases under literal amplification,
bounded/reduced under decoupling+steering). (7) Independent testable
predictions (Key Q6, "the T26 payoff" per the note at line ~1669): T35
(analog-horizon Hawking test) and Goal 1's breathing-mode/birefringence
predictions, both independent of Lazar entirely. No claim treated as
evidence for or against PDTP or Lazar, per the constraints below.

**Part:** 135
**What:** Systematic analysis of Bob Lazar's claims using a truth table framework.
The goal is NOT to judge credibility but to extract any testable physics from
the claims and map them to PDTP's decoupling predictions (Goal 2).

**Truth table scenarios:**
1. His recollection is true
2. His recollection is true but misinterpreted (they misunderstood what they had)
3. His recollection is partly false
4. His recollection is partly false by misdirection (deliberate misinformation)
5. His recollection is completely false

**Key questions (for each scenario):**
1. What specific physical claims does Lazar make about the craft's propulsion?
   (gravity amplification, Element 115, field generators)
2. For each claim, what is the PDTP translation?
   - "Gravity amplification" -> alpha = cos(psi-phi) manipulation?
   - "Element 115" -> specific nuclear properties relevant to phase coupling?
   - "Field generators" -> local phi_- excitation (Leidenfrost, Part 71)?
3. Under scenarios 1-2, what energy budget does PDTP predict?
   - Decoupling energy: ~10 kW/ton (Part 29) — is this consistent?
   - Mechanism: sustained phi_- excitation or metastable decoupled state?
4. Under scenarios 3-4, which parts are most likely the distortion?
   (Specific element vs general mechanism; engineering details vs physics)
5. What PDTP predictions would distinguish scenario 1 from scenario 2?
   (e.g., if Lazar describes gravity amplification but the actual mechanism
   is phase decoupling, the observable signatures differ)
6. What independently testable prediction does PDTP make that does NOT
   depend on Lazar's claims? (breathing mode, birefringence, etc.)

**Constraints:**
- This is Goal 2 territory — entirely contingent on Goal 1 (proving
  phase-locking Lagrangian first)
- No claim from this analysis should be treated as evidence for PDTP
- The truth table is an analytical tool, not an endorsement
- Focus on physics that could be tested regardless of source

**Expected effort:** Low-medium. Mostly literature review + PDTP mapping.
**Likely outcome:** Reference doc mapping each Lazar claim to PDTP predictions
under each truth table scenario. Main value: identifies which PDTP predictions
are independently testable (valuable regardless of Lazar's credibility).
**Priority:** Low (Goal 2; depends on Goal 1 validation).

#### [x] T27. Elastic Universe Review — Shear Modes and Visualizations — DONE (2026-08-30)

**RESULT:** All three phases complete. Full writeups:
`Elastic_Universe/E2-E8_phase1_core_physics_review.md` (Phase 1, core
physics, E1-E9), `Elastic_Universe/E10-E16_phase2_interpretive_review.md`
(Phase 2, interpretive/meta, E10-E16), `Elastic_Universe/
J1-J3_jsfiddle_code_review.md` (Phase 3, JSFiddle code).

**Phase 1 headline:** the site's Technical Summary page (E2) now has an
actual Lagrangian (`L = (1/2)*rho*du^2 - mu*eps_dev:eps_dev + p*(div(u)-chi)
+ L_core`, a displacement-field continuum-mechanics Lagrangian) plus a
Gauss-law-style eigenstrain-charge closure and an EM potential mapping
(A = solenoidal transport covector/pseudomomentum, explicitly NOT raw
velocity) -- corrects the project's earlier (E9, 2026-04-11) "no
Lagrangian" finding, though the two Lagrangians are structurally unrelated
(theirs is vector-displacement, PDTP's is a phase angle). Confirmed still
true: no stress-energy tensor, no Einstein field equations, no
Schwarzschild derivation, no charge-quantization mechanism, no finished
Dirac/Pauli electron model -- site repeatedly self-labels as provisional.

**Phase 2 headline:** author = Chantal Roth (PhD Scientific Computing, ETH
Zurich; no physics PhD or peer-reviewed physics record -- calibrates the
whole site's epistemic status). Two new real-academic citation trails
found beyond the already-known Close/Kleinert: Marek Danielewski (Wroclaw
Univ. of Sci. and Tech., elastic-solid/Cauchy-crystal papers) and Jarek
Duda (Jagiellonian Univ., topological charge models). Quantum-eraser and
entanglement pages both restate standard mainstream physics (post-
selection; Eberhard eta_min~=0.828 detection-loophole bound) in the site's
own wave-ontology language -- not new physics, and outside PDTP's Goal-1
scope regardless.

**Phase 3 headline:** ~310 listings across 9/10 JSFiddle collections
(~150-220 unique demos after de-duplication; EM Waves collection could not
be fetched -- persistent HTTP 500 from jsfiddle.net, 3 attempts, an open
gap not a scope choice). 6-fiddle shortlist source-reviewed: Hopf
(fibration, Three.js, genuinely reusable), FCC Grid+tensor (metric-from-
lattice-distortion demo, cosmetic "frame dragging" not GR-derived), Liquid
Crystal (correctly implements real nematic order parameter S and a
biaxiality metric B -- matches E9's flagged idea), Smoke Rings and Knots
(prescribed kinematic animation of vortex rings/Hopf links/knots, NOT a
dynamical solution -- do not cite as physics), **Cosserat Charge
(NEGATIVE finding: despite the name, does NOT implement Cosserat
microrotation theory -- plain Coulomb-field visualizer; directly relevant
to T66, which should not assume this collection provides ready-made
Cosserat code)**, and 3D Lattice (mislabeled -- actually an SR clock demo).

**Three candidate ideas flagged (NOT adopted, per CLAUDE.md's Elastic
Universe rule) for possible future PDTP T-items:** (1) transport-covector
framing for a PDTP EM/U(1) vector potential, which PDTP currently has no
construction for at all; (2) a high-k lattice dispersion correction
analogous to their `omega^2=c^2k^2(1+eta(kl)^2+...)`, distinct from PDTP's
existing low-k mass-gap dispersion (Eq 89.1); (3) Eshelby eigenstrain
formalism as a general computational tool for PDTP's own vortex defects.
None recommended as immediate action -- Low priority throughout, per T27's
own tag.

**Part:** N/A (external review, kept separate)
**What:** Review elastic-universe.org and Inductica YouTube for insights on shear
modes, liquid crystal order, microrotation, and visualization code. Kept in
`Elastic_Universe/` folder, separate from PDTP. See `Elastic_Universe/TODO_Elastic.md`
for the full investigation plan (16 website pages + JSFiddle code review).
**Key potential insights for PDTP:**
1. Liquid crystal order (biaxial nematic, 5 DOF) -- alternative to SU(3) for g_ij?
2. Cosserat microrotation -- rotational DOF in condensate?
3. JS visualization code -- adaptable for PDTP wave/vortex simulations
4. Independent confirmation: their c=sqrt(mu/rho) = PDTP Part 34; their gravity-as-refraction = PDTP Part 98
**Priority:** Low (external; speculative; visualization value high).

#### [x] T66. Rotation-Field / Tetrad Promotion (Cosserat-Continua Analogy) — DONE (Part 136, 2026-08-30)

**RESULT:** Full writeup `docs/research/rotation_field_gate_check.md`.
Step 1 of the approved plan (a representation-theoretic gate check) turned
out to resolve all four Key Questions directly, so Steps 2-4 (toy-model
EOM construction, Cosserat-EOM comparison, defect reclassification) were
not needed. Core finding: SO(2) is a 1-dimensional Lie group (dim SO(n) =
n(n-1)/2, re-derived here from the antisymmetry constraint, not just
quoted) -- exactly the same information content as the scalar phi(x) it
was meant to replace. Since the note's own construction sets theta(x) :=
phi(x), the map phi(x) -> R(x) is a SymPy-verified, information-free
bijection: the Lagrangian g*cos(psi-phi) is symbolically IDENTICAL after
the substitution (residual = 0), so every downstream result (Newtonian
limit, GR recovery Part 98/101, PPN Part 112, vortex winding Part 33)
carries over unchanged, not approximately -- because nothing about the
field content changed. KQ2: R(x) sits exactly at U(1)'s 1-DOF level,
strictly below Part 84's 8-DOF SU(3) tetrad -- not a re-derivation of it,
not incompatible with it, just structurally weaker by construction. KQ3:
Cosserat theory's defining feature (microrotation INDEPENDENT of the
translational field) is violated by construction, since R(x) is built
FROM phi(x) -- there is no independent DOF for a couple-stress EOM to
act on. KQ4: topological defects identical to Part 33 (same target space,
same pi_1). 11/12 Sudoku (1 informative contradiction = the KQ3 finding
itself, correctly flagged as the finding not a failure). Cross-checked
against T27's independent "Cosserat Charge" negative finding (Elastic
Universe's own code also doesn't implement real Cosserat theory) -- two
unrelated external sources both reached for "Cosserat" without the
underlying math matching, worth recording as a pattern. A genuinely new
extension (independent SO(3) or decoupled-SO(2) field) is flagged but
explicitly NOT adopted -- would need its own plan-first pass, and even
the maximal SO(3) case still falls 5 DOF short of Part 84's structure.

**Part:** 136
**Source:** External ChatGPT session note, reviewed 2026-08-01 --
`docs/misc/notes speedoflight/note Greek Cross Orientation Lattice as an Analogy for
Spacetime Phase Fields.md` (per CLAUDE.md's External AI Reviews rule -- judged
on its own merits given the session's limited context; it did not have access
to Part 84 or Part 116).

**What:** The note visualizes the PDTP lattice as a field of rotating "Greek
crosses" and suggests promoting the scalar phase field phi(x) to a full local
rotation field R(x) in SO(2) (matrix form, not just an angle). This is not new
notation -- U(1) and SO(2) are isomorphic as sets -- but treating each lattice
site as carrying a full local frame rather than a single angle is a real
structural step, and connects to established continuum-mechanics formalisms
(Cosserat continua, E. and F. Cosserat 1909; micropolar media, Eringen 1966).
**Notably, T27 (Elastic Universe review) independently flagged the same idea**
("Cosserat microrotation -- rotational DOF in condensate?") from a completely
different source -- two independent external inputs converging on the same
suggestion is worth taking seriously even though neither alone is a derivation.
**Caution (T27 Phase 3, 2026-08-30):** elastic-universe.org's own "Cosserat
Charge" JSFiddle demos (3 fiddles, titles include "Cosserat") were checked
at the source-code level and do NOT actually implement Cosserat microrotation
theory -- no couple-stress tensor, no independent rotational DOF, plain
Coulomb-field code with a misleading name. Do not treat that site as a
source of ready-made Cosserat-mechanics code or worked examples; the
convergence noted above is only that both sources independently suggest the
idea is worth trying, not that either has done it.

**Key questions:**
1. Can phi(x) be reformulated as a local rotation field R(x) without breaking
   any existing single-phase derivation (Newtonian limit, GR recovery via
   Part 98/101, PPN parameters Part 112)?
2. How does R(x) relate to PDTP's CURRENT best tetrad candidate -- Part 84's
   SU(3)-derived tetrad (which already beat the older Part 12 acoustic-analogy
   tetrad 6-4 with 7 ties) -- rather than Part 12, which the note cites?
   Is R(x) a re-derivation of Part 84, a genuinely different structure, or
   incompatible with it?
3. Does the Cosserat/micropolar formalism supply a ready-made equation of
   motion for microrotation that PDTP could borrow directly, or does the
   coupling term (g*cos(psi-phi)) need to be rebuilt from scratch for a
   matrix-valued field?
4. Do vortices/domain walls in the R(x) picture reduce to the SAME topological
   defects already used elsewhere in PDTP (Part 33 vortex winding, Part 37
   SU(3) Z_3 vortices), or would this introduce new defect types needing
   separate stability analysis?

**Explicitly NOT adopted from the same note (recorded so it isn't re-proposed
without this context):** the note's dark-matter mechanism -- gravitational
coupling ~ |cos(Delta_phi)| with EM coupling ~ (1+cos(Delta_phi))/2, and
separately, phi_- shifting the equilibrium by 180 degrees for a "hidden
sector" -- was reviewed and rejected as a next step. Reasons: (a) |cos(theta)|
has a differentiability kink at theta=pi/2 that is not addressed; (b) it is a
third, uncoordinated dark-matter mechanism competing with the already-DERIVED
winding-based mechanism (Part 116, T43: n=1 vortex stability + Kibble-Zurek ->
m_DM = m_P); (c) the phi_- claim does not match the actual derived vacuum
structure (true vacuum at phi_- = pi/2, Part 119, not a matter-induced 180
degree shift from a phi_-=0 baseline, Part 125). If DM-via-phase-structure is
revisited later, it must be reconciled against Part 116 first, not treated as
a fresh proposal.

**Expected effort:** Medium-large if pursued (structural extension, comparable
in scope to the two-phase Lagrangian or SU(3) extension -- needs a Problem-
Solving Protocol plan-first pass per CLAUDE.md before any code/derivation work).
**Likely outcome:** Either a genuine unification of Part 84's tetrad with a
Cosserat-style microrotation field (positive), or a demonstration that R(x)
reduces to Part 84 in disguise (negative but clarifying).
**Priority:** Low (speculative, large scope; no immediate gap it closes; revisit
if T27's Elastic Universe review also independently reaches this point).

---

#### [x] T69. Dark Matter Doc Audit + Two Current External Events — DONE (Parts 138-139, 2026-09-02)

**RESULT:**

**Sub-point 1 (consistency audit) found and fixed TWO real bugs**, not
zero as originally expected -- full writeup `docs/research/
dm_bullet_bound_erratum.md` (Part 138). (a) The "44.3 orders of magnitude"
Bullet Cluster safety margin, cited everywhere Part 118's DM self-
interaction result appears, used a WRONG bound constant: 1 cm^2/g was
coded as 1e-4 m^2/kg when it is actually 1e-1 m^2/kg (SymPy-verified via
sympy.physics.units.convert_to) -- a 1000x error baked into the actual
Python constant (`BULLET_BOUND_M2KG` in `sigma_m_erratum.py`) since Part
118, and into two other scripts (`condensate_layer_fcc.py`,
`condensate_layer_optics.py`) since Part 89/96. Corrected margin: **47.3
orders**. (b) A SEPARATE bug in the same neutrino-detectability material:
KM3-230213A's E/m_W ratio was stated as 2737, correct value is **2.7e6**
(220 PeV/80.4 GeV) -- a 1000x PeV-to-GeV conversion slip, also affecting
the Glashow-resonance and previous-record rows of the same table in
`condensate_layer_optics.md`. **Neither bug changes any PASS/FAIL verdict
anywhere** -- PDTP's own predicted values were always correct; only the
comparison constants were wrong. All three affected scripts fixed and
rerun (Sudoku unchanged: 7/7, 12/12, 12/12); every citing .md doc updated
(`dark_matter_energy.md`, `condensate_layer_optics.md`,
`dm_winding_selection.md`, `notes_mcond_lambda.md`, `equation_reference.md`,
this file).

**Sub-points 2-3** -- full writeup `docs/research/t69_dm_current_events.md`
(Part 139). LZ's 2.6-sigma event (if real, implies a WIMP >= 200 GeV)
matches NEITHER of PDTP's own DM candidates: 16-17 orders too heavy for
Part 116's preferred n=1 Planck-vortex relic, ~1000x too light for Part
89's ~200 MeV C1-trap candidate. [Correction, 2026-09-06: this RESULT
text had the two directions swapped; fixed to match the source doc and
the quick-reference line above.] Honest fork flagged for future LZ data,
not resolved from one sub-threshold event: a null result is consistent
with PDTP's own undetectability prediction; a confirmed ~200 GeV signal
would be in real tension with Part 116's n=1 selection specifically.
Roman's flagship lensing/substructure-mapping capability tests NOTHING
PDTP-specific -- the one route that would have (biharmonic gravity,
Prediction 11) already failed by 20 orders of magnitude (dark_matter_
energy.md Sec 2.5), and PDTP's live DM falsifiable test (Prediction 13)
needs a CMB polarimeter, not an optical/IR telescope. Roman's actual PDTP
connection is the already-on-record dark-energy w(z) test (Prediction 5);
`falsifiable_predictions.md`'s stale "Launch ~2027" note corrected to the
actual 2026-08-30 launch date.

**Part:** 138 (sub-point 1), 139 (sub-points 2-3)
**Source:** User request, 2026-09-02. `docs/research/dark_matter_energy.md` was
last updated for Part 118 (2026-06-11) -- confirmed stale relative to two
external events from the past few days that the file cannot yet reflect.

**What:** Three bounded sub-checks on PDTP's dark matter picture, run together
since they all touch the same living document.

1. **Consistency audit of `dark_matter_energy.md`.** Read start to finish;
   verify every computed number in the Quick Reference table and the
   Consolidated Equation Reference (Part 8) still traces correctly to its
   cited Part; cross-check against `equation_reference.md` for drift; flag
   anything stale (in the style of the `TODO_Elastic.md` staleness note
   found during T27). No new physics expected -- this is bookkeeping.
2. **LZ (LUX-ZEPLIN) 2.6-sigma event, announced 2026-09-01.** Single
   anomalous event in a 10-tonne liquid xenon WIMP search (220 live days,
   TeV Particle Astrophysics conference, Japan) -- explicitly not a
   confirmed discovery per the collaboration itself. Summarize what was
   actually reported, then map it against PDTP's existing DM candidates
   (Part 116's n=1 "Planck vortex relic"/wimpzilla, Part 89's ~200 MeV
   C1-confined candidate): does a WIMP-mass-range signal sit comfortably
   with either, or in tension? Scoped to one bounded point, no new
   derivation -- a mapping exercise, not an investigation.
3. **Nancy Grace Roman Space Telescope, launched 2026-08-30.** No data yet
   (first images expected early 2027), so scoped as: does Roman's actual
   survey design (weak-lensing / dark-matter-substructure mapping) test
   any PDTP prediction already on record (e.g. the vortex-DM smoothness
   claim, or the microlensing-unconstrained note in dark_matter_energy.md
   Sec 6.4)? If yes, flag as a future falsifiable-prediction test to watch
   for once 2027 data arrives -- not something to analyze today.

**Cross-check with:** Part 89, Part 96, Part 116, Part 118 (DM candidates
and self-interaction cross-section), `equation_reference.md`,
`falsifiable_predictions.md` (any new/updated prediction from sub-point 3
goes through that file's own separate "plan first" rule before being
added, per CLAUDE.md).
**Effort:** Low-Medium. Audit + two literature-comparison mappings, no new
derivation expected -- comparable in kind to T27's Elastic Universe review,
not a new-physics investigation like T28/T66.
**Priority:** Medium (higher than typical Low-priority filed items --
both external events are current enough that the comparison is time-
sensitive; letting the doc go further stale defeats its own purpose as a
"living reference").

---

#### [x] T70. N_eff via Spin-Weighted Seeley-DeWitt Heat-Kernel Coefficient — DONE (Part 140, 2026-09-06)

**RESULT:** Full writeup `docs/research/neff_seeley_dewitt_applicability.md`.
CONSTRUCTIVE NEGATIVE, decided by the plan's own Step 1 and Step 2 before
Steps 4-6 (recompute/write-up) were needed as originally scoped -- they were
still run, but only as a completeness check on an already-closed question.
Step 1: the suggested formula (Eq 140.1 below) could not be attributed to
any source after two targeted literature searches -- fails CODING_STANDARDS'
citation bar on its own. Step 2 (decisive regardless of Step 1): re-read
every version of PDTP's own continuum Lagrangian (U(1) Eq 140.2, SU(3) Eq
140.3, two-phase Eq 140.4) line by line -- N_v (vector fields) and N_f
(Dirac fermions) are BOTH zero identically throughout. PDTP's "8 gluons"
are nonlinear-sigma-model scalar fluctuations (Tr[(dU-dag)(dU)] kinetic
term, no gauge connection, no field-strength tensor anywhere), independently
confirmed by Part 114's own classification ("8 real massless scalars") and
its SU(2) reduction matching Weinberg's pion (scalar/pseudoscalar) vertex
exactly. The one place real Dirac fermions appear in the project (Part 40's
Wilson-fermion lattice calculation) is explicitly borrowed standard-QCD
machinery used as a numerical scaffold for one string-tension side-check,
not a redefinition of PDTP's own matter field Psi_i(x) (also matrix-valued
and scalar per Eq 140.3). Computed anyway for completeness
(`t70_neff_seeley_dewitt.py`): the QCD-analogy reading (treating gluons as
literal vectors, matter as literal Dirac fermions) gives G_ind/G = 0.13-0.18
-- worse than Part 83's existing [0.554, 2.356] range; the structurally-
honest reading (N_v=N_f=0, only the formula's 1/6 scalar weight applied)
gives G_ind/G = 3.3-14.1 -- also worse than Part 83's own unweighted scalar
count. Neither reading helps. Part 83's own N_eff gap characterization
(range [8,34], target 6*pi=18.85, 1%-off Casimir near-miss) is UNCHANGED --
its scalar-only tool was already the right category of tool, confirmed
rather than merely assumed. Cross-checked against T12/Part 129 (M=0
refractive-index negative): structurally independent, non-overlapping,
no contradiction. 10/10 Sudoku (structural/citation-verification style,
consistent with the project's non-numerical Sudoku precedent e.g. Part 114).

**Part:** 140
**Source:** External AI review (qwen3.7), given the actual GitHub repo URL
to read directly (not just pasted text) -- `docs/misc/qwen3.7. pdtp. suggest.md`.
Reviewed per CLAUDE.md's External AI Reviews rule: judged on its own merits:
it did not have access to Part 114's Trace Theorem (see below), and its
companion "CKN bound factor 12" claim (its Suggestion 4) could not be
located anywhere in the project after a full-repo search -- treated as
unverified, not acted on here.

**What:** Part 83 (`neff_sakharov.md`) characterizes the N_eff = 6*pi gap
in Sakharov induced gravity (8 SU(3) gluons alone give G_ind/G = 3*pi/4 =
2.356; need N_eff = 6*pi = 18.85 for an exact match) using two admittedly
crude tools: the Visser scalar-only heat-kernel formula, and a naive
signed helicity sum (N_eff = sum_i eps_i*nu_i) that the doc itself flags
as inadequate (it gives N_eff(SM) = -62, implying repulsive gravity --
obviously wrong). The external suggestion: use the actual spin-weighted
Seeley-DeWitt a_2 coefficient formula instead,

```
N_eff = N_v + (11/2)*N_f + (1/6)*N_s
```

(N_v = vector bosons, N_f = Dirac fermions, N_s = real scalars, with
gauge-fixing + Faddeev-Popov ghost contributions accounted for), applied
to PDTP's actual field content: 8 gluons (N_v), phi_+ and phi_- (N_s),
and matter vortices as fermionic content (N_f) if 3 generations x 3
colors x 2 chiralities = 18 quark fields (plus leptons, per Part 83's own
24-species matter count) are included.

**Why this matters more than the external reviewer knew:** Part 114
(`su3_nonlinear_vertex.md`) proved a Trace Theorem -- the tree-level
condensate action carries no graviton dynamics at all; the Sakharov
1-loop mechanism is not one route among several, it is PDTP's *only*
source of gravity. That makes N_eff's exact value more central than
Suggestion 1's framing assumed, not less.

**Proposed steps (plan before starting, per the Problem-Solving Protocol):**
1. Derive/cite the spin-weighted a_2 formula from a proper source (e.g.
   Vassilevich (2003), "Heat kernel expansion: user's manual", Phys. Rept.
   388, 279) rather than taking the external suggestion's formula on faith.
2. Pin down PDTP's actual field content precisely -- in particular whether
   PDTP's matter vortices are naturally Dirac-like fermions or something
   else (check Parts 33/37's own vortex construction; this is not yet
   established and the spin-weighted formula depends on it).
3. Recompute N_eff for the same three scenarios Part 83 already tabulated
   (minimal/two-phase/+matter) using the new weights, and see whether the
   crossover shifts toward or away from 6*pi and the existing 18.67
   Casimir near-miss.
4. Cross-check against T12/Part 129 (n_PDTP cannot modify the Sakharov
   cutoff -- established negative) to confirm this does not re-open a
   closed question, only refines the DOF-counting side of Part 83.
5. Sudoku consistency check (10+), per standard.
6. Write up as a new section in `neff_sakharov.md` (same investigation,
   better tool) rather than a separate research doc.

**Expected outcome:** either a tighter, more principled characterization
of the gap than the existing 1%-off Casimir guess, a different but still
open characterization, or a finding that naive and spin-weighted counting
agree closely (meaning Part 83's existing bound already captures the
right physics).

**Effort:** Medium (well-scoped calculation, existing Part 83 scaffolding
to build on).
**Priority:** Medium -- same class as T12 (heat-kernel refinement of an
already-PARTIAL, non-blocking result), not urgent, but concrete and
actionable, unlike most of the SPEC/low-priority backlog around it.

---

#### [ ] T71. Audit the CKN "Factor 12" Formula Discrepancy (Part 54)

**Status:** PENDING. Filed 2026-09-06.
**Source:** Found as a side effect of a repo-wide search for the phrase
"factor 12", run to check whether qwen's Suggestion 4 (`docs/misc/
qwen3.7. pdtp. suggest.md`) had a real basis in the project. It did --
Part 54 (`cosmological_constant_fcc.md`) states rho_CKN = 7.1e-26 kg/m^3
vs rho_Lambda = 5.8e-27 kg/m^3, ratio ~12.2, cited as "factor 12" in both
`TODO_02.md` and `equation_reference.md`.

**What:** Two citations of the same CKN (Cohen-Kaplan-Nelson) bound formula
do not obviously match:

```
cosmological_constant_fcc.md (Part 54, CC-L5): rho_CKN = hbar*c / (l_P^2 * L_H^2)
TODO_02.md / equation_reference.md:            rho_CKN = c^2 / (G * L_H^2)
```

A quick unit check (l_P^2 = hbar*G/c^3, substituted into the first form)
did not reduce to the second form cleanly -- worth a proper SymPy
dimensional check before trusting either number further. This was not
chased down when found (out of scope for the search task that surfaced
it); filing here so it is not lost.

**Proposed steps:**
1. Re-derive both forms symbolically (SymPy, `sympy.physics.units`) and
   check whether they are actually equivalent (e.g. via a substitution or
   convention I'm missing) or genuinely inconsistent.
2. If inconsistent, determine which is correct, recompute rho_CKN, and
   check whether "factor 12" survives, changes, or disappears.
3. Update whichever of Part 54's doc / TODO_02.md / equation_reference.md
   is wrong, propagating the correction the same way T69/Part 138 did for
   the Bullet Cluster bound (trace every citation, fix at the source,
   re-verify, no silent drift).
4. Only after the number is confirmed: decide whether qwen's Suggestion 4
   (GHY boundary term + Padmanabhan bulk-surface DOF equipartition on the
   Hubble horizon, applied to PDTP's SU(3) condensate) is worth planning
   as its own task to explain the (possibly revised) factor.

**Effort:** Low for steps 1-3 (a focused dimensional-consistency check);
step 4 would be its own scoped task if reached.
**Priority:** Low-Medium -- a loose end worth closing before it's forgotten,
not blocking anything currently in progress.

---

#### [x] T73. Glueball Mass Test vs X(2370) (BESIII, arXiv:2607.20366) — DONE (Part 141, 2026-09-10)

**RESULT:**

**CONSTRUCTIVE on mass scale, NEGATIVE on quantum numbers.** Full writeup
`docs/research/glueball_x2370_test.md`; script
`simulations/solver/t73_glueball_x2370.py`; 10/12 Sudoku PASS (1
informative FAIL, 1 honest N/A).

**What was found:**
1. Mechanism A [PDTP Original]: glueball modeled as a closed loop of
   PDTP's own confining flux tube (Parts 36-37, no quark ends) --
   M_loop(R) = sigma*2*pi*R/(hbar*c). Using ONLY already-published PDTP
   inputs (sigma_SU3=0.053 GeV^2 or sigma_measured=0.18 GeV^2, xi_QCD=
   0.70 fm), the minimal-radius (R=xi_QCD) estimate BRACKETS X(2370)'s
   real mass (1.18 GeV and 4.01 GeV around 2.376 GeV); all (sigma,R)
   combinations for R=1-3*xi_QCD land within a factor of 5 (same
   "right ballpark" standard Part 37 itself used for its own 3.4x/1.8x
   estimates) except the single most extreme corner (measured sigma,
   R=3*xi, ratio 5.07 -- informative FAIL, not an error).
2. Mechanism B [PDTP Original]: Part 114's chi^a contact-vertex EFT
   breakdown formula (E_break=sqrt(6/pi)*m_cond), reapplied unchanged at
   the QCD condensate layer (m_cond_QCD=367 MeV instead of m_P) gives
   E_break_QCD=507 MeV -- X(2370) sits 4.7x ABOVE this, meaning the
   contact-vertex mechanism specifically CANNOT reach X(2370)'s mass at
   all. Clean negative, sharply distinguishes it from Mechanism A.
3. Quantum numbers [DERIVED, NEGATIVE]: PDTP's SU(3) sector has NO field
   content able to predict or accommodate X(2370)'s measured J^PC=0-+ --
   chi^a fields are already classified (T70/Part 140) as nonlinear-
   sigma-model SCALARS, not real spin-1 QCD gluons, so there is no
   vector-gluon color-magnetic structure to build a 0-+ state from.
4. R (the loop radius) is an OPEN parameter -- no PDTP-internal
   principle fixes it; the bracketing result at R=xi_QCD is the robust
   finding, not the closer (but essentially R-tuned, not independently
   derived) match at R=2*xi_QCD.
5. Width (83+-17 MeV) NOT computed -- no decay mechanism exists yet for
   a closed PDTP flux-tube loop; documented as an explicit open gap
   (Sudoku check S12), not silently skipped.
6. Independence verified: uses only SU(3)-layer quantities already
   established in Parts 29/35/36/37/114; touches no U(1) or two-phase
   (phi_-) symbol (Sudoku rule 4).

**Overall verdict:** a genuinely interesting, non-hand-waved mass-scale
consistency result (PDTP's confinement machinery, built for quark
binding, happens to land near a real hadron it was never built to
predict) -- but a coincidence check, not a derivation of X(2370); the
quantum-number gap means this should be reported as suggestive, not as
"PDTP predicts the glueball."

**Open items:** loop radius R unconstrained; no rotational/vibrational
quantization to assign J^PC; width not derivable without a decay
mechanism.

**Part:** 141 (`simulations/solver/t73_glueball_x2370.py`)
**Filed:** 2026-09-10.
**Source:** `docs/misc/notes 2026-09-10.txt` (user's week-of-notes dump);
PDF at `assets/pdfs/2607.20366v1.pdf`, read in full. BESIII Collaboration,
arXiv:2607.20366v1 (22 Jul 2026), "Lightest 0-+ Glueball as Dominant
Constituent of X(2370)" -- real hep-ex paper, 10 billion J/psi events.
**Framing note (user correction, 2026-09-10):** this item is NOT a
dark-matter candidate search. The user explicitly did not associate the
gluball with dark matter -- the question is purely whether PDTP's own
SU(3) sector math can reproduce/predict something glueball-like. Treat
this as a structural validation test of existing PDTP machinery against
a real measured particle, same genre as the string-tension check
(Part 37-41, 4% match), not as a new physics mechanism proposal.

**What the paper actually established (real physics, for reference):**
- X(2370): mass 2376.3 +- 8.7 MeV/c^2, width 83 +- 17 MeV, spin-parity
  0-+ (confirmed via a separate 9.8-sigma analysis), flavor-singlet
  (first light hadron above 1 GeV/c^2 confirmed as such).
- BESIII searched X(2370) -> K*(892)^0 K-bar^0 + c.c. and found NO
  evidence (B < 2.7e-6 at 90% CL) -- the suppressed K*(892)K-bar mode is
  the signature of a 0-+ flavor-singlet (forbidden from that mode by
  generalized G-parity), and rules out q-qbar / multiquark / hybrid
  interpretations (which would allow it via OZI-allowed decay).
- Narrow partial decay widths + strongly suppressed radiative decays to
  gamma-omega/gamma-phi (rules out q-qbar content) + production rate and
  mass both consistent with LQCD's predicted 0-+ glueball (2.3-3.0 GeV/c^2
  range, J/psi radiative production channel).
- Also rules out Sigma-Sigma-bar baryonium and eta-eta' excitation as
  alternative explanations (wrong production rate / wrong partial width).

**The actual PDTP question:**
1. Part 114 already derived an EXACT self-interaction quartic vertex for
   the 8 chi^a "gluon" fields (coefficient -1/24, SymPy-verified, anchored
   to Weinberg's ChPT pi-pi vertex). Does this vertex, combined with
   Part 37-41's already-fit string tension (sigma_SU(3) = 4/3 * sigma_U(1),
   4% off QCD lattice), predict a bound state at all in the chi^a sector?
2. If a bound-state mass falls out of the existing machinery (e.g. via a
   Bag-model-style or lattice-style estimate from sigma and m_cond_QCD,
   Part 37-41's ~367 MeV condensate scale), how does it compare to
   X(2370)'s real mass (2376.3 MeV) and width (83 MeV)?
3. Is there a natural 0-+ (pseudoscalar, flavor-singlet) quantum-number
   assignment available in the chi^a field content, or does PDTP's
   nonlinear-sigma-model classification (T70/Part 140: chi^a are NLSM
   scalars, not real gauge bosons) forbid a clean spin-parity match from
   the start? (T70 already found PDTP has no real gluon d.o.f. in the
   gauge-theory sense -- this may cap what's achievable here.)
4. If no PDTP-internal number is derivable (most likely outcome, given
   T70's finding that "gluons" are sigma-model scalars not QCD gauge
   fields), document that explicitly as a scope boundary -- this is a
   legitimate, informative negative, not a failure to force.
**Cross-check with:** Part 37-41 (string tension), Part 114 (exact
quartic vertex), T70/Part 140 (chi^a classification as NLSM scalars, not
gauge bosons -- directly bears on whether a glueball-like bound state is
even the right kind of object to look for in PDTP's SU(3) sector).
**Effort:** Medium -- requires a genuine bound-state estimate (not just a
scale comparison), likely bounded by T70's existing classification result.
**Priority:** HIGH -- concrete, falsifiable numbers to test against,
builds directly on two already-DERIVED results (Part 37-41, Part 114)
rather than opening new speculative ground.

---

#### [x] T74. GW170817 Constraint on PDTP's GW Structure — DONE (Part 142, 2026-09-10)

**RESULT:**

**PASS (tensor sector, by construction) + CONSTRUCTIVE NEGATIVE (scalar
sector, structurally undetectable).** Full writeup
`docs/research/gw170817_dispersion_check.md`; script
`simulations/solver/t74_gw170817_dispersion.py`; 11/12 Sudoku PASS, 1
honest N/A.

**What was found:**
1. PDTP has TWO structurally distinct GW modes, requiring separate
   treatment: the tensor sector (phi_+/SU(3), Parts 75-76 -- the actual
   quadrupole signal LIGO detected) and the scalar/breathing sector
   (phi_-, Parts 61-63/113 -- a separate, already-derived MASSIVE mode,
   not what GW170817's arrival-time measurement even probes).
2. Tensor sector [PDTP Original, numeric]: c_s=c is an EXACT algebraic
   identity (condensate_microphysics.md Constraint 3, re-verified Part
   63 Sudoku S8) -- a PPN-gamma=1 design requirement predating GW170817,
   not tuned to satisfy it. Computed GW170817's own speed bound directly
   from the downloaded paper's source numbers (Delta t=1.7s, d=40 Mpc,
   NOT quoted from memory): |dv|/c ~ 4.13e-16. PDTP's deviation (0)
   trivially satisfies this.
3. Scalar sector [DERIVED, NEGATIVE]: reusing T68's corrected bare
   coupling (g_bare=omega_gap^2/c^2) inside Part 63's own dispersion
   relation (omega^2=c^2 k^2+2g*Phi), cross-verified via two independent
   symbolic routes (SymPy residual 0) and cross-checked against T68's
   own published Earth-surface number (agrees to <1%): phi_- is
   EVANESCENT (non-propagating) at LIGO-band frequencies (24-500 Hz) for
   EVERY physically realized gravitational potential in the universe --
   the propagation threshold sits 77 orders of magnitude below even the
   Sachs-Wolfe large-scale-structure potential scale (Phi/c^2~1e-5), the
   real cosmological estimate of how small Phi gets even in the emptiest
   voids. There is no possible phi_- signal for GW170817 to have
   constrained -- the question is dissolved, not merely answered yes.
4. Byproduct: found and fixed a ~22-orders-of-magnitude numerical
   erratum in two_phase_rederivation.md (Part 63) Section S7 -- its
   stated "g_coupling ~ G*m_P^2/hbar ~ 2.95e42 rad/s" is dimensionally
   not a frequency at all (SymPy confirms G*m_P^2/hbar reduces
   IDENTICALLY to c, by the definition G=hbar*c/m_cond^2) -- a distinct
   erratum from T68's bug (Part 63 S7 was not one of T68's audited
   Parts), same general class. No PASS/FAIL verdict changes; only the
   illustrative numeric plug-in was wrong. Corrected at the source.

**Overall verdict:** PDTP passes this real, historically theory-killing
constraint cleanly on both fronts -- trivially for the tensor sector (a
pre-existing design requirement), and because the extra scalar mode is
structurally incapable of being what such a measurement could probe.
Neither outcome required a new assumption or free parameter.

**Open items:** whether phi_-'s coupling to a BNS merger SOURCE (as
opposed to its propagation, addressed here) could produce any other
near-merger signature -- not attempted, flagged as a possible future item.

---

**Part:** 142 (`simulations/solver/t74_gw170817_dispersion.py`)
**Filed:** 2026-09-10.
**Source:** `docs/misc/notes 2026-09-10.txt`; PDF at
`assets/pdfs/1710.06168v2.pdf` (arXiv:1710.06168v2, real 2017 paper,
"GW170817 Falsifies Dark Matter Emulators" -- confirmed via the original
LIGO/Virgo GW170817 multi-messenger result: GW and gamma-ray signals
arrived within ~1.7s after propagating ~130 million light-years, pinning
GW speed to c to ~1 part in 10^15). **User confirmed this item is
dark-matter-related** (2026-09-10 correction), grouped with T75/TeVeS.

**What:** GW170817's speed bound killed or severely constrained a large
class of modified-gravity / dark-matter-emulator theories (incl. TeVeS,
see T75) whose extra field content predicted GW propagation at a speed
different from c. PDTP already has an existing, on-the-books negative in
this space: the biharmonic gravity correction (nabla^4 Phi + 4g^2 Phi,
Part 61) has a screening/healing length L_heal on the order of the
Planck length, far below any observable scale -- but that finding was
about the STATIC/Newtonian correction, not GW propagation speed
specifically.
**Key questions:**
1. Does PDTP's phi_- (scalar) mode, or the biharmonic correction, carry
   any independent propagation speed for gravitational waves distinct
   from c? (The U(1)/two-phase field equations are already built on a
   fixed c_s = c identity, Part 34 -- worth confirming this holds for
   EVERY propagating mode, not just the base phi_+ mode used in that
   derivation.)
2. If a second mode (phi_-, or the SU(3) chi^a tensor sector, Part 75-76)
   propagates, does it inherit c_s = c automatically, or does it need a
   separate check?
3. Quantitatively: what is |c_GW - c|/c predicted by PDTP's own field
   equations, and does it sit safely inside GW170817's ~1e-15 bound, or
   does it expose a new constraint the project hasn't stated explicitly
   yet?
**Cross-check with:** Part 34 (c_s = c derivation), Part 61-63 (biharmonic
gravity, L_heal ~ l_P), Part 75-76 (SU(3) tensor metric, 2 TT GW
polarizations), T75 (TeVeS, same external constraint).
**Effort:** Low-Medium -- likely a direct dispersion-relation check on
existing field equations, not a new derivation from scratch.
**Priority:** HIGH-MEDIUM -- a real, quantitative, already-published
constraint; either PDTP passes cleanly (strengthens Part 34's c_s=c
result into a stated falsifiable margin) or surfaces a genuine problem
worth knowing about now rather than later.

---

#### [ ] T75. TeVeS Structural Comparison [Scoping]

**Status:** PENDING. Filed 2026-09-10.
**Source:** `docs/misc/notes 2026-09-10.txt` (Wikipedia link, TeVeS /
Tensor-Vector-Scalar gravity). **User confirmed dark-matter-related**
(2026-09-10 correction), grouped with T74/GW170817 and the two topology
items (T76).

**What:** TeVeS (Bekenstein 2004) is MOND's relativistic completion --
tensor + vector + scalar field combination reproducing MOND phenomenology
relativistically. Largely killed/severely constrained by the GW170817
speed bound (see T74). This item is a lower-effort scoping/comparison,
not a derivation:
1. What does TeVeS's extra VECTOR field structurally buy it that a pure
   scalar (PDTP's phi) or PDTP's SU(3) octet (chi^a, still Lie-algebra
   valued scalars per T70) cannot? PDTP has no true vector (spin-1) field
   anywhere in its Lagrangian -- already confirmed as an explicit gap by
   T70/Part 140's classification work, and separately flagged in
   `docs/research/polarization_analogy.md` (Part 28b) as the reason PDTP
   has no natural U(1) electromagnetic construction (a scalar field
   supports only longitudinal waves, not EM's transverse 2-polarization
   structure).
2. Does TeVeS's MOND-recovery mechanism (via its scalar field's
   nonstandard kinetic term) share any structure with PDTP's own
   MOND-like results, if any exist? (Check whether PDTP has ever derived
   MOND-like rotation-curve behavior -- if not, this is itself worth
   noting as a gap, separate from the vector-field question.)
3. Is TeVeS's post-GW170817 status (constrained but not fully dead --
   some variants survive with a decoupled GW sector) instructive for how
   PDTP should present ITS OWN GW170817 check (T74) if a discrepancy is
   found?
**Cross-check with:** T74 (GW170817), T70/Part 140 (no gauge vector
field), `docs/research/polarization_analogy.md` (PDTP's EM gap).
**Effort:** Low -- literature/structural comparison, not new math.
**Priority:** MEDIUM -- context and comparison value, not a blocking
derivation; useful mainly as a companion to T74.

---

#### [ ] T76. Topological Dark-Matter Candidate: Ring-on-Chain Linking [SPECULATIVE]

**Status:** PENDING. Filed 2026-09-10.
**Source:** `docs/misc/notes 2026-09-10.txt` -- **user's own original
idea, not a citable paper.** Per explicit user instruction (2026-09-10):
"remember all are speculation except the scientific papers that we might
build on or use" -- this entire item stays tagged [SPECULATIVE]
throughout any future work, distinct from T73/T74/T77/T78 which engage
with real published papers.
**User's framing (2026-09-10 correction):** originally logged as a minor
addition to T30; the user explicitly elevated this to its own dark-matter
CANDIDATE item ("the one topology with the rings as another dark matter
candidate"), not a footnote.

**The idea (two linked observations from the notes):**
1. "Ring on a chain" trick: a chain laid out with two parallel lines (a
   "U" shape at the bottom); a ring dropped over the two lines can become
   looped/tangled with the chain purely through the geometry/topology of
   the setup -- no extra force or energy input, just the linking topology
   of the path.
2. "Roving Bridges" (Reddit post, canal tow-rope spiral crossings) --
   real-world example of the same class of effect: topology/linking
   producing a mechanical entanglement "for free," used descriptively
   here as a second illustration of the same principle, not as a separate
   TODO item.
**User's speculative question:** could a similar topological-linking
principle cause matter to become "twisted" into dark-matter-like behavior
without needing the exotic energy budget normally assumed -- i.e., is
dark matter's mass/abundance possibly a topology effect rather than an
energy-cost effect?

**Why this needs to be checked against existing PDTP results before being
treated as new:**
1. `docs/research/dark_matter_energy.md` Part 2 already has a mature
   candidate roster (Mechanism 1 TIR confinement, Mechanism 2 mode-mismatch
   U(1)-only vortex [STRONGEST], Mechanism 3 interference dark zones
   [NEGATIVE], plus antimatter/biharmonic/Anderson-localization/winding-
   number sub-entries). The winding-number result (Section 2.7, Part 116,
   T43: n=1 vortex stability + Kibble-Zurek -> m_DM = m_P) is ALREADY a
   topological mechanism (vortex winding number is a topological
   invariant) -- the ring-on-chain idea must be shown to be genuinely
   distinct from this, not a re-description of it.
2. T30 (Hopf-link topology protection, PENDING, SPEC) already investigates
   linked-loop topology in PDTP, but for a different purpose (decoherence
   protection / device coherence lifetime, not mass generation or DM
   abundance). T76 and T30 need to be cross-referenced so they don't drift
   into duplicate investigations of the same underlying topology
   (interlinked loops in a phase condensate) from two different angles.
**Key questions:**
1. Does PDTP's condensate (U(1) phase field, or SU(3) Z_3 vortices) admit
   a "ring dropped over two parallel lines" analog at all? What would the
   two "chain lines" and the "ring" correspond to physically (e.g. two
   parallel vortex filaments and a closed loop crossing between them)?
2. If such a configuration exists, is it topologically STABLE (protected
   by a conserved linking number, like Part 116's winding number) or just
   transiently entangled?
3. Does the mechanism actually avoid an energy cost, or does forming the
   linked state cost energy equal to what winding-number formation
   already costs (in which case this is Mechanism 2/T43 restated in
   different language, not a new candidate)?
4. Rubik's-cube/Cayley-graph state-space idea (user's second topology
   idea, also from the notes: modeling all scrambled states as nodes and
   twists as directed edges in a massive Cayley graph) -- folded in here
   as a second, weaker analogy. No specific PDTP field-theoretic mapping
   proposed yet; likely relevant only if T76's main line of inquiry
   produces a genuine "state-space topology determines mass/abundance"
   result, at which point the Cayley-graph framing might offer a
   combinatorial way to count accessible topological states. On its own,
   too underspecified to investigate directly.
**Cross-check with:** `docs/research/dark_matter_energy.md` Section 2.7
(Part 116 winding number, T43), T30 (Hopf-link protection).
**Likely outcome:** most probable result is that this collapses into
Part 116's already-DERIVED winding-number mechanism restated via a
different real-world analogy (a genuine but not NEW finding) -- flag this
as the leading hypothesis to test first, per the Sudoku-check discipline
of checking against established results before treating something as new.
**Effort:** Medium -- needs a real topological-invariant identification
in the PDTP condensate before any energetics can be compared.
**Priority:** LOW-MEDIUM -- explicitly speculative, real risk of
collapsing into an existing result; worth a scoping pass but not urgent.

---

#### [ ] T77. Timeflow Gravity Comparison (Trofimov 2026, *Class. Quantum Grav.* 43)

**Status:** PENDING. Filed 2026-09-10. PDF now in hand:
`assets/pdfs/Trofimov_2026_Class._Quantum_Grav._43_135020.pdf` (saved by
user 2026-09-10 -- full text available, no longer blocked on paywall
access).
**Source:** Reference list of a Consensus.app AI literature-search review
of PDTP (using Introduction.md + the 3 Lagrangians as input snippets),
which cited: "One recent theoretical framework, Timeflow Gravity,
explicitly proposes that gravity emerges from phase-locking between
baryonic matter and a U(1) spacetime medium, deriving MOND-like dynamics
and dark energy from coherent versus decoherent phase states (Trofimov,
2026)." Verified as a real, peer-reviewed paper via WebSearch: Trofimov,
M. (2026), "Timeflow Gravity: a thermodynamic theory of spacetime,"
*Classical and Quantum Gravity* 43, published 8 Jul 2026, DOI
10.1088/1361-6382/ae811d.

**Why this is flagged HIGH priority:** of everything in the notes-file
batch, this is the single most consequential item given the depth of
structural overlap with PDTP's own core framework, per the WebSearch
summary (not yet cross-checked against the actual paper text):
- Fundamental state space proposed as a ONE-DIMENSIONAL CIRCLE (the
  "Timeflow field") -- directly matching PDTP's U(1) phase phi.
- Gravity as an emergent thermodynamic/entropic force, deriving Einstein
  field equations via **Jacobson's Clausius-relation argument** -- the
  SAME external tool PDTP's own Part 86 uses (S_PDTP = k_B*ln(2)*A/a_0^2,
  lattice-cell counting, recovering full nonlinear GR).
- At galactic scales, "constructive phase interference between baryonic
  matter and the vacuum recovers MOND-like dynamics" -- a phase-coherence
  route to MOND-like behavior, thematically close to what T75 asks
  whether PDTP has ever derived.
- "Kinematic phase decoherence" invoked to address MOND's cluster mass
  discrepancy and the Bullet Cluster offset -- PDTP has its own Bullet
  Cluster margin result (T69/Part 138, 47.3 OoM) via a completely
  different (particle-mass) route; worth knowing whether these are
  compatible pictures or competing ones.
- Dark matter AND dark energy both interpreted as "wave-mechanical
  projections of the underlying phase space" -- compare directly against
  PDTP's own DM (winding number, Part 116) and DE (phi_- locking fossil,
  Part 119/T46) mechanisms.
- Time itself is presented as the continuous evolution of quantum phase
  -- worth comparing against PDTP's own treatment of time (currently just
  the ordinary time coordinate in the Lagrangian, no special status).
**Key questions:**
1. Is Timeflow Gravity's U(1)/circle state space mathematically the SAME
   object as PDTP's phi, or only thematically similar (different
   Lagrangian, different coupling, different field content)?
2. Does Trofimov's use of Jacobson's argument reach the same S = k_B ln(2)
   A/a_0^2 entropy relation as Part 86, or a different one? If different,
   what does the difference correspond to physically?
3. Does Timeflow Gravity's MOND-recovery mechanism have a direct PDTP
   analog, or is this a place PDTP has NOT reached (i.e., a genuine gap
   Timeflow Gravity fills that PDTP doesn't)?
4. Is this convergent independent validation (two groups reaching similar
   structure from different starting points -- a positive signal for the
   general approach), or does it reveal a result PDTP should have already
   derived and hasn't (a gap to close)? Must be assessed honestly, not
   assumed to be either.
**Cross-check with:** Part 86 (Jacobson entropy derivation), Part 116/T43
(DM winding number), Part 119/T46 (DE locking fossil), T69/Part 138
(Bullet Cluster margin), T75 (TeVeS/MOND).
**Effort:** Medium-High -- requires a full, careful read of the actual
paper (now available) followed by a structured side-by-side, not a quick
skim.
**Priority:** HIGH -- real, peer-reviewed, unusually close overlap; now
unblocked since the PDF is in hand.

---

#### [ ] T78. De Broglie Double-Solution Pilot-Wave Comparison (Darrow & Bush 2024)

**Status:** PENDING. Filed 2026-09-10.
**Source:** `docs/misc/notes 2026-09-10.txt`; PDF at
`assets/pdfs/2408.06972v1.pdf` (arXiv:2408.06972v1). Darrow & Bush (2024),
published in *Symmetry* -- real, peer-reviewed, open-access paper on a
Lorentz-covariant, two-way-coupled pilot-wave framework with Compton-scale
oscillations satisfying the de Broglie relation. Also the paper the
Consensus.app review cited as the literature backing its "Moderate (6/10)"
rating for PDTP's "wave-based matter models" claim.
**What:** Compare against PDTP's own matter-wave (psi) framework --
same spirit and rigor level as the Elastic Universe review (T27): extract
useful structural parallels and differences, honestly, without claiming
either framework validates the other.
**Key questions:**
1. Does Darrow & Bush's Compton-scale oscillation mechanism match PDTP's
   own treatment of matter-wave oscillation (psi field, coupling to phi)
   structurally, or only by analogy?
2. Is their two-way coupling (particle affects wave, wave affects
   particle) the same coupling structure as PDTP's cos(psi - phi) term,
   or a different mechanism?
3. Does their Lorentz-covariant formulation offer anything PDTP's current
   (largely non-relativistic-limit-first) derivations haven't addressed?
**Cross-check with:** T27 (Elastic Universe review methodology), core
Lagrangian psi field definition.
**Effort:** Low-Medium -- comparison doc, not new derivation.
**Priority:** MEDIUM.

---

### Phase 7 — Decoupling Device Speculation / Frequency-Ladder Brainstorm (2026-04-16)

**Source:** User conversation 2026-04-16 on Element 115, Lazar device geometry,
and how to bridge the 10^27 frequency gap from current technology (~10^15 Hz)
to omega_gap ~ 10^42 Hz (Part 29 bottleneck).

**Motivation:** T26 (Lazar truth table) identified the frequency gap as the
central physics problem for Goal 2. T28-T35 break the gap into specific,
mathematically-tractable sub-problems. All are [SPECULATIVE] and depend on
Goal 1 being validated. The purpose is to surface candidate mechanisms that
might fall out of the math when treated rigorously — a brainstorm channel.

**Device geometry (Lazar-described, for reference in all T28-T35):**
- Triangular element pointed downward (Z_3 symmetry axis)
- Tube with wider bottom, narrower top (converging horn)
- Top cap connected via DOME to base plate (closed outer loop)
- Toroidal channel inside the base plate (closed inner loop)
- Outer + inner loops = Hopf-linked topology
- Radial injector protruding into the main tube (mode driver)

#### [x] T28. Element 115 / Mc-299 Topological Closure Lens — DONE (Part 137, 2026-08-30)

**RESULT:** Full writeup `docs/research/magic_number_topology.md`, resolved
together with T40 (near-identical hypothesis, see that entry's RESULT for
the shared verdict). Three independent tests, all NEGATIVE: (1) no
candidate closed-network counting sequence (3D harmonic oscillator,
cuboctahedral/FCC shells -- Part 54's own lattice type, tetrahedral
numbers) reproduces the real magic numbers 2,8,20,28,50,82,126 beyond
the first 2-3 terms, which are already explained by the standard
pre-spin-orbit shell model (Mayer 1949; Haxel/Jensen/Suess 1949) -- not
evidence of Z_3 structure. (2) Consecutive differences of the real magic
numbers are NOT uniformly divisible by 3 (fails at the 3rd gap: 8 is not
a multiple of 3) -- directly answers KQ3, no. (3) Even hypothetically,
PDTP's own established vortex-baryon energies (E_Y=2.74 GeV, E_H=17.2
GeV, Part 37/106) overshoot the ~1-2 MeV target shell gap by 1800-11000x,
with no established suppression mechanism (contrast Part 118's derived
v^4 DM suppression). KQ1 (derive shell gap from topology): no. KQ2 (is
Mc-299 topologically special): no principled basis, since no Z_3-network
structure exists to make it special within. The underlying T37 gap
(~9-15 MeV to Lazar's stable-115 claim) is NOT closed by this negative --
it only rules out the PDTP-topological explanation specifically;
standard shell-correction theory (Strutinsky, FRDM, Moller-Nix) remains
the unexamined path.

**What:** Apply PDTP Z_3 / baryon-triangulation view to nuclear magic numbers.
Does shell closure at N=184, Z=114/120/126 correspond to closed vortex-network
topology in the SU(3) condensate?
**Key questions:**
1. Can the nuclear shell model's ~1-2 MeV extra binding at magic numbers be
   derived from closed Z_3 vortex-loop topology rather than mean-field potential?
2. Does Mc-299 (Z=115, N=184) sit at a special topological point (one away from
   double-magic closure)? Predicted half-life in PDTP terms?
3. For each candidate magic N, can a corresponding closed Z_3 network be drawn?
   (2,8,20,28,50,82,126,184 — is this a Z_3 sequence?)
**Cross-check with:** Part 37 (SU(3) Y-junctions), Part 38 (lattice MC), Part 53 (Z_3 Koide)
**Effort:** Medium. Algebra + comparison to standard nuclear shell model.
**Likely outcome:** Either a topological re-derivation of magic numbers (huge) or
a NEGATIVE showing the sequence is not Z_3-generated (confirms nuclear shells
are independent of PDTP condensate). Both informative.

#### [ ] T29. Phase Self-Locking Mechanism [SPEC]

**What:** Derive the conditions under which a matter phase psi locks to an
INTERNAL resonance ψ_nuc (nuclear mode) rather than to the external spacetime
phase phi. If achievable, this is the PDTP mechanism for "self-generated
antigravity" — the object becomes its own phase reference.
**Key equations to derive:**
1. Two-timescale EOM: ddot(psi) = -g sin(psi - phi) + g_int sin(psi - psi_nuc)
2. Regime condition: g_int >> g => <cos(psi - phi)> averages to 0 over coupling time
3. Required Q-factor of internal oscillator: Q > omega_internal / g
4. Compatibility with Part 33 (winding n = m_cond/m) — does a high-Q internal
   mode change the effective winding?
**Key questions:**
- What nuclear isomers or resonances could provide g_int >> g?
- Can two-phase Delta_- (Part 61) act as the internal reference?
- Does self-locking require the nucleus to be in a metastable state, or can
  ground-state nuclei self-lock under external drive?
**Cross-check with:** Part 29 (decoupling energy 10 kW/ton), Part 33 (winding),
Part 61 (two-phase Delta_-), Part 62 (reversed Higgs mass m^2 = 2g Phi)
**Effort:** Medium. New SymPy derivation of two-timescale EOM.
**Likely outcome:** Either a concrete Q-factor threshold (testable against
known nuclear isomers) or a proof that no known isomer can reach it.

#### [ ] T30. Hopf-Link Topology Protection [SPEC]

**What:** Hopf-linked structures (two interlocking vortex loops that cannot be
separated without cutting) are topologically protected in real condensates
(liquid crystals, ferromagnets, superfluids). Investigate whether a Hopf-
linked geometry in the PDTP condensate preserves phase coherence for vastly
longer than simple vortex structures.
**Key questions:**
1. What is the decoherence time of a Hopf-linked phase mode vs an ordinary
   vortex ring? (Standard result: topological protection ~ exp(E_barrier/kT).)
2. Does the PDTP Lagrangian admit Hopfion solutions? (Skyrme-Faddeev model is
   known to.)
3. Can a macroscopic Hopf-link device enforce coherence at 10^15 Hz for 10^27
   cycles? (N cycles / f gives physical time to hold coherence.)
4. Is the Lazar-device geometry (dome + toroid) literally Hopf-linked, and if
   so does that match the condensate Hopfion mode?
**References:** Kedia-Bialynicki-Birula (2013) Hopfion EM solutions; Faddeev-
Niemi (1997) Hopfions in SU(2) sigma model; Shen et al. (2014) optical Hopfions.
**Cross-check with:** Part 27 (tensor GW modes), Part 36 (flux tubes)
**Effort:** Medium-High. Requires introducing Hopfion ansatz into PDTP EOM.
**Likely outcome:** Either PDTP admits stable Hopfion solitons (major new
object type) or the Lagrangian is too simple to support them (new constraint).
**Cross-reference (2026-09-10):** T76 investigates a related but distinct
question -- linked-loop topology as a possible dark-matter MASS/ABUNDANCE
mechanism (ring-on-chain idea, [SPECULATIVE]), vs. this item's DECOHERENCE
PROTECTION question. Both concern interlinked-loop topology in the PDTP
condensate; check T76 for overlap before extending either investigation,
so they don't duplicate work on the same underlying structure.

#### [ ] T31. Nonlinear Converging Horn / High-Harmonic Generation [SPEC]

**What:** In a nonlinear medium, concentrating a wave to small cross-section
triggers high-harmonic generation (HHG) — the mechanism behind attosecond
science (Nobel 2023). PDTP's cos(psi - phi) is automatically nonlinear.
Derive HHG in the cos coupling: what harmonic ladder does amplitude
concentration produce?
**Key equations to derive:**
1. Expand cos(Delta) = 1 - Delta^2/2 + Delta^4/24 - Delta^6/720 + ... up to O(Delta^8)
2. For a driving wave Delta(t) = A sin(omega t), compute output harmonics
   (A^2 gives 2omega, A^3 gives 3omega, etc.)
3. Effective "chi3" nonlinear coefficient of the cos coupling compared to
   fused-silica Kerr chi3 (~ 10^-22 m^2/V^2)
4. Amplitude amplification factor vs tip diameter ratio (bottom/top) of horn
5. Predicted harmonic efficiency: A_n / A_1 as function of driving amplitude A
**Key questions:**
- What is the cutoff harmonic order for PDTP HHG?
- Does the Z_3 triangular tip preferentially generate harmonics at 3n (n=1,2,3...)
  rather than at all integer harmonics?
- Can stacked converging horns (fractal cascade) chain HHG stages?
**Cross-check with:** Part 28c (nonlinear wave effects), Part 61 (two-phase)
**Effort:** Medium. SymPy expansion of cos + harmonic balance analysis.
**Likely outcome:** Explicit formula for harmonic amplitudes; efficiency estimate
tells us whether ~90 stages are physically plausible or hopeless.

#### [ ] T32. Soliton Compression / Supercontinuum in PDTP [SPEC]

**What:** In Kerr-nonlinear media, a single strong pulse undergoes soliton
fission and shedding, generating a frequency comb spanning 4-5 orders of
magnitude from one input. Does PDTP cos coupling support Kerr-like self-phase
modulation? Can a single phase pulse generate a comb reaching omega_gap?
**Key equations to derive:**
1. NLSE (nonlinear Schrodinger equation) reduction of PDTP EOM for slowly-
   varying phase envelope: i dA/dt = -beta d^2A/dz^2 + gamma |A|^2 A
2. Soliton solution: A(z,t) = A_0 sech(t/T_0) exp(i z/z_s)
3. Soliton fission threshold: pulse energy E > N * E_fundamental gives N-soliton
   breakup into comb
4. Spectral width formula: Delta omega / omega ~ gamma |A_0|^2 L (accumulated
   nonlinear phase)
**Key questions:**
- Does PDTP cos coupling reduce to NLSE in the slowly-varying approximation?
- What is the "dispersion" beta in PDTP? (Derivative term in the Lagrangian.)
- Single-pulse comb span: what is the maximum omega_max / omega_min achievable?
- Can soliton compression + horn concentration (T31) combine to bridge 10^27?
**References:** Dudley-Genty-Coen (2006) Rev.Mod.Phys. "Supercontinuum generation
in photonic crystal fiber"; Agrawal "Nonlinear Fiber Optics" (textbook)
**Cross-check with:** Part 27 (wave modes), Part 28c (nonlinear catalog), T31
**Effort:** Medium-High. NLSE reduction + SymPy + numerical soliton fission.
**Likely outcome:** Either PDTP supports supercontinuum (new mechanism for
broad-spectrum phase emission) or reduces to a trivial NLSE that doesn't
span orders of magnitude.

#### [ ] T33. Geometric Blueshift via Condensate Infall [SPEC]

**What:** Waves falling toward a gravitational horizon blueshift by 1/(1-v/c),
which diverges at the horizon. This is the mechanism behind the "trans-
Planckian problem" in Hawking radiation. If a device can engineer a LOCAL
condensate infall flow (analogous to Painleve-Gullstrand), any input wave
moving with the flow blueshifts by 1/(1-v/c). For v/c = 1 - epsilon,
blueshift factor = 1/epsilon. For epsilon = 10^-27, gives the 10^27x
kick "for free."
**Key equations to derive:**
1. Extend Part 101 condensate infall velocity profile v(r) to arbitrary
   toroidal geometry
2. Compute wave blueshift factor f_out / f_in = sqrt((1+v/c)/(1-v/c)) (rel. Doppler)
3. Derive v(r) for the Lazar-device toroidal-channel geometry
4. Find maximum v/c achievable without forming a true horizon (wavebreaking limit)
5. Energy balance: how much input energy does the condensate flow consume to
   provide the blueshift? (Conservation: blueshift is paid for by flow kinetic energy.)
**Key questions:**
- Can the toroidal-channel geometry force v/c close to 1 stably?
- What is the backreaction on the condensate flow from the blueshifted wave?
- Does this mechanism predict a maximum attainable frequency f_max before
  the flow wavebreaks or the geometry collapses?
**Cross-check with:** Part 73 (acoustic metric), Part 98 (TIR at r_S), Part 101
(condensate compression), Part 24 (Hawking T_H)
**Effort:** High. New hydrodynamic derivation in toroidal coordinates.
**Likely outcome:** Formula for max f_max given flow geometry; may reveal
that infall geometry naturally hits an analog horizon and the Hawking emission
(T35) becomes the dominant effect.

#### [ ] T34. Fractal Z_3 Cascade / Frequency Ladder [SPEC]

**What:** If Z_3 vortex structure self-replicates fractally — each vortex
spawning 3 sub-vortices at 3x frequency and 1/3 scale — a cascade of n
generations gives 3^n frequency ladder. Reaching omega_gap / omega_0 = 10^27
requires log_3(10^27) = 57 generations. Investigate whether the PDTP
Lagrangian supports such a fractal Z_3 cascade.
**Key equations to derive:**
1. SU(3) nested-vortex ansatz: U(x) = U_0(x) U_1(x/l_1) U_2(x/l_2) ...
   with l_n = l_0 / 3^n
2. Stability analysis: is the n-th level stable against decay to the (n-1)-th?
3. Frequency hierarchy: does each nested vortex oscillate at 3 times the
   frequency of its parent?
4. Energy of the cascade: sum E_n = sum (1/n)^alpha — convergence condition
5. Cut-off depth: at which n does the scale reach sub-Planckian (l_n < l_P)?
**Key questions:**
- Does SU(3) admit Z_3 nested-vortex solutions analytically?
- Is the Z_3 center an exact fractal generator, or does each level have
  different group structure?
- If cascade reaches depth 57 then terminates at sub-Planck scale, the
  maximum frequency is ~ 3^57 * omega_0 — matches 10^42 Hz for omega_0 ~ 10^15?
**Cross-check with:** Part 37 (Z_3 center), Part 53 (Koide Z_3), Part 38 (lattice MC)
**Effort:** High. Novel SU(3) soliton construction + renormalization-group
style analysis of scale hierarchy.
**Likely outcome:** Either PDTP has a natural fractal cascade (beautiful, and
matches the 10^27 gap) or the Lagrangian forbids nesting below l_P (expected).

#### [x] T36. Three-Component Hopf Link as Baryon Structure [DONE Part 106 Phase 74, 2026-04-18]

**Resolution:** PARTIAL — structurally consistent but energetically disfavored
vs Y-junction (Part 37). Hopf-link remains a candidate for excited baryons
and for T30 (topologically protected device coherence).

**Script:** `simulations/solver/t36_hopf_link_baryon.py` (7 steps)
**Doc:** `docs/research/hopf_link_baryon.md`
**Tests:** SymPy 9/9 PASS, Sudoku 20/20 PASS (all reading COMPUTED values).

**Key results:**
- Eq 106.1 [DERIVED]: 3 Hopf fibers at 120 deg pairwise linked |lk|=1.
- Eq 106.2 [VERIFIED]: Gauss integral |lk| = 1.000 (200x200 grid).
- Eq 106.3 [DERIVED]: B = sum(o_i)/3 reproduces standard QCD baryon numbers
  for baryon, antibaryon, meson, tetraquark (4/4 match).
- Eq 106.4 [DERIVED]: E_H / E_Y = 2 pi EXACTLY at same scale.
  Y-junction is energetically favored; Hopf-link has topological protection.
- Eq 106.5 [DERIVED + WZ fix]: loop circulation alone gives J = integer;
  Wess-Zumino phase exp(i N_c pi B) = -1 at (N_c=3, B=1) gives fermion
  statistics (same Skyrme-Witten fix as all topological baryon models).
- Eq 106.6 [DERIVED]: Z_3 color x SU(3) flavor x U(1)_EM factorisation;
  proton = +1, neutron = 0, Delta++ = +2 all computed correctly.
- Eq 106.7 [DERIVED]: R_i = m_i c^2 / (2 pi sigma); u,d ~ 0.058 fm; s ~ 0.087 fm.

**Negative results:** Hopf-link is NOT the energetic ground state; Y-junction
(Part 37) remains preferred.

**Open questions for future work:**
- Hopf <-> Y-junction transition energy barrier (lattice MC).
- Mass matching to specific excited baryons (Roper N(1440), etc.).
- T30 device-scale Hopf coherence signature.

---

#### Original entry (for historical reference): T36. Three-Component Hopf Link as Baryon Structure [SPEC, Goal 1]

**Source:** User proposal 2026-04-16 based on Hopf-link / trefoil covering.
**Reference image:** `assets/images/Hopf link 3 hoops GWWJV.gif`
**Reference:** Math StackExchange 4066425 (3-component Hopf link covers the trefoil)
https://math.stackexchange.com/questions/4066425/the-3-component-hopf-link-covering-the-trefoil

**What:** In Part 37 a baryon is modelled as a Y-junction of three Z_3 vortices
meeting at a point (three rays). Investigate an alternative topology: the baryon
is a **three-component Hopf link** — three interlinked CLOSED loops, each a
quark, pairwise linked with linking number 1. Total linking number = 3 =
baryon number. The three loops form a 3-fold Z_3-symmetric structure that
covers a trefoil knot.

**Why this could work (structural reasons):**
1. Baryon number B = sum of pairwise linking numbers = 3 (from 3 pairs of loops)
2. Color confinement = topological protection: can't remove one quark without
   breaking all three loops (must cut the link)
3. Z_3 symmetry is manifest: 120-degree rotation cycles the three loops
4. Trefoil connection: the 3-link double-covers the trefoil knot (deep
   topological relationship; trefoil appears in SU(2) Wess-Zumino anomaly
   and in color-flavor locking)
5. Meson = 2-component Hopf link (quark-antiquark pair), linking number 1
6. Connection to T30 (2-component Hopf link in device): same topological
   mechanism at two scales — baryons microscopic, device macroscopic

**Key equations to derive:**
1. Hopf-link ansatz in SU(3) condensate: U(x) from 3 linked loops gamma_1,
   gamma_2, gamma_3 with pairwise linking lk(gamma_i, gamma_j) = 1
2. Total baryon charge: B = (1/3) * sum_{i<j} lk(gamma_i, gamma_j) = 1 (for 3 pairs)
3. Energy of 3-link configuration vs energy of Y-junction flux tube (Part 37):
   E_Hopf = f(R, r, separation) — does it beat E_Y = 3 * sigma * L?
4. Stability: compute the pair-linking-number conservation law. Is
   decay = unlinking forbidden for any continuous field evolution?
5. Angular momentum: each loop has circulation n_i * h/m_cond. Sum to total
   baryon spin. Can we get J = 1/2 (proton spin) from three linked loops?
6. Mass from loop radii: does R_i * r_i * mass density give quark masses?
   Compare to Part 53 Koide: M_u : M_d : M_s = 2 : 5 : 95. Does loop-
   radius ratio reproduce this?
7. Charge distribution: each loop carries fractional charge +/- 1/3 or +/- 2/3.
   Is the Hopf link compatible with the (2/3, -1/3, -1/3) proton charge pattern?

**Key questions:**
- Is the 3-link energetically favored over the Y-junction in PDTP?
- Does the 3-link support Regge trajectories (J vs M^2 linear) like mesons/baryons?
- Do excited baryons correspond to trefoil -> figure-8 -> higher knot transitions?
- Can the glueball spectrum be derived from closed-loop (unlinked) solutions?
- Connection to Skyrme baryons (U(x) with non-trivial pi_3(SU(3)) = Z)?

**Topology math needed:**
- Linking number via Gauss integral: lk = (1/4 pi) * integral integral
  (dr_1 x dr_2).(r_1-r_2) / |r_1-r_2|^3
- Covering map: how the 3-link projects to the trefoil
- Z_3 symmetry group action on the link

**Cross-check with:**
- Part 37 (Y-junction baryon — the current PDTP baryon model)
- Part 38 (lattice string tension — can Hopf-link give same sigma?)
- Part 53 (Koide Z_3 — linking numbers and Z_3 both give "three")
- Part 30 (Faddeev-Niemi Hopfions — related construction in SU(2))
- T30 (2-component Hopf link in device geometry)

**Connection to T30:** If both baryons AND the Lazar device geometry are
Hopf-linked, it suggests Hopf structure is THE natural topology for stable
phase objects in PDTP. This would unify: baryons (3-link), mesons (2-link),
device cavities (2-link at macro scale), Hopfion solitons (T30).

**Effort:** High. Topological / knot-theoretic derivation + SymPy for
linking-number integrals + numerical energy comparison to Y-junction.

**Likely outcome:**
- If E_Hopf < E_Y: major model shift — baryons are loops, not Y-junctions.
  Rewrites Part 37 and knocks on to Parts 38-41 (lattice).
- If E_Hopf > E_Y: Y-junction is confirmed as the stable topology.
- If both are metastable: baryon ground state vs excited state candidates.

**Priority:** Medium-High. Structural alternative to Part 37 is foundational
enough to investigate even speculatively. Could resolve or deepen the SU(3)
confinement picture.

#### [ ] T35. Analog-Horizon Hawking Emission Test [SPEC, testable]

**What:** If T33 succeeds (condensate-flow geometry creates a local analog
horizon), the device should emit Hawking-like phase noise at temperature
T_H = hbar kappa / (2 pi k_B) where kappa is the surface gravity of the
analog horizon. This is a TESTABLE consequence that does not depend on
whether the device "works" for antigravity.
**Key equations to derive:**
1. Compute kappa for the Lazar-device toroidal-flow geometry from T33
2. Predict T_H (likely micro-Kelvin or nano-Kelvin range for lab-scale devices)
3. Predict phase-noise spectrum at the tip of the triangular element
4. Specific-heat signature: device under drive should have excess phase
   fluctuations proportional to T_H
5. Dependence on drive amplitude: T_H scales with v/c at the horizon, which
   scales with drive amplitude
**Key questions:**
- At what drive power does T_H exceed thermal noise floor of best detectors?
- Is the spectrum Planckian (thermal) or structured (informs horizon physics)?
- Does the Z_3 triangular tip produce anisotropic emission (preferred directions)?
**Cross-check with:** Part 24 (Hawking T_H exact), Part 73 (acoustic metric),
Part 98 (TIR / evanescent signature), T33
**Effort:** Medium-High. Depends on T33 being derived first; then standard
analog-gravity machinery (Unruh-DeWitt detector analysis).
**Likely outcome:** A concrete, numerical, testable prediction — independent
of whether Lazar's claims are true. This is the T26 truth-table payoff:
a test that works regardless of the source of the hypothesis.

#### [x] T37. Isotope Stability Mini-Project (SEMF Baseline) [DONE PARTIAL Part 107 Phase 75, 2026-04-29]

**What:** Build an empirical baseline predictor for isotope stability and
decay half-lives using the Bethe-Weizsacker Semi-Empirical Mass Formula
(SEMF) plus standard decay-channel formulas. Validate against ~15 known
isotopes. Then scan Z=115 to find the SEMF-predicted longest-lived
moscovium isotope. This is the foundation for T28 (topological magic-number
derivation) and T40 (PDTP topological correction to nuclear binding).

**Why:** Bob Lazar (transcript "This Is The Truth About Element 115",
2026-04-28) claims a stable isotope of Z=115 exists and is the propulsion
fuel of the S4 craft. Standard SEMF almost certainly predicts NO stable
Z=115 isotope -- not even near the predicted island of stability (N=184).
The gap between SEMF prediction and Lazar's claim is exactly what PDTP
topology must close (T28, T40) to be relevant to engineering Goal 2.
Without a working SEMF predictor, we cannot quantify the size of that gap.

**Steps (checklist):**

- [x] 1. SEMF binding_energy(Z, N) implemented with Krane (1988) coeffs (Eq 107.1).
- [x] 2. Q-values for alpha / beta- / beta+ / EC / p / n channels (Eqs 107.3a-e); all computed from mass-excess differences.
- [x] 3. Decay-rate formulas: Viola-Seaborg (alpha), Sargent (beta), Bohr-Wheeler+WKB (SF) (Eqs 107.4-6); all computed from Q.
- [x] 4. nucleon_stats(Z, N, electrons=Z) wrapper; every field computed (RECHECK rule); special-case A<=1 returns stable for H-1.
- [x] 5. Reference T_1/2 table for 15 isotopes (NUBASE2020); H-1, He-4, Be-8, C-12, O-16, Ca-40, Ca-48, Fe-56, Pb-208, Bi-209, Po-210, Th-232, U-235, U-238, Mc-289.
- [x] 6. Sudoku validation built; **6/15 PASS** at 1.0 OoM tolerance (under the aspirational 12/15 target). Failures cluster cleanly at shell-stabilised nuclei (Pb-208, Bi-209, Ca-48), Be-8 (He-4 doubly-magic), heavy alpha emitters (actinide Q-value sensitivity through Viola-Seaborg), and super-heavy SF (no shell corrections).
- [x] 7. Z=115 scan: longest-lived predicted **A=315 (N=200)**, log_T = +1.06, T ~ 11 s, dominant SF (edge-of-scan; SEMF cannot see N=184 magic-number bump).
- [x] 8. Z=114, 116, 118 cross-check: monotonic decrease of longest-lived T with Z (Z=114 -> +4.06, Z=116 -> -1.77, Z=118 -> -6.88). Real island has non-monotonic bump at N=184 from shell effects -- our baseline misses this cleanly.
- [x] 9. Empty stub `pdtp_topology_correction(Z, N) -> 0.0` reserved for T40.
- [x] 10. Log saved to `simulations/solver/outputs/isotope_stability_<ts>.txt`.
- [x] 11. Research doc `docs/research/isotope_stability.md` (~280 lines, plain English + full derivations + Lazar gap quantification at ~10 MeV).
- [x] 12. equation_reference.md updated with Eqs 107.1-107.11 (all tagged ESTABLISHED / VERIFIED; no PDTP Original results in this Part).
- [x] 13. MEMORY.md updated (one new entry); falsifiable_predictions.md updated with topology-correction row + pending Prediction 13 placeholder (deferred until T40 supplies pdtp_topology_correction).

**Cross-check with:** T28 (topological closure lens for Mc-299), T40 (proposed
nuclear topology from Y-junction packing), Part 37 (SU(3) Y-junction baryon),
Part 106 (Hopf-link baryon variant).

**Files:**
- Script: `simulations/solver/isotope_stability.py` (Phase 75)
- Doc:    `docs/research/isotope_stability.md` (Part 107)
- Log:    `simulations/solver/outputs/isotope_stability.txt`

**Effort:** Medium. SEMF and decay formulas are textbook (~150 lines core);
validation table and Sudoku checks are the bulk of the work.

**Likely outcome:** SEMF reproduces the stable-isotope chart at >= 12/15 hit
rate. Z=115 SEMF prediction: longest-lived isotope is Mc-289 or similar with
T_1/2 ~ milliseconds-seconds, NO stable isotope at any N. This is the
EXPECTED gap that T28 / T40 need to close. The size of that gap (in MeV of
binding energy needed for stability at Mc-299) becomes a quantitative
target for PDTP topology.

**Related to Lazar transcript:** "Bob Lazar -- This Is The Truth About
Element 115" (YouTube video Yci8FyI1768; transcript in repo root). Bismuth
(Z=83) is the heaviest near-stable element; same column as Z=115 (group 15).
Lazar predicts a stable Z=115 isotope used for gravitomagnetic propulsion
(Ning Li). SEMF gives the standard-physics answer; PDTP topology (T28, T40)
is the candidate mechanism for the gap.

---

### Phase 8 — Nuclear Topology and WCT Cross-checks (2026-05-09)

#### [x] T40. Nuclear Geometry from Y-Junction Packing — DONE (conceptual, Part 137, 2026-08-30)

**RESULT:** Full writeup `docs/research/magic_number_topology.md`, run
together with T28 since both test the identical core hypothesis (verbatim
overlap confirmed before starting: T40 KQ1 = T28 KQ3; T40's own text
lists T28 as a cross-check partner). Conceptual Key Questions 1, 2, 4
resolved NEGATIVE -- see T28's RESULT above for the shared numeric
findings (no surviving closed-network counting rule; E_Y/E_H overshoot
the ~11 MeV target by 249x/1566x). KQ3 (is Mc-299 one proton from a
closed network at Z=114) not assessable -- no established closed-network
definition exists at the nuclear scale to test proximity to. KQ5
(implementable as `pdtp_topology_correction(Z,N)`): no principled formula
survived to implement. **Implementation steps 4-8 (build the correction
function, wire into t37_isotope_stability.py, re-run Sudoku/Z=115 scan,
update falsifiable_predictions.md Prediction 13) were explicitly NOT
executed** -- there is no formula to wire in, and implementing a null/
zero correction would only reproduce T37's already-on-record baseline
(6/15 Sudoku, Mc-315 longest-lived ~11s), adding no new information.
This is the "clean NEGATIVE... rules out this mechanism" outcome T40's
own "Likely outcome" field anticipated as valid.

**Part:** 137
**What:** Apply PDTP Y-junction / Z_3 vortex-network geometry (Part 37) to
nuclear magic numbers. The goal is to fill `pdtp_topology_correction(Z, N)`
in `t37_isotope_stability.py` with a PDTP-derived correction rather than
a zero stub, closing the ~27 OoM / ~8-14 MeV gap identified in T37.

**Why now:** T37 (Part 107) established the SEMF floor and quantified the
gap from standard physics to Lazar's stable Z=115 claim. Standard shell
corrections (Strutinsky, FRDM, Moller-Nix) explain ~1-2 MeV of shell
binding via mean-field potential. PDTP candidate: closed Z_3 vortex-loop
networks (Y-junction packing) give extra binding at magic-number closures
from topological protection, not mean-field.

**Key questions:**
1. Do the nuclear magic numbers (2, 8, 20, 28, 50, 82, 126, 184) correspond
   to complete closed Z_3 vortex networks in the SU(3) condensate?
2. Is the magic-number sequence derivable from a Z_3 packing rule, or is
   it purely coincidental?
3. Does Mc-299 (Z=115, N=184) sit one proton away from a closed Z_3
   network at Z=114 (Fl), making it "almost magic" with partial extra binding?
4. How much extra binding (in MeV) does a closed vs open Z_3 network predict?
   Target: ~8-14 MeV at (Z=115, N=184) to bridge the Lazar gap.
5. Can the correction be expressed as a function `pdtp_topology_correction(Z, N)`
   that can be dropped into T37's SEMF predictor without restructuring?

**Steps (checklist):**
- [x] 1. Review magic-number sequence vs Z_3 closed-network counting rule. -- DONE, NEGATIVE (Sec 3-4, magic_number_topology.md)
- [x] 2. Derive topological binding delta_B_topo(Z, N) from Y-junction geometry. -- ATTEMPTED: no closed network survived step 1 to derive a binding formula FROM; energy-scale check (Sec 5) shows E_Y/E_H are 1800-11000x too large regardless
- [x] 3. SymPy verify; Sudoku 10+ tests reading from computed values. -- N/A, no formula produced by steps 1-2 to verify (all comparisons in Sec 3-5 are direct numeric computation, RECHECK-compliant, no hand-waved returns)
- [ ] 4. Implement `pdtp_topology_correction(Z, N)` and drop into t37_isotope_stability.py. -- NOT EXECUTED, no surviving formula to implement (would just be a null/zero stub, no new information)
- [ ] 5. Re-run Sudoku; target >= 15/19 (was 10/19 with delta_B = 0). -- NOT EXECUTED, moot (step 4 not done)
- [ ] 6. Re-run Z=115 scan; report new longest-lived and Mc-299 half-life. -- NOT EXECUTED, moot (step 4 not done)
- [x] 7. Research doc (full derivation + plain English); update equation_reference.md. -- DONE, `docs/research/magic_number_topology.md`
- [ ] 8. Update falsifiable_predictions.md Prediction 13 placeholder. -- NOT EXECUTED; Prediction 13 remains an open target for standard shell-correction theory (Sec 9), not PDTP topology -- no update needed from this result

**Cross-check with:** T37 (SEMF baseline), T28 (Mc-299 topological closure),
Part 37 (SU(3) Y-junction), Part 106 (Hopf-link baryon)
**Effort:** Medium-High.
**Likely outcome:** Either a topological re-derivation of some magic numbers
(validates PDTP nuclear sector) or a clean NEGATIVE showing Z_3 packing
gives the wrong sequence (rules out this mechanism; narrows T28 search).

---

#### [ ] T38. WCT Regularizer as UV-Cure Candidate [SPEC, low priority]

**Part:** TBD
**Source:** Wave Confinement Theory YouTube video review, May 2026.
**Reference:** `D:\Dropbox\wave\` (screenshots + video summary)

**What:** The WCT regularizer has the form:
  Theta[psi] = -Delta(psi) / (psi + epsilon * exp(-alpha |psi|^2))
This suppresses UV divergences by introducing amplitude-dependent damping,
without requiring explicit renormalization counterterms. Investigate whether
this functional form appears naturally in PDTP from the cos coupling
nonlinearity, or whether it can be adopted as a UV completion of the
PDTP Lagrangian.

**Key questions:**
1. Does the PDTP cos(psi - phi) coupling produce a similar amplitude-
   dependent regularization when expanded to high order?
   (cos expansion: 1 - x^2/2 + x^4/24 - ... gives built-in convergence.)
2. Is the WCT Theta functional equivalent to any known PDTP term
   (phi_- mass, reversed Higgs, higher-harmonic sin^2 from T23)?
3. If Theta[psi] is NOT already in PDTP, could it be added as a
   new Lagrangian term without breaking established results (Newton, GR, Hawking)?
4. Does the epsilon parameter in Theta have a PDTP interpretation
   (condensate healing length xi? decoupling coupling g?)?

**Cross-check with:** Part 35 (dimensional transmutation, beta function),
T23 (sin^2 second harmonic), Part 62 (reversed Higgs mass)
**Effort:** Low-Medium. Mostly analytical comparison; no new simulation needed
unless the form survives initial scrutiny.
**Priority:** Low — speculative cross-framework import.

---

#### [ ] T39. WCT Effective Metric Cross-check [SPEC, low priority]

**Part:** TBD
**Source:** Wave Confinement Theory YouTube video review, May 2026.

**What:** WCT derives an effective spacetime metric from wave-confinement
geometry. Cross-check whether this effective metric matches:
(A) PDTP acoustic metric (Part 73 / Unruh 1981): g_mu_nu derived from
    condensate flow field v(r) and speed of sound c_s = c
(B) PDTP SU(3) spatial metric (Part 75-76): g_ij = (1/3) Tr(dU^dag dU)

**Key questions:**
1. Does the WCT effective metric reproduce g_tt = -(1 - 2GM/rc^2)?
   (If yes: same Newtonian limit as PDTP; if no: which one is wrong?)
2. Does WCT give gamma = 1 (full spatial curvature) or gamma = 0 (scalar only)?
   This is the Part 100 lensing question applied to an independent framework.
3. Does WCT have a breathing-mode analogue (massive scalar sector)?
   If yes: independent prediction of the PDTP breathing mode (testable overlap).
4. Are there any WCT predictions that DIFFER from both GR and PDTP?
   If so: which framework wins against experiment?

**Cross-check with:** Part 73 (acoustic metric), Part 98 (n_PDTP = 1/alpha),
Part 100 (lensing gap NEGATIVE), Part 75-76 (SU(3) graviton)
**Effort:** Low. Mostly literature/video review + comparison table.
**Priority:** Low — external framework; useful only if WCT metric is distinct
enough from PDTP to provide independent constraints.

---

#### [x] T41. O(eps^4) Nonlinear Vertex vs Einstein-Hilbert — DONE (Part 114, Phase 82, 2026-06-10)

**Part:** 114 (Phase 82) -- `simulations/solver/su3_nonlinear_vertex.py`
**Doc:** `docs/research/su3_nonlinear_vertex.md`
**Closes:** Part 76g OPEN item ("full nonlinear equivalence remains OPEN")
**Result:** CONSTRUCTIVE NEGATIVE + PRODUCTIVE. 14/14 Sudoku PASS.

**What was found:**
1. Exact quartic vertex [DERIVED]: g^(4)_mu_nu = -(eps^4/24) f^(abe) f^(cde)
   chi^a (d_mu chi^b) chi^c (d_nu chi^d) — upgrades 76g.1 from "~" to exact.
   O(eps^3) vanishes identically; coefficient is group-independent; 0 for U(1).
2. Trace theorem [DERIVED]: L_tree = K*eta^(mu nu)*g_mu_nu — the tree action
   is the eta-trace of the emergent metric, so it contains NO graviton kinetic
   term at any order. Sakharov 1-loop is the UNIQUE source of graviton
   dynamics (Part 74/75's route is forced, not chosen).
3. External anchor [VERIFIED]: SU(2) reduction reproduces Weinberg's 1966
   pi-pi ChPT vertex 1/(6F^2)[(pi.dpi)^2 - pi^2(dpi.dpi)] exactly (residual 0).
4. No-go [DERIVED, NEGATIVE]: derivative grading (NLSM D=2 vs EH D=4,6)
   forbids identifying the tree vertex with GR's nonlinear vertex, on- or
   off-shell.
5. Planck suppression [PDTP Original]: lambda_4/(8*pi*G) = 1/48; the non-GR
   contact term turns on only at E ~ sqrt(6/pi)*m_P = 1.382 m_P. GR recovery
   at first nonlinear order SURVIVES at all accessible energies (~3.5e-31
   at 10 TeV).

**Open items unchanged:** N_eff = 6*pi gap; 2-DOF deficit (8 fields vs 10
metric components); m_cond underdetermined (kappa = c^2/(4*pi*G) still free).

---

#### [x] T42. Extremal Condensate Closure (Option B for m_cond) — DONE (Part 115, Phase 83, 2026-06-10)

**Part:** 115 (Phase 83) -- `simulations/solver/extremal_condensate_closure.py`
**Doc:** `docs/research/extremal_condensate_closure.md`
**Closes:** Eq. 77.25 (extremal condensate hypothesis); problem A1 -> CLOSED-INTERNAL
**Result:** CONSTRUCTIVE NEGATIVE with no-go theorem. 12/12 Sudoku PASS.

**What was found:**
1. Bookkeeping correction [DERIVED]: m_cond = m_P EXCEEDS the literal Eq. 77.24
   bound by sqrt(2) — the Part 77 "saturation" was order-of-magnitude only.
2. Bridge reading [DERIVED]: with G = hbar*c/m_cond^2, the BH bound is
   IDENTICALLY marginal for any m_cond (r_S = 2*lambda_C, l_P = a_0,
   m_cond = m_P all scale-invariant identities). A bound saturated by every
   value selects none.
3. Criticality identity [PDTP Original]: alpha_gr = G*m_cond^2/(hbar*c) = 1
   exactly — the bridge IS the Dvali-Gomez black-hole criticality condition
   alpha*N = 1 (N=1). Each condensate quantum is a marginal black hole.
   Explains why ALL Part 77/78 bounds saturate.
4. No-go theorem [DERIVED, NEGATIVE]: every PDTP-internal observable is
   C*m_cond^d — monotonic (d != 0) or constant (d = 0); no finite extremum
   exists, so NO internal variational principle can select m_cond. Quantum
   transmutation loophole closed by Parts 35/77/38-41.
5. A1 status: OPEN -> CLOSED-INTERNAL. kappa = c^2/(4*pi*G) is PROVABLY
   external input (like Lambda in GR — proven, not analogized). Live route:
   MEASURE omega_gap (breathing mode, Part 29 Strategy A). Stop attempt #13.

#### [x] T43. DM Winding Number Selection — DONE (Part 116, Phase 84, 2026-06-11)

**Part:** 116 (Phase 84) -- `simulations/solver/dm_winding_selection.py`
**Doc:** `docs/research/dm_winding_selection.md`
**Closes:** "DM mass = free parameter" gap (Part 96 D3 / dark_matter_energy.md Part 7)
**Result:** n = 1 SELECTED -> m_DM = m_P. 12/12 Sudoku PASS.

**What was found:**
1. Vortex energy E(n) ~ n^2 ln(R/r_c) [SymPy residual 0]; splitting of n >= 2
   bare vortices releases energy even WITH the PDTP core condition
   r_c = n*lambda_cond [DERIVED] -> only n = 1 survives.
2. Kibble-Zurek Monte Carlo (2M loops): P(|n|>=2)/P(|n|=1) = 0.038 -> defect
   formation makes (almost) only |n| = 1 [DERIVED, numerical].
3. m_DM = m_P = 1.22e19 GeV ("Planck vortex relic") [PDTP Original]. All
   observational tests pass (Bullet 40 OoM margin, cold, smooth on dwarf
   scales, grav-only flux 0.23 /m^2/yr, topologically stable -> no super-GZK
   decays, microlensing unconstrained).
4. NEGATIVE: KZ-at-Planck-epoch + inflation under-produces by ~50 OoM
   (monopole-problem logic). Abundance needs post-inflation production
   (PIDM, Garny+ 2016 PRL 116 101302); pure gravitational channel excludes
   m > 0.01 m_P -> defect channel at preheating required [OPEN].
5. Kill test: scenario requires high-scale inflation -> detectable
   tensor-to-scalar ratio r; LiteBIRD/CMB-S4 null result kills it.
6. Open: O1 line-energy vs mass-map bookkeeping; O2 preheating defect yield;
   O3 Part 89 sigma/m factor-100 erratum check; O4 Omega_DM = 27% not predicted.

#### [x] T44. Positive phi_-^4 Quartic Origin — DONE (Part 117, Phase 85, 2026-06-11)

**Part:** 117 (Phase 85) -- `simulations/solver/phi_minus_quartic.py`
**Doc:** `docs/research/phi_minus_quartic.md`
**Closes:** Part 88 "missing phi_-^4 term" diagnosis (Eq 88.13 gap)
**Result:** POSITIVE quartic FOUND in the induced channel. 10/10 Sudoku PASS.

**What was found:**
1. Channel 1 (tree cosine): quartic = -g/12, wrong sign [NEGATIVE, confirms
   Part 88 Eq 88.13 exactly].
2. Channel 2 (zero-point of locked mode): quartic < 0 [NEGATIVE].
3. Channel 3 [PDTP Original]: integrating out phi_+ at PARTIAL lock
   (psi - phi_+ = pi/2 - beta) gives
   V_ind = -(2g^2 sin^2(beta)/kbar^2) sin^2(phi_-)
   -> lambda_4 = +2g^2 sin^2(beta)/(3 kbar^2) > 0; = (g/3) sin^2(beta) at the
   gap scale kbar^2 = 2g (Part 88 needs ~g: within factor 3-6). SymPy-verified
   (Gaussian matching exact, closed form exact, sign via sp.ask).
4. Self-switching: J, V_ind, lambda_4 all vanish IDENTICALLY at beta = 0 ->
   w = -1 today automatic; Parts 61/63/87 untouched (two-phase Sudoku rule).
5. Open: beta(z) locking history (sets EDE amplitude); tachyonic-roll
   reconciliation with Part 87 phi_-_vac ~ 1e-70 rad.

#### [x] T45. Cleanup: Eq 89.17 Erratum + check_urls.py — DONE (Part 118, Phase 86, 2026-06-11)

**Part:** 118 (Phase 86) -- `simulations/solver/sigma_m_erratum.py`
**Closes:** Part 116 Open Question O3 (Part 89 sigma/m discrepancy)
**Result:** Eq 89.17 corrected. 7/7 Sudoku PASS. Verdicts unchanged.

**What was found:**
1. Eq 89.17 (sigma/m ~ G/c^4 ~ 8.3e-43 m^2/kg = 8.3e-39 cm^2/g) was wrong
   three ways: dimensionally inconsistent (SymPy units), factor-100 numeric
   error, factor-1000 internal unit conversion error.
2. Corrected [DERIVED]: gravitational Rutherford scattering b_90 = 2Gm/v^2,
   sigma = pi b_90^2 -> sigma/m = 4 pi G^2 m_DM/v^4 = 5.2e-49 m^2/kg at
   m_DM = m_P, v = 220 km/s. Bullet margin IMPROVES to 47.3 orders (T69/
   Part 138 correction, 2026-09-02: the Bullet bound constant itself had a
   separate 1000x unit error, 1e-4 vs the correct 1e-1 m^2/kg; original
   Part 118 figure of 44.3 was computed with the wrong constant -- see T69).
3. Updated: condensate_layer_optics.md (erratum block), dark_matter_energy.md,
   dm_winding_selection.md + .py (re-run, still 12/12), equation_reference.md.
4. Tooling: check_urls.py fixed (REPO_DIR pointed at non-existent path after
   the script moved to "github-repo misc/"; non-ASCII print chars crashed
   on Windows cp1252). Now takes optional repo-path argument.

---

## Status Summary

| ID | Investigation | Priority | Status | Part # |
|----|---------------|----------|--------|--------|
| T1 | PDTP refractive index | 1 | DONE | 98 |
| T2 | Critical point tan=1 | 2 | DONE | 99 |
| T3 | Loss tangent + dark energy | 3 | DONE (PARTIAL) | 102 |
| T4 | Brewster angle for GWs | 4 | DONE (PRODUCTIVE) | 108 |
| T5 | Multi-layer stacks | 5 | DONE (PRODUCTIVE+NEG) | 109 |
| T6 | Leidenfrost + phase transition | 6 | DONE (PRODUCTIVE) | 110 |
| T7 | Hawking + n_PDTP | 7 | DONE (CONSTR. NEG.) | 111 |
| T8 | PPN corrections | 8 | DONE (PRODUCTIVE) | 112 |
| T9 | Two-phase tan | 9 | DONE | 113 |
| T10 | SU(3) group tan | 10 | DONE | 121 |
| T11 | Koide angle | 11 | DONE | 122 |
| T12 | Heat kernel tan | 12 | DONE (NEGATIVE) | 129 |
| T13 | Update predictions | -- | DONE | -- (added Predictions 15-16) |
| T14 | Update equation ref | -- | DONE | -- (added Parts 121, 122) |
| M1 | Pythagorean lock-in alpha_EM | SPEC | DONE -- QUASIPERIODIC | -- |
| M2 | tan(theta_W) Pythagorean | SPEC | DONE -- INCONCLUSIVE | -- |
| M3 | Band spacing vs evanescent depth | SPEC | DONE -- DEGENERATE (a=lambda_evan forced) | -- |
| M4 | Min displacement vs vortex winding | SPEC | DONE -- NEGATIVE (pair is forced+unique, not small) | -- |
| T15 | Final verdict | -- | DONE (CLOSED, productive) | -- |
| T16 | Two-phase G_eff closes lensing factor-2? | 16 | DONE (NEGATIVE) | 100 |
| T17 | n=sqrt(2) observable near compact objects | 17 | DONE (NEGATIVE + positive byproduct) | Part 130 |
| T18 | Two-phase Delta_- crossover in dense matter | 18 | DONE (NEGATIVE + true-vacuum re-derivation) | Part 131 |
| T19 | L_4 SymPy verify + b quark check | 19 | DONE (2 errors found+fixed; b-quark match downgraded) | Part 132 |
| T20 | L_4 Goldstone mode -- what is it? | 20 | DONE (genuine independent scalar; not graviton/phi_-) | Part 133 |
| T21 | Condensate compression as spatial curvature (lensing fix?) | 21 | DONE (MIXED) | 101 |
| T22 | Platonic solids lens (discrete symmetry) | 24 (low) | DONE (PARTIAL) | 105 |
| T23 | Hilbert space lens (sin^2 / Im^2 missing term) | 22 (high) | DONE (PRODUCTIVE) | 104 |
| T24 | Backward GR -> PDTP Lagrangian (missing tensor term) | 23 (high) | DONE (CONSTR. NEG.) | 103 |
| T25 | String theory and PDTP (Regge slope, graviton, extra dims) | 25 (low) | DONE (Regge slope NEGATIVE, structural) | 134 |
| T26 | Bob Lazar truth table (decoupling phenomenology) | 26 (low) | DONE (energy budget NEGATIVE ~7 OoM beyond universe mass-energy; 3-emitter/Z3 match = coincidence not evidence) | 135 |
| T27 | Elastic Universe review (shear modes, visualizations) | 27 (low) | DONE -- all 3 phases (E1-E16, J1-J3); site now HAS a Lagrangian (updates prior finding); "Cosserat Charge" fiddle NEGATIVE (no actual Cosserat theory, relevant to T66) | -- |
| T28 | Mc-299 / Element 115 topological closure lens | SPEC | DONE -- NEGATIVE, not Z_3-generated, FCC shells give 0 matches, energy scale 1800-11000x too large | 137 |
| T29 | Phase self-locking mechanism (internal vs external) | SPEC | PENDING | -- |
| T30 | Hopf-link topology protection for phase coherence | SPEC | PENDING | -- |
| T31 | Nonlinear converging horn -> high-harmonic generation | SPEC | PENDING | -- |
| T32 | Soliton compression / supercontinuum in PDTP | SPEC | PENDING | -- |
| T33 | Geometric blueshift via condensate infall (frequency pump) | SPEC | PENDING | -- |
| T34 | Fractal Z_3 cascade / frequency ladder 3^n | SPEC | PENDING | -- |
| T35 | Analog-horizon Hawking emission test (testable signature) | SPEC | PENDING | -- |
| T36 | Three-component Hopf link as baryon (vs Y-junction flux tube) | SPEC (med-high) | DONE (Part 106, Phase 74, 2026-04-18) | PARTIAL -- structurally consistent, E_H/E_Y=2pi, Y-junction preferred |
| T37 | Isotope stability mini-project (SEMF baseline + decay rates; baseline for T28/T40 + Lazar Z=115 gap quantification) | SPEC (med) | DONE PARTIAL (Part 107, Phase 75, 2026-04-29) | 10/19 Sudoku (Wapstra coeffs + 4 extra isotopes); Z=115 longest=1067s; Mc-299(N=184)~9ns; Lazar gap ~27 OoM ~ 8-14 MeV |
| T38 | WCT regularizer Theta[psi] as UV-cure candidate in PDTP | SPEC (low) | PENDING | -- |
| T39 | WCT effective metric cross-check vs PDTP acoustic / SU(3) metric | SPEC (low) | PENDING | -- |
| T40 | Nuclear geometry from Y-junction packing (PDTP shell correction; fills pdtp_topology_correction stub) | SPEC (med-high) | DONE (conceptual) -- resolved with T28, NEGATIVE; implementation steps 4-8 not executed, no formula survived | 137 |
| T41 | O(eps^4) nonlinear vertex vs Einstein-Hilbert (closes 76g OPEN; exact -1/24 vertex; trace theorem; Weinberg ChPT anchor; 1/48 Planck suppression) | high | DONE (CONSTR. NEG. + PRODUCTIVE) | 114 |
| T42 | Extremal condensate closure (closes 77.25; bridge = Dvali-Gomez criticality; scale-invariance no-go theorem; A1 CLOSED-INTERNAL — kappa provably external) | high | DONE (CONSTR. NEG. + no-go theorem) | 115 |
| T43 | DM winding selection (n=1 by stability + KZ; m_DM = m_P; KZ relic abundance NEGATIVE 50 OoM; kill test = CMB tensor modes) | high | DONE (DERIVED + CONSTR. NEG.) | 116 |
| T44 | Positive phi_-^4 quartic (induced channel at partial lock; lambda_4 = 2g^2 sin^2(beta)/(3 kbar^2); transient self-switching EDE; beta(z) OPEN) | high | DONE (PRODUCTIVE) | 117 |
| T45 | Cleanup: Eq 89.17 erratum (sigma/m = 4 pi G^2 m_DM/v^4; Bullet margin 47.3 OoM, corrected T69/Part 138 from misstated 44.3) + check_urls.py path/Unicode fixes | maintenance | DONE | 118 |
| T46 | Lambda as locking relic: phi_-_vac = frozen residue of Part 117 roll; beta(z) -> {EDE, Lambda, w(z)} (3 observables, 1 input) | high (SPEC) | DONE PARTIAL | 119 |
| T47 | m_cond consequence scanner: lookup table of all observables vs candidate m_cond (1 eV..m_P); measurement rules out bands — NOT a brute-force finder (no-go, Part 115) | medium | DONE | 120 |
| T65 | Backfill mathematical_formalization.md (SU(3) + two-phase sections missing) | integration (LARGE) | PENDING | -- |
| T66 | Rotation-field / tetrad promotion (Cosserat-continua analogy) | SPEC (low) | DONE -- info-free relabeling of phi(x) (dim SO(2)=1); sits below Part 84 (1 vs 8 DOF); Cosserat independence violated by construction | 136 |
| T69 | Dark matter doc audit + two current external events (LZ 2.6-sigma event, Roman Space Telescope launch) | audit + lit. review (medium) | DONE -- found+fixed 2 real 1000x unit-conversion bugs (Bullet margin, KM3 ratio); LZ/Roman map to neither PDTP candidate / no PDTP-specific test | 138, 139 |
| T70 | N_eff via spin-weighted Seeley-DeWitt a_2 heat-kernel coefficient (replaces Part 83's naive DOF counting) | medium | DONE -- CONSTR. NEG.: formula unsourced + PDTP has N_v=N_f=0 identically (sigma-model, not gauge theory); Part 83's gap unchanged | 140 |
| T71 | Audit CKN "factor 12" formula discrepancy (Part 54) -- two cited rho_CKN forms don't obviously match | low-medium | PENDING | -- |
| T73 | Glueball mass test vs X(2370) (BESIII, arXiv:2607.20366) -- closed flux-tube loop (Mechanism A) brackets X(2370)'s mass within x5; chi^a contact vertex (Mechanism B) 4.7x too weak; J^PC=0-+ not derivable by either (chi^a are NLSM scalars, T70) | high | DONE -- CONSTRUCTIVE (mass scale) + NEGATIVE (quantum numbers) | 141 |
| T74 | GW170817 constraint on PDTP's GW structure (arXiv:1710.06168) -- tensor sector c_s=c EXACT, trivially passes (4.13e-16 bound computed from source); phi_- scalar sector evanescent at LIGO frequencies for any realized Phi (77 OoM margin) -- no signal existed to constrain; byproduct: fixed 22-OoM erratum in Part 63 S7 | high-medium | DONE -- PASS (tensor) + CONSTRUCTIVE NEGATIVE (scalar) | 142 |
| T75 | TeVeS structural comparison [scoping] -- what does TeVeS's vector field buy it that PDTP's all-scalar field content lacks? | medium | PENDING | -- |
| T76 | Topological DM candidate: ring-on-chain linking [SPECULATIVE, user-original] -- could linking topology alone produce DM-like behavior without exotic energy cost? Must be checked against Part 116 winding-number mechanism first; Rubik's-cube/Cayley-graph idea folded in as secondary analogy | low-medium | PENDING | -- |
| T77 | Timeflow Gravity comparison (Trofimov 2026, Class. Quantum Grav. 43) -- U(1)/circle state space, Jacobson entropic gravity (same tool as Part 86), MOND from phase coherence; PDF now in hand | high | PENDING | -- |
| T78 | De Broglie pilot-wave comparison (Darrow & Bush 2024, Symmetry, arXiv:2408.06972) -- compare Compton-scale pilot-wave oscillation to PDTP's psi field | medium | PENDING | -- |
