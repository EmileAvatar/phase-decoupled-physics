# Coupling Constant g — A6 FCC (Part 94)

**Status:** PARTIAL + FREE
**Script:** `simulations/solver/coupling_constant_g.py` (Phase 63)
**Scorecard:** 12/12 PASS

---

## Problem Statement

The PDTP Lagrangian contains a coupling constant g:

```
L = (1/2)(d_mu phi)(d^mu phi) + Sum_i (1/2)(d_mu psi_i)(d^mu psi_i) + Sum_i g_i cos(psi_i - phi)
```

**A6 question:** What determines g? Can it be derived from first principles, or is it a free parameter?

---

## Plain English Summary

g is the "strength of gravity" in the PDTP Lagrangian — how strongly matter-waves pull on spacetime-waves. It turns out g equals the Planck frequency (the fastest possible oscillation rate), about 1.86×10⁴³ cycles per second. You can compute it from G, ℏ, and c alone. But that means g is just another name for G — they carry the same information. Knowing one tells you the other. Neither is independently derived from topology or group theory (yet). So g remains a free parameter, just like Newton's G.

**The key new result:** G × g² = c⁵/ℏ. This is a constraint linking gravity and the Lagrangian coupling — not a free-parameter reduction, but a useful identity showing all three (G, g, m_cond) encode the same physics.

---

## Starting Equations

**Eq 2a** [PDTP Original, DERIVED — Part 33]:
```
(94.0)  G = hbar * c / m_cond^2
```
Source: vortex winding derivation, `vortex_winding_derivation.md`

**Eq 4e** [PDTP Original — Part 34]:
```
(94.1)  g = m_cond * c^2 / hbar     [units: rad/s]
```
Source: condensate self-consistency, `condensate_selfconsist.py`

---

## Derivation: G × g² = c⁵/ℏ

**Step 1.** From Eq 94.1, solve for m_cond:
```
(94.2)  m_cond = hbar * g / c^2
```

**Step 2.** Substitute Eq 94.2 into Eq 94.0:
```
(94.3)  G = hbar * c / (hbar * g / c^2)^2
           = hbar * c * c^4 / (hbar^2 * g^2)
           = c^5 / (hbar * g^2)
```

**Step 3.** Rearrange:
```
(94.4)  G * g^2 = c^5 / hbar    [PDTP Original, DERIVED]
```

This is an exact algebraic identity — no approximations. It holds for any value of m_cond.

**Step 4.** Solve for g:
```
(94.5)  g = sqrt(c^5 / (hbar * G))
```

Numerically:
```
g = sqrt((2.998e8)^5 / (1.055e-34 * 6.674e-11))
  = sqrt(2.431e42 / 7.04e-45)
  = sqrt(3.45e86)
  = 1.855e43 rad/s
```

**Step 5.** Verify this equals the Planck angular frequency:
```
(94.6)  omega_P = m_P * c^2 / hbar = 1.855e43 rad/s    [known value]
```
g = omega_P exactly. [VERIFIED, residual = 1.4e-16, machine precision]

---

## What Does g Measure?

In PDTP, g controls the strength of phase coupling between matter (psi) and spacetime (phi). It appears in:

| Equation | Role of g | Source |
|---|---|---|
| omega_gap = g | Breathing mode gap frequency | Eq 6a, Part 33 |
| nabla^4 Phi + 4g^2 Phi = source | Biharmonic gravity coefficient | Eq 2e, Part 61 |
| m_phi^2 = 2g * Phi (near matter) | phi_- reversed-Higgs mass | Eq 6c, Part 62 |
| n = (g/c)^3 | Condensate number density | Eq 4d, Part 34 |
| mu = m_cond * c^2 = hbar * g | Chemical potential | Eq 4c, Part 34 |

**Plain English:** g sets the natural frequency of the spacetime condensate. Everything in PDTP that depends on "how fast" the condensate oscillates ultimately depends on g.

---

## Planck Units from g Alone

Given only g (and c, ℏ — without using G or m_P directly):

