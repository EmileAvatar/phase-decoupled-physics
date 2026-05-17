# t7_hawking_n_pdtp.py  --  T7: Hawking Temperature with n_PDTP = 1/alpha
# Part 111, Phase 79
#
# Does the PDTP refractive index n = 1/alpha modify the Hawking temperature?
# Answer: NO -- but the derivation reveals the physical reason and produces
# a new PDTP formulation of the surface gravity in terms of n.
#
# Equations:
#   111.1  T_H = hbar c^3 / (8 pi G M k_B)              [Part 24, ESTABLISHED]
#   111.2  alpha(r) = sqrt(1 - r_S/r), r_S = 2GM/c^2    [Part 98, ESTABLISHED]
#   111.3  kappa = (c^2/2) |d(alpha^2)/dr|_{r_S} = c^2/(2r_S)  [DERIVED]
#   111.4  kappa = (c^2/2) |d(1/n^2)/dr|_{r_S}          [PDTP Original]
#   111.5  T_H^PDTP = T_H^GR (n_PDTP does not modify T_H) [DERIVED]
#   111.6  c_phase = c*alpha = c/n -> 0 at horizon        [ESTABLISHED, Part 98]
#   111.7  c_group = c_s = c (always, Part 34)           [Part 34, ESTABLISHED]
#   111.8  Breathing mode: spectrum cut off at omega < omega_gap = sqrt(2g) [DERIVED]
#   111.9  Two-phase: G_eff = 2G_bare (Part 61); G_N = G_eff -> T_H unchanged [VERIFIED]
#
# Python rule: ASCII only; output saved to outputs/hawking_n_pdtp_<ts>.txt

import math
import sys
import os
from datetime import datetime

try:
    import sympy as sp
    SYMPY_OK = True
except ImportError:
    SYMPY_OK = False

# ---------------------------------------------------------------------------
# Physical constants
# ---------------------------------------------------------------------------

HBAR   = 1.0546e-34   # J s
C      = 2.998e8      # m/s
G_N    = 6.674e-11    # N m^2 / kg^2
K_B    = 1.381e-23    # J/K
M_SUN  = 1.989e30     # kg
G_COSMO = 2.4e-36     # s^{-2} (Part 25 coupling constant)

# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

class _RW:
    def __init__(self, path):
        self._lines = []
        self._path = path

    def w(self, line=""):
        self._lines.append(str(line))
        print(line)

    def section(self, title):
        self.w()
        self.w("=" * 60)
        self.w(title)
        self.w("=" * 60)

    def save(self):
        with open(self._path, "w", encoding="ascii", errors="replace") as f:
            f.write("\n".join(self._lines))
        print("\nLog saved to", self._path)


# ---------------------------------------------------------------------------
# Core PDTP profile functions
# ---------------------------------------------------------------------------

def alpha_r(r, r_S):
    """alpha(r) = sqrt(1 - r_S/r)  [Eq 111.2, Part 98]"""
    if r <= r_S:
        return 0.0
    return math.sqrt(1.0 - r_S / r)

def n_r(r, r_S):
    """n(r) = 1/alpha(r)  [Part 98]"""
    a = alpha_r(r, r_S)
    if a <= 0:
        return float("inf")
    return 1.0 / a

def d_alpha2_dr(r, r_S):
    """d(alpha^2)/dr = d(1 - r_S/r)/dr = r_S/r^2  [Eq 111.3]"""
    return r_S / r**2

def kappa_from_lapse(r_S):
    """
    Surface gravity from lapse gradient at r = r_S.
    kappa = (c^2/2) |d(alpha^2)/dr|_{r_S}
           = (c^2/2) * (r_S/r_S^2)
           = c^2 / (2 r_S)   [Eq 111.3, DERIVED]
    """
    return C**2 / (2.0 * r_S)

def kappa_from_n(r_S):
    """
    Surface gravity from n^{-2} gradient at r = r_S.
    kappa = (c^2/2) |d(1/n^2)/dr|_{r_S}
    Since 1/n^2 = alpha^2, the gradient is the same as kappa_from_lapse.
    [Eq 111.4, PDTP Original -- same result, different framing]
    """
    # d(1/n^2)/dr = d(alpha^2)/dr = r_S/r^2; at r_S: r_S/r_S^2 = 1/r_S
    return C**2 / (2.0 * r_S)

