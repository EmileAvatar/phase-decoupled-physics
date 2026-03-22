# Full Stress-Energy Tensor T_μν for PDTP (Part 72)

**Status:** DERIVED, VERIFIED (SymPy 6/6, Sudoku 10/10)
**PDTP Original** — full spatial components T_0i and T_ij derived for the first time.
**Closes:** ChatGPT review gap #1 (only T_00 existed from Part 43).
**Script:** `simulations/solver/stress_energy_full.py` (Phase 41)

---

## 1. Motivation

Part 43 (`scalar_backreaction.py`) derived only T_00 (energy density) and pressure p = L
for spatially uniform fields. A complete stress-energy tensor requires:

- **T_00** — energy density (existed)
- **T_0i** — energy flux / momentum density (**NEW**)
- **T_ij** — spatial stress, including anisotropic shear (**NEW**)
- Conservation law ∇^μ T_μν = 0 (**NEW** — explicit proof)
- Two-phase decomposition for all components (**NEW**)

Without the full tensor, reviewers cannot verify energy-momentum conservation,
gravitational source terms, or the equation of state beyond the isotropic limit.

---

## 2. Conventions

- **Metric signature:** (+−−−) (Minkowski, particle physics convention)
- **Canonical stress-energy tensor** (Noether / Peskin & Schroeder):

  T_μν = Σ_a (∂L/∂(∂^μ φ_a)) ∂_ν φ_a − g_μν L       ... (1) [ASSUMED]

  **Source:** Peskin & Schroeder (1995), sec 2.2, eq (2.17)

- **Hilbert stress-energy** (variational, used in GR) agrees with canonical
  for scalar fields without gauge symmetry. For PDTP scalars: canonical = Hilbert.

  **Source:** Weinberg (1972), Gravitation and Cosmology, ch 12.

---

## 3. Single-Phase Derivation

### 3.1 Lagrangian

L = ½(∂_μ φ)(∂^μ φ) + ½(∂_μ ψ)(∂^μ ψ) + g cos(ψ − φ)       ... (2) [ASSUMED]

In (+−−−) metric: (∂_μ φ)(∂^μ φ) = φ̇² − |∇φ|²

So: L = ½(φ̇² − |∇φ|²) + ½(ψ̇² − |∇ψ|²) + g cos(ψ − φ)       ... (3)

**Source:** CLAUDE.md (PDTP Lagrangian)

### 3.2 Canonical momenta

π^φ_μ = ∂L/∂(∂^μ φ) = ∂_μ φ       ... (4) [DERIVED]
π^ψ_μ = ∂L/∂(∂^μ ψ) = ∂_μ ψ       ... (5) [DERIVED]

(Standard result for canonical kinetic terms.)

### 3.3 T_00 — Energy density

T_00 = Σ_a π^a_0 ∂_0 φ_a − g_00 L       ... (from eq 1)
     = φ̇² + ψ̇² − L       (since g_00 = +1)

Substituting eq (3):

T_00 = φ̇² + ψ̇² − ½φ̇² + ½|∇φ|² − ½ψ̇² + ½|∇ψ|² − g cos(ψ−φ)

**T_00 = ½φ̇² + ½|∇φ|² + ½ψ̇² + ½|∇ψ|² − g cos(ψ − φ)**       ... (6) [DERIVED]

**SymPy verification:** residual = 0 ✓

Note: For spatially uniform fields (∇φ = 0), this reduces to Part 43:
ρ = ½φ̇² − g cos(ψ − φ) (single-field version with ψ implicit).

### 3.4 T_0i — Energy flux / momentum density

T_0i = Σ_a π^a_0 ∂_i φ_a − g_0i L       (g_0i = 0 for Minkowski)

**T_0i = φ̇ ∂_i φ + ψ̇ ∂_i ψ**       ... (7) [DERIVED]

Physical interpretation: energy flux in the i-direction. This is the Poynting-vector
analogue for the PDTP scalar fields. It vanishes for spatially uniform fields.

**PDTP Original:** Not previously derived. Required for momentum conservation checks.

### 3.5 T_ij — Spatial stress

T_ij = Σ_a ∂_i φ_a ∂_j φ_a − g_ij L       (g_ij = −δ_ij)

