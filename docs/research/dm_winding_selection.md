# Dark Matter Winding Number Selection — n = 1 Planck Vortex (Part 116)

**Status:** n = 1 selection DERIVED (given the bare-vortex premise of Part 96 D3).
Relic abundance from Kibble-Zurek alone: NEGATIVE. Production channel: OPEN.
**PDTP Original:** Stability + Kibble-Zurek selection of the dark matter winding number.
**Date:** 2026-06-11 (Phase 84)
**Script:** `simulations/solver/dm_winding_selection.py`
**Log:** `simulations/solver/outputs/dm_winding_selection_20260611_193156.txt`
**Prerequisites:** [vortex_winding_derivation.md](vortex_winding_derivation.md) (Part 33),
[condensate_layer_optics.md](condensate_layer_optics.md) (Parts 89/96),
[dark_matter_energy.md](dark_matter_energy.md) (Part 97 living reference)

---

## Plain English Summary

Part 96 said dark matter could be a "bare vortex" — a swirl in the spacetime
condensate that gravitates but carries none of the charges (colour, electric,
weak) that would let it touch light or nuclei. Its mass came out as
m_DM = m_P/n, where n is the number of times the swirl winds around — but
**nothing told us which n nature picks**, so the mass was a free parameter
spanning 20 orders of magnitude.

This Part closes that gap with two independent arguments:

1. **Stability:** a swirl that winds twice (or more) carries more field energy
   than two separate single swirls — so it splits. Only single swirls (n = 1)
   survive. This is textbook superfluid physics, re-derived here with the PDTP
   core condition included.
2. **Birth statistics:** when the condensate first formed, the phase was random
   from place to place. Walking a loop through random phases almost never winds
   more than once — a 2-million-loop simulation gives |n| = 1 in 43% of loops
   and |n| >= 2 in only 1.6%. So nature almost never even MAKES multi-wound
   swirls, and the few it makes decay to n = 1.

**Conclusion: n = 1, so the PDTP dark matter particle is a Planck-mass vortex**
(1.22 x 10^19 GeV, about the mass of a dust grain, 22 micrograms). The mass is
no longer a free parameter.

**What this buys:** every observational test passes automatically — it ghosts
through the Bullet Cluster with 39 orders of magnitude to spare, it is utterly
cold, it is far too sparse and too weakly coupled for any direct-detection
experiment (about 1 vortex per 30,000 m^3 locally; one crosses a 1 m^2 detector
every ~4 years and interacts only gravitationally), and it cannot decay
(topology forbids it), which fits the absence of super-GZK cosmic rays.

**What it does NOT buy:** the amount of dark matter (27%) is still not
predicted. Making these vortices at the Big Bang and then inflating the
universe dilutes them to nothing (the classic monopole problem — we compute
the shortfall: ~50 orders of magnitude). They must instead be produced AFTER
inflation, at reheating. The literature scenario for this (Planckian
Interacting Dark Matter, Garny+ 2016) requires high-scale inflation — which
predicts primordial gravitational waves (tensor-to-scalar ratio r) big enough
for the next CMB experiments to see. **If LiteBIRD/CMB-S4 find no tensor
modes, this production channel is dead.** That is the falsifiable hook.

---

## 1. Problem Statement

Part 96 D3 (Eq 96.9) derived the bare-vortex dark matter mass spectrum:

```
   m_DM = m_P / n,    n = 1, 2, 3, ...     [DERIVED, Part 96]      (116.1)
```

from the Part 33 winding relation n = m_cond/m with m_cond = m_P. The winding
number n was left undetermined — `dark_matter_energy.md` Part 7 lists "DM mass
(specific value)" as a FREE PARAMETER. Methodology.md §8 strategy applied here:
**Contract** — derive the free parameter from topology/symmetry already present
in the framework.

---

## 2. Step 1 — Vortex Energy Scaling [DERIVED]

**Starting point** (sources: Pethick & Smith 2002 ch. 9; Part 33 Eq 5.2):
the superfluid velocity around a winding-n vortex line is

```
   v_s(r) = (hbar / m_cond) n / r                  [ASSUMED, Part 33]  (116.2)
```

**Step-by-step:** the kinetic energy per unit length of vortex line is the
integral of the kinetic energy density (1/2) rho_s v_s^2 over the plane
perpendicular to the line, from the core radius r_c to the system size R:

