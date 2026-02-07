# TODO: Mathematical Formalization Roadmap

This file tracks the critical mathematical gaps that must be resolved for PDTP
to move from conceptual framework to testable physical theory.

See [math_status.md](docs/research/math_status.md) and
[quantum_gravity_deep_dive.md](docs/research/quantum_gravity_deep_dive.md) for
full context.

---

## Critical Gaps (Must Solve)

- [ ] **Field equation for coupling parameter alpha**
  - No governing equation exists for alpha(x,t)
  - Required form: `Box(alpha) = f(psi, g_mu_nu, nabla psi)`
  - Without this, alpha remains a heuristic, not a calculable quantity
  - This is the single most important missing piece

- [ ] **Energy cost of phase control**
  - Decoupling must require energy — how much?
  - Candidate: `E_coherence proportional to integral |nabla alpha|^2 dV`
  - If energy scales too high, PDTP is not physically realizable
  - Determines whether the framework describes possible or impossible physics

- [ ] **Stability analysis**
  - Phase-lock systems can destabilize
  - Need Lyapunov function V where dV/dt < 0
  - Must prove the system returns to equilibrium after perturbations
  - No stability analysis currently exists

- [ ] **Conservation law compliance**
  - Must prove energy conservation holds under variable alpha
  - Must prove momentum conservation holds
  - Must prove causality is preserved (no FTL information transfer)
  - Currently assumed but not mathematically demonstrated

- [ ] **Quantum description of spacetime phase field (phi)**
  - phi is currently undefined in standard physics
  - Framework implicitly requires spacetime to have a quantum phase structure
  - Defining phi rigorously is the biggest foundational challenge
  - Must be compatible with Lorentz invariance

- [ ] **Quantitative GR recovery**
  - Must reproduce all GR predictions numerically, not just qualitatively
  - Perihelion precession of Mercury
  - Gravitational lensing angles
  - Gravitational wave frequencies and amplitudes
  - Frame-dragging (Lense-Thirring effect)
  - Shapiro time delay

- [ ] **Numerical experimental predictions**
  - How much should alpha deviate in a BEC of N atoms?
  - At what coherence threshold do gravitational anomalies appear?
  - What is the predicted phase-noise-to-weight-change ratio?
  - Without specific numbers, the framework cannot be tested or falsified

---

## Structural Requirements (Any Future Math Must Satisfy)

- [ ] Preserve Lorentz invariance
- [ ] Preserve energy-momentum conservation
- [ ] Be derivable from a consistent Lagrangian
- [ ] Be experimentally testable
- [ ] Be distinguishable from existing GR/QFT predictions

---

## Stretch Goals (Would Strengthen the Framework)

- [ ] **Derive the Koide formula** from phase harmonic geometry
  - Show that Q = 2/3 follows necessarily from three-mode standing waves in 3D
  - Predict quark mass relations using the same mechanism

- [ ] **Derive the fine-structure constant** from phase impedance matching
  - Calculate 1/137 from the impedance ratio of matter-wave and EM phase media

- [ ] **Connect to Kuramoto model** formally
  - Show that the PDTP coupling equations are a field-theoretic extension of
    the Kuramoto coupled oscillator model
  - Import stability results from Kuramoto literature

- [ ] **Simulation of emergent GR**
  - N-body simulation of phase-coupled oscillators
  - Show that smooth curvature emerges from statistical averaging
  - Compare to actual GR predictions quantitatively

---

## Status

```
PDTP is mathematically inspired but mathematically incomplete.
It is internally consistent but externally unverified.
It proposes extensions beyond established physics.
```

Tomorrow: begin the math.

---

End of TODO
