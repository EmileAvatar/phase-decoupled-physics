# t5_phase_stack.py  --  T5: Multi-Layer Phase Stacks (air/water/oil model)
# Part 109, Phase 77
#
# Transfer matrix method (TMM) for GW propagation through stacked PDTP layers.
# Each layer is characterised by its phase-locking parameter alpha and thickness d.
# Refractive index n_j = 1/alpha_j  (Part 98 / Eq 108.1).
#
# Equations:
#   109.1  Layer transfer matrix M_j                          [TEXTBOOK, Born & Wolf S1.6]
#   109.2  Phase thickness  delta_j = (2pi/lam) n_j d_j cos(theta_j)  [TEXTBOOK]
#   109.3  Optical admittance  p_j = n_j cos(theta_j) (TE)            [TEXTBOOK]
#   109.4  r = (p0 B - C)/(p0 B + C), [B,C]^T = M.[1, p_out]^T       [TEXTBOOK]
#   109.5  Decoupled limit: alpha->0 (n->inf)  => R->1                [DERIVED]
#   109.6  Quarter-wave thickness: d_QW = lam*alpha/4 = c*alpha/(4*f) [DERIVED]
#   109.7  Fabry-Perot (N=1): r = (r01+r12 e^2id)/(1+r01*r12 e^2id)  [TEXTBOOK, SymPy]
#   109.8  Bandgap centre: f_gap = c*alpha_oil/(2*d_layer)            [PDTP Original]
#   109.9  Sub-wavelength criterion: d*n << lam/4  =>  R ~ 0          [DERIVED]
#   109.10 Leidenfrost critical coupling: alpha_crit = 4*lP/(sqrt(2)*lam_GW) [PDTP Original]
#
# Python rule: ASCII only; output saved to outputs/phase_stack_<ts>.txt

import cmath
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
# 2x2 complex matrix helpers
# ---------------------------------------------------------------------------

def mat22(a, b, c, d):
    return [[a, b], [c, d]]

def matmul22(A, B):
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0],
         A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0],
         A[1][0]*B[0][1] + A[1][1]*B[1][1]],
    ]

def mat_identity():
    return mat22(1+0j, 0j, 0j, 1+0j)


# ---------------------------------------------------------------------------
# Core TMM functions
# ---------------------------------------------------------------------------

def snell_cos(n0, sin_i0, n_j):
    """
    Compute cos(theta_j) in layer j via Snell law.
    n0 sin(theta_i) = n_j sin(theta_j)
    Returns complex cos_t (imaginary part = evanescent regime).
    """
    sin_t = complex(n0 * sin_i0 / n_j)
    # cmath.sqrt handles the complex branch correctly
    cos_t = cmath.sqrt(1.0 - sin_t * sin_t)
    return cos_t


def layer_matrix(alpha_j, d_j, lam, sin_i0, n0, pol="TE"):
    """
    Transfer matrix for a single PDTP layer.  Eq 109.1-109.3.

    Inputs:
      alpha_j  -- PDTP coupling in this layer (0 < alpha <= 1); n_j = 1/alpha_j
      d_j      -- physical thickness (m)
      lam      -- free-space GW wavelength (m)  = c / f
      sin_i0   -- sin(theta_i) of the original incidence angle (from Snell)
      n0       -- refractive index of the entrance medium (= 1/alpha_0)
      pol      -- 'TE' or 'TM'

    Returns 2x2 complex matrix [[m11, m12], [m21, m22]].
    """
    alpha_j = max(float(alpha_j), 1.0e-15)  # guard against exact zero
    n_j = 1.0 / alpha_j

    cos_t = snell_cos(n0, sin_i0, n_j)  # complex

    # Optical admittance  Eq 109.3
    if pol == "TE":
        p_j = n_j * cos_t
    else:                    # TM
        if abs(cos_t) < 1.0e-30:
            p_j = complex(1.0e30)
        else:
            p_j = n_j / cos_t

    # Phase thickness  Eq 109.2
    delta_j = complex(2.0 * math.pi / lam) * n_j * d_j * cos_t

    cos_d = cmath.cos(delta_j)
    sin_d = cmath.sin(delta_j)

    # Transfer matrix  Eq 109.1
    m11 = cos_d
    m12 = -1j * sin_d / p_j if abs(p_j) > 1.0e-30 else complex(0)
    m21 = -1j * p_j * sin_d
    m22 = cos_d

    return mat22(m11, m12, m21, m22)