**T_ij = ∂_i φ ∂_j φ + ∂_i ψ ∂_j ψ + δ_ij L**       ... (8) [DERIVED]

where the +δ_ij comes from −g_ij = +δ_ij in (+−−−).

Structure:
- **Diagonal (i = j):** T_ii = (∂_i φ)² + (∂_i ψ)² + L (pressure + gradient stress)
- **Off-diagonal (i ≠ j):** T_ij = ∂_i φ ∂_j φ + ∂_i ψ ∂_j ψ (anisotropic shear)

For spatially uniform fields: T_ij = δ_ij L = p δ_ij, confirming p = L (Hilbert).

**SymPy verification:** T_xx(∇=0) − L(∇=0) = 0 ✓

**PDTP Original:** Spatial components not previously derived.

### 3.6 Summary table (single-phase)

| Component | Formula | Physical meaning |
|-----------|---------|-----------------|
| T_00 | ½φ̇² + ½\|∇φ\|² + ½ψ̇² + ½\|∇ψ\|² − g cos(ψ−φ) | Energy density |
| T_0i | φ̇ ∂_i φ + ψ̇ ∂_i ψ | Energy flux / momentum density |
| T_ij | ∂_i φ ∂_j φ + ∂_i ψ ∂_j ψ + δ_ij L | Stress (pressure + shear) |
| Trace T | T_00 − Σ_i T_ii = ρ − 3p (in 3+1D) | Gravitational coupling |

---

## 4. Two-Phase Derivation

### 4.1 Two-Phase Lagrangian (Part 61)

L₂ = ½(∂_μ φ_b)² + ½(∂_μ φ_s)² + ½(∂_μ ψ)²
     + g cos(ψ − φ_b) − g cos(ψ − φ_s)       ... (9) [DERIVED, Part 61]

Three fields: φ_b (bulk/gravity, +cos), φ_s (surface/tension, −cos), ψ (matter).

**Source:** Part 61, `two_phase_lagrangian.py`; CLAUDE.md

### 4.2 Two-Phase T_μν components

Applying eq (1) with three fields:

**T_00 = ½|∂φ_b|² + ½|∂φ_s|² + ½|∂ψ|² − g cos(ψ−φ_b) + g cos(ψ−φ_s)**       ... (10) [DERIVED]

where |∂φ_a|² = φ̇_a² + |∇φ_a|² (note: positive-definite, time + space).

**T_0i = φ̇_b ∂_i φ_b + φ̇_s ∂_i φ_s + ψ̇ ∂_i ψ**       ... (11) [DERIVED]

**T_ij = ∂_i φ_b ∂_j φ_b + ∂_i φ_s ∂_j φ_s + ∂_i ψ ∂_j ψ + δ_ij L₂**       ... (12) [DERIVED]

**SymPy verification:** T_00(vacuum) = 0 ✓

**PDTP Original:** Two-phase T_μν components derived for the first time.

### 4.3 Per-field decomposition

The kinetic contributions to T_μν are additive per field:

K_μν^(a) = ∂_μ φ_a ∂_ν φ_a       ... (13)

Total: T_μν = Σ_a K_μν^(a) − g_μν L₂       ... (14)

The coupling terms (±g cos) appear only in L₂ (the metric term), not in K_μν.
This means each field carries its own momentum density (K_0i^(a)), but pressure
is a collective property from the full Lagrangian.

---

## 5. Mode Decomposition (φ_+, φ_−)

### 5.1 Change of variables

φ_+ = (φ_b + φ_s)/2       (gravity mode)       ... (15)
φ_− = (φ_b − φ_s)/2       (surface mode)       ... (16)

**Source:** Part 61, two_phase_lagrangian.py

### 5.2 Kinetic sector transformation

½(∂_μ φ_b)² + ½(∂_μ φ_s)² = (∂_μ φ_+)² + (∂_μ φ_−)²       ... (17) [DERIVED]

**Proof:**
  φ_b = φ_+ + φ_−, φ_s = φ_+ − φ_−
  ½(∂φ_+ + ∂φ_−)² + ½(∂φ_+ − ∂φ_−)²
  = ½(∂φ_+² + 2∂φ_+∂φ_− + ∂φ_−²) + ½(∂φ_+² − 2∂φ_+∂φ_− + ∂φ_−²)
  = ∂φ_+² + ∂φ_−²   (cross terms cancel) ✓

