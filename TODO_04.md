# TODO_04 — Tangent Function Investigation

**Type:** Full FCC + Wave Check
**Initial investigation:** `docs/research/tan_initial_investigation.md`
**Date opened:** 2026-03-28
**Previous roadmaps:** [TODO_01.md](TODO_01.md) (Parts 1-41) |
[TODO_02.md](TODO_02.md) (Parts 42-76) | [TODO_03.md](TODO_03.md) (Parts 77-83+)

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

#### [ ] T4. Gravitational Brewster Angle — PRIORITY 4

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

#### [ ] T5. Multi-Layer Phase Stacks (Air/Water/Oil Model) — PRIORITY 5

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

#### [ ] T6. Leidenfrost + Tan: Phase Transition Analysis — PRIORITY 6

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

#### [ ] T7. Hawking Temperature with n_PDTP — PRIORITY 7

**What:** Does the refractive index n = 1/alpha modify the Hawking radiation
derivation (Part 24)? The surface gravity kappa involves the gradient of the
metric — which is related to the gradient of alpha (and therefore of n).
**Cross-check with:** Part 24 (Hawking: T_H = hbar*c^3/(8*pi*G*M*k_B))

#### [ ] T8. PPN Parameters with Tan Corrections — PRIORITY 8

**What:** Do the PPN parameters gamma and beta acquire tan-dependent corrections
at post-Newtonian order? PDTP must maintain gamma = 1, beta = 1 to match
solar system tests.
**Cross-check with:** Part 12 (tetrad extension), Part 73 (Einstein recovery)

#### [ ] T9. Two-Phase Tan: Delta_+ and Delta_- — PRIORITY 9

**What:** In the two-phase Lagrangian (Part 61), there are TWO phase differences.
Define tan(Delta_+) and tan(Delta_-). What does the ratio tan(Delta_-)/tan(Delta_+) mean?
Does this connect to the reversed Higgs mass m^2 = 2g*Phi?
**Cross-check with:** Part 61-63 (two-phase Lagrangian, all 16 tests)

#### [ ] T10. SU(3) Tan: Group Manifold Geometry — PRIORITY 10

**What:** Does tan appear naturally in SU(3) Wilson action or group manifold?
The SU(3) generators contain sqrt(3) = tan(60 deg) and 1/2 = tan(~26.6 deg).
Is there a "Brewster angle" on the SU(3) group manifold?
**Cross-check with:** Part 37 (SU(3) condensate), Part 38 (lattice MC)

#### [ ] T11. Koide Angle and Tan — PRIORITY 11

**What:** Koide formula has theta_0 = 2/9. Is tan(2/9) or arctan related to
Z_3 geometry? The Koide angle lives on the flavor circle — does Brewster's
angle appear there?
**Cross-check with:** Part 53 (Z3-Koide derivation)

#### [ ] T12. N_eff and Heat Kernel Tan — PRIORITY 12

**What:** The Sakharov formula heat kernel a_1 coefficient involves curvature
integrals. Does n_PDTP = 1/alpha enter the heat kernel expansion? Could this
modify the 6*pi factor?
**Cross-check with:** Part 83 (N_eff = 6pi gap)

---

### Phase 4 — Integration

#### [ ] T13. Update Falsifiable Predictions

**What:** After T1-T6, update `docs/research/falsifiable_predictions.md` with
any new testable predictions (Brewster angle, transition redshift, etc.).

#### [ ] T14. Update Equation Reference

**What:** Add all new equations (T.1-T.14 and any derived during Parts) to
`docs/research/equation_reference.md`.

#### [ ] T15. Final Verdict and Summary

**What:** Write up the overall findings. Did tan reveal new physics?
Which predictions survived the full FCC + Wave check?
Does any tan result help constrain m_cond or derive G?

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

#### [ ] M3. Band spacing formula and PDTP condensate layers [SPECULATION]

**Formula:** lambda_moire = (1/2) * csc(theta/2) * a  (a = lattice spacing)
  For C1/C2 boundary: theta = angle between gravitational and QCD condensate lattices
  lambda_moire = ? -- if this equals the evanescent depth from Part 89, that
  would be a non-trivial cross-check.
  Part 89: lambda_evan(C2) = 0.00245 fm; lambda_evan(C1) = 0.987 fm
  Can these be expressed as moire band spacings of two misaligned condensates?
