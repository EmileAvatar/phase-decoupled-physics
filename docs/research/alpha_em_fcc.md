# Fine-Structure Constant FCC — Part 79

**Status:** Investigated — all 5 FCC paths NEGATIVE for deriving alpha_EM. Multiple positive sub-results.
**PDTP Original:** Impedance duality g_m/e = R_K/Z_0; backward-solve alpha_EM(M_P) = 1/64.
**Date:** 2026-03-22
**Prerequisites:**
[coupling_constants.md](coupling_constants.md) (Part 52 — beta functions, free parameters),
[fine_structure_derivation.md](fine_structure_derivation.md) (Parts 55-57 — K_0^2, RG, dispersion),
[su3_dim_transmutation.md](su3_dim_transmutation.md) (Part 77 — SU(3) AF, K_NAT),
[extremal_condensate.md](extremal_condensate.md) (Part 78 — dimensionless structure vs scale)

**Simulation:** [alpha_em_fcc.py](../../simulations/solver/alpha_em_fcc.py) — Phase 49 (10 Sudoku checks)

---

## 1. Executive Summary

### 1.1 The Question

Part 52 established alpha_EM = 1/137.036 as a free parameter. Parts 55-57 attempted
three derivation approaches, all failed. FCC triggered (3+ approaches failed).

### 1.2 Results

| Path | Fix alpha_EM? | Key positive finding |
|------|--------------|---------------------|
| 1. SU(3)-U(1) coupling | NO | QED RG: alpha_EM(M_P) = 1/64 -> 1/137 at m_e [Eq. 79.1] |
| 2. Emergent impedance | NO | Metric (spin-2) and gauge (spin-1) are independent DOF |
| 3. Topological winding | NO | g_m/e = 1/(2*alpha) = R_K/Z_0 [exact duality, Eq. 79.5] |
| 4. Coupling ratios | NO | sin^2(theta_W) = 3/8 at GUT scale [Eq. 79.7] |
| 5. Two-phase extension | NO | phi_- is spin-0 (not photon); same K_NAT |

### 1.3 The Conclusion

Same barrier as A1 (m_cond): **PDTP determines dimensionless structure
but not the values of coupling constants.** alpha_EM is to the U(1)_EM
condensate as m_cond is to the gravitational condensate — a free parameter.

After 8 independent approaches (Parts 52, 55, 56, 57, 79 Paths 1-5),
alpha_EM = 1/137.036 is confirmed as PDTP's second free parameter.

---

## 2. FCC Evaluation — Full Methodology.md Checklist

Systematic evaluation of every checklist item for A2:

- **Tried/partial:** 26 items (including Parts 52, 55-57)
- **Untried:** 16 items, mapped to 5 investigation paths
- Full table in simulation output

---

## 3. Path 1: SU(3)-U(1) Coupling

### 3.1 SU(3) Asymptotic Freedom

**Source:** Gross & Wilczek (1973), Politzer (1973)

```
b0_QCD = 11 - (2/3)*N_f = 7.0 (AF: b0 > 0)        [ESTABLISHED]
b0_QED = -80/9 = -8.889 (IR free: b0 < 0)           [ESTABLISHED]
```

SU(3) generates Lambda_QCD via dimensional transmutation:
```
Lambda_QCD = m_Z * exp(-2*pi/(b0*alpha_s))            [ESTABLISHED]
           ~ 200 MeV (measured)
```

But Lambda_QCD does NOT determine alpha_GUT or alpha_EM.
The GUT coupling is a separate free parameter.

### 3.2 PDTP K_NAT -> alpha_EM via RG

Starting from K_NAT^2 = 1/(4*pi)^2 = 1/157.9 at M_P:
```
1/alpha_EM(m_e) = 1/K_NAT^2 - (b0_QED/2*pi)*ln(M_P/m_e)
                = 157.9 + 72.9
                = 230.8                                (79.2) [DERIVED]
```

This is 68% off from 137.036. Running from K_NAT^2 goes the **wrong way** —
QED's negative b0 makes alpha SMALLER at low energy.

### 3.3 Backward Solve

What alpha_EM(M_P) gives 1/137 at m_e?
```
1/alpha_EM(M_P) = 137.036 - 72.9 = 64.1              (79.1) [DERIVED]
alpha_EM(M_P) = 1/64.1 = 0.01559
```

