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

## The Wave Itself — Phase Sign Revealed (Image 2)

The image above shows **|ψ|²** — the probability density, always positive.
This second image shows something different: **ψ itself**, with a signed
color scale (− to +). This reveals the actual phase of the wave.

![Hydrogen Wave Function — phase signed](../../assets/images/hydrogen%20wave%20function%200_kGoy-0UmjweaqEZB.png)

The color scale runs from **dark (negative)** through white (zero) to
**bright (positive)**. White boundaries — where the color crosses zero — are
the **nodal surfaces** where ψ = 0.

### Standard QM: What the Signs Mean

In standard quantum mechanics, the sign (phase) of ψ at any single point has
no direct physical meaning — only **relative** signs between regions matter:

- Two adjacent lobes of **opposite sign** will **interfere destructively** when
  mixed together (e.g., by a perturbation or bond formation in chemistry)
- Two lobes of the **same sign** interfere constructively (bonding in molecular
  orbitals)
- The absolute phase is unobservable — rotating all phases by the same amount
  changes nothing

The patterns visible in Image 2 match Image 1 exactly: the same (n, l, m)
structure, same nodal surfaces. Image 2 just shows the signed amplitude rather
than its square. For example:

- **(2, 1, 0)**: two lobes, one bright (+), one dark (−) — a p-orbital with
  one nodal plane separating opposite-phase halves
- **(3, 2, 0)**: cloverleaf with alternating +/−/+/− lobes around the nodal
  planes of the d-orbital
- **(4, 0, 0)**: concentric rings — the sign alternates between each radial
  shell, with nodal spheres at each sign change

**Source:** [Hydrogen atom — Wikipedia](https://en.wikipedia.org/wiki/Hydrogen_atom)

### PDTP: The Phase Signs Are Physically Real

This image is the clearest visual evidence for the PDTP interpretation.

In standard QM, the +/− signs are "just math" — the global phase is arbitrary.
PDTP takes the opposite position: **the signed wavefunction ψ is the actual
physical displacement of the phase medium (the condensate)**. The signs are
not abstract; they are literal wave crests (+) and wave troughs (−).

| Feature in Image 2 | Standard QM | PDTP |
|---------------------|-------------|------|
| Bright (+ regions) | Positive wave amplitude — unobservable alone | Condensate displaced in positive phase direction — physically real crest |
| Dark (− regions) | Negative wave amplitude — unobservable alone | Condensate displaced in negative phase direction — physically real trough |
| White nodal surfaces | ψ = 0, purely mathematical boundary | Phase medium at rest — true physical node, like a node in a standing sound wave |
| Alternating lobes | Sign convention, arbitrary overall | Opposite oscillation phases — medium pushes out on one side while pulling in on the other |

The analogy: a vibrating drumhead has real physical regions that move **up**
(crest) and regions that move **down** (trough), separated by nodal lines that
don't move. Image 2 shows the hydrogen orbital as exactly this — a 3D standing
wave with real spatial phase structure, not a probability cloud.

**Why this matters for PDTP:**

The d-orbital (l = 2) shows four lobes in alternating + and − pairs. In standard
QM, these signs are mathematical and their absolute values are unphysical. In
PDTP, the electron is a 3D standing wave mode of the phase medium, and these
four lobes represent a real spatial oscillation pattern — two regions of the
medium compressed in one phase direction, two compressed in the opposite. The
whole structure oscillates coherently at the electron's de Broglie frequency.

**PDTP Original:** The signed wavefunction ψ in PDTP is interpreted as the
physical phase displacement of the condensate medium, making the orbital phase
structure directly observable in principle — not merely a calculation artifact.

---

## Summary

| Aspect | Standard QM | PDTP |
|--------|-------------|------|
| What is ψ? | Probability amplitude (abstract) | Physical wave in phase medium (real) |
| What are orbitals? | Probability distributions | Standing wave nodal patterns |
| Why quantized? | Boundary conditions on ψ | Boundary conditions on standing waves |
| What is the electron? | Point particle (undefined between measurements) | Extended standing wave |
| What is measurement? | Mysterious "collapse" | Phase-locking to macroscopic detector |
| What do the +/− signs in ψ mean? | Relative interference only — no absolute meaning | Physical wave crests (+) and troughs (−) of the condensate |
| What are the nodal surfaces? | Where ψ = 0 — abstract boundary | Physical rest points of the oscillating medium |

Both frameworks produce identical predictions. PDTP provides a concrete
physical picture: the hydrogen wavefunction images are not abstract math —
they are photographs of a real wave in a real medium.

The signed image (Image 2) is the most direct view of this wave structure.
Where standard QM sees a mathematical sign with no individual meaning, PDTP
sees the actual shape of the condensate's oscillation — crests, troughs,
and the nodal surfaces between them.

---

End of Document