**Connection:** T5 (multi-layer stacks) -- each layer boundary has a moire
  angle; the evanescent depth may equal the moire band spacing.

#### [ ] M4. Minimum displacement {s,r} and vortex winding [SPECULATION]

**Wolfram:** Minimum displacement = {s, r} where u=r^2-s^2, v=2rs (Pythagorean generator)
  This {s,r} pair is the smallest lattice vector that leaves the moire unchanged.
  In PDTP: winding number n = m_cond/m_particle (Part 33).
  Is n = r - s or r + s for some Pythagorean generator pair?
  For electron: n = m_P/m_e ~ 2.4e22 -- too large for small integers.
  For QCD condensate: n = m_cond_QCD/m_quark ~ 367MeV/5MeV ~ 73 -- small!
  Check: is 73 = r^2 - s^2 for small integers? 73 = 37^2 - 36^2 = (37-36)(37+36) = 1*73.
  Primitive pair: (r,s) = (37,36), u=73, v=2*37*36=2664. GCD(73,2664) = 1. YES.
  This means quark winding n=73 MAY correspond to a primitive Pythagorean moire.

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

#### [ ] T17. n = sqrt(2) Observable Signature — PRIORITY 17
**Source:** Part 99 open question 2; tan_critical_point.md Sec 10.2
**What:** Near a compact object where Delta_+ approaches pi/4, n_PDTP = sqrt(2) = 1.414.
Is this distinguishable from standard GR lensing at that density?
**Key questions:**
- At what mass density does Delta reach pi/4? Use alpha = 1/sqrt(2) => GM/(rc^2) = 1 - 1/sqrt(2) ~ 0.293.
  => r = GM/(0.293 * c^2) = 0.293 * r_S (inside the Schwarzschild radius!) -- probably not observable.
- For neutron stars (r ~ 3 r_S): Delta_+ is small but nonzero. What is n there?
- Could the n=sqrt(2) signature appear in gravitational lensing of light near black holes?
  VLBI/EHT images of M87* and Sgr A* probe r ~ 1.5-6 r_S.
**Cross-check with:** Part 98 (TIR table: n=3.3 at r=1.1*r_S), Part 73 (Kerr metric PDTP)
**Effort:** Medium (need to map density to Delta; VLBI data comparison).

#### [ ] T18. Two-Phase Delta_- Crossover Near Dense Matter — PRIORITY 18
**Source:** Part 99 open question 3; tan_critical_point.md Sec 10.3
**What:** The reversed Higgs (Part 62) gives phi_- a mass near matter: m^2 = 2g*Phi.
Does Delta_- ever reach pi/4 inside a neutron star or white dwarf?
**Key questions:**
- Delta_- equation of motion: involves phi_- mass term from Part 62.
  Is there a stable crossover state Delta_- = pi/4 inside dense objects?
- If Delta_- = pi/4 inside a neutron star: n_- = sqrt(2). Would this affect
  neutron star oscillation modes (f-modes, g-modes)?
- Connection: reversed Higgs at equilibrium phi_- = pi/2 (Part 62) vs crossover pi/4.
  Are these the same thing or different states?
**Cross-check with:** Part 61-62 (two-phase, reversed Higgs), Part 99 (crossover analysis)
**Effort:** Medium (extend Part 62 to solve for Delta_- profile inside dense star).

#### [ ] T19. L_4 SymPy Verification and b Quark Check — PRIORITY 19
**Source:** pdtp_lagrangian4.md -- all results currently [SPECULATIVE, unverified]
**What:** L_4 = L_kinetic + L_self + L_cross adds J_{ab} cos(phi_a - phi_b) inter-layer coupling.
Verify ALL results with SymPy before accepting any as [DERIVED].
**Tasks (in order):**
1. SymPy: Euler-Lagrange equations for all 4 fields (phi_1, phi_2, phi_3, psi) from L_4.
   Verify signs, symmetry, conservation law sum_a FE_a.
2. SymPy: Mass matrix M^2 eigenvalues (3x3 Laplacian). Verify zero eigenvalue (Goldstone) exact.
3. SymPy: Isolated C2-C3 mode mass = sqrt(g_2 * g_3) with J_{23} = g_2*g_3/2.
   Numerical: sqrt(0.200 GeV * 80.4 GeV) = 4.010 GeV vs m_b = 4.18 GeV (4% off).