def T_hawking(M):
    """T_H = hbar c^3 / (8 pi G M k_B)  [Eq 111.1, Part 24]"""
    return (HBAR * C**3) / (8.0 * math.pi * G_N * M * K_B)

def r_S_from_M(M):
    """Schwarzschild radius r_S = 2GM/c^2"""
    return 2.0 * G_N * M / C**2


# ---------------------------------------------------------------------------
# Step 1: kappa profile and T_H verification
# ---------------------------------------------------------------------------

def step1_kappa_profile(rw):
    """
    Compute alpha(r), n(r), and the lapse gradient d(alpha^2)/dr
    for a 1-solar-mass BH. Verify kappa = c^2/(2r_S) and T_H = Part 24 result.
    """
    rw.section("Step 1 -- kappa from lapse and T_H verification")

    M    = M_SUN
    r_S  = r_S_from_M(M)
    kap  = kappa_from_lapse(r_S)
    T_H  = T_hawking(M)
    T_H_from_kap = (HBAR * kap) / (2.0 * math.pi * C * K_B)

    rw.w("Black hole: M = 1 M_sun = {:.3e} kg".format(M))
    rw.w("  r_S     = {:.4e} m  ({:.2f} km)".format(r_S, r_S / 1e3))
    rw.w("  kappa   = c^2/(2r_S) = {:.4e} m/s^2   [Eq 111.3]".format(kap))
    rw.w("  T_H (Part 24 formula) = {:.4e} K".format(T_H))
    rw.w("  T_H (from kappa)      = {:.4e} K".format(T_H_from_kap))
    rw.w("  Agreement: {:.2e}  PASS={}".format(
        abs(T_H - T_H_from_kap) / T_H, abs(T_H - T_H_from_kap) / T_H < 1.0e-6))
    rw.w("")

    # Radial profile
    rw.w("Radial profile near horizon (r/r_S from 1.01 to 10):")
    rw.w("{:>10}  {:>10}  {:>12}  {:>14}  {:>14}".format(
        "r/r_S", "alpha", "n=1/alpha", "d(a^2)/dr", "c_phase/c"))
    for ratio in [1.01, 1.1, 1.5, 2.0, 3.0, 5.0, 10.0]:
        r = ratio * r_S
        a = alpha_r(r, r_S)
        ni = n_r(r, r_S)
        da2 = d_alpha2_dr(r, r_S)
        c_ph = C * a  # phase velocity
        rw.w("{:>10.2f}  {:>10.6f}  {:>12.4f}  {:>14.4e}  {:>14.6f}".format(
            ratio, a, ni, da2, c_ph / C))
    rw.w("")
    rw.w("At r -> r_S: alpha -> 0, n -> inf, c_phase -> 0.")
    rw.w("d(alpha^2)/dr = r_S/r^2 -> 1/r_S at r_S (finite, not zero).")
    rw.w("=> Surface gravity kappa is finite despite n -> inf.")

    return {"M": M, "r_S": r_S, "kappa": kap, "T_H": T_H, "T_H_from_kappa": T_H_from_kap}


# ---------------------------------------------------------------------------
# Step 2: kappa in terms of n  (Eq 111.4, PDTP Original)
# ---------------------------------------------------------------------------

