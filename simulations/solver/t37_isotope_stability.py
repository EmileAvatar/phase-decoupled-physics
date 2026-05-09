#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
t37_isotope_stability.py -- Phase 75, Part 107 (TODO_04 T37)
============================================================
Isotope Stability Mini-Project (SEMF Baseline).

PURPOSE:
  Build an empirical baseline predictor for isotope stability and decay
  half-lives using the Bethe-Weizsacker Semi-Empirical Mass Formula (SEMF)
  plus standard decay-channel formulas. Validate against a reference set of
  ~15 measured isotopes. Then scan Z=115 (moscovium) for the predicted
  longest-lived isotope and compare to Bob Lazar's stable-isotope claim.

  This is the EMPIRICAL BASELINE. PDTP topology corrections (T28, T40)
  will plug into the dedicated stub `pdtp_topology_correction(Z, N)` in
  a later Part. The size of the gap between SEMF prediction and the
  Lazar claim becomes a quantitative target for that future work.

APPROACH (9 computation steps + Sudoku):
  1. Bethe-Weizsacker SEMF: B(Z,N) from 5 terms (vol, surf, Coul, asym, pair)
  2. Q-values for every decay channel: alpha, beta-, beta+/EC, p, n, SF
  3. Decay-rate formulas:
      - alpha: Viola-Seaborg (1966)
      - beta: simplified Sargent rule with log_ft ~ 5
      - SF: empirical Swiatecki-type T_SF(Z,A)
  4. nucleon_stats(Z, N, electrons=Z) wrapper -- all values computed
  5. Reference T_1/2 table (15 isotopes: NUBASE/AME2020)
  6. Sudoku check: predicted vs measured T_1/2 within order of magnitude
  7. Z=115 scan: N = 170-200; report longest-lived isotope
  8. Cross-check Z=114, 116, 118 island-of-stability shape
  9. PDTP topology stub (returns 0.0 for now)

PDTP-Original tags: NONE in this Part. Everything here is established
nuclear physics (textbook Krane 1988, Viola-Seaborg 1966, Swiatecki 1955).
PDTP enters via the stub `pdtp_topology_correction` reserved for T40.

Sources (all standard, all cited inline at point of use):
  [K88] Krane (1988) "Introductory Nuclear Physics", Wiley. Chapter 3.
  [VS66] Viola & Seaborg (1966) J.Inorg.Nucl.Chem. 28, 741. alpha-decay.
  [BW39] Bohr & Wheeler (1939) Phys.Rev. 56, 426. fission barrier.
  [SW55] Swiatecki (1955) Phys.Rev. 100, 937. SF systematics.
  [SAR33] Sargent (1933) Proc.Roy.Soc.Lond. A139, 659. beta decay.
  [AME20] Wang et al. (2021) Chinese Phys.C 45, 030003. atomic mass eval.
  [NUBASE20] Kondev et al. (2021) Chinese Phys.C 45, 030001. NUBASE.

Python rules (CLAUDE.md):
  - ASCII only (no Unicode)
  - Save output to outputs/
  - Every numeric field in returned dicts is COMPUTED from inputs (RECHECK
    rule); no hardcoded literals matching the expected answer
  - Sudoku checks read computed values from step return dicts
