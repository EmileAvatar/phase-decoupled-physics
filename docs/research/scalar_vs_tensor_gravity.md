# Part 27: Scalar vs Tensor Gravity — The PDTP Gap and How to Close It

## Status
**PDTP Original** — Analysis of the scalar/tensor problem and path to resolution.

**Conceptual framework — not experimentally validated.**

**Diagram:** [scalar_vs_tensor_gravity.svg](../../assets/images/scalar_vs_tensor_gravity.svg)

---

## 1. The Problem in Plain English

PDTP currently describes spacetime with **one field** φ (the condensate phase).
That's a **scalar** — a single number at every point in space, like a temperature map.

Einstein's General Relativity describes spacetime with a **metric tensor** g_μν —
a 4×4 matrix at every point (10 independent numbers). This encodes gravity's
strength **and direction** in all four dimensions of spacetime.

For everyday gravity (falling apples, orbiting planets), the scalar is enough —
the **gradient** of φ gives you a direction (it points "downhill" toward masses).

The problem shows up specifically in **gravitational waves far from any source**.

---

## 2. What LIGO Sees vs What Scalar Predicts

### 2.1 Gravitational Wave Polarizations

When a gravitational wave passes through a ring of test particles:

**Scalar (breathing mode):**
- The ring expands and contracts uniformly
- Circle stays a circle — just gets bigger and smaller
- Like a balloon inflating and deflating
- All directions are treated equally

**Tensor (+ and × modes):**
- The ring stretches in one direction while squeezing in the perpendicular direction
- Circle becomes an ellipse, then flips to the other ellipse
- Two independent polarizations: "plus" (+) and "cross" (×)
- The × mode is the same as + but rotated 45°

### 2.2 What Nature Does

