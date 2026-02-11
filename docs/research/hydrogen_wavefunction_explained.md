# Hydrogen Wavefunction — Existing Physics and PDTP Interpretation

This document explains the hydrogen atom wavefunction visualization, first
using standard quantum mechanics, then through the PDTP phase framework lens.

![Hydrogen Wavefunction](../../assets/images/Hydrogen%20wavefunction%20existing%20physics%20.jpeg)

---

## Existing Physics (Standard Quantum Mechanics)

The image shows the hydrogen atom electron wavefunctions — specifically the
probability density |ψ|² — for quantum numbers (n, l, m) up to n = 4.

The hydrogen wavefunction is an exact solution to the Schrödinger equation for
a single electron in the Coulomb potential of a proton:

```
ψ_{nlm}(r, θ, φ) = R_nl(r) · Y_l^m(θ, φ)
```

where R_nl is the radial part (Laguerre polynomials) and Y_l^m is the angular
part (spherical harmonics).

**Source:** [Hydrogen atom — Wikipedia](https://en.wikipedia.org/wiki/Hydrogen_atom)

### The Three Quantum Numbers

| Quantum # | Name | Controls | Values |
|-----------|------|----------|--------|
| **n** (horizontal axis →) | Principal | Energy level, E = −13.6/n² eV | 1, 2, 3, 4... |
| **l** (vertical axis ↓) | Azimuthal | Angular momentum magnitude, L = √(l(l+1))ℏ | 0 to n−1 |
| **m** (vertical within l) | Magnetic | Angular momentum z-projection, L_z = mℏ | −l to +l |

### What the Image Shows

- **Color = |ψ|²** — the probability density of finding the electron at each
  point (bright = high probability, dark = low probability)
- **(1,0,0)** — the ground state: a spherically symmetric cloud (1s orbital)
- **Higher n** — larger, more diffuse orbitals with more radial nodes (dark
  rings where |ψ|² = 0)
- **Higher l** — more angular structure (lobes):
  - l = 0: spherical (s-orbitals)
  - l = 1: dumbbell shapes (p-orbitals)
  - l = 2: cloverleaf shapes (d-orbitals)
  - l = 3: complex multi-lobed shapes (f-orbitals)
- **Different m** — rotates the angular pattern around the z-axis

The right side of the image shows artistic 3D renders of some of these
orbitals, illustrating their spatial structure.

### Why Only These Patterns Exist

The shapes arise entirely from the **boundary conditions** of the Schrödinger
equation in a central (Coulomb) potential. The electron's allowed states are
quantized because only certain standing wave patterns "fit" in the potential
well:

- The wavefunction must be normalizable (→ quantized n)
- It must be single-valued on the sphere (→ integer l and m)
- It must vanish at infinity (→ exponential decay envelope)

These constraints restrict the electron to a discrete set of allowed states,
each with a specific energy E_n = −13.6/n² eV.

---

## PDTP Framework Interpretation

In the PDTP framework, the electron is not a point particle existing in a
probability cloud — it is a **standing wave** in the phase medium, phase-locked
to the proton's wave pattern via electromagnetic coupling.

### The Orbital Shapes Are Standing Wave Nodal Patterns

Each (n, l, m) state is literally what the image shows: a **3D standing wave**
in the EM phase field surrounding the proton. PDTP takes the wavefunction at
face value — |ψ|² is not just a "probability of finding a particle," it **is**
the wave intensity of a physical oscillation in the phase medium.

| Standard QM | PDTP Reframing |
|-------------|----------------|
| ψ is a probability amplitude | ψ is the physical wave amplitude in the EM phase medium |
| \|ψ\|² = probability density | \|ψ\|² = energy density of the standing wave |
| Electron "found" somewhere when measured | Measurement forces the extended wave to phase-lock to a single spatial node |
| Quantized energy levels | Only certain standing wave patterns satisfy the boundary conditions of the phase medium |
| Orbital angular momentum (l) | Number of angular nodal planes in the standing wave |
| Magnetic quantum number (m) | Orientation of the nodal pattern relative to an external phase reference (magnetic field) |

### Why Only Certain Patterns Exist

The quantum numbers arise from **boundary conditions on standing waves in 3D**:

- **n** (radial) — how many wavelengths fit between the proton and the
  exponential decay envelope. Higher n = higher harmonic = higher energy. The
  dark rings in the image are **radial nodes** — zero-crossings of the wave.
- **l** (angular) — how many angular nodal surfaces the wave pattern has. This
  is exactly like a vibrating drum head: l = 0 is the fundamental (dome shape),
  l = 1 has one nodal line (two lobes), l = 2 has two nodal lines (four lobes),
  etc.
- **m** (orientation) — which direction the angular pattern points, i.e., the
  wave's phase relationship with an external reference direction.

### Connection to the Koide Formula

This image directly illustrates the same physics behind the Koide formula
(see [koide_derivation.md](koide_derivation.md)): **standing waves in 3D
naturally organize into discrete modes indexed by integers**.

The three charged lepton generations (e, μ, τ) are analogous to three harmonic
modes — but of the *electron itself* as a standing wave pattern, not the
electron's orbital around a nucleus. The hydrogen orbitals show how rich the
mode structure becomes in 3D: one quantum number is not enough — you need three
(n, l, m) to fully specify the pattern. Similarly, the three lepton generations
may correspond to different mode indices of the fundamental charged lepton
standing wave.

### What's Different from Standard QM

Standard QM says: "We don't know what the electron *is* between measurements;
ψ is just a calculation tool."

PDTP says: "The electron **is** this wave pattern. It is a real, physical
standing wave in the phase medium. What you see in this image is what actually
exists."

The math is identical — same Schrödinger equation, same solutions, same
predictions. The difference is **ontological**: PDTP commits to the wave being
physically real, not just a mathematical convenience.

---

## Summary

| Aspect | Standard QM | PDTP |
|--------|-------------|------|
| What is ψ? | Probability amplitude (abstract) | Physical wave in phase medium (real) |
| What are orbitals? | Probability distributions | Standing wave nodal patterns |
| Why quantized? | Boundary conditions on ψ | Boundary conditions on standing waves |
| What is the electron? | Point particle (undefined between measurements) | Extended standing wave |
| What is measurement? | Mysterious "collapse" | Phase-locking to macroscopic detector |

Both frameworks produce identical predictions. PDTP provides a concrete
physical picture: the hydrogen wavefunction images are not abstract math —
they are photographs of reality.

---

End of Document