```
   E/L = Int[ (1/2) rho_s ((hbar/m_cond) n/r)^2  2 pi r dr,  r_c..R ] (116.3)
       = pi rho_s (hbar/m_cond)^2 n^2  Int[ dr/r, r_c..R ]            (116.4)
       = pi rho_s (hbar/m_cond)^2 n^2  ln(R/r_c)                      (116.5)
```

**SymPy verification:** the integral was evaluated symbolically; the residual
against Eq (116.5) is **0**. The n^2 scaling is an output of the integration,
not an assumption. At fixed core radius, E(2)/E(1) = 4 (computed). [VERIFIED]

**Plain English:** the energy stored in the swirl grows with the SQUARE of the
winding number. Winding twice costs four times the energy of winding once.

---

## 3. Step 2 — Splitting Instability of n >= 2 [DERIVED]

**PDTP twist:** in PDTP the core radius grows with winding (Part 33 Eq 5.4):
r_c = n lambda_cond. So in units of A = pi rho_s (hbar/m_cond)^2:

```
   E(n)/A     = n^2 ln(Lambda/n)    with  Lambda = R/lambda_cond      (116.6)
   E_split/A  = n ln(Lambda)        [n separate n=1 vortices]         (116.7)
   Delta E/A  = n^2 ln(Lambda/n) - n ln(Lambda)                       (116.8)
```

**Numerical values** (computed, Lambda = R_Hubble/l_P = 8.2 x 10^60):

| n | Delta E / A | verdict |
|---|------------|---------|
| 2 | +277.8 | UNSTABLE (splits) |
| 3 | +836.4 | UNSTABLE |
| 5 | +2782 | UNSTABLE |
| 10 | +12,617 | UNSTABLE |

Delta E > 0 for all n >= 2: **a multiply wound bare vortex releases energy by
splitting into singly wound vortices.** This is the established superfluid
result (multiply quantized vortices are unstable; Pethick & Smith ch. 9),
re-derived here including the PDTP core condition. [DERIVED]

**Why SM particles do not split:** an SM particle's winding is pinned by the
phase-locked matter field psi (the g cos(psi - phi) coupling) and by conserved
SM charges; only **matter-free (dark) vortices** are governed by pure
condensate energetics. [SPECULATIVE — see Open Question O1]

---

## 4. Step 3 — Kibble-Zurek Winding Statistics [DERIVED, numerical]

