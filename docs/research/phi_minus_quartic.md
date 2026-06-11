# Origin of a Positive phi_-^4 Term — Induced Quartic at Partial Lock (Part 117)

**Status:** Tree and zero-point channels NEGATIVE (wrong sign, as Part 88 found).
Induced channel POSITIVE: lambda_4 = 2 g^2 sin^2(beta)/(3 kbar^2) > 0 at partial
locking. Algebra SymPy-verified; the cosmological mechanism remains [SPECULATIVE].
**PDTP Original:** Induced positive quartic from integrating out the gravity mode
phi_+ at a partially locked background.
**Date:** 2026-06-11 (Phase 85)
**Script:** `simulations/solver/phi_minus_quartic.py`
**Log:** `simulations/solver/outputs/phi_minus_quartic_20260611_193027.txt`
**Prerequisites:** [two_phase_rederivation.md](two_phase_rederivation.md) (Parts 61/63),
[hubble_tension_c1.md](hubble_tension_c1.md) (Part 88),
[cosmo_constant_a3.md](cosmo_constant_a3.md) (Part 87)

---

## Plain English Summary

Part 88 found that PDTP cannot explain the Hubble tension unless the phi_-
field (the condensate's "surface tension mode") has a **stiffening** quartic
term — a +phi_-^4 piece in its potential with strength about g. The problem:
the natural cosine potential gives the term with the **wrong sign** (it
softens instead of stiffens). Part 88 filed three speculative places the
right-signed term could come from. This Part computes all three.

**What we found:**

1. **Tree level:** wrong sign, exactly as Part 88 said (coefficient -g/12).
   Confirmed, not fixed. [NEGATIVE]
2. **Quantum zero-point energy:** also wrong sign. [NEGATIVE]
3. **The new result:** if the universe is only PARTIALLY phase-locked —
   matter waves not yet fully synchronised with spacetime waves, which is the
   natural state of the EARLY universe — then the gravity mode phi_+ can be
   "integrated out" (its back-reaction computed), and this back-reaction
   generates exactly the missing term, with the RIGHT sign and roughly the
   RIGHT size: lambda_4 = (g/3) x (degree of mis-lock)^2. [PDTP Original]

**Why this is elegant:** the term exists ONLY while locking is incomplete.
As the universe finishes locking (today), the term switches itself off
automatically — so dark energy behaves like a plain cosmological constant
now (w = -1, as observed), but acted differently in the early universe
(Early Dark Energy), which is exactly the ingredient the Hubble tension
needs. No tuning is required to turn it off; the physics does it.

**What is still missing:** how mis-locked the universe was at each epoch
(the function beta(z)). Without that we can predict the SHAPE of the effect
but not its absolute size. That is the next open problem.

**Honest caveat:** the induced term also pushes phi_- away from zero while
locking is incomplete (a "tachyonic roll"). Whether that roll deposits the
right amount of energy at redshift ~3000, and how it reconciles with the
tiny present-day value phi_-_vac ~ 1e-70 rad (Part 87), is open.

---

## 1. Problem Statement

Part 88 Eq 88.12b-88.13: Early Dark Energy (the leading proposal to resolve
the 5-sigma Hubble tension) requires

```
   V_EDE(phi_-) = g phi_-^2 + lambda_4 phi_-^4,   lambda_4 ~ +g   [REQUIRED]
```

but the two-phase cosine potential supplies the quartic with the wrong sign:

```
   -2g cos(phi_-) = -2g + g phi_-^2 - (g/12) phi_-^4 + ...   [Part 88 Eq 88.13]
```

Methodology.md strategies applied: **Scaffolding term** (Maxwell-style: what
term would close the gap, and is it physical?) and **Work backwards** (what
generates lambda_4 > 0?). Three candidate channels (Part 88 §"Origin of
quartic term") are computed below.

---

## 2. Setup — Exact Two-Phase Coupling [VERIFIED]

**Starting point** (Part 61): with phi_b = phi_+ + phi_- and
phi_s = phi_+ - phi_-,

```
   cos(psi - phi_b) - cos(psi - phi_s) = 2 sin(psi - phi_+) sin(phi_-) (117.1)
```

**SymPy verification:** residual = 0. [VERIFIED]

The interaction potential is V = -L_int:

```
   V(psi, phi_+, phi_-) = -2 g sin(psi - phi_+) sin(phi_-)            (117.2)
```

**Background convention** (Part 63): the locked vacuum has psi - phi_+ = pi/2
(the map chi = phi_+ + pi/2 reduces two-phase to single-phase exactly).
**Partial locking** means

```
   psi - phi_+ = pi/2 - beta,    beta != 0                            (117.3)
```

beta = 0 is today's fully locked universe; beta ~ O(1) is the generic
pre-locked early universe. [ASSUMED — the locking history beta(z) is not
derived here; see Open Question O1]

---

## 3. Channel 1 — Tree Level [NEGATIVE]

Expand (117.2) about the joint vacuum (delta = psi - phi_+ - pi/2,
chi = phi_- - pi/2):

```
   V = -2g sin(pi/2 + delta) sin(pi/2 + chi) = -2g cos(delta) cos(chi) (117.4)
```

Setting delta = 0 (its minimum) and series-expanding (SymPy, computed):

```
   V(0, chi) = -2g cos(chi) = -2g + g chi^2 - (g/12) chi^4 + ...      (117.5)
```

- mass term coefficient: **+g** (stable) [VERIFIED]
- quartic coefficient: **-g/12** — exactly Part 88 Eq 88.13. [VERIFIED]

**Verdict: NEGATIVE.** Tree level cannot supply the EDE term. (Confirms
Part 88; the cosine softens — every bounded periodic potential flattens away
from its minimum at this order.)

---

## 4. Channel 2 — Zero-Point (One-Loop) [NEGATIVE]

The locked matter mode delta has a chi-dependent mass (computed from the
delta^2 coefficient of 117.4):

```
   m_delta^2(chi) = 2 g cos(chi)                                      (117.6)
```

Its zero-point energy (Coleman-Weinberg 1973, single-mode approximation,
hbar = 1):

```
   V_zp(chi) = (1/2) omega(chi) = (1/2) sqrt(2 g cos(chi))            (117.7)
```

Series expansion (SymPy, computed):

```
   V_zp = sqrt(2g)/2 - (sqrt(2) sqrt(g)/8) chi^2
          - (sqrt(2) sqrt(g)/192) chi^4 + ...                         (117.8)
```

Quartic coefficient = -0.00737 sqrt(g) at g = 1: **negative again.**

**Verdict: NEGATIVE.** Quantum corrections of the locked mode also soften.
(SymPy applicability note: the single-mode zero-point form (117.7) is itself
an approximation; the SIGN conclusion is what is used, and it is computed.)

---

## 5. Channel 3 — Induced Quartic at Partial Lock [PDTP Original]

### 5.1 Derivation, step by step

**Step 1.** Background (117.3) with phi_+ fluctuation eta:

```
   V(eta, phi_-) = -2 g sin(pi/2 - beta + eta) sin(phi_-)             (117.9)
```

**Step 2.** Expand to O(eta^2) (SymPy, computed):

```
   V_0   = -2 g cos(beta) sin(phi_-)            [eta^0 term]          (117.10)
   J     = +2 g sin(beta) sin(phi_-)            [linear source, -J eta] (117.11)
   M_pot = +2 g cos(beta) sin(phi_-)            [eta^2 stiffness part] (117.12)
```

Note J vanishes at beta = 0: at full lock there is NO linear coupling of
phi_+ fluctuations to phi_- (this is why Parts 61-63 never saw this term).

**Step 3.** The phi_+ kinetic term contributes gradient stiffness
(1/2) kbar^2 eta^2 for a mode of momentum kbar. Full stiffness
M = kbar^2 + M_pot.

**Step 4.** Integrate out eta exactly (Gaussian; tree-level matching,
Peskin & Schroeder ch. 11). Minimising (M/2) eta^2 - J eta + V_0:

```
   eta* = J/M,    V_min = V_0 - J^2/(2M)                              (117.13)
```

**SymPy verification:** solve + substitute reproduces V_0 - J^2/(2M)
exactly; residual = 0. [VERIFIED]

**Step 5.** Gradient-dominated regime (kbar^2 >> M_pot):

```
   V_ind = -J^2/(2 kbar^2) = -(2 g^2 sin^2(beta)/kbar^2) sin^2(phi_-) (117.14)
```

**SymPy verification:** closed form matches; residual = 0. [VERIFIED]

**Step 6.** Series in phi_- (sin^2 x = x^2 - x^4/3 + ...; SymPy, computed):

```
   V_ind = -(2 g^2 sin^2(beta)/kbar^2) phi_-^2
           + (2 g^2 sin^2(beta)/(3 kbar^2)) phi_-^4 + ...             (117.15)
```

### 5.2 Result

```
┌──────────────────────────────────────────────────────────────────────┐
│   lambda_4 = + 2 g^2 sin^2(beta) / (3 kbar^2)  >  0   for beta != 0  │
│                                                                      │
│   [PDTP Original — POSITIVE quartic, generated by integrating out   │
│    the gravity mode phi_+ at a partially locked background.          │
│    Algebra DERIVED + SymPy-verified; cosmological application        │
│    SPECULATIVE.]                                            (117.16) │
└──────────────────────────────────────────────────────────────────────┘
```

**Sign check (SymPy ask):** lambda_4 positive for g, kbar^2 > 0, beta != 0.
[VERIFIED]

**Plain English (why the sign flips):** integrating out a field always LOWERS
the potential by J^2/(2M), and the lowering is strongest where the source J
is largest — at phi_- = +/-pi/2. Digging the potential down at pi/2 relative
to 0 is precisely a stiffening +phi_-^4 contribution around 0 (together with
a destabilising mass term that starts phi_- rolling). The cosine could never
do this at tree level because it only ever flattens.

---

## 6. Magnitude and Locked Limit

### 6.1 Magnitude [PARTIAL]

At the natural stiffness scale kbar^2 = 2g (the two-phase gap scale, Part 61):

```
   lambda_4 / g = sin^2(beta) / 3                                     (117.17)
```

| beta | lambda_4/g (computed) |
|------|----------------------|
| 5 deg | 0.0025 |
| 30 deg | 0.083 |
| 45 deg | 0.167 |
| 90 deg | 0.333 |

Part 88 requires lambda_4 ~ g. At order-unity partial lock the induced value
is within a factor 3-6. **Shape and order of magnitude supplied; the absolute
EDE energy density depends on the cosmological g and on beta(z), which are
not derived here.** [PARTIAL]

### 6.2 Locked limit beta -> 0 (today) [VERIFIED]

```
   J(0) = 0,   V_ind(0) = 0,   lambda_4(0) = 0      [computed, exact] (117.18)
```

The induced term vanishes IDENTICALLY at full lock. Therefore (two-phase
Sudoku check, CLAUDE.md rule 4):

- Newton's 3rd law psi_dd = -2 phi_+_dd (Part 61) — unchanged (derived at
  the locked background, where the new term is zero).
- Biharmonic equation nabla^4 Phi + 4g^2 Phi (Part 61) — unchanged.
- Jeans eigenvalue +2 sqrt(2) g (Part 61) — unchanged.
- Lambda = g phi_-_vac^2 (Part 87) and w = -1 today — recovered automatically.

**This is the self-switching-off property: EDE is transient by construction.**

---

## 7. Sudoku Scorecard

| # | Test | Computed value | Verdict |
|---|------|---------------|---------|
| T1 | product identity residual = 0 | 0 | PASS |
| T2 | tree quartic = -g/12 (Part 88 Eq 88.13) | -g/12 | PASS |
| T3 | zero-point quartic < 0 | -0.00737 g | PASS |
| T4 | Gaussian V_min = V_0 - J^2/(2M) exact | residual 0 | PASS |
| T5 | V_ind closed form -c sin^2(phi_-) | match | PASS |
| T6 | lambda_4 = 2g^2 sin^2(beta)/(3 kbar^2) | match | PASS |
| T7 | lambda_4 > 0 for beta != 0 | positive (SymPy ask) | PASS |
| T8 | magnitude order unity at gap scale | 0.333 g at beta = 90 deg | PASS |
| T9 | induced term vanishes at beta = 0 | all zero | PASS |
| T10 | induced mass^2 < 0 at partial lock | -2g^2 sin^2(beta)/kbar^2 | PASS (tachyonic roll, flagged) |

**Score: 10/10 PASS.** Channels 1-2 pass by CONFIRMING their negative sign —
the Part 88 diagnosis was correct; only the third channel produces the
required term.

---

## 8. Falsifiable Consequence (proposal — not yet filed)

If the Hubble tension is real physics, PDTP now has a CANDIDATE mechanism
(not just a missing-term diagnosis): transient EDE from incomplete phase
locking, which automatically switches off as beta -> 0. The sharpened fork of Part 88
Eq 88.14:

- Hubble tension real -> w(z) deviates from -1 around matter-radiation
  equality with amplitude controlled by sin^2(beta(z)); DESI DR2 + CMB-S4
  test this.
- Hubble tension systematics -> beta(z) was already negligible by z ~ 3000;
  no PDTP modification needed.

(Addition to `falsifiable_predictions.md` requires user approval — proposed
in the session summary, not yet filed.)

---

## 9. Open Questions

- **O1 — locking history beta(z).** The single undetermined input. Needs a
  cosmological solution of the two-phase equations through the radiation era.
  Until then the mechanism gives shape, not amplitude. [OPEN]
- **O2 — tachyonic roll vs Part 87.** The induced mass term -2c phi_-^2
  drives phi_- from 0 toward pi/2 while beta != 0. How the field returns to
  the tiny present value phi_-_vac ~ 1e-70 rad (Part 87) as the term switches
  off — and how much energy the roll deposits at z ~ 3000 — is open. (Hubble
  friction freezes the roll once the induced mass drops below H; a dynamical
  study is needed.) [OPEN]
- **O3 — beyond single-mode zero-point.** Channel 2 used a single-oscillator
  approximation; a full one-loop computation could shift the (negative)
  coefficient but not obviously the sign. [OPEN, low priority]
- **O4 — gradient-dominated assumption.** (117.14) takes kbar^2 >> M_pot;
  the opposite regime gives V_ind ~ -g tan(beta) sin(beta) sin(phi_-)
  (renormalised tilt, odd powers only — no quartic). The physical kbar is
  set by the horizon-scale mode spectrum. [OPEN]

---

## 10. References

**Source:** Coleman, S. & Weinberg, E. (1973), Phys. Rev. D 7, 1888
(one-loop effective potential).
**Source:** Peskin, M. & Schroeder, D. (1995), *An Introduction to Quantum
Field Theory*, ch. 11 (integrating out fields; effective action matching).
**Source:** Part 61/63 — `two_phase_rederivation.md` (product identity,
locked background chi = phi_+ + pi/2).
**Source:** Part 88 — `hubble_tension_c1.md` (EDE requirement; Eq 88.13).
**Source:** DESI Collaboration (2024), arXiv:2404.03002 (evolving dark energy).
**PDTP Original:** Induced positive quartic
lambda_4 = 2 g^2 sin^2(beta)/(3 kbar^2) at partial lock; self-switching-off
transient EDE (this document).

---

*Part 117, Phase 85. Previous: Part 116 (DM winding selection).*
*Updates: `dark_matter_energy.md` (DE section), `equation_reference.md`.*
