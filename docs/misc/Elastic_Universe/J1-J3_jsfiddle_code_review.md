# J1-J3 — JSFiddle Code Review

**Source:** https://jsfiddle.net/u/Chenopdodium/ (10 named collections)
**Date reviewed:** 2026-08-30
**Tag:** [EXTERNAL]

---

## J1. Inventory of All JSFiddle Collections

| Collection | Fiddle count | Notes |
|---|---:|---|
| General Relativity | 36 | refraction, GRIN optics, jello-metaphor GR, FCC lattice+tensor |
| Special Relativity | 33 | time dilation, length contraction, Michelson-Morley, Doppler |
| Spherical Harmonics | 19 | electron orbitals, drum-head modes, vector harmonics |
| Spin 1/2 | 43 | belt trick, spinors, Stern-Gerlach, Rashkovskiy models, Mobius strip |
| Wave vs Particle | 39 | double-slit, Compton/Brillouin scattering, Bohmian mechanics, blackbody |
| Fermi's Golden Rule / Resonance | 7 | coupled oscillators, photoelectric effect |
| Bell / EPR | 21 | CHSH geometry, Eberhard mechanism, detection-loophole demos |
| EM Waves | -- | **could not fetch — JSFiddle returned HTTP 500 on every attempt (3 retries), server-side issue on their end, not a access/auth problem** |
| Charge | 42 | eigenstrain, Cosserat-labeled, Duda topological charge, Biot-Savart |
| Other Charge Models (marked incorrect) | 20 | explicitly superseded/rejected charge models, kept public |
| Demo Set (curated subset) | 50 | cross-selection of the above, includes Hopf, knots, Cosserat |

**Total catalogued: ~310 listings across 9/10 collections** (collections
overlap — the same fiddle often appears in 2-3 collections, so the true
unique count is smaller, likely 150-220; not de-duplicated here since the
titles alone are sufficient for the J2 relevance screen below). The EM
Waves collection could not be retrieved despite being listed correctly on
the Simulations hub page (E12) — flagged as an open gap, not a scope
decision; worth one retry in a future session if EM-sector code becomes a
priority.

---

## J2. PDTP-Relevance Shortlist

Screened by title against every currently-open PDTP thread. Selected for
source-code extraction (Sec J3) based on direct name-matches to specific
Parts/T-items:

| Fiddle | Collection | PDTP connection |
|---|---|---|
| Hopf | Demo Set | Part 106 (Hopf-link baryon), T30 (Hopf-link topology protection) |
| FCC Grid (with tensor) | GR | Part 54 (FCC lattice, cosmological constant), Part 73 (emergent metric) |
| Cosserat Charge / Charge as Cosserat microrotations (3D) / Cosserat 3D, 2 charges | Charge | T66 (rotation-field/tetrad promotion, Cosserat-continua analogy) |
| Smoke Rings and Knots in an Elastic Continuum | Demo Set | Part 106, T30 (topological solitons: rings, links, trefoil/figure-8/torus knots) |
| Liquid Crystal / Liquid Crystal Electron (Duda) | Wave vs Particle, Charge | E9's flagged "biaxial nematic, 5 DOF" alternative route to g_ij |
| 3D Lattice | SR | general lattice-visualization technique (turned out mislabeled, Sec J3) |

Not pursued further (title-screened, lower direct relevance): the Bell/
EPR collection (21 fiddles — quantum-foundations, outside PDTP's scope per
Sec E11), most of the Spin-1/2 and Wave-vs-Particle collections (electron-
orbital and scattering demos with no PDTP-specific hook beyond what E9
already covered), the Fermi's Golden Rule collection (standard coupled-
oscillator resonance, textbook content).

---

## J3. Source Code Findings (6 fiddles extracted)

### Hopf — `jsfiddle.net/Chenopdodium/p4mxs32t/`
Modern Three.js/WebGL module (ES6 imports, OrbitControls, lil-gui). Six
generation modes for Hopf fibration base points on S2 (great circle,
random, loxodrome, curl/stereographic, Fibonacci, spin-1/2 Bloch-sphere
precession), each mapped to fibers in S3 and projected to 3D. Includes an
inset S2 preview, planar shadow projection, and OBJ mesh export.
**Assessment: genuinely sophisticated, reusable visualization code** for
Hopf-fibration structure specifically — directly relevant to illustrating
Part 106's Hopf-link baryon topology, IF adapted (the underlying math is
generic Hopf fibration, not anything PDTP-specific; it would need PDTP's
own field data piped in to visualize an actual PDTP soliton rather than
the generic fibration).

