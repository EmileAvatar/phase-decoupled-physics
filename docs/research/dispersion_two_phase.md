# Dispersion Model Re-examination with Two-Phase phi_- — Part 80

**Status:** NEGATIVE CONFIRMED — all 4 fatal problems persist (2 improved, 2 unchanged)
**PDTP Original:** Environment-dependent gap E_gap = hbar*sqrt(2*g*Phi)
**Date:** 2026-03-24
**Prerequisites:**
[fine_structure_derivation.md](fine_structure_derivation.md) (Parts 55-57 — dispersion model),
[two_phase_rederivation.md](two_phase_rederivation.md) (Part 63 — 16/16 pass),
[su3_dim_transmutation.md](su3_dim_transmutation.md) (Part 77 — SU(3) AF),
[alpha_em_fcc.md](alpha_em_fcc.md) (Part 79 — alpha_EM FCC)

**Simulation:** [dispersion_two_phase.py](../../simulations/solver/dispersion_two_phase.py) — Phase 50 (10 Sudoku checks)

---

## 1. Executive Summary

### 1.1 The Question

Part 57 proposed that coupling constant running could be explained as condensate
dispersion: alpha_eff(E) = alpha_0 * v_g(E)/c. It failed with 4 fatal problems.
D3 in the FCC queue asks: does the two-phase phi_- (Parts 61-62) fix any of them?

### 1.2 Results

| Check | Fatal Problem | Part 57 | Part 80 (two-phase) | Status |
|-------|--------------|---------|---------------------|--------|
| F1 | Hard cutoff at E_P | alpha=0 below E_P | Gap varies with Phi; smooth in SPACE | IMPROVED, STILL NEG |
| F2 | Massless modes no dispersion | No running for EM/strong | phi_- is spin-0, no coupling to spin-1 | UNCHANGED, NEGATIVE |
| F3 | Strong AF direction | Dispersion opposite to AF | phi_- not in color loops; AF is quantum | UNCHANGED, NEGATIVE |
| F4 | GUT scale 3 orders off | E_gap=E_P vs E_GUT=10^16 | E_gap=hbar*sqrt(2gPhi); BH gap ~ MeV | REFRAMED, STILL NEG |

### 1.3 The Conclusion

**Coupling constant running is a quantum effect (vacuum polarization, loop diagrams).
Condensate dispersion is a classical wave property. Two-phase enriches the classical
level but cannot bridge to quantum.** This is the same root cause as Part 57, now
confirmed from a second angle.

---

## 2. Background

### 2.1 Part 57's Dispersion Model

**Source:** `simulations/solver/dispersion_coupling.py` (Phase 19)

The dispersion hypothesis: in a BEC with Bogoliubov dispersion
omega^2 = c^2*k^2 + omega_gap^2, the effective coupling of a mode is:

```
alpha_eff(E) = alpha_0 * v_g(E) / c
             = alpha_0 * sqrt(1 - (E_gap/E)^2)    for E > E_gap    [SPECULATIVE]
             = 0                                     for E < E_gap
```

For the breathing mode (gravity channel), E_gap = E_Planck = 1.22×10^19 GeV.

**4 fatal problems identified:**
1. Hard cutoff at E_P (gravity works at all energies, not just above E_P)
2. Massless modes (photon, gluon) have no dispersion → no running
3. Strong force runs the WRONG direction (AF: stronger at low E)
4. GUT scale: E_P = 10^19 GeV vs observed 10^16 GeV (3 orders off)

### 2.2 Two-Phase New Ingredient

**Source:** Parts 61-62; `two_phase_lagrangian.py`, `reversed_higgs.py`

The two-phase Lagrangian (Part 61) produces phi_- with environment-dependent mass:

```
m^2(phi_-) = 2*g*Phi                                              [DERIVED, Part 62]
```

where g = omega_P = M_P*c^2/hbar and Phi = GM/(Rc^2) is the local gravitational potential.

