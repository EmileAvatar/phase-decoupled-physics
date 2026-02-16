# TODO: Mathematical Formalization Roadmap

This file tracks the critical mathematical gaps that must be resolved for PDTP
to move from conceptual framework to testable physical theory.

See [math_status.md](docs/research/math_status.md),
[quantum_gravity_deep_dive.md](docs/research/quantum_gravity_deep_dive.md), and
[mathematical_formalization.md](docs/research/mathematical_formalization.md) for
full context.

---

## Critical Gaps

- [x] **Field equation for coupling parameter alpha**
  - ~~No governing equation exists for alpha(x,t)~~
  - Alpha is now derived from the Lagrangian: α = cos(ψ − φ)
  - Field equations derived via Euler-Lagrange in
    [mathematical_formalization.md](docs/research/mathematical_formalization.md) Section 3
  - **Sign error corrected:** coupling must be +cos for stability (Section 2.3)

- [x] **Energy cost of phase control**
  - Derived from Hamiltonian in Section 8
  - Decoupling energy per mode: ΔE = gᵢ (coupling constant)
  - Order of magnitude: ~10⁻⁹ J per kg (gravitational self-energy scale)
  - Gradient energy cost: E_grad = ∫ ½(∇(ψ−φ))² d³x

- [x] **Stability analysis**
  - Linearized perturbations satisfy Klein-Gordon equation (Section 6.2)
  - Dispersion relation: ω² = k² + 2g > 0 — all modes stable (Section 6.3)
  - Lyapunov stability proved via bounded Hamiltonian (Section 6.5)
  - Asymptotic stability holds in overdamped (Kuramoto) limit

- [x] **Conservation law compliance**
  - Energy conservation: proved via Noether's theorem + direct verification
    (Section 5.1, 5.4)
  - Momentum conservation: proved via Noether's theorem (Section 5.2)
  - Phase charge conservation: proved via global phase symmetry (Section 5.3)
  - Causality: preserved by Lorentz-invariant Lagrangian construction

- [x] **Quantum description of spacetime phase field (phi)**
  - ~~phi is currently undefined in standard physics~~
  - φ identified as the phase of a vacuum superfluid condensate (SVT)
  - Connected to established research: Volovik (2003), Barceló-Liberati-Visser (2005)
  - Lorentz invariance emerges at low energies (Volovik mechanism)
  - See [advanced_formalization.md](docs/research/advanced_formalization.md) §1
  - **Remaining:** microscopic structure of the condensate is unknown

- [x] **Quantitative GR recovery (Newtonian limit)**
  - Newtonian 1/r potential recovered in weak-field static limit (Section 7)
  - Poisson equation ∇²φ = −ρ_phase recovered (Section 7.5)
  - Newton's constant G identified via coupling-to-mass mapping (Section 7.5)
  - **Remaining:** Post-Newtonian corrections (perihelion, lensing, waves)

- [x] **Numerical experimental predictions**
  - δα at Earth surface: ~10⁻¹⁹ (Section 9.1)
  - BEC coherence amplification factor: √N (Section 9.2)
  - BEC prediction (N=10⁶): δα ~ 10⁻⁷ (approaching testability)
  - Falsifiable: coherent vs incoherent matter should show different free-fall

- [x] **Connect to Kuramoto model formally**
  - Overdamped limit of PDTP = standard Kuramoto model (Section 4.1)
  - PDTP is a relativistic, spatially-extended, second-order Kuramoto (Section 4.3)
  - Known Kuramoto results imported: critical coupling, phase transition,
    spontaneous synchronization (Section 4.2)

---

## Structural Requirements

- [x] Preserve Lorentz invariance — Lagrangian is Lorentz scalar by construction
- [x] Preserve energy-momentum conservation — proved via Noether (Section 5)
- [x] Be derivable from a consistent Lagrangian — Sections 2–3
- [x] Be experimentally testable — predictions in Section 9
- [x] Be distinguishable from existing GR/QFT predictions — coherence-dependent
  gravity is unique to PDTP (advanced_formalization.md §4.1)