**SymPy verification:** residual = 0 ✓

### 5.3 Mode-basis T_μν

**T_00 = (φ̇_+)² + |∇φ_+|² + (φ̇_−)² + |∇φ_−|² + ½ψ̇² + ½|∇ψ|²
       − g cos(ψ−φ_b) + g cos(ψ−φ_s)**       ... (18) [DERIVED]

**T_0i = 2 φ̇_+ ∂_i φ_+ + 2 φ̇_− ∂_i φ_− + ψ̇ ∂_i ψ**       ... (19) [DERIVED]

The factor 2 comes from the normalisation: ½(∂φ_b)² + ½(∂φ_s)² → (∂φ_+)² + (∂φ_−)²
means the canonical momentum for φ_+ is π_+ = 2φ̇_+, not φ̇_+.

**Physical interpretation:**
- φ_+ channel: gravitational energy transport (bulk mode)
- φ_− channel: surface/screening energy transport (reversed Higgs mode)
- ψ channel: matter energy transport

**PDTP Original:** Mode-basis T_μν not previously derived.

---

## 6. Conservation Law: ∇^μ T_μν = 0

### 6.1 Proof from Euler-Lagrange equations

**Theorem (Noether, 1918):** For any Lagrangian L(φ_a, ∂_μ φ_a) that is invariant
under spacetime translations, the canonical T_μν satisfies ∇^μ T_μν = 0 whenever
the Euler-Lagrange equations hold.

**Proof:**

Step 1. Start from T^μν = Σ_a π^a_μ ∂^ν φ_a − g^μν L       ... (from eq 1)

Step 2. Take divergence:
  ∂_μ T^μν = Σ_a [(∂_μ π^a_μ) ∂^ν φ_a + π^a_μ ∂_μ ∂^ν φ_a] − ∂^ν L       ... (20)

Step 3. Use Euler-Lagrange: ∂_μ π^a_μ = ∂L/∂φ_a       ... (21) [E-L equation]

Step 4. Expand ∂^ν L by chain rule:
  ∂^ν L = Σ_a [(∂L/∂φ_a) ∂^ν φ_a + (∂L/∂(∂_μ φ_a)) ∂_μ ∂^ν φ_a]
        = Σ_a [(∂L/∂φ_a) ∂^ν φ_a + π^a_μ ∂_μ ∂^ν φ_a]       ... (22)

Step 5. Substitute eqs (21) and (22) into eq (20):
  ∂_μ T^μν = Σ_a [(∂L/∂φ_a) ∂^ν φ_a + π^a_μ ∂_μ ∂^ν φ_a]
            − Σ_a [(∂L/∂φ_a) ∂^ν φ_a + π^a_μ ∂_μ ∂^ν φ_a]
           = 0       ... (23) [DERIVED]

**∇^μ T_μν = 0   (QED)**

**Source:** Peskin & Schroeder (1995) sec 2.2; Noether (1918)

### 6.2 Applicability to PDTP

This proof uses only:
1. The canonical form of T_μν (eq 1)
2. Euler-Lagrange equations (eq 21)
3. Chain rule for ∂^ν L (eq 22)

It makes NO assumptions about the specific form of L. Therefore:

- **Single-phase PDTP** (2 fields: φ, ψ): conservation holds ✓
- **Two-phase PDTP** (3 fields: φ_b, φ_s, ψ): conservation holds ✓
- **SU(3) extension** (matrix fields): conservation holds (same Noether argument) ✓

### 6.3 Numerical verification

For spatially uniform fields:
  dT_00/dt + ∂_i T^0i = 0
  Since T_0i = 0 (uniform), this reduces to dT_00/dt = 0.
  T_00 = ½φ̇² + V(φ), dT_00/dt = φ̇(φ̈ − g sin(ψ−φ)) = φ̇ × 0 = 0 when E-L holds.

**Sudoku test SE-S10:** residual = 0 ✓

---

## 7. Equation of State (EOS)

### 7.1 General (with spatial gradients)

For a perfect fluid approximation: w = p/ρ = L/T_00

