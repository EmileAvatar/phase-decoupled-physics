# Deriving Newton's Constant from Condensate Properties

**Status:** Partial resolution — reduces circularity from two free parameters to one
**Date:** 2026-02-16
**Prerequisites:** [mathematical_formalization.md](mathematical_formalization.md) §7,
[hard_problems.md](hard_problems.md) §2.5–2.11,
[advanced_formalization.md](advanced_formalization.md) §1.4–1.5

---

## 1. The Circularity Problem

### 1.1 Statement of the Problem

In [mathematical_formalization.md](mathematical_formalization.md) §7.5, Newton's
constant G enters through the identification:

$$\rho_{\text{phase}}(x) = \sum_i g_i (\psi_i - \phi) \quad \longleftrightarrow \quad 4\pi G \,\rho_{\text{mass}}$$

This maps the PDTP source term onto the Newtonian Poisson equation. But the mapping
*assumes* we already know what G is — we use the GR/Newtonian answer to calibrate
the PDTP parameter. The same circularity appears in §8.2, where the decoupling
energy per particle is estimated via E ~ Gm²/R, which again presupposes G.

**Source:** [mathematical_formalization.md](mathematical_formalization.md) §7.5,
equations (7.3)–(7.6)

### 1.2 What Would a Non-Circular Derivation Look Like?

A genuine derivation of G would express it purely in terms of condensate properties:

$$G = f(\rho_0, c_s, \hbar, \text{condensate microphysics})$$

where ρ₀ is the vacuum condensate density and c_s is the speed of sound in the
condensate (= c, as required by Lorentz invariance — see
[hard_problems.md](hard_problems.md) §2.11).

**Analogy:** In BEC analogue gravity, the analogue Newton's constant G_analogue is
fully determined by the atomic mass, scattering length, and condensate density — no
external calibration is needed.

