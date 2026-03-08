# TODO_02 — Active Roadmap

Summary of completed work: [TODO_Summary.md](TODO_Summary.md)
Full archive: [TODO_01.md](TODO_01.md)

---

## Current Status

Parts 1–41 complete. The QCD lattice progression has reached:
- Strong-coupling sigma = 0.1729 GeV² (4% off QCD) — analytically closed
- Physical beta (β=6.0) confirmed working with small-step Metropolis
- N=4 CPU demo done; N≥16 GPU required for reliable Cornell fit

**Central open problem:** m_cond is underdetermined. G = ħc/m_cond² is exact but
m_cond = m_P cannot be derived perturbatively (Parts 29–35 exhausted this path).
This is analogous to Λ in GR.

---

## Part 42 — GPU Lattice at Physical Beta (NEXT TASK)

**Goal:** Run SU(3) lattice at β=6.0, N=16 on GPU (RTX 3060 + CuPy) to get a
box size of 1.5 fm and reliable Cornell fit giving σ_phys ≈ 0.18 GeV².

**Why N≥16 is required:**
- At β=6.0, lattice spacing a = 0.093 fm (Necco-Sommer 2001)
- Confinement onset at R > 0.5 fm = ~5 lattice spacings
- N=4 box = 0.37 fm < onset → only Coulomb regime accessible
- N=16 box = 1.5 fm → R up to 8 spacings → linear regime accessible

**Steps:**
- [ ] Install CuPy for CUDA 12.x on RTX 3060 (`pip install cupy-cuda12x`)
- [ ] Add GPU support to `simulations/solver/su3_physical_beta.py`
  - Replace `np` with `cp` (CuPy) for link matrices
  - Keep CPU fallback when CuPy not available
- [ ] Run: `python su3_physical_beta.py --N 16 --beta 6.0 --meas 500 --gpu`
- [ ] Verify Cornell fit: V(R) = σR + A/R + c with R = 1..8
- [ ] Target: σ_lat ~ 0.04 → σ_phys ~ 0.18 GeV² (standard quenched QCD)
- [ ] Optional: beta scan β = 5.7, 5.9, 6.0, 6.2 to confirm scaling window

**Expected Sudoku scorecard:** 7/7 (S26 should now pass with N=16)

**Files to update:**
- `simulations/solver/su3_physical_beta.py` — add GPU mode
- `docs/research/su3_physical_beta.md` — update with GPU results
- `simulations/solver/main.py` — no change needed (Phase 16 already wired)

---

## Open Problems (from TODO_01.md — still unresolved)

### Structural

- [ ] **SU(3) gauge structure from phase lattice** *(from Part 27b)*
  - Can 8 gluon modes emerge as normal modes of the quark-condensate system?
  - Does asymptotic freedom follow from phase-locking?
  - Can SU(2) weak structure emerge from Z₂ matter/antimatter phase symmetry?

- [ ] **Scalar sector backreaction on tensor sector**
  - Does φ dynamics modify the effective T_μν seen by the Einstein equation?
  - Could bridge scalar (vacuum-insensitive) and tensor (vacuum-sensitive) sectors

- [ ] **Derive hierarchy ratio R = α_G/α_EM from lattice topology** *(Strategy B)*
  - From Part 29 Chain 7: if R ~ 10⁻³⁷ can be derived, G follows from particle physics alone
  - Sakharov path: determine N_eff (lattice symmetry) + a (breathing mode) independently

### Black Holes

- [ ] **Black hole singularity as topological defect**
  - r=0 replaced by vortex core with finite healing length ξ
  - Penrose theorems assume continuous manifold — lattice cutoff may evade them

- [ ] **Hawking radiation information paradox in PDTP condensate**
  - Do exterior condensate phase correlations encode infalling matter state?
  - Testable in analogue systems (sonic BHs in BECs — Steinhauer 2016)

- [ ] **Black hole evaporation endpoint**
  - At M ~ M_Planck: condensate picture breaks down
  - What replaces the classical singularity? Phase soliton? Local decoherence?

### Cosmological

- [ ] **CP violation and baryogenesis**
  - PDTP Lagrangian is C, P, T invariant separately → no CP violation
  - Sakharov baryogenesis blocked — needs an extension to break CP

---

## Methodology Note

Before starting any new part, follow the Problem-Solving Protocol (CLAUDE.md):
1. Read `docs/Methodology.md` and select relevant checklist items
2. Write a plan and present to user
3. Only proceed after approval

---

## Rules

- Do one part at a time (CLAUDE.md)
- User approves before committing/pushing to GitHub
- Every new equation needs a source citation or **PDTP Original** label
- All new Python files: ASCII only (no Unicode — Windows cp1252)
- Sudoku check on every new value/equation introduced