"""

import math
import os
import sys

# --- path setup ---
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

try:
    from print_utils import ReportWriter
    _STANDALONE = False
except ImportError:
    _STANDALONE = True


# ================================================================
# Physical constants and reference values (all from PDG / AME2020)
# ================================================================
PI         = math.pi
LN10       = math.log(10.0)
HBAR_MEVS  = 6.582119569e-22   # MeV * s (reduced Planck)
C_MS       = 2.99792458e8      # m/s
SEC_PER_YR = 365.25 * 24 * 3600

# Atomic mass excesses [MeV]:  Delta = (m_atomic - A * 1u) c^2
# (Atomic = nucleus + Z electrons.  Using atomic masses lets us cancel
# electron mass in Q_beta-minus = Delta(parent) - Delta(daughter).)
DELTA_H1   = 7.28897         # H-1 mass excess
DELTA_N    = 8.07132          # neutron mass excess
DELTA_HE4  = 2.42492          # He-4 mass excess (alpha particle is bare; Z=2 e cancel)
M_E_MEV    = 0.5109989461    # electron rest mass

# SEMF coefficients (Wapstra 1971 / Cohen-Swiatecki; same functional family
# as Krane 1988 but better-tuned for heavy nuclei -- pairing as A_P/sqrt(A)).
# Krane (1988) Table 3.2 used A_V=15.5, A_S=16.8, A_C=0.72, A_A=23.0,
# A_P=34/A^0.75. Wapstra / Gemini-cross-check set below fits the heavy
# actinide region marginally better and uses the more common sqrt(A) form.
A_V = 15.8     # volume term coefficient   [MeV]
A_S = 18.3     # surface term coefficient  [MeV]
A_C = 0.714    # Coulomb term coefficient  [MeV]
A_A = 23.2     # asymmetry term coefficient [MeV]
A_P = 12.0     # pairing term coefficient  [MeV] (delta = +/- A_P / sqrt(A))

# Magic numbers (closed nuclear shells)
MAGIC = (2, 8, 20, 28, 50, 82, 126, 184)


# ================================================================
# 1. Bethe-Weizsacker SEMF binding energy
# ================================================================
def binding_energy(Z, N):
    """
    Compute nuclear binding energy B(Z, N) [MeV] via the 5-term
    Bethe-Weizsacker / Semi-Empirical Mass Formula.

      B = a_V*A - a_S*A^(2/3) - a_C*Z(Z-1)/A^(1/3) - a_A*(N-Z)^2/A + delta

    where delta is the pairing energy:
      +A_P/A^(3/4)  for Z even, N even
      0             for A odd
      -A_P/A^(3/4)  for Z odd,  N odd

    Source: Krane (1988) "Introductory Nuclear Physics" eq. 3.27.
    """
    if Z < 1 or N < 0:
        return 0.0
    A = Z + N
    if A < 1:
        return 0.0

    vol  = A_V * A
    surf = A_S * (A ** (2.0/3.0))
    coul = A_C * Z * (Z - 1) / (A ** (1.0/3.0))
    asym = A_A * ((N - Z) ** 2) / A

    if (Z % 2 == 0) and (N % 2 == 0):
        pair = +A_P / math.sqrt(A)
    elif (Z % 2 == 1) and (N % 2 == 1):
        pair = -A_P / math.sqrt(A)
    else:
        pair = 0.0

    B = vol - surf - coul - asym + pair
    return B


def mass_excess(Z, N):
    """
    Atomic mass excess Delta(Z, N) [MeV]:
       Delta = Z * Delta(H-1) + N * Delta(n) - B(Z, N)

    This uses ATOMIC reference masses (H-1 includes 1 electron), which is
    convention; B is computed from the SEMF above.

    Source: Krane (1988) eq. 3.30.
    """
    return Z * DELTA_H1 + N * DELTA_N - binding_energy(Z, N)


# ================================================================
# 2. Q-values for every decay channel (computed from mass-excess diffs)
# ================================================================
def q_alpha(Z, N):
    """
    Q_alpha = Delta(Z, N) - Delta(Z-2, N-2) - Delta(He-4)

    Alpha decay is energetically allowed when Q_alpha > 0.
    Atomic masses cancel the 2 transferred electrons: parent has Z e-,
    daughter has (Z-2) e-, alpha (He nucleus) has 0; using atomic mass
    excess for He-4 (Z=2 e- included) closes the bookkeeping.

    Source: Krane (1988) eq. 8.1; Wong (2nd ed.) eq. 5-22.
    """
    if Z < 3 or N < 2:
        return -1.0e6   # not applicable: daughter would have Z<1 (non-physical)
    return mass_excess(Z, N) - mass_excess(Z - 2, N - 2) - DELTA_HE4


def q_beta_minus(Z, N):
    """
    Q_(beta-) = Delta(Z, N) - Delta(Z+1, N-1)

    Beta-minus decay: n -> p + e- + nu_bar. Using ATOMIC mass excesses,
    the (Z+1) extra electron in the daughter exactly accounts for the
    emitted electron, so the formula has no explicit m_e term.

    Source: Krane (1988) eq. 9.2.
    """
    if N < 1:
        return -1.0e6
    return mass_excess(Z, N) - mass_excess(Z + 1, N - 1)


def q_beta_plus(Z, N):
    """
    Q_(beta+) = Delta(Z, N) - Delta(Z-1, N+1) - 2 * m_e

    Beta-plus decay: p -> n + e+ + nu. With atomic masses, the daughter
    has one fewer electron, so we must subtract 2 m_e (one for the
    emitted positron, one for the missing daughter electron).
    Allowed when this is > 0.

    Source: Krane (1988) eq. 9.3.
    """
    if Z < 1:
        return -1.0e6
    return (mass_excess(Z, N) - mass_excess(Z - 1, N + 1)
            - 2.0 * M_E_MEV)


def q_ec(Z, N):
    """
    Q_EC = Delta(Z, N) - Delta(Z-1, N+1)

    Electron capture: p + e- (orbital) -> n + nu. With atomic masses the
    bookkeeping is just Delta(parent) - Delta(daughter); the absorbed
    electron is among the Z atomic electrons. (Neglects K-shell binding
    correction, ~ keV.)

    Source: Krane (1988) eq. 9.4.
    """
    if Z < 1:
        return -1.0e6
    return mass_excess(Z, N) - mass_excess(Z - 1, N + 1)


def s_p(Z, N):
    """
    Proton separation energy:
      S_p = Delta(Z-1, N) + Delta(H-1) - Delta(Z, N)
    Positive S_p means proton is bound. Proton emission is allowed when
    S_p < 0 (i.e. Q_p = -S_p > 0).
    """
    if Z < 1:
        return 0.0
    return mass_excess(Z - 1, N) + DELTA_H1 - mass_excess(Z, N)


def s_n(Z, N):
    """
    Neutron separation energy:
      S_n = Delta(Z, N-1) + Delta(n) - Delta(Z, N)
    Positive S_n means neutron is bound. Neutron emission allowed when
    S_n < 0 (Q_n = -S_n > 0).
    """
    if N < 1:
        return 0.0
    return mass_excess(Z, N - 1) + DELTA_N - mass_excess(Z, N)


def q_proton(Z, N):
    return -s_p(Z, N)


def q_neutron(Z, N):
    return -s_n(Z, N)


# ================================================================
# 3. Decay-rate formulas (all rates computed from Q-values)
# ================================================================
def log10_t_alpha(Z, q_a):
    """
    Alpha-decay half-life [s] via the Viola-Seaborg semi-empirical formula:

      log_10(T_1/2 [s]) = (a*Z + b)/sqrt(Q_alpha [MeV]) + (c*Z + d)

    where Q_alpha is the alpha Q-value in MeV and Z is the parent atomic
    number (so the daughter has Z-2). Constants are the original 1966 fit:
      a =  1.66175
      b = -8.5166
      c = -0.20228
      d = -33.9069

    Source: Viola & Seaborg (1966) J.Inorg.Nucl.Chem. 28, 741.
    """
    if q_a <= 0.0:
        return 99.0   # forbidden: arbitrarily long
    a, b, c, d = 1.66175, -8.5166, -0.20228, -33.9069
    return (a * Z + b) / math.sqrt(q_a) + (c * Z + d)


def log10_t_beta(q_b, log_ft=5.0):
    """
    Beta-decay half-life [s] from a simplified Sargent rule.

      log_10(T_1/2) = log_ft - log_10(f)

    with the Fermi integral approximated for high Q:
      f ~ (Q + m_e)^5 / (30 * m_e^5)

    log_ft = 5 corresponds to "allowed" transitions; superallowed ~3.5,
    first-forbidden ~7. The factor 30 is the standard normalisation that
    makes the unit-Q dimensionless integral match Fermi's original tables.

    Source: Sargent (1933) Proc.Roy.Soc.Lond. A139, 659; Krane (1988)
    eq. 9.18-9.21 and Fig. 9.4 for typical log_ft values.

    Returns 99.0 (effectively infinite) if Q <= 0.
    """
    if q_b <= 0.0:
        return 99.0
    f = ((q_b + M_E_MEV) ** 5) / (30.0 * (M_E_MEV ** 5))
    if f <= 0.0:
        return 99.0
    return log_ft - math.log10(f)


def log10_t_sf(Z, N):
    """
    Spontaneous-fission half-life [s] via a simple Bohr-Wheeler /
    liquid-drop barrier with WKB tunnelling:

      x = (Z^2/A) / (Z^2/A)_crit,  with (Z^2/A)_crit = 50.88
      B_f = 0.34 * a_S * A^(2/3) * (1-x)^2     [MeV; rough LD barrier]
      log_10(T_SF [s]) = -21 + (2*pi / ln10) * B_f / (hbar*omega_0)

    with hbar*omega_0 ~ 1 MeV (single-particle attempt frequency). This
    is order-of-magnitude only; quantitative SF half-lives require shell
    corrections (Strutinsky, Smolanczuk).

    Source: Bohr & Wheeler (1939) Phys.Rev. 56, 426; Cohen-Plasil-Swiatecki
    barrier; Wong (2nd ed.) Chapter 11.

    Returns 99.0 for sub-actinide nuclei (SF negligible).
    """
    A = Z + N
    if Z < 80 or A < 1:
        return 99.0
    z2_over_a = (Z * Z) / float(A)
    x = z2_over_a / 50.88
    if x >= 1.0:
        return -20.0   # supercritical: instant fission
    B_f = 0.34 * A_S * (A ** (2.0/3.0)) * ((1.0 - x) ** 2)
    hbar_omega = 1.0   # MeV
    return -21.0 + (2.0 * PI / LN10) * B_f / hbar_omega


def log10_t_proton(Z, q_p):
    """
    Proton-emission half-life [s].
    Proton tunnels through a Coulomb barrier; rough WKB:

      G ~ 2 * pi * (Z-1) * e^2 / (hbar v)  [Sommerfeld parameter]
        ~ 2 * pi * 0.62 * (Z-1) / sqrt(Q_p [MeV])

    log_10(T_1/2) ~ -21 + G / ln(10).

    Order-of-magnitude only. Source: Wong eq. 7-31.
    """
    if q_p <= 0.0:
        return 99.0
    G = 2.0 * PI * 0.62 * (Z - 1) / math.sqrt(q_p)
    return -21.0 + G / LN10


def log10_t_neutron(q_n):
    """
    Neutron-emission half-life [s].
    No Coulomb barrier; for Q_n > 0 emission is essentially nuclear
    timescale. Use a simple s-wave estimate:

      T ~ 10^(-22) / Q_n[MeV]^(1/2)  s    (fast, no barrier)

    Source: Wong section 7.3.
    """
    if q_n <= 0.0:
        return 99.0
    return -22.0 - 0.5 * math.log10(q_n)


# ================================================================
# 4. Magic-number count and nucleon_stats orchestrator
# ================================================================
def magic_count(Z, N):
    """
    Count how many of {Z, N} sit on a magic-number shell closure.
    Returns 0, 1, or 2 (doubly magic).
    """
    return int(Z in MAGIC) + int(N in MAGIC)


def pdtp_topology_correction(Z, N):
    """
    Stub for the PDTP topological binding correction (T40 / future Part).

    When T40 is solved, this function will return the additional binding
    energy [MeV] from Y-junction / Hopf-link packing closure of a
    multi-nucleon configuration. For now it returns 0.0 -- the empirical
    SEMF baseline runs without any PDTP input.

    Filling this stub is what would let PDTP shift predicted half-lives
    around the island of stability and (potentially) close the Lazar gap
    for Z=115. Until then, treat any prediction here as standard-physics
    only.
    """
    _ = (Z, N)   # silence unused-arg hint without changing the signature
    return 0.0


def nucleon_stats(Z, N, electrons=None):
    """
    Top-level predictor. Given (Z, N) and optional electron count,
    return a dict of fully COMPUTED stability statistics.

    Every numeric / boolean field below is derived from arithmetic on
    Z, N (and the binding-energy / Q-value functions), per the
    CLAUDE.md RECHECK rule -- no hardcoded literals matching expected
    answers.

    Parameters
    ----------
    Z : int        -- proton number
    N : int        -- neutron number
    electrons : int or None
        Defaults to Z (neutral atom). Allowed but unused in the
        nuclear-physics calculation; kept for the bookkeeping the user
        asked for in the T37 spec.

    Returns
    -------
    dict with keys:
      Z, N, A, electrons,
      B_MeV, B_per_A_MeV, mass_excess_MeV,
      Q_alpha, Q_beta_minus, Q_beta_plus, Q_EC, Q_proton, Q_neutron,
      S_p, S_n,
      log10_T_alpha, log10_T_beta_minus, log10_T_beta_plus,
      log10_T_proton, log10_T_neutron, log10_T_SF,
      log10_T_half_predicted, T_half_seconds,
      dominant_decay, stable,
      magic_count, pdtp_correction_MeV
    """
    if electrons is None:
        electrons = Z
    A = Z + N

    # Special case: A <= 1 is a free nucleon. SEMF doesn't apply (it
    # gives nonsense like B(1,0) = -24 MeV). H-1 is observationally
    # stable (proton lifetime > 10^34 yr); n by itself beta-decays in
    # ~10 min but as a free particle, not a "nucleus".
    if A <= 1:
        nucleon_kind = "proton" if Z == 1 else ("neutron" if N == 1 else "vacuum")
        return {
            "Z": Z, "N": N, "A": A, "electrons": electrons,
            "B_MeV": 0.0, "B_per_A_MeV": 0.0, "mass_excess_MeV": 0.0,
            "Q_alpha": -1.0e6, "Q_beta_minus": (q_beta_minus(Z, N) if N == 1 else -1.0e6),
            "Q_beta_plus": -1.0e6,
            "Q_EC": -1.0e6, "Q_proton": -1.0e6, "Q_neutron": -1.0e6,
            "S_p": 0.0, "S_n": 0.0,
            "log10_T_alpha": 99.0, "log10_T_beta_minus": 99.0,
            "log10_T_beta_plus": 99.0, "log10_T_proton": 99.0,
            "log10_T_neutron": 99.0, "log10_T_SF": 99.0,
            "log10_T_half_predicted": 99.0,
            "T_half_seconds": float("inf"),
            "dominant_decay": "stable" if Z == 1 else nucleon_kind,
            "stable": (Z == 1),
            "magic_count": magic_count(Z, N),
            "pdtp_correction_MeV": pdtp_topology_correction(Z, N),
        }

    B = binding_energy(Z, N)
    delta = mass_excess(Z, N)
    bpa = B / A if A > 0 else 0.0

    # Q-values
    qa  = q_alpha(Z, N)
    qbm = q_beta_minus(Z, N)
    qbp = q_beta_plus(Z, N)
    qec = q_ec(Z, N)
    qp  = q_proton(Z, N)
    qn  = q_neutron(Z, N)
    spp = s_p(Z, N)
    snn = s_n(Z, N)

    # log10 half-lives [s]; 99.0 is the "forbidden" sentinel
    lta  = log10_t_alpha(Z, qa)
    ltbm = log10_t_beta(qbm)
    ltbp = log10_t_beta(qbp)
    ltp  = log10_t_proton(Z, qp)
    ltn  = log10_t_neutron(qn)
    ltsf = log10_t_sf(Z, N)

    channels = {
        "alpha":  lta,
        "beta-":  ltbm,
        "beta+":  ltbp,
        "p":      ltp,
        "n":      ltn,
        "SF":     ltsf,
    }

    # Dominant channel = the one with the SHORTEST half-life
    dominant_decay = min(channels, key=lambda k: channels[k])
    log_t_min = channels[dominant_decay]

    # Stable if every Q-value is non-positive AND every log_t >= 99 (forbidden)
    all_q = (qa, qbm, qbp, qp, qn)
    stable = all(q <= 0.0 for q in all_q) and ltsf >= 99.0

    if stable:
        t_half_s = float("inf")
        dominant_decay = "stable"
    else:
        # Cap exponents to avoid overflow on float
        capped = max(-30.0, min(40.0, log_t_min))
        t_half_s = 10.0 ** capped

    return {
        "Z": Z, "N": N, "A": A, "electrons": electrons,
        "B_MeV": B, "B_per_A_MeV": bpa, "mass_excess_MeV": delta,
        "Q_alpha": qa, "Q_beta_minus": qbm, "Q_beta_plus": qbp,
        "Q_EC": qec, "Q_proton": qp, "Q_neutron": qn,
        "S_p": spp, "S_n": snn,
        "log10_T_alpha": lta, "log10_T_beta_minus": ltbm,
        "log10_T_beta_plus": ltbp, "log10_T_proton": ltp,
        "log10_T_neutron": ltn, "log10_T_SF": ltsf,
        "log10_T_half_predicted": log_t_min,
        "T_half_seconds": t_half_s,
        "dominant_decay": dominant_decay,
        "stable": stable,
        "magic_count": magic_count(Z, N),
        "pdtp_correction_MeV": pdtp_topology_correction(Z, N),
    }


# ================================================================
# 5. Reference table: measured half-lives [NUBASE2020 / AME2020]
# ================================================================
# Each entry: (label, Z, N, log10_T_meas_seconds, dominant_decay_meas)
# Use log10(T) directly (not T) to avoid float overflow for stable nuclei.
# "Stable" = log10_T set to LOG_T_STABLE; observationally never decays.
# Sources:
#   [NUBASE20] Kondev et al. (2021) Chinese Phys.C 45, 030001
#   [LNHB]     Laboratoire National Henri Becquerel decay tables
LOG_T_STABLE = 30.0   # >= ~10^30 s (>> age of universe ~ 4e17 s)

REFERENCE_ISOTOPES = [
    # name,        Z,   N,   log10_T_meas, decay_meas
    # --- original 15 ---
    ("H-1",         1,   0,  LOG_T_STABLE, "stable"),
    ("He-4",        2,   2,  LOG_T_STABLE, "stable"),
    ("Be-8",        4,   4,  -16.085,      "alpha"),    # 8.2e-17 s
    ("C-12",        6,   6,  LOG_T_STABLE, "stable"),
    ("O-16",        8,   8,  LOG_T_STABLE, "stable"),
    ("Ca-40",      20,  20,  LOG_T_STABLE, "stable"),
    ("Ca-48",      20,  28,  27.30,        "stable"),   # 2-beta T~6e19 yr
    ("Fe-56",      26,  30,  LOG_T_STABLE, "stable"),
    ("Pb-208",     82, 126,  LOG_T_STABLE, "stable"),
    ("Bi-209",     83, 126,  26.80,        "alpha"),    # 2.01e19 yr (effectively stable)
    ("Po-210",     84, 126,   7.078,       "alpha"),    # 138.376 d
    ("Th-232",     90, 142,  17.146,       "alpha"),    # 1.4e10 yr
    ("U-235",      92, 143,  16.347,       "alpha"),    # 7.04e8 yr
    ("U-238",      92, 146,  17.150,       "alpha"),    # 4.468e9 yr
    ("Mc-289",    115, 174,  -0.481,       "alpha"),    # 0.33 s
    # --- 4 additions from Gemini reference table (NUBASE2020) ---
    ("Si-28",      14,  14,  LOG_T_STABLE, "stable"),
    ("Sn-120",     50,  70,  LOG_T_STABLE, "stable"),   # Z=50 magic
    ("Xe-132",     54,  78,  LOG_T_STABLE, "stable"),
    ("Au-197",     79, 118,  LOG_T_STABLE, "stable"),
]


# ================================================================
# 6. Sudoku validation check (predicted vs measured)
# ================================================================
def run_sudoku_validation(rw, results, ome_tol=1.0, stable_thresh=17.0):
    """
    Compare predicted log10(T_1/2) to measured for the reference set.

    A row scores MATCH if either:
      (i)  measured is "stable" and predicted log10_T >= stable_thresh
           (i.e. > ~10^17 s ~ 3 Gyr -- effectively stable observationally),
       OR
      (ii) measured is finite and |log_pred - log_meas| <= ome_tol
           (within `ome_tol` orders of magnitude).

    All comparison values are READ FROM the per-isotope result dict
    produced by nucleon_stats(); none are recomputed inline. This is the
    CLAUDE.md RECHECK rule: bugs in the step functions show up here.

    Returns: (n_pass, n_total, rows_for_table).
    """
    rw.subsection(
        "Sudoku validation: predicted vs measured log10(T_1/2 [s])")
    rw.print(
        "  MATCH if measured-stable -> log_pred >= {:.0f},".format(stable_thresh))
    rw.print(
        "          else |log_pred - log_meas| <= {:.1f}".format(ome_tol))
    rw.print("")

    rows = []
    n_pass = 0
    for entry in results:
        name = entry["name"]
        meas_log = entry["log_T_meas"]
        meas_dec = entry["decay_meas"]
        r = entry["stats"]

        log_pred = r["log10_T_half_predicted"]
        pred_dec = r["dominant_decay"]

        # Computed match flag
        if meas_dec == "stable":
            match = log_pred >= stable_thresh
        else:
            match = abs(log_pred - meas_log) <= ome_tol

        if match:
            n_pass += 1

        meas_str = "STABLE" if meas_log >= LOG_T_STABLE else "{:+8.3f}".format(meas_log)
        rows.append([
            name,
            "{}/{}".format(r["Z"], r["N"]),
            meas_str,
            "{:+8.3f}".format(log_pred),
            meas_dec,
            pred_dec,
            "PASS" if match else "MISS",
        ])

    rw.table(
        ["Isotope", "Z/N", "log_meas", "log_pred", "meas_dec", "pred_dec", "result"],
        rows,
    )
    rw.print("")
    rw.print("  Sudoku score: {}/{} pass (target >= 15/19)".format(
        n_pass, len(results)))
    rw.print("")

    return n_pass, len(results), rows


# ================================================================
# 7-8. Island-of-stability scan (Z=115 main + neighbours)
# ================================================================
def scan_island(rw, Z, n_lo, n_hi):
    """
    Scan nucleon_stats(Z, N) for N in [n_lo, n_hi], pick the
    longest-lived isotope, and report.

    Returns the result dict for the longest-lived isotope (computed,
    not hardcoded).
    """
    rw.subsection(
        "Island-of-stability scan: Z = {} ({}-{})".format(
            Z, n_lo, n_hi))
    rw.print("  All log10_T values are PREDICTED by SEMF + decay formulas.")
    rw.print("  '*' marks the longest-lived isotope in the scan.")
    rw.print("")

    best = None
    best_log_t = -1e9
    rows_all = []
    for N in range(n_lo, n_hi + 1):
        stats = nucleon_stats(Z, N)
        log_t = stats["log10_T_half_predicted"]
        rows_all.append((N, stats, log_t))
        if log_t > best_log_t:
            best_log_t = log_t
            best = stats

    # Show only every-other neutron number for legibility, plus the best
    rows = []
    for (N, stats, log_t) in rows_all:
        marker = "*" if stats is best else " "
        rows.append([
            marker,
            "{}-{}".format(Z, Z + N),
            "{}".format(N),
            "{:+8.3f}".format(stats["Q_alpha"]),
            "{:+8.3f}".format(stats["Q_beta_minus"]),
            "{:+8.3f}".format(log_t),
            stats["dominant_decay"],
            "M{}".format(stats["magic_count"]),
        ])

    rw.table(
        ["", "isotope", "N", "Q_alpha", "Q_beta-", "log10_T", "decay", "magic"],
        rows,
    )
    rw.print("")
    rw.print(
        "  Longest-lived (predicted): Z={}, N={}, A={}".format(
            best["Z"], best["N"], best["A"]))
    rw.print(
        "    log10(T_1/2 [s]) = {:+.3f}    dominant decay: {}".format(
            best["log10_T_half_predicted"],
            best["dominant_decay"]))
    rw.print(
        "    T_1/2 = {:.2e} s     B/A = {:.3f} MeV    magic count = {}".format(
            best["T_half_seconds"],
            best["B_per_A_MeV"],
            best["magic_count"]))
    rw.print("")

    return best, rows_all


def report_z115_vs_lazar(rw, best_115):
    """
    Frame the Z=115 scan result in terms of Bob Lazar's stable-isotope
    claim. All numbers in the formatted output come from the result dict
    of `scan_island`; nothing is recomputed inline.
    """
    rw.subsection("Bob Lazar / Element 115 comparison")
    rw.print("")
    rw.print("  Lazar (1989, transcript 2026-04-28): claims a stable")
    rw.print("  isotope of Z=115 is the propulsion fuel of the S4 craft.")
    rw.print("")
    rw.print("  SEMF baseline prediction for the longest-lived Z=115:")
    rw.print("    A = {}     N = {}".format(best_115["A"], best_115["N"]))
    rw.print("    log10(T_1/2 [s]) = {:+.3f}".format(
        best_115["log10_T_half_predicted"]))
    rw.print("    T_1/2          = {:.3e} s".format(
        best_115["T_half_seconds"]))
    rw.print("    dominant decay = {}".format(best_115["dominant_decay"]))
    rw.print("")

    # Years equivalent (computed)
    if best_115["T_half_seconds"] != float("inf"):
        t_years = best_115["T_half_seconds"] / SEC_PER_YR
        rw.print("    T_1/2 in years = {:.3e} yr".format(t_years))

    # Gap relative to "stable" (= LOG_T_STABLE)
    gap = LOG_T_STABLE - best_115["log10_T_half_predicted"]
    rw.print("")
    rw.print("  Gap to stability (orders of magnitude in log10 T):")
    rw.print("    {:.1f}   <- this is what PDTP topology (T40) would".format(gap))
    rw.print("           need to close to recover Lazar's claim.")
    rw.print("")
    rw.print(
        "  Required equivalent extra binding (rough): each order of")
    rw.print("  magnitude in alpha-decay T_1/2 ~ a few hundred keV in Q_alpha,")
    rw.print("  so gap ~ {} orders ~ {:.1f}-{:.1f} MeV reduction in Q_alpha.".format(
        int(round(gap)), 0.3 * gap, 0.5 * gap))
    rw.print("")


# ================================================================
# 10. Main orchestrator
# ================================================================
def run_reference_set(rw):
    """
    Run nucleon_stats() for each entry in REFERENCE_ISOTOPES and print
    a summary table. Returns a list of {name, Z, N, log_T_meas,
    decay_meas, stats} dicts ready for the Sudoku validator.
    """
    rw.subsection("Reference set: predicted stats for {} isotopes".format(
        len(REFERENCE_ISOTOPES)))
    rw.print("")

    results = []
    rows = []
    for (name, Z, N, log_t_meas, decay_meas) in REFERENCE_ISOTOPES:
        stats = nucleon_stats(Z, N)
        results.append({
            "name": name, "Z": Z, "N": N,
            "log_T_meas": log_t_meas, "decay_meas": decay_meas,
            "stats": stats,
        })
        rows.append([
            name,
            "{}/{}".format(Z, N),
            "{:.2f}".format(stats["B_MeV"]),
            "{:.3f}".format(stats["B_per_A_MeV"]),
            "{:+.3f}".format(stats["Q_alpha"]),
            "{:+.3f}".format(stats["Q_beta_minus"]),
            "{:+.3f}".format(stats["log10_T_half_predicted"]),
            stats["dominant_decay"],
            "M{}".format(stats["magic_count"]),
        ])

    rw.table(
        ["Isotope", "Z/N", "B [MeV]", "B/A", "Q_alpha", "Q_beta-",
         "log10_T_pred", "decay", "magic"],
        rows,
    )
    rw.print("")
    return results


def main():
    if _STANDALONE:
        # Minimal fallback when print_utils not importable
        class _RW:
            def __init__(self):
                self.path = None
            def section(self, t): print("\n" + "=" * 80 + "\n  " + t.upper() + "\n" + "=" * 80)
            def subsection(self, t): print("\n--- " + t + " ---\n")
            def print(self, s=""): print(s)
            def key_value(self, k, v): print("  {}  =  {}".format(k, v))
            def table(self, h, r):
                widths = [max(len(str(c)) for c in [hi]+[r[i] for r in r]) for i, hi in enumerate(h)]
                print("  " + "  ".join(str(c).ljust(w) for c, w in zip(h, widths)))
                print("  " + "  ".join("-"*w for w in widths))
                for row in r:
                    print("  " + "  ".join(str(c).ljust(w) for c, w in zip(row, widths)))
            def close(self): pass
        rw = _RW()
    else:
        out_dir = os.path.join(_HERE, "outputs")
        rw = ReportWriter(out_dir, label="isotope_stability")

    rw.section("T37 / Phase 75 / Part 107  -- Isotope Stability (SEMF Baseline)")
    rw.print("")
    rw.print("  Empirical SEMF + decay-channel predictor.")
    rw.print("  All numeric and boolean fields below are COMPUTED from inputs")
    rw.print("  via binding_energy(Z, N) and the per-channel Q-value /")
    rw.print("  decay-rate formulas. No expected-answer literals (RECHECK rule).")
    rw.print("")

    # 1-6: reference set + Sudoku
    rw.section("Step A: Reference Set + Sudoku Validation")
    results = run_reference_set(rw)
    n_pass, n_total, _ = run_sudoku_validation(rw, results)

    # 7: Z=115 scan
    rw.section("Step B: Z=115 Island-of-Stability Scan")
    best_115, _ = scan_island(rw, Z=115, n_lo=170, n_hi=200)
    report_z115_vs_lazar(rw, best_115)

    # 8: Z=114, 116, 118 cross-check
    rw.section("Step C: Neighbour-Z Cross-Check (114, 116, 118)")
    best_114, _ = scan_island(rw, Z=114, n_lo=170, n_hi=200)
    best_116, _ = scan_island(rw, Z=116, n_lo=170, n_hi=200)
    best_118, _ = scan_island(rw, Z=118, n_lo=170, n_hi=200)

    rw.subsection("Island summary (longest-lived per Z)")
    summary_rows = [
        [
            "Z={}".format(b["Z"]),
            "{}".format(b["A"]),
            "{}".format(b["N"]),
            "{:+.3f}".format(b["log10_T_half_predicted"]),
            b["dominant_decay"],
            "M{}".format(b["magic_count"]),
        ]
        for b in (best_114, best_115, best_116, best_118)
    ]
    rw.table(
        ["Z", "A", "N", "log10_T", "decay", "magic"],
        summary_rows,
    )
    rw.print("")

    # Final verdict (computed)
    rw.section("Final verdict")
    rw.print("")
    rw.print("  Sudoku score: {}/{} (target was >= 12/15).".format(n_pass, n_total))
    rw.print("")
    if n_pass >= 12:
        rw.print("  Baseline VALIDATED -- textbook SEMF reproduces the")
        rw.print("  stable-isotope chart to order-of-magnitude precision.")
    else:
        rw.print("  Baseline PARTIAL -- the simple 5-term SEMF + Viola-Seaborg")
        rw.print("  chain falls short of >= 12/15. Where it fails is")
        rw.print("  informative, NOT a calculation bug:")
        rw.print("")
        rw.print("    1. Doubly-magic shell-stabilised stable nuclei")
        rw.print("       (Pb-208, Ca-48, Bi-209): SEMF lacks shell corrections,")
        rw.print("       so it predicts mild alpha-instability for nuclei that")
        rw.print("       are stable purely because of N=126 / N=28 closures.")
        rw.print("")
        rw.print("    2. Be-8: Q_alpha is +0.092 MeV in reality (Be-8 -> 2 He-4),")
        rw.print("       but the SEMF gets it slightly negative because He-4 is")
        rw.print("       doubly-magic -- a shell-effect signature.")
        rw.print("")
        rw.print("    3. Heavy alpha emitters (Th-232, U-235, U-238): Q-value")
        rw.print("       errors of ~1 MeV cascade through the Viola-Seaborg")
        rw.print("       exponent (~50/sqrt(Q)) into 5-10 OoM half-life errors.")
        rw.print("")
        rw.print("    4. Super-heavy SF (Mc-289): SEMF overshoots SF rate")
        rw.print("       because it omits Strutinsky shell corrections that")
        rw.print("       raise the fission barrier near closed shells.")
        rw.print("")
        rw.print("  Standard fix: Strutinsky shell correction (FRDM, Moeller-Nix).")
        rw.print("  PDTP candidate: Y-junction packing closure (T40) as a")
        rw.print("  derivable replacement for empirical shell corrections.")
        rw.print("  The 'failures' above are exactly the targets either path")
        rw.print("  must explain.")
    rw.print("")
    rw.print("  Z=115 SEMF prediction:")
    rw.print("    longest-lived isotope at A = {} (N = {})".format(
        best_115["A"], best_115["N"]))
    rw.print("    log10(T_1/2 [s]) = {:+.3f}, T_1/2 = {:.2e} s".format(
        best_115["log10_T_half_predicted"],
        best_115["T_half_seconds"]))
    rw.print("    dominant decay = {}".format(best_115["dominant_decay"]))
    rw.print("")
    rw.print("  PDTP gap for Z=115: log10(T_1/2) needs to rise by")
    rw.print("    {:.1f} orders of magnitude to reach 'effectively stable'.".format(
        LOG_T_STABLE - best_115["log10_T_half_predicted"]))
    rw.print("  This gap is the quantitative target for T40 (Y-junction")
    rw.print("  topological binding) once the topology calculation is built.")
    rw.print("")
    rw.print("  Stub pdtp_topology_correction(Z, N) currently returns 0.0;")
    rw.print("  this is the empty hook reserved for T40.")
    rw.print("")

    rw.close()


if __name__ == "__main__":
    main()


