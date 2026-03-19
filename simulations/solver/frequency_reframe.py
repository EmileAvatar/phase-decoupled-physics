#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
frequency_reframe.py -- Conceptual exploration: spacetime as frequency
======================================================================
NOT a numbered Part. Exploratory analysis of:
  1. Planck frequency as a harmonic of particle Compton frequencies
  2. Spacetime at LOW frequency (Hubble) vs HIGH frequency (Planck)
  3. Check against +cos Lagrangian (single-phase)
  4. Check against two-phase Lagrangian (phi_+, phi_-)
  5. The cosmological constant as a frequency ratio

This is a REFRAMING exercise, not new physics. All equations are from
established PDTP results (Parts 29-67).
"""

import numpy as np
from sudoku_engine import HBAR, C, G, M_P, M_E, L_P, M_P_PROTON, ALPHA_EM
from print_utils import ReportWriter
import os

# -----------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------
_HERE = os.path.dirname(os.path.abspath(__file__))

# Particle masses (kg)
M_MUON = 1.8835e-28
M_TAU = 3.1675e-27
M_NEUTRINO_E = 1.0e-36       # ~0.06 eV upper bound
M_HIGGS = 2.2319e-25
M_W = 1.4328e-25
M_Z = 1.6255e-25
M_TOP = 3.0784e-25

# Hubble constant
H_0 = 2.184e-18   # rad/s  (67.4 km/s/Mpc)

# Planck frequency
OMEGA_P = M_P * C**2 / HBAR

# Cosmological constant energy density
RHO_LAMBDA = 5.96e-27  # kg/m^3 (observed)
RHO_PLANCK = C**5 / (HBAR * G**2)  # Planck density


def compton_freq(m):
    """Compton frequency omega = m*c^2/hbar"""
    return m * C**2 / HBAR


def compton_wavelength(m):
    """Reduced Compton wavelength lambda_C = hbar/(m*c)"""
    return HBAR / (m * C)


def main():
    output_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(output_dir, label="frequency_reframe")

    rw.section("Frequency Reframe: Spacetime as Oscillator")
    rw.print("  Exploratory analysis -- not a numbered Part")
    rw.print("  All equations from established PDTP results (Parts 29-67)")
    rw.print("")

    # ==================================================================
    # SECTION 1: The frequency ladder
    # ==================================================================
    rw.subsection("1. The Frequency Ladder -- Every Scale Has a Frequency")
    rw.print("")
    rw.print("  In QM, energy = frequency: E = hbar * omega")
    rw.print("  Every mass has a Compton frequency: omega = m*c^2/hbar")
    rw.print("  GR has NO frequency -- PDTP says spacetime oscillates at omega_gap")
    rw.print("")

    particles = [
        ("Hubble (H_0)",         H_0,                    "cosmological"),
        ("neutrino (e)",         compton_freq(M_NEUTRINO_E), "particle"),
        ("electron",             compton_freq(M_E),      "particle"),
        ("muon",                 compton_freq(M_MUON),   "particle"),
        ("proton",               compton_freq(M_P_PROTON), "particle"),
        ("tau",                  compton_freq(M_TAU),    "particle"),
        ("W boson",              compton_freq(M_W),      "particle"),
        ("Z boson",              compton_freq(M_Z),      "particle"),
        ("Higgs",                compton_freq(M_HIGGS),  "particle"),
        ("top quark",            compton_freq(M_TOP),    "particle"),
        ("Planck (omega_P)",     OMEGA_P,                "Planck scale"),
    ]

    rw.print("  {:25s} {:>15s} {:>15s} {:>12s}".format(
        "Scale", "omega (rad/s)", "log10(omega)", "Type"))
    rw.print("  " + "-" * 72)
    for name, omega, ptype in particles:
        rw.print("  {:25s} {:15.4e} {:15.2f} {:>12s}".format(
            name, omega, np.log10(omega), ptype))

    rw.print("")
    rw.print("  Total range: {:.1f} decades (Hubble to Planck)".format(
        np.log10(OMEGA_P / H_0)))
    rw.print("")

    # ==================================================================
    # SECTION 2: Planck as harmonic
    # ==================================================================
    rw.subsection("2. Planck as the n-th Harmonic")
    rw.print("")
    rw.print("  From Part 33: n = m_cond/m_particle = omega_gap/omega_particle")
    rw.print("  If m_cond = m_P, then omega_gap = omega_P")
    rw.print("  => omega_P = n * omega_particle  (Planck IS the n-th harmonic)")
    rw.print("")

    rw.print("  {:20s} {:>15s} {:>12s} {:>15s}".format(
        "Particle", "omega (rad/s)", "n = m_P/m", "n^2 = 1/alpha_G"))
    rw.print("  " + "-" * 65)

    particle_data = [
        ("neutrino (e)", M_NEUTRINO_E),
        ("electron",     M_E),
        ("muon",         M_MUON),
        ("proton",       M_P_PROTON),
        ("tau",          M_TAU),
        ("W boson",      M_W),
        ("Z boson",      M_Z),
        ("Higgs",        M_HIGGS),
        ("top quark",    M_TOP),
    ]

    for name, mass in particle_data:
        omega = compton_freq(mass)
        n = M_P / mass
        rw.print("  {:20s} {:15.4e} {:12.4e} {:15.4e}".format(
            name, omega, n, n**2))

    rw.print("")
    rw.print("  KEY: n is the 'harmonic number' of Planck relative to each particle.")
    rw.print("  The hierarchy problem = 'why are these harmonic numbers so large?'")
    rw.print("  In music: 22nd harmonic is already exotic.")
    rw.print("  In PDTP: the 10^22-nd harmonic (for electron) IS gravity's weakness.")
    rw.print("")

    # ==================================================================
    # SECTION 3: What if spacetime is LOW frequency?
    # ==================================================================
    rw.subsection("3. Scenario A: Spacetime at LOW Frequency (Hubble)")
    rw.print("")
    rw.print("  What if the condensate oscillates at H_0 ~ {:.3e} rad/s?".format(H_0))
    rw.print("  Then Planck would be a HIGH harmonic of the Hubble frequency:")
    rw.print("")

    n_hubble_planck = OMEGA_P / H_0
    rw.print("  omega_P / H_0 = {:.4e}".format(n_hubble_planck))
    rw.print("  (omega_P / H_0)^2 = {:.4e}".format(n_hubble_planck**2))
    rw.print("")
    rw.print("  Compare to cosmological constant problem:")
    ratio_lambda = RHO_LAMBDA / RHO_PLANCK
    rw.print("  rho_Lambda / rho_Planck = {:.4e}".format(ratio_lambda))
    rw.print("  (H_0 / omega_P)^2       = {:.4e}".format((H_0 / OMEGA_P)**2))
    rw.print("")
    rw.print("  RESULT: (H_0/omega_P)^2 ~ rho_Lambda/rho_Planck ~ 10^-122")
    rw.print("  The cosmological constant IS the frequency ratio squared!")
    rw.print("")

    # Check: what G would Hubble-frequency spacetime predict?
    # From G = hbar*c / m_cond^2 (Part 33)
    # If omega_gap = H_0, then m_cond = hbar*H_0/c^2
    m_cond_hubble = HBAR * H_0 / C**2
    G_hubble = HBAR * C / m_cond_hubble**2
    rw.print("  If omega_gap = H_0:")
    rw.print("    m_cond = hbar*H_0/c^2 = {:.4e} kg  ({:.4e} eV)".format(
        m_cond_hubble, m_cond_hubble * C**2 / 1.602e-19))
    rw.print("    G_pred = hbar*c/m_cond^2 = {:.4e} m^3 kg^-1 s^-2".format(G_hubble))
    rw.print("    G_known = {:.5e}".format(G))
    rw.print("    Ratio G_pred/G_known = {:.4e}  (OFF by {:.1f} decades)".format(
        G_hubble / G, np.log10(G_hubble / G)))
    rw.print("")
    rw.print("  VERDICT: Hubble-frequency spacetime gives G ~ 10^122 times too large.")
    rw.print("  Gravity would be overwhelmingly strong -- not what we observe.")
    rw.print("  Slow spacetime = strong gravity. Fast spacetime = weak gravity.")
    rw.print("")

    # ==================================================================
    # SECTION 4: What if spacetime is HIGH frequency (Planck)?
    # ==================================================================
    rw.subsection("4. Scenario B: Spacetime at HIGH Frequency (Planck)")
    rw.print("")
    rw.print("  If omega_gap = omega_P ~ {:.4e} rad/s:".format(OMEGA_P))
    rw.print("  m_cond = m_P = {:.4e} kg".format(M_P))
    rw.print("  G_pred = hbar*c/m_P^2 = {:.5e}  (= G_known exactly)".format(
        HBAR * C / M_P**2))
    rw.print("")
    rw.print("  This is the standard PDTP picture (Parts 29-35).")
    rw.print("  Spacetime oscillates at Planck frequency -- so fast that")
    rw.print("  everything we observe (atoms, planets, light) is SLOW compared to it.")
    rw.print("  GR emerges as the time-averaged behavior over many Planck oscillations.")
    rw.print("")

    # What about even HIGHER than Planck?
    rw.print("  What about HIGHER than Planck?")
    for factor, label in [(10, "10x Planck"), (100, "100x Planck"),
                          (1e10, "10^10 x Planck")]:
        m_cond = M_P * factor
        G_pred = HBAR * C / m_cond**2
        rw.print("    omega = {} (m_cond = {:.2e} kg): G = {:.4e}, ratio = {:.4e}".format(
            label, m_cond, G_pred, G_pred / G))
    rw.print("")
    rw.print("  Higher frequency = smaller G = weaker gravity.")
    rw.print("  Lower frequency = larger G = stronger gravity.")
    rw.print("  G ~ 1/omega_gap^2 -- inverse square law in FREQUENCY space!")
    rw.print("")

    # ==================================================================
    # SECTION 5: Check against single-phase (+cos) Lagrangian
    # ==================================================================
    rw.subsection("5. Single-Phase (+cos) Lagrangian Check")
    rw.print("")
    rw.print("  L = 1/2(d_mu phi)^2 + 1/2(d_mu psi)^2 + g*cos(psi - phi)")
    rw.print("")
    rw.print("  Field equations:")
    rw.print("    box(phi) = g*sin(psi - phi)")
    rw.print("    box(psi) = -g*sin(psi - phi)")
    rw.print("")

    # Dispersion relation
    rw.print("  Dispersion relation (condensate excitations):")
    rw.print("    omega^2 = c^2*k^2 + omega_gap^2")
    rw.print("    where omega_gap^2 = 2*g*Phi_0 (from linearization around background)")
    rw.print("")

    # Key frequency properties
    rw.print("  KEY FREQUENCY PROPERTIES:")
    rw.print("")
    rw.print("  1. GAP FREQUENCY: omega_gap = m_cond*c^2/hbar")
    rw.print("     - Below omega_gap: no propagating modes (evanescent)")
    rw.print("     - At omega_gap: standing wave (rest mass of excitation)")
    rw.print("     - Above omega_gap: propagating waves")
    rw.print("")
    rw.print("  2. PHASE-LOCKING: cos(psi - phi) requires psi ~ phi")
    rw.print("     - Phase-locked: psi - phi ~ 0  -> gravity (attractive)")
    rw.print("     - Phase-unlocked: psi - phi ~ pi  -> anti-gravity")
    rw.print("     - For phase-locking: both fields must be able to 'track' each other")
    rw.print("")

    # The frequency matching question
    rw.print("  3. FREQUENCY MATCHING:")
    rw.print("     If phi oscillates at omega_gap and psi at omega_particle:")
    rw.print("     cos(psi - phi) = cos((omega_p - omega_gap)*t + spatial terms)")
    rw.print("")
    rw.print("     CASE A: omega_gap = omega_particle  (resonance)")
    rw.print("       -> cos(0 + ...) = cos(spatial phase) -> static force -> GRAVITY")
    rw.print("       This happens when m_cond = m_particle (winding n=1)")
    rw.print("")
    rw.print("     CASE B: omega_gap >> omega_particle  (Planck >> Compton)")
    rw.print("       -> cos(huge*t + ...) -> rapidly oscillating -> averages to zero??")
    rw.print("       BUT: the condensate background is a STATIC condensate,")
    rw.print("       not a freely oscillating wave. The gap frequency is the REST")
    rw.print("       frequency of excitations, not the background oscillation.")
    rw.print("")
    rw.print("     RESOLUTION: In BEC language, the condensate has a MACROSCOPIC")
    rw.print("     occupation of the k=0 mode. Its phase phi(x,t) = omega_gap*t + theta(x).")
    rw.print("     The temporal part omega_gap*t is GLOBAL and unobservable")
    rw.print("     (like the overall phase of a BEC -- Goldstone mode).")
    rw.print("     What couples to matter is the SPATIAL phase gradient: nabla(theta).")
    rw.print("     Gravity comes from spatial phase gradients, NOT temporal oscillations.")
    rw.print("")
    rw.print("  4. SO WHAT DOES omega_gap CONTROL?")
    rw.print("     omega_gap = m_cond*c^2/hbar sets:")
    rw.print("     - The mass of the lightest excitation above the condensate (breathing mode)")
    rw.print("     - The healing length: xi = hbar/(m_cond*c) = l_P/sqrt(2)  [if m_cond=m_P]")
    rw.print("     - Newton's constant: G = hbar*c/m_cond^2 = c^3/(hbar*omega_gap^2)")
    rw.print("     - The strength of gravity: HIGHER omega_gap = WEAKER gravity")
    rw.print("")

    # Numerical: G as function of omega_gap
    rw.print("  G vs omega_gap (inverse-square relationship):")
    rw.print("  {:>20s} {:>15s} {:>15s}".format("omega_gap (rad/s)", "G_pred", "G_pred/G_known"))
    rw.print("  " + "-" * 55)
    for log_omega in [0, 10, 20, 30, 40, 43.27, 50, 60]:
        omega = 10**log_omega
        m_cond = HBAR * omega / C**2
        G_pred = HBAR * C / m_cond**2 if m_cond > 0 else float('inf')
        # Equivalently G = c^3 / (hbar * omega^2) but use m_cond form
        G_pred2 = C**5 / (HBAR * omega**2)
        ratio = G_pred2 / G
        rw.print("  {:>20.4e} {:15.4e} {:15.4e}".format(omega, G_pred2, ratio))

    rw.print("")
    rw.print("  omega_gap = omega_P ~ 10^43.27 gives G = G_known (by definition)")
    rw.print("  Every decade change in omega_gap changes G by 2 decades (inverse square)")
    rw.print("")

    # ==================================================================
    # SECTION 6: Check against two-phase Lagrangian
    # ==================================================================
    rw.subsection("6. Two-Phase Lagrangian Check")
    rw.print("")
    rw.print("  L = +g*cos(psi - phi_b) - g*cos(psi - phi_s)")
    rw.print("")
    rw.print("  phi_+ = (phi_b + phi_s)/2  = gravity mode (average)")
    rw.print("  phi_- = (phi_b - phi_s)/2  = surface mode (difference)")
    rw.print("")
    rw.print("  TWO FREQUENCY SCALES EMERGE NATURALLY:")
    rw.print("")

    # phi_+ frequency
    rw.print("  phi_+ (gravity mode):")
    rw.print("    Gap frequency: omega_+ ~ omega_gap = m_cond*c^2/hbar = omega_P")
    rw.print("    This is the HIGH frequency scale (~10^43 Hz)")
    rw.print("    Controls: Newton's constant, healing length, graviton mass")
    rw.print("")

    # phi_- frequency
    rw.print("  phi_- (surface mode) -- the REVERSED HIGGS (Part 62):")
    rw.print("    In vacuum: MASSLESS (m^2 = 0) -> frequency can be ARBITRARILY LOW")
    rw.print("    Near matter: MASSIVE (m^2 = 2*g*Phi) -> frequency rises")
    rw.print("    This is the opposite of the Higgs: Higgs is massive in vacuum,")
    rw.print("    massless near the symmetry-breaking field.")
    rw.print("")
    rw.print("  THE TWO-PHASE INSIGHT:")
    rw.print("    The two-phase Lagrangian NATURALLY produces two frequency scales:")
    rw.print("    - phi_+ at PLANCK frequency   (~10^43 Hz)  -- gravity")
    rw.print("    - phi_- at COSMOLOGICAL frequency  (~10^-18 Hz)  -- dark energy??")
    rw.print("")

    # The frequency ratio
    omega_plus = OMEGA_P
    omega_minus_cosmo = H_0  # hypothesis
    ratio = omega_minus_cosmo / omega_plus
    rw.print("  If phi_- oscillates at Hubble frequency:")
    rw.print("    omega_- / omega_+ = H_0 / omega_P = {:.4e}".format(ratio))
    rw.print("    (omega_- / omega_+)^2 = {:.4e}".format(ratio**2))
    rw.print("    rho_Lambda / rho_Planck = {:.4e}".format(RHO_LAMBDA / RHO_PLANCK))
    rw.print("")
    rw.print("  MATCH: (H_0/omega_P)^2 ~ rho_Lambda/rho_Planck ~ 10^-122")
    rw.print("  The cosmological constant problem IS the ratio of the two phase frequencies!")
    rw.print("")

    # Jeans eigenvalue check
    rw.print("  Jeans eigenvalue (Part 61): +2*sqrt(2)*g > 0  (gravitational collapse)")
    rw.print("  This is the phi_+ mode -- HIGH frequency, attractive.")
    rw.print("  The phi_- mode has NEGATIVE eigenvalue (repulsive -- surface tension).")
    rw.print("  Two modes, two frequencies, two forces: gravity + dark energy.")
    rw.print("")

    # Newton's 3rd law check
    rw.print("  Newton's 3rd law: psi_ddot = -2*phi_+_ddot  (Part 61)")
    rw.print("  This is about phi_+ ONLY. The phi_- mode does NOT enter Newton's laws.")
    rw.print("  phi_- is a SEPARATE degree of freedom -- the 'dark sector'.")
    rw.print("")

    # ==================================================================
    # SECTION 7: Beat frequencies / combination tones
    # ==================================================================
    rw.subsection("7. Beat Frequencies and Combination Tones (Heterodyne Mixing)")
    rw.print("")
    rw.print("  TUNING FORK ANALOGY:")
    rw.print("  Two tuning forks at f1=400 Hz and f2=450 Hz produce:")
    rw.print("    - f1 = 400 Hz  (original)")
    rw.print("    - f2 = 450 Hz  (original)")
    rw.print("    - |f2-f1| = 50 Hz   (BEAT / difference tone)")
    rw.print("    - f1+f2 = 850 Hz   (SUM tone / combination tone)")
    rw.print("")
    rw.print("  This happens because the interaction is NONLINEAR.")
    rw.print("  Linear superposition: you just hear both tones separately.")
    rw.print("  Nonlinear mixing: new frequencies appear (sum and difference).")
    rw.print("")
    rw.print("  Names for this effect:")
    rw.print("    Acoustics:  combination tones, Tartini tones, beat frequencies")
    rw.print("    Radio:      heterodyne mixing (AM radio works this way)")
    rw.print("    Optics:     sum/difference frequency generation")
    rw.print("    Music:      beating, resultant tones")
    rw.print("")

    # The PDTP cosine IS a nonlinear mixer
    rw.print("  THE PDTP COSINE COUPLING IS EXACTLY THIS KIND OF MIXER:")
    rw.print("")
    rw.print("  Single-phase: g * cos(psi - phi)")
    rw.print("  If psi = omega_psi * t and phi = omega_phi * t:")
    rw.print("    cos(psi - phi) = cos((omega_psi - omega_phi) * t)")
    rw.print("  This IS the beat frequency! The coupling oscillates at the DIFFERENCE.")
    rw.print("")
    rw.print("  Two-phase: the product formula (Part 61) makes it explicit:")
    rw.print("    cos(psi - phi_b) - cos(psi - phi_s)")
    rw.print("    = 2 * sin(psi - phi_+) * sin(phi_-)")
    rw.print("")
    rw.print("  The PRODUCT of two sines IS a frequency mixer:")
    rw.print("    sin(A) * sin(B) = 1/2 * [cos(A-B) - cos(A+B)]")
    rw.print("")
    rw.print("  So the two-phase coupling produces:")
    rw.print("    A = psi - phi_+  (matter-gravity phase difference)")
    rw.print("    B = phi_-        (surface mode)")
    rw.print("    -> cos(A - B) = cos(psi - phi_+ - phi_-)  [DIFFERENCE tone]")
    rw.print("    -> cos(A + B) = cos(psi - phi_+ + phi_-)  [SUM tone]")
    rw.print("")
    rw.print("  In frequencies:")
    rw.print("    A oscillates at omega_psi - omega_+  (matter-gravity beat)")
    rw.print("    B oscillates at omega_-              (surface mode)")
    rw.print("    Difference tone: (omega_psi - omega_+) - omega_-")
    rw.print("    Sum tone:        (omega_psi - omega_+) + omega_-")
    rw.print("")

    # Numerical: what combination tones does the PDTP mixer produce?
    rw.print("  NUMERICAL: What frequencies does PDTP mixing produce?")
    rw.print("")

    omega_e = compton_freq(M_E)
    omega_p = compton_freq(M_P_PROTON)

    rw.print("  Input frequencies:")
    rw.print("    omega_e (electron Compton)  = {:.4e} rad/s".format(omega_e))
    rw.print("    omega_p (proton Compton)    = {:.4e} rad/s".format(omega_p))
    rw.print("    omega_P (Planck = phi_+)    = {:.4e} rad/s".format(OMEGA_P))
    rw.print("    H_0     (Hubble = phi_-?)   = {:.4e} rad/s".format(H_0))
    rw.print("")

    # Single-phase beats
    rw.print("  SINGLE-PHASE BEATS (cos(psi - phi)):")
    rw.print("  {:30s} {:>15s} {:>12s}".format(
        "Beat", "freq (rad/s)", "log10"))
    rw.print("  " + "-" * 60)
    beats_single = [
        ("omega_P - omega_e", OMEGA_P - omega_e),
        ("omega_P - omega_p", OMEGA_P - omega_p),
        ("omega_p - omega_e", omega_p - omega_e),
        ("omega_P + omega_e", OMEGA_P + omega_e),
        ("omega_P + omega_p", OMEGA_P + omega_p),
    ]
    for label, freq in beats_single:
        rw.print("  {:30s} {:15.4e} {:12.2f}".format(label, freq, np.log10(freq)))
    rw.print("")
    rw.print("  NOTE: omega_P >> omega_e, so omega_P - omega_e ~ omega_P.")
    rw.print("  The beat frequency is essentially unchanged from Planck.")
    rw.print("  Single-phase: NO new frequencies emerge (Planck dominates everything).")
    rw.print("")

    # Two-phase combination tones
    rw.print("  TWO-PHASE COMBINATION TONES (2*sin(A)*sin(B)):")
    rw.print("  A = psi - phi_+, B = phi_-")
    rw.print("")
    rw.print("  If phi_- ~ H_0 (cosmological):")
    rw.print("  {:30s} {:>15s} {:>12s}".format(
        "Tone", "freq (rad/s)", "log10"))
    rw.print("  " + "-" * 60)

    # For electron as matter field
    A_e = omega_e - OMEGA_P  # matter-gravity beat (negative, take abs)
    B_cosmo = H_0
    tones_2phase = [
        ("A = |omega_e - omega_P|", abs(A_e)),
        ("B = omega_- (H_0)", B_cosmo),
        ("|A| - B (diff tone)", abs(abs(A_e) - B_cosmo)),
        ("|A| + B (sum tone)", abs(A_e) + B_cosmo),
    ]
    for label, freq in tones_2phase:
        rw.print("  {:30s} {:15.4e} {:12.2f}".format(label, freq, np.log10(freq)))
    rw.print("")
    rw.print("  RESULT: |A| ~ omega_P >> B ~ H_0, so sum and diff ~ omega_P again.")
    rw.print("  The huge frequency mismatch means mixing produces nothing new.")
    rw.print("")

    # BUT: what if two phi modes are CLOSE in frequency?
    rw.print("  BUT WHAT IF phi_b and phi_s are CLOSE in frequency?")
    rw.print("  Like two tuning forks almost in tune:")
    rw.print("")
    rw.print("  phi_b at omega_P + delta/2")
    rw.print("  phi_s at omega_P - delta/2")
    rw.print("  Then:")
    rw.print("    phi_+ = (phi_b + phi_s)/2 oscillates at omega_P  (Planck)")
    rw.print("    phi_- = (phi_b - phi_s)/2 oscillates at delta/2  (the BEAT)")
    rw.print("")
    rw.print("  For delta/2 = H_0:  delta = 2*H_0 = {:.4e} rad/s".format(2*H_0))
    rw.print("  phi_b freq = omega_P + H_0 = omega_P * (1 + {:.4e})".format(H_0/OMEGA_P))
    rw.print("  phi_s freq = omega_P - H_0 = omega_P * (1 - {:.4e})".format(H_0/OMEGA_P))
    rw.print("")
    rw.print("  The two condensate phases are detuned by only 1 part in 10^61!")
    rw.print("  Almost PERFECTLY in tune -- the tiniest mismatch produces")
    rw.print("  a beat note at Hubble frequency = dark energy timescale.")
    rw.print("")
    rw.print("  [SPECULATIVE] COSMOLOGICAL CONSTANT AS A BEAT FREQUENCY:")
    rw.print("  Two nearly-identical Planck-frequency oscillators,")
    rw.print("  detuned by 1 part in 10^61, produce a beat at H_0.")
    rw.print("  rho_Lambda/rho_Planck = (delta/omega_P)^2 ~ 10^-122.")
    rw.print("")
    rw.print("  CRITICAL CAVEAT: This requires 10^-61 precision tuning with NO")
    rw.print("  mechanism to explain WHY delta has this value. The numerical")
    rw.print("  coincidence is striking but not a derivation. Part 68 investigates")
    rw.print("  whether omega_- emerges from symmetry/boundary conditions (not tuning).")
    rw.print("")

    # What about particle-scale beats?
    rw.print("  PARTICLE-SCALE BEATS:")
    rw.print("  What detuning gives beats at particle Compton frequencies?")
    rw.print("")
    rw.print("  {:20s} {:>15s} {:>15s} {:>12s}".format(
        "Particle", "omega_Compton", "delta needed", "delta/omega_P"))
    rw.print("  " + "-" * 65)
    for name, mass in particle_data:
        omega_c = compton_freq(mass)
        delta = 2 * omega_c  # phi_- oscillates at delta/2 = omega_c
        ratio_d = delta / OMEGA_P
        rw.print("  {:20s} {:15.4e} {:15.4e} {:12.4e}".format(
            name, omega_c, delta, ratio_d))
    rw.print("")
    rw.print("  To produce electron Compton as a beat: detuning = 1 part in 10^22")
    rw.print("  To produce proton Compton as a beat:   detuning = 1 part in 10^19")
    rw.print("  To produce Hubble as a beat:           detuning = 1 part in 10^61")
    rw.print("")
    rw.print("  [SPECULATIVE] INTERPRETATION:")
    rw.print("  The hierarchy of particle masses COULD be a hierarchy of detunings")
    rw.print("  between the two condensate phases phi_b and phi_s.")
    rw.print("  Heavier particles = larger detuning = stronger beat.")
    rw.print("  WARNING: This is a numerical fit, NOT a derivation.")
    rw.print("  No mechanism selects these detuning values.")
    rw.print("  The hierarchy more likely comes from MULTI-MODE structure")
    rw.print("  of the condensate (see Part 68 investigation).")
    rw.print("")

    # AM radio analogy
    rw.print("  AM RADIO ANALOGY:")
    rw.print("  The two-phase coupling 2*sin(psi-phi_+)*sin(phi_-) is literally")
    rw.print("  amplitude modulation (AM):")
    rw.print("    Carrier wave:  sin(psi - phi_+)  at high frequency")
    rw.print("    Modulation:    sin(phi_-)         at low frequency")
    rw.print("    Gravity = the demodulated signal (product)")
    rw.print("")
    rw.print("  When phi_- = pi/2 (equilibrium near matter): full signal (gravity ON)")
    rw.print("  When phi_- = 0 (vacuum equilibrium): no signal (gravity OFF)")
    rw.print("  phi_- is the VOLUME KNOB for gravity.")
    rw.print("")
    rw.print("  In AM radio: you tune to the carrier (omega_P), but the INFORMATION")
    rw.print("  is in the modulation envelope (phi_-). The physics we observe")
    rw.print("  (gravity, dark energy) is the low-frequency envelope, not the carrier.")
    rw.print("")

    # ==================================================================
    # SECTION 8: The gap as interface between layers
    # ==================================================================
    rw.subsection("8. The Gap as Interface Between Layers (Air/Water/Oil Analogy)")
    rw.print("")
    rw.print("  LAYER ANALOGY:")
    rw.print("  Consider three fluids stacked: air / water / oil.")
    rw.print("  Each has a different wave speed (sound speed).")
    rw.print("  At each INTERFACE, waves partially reflect, partially transmit.")
    rw.print("  The interface itself supports SURFACE WAVES (gravity waves on water).")
    rw.print("")
    rw.print("  In PDTP, the two-phase Lagrangian has exactly this structure:")
    rw.print("    phi_b = bulk condensate (like the deep water layer)")
    rw.print("    phi_s = surface condensate (like the surface/interface layer)")
    rw.print("    psi   = matter (like an object floating at the interface)")
    rw.print("")
    rw.print("  The DIFFERENCE phi_- = (phi_b - phi_s)/2 IS the interface itself.")
    rw.print("  It measures how much the bulk and surface phases DISAGREE.")
    rw.print("  Where they agree (phi_- = 0): no interface effects (vacuum).")
    rw.print("  Where they disagree (phi_- = pi/2): maximal interface (near matter).")
    rw.print("")
    rw.print("  FREQUENCY INTERPRETATION OF THE INTERFACE:")
    rw.print("  In the fluid analogy, surface waves have DIFFERENT dispersion")
    rw.print("  than bulk waves:")
    rw.print("    Bulk (deep water):    omega^2 = g*k       (gravity waves)")
    rw.print("    Surface (capillary):  omega^2 = sigma*k^3/rho  (surface tension)")
    rw.print("    Transition at:        k* = sqrt(rho*g/sigma)")
    rw.print("")
    rw.print("  In PDTP:")
    rw.print("    phi_+ (bulk mode):    omega^2 = c^2*k^2 + omega_gap^2  (massive)")
    rw.print("    phi_- (surface mode): omega^2 = c^2*k^2 + m_-^2       (m_-=0 in vacuum)")
    rw.print("    The gap omega_gap IS the bulk mode's rest frequency.")
    rw.print("    The surface mode is GAPLESS in vacuum (propagates at all frequencies).")
    rw.print("")
    rw.print("  THREE LAYERS IN PDTP:")
    rw.print("    Layer 1: phi_b (bulk, +cos, attractive, gravity)")
    rw.print("    Layer 2: phi_s (surface, -cos, repulsive, tension)")
    rw.print("    Layer 3: psi (matter, coupled to both layers)")
    rw.print("")
    rw.print("  The GAP frequency omega_gap arises from the BULK layer's")
    rw.print("  phase stiffness. It's like the minimum frequency for a wave")
    rw.print("  to propagate through a medium (cutoff frequency in a waveguide).")
    rw.print("")
    rw.print("  Below the gap: evanescent waves (exponential decay, no propagation)")
    rw.print("  Above the gap: propagating waves")
    rw.print("  AT the gap: standing wave = REST MASS of the condensate excitation")
    rw.print("")

    # Numerical: interface properties
    xi = HBAR / (M_P * C * np.sqrt(2))  # healing length
    rw.print("  Interface thickness (healing length): xi = {:.4e} m".format(xi))
    rw.print("    = l_P / sqrt(2) = {:.4e} m".format(L_P / np.sqrt(2)))
    rw.print("  This is the Planck length -- the thinnest possible interface.")
    rw.print("")
    rw.print("  In the fluid analogy: the air-water interface is a few molecules thick.")
    rw.print("  In PDTP: the phi_b/phi_s interface is a few Planck lengths thick.")
    rw.print("  Particles (matter vortices) LIVE at this interface,")
    rw.print("  like floating objects live at the water surface.")
    rw.print("")
    rw.print("  THE GAP AS IMPEDANCE MISMATCH:")
    rw.print("  When a wave crosses from one medium to another (air->water),")
    rw.print("  the impedance mismatch causes reflection + frequency filtering.")
    rw.print("  In PDTP, the omega_gap is the impedance mismatch between")
    rw.print("  the condensate (phi) and matter (psi).")
    rw.print("  Frequencies below omega_gap cannot propagate through the condensate")
    rw.print("  -> this is WHY low-frequency modes (dark energy, cosmological)")
    rw.print("     are decoupled from high-frequency modes (particles, gravity).")
    rw.print("")
    rw.print("  The 10^122 ratio between Lambda and Planck IS the impedance mismatch")
    rw.print("  between the bulk and surface modes of the condensate.")
    rw.print("")

    # ==================================================================
    # SECTION 9: The harmonic structure (p1, p2, p3 reframe)
    # ==================================================================
    rw.subsection("9. Harmonic Structure -- What the Solver Was Really Searching")
    rw.print("")
    rw.print("  The solver's power-law sweep (Phase 2):")
    rw.print("    a = l_P * (m_e/m_P)^p1 * (m_p/m_P)^p2 * alpha^p3")
    rw.print("")
    rw.print("  Rewrite in frequencies (omega = m*c^2/hbar, a = hbar/(m*c)):")
    rw.print("    omega_gap = omega_P * (omega_e/omega_P)^p1 * (omega_p/omega_P)^p2 * alpha^p3")
    rw.print("")
    rw.print("  This is asking: is Planck frequency some POWER-LAW COMBINATION")
    rw.print("  of particle frequencies?")
    rw.print("")

    # Check specific cases
    rw.print("  Specific harmonic relationships:")
    rw.print("")

    omega_e = compton_freq(M_E)
    omega_p = compton_freq(M_P_PROTON)

    cases = [
        ("Trivial",       0,    0,    0,   "omega_gap = omega_P (circular)"),
        ("Electron only", -1,   0,    0,   "omega_gap = omega_P^2/omega_e"),
        ("Proton only",   0,    -1,   0,   "omega_gap = omega_P^2/omega_p"),
        ("Best solver",   -1,   1,    1.5, "omega_gap = omega_P * (omega_e/omega_P)^-1 * ..."),
        ("Geometric mean", 0.5, 0.5,  0,   "omega_gap = sqrt(omega_e*omega_p) * corrections"),
    ]

    for label, p1, p2, p3, desc in cases:
        # a = l_P * (m_e/m_P)^p1 * (m_p/m_P)^p2 * alpha^p3
        a = L_P * (M_E/M_P)**p1 * (M_P_PROTON/M_P)**p2 * ALPHA_EM**p3
        G_pred = C**3 * a**2 / HBAR
        omega_pred = C / a  # model M1
        ratio_G = G_pred / G
        rw.print("  {:20s} p=({:+.1f},{:+.1f},{:+.1f})".format(label, p1, p2, p3))
        rw.print("  {:20s} omega = {:.4e} rad/s, G/G_known = {:.4e}".format(
            "", omega_pred, ratio_G))
        rw.print("  {:20s} {}".format("", desc))
        rw.print("")

    rw.print("  RESULT: No power-law combination of particle frequencies gives G_known.")
    rw.print("  This is the ALGEBRAIC INEVITABILITY from Part 29:")
    rw.print("  1 equation (G = hbar*c/m_cond^2), 2 unknowns (G, m_cond).")
    rw.print("  The harmonic number n = m_P/m is HUGE and has no known derivation.")
    rw.print("")

    # ==================================================================
    # SECTION 10: The hierarchy as a musical interval
    # ==================================================================
    rw.subsection("10. The Hierarchy Problem as a Musical Interval")
    rw.print("")
    rw.print("  In music: octave = 2x frequency, fifth = 3/2x, etc.")
    rw.print("  In PDTP: the 'interval' from electron to Planck is:")
    rw.print("")

    n_e = M_P / M_E
    n_p = M_P / M_P_PROTON

    rw.print("  omega_P / omega_e = n_e = {:.6e}".format(n_e))
    rw.print("  = 2^{:.2f}  (number of 'octaves' from electron to Planck)".format(
        np.log2(n_e)))
    rw.print("  = {:.2f} decades".format(np.log10(n_e)))
    rw.print("")
    rw.print("  omega_P / omega_p = n_p = {:.6e}".format(n_p))
    rw.print("  = 2^{:.2f}  (number of 'octaves' from proton to Planck)".format(
        np.log2(n_p)))
    rw.print("  = {:.2f} decades".format(np.log10(n_p)))
    rw.print("")
    rw.print("  omega_P / H_0 = {:.6e}".format(OMEGA_P / H_0))
    rw.print("  = 2^{:.2f}  (number of 'octaves' from Hubble to Planck)".format(
        np.log2(OMEGA_P / H_0)))
    rw.print("  = {:.2f} decades".format(np.log10(OMEGA_P / H_0)))
    rw.print("")
    rw.print("  The hierarchy problem = 'why is this interval so large?'")
    rw.print("  In music, you'd ask: 'why is the instrument 74 octaves wide?'")
    rw.print("  In PDTP, we derived: n = m_cond/m (Part 33), but m_cond is free.")
    rw.print("")

    # ==================================================================
    # SECTION 11: Summary -- what the frequency picture reveals
    # ==================================================================
    rw.subsection("11. Summary -- What the Frequency Picture Reveals")
    rw.print("")
    rw.print("  GR: no frequency, smooth spacetime")
    rw.print("  QM: every particle has a frequency omega = mc^2/hbar")
    rw.print("  PDTP: spacetime IS a condensate with gap frequency omega_gap")
    rw.print("")
    rw.print("  KEY RELATIONSHIPS:")
    rw.print("  1. G = c^5 / (hbar * omega_gap^2)    -- gravity from frequency")
    rw.print("  2. n = omega_gap / omega_particle     -- winding = frequency ratio")
    rw.print("  3. alpha_G = (omega_particle/omega_gap)^2  -- gravity coupling = frequency ratio^2")
    rw.print("")
    rw.print("  WHAT THE LAGRANGIANS SAY:")
    rw.print("")
    rw.print("  Single-phase (+cos):")
    rw.print("    - ONE gap frequency (omega_gap = omega_P)")
    rw.print("    - Gravity comes from spatial phase gradients, not temporal oscillations")
    rw.print("    - omega_gap sets healing length, G, and breathing mode mass")
    rw.print("    - ALL particles phase-lock to the SAME condensate background")
    rw.print("    - Hierarchy = why omega_gap >> omega_particle (OPEN)")
    rw.print("")
    rw.print("  Two-phase (+cos/-cos):")
    rw.print("    - TWO gap frequencies: omega_+ (Planck) and omega_- (free/cosmological)")
    rw.print("    - phi_+ = gravity (high freq), phi_- = surface tension/dark energy (low freq)")
    rw.print("    - Newton's 3rd law uses phi_+ ONLY")
    rw.print("    - Cosmological constant ~ (omega_-/omega_+)^2 ~ 10^-122")
    rw.print("    - TWO hierarchy problems become ONE: omega_+ vs omega_- ratio")
    rw.print("")
    rw.print("  OPEN QUESTIONS (not resolved by frequency reframe):")
    rw.print("  1. WHY is omega_gap = omega_P? (= why is m_cond = m_P?)")
    rw.print("  2. Is Planck the FUNDAMENTAL or a harmonic? (underdetermined)")
    rw.print("  3. Does the two-phase phi_- mode really sit at H_0? (speculative)")
    rw.print("  4. Can any experiment distinguish 'Planck-fundamental' from 'Planck-harmonic'?")
    rw.print("")
    rw.print("  WHAT THIS REFRAME ACHIEVES:")
    rw.print("  - Unifies G, Lambda, hierarchy problem as FREQUENCY RATIOS")
    rw.print("  - Makes the two-phase Lagrangian more physical (two frequencies)")
    rw.print("  - Shows G ~ 1/omega^2 explicitly (inverse square in frequency space)")
    rw.print("  - Clarifies that gravity comes from SPATIAL gradients, not temporal frequency")
    rw.print("  - Does NOT solve the hierarchy problem (m_cond still free)")
    rw.print("")

    rw.close()


if __name__ == "__main__":
    main()