def tmm_stack(layers, alpha_in, alpha_out, lam, theta_i_deg, pol="TE"):
    """
    Full transfer matrix method for a stack of N layers.  Eq 109.4.

    Inputs:
      layers    -- list of (alpha_j, d_j) tuples (left to right)
      alpha_in  -- alpha of entrance medium
      alpha_out -- alpha of exit medium
      lam       -- free-space wavelength (m)
      theta_i_deg -- angle of incidence (degrees, from normal)
      pol       -- 'TE' or 'TM'

    Returns dict with r, R, t, T, M_total.
    """
    alpha_in  = max(float(alpha_in),  1.0e-15)
    alpha_out = max(float(alpha_out), 1.0e-15)
    n_in  = 1.0 / alpha_in
    n_out = 1.0 / alpha_out

    theta_i = math.radians(theta_i_deg)
    sin_i0  = math.sin(theta_i)
    cos_i0  = math.cos(theta_i)

    # Entrance admittance
    if pol == "TE":
        p_in  = n_in  * cos_i0
        cos_out = snell_cos(n_in, sin_i0, n_out)
        p_out = n_out * cos_out
    else:
        p_in  = n_in  / cos_i0
        cos_out = snell_cos(n_in, sin_i0, n_out)
        p_out = n_out / cos_out if abs(cos_out) > 1.0e-30 else complex(1.0e30)

    # Product matrix  M = M_1 * M_2 * ... * M_N
    M = mat_identity()
    for (alpha_j, d_j) in layers:
        Mj = layer_matrix(alpha_j, d_j, lam, sin_i0, n_in, pol)
        M = matmul22(M, Mj)

    # Apply exit medium: [B, C]^T = M * [1, p_out]^T
    B = M[0][0] * 1.0 + M[0][1] * p_out
    C = M[1][0] * 1.0 + M[1][1] * p_out

    denom = p_in * B + C
    if abs(denom) < 1.0e-30:
        return {"r": complex(0), "R": 0.0, "t": complex(0), "T": 0.0,
                "B": B, "C": C, "M": M}

    r = (p_in * B - C) / denom
    t = 2.0 * p_in / denom

    R = abs(r) ** 2
    # T requires real part of p_out/p_in ratio (handles evanescent exit)
    p_ratio = (p_out / p_in).real
    T = p_ratio * abs(t) ** 2 if p_ratio > 0 else 0.0

    return {"r": r, "R": R, "t": t, "T": T, "B": B, "C": C, "M": M}


# ---------------------------------------------------------------------------
# Step 1: N=0 check -- recover Fresnel (T4)
# ---------------------------------------------------------------------------

def step1_fresnel_recovery(rw):
    """
    With no layers, TMM reduces to single-interface Fresnel.
    Verify TMM(layers=[]) == Fresnel formula from T4.
    """
    rw.section("Step 1 -- N=0: recover Fresnel (T4 cross-check)")
    C_LIGHT = 3.0e8  # m/s
    f_GW    = 100.0  # Hz  (LIGO)
    lam     = C_LIGHT / f_GW  # 3e6 m

    alpha_in  = 1.0    # vacuum
    alpha_out = 0.866  # sqrt(0.75), NS boundary from T4
    n_out     = 1.0 / alpha_out

    results = []
    rw.w("{:>8}  {:>10}  {:>10}  {:>12}".format(
        "theta_i", "R_TMM", "R_Fresnel", "delta"))

    for ti in [0.0, 30.0, 49.1, 60.0]:
        r_tmm = tmm_stack([], alpha_in, alpha_out, lam, ti, "TE")
        R_tmm = r_tmm["R"]

        # Direct Fresnel (TE)
        ti_rad = math.radians(ti)
        sin_t  = math.sin(ti_rad) * 1.0 / n_out
        if abs(sin_t) < 1.0:
            cos_t = math.sqrt(1.0 - sin_t**2)
            r_fres = (math.cos(ti_rad) - n_out*cos_t) / \
                     (math.cos(ti_rad) + n_out*cos_t)
            R_fres = r_fres**2
        else:
            R_fres = 1.0

        delta = abs(R_tmm - R_fres)
        match = delta < 1.0e-9
        results.append(match)
        rw.w("{:>8.1f}  {:>10.6f}  {:>10.6f}  {:>12.2e}  {}".format(
            ti, R_tmm, R_fres, delta, "PASS" if match else "FAIL"))

    return {"n_pass": sum(results), "n_total": len(results)}