Key property: **massless in vacuum (Phi → 0), massive near matter (Phi > 0).**

---

## 3. Check 1: Hard Cutoff vs Gradual Coupling (F1)

### 3.1 Environment-Dependent Gap

The two-phase gap varies continuously with environment:

```
omega_gap = sqrt(2*g*Phi)                                          (80.1) [DERIVED]
E_gap = hbar * omega_gap = hbar * sqrt(2*g*Phi)
```

| Environment | Phi | E_gap [eV] | Range [m] |
|------------|-----|-----------|----------|
| Deep space | ~0 | 0 | infinity |
| Earth surface | 6.96×10^-10 | 106 | 1.87×10^-9 |
| Sun surface | 2.12×10^-6 | 5,840 | 3.38×10^-11 |
| Neutron star | 0.414 | 2.58×10^6 | 7.65×10^-14 |
| BH horizon | 0.5 | 2.83×10^6 | 6.96×10^-14 |

### 3.2 Does This Fix the Cutoff?

The gap now varies continuously across space — this IS an improvement over Part 57's
fixed E_Planck cutoff. But the dispersion formula still gives a step function at
E = E_gap for any given environment.

The actual gravitational coupling alpha_G = (m/m_P)^2 comes from the winding number
n = m_P/m (Part 33). This is topological, not dispersive.

**RESULT:** PARTIALLY IMPROVED but STILL NEGATIVE. [Eq. 80.1]

---

## 4. Check 2: Massless Mode Dispersion (F2)

### 4.1 phi_- vs Photon/Gluon

phi_- is a gravitational-sector scalar (spin-0). For it to modify photon dispersion,
it would need to:
(a) Couple to F_mu_nu (EM field strength)
(b) Break gauge invariance

Neither happens in the two-phase Lagrangian:
```
L = +g*cos(psi - phi_b) - g*cos(psi - phi_s)
```

There is no A_mu field. The EM sector is independent of the gravitational condensate.
Part 79 Path 2 established: metric (spin-2) and gauge (spin-1) are independent DOF.

### 4.2 Literature Comparison

Some modified gravity theories do couple scalars to photons:
- **Dilaton:** L ~ phi*F_mu_nu*F^mu_nu (Damour & Polyakov 1994)
- **Chameleon:** L ~ beta*phi*T^mu_mu (Khoury & Weltman 2004)
- **Axion:** L ~ phi*F_mu_nu*F_dual^mu_nu (Peccei & Quinn 1977)

PDTP phi_- has **none** of these couplings.

**RESULT:** STILL NEGATIVE. phi_- does not couple to spin-1 carriers.     (80.2) [DERIVED]

---

## 5. Check 3: Strong Force Direction (F3)

### 5.1 Asymptotic Freedom is Quantum

**Source:** Gross & Wilczek (1973), PRL 30, 1343; Politzer (1973), PRL 30, 1346

```
b0_QCD = 11 - 2*N_f/3 = 7.0    (AF: b0 > 0)                     [ESTABLISHED]
```

This comes from SU(3) gluon self-interaction in 1-loop diagrams. phi_- does not
carry color charge, does not appear in SU(3) loops, and does not modify b0.

The direction mismatch is structural:
- Classical dispersion: slower modes couple WEAKER (always)
- Quantum AF: virtual gluon loops ANTI-screen at high E

**RESULT:** STILL NEGATIVE. AF is quantum; dispersion is classical.        (80.3) [DERIVED]

---

## 6. Check 4: GUT Scale (F4)

### 6.1 Environment-Dependent Gap vs GUT Scale

```
E_gap(Phi) = hbar * sqrt(2*g*Phi)                                 (80.4) [DERIVED]
```

At BH horizon (Phi = 0.5, maximum physical potential):
```
E_gap(BH) = hbar * sqrt(g) = 2.83×10^-3 GeV = 2.83 MeV
E_GUT = 2×10^16 GeV
E_gap(BH) / E_GUT = 1.4×10^-19
```