**Source:** Barceló, Liberati & Visser (2005), "Analogue Gravity",
[arXiv:gr-qc/0505065](https://arxiv.org/abs/gr-qc/0505065)

---

## 2. Dimensional Analysis Constraints

### 2.1 Available Condensate Parameters

The PDTP condensate is characterized by:

| Parameter | Symbol | Dimensions | Status |
|-----------|--------|-----------|--------|
| Condensate density | ρ₀ | [mass/length³] | Unknown; "sets the Planck scale" |
| Speed of sound | c_s | [length/time] | = c (required by Lorentz invariance) |
| Reduced Planck constant | ℏ | [mass·length²/time] | Known: 1.055 × 10⁻³⁴ J·s |
| Coupling constants | gᵢ | See §3 | Related to particle mass |

**Source:** [advanced_formalization.md](advanced_formalization.md) §1.5, §1.7

### 2.2 Dimensional Argument

Newton's constant has dimensions:

$$[G] = \frac{\text{length}^3}{\text{mass} \cdot \text{time}^2}$$

From the available condensate parameters {ρ₀, c_s, ℏ}, the unique combination with
these dimensions is:

$$G \sim \frac{c_s^a \, \hbar^b}{\rho_0^d}$$

**Source:** Standard dimensional analysis,
[Wikipedia: Dimensional analysis](https://en.wikipedia.org/wiki/Dimensional_analysis)

Solving the system:

- length: 3 = a + 2b + 3d → (from [G] numerator)
- mass: -1 = b - d → (from [G] denominator)
- time: -2 = -a - b → (from [G] denominator)

From the third equation: a + b = 2.
From the second: d = b + 1.
Substituting into the first: 3 = a + 2b + 3(b+1) = a + 5b + 3, so a = -5b.
Combined with a + b = 2: -5b + b = 2, so b = -1/2, a = 5/2, d = 1/2.

Therefore:

$$\boxed{G \sim \frac{c_s^{5/2} \, \hbar^{-1/2}}{\rho_0^{1/2}}}$$

**(2.1)**

Or equivalently:

$$G \sim \frac{c^{5/2}}{\sqrt{\hbar \, \rho_0}}$$

**PDTP Original:** This dimensional constraint on G in terms of condensate parameters.

### 2.3 Consistency Check with Planck Units

In Planck units, G = ℓ_P³/(m_P t_P²) and the Planck density is
ρ_P = m_P/ℓ_P³ = c⁵/(ℏG²).

**Source:** [Wikipedia: Planck units](https://en.wikipedia.org/wiki/Planck_units)

Check equation (2.1):

$$\frac{c^{5/2}}{\sqrt{\hbar \rho_P}} = \frac{c^{5/2}}{\sqrt{\hbar \cdot c^5/(\hbar G^2)}} = \frac{c^{5/2}}{\sqrt{c^5/G^2}} = \frac{c^{5/2}}{c^{5/2}/G} = G \quad \checkmark$$

So equation (2.1) is exact (not just "~") if ρ₀ = ρ_P. This gives:

$$\boxed{G = \frac{c^{5/2}}{\sqrt{\hbar \, \rho_0}}}$$

**(2.2)**

**if and only if** the dimensionless prefactor is exactly 1.

### 2.4 What This Tells Us

Equation (2.2) inverted gives:

$$\rho_0 = \frac{c^5}{\hbar \, G^2} = \rho_{\text{Planck}} \approx 5.16 \times 10^{96} \;\text{kg/m}^3$$

**Source:** [Wikipedia: Planck density](https://en.wikipedia.org/wiki/Planck_units#Planck_density)

**Interpretation:** If G is determined by condensate parameters alone, the condensate
density must be of order the Planck density. This is consistent with the statement
in [advanced_formalization.md](advanced_formalization.md) §1.7 that "ρ₀ sets the
Planck scale."

**PDTP Original:** Identification of ρ₀ = ρ_Planck as the consistency condition for
G to emerge from condensate dynamics.

---

## 3. The Coupling-Mass Relation

### 3.1 From De Broglie to Coupling Strength

Each matter field ψᵢ has the de Broglie frequency:

$$\omega_i = \frac{m_i c^2}{\hbar}$$

**Source:** [Wikipedia: Matter wave](https://en.wikipedia.org/wiki/Matter_wave)

The PDTP coupling gᵢ determines how strongly particle i's phase couples to the
condensate phase φ. The field equation is:

$$\Box \phi = \sum_i g_i \sin(\psi_i - \phi)$$

**Source:** [mathematical_formalization.md](mathematical_formalization.md) §3,
equation (3.1)

### 3.2 Dimensional Analysis of gᵢ

In the field equation □φ = Σ gᵢ sin(ψᵢ - φ), the left side has dimensions
[1/length²] (since φ is dimensionless and □ = ∂²). Therefore gᵢ must also have
dimensions [1/length²] for a point-like source, or be dimensionless if it represents
a coupling density integrated over space.

For a localized particle, the source term acts as:

$$g_i \sin(\psi_i - \phi) \;\to\; g_i (\psi_i - \phi) \, \delta^3(\mathbf{x} - \mathbf{x}_i)$$

in the weak-field limit, with gᵢ having dimensions [length] (to compensate the
delta function [1/length³] and produce [1/length²]).

### 3.3 Matching to Poisson's Equation

The Newtonian identification requires (from §7.5 of mathematical_formalization.md):

$$\nabla^2 \phi = \sum_i g_i (\psi_i - \phi) \delta^3(\mathbf{x} - \mathbf{x}_i)$$

With the mapping Φ_N = c² φ and comparison to ∇²Φ_N = 4πGρ:

$$c^2 \sum_i g_i \, \delta\psi_i \, \delta^3(\mathbf{x} - \mathbf{x}_i) = 4\pi G \sum_i m_i \, \delta^3(\mathbf{x} - \mathbf{x}_i)$$

Therefore for each particle:

$$g_i \, \delta\psi_i = \frac{4\pi G \, m_i}{c^2}$$

**(3.1)**

where δψᵢ = ψᵢ − φ is the phase difference at the particle's location.

### 3.4 The Self-Consistent Phase Difference

The phase difference δψᵢ is not a free parameter — it is determined self-consistently
by the field equations. For a static, spherically symmetric mass:

From the solution φ(r) = -GM/(rc²) outside the mass (equation (7.2) of
mathematical_formalization.md), and ψ ≈ const inside the mass (locked phase), the
phase difference at the particle boundary R is:

$$\delta\psi \sim \frac{GM}{Rc^2}$$

Substituting into (3.1):

$$g_i \cdot \frac{G m_i}{R_i c^2} = \frac{4\pi G m_i}{c^2}$$

$$\boxed{g_i = \frac{4\pi R_i \, G m_i}{c^2 \, \delta\psi_i} \sim 4\pi R_i}$$

**(3.2)**

Wait — the mass and G cancel! This suggests gᵢ is determined by the geometric size
Rᵢ of the source, not directly by its mass. The mass enters through the phase
difference δψ, which is self-consistently determined.

**PDTP Original:** This self-consistency relation between coupling strength and
geometric size.

### 3.5 Interpretation

Equation (3.2) reveals something important: **the coupling constant gᵢ is not an
independent parameter per particle.** Once the field equations are solved
self-consistently:

- The mass m determines δψ (through the field equation)
- δψ determines how strongly the source acts (through the sin coupling)
- gᵢ characterizes the *spatial extent* of the coupling, not its strength

This partially resolves the circularity: gᵢ is geometric, and the gravitational
strength is encoded in δψ, which emerges from solving the field equations — not
from external input.

---

## 4. G from the Acoustic Metric

### 4.1 The Acoustic Metric Approach

The PDTP acoustic metric is:

$$g_{\mu\nu}^{\text{acoustic}} = \frac{\rho_0}{c_s} \begin{pmatrix} -(c_s^2 - v^2) & -v_j \\ -v_i & \delta_{ij} \end{pmatrix}$$

**Source:** [advanced_formalization.md](advanced_formalization.md) §1.4;
Unruh (1981), "Experimental black-hole evaporation?",
[DOI:10.1103/PhysRevLett.46.1351](https://doi.org/10.1103/PhysRevLett.46.1351)

With c_s = c (Lorentz-invariant condensate), the conformal prefactor is ρ₀/c.

### 4.2 Deriving the Effective Einstein Equation

For the acoustic metric to reproduce linearized GR in the weak-field limit:

$$g_{00} \approx -\left(1 - \frac{2\Phi_N}{c^2}\right)$$

**Source:** [Wikipedia: Linearized gravity](https://en.wikipedia.org/wiki/Linearized_gravity)

The acoustic metric gives:

$$g_{00} = \frac{\rho_0}{c}(-(c^2 - v^2)) \approx -\rho_0 c\left(1 - \frac{v^2}{c^2}\right)$$

For the normalization g₀₀ → -1 at spatial infinity (flat space), we need:

$$\rho_0 \, c = 1 \quad \text{(in geometric units)}$$

**(4.1)**

Or in SI units, ρ₀ c has the dimensions of [mass/(length²·time)] and must equal the
appropriate normalization constant.

### 4.3 The Velocity-Potential Relation

The superfluid velocity is:

$$v_i = \frac{\hbar}{m_{\text{cond}}} \partial_i \phi$$

**Source:** [Wikipedia: Superfluid helium-4](https://en.wikipedia.org/wiki/Superfluid_helium-4),
equation for superfluid velocity

where m_cond is the mass of the condensate constituent (unknown in PDTP).

In the weak-field regime, v ≪ c, and:

$$\frac{v^2}{c^2} = \frac{\hbar^2}{m_{\text{cond}}^2 c^2} |\nabla\phi|^2 = \frac{2\Phi_N}{c^2}$$

For the Newtonian potential Φ_N = -GM/r:

$$|\nabla\Phi_N| = \frac{GM}{r^2}$$

The velocity-potential relation connects the condensate microphysics (m_cond) to the
gravitational field through ℏ.

### 4.4 G in Terms of Condensate Parameters

Combining the acoustic metric normalization (4.1), the velocity-potential relation,
and the Poisson equation:

The density perturbation from [hard_problems.md](hard_problems.md) §2.5:

$$\frac{\delta\rho}{\rho_0} = -\frac{\Phi_N}{c_s^2} = -\frac{\Phi_N}{c^2}$$

**Source:** [hard_problems.md](hard_problems.md) §2.5, equation for hydrostatic
equilibrium perturbation

The condensate Euler equation (from
[radiation_era_cosmology.md](radiation_era_cosmology.md) §2.3) in the static limit
becomes the hydrostatic equilibrium:

$$\nabla P = -\rho \nabla\Phi_N$$

With equation of state P = c_s² ρ = c² ρ:

$$c^2 \nabla\rho = -\rho_0 \nabla\Phi_N$$

$$c^2 \nabla^2\rho = -\rho_0 \nabla^2\Phi_N = -\rho_0 (4\pi G \rho_{\text{mass}})$$

**(4.2)**

This is a self-consistency relation: the condensate density perturbation δρ is
sourced by matter through G, and G itself is determined by how the condensate
responds to perturbations.

### 4.5 The Healing Length Connection

The PDTP phase field has a dispersion relation (from
[hard_problems.md](hard_problems.md) §3.2):

$$\omega^2 = c^2 k^2 + 2g$$

**Source:** [hard_problems.md](hard_problems.md) §3.2, equation for constraint 3

This defines a healing length (the scale below which the condensate resists
perturbation):

$$\xi = \frac{c}{\sqrt{2g}} = \frac{1}{m_\phi}$$

**Source:** [Wikipedia: Healing length](https://en.wikipedia.org/wiki/Healing_length)
(BEC analogy)

In BEC analogue gravity, the analogue Newton's constant is:

$$G_{\text{BEC}} \sim \frac{c_s^3}{\rho_0 \, \xi^2 \, c_s} = \frac{c_s^2}{\rho_0 \, \xi^2}$$

**Source:** Barceló, Liberati & Visser (2005), §5.1, equation for effective
gravitational coupling in analogue systems

For PDTP with c_s = c:

$$G \sim \frac{c^2}{\rho_0 \, \xi^2}$$

**(4.3)**

But for Newtonian gravity (infinite range, 1/r potential), we need ξ → ∞, which
sends G → 0. This means the BEC-analogy formula (4.3) applies to a *massive*
graviton scenario (Yukawa potential with range ξ), not to standard gravity.

**For massless gravity (g → 0 in vacuum, ξ → ∞):**

The coupling g is zero in vacuum and nonzero only inside matter. The healing length
is not a global property but a local one. G is then set by the global condensate
parameter ρ₀ alone, as in the dimensional analysis of §2:

$$G = \frac{c^{5/2}}{\sqrt{\hbar \, \rho_0}} \times (\text{dimensionless prefactor})$$

**(4.4)**

The dimensionless prefactor must be determined by the full nonlinear condensate
dynamics, which are not yet specified.

**PDTP Original:** Connection between healing length, analogue G, and the massless
gravity limit.

---

## 5. Reduction of Free Parameters

### 5.1 Before This Analysis

The PDTP framework had the following free parameters:

| Parameter | Status |
|-----------|--------|
| ρ₀ (condensate density) | Unknown |
| c_s (speed of sound) | Fixed: c_s = c |
| gᵢ (coupling per particle) | Unknown; one per particle species |
| G (Newton's constant) | Matched to observation |

Total: 1 (ρ₀) + N (couplings gᵢ) + 1 (G) free parameters, with one constraint
(the Poisson equation match), leaving N + 1 unknowns.

### 5.2 After This Analysis

The results above impose new constraints:

**Constraint 1 (§2.2):** G is determined by ρ₀ up to a dimensionless prefactor:

$$G = \mathcal{C} \cdot \frac{c^{5/2}}{\sqrt{\hbar \, \rho_0}}$$

where 𝒞 is an O(1) constant determined by the full condensate dynamics.

**Constraint 2 (§3.4):** The coupling gᵢ is geometric — determined by the spatial
extent of the source, not an independent parameter:

$$g_i \sim 4\pi R_i$$

**Constraint 3 (§2.4):** Consistency requires ρ₀ ~ ρ_Planck.

**Reduced parameter count:**

| Parameter | Status |
|-----------|--------|
| ρ₀ | Constrained to ~ ρ_Planck by §2.4 |
| c_s | Fixed: c_s = c |
| gᵢ | Determined geometrically by §3.4 |
| G | Determined by ρ₀ via §2.2 |
| 𝒞 | O(1) prefactor; requires microscopic theory |

**Effective free parameters: 1** (either ρ₀ or equivalently 𝒞)

**PDTP Original:** Reduction from N+2 apparent parameters to 1 effective free
parameter.

### 5.3 Comparison: How Other Theories Handle G

| Theory | How G enters | Free parameters |
|--------|-------------|-----------------|
| **GR** | Fundamental constant; no derivation | G is input |
| **Brans-Dicke** | G = 1/Φ where Φ is a scalar field; Φ determined by matter + ω parameter | ω (dimensionless) |
| **String theory** | G ~ g_s² α'⁴/V₆ (string coupling, string length, compact volume) | g_s, α', V₆ |
| **Loop quantum gravity** | G is input; discreteness scale ~ ℓ_P = √(ℏG/c³) | G is input |
| **BEC analogue** | G_analogue = f(a_s, m_atom, n₀) fully determined by microphysics | 0 (all measurable) |
| **PDTP** | G = 𝒞 c^(5/2)/√(ℏρ₀), with ρ₀ ~ ρ_Planck | 1 (𝒞 or ρ₀) |

**Source:** Brans & Dicke (1961), "Mach's Principle and a Relativistic Theory of
Gravitation", [DOI:10.1103/PhysRev.124.925](https://doi.org/10.1103/PhysRev.124.925)

**PDTP Original:** This comparative analysis.

---

## 6. What Would Fully Determine G?

### 6.1 The Missing Ingredient: Condensate Microphysics

The one remaining free parameter (ρ₀ or 𝒞) encodes the microphysics of the vacuum
condensate — the analogue of knowing the atomic mass and scattering length in a BEC.

To fully determine G, PDTP would need to specify:

1. **What condenses:** The microscopic degrees of freedom (analogous to atoms in He-4)
2. **The interaction:** The self-interaction that causes condensation
3. **The ground state:** The condensate wavefunction Ψ₀ = √ρ₀ exp(iφ₀)

From these, ρ₀ would be calculable, and G would follow from equation (2.2).

**Source:** [advanced_formalization.md](advanced_formalization.md) §1.7 identifies
these as the deepest open questions in PDTP.

### 6.2 The Planck Density Prediction

Even without the microphysics, the dimensional analysis provides a *prediction*:

$$\rho_0 = \frac{c^5}{\hbar G^2 \mathcal{C}^2}$$

If 𝒞 = 1, then ρ₀ = ρ_Planck ≈ 5.16 × 10⁹⁶ kg/m³.

This is testable in principle: any independent measurement or theoretical
determination of ρ₀ would either confirm or falsify this prediction.

**Comparison with the cosmological constant problem:**

The observed vacuum energy density is ρ_vacuum ~ 10⁻²⁶ kg/m³, which differs from
ρ_Planck by a factor of ~10¹²². In PDTP, ρ₀ is the *total* condensate density (not
the vacuum energy measured by expansion), so this discrepancy may not apply directly.
The cosmological constant in PDTP would correspond to small perturbations of ρ₀,
not ρ₀ itself.

**Source:** [Wikipedia: Cosmological constant problem](https://en.wikipedia.org/wiki/Cosmological_constant_problem)

**PDTP Original:** Distinction between condensate density ρ₀ and vacuum energy
density ρ_vacuum as a possible reframing of the cosmological constant problem.

### 6.3 Roadmap for Full Derivation

A complete derivation of G would require:

1. **Specify condensate constituents** — What are the "atoms" of the vacuum?
   Candidates: Planck-scale degrees of freedom, spin-network nodes, pre-geometric
   elements.

2. **Derive the condensation mechanism** — Why does the vacuum form a condensate?
   In BEC: Bose-Einstein statistics + low temperature. In PDTP: unknown.

3. **Calculate ρ₀ from the microscopic theory** — Given the constituents and their
   interactions, compute the ground-state condensate density.

4. **Derive 𝒞** — Solve the full nonlinear condensate equations to determine the
   exact prefactor relating G to ρ₀.

**Status:** Steps 1–4 are the deepest open problems in PDTP. They are analogous to
deriving atomic physics from the Standard Model — correct in principle, but
technically far beyond current capability.

---

## 7. Resolution of the Energy-Cost Circularity

### 7.1 The Original Problem

In [mathematical_formalization.md](mathematical_formalization.md) §8.2, the
decoupling energy was estimated as:

$$E_{\text{decouple}} \sim g_j \sim \frac{G m_j^2}{R_j}$$

This uses G to estimate gⱼ — circular if gⱼ is supposed to determine G.

### 7.2 Resolution Using §3 Results

From §3.4, gᵢ ~ 4πRᵢ (geometric). The decoupling energy from the Hamiltonian
([mathematical_formalization.md](mathematical_formalization.md) §5.1) is:

$$E_{\text{decouple}} = g_i [1 - \cos(\psi_i - \phi)]$$

At full decoupling (ψᵢ − φ = π/2):

$$E_{\text{decouple}} = g_i = 4\pi R_i$$

This is *not* circular: the decoupling energy is determined by the geometric size
of the object, with no reference to G. The previous estimate E ~ Gm²/R was a
convenient approximation, not a definition.

**However:** The numerical value of Rᵢ for a fundamental particle is itself unclear
(is it the Compton wavelength? The Schwarzschild radius? The classical radius?). So
the circularity is softened but not fully eliminated at the fundamental particle
level.

### 7.3 For Composite Objects

For macroscopic objects (mass M, radius R), the total decoupling energy is:

$$E_{\text{decouple}} = \sum_i g_i [1 - \cos(\psi_i - \phi)] \approx \sum_i g_i \cdot \frac{(\delta\psi_i)^2}{2}$$

With δψᵢ ~ GM/(Rc²) and gᵢ ~ 4πRᵢ per constituent:

$$E_{\text{decouple}} \sim N \cdot 4\pi R_{\text{particle}} \cdot \frac{G^2 M^2}{2R^2 c^4}$$

This depends on G but is now a *prediction* (given G from §2.2), not a circular
definition.

**PDTP Original:** Resolution of the energy-cost circularity via geometric coupling.

---

## 8. Summary

### 8.1 What Was Achieved

| Question | Answer | Section |
|----------|--------|---------|
| Can G be expressed in terms of condensate parameters? | Yes: G = 𝒞 c^(5/2)/√(ℏρ₀) | §2 |
| What determines ρ₀? | Must be ~ ρ_Planck for consistency | §2.4 |
| Are the gᵢ independent parameters? | No — they are geometric (~ 4πRᵢ) | §3 |
| Is the circularity fully resolved? | Partially — reduced to one unknown (𝒞 or ρ₀) | §5 |
| What would complete the derivation? | Microscopic theory of the vacuum condensate | §6 |

### 8.2 Honest Assessment

**Progress:**
- The apparent N+2 free parameters are reduced to 1
- G is constrained by dimensional analysis to depend on ρ₀ in a specific way
- The coupling constants gᵢ are not independent — they're determined geometrically
- The energy-cost estimate is no longer circular

**Remaining gap:**
- The dimensionless prefactor 𝒞 is undetermined without condensate microphysics
- ρ₀ ~ ρ_Planck is a consistency condition, not a derivation
- The geometric coupling gᵢ ~ 4πRᵢ raises the question of what "Rᵢ" means for a
  fundamental particle
- A truly non-circular derivation requires specifying what the vacuum condensate
  is *made of* — the deepest unsolved problem in this framework

**Comparison with standard physics:** GR does not derive G at all; it is a measured
input. PDTP at least provides a *framework* in which G could in principle be
derived, even if the derivation is incomplete. This is analogous to how QCD provides
a framework for deriving hadron masses from quark masses and αₛ, even though αₛ
itself is measured.

---

## 9. References

### Established Physics Sources
- [Wikipedia: Dimensional analysis](https://en.wikipedia.org/wiki/Dimensional_analysis)
- [Wikipedia: Planck units](https://en.wikipedia.org/wiki/Planck_units)
- [Wikipedia: Matter wave](https://en.wikipedia.org/wiki/Matter_wave)
- [Wikipedia: Linearized gravity](https://en.wikipedia.org/wiki/Linearized_gravity)
- [Wikipedia: Healing length](https://en.wikipedia.org/wiki/Healing_length)
- [Wikipedia: Superfluid helium-4](https://en.wikipedia.org/wiki/Superfluid_helium-4)
- [Wikipedia: Cosmological constant problem](https://en.wikipedia.org/wiki/Cosmological_constant_problem)

### Academic Papers
- Unruh, W. G. (1981), "Experimental black-hole evaporation?",
  *Physical Review Letters* **46**, 1351.
  [DOI:10.1103/PhysRevLett.46.1351](https://doi.org/10.1103/PhysRevLett.46.1351)
- Barceló, C., Liberati, S. & Visser, M. (2005), "Analogue Gravity",
  *Living Reviews in Relativity* **8**, 12.
  [arXiv:gr-qc/0505065](https://arxiv.org/abs/gr-qc/0505065)
- Brans, C. & Dicke, R. H. (1961), "Mach's Principle and a Relativistic Theory
  of Gravitation", *Physical Review* **124**, 925.
  [DOI:10.1103/PhysRev.124.925](https://doi.org/10.1103/PhysRev.124.925)

---

End of G_derivation.md