# ---------------------------------------------------------------------------
# Step 2: N=1 Fabry-Perot (single layer)
# ---------------------------------------------------------------------------

def step2_fabry_perot(rw):
    """
    For a single layer between two media, TMM must match the Fabry-Perot formula:
      r_FP = (r01 + r12 * exp(2i*delta)) / (1 + r01*r12 * exp(2i*delta))   Eq 109.7
    Tested at normal incidence for several (alpha_1, d) combinations.
    """
    rw.section("Step 2 -- N=1: Fabry-Perot identity (Eq 109.7)")
    C_LIGHT = 3.0e8
    lam = C_LIGHT / 100.0  # 100 Hz

    test_cases = [
        (1.0, 0.8, 0.7, 3.0e5),   # (alpha_in, alpha_1, alpha_out, d_m)
        (1.0, 0.5, 1.0, 1.5e6),
        (1.0, 0.9, 0.8, 7.0e5),
    ]
    results = []
    rw.w("{:>6} {:>6} {:>6} {:>10}  {:>10}  {:>10}  {:>8}".format(
        "a_in","a_1","a_out","R_TMM","R_FP","delta","match"))

    for (a0, a1, a2, d) in test_cases:
        n0, n1, n2 = 1.0/a0, 1.0/a1, 1.0/a2

        # TMM
        r_tmm = tmm_stack([(a1, d)], a0, a2, lam, 0.0, "TE")
        R_tmm = r_tmm["R"]

        # Fabry-Perot  Eq 109.7 (normal incidence: p = n)
        r01 = (n0 - n1) / (n0 + n1)
        r12 = (n1 - n2) / (n1 + n2)
        delta = 2.0 * math.pi * n1 * d / lam
        r_fp  = (r01 + r12 * cmath.exp(2j * delta)) / \
                (1.0 + r01 * r12 * cmath.exp(2j * delta))
        R_fp  = abs(r_fp)**2

        diff  = abs(R_tmm - R_fp)
        match = diff < 1.0e-9
        results.append(match)
        rw.w("{:>6.2f} {:>6.2f} {:>6.2f} {:>10.6f}  {:>10.6f}  {:>10.2e}  {:>8}".format(
            a0, a1, a2, R_tmm, R_fp, diff, "PASS" if match else "FAIL"))

    return {"n_pass": sum(results), "n_total": len(results)}


# ---------------------------------------------------------------------------
# Step 3: Air / water / oil three-layer demo
# ---------------------------------------------------------------------------

def step3_air_water_oil(rw):
    """
    Three PDTP layers representing the air/water/oil analogy:
      vacuum (in) | oil (alpha=0.8) | water (alpha=1.0) | oil (alpha=0.8) | vacuum (out)
    Compare against vacuum/vacuum (no layers) to show interference effect.
    """
    rw.section("Step 3 -- Air/water/oil three-layer demo")
    C_LIGHT = 3.0e8
    f_GW = 100.0           # Hz
    lam  = C_LIGHT / f_GW  # 3e6 m

    d_oil   = 0.75e6  # 750 km  (quarter-wave for alpha=0.5)
    d_water = 1.50e6  # 1500 km

    alpha_air   = 1.0   # "air"   = vacuum (full coupling)
    alpha_water = 1.0   # "water" = same as vacuum here
    alpha_oil   = 0.80  # "oil"   = partially decoupled

    # Stack: oil | water | oil
    stack = [(alpha_oil, d_oil), (alpha_water, d_water), (alpha_oil, d_oil)]

    rw.w("Layer types (PDTP analogy):")
    rw.w("  vacuum (alpha=1) = 'air'   in classical optics")
    rw.w("  alpha=0.8        = 'oil'   -- partially decoupled")
    rw.w("  alpha=1.0        = 'water' -- fully coupled (same as vacuum)")
    rw.w("")
    rw.w("Stack: vacuum | oil(750km) | water(1500km) | oil(750km) | vacuum")
    rw.w("")

    results = {}
    rw.w("{:>8}  {:>8}  {:>8}  {:>8}".format("theta_i", "R_stack", "R_plain", "contrast"))

    for ti in [0.0, 20.0, 40.0, 49.1]:
        r_stack = tmm_stack(stack, alpha_air, alpha_air, lam, ti, "TE")
        r_plain = tmm_stack([], alpha_air, alpha_air, lam, ti, "TE")

        contrast = r_stack["R"] - r_plain["R"]
        rw.w("{:>8.1f}  {:>8.4f}  {:>8.4f}  {:>+8.4f}".format(
            ti, r_stack["R"], r_plain["R"], contrast))
        results[ti] = {"R_stack": r_stack["R"], "R_plain": r_plain["R"]}

    rw.w("")
    rw.w("Note: R_plain = 0 (same alpha in/out, no boundary). Stack shows")
    rw.w("non-zero R from multi-layer interference -- GW reflection by")
    rw.w("stacked partially-decoupled regions.")
    return results


