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

- [ ] **Quantum description of spacetime phase field (phi)**
  - phi is currently undefined in standard physics
  - Framework implicitly requires spacetime to have a quantum phase structure
  - Defining phi rigorously is the biggest foundational challenge
  - Must be compatible with Lorentz invariance

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
- [ ] Be distinguishable from existing GR/QFT predictions — requires
  post-Newtonian calculation

---

## Remaining Work

- [ ] **Post-Newtonian corrections**
  - Perihelion precession of Mercury
  - Gravitational lensing angles
  - Gravitational wave frequencies and amplitudes
  - Frame-dragging (Lense-Thirring effect)
  - Shapiro time delay
  - These require going beyond the linearized (weak-field) approximation

- [ ] **Quantum description of spacetime phase field (phi)**
  - The biggest open foundational challenge
  - Must define what φ is in terms of standard quantum field theory
  - Or must argue why φ is a new degree of freedom not in existing QFT

- [ ] **EM and nuclear force integration**
  - Current Lagrangian only describes gravitational coupling
  - EM, strong, and weak interactions need to be incorporated
  - May require additional coupling terms or field structure

- [ ] **Experimental test design**
  - Specific BEC experiment protocol
  - Required precision and coherence levels
  - Control experiments (incoherent vs coherent)

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
Mathematical formalization in progress.
Core derivations complete: Lagrangian, field equations, conservation laws,
stability, Newtonian recovery, order-of-magnitude predictions.
Remaining: post-Newtonian corrections, quantum φ definition, force integration.
```

---

End of TODO