4. Physical argument: why does J_{ab} = g_a*g_b/2 (product rule) rather than sqrt(g_a*g_b)/2
   (geometric mean rule)? Is there a symmetry or dimensional argument?
5. What IS the C2-C3 mode physically? It has no colour charge, no spin-1/2.
   Candidates: scalar meson near 4 GeV? Chi_c(1P) charmonium at 3.51 GeV? B meson (5.28 GeV)?
**Cross-check with:** L_1/L_2/L_3; Part 37 (SU(3) condensate); Part 53 (Koide Z3)
**Effort:** Medium-High (new script needed: lagrangian4.py)

#### [ ] T20. L_4 Goldstone Mode — What Is It? — PRIORITY 20
**Source:** pdtp_lagrangian4.md Sec "Goldstone mode"
**What:** L_4 has a global U(1) symmetry phi_a -> phi_a + c for all a simultaneously.
This guarantees one massless Goldstone mode. What is this mode physically?
**Key questions:**
- The Goldstone is the overall phase of the combined condensate (gravity + QCD + EW).
  Is this the graviton? (massless, spin-2 -- but Goldstone is spin-0 scalar)
- Or is this phi_- from Part 61? (also massless in vacuum, from broken Z_2 symmetry)
  Connection: L_4 Goldstone + Part 61 phi_- -- are they the same degree of freedom?
- If the Goldstone is eaten by a gauge field (Higgs mechanism for inter-layer coupling):
  what gets mass? Could this be the mechanism behind the W/Z mass acquisition?
- Sudoku check: Goldstone theorem (Weinberg 1995, Sec 19.2) requires massless mode
  for every broken continuous symmetry. L_4 has one U(1) -- one Goldstone. VERIFY.
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

#### [ ] T22. Platonic Solids Lens — Topology / Discrete Symmetry

**Part:** TBD (after user picks order)
**What:** Use the 5 Platonic solids and their finite symmetry groups
(tetrahedral T_d, octahedral O_h, icosahedral I_h) as a discrete-symmetry lens
on PDTP. McKay correspondence (finite SU(2) subgroups <-> Platonic groups <->
ADE Lie algebras) gives a bridge from discrete geometry to gauge symmetry.

**Key questions:**
1. Part 37 Y-junction (3 vortices at 120 deg) is a 2-simplex. Extending to a
   tetrahedral 4-vortex 3-simplex: does it forbid (3 only allowed) or permit
   a 4th flavour generation?
2. Part 21 oscillator lattice -- what crystal structure (cubic, FCC, BCC,
   diamond)? The coordination number could fix K = 1/(4 pi) geometrically.
3. Could the 3 fermion generations be the 3 reflection planes of T_d?
4. McKay: SU(2) finite subgroups -> Platonic -> ADE. Does PDTP's SU(3) extension
   have a Platonic-group precursor that constrains its representations?
5. Anti-icosahedral (Z_5) -- could this give a hidden 5-fold symmetry that
   relates to the cosmological constant scale (Penrose tiling, quasicrystals)?

**Expected effort:** Medium. Mostly literature + algebra.
**Likely outcome:** [SPECULATIVE]. Best case: discrete group fixes N_gen or Omega_m.
Worst case: reframes "why 3 generations" without solving it.
**Priority:** Lower (most speculative of the three).

#### [ ] T23. Hilbert Space Lens — Real and Imaginary Parts

**Part:** TBD
**What:** Promote PDTP's classical phase fields phi, psi to Hilbert-space states
|phi>, |psi> and examine what new terms appear from the imaginary part of the
inner product. Currently alpha = cos(Delta) = Re<psi|phi> is the gravitational
coupling [Part 28b]. The imaginary part Im<psi|phi> = sin(Delta) appears only
as a force gradient -- never as an independent Lagrangian term.

**Hypothesis (Maxwell scaffolding move, Methodology section 2):**
There may be a missing term proportional to sin^2(Delta) = (Im<psi|phi>)^2
in the Lagrangian. This would be a Z_2-doubled coupling with period pi
(half the period of the existing cos coupling).

**Key questions:**
1. Add L_new = lambda * sum_i sin^2(psi_i - phi) to the PDTP Lagrangian.
   - Use sin^2 = (1 - cos(2 Delta))/2 to rewrite as a doubled-frequency cos term.
   - Re-derive the field equations: Box(phi) = sum_i [g_i sin(Delta_i) + lambda sin(2 Delta_i)]
   - Re-do the pendulum stability analysis -- does the new term shift Delta = pi/4?