---

## Completed (Advanced Topics — Part 2)

- [x] **Post-Newtonian corrections** ([advanced_formalization.md](docs/research/advanced_formalization.md) §2)
  - Cosine nonlinearity gives 1/r² correction to potential → perihelion precession ✓
  - Correct functional form (1/r³ force); magnitude depends on parameter fit
  - Gravitational waves propagate at c ✓ (Lorentz invariant by construction)
  - **Unresolved:** GW polarization (PDTP: scalar; GR: tensor); PPN parameter γ exact value
  - **Unresolved:** Shapiro delay, frame-dragging require full PPN calculation

- [x] **Quantum description of spacetime phase field** ([advanced_formalization.md](docs/research/advanced_formalization.md) §1)
  - φ = phase of vacuum superfluid condensate (SVT identification)
  - Connected to Volovik (2003), Barceló-Liberati-Visser (2005), Unruh (1981)
  - **Remaining:** microscopic condensate structure

- [x] **EM and nuclear force integration** ([advanced_formalization.md](docs/research/advanced_formalization.md) §3)
  - PDTP adds gravitational coupling to Standard Model (doesn't replace it)
  - Full combined Lagrangian written (L_PDTP + L_SM)
  - Gauge invariance resolved: gravity couples to de Broglie phase (gauge-invariant)
  - **Remaining:** photon coupling to φ (needs tensor extension)

- [x] **Experimental test design** ([advanced_formalization.md](docs/research/advanced_formalization.md) §4)
  - Dual-state BEC atom interferometry protocol designed
  - Three-phase experiment: baseline → increased coherence → phase modulation
  - Signal estimates: conservative ~10⁻¹⁶, optimistic ~10⁻¹³ (Δg/g)
  - Current precision ~10⁻¹² — approaching testability

## Remaining Work (Hard Open Problems)

- [x] **Gravitational wave polarization mismatch**
  - ~~PDTP gives 1 scalar mode; GR gives 2 tensor modes (LIGO-confirmed)~~
  - Resolved: tensor modes emerge from condensate tetrad structure (Volovik mechanism)
  - PDTP predicts E(2) class N₃: 2 tensor + 1 breathing mode
  - Breathing mode is a new testable prediction (multi-detector GW polarimetry)
  - See [hard_problems.md](docs/research/hard_problems.md) §1

- [x] **Full PPN parameter calculation**
  - γ = 1 from acoustic metric density perturbation (equal g₀₀ and gᵢⱼ)
  - β = 1 from Lorentz invariance and linear weak-field superposition
  - Independently: massive scalar Yukawa suppression → γ ≈ 1 at solar system scales
  - Nordtvedt parameter η_N = 0 (consistent with LLR)
  - **Caveat:** γ = 1 depends on condensate equation of state parameter κ = −2
  - See [hard_problems.md](docs/research/hard_problems.md) §2

- [x] **Vacuum condensate microscopic structure**
  - Constraints from PDTP Lagrangian: U(1) symmetry, Lorentz-invariant ground state,
    correct dispersion relation, cosine coupling emergence
  - Connected to Group Field Theory (Oriti 2014, Gielen & Sindoni 2016): spacetime
    as condensate of quantum tetrahedra
  - **Remains genuinely open:** microscopic constituents unknown (open in SVT itself)
  - See [hard_problems.md](docs/research/hard_problems.md) §3

- [x] **Photon coupling to φ**
  - Resolved: photons couple INDIRECTLY via acoustic metric (not via cos coupling)
  - Photons follow null geodesics of the acoustic metric
  - Light bending: θ = 4GM/(bc²) — matches GR (factor of 2 from γ = 1)
  - Gravitational redshift: Δν/ν = ΔU/c² — matches GR
  - No tensor extension of fundamental Lagrangian needed; tensor structure is emergent
  - See [hard_problems.md](docs/research/hard_problems.md) §4

## Remaining Questions (Identified During Part 3 Work)

- [x] **Derive κ = −2 from first principles**
  - ~~Currently assumed; should be derived from the condensate dynamics~~
  - Derived via Painlevé-Gullstrand representation: acoustic metric with constant
    density + free-fall velocity = Schwarzschild metric, which has γ = 1
  - κ is coordinate-dependent (0 in PG, −2 in isotropic); γ = 1 is physical
  - Independently confirmed: relativistic Euler equation with c_s = c gives δρ/ρ₀ = 2U
  - See [hard_problems.md](docs/research/hard_problems.md) §2.11

- [x] **Condensate tetrad structure**
  - Analyzed: He-3A order parameter (Volovik) provides the physical precedent
  - PDTP scalar Lagrangian does NOT produce tetrads — explicit extension needed
  - Minimal extension: Φ_vacuum = √ρ₀ e^{iφ} e^a_μ (tetrad + phase)
  - **Remains the most important structural gap in PDTP**
  - See [hard_problems.md](docs/research/hard_problems.md) §1.10

- [x] **Breathing mode amplitude relative to tensor**
  - Mapped to Brans-Dicke: h_breathing/h_tensor < 1/(2ω+3) < 1.25 × 10⁻⁵ (Cassini)
  - Massive scalar adds Yukawa suppression above threshold frequency
  - Below current LIGO detection threshold; may be accessible with 5+ detectors in 2030s
  - See [hard_problems.md](docs/research/hard_problems.md) §1.9

- [x] **EM coupling constant G_EM in equation (4.3)**
  - ~~Should be fixed by requiring equivalence principle (E = mc²)~~
  - **Resolved: the G_EM term must be REMOVED.** EM stress-energy tensor is traceless
    (T^μ_μ = 0), so photons cannot source a scalar field at classical level. This is
    Nordström's problem. Equation (4.3) replaced by equation (4.7) with only matter sources.
  - Photons still gravitate via acoustic metric geodesics (test particles) and through
    bound EM energy in composite matter (gravitational sources)
  - See [hard_problems.md](docs/research/hard_problems.md) §4.8

## New Questions (Identified During Part 3b Work)

- [x] **Free photon radiation as gravitational source**
  - Free photons don't source □φ (EM trace = 0) — established physics
  - Energy bookkeeping: emitter loses mass E/c², absorber gains it back
  - Thermal equilibrium suppression: t_interaction/t_grav ~ 10⁻¹⁴ in stellar interiors
  - Solar system deficit: ΔM/M☉ ~ 2 × 10⁻²¹ per second — undetectable
  - Self-limiting argument: radiation dominates only when tightly coupled
  - **Conclusion:** cosmological problem, not astrophysical; negligible for all
    post-equality physics. Radiation-era implications addressed separately.
  - See [photon_gravity_analysis.md](docs/research/photon_gravity_analysis.md)

- [x] **Radiation-dominated era cosmology**
  - Matter-era Friedmann equation derived from condensate Euler + continuity
  - Cosmic expansion = condensate Hubble flow v_i = H(t) x_i
  - Tight-coupling resolves photon contribution: effective mass m_eff = m_b + ρ_γ/(n_b c²)
  - Self-limiting: radiation dominates only when tightly coupled to baryons
  - **Genuine gap:** decoupled neutrinos at BBN (41% of ρ_total missing, ~23% error in H)
  - Resolution requires acoustic metric tensor channel or condensate extension
  - See [radiation_era_cosmology.md](docs/research/radiation_era_cosmology.md)

- [x] **Derive Newton's constant G from coupling constants gᵢ independently**
  - Dimensional analysis: G = 𝒞 c^(5/2)/√(ℏρ₀), exact for ρ₀ = ρ_Planck (§2)
  - Coupling gᵢ shown to be geometric (~4πRᵢ), not independent parameters (§3)
  - Reduces N+2 apparent free parameters to 1 effective unknown (𝒞 or ρ₀)
  - Energy-cost circularity resolved: decoupling energy from gᵢ, not Gm²/R (§7)
  - **Remaining gap:** dimensionless prefactor 𝒞 requires condensate microphysics
  - Full derivation needs: what condenses, why, and the ground-state density
  - See [G_derivation.md](docs/research/G_derivation.md)

- [x] **Strong-field equivalence principle**
  - Phase difference δψ = compactness Ξ = GM/(Rc²): 0.21 for NS, 0.50 at BH horizon
  - Nonlinearity sin(δψ)/δψ: 0.7% for NS, 4.1% at horizon — mild throughout
  - Strong-field Nordtvedt parameter: η ~ Ξ²/6 ≈ 7×10⁻³ for NS
  - Gravitational binding energy gravitates correctly to leading order: M_eff = M(1−Ξ/2)
  - Cosine saturation unobservable: δψ < 0.5 for all objects outside their horizons
  - Acoustic horizon at r = 2GM/c² (exact Schwarzschild radius)
  - **Tension:** Double pulsar Ṗ_b (0.013% precision) vs ~1% PDTP GW emission deficit
  - Resolution requires numerical NS interior solution or self-consistent metric proof
  - See [strong_field_ep.md](docs/research/strong_field_ep.md)

- [ ] **Explicit momentum balance for phase-gradient motion**
  - Noether's theorem proves total momentum is conserved (Section 5.2)
  - Missing: a concrete worked example showing momentum transfer between
    matter (ψ) and the phase field (φ) during gradient-following motion
  - Show quantitatively: when a body moves through a phase gradient,
    the phase field φ absorbs equal and opposite momentum
  - This directly addresses the "reactionless drive" objection
  - The momentum density P^k = (∂₀φ)(∂^k φ) + Σⱼ(∂₀ψⱼ)(∂^k ψⱼ) (eq. 5.2)
    should be evaluated for a specific scenario

---

## Stretch Goals (Would Strengthen the Framework)

- [x] **Derive the Koide formula** from phase harmonic geometry
  - Proved: Z₃ phase parametrization √mᵢ = μ(1 + δ cos(θ₀ + 2πi/3)) gives Q = (1+δ²/2)/3
  - Q = 2/3 ⟺ δ = √2 (exact mathematical result)
  - Geometric interpretation: √m vector at 45° to democratic direction (1,1,1)
  - Lepton fit: μ = 17.72 MeV^{1/2}, θ₀ ≈ 2/9 (Brannen)
  - Quark extension: (c,b,t) near-Koide Q = 0.669, signed (s,c,b) ≈ 0.675
  - Physical argument: δ = √2 from equal partition of symmetric/breaking energy
  - See [koide_derivation.md](docs/research/koide_derivation.md)

- [x] **Derive the fine-structure constant** from phase impedance matching
  - Exact identity: α = Z₀/(2R_K) = (EM impedance)/(2 × quantum impedance) = 1/137.036
  - PDTP interpretation: coupling efficiency between EM and matter-wave phase media
  - Impedance mismatch explains why α is small: R_K/Z₀ ≈ 69 (media stiffness ratio)
  - Length scale cascade: r_e = αλ̄_C = α²a₀ as standing-wave harmonics
  - Running of α: energy-dependent quantum impedance from vacuum polarization
  - Wyler's formula discussed (α_W⁻¹ = 137.036..., 0.6 ppm, but no solid derivation)
  - **Honest status:** structural interpretation achieved; numerical derivation remains open
  - See [fine_structure_derivation.md](docs/research/fine_structure_derivation.md)

- [x] **Simulation of emergent GR**
  - N-body simulation of phase-coupled oscillators → 5 independent tests
  - Smooth curvature from N=10 to N=1000 discrete oscillators (< 0.5% error)
  - Quantitative match to Newtonian predictions: 1/r potential (1.35% error),
    1/d force law (exponent −0.984), Kuramoto synchronization (R = 1.0000),
    weak-field linearization (machine-precision match)
  - See [emergent_gr_results.md](docs/research/emergent_gr_results.md)
  - Simulation: [emergent_gr_simulation.py](simulations/emergent_gr_simulation.py)

---

## Status

```
Mathematical formalization complete (three parts + follow-up).

Part 1: Lagrangian, field equations, conservation laws, stability,
Newtonian recovery, order-of-magnitude predictions.

Part 2: Quantum φ definition (superfluid vacuum), post-Newtonian corrections,
Standard Model integration, experimental test design.

Part 3: GW polarization (emergent tensor + breathing mode), PPN parameters
(γ=1, β=1), vacuum condensate constraints (GFT connection), photon coupling
(indirect via acoustic metric, factor-of-2 recovered).

Part 3b (follow-up): κ=−2 derived (PG representation), breathing mode
amplitude quantified (<10⁻⁵), tetrad structure analyzed (extension needed),
G_EM resolved (removed — trace problem). Field equation simplified.

All "Remaining Questions" from Part 3 addressed.
Part 4: Koide formula derived from Z₃ phase harmonic geometry. Proved
Q = 2/3 ⟺ δ = √2. Extended to quarks: (c,b,t) near-Koide. Physical
origin of δ = √2 from equal energy partition. θ₀ = 2/9 remains empirical.

Koide stretch goal completed.
Part 5: Fine-structure constant analyzed as impedance ratio. α = Z₀/(2R_K)
exact identity. Impedance mismatch interpretation, length scale hierarchy,
running coupling, Wyler's formula. Numerical value NOT derived — requires
condensate microscopic structure (open in SVT itself).

Fine-structure constant stretch goal completed (structural analysis).
Part 6: Emergent GR simulation. Five independent numerical tests: 1/r
potential recovery (Thomas algorithm, 1.35% err), smooth curvature emergence
from N=10–1000 discrete oscillators (0.44% err), Kuramoto synchronization
(R: 0.329→1.000), two-body 1/d force law (exponent −0.984), weak-field
linearization validation (machine-precision match to |1−sin(x)/x|).
Runtime ~10s. All tests PASS.

Simulation stretch goal completed.
Part 7: Free photon gravity analysis. Quantitative assessment: solar
deficit ~10⁻²¹/s, thermal suppression ~10⁻¹⁴, trace anomaly ~0.04%.
Key insight: radiation dominates only when tightly coupled (pre-
recombination), and free-streams only when subdominant. Problem is
cosmological, not astrophysical. Plasma frequency effective mass as
possible pre-recombination coupling mechanism.

Free photon analysis completed.
Part 8: Radiation-era cosmology. Matter-era Friedmann equation derived
from condensate dynamics (Euler + continuity). Tight-coupling argument
resolves photon contribution (effective mass). Genuine gap: decoupled
neutrino kinetic energy at BBN (41% of ρ_total, 23% error in H).
Requires acoustic metric tensor channel for full resolution.

Radiation-era cosmology analysis completed.
Part 9: Newton's constant G derivation. Dimensional analysis gives
G = 𝒞 c^(5/2)/√(ℏρ₀), exact when ρ₀ = ρ_Planck. Coupling constants
gᵢ shown to be geometric (~4πRᵢ), not free parameters. Reduces N+2
apparent parameters to 1 unknown (𝒞). Energy-cost circularity resolved.
Full derivation requires condensate microphysics (deepest open problem).

G derivation completed (partial — one free parameter remains).
Part 10: Strong-field equivalence principle. Phase difference = compactness
parameter: δψ = GM/(Rc²). Nonlinearity sin(δψ)/δψ is 0.7% for NS, 4.1%
at BH horizon. Strong-field Nordtvedt η ~ Ξ²/6. Binding energy gravitates
correctly to O(Ξ). Acoustic horizon at r = 2GM/c² (exact). Tension with
double pulsar Ṗ_b at ~1% level — critical open question.

Strong-field EP analysis completed.
Open: momentum balance,
structural gaps (tetrad extension),
and genuinely open problems (condensate microscopy, neutrino energy).
```

---

End of TODO
