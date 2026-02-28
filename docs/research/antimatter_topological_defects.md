# Part 22: Antimatter as Opposite-Winding Topological Defects

**Status:** Interpretive framework — not experimentally validated.
Established physics sections are sourced. PDTP sections are marked
**PDTP Original** (derived from Lagrangian) or **PDTP Speculative**
(not yet derived).

**Date:** 2026-02-28

**Cross-references:** [Part 18](aharonov_bohm_pdtp.md) (topological defects,
vortex lines), [Part 23](charge_quantum_numbers.md) (charge as winding number,
Z₃ structure), [Part 27b](phase_locking_unification.md) (universal
phase-locking), [Part 28b](polarization_analogy_pdtp.md) (decoupling energy).

---

## §1: Executive Summary

In the Standard Model, every particle has an antiparticle with the same mass
but opposite charges. In PDTP, this maps to a simple geometric picture:
particles are topological defects with winding number n = +1 in the matter
phase field ψ, and antiparticles are defects with winding number n = −1. When
they meet, the windings cancel (n = +1 + n = −1 = 0), and the stored energy
radiates away as φ-waves (photons).

Part 23 introduced two competing models for antimatter:

- **Model A (winding):** antiparticle = opposite winding number in ψ
- **Model B (trough):** antiparticle = matter at the unstable equilibrium
  ψ = φ + π of the cosine potential

A key finding of this document: **these are not the same thing.** Model A
describes the topological identity of the defect (its conserved charge).
Model B describes a different object — a metastable excitation in the
opposite vacuum sector. Both are valid physics, but they describe different
configurations. The Standard Model antiparticle corresponds to Model A.

This document also checks CPT symmetry (the PDTP Lagrangian is CPT-invariant,
as expected), annihilation energetics (consistent), and antimatter gravity
(falls down, matching the ALPHA-g experiment). The honest gap: PDTP has
exact CP symmetry, which blocks the standard mechanism for baryogenesis.

---

## §2: Antimatter — Established Physics

### §2.1: The Dirac Equation and Antiparticles

In 1928, Paul Dirac tried to write a quantum wave equation that was
compatible with special relativity. The equation he found:

(iγ^μ ∂_μ − m)ψ = 0

had four solutions where only two were expected. Two solutions describe a
particle with positive energy (spin up and spin down). The other two
describe a particle with the same mass but opposite charge — the
**antiparticle**.

