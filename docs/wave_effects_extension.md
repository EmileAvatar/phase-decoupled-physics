# Wave Effects Extension — Unified Reference

**Purpose:** Comprehensive checklist of ALL wave phenomena — types, emergent effects,
layers, and governing variables. Use like Methodology.md: systematically check PDTP
against this list to ensure nothing is missed.

**Sources:** `docs/waves.md` (ChatGPT compilation), `docs/research/wave_effects_pdtp.md`
(Part 28c, 50 effects with PDTP mappings).

**Date:** 2026-03-24

---

## Section 1: Wave Types, Actions & Behaviors

Every known wave type, behavior, and interaction — merged from both source files,
deduplicated. The "Category" groups related items; the rest is self-explanatory.

| # | Category | Name | Description | Example | Where | Medium |
|---|----------|------|-------------|---------|-------|--------|
| 1 | Fundamental Types | Mechanical waves | Require a physical medium to propagate | Sound in air, water waves | Fluids, solids | Air, water, rock |
| 2 | Fundamental Types | Electromagnetic waves | Oscillating electric + magnetic fields; no medium needed | Light, radio, X-rays | Vacuum + materials | Spacetime / vacuum |
| 3 | Fundamental Types | Matter waves (de Broglie) | Particles behave as waves; lambda = h/p | Electron interference patterns | Quantum systems | Quantum fields |
| 4 | Fundamental Types | Gravitational waves | Ripples in spacetime curvature from accelerating masses | Black hole mergers | Astrophysical scales | Spacetime |
| 5 | Fundamental Types | Quantum field waves | Excitations of underlying quantum fields | Photons = EM field excitations | Quantum field theory | Quantum vacuum |
| 6 | Direction & Motion | Longitudinal waves | Oscillation parallel to direction of travel | Sound, P-waves | Air, fluids, solids | Compressible media |
| 7 | Direction & Motion | Transverse waves | Oscillation perpendicular to direction of travel | Light, S-waves, string waves | EM fields, strings, solids | Rigid / EM media |
| 8 | Direction & Motion | Surface waves | Combination of longitudinal + transverse at interface | Ocean waves, Rayleigh waves | Interfaces (air-water, crust) | Boundary layers |
| 9 | Direction & Motion | Standing waves | Fixed nodes + antinodes from counter-propagating waves | Vibrating string, organ pipe | Resonant / bounded systems | Any bounded medium |
| 10 | Direction & Motion | Traveling (progressive) waves | Energy transported through space; pattern moves at phase velocity | All freely propagating waves | All media and vacuum | Any |
| 11 | Core Behaviors | Reflection | Wave bounces off boundary; angle in = angle out | Echo, mirror | Walls, mirrors, density changes | Any interface |
| 12 | Core Behaviors | Refraction | Wave bends due to speed change at medium transition | Light bending in water, lensing | Medium boundaries | Glass, water, atmosphere |
| 13 | Core Behaviors | Diffraction | Wave spreads around obstacles or through openings | Sound through doorway, single slit | Edges, slits, obstacles | Any |
| 14 | Core Behaviors | Constructive interference | In-phase waves add; amplitude increases | Bright fringes in double slit | Overlapping wave fields | Any |
| 15 | Core Behaviors | Destructive interference | Out-of-phase waves cancel; amplitude decreases | Dark fringes, noise canceling | Overlapping wave fields | Any |
| 16 | Core Behaviors | Superposition | Total displacement = sum of individual displacements | Overlapping ripples | All linear systems | Any |
| 17 | Core Behaviors | Resonance | System oscillates at max amplitude at natural frequency | Tuning fork, bridge vibration | Oscillators, cavities | Any |
| 18 | Core Behaviors | Beats | Two close frequencies interfere; amplitude modulates | "Wah-wah" sound from two tuning forks | Acoustics, signals | Any |
| 19 | Energy & Interaction | Absorption | Medium converts wave energy into internal energy (heat) | Sound dampened by foam | Materials | Lossy media |
| 20 | Energy & Interaction | Transmission | Wave passes through a medium | Light through glass | Transparent media | Glass, water, air |
| 21 | Energy & Interaction | Scattering | Wave redirected in many directions by irregularities | Blue sky (Rayleigh), X-ray diffraction | Particles, atmosphere | Any inhomogeneous |
| 22 | Energy & Interaction | Attenuation | Amplitude decreases over distance (absorption + scattering + spreading) | Sound fading with distance | Lossy media | Any |
| 23 | Energy & Interaction | Dispersion | Different frequencies travel at different speeds; packet spreads | Rainbow through prism | Prisms, water, waveguides | Dispersive media |
| 24 | Energy & Interaction | Impedance matching | Minimizes reflection; maximizes energy transfer at boundary | Antenna design, acoustic horns | EM systems, acoustics | Any interface |
| 25 | Energy & Interaction | Mode conversion | One wave type converts to another at boundary | Seismic P-wave to S-wave | Solid boundaries | Solids |
| 26 | Polarization | Linear polarization | Oscillation confined to single plane | Polarized sunglasses | EM waves, transverse waves | EM / rigid media |
| 27 | Polarization | Circular polarization | Field vector rotates in circle as wave propagates | Satellite signals, 3D glasses | EM waves | EM / vacuum |
| 28 | Polarization | Elliptical polarization | General case: field traces ellipse (linear + circular are special cases) | Reflected light off surfaces | EM waves | EM / vacuum |
| 29 | Polarization | Birefringence | Material has different refractive index per polarization; splits beam | Calcite double image | Crystals, anisotropic media | Anisotropic solids |
| 30 | Polarization | Dichroism | Material absorbs one polarization more than another | Polaroid filters | Crystals, thin films | Anisotropic media |
| 31 | Frequency & Velocity | Doppler effect | Observed frequency shifts when source/observer moves | Ambulance siren pitch change | All wave types | Any |
| 32 | Frequency & Velocity | Group velocity | Speed of wave packet envelope; carries energy/information | Signal speed in fiber optics | Dispersive media | Any dispersive |
| 33 | Frequency & Velocity | Phase velocity | Speed of single frequency phase advance; can exceed c | Crest movement in deep water | All waves | Any |
| 34 | Frequency & Velocity | Redshift / Blueshift | Frequency shifts from motion, gravity, or cosmic expansion | Galaxy recession, GPS corrections | Astronomy, astrophysics | Spacetime |
| 35 | Nonlinear & Advanced | Harmonics / Overtones | Integer multiples of fundamental frequency | Musical instrument timbre | Resonant systems | Strings, pipes, cavities |
| 36 | Nonlinear & Advanced | Solitons | Stable self-reinforcing wave packets; dispersion balanced by nonlinearity | Fiber optic pulses, tsunamis | Nonlinear media | Water, fiber, plasma |
| 37 | Nonlinear & Advanced | Shock waves | Abrupt pressure discontinuity from supersonic source | Sonic boom, supernova blast | Supersonic flow, explosions | Compressible media |
| 38 | Nonlinear & Advanced | Modulation (AM/FM) | One wave modifies another's amplitude or frequency | Radio broadcasting | Communications | EM carriers |
| 39 | Nonlinear & Advanced | Wave mixing | Multiple frequencies interact in nonlinear medium; produce new frequencies | Second harmonic generation | Nonlinear optics | Crystals, plasmas |
| 40 | Nonlinear & Advanced | Parametric amplification | Pump wave transfers energy to signal wave via nonlinear medium | Optical parametric oscillator | Nonlinear optics | Crystals |
| 41 | Nonlinear & Advanced | Phase locking | Waves synchronize phases through nonlinear coupling | Lasers, coupled oscillators | Nonlinear systems | Any nonlinear |
| 42 | Nonlinear & Advanced | Wave packets | Localized group of waves; particle-like behavior | Electron wavefunction | Quantum mechanics | Quantum fields |
| 43 | Quantum | Wave-particle duality | All matter exhibits both wave and particle behavior | Electron double slit | Quantum systems | Quantum fields |
| 44 | Quantum | Double-slit interference | Single particles produce interference pattern over many trials | Electron, photon, molecule experiments | Quantum systems | Quantum vacuum |
| 45 | Quantum | Aharonov-Bohm effect | Quantum phase shifts in zero-field region; vector potential matters | Electron around solenoid | Quantum EM | EM vacuum |
| 46 | Quantum | Quantum tunneling | Wavefunction penetrates classically forbidden barrier | Alpha decay, STM microscope | Quantum systems | Potential barriers |
| 47 | Quantum | Wavefunction collapse | Probabilistic superposition resolves to definite state on measurement | Schrodinger's cat, spin measurement | Quantum measurement | Quantum systems |
| 48 | Quantum | Coherence / Decoherence | Phase consistency maintained (coherence) or lost (decoherence) | Lasers vs thermal light | Quantum / macroscopic | Any |
| 49 | Quantum | Entanglement | Correlated wave states; measurement of one determines the other | EPR pairs, Bell tests | Quantum systems | Quantum vacuum |
| 50 | Boundary & Medium | Evanescent waves | Exponentially decaying waves beyond boundary; no propagation | Quantum tunneling, FTIR | Near boundaries, waveguides | Any at interface |
| 51 | Boundary & Medium | Guided waves | Waves confined to a structure by boundaries | Optical fiber, microwave waveguide | Waveguides | Fiber, metal pipes |
| 52 | Boundary & Medium | Total internal reflection | Wave reflects completely at boundary above critical angle | Fiber optics, diamond sparkle | High-to-low index boundary | Glass, water |
| 53 | Exotic & Cosmological | Cherenkov radiation | EM radiation when particle exceeds phase velocity in medium | Blue glow in nuclear reactors | Nuclear reactors, atmosphere | Dielectric media |
| 54 | Exotic & Cosmological | Spacetime stretching | Gravitational wave distortion of distances | LIGO strain measurement | Cosmic scale | Spacetime |
| 55 | Exotic & Cosmological | Vacuum fluctuations | Temporary wave excitations from uncertainty principle | Casimir effect, Lamb shift | Quantum vacuum | Quantum vacuum |

