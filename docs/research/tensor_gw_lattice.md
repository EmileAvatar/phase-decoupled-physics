# Part 28: Tensor Gravitational Wave Modes from the Oscillator Lattice

## Status
**PDTP Original** — Bottom-up derivation of tensor GW modes from condensate lattice.

**Conceptual framework — not experimentally validated.**

---

## 1. The Problem in Plain English

Part 21 built a model of spacetime as a lattice of coupled phase oscillators.
That model successfully derived:
- The speed of light: c² = κ/ρ (stiffness divided by inertia)
- Newton's constant: G = c²/(4πκ) (gravity = inverse stiffness)
- Inertial mass: M = energy of phase distortion

But it has **one degree of freedom per site** — a single phase angle θᵢ.
One number per point gives one type of wave: **longitudinal** (compression).
That's the breathing mode — the ring of test particles just gets bigger
and smaller, uniformly.

**The problem:** LIGO observes gravitational waves with **tensor**
polarizations — the ring stretches in one direction while squeezing in the
perpendicular direction. This requires **transverse** waves, which need
**more than one degree of freedom per site.**

Part 27 identified the fix: the same lattice, but with **three displacement
components** per site (one for each spatial direction) instead of one phase angle.
A lattice with vector displacements supports both compression AND shear waves.
The shear waves have two independent polarizations — and those are exactly
the tensor + and × modes that LIGO sees.

**This document derives that result step by step.**

**Goal:** Start from the Part 21 lattice, generalize it from scalar to vector,
compute all wave modes, and show that the two transverse (shear) modes are
the tensor gravitational waves. Then check whether they propagate at the
speed of light.

---

## 2. From Scalar Phase to Vector Displacement

### 2.1 The Part 21 Scalar Model (Recap)

The oscillator lattice from Part 21 (efv_microphysics.md §4) has one scalar
phase angle θᵢ at each site:

```
H = Σᵢ (I/2)(∂ₜθᵢ)² + (K/2) Σ⟨i,j⟩ (θᵢ − θⱼ)²        (Eq. 21.4.3)
```