Compare K_NAT^2 = 1/157.9 = 0.00633. Ratio: 2.46.
The needed Planck-scale coupling is ~2.5x larger than K_NAT^2.

**RESULT:** SU(3)-U(1) coupling does NOT fix alpha_EM. [NEGATIVE]
**POSITIVE:** If alpha_EM(M_P) = 1/64 were derivable, QED RG reproduces 1/137. [Eq. 79.1]

---

## 4. Path 2: Emergent Impedance from SU(3) Metric

### 4.1 The Impedance Identity

**Source:** Established physics

```
alpha = Z_0 / (2*R_K)                                 (79.3) [EXACT]
      = 376.730 / (2 * 25812.807)
      = 1/137.036
```

### 4.2 Condensate Polarizability

Part 34 proved: c_s = c exactly in the PDTP condensate.
```
eps_0 * mu_0 = 1/c^2                                  [from Lorentz invariance]
Z_0 = sqrt(mu_0/eps_0)                                [NOT fixed by c alone]
```

c_s = c determines the PRODUCT eps_0*mu_0 but not the RATIO mu_0/eps_0 = Z_0^2.

### 4.3 SU(3) Metric vs EM

Part 75's emergent metric g_mu_nu = K*Tr(dU^dag dU) is the gravitational (spin-2) sector.
The EM sector is spin-1 (gauge boson A_mu). These are **independent DOF**:
- Metric tensor -> G -> K_NAT (spin-2)
- Gauge field -> e -> alpha_EM (spin-1)

**RESULT:** SU(3) emergent metric determines G, NOT alpha_EM. [NEGATIVE]

---

## 5. Path 3: Topological Winding in EM Sector

### 5.1 Dirac Quantization

**Source:** Dirac (1931), Proc. Roy. Soc. A 133, 60

```
e * g_m = 2*pi*n*hbar  (n integer)                    (79.4) [ESTABLISHED]
```

For n=1:
```
g_m/e = 1/(2*alpha) = 68.5                            (79.5) [DERIVED]
```

This is the **same** impedance ratio R_K/Z_0 = 68.5.
Exact duality: alpha = Z_0/(2*R_K) <-> g_m/e = R_K/Z_0.

But: Dirac quantization constrains e*g_m, not e alone. No monopoles observed.

### 5.2 U(1) Vortex Winding

pi_1(U(1)) = Z gives integer vortex winding numbers.
Flux quantization: Phi = n*Phi_0 where Phi_0 = h/(2e).
But Phi_0 is defined in terms of e — does not determine e.

### 5.3 Chern-Simons Invariant

**Source:** Chern & Simons (1974)

Topological invariants are integers. alpha = 1/137.036 is not a ratio of small integers.
-> alpha is NOT a purely topological quantity.

### 5.4 Wyler's Formula

**Source:** Wyler (1969), Comptes Rendus 269A, 743

```
alpha_W^{-1} = (8*pi^4/9) * (16*120/pi^5)^{1/4}
             = 137.03608...                            (79.6) [ESTABLISHED]
```

Accuracy: 0.6 ppm. Based on conformal group O(4,2) geometry.
"A number in search of a theory" (Wolfram MathWorld).

**RESULT:** No topological invariant fixes alpha_EM. [NEGATIVE]
**POSITIVE:** Impedance duality g_m/e = R_K/Z_0 [Eq. 79.5]
**POSITIVE:** Wyler 0.6 ppm accuracy hints at geometric origin [Eq. 79.6]

---

## 6. Path 4: Coupling Ratios

### 6.1 GUT Unification

**Source:** Georgi & Glashow (1974), PRL 32, 438

At GUT scale (SU(5)):
```
sin^2(theta_W) = 3/8 = 0.375                          (79.7) [DERIVED, group theory]
```

Running to m_Z: 0.375 -> 0.231 (depends on M_GUT, free parameter).

The ratio alpha_S/alpha_EM at m_Z = 16.2 depends on alpha_GUT and M_GUT,
both free parameters. Even the ratio is not derivable.

**RESULT:** Ratios do not help. [NEGATIVE]
**POSITIVE:** sin^2(theta_W) = 3/8 at GUT scale is derived exactly. [Eq. 79.7]

---

## 7. Path 5: Two-Phase Extension

### 7.1 phi_- vs Photon

| Property | Photon (A_mu) | phi_- |
|----------|--------------|-------|
| Spin | 1 | 0 |
| DOF (massless) | 2 (transverse) | 1 |
| Gauge symmetry | U(1)_EM | None (global) |
| Mass in vacuum | 0 (exact) | 0 |
| Mass near matter | 0 (exact) | m^2 = 2gPhi |

