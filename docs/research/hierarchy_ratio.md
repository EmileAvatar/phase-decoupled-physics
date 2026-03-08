# Hierarchy Ratio R = alpha_G / alpha_EM — Part 44

**Status:** Computed — NEGATIVE result (cannot derive from topology alone)
**Prerequisite reading:** Part 29 (substitution chains), Part 33 (vortex winding),
Part 38 (SU(3) lattice, QCD string tension)

---

## What We Are Asking

Can the dimensionless ratio

```
R = alpha_G(proton) / alpha_EM   ~  8e-37
```

be derived from PDTP lattice topology, without using G as input?

- alpha_G(p) = G m_p^2 / (hbar c)  ~  5.9e-39   [gravitational fine-structure constant]
- alpha_EM = e^2/(4*pi*eps_0*hbar*c)  ~  7.3e-3  [= 1/137]
- R ~ 8e-37 is the hierarchy between gravity and electromagnetism at the proton mass scale

If R can be derived from topology, G follows via G = alpha_G(p) * hbar * c / m_p^2 —
**without circular input.**

---

## PDTP Identity (PDTP Original)

From Part 33: G = hbar*c / m_cond^2. Substituting into alpha_G:

```
alpha_G(p) = G m_p^2 / (hbar c) = (hbar*c / m_cond^2) * m_p^2 / (hbar*c) = (m_p / m_cond)^2
```

So alpha_G(p) = 1 / n_p^2, where n_p = m_cond / m_p is the proton's vortex winding number (Part 33).

Therefore:

```
R = alpha_G(p) / alpha_EM = 1 / (n_p^2 * alpha_EM)         [PDTP Original]
```

This is exact given G = hbar*c/m_cond^2. Cross-check:
- n_p = M_P / m_p = 2.176e-8 / 1.673e-27 = 1.30e19
- R = 1 / (n_p^2 * alpha_EM) = 1 / (1.69e38 * 7.30e-3) = 8.1e-37  [matches observed R]

**Significance:** The hierarchy problem is not two separate unexplained numbers (G weak, EM strong) but ONE: the vortex winding number n_p ~ 10^19. If n_p can be derived from topology, both G and R follow.

---

## Path A — QCD String Tension Chain

**Idea:** Use the measured QCD string tension sigma_QCD (G-free) to infer m_cond, then derive G.

**Chain:**
```
sigma_QCD  [measured, G-free]
  -> m_cond^2 = sigma_QCD * hbar / (F_SC * c^3)   [Part 38 SC formula]
  -> G = hbar*c / m_cond^2
  -> alpha_G = G m_p^2 / (hbar c)
  -> R = alpha_G / alpha_EM
```

where F_SC = ln(2N/beta) = ln(6 * 4pi) ~ 4.32 (SU(3) strong coupling factor from Part 38).

**Result:**
- sigma_QCD = 0.18 GeV^2 -> m_cond = 3.6e-28 kg ~ Λ_QCD ~ 200 MeV/c^2 [Part 38 confirmed this]
- G_pred = hbar*c / m_cond^2 ~ 2.4e29  vs  G_known = 6.67e-11 m^3/(kg s^2)
- Ratio G_pred / G_known ~ 3.6e39 ~ 10^40 — off by 40 orders of magnitude
- R_pred ~ 10^-37 * 10^40 = 10^3 >> R_observed ~ 10^-37

**Interpretation:** Path A correctly identifies the QCD condensate scale (m_cond ~ Λ_QCD)
but the GRAVITATIONAL condensate operates at m_cond = m_P, not Λ_QCD. The factor 10^40
gap IS the hierarchy problem restated: (m_P / Λ_QCD)^2 = (1.22e19 / 0.2)^2 ~ 3.7e39.

Path A is G-free in chain structure, but does NOT close the gap. The missing ingredient is
explaining why the GRAVITATIONAL condensate scale is m_P and not Λ_QCD.

---

## Path B — Dirac Large Numbers

**Idea:** The large numbers N in nature might fix n_p topologically.

Dirac large numbers hypothesis (Dirac 1937): large dimensionless ratios are related.
Two key numbers: N_Eddington ~ 10^80 (protons in universe), N_Hubble = t_H/t_P ~ 8e60.

| Candidate | Value | n_pred = sqrt(N) | n_p actual | Ratio |
|---|---|---|---|---|
| Eddington N ~ 10^80 | 1e80 | 1e40 | 1.30e19 | 7.7e20 off |
| Hubble N = t_H/t_P ~ 8e60 | 8e60 | 2.8e30 | 1.30e19 | 2.2e11 off |
| N = t_H/t_P (1/2 power) | 8e60 | 2.8e30 | 1.30e19 | 2.2e11 off |

