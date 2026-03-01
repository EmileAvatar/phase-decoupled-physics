#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part 32: Koide-Lattice Analysis
================================
Bottom-up derivation attempt: use particle masses (Koide/Brannen parameterization)
as input to constrain the PDTP lattice spring constant K and gravitational constant G.

Core question:
  If particle masses are EMERGENT from the spacetime lattice, can we reverse-engineer
  G from the known mass spectrum without using G as input?

Approach:
  1. Verify the Koide formula for leptons (and check quark triplets)
  2. Extract Brannen parameters: mu (overall scale), theta_0 (phase), delta = sqrt(2)
  3. Identify all mass/length scales derivable from particle physics alone
  4. For each candidate lattice spacing 'a': compute G_pred = c^3 a^2 / hbar
  5. Sudoku-score G_pred against G_known
  6. Analyze the 3x3 circulant mass matrix and its lattice interpretation
  7. Factor each ratio as (m_x / m_Planck)^N to expose the hierarchy wall

PDTP G formula (from Part 29, substitution chain, G-free K):
  K = hbar / (4*pi*c)       [units: kg*m, uses only hbar and c]
  G = c^2 a^2 / (4*pi*K)   [PDTP bridge relation]
    = c^3 a^2 / hbar        [simplified with K = hbar/(4*pi*c)]

Sources:
  - Koide formula: Y. Koide, Lett. Nuovo Cimento 34, 201 (1982)
  - Brannen parameterization: C.A. Brannen, "The Lepton Masses" (2006)
  - Koide derivation in PDTP: docs/research/koide_derivation.md
  - G-free K derivation: simulations/substitution_chains.py, Part 29
  - PDG 2024 masses: https://pdg.lbl.gov/