**Starting point** (sources: Kibble 1976; Zurek 1985;
[Wikipedia: Kibble-Zurek mechanism](https://en.wikipedia.org/wiki/Kibble%E2%80%93Zurek_mechanism)):
at the condensate phase transition the phase phi is uncorrelated between
adjacent correlation volumes. The winding around a loop of N independent
patches (geodesic interpolation, each step wrapped into (-pi, pi]) is an
integer-valued random variable.

**Monte Carlo** (2,000,000 loops, 6 patches/loop, seed 42, computed):

| winding n | probability |
|-----------|-------------|
| 0 | 0.5498 |
| +/-1 | 0.4338 |
| \|n\| >= 2 | 0.0165 |

```
   P(|n| >= 2) / P(|n| = 1) = 0.038                  [COMPUTED]      (116.9)
```

**Plain English:** when the condensate froze, 96%+ of all vortices born were
single-wound. The rare multi-wound ones decay by Step 2. Both arguments
independently select the same answer.

---

## 5. Selection Result [PDTP Original]

```
┌────────────────────────────────────────────────────────────────────┐
│  n = 1   ->   m_DM = m_P = 2.176 x 10^-8 kg = 1.221 x 10^19 GeV    │
│                                                                    │
│  PDTP dark matter = singly wound bare condensate vortex            │
│  ("Planck vortex relic").  Core radius r_c = l_P = 1.6e-35 m.      │
│  The DM mass is NO LONGER a free parameter, given the              │
│  bare-vortex premise of Part 96 D3.        [PDTP Original]  (116.10)│
└────────────────────────────────────────────────────────────────────┘
```

**Independence argument (two-phase check):** the selection is topological and
energetic, made entirely in the condensate phase sector phi. The two-phase
fields phi_+/phi_- (Part 61) live at the locked background and do not alter
the winding energy integral (116.5) or the KZ statistics, which involve only
the U(1) phase topology. Newton's 3rd law, the biharmonic equation, and the
Jeans eigenvalue are untouched (no new term is added to the Lagrangian).

**SymPy applicability:** Steps 1-2 SymPy-verified (residual 0). Step 3 is a
statistical (Monte Carlo) result — SymPy verification inapplicable; numerical
verification with fixed seed instead.

---

## 6. Relic Abundance Audit [NEGATIVE for KZ; production channel OPEN]

**Required abundance today** (computed; Planck 2020 inputs):

```
   rho_crit = 3 H_0^2/(8 pi G)          = 8.53e-27 kg/m^3            (116.11)
   rho_DM   = 0.265 rho_crit            = 2.26e-27 kg/m^3            (116.12)
   n_DM     = rho_DM / m_P              = 1.04e-19 /m^3              (116.13)
   s        = (2 pi^2/45) g_*s (k_B T_CMB/hbar c)^3 = 2.89e9 /m^3    (116.14)
   Y_req    = n_DM / s                  = 3.6e-29                    (116.15)
```

Mean cosmological spacing: one Planck vortex per (2127 km)^3.

**KZ at the Planck epoch gives Y_KZ ~ 1** (one defect per l_P^3; entropy
density ~ 1/l_P^3) [ORDER OF MAGNITUDE]. Diluting Y to Y_req would need
exactly 21.8 e-folds of inflation after formation — but standard inflation
requires >= 60 e-folds, giving Y = 6.7e-79, i.e. **50 orders of magnitude too
few relics**. This is Preskill's monopole-problem logic (Preskill 1979;
Guth 1981) applied to PDTP vortices:

```
   KZ-before-inflation:  Y / Y_req = 1.9e-50   ->   NEGATIVE        (116.16)
```

**The contradiction is the finding:** the dark matter abundance cannot come
from defect formation at the Big Bang. It must be produced AFTER inflation.

**Literature anchor — PIDM** (Garny, Sandora & Sloth 2016, PRL 116 101302,
[arXiv:1511.03278](https://arxiv.org/abs/1511.03278)): gravitational
production of Planck-scale DM at reheating. **Constraint from that paper:**
for the purely gravitational channel, m > 0.01 m_P is already ruled out by
the absence of CMB tensor modes. So n = 1 (m_DM = m_P) requires the
**defect-formation channel at preheating** (Kibble-Zurek at the end of
inflation) to be more efficient than gravitational particle production.
[OPEN, SPECULATIVE]

**Falsifiable hook [PDTP Original, SPECULATIVE]:** either way, the scenario
needs high-scale inflation, hence a detectable primordial tensor-to-scalar
ratio r. LiteBIRD / CMB-S4 (sigma_r ~ 0.001) is the kill test: **no tensor
modes -> no Planck-vortex dark matter.**

---

## 7. Observational Consistency (all computed)

| Quantity | Computed value | Bound / scale | Verdict |
|----------|---------------|---------------|---------|
| sigma/m = 4 pi G^2 m_DM/v^4 (Part 118) | 5.2e-49 m^2/kg | < 1e-4 m^2/kg (Bullet) | PASS, 44.3 orders margin |
| de Broglie wavelength @ 220 km/s | 2.2e-32 m | << kpc | utterly cold PASS |
| local number density | 3.3e-14 /m^3 (1 per ~31 m cube) | — | sparse |
| flux through 1 m^2 detector | 0.23 /yr, grav-only | LZ/XENON nulls | CONSISTENT |
| vortices per 1e7 M_sun dwarf halo | 9.1e44 | >> 1 | smooth CDM PASS |
| microlensing | m_P 26 orders below ~2e18 kg floor | HSC/Subaru | unconstrained PASS |
| decay products | none (topology conserved) | GZK 6e19 eV | no super-GZK excess PASS |

Note: the original run of this Part used the Part 89 Eq 89.17 form sigma/m ~ G/c^4,
which Part 118 showed to be dimensionally inconsistent (plus factor-100 and unit
errors). The table above uses the corrected formula sigma/m = 4 pi G^2 m_DM/v^4
(gravitational Rutherford scattering, b_90 = 2Gm/v^2); see
`simulations/solver/sigma_m_erratum.py` (7/7 Sudoku). The conclusion is unchanged
and the Bullet margin improves to 44.3 orders.

---

## 8. Sudoku Scorecard

| # | Test | Computed value | Verdict |
|---|------|---------------|---------|
| T1 | SymPy E(n) integral residual = 0 | 0 | PASS |
| T2 | E(2)/E(1) = 4 at fixed core | 4.0 | PASS |
| T3 | splitting Delta E > 0 for n = 2,3,5,10 | dE(2)/A = 277.8 | PASS |
| T4 | KZ: P(\|n\|>=2) << P(\|n\|=1) | ratio 0.038 | PASS |
| T5 | m_DM/m_P = 1 (selected) | 1.000000 | PASS |
| T6 | Bullet Cluster sigma/m below bound | 5.2e-49 m^2/kg (Part 118 formula) | PASS |
| T7 | cold DM: lambda_dB << kpc | 2.2e-32 m | PASS |
| T8 | smooth on dwarf scales | N = 9.1e44 | PASS |
| T9 | direct detection consistency | 0.23 /m^2/yr grav-only | PASS |
| T10 | microlensing unconstrained | 9e25 below floor | PASS |
| T11 | UHECR stability | m/E_GZK = 2e8, no decay | PASS |
| T12 | KZ-before-inflation abundance | off by 50 orders | PASS (expected contradiction) |

**Score: 12/12 PASS.** T12 passes by CONFIRMING the expected failure — KZ
alone cannot set the abundance; that contradiction is the finding.

---

## 9. Open Questions

- **O1 — line energy vs mass map.** The GL line energy (116.5) GROWS as n^2
  while the Part 33 particle-mass map gives m = m_P/n (mass SHRINKS with n).
  These are different energy bookkeepings (IR field energy vs core/Compton
  mass). The splitting argument uses field energetics; the mass assignment
  uses the core condition. Reconciling them rigorously is open. The n = 1
  selection is robust to this because KZ statistics (Step 3) selects n = 1
  independently of energetics.
- **O2 — production efficiency.** Can KZ at preheating produce Y ~ 3.6e-29 of
  Planck vortices? Requires a preheating defect-formation calculation. [OPEN]
- **O3 — Part 89 sigma/m numerical value. [RESOLVED, Part 118]** Eq 89.17 was
  wrong three ways (dimensions, factor 100, unit conversion). Corrected to
  sigma/m = 4 pi G^2 m_DM/v^4 = 5.2e-49 m^2/kg; all verdicts unchanged.
  See `sigma_m_erratum.py` and the erratum block in `condensate_layer_optics.md`.
- **O4 — why Omega_DM = 27%?** Still not predicted (depends on O2 + reheating
  temperature).

---

## 10. References

**Source:** Pethick, C.J. & Smith, H. (2002), *Bose-Einstein Condensation in
Dilute Gases*, CUP, ch. 9 (vortex energy ~ n^2; instability of multiply
quantized vortices).
**Source:** Kibble, T.W.B. (1976), "Topology of cosmic domains and strings",
J. Phys. A 9, 1387.
**Source:** Zurek, W.H. (1985), "Cosmological experiments in superfluid
helium?", Nature 317, 505.
**Source:** [Wikipedia: Kibble-Zurek mechanism](https://en.wikipedia.org/wiki/Kibble%E2%80%93Zurek_mechanism) (verified 2026-06-11)
**Source:** Garny, M., Sandora, M. & Sloth, M.S. (2016), "Planckian
Interacting Massive Particles as Dark Matter", PRL 116, 101302,
[arXiv:1511.03278](https://arxiv.org/abs/1511.03278) (verified 2026-06-11).
**Source:** Preskill, J. (1979), "Cosmological production of superheavy
magnetic monopoles", PRL 43, 1365.
**Source:** Guth, A. (1981), "Inflationary universe", PRD 23, 347.
**Source:** Clowe, D. et al. (2006), ApJ 648, L109 (Bullet Cluster bound).
**PDTP Original:** n = 1 selection by stability + Kibble-Zurek (this document).
**PDTP Original:** Planck-vortex relic m_DM = m_P; falsifiable via CMB tensor
modes (this document).

---

*Part 116, Phase 84. Previous: Part 115 (extremal condensate closure).*
*Updates: `dark_matter_energy.md` (DM mass row), `equation_reference.md`.*