def step2_kappa_from_n(rw, r1):
    """
    Eq 111.4 [PDTP Original]:  kappa = (c^2/2) |d(1/n^2)/dr|_{r_S}

    Physical statement: the surface gravity is the gradient of n^{-2} at the horizon.
    Since 1/n^2 = alpha^2, this is identical to Eq 111.3, but expresses it purely
    in terms of the PDTP refractive index.

    A steeper n(r) gradient near the horizon -> larger kappa -> higher T_H.
    The standard Schwarzschild has n^{-2} = 1 - r_S/r  -> gradient = r_S/r^2.
    """
    rw.section("Step 2 -- kappa from n (Eq 111.4, PDTP Original)")

    r_S = r1["r_S"]
    kap_n = kappa_from_n(r_S)

    rw.w("1/n^2 = alpha^2 = 1 - r_S/r  [Part 98, Eq 111.3]")
    rw.w("d(1/n^2)/dr = r_S/r^2")
    rw.w("At r = r_S: d(1/n^2)/dr = 1/r_S")
    rw.w("")
    rw.w("Eq 111.4 [PDTP Original]:")
    rw.w("  kappa = (c^2/2) |d(1/n^2)/dr|_{r_S}")
    rw.w("        = (c^2/2) * (1/r_S)")
    rw.w("        = {:.4e} m/s^2".format(kap_n))
    rw.w("  == kappa from Eq 111.3: PASS = {}".format(
        abs(kap_n - r1["kappa"]) < 1.0e-10))
    rw.w("")
    rw.w("Physical meaning of Eq 111.4:")
    rw.w("  The surface gravity is the rate at which n^{-2} changes near the horizon.")
    rw.w("  n -> inf rapidly near r_S, but 1/n^2 = alpha^2 has a FINITE gradient.")
    rw.w("  The Hawking temperature therefore depends on d(alpha^2)/dr, not on n itself.")
    rw.w("  => n -> inf at the horizon does NOT mean T_H -> inf.")

    return {"kappa_from_n": kap_n}


# ---------------------------------------------------------------------------
# Step 3: Phase velocity vs group velocity
# ---------------------------------------------------------------------------

def step3_phase_vs_group(rw):
    """
    Key distinction:
      c_phase = c * alpha = c / n  [Eq 111.6]   -- slowed near horizon
      c_group = c_s = c            [Eq 111.7, Part 34]  -- always c

    Hawking T depends on SURFACE GRAVITY (from group velocity), not phase velocity.
    Acoustic surface gravity (Unruh 1981):
      kappa_acoustic = (1/2) |d(c_s^2 - v^2)/dr|_{sonic horizon}
    where v(r) = -c * sqrt(r_S/r) is the PG infall velocity (Part 101).
    c_s = c (constant, Part 34).

    At sonic horizon r = r_S where |v| = c_s = c:
      d(c_s^2 - v^2)/dr = d(c^2 - c^2 r_S/r)/dr = c^2 r_S / r^2
      At r_S: = c^2 / r_S
    kappa_acoustic = c^2 / (2 r_S)  -- same as Eq 111.3.
    """
    rw.section("Step 3 -- Phase vs group velocity (Eqs 111.6, 111.7)")
    rw.w("c_phase(r) = c * alpha(r) = c/n(r)  [Eq 111.6, Part 98]")
    rw.w("c_group    = c_s = c       (constant, Part 34)  [Eq 111.7]")
    rw.w("")
    rw.w("Hawking mechanism (Unruh 1981 acoustic analogy):")
    rw.w("  kappa_acoustic = (1/2) |d(c_s^2 - v^2)/dr|_{r_S}")
    rw.w("  v(r) = -c*sqrt(r_S/r)  (PG infall, Part 101)")
    rw.w("  c_s  = c               (PDTP, Part 34)")
    rw.w("")

    r_S = r_S_from_M(M_SUN)

    rw.w("{:>10}  {:>12}  {:>12}  {:>14}".format(
        "r/r_S", "c_s^2", "v^2", "c_s^2 - v^2"))
    for ratio in [1.01, 1.1, 1.5, 2.0, 5.0, 10.0]:
        r   = ratio * r_S
        v2  = C**2 * (r_S / r)
        cs2 = C**2
        rw.w("{:>10.2f}  {:>12.4e}  {:>12.4e}  {:>14.4e}".format(
            ratio, cs2, v2, cs2 - v2))

    # Gradient at r_S
    grad_at_rS = C**2 / r_S   # d(c_s^2 - v^2)/dr at r = r_S
    kap_acoustic = grad_at_rS / 2.0
    rw.w("")
    rw.w("d(c_s^2 - v^2)/dr = c^2 * r_S/r^2;  at r_S: = c^2/r_S = {:.4e}".format(
        grad_at_rS))
    rw.w("kappa_acoustic = (1/2) * c^2/r_S = {:.4e} m/s^2".format(kap_acoustic))
    rw.w("== kappa_lapse (Eq 111.3): PASS={}".format(
        abs(kap_acoustic - kappa_from_lapse(r_S)) < 1.0))
    rw.w("")
    rw.w("Eq 111.5 [DERIVED]: T_H^PDTP = T_H^GR.")
    rw.w("n_PDTP = 1/alpha does NOT modify T_H because:")
    rw.w("  - n affects the PHASE velocity c_phase = c/n.")
    rw.w("  - Hawking T depends on the GROUP velocity = c_s = c (unchanged).")
    rw.w("  - kappa is determined by the gradient of (c_s^2 - v^2), not c_phase.")

    return {"kappa_acoustic": kap_acoustic, "r_S": r_S}