No large-number coincidence gives n_p ~ 10^19 without additional assumptions.
The Dirac hypothesis would predict G changes with cosmic time (G ~ 1/t), which
is observationally constrained: |dG/dt| / G < 10^-12 per year (lunar laser ranging).

---

## Path C — Dvali Species Counting

**Idea (Dvali 2007):** If there are N_species particle species, gravity is diluted:
G_eff = G_bare / N_species, where G_bare = hbar*c / m_P^2.

For G_eff = G_measured, we need N_species = n_p^2 ~ 1.69e38.

**Problem (circular):** N_species = n_p^2 = (m_P/m_p)^2, which requires knowing m_P,
which requires knowing G. The Dvali mechanism works only if N_species can be counted
independently. In the SM: N_SM ~ 118 (standard model degrees of freedom).

| Mechanism | N_required | N_actual | Ratio |
|---|---|---|---|
| SM degrees of freedom | 1.69e38 | ~118 | 1.43e36 off |

Dvali would need ~10^38 species — possible in string landscape but not derivable
from the known SM particle content.

---

## Sudoku Scorecard (Phase 19 — 10 tests)

See `simulations/solver/hierarchy_ratio.py` for numerical verification.

| Test | Description | Result |
|---|---|---|
| H1 | R_proton = alpha_G(p) / alpha_EM (definition check) | PASS |
| H2 | PDTP identity: n_p^2 * R * alpha_EM = 1 (proton) | PASS (exact) |
| H3 | PDTP identity: n_e^2 * R_e * alpha_EM = 1 (electron) | PASS (exact) |
| H4 | alpha_G(p) = (m_p/m_cond)^2 = 1/n_p^2 | PASS (exact) |
| H5 | Path A: m_cond from sigma_QCD matches Lambda_QCD | PASS (~1%) |
| H6 | Path A: G_pred/G_known >> 1 (hierarchy gap ~ 10^40) confirmed | PASS (gap confirmed) |
| H7 | Path B: Eddington n_pred >> n_p (off by ~10^21) confirmed | PASS (gap confirmed) |
| H8 | Path B: Hubble n_pred != n_p (off by ~10^11) confirmed | PASS (gap confirmed) |
| H9 | Path C: Dvali N_required >> N_SM (gap ~ 10^36) confirmed | PASS (gap confirmed) |
| H10 | Two-param: R needs alpha_EM AND n (both indispensable) | PASS (exact) |

**Score: 10/10 pass** — H1–H5 confirm the PDTP identity and Path A QCD result;
H6–H9 confirm (by passing) that all three derivation paths fail to close the gap;
H10 confirms two parameters are required. Verified: `hierarchy_ratio.py`.

---

## Key Results

**Result 1 (PDTP Original):** R = 1/(n^2 * alpha_EM)
The hierarchy ratio is not two unexplained numbers but one: the vortex winding number
n_p = m_cond/m_p. If n could be derived from topology without G as input, the full
hierarchy problem would be solved.

**Result 2 (negative):** No path from pure lattice topology gives n_p ~ 10^19.
All three candidate mechanisms fail by at least 10^11 (Hubble time) or more.

**Result 3 (finding):** Path A is G-free in structure and correctly identifies
m_cond = Lambda_QCD from QCD string tension. But the gravitational condensate is at
m_cond = m_P, not Lambda_QCD. The missing insight is: WHY are there two condensate
scales, and what forces the gravitational one to be m_P?

**Result 4:** The problem requires TWO undetermined inputs: m_cond (sets G) and
alpha_EM (known from experiment but not derived in PDTP). This means the hierarchy
problem splits into two independent open questions, not one.

**Open path:** The Sakharov approach from TODO_02 — determine N_eff (lattice symmetry
count) + a (breathing mode measurement) independently — remains the most promising
avenue. It bypasses the need to derive n_p algebraically.

---

## Sources

- Dirac (1937), "The Cosmological Constants," Nature 139, 323 — large numbers hypothesis
- Dvali (2007), arXiv:0706.1075 — species mechanism for gravity dilution
- PDG (2022), particle data tables — alpha_EM, alpha_G values, Lambda_QCD
- **PDTP Original:** R = 1/(n^2 * alpha_EM) identity; hierarchy problem = winding number problem;
  Path A QCD chain showing m_cond = Lambda_QCD from sigma_QCD
- Cross-references: Part 29 (substitution chains), Part 33 (vortex winding, n = m_cond/m),
  Part 38 (SU(3) lattice, strong coupling string tension formula)