```
(94.7)  l_P = c / g  = 1.616e-35 m    [Planck length]   [DERIVED]
(94.8)  t_P = 1 / g  = 5.391e-44 s    [Planck time]     [DERIVED]
(94.9)  m_P = hbar*g / c^2 = 2.176e-8 kg [Planck mass]  [DERIVED]
(94.10) E_P = hbar*g = 1.956e9 J       [Planck energy]   [DERIVED]
```

All four Planck units follow from g × (simple combinations of c and ℏ). This is consistent with the standard definitions — not a new result, but confirmation that g IS the fundamental Planck scale.

---

## phi_- Mass Near Matter

From Eq 6c: the reversed-Higgs field phi_- acquires a position-dependent frequency near matter:
```
(94.11)  omega_phi^2 = 2 * g * Phi(r)
```
where Phi(r) = G * M / r is the Newtonian gravitational potential (units m^2/s^2).

At Earth's surface (Phi_E = G * M_E / R_E = 6.26e7 m^2/s^2):
```
omega_phi = sqrt(2 * 1.855e43 * 6.26e7) = 4.82e25 rad/s
E_phi = hbar * omega_phi ~ 31.7 GeV
```

**Plain English:** Near Earth, the phi_- field acts like a particle of about 31.7 GeV. Near the Sun or near a neutron star, it would be heavier. In empty vacuum (Phi = 0), it is exactly massless — the "reversed Higgs" behavior from Part 62.

**Note on units:** The "m_phi^2 = 2g*Phi" formula from Eq 6c mixes SI units in a PDTP-specific way. The quantity omega_phi^2 = 2g*Phi has units (rad/s)(m^2/s^2) = m^2/s^3, which is not a mass^2. The correct interpretation is omega_phi = sqrt(2g*Phi) as a frequency (rad/s), with mass equivalent m_phi = hbar * omega_phi / c^2.

---

## The Free Parameter Problem

**Key conclusion:** G, g, and m_cond are three names for the same free parameter.

```
G <-----> m_cond <-----> g
  G = hbar*c/m_cond^2     g = m_cond*c^2/hbar
  G * g^2 = c^5/hbar  (direct relation, Eq 94.4)
```

Given any one of {G, g, m_cond}, the other two follow immediately. There is one free parameter, not three.

**This is the same conclusion as A1 (m_cond = m_P underdetermined).** A6 does not introduce a new free parameter; it identifies that the existing one (A1) already determines g.

**What is NOT determined:** WHY g equals the Planck frequency. The value is consistent with all known physics but is not derived from topology, group theory, or any other structural principle (so far). This is exactly analogous to asking why G has the value it does in GR.

---

## Algebraic Verification

SymPy check (done analytically, not symbolically):

Substituting m_cond = hbar*g/c^2 into G = hbar*c/m_cond^2:

```
G = hbar * c / (hbar * g / c^2)^2
  = hbar * c * c^4 / hbar^2 / g^2
  = c^5 / hbar / g^2
```

Numerical residual: |G*g^2 - c^5/hbar| / (c^5/hbar) = 1.4e-16 [machine precision, VERIFIED]

---

## Sudoku Scorecard — 12/12 PASS

| Test | Result | Ratio | Tag |
|---|---|---|---|
| S1: G = c^5/(hbar*g^2) recovers G_Newton | PASS | 1.000000 | [DERIVED] |
| S2: m_cond = hbar*g/c^2 = m_Planck | PASS | 1.000000 | [DERIVED] |
| S3: l_P = c/g | PASS | 1.000000 | [DERIVED] |
| S4: t_P = 1/g | PASS | 1.000000 | [DERIVED] |
| S5: E_P = hbar*g | PASS | 1.000000 | [DERIVED] |
| S6: omega_gap = g [Eq 6a] | PASS | 1.000000 | [DERIVED] |
| S7: 4g^2 biharmonic coeff [Eq 2e] | PASS | 1.000000 | [DERIVED] |
| S8: n = (g/c)^3 = 1/l_P^3 [Eq 4d] | PASS | 1.000000 | [DERIVED] |
| S9: BEC mu = g_GP*n = m_cond*c^2 [Eq 4c] | PASS | 1.000000 | [DERIVED] |
| S10: omega_phi(Earth) << g [Eq 6c] | PASS | 2.6e-18 | [DERIVED] |
| S11: G*g^2 = c^5/hbar [PDTP Original] | PASS | 1.000000 | [DERIVED] |
| S12: E_P = m_P*c^2 = hbar*g | PASS | 1.000000 | [DERIVED] |