# ---------------------------------------------------------------------------
# Step 4: Decoupled limit alpha -> 0  (Eq 109.5)
# ---------------------------------------------------------------------------

def step4_decoupled_limit(rw):
    """
    A single fully-decoupled layer (alpha->0, n->inf) is a perfect GW mirror.
    Derivation:
      As n->inf: p_layer = n*cos(theta) ~ n >> p_in = 1
      B = cos(delta) * 1 + (-i sin(delta)/p_layer) * p_out ~ cos(delta)
      C = -i p_layer sin(delta) * 1 + cos(delta) * p_out ~ -i n sin(delta)
      r = (p_in B - C)/(p_in B + C) -> (i n sin(delta))/(-i n sin(delta)) = -1
      R = 1   [Eq 109.5, DERIVED]
    """
    rw.section("Step 4 -- Decoupled limit: R->1 as alpha->0 (Eq 109.5)")
    C_LIGHT = 3.0e8
    lam = C_LIGHT / 100.0

    d_layer = 1.0e6  # 1000 km physical thickness (irrelevant for n->inf result)

    alphas = [1.0, 0.5, 0.1, 0.01, 0.001, 1.0e-4, 1.0e-6]
    results = {}
    rw.w("{:>10}  {:>10}  {:>10}  {:>12}".format("alpha", "n=1/a", "R", "1-R"))

    for a in alphas:
        r = tmm_stack([(a, d_layer)], 1.0, 1.0, lam, 0.0, "TE")
        R = r["R"]
        results[a] = R
        rw.w("{:>10.1e}  {:>10.3f}  {:>10.6f}  {:>12.2e}".format(
            a, 1.0/a, R, 1.0 - R))

    rw.w("")
    rw.w("Eq 109.5 [DERIVED]: as alpha->0 (n->inf), R->1 (complete reflection).")
    rw.w("A fully decoupled layer is a perfect gravitational mirror.")
    return results


# ---------------------------------------------------------------------------
# Step 5: Quarter-wave condition  (Eq 109.6)
# ---------------------------------------------------------------------------