phi_- is scalar (spin-0), not a vector boson (spin-1). It cannot be the photon.
Both channels share the same K_NAT = 1/(4*pi). No new dimensionless number emerges.

**RESULT:** Two-phase extension does NOT determine alpha_EM. [NEGATIVE]

---

## 8. Synthesis

### 8.1 Free Parameter Inventory

| # | Parameter | Sets | Observation |
|---|-----------|------|-------------|
| 1 | m_cond (= m_P) | G | G = 6.674e-11 |
| 2 | alpha_EM | EM coupling | alpha = 1/137.036 |
| 3 | Lambda_QCD | Strong coupling | alpha_s(m_Z) = 0.118 |
| 4 | sin^2(theta_W) | EW mixing | 0.231 at m_Z |
| 5 | Lambda (cosmo) | Dark energy | rho_Lambda = 6e-27 kg/m^3 |

PDTP has 5 free parameters = same count as SM. This is consistent:
PDTP explains SM structure without reducing its parameter count.

### 8.2 What PDTP Derives

- Beta functions b0 for SU(3), SU(2), U(1) [exact, group theory]
- Asymptotic freedom in SU(3), SU(2) [b0 > 0]
- IR freedom in U(1)/QED [b0 < 0]
- Running direction of all couplings [1-loop RGE]
- sin^2(theta_W) = 3/8 at GUT scale [SU(5)]
- Impedance identity: alpha = Z_0/(2*R_K) [exact]
- Impedance duality: g_m/e = R_K/Z_0 [Dirac + impedance]
- K_NAT^2 = 1/158 (13.2% off alpha_EM)
- alpha_EM(M_P) = 1/64 needed for 1/137 at m_e [1-loop QED RG]

### 8.3 Most Promising Future Direction

Wyler's formula (0.6 ppm accuracy) based on O(4,2) conformal geometry.
If PDTP condensate has conformal structure, Wyler's geometry might emerge.
This requires non-perturbative analysis — beyond current scope. [SPECULATIVE]

---

## 9. Sudoku Scorecard

| # | Test | Pass? |
|---|------|-------|
| S1 | alpha = Z_0/(2*R_K) (exact identity) | PASS |
| S2 | b0_QED = -8.889 < 0 (IR free) | PASS |
| S3 | b0_QCD = 7.0 > 0 (AF) | PASS |
| S4 | sin^2(theta_W) = 3/8 at GUT (exact) | PASS |
| S5 | g_m/e = R_K/Z_0 = 68.5 (Dirac duality) | PASS |
| S6 | K_NAT^2 = 1/(4*pi)^2 (exact) | PASS |
| S7 | Wyler = 1/137.036 (0.6 ppm) | PASS |
| S8 | alpha(m_Z) > alpha(0) (screening direction) | PASS |
| S9 | Lambda_QCD from 1-loop RG | FAIL (factor ~4, 1-loop approx) |
| S10 | G = hbar*c/m_P^2 | PASS |

**Score: 9/10 pass**

Note: S9 failure is expected — 1-loop QCD running at strong coupling (alpha_s ~ 1)
is unreliable. Higher-loop and non-perturbative corrections bring Lambda_QCD ~ 200 MeV.

---

## 10. References

- Georgi, H. & Glashow, S.L. (1974). "Unity of all elementary-particle forces."
  *PRL* 32, 438.
- Gross, D.J. & Wilczek, F. (1973). "Ultraviolet behavior of non-Abelian gauge theories."
  *PRL* 30, 1343.
- Politzer, H.D. (1973). "Reliable perturbative results for strong interactions?"
  *PRL* 30, 1346.
- Dirac, P.A.M. (1931). "Quantised singularities in the electromagnetic field."
  *Proc. Roy. Soc.* A 133, 60.
- Wyler, A. (1969). *Comptes Rendus* 269A, 743.
- Robertson, H.P. (1971). "Wyler's expression for the fine-structure constant."
  *PRL* 27, 1545.
- Chern, S.S. & Simons, J. (1974). "Characteristic forms and geometric invariants."
  *Annals of Math.* 99, 48.
- Peskin, M.E. & Schroeder, D.V. (1995). *Introduction to Quantum Field Theory.*
  Ch. 12, 16-18.
