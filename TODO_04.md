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

#### [ ] T1. PDTP Refractive Index — PRIORITY 1

**Part:** 84 (or next available)
**What:** Rigorously derive n_PDTP = 1/cos(Delta) = 1/alpha from the Lagrangian.
Show it reduces to the GR refractive index n_GR = 1 + 2Phi/c^2 in the weak-field limit.
**Cross-check with:**
- Part 31 (phase refraction analysis) — already uses Snell's law
- Part 28c (wave catalog: lensing = refraction, horizon = TIR)
- Part 24 (Hawking radiation) — does n_PDTP modify the derivation?
**Sudoku:** Standard 10+ tests with n_PDTP substituted
**SymPy:** Verify weak-field expansion: 1/cos(Delta) ≈ 1 + Delta^2/2 + ... ≈ 1 + 2Phi/c^2
**Wave check:** Effects 5 (refraction), 6 (TIR), 12 (lensing) from wave catalog

#### [ ] T2. Critical Point at tan = 1 (45 degrees) — PRIORITY 2

**Part:** Next after T1
**What:** Derive the physical meaning of tan(Delta) = 1. Is Delta = pi/4 a
dynamical attractor, repeller, or saddle point? Stability analysis.
**Key questions:**
- In the potential V = -g*cos(Delta), what happens at Delta = pi/4?
- Is this a bifurcation point? Does the system behaviour change qualitatively?
- Connection to the Leidenfrost "sizzling" regime (Part 71 Sec 4.1)
**Cross-check with:**
- Part 71 (Leidenfrost: potential landscape V(theta) at pi/4)
- Part 61 (two-phase: does phi_- affect the critical angle?)
**SymPy:** Stability eigenvalues at Delta = pi/4

#### [ ] T3. Gravitational Loss Tangent and Dark Energy — PRIORITY 3

**Part:** Next after T2
**What:** Connect tan(Delta) = force/coupling to the dark energy equation of state.
Derive whether tan = 1 predicts the transition redshift z ~ 0.7.
**Key questions:**
- Part 19 gives w(z) = (epsilon-1)/(epsilon+1). If epsilon maps to tan, what w(z) does this give?
- At the transition: alpha = cos(pi/4) = 0.707. Does this constrain g_eff/H^2?
- Is the phase drift rate d(Delta)/dt derivable from the field equations?
**Cross-check with:**
- Part 19, 25 (dark energy as phase drift / normal fraction)
- Part 54 (cosmological constant FCC)
- DESI w(z) data (2024-2025 releases)
**Wave check:** Effect 40 (beats/dark energy) from wave catalog
**Sudoku:** Test w(z_transition) prediction against observed value

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

#### [ ] M1. Pythagorean lock-in of alpha_EM [SPECULATION]

**Compute:** arccos(sqrt(alpha_EM)) = arccos(0.08542) = 85.1 degrees
  tan(85.1 deg) = 11.55...   -> nearest Pythagorean: tan=u/v
  Closest primitive pairs: (11,1)->(11.0), (23,2)->(11.5), (34,3)->(11.33)
  Best: (23,2): tan=11.5 -> alpha_pred = 1/(1+11.5^2) * ... -> check
**Why:** If alpha_EM corresponds to a Pythagorean angle, the EM and spacetime
  lattices are in exact rational commensurability and alpha_EM is derivable
  from the pair (u,v). If not, alpha_EM is quasiperiodic (confirmed free param).
**Connection:** T10 (SU(3) group tan) -- the SU(3) generators define angles
  in group space; their tan ratios may be Pythagorean.

#### [ ] M2. tan(theta_W) = u/v for Weinberg angle [SPECULATION]

**Compute:** tan(theta_W) where sin^2(theta_W) = 0.231 -> theta_W = 28.74 deg
  tan(28.74) = 0.549...   -> nearest primitive: (1,2)=0.5, (3,5)=0.6, (5,9)=0.555
  Best: (5,9) -> tan=5/9=0.556 (1.2% off). Check: is (5,9) primitive? GCD(5,9)=1. YES.
  -> sin^2(theta_W) from (5,9): sin^2 = 25/(25+81) = 25/106 = 0.2358 (2% off 0.231)
  At GUT scale: sin^2=3/8 -> tan=sqrt(3/5)=0.7746 ~ (3,4) Pythagorean? tan(3/4)=0.75 (3%)
**Why:** If SU(5) embedding sets a Pythagorean angle, RG running rotates
  the moire pattern from (3,4) at GUT to (5,9) at weak scale. This gives
  a GEOMETRIC running of sin^2(theta_W) -- same physics as T3 (loss tangent).

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

## Status Summary

| ID | Investigation | Priority | Status | Part # |
|----|---------------|----------|--------|--------|
| T1 | PDTP refractive index | 1 | PENDING | TBD |
| T2 | Critical point tan=1 | 2 | PENDING | TBD |
| T3 | Loss tangent + dark energy | 3 | PENDING | TBD |
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
| M1 | Pythagorean lock-in alpha_EM | SPEC | PENDING | -- |
| M2 | tan(theta_W) Pythagorean | SPEC | PENDING | -- |
| M3 | Band spacing vs evanescent depth | SPEC | PENDING | -- |
| M4 | Min displacement vs vortex winding | SPEC | PENDING | -- |
| T15 | Final verdict | -- | PENDING | -- |