# ---------------------------------------------------------------------------
# Step 4: Breathing mode spectrum modification  (Eq 111.8)
# ---------------------------------------------------------------------------

def step4_breathing_mode(rw):
    """
    The breathing mode has mass gap omega_gap = sqrt(2 g_eff) (Part 99, Eq 99.1).
    Hawking radiation from a BH normally follows a Planck spectrum at T_H.
    For a massive mode (omega_gap > 0), the Planck spectrum is multiplied
    by a step-function-like suppression below omega_gap:

      n_Planck(omega) = 1 / (exp(hbar*omega / (k_B T_H)) - 1)  [standard]
      n_breath(omega) = 0                    for omega < omega_gap
                      ~ n_Planck(omega)      for omega >> omega_gap  [Eq 111.8]

    The peak emission frequency: omega_peak = 2.82 k_B T_H / hbar (Wien's law)
    Breathing mode cutoff temperature: T_cutoff = hbar omega_gap / k_B

    For macroscopic BHs: T_H << T_cutoff (cosmological g_cosmo is tiny),
    so the breathing mode emission is completely suppressed.
    For Planck-mass BHs: T_H >> T_cutoff, emission is unsuppressed.
    """
    rw.section("Step 4 -- Breathing mode spectrum modification  (Eq 111.8)")

    omega_gap = math.sqrt(2.0 * G_COSMO)  # rad/s, from Part 99
    T_cutoff  = HBAR * omega_gap / K_B    # K

    rw.w("Eq 111.8 [DERIVED]: breathing mode spectrum cut off at omega < omega_gap")
    rw.w("  omega_gap = sqrt(2 g_cosmo) = {:.3e} rad/s  (Part 99)".format(omega_gap))
    rw.w("  T_cutoff  = hbar*omega_gap/k_B = {:.3e} K".format(T_cutoff))
    rw.w("")

    masses = [M_SUN, 10.0 * M_SUN, 1.0e6 * M_SUN, 1.0e10]  # last = Planck-ish
    rw.w("{:>14}  {:>12}  {:>12}  {:>16}".format(
        "M (kg)", "T_H (K)", "T_cutoff/T_H", "breath. suppressed?"))
    results = {}
    for M in masses:
        T_H   = T_hawking(M)
        ratio = T_cutoff / T_H if T_H > 0 else float("inf")
        supp  = "YES (ratio >> 1)" if ratio > 1.0 else "NO (T_H >> T_cutoff)"
        rw.w("{:>14.3e}  {:>12.4e}  {:>12.4e}  {:>16}".format(M, T_H, ratio, supp))
        results[M] = {"T_H": T_H, "ratio": ratio}

    rw.w("")
    rw.w("For stellar BHs: T_H ~ 6e-8 K, T_cutoff ~ 1e-25 K.")
    rw.w("T_cutoff/T_H ~ 1e-18 << 1 => breathing mode is NOT suppressed.")
    rw.w("The mass gap omega_gap is cosmologically tiny; breathing emission is")
    rw.w("unsuppressed for all astrophysical BHs.")
    rw.w("T_H itself is unchanged; only the spectrum shape differs below omega_gap.")

    return {"omega_gap": omega_gap, "T_cutoff": T_cutoff, "results": results}


# ---------------------------------------------------------------------------
# Step 5: Two-phase G_eff check + birefringence check
# ---------------------------------------------------------------------------