**Note on S10:** The phi_- frequency near Earth (4.82e25 rad/s) is 2.6e-18 times g. This confirms phi_- is a sub-Planck mode near ordinary matter — physically sensible.

**Note on Jeans test:** Eq 2f (lambda = 2*sqrt(2)*g) uses g in natural units [mass^2], while Eq 4e uses SI units [rad/s]. These are different normalizations and cannot be directly compared in SI. The Jeans eigenvalue formula is dimensionally consistent within the two-phase natural-unit framework but excluded from cross-unit tests.

---

## Observational Path

The only way to independently determine g (rather than inferring it from G) is to measure omega_gap directly:

```
omega_gap = g = sqrt(c^5 / (hbar * G)) ~ 1.86e43 rad/s
```

This is the Planck frequency — 43 orders of magnitude above LISA sensitivity (Part 29, Phase 7). No current detector can reach it. However:

1. If a future measurement of omega_gap gives a value different from sqrt(c^5/(hbar*G)), it would indicate that g is NOT equal to G's condensate (i.e., the gravitational and QCD condensates are decoupled — consistent with the two-condensate hypothesis from Part 36).

2. Near matter, phi_- acquires a mass from Eq 94.11. If phi_- couples to SM particles, it could be searched for as a new scalar boson — but its mass depends on the local gravitational potential and would not be a fixed resonance.

---

## Comparison: A-Series Free Parameters

| Parameter | Status | Structural anchor | Part |
|---|---|---|---|
| A1: m_cond | FREE | None (= m_P by construction) | 33-35 |
| A2: alpha_EM | FREE | No PDTP topology | — |
| A3: Lambda_QCD | FREE | QCD condensate scale | 36-38 |
| A4: theta_0 (Koide) | FREE | No SU(3) derivation | 53, 91 |
| A5: sin^2(theta_W) | PARTIAL | SU(5) fixes at M_GUT | 92 |
| **A6: g** | **PARTIAL** | **G*g^2=c^5/hbar; g=omega_P** | **94** |
| A7: c (emergent?) | OPEN | c_s=c (Part 34) | — |

A6 is PARTIAL in the same sense as A5: there is a structural relation (G*g^2=c^5/hbar), but it does not reduce the number of free parameters — it just shows g is equivalent to G.

---

## Conclusion

**New result [PDTP Original]:**
```
G * g^2 = c^5 / hbar    =>    g = sqrt(c^5/(hbar*G)) = omega_Planck
```

g equals the Planck angular frequency ~ 1.86e43 rad/s. All Planck units follow from g alone. The constraint G*g^2=c^5/hbar is exact (machine-precision verified).

**Negative result:** g is not independently determined. A6 reduces to A1 — the open problem is the same: why does m_cond = m_P? Until that is answered, g = omega_P remains a consequence of measuring G, not a prediction.

**Status change:** A6 OPEN (HIGH) → PARTIAL + FREE
G, g, m_cond are three encodings of the same single free parameter of the PDTP condensate.

---

**Sources:**
- Part 33, `vortex_winding_derivation.md` — Eq 2a: G = hbar*c/m_cond^2
- Part 34, `condensate_selfconsist.py` — Eq 4e: g = m_cond*c^2/hbar
- Part 61, `two_phase_lagrangian.py` — Eq 2e: 4g^2 biharmonic
- Part 62, `reversed_higgs.py` — Eq 6c: m_phi^2 = 2g*Phi
- PDG 2023 — G, hbar, c, m_P numerical values

**Changelog:** 2026-04-04 — Part 94 created (A6 FCC)
