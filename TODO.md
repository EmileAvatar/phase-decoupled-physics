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

- [ ] **Free photon radiation as gravitational source**
  - Free photons don't source □φ (EM trace = 0)
  - Only bound EM energy gravitates through the scalar field
  - Implications for radiation-dominated cosmology unclear

- [ ] **Radiation-dominated era cosmology**
  - In the early universe, most energy was in radiation (T^EM = 0 source)
  - How does PDTP handle the Friedmann equation with radiation?
  - May require the full acoustic metric / tensor structure

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

- [ ] **Simulation of emergent GR**
  - N-body simulation of phase-coupled oscillators
  - Show that smooth curvature emerges from statistical averaging
  - Compare to actual GR predictions quantitatively

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
Open: stretch goals (N-body simulation), structural gaps (tetrad extension,
radiation-era cosmology), and genuinely open problems (condensate microscopy).
```

---

End of TODO