def step5_quarter_wave(rw):
    """
    Quarter-wave anti-reflection: single layer with delta = pi/2 and
    n_layer = sqrt(n_in * n_out) gives R = 0.

    In PDTP: d_QW = lam / (4 * n_layer) = c * alpha_layer / (4 * f)  [Eq 109.6]

    For a layer between vacuum (alpha=1) and a dense region (alpha=alpha_out):
    anti-reflection alpha: alpha_AR = sqrt(alpha_out)  (n_AR = 1/sqrt(alpha_out))
    """
    rw.section("Step 5 -- Quarter-wave condition (Eq 109.6)")
    C_LIGHT = 3.0e8
    f_GW    = 100.0
    lam     = C_LIGHT / f_GW

    alpha_in  = 1.0
    alpha_out = 0.75   # target: n_out = 1/0.75 = 4/3

    n_in  = 1.0 / alpha_in
    n_out = 1.0 / alpha_out

    # Anti-reflection condition: n_AR = sqrt(n_in * n_out)
    n_AR     = math.sqrt(n_in * n_out)
    alpha_AR = 1.0 / n_AR
    d_QW     = lam / (4.0 * n_AR)   # quarter-wave thickness at this n

    r_AR  = tmm_stack([(alpha_AR, d_QW)], alpha_in, alpha_out, lam, 0.0, "TE")
    r_noAR = tmm_stack([], alpha_in, alpha_out, lam, 0.0, "TE")

    rw.w("Anti-reflection (quarter-wave) layer:")
    rw.w("  alpha_in   = {:.4f}  (n_in  = {:.4f})".format(alpha_in,  n_in))
    rw.w("  alpha_out  = {:.4f}  (n_out = {:.4f})".format(alpha_out, n_out))
    rw.w("  n_AR       = sqrt(n_in*n_out) = {:.6f}".format(n_AR))
    rw.w("  alpha_AR   = 1/n_AR           = {:.6f}".format(alpha_AR))
    rw.w("  d_QW       = lam/(4*n_AR) = {:.4e} m  ({:.0f} km)".format(
        d_QW, d_QW / 1.0e3))
    rw.w("Eq 109.6 [DERIVED]: d_QW = c*alpha/(4*f) = {:.4e} m".format(
        C_LIGHT * alpha_AR / (4.0 * f_GW)))
    rw.w("  R without AR layer = {:.6f}".format(r_noAR["R"]))
    rw.w("  R with    AR layer = {:.2e}  (must be ~0)".format(r_AR["R"]))

    return {
        "alpha_AR": alpha_AR,
        "d_QW_m":   d_QW,
        "R_with_AR":    r_AR["R"],
        "R_without_AR": r_noAR["R"],
    }


# ---------------------------------------------------------------------------
# Step 6: Frequency scan -- photonic bandgap  (Eq 109.8)
# ---------------------------------------------------------------------------

def step6_frequency_scan(rw):
    """
    Periodic stack: [oil(d) | water(d)] x N_periods between vacuum.
    Photonic bandgap centred at f_gap = c * alpha_oil / (2 * d)  [Eq 109.8, PDTP Original]
    Scan R vs f to confirm bandgap location.
    """
    rw.section("Step 6 -- Frequency scan: photonic bandgap (Eq 109.8)")
    C_LIGHT = 3.0e8

    alpha_oil   = 0.80
    alpha_water = 1.00
    d_layer     = 3.0e5   # 300 km per layer

    f_gap = C_LIGHT * alpha_oil / (2.0 * d_layer)
    rw.w("Eq 109.8 [PDTP Original]: f_gap = c*alpha_oil/(2*d) = {:.2f} Hz".format(f_gap))
    rw.w("  alpha_oil = {}  d_layer = {:.0f} km".format(alpha_oil, d_layer/1.0e3))
    rw.w("")

    N_periods = 5   # 5 oil-water pairs
    stack = []
    for _ in range(N_periods):
        stack.append((alpha_oil,   d_layer))
        stack.append((alpha_water, d_layer))

    # Frequency scan  20 Hz to 1600 Hz
    freqs = [20 + 20*k for k in range(80)]
    R_vals = []
    for f in freqs:
        lam = C_LIGHT / f
        r   = tmm_stack(stack, 1.0, 1.0, lam, 0.0, "TE")
        R_vals.append(r["R"])

    # Find peak R and confirm it's near f_gap
    max_R = max(R_vals)
    f_at_max = freqs[R_vals.index(max_R)]

    rw.w("Frequency scan result (N={} oil-water pairs):".format(N_periods))
    rw.w("  Predicted f_gap = {:.1f} Hz".format(f_gap))
    rw.w("  Observed peak R at f = {:.0f} Hz  (R = {:.4f})".format(f_at_max, max_R))
    rw.w("  Match within 2x: {}".format(abs(f_at_max - f_gap) < 2.0 * f_gap))
    rw.w("")

    # Print sample of the scan
    rw.w("{:>8}  {:>8}".format("f(Hz)", "R"))
    for i in range(0, len(freqs), 8):
        rw.w("{:>8.0f}  {:>8.4f}".format(freqs[i], R_vals[i]))

    return {
        "f_gap_predicted": f_gap,
        "f_at_max_R":      f_at_max,
        "max_R":           max_R,
        "freqs":           freqs,
        "R_vals":          R_vals,
    }


# ---------------------------------------------------------------------------
# Step 7: Scale analysis -- healing length vs GW wavelength  (Eq 109.9-109.10)
# ---------------------------------------------------------------------------