2. Compute the new ε(Delta, H) for slow-roll. Does the extra term resolve T3's
   w_a tension? It should ADD a positive contribution to K/V at finite Delta.
3. Density-matrix promotion: rho = |phi><phi|. Mixed states give intrinsic
   damping (loss tangent at the field-theory level, not just cosmological friction).
4. Promote U(1) -> U(2). The 4 generators split as U(1) x SU(2) -- electroweak.
   Does this come naturally from the Hilbert-space promotion?
5. Entanglement: if matter ψ_i and condensate phi are entangled, the reduced
   density matrix has off-diagonal coherences. These contribute extra <H> terms
   absent in the classical limit.

**Expected effort:** Medium-High. Concrete math, SymPy verifiable, can become
a Phase script (Part 103) if the sin^2 term gives a clean derivation.
**Likely outcome:** [DERIVED] Either (a) a new Lagrangian term that resolves
w_a, or (b) a NEGATIVE proving the sin^2 term is forbidden by some symmetry.
**Priority:** High (most concrete path to a new Lagrangian term).

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

#### [ ] T25. String Theory and PDTP — Graviton Comparison

**Part:** TBD
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

#### [ ] T26. Bob Lazar Truth Table — Decoupling Phenomenology

**Part:** TBD
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

#### [ ] T27. Elastic Universe Review — Shear Modes and Visualizations

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

---

## Status Summary

| ID | Investigation | Priority | Status | Part # |
|----|---------------|----------|--------|--------|
| T1 | PDTP refractive index | 1 | DONE | 98 |
| T2 | Critical point tan=1 | 2 | DONE | 99 |
| T3 | Loss tangent + dark energy | 3 | DONE (PARTIAL) | 102 |
| T4 | Brewster angle for GWs | 4 | PENDING | TBD |
| T5 | Multi-layer stacks | 5 | PENDING | TBD |
| T6 | Leidenfrost + phase transition | 6 | PENDING | TBD |
| T7 | Hawking + n_PDTP | 7 | PENDING | TBD |
| T8 | PPN corrections | 8 | PENDING | TBD |
| T9 | Two-phase tan | 9 | PENDING | TBD |
| T10 | SU(3) group tan | 10 | PENDING | TBD |
| T11 | Koide angle | 11 | PENDING | TBD |
| T12 | Heat kernel tan | 12 | PENDING | TBD |
| T13 | Update predictions | -- | PENDING | -- |
| T14 | Update equation ref | -- | PENDING | -- |
| M1 | Pythagorean lock-in alpha_EM | SPEC | DONE -- QUASIPERIODIC | -- |
| M2 | tan(theta_W) Pythagorean | SPEC | DONE -- INCONCLUSIVE | -- |
| M3 | Band spacing vs evanescent depth | SPEC | PENDING | -- |
| M4 | Min displacement vs vortex winding | SPEC | PENDING | -- |
| T15 | Final verdict | -- | PENDING | -- |
| T16 | Two-phase G_eff closes lensing factor-2? | 16 | DONE (NEGATIVE) | 100 |
| T17 | n=sqrt(2) observable near compact objects | 17 | PENDING | -- |
| T18 | Two-phase Delta_- crossover in dense matter | 18 | PENDING | -- |
| T19 | L_4 SymPy verify + b quark check | 19 | PENDING | -- |
| T20 | L_4 Goldstone mode -- what is it? | 20 | PENDING | -- |
| T21 | Condensate compression as spatial curvature (lensing fix?) | 21 | DONE (MIXED) | 101 |
| T22 | Platonic solids lens (discrete symmetry) | 24 (low) | PENDING | -- |
| T23 | Hilbert space lens (sin^2 / Im^2 missing term) | 22 (high) | PENDING | -- |
| T24 | Backward GR -> PDTP Lagrangian (missing tensor term) | 23 (high) | DONE (CONSTR. NEG.) | 103 |
| T25 | String theory and PDTP (Regge slope, graviton, extra dims) | 25 (low) | PENDING | -- |
| T26 | Bob Lazar truth table (decoupling phenomenology) | 26 (low) | PENDING | -- |
| T27 | Elastic Universe review (shear modes, visualizations) | 27 (low) | PENDING | -- |