### FCC Grid (with tensor) — `jsfiddle.net/Chenopdodium/2o49e03b/`
Three.js instanced-mesh FCC lattice (~256 atoms: corner sites at integer
(x,y,z) plus face-centered sites at (x+0.5,y+0.5,z)-type offsets),
computes a metric tensor (3x3 spatial or 4x4 spacetime) at a probe point
from partial derivatives of an applied deformation field (static stretch,
"gravitational" quadratic bending, twist/"frame-dragging," dynamic waves).
**Assessment: a real, working "metric-from-lattice-distortion" visual
tool** — structurally the right kind of demo for Part 54/73, but the
"frame dragging" and "gravity" labels are cosmetic animation presets
chosen by the author, not derived from any field equation (their own
site, Sec E3, explicitly disclaims deriving Einstein's equations). Useful
as a rendering technique to adapt with PDTP's own actual deformation
field, not as a physics result to cite.

### Cosserat Charge — `jsfiddle.net/Chenopdodium/xpb4rgq1/`
**Negative finding, worth flagging clearly for T66.** Despite the name,
this fiddle does NOT implement Cosserat microrotation theory. It is a
standard inverse-square electrostatic field visualizer (vectors from one
or two point charges, colored by direction) with "Cosserat" in the title
only — no couple-stress tensor, no independent rotational degrees of
freedom, no micropolar deformation anywhere in the code. **T66 should NOT
assume this collection provides ready-made Cosserat-mechanics code** — it
does not; the name is misleading (likely an aspirational/working title
kept from an earlier plan that was never implemented). The two sibling
fiddles ("Charge as Cosserat microrotations (3D)," "Cosserat 3D, 2
charges") were not independently re-checked but should be assumed to have
the same gap until verified, given they share the same collection and
apparent authorship pattern.

### Smoke Rings and Knots in an Elastic Continuum — `jsfiddle.net/Chenopdodium/ja3mL8pt/`
Three.js visualization of vortex rings, Hopf links, trefoil/figure-8
knots, and torus knots via a prescribed displacement field `u(x,t) = A *
exp(-r^2/a^2) * [n1*cos(Phi) + n2*sin(Phi)]`, Phi = omega*t - k.s, with
n1/n2 parallel-transported frame vectors along the filament and a Gaussian
envelope confining motion to a core radius a. **Assessment: this is a
prescribed KINEMATIC animation (a chosen displacement pattern that LOOKS
like a knotted vortex), not a solution of any dynamical field equation** —
useful purely as a rendering/topology-visualization technique (e.g. for
illustrating Part 106's Hopf-link baryon or T30's Hopfion question
visually), not as physics content, and should never be cited as if it
demonstrated that such knots are dynamically stable in any theory.

### Liquid Crystal — `jsfiddle.net/Chenopdodium/9zwb5gh1/`
Three-cell side-by-side comparison (isotropic / uniaxial nematic / biaxial
nematic) implementing the real nematic order parameter `S = <(3cos^2(theta)-1)/2>`
and a "side-axis lock" biaxiality metric `B = <(a.m)^2 - (a.l)^2>`, with
director-field arrows and per-molecule 3D orientation rendering.
**Assessment: legitimate, correctly-implemented liquid-crystal physics**
(S is the standard Tsvetkov/Maier-Saupe nematic order parameter; the
biaxial construction is a reasonable pedagogical simplification, though
not the standard biaxiality parameter used in the liquid-crystal
literature). Directly usable as a visualization reference if E9/T27's
flagged "biaxial nematic as alternative route to g_ij" idea is ever
pursued as an actual PDTP derivation.

### 3D Lattice — `jsfiddle.net/Chenopdodium/2gnydpmk/`
**Listing/content mismatch, not a lattice demo.** The fiddle at this URL
is actually a 3-clock special-relativity time-dilation simulator (spring-
damped clock housings, bouncing photons, proper-time HUD, a "SYNC" button)
— unrelated to its "3D Lattice" title in the SR collection listing. Likely
a stale collection tag pointing at a fiddle that was repurposed/renamed
after being added to the collection. No lattice-visualization content
found at this specific URL; not pursued further.

---

## Verdict (J1-J3)

[EXTERNAL] The JSFiddle library is large (~150-220 unique demos) and of
genuinely high production quality (modern Three.js/WebGL, real-time GUI
controls) — confirming E9's original "good visualizations" assessment at
much greater scale than the initial 14-demo Big-Picture-Guide sample
suggested. Of the six fiddles pulled for source-level review, three are
strong reusable **rendering-technique** candidates (Hopf fibration, FCC
lattice+tensor, liquid-crystal order parameters) if PDTP ever wants
polished visual explainers for Part 106/54/73 or the liquid-crystal g_ij
idea; one (Smoke Rings and Knots) is a good rendering technique but must
never be mistaken for a dynamical result; one (Cosserat Charge) is a
**named-but-not-implemented negative finding** directly relevant to not
over-trusting T66's source material; and one (3D Lattice) turned out to be
a mislabeled/unrelated fiddle. **Recommendation: if any of Hopf, FCC+tensor,
or Liquid Crystal are wanted as actual PDTP visualization assets, adapt
their Three.js rendering scaffolding but replace all underlying field data
with PDTP's own derived quantities — do not present their generic/
illustrative field configurations as PDTP results.**