**Direction reversal:** Part 57 gap was 1000× ABOVE E_GUT; Part 80 gap is ~10^19× BELOW.
The GUT scale falls between the two extremes.

To match E_GUT, need Phi = 2.49×10^37 — far exceeds BH horizon (0.5). Unphysical.

**RESULT:** REFRAMED but STILL NEGATIVE. Neither fixed gap (Part 57) nor
environment-dependent gap (Part 80) matches E_GUT. [Eq. 80.4]

---

## 7. Root Cause Analysis

**DISPERSION** is a classical wave property:
- Single mode propagating through a medium
- Group velocity depends on frequency
- Coupling ~ v_g/c (reach/propagation speed)

**COUPLING RUNNING** is a quantum loop effect:
- Virtual particle-antiparticle pairs screen/anti-screen
- Depends on gauge group (SU(3) vs U(1) vs SU(2))
- Direction: screening (EM) vs anti-screening (QCD)

**Source:** Peskin & Schroeder (1995), *Introduction to QFT*, Ch. 16-18

These are different levels of physics. Two-phase enriches the classical level
(environment-dependent gap, spatial variation) but does not bridge to quantum.

---

## 8. Positive Findings

Despite the negative overall result, Part 80 produces useful insights:

1. **phi_- dispersion IS physical:** omega^2 = c^2*k^2 + 2*g*Phi (massive Klein-Gordon).
   The breathing mode really does have environment-dependent group velocity.

2. **Environment-dependent gap** is a genuine PDTP prediction. Phi_- is massless in
   vacuum, massive near matter. This is the "reversed Higgs" (Part 62).

3. **Boundary clarified:** PDTP condensate physics describes WHERE particles propagate
   (geometry, topology); QFT describes HOW STRONGLY they interact (loop corrections).

4. **Weak force IS genuine dispersion:** W/Z mass gap from EW symmetry breaking acts
   exactly like a dispersion cutoff. This qualitative win from Part 57 is confirmed.

---

## 9. Sudoku Scorecard

| # | Test | Pass? |
|---|------|-------|
| S1 | phi_- mass: 0 in vacuum, >0 near Earth | PASS |
| S2 | phi_- dispersion: omega^2=c^2*k^2+2*g*Phi | PASS |
| S3 | v_g(phi_-) < c near matter (massive KG) | PASS |
| S4 | Photon mass = 0 (gauge invariance exact) | PASS |
| S5 | Gluon mass = 0 (SU(3) gauge invariance) | PASS |
| S6 | b0_QCD = 7 > 0 (AF direction correct) | PASS |
| S7 | b0_QED = -8.89 < 0 (IR free direction) | PASS |
| S8 | E_gap(BH) < E_Planck (2.83 MeV << 1.22×10^19 GeV) | PASS |
| S9 | E_gap(BH)/E_GUT = 1.4×10^-19 (mismatch confirmed) | PASS |
| S10 | alpha_G(e) = 1.75×10^-45 (nonzero, topological) | PASS |

**Score: 10/10 pass**

---

## 10. References

- Gross, D.J. & Wilczek, F. (1973). "Ultraviolet behavior of non-Abelian gauge theories."
  *PRL* 30, 1343.
- Politzer, H.D. (1973). "Reliable perturbative results for strong interactions?"
  *PRL* 30, 1346.
- Peskin, M.E. & Schroeder, D.V. (1995). *Introduction to Quantum Field Theory.*
  Ch. 16-18.
- Khoury, J. & Weltman, A. (2004). "Chameleon fields."
  *PRL* 93, 171104.
- Damour, T. & Polyakov, A.M. (1994). "The string dilaton and a least coupling principle."
  *Nucl.Phys.B* 423, 532.
- Burrage, C. & Sakstein, J. (2018). "Tests of chameleon gravity."
  *Living Rev.Rel.* 21, 1.