**Source:** [LIGO detection of GW150914](https://en.wikipedia.org/wiki/First_observation_of_gravitational_waves)

LIGO confirmed tensor polarizations (+ and ×) starting with GW150914 (2015).
The three-detector event GW170814 (LIGO Hanford + Livingston + Virgo) provided
the first polarization test, favouring pure tensor over pure scalar.

**Source:** Abbott et al. (2017), "GW170814: A Three-Detector Observation of
Gravitational Waves from a Binary-Black-Hole Coalescence,"
*Physical Review Letters* 119(14), 141101.

| Situation | Scalar PDTP | Tensor GR | Verdict |
|-----------|------------|-----------|---------|
| Apple falling | Works | Works | Tie |
| Planet orbits | Works | Works | Tie |
| Light bending | Works (with correction) | Works naturally | GR slightly better |
| Perihelion precession | Works (acoustic metric) | Works | Tie |
| GW polarization | Breathing mode | + and × modes | **GR confirmed by LIGO** |

**The scalar limitation is the single biggest gap in PDTP.**

---

## 3. Why Scalar Works for Most Gravity

A scalar field φ has a **gradient** ∇φ — and a gradient IS a vector (it points
in a direction). For static or slow-moving gravity, the gradient tells particles
which way to fall:

```
Matter creates a phase distortion in the condensate
   → Phase gradient points toward the mass
   → Other particles follow the gradient
   → That's gravity

More mass = deeper phase distortion = steeper gradient = stronger pull
```

This is the field equation in action:

```
□φ = Σᵢ gᵢ sin(ψᵢ − φ)
```

Each matter particle (ψᵢ) pulls the condensate phase (φ) toward it. The
resulting phase slope is what we experience as gravitational acceleration.

**The scalar description fails only when we ask about free gravitational waves
propagating through empty space** — because there's no mass to create a gradient,
and the wave's own oscillation pattern reveals whether the field has one
component (scalar) or multiple components (tensor).

---

## 4. Why Waves Have Direction — The Key Insight

### 4.1 Longitudinal vs Transverse Waves

A wave in a medium can oscillate in two fundamentally different ways:

**Longitudinal (like sound):**
```
Wave direction →
Particles: ← → ← → ← →   (move along wave direction)
```
- Compression and rarefaction
- No preferred direction perpendicular to the wave
- This is scalar-like → produces the breathing mode
- **Liquids only support this type**

**Transverse (like a guitar string):**
```
Wave direction →
Particles: ↑ ↓ ↑ ↓ ↑ ↓   (move perpendicular to wave direction)
```
- Shear deformation
- Picks out a specific perpendicular direction (polarization)
- This is tensor-like → produces + and × modes
- **Only materials with rigidity support this type**

### 4.2 What Kind of Medium Is the Condensate?

This is the critical question for PDTP:

| Medium type | Supports | GW modes | PDTP status |
|------------|---------|----------|-------------|
| Simple fluid (superfluid) | Longitudinal only | Breathing only | Current scalar theory |
| Elastic solid (lattice) | Longitudinal + transverse | Breathing + tensor | What we need |
| Supersolid (both) | Both | All modes | Most general case |

**Source:** [Supersolid](https://en.wikipedia.org/wiki/Supersolid)

### 4.3 The Lattice Already Has Rigidity

From Part 21 (§4, efv_microphysics.md), the condensate is modeled as an
**oscillator lattice** — discrete sites connected by coupling springs K:

```
H = Σ_sites [½ I θ̇² + ½ K Σ_neighbours (θᵢ − θⱼ)²]
```

A lattice with nearest-neighbour coupling has **shear rigidity**. Unlike a simple
fluid, it resists being deformed sideways. This means it naturally supports
transverse (shear) waves in addition to longitudinal (sound) waves.

**PDTP Original:** The oscillator lattice from Part 21 already contains the
physics needed for tensor gravitational waves. The current scalar description
(one phase field φ) captures only the longitudinal sector. The full lattice
dynamics includes transverse oscillations that should map to tensor GW modes.

---

## 5. The Matter Convergence Picture

### 5.1 Single Particle — Phase Ripple

A single matter particle in the condensate is like a pebble in a pond:

```
    · · · · · · · · · ·
    · · · · · · · · · ·
    · · · ↗ ↑ ↑ ↖ · · ·
    · · → → ● ← ← · · ·    ● = matter particle
    · · · ↘ ↓ ↓ ↙ · · ·    → = phase gradient (toward particle)
    · · · · · · · · · ·
    · · · · · · · · · ·
```

The phase gradient points inward — other particles follow it. That's gravity.

### 5.2 Many Particles — Reinforced Gradient

Multiple particles clumped together create overlapping phase distortions:

```
    · · · · ↑ ↑ ↑ · · · ·
    · · · ↗ ↑ ↑ ↑ ↖ · · ·
    · · → → ● ● ← ← · · ·    ●● = clump of matter
    · · → → ● ● ← ← · · ·    → = stronger gradient (steeper)
    · · · ↘ ↓ ↓ ↓ ↙ · · ·
    · · · · ↓ ↓ ↓ · · · ·
```

The gradients **reinforce** toward the center of mass. More matter = deeper
phase well = steeper gradient = stronger gravity. This is the PDTP version
of "mass curves spacetime."

### 5.3 The Wave Convergence

The condensate field around a mass has the form (from §8.4 of efv_microphysics):

```
φ(r) = −GM/(c²r)    [Newtonian limit]
```

The condensate waves converge toward the mass — the phase surfaces are
concentric shells getting denser toward the center. More mass = tighter
shell spacing = stronger gravitational field.

**This directionality is present even in the scalar theory.** The gradient of a
scalar field provides all the directional information needed for static gravity.

---

## 6. Path to Tensor Gravity — Three Approaches

### 6.1 Approach A: Tetrad Extension (Current Effort)

Replace single scalar φ with four phase fields φ^a (a = 0,1,2,3):

```
Current:    L = ½(∂φ)² + g cos(ψ − φ)           [1 field, scalar]
Extended:   L = ½(∂φ^a)² + g cos(ψ^a − φ^a)     [4 fields, tetrad]
```

The four fields form a tetrad (vierbein) — a local frame at each point.
The metric tensor emerges as:

```
g_μν = η_ab ∂_μφ^a ∂_νφ^b
```

where η_ab = diag(−1,+1,+1,+1) is the flat Minkowski metric.

**Status:** Partially developed in tetrad_extension.md (Part 12).
Conceptually sound but field equations not yet fully derived.

**Source:** The tetrad/vierbein approach to gravity is standard —
see [Tetrads in general relativity](https://en.wikipedia.org/wiki/Tetrad_formalism)

### 6.2 Approach B: Lattice Shear Modes (New — Most Promising)

Start from the oscillator lattice (Part 21) and compute ALL normal modes,
not just the longitudinal ones.

A 3D lattice with nearest-neighbour coupling has:
- 1 longitudinal (acoustic) branch → the current scalar φ
- 2 transverse (shear) branches → the missing tensor modes

```
Longitudinal:  ← · → · ← · → ·    (compression wave)
                = scalar φ = breathing mode

Transverse 1:  ↑ · ↓ · ↑ · ↓ ·    (shear wave, polarization 1)
                = tensor h₊ = plus mode

Transverse 2:  ↗ · ↙ · ↗ · ↙ ·    (shear wave, polarization 2)
                = tensor h× = cross mode
```

**PDTP Original:** The oscillator lattice from Part 21 naturally produces
three wave branches. The scalar PDTP theory has been working with only
the longitudinal branch. The two transverse branches contain the tensor
gravitational wave modes that LIGO observes.

**This is the most promising approach** because it derives tensor gravity
from the same lattice that already gives scalar gravity — no new assumptions
needed, just completing the analysis.

### 6.3 Approach C: Elastic Condensate (Complementary)

Treat the condensate not as a perfect superfluid but as an elastic medium
with finite shear modulus μ_s:

```
L = ½ρ (∂_t u)² − ½(λ + 2μ)(∇·u)² − ½μ(∇×u)²
```

where u is the displacement field. The speed of longitudinal waves is
c_L² = (λ + 2μ)/ρ = c² and the speed of transverse waves is
c_T² = μ/ρ.

For gravitational waves to propagate at c (as observed by LIGO+Virgo
from the neutron star merger GW170817 + GRB 170817A):

```
c_T = c  →  μ = ρc² = v²  (same as the bulk modulus!)
```

**Source:** Abbott et al. (2017), "Gravitational Waves and Gamma-Rays
from a Binary Neutron Star Merger: GW170817 and GRB 170817A,"
*The Astrophysical Journal Letters*, 848(2), L13.

**PDTP Original:** If the condensate's shear modulus equals its bulk modulus
(μ = B = v² = κ), then both longitudinal and transverse waves propagate at c,
and the tensor gravitational wave speed matches observation. This is a
non-trivial constraint that the lattice model can be checked against.

---

## 7. What Needs To Be Done

### 7.1 Immediate (Part 28 Target)

1. **Compute the full dispersion relation** of the Part 21 oscillator lattice
   - Include both longitudinal and transverse branches
   - Show that transverse modes propagate at c in the continuum limit
   - Identify the two transverse polarizations with GR's + and × modes

2. **Derive the effective metric** from the lattice dynamics
   - Show that g_μν = η_ab ∂_μφ^a ∂_νφ^b emerges from the lattice
   - Verify that it satisfies (linearized) Einstein equations

3. **Check the shear modulus condition**
   - Compute μ from the lattice coupling K and spacing a
   - Verify μ = B = κ = v² (required for c_T = c)

### 7.2 Medium Term

4. **Gravitational wave generation** from the lattice
   - Show that an accelerating phase defect (matter) emits
     transverse waves with the correct quadrupole formula
   - Compare radiated power with Einstein's formula

5. **Post-Newtonian corrections**
   - Derive the PPN parameters (γ, β) from the full lattice theory
   - Current scalar theory gives γ = 1 from acoustic metric argument
   - Full lattice should give both γ = 1 and β = 1

### 7.3 Long Term (Decisive Test)

6. **Mixed polarization prediction**
   - Does the lattice predict ONLY tensor modes (like GR)?
   - Or does it predict tensor + breathing (scalar-tensor theory)?
   - If mixed: what is the ratio of breathing to tensor amplitude?
   - This is a **falsifiable prediction** testable by future GW detectors

---

## 8. Summary

| What we know | Status |
|-------------|--------|
| Scalar PDTP gives correct static gravity | Confirmed (Parts 1, 21) |
| Scalar predicts breathing mode GWs | Problem — LIGO sees tensor modes |
| The oscillator lattice has shear rigidity | True — lattices support transverse waves |
| Transverse lattice modes could be tensor GWs | Plausible — needs derivation |
| GW speed must equal c | Requires shear modulus = bulk modulus |
| The tetrad extension captures this | Partially — needs completion |

**The gap is not fatal.** The physics for tensor modes is already present in the
Part 21 lattice — it just hasn't been extracted yet. This is a mathematical
completion task, not a conceptual redesign.

**The key equation to derive:**

```
From lattice:  H = Σ [½I θ̇ᵢ² + ½K Σ_nn (θᵢ − θⱼ)²]

Extract:       g_μν(x) = η_ab e^a_μ(x) e^b_ν(x)

Where:         e^a_μ = ∂_μ φ^a  (tetrad from four phase fields)

Show:          G_μν = 8πG T_μν  (Einstein equations emerge)
```

If this derivation succeeds, PDTP goes from "scalar approximation that works
for most things" to "full tensor theory of gravity derived from a condensate
lattice" — and the breathing mode problem is solved.