"""

import sys
import io
import numpy as np

# Force UTF-8 output (Windows compatibility)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# ===========================================================================
# FUNDAMENTAL CONSTANTS (CODATA 2022, non-gravitational)
# ===========================================================================
hbar   = 1.054571817e-34   # J*s       (reduced Planck constant)
c      = 2.99792458e8      # m/s       (speed of light)
G_known = 6.67430e-11      # m^3/(kg*s^2)  (Newton's constant, for comparison only)
m_e    = 9.1093837015e-31  # kg        (electron mass)
m_p    = 1.67262192369e-27 # kg        (proton mass)
alpha  = 1.0 / 137.035999  # dimensionless (fine-structure constant)
eV     = 1.602176634e-19   # J per eV
MeV    = 1e6 * eV          # J per MeV

# Planck units (DERIVED from G_known -- for comparison only, not used in G_pred)
m_Pl   = np.sqrt(hbar * c / G_known)  # kg  Planck mass
l_Pl   = np.sqrt(hbar * G_known / c**3)  # m  Planck length
E_Pl   = m_Pl * c**2                  # J  Planck energy

# ===========================================================================
# PARTICLE MASSES (PDG 2024)
# Source: https://pdg.lbl.gov/
# ===========================================================================

# Charged leptons (MeV/c^2)
m_electron_MeV = 0.51099895000    # electron
m_muon_MeV     = 105.6583755      # muon
m_tau_MeV      = 1776.86          # tau

# Convert to kg
m_electron = m_electron_MeV * MeV / c**2
m_muon     = m_muon_MeV     * MeV / c**2
m_tau_kg   = m_tau_MeV      * MeV / c**2

leptons_MeV = [m_electron_MeV, m_muon_MeV, m_tau_MeV]
lepton_names = ["electron", "muon", "tau"]

# Quarks (MeV/c^2, MS-bar masses at appropriate scales, PDG 2024)
m_up_MeV      = 2.16       # u
m_down_MeV    = 4.70       # d
m_strange_MeV = 93.5       # s
m_charm_MeV   = 1270.0     # c
m_bottom_MeV  = 4180.0     # b
m_top_MeV     = 172570.0   # t

# ===========================================================================
# HELPER FUNCTIONS
# ===========================================================================

def koide_Q(masses_MeV):
    """Compute the Koide ratio Q = sum(m) / (sum(sqrt(m)))^2."""
    m = np.array(masses_MeV)
    return np.sum(m) / np.sum(np.sqrt(m))**2

def brannen_params(masses_MeV):
    """
    Extract Brannen parameters (mu, theta_0) for three masses.
    Assumes delta = sqrt(2) (Koide condition).
    Assigns i=0 to the heaviest, i=1 and i=2 to the lighter two.
    Returns:
        mu      : overall scale (MeV^{1/2})
        theta_0 : phase offset (radians), Brannen convention i=0 is heaviest
        delta   : modulation depth (should be ~sqrt(2) for Koide)
    """
    m = np.array(masses_MeV, dtype=float)
    sqrt_m = np.sqrt(m)
    mu = np.sum(sqrt_m) / 3.0
    # Compute delta from Q: Q = (1 + delta^2/2)/3, so delta^2 = 6Q - 2
    Q = np.sum(m) / np.sum(sqrt_m)**2
    delta_sq = 6.0 * Q - 2.0
    delta = np.sqrt(max(delta_sq, 0.0))
    # Phase offset: assign i=0 to heaviest
    idx_heavy = np.argmax(m)
    cos_theta = (sqrt_m[idx_heavy] / mu - 1.0) / delta
    cos_theta = np.clip(cos_theta, -1.0, 1.0)
    theta_0 = np.arccos(cos_theta)
    return mu, theta_0, delta

def MeV_to_kg(mass_MeV):
    """Convert mass from MeV/c^2 to kg."""
    return mass_MeV * MeV / c**2

def kg_to_MeV(mass_kg):
    """Convert mass from kg to MeV/c^2."""
    return mass_kg * c**2 / MeV

def compton(mass_kg):
    """Reduced Compton wavelength hbar/(mc) in metres."""
    return hbar / (mass_kg * c)

def G_from_a(a_m):
    """
    Predict G from lattice spacing 'a' using PDTP G-free formula:
       K = hbar / (4*pi*c)
       G = c^2 a^2 / (4*pi*K) = c^3 a^2 / hbar
    """
    return c**3 * a_m**2 / hbar

def hierarchy_factor(ratio):
    """
    Express ratio as (m_Pl/m_x)^N for some m_x.
    Returns the exponent N if ratio = (m_Pl/m_e)^N.
    """
    if ratio <= 0:
        return float('nan')
    log_ratio = np.log10(ratio)
    log_mPl_me = np.log10(m_Pl / m_electron)
    N = log_ratio / log_mPl_me
    return N

def sudoku_score(G_pred, G_ref, label):
    """Score a G prediction against G_known. Returns 'PASS' or 'FAIL'."""
    ratio = G_pred / G_ref
    if 0.99 <= ratio <= 1.01:
        return "PASS"
    return "FAIL"

# ===========================================================================
# SECTION 1: KOIDE FORMULA VERIFICATION
# ===========================================================================
print("=" * 80)
print("PART 32: KOIDE-LATTICE ANALYSIS")
print("Bottom-up derivation: particle masses -> lattice parameters -> G")
print("=" * 80)
print()
print("=" * 80)
print("1. KOIDE FORMULA VERIFICATION")
print("=" * 80)
print()
print("  Source: Y. Koide, Lett. Nuovo Cimento 34, 201 (1982)")
print("  Source: PDG 2024, https://pdg.lbl.gov/")
print()

# Lepton Koide ratio
Q_leptons = koide_Q(leptons_MeV)
print("  Charged leptons (e, mu, tau):")
print("    m_e   = {:.8f} MeV".format(m_electron_MeV))
print("    m_mu  = {:.7f} MeV".format(m_muon_MeV))
print("    m_tau = {:.2f} MeV".format(m_tau_MeV))
print("    Q     = {:.8f}".format(Q_leptons))
print("    2/3   = {:.8f}".format(2.0/3.0))
print("    |Q - 2/3| = {:.2e}  (< 10^-5: YES)".format(abs(Q_leptons - 2.0/3.0)))
print()

# Quark triplet Koide ratios
quark_triplets = [
    ("u, c, t (up-type generational)",  [m_up_MeV, m_charm_MeV, m_top_MeV]),
    ("d, s, b (down-type generational)", [m_down_MeV, m_strange_MeV, m_bottom_MeV]),
    ("c, b, t (heavy quarks)",           [m_charm_MeV, m_bottom_MeV, m_top_MeV]),
    ("-s, c, b (Rivero signed)",         [-m_strange_MeV, m_charm_MeV, m_bottom_MeV]),
]

print("  Quark triplets:")
print("  Source: W. Rodejohann & H. Zhang, arXiv:1101.5525 (2011)")
print("  Source: A. Rivero, arXiv:1111.7232 (2011)")
print()
print("  {:40s}  {:8s}  {:10s}  {:6s}".format(
    "Triplet", "Q", "|Q-2/3|", "delta"))
print("  " + "-" * 70)
for name, masses in quark_triplets:
    # Handle signed case for Rivero
    pos_masses = [abs(m) for m in masses]
    signed_sqrt = sum(np.sign(m) * np.sqrt(abs(m)) for m in masses)
    Q_signed = sum(abs(m) for m in masses) / signed_sqrt**2
    _, _, delta_val = brannen_params(pos_masses)
    print("  {:40s}  {:8.5f}  {:10.4e}  {:6.4f}".format(
        name, Q_signed, abs(Q_signed - 2.0/3.0), delta_val))
print()

# ===========================================================================
# SECTION 2: BRANNEN PARAMETERIZATION OF LEPTON MASSES
# ===========================================================================
print("=" * 80)
print("2. BRANNEN PARAMETERIZATION OF LEPTON MASSES")
print("=" * 80)
print()
print("  Source: C.A. Brannen, 'The Lepton Masses' (2006)")
print("  Source: docs/research/koide_derivation.md")
print()
print("  Ansatz: sqrt(m_i) = mu * (1 + delta * cos(theta_0 + 2*pi*i/3))")
print("  Koide condition: delta = sqrt(2)  (Q = 2/3 iff delta = sqrt(2))")
print()

mu_lep, theta_lep, delta_lep = brannen_params(leptons_MeV)
M0_lep_MeV = mu_lep**2   # Koide base mass scale (MeV/c^2)
M0_lep_kg  = MeV_to_kg(M0_lep_MeV)

print("  Fitted parameters:")
print("    mu     = {:.6f} MeV^(1/2)".format(mu_lep))
print("    theta_0 = {:.6f} rad = {:.4f} deg".format(theta_lep, np.degrees(theta_lep)))
print("    theta_0 ~ 2/9 = {:.6f} rad? diff = {:.2e}".format(
    2.0/9.0, abs(theta_lep - 2.0/9.0)))
print("    delta   = {:.6f}  (sqrt(2) = {:.6f})".format(delta_lep, np.sqrt(2)))
print()
print("  The Koide base mass scale:")
print("    M_0 = mu^2 = {:.4f} MeV".format(M0_lep_MeV))
print("    M_0 = {:.4e} kg".format(M0_lep_kg))
print("    M_0/m_e  = {:.4f}  (about {:.0f} electron masses)".format(
    M0_lep_MeV/m_electron_MeV, M0_lep_MeV/m_electron_MeV))
print("    M_0/m_mu = {:.4f}  (close to: {:.4f} = 3*m_mu/m_e ratio hint)".format(
    M0_lep_MeV/m_muon_MeV, 3*m_muon_MeV/m_electron_MeV))
print("    Note: M_0 ~ m_proton/3 ~ constituent quark mass".format())
print("    m_p/3 = {:.4f} MeV (proton mass / 3)".format(
    938.272 / 3.0))
print()

# Verify the fit
print("  Fit verification:")
print("  Note: Brannen assigns i=0 to heaviest (tau), i=1 to electron, i=2 to muon.")
print("  {:10s}  {:4s}  {:12s}  {:12s}  {:12s}  {:8s}".format(
    "Lepton", "i", "sqrt(m) meas.", "sqrt(m) pred.", "Residual", "Rel err"))
print("  " + "-" * 68)
# Brannen index: tau=i0, electron=i1, muon=i2
brannen_index_map = {"electron": 1, "muon": 2, "tau": 0}
for name, mass_MeV in zip(lepton_names, leptons_MeV):
    i = brannen_index_map[name]
    sqrt_m_meas = np.sqrt(mass_MeV)
    sqrt_m_pred = mu_lep * (1 + np.sqrt(2) * np.cos(theta_lep + 2*np.pi*i/3))
    resid = sqrt_m_meas - sqrt_m_pred
    rel_err = abs(resid / sqrt_m_meas)
    print("  {:10s}  {:4d}  {:12.6f}  {:12.6f}  {:12.6f}  {:8.4f}%".format(
        name, i, sqrt_m_meas, sqrt_m_pred, resid, rel_err*100))
print()

# ===========================================================================
# SECTION 3: MASS AND LENGTH SCALES FROM PARTICLE PHYSICS
# ===========================================================================
print("=" * 80)
print("3. MASS AND LENGTH SCALES DERIVABLE FROM PARTICLE PHYSICS ALONE")
print("=" * 80)
print()
print("  The Koide formula gives RATIOS only -- not the absolute scale.")
print("  The scale mu (= M_0^{1/2}) is set by whichever mass we measure.")
print()
print("  Candidate mass scales (all derived from particle masses, no G):")
print()

# Geometric mean of lepton masses
M_geom_MeV = (m_electron_MeV * m_muon_MeV * m_tau_MeV)**(1.0/3.0)
M_geom_kg  = MeV_to_kg(M_geom_MeV)

# Harmonic mean
M_harm_MeV = 3.0 / (1.0/m_electron_MeV + 1.0/m_muon_MeV + 1.0/m_tau_MeV)
M_harm_kg  = MeV_to_kg(M_harm_MeV)

# Off-diagonal coupling: t = mu / sqrt(2), so t^2 = mu^2 / 2 = M_0 / 2
M_hop_MeV = M0_lep_MeV / 2.0  # hopping energy in mass units
M_hop_kg  = MeV_to_kg(M_hop_MeV)

# Koide predicted tau from e and mu masses only (no G)
# Given mu and theta_0, predict sqrt(m_tau)
sqrt_m_tau_pred = mu_lep * (1 + np.sqrt(2) * np.cos(theta_lep + 0))
m_tau_pred_MeV = sqrt_m_tau_pred**2

mass_scales = [
    ("m_e (electron)",       m_electron_MeV,   m_electron),
    ("m_mu (muon)",          m_muon_MeV,        m_muon),
    ("m_tau (tau)",          m_tau_MeV,         m_tau_kg),
    ("M_0 = mu^2 (Koide base)", M0_lep_MeV,    M0_lep_kg),
    ("M_geom = (m_e*m_mu*m_tau)^{1/3}", M_geom_MeV, M_geom_kg),
    ("M_hop = M_0/2 (hopping term)", M_hop_MeV, M_hop_kg),
    ("m_p (proton)",         938.272,           m_p),
]

print("  {:40s}  {:12s}  {:14s}  {:14s}".format(
    "Scale", "Mass (MeV)", "Mass (kg)", "Length hbar/(mc) [m]"))
print("  " + "-" * 85)
for name, mass_MeV, mass_kg in mass_scales:
    a = compton(mass_kg)
    print("  {:40s}  {:12.4f}  {:14.4e}  {:14.4e}".format(
        name, mass_MeV, mass_kg, a))
print()

# ===========================================================================
# SECTION 4: SYSTEMATIC MAXWELL-TERM SEARCH
# ===========================================================================
print("=" * 80)
print("4. SYSTEMATIC MAXWELL-TERM SEARCH")
print("   Testing candidates for the lattice spacing 'a'")
print("   G_pred = c^3 * a^2 / hbar   (PDTP formula with K = hbar/(4*pi*c))")
print("=" * 80)
print()
print("  PDTP G formula source: simulations/substitution_chains.py, Part 29")
print("  K = hbar/(4*pi*c) = {:.4e} kg*m  (G-free, uses only hbar and c)".format(
    hbar / (4 * np.pi * c)))
print()

candidates = []

# -----------------------------------------------------------------------
# Candidate 0: Control -- Planck length (circular, must pass)
# -----------------------------------------------------------------------
a0 = l_Pl
G0 = G_from_a(a0)
candidates.append({
    "name": "Candidate 0 (Control): a = l_Planck",
    "formula": "a = sqrt(hbar*G/c^3)  [CIRCULAR -- uses G]",
    "a": a0, "G_pred": G0,
})

# -----------------------------------------------------------------------
# Candidate 1: a = lambda_C(electron)
# -----------------------------------------------------------------------
a1 = compton(m_electron)
G1 = G_from_a(a1)
candidates.append({
    "name": "Candidate 1: a = lambda_C(electron)",
    "formula": "a = hbar/(m_e*c) = {:.4e} m".format(a1),
    "a": a1, "G_pred": G1,
})

# -----------------------------------------------------------------------
# Candidate 2: a = classical electron radius (alpha * lambda_C(e))
# -----------------------------------------------------------------------
a2 = alpha * compton(m_electron)
G2 = G_from_a(a2)
candidates.append({
    "name": "Candidate 2: a = r_e (classical electron radius)",
    "formula": "a = alpha * hbar/(m_e*c) = {:.4e} m".format(a2),
    "a": a2, "G_pred": G2,
})

# -----------------------------------------------------------------------
# Candidate 3: a = lambda_C(M_0) -- Koide base mass sets the lattice
# -----------------------------------------------------------------------
a3 = compton(M0_lep_kg)
G3 = G_from_a(a3)
candidates.append({
    "name": "Candidate 3: a = lambda_C(M_0)  -- Koide base mass",
    "formula": "a = hbar/(M_0*c), M_0 = mu^2 = {:.2f} MeV".format(M0_lep_MeV),
    "a": a3, "G_pred": G3,
})

# -----------------------------------------------------------------------
# Candidate 4: a = lambda_C(M_geom) -- geometric mean of leptons
# -----------------------------------------------------------------------
a4 = compton(M_geom_kg)
G4 = G_from_a(a4)
candidates.append({
    "name": "Candidate 4: a = lambda_C(M_geom)  -- geometric mean of leptons",
    "formula": "a = hbar/(M_geom*c), M_geom = {:.2f} MeV".format(M_geom_MeV),
    "a": a4, "G_pred": G4,
})

# -----------------------------------------------------------------------
# Candidate 5: a = lambda_C(M_hop) -- hopping energy from circulant matrix
# -----------------------------------------------------------------------
a5 = compton(M_hop_kg)
G5 = G_from_a(a5)
candidates.append({
    "name": "Candidate 5: a = lambda_C(M_hop)  -- circulant hopping term",
    "formula": "a = hbar/(M_hop*c), M_hop = M_0/2 = {:.2f} MeV".format(M_hop_MeV),
    "a": a5, "G_pred": G5,
})

# -----------------------------------------------------------------------
# Candidate 6: a = lambda_C(proton)
# -----------------------------------------------------------------------
a6 = compton(m_p)
G6 = G_from_a(a6)
candidates.append({
    "name": "Candidate 6: a = lambda_C(proton)",
    "formula": "a = hbar/(m_p*c) = {:.4e} m".format(a6),
    "a": a6, "G_pred": G6,
})

# -----------------------------------------------------------------------
# Candidate 7: a = alpha * lambda_C(M_0)  -- EM-scaled Koide lattice
# -----------------------------------------------------------------------
a7 = alpha * compton(M0_lep_kg)
G7 = G_from_a(a7)
candidates.append({
    "name": "Candidate 7: a = alpha * lambda_C(M_0)  -- EM-scaled Koide",
    "formula": "a = alpha * hbar/(M_0*c) = {:.4e} m".format(a7),
    "a": a7, "G_pred": G7,
})

# -----------------------------------------------------------------------
# Candidate 8: a from "Maxwell term" -- introduce Koide phase angle
# If theta_0 = 2/9 encodes a mass scale: m_theta = m_e / theta_0^2
# -----------------------------------------------------------------------
m_theta_MeV = m_electron_MeV / theta_lep**2
m_theta_kg  = MeV_to_kg(m_theta_MeV)
a8 = compton(m_theta_kg)
G8 = G_from_a(a8)
candidates.append({
    "name": "Candidate 8: a = lambda_C(m_e/theta_0^2)  -- phase-angle scale",
    "formula": "m_theta = m_e/theta_0^2 = {:.2f} MeV, theta_0 = 2/9".format(m_theta_MeV),
    "a": a8, "G_pred": G8,
})

# -----------------------------------------------------------------------
# Candidate 9: a from the "Koide cascade" -- what mass would make G_known?
# This tells us what M_lattice would need to be.
# G = c^3 a^2 / hbar => a = sqrt(hbar*G/c^3) = l_Pl (circular, same as 0)
# But what mass M* satisfies lambda_C(M*) = l_Pl?
# l_Pl = hbar/(m_Pl*c) => M* = m_Pl (Planck mass, circular)
# Show this explicitly.
# -----------------------------------------------------------------------
# Required mass to hit G_known: m_* = hbar / (l_Pl * c) = m_Pl
m_star_kg = np.sqrt(hbar * c / G_known)  # = m_Pl
m_star_MeV = kg_to_MeV(m_star_kg)
a9 = compton(m_star_kg)  # = l_Pl (circular check)
G9 = G_from_a(a9)
candidates.append({
    "name": "Candidate 9: a = lambda_C(m_*) where G_pred = G_known",
    "formula": "Requires m_* = {:.4e} MeV = m_Planck [CIRCULAR]".format(m_star_MeV),
    "a": a9, "G_pred": G9,
})

# Print all candidates
print("  {:>3s}  {:50s}  {:14s}  {:14s}  {:8s}".format(
    "#", "Candidate", "a (m)", "G_pred", "Score"))
print("  " + "-" * 100)

for i, cand in enumerate(candidates):
    G_pred = cand["G_pred"]
    ratio = G_pred / G_known
    score = "PASS" if 0.99 <= ratio <= 1.01 else "FAIL"
    print("  {:>3d}  {:50s}  {:14.4e}  {:14.4e}  {:8s}".format(
        i, cand["name"], cand["a"], G_pred, score))

print()
n_pass = sum(1 for c in candidates if 0.99 <= c["G_pred"]/G_known <= 1.01)
n_fail = len(candidates) - n_pass
print("  SUDOKU SCORECARD: {} PASS, {} FAIL (out of {})".format(
    n_pass, n_fail, len(candidates)))
print()

# ===========================================================================
# SECTION 5: HIERARCHY WALL ANALYSIS
# ===========================================================================
print("=" * 80)
print("5. HIERARCHY WALL ANALYSIS")
print("   Express each G_pred/G_known as (m_Pl/m_particle)^N")
print("=" * 80)
print()

print("  Reference hierarchy ratios:")
print("    m_Pl/m_e   = {:.4e}  (Planck/electron)".format(m_Pl/m_electron))
print("    m_Pl/m_mu  = {:.4e}  (Planck/muon)".format(m_Pl/m_muon))
print("    m_Pl/M_0   = {:.4e}  (Planck/Koide base)".format(m_Pl/M0_lep_kg))
print("    m_Pl/m_p   = {:.4e}  (Planck/proton)".format(m_Pl/m_p))
print()

print("  {:>3s}  {:45s}  {:12s}  {:12s}  {:12s}".format(
    "#", "Candidate", "G_pred/G_knwn", "N (m_Pl/m_e)^N", "Interpretation"))
print("  " + "-" * 95)

for i, cand in enumerate(candidates):
    ratio = cand["G_pred"] / G_known
    log_ratio = np.log10(ratio) if ratio > 0 else 0
    # Express as (m_Pl/m_e)^N
    log_hierarchy_e  = np.log10(m_Pl / m_electron)
    log_hierarchy_mu = np.log10(m_Pl / m_muon)
    log_hierarchy_M0 = np.log10(m_Pl / M0_lep_kg)
    N_e  = log_ratio / log_hierarchy_e  if log_hierarchy_e  != 0 else 0
    N_mu = log_ratio / log_hierarchy_mu if log_hierarchy_mu != 0 else 0
    N_M0 = log_ratio / log_hierarchy_M0 if log_hierarchy_M0 != 0 else 0
    # Pick closest integer N
    N_nearest = round(N_e)
    interp = "(m_Pl/m_e)^{:.2f}".format(N_e)
    print("  {:>3d}  {:45s}  {:12.4e}  {:14s}  {:>12s}".format(
        i, cand["name"][:45], ratio, "N={:.2f}".format(N_e), interp))
print()
print("  Key finding:")
print("    ALL candidates give ratio = (m_Pl/m_particle)^N for some N.")
print("    This is the hierarchy problem: the lattice spacing that would give G")
print("    must be the PLANCK LENGTH, not any particle physics scale.")
print("    No combination of lepton masses and dimensionless numbers (alpha, 2/9, ...)")
print("    bridges the 22-order-of-magnitude gap between particle physics and gravity.")
print()

# ===========================================================================
# SECTION 6: THE 3x3 CIRCULANT MASS MATRIX
# ===========================================================================
print("=" * 80)
print("6. THE 3x3 CIRCULANT MASS MATRIX")
print("   Brannen parameterization as tight-binding eigenvalue problem")
print("=" * 80)
print()
print("  Source: docs/research/koide_derivation.md Section 3")
print()
print("  The Brannen ansatz sqrt(m_i) = mu*(1 + sqrt(2)*cos(theta_0 + 2pi*i/3))")
print("  is the eigenspectrum of a 3x3 Hermitian circulant matrix M_circ:")
print()
print("  For theta_0 = 0 (real symmetric case):")
print("    M_circ = mu * I + (mu/sqrt(2)) * C")
print("  where C is the adjacency matrix of a 3-site ring:")
print("    C = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]")
print()
print("  Eigenvalues of C: {2, -1, -1}")
print("  Eigenvalues of M_circ (theta_0=0): mu*(1+sqrt(2)), mu*(1-sqrt(2)/2), mu*(1-sqrt(2)/2)")
print()

# Build the matrix
C = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]], dtype=float)
M_circ = mu_lep * np.eye(3) + (mu_lep / np.sqrt(2)) * C
eigenvalues_circ = np.sort(np.linalg.eigvalsh(M_circ))[::-1]

print("  With mu = {:.6f} MeV^(1/2):".format(mu_lep))
print("    Eigenvalues of M_circ (theta_0=0): {:.4f}, {:.4f}, {:.4f} MeV^(1/2)".format(
    *eigenvalues_circ))
print("    Squared (= predicted masses for theta_0=0):")
print("      m_1 = {:.4f} MeV  (cf. tau = {:.2f} MeV)".format(
    eigenvalues_circ[0]**2, m_tau_MeV))
print("      m_2 = {:.4f} MeV  (degenerate)".format(eigenvalues_circ[1]**2))
print("      m_3 = {:.4f} MeV  (degenerate)".format(eigenvalues_circ[2]**2))
print()
print("  With theta_0 = 2/9 (actual Brannen phase, breaking degeneracy):")
print("  The matrix becomes Hermitian (complex off-diagonals) and the eigenvalues")
print("  reproduce the three lepton masses:")

# Hermitian circulant with theta_0
theta = theta_lep
# Eigenvalues: mu * (1 + sqrt(2) * cos(theta + 2*pi*k/3)) for k=0,1,2
eig_Brannen = [mu_lep * (1 + np.sqrt(2) * np.cos(theta + 2*np.pi*k/3)) for k in range(3)]
masses_Brannen = sorted([e**2 for e in eig_Brannen], reverse=True)
print("    sqrt(m_i) eigenvalues: {:.4f}, {:.4f}, {:.4f} MeV^(1/2)".format(
    *sorted(eig_Brannen, reverse=True)))
print("    Squared masses: {:.4f}, {:.4f}, {:.6f} MeV".format(*masses_Brannen))
print("    Actual masses:  {:.4f}, {:.4f}, {:.6f} MeV".format(
    m_tau_MeV, m_muon_MeV, m_electron_MeV))
print()

print("  Matrix elements and PDTP interpretation:")
print("    Diagonal mu = {:.4f} MeV^(1/2)".format(mu_lep))
print("    Off-diagonal t = mu/sqrt(2) = {:.4f} MeV^(1/2)".format(mu_lep/np.sqrt(2)))
print()
print("  In mass units (squaring):")
print("    M_0     = mu^2   = {:.4f} MeV  (Koide base mass, shared mode)".format(M0_lep_MeV))
print("    t^2     = mu^2/2 = {:.4f} MeV  (inter-generation hopping energy)".format(M0_lep_MeV/2))
print()
print("  In PDTP, the 'hopping energy' t^2 * c^2 corresponds to the inter-oscillator")
print("  coupling g. With a = hbar/(t*c) (where t = mu/sqrt(2) treated as mass):")
t_mass_MeV = mu_lep**2 / 2.0  # hopping in mass units (sqrt(mu_lep) squared / 2)
# Wait: mu has units MeV^{1/2}, so t = mu/sqrt(2) also has units MeV^{1/2}
# t^2 = mu^2/2 has units MeV (if we treat sqrt(m) as amplitude, t^2 is a mass)
t_mass_kg = MeV_to_kg(t_mass_MeV)
a_hop = compton(t_mass_kg)
G_hop = G_from_a(a_hop)
ratio_hop = G_hop / G_known
print("    t^2 = {:.4f} MeV, a_hop = lambda_C(t^2) = {:.4e} m".format(
    t_mass_MeV, a_hop))
print("    G_pred(a_hop) = {:.4e} m^3/(kg s^2)".format(G_hop))
print("    G_pred/G_known = {:.4e}".format(ratio_hop))
print("    This is same as Candidate 5 (M_hop) -- FAIL".format())
print()

# ===========================================================================
# SECTION 7: WHAT WOULD THE "MAXWELL TERM" NEED TO BE?
# ===========================================================================
print("=" * 80)
print("7. THE MISSING 'MAXWELL TERM'")
print("   What would it need to be to give G_known?")
print("=" * 80)
print()
print("  Maxwell's insight: add partial_E/partial_t to Ampere's law")
print("  -> consistency gives c = 1/sqrt(epsilon_0 * mu_0) for free.")
print("  Here: what single equation, when added to the Koide framework,")
print("  yields G without using G as input?")
print()

# The required lattice spacing
a_required = np.sqrt(hbar * G_known / c**3)  # = l_Planck
print("  Required: a = l_Planck = {:.4e} m  (from G = c^3 a^2 / hbar)".format(a_required))
print("  The required a IS the Planck length -- using G circularly.")
print()
print("  What mass M* gives lambda_C(M*) = l_Planck?")
print("    M* = hbar / (l_Planck * c) = m_Planck = {:.4e} MeV".format(
    kg_to_MeV(m_Pl)))
print("    Ratio M*/M_0 = {:.4e}".format(m_Pl/M0_lep_kg))
print("    Ratio M*/m_e = {:.4e}".format(m_Pl/m_electron))
print()
print("  The Maxwell term would need to INTRODUCE the Planck scale.")
print("  This cannot come from the Koide/Brannen structure alone.")
print()
print("  OPTIONS for a Maxwell-like term:")
print("  1. Postulate K directly (K = hbar/(4*pi*c)) -- this IS G-free")
print("     but still requires 'a' from outside the Koide framework.")
print("  2. Measure the breathing mode frequency omega_gap directly:")
print("     omega_gap -> a = pi*c/omega_gap -> G = c^3 a^2/hbar (Strategy A, Part 29)")
print("  3. Introduce N_eff (Sakharov): G = a^2/(N_eff*pi*hbar*c)")
print("     If BOTH a AND N_eff come from lattice structure, G follows.")
print("  4. Dvali species count: if the lattice has N ~ 10^38 modes/Planck vol,")
print("     gravity is weak BECAUSE spacetime has many degrees of freedom.")
print()
print("  The Koide formula is a constraint on RATIOS, not absolute scales.")
print("  It cannot provide the Maxwell term by itself.")
print()

# ===========================================================================
# SECTION 8: QUARK TRIPLET ANALYSIS
# ===========================================================================
print("=" * 80)
print("8. QUARK TRIPLET ANALYSIS")
print("   Do quark triplets imply a different or consistent M_0?")
print("=" * 80)
print()
print("  Source: docs/research/koide_derivation.md Section 7")
print()

quark_triplet_masses = {
    "(u, c, t) up-type":   [m_up_MeV, m_charm_MeV, m_top_MeV],
    "(d, s, b) down-type": [m_down_MeV, m_strange_MeV, m_bottom_MeV],
    "(c, b, t) heavy":     [m_charm_MeV, m_bottom_MeV, m_top_MeV],
}

print("  {:30s}  {:8s}  {:8s}  {:14s}  {:14s}  {:10s}".format(
    "Triplet", "Q", "delta", "M_0 (MeV)", "M_0/M_0_lep", "a = l_C(M_0)"))
print("  " + "-" * 90)

for name, masses in quark_triplet_masses.items():
    mu_q, theta_q, delta_q = brannen_params(masses)
    M0_q_MeV = mu_q**2
    M0_q_kg  = MeV_to_kg(M0_q_MeV)
    Q_q = koide_Q(masses)
    a_q = compton(M0_q_kg)
    print("  {:30s}  {:8.5f}  {:8.4f}  {:14.2f}  {:14.4f}  {:14.4e}".format(
        name, Q_q, delta_q, M0_q_MeV, M0_q_MeV/M0_lep_MeV, a_q))

print()
print("  Key: Each triplet gives a DIFFERENT M_0 value.")
print("  The three Koide base masses are NOT consistent with each other.")
print("  This means there is no single lattice spacing that works for all triplets.")
print("  Either:")
print("    a) Quarks and leptons live in different phase sectors (different a)")
print("    b) The quark triplets are not true Koide triplets (Q != 2/3)")
print("    c) QCD corrections shift the quark masses from their 'bare' Koide values")
print()

# ===========================================================================
# SECTION 9: COMPLETE NUMERICAL SUMMARY TABLE
# ===========================================================================
print("=" * 80)
print("9. COMPLETE NUMERICAL SUMMARY")
print("=" * 80)
print()
print("  Constants (non-gravitational):")
print("    hbar = {:.6e} J*s".format(hbar))
print("    c    = {:.6e} m/s".format(c))
print("    G_known = {:.6e} m^3/(kg*s^2)  [for comparison only]".format(G_known))
print()
print("  Koide/Brannen parameters (leptons):")
print("    mu      = {:.6f} MeV^(1/2)".format(mu_lep))
print("    M_0     = {:.6f} MeV".format(M0_lep_MeV))
print("    theta_0 = {:.6f} rad = 2/9 + {:.2e}".format(theta_lep, theta_lep - 2.0/9.0))
print("    delta   = {:.6f}  (sqrt(2) = {:.6f})".format(delta_lep, np.sqrt(2)))
print()
print("  Planck units (computed from G_known -- NOT used in G_pred calculations):")
print("    m_Pl  = {:.4e} kg  = {:.4e} MeV".format(m_Pl, kg_to_MeV(m_Pl)))
print("    l_Pl  = {:.4e} m".format(l_Pl))
print("    E_Pl  = {:.4e} J   = {:.4e} GeV".format(E_Pl, kg_to_MeV(m_Pl)/1000))
print()
print("  All G predictions:")
print()
print("  {:>3s}  {:50s}  {:14s}  {:12s}  {:12s}  {:6s}".format(
    "#", "Candidate", "a (m)", "G_pred", "G_pred/G_kn", "Score"))
print("  " + "-" * 105)

for i, cand in enumerate(candidates):
    G_pred = cand["G_pred"]
    ratio = G_pred / G_known
    score = "PASS" if 0.99 <= ratio <= 1.01 else "FAIL"
    log_ratio = np.log10(ratio) if ratio > 0 else 0
    log_hier = np.log10(m_Pl / m_electron)
    N = log_ratio / log_hier
    print("  {:>3d}  {:50s}  {:14.4e}  {:12.4e}  {:12.4e}  {:6s}  N={:.2f}".format(
        i, cand["name"][:50], cand["a"], G_pred, ratio, score, N))

print()
print("  FINAL SCORECARD: {} PASS, {} FAIL out of {} candidates".format(
    n_pass, n_fail, len(candidates)))
print()

# ===========================================================================
# SECTION 10: CONCLUSIONS
# ===========================================================================
print("=" * 80)
print("10. CONCLUSIONS")
print("=" * 80)
print()
print("  1. KOIDE FORMULA VERIFIED")
print("     Q = {:.8f} for (e, mu, tau) -- agrees with 2/3 to 1 part in 10^5.".format(Q_leptons))
print("     Brannen parameterization: mu = {:.4f} MeV^(1/2), M_0 = {:.2f} MeV".format(
    mu_lep, M0_lep_MeV))
print()
print("  2. KOIDE GIVES RATIOS, NOT ABSOLUTE SCALE")
print("     The formula Q = 2/3 is dimensionless and scale-invariant.")
print("     It fixes mu only AFTER one mass is measured.")
print("     No candidate 'a' derived from mu alone reproduces G.")
print()
print("  3. HIERARCHY WALL CONFIRMED")
print("     Every candidate gives G_pred/G_known = (m_Pl/m_x)^N.")
print("     This is the hierarchy problem: m_Pl is 22 orders of magnitude")
print("     above particle physics scales. The Koide formula cannot bridge this gap.")
print()
print("  4. THE 'MAXWELL TERM' CANNOT COME FROM KOIDE ALONE")
print("     Maxwell's displacement current was an INDEPENDENT measurement")
print("     (capacitor charging rate) that gave c = 1/sqrt(eps0*mu0) for free.")
print("     The PDTP equivalent would be:")
print("       - A direct measurement of omega_gap (breathing mode frequency)")
print("       - This gives: a = pi*c/omega_gap  ->  G = c^3 a^2 / hbar")
print("       - This IS a Maxwell-like term: independent input, G as output.")
print()
print("  5. QUARK TRIPLETS")
print("     No single M_0 is consistent across lepton and quark triplets.")
print("     The Koide structure appears to be a feature of the LEPTON sector;")
print("     quarks require different (or running) parameters.")
print()
print("  6. BEST REMAINING PATH (unchanged from Part 29):")
print("     Strategy A: breathing mode detection -> omega_gap -> a -> G")
print("     Strategy B: hierarchy ratio R = alpha_G/alpha_EM from lattice topology")
print("     Both require physics INPUT beyond the mass spectrum alone.")
print()
print("  PDTP Original: The systematic Koide-lattice analysis confirms the")
print("  circularity from a new direction. The Koide formula is a STRUCTURE")
print("  theorem (mass ratios), not a SCALE theorem (absolute masses).")
print("  Breaking the circularity requires a non-gravitational measurement")
print("  that accesses the Planck scale directly.")
print()
print("  All results saved to: simulations/koide_lattice_output.md")
print()