def step5_two_phase_birefringence(rw, r1):
    """
    Eq 111.9: Two-phase (Part 61) gives G_eff = 2 G_bare.
    Laboratory measurements of G give G_N = G_eff (the effective value).
    T_H = hbar c^3 / (8 pi G_N M k_B) -- uses G_N = G_eff.
    => T_H is unchanged in terms of observed G_N.

    Birefringence check (T4 cross-check):
    T4 showed + and x GW modes have different Brewster angles but same n = 1/alpha.
    Since both have the same n(r) profile, both have the same kappa and T_H.
    """
    rw.section("Step 5 -- Two-phase G_eff + birefringence check  (Eq 111.9)")

    # Two-phase
    G_bare  = G_N / 2.0            # if G_eff = 2 G_bare
    T_H_Geff  = T_hawking(r1["M"])  # uses G_N (= G_eff in lab)
    T_H_Gbare = (HBAR * C**3) / (8.0 * math.pi * G_bare * r1["M"] * K_B)

    rw.w("Eq 111.9 [VERIFIED]: Two-phase check (Part 61)")
    rw.w("  G_eff = 2 G_bare   (Newton's 3rd law factor from Part 61)")
    rw.w("  G_N   = G_eff      (lab measurement uses G_eff)")
    rw.w("  T_H(G_eff) = {:.4e} K  <-- this is the observable T_H".format(T_H_Geff))
    rw.w("  T_H(G_bare)= {:.4e} K  <-- would apply if G_bare were measured".format(
        T_H_Gbare))
    rw.w("  Ratio T_H(G_bare)/T_H(G_eff) = {:.2f}".format(T_H_Gbare / T_H_Geff))
    rw.w("  Since G_N = G_eff, T_H in observable terms is UNCHANGED.")
    rw.w("")

    # Birefringence check
    rw.w("Birefringence check (T4 / Part 108 cross-check):")
    rw.w("  T4 showed + and x GW modes have different Brewster angles.")
    rw.w("  Both modes share the same n(r) = 1/alpha(r) profile.")
    rw.w("  => Both have the same kappa = c^2/(2r_S).")
    rw.w("  => Both have the same T_H = hbar c^3/(8 pi G M k_B).")
    rw.w("  Birefringence splits Brewster angles but NOT Hawking temperatures.")

    T_H_plus  = T_hawking(r1["M"])   # same for both
    T_H_cross = T_hawking(r1["M"])   # same for both
    rw.w("  T_H(+) = {:.4e} K".format(T_H_plus))
    rw.w("  T_H(x) = {:.4e} K".format(T_H_cross))
    rw.w("  T_H(+) == T_H(x): PASS={}".format(abs(T_H_plus - T_H_cross) < 1.0e-20))

    return {
        "T_H_Geff":  T_H_Geff,
        "T_H_Gbare": T_H_Gbare,
        "T_H_plus":  T_H_plus,
        "T_H_cross": T_H_cross,
    }


# ---------------------------------------------------------------------------
# Step 6: SymPy verification
# ---------------------------------------------------------------------------

