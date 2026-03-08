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

- [x] **SU(3) gauge structure from phase lattice** *(from Part 27b — RESOLVED 2026-03-08)*
  - 8 gluons as normal modes: YES — SU(3) small fluctuations give 8 massless spin-1 modes ✓
  - Asymptotic freedom: NEGATIVE — β(K)=+K²/(8π²)>0 (IR free); QCD AF is a gauge-level property ✓
  - SU(2) from Z₂: PARTIAL — generator count matches, chirality/mass incomplete
  - Key insight: K (condensate stiffness) ≠ g (QCD coupling) — distinct levels
  - Docs: `docs/research/su3_gauge_structure.md`; Script: Phase 17 `su3_gauge_structure.py`

- [x] **Scalar sector backreaction on tensor sector** *(RESOLVED 2026-03-08)*
  - T_μν^φ = 0 in vacuum: U(1) shift symmetry makes condensate vacuum-insensitive ✓
  - Excited condensate (breathing mode) gives w = −1 (potential) to +1 (kinetic) → dark energy ✓
  - Bridges Part 25 w(z) result: phase drift IS a geometric backreaction on the Einstein eq ✓
  - Does NOT fully solve Λ problem: matter-sector vacuum energy still contributes T_μν^vac^matter
  - 11/11 Sudoku tests pass
  - Docs: `docs/research/scalar_tensor_backreaction.md`; Script: Phase 18 `scalar_backreaction.py`

- [x] **Derive hierarchy ratio R = α_G/α_EM from lattice topology** *(Strategy B — RESOLVED 2026-03-08)*
  - **PDTP Original:** R = 1/(n² × α_EM) where n = m_cond/m (vortex winding number, Part 33) ✓
  - Hierarchy problem = winding number problem: why is n_p = m_P/m_p ~ 10¹⁹?
  - Path A (QCD chain): m_cond = Λ_QCD ≈ 200 MeV correctly inferred from σ_QCD; G off by 10⁴⁰ (hierarchy gap)
  - Path B (Dirac large numbers): Eddington off 10²¹, Hubble off 10¹¹ — no clean coincidence
  - Path C (Dvali species): N_required = n² ~ 10³⁸ >> N_SM ~ 118 — circular (needs G) and off by 10³⁶
  - Two free parameters block derivation: m_cond (undetermined) AND α_EM (not derived in PDTP)
  - 10/10 Sudoku tests pass
  - Docs: `docs/research/hierarchy_ratio.md`; Script: Phase 19 `hierarchy_ratio.py`
  - Open path: Sakharov route — N_eff from lattice symmetry + a from breathing mode measurement

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

### Standard Model Gaps (from OP#1 — SU(2) partial result)

PDTP now explains the *structure* of SU(3)×SU(2)×U(1) (force carriers, confinement,
symmetry groups). The following **values and mechanisms** remain open:

- [ ] **Weak coupling strength g_W**
  - SU(2) coupling g_W ≈ 0.65 has no derivation in PDTP
  - Analogous to the m_cond problem: structure known, scale not derived

- [ ] **W and Z boson masses (Higgs mechanism)**
  - W and Z are massive; current PDTP SU(2) gives massless bosons
  - Needs a Higgs-like sector or symmetry-breaking mechanism within the condensate
  - Candidate: condensate phase transition at electroweak scale ~246 GeV

- [ ] **Chirality — why SU(2) couples only to left-handed particles**
  - Biggest structural gap: PDTP Lagrangian has no left/right asymmetry
  - Parity violation is observed (Wu 1956) but not yet explained
  - Possible path: Z₂ vortex chirality from condensate winding direction?

- [ ] **Three generations of fermions (electron, muon, tau + neutrinos)**
  - Standard Model has 3 identical copies of the fermion sector at different masses
  - No explanation in any current theory including PDTP
  - Possible path: excited vortex states (n=1,2,3 winding) → three generations?

- [ ] **Coupling constant values (α_EM, α_W, α_S)**
  - The three coupling constants run with energy and unify near 10¹⁶ GeV (GUT scale)
  - PDTP predicts the group structure but not the coupling values
  - Strategy B (hierarchy ratio R = α_G/α_EM) is the existing path toward this

### Cosmological

- [ ] **Cosmological Constant via Forced Checklist Check**
  - Part 43: condensate T_μν^φ = 0 in vacuum (U(1) shift) — does NOT add to Λ ✓
  - But: matter-sector vacuum energy (quarks, leptons, Higgs zero-point) still unresolved
  - Observed: Λ_obs ~ 1.1×10⁻⁵² m⁻²; QFT predicts ~10¹²⁰ × Λ_obs (worst prediction in physics)
  - **Method: Forced Checklist Check** — go through ALL Methodology.md items one by one
  - Question: can any checklist path reduce or explain the Λ problem in PDTP?
  - Candidate paths not yet tried: topological argument (Λ from lattice winding?), order parameter (Λ as condensate gap?), analogy (BCS gap → Λ?), postulate-and-derive

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
