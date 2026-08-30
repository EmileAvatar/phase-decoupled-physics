# E2-E8 — Phase 1 Core Physics Pages Review

**Source:** elastic-universe.org (7 pages, see per-section URLs below)
**Date reviewed:** 2026-08-30
**Tag:** [EXTERNAL]
**Method:** WebFetch per page, extracting (a) equations, (b) physical claims,
(c) visualization/simulation code, (d) PDTP relevance — per TODO_Elastic.md's
own review criteria.
**Supersedes in part:** `E9_big_picture_guide.md`'s verdict "no Lagrangian" —
see Sec 8 below. The site has evidently been updated since the 2026-04-11 E9
review; the Technical Summary page now carries a substantial mathematical
apparatus that was not present (or not found) in the earlier pass.

---

## E2. Technical Summary
**URL:** https://elastic-universe.org/technical-summary/

By far the most mathematically developed page on the site — this is where
their actual formalism lives.

**Equations (selected, full list is long):**
- Kinematics: `x(X,t) = X + u(X,t)`, strain `eps = (1/2)(grad(u) + grad(u)^T)`
- Eigenstrain/charge: `chi = tr(eps*)`, `Q ~ Delta_V = INT chi dV`
- Stress: `sigma = lambda*tr(eps-eps*)*I + 2*mu*(eps-eps*)`
- Momentum balance: `rho*d2u/dt2 = div(sigma)`
- **Lagrangian:** `L = (1/2)*rho*|du/dt|^2 - mu*eps_dev:eps_dev + p*(div(u)-chi) + L_core[eps*,...]`
- EM mapping: `phi = kappa_phi * p`, `A = kappa_A * alpha_perp` (alpha =
  transport covector), `B = curl(A)`, `E = -grad(phi) - dA/dt`
- Gauss-law closure: `grad^2(p) = -beta*chi`, `rho_e = eps_0*kappa_phi*beta*chi`
- Wave speed: `c = c_T = sqrt(mu/rho)` (claimed same speed for shear AND EM waves)
- Dispersion with microstructure: `omega^2 = c^2*k^2*[1 + eta*(k*l)^2 + O((k*l)^4)]`
- GR: `n(x) = c0/c_local(x)`, weak field `n(x) ~= 1 - 2*Phi(x)/c0^2`
- Minimal-coupling Lagrangian: `L = (1/2)*m*|rdot|^2 + q*rdot.A - q*phi`
- CHSH: `S = E(a,b) - E(a,b') + E(a',b) + E(a',b')`, `|S|<=2` (standard bound)

**Physical claims:** charge = volumetric eigenstrain defect (excess/deficit
volume); mass = stored elastic energy (`m = E_total/c^2`); spin = real local
rotational motion (`s ~ rho*u x v`), spinor structure `q(x,t) in SU(2)`;
gravity = refraction from spatially-varying wave speed; vector potential A
identified with the *solenoidal part of a transport covector* (pseudomomentum),
NOT raw velocity — explicitly likened to Stokes drift in water waves.

**Self-identified open problems:** charge quantization mechanism, a finished
Pauli/Dirac-type derivation, full source/detector QM account, moving-charge
dynamics, Fresnel-drag closure. The page explicitly calls itself "a living
set of notes, not final wording."

**Visualization:** references an interactive-visualization-software page and
simple-wave demos; grid-based field storage mentioned.

---

## E3. Properties of Space and General Relativity
**URL:** https://elastic-universe.org/properties-of-space-and-general-relativity/

**Equations:** `c_T = sqrt(mu/rho_m)`, Snell's law, `ds^2 = g_munu dx^mu dx^nu`,
static form `ds^2 = g_00*c^2*dt^2 + g_ij*dx^i*dx^j`, `n(x) = c0/c(x)`,
weak-field `n(x) ~= 1 - 2*Phi(x)/c0^2`, `E=mc^2`.

