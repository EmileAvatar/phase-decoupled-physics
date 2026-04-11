# TODO_Elastic — Elastic Universe Investigation

**Type:** External framework review (SPECULATIVE — kept separate from PDTP)
**Date opened:** 2026-04-11
**Status:** PENDING

**IMPORTANT:** This investigation is SEPARATE from PDTP. It is speculative
exploration of an external framework to identify useful thinking, analogies,
and visualization code. Results do NOT flow into PDTP unless explicitly
validated through PDTP's own Sudoku consistency checks and SymPy verification.

---

## Sources

- **Main website:** https://elastic-universe.org/
- **JSFiddle simulations:** https://jsfiddle.net/u/Chenopdodium/
- **YouTube channel:** Inductica (screenshots in `assets/images/inductia/`)

---

## Website Pages to Review

Each page should be fetched and analyzed for:
(a) Mathematical content (equations, Lagrangians, field equations)
(b) Physical claims (predictions, mechanisms, derivations)
(c) Visualization code (simulations, animations, interactive demos)
(d) Potential PDTP relevance (new thinking, analogies, missing terms)

### Phase 1 — Core Physics Pages

| # | Page | Status | Notes |
|---|------|--------|-------|
| E1 | Home (overview) | DONE | Elastic continuum; no Lagrangian; qualitative |
| E2 | Technical Summary | PENDING | Most likely to have equations |
| E3 | Properties of Space and General Relativity | PENDING | GR from elasticity; metric from strain? |
| E4 | Special Relativity | PENDING | c = sqrt(mu/rho) mechanism |
| E5 | Spin 1/2: Stern-Gerlach, 720-deg repeat | PENDING | Mechanical spin model |
| E6 | Wave Particle Duality | PENDING | Ontological model |
| E7 | Electromagnetic Waves and Charge | PENDING | EM from elastic waves |
| E8 | Maxwell Episode: Fields, Convection, Induction | PENDING | Maxwell from elastic medium |
| E9 | Big Picture Guide | DONE | Most complete overview; no equations; 14 JSFiddle demos; eigenstrain for charge |

### Phase 2 — Speculative / Interpretive Pages

| # | Page | Status | Notes |
|---|------|--------|-------|
| E10 | Quantum Eraser Without Retrocausality | PENDING | Interpretation |
| E11 | Is Entanglement Ontological or Epistemic? | PENDING | Interpretation |
| E12 | Simulations | PENDING | Links to interactive demos |
| E13 | Links and Papers | PENDING | Bibliography / references |
| E14 | About | PENDING | Authors, background |
| E15 | Spin Visualizations | PENDING | Visual demos |
| E16 | Mechanical Universe S01 | PENDING | Lecture series |

### Phase 3 — JSFiddle Code Review

| # | Item | Status | Notes |
|---|------|--------|-------|
| J1 | Inventory all JSFiddle simulations | PENDING | https://jsfiddle.net/u/Chenopdodium/ |
| J2 | Identify visualizations useful to PDTP | PENDING | Wave sims, lattice, vortex, etc. |
| J3 | Extract/adapt visualization code | PENDING | JS -> Python or standalone HTML |

---

## Initial Assessment (from Home page + YouTube screenshots)

### Their Model
- Spacetime = elastic continuum (Cauchy elastic solid, "possibly supersolid")
- Supports transverse (shear) waves = gravitational waves
- c = sqrt(mu_shear / rho) where mu = shear modulus
- Gravity = refraction in variable-density medium
- Spin-1/2 = mechanical oscillation (720-degree belt trick)
- Matter/antimatter = wave/anti-wave interference
- EM = elastic waves in the medium
- Charge = volume eigenstate or microrotation

### Comparison to PDTP (from Image 01 table)
- Their "elastic continuum" ~ PDTP's condensate lattice
- Their "shear waves" ~ PDTP's tensor GW modes (Part 28)
- Their "c = sqrt(mu/rho)" ~ PDTP's c_s = c (Part 34)
- Their "metric from strain" ~ PDTP's emergent metric (Part 73)
- Their "gravity as refraction" ~ PDTP's n_PDTP = 1/alpha (Part 98)
- Their "spin from belt trick" ~ PDTP's Berry phase (Part 93)

### What They Have That PDTP Doesn't
- Good visualizations (interactive JS simulations)
- Liquid crystal analogy (biaxial nematic, 5 DOF, hedgehog defects)
- Explicit "microrotation" model for charge

### What PDTP Has That They Don't
- Lagrangian (they have none)
- Field equations (derived, SymPy verified)
- Quantitative predictions (6+ falsifiable)
- SU(3) extension (quarks, gluons, confinement)
- Sudoku consistency methodology
- 100+ Parts of systematic derivation

### Potential Insights for PDTP
1. **Liquid crystal order** — biaxial nematic has 5 DOF; close to 6 needed
   for g_ij. Could supplement SU(3) or offer alternative route to spatial curvature.
2. **Microrotation** — Cosserat elasticity has rotational DOF beyond displacement.
   Maps to: does the PDTP condensate have rotational (spin) DOF beyond phase?
3. **Visualization techniques** — their JS sims could be adapted for PDTP
   (wave coupling, vortex dynamics, lattice deformation).
4. **Refraction = gravity** — independently confirms PDTP Part 98 (n = 1/alpha).

---

## Rules

- All findings stay in `Elastic_Universe/` folder
- Nothing flows into PDTP docs/simulations without explicit Sudoku validation
- Tag all content [EXTERNAL] or [SPECULATIVE]
- Credit the source (elastic-universe.org / Inductica)
- Focus on extractable physics and code, not framework endorsement