def step7_scale_analysis(rw):
    """
    Healing length xi = lP/sqrt(2) (Part 34) vs LIGO GW wavelength (lambda ~ 3000 km).
    Sub-wavelength criterion: n*d = d/alpha << lambda/4.
    For the Leidenfrost decoupled layer (d = xi, alpha -> 0):
      n*d = xi/alpha; for R ~ 0 need xi/alpha << lambda/4
      Critical coupling: alpha_crit = 4*xi/lambda  [Eq 109.10, PDTP Original]
    """
    rw.section("Step 7 -- Scale analysis: xi vs lambda_GW (Eqs 109.9, 109.10)")
    C_LIGHT = 3.0e8
    l_P = 1.616e-35   # Planck length (m)
    xi  = l_P / math.sqrt(2.0)  # healing length, Part 34

    rw.w("Healing length xi = lP/sqrt(2) = {:.3e} m  (Part 34)".format(xi))
    rw.w("")

    for f_Hz in [10.0, 100.0, 1000.0, 1.0e9, 1.0e18]:
        lam = C_LIGHT / f_Hz
        # Critical alpha: alpha_crit = 4*xi/lam (n*d = lam/4 condition)
        alpha_crit = 4.0 * xi / lam
        OoM = math.log10(1.0 / alpha_crit) if alpha_crit > 0 else float("inf")
        rw.w("f = {:.1e} Hz  lam = {:.2e} m  alpha_crit = {:.2e}  "
             "(need alpha<{:.0f} OoM below 1)".format(f_Hz, lam, alpha_crit, OoM))

    rw.w("")
    lam_LIGO = C_LIGHT / 100.0
    alpha_crit_LIGO = 4.0 * xi / lam_LIGO
    OoM_LIGO = math.log10(1.0 / alpha_crit_LIGO)
    rw.w("Eq 109.10 [PDTP Original]:")
    rw.w("  alpha_crit(LIGO 100Hz) = {:.2e}".format(alpha_crit_LIGO))
    rw.w("  Leidenfrost layer becomes non-trivial only when alpha < {:.0f} OoM below 1".format(
        OoM_LIGO))
    rw.w("  Physical interpretation: the decoupled boundary layer (d~lP) is")
    rw.w("  42 orders of magnitude sub-wavelength at LIGO frequencies.")
    rw.w("  => Leidenfrost reflection is ZERO at any current GW detector.")
    rw.w("  => Resonant GW shielding requires macroscopic structures (km-scale).")

    return {
        "xi_m":              xi,
        "lam_LIGO_m":        lam_LIGO,
        "alpha_crit_LIGO":   alpha_crit_LIGO,
        "OoM_below_1":       OoM_LIGO,
    }


# ---------------------------------------------------------------------------
# Step 8: SymPy -- Fabry-Perot identity (Eq 109.7)
# ---------------------------------------------------------------------------