**Mechanism:** spatial metric identified with the medium's strain field;
`g_00` set by local wave speed (lower speed -> slower clocks). **Explicitly
no stress-energy tensor, no Einstein field equations, no Ricci/Riemann
tensor, and no derivation connecting the elastic constitutive law to the
actual GR field equations** — the page states it works only "in appropriate
limits" and "weak-field regimes."

---

## E4. Special Relativity
**URL:** https://elastic-universe.org/special-relativity/

**Equations:** Hooke's law, 1D wave equation, `c_T = sqrt(mu/rho)`, light-clock
derivation `(c*t)^2 = L^2 + (v*t)^2 -> t = gamma*t0`, length contraction
`L = L0/gamma`.

**Mechanism:** time dilation and length contraction both derived from wave
kinematics (light-clock diagonal path; standing-wave Doppler compression) —
i.e. **SR is presented as derived, not postulated**, given only "wave
equation with fixed propagation speed c." Explicitly keeps open the
possibility of an undetectable preferred medium frame, since "all practical
rods and clocks are wave-based" and therefore co-transform. Distinguishes
two-way (measurable) vs one-way (synchronization-dependent) light speed.
Lists 20 JSFiddle demos (light clock, Michelson-Morley, twin paradox with
an optional ether-wind parameter, aberration, etc.)

---

## E5. Spin 1/2: Stern-Gerlach, 720-degree repeat
**URL:** https://elastic-universe.org/spin-1-2-stern-gerlach-the-720-degree-repeat-and-a-mechanical-picture-in-an-elastic-medium/

**Equations:** `F ~= grad(mu.B)`, `dL/dt = mu x B`, spinor sign flip under
2*pi (`|psi> -> -|psi>`) and identity under 4*pi, a schematic twist-decay
ansatz `k(r) ~ 1/(r-r0+1)^p`.

**Mechanism:** "hula-hoop" local rotation (material points trace small
circles, opposite sense above/below a mid-plane); belt-trick topology for
the 720-degree return. Stern-Gerlach reframed semiclassically: spin as a
real precessing vector that "slowly aligns" toward a stable direction
(bifurcation dynamics) rather than instantaneous collapse. **Explicitly
flagged by the site itself as "a mechanical candidate picture... not yet a
finished derivation of the electron."**

---

## E6. Wave Particle Duality
**URL:** https://elastic-universe.org/wave-particle-duality/

**Equations:** de Broglie loop quantization `2*pi*r = n*lambda`, Fermi's
golden rule, photoelectric relation `K_max ~= h*f - phi`, double-slit
`I(x) ~ |psi1+psi2|^2`.

**Mechanism:** "photon" reframed as a detection event, not a traveling
pellet; discreteness lives in detector thresholds, not the field;
double-slit interference is ordinary wave superposition with discrete
clicks accumulating where intensity is high. Standard textbook-level
formulas, no new mathematical content beyond existing QM.

---

## E7. Electromagnetic Waves and Charge
**URL:** https://elastic-universe.org/electromagnetic-waves-and-charge/

**Equations:** `E = -grad(phi) - dA/dt`, `B = curl(A)`, Gauss's law
`div(E) = rho/eps0` combined with `E=-grad(phi)` gives `-grad^2(phi) ~ rho`.

**Mechanism:** charge = localized volumetric eigenstrain (excess volume =
positive, deficit = negative), explicitly analogized to Eshelby inclusions
and point defects (vacancies/interstitials) in real elastic solids. Charge
conservation "becomes almost automatic" because eigenstrain defects
naturally form in +/- pairs (an excess-volume region generically induces a
neighboring deficit-volume region). **No Coulomb's law or charge
quantization derivation given on this page.**

---

## E8. Maxwell Episode
**URL:** https://elastic-universe.org/maxwell/

