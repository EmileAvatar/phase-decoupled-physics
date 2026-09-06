# T69 Sub-Points 2-3: LZ Event and Roman Space Telescope (Part 139)

**Method:** Bounded literature-comparison mapping (per T69's own scope —
"no new derivation expected... a mapping exercise, not an investigation").
**Status:** [DERIVED, mass-scale comparison] + [SPECULATIVE/mapping elsewhere].
**Cross-checks:** Part 89 (Mechanism 1), Part 116 (n=1 winding selection),
`falsifiable_predictions.md` (Predictions 5, 11, 13)
**Date:** 2026-09-02

---

## Plain English Summary

Two things happened in physics in the last few days: a dark-matter
detector (LZ) reported a single unusual event that might — cautiously,
not confidently — be a first hint of a dark matter particle; and NASA's
Roman Space Telescope, built specifically to map dark matter and dark
energy, launched. **Neither connects cleanly to PDTP's own current dark
matter picture, and being honest about exactly how and why is more useful
than forcing a connection.** The LZ event, if real, points to a particle
about a billion billion times lighter than PDTP's own preferred dark
matter candidate (Part 116's "Planck vortex relic") — so it would either
be background noise (consistent with PDTP predicting direct detection
should see nothing), or evidence for a completely different kind of dark
matter than PDTP currently favors. Roman's headline capability — mapping
dark matter's fine structure via gravitational lensing — doesn't test
anything PDTP-specific either, because PDTP's own attempt to make a
distinctive lensing prediction (Part 61's biharmonic gravity) already
failed by 20 orders of magnitude at galactic scale. Roman's real
connection to PDTP is a different, quieter one: it's one of the surveys
already on record (`falsifiable_predictions.md` Prediction 5) that will
help test PDTP's dark *energy* prediction, once its data start arriving.

---

## 1. The LZ 2.6-Sigma Event, Mapped Against PDTP's DM Candidates

**What was reported** (LBNL press release, 2026-09-01; TeV Particle
Astrophysics conference, Japan): a single anomalous event in the LZ
(LUX-ZEPLIN) 10-tonne liquid xenon detector at Sanford Underground
Research Facility, from 220 live days of data (March 2023-April 2024).
2.6-sigma significance (~0.5% chance of a known-background origin) — well
short of the 5-sigma discovery threshold. The collaboration is explicit
this is not a confirmed detection; further data collection is planned.
If caused by dark matter, the event implies **a WIMP of mass at least
~200 GeV/c², via an interaction type beyond the simplest spin-independent
nuclear-recoil model.**

**Mapped against PDTP's own DM candidates:**

| PDTP candidate | Predicted mass | Ratio to LZ-implied ~200 GeV | Structural fit? |
|---|---:|---:|---|
| Part 116 n=1 "Planck vortex relic" (PDTP's preferred candidate) | m_Planck = 1.22×10^19 GeV | ~6×10^16 too heavy | No |
| Part 89 Mechanism 1, C1 energy-trap candidate | ~200 MeV | ~1000 too light | No |
| Winding spectrum at some other n (m_DM = m_Planck/n) | 200 GeV requires n ~ 6×10^16 | exact match by construction | Only by abandoning Part 116's own n=1 selection |

[DERIVED, computed] Neither of PDTP's two actual candidates sits anywhere
near the LZ-implied mass scale — the mismatch is 16-17 orders of
magnitude one way, 3 orders the other. The third row is not really a
third candidate: the general formula m_DM = m_Planck/n can produce
*any* mass for the right n, but Part 116 specifically derived (via vortex
stability and Kibble-Zurek formation statistics, not by assumption) that
n=1 is strongly favored over every other winding number — so treating
n~6×10^16 as "PDTP's prediction" would mean discarding Part 116's own
result, not confirming it.

**Verdict:** two honest, mutually exclusive readings, and no way from
PDTP's side to prefer one yet:
1. **Most likely, per the collaboration's own caution:** the event is a
   rare background fluctuation. This is *consistent* with PDTP's own
   prediction — Part 116's n=1 candidate is essentially undetectable by
   direct detection (σ/m dozens of orders below current sensitivity,
   Part 138-corrected), so PDTP predicts LZ (and every other direct-
   detection experiment) should keep seeing nothing. A null result
   strengthens, not weakens, PDTP's current picture.
2. **If future LZ data confirm a ~200 GeV WIMP:** this would be in real
   tension with PDTP's n=1 selection specifically — either dark matter
   is not purely the Planck-vortex relic (a mixed-component picture, with
   PDTP's vortex as only part of the total 27%), or Part 116's stability/
   Kibble-Zurek argument for n=1 needs revisiting. **This is a genuine,
   falsifiable fork** — worth remembering as a marker if LZ's signal
   strengthens with more data, not something to resolve now from a
   single 2.6-sigma event.

**No PDTP claim is made or implied here about which reading is correct.**

---

## 2. Roman Space Telescope Relevance

**What it is:** NASA's Nancy Grace Roman Space Telescope launched
2026-08-30 (SpaceX Falcon Heavy, Kennedy Space Center). Wide-field
(0.281 deg² FOV, ~0.1 arcsec diffraction-limited resolution) survey
instrument, designed to build "the most comprehensive 3D map of the
distribution of galaxies and galaxy clusters" via weak lensing, and to
characterize dark matter substructure through a large population of
strong gravitational lenses. First images expected early 2027 — no data
exists yet to analyze.

**Checked against every currently-live PDTP falsifiable prediction that
touches lensing, dark matter, or dark energy** (`falsifiable_predictions.md`):

| Prediction | What it needs | Does Roman test it? |
|---|---|---|
| 5 — w(z) ≠ -1 (dark energy) | Weak lensing + BAO + SNe over cosmic time | **Yes — already listed** in `falsifiable_predictions.md`'s own survey table, alongside DESI/Euclid/Rubin. Table's "Launch ~2027" note is now stale (already launched 2026-08-30) — corrected below. |
| 11 — Biharmonic gravity at galactic scale (would show up as a distinctive lensing signature) | Requires L_heal > l_Planck | **No** — `dark_matter_energy.md` §2.5 already found L_heal ~ l_Planck, 20 orders of magnitude too small for any galactic-scale effect. This route is already dead; Roman's substructure maps cannot resurrect it. |
| 13 — Planck-vortex DM ⇒ detectable CMB tensor modes | CMB polarization instrument (LiteBIRD, CMB-S4) | **No** — Roman is an optical/near-IR imaging telescope, not a CMB polarimeter. Wrong instrument class entirely. |

**Verdict:** Roman's headline capability — precision dark-matter
substructure mapping via strong/weak lensing — does **not** test any
PDTP-specific prediction, not because Roman lacks the power, but because
PDTP itself currently makes no distinctive prediction at the scales Roman
probes: the one mechanism that would have produced a PDTP-specific
lensing signature (biharmonic gravity, Prediction 11) already failed by
20 orders of magnitude on its own precondition, and PDTP's live DM test
(Prediction 13) needs an entirely different kind of instrument. Roman's
real, useful connection to PDTP is the quieter one already on record —
Prediction 5's dark energy w(z) test — where it joins DESI, Euclid, and
Rubin as one more survey PDTP should watch once data arrive in 2027.

**Action taken:** `falsifiable_predictions.md`'s Roman row updated from
"Launch ~2027" to reflect the actual 2026-08-30 launch (data still not
expected until early 2027, so no other change to that prediction's status).

---

## 3. Verdict

Both sub-points resolve honestly negative-to-neutral, in the same spirit
as T69 sub-point 1's findings: no forced connections, no new PDTP claims
introduced, existing predictions checked and one stale status note fixed.
The LZ mapping identifies a real, specific, falsifiable fork for the
future (does confirmed WIMP-mass dark matter contradict Part 116's n=1
selection?) without prejudging it from one 2.6-sigma event. The Roman
check confirms PDTP has nothing further to say about weak-lensing
substructure than what's already on record for dark energy — an honest
scope boundary, not a gap to manufacture a prediction for.

---

## References

- Berkeley Lab News Center (2026-09-01), "LZ Sees Surprising Result in
  Search for Dark Matter."
- NASA/JPL (2026-08-30), "NASA's Dark Universe-Seeking Nancy Grace Roman
  Space Telescope Launches."
- Part 116 (`dm_winding_selection.md`) — n=1 winding selection.
- Part 89 (`condensate_layer_optics.md`) — Mechanism 1, C1 energy trap.
- Part 138 (`dm_bullet_bound_erratum.md`) — corrected σ/m margin cited above.
- `docs/research/falsifiable_predictions.md` — Predictions 5, 11, 13.

---

*End of Part 139 (T69 sub-points 2-3).*