---

## Section 2: Emergent Wave Phenomena

These are **multi-factor effects** — where multiple items from Section 1 combine to
produce a distinct, often surprising result. Think of these as "wave recipes."

| # | Name | Combines | Emerges | Where |
|---|------|----------|---------|-------|
| E1 | SOFAR channel | Temperature gradient + pressure gradient + refraction (#12) | Trapped long-distance acoustic waveguide; sound travels 1000s of km | Deep ocean (~600-1200 m depth) |
| E2 | Total internal reflection | Refractive index contrast + refraction (#12) + critical angle | Perfect reflection; no transmitted wave | Optical fibers, diamond, glass-air |
| E3 | Optical fiber waveguiding | Total internal reflection (E2) + geometry + refractive index profile | Low-loss signal transmission over long distances | Internet cables, medical scopes |
| E4 | Atmospheric ducting | Temperature inversion + humidity layers + refraction (#12) | Radio/radar waves bend along Earth's surface | Atmosphere, radar systems |
| E5 | Mirage | Temperature gradient + refractive index gradient + refraction (#12) | Light bends upward; "fake water" or inverted images | Deserts, hot roads |
| E6 | Whispering gallery mode | Curved geometry + continuous reflection (#11) + coherence (#48) | Waves travel along curved walls with very low loss | Domes (St Paul's), ring resonators |
| E7 | Standing wave modes | Reflection (#11) + interference (#14,#15) + boundary conditions | Fixed discrete patterns (nodes); quantized frequencies | Strings, cavities, atoms |
| E8 | Bragg reflection | Periodic structure + interference (#14,#15) | Selective reflection of specific wavelengths only | Crystals, photonic materials |
| E9 | Photonic band gap | Periodic refractive index + interference (#14,#15) + resonance (#17) | Forbidden frequency bands; light cannot propagate | Photonic crystals |
| E10 | Anderson localization | Disorder + interference (#14,#15) | Waves get trapped without boundaries; exponential confinement | Disordered media, cold atoms |
| E11 | Soliton formation | Dispersion (#23) + nonlinearity | Stable self-maintaining wave packet; shape preserved | Fiber optics, shallow water |
| E12 | Sonic boom / shock wave | Supersonic motion + compression + nonlinearity | Abrupt pressure discontinuity; Mach cone | Jets, explosions, whip crack |
| E13 | Cherenkov radiation | Particle speed > phase velocity + EM interaction | Cone of light emission (optical shock wave) | Nuclear reactors, cosmic rays |
| E14 | Beats | Two close frequencies + interference (#14,#15) | Amplitude modulation at difference frequency | Acoustics, radio, music tuning |
| E15 | Resonance catastrophe | Resonance (#17) + sustained driving + low damping | Exponential amplitude growth; structural failure | Tacoma Narrows bridge, wine glass |
| E16 | Black hole horizon | Total internal reflection (E2) + extreme spacetime curvature | Refractive index -> infinity; no wave escapes | Black holes |
| E17 | Gravitational lensing | Refraction (#12) + spacetime curvature (gravity) | Light bends around massive objects; multiple images | Galaxy clusters, stars |
| E18 | Hawking radiation | Vacuum fluctuations (#55) + horizon (E16) + quantum tunneling (#46) | Thermal radiation from black hole; T = hbar*c^3/(8*pi*G*M*k_B) | Black hole horizons |
| E19 | Superradiance | Parametric amplification (#40) + rotating horizon (E16) | Wave extracts rotational energy from black hole | Kerr black holes |
| E20 | Gravitational redshift | Redshift (#34) + spacetime curvature | Photon loses energy climbing out of gravity well | GPS satellites, white dwarfs |
| E21 | Cosmological redshift | Redshift (#34) + spacetime stretching (#54) | Light wavelength stretched by expanding universe | Distant galaxies |
| E22 | Phase locking (gravity) | Phase coupling (#41) + matter waves (#3) + spacetime field | Gravity as constructive interference between matter and spacetime | PDTP framework |
| E23 | Phase decoupling | Destructive interference (#15) + phase coupling (#41) | Zero gravitational coupling; alpha = cos(psi-phi) -> 0 | PDTP prediction |
| E24 | Spacetime birefringence | Birefringence (#29) + massive vs massless modes + condensate anisotropy | Breathing mode (massive) and tensor modes (massless) travel at different speeds | PDTP prediction |
| E25 | Dark energy as beats | Beats (E14) + cosmological phase fields | Slow phase drift between condensate and matter produces accelerating expansion | PDTP prediction (Part 25) |

---

## Section 3: Wave Domains (where waves can happen)

A catalog of physical domains where wave phenomena occur. These are "arenas" —
not necessarily physical layers of the condensate (see Section 3a for that).

| # | Layer | Field / Medium | Characteristic Waves | Key Parameters | Typical Speed | PDTP Status |
|---|-------|---------------|---------------------|----------------|---------------|-------------|
| L1 | Spacetime (gravity) | Metric g_uv / condensate phi | GW tensor (+, x), breathing scalar | kappa, rho, G, c | c | Core — condensate IS spacetime |
| L2 | Electromagnetic (QED) | A_mu, F_uv | Photons (transverse EM waves) | alpha_EM, e, epsilon_0, mu_0 | c | Independent DOF (spin-1); not from condensate |
| L3 | Strong (QCD) | Gluon field A_mu^a (SU(3)) | Color flux tubes, gluon waves | alpha_s, Lambda_QCD, sigma | c | SU(3) condensate extension (Part 37) |
| L4 | Weak | W+/-, Z bosons (SU(2)) | Massive gauge bosons | g_W, m_W, m_Z, theta_W | < c (massive) | EW symmetry breaking; dispersion from mass gap |
| L5 | Higgs | Higgs field H | Higgs boson (scalar excitation) | v = 246 GeV, m_H = 125 GeV, lambda | < c (massive) | phi_- as reversed Higgs analog (Part 62) |
| L6 | Matter-wave (quantum) | Wavefunction psi | de Broglie waves, atomic orbitals | hbar, m, lambda_dB = h/p | v < c | psi_i fields in PDTP Lagrangian |
| L7 | Acoustic (mechanical) | Bulk matter (density, pressure) | Sound, seismic P/S waves | rho_matter, bulk modulus K, shear modulus mu | ~340 m/s (air) to ~6 km/s (rock) | Analogy: c^2 = kappa/rho mirrors c_s^2 = K/rho |
| L8 | Fluid surface | Water, atmosphere interfaces | Ocean waves, capillary waves | surface tension, gravity, depth | ~1-200 m/s | SOFAR = natural waveguide analog |
| L9 | Plasma | Ionized gas | Alfven waves, Langmuir waves | B, n_e, T, omega_pe | v_A (Alfven) | Not yet explored in PDTP |
| L10 | Cosmological | Expanding spacetime | CMB fluctuations, BAO | H_0, Omega_m, Omega_Lambda | c | Phase drift model (Part 25); Lambda = free param (Part 54) |

### Layer Interactions (where PDTP makes claims)

- **L1 <-> L6:** Gravity = phase locking between spacetime (phi) and matter (psi). This is the core PDTP mechanism.
- **L1 <-> L3:** SU(3) condensate extension; QCD flux tubes from Z_3 vortices in condensate.
- **L1 <-> L5:** phi_- (breathing mode) has reversed Higgs behavior: massless in vacuum, massive near matter.
- **L1 <-> L10:** Dark energy from slow phase drift (beats) between phi and psi fields.
- **L1 <-> L7:** Exact structural analogy: c^2 = kappa/rho in both; PDTP spacetime IS a superfluid/elastic medium.
- **L2, L3:** Independent gauge sectors — PDTP does NOT derive EM or QCD coupling running from condensate (Part 80 confirmed).

---

## Section 3a: Physical Condensate Layers (the actual structure)

Section 3 catalogs wave "arenas." This section describes the **actual physical
layer structure** of the PDTP condensate — like how the ocean has real physical
layers (surface / thermocline / deep water) with boundaries between them.

**Source:** `condensate_layers.py` (standalone investigation); Parts 37, 53, 61.

### The Three Condensate Layers

PDTP has three confirmed condensate layers, each with the **same Lagrangian
structure** but different gauge group, condensate mass, and coupling:

```
L = K Tr[(dU)^dag(dU)] + g Re[Tr(Psi^dag U)] / N
```

| # | Layer | Gauge Group | m_cond | VEV / Scale | Coupling | Vortex Winding | Phase Transition |
|---|-------|-------------|--------|-------------|----------|----------------|------------------|
| C1 | Gravitational (deepest) | U(1) | m_P = 1.22 x 10^19 GeV | m_P | G = hbar*c/m_P^2 | n (any integer) | Unknown (Planck scale?) |
| C2 | QCD (middle) | SU(3) | Lambda_QCD ~ 200 MeV | ~200 MeV | alpha_s ~ 0.12 | n/3 (fractional) | ~150 MeV (hadronization) |
| C3 | Electroweak (top) | SU(2) x U(1) | v = 246 GeV | 246 GeV | alpha_EM ~ 1/137 | n/2 (half-integer) | ~160 GeV (Higgs mechanism) |

**Ordering:** By energy density (heaviest sinks to bottom). The gravitational layer
is the densest and most fundamental — it is the "container" of the density tower.

### Oil-Water-Air Analogy

The layers are **immiscible** — they cannot mix because their topological defects
(vortex windings) are incompatible. This is exactly like oil and water: they coexist
but do not blend.

```
AIR         <-->  Electroweak (SU(2)xU(1))   lightest, on top
---------         -------- boundary: EW phase transition (160 GeV) --------
WATER       <-->  QCD (SU(3))                 middle density
---------         -------- boundary: QCD phase transition (150 MeV) --------
OIL         <-->  Gravitational (U(1))        densest, at bottom
```

### Boundaries Between Layers

The boundaries are **physically real interfaces** — like the thermocline in the
ocean or the oil-water surface. This is where the most interesting physics happens:

| Boundary | Between | Phase Transition | Temperature | What Happens |
|----------|---------|-----------------|-------------|--------------|
| B1 | Gravitational / QCD | QCD confinement | ~150 MeV (~1.7 x 10^12 K) | Flux tubes form; quarks get confined; hadrons appear |
| B2 | QCD / Electroweak | EW symmetry breaking | ~160 GeV (~1.9 x 10^15 K) | Higgs mechanism; W/Z bosons become massive |
| B3 | Gravitational / Planck? | Unknown | ~10^19 GeV (~10^32 K) | All layers merge? Quantum gravity regime |

**Key insight:** These boundaries are not just abstract — they are where
**interference, confinement, and cross-layer effects** occur. The boundary
itself acts as a layer where particles interact with both sides.

### What Can Cross Between Layers?

This is the confinement table — which particles can exist in which layers,
and which can cross boundaries:

| Particle | Winding | Layer Compatibility | Crosses Boundary? | Analogy |
|----------|---------|--------------------|--------------------|---------|
| Baryon (3 quarks) | 3 x 1/3 = 1 | Integer -> valid in U(1) gravitational | YES — crosses B1 | Soap (surfactant): made of oil-soluble parts but the combination works in water |
| Meson (q + qbar) | 1/3 + (-1/3) = 0 | Zero winding -> invisible to U(1) | YES — crosses B1 | Neutral molecule: passes through interface |
| Single quark | 1/3 | Not integer -> CONFINED to SU(3) | NO — trapped below B1 | Dye in oil: cannot cross into water |
| Lepton (electron) | 1 (integer) | Already in U(1) -> free | YES — lives above B1 | Salt in water: lives in water layer, doesn't know oil exists |
| W/Z boson | SU(2) adjoint | Confined to SU(2) above EW scale | NO — trapped above B2 (massive) | Foam on water surface: confined to top layer |
| Photon | U(1) gauge | Gauge field of U(1) -> free | YES — propagates everywhere | Light: passes through all transparent layers |
| Gluon | SU(3) adjoint | Confined to SU(3) | NO — trapped between B1 and B2 | Currents inside oil: can't escape into water |

**This IS colour confinement, restated topologically.** A quark has winding 1/3
in SU(3), but U(1) only allows integer windings. The quark literally cannot exist
as a standalone defect in the gravitational layer. Three quarks together (winding
3 x 1/3 = 1) CAN exist — that's a baryon.

### Boundary Physics: Where Interference Happens

The boundaries are where the wave effects from Section 1 become most interesting:

- **At B1 (Grav/QCD boundary):** This is where quarks get confined into hadrons.
  The interference pattern at this boundary determines which composites can form.
  Flux tubes (Section 2, E7 standing wave modes) stretch between quarks within the
  QCD layer. When they try to cross into the gravitational layer, the winding
  mismatch forces them to snap — producing new quark pairs (string breaking).

- **At B2 (QCD/EW boundary):** This is where the Higgs mechanism operates.
  Above this boundary (high energy), W/Z bosons are massless and free. Below it,
  they acquire mass from the Higgs VEV — like a wave entering a dispersive medium
  and acquiring a mass gap (Section 1 #23 dispersion).

- **Leptons at B1:** The electron has integer winding (1) in U(1), so it can
  exist in the gravitational layer freely. But it also couples to the electroweak
  layer (it has weak charge). It lives IN the gravitational layer but can INTERACT
  with the QCD layer through virtual photons — like salt dissolved in water that
  can sense the oil layer through surface vibrations, but never enters it.

- **Proton as bridge:** The proton is a composite (3 quarks = integer winding)
  that couples to BOTH the QCD layer (via quarks) and the gravitational layer
  (via integer winding). It acts as a **surfactant** — a molecule with one end
  in oil and one end in water. This is how the layers communicate indirectly:
  not through bulk coupling, but through shared defects.

### No Direct Cross-Layer Coupling

The PDTP Lagrangian has **no cross terms** between layers:

```
L_total = L_grav(phi, psi) + L_QCD(U, Psi) + L_EW(Phi_H, psi)
```

Each layer couples to matter independently. There is no phi-U or U-Phi_H term.
This is **consistent with immiscibility** — oil and water don't interact through
their bulk, only at the interface through shared objects (surfactants = composite
particles).

---

## Section 4: Variables & Parameters

Every variable that governs wave behavior, regardless of wave type. These are the
"knobs" — if you can control these, you can control waves.

| # | Name | Type | Unit | Description | How Used in Waves |
|---|------|------|------|-------------|-------------------|
| V1 | Wavelength (lambda) | Spatial | m (meters) | Distance between consecutive crests | Sets spatial scale; lambda = v/f; determines diffraction regime |
| V2 | Frequency (f) | Temporal | Hz (1/s) | Oscillations per second | Sets time scale; energy E = hf (quantum); determines resonance |
| V3 | Angular frequency (omega) | Temporal | rad/s | Rate of phase change; omega = 2*pi*f | Used in dispersion relations: omega(k) |
| V4 | Wave number (k) | Spatial | rad/m | Spatial rate of phase change; k = 2*pi/lambda | Momentum p = hbar*k (quantum); dispersion omega(k) |
| V5 | Amplitude (A) | Magnitude | varies (m, V/m, Pa) | Maximum displacement from equilibrium | Energy proportional to A^2; determines intensity |
| V6 | Phase (phi) | Angular | rad (radians) | Position within oscillation cycle (0 to 2*pi) | Determines interference (constructive/destructive); PDTP: alpha = cos(psi-phi) |
| V7 | Period (T) | Temporal | s (seconds) | Time for one complete cycle; T = 1/f | Sets temporal scale of oscillation |
| V8 | Wave speed / phase velocity (v_p) | Velocity | m/s | Speed at which phase pattern propagates; v = f*lambda | Medium-dependent; can exceed c; determines refraction via Snell's law |
| V9 | Group velocity (v_g) | Velocity | m/s | Speed of wave packet envelope; v_g = d(omega)/dk | Carries energy and information; <= c for physical signals |
| V10 | Refractive index (n) | Dimensionless | (none) | Ratio c/v_medium; describes how much medium slows wave | Controls refraction: n1*sin(theta1) = n2*sin(theta2); higher n = more bending |
| V11 | Impedance (Z) | Medium property | varies (Pa*s/m, Ohm) | Resistance to wave propagation; Z = sqrt(stiffness * density) | Reflection at boundaries: R = ((Z2-Z1)/(Z2+Z1))^2; impedance matching |
| V12 | Density (rho) | Medium property | kg/m^3 | Mass per unit volume of medium | Wave speed: c^2 = stiffness/rho; higher density = slower waves |
| V13 | Stiffness / elastic modulus (K, mu) | Medium property | Pa (N/m^2) | Resistance of medium to deformation | Wave speed: c^2 = K/rho (longitudinal), c^2 = mu/rho (transverse) |
| V14 | Damping coefficient (gamma) | Temporal | 1/s | Rate of energy loss; amplitude decays as e^(-gamma*t) | Controls attenuation; Q factor = omega/(2*gamma) |
| V15 | Quality factor (Q) | Dimensionless | (none) | Ratio of energy stored to energy lost per cycle | High Q = sharp resonance, low damping; Q = omega_0/(2*gamma) |
| V16 | Coupling strength (g) | Interaction | varies (rad/s in PDTP) | How strongly two systems exchange energy | Phase locking strength; PDTP: g = omega_P = M_P*c^2/hbar |
| V17 | Nonlinearity parameter | Medium property | varies | Deviation from linear response at high amplitude | Enables solitons, harmonics, shock waves, wave mixing |
| V18 | Polarization state | Vector | (none) | Direction of oscillation (linear, circular, elliptical) | Only for transverse waves; determines birefringence, dichroism |
| V19 | Bandwidth (Delta_f) | Spectral | Hz | Range of frequencies in a wave packet | Uncertainty: Delta_f * Delta_t >= 1/(4*pi); wider = shorter pulse |
| V20 | Coherence length (L_c) | Spatial | m | Distance over which phase relationship is maintained | Determines interference visibility; L_c = c/(Delta_f) |
| V21 | Coherence time (tau_c) | Temporal | s | Time over which phase relationship is maintained | tau_c = 1/Delta_f; laser >> thermal source |
| V22 | Dispersion relation | Functional | omega(k) | The relationship between frequency and wave number | THE master equation: determines v_p, v_g, mass gap, everything |
| V23 | Mass gap (omega_gap) | Frequency | rad/s | Minimum frequency for propagation in dispersive medium | omega^2 = c^2*k^2 + omega_gap^2; particle mass = hbar*omega_gap/c^2 |
| V24 | Attenuation coefficient (alpha_att) | Spatial | 1/m (or dB/m) | Rate of amplitude decay with distance | Intensity: I = I_0 * e^(-2*alpha_att*x); frequency dependent |
| V25 | Surface tension (sigma_s) | Interface property | N/m | Force per unit length at interface | Capillary waves: omega^2 = (sigma_s/rho)*k^3; controls ripples |
| V26 | Temperature (T) | Thermodynamic | K (Kelvin) | Thermal energy of medium | Affects speed of sound; creates gradients (SOFAR, mirages, ducting) |
| V27 | Pressure (P) | Thermodynamic | Pa (N/m^2) | Force per unit area in medium | Affects density and wave speed; shock waves from pressure jumps |
| V28 | Gravitational potential (Phi) | Field | m^2/s^2 (or dimensionless Phi/c^2) | Strength of gravitational field; Phi = GM/(Rc^2) | PDTP: phi_- mass depends on Phi; redshift: Delta_f/f = Delta_Phi/c^2 |

---

## How to Use This Reference

1. **Checking PDTP completeness:** Go through Section 1 row by row. For each wave
   effect, ask: does PDTP predict/explain this? How? (See wave_effects_pdtp.md for
   existing mappings of effects 1-50.)

2. **Checking emergent phenomena:** Section 2 shows what COMBINATIONS produce new
   effects. When proposing a PDTP mechanism, check: which Section 1 ingredients
   does it use? Are there emergent effects (Section 2) that should also appear?

3. **Layer analysis:** Section 3 shows which layer a phenomenon lives in. PDTP makes
   specific claims about layer connections — check these are consistent.

4. **Parameter completeness:** Section 4 lists every knob. When deriving a PDTP
   result, check: which variables appear? Are any missing that should be there?
   Are any present that shouldn't be?

5. **Engineering translation:** For experimental design, Section 4 tells you what
   you need to control. Section 2 tells you what combinations produce useful effects.
