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

- [ ] **Derive κ = −2 from first principles**
  - The acoustic metric PPN result γ = 1 requires the condensate equation-of-state
    parameter κ = δρ/(ρ₀ U) = −2
  - Currently assumed; should be derived from the condensate dynamics

- [ ] **Condensate tetrad structure**
  - Tensor GW modes require the condensate to have tetrad (vierbein) degrees of freedom
  - Assumed by analogy with He-3 (Volovik); not derived from PDTP Lagrangian

- [ ] **Breathing mode amplitude relative to tensor**
  - PDTP predicts a breathing mode; what is its amplitude relative to tensor modes?
  - Needed for quantitative LIGO/Virgo/KAGRA comparison

- [ ] **EM coupling constant G_EM in equation (4.3)**
  - The photon source term □φ = ... + G_EM · T₀₀^EM has undetermined coefficient
  - Should be fixed by requiring equivalence principle (E = mc²)

---

## Stretch Goals (Would Strengthen the Framework)

- [ ] **Derive the Koide formula** from phase harmonic geometry
  - Show that Q = 2/3 follows necessarily from three-mode standing waves in 3D
  - Predict quark mass relations using the same mechanism

- [ ] **Derive the fine-structure constant** from phase impedance matching
  - Calculate 1/137 from the impedance ratio of matter-wave and EM phase media

- [ ] **Simulation of emergent GR**
  - N-body simulation of phase-coupled oscillators
  - Show that smooth curvature emerges from statistical averaging
  - Compare to actual GR predictions quantitatively

---

## Status

```
Mathematical formalization complete (three parts).

Part 1: Lagrangian, field equations, conservation laws, stability,
Newtonian recovery, order-of-magnitude predictions.

Part 2: Quantum φ definition (superfluid vacuum), post-Newtonian corrections,
Standard Model integration, experimental test design.

Part 3: GW polarization (emergent tensor + breathing mode), PPN parameters
(γ=1, β=1), vacuum condensate constraints (GFT connection), photon coupling
(indirect via acoustic metric, factor-of-2 recovered).

All four "Hard Open Problems" addressed. Remaining: stretch goals
(Koide, fine-structure constant, N-body simulation) and genuinely
open questions (condensate microscopy, κ=−2 derivation).
```

---

End of TODO