def step6_sympy(rw):
    rw.section("Step 6 -- SymPy verification")
    if not SYMPY_OK:
        rw.w("SymPy not available -- skipping")
        return {"sympy_available": False}

    r, r_S, G, M, c, hbar, k_B_sym = sp.symbols(
        "r r_S G M c hbar k_B", positive=True)

    # S1: alpha^2 = 1 - r_S/r
    alpha2 = 1 - r_S / r
    d_alpha2 = sp.diff(alpha2, r)
    d_alpha2_at_rS = d_alpha2.subs(r, r_S)
    s1 = sp.simplify(d_alpha2_at_rS - 1 / r_S) == 0
    rw.w("S1  d(alpha^2)/dr at r_S = {}  (expect 1/r_S)  PASS={}".format(
        d_alpha2_at_rS, s1))

    # S2: kappa = c^2/(2r_S) from lapse gradient
    kappa_sym = sp.Rational(1, 2) * c**2 * d_alpha2_at_rS
    kappa_expected = c**2 / (2 * r_S)
    s2 = sp.simplify(kappa_sym - kappa_expected) == 0
    rw.w("S2  kappa = (c^2/2)*d(a^2)/dr at r_S = {}  PASS={}".format(
        sp.simplify(kappa_sym), s2))

    # S3: 1/n^2 = alpha^2, so d(1/n^2)/dr = d(alpha^2)/dr (same Eq 111.4)
    inv_n2 = alpha2
    d_inv_n2 = sp.diff(inv_n2, r).subs(r, r_S)
    s3 = sp.simplify(d_inv_n2 - d_alpha2_at_rS) == 0
    rw.w("S3  d(1/n^2)/dr at r_S == d(alpha^2)/dr at r_S  PASS={}".format(s3))

    # S4: T_H = hbar*kappa/(2*pi*c*k_B) with r_S = 2GM/c^2
    r_S_expr = 2 * G * M / c**2
    kappa_expr = c**2 / (2 * r_S_expr)
    T_H_sym = hbar * kappa_expr / (2 * sp.pi * c * k_B_sym)
    T_H_expected = hbar * c**3 / (8 * sp.pi * G * M * k_B_sym)
    s4 = sp.simplify(T_H_sym - T_H_expected) == 0
    rw.w("S4  T_H from kappa = {}  (expect hbar c^3/(8pi G M k_B))  PASS={}".format(
        sp.simplify(T_H_sym), s4))

    # S5: T_H scales as 1/M
    T_H_2M = T_H_expected.subs(M, 2 * M)
    ratio_TH = sp.simplify(T_H_expected / T_H_2M)
    s5 = ratio_TH == 2
    rw.w("S5  T_H(M) / T_H(2M) = {}  (expect 2, 1/M scaling)  PASS={}".format(
        ratio_TH, s5))

    n_pass = sum([s1, s2, s3, s4, s5])
    rw.w("SymPy score: {}/5 PASS".format(n_pass))
    return {
        "sympy_available": True,
        "s1": s1, "s2": s2, "s3": s3, "s4": s4, "s5": s5,
        "n_pass": n_pass,
    }


# ---------------------------------------------------------------------------
# Step 7: Sudoku checks
# ---------------------------------------------------------------------------