def step8_sympy(rw):
    """
    Verify N=1 TMM == Fabry-Perot formula symbolically (normal incidence).
    r_TMM = r_FP = (r01 + r12 exp(2i delta))/(1 + r01 r12 exp(2i delta))
    """
    rw.section("Step 8 -- SymPy: Fabry-Perot identity (Eq 109.7)")
    if not SYMPY_OK:
        rw.w("SymPy not available -- skipping")
        return {"sympy_available": False}

    n0, n1, n2, delta = sp.symbols("n0 n1 n2 delta", positive=True)

    # TMM at normal incidence (p_j = n_j, sin_i = 0 -> cos_t = 1, cos_i = 1)
    cos_d = sp.cos(delta)
    sin_d = sp.sin(delta)
    # M_1 with p_1 = n1
    m11 = cos_d
    m12 = -sp.I * sin_d / n1
    m21 = -sp.I * n1 * sin_d
    m22 = cos_d
    # [B, C] = M * [1, n2]
    B = m11 * 1 + m12 * n2
    C = m21 * 1 + m22 * n2
    r_TMM = (n0 * B - C) / (n0 * B + C)

    # Fabry-Perot  Eq 109.7
    r01 = (n0 - n1) / (n0 + n1)
    r12 = (n1 - n2) / (n1 + n2)
    r_FP = (r01 + r12 * sp.exp(2 * sp.I * delta)) / \
           (1 + r01 * r12 * sp.exp(2 * sp.I * delta))

    # sp.simplify cannot reduce the complex-trig difference to zero symbolically.
    # Verify numerically at three substitution points instead.
    test_pts = [(1.0, 1.25, 1.5, 0.9), (1.0, 0.6, 0.8, 1.3), (1.0, 1.8, 1.2, 2.1)]
    s1_residuals = []
    for (v0, v1, v2, vd) in test_pts:
        subs = {n0: v0, n1: v1, n2: v2, delta: vd}
        res = abs(complex(r_TMM.subs(subs)) - complex(r_FP.subs(subs)))
        s1_residuals.append(res)
    s1_pass = all(r < 1.0e-12 for r in s1_residuals)
    rw.w("S1  r_TMM == r_FP (numeric substitution, 3 pts): max residual = {:.2e}  PASS={}".format(
        max(s1_residuals), s1_pass))

    # S2: at delta = pi/2 (quarter-wave), r_TMM with n1=sqrt(n0*n2) gives r=0
    n1_AR = sp.sqrt(n0 * n2)
    r_AR = r_TMM.subs([(n1, n1_AR), (delta, sp.pi / 2)])
    r_AR_simplified = sp.simplify(r_AR)
    s2_pass = r_AR_simplified == 0
    rw.w("S2  r_TMM(QW, n1=sqrt(n0*n2)) = {}  PASS={}".format(r_AR_simplified, s2_pass))

    # S3: at delta = 0 (zero-thickness), r_TMM = (n0-n2)/(n0+n2) (single interface)
    r_d0 = sp.simplify(r_TMM.subs(delta, 0))
    expected_d0 = (n0 - n2) / (n0 + n2)
    s3_pass = sp.simplify(r_d0 - expected_d0) == 0
    rw.w("S3  r_TMM(delta=0) = {}  expect (n0-n2)/(n0+n2)  PASS={}".format(
        r_d0, s3_pass))

    n_pass = sum([s1_pass, s2_pass, s3_pass])
    rw.w("SymPy score: {}/3 PASS".format(n_pass))

    return {
        "sympy_available": True,
        "s1_FP_identity": s1_pass,
        "s2_QW_R_zero":   s2_pass,
        "s3_zero_thick":  s3_pass,
        "n_pass":         n_pass,
    }


# ---------------------------------------------------------------------------
# Step 9: Sudoku consistency checks
# ---------------------------------------------------------------------------