**Source:** [Dirac equation — Wikipedia](https://en.wikipedia.org/wiki/Dirac_equation)

Dirac initially interpreted the negative-energy solutions as "holes" in a
filled sea of electrons. In 1932, Carl Anderson discovered the positron
(anti-electron) in cosmic ray tracks, confirming Dirac's prediction.

**Source:** Anderson, C. D. (1933), "The Positive Electron," *Physical
Review* 43, 491.

Every particle in the Standard Model has an antiparticle. For some neutral
particles (like the photon), the antiparticle is the particle itself.

### §2.2: The CPT Theorem

CPT is a combination of three discrete transformations:

- **C (charge conjugation):** replace every particle with its antiparticle
  (all charges flip sign)
- **P (parity):** mirror-reflect all spatial coordinates (x → −x)
- **T (time reversal):** reverse the direction of time (t → −t)

The **CPT theorem** states: any quantum field theory that is (a) Lorentz
invariant, (b) local (no action at a distance in the Lagrangian), and (c)
has a Hermitian Hamiltonian, must be invariant under the combined CPT
transformation.

**Source:** [CPT symmetry — Wikipedia](https://en.wikipedia.org/wiki/CPT_symmetry)

This is a theorem, not an assumption. It was proved independently by
Lüders (1954) and Pauli (1955). It means that if you flip all charges,
mirror space, and reverse time simultaneously, the laws of physics look
identical. Individual C, P, or T symmetries can be violated (and are — the
weak force violates P and CP), but the combination CPT is always exact.

### §2.3: Pair Creation and Annihilation

**Pair creation:** a photon with energy E ≥ 2m_e c² = 1.022 MeV can convert
into an electron-positron pair near a nucleus (the nucleus absorbs recoil
momentum to conserve both energy and momentum):

γ + nucleus → e⁻ + e⁺ + nucleus

**Source:** [Pair production — Wikipedia](https://en.wikipedia.org/wiki/Pair_production)

**Annihilation:** when an electron meets a positron, they annihilate into
photons. Two photons are required (not one) to conserve both energy and
momentum simultaneously:

e⁻ + e⁺ → γ + γ

Each photon carries energy E = m_e c² = 0.511 MeV in the center-of-mass
frame.

**Source:** [Electron–positron annihilation — Wikipedia](https://en.wikipedia.org/wiki/Electron%E2%80%93positron_annihilation)

The electron and positron can also form a bound state called **positronium**
before annihilating. Parapositronium (spins antiparallel) lives ~125 ps;
orthopositronium (spins parallel) lives ~142 ns.

**Source:** [Positronium — Wikipedia](https://en.wikipedia.org/wiki/Positronium)

### §2.4: The ALPHA-g Experiment (2023)

The ALPHA collaboration at CERN trapped antihydrogen atoms (one antiproton
+ one positron) in a magnetic bottle, then released them to fall freely
under gravity. This is the first direct measurement of antimatter's
gravitational acceleration.

**Result:** The measured gravitational acceleration of antihydrogen is:

g_anti = (0.75 ± 0.13 (stat+syst) ± 0.16 (simulation)) × g

This is consistent with g_anti = g (antimatter falls down at the same
rate as matter), ruling out gravitational repulsion at high confidence.
The precision is ~20% — future runs aim for ~1%.

**Source:** ALPHA Collaboration (2023), "Observation of the effect of
gravity on the motion of antimatter," *Nature* 621, 716–722.

This is the observational constraint that any PDTP antimatter model must
satisfy.

---

## §3: BEC Vortex-Antivortex Physics — The Physical Precedent

The reason PDTP can discuss antimatter as "opposite-winding defects" is
that this physics is well established in Bose-Einstein condensates (BECs)
and superfluids. This section reviews the real condensed matter physics
that motivates the PDTP analogy.

### §3.1: What Is a BEC Vortex?

A BEC is described by a complex order parameter:

Ψ(x) = √ρ(x) × e^{iθ(x)}

where ρ is the particle density and θ is the phase. A **quantum vortex**
is a point (in 2D) or line (in 3D) where the density goes to zero and the
phase θ winds by an integer multiple of 2π around it:

∮ ∇θ · dl = 2πn,     n ∈ ℤ                              ... (3.1)

The integer n is the **winding number** — a topological invariant. You
cannot remove a vortex by smoothly deforming the field; you must either
move it to the boundary or annihilate it with an opposite-winding vortex.

**Source:** [Quantum vortex — Wikipedia](https://en.wikipedia.org/wiki/Quantum_vortex)

At the vortex core, the density ρ → 0 over a characteristic distance
called the **healing length** ξ. The core has finite energy density —
there is no singularity.

**Source:** [Gross–Pitaevskii equation — Wikipedia](https://en.wikipedia.org/wiki/Gross%E2%80%93Pitaevskii_equation)

### §3.2: Vortex and Antivortex — Opposite Winding

An **antivortex** has winding number n = −1: the phase winds in the
opposite direction compared to a vortex (n = +1). Key properties:

1. **Attraction:** A vortex and antivortex attract each other (the combined
   field has lower energy when they overlap).

2. **Annihilation:** When they meet, n = +1 + (−1) = 0. The topological
   defect disappears and the stored energy is released as **sound waves
   (phonons)** in the condensate.

3. **BKT transition:** At low temperature, vortex-antivortex pairs are
   bound together. Above the Berezinskii-Kosterlitz-Thouless (BKT)
   temperature T_BKT, the pairs unbind and proliferate. This is a genuine
   phase transition driven entirely by topology — no symmetry is broken
   in the Landau sense.

**Source:** [Berezinskii–Kosterlitz–Thouless transition — Wikipedia](https://en.wikipedia.org/wiki/Berezinskii%E2%80%93Kosterlitz%E2%80%93Thouless_transition)

### §3.3: Mapping BEC → PDTP

The structural correspondence between BEC vortex physics and PDTP:

| BEC concept | PDTP equivalent | Established? |
|:------------|:---------------|:-------------|
| Condensate Ψ = √ρ e^{iθ} | Spacetime field √ρ₀ e^{iφ} | Part 14, Part 21 |
| Matter excitation | Matter phase field ψᵢ | Part 1 |
| Vortex (n = +1) | Particle (positive charge) | Part 23 §5 |
| Antivortex (n = −1) | Antiparticle (negative charge) | Part 23 §5 |
| Vortex-antivortex annihilation → phonons | e⁺e⁻ annihilation → φ-radiation (photons) | Part 23 §7 |
| Healing length ξ | Defect core size ~ ℓ_P | Part 21 |
| BKT transition | (no PDTP equivalent established) | Open |

**Limit of the analogy:** BEC vortices exist in non-relativistic 2D or 3D
condensates. PDTP requires a relativistic, Lorentz-invariant, 4D version.
The mapping is structural — the same mathematics describes both systems —
but PDTP has not derived vortex solutions from its field equations. The
analogy is physically motivated but not formally proved.

---

## §4: Antimatter in PDTP — The Two Models

This section addresses the central question: what IS antimatter in PDTP?
Part 23 introduced two models. We show here that they describe different
physical objects, and clarify which one corresponds to the Standard Model
antiparticle.

### §4.1: Recap of the Two Models

**Model A — Opposite winding (Part 23 §5):**

A particle is a topological defect in the matter phase field ψ with winding
number n = +1. An antiparticle has n = −1. The charge is the topological
invariant:

∮ ∇ψ · dl = 2πn                                          ... (4.1)

Charge is conserved because winding numbers are topological invariants —
they can only change by moving defects to the boundary or annihilating
them with opposite-winding defects. This maps directly to the conservation
of electric charge via Noether's theorem applied to the global U(1)
symmetry of the ψ field.

**Model B — Trough equilibrium (Part 23 §7):**

The PDTP potential is V(ψ − φ) = −g cos(ψ − φ). This has two equilibria:

∂V/∂ψ = g sin(ψ − φ) = 0

Solution 1: ψ = φ (the "crest")

∂²V/∂ψ² = g cos(ψ − φ)|_{ψ=φ} = g > 0     → stable minimum   ... (4.2)

Solution 2: ψ = φ + π (the "trough")

∂²V/∂ψ² = g cos(ψ − φ)|_{ψ=φ+π} = −g < 0  → unstable maximum ... (4.3)

Model B identifies the particle with the stable crest (ψ = φ) and the
antiparticle with the unstable trough (ψ = φ + π).

### §4.2: The Key Distinction — These Are Different Objects

At first glance, Models A and B seem like two descriptions of the same
thing. They are not.

**Model A** describes the global topology of the ψ field. Far from the
defect core, the field returns to the ground state ψ → φ regardless of
whether n = +1 or n = −1. The winding number tells you how many times
the phase wraps around the core, not what value it takes far away. A
vortex (n = +1) and an antivortex (n = −1) both live in the same vacuum
(ψ = φ everywhere far from the core).

**Model B** describes a different configuration: ψ is globally displaced
to the opposite equilibrium ψ = φ + π. This is not a topological defect
at all — it is a metastable excitation sitting at the maximum of the
cosine potential. In condensed matter, this is analogous to a **false
vacuum bubble** or a **domain wall** between two regions of different
phase.

In plain English:
- Model A: the antiparticle is a whirlpool spinning the other way
  (opposite winding, same water level)
- Model B: the antiparticle is sitting on top of a hill instead of in
  a valley (different equilibrium, no whirlpool)

**PDTP Original:** In quantum field theory, the antiparticle corresponds
to Model A — a topological defect with opposite quantum numbers in the
same vacuum. Model B describes a different physical object (a domain-wall
excitation or false vacuum state). Both are valid configurations of the
PDTP field equations, but they are not the same thing and should not be
conflated.

### §4.3: Two-Level Picture

Although Models A and B describe different objects, they are complementary
descriptions at different scales:

- **Level 1 (Topology):** The winding number n = ±1 classifies particles
  and antiparticles. This is a global property protected by topology.
  Conservation of n = conservation of charge.

- **Level 2 (Local dynamics):** At the core of a topological defect, the
  phase ψ − φ passes through all values from 0 to ±2π. In particular,
  it passes through π (the trough). So the trough physics is relevant
  inside the defect core, even though the far-field vacuum is at ψ = φ.

This suggests a possible unification: the antiparticle (Model A) has a
core where ψ − φ passes through π (Model B physics), but far from the
core it returns to the same vacuum as the particle. The trough is not
the asymptotic state — it is the interior structure of the antivortex.

**PDTP Speculative:** This two-level picture is plausible but requires
solving the PDTP field equations for an explicit vortex profile ψ(r) to
confirm that the n = −1 solution has the expected core structure. This
is an open calculation.

### §4.4: C Conjugation in PDTP

In the Standard Model, C (charge conjugation) maps every particle to its
antiparticle: all internal quantum numbers flip sign. In PDTP:

**C: n → −n (winding number flip)**

This maps a vortex to an antivortex. The PDTP Lagrangian:

L = ½(∂_μ φ)(∂^μ φ) + Σᵢ ½(∂_μ ψᵢ)(∂^μ ψᵢ) + Σᵢ gᵢ cos(ψᵢ − φ)

has no explicit dependence on the winding number n. The kinetic terms
depend on derivatives of ψ, not on n directly. The cosine coupling
depends on ψ − φ, which is the same function regardless of whether
ψ winds as +2π or −2π around a closed loop. Therefore:

**The Lagrangian is C-invariant.** A solution with winding n = +1 has
the same energy as a solution with n = −1.

**PDTP Original:** C conjugation in PDTP = winding number reversal.
The Lagrangian is manifestly C-invariant because it depends only on
local field values and derivatives, not on the global topological
charge.

**Caveat:** For real scalar fields (as φ and ψ are written in PDTP),
there is no natural "complex conjugation" operation. C conjugation
must be imposed as an external map between solutions with different
winding numbers. This is conceptually different from C in QFT, where
it acts on complex spinor fields via complex conjugation. The PDTP
version is well-defined but should not be over-identified with the
QFT operation.

---

## §5: Annihilation Energetics

### §5.1: Annihilation in Plain English

When a particle (winding +1) meets an antiparticle (winding −1), their
combined winding number is +1 + (−1) = 0. Topologically, the defect
pair can disappear — there is no topological obstruction to annihilation.

The energy stored in the defect pair is released as oscillations of the
spacetime phase field φ — which propagate outward as waves. In PDTP,
small-amplitude φ-waves are identified with photons (via the acoustic
metric correspondence, see Part 12).

This is structurally identical to BEC vortex-antivortex annihilation,
where the released energy goes into phonons (sound waves in the
condensate).

### §5.2: Energy Released per Pair

Using Model B's equilibrium analysis (Part 23 §7.3) as a guide to
the energy scale:

**Step 1:** Particle at the stable minimum of V = −g cos(ψ − φ):

V_particle = −g cos(0) = −g                              ... (5.1)

**Step 2:** Antiparticle at the unstable maximum:

V_antiparticle = −g cos(π) = +g                           ... (5.2)

**Step 3:** Energy released when both reach the vacuum (V = −g):

ΔV = V_antiparticle − V_particle = g − (−g) = 2g         ... (5.3)

**Step 4:** Identifying with the known electron-positron annihilation
energy (2m_e c²):

2g = 2m_e c²

g = m_e c² ≈ 8.19 × 10⁻¹⁴ J ≈ 0.511 MeV                ... (5.4)

**PDTP Original:** The coupling constant g for the electron-spacetime
interaction equals the electron rest energy. This is a self-consistency
identification, not a prediction — we set g = m_e c² to match the known
annihilation energy.

**Dimensional caveat:** The coupling g in the field-theory Lagrangian
has dimensions of [energy density] (energy per unit volume), not [energy].
Equation (5.4) implicitly integrates over the defect volume. The
relevant volume is the defect core (radius ~ healing length ξ), which
is unknown in PDTP. This is a dimensional subtlety that requires the
full vortex solution to resolve.

### §5.3: Two-Photon Requirement

In standard QED, e⁺e⁻ → γ (single photon) is forbidden by simultaneous
conservation of energy and momentum. In the center-of-mass frame, the
initial state has zero total momentum, so the final state must also have
zero momentum. A single photon always carries momentum p = E/c ≠ 0.
Therefore, at least two photons traveling in opposite directions are
required:

e⁺ + e⁻ → γ + γ     (each with E = m_e c² = 0.511 MeV)

**Source:** [Electron–positron annihilation — Wikipedia](https://en.wikipedia.org/wiki/Electron%E2%80%93positron_annihilation)

In PDTP: the φ-radiation produced by vortex-antivortex annihilation must
carry zero net momentum (in the CM frame). Two φ-wave packets traveling
in opposite directions satisfy this. The two-photon requirement follows
from the same momentum conservation that applies in standard physics.

### §5.4: Positronium Lifetime — An Honest Gap

The electron and positron can form a bound state (positronium) before
annihilating. The measured lifetimes are:

- Parapositronium (spin singlet): τ ≈ 125 ps → annihilates to 2γ
- Orthopositronium (spin triplet): τ ≈ 142 ns → annihilates to 3γ

**Source:** [Positronium — Wikipedia](https://en.wikipedia.org/wiki/Positronium)

PDTP cannot currently predict these lifetimes. The coupling constant g
determines the energy released but not the transition rate. Computing
the rate would require a quantum treatment of the φ field (quantizing
the spacetime phase oscillations), which PDTP does not yet have. This
is an honest gap — the framework gives the right energy but not the
right rate.

---

## §6: CPT Symmetry — Explicit Verification

### §6.1: Checking Each Symmetry

The PDTP Lagrangian is:

L = ½(∂_μ φ)(∂^μ φ) + Σᵢ ½(∂_μ ψᵢ)(∂^μ ψᵢ) + Σᵢ gᵢ cos(ψᵢ − φ)

We check T, P, and C separately.

**T (time reversal, t → −t):**

Under T: ∂₀ → −∂₀ (time derivative flips sign).

Kinetic term: ½(∂₀φ)² → ½(−∂₀φ)² = ½(∂₀φ)². Unchanged. ✓

Spatial gradients: ∂ᵢφ → ∂ᵢφ. Unchanged. ✓

Cosine coupling: cos(ψᵢ − φ) → cos(ψᵢ − φ). Unchanged (cos is even,
and neither ψ nor φ are odd under T for real scalar fields). ✓

**Result: L is T-invariant.** ✓

**P (parity, x → −x):**

Under P: ∂ᵢ → −∂ᵢ (spatial derivatives flip sign).

Kinetic term: ½(∂ᵢφ)² → ½(−∂ᵢφ)² = ½(∂ᵢφ)². Unchanged. ✓

Time derivatives: ∂₀φ → ∂₀φ. Unchanged. ✓

Cosine coupling: cos(ψᵢ − φ) → cos(ψᵢ − φ). Unchanged (scalars are
P-even). ✓

**Result: L is P-invariant.** ✓

**C (charge conjugation, n → −n):**

For real scalar fields, there is no natural complex conjugation operation.
In PDTP, C is defined as the map between solutions: a vortex solution
with n = +1 maps to an antivortex solution with n = −1. Since the
Lagrangian depends only on local field values (ψ, φ) and their
derivatives — not on the global winding number — both solutions have
the same Lagrangian density everywhere.

**Result: L is C-invariant.** ✓

**CPT combined:** Since L is separately T-invariant, P-invariant, and
C-invariant, it is also CPT-invariant. This is consistent with the
Lüders-Pauli theorem, which guarantees CPT invariance for any Lorentz-
invariant local Lagrangian.

**PDTP Original:** The PDTP Lagrangian is independently T, P, and C
invariant. CPT holds as a consequence. This is stronger than what the
CPT theorem requires (only the combination must hold) — individual C,
P, and T are each exact symmetries of the PDTP Lagrangian.

### §6.2: CP Violation — A Real Problem

In the Standard Model, CP is violated. This is observed experimentally
in K meson and B meson decays, and is essential for baryogenesis (see
§7). The CP violation in the Standard Model comes from the complex phase
in the CKM matrix (quark mixing matrix).

**Source:** [CP violation — Wikipedia](https://en.wikipedia.org/wiki/CP_violation)

The PDTP Lagrangian has **exact CP symmetry** — there is no mechanism
within the current framework to produce CP violation. This is because:

1. The fields φ and ψ are real scalars (no complex phases to play the
   role of the CKM phase)
2. The cosine coupling is symmetric under ψ − φ → −(ψ − φ)
3. No weak interaction structure (SU(2)_L) is present in the PDTP
   Lagrangian

This is an honest limitation: **PDTP cannot currently produce CP violation.**
Since CP violation is experimentally confirmed and necessary for
baryogenesis, this means either:

(a) CP violation must come from the Standard Model sector (which PDTP
preserves unchanged — see Part 20), or

(b) An extension of the PDTP Lagrangian is needed that introduces a
CP-violating phase (perhaps through complex field structure or explicit
symmetry-breaking terms).

---

## §7: Baryogenesis — Matter-Antimatter Asymmetry

### §7.1: The Problem and the Sakharov Conditions

The Big Bang should have produced equal amounts of matter and antimatter.
If they annihilated completely, the universe would contain only radiation
and no atoms. Instead, the universe is made almost entirely of matter.
The observed baryon-to-photon ratio is:

η = n_b / n_γ ≈ 6.1 × 10⁻¹⁰

meaning roughly one extra baryon survived for every billion photon pairs
produced by annihilation.

**Source:** [Baryogenesis — Wikipedia](https://en.wikipedia.org/wiki/Baryogenesis)

Sakharov (1967) identified three necessary conditions for generating this
asymmetry from initially equal amounts:

1. **Baryon number violation:** some process must change the total number
   of baryons minus antibaryons
2. **C and CP violation:** the process must distinguish matter from
   antimatter
3. **Departure from thermal equilibrium:** otherwise, every baryon-creating
   process would be balanced by its reverse

**Source:** Sakharov, A. D. (1967), "Violation of CP invariance, C
asymmetry, and baryon asymmetry of the Universe," *JETP Letters* 5, 24.

The Standard Model satisfies all three conditions in principle (sphaleron
processes violate B, CKM phase violates CP, electroweak phase transition
provides non-equilibrium), but the predicted asymmetry is too small by
many orders of magnitude. Baryogenesis remains an open problem.

### §7.2: PDTP Reframing

The PDTP framework (as discussed in
[phase_framework_mysteries.md](phase_framework_mysteries.md) §2) reframes
the problem as follows:

If particles are defects with winding n = +1 and antiparticles have
n = −1, the matter-antimatter asymmetry becomes: **why did slightly more
n = +1 defects form than n = −1?**

The phase-locking mechanism offers a qualitative story:

1. In the early universe, the condensate phase φ is rapidly fluctuating
   (high temperature → thermal fluctuations dominate).

2. As the universe cools below some critical temperature T_c, the
   condensate undergoes a phase transition (analogous to BKT). Defects
   form via the Kibble-Zurek mechanism — vortices and antivortices
   nucleate in roughly equal numbers.

3. If a small initial bias exists (slightly more n = +1 than n = −1),
   phase-locking amplifies it: the background φ field aligns with the
   majority, making it energetically slightly easier to form more n = +1
   defects. Positive feedback.

4. After most vortex-antivortex pairs annihilate, the small excess of
   n = +1 defects survives as the observed matter.

**PDTP Speculative:** This mechanism is qualitatively appealing but
has not been derived from the PDTP field equations. The "small initial
bias" is assumed, not explained.

### §7.3: Honest Assessment — Sakharov Conditions in PDTP

| Sakharov condition | PDTP status | Assessment |
|:-------------------|:------------|:-----------|
| Baryon number violation | Winding number is topologically conserved → no B violation | **Fails** |
| C and CP violation | Lagrangian has exact C and CP symmetry (§6) | **Fails** |
| Departure from equilibrium | Phase transition (BKT-like) could provide this | **Partial** |

**Honest conclusion:** The PDTP Lagrangian in its current form does NOT
satisfy the Sakharov conditions. The topological conservation of winding
number — which is a strength for explaining charge conservation — is a
weakness for baryogenesis, because it forbids the creation of net baryon
number.

Possible resolutions (all speculative and undeveloped):

1. **Winding number non-conservation at high energy:** If the lattice
   spacing a ~ ℓ_P provides a UV cutoff, topology may not be conserved
   at Planck-scale energies. The defect cores could overlap and exchange
   winding number.

2. **CP violation from Standard Model sector:** PDTP preserves the full
   SM gauge structure (Part 20). CP violation from the CKM matrix is
   still present. Baryogenesis may occur through the SM mechanism
   (sphalerons + CKM phase) without needing the PDTP sector at all.

3. **Extended Lagrangian with complex fields:** If ψ were a complex
   field rather than a real scalar, a CP-violating phase could be
   introduced.

None of these have been developed. Baryogenesis remains an open problem
in PDTP, just as it remains open in the Standard Model.

---

## §8: Gravity of Antimatter — ALPHA-g Consistency Check

### §8.1: What ALPHA Measured

The ALPHA-g experiment (§2.4) measured the gravitational acceleration of
antihydrogen to be consistent with g, with ~20% precision. The key result:

g_anti / g = 0.75 ± 0.13 (stat+syst) ± 0.16 (simulation)

This is consistent with 1.0 (antimatter falls down at the same rate as
matter) and rules out gravitational repulsion (g_anti < 0) at high
confidence.

### §8.2: PDTP Predicts Equal Gravitational Coupling

**Model A (winding):** The gravitational force on a defect comes from the
gradient of the spacetime phase φ (see Part 11, momentum balance). The
field equation for φ is:

□φ = Σᵢ gᵢ sin(ψᵢ − φ)                                   ... (8.1)

The force on particle i depends on the gradient ∇φ generated by all other
matter. The coupling cos(ψᵢ − φ) determines how strongly particle i
responds to the spacetime field. Neither the source term sin(ψᵢ − φ) nor
the coupling cos(ψᵢ − φ) depends on the winding number n of particle i.

Explicitly: a defect with n = +1 (phase winding +2π around the core) has
the same local coupling to φ as a defect with n = −1 (phase winding −2π).
The coupling depends on the local value of ψ − φ, not on the global
winding.

**Model B (trough):** A particle at ψ = φ (crest) has coupling:

α_particle = cos(φ − φ) = cos(0) = 1                      ... (8.2)

An antiparticle at ψ = φ + π (trough) has coupling:

α_antiparticle = cos((φ + π) − φ) = cos(π) = −1           ... (8.3)

The gravitational acceleration is proportional to −g sin(ψ − φ) × ∇φ.
For both equilibria, sin(ψ − φ) = 0, so the restoring force vanishes and
both particle and antiparticle follow the same gravitational gradient ∇φ.
More precisely: for a small displacement δ from either equilibrium, the
linearized equation of motion gives the same acceleration from the
background gradient of φ.

**PDTP Original:** Both Model A and Model B predict identical gravitational
acceleration for matter and antimatter. The PDTP coupling is symmetric
under C conjugation (§4.4). Antimatter falls down.

### §8.3: PDTP Prediction for Future Measurements

PDTP predicts:

g_anti / g = 1.000 (exactly, within the framework)        ... (8.4)

This prediction is testable: future ALPHA-g runs aim for ~1% precision.
If a deviation from unity is found, it would require a modification to
the cosine coupling that distinguishes n = +1 from n = −1 defects. No
such modification currently exists in the PDTP framework.

**PDTP Original:** The prediction g_anti = g is a consequence of the
C-invariance of the Lagrangian (§6.1). It is a consistency check, not
a unique prediction — GR and virtually all metric theories of gravity
also predict g_anti = g via the equivalence principle.

---

## §9: Honest Assessment

| Question | PDTP answer | Works? | Notes |
|:---------|:-----------|:------:|:------|
| What is antimatter? | Opposite winding (n = −1) defect | ✓ | Consistent with QFT picture |
| Why opposite charge? | Winding number is the conserved charge | ✓ | Topological conservation = Noether charge |
| Models A and B compatible? | Different objects (topology vs dynamics) | Clarified | Model A = antiparticle; Model B = domain excitation |
| Annihilation energy | Winding cancellation releases 2g = 2mc² | ✓ | Self-consistent identification |
| Two-photon requirement | Momentum conservation (same as standard) | ✓ | Not a new prediction |
| CPT symmetry | Lagrangian is C, P, T invariant | ✓ | Stronger than CPT theorem requires |
| CP violation | Lagrangian has exact CP symmetry | **✗** | Blocks Sakharov baryogenesis |
| Baryogenesis | Phase bias + phase-locking amplification | Suggestive | Does not satisfy Sakharov conditions |
| Antimatter gravity | Both models predict g_anti = g | ✓ | Consistent with ALPHA-g (2023) |
| Positronium lifetime | Not predicted | **✗** | Needs quantum φ treatment |
| Antiparticle mass = particle mass | CPT → same mass (same defect energy) | ✓ | Structural, not independently derived |
| Vortex profile solution | Not computed | Open | Requires solving □φ with boundary conditions |

**Key strengths:**
- Charge quantization from topology (integers only, automatically)
- Charge conservation from topological protection (robust)
- Annihilation as winding cancellation (natural geometric picture)
- Antimatter gravity consistent with ALPHA-g (trivially)

**Key gaps:**
- CP violation absent → baryogenesis mechanism missing
- Positronium lifetime not predictable (no quantum φ)
- Dimensional subtlety in g = mc² identification
- Vortex solution not explicitly computed

**Honest status:** The PDTP antimatter picture is structurally consistent
with known physics but does not make new quantitative predictions beyond
what the Standard Model already provides. The topological charge
interpretation is elegant but has the trade-off of making baryogenesis
harder (winding conservation blocks baryon number violation).

---

## §10: References

### Wikipedia (established physics)

| # | Article | URL | Used for |
|:--|:--------|:----|:---------|
| 292 | Antimatter | [Link](https://en.wikipedia.org/wiki/Antimatter) | General antimatter overview |
| 293 | Dirac equation | [Link](https://en.wikipedia.org/wiki/Dirac_equation) | Antiparticle prediction |
| 294 | CPT symmetry | [Link](https://en.wikipedia.org/wiki/CPT_symmetry) | CPT theorem statement |
| 295 | Pair production | [Link](https://en.wikipedia.org/wiki/Pair_production) | e⁺e⁻ creation threshold |
| 296 | Electron–positron annihilation | [Link](https://en.wikipedia.org/wiki/Electron%E2%80%93positron_annihilation) | Annihilation to 2γ |
| 297 | Positronium | [Link](https://en.wikipedia.org/wiki/Positronium) | Bound state lifetimes |
| 298 | Quantum vortex | [Link](https://en.wikipedia.org/wiki/Quantum_vortex) | BEC vortex physics |
| 299 | Berezinskii–Kosterlitz–Thouless transition | [Link](https://en.wikipedia.org/wiki/Berezinskii%E2%80%93Kosterlitz%E2%80%93Thouless_transition) | Vortex-antivortex unbinding |
| 300 | Baryogenesis | [Link](https://en.wikipedia.org/wiki/Baryogenesis) | Sakharov conditions |
| 301 | CP violation | [Link](https://en.wikipedia.org/wiki/CP_violation) | Observed CP violation |

### Academic papers

| # | Reference | Used for |
|:--|:----------|:---------|
| 80 | Anderson, C. D. (1933), "The Positive Electron," *Phys. Rev.* 43, 491 | Positron discovery |
| 81 | Dirac, P. A. M. (1928), "The Quantum Theory of the Electron," *Proc. Roy. Soc. A* 117, 610 | Antiparticle prediction |
| 82 | ALPHA Collaboration (2023), "Observation of the effect of gravity on the motion of antimatter," *Nature* 621, 716 | ALPHA-g result |
| 83 | Sakharov, A. D. (1967), "Violation of CP invariance, C asymmetry, and baryon asymmetry of the Universe," *JETP Lett.* 5, 24 | Sakharov conditions |

### Internal references

| Part | Document | Used for |
|:-----|:---------|:---------|
| 1 | [mathematical_formalization.md](mathematical_formalization.md) | Lagrangian, field equations |
| 11 | [momentum_balance.md](momentum_balance.md) | Gravitational force from ∇φ |
| 12 | [tetrad_extension.md](tetrad_extension.md) | φ-waves as photons |
| 14 | [condensate_microphysics.md](condensate_microphysics.md) | Condensate = BEC analogy |
| 18 | [aharonov_bohm_pdtp.md](aharonov_bohm_pdtp.md) | U(1) topology, vortex lines |
| 20 | [standard_model_pdtp_mapping.md](standard_model_pdtp_mapping.md) | SM preserved in PDTP |
| 21 | [efv_microphysics.md](efv_microphysics.md) | Lattice, healing length |
| 23 | [charge_quantum_numbers.md](charge_quantum_numbers.md) | Winding numbers, Z₃ structure |

### PDTP Original and Speculative Results

| Result | Section | Type |
|:-------|:--------|:-----|
| Models A and B are different objects (topology vs dynamics) | §4.2 | PDTP Original |
| C conjugation = winding flip n → −n | §4.4 | PDTP Original |
| Lagrangian is separately C, P, T invariant | §6.1 | PDTP Original |
| g = m_e c² identification for electron coupling | §5.2 | PDTP Original |
| g_anti / g = 1.000 prediction | §8.3 | PDTP Original |
| Two-level picture: winding (topology) + trough (dynamics) | §4.3 | PDTP Speculative |
| Phase-bias mechanism for baryogenesis | §7.2 | PDTP Speculative |
| Winding non-conservation at Planck energies | §7.3 | PDTP Speculative |