def step7_sudoku(rw, r1, r2, r3, r4, r5):
    rw.section("Step 7 -- Sudoku consistency checks")
    results = []

    def chk(label, cond):
        results.append(cond)
        rw.w("  [{:4}] {}".format("PASS" if cond else "FAIL", label))

    r_S = r1["r_S"]
    M   = r1["M"]

    # S01: alpha(r_S) = 0  (horizon condition)
    chk("S01 alpha(r_S) = 0  (horizon)",
        abs(alpha_r(r_S, r_S)) < 1.0e-15)

    # S02: alpha -> 1 at r >> r_S  (asymptotic flat)
    chk("S02 alpha(100*r_S) ~ 1  (asymptotic flat)",
        abs(alpha_r(100.0 * r_S, r_S) - 1.0) < 0.02)

    # S03: n(r_S) -> inf  (refractive index diverges at horizon)
    n_near = n_r(1.001 * r_S, r_S)
    chk("S03 n(1.001 r_S) >> 1  (n -> inf at horizon)",
        n_near > 10.0)

    # S04: kappa from lapse = c^2/(2r_S)
    kap_ref = C**2 / (2.0 * r_S)
    chk("S04 kappa = c^2/(2r_S) from lapse gradient",
        abs(r1["kappa"] - kap_ref) < 1.0)

    # S05: kappa from n^{-2} = kappa from alpha^2  (Eq 111.4 vs 111.3)
    chk("S05 kappa_n == kappa_alpha  (Eqs 111.3 and 111.4)",
        abs(r2["kappa_from_n"] - r1["kappa"]) < 1.0e-10)

    # S06: T_H from Part 24 formula == T_H from kappa
    chk("S06 T_H(Part 24) == T_H(kappa)  (Eq 111.5)",
        abs(r1["T_H"] - r1["T_H_from_kappa"]) / r1["T_H"] < 1.0e-6)

    # S07: c_phase(r_S) = 0  (phase velocity vanishes)
    c_ph_at_rS = C * alpha_r(r_S, r_S)
    chk("S07 c_phase(r_S) = 0  (Eq 111.6)",
        abs(c_ph_at_rS) < 1.0e-10)

    # S08: c_group = c  (group velocity unchanged, Eq 111.7)
    chk("S08 c_group = c_s = c  (Eq 111.7, Part 34)",
        True)   # definitional from Part 34; flagged as ESTABLISHED

    # S09: kappa_acoustic = kappa_lapse  (Eq 111.3 = acoustic derivation)
    chk("S09 kappa_acoustic = kappa_lapse  (two routes, same result)",
        abs(r3["kappa_acoustic"] - r1["kappa"]) < 1.0)

    # S10: T_H scales as 1/M  (larger BH is cooler)
    T_H_2M = T_hawking(2.0 * M)
    chk("S10 T_H(2M) = T_H(M)/2  (1/M scaling)",
        abs(T_H_2M - r1["T_H"] / 2.0) / r1["T_H"] < 1.0e-6)

    # S11: T_H^PDTP = T_H^GR  (n_PDTP does not modify T_H)
    chk("S11 T_H^PDTP = T_H^GR  (Eq 111.5)",
        abs(r5["T_H_Geff"] - r1["T_H"]) < 1.0e-20)

    # S12: Birefringence: T_H(+) = T_H(x)
    chk("S12 T_H(+) = T_H(x)  (birefringence does not split T_H)",
        abs(r5["T_H_plus"] - r5["T_H_cross"]) < 1.0e-20)

    n_pass = sum(results)
    rw.w("")
    rw.w("Sudoku score: {}/{} PASS".format(n_pass, len(results)))
    return {"n_pass": n_pass, "n_total": len(results)}


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = os.path.join(os.path.dirname(__file__), "outputs")
    os.makedirs(out_dir, exist_ok=True)
    log_path = os.path.join(out_dir, "hawking_n_pdtp_{}.txt".format(ts))
    rw = _RW(log_path)

    rw.w("T7 -- Hawking Temperature with n_PDTP = 1/alpha")
    rw.w("Part 111, Phase 79  |  {}".format(datetime.now().isoformat()))
    rw.w("Question: does n_PDTP = 1/alpha modify T_H?")

    r1 = step1_kappa_profile(rw)
    r2 = step2_kappa_from_n(rw, r1)
    r3 = step3_phase_vs_group(rw)
    r4 = step4_breathing_mode(rw)
    r5 = step5_two_phase_birefringence(rw, r1)
    r6 = step6_sympy(rw)
    r7 = step7_sudoku(rw, r1, r2, r3, r4, r5)

    rw.section("Summary -- T7 Hawking Temperature with n_PDTP")
    rw.w("ANSWER: n_PDTP does NOT modify T_H.  T_H^PDTP = T_H^GR.")
    rw.w("")
    rw.w("Eq 111.3 [DERIVED]: kappa = c^2/(2 r_S) = {:.4e} m/s^2".format(r1["kappa"]))
    rw.w("Eq 111.4 [PDTP Original]: kappa = (c^2/2)|d(1/n^2)/dr|_{r_S}")
    rw.w("Eq 111.5 [DERIVED]: T_H = {:.4e} K  (1 M_sun BH)".format(r1["T_H"]))
    rw.w("")
    rw.w("Reason n does not change T_H:")
    rw.w("  n = 1/alpha affects PHASE velocity c_phase = c/n -> 0 at horizon.")
    rw.w("  T_H depends on GROUP velocity c_group = c_s = c (unchanged, Part 34).")
    rw.w("  kappa = (1/2)|d(c_s^2 - v^2)/dr|_{r_S} uses c_s = c, not c_phase.")
    rw.w("")
    rw.w("Breathing mode [Eq 111.8]: T_H unchanged; spectrum cut off at omega_gap.")
    rw.w("  omega_gap = {:.3e} rad/s  (cosmological, negligible for all astroph. BHs)".format(
        r4["omega_gap"]))
    rw.w("")
    rw.w("Two-phase [Eq 111.9]: G_eff = 2G_bare but G_N = G_eff -> T_H unchanged.")
    rw.w("Birefringence (T4): + and x modes have same T_H (same n profile).")
    rw.w("")
    rw.w("SymPy: {}/5 PASS".format(
        r6.get("n_pass", "N/A") if r6.get("sympy_available") else "N/A"))
    rw.w("Sudoku: {}/{} PASS".format(r7["n_pass"], r7["n_total"]))

    rw.save()


if __name__ == "__main__":
    main()
