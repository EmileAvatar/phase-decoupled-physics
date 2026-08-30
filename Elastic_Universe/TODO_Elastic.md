# TODO_Elastic — Elastic Universe Investigation

**Type:** External framework review (SPECULATIVE — kept separate from PDTP)
**Date opened:** 2026-04-11
**Status:** DONE 2026-08-30. All three phases complete: Phase 1 (E1-E9,
core physics), Phase 2 (E10-E16, interpretive/meta), Phase 3 (J1-J3,
JSFiddle code). One residual gap: the "EM Waves" JSFiddle collection could
not be fetched (persistent HTTP 500 from jsfiddle.net across 3 attempts) —
not a scope decision, worth a retry if EM-sector code ever becomes a
priority. See `E2-E8_phase1_core_physics_review.md`,
`E10-E16_phase2_interpretive_review.md`, `J1-J3_jsfiddle_code_review.md`.

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
| E2 | Technical Summary | DONE (2026-08-30) | HAS a Lagrangian (displacement-field, not phase-field); eigenstrain charge model; A=transport covector; dispersion correction with microstructure scale -- see `E2-E8_phase1_core_physics_review.md` |
| E3 | Properties of Space and General Relativity | DONE (2026-08-30) | n(x)=c0/c_local(x); explicitly NO stress-energy tensor, NO Einstein field equations, NO Schwarzschild derivation |
| E4 | Special Relativity | DONE (2026-08-30) | SR "derived" from wave kinematics; keeps an undetectable preferred-frame option open; 20 JSFiddle demos |
| E5 | Spin 1/2: Stern-Gerlach, 720-deg repeat | DONE (2026-08-30) | Hula-hoop/belt-trick model; self-acknowledged "not a finished derivation" |
| E6 | Wave Particle Duality | DONE (2026-08-30) | Standard textbook QM formulas; photon=detection event; no new math |
| E7 | Electromagnetic Waves and Charge | DONE (2026-08-30) | Eigenstrain charge (Eshelby); no Coulomb's law or quantization derived |
| E8 | Maxwell Episode: Fields, Convection, Induction | DONE (2026-08-30) | A=pseudomomentum; Faraday sign as medium inertia; A-B phase "physically real" |
| E9 | Big Picture Guide | DONE | Most complete overview; no equations; 14 JSFiddle demos; eigenstrain for charge |

### Phase 2 — Speculative / Interpretive Pages

| # | Page | Status | Notes |
|---|------|--------|-------|
| E10 | Quantum Eraser Without Retrocausality | DONE (2026-08-30) | Standard post-selection explanation; mainstream physics, no new claim |
| E11 | Is Entanglement Ontological or Epistemic? | DONE (2026-08-30) | Epistemic view; cites real Eberhard eta_min~=0.828 bound; outside PDTP scope |
| E12 | Simulations | DONE (2026-08-30) | Hub page; 10 named collections, full inventory in J1-J3 doc |
| E13 | Links and Papers | DONE (2026-08-30) | NEW names found: Danielewski, Duda (real academics); Close/Kleinert refs specified |
| E14 | About | DONE (2026-08-30) | Author = Chantal Roth, PhD Sci. Computing (ETH Zurich); no physics PhD |
| E15 | Spin Visualizations | DONE (2026-08-30) | 3 sub-pages; Unity tool has NO published source code (dead end for extraction) |
| E16 | Mechanical Universe S01 | DONE (2026-08-30) | Lecture hub, no new content beyond E2-E11 |

See `E10-E16_phase2_interpretive_review.md` for full writeup.

### Phase 3 — JSFiddle Code Review

| # | Item | Status | Notes |
|---|------|--------|-------|
| J1 | Inventory all JSFiddle simulations | DONE (2026-08-30) | ~310 listings, 9/10 collections (EM Waves collection: persistent HTTP 500, could not fetch) |
| J2 | Identify visualizations useful to PDTP | DONE (2026-08-30) | 6-fiddle shortlist: Hopf, FCC+tensor, Cosserat Charge (x3), Smoke Rings/Knots, Liquid Crystal, 3D Lattice |
| J3 | Extract/adapt visualization code | DONE (2026-08-30) | Source pulled for all 6 shortlisted; 3 good rendering-technique candidates, 1 negative (Cosserat Charge doesn't implement Cosserat theory), 1 mislabeled (3D Lattice) |

See `J1-J3_jsfiddle_code_review.md` for full writeup.

---

## Initial Assessment (from Home page + YouTube screenshots)

**Note (2026-08-30):** the summary immediately below is the ORIGINAL
2026-04-11 pass (Home page + screenshots only) and is partially stale —
see `E2-E8_phase1_core_physics_review.md` for the full Phase 1 review,
which found the Technical Summary page (E2) now has a genuine Lagrangian
and a developed eigenstrain-charge closure, contradicting this section's
"no Lagrangian" line below. Kept here unedited for history; do not treat
"What They Have That PDTP Doesn't" / "What PDTP Has That They Don't" below
as current without cross-checking Sec 8-11 of the Phase 1 review doc.

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