**Equations:** wave equation, `E=-grad(phi)-dA/dt`, `B=curl(A)`, all four
Maxwell equations stated in standard form, Lorentz force `F=q(E+vxB)`,
Aharonov-Bohm phase `Delta_phi = (q/hbar)*OINT(A.dl) = (q/hbar)*Phi_B`.

**Mechanism:** A reframed as a "convective pseudomomentum" transport field
rather than raw material velocity (same construction as E2); Faraday's law
minus sign interpreted as medium inertia/restoring response ("spinning up
the local hula-hoop motion costs energy"); parallel-current attraction
explained as twist-cancellation lowering local energy density. States the
Aharonov-Bohm vector potential is "physically real" — phase accumulates
from circulating A even where B~=0 outside a solenoid core (a topological,
not-simply-connected-region argument).

---

## 8. Updated Assessment vs E9 (2026-04-11)

**E9's verdict said "no Lagrangian, no field equations... mathematically
underdeveloped."** That is no longer accurate for the site as it stands
today. E2 (Technical Summary) now carries a genuine continuum-mechanics
Lagrangian (Sec E2 above), a Gauss-law-style closure relation for charge,
and an explicit EM-potential mapping with a stated gauge choice (Coulomb
gauge as the "natural" one, with a Lorenz-type alternative also given).
**This is a real update to the project's prior assessment of the site, not
a contradiction of E9's methodology** — E9 reviewed the Home and Big
Picture Guide pages, which remain qualitative; the Technical Summary page
(E2) was correctly flagged PENDING in E9's own table and turns out to hold
essentially all of the site's math.

**What is still true from E9, confirmed again here:** no stress-energy
tensor, no Einstein field equations, no Ricci/Riemann curvature, no
Schwarzschild-type derivation, no charge-quantization mechanism, no
finished Dirac/Pauli derivation of the electron. The GR page (E3)
explicitly disclaims completeness ("appropriate limits," "weak-field").
Their own site repeatedly and explicitly labels itself provisional
("a living set of notes") — this is a genuinely unusual level of
self-disclosed incompleteness for a physics website, and should be read
at face value rather than discounted.

---

## 9. PDTP Comparison Table (Phase 1 pages)

| Their claim (page) | PDTP equivalent | Part | Verdict |
|---|---|---|---|
| `n(x)=c0/c_local(x)` gravity-as-refraction (E2, E3) | `n_PDTP = 1/alpha = 1/cos(Delta)` | Part 98 | Independent confirmation (already noted, E9) |
| `c = sqrt(mu/rho)` wave speed (E2, E4) | `c_s = c` for any m_cond | Part 34 | Independent confirmation (already noted, E9) |
| Lagrangian `L = (1/2)*rho*du^2 - mu*eps_dev:eps_dev + p*(div(u)-chi) + L_core` (E2) | `L = (1/2)(d_mu*phi)^2 + Sum g_i*cos(psi_i-phi)` (Part 1) | -- | **Structurally different, not comparable term-by-term.** Theirs is a displacement-field continuum-mechanics Lagrangian (u is a vector field, strain eps is its gradient); PDTP's is a phase-field Lagrangian (phi is a scalar angle, coupling is cos of a phase difference). Both being "a Lagrangian for an elastic-like medium" does not make them the same theory. |
| Eigenstrain charge `chi=tr(eps*)`, `Q~Delta_V`, `grad^2(p)=-beta*chi` (E2, E7) | Charge from vortex winding (Part 22) | Part 22 | Different mechanism (volume defect vs phase winding); both un-derive charge *quantization* from first principles — neither framework has solved this piece. Worth noting as a shared open problem, not a PDTP gap unique to either side. |
| Vector potential A = solenoidal transport covector / pseudomomentum (E2, E8) | No dedicated PDTP U(1)_EM vector-potential construction exists yet | -- | **Candidate new angle, not yet explored in PDTP** — flagged in Sec 10, not adopted. |
| Dispersion correction `omega^2=c^2k^2[1+eta(kl)^2+...]` from microstructure scale l (E2) | PDTP dispersion: `omega^2 = c^2*k^2 + omega_gap^2` (Eq 89.1, [ASSUMED]) | Part 89 | **Not the same effect, checked against equation_reference.md.** PDTP's Eq 89.1 is a mass-GAP term (constant offset at k=0, from the coupling curvature at the cos-potential minimum) — an IR/long-wavelength effect. Theirs is a high-k UV correction growing with (k*l)^2 from a lattice/microstructure length l — the opposite regime. The two could in principle coexist in a single full dispersion relation (gap at low k, lattice correction at high k), but PDTP has not derived a high-k lattice-correction term of this form; this is a real gap, not a duplicate of Eq 89.1. |
| Spin-1/2 hula-hoop / belt-trick, `k(r)~1/(r-r0+1)^p` (E5) | Fermion statistics from Berry phase (Part 93) | Part 93 | Same qualitative topological picture (720-degree return); their radial twist-decay ansatz has no PDTP counterpart and is itself un-derived on their own site. |
| CHSH / detector-threshold reframing of Bell tests (E2) | No PDTP measurement-interpretation layer exists | -- | Out of scope for PDTP's current goals (Goal 1 is classical-limit gravity, not a QM foundations program); noted, not pursued. |

---

## 10. Candidate New Ideas for PDTP (flagged only — NOT adopted)

Per CLAUDE.md's Elastic Universe rule, nothing below is imported into PDTP.
These are noted as possible future T-items, for the user to decide whether
to file:

1. **Transport-covector vector potential** (`A ~ v - (grad(u))^T v`,
   solenoidal part) — PDTP currently has no explicit U(1)_EM sector
   construction at all (the SU(3) extension is QCD-only). If PDTP ever
   builds an EM sector, this "A as pseudomomentum, not raw velocity" framing
   is a genuinely different starting point worth comparing against the
   obvious naive choice (A = phase-gradient of some U(1)_EM phase field).
2. **High-k lattice dispersion correction** `omega^2 = c^2k^2(1+eta(kl)^2+...)`
   — PDTP has the ingredients to derive an analogous term (lattice spacing
   a_0 = l_Planck, Part 34) and already has a low-k mass-gap term
   (Eq 89.1, `omega^2=c^2k^2+omega_gap^2`), but no equation_reference.md
   entry currently gives PDTP's own high-k lattice-correction piece — this
   is a genuinely open, bounded derivation task (standard lattice-QFT
   dispersion expansion applied to PDTP's own cos-coupling lattice), not
   something borrowed from Elastic Universe's specific formula.
3. **Eigenstrain formalism (Eshelby 1957)** as a general continuum-mechanics
   tool — independent of whether their specific charge model is right, the
   mathematical machinery (relaxation volumes, inclusion theory) is
   established and could in principle be applied to PDTP's own vortex
   defects as an alternative computational technique, not a competing
   physical claim.

None of these are recommended as immediate action — they are Low-priority,
optional candidates consistent with T27's own "Low priority" tag.

---

## 11. Verdict

[EXTERNAL] Phase 1 (E2-E8) confirms E9's core finding that Elastic Universe
is **conceptually well-aligned but mathematically far behind** PDTP overall
(no SU(3)/QCD sector, no quantitative falsifiable predictions, no Sudoku-
style consistency methodology, no charge quantization) — but **revises E9's
specific "no Lagrangian" claim**: the Technical Summary page (E2) does have
one, for a displacement-field elastic continuum, structurally distinct from
PDTP's phase-field Lagrangian. The strongest genuinely new angle for PDTP
to consider (not adopt) is the transport-covector treatment of the vector
potential A, since PDTP has no EM-sector construction to compare it against
yet. Recommendation unchanged from E9: extract visualization code (Phase 3,
J1-J3) if useful; do not import any physics claim without independent
Sudoku validation.