This is ONLY valid when the field is spatially uniform (isotropic pressure).
When gradients are present, T_ij is anisotropic and a single w does not describe
the full stress.

### 7.2 Limiting cases (spatially uniform)

| Regime | T_00 (= ρ) | T_ii (= p) | w = p/ρ | Physical analogue |
|--------|-------------|-------------|---------|------------------|
| Kinetic (g→0) | ½φ̇² | ½φ̇² | +1 | Stiff fluid |
| Potential (φ̇→0) | −g cos(ψ−φ) | +g cos(ψ−φ) | −1 | Dark energy / Λ |
| Mixed | ½φ̇² − g cos | ½φ̇² + g cos | (K+V)/(K−V) | Quintessence |

**SymPy verification:** Both limits verified ✓
**Sudoku tests SE-S5, SE-S6:** PASS ✓

---

## 8. SymPy Verification Summary

| # | Identity | Result |
|---|----------|--------|
| V1 | T_00 + T_xx = Σ_a \|∂φ_a\|² (coupling cancels in sum) | PASS ✓ |
| V2 | T_xx(∇=0) = L(∇=0) (pressure = L for uniform) | PASS ✓ |
| V3 | Trace(uniform, 1+1D) = −2g cos(ψ−φ) | PASS ✓ |
| V4 | T_00 invariant under U(1) shift φ→φ+δ, ψ→ψ+δ | PASS ✓ |
| V5 | Mode decomposition: \|∂φ_b\|² + \|∂φ_s\|² = 2\|∂φ_+\|² + 2\|∂φ_−\|² | PASS ✓ |
| V6 | Two-phase coupling = 0 when φ_b = φ_s (φ_− = 0) | PASS ✓ |

**Score: 6/6 pass**

---

## 9. Sudoku Scorecard

| Test | Description | Result |
|------|-------------|--------|
| SE-S1 | T_00 formula (uniform, single-phase) | PASS |
| SE-S2 | T_0i = 0 for spatially uniform fields | PASS |
| SE-S3 | Pressure p = L (uniform, Hilbert convention) | PASS |
| SE-S4 | Trace identity T = ρ(1−3w) for w=−1 | PASS |
| SE-S5 | EOS kinetic limit: w = +1 (stiff fluid) | PASS |
| SE-S6 | EOS potential limit: w = −1 (dark energy) | PASS |
| SE-S7 | U(1) shift invariance of T_00 | PASS |
| SE-S8 | T_00 = 0 in vacuum | PASS |
| SE-S9 | Mode decomposition identity | PASS |
| SE-S10 | Conservation dT_00/dt = 0 when E-L holds | PASS |

**Score: 10/10 pass**

---

## 10. What This Enables

With the full T_μν now derived, the following downstream work is unblocked:

1. **Gravitational source terms:** G_μν = (8πG/c⁴) T_μν now has all components available.
2. **Light bending calculations:** T_0i and T_ij needed for the full geodesic equation.
3. **Frame-dragging:** T_0i (momentum density) is the source of gravitomagnetic effects.
4. **Energy conditions:** Null (T_μν k^μ k^ν ≥ 0), weak (T_00 ≥ 0), strong (T_μν − ½T g_μν)
   can now be checked for arbitrary field configurations.
5. **Anisotropic cosmology:** T_ij shear terms drive Bianchi-type evolution.

---

## 11. Relation to Other Parts

| Part | Connection |
|------|-----------|
| Part 43 (scalar_backreaction.py) | T_00 and p = L derived there; now EXTENDED to full tensor |
| Part 61 (two_phase_lagrangian.py) | Two-phase Lagrangian is the starting point for §4 |
| Part 63 (two_phase_rederivation.py) | 16/16 tests all use T_00; full tensor adds T_0i, T_ij |
| Part 25 (dark energy w(z)) | EOS w = p/ρ confirmed as limiting case of full T_μν |
| Part 12 (tetrad) | Emergent metric g_μν requires full T_μν as source |

---

## Changelog

- 2026-03-20: Initial derivation — all components for single-phase and two-phase.
  Conservation law proved from Noether/E-L. SymPy 6/6, Sudoku 10/10.
  Closes ChatGPT review gap #1.