**Source:** [Classical XY model](https://en.wikipedia.org/wiki/Classical_XY_model)
(standard lattice model in statistical mechanics)

This gives one wave type — longitudinal sound — with speed c² = κ/ρ.

### 2.2 Why Vector?

The condensate lives in three-dimensional space. When a lattice site is
disturbed, the disturbance can point in **any** spatial direction — not just
along the line connecting the sites.

Think of it this way:
- The scalar θᵢ captures only the "push-pull" (compression) along bond directions
- A site can also be displaced **sideways** — perpendicular to the bond
- Sideways displacements are **shear** deformations
- Shear waves have transverse polarization — exactly what LIGO needs

The physical motivation comes directly from Part 12 (tetrad_extension.md):
the full condensate order parameter has four phase fields φᵃ (a = 0,1,2,3),
not just one. At the lattice level, the three spatial components of the
tetrad perturbation correspond to three displacement components per site.

### 2.3 The Vector Model

Replace the scalar phase θᵢ with a three-component displacement vector
**u**ᵢ = (uˣᵢ, uʸᵢ, uᶻᵢ):

```
Scalar (Part 21):   θᵢ       → one number per site → 1 wave branch
Vector (Part 28):   uᵢ = (uˣ, uʸ, uᶻ)  → three numbers per site → 3 wave branches
```

The scalar model is the **longitudinal projection** of the vector model.
If the wave travels in the z-direction, then θ corresponds to uᶻ (displacement
along the wave direction). The vector model adds uˣ and uʸ (displacements
perpendicular to the wave direction) — these are the transverse modes.

**PDTP Original:** The Part 21 scalar lattice is the longitudinal sector of
a vector lattice. Generalizing from one to three degrees of freedom per site
unlocks the two missing transverse (tensor) branches without changing the
lattice structure or coupling constant K.

---

## 3. The Vector Lattice Hamiltonian

### 3.1 Central-Force Model

The simplest vector generalization replaces the scalar coupling (θᵢ − θⱼ)²
with the vector coupling |**u**ᵢ − **u**ⱼ|²:

```
H = Σᵢ (m/2)|∂ₜuᵢ|² + (K/2) Σ⟨i,j⟩ |uᵢ − uⱼ|²             (Eq. 28.1)
```

where:
- m = I = moment of inertia per site (same as Part 21)
- K = coupling stiffness between neighbors (same K as Part 21)
- |**u**ᵢ − **u**ⱼ|² = (uˣᵢ − uˣⱼ)² + (uʸᵢ − uʸⱼ)² + (uᶻᵢ − uᶻⱼ)²
- The sum ⟨i,j⟩ runs over nearest-neighbor pairs on a simple cubic lattice

**Source:** [Phonon](https://en.wikipedia.org/wiki/Phonon) (standard treatment
of lattice vibrations in 3D)

This is called a **central-force** model because the interaction |**u**ᵢ − **u**ⱼ|²
depends only on the distance between sites — it pulls along the line
connecting them, like a spring.

### 3.2 Equation of Motion

The force on site i in direction α (= x, y, or z) is:

```
m ∂²uᵅᵢ/∂t² = −K Σⱼ∈nn(i) (uᵅᵢ − uᵅⱼ)                     (Eq. 28.2)
```

**Key observation:** For central forces, the three components (x, y, z) decouple.
Each component α obeys the **same** equation as the scalar θᵢ from Part 21.
This means the vector model with central forces is literally **three independent
copies** of the scalar model.

This will be important — it means central forces alone cannot distinguish
between longitudinal and transverse modes.

### 3.3 Comparison with Part 21

Setting α = z for a wave traveling in the z-direction:

```
m ∂²uᶻᵢ/∂t² = −K Σⱼ∈nn(i) (uᶻᵢ − uᶻⱼ)
```

This is identical to Part 21's equation for θᵢ. The identification is
uᶻ ↔ θ (longitudinal displacement = phase). The transverse components
uˣ and uʸ are the new degrees of freedom — they were absent in the scalar model.

---

## 4. Continuum Limit — The Elastic Wave Equation

### 4.1 Taylor Expansion (Same Method as Part 21)

For wavelengths much larger than the lattice spacing a, the displacement
field becomes smooth: **u**ᵢ → **u**(x). Expand the neighbor's displacement
in a Taylor series:

```
uᵅⱼ = uᵅᵢ + aᵝ(∂uᵅ/∂xᵝ) + ½ aᵝ aᵧ(∂²uᵅ/∂xᵝ∂xᵧ) + ...    (Eq. 28.3)
```

where **a** is the lattice vector from site i to neighbor j, and we sum
over repeated Greek indices (Einstein convention).

**Source:** [Taylor series](https://en.wikipedia.org/wiki/Taylor_series)
(standard continuum limit procedure)

### 4.2 Summing Over Nearest Neighbors

On a simple cubic lattice, site i has 6 neighbors at positions:

```
(±a, 0, 0),  (0, ±a, 0),  (0, 0, ±a)
```

For each neighbor pair (e.g., j at +a and j' at −a in the x-direction):

```
(uᵅᵢ − uᵅⱼ) + (uᵅᵢ − uᵅⱼ') = −a² ∂²uᵅ/∂x²               (Eq. 28.4)
```

The first-order terms cancel by symmetry. Summing over all 3 axis pairs:

```
Σⱼ∈nn(i) (uᵅᵢ − uᵅⱼ) = −a² ∇²uᵅ                           (Eq. 28.5)
```

### 4.3 The Naive Continuum Equation

Substituting (28.5) into the equation of motion (28.2):

```
m ∂²uᵅ/∂t² = Ka² ∇²uᵅ                                      (Eq. 28.6)
```

Dividing by the volume per site a³ to get densities:

```
ρ ∂²uᵅ/∂t² = (K/a) ∇²uᵅ                                    (Eq. 28.7)
```

where ρ = m/a³ is the mass density.

This is a simple wave equation for each component, with wave speed:

```
c² = K/(aρ) = Ka²/m                                          (Eq. 28.8)
```

**But this is wrong.** It says all three components have the same speed —
no distinction between longitudinal and transverse. The problem is that
for the central-force potential |**u**ᵢ − **u**ⱼ|², the Taylor expansion
at second order gives only the ∇²uᵅ term.

### 4.4 The Correct Expansion — Cross Terms Matter

The issue is that |**u**ᵢ − **u**ⱼ|² is NOT the same as Σᵅ(uᵅᵢ − uᵅⱼ)²
when expanded to second order in gradients for a **specific bond direction**.

For a bond along the x-direction (neighbor at j = i + aê_x):

```
|uᵢ − uⱼ|² = Σᵅ (uᵅᵢ − uᵅⱼ)²
            = Σᵅ [−a ∂uᵅ/∂x − ½a² ∂²uᵅ/∂x² − ...]²
            ≈ a² Σᵅ (∂uᵅ/∂x)²                              (Eq. 28.9)
```

to leading order. When we sum over **all 6 neighbors** (bonds along ±x, ±y, ±z)
and convert to a continuum integral:

```
V = (K/2) Σ⟨i,j⟩ |uᵢ − uⱼ|²

  → ∫ d³x (K/2a³) · a² [Σᵅ(∂uᵅ/∂x)² + Σᵅ(∂uᵅ/∂y)² + Σᵅ(∂uᵅ/∂z)²]

  = ∫ d³x (K/2a) Σᵅ,ᵝ (∂uᵅ/∂xᵝ)²                          (Eq. 28.10)
```

The factor counting: each bond contributes once to the ⟨i,j⟩ sum, and each
site has z/2 = 3 bonds (for coordination number z = 6). The 3 bonds times
the a² from the gradient squared, divided by a³ per site, gives K/a per
unit volume.

**Source:** [Linear elasticity](https://en.wikipedia.org/wiki/Linear_elasticity)
(standard derivation of elastic energy from discrete lattice)

### 4.5 Identifying the Elastic Constants

The elastic energy density for an isotropic solid is:

```
ε = ½ Σᵅ,ᵝ Cᵅᵝᵧᵟ eᵅᵝ eᵧᵟ                                  (Eq. 28.11)
```

where eᵅᵝ = ½(∂uᵅ/∂xᵝ + ∂uᵝ/∂xᵅ) is the strain tensor and Cᵅᵝᵧᵟ is
the elastic stiffness tensor.

**Source:** [Lamé parameters](https://en.wikipedia.org/wiki/Lam%C3%A9_parameters)

For an isotropic material, the stiffness tensor has only two independent
parameters — the Lamé parameters λ and μ:

```
Cᵅᵝᵧᵟ = λ δᵅᵝ δᵧᵟ + μ (δᵅᵧ δᵝᵟ + δᵅᵟ δᵝᵧ)                (Eq. 28.12)
```

The elastic energy becomes:

```
ε = ½ λ (∇·u)² + μ Σᵅ,ᵝ eᵅᵝ²
  = ½ λ (∇·u)² + ¼ μ Σᵅ,ᵝ (∂uᵅ/∂xᵝ + ∂uᵝ/∂xᵅ)²          (Eq. 28.13)
```

### 4.6 The Lattice Result

From our lattice (Eq. 28.10), the elastic energy density is:

```
ε_lattice = (K/2a) Σᵅ,ᵝ (∂uᵅ/∂xᵝ)²                        (Eq. 28.14)
```

We can split each gradient into symmetric and antisymmetric parts:

```
∂uᵅ/∂xᵝ = eᵅᵝ + ωᵅᵝ
```

where eᵅᵝ = ½(∂uᵅ/∂xᵝ + ∂uᵝ/∂xᵅ) is strain (symmetric) and
ωᵅᵝ = ½(∂uᵅ/∂xᵝ − ∂uᵝ/∂xᵅ) is rotation (antisymmetric).

Then:

```
Σᵅ,ᵝ (∂uᵅ/∂xᵝ)² = Σᵅ,ᵝ eᵅᵝ² + Σᵅ,ᵝ ωᵅᵝ²                (Eq. 28.15)
```

(Cross terms vanish by symmetry.) The rotation part ωᵅᵝ corresponds to
rigid rotations that cost no elastic energy in the continuum limit. For
proper elastic theory, only the strain part matters.

Keeping only the strain part and comparing with (28.13):

```
(K/2a) Σᵅ,ᵝ eᵅᵝ² = ½ λ (Σᵅ eᵅᵅ)² + μ Σᵅ,ᵝ eᵅᵝ²           (Eq. 28.16)
```

**PDTP Original:** Expanding the left side and matching term by term with
the right side, the central-force cubic lattice gives:

```
┌─────────────────────────────────────────────────┐
│  λ = μ = K/a                                     │
│                                                   │
│  This is the Cauchy relation for central forces   │
└─────────────────────────────────────────────────┘
```

**Source:** Born, M. & Huang, K. (1954), *Dynamical Theory of Crystal Lattices*,
Oxford University Press. The Cauchy relation λ = μ holds for any lattice with
purely central (pairwise) interactions where every atom is a centre of symmetry.

### 4.7 Wave Speeds

The equation of motion for the elastic continuum (Navier-Cauchy equation) is:

```
ρ ∂²u/∂t² = (λ + μ) ∇(∇·u) + μ ∇²u                        (Eq. 28.17)
```

**Source:** [Linear elasticity](https://en.wikipedia.org/wiki/Linear_elasticity)
(Navier-Cauchy equation of motion)

Using the Helmholtz decomposition **u** = ∇Φ + ∇×**A**, where Φ is a scalar
potential (longitudinal part) and **A** is a vector potential (transverse part):

**Source:** [Helmholtz decomposition](https://en.wikipedia.org/wiki/Helmholtz_decomposition)

**Longitudinal waves** (∇·u ≠ 0, ∇×u = 0):

```
ρ ∂²Φ/∂t² = (λ + 2μ) ∇²Φ

→  c²_L = (λ + 2μ)/ρ                                        (Eq. 28.18)
```

**Transverse waves** (∇·u = 0, ∇×u ≠ 0):

```
ρ ∂²A/∂t² = μ ∇²A

→  c²_T = μ/ρ                                               (Eq. 28.19)
```

### 4.8 The Key Result: Wave Speeds for the PDTP Lattice

For the central-force cubic lattice with λ = μ = K/a:

```
c²_L = (λ + 2μ)/ρ = 3μ/ρ = 3K/(aρ) = 3Ka²/m

c²_T = μ/ρ = K/(aρ) = Ka²/m
```

From Part 21 (efv_microphysics.md Eq. 4.16), the speed of light was identified as:

```
c² = 3Ka²/I = 3Ka²/m    (using I = m for the phase oscillator)
```

Therefore:

```
┌────────────────────────────────────────────────────────────┐
│  c²_L = c²            (longitudinal waves travel at c)     │
│  c²_T = c²/3          (transverse waves travel at c/√3)    │
│                                                             │
│  c_T = c/√3 ≈ 0.577 c                                      │
└────────────────────────────────────────────────────────────┘
```

**PDTP Original:** The central-force oscillator lattice from Part 21 gives
transverse (shear) wave speed c_T = c/√3 ≈ 1.73 × 10⁸ m/s. This is
**significantly slower than the speed of light.**

### 4.9 The Problem

The LIGO-Virgo observation of GW170817 (binary neutron star merger), combined
with the simultaneous gamma-ray burst GRB 170817A detected 1.7 seconds later
after a ~130 million light-year journey, constrains:

```
|c_GW − c| / c < 10⁻¹⁵
```

**Source:** Abbott et al. (2017), "Gravitational Waves and Gamma-Rays from a
Binary Neutron Star Merger: GW170817 and GRB 170817A," *The Astrophysical
Journal Letters* 848(2), L13.

A transverse wave speed of c/√3 ≈ 0.577c is **ruled out by 15 orders of
magnitude.** The simple central-force lattice does not work for tensor
gravitational waves.

**This is not a failure of PDTP** — it is a precise constraint telling us
what kind of lattice the spacetime condensate must be.

---

## 5. The Cauchy Relation Problem and Its Resolution

### 5.1 What the Cauchy Relation Means

The result λ = μ (central forces) leads to c_T = c_L/√3. This is the
**Cauchy relation** — a classical result from crystal physics that holds
whenever:

1. The interactions are purely pairwise (central forces)
2. Every atom sits at a centre of inversion symmetry
3. The lattice is Bravais (one atom per unit cell)

**Source:** Born, M. & Huang, K. (1954), *Dynamical Theory of Crystal Lattices*,
Oxford University Press, Chapter 3.

In real crystals, the Cauchy relation is almost never exactly satisfied.
Diamond, silicon, and most covalent crystals violate it strongly because
they have **angular** (non-central) forces — the bonds resist bending,
not just stretching.

### 5.2 Three Ways to Break the Cauchy Relation

**(a) Non-central (angular) forces:**
Add terms that resist angular deformation between bonds. For example,
if three sites i, j, k form a bond angle, the potential includes:

```
V_angular = (K_θ/2) Σ_⟨ijk⟩ (θ_ijk − θ₀)²                   (Eq. 28.20)
```

This adds shear stiffness beyond what central forces provide, increasing
μ relative to λ.

**(b) Many-body interactions:**
If the potential depends on the local environment (not just pairwise
distances), the Cauchy relation is violated. Example: embedded-atom
methods in metallurgy.

**(c) Non-Bravais lattice:**
If the unit cell contains multiple sublattices (like diamond = 2 FCC sublattices),
the Cauchy relation is violated even with central forces, because not every
atom is at a centre of symmetry.

### 5.3 Physical Motivation for Angular Forces in PDTP

The PDTP condensate is not an ordinary crystal with atoms on springs.
The "sites" are points in spacetime, and the "displacements" are perturbations
of the local reference frame (the tetrad from Part 12).

A local reference frame has **orientation** as well as position. Rotating
one frame relative to its neighbors costs energy — this is what the
**spin connection** describes in general relativity.

```
Central forces:  resist stretching     → bulk modulus
Angular forces:  resist twisting       → shear modulus (additional)
Spin connection: resist frame rotation → torsional stiffness
```

**Source:** [Tetrad formalism](https://en.wikipedia.org/wiki/Tetrad_formalism)
(tetrads in general relativity; the spin connection encodes how frames rotate)

In the He-3A superfluid analogy (Part 12 §2), the orbital triad (m̂, n̂, l̂)
has both stretch and twist stiffness. The twist stiffness is what gives
the transverse modes their speed.

**Source:** Volovik, G. E. (2003), *The Universe in a Helium Droplet*,
Oxford University Press, Chapter 9.

**PDTP Original:** The spacetime condensate must have angular (non-central)
forces — equivalently, the lattice must resist frame rotation. This is
physically natural: it is the microscopic origin of the spin connection
in general relativity. Central forces alone give only scalar gravity;
angular forces are required for tensor gravity.

### 5.4 The Condition for c_T = c

For the general (non-central) lattice, the Lamé parameters become independent:

```
λ = K_central/a − K_angular/a    (reduced by angular forces)
μ = K_central/a + K_angular/a    (enhanced by angular forces)
```

(The exact coefficients depend on the lattice geometry and the angular
potential; the signs show the qualitative effect.)

For c_T = c, we need:

```
c²_T = μ/ρ = c²

→  μ = ρ c²                                                  (Eq. 28.21)
```

From Part 21, ρ = κ/c² where κ is the phase stiffness. So:

```
μ = (κ/c²) × c² = κ                                          (Eq. 28.22)
```

```
┌──────────────────────────────────────────────────────────┐
│  The condition for tensor GW speed = c is:                │
│                                                           │
│  μ_shear = κ = c²/(4πG)                                  │
│                                                           │
│  The shear modulus of the condensate must equal            │
│  the phase stiffness (= inverse of 4πG).                  │
│                                                           │
│  Numerically: μ = κ ≈ 1.07 × 10²⁶ J/m = 1.07 × 10²⁶ Pa │
└──────────────────────────────────────────────────────────┘
```

**PDTP Original:** This is a specific, falsifiable internal consistency
condition. If the condensate's shear modulus differs from its phase stiffness,
the tensor GW speed would differ from c — and that is ruled out by
GW170817 to 15 decimal places.

### 5.5 What About the Longitudinal Speed?

With μ = κ, we also need c_L = c for the breathing mode (in the massless limit).
From Eq. 28.18:

```
c²_L = (λ + 2μ)/ρ = (λ + 2κ)/(κ/c²)
```

For c_L = c: λ + 2κ = κ, which gives λ = −κ.

A negative first Lamé parameter is unusual but not unphysical. It corresponds
to **Poisson's ratio** ν = λ/(2(λ+μ)) = −κ/(2(−κ+κ)) → 0/0 (degenerate).

More carefully: for λ = −μ, ν = −1/(2·0) which is singular. This indicates that
the standard elastic description breaks down at this special point — the material
has zero resistance to pure volume change while having maximum resistance to shear.

**However,** in PDTP the longitudinal mode is NOT a simple elastic wave.
It has a **mass gap** from the phase-locking coupling (the cos(ψ − φ) term).
The breathing mode dispersion relation is (from Part 12, Eq. 6.10):

```
ω² = c² k² + 2g                                              (Eq. 28.23)
```

where g is the matter-condensate coupling constant. This means the breathing
mode is **massive** (like a Klein-Gordon field with mass m² = 2g), and its
group velocity is always less than c at finite frequency.

**PDTP Original:** The longitudinal (breathing) mode acquires a mass gap from
the phase-locking coupling. This resolves the λ = −μ issue: the longitudinal
sector is not purely elastic but has an additional restoring force from the
cosine potential. Only the transverse (tensor) modes are purely elastic
and massless.

### 5.6 Summary of the Resolution

```
The lattice requires TWO types of stiffness:

Central forces (K):  Resist compression  →  Longitudinal waves
Angular forces (K_θ): Resist shear/twist →  Additional transverse stiffness

Central only:   μ = K/a,  c_T = c/√3        ← Too slow (ruled out)
Central+Angular: μ = κ,   c_T = c            ← Required by LIGO

The condition μ = κ is the LATTICE-LEVEL version of the statement
"gravity propagates at the speed of light."
```

---

## 6. Dispersion Relations and Mode Mapping

### 6.1 The Three Branches

For the extended lattice with μ = κ (angular forces included), the
dispersion relations for a wave traveling in the z-direction are:

**Branch 1 — Transverse polarization 1 (shear):**

```
u = (u₀, 0, 0) exp[i(kz − ωt)]      (displacement along x)

ω² = (μ/ρ) k² = c² k²                                       (Eq. 28.24a)
```

Massless, speed c. This is the **+ polarization** of gravitational waves.

**Branch 2 — Transverse polarization 2 (shear):**

```
u = (0, u₀, 0) exp[i(kz − ωt)]      (displacement along y)

ω² = (μ/ρ) k² = c² k²                                       (Eq. 28.24b)
```

Massless, speed c. This is the **× polarization** of gravitational waves.

**Branch 3 — Longitudinal (compression + phase coupling):**

```
u = (0, 0, u₀) exp[i(kz − ωt)]      (displacement along z)

ω² = c² k² + m²_breathing                                    (Eq. 28.24c)

where m²_breathing = 2g (from phase-locking coupling)
```

Massive, speed < c at finite frequency. This is the **breathing mode**.

**Source:** [Dispersion relation](https://en.wikipedia.org/wiki/Dispersion_relation)

### 6.2 Dispersion Diagram

```
ω (frequency)
│
│           ╱ Branch 1 (transverse +)  ω = ck
│         ╱  Branch 2 (transverse ×)   ω = ck  [degenerate]
│       ╱
│     ╱    ╱ Branch 3 (longitudinal/breathing)
│   ╱    ╱   ω = √(c²k² + 2g)
│ ╱    ╱
│╱   ╱
│  ╱
│╱───── mass gap √(2g)
├──────────────────────────── k (wavenumber)

Two massless transverse branches (identical slope = c)
One massive longitudinal branch (starts at ω = √(2g) > 0)
```

### 6.3 Mapping to Gravitational Wave Polarizations

**Source:** [Gravitational wave](https://en.wikipedia.org/wiki/Gravitational_wave)
(polarization section)

When a gravitational wave passes through a ring of test particles:

```
Transverse 1 (h₊ mode):       Transverse 2 (h× mode):
   ↑                              ↗
   |                             /
← ─ ○ ─ →                    ↙  ○  ↗
   |                             \
   ↓                              ↙

Stretches x, squeezes y        Same pattern rotated 45°

Longitudinal (breathing mode):
      ↗ ↑ ↖
    →  ○  ←
      ↙ ↓ ↘

Expands and contracts uniformly (isotropic)
```

| Lattice mode | GW polarization | Speed | Mass | LIGO detectable? |
|-------------|----------------|-------|------|-----------------|
| Transverse 1 | h₊ (plus) | c | 0 | Yes — confirmed |
| Transverse 2 | h× (cross) | c | 0 | Yes — confirmed |
| Longitudinal | Breathing | < c | √(2g) | Suppressed (Yukawa) |

**PDTP Original:** The two transverse lattice modes are the tensor GW
polarizations observed by LIGO. The longitudinal mode is the breathing
mode predicted by scalar PDTP, suppressed by its mass gap. This matches
the E(2) class N₃ classification from Part 12: two tensor + one scalar mode.

### 6.4 Why LIGO Doesn't See the Breathing Mode

The breathing mode mass m_breathing = √(2g) gives a Compton wavelength:

```
λ_breathing = ℏ/(m_breathing c) = ℏ c / √(2g)
```

At distances larger than λ_breathing, the breathing mode amplitude decays
exponentially (Yukawa suppression). For typical stellar-mass black hole
mergers detected by LIGO (frequency ~ 100 Hz), the breathing mode
contribution is suppressed by the ratio:

```
h_breathing / h_tensor < 1/(2ω_BD + 3) < 1.25 × 10⁻⁵  (Cassini bound)
```

**Source:** Part 12 (tetrad_extension.md §6.3) and hard_problems.md §1.9.

This is below LIGO's current sensitivity. Multi-detector GW polarimetry
with 5+ detectors in the 2030s may be able to detect or constrain it.

---

## 7. Connection to the Tetrad Extension

### 7.1 Bottom-Up Meets Top-Down

Part 12 derived tensor GW modes **top-down**: start with the tetrad order
parameter Φ = √ρ₀ e^{iφ} e^a_μ, write the Palatini action, vary it,
and get linearized Einstein equations.

This document derives them **bottom-up**: start with the oscillator lattice,
generalize to vector displacements, compute the continuum elastic wave
equation, and identify transverse modes as tensor GWs.

Both approaches give the **same answer:**

| Property | Top-down (Part 12) | Bottom-up (Part 28) |
|----------|-------------------|---------------------|
| Tensor modes | □h^TT = 0 (massless, speed c) | c²_T = μ/ρ = c² (when μ = κ) |
| Breathing mode | □θ + 2gθ = 0 (massive) | ω² = c²k² + 2g (massive) |
| Classification | E(2) class N₃ | 2 transverse + 1 longitudinal |
| Source of tensor | Tetrad DOF | Shear rigidity of lattice |
| Constraint | Lorentz invariance | μ = κ (shear = bulk stiffness) |

### 7.2 The Strain-Metric Correspondence

The lattice displacement gradient ∂uᵅ/∂xᵝ is the **strain tensor**
of the condensate. In linearized gravity, the metric perturbation h_μν
is related to the strain by:

```
h_αβ = ε_αβ + ε_βα = ∂u_α/∂x_β + ∂u_β/∂x_α                (Eq. 28.25)
```

(the symmetrized gradient). The transverse-traceless (TT) projection
of h_αβ extracts the tensor GW content:

**Source:** [Linearized gravity](https://en.wikipedia.org/wiki/Linearized_gravity)

```
h^TT_αβ = TT projection of (∂u_α/∂x_β + ∂u_β/∂x_α)         (Eq. 28.26)
```

For a transverse wave u = (u₀, 0, 0)e^{i(kz−ωt)} traveling in z:

```
h^TT_xx = −h^TT_yy = iku₀ e^{i(kz−ωt)}    → h₊ mode
```

For u = (u₀, u₀, 0)e^{i(kz−ωt)} at 45°:

```
h^TT_xy = h^TT_yx = iku₀ e^{i(kz−ωt)}     → h× mode
```

The elastic wave equation μ∇²u = ρ∂²u/∂t² for the transverse mode
translates directly to:

```
□ h^TT_αβ = 0                                                (Eq. 28.27)
```

when μ/ρ = c². **This is the linearized Einstein equation in vacuum.**

**PDTP Original:** The lattice shear wave equation IS the linearized
Einstein equation for tensor GW modes, when the condensate shear modulus
equals the phase stiffness (μ = κ). The lattice provides a microscopic
origin for the metric tensor.

### 7.3 Identification of G

From Part 21: G = c²/(4πκ). In the elastic medium picture, Newton's
constant relates to the shear modulus as:

```
G = c⁴/(16πμc²) = c²/(16πμ)     (linearized gravity from elastic medium)
```

With μ = κ, this gives G = c²/(16πκ), which differs from Part 21's
G = c²/(4πκ) by a factor of 4.

**PDTP Original:** The factor-of-4 discrepancy between the scalar
derivation (Part 21) and the elastic medium derivation arises from the
difference between how scalar and tensor coupling propagate. In the
scalar theory, the gravitational potential φ directly couples to mass.
In the tensor theory, the metric perturbation h_μν couples to the
stress-energy tensor T_μν, with different numerical prefactors.

This discrepancy is **expected and documented** — the scalar theory
(Part 21) was known to give the correct G by construction (it was
derived from the Poisson equation). The tensor theory introduces
geometric factors from the TT projection that modify the prefactor.
Resolving this requires a careful treatment of the full tensor
coupling that matches Part 12's Palatini derivation, where G is
input as a parameter of the action rather than derived.

---

## 8. What Works, What Doesn't, and What's Next

### 8.1 Results Summary

| Result | Status | Where |
|--------|--------|-------|
| Vector lattice gives 3 wave branches | **Derived** | §4 |
| 2 transverse + 1 longitudinal | **Derived** | §6 |
| Transverse modes map to h₊ and h× | **Derived** | §6.3 |
| Central forces give c_T = c/√3 | **Derived (problem)** | §4.8 |
| Angular forces needed for c_T = c | **Argued** | §5.3 |
| Condition: μ = κ for c_T = c | **Derived** | §5.4 |
| Breathing mode is massive | **Consistent** with Part 12 | §6.1 |
| Strain → metric correspondence | **Derived** | §7.2 |
| □h^TT = 0 from lattice | **Derived** (when μ = κ) | §7.2 |
| G factor matches Part 21 | **Factor of 4 discrepancy** | §7.3 |

### 8.2 Honest Assessment

**What works:**
- The vector lattice naturally produces three wave branches
- Two transverse branches are massless and map to tensor GW polarizations
- The breathing mode is massive (from phase coupling), consistent with Part 12
- The strain-metric correspondence is clean and standard
- The lattice gives a microscopic origin for the tetrad

**What doesn't (yet):**
1. **Central forces fail.** The simplest lattice gives c_T = c/√3, not c.
   Angular forces are required, adding a new parameter K_θ constrained by μ = κ.

2. **The angular potential is not specified.** We know the condition (μ = κ)
   but have not derived the specific angular potential from first principles.

3. **Factor-of-4 in G.** The elastic medium gives G = c²/(16πκ) while
   Part 21 gives G = c²/(4πκ). This geometric factor needs resolution.

4. **Cubic lattice is not isotropic.** A simple cubic lattice has cubic
   symmetry, not full rotational symmetry. True isotropy requires either
   averaging over orientations (reasonable for a disordered condensate)
   or a different lattice structure.

### 8.3 What This Means for PDTP

**The good news:** Tensor GW modes exist in the lattice. The mathematical
structure is correct — transverse shear waves map to tensor gravitational
waves, and the condition μ = κ ensures they propagate at c.

**The constraint:** The condensate must have angular stiffness (non-central
forces). This is physically natural — the tetrad represents a local frame,
and frames resist rotation. But it goes beyond Part 21's minimal model.

**The interpretation:** The Cauchy relation violation μ ≠ λ is the
lattice-level signature of the spin connection. In GR, the spin connection
encodes how local frames rotate relative to each other. In the condensate
lattice, angular forces encode the same physics. Central forces give only
scalar gravity; angular forces are needed for full tensor gravity.

### 8.4 Open Problems for Future Work

1. **Derive the angular potential** from the condensate symmetry breaking
   pattern GL(4,ℝ) × U(1) → SO(3,1) (Part 12). This should fix K_θ
   in terms of K.

2. **Quadrupole radiation formula:** Show that an accelerating lattice
   defect (matter particle) emits transverse waves with the correct
   quadrupole angular pattern.

3. **Full nonlinear analysis:** Go beyond linearized waves to show that
   the full lattice dynamics reproduces nonlinear GR effects.

4. **Resolve the G prefactor:** Careful matching between the scalar
   (Poisson equation) and tensor (Einstein equation) derivations.

5. **Lattice isotropy:** Determine whether the condensate has an ordered
   lattice (cubic, FCC, etc.) or a disordered structure (amorphous), and
   how isotropy emerges in either case.

---

## 9. Summary

| Concept | Part 21 (scalar) | Part 28 (vector) |
|---------|-----------------|------------------|
| DOF per site | 1 (phase θ) | 3 (displacement **u**) |
| Wave branches | 1 (longitudinal) | 3 (1 long. + 2 transverse) |
| GW polarization | Breathing only | Breathing + tensor (h₊, h×) |
| Forces needed | Central (K) | Central (K) + angular (K_θ) |
| c_T | N/A (no transverse) | c (when μ = κ) |
| Matches LIGO? | No (breathing only) | Yes (two tensor modes) |
| Matches Part 12? | Scalar sector only | Full tensor sector |

**The key equation derived in this document:**

```
┌──────────────────────────────────────────────────────┐
│                                                       │
│  Tensor GW speed = c  ⟺  μ_shear = κ = c²/(4πG)    │
│                                                       │
│  The shear modulus of the spacetime condensate must    │
│  equal its phase stiffness.                           │
│                                                       │
│  Central forces give μ = κ/3 → c_T = c/√3 (fails)    │
│  Angular forces can give μ = κ → c_T = c (required)   │
│                                                       │
└──────────────────────────────────────────────────────┘
```

**The honest bottom line:** The oscillator lattice from Part 21 **can**
produce tensor gravitational waves, but only if it has angular (non-central)
forces in addition to the central coupling K. The condition μ = κ is a
specific, falsifiable constraint that relates the shear stiffness to the
phase stiffness — and therefore to Newton's constant G.

This is a **mathematical completion task with one surprise**: the central-force
model alone doesn't work. The condensate must resist shear deformation as
strongly as it resists compression. In the language of general relativity,
this means the spin connection (frame rotation resistance) contributes equally
to the metric dynamics — which is exactly what the Palatini formulation in
Part 12 assumes.