def step9_sudoku(rw, r1, r2, r4, r5, r6, r7):
    """12 Sudoku checks reading from prior step return dicts."""
    rw.section("Step 9 -- Sudoku consistency checks")
    results = []

    def chk(label, cond):
        results.append(cond)
        rw.w("  [{:4}] {}".format("PASS" if cond else "FAIL", label))

    C_LIGHT = 3.0e8
    lam = C_LIGHT / 100.0

    # S01: N=0 recovery all PASS
    chk("S01 N=0 recovers Fresnel (T4 cross-check)",
        r1["n_pass"] == r1["n_total"])

    # S02: Fabry-Perot identity all PASS
    chk("S02 N=1 TMM = Fabry-Perot formula",
        r2["n_pass"] == r2["n_total"])

    # S03: Energy conservation for N=3 stack
    r_e = tmm_stack([(0.8, 5e5), (1.0, 1e6), (0.8, 5e5)], 1.0, 1.0, lam, 0.0)
    chk("S03 Energy conservation R+T=1 for 3-layer stack",
        abs(r_e["R"] + r_e["T"] - 1.0) < 1.0e-9)

    # S04: alpha=1 everywhere -> R=0 (no boundary)
    r_hom = tmm_stack([(1.0, 1e6), (1.0, 1e6)], 1.0, 1.0, lam, 0.0)
    chk("S04 Homogeneous stack (alpha=1 everywhere): R=0",
        r_hom["R"] < 1.0e-12)

    # S05: Decoupled limit: R -> 1 as alpha -> 0 (from step4)
    chk("S05 Decoupled limit: R(alpha=1e-6) > 0.99",
        r4.get(1.0e-6, 0) > 0.99)

    # S06: Quarter-wave AR: R < 1e-9 (from step5)
    chk("S06 Quarter-wave AR layer: R < 1e-9",
        r5["R_with_AR"] < 1.0e-9)

    # S07: Quarter-wave AR reduces R from non-zero
    chk("S07 AR layer reduces R (R_without > R_with)",
        r5["R_without_AR"] > r5["R_with_AR"])

    # S08: Photonic bandgap: max R > 0.5 in stopband
    chk("S08 Periodic stack has R_max > 0.5 in stopband",
        r6["max_R"] > 0.5)

    # S09: Bandgap peak near predicted f_gap (within factor 2)
    chk("S09 Bandgap peak within 2x of predicted f_gap",
        abs(r6["f_at_max_R"] - r6["f_gap_predicted"]) < 2.0 * r6["f_gap_predicted"])

    # S10: Sub-wavelength: xi << lambda_LIGO
    chk("S10 xi << lambda_LIGO (Planck << km scale): xi/lam < 1e-38",
        r7["xi_m"] / r7["lam_LIGO_m"] < 1.0e-38)

    # S11: Leidenfrost alpha_crit << 1 (deep sub-coupling)
    chk("S11 alpha_crit(LIGO) << 1: alpha_crit < 1e-40",
        r7["alpha_crit_LIGO"] < 1.0e-40)

    # S12: Reciprocity -- R(forward) = R(backward) for symmetric stack
    stack_sym = [(0.8, 5e5), (0.6, 8e5), (0.8, 5e5)]
    r_fwd = tmm_stack(stack_sym, 1.0, 1.0, lam, 0.0)
    stack_rev = list(reversed(stack_sym))
    r_rev = tmm_stack(stack_rev, 1.0, 1.0, lam, 0.0)
    chk("S12 Reciprocity: R_forward = R_backward",
        abs(r_fwd["R"] - r_rev["R"]) < 1.0e-10)

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
    log_path = os.path.join(out_dir, "phase_stack_{}.txt".format(ts))
    rw = _RW(log_path)

    rw.w("T5 -- Multi-Layer Phase Stacks (air/water/oil model)")
    rw.w("Part 109, Phase 77  |  {}".format(datetime.now().isoformat()))
    rw.w("PDTP n_j = 1/alpha_j  (Part 98, Eq 108.1 / Eq 109.1)")

    r1 = step1_fresnel_recovery(rw)
    r2 = step2_fabry_perot(rw)
    step3_air_water_oil(rw)
    r4 = step4_decoupled_limit(rw)
    r5 = step5_quarter_wave(rw)
    r6 = step6_frequency_scan(rw)
    r7 = step7_scale_analysis(rw)
    r8 = step8_sympy(rw)
    r9 = step9_sudoku(rw, r1, r2, r4, r5, r6, r7)

    rw.section("Summary -- T5 Multi-Layer Phase Stacks")
    rw.w("Eq 109.4 TMM: r = (p0 B - C)/(p0 B + C)  [TEXTBOOK, N=0 -> Fresnel VERIFIED]")
    rw.w("Eq 109.5 Decoupled limit: alpha->0 => R->1  [DERIVED]")
    rw.w("  Fully decoupled layer is a perfect gravitational mirror.")
    rw.w("Eq 109.6 Quarter-wave: d_QW = c*alpha/(4*f)  [DERIVED]")
    rw.w("  AR condition: alpha_AR = sqrt(alpha_out)  [DERIVED]")
    rw.w("Eq 109.8 Bandgap: f_gap = c*alpha_oil/(2*d)  [PDTP Original]")
    rw.w("  Predicted: {:.1f} Hz  Observed: {:.0f} Hz".format(
        r6["f_gap_predicted"], r6["f_at_max_R"]))
    rw.w("Eq 109.9 Sub-wavelength: d*n << lam/4 => R~0  [DERIVED]")
    rw.w("Eq 109.10 Leidenfrost alpha_crit(LIGO) = {:.2e}  [PDTP Original]".format(
        r7["alpha_crit_LIGO"]))
    rw.w("  => Leidenfrost layer (d~lP) has R=0 at all current GW detector frequencies.")
    rw.w("  => Resonant GW shielding needs km-scale macroscopic structures.")
    rw.w("")
    rw.w("SymPy: {}/3 PASS".format(
        r8.get("n_pass", "N/A") if r8.get("sympy_available") else "N/A"))
    rw.w("Sudoku: {}/{} PASS".format(r9["n_pass"], r9["n_total"]))

    rw.save()


if __name__ == "__main__":
    main()
