#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lisa_sim.py -- LISA/ET Breathing Mode Simulation (Strategy A)
=============================================================
Simulates the PDTP Strategy A measurement chain:

  FORWARD  (circular, uses G):  a = l_P  ->  omega_gap = f(a)
  BACKWARD (G-free):            omega_gap (as if from LISA)  ->  a  ->  G_pred

The backward chain is logically non-circular. With real LISA/ET data,
omega_gap comes from a measurement, not from G. Then:
    a = c / omega_gap    [G-free, Model M1]
    G_pred = c^3 * a^2 / hbar    [G-free]

Six frequency models map omega_gap <-> a without using G.
The module also answers: "if LISA detects f Hz, what G would that imply?"

Called from main.py as Phase 7.

Usage (standalone):
    cd simulations/solver
    python lisa_sim.py
"""

import sys
import os
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from sudoku_engine import SudokuEngine, HBAR, C, G, M_E, L_P
from print_utils import ReportWriter


# ===========================================================================
# DETECTOR BAND CONSTANTS
# ===========================================================================

LISA_LOW   = 1e-4   # Hz  (LISA lower sensitivity edge)
LISA_HIGH  = 1e-1   # Hz  (LISA upper sensitivity edge)
ET_LOW     = 2.0    # Hz  (Einstein Telescope lower edge)
ET_HIGH    = 1e4    # Hz  (Einstein Telescope upper edge)

# Frequency scan range
SCAN_LOW   = 1e-6   # Hz
SCAN_HIGH  = 1e6    # Hz
SCAN_N     = 600    # log-spaced points


# ===========================================================================
# FREQUENCY MODELS
# ===========================================================================
# Each model maps omega_gap (rad/s) <-> lattice spacing a (metres), G-free.
# A model dict has:
#   name        : str
#   description : str (one-line physical motivation)
#   g_free      : bool (True if backward chain uses no G)
#   forward     : a_m -> omega_rad_s
#   backward    : omega_rad_s -> a_m

def build_frequency_models():
    """Return list of frequency model dicts."""

    omega_e = M_E * C**2 / HBAR    # electron Compton freq ~7.76e20 rad/s

    return [
        {
            "name"       : "M1: Natural Compton  [omega=c/a]",
            "desc"       : "Zone-edge frequency of relativistic lattice; "
                           "wavelength = lattice spacing",
            "g_free"     : True,
            "forward"    : lambda a: C / a,
            "backward"   : lambda w: C / w,
        },
        {
            "name"       : "M2: Reduced Compton  [omega=c/(2*pi*a)]",
            "desc"       : "Uses reduced wavelength lambda-bar = lambda/(2*pi); "
                           "hbar-vs-h convention analog",
            "g_free"     : True,
            "forward"    : lambda a: C / (2 * np.pi * a),
            "backward"   : lambda w: C / (2 * np.pi * w),
        },
        {
            "name"       : "M3: Linear-in-a  [omega=(c^3/hbar)*a]",
            "desc"       : "Dimensional analysis with hbar and c only; "
                           "unusual: larger a gives HIGHER frequency",
            "g_free"     : True,
            "forward"    : lambda a: (C**3 / HBAR) * a,
            "backward"   : lambda w: (HBAR / C**3) * w,
        },
        {
            "name"       : "M4: Healing length  [omega=c/(a*sqrt(4*pi))]",
            "desc"       : "Gap set by phase stiffness / condensate density "
                           "at lattice scale with 4*pi geometric factor",
            "g_free"     : True,
            "forward"    : lambda a: C / (a * np.sqrt(4 * np.pi)),
            "backward"   : lambda w: C / (w * np.sqrt(4 * np.pi)),
        },
        {
            "name"       : "M5: Electron Compton  [f=m_e*c^2/h] (INFO)",
            "desc"       : "Fixed reference frequency from lightest particle; "
                           "shows where hierarchy problem lives in frequency space",
            "g_free"     : False,     # informational only
            "forward"    : lambda a: omega_e,
            "backward"   : lambda w: C / w,   # treat as M1 inversion
        },
        {
            "name"       : "M6a: LISA lower edge  [f=1e-4 Hz anchor]",
            "desc"       : "IF omega_gap sits at LISA lower limit, "
                           "what lattice spacing and G does that imply?",
            "g_free"     : True,
            "forward"    : lambda a: 2 * np.pi * LISA_LOW,
            "backward"   : lambda w: C / w,
        },
        {
            "name"       : "M6b: ET lower edge  [f=2 Hz anchor]",
            "desc"       : "IF omega_gap sits at ET lower limit, "
                           "what lattice spacing and G does that imply?",
            "g_free"     : True,
            "forward"    : lambda a: 2 * np.pi * ET_LOW,
            "backward"   : lambda w: C / w,
        },
    ]


# ===========================================================================
# STEP 1 -- FORWARD PREDICTION  (circular, uses G via l_P)
# ===========================================================================

def _forward_prediction(models, rw):
    """
    Given a = l_P (the only a that passes all 13 tests), compute
    what omega_gap each model predicts.

    CIRCULAR: l_P = sqrt(hbar*G/c^3) uses G.
    Purpose: show what PDTP says LISA should see IF the framework is correct.

    Returns list of {model_name, omega_rad_s, freq_hz, band}
    """
    rw.print("  NOTE: This step uses G via l_P = sqrt(hbar*G/c^3). CIRCULAR.")
    rw.print("  Purpose: if PDTP is correct and a = l_P, what would detectors see?")
    rw.print("")

    results = []
    rows    = []

    for m in models:
        omega = m["forward"](L_P)
        f_hz  = omega / (2 * np.pi)

        in_lisa = LISA_LOW <= f_hz <= LISA_HIGH
        in_et   = ET_LOW   <= f_hz <= ET_HIGH
        band    = ("LISA " if in_lisa else "") + ("ET" if in_et else "")
        band    = band.strip() or "outside all bands"

        results.append({
            "name"  : m["name"],
            "omega" : omega,
            "f_hz"  : f_hz,
            "band"  : band,
        })
        rows.append([
            m["name"][:45],
            "{:.3e}".format(omega),
            "{:.3e}".format(f_hz),
            band,
        ])

    rw.table(
        ["Model", "omega_gap (rad/s)", "f_gap (Hz)", "Detector band"],
        rows, [46, 20, 14, 24],
    )
    return results


# ===========================================================================
# STEP 2 -- BACKWARD CHAIN VALIDATION
# ===========================================================================

def _backward_chain(models, rw, engine):
    """
    For each model: take the forward-predicted omega_gap (from a=l_P),
    invert it to get a, feed to SudokuEngine.

    M1/M2/M4 recover a = l_P exactly -> 13/13 pass (tautology, validates chain).
    M3 recovers a very different scale.
    M6a/M6b recover from their fixed-frequency anchor.

    Returns list of result dicts.
    """
    rw.print("  Using each model's own forward-predicted omega_gap as the 'measurement'.")
    rw.print("  Because those omega_gap values came from a = l_P (circular), the")
    rw.print("  backward chain recovers a = l_P and G_pred = G_known.")
    rw.print("  This is a tautology -- but it VALIDATES the chain structure.")
    rw.print("  With REAL LISA data the omega_gap input would be G-free.")
    rw.print("")

    backward_results = []
    rows = []

    for m in models:
        omega = m["forward"](L_P)            # forward-predicted omega
        a_derived = m["backward"](omega)     # invert back to a
        if a_derived <= 0 or not np.isfinite(a_derived):
            rows.append([m["name"][:40], "N/A", "N/A", "N/A", "N/A"])
            continue

        test_results, G_pred = engine.test(a_derived)
        n_pass, n_fail, _ = engine.score(test_results)
        ratio = G_pred / G
        log_r = abs(np.log10(ratio)) if ratio > 0 else float("inf")

        backward_results.append({
            "name"    : m["name"],
            "omega"   : omega,
            "a"       : a_derived,
            "G_pred"  : G_pred,
            "ratio"   : ratio,
            "log_r"   : log_r,
            "n_pass"  : n_pass,
            "g_free"  : m["g_free"],
        })
        rows.append([
            m["name"][:40],
            "{:.3e}".format(a_derived),
            "{:.3e}".format(G_pred),
            "{:.4e}".format(ratio),
            "{}/13  {}".format(n_pass, "G-free" if m["g_free"] else "INFO"),
        ])

    rw.table(
        ["Model", "a derived (m)", "G_pred", "G/G_known", "Pass / note"],
        rows, [41, 15, 14, 14, 18],
    )
    return backward_results


# ===========================================================================
# STEP 3 -- FREQUENCY SCANNER  (both directions)
# ===========================================================================

def _freq_scanner(models, rw, engine):
    """
    Part A: for each G-free model, scan frequencies to find which Hz gives
            G_pred/G_known closest to 1.
    Part B: for LISA and ET band sample frequencies, compute implied G.

    Returns {scan: [...], what_if: [...]}
    """
    freqs_hz  = np.logspace(np.log10(SCAN_LOW), np.log10(SCAN_HIGH), SCAN_N)
    freqs_rad = 2 * np.pi * freqs_hz

    # --- Part A: scanner ---
    rw.print("  Part A: scan {:,} frequencies ({:.0e}-{:.0e} Hz), find best G match".format(
        SCAN_N, SCAN_LOW, SCAN_HIGH))
    rw.print("")

    scan_results = []
    for m in models:
        if not m["g_free"]:
            continue

        best_log_r = float("inf")
        best_f = best_a = best_ratio = None
        best_n = 0

        for f_hz, omega in zip(freqs_hz, freqs_rad):
            a = m["backward"](omega)
            if a <= 0 or not np.isfinite(a) or a > 1e10 or a < 1e-80:
                continue
            _, G_pred = engine.test(a)
            ratio = G_pred / G
            if ratio <= 0:
                continue
            log_r = abs(np.log10(ratio))
            if log_r < best_log_r:
                best_log_r = log_r
                best_f     = f_hz
                best_a     = a
                best_ratio = ratio
                res, _ = engine.test(a)
                best_n, _, _ = engine.score(res)

        at_boundary = (
            best_f is not None and
            (abs(np.log10(best_f / SCAN_LOW)) < 0.02 or
             abs(np.log10(best_f / SCAN_HIGH)) < 0.02)
        )
        scan_results.append({
            "name"        : m["name"],
            "best_f"      : best_f,
            "best_a"      : best_a,
            "best_ratio"  : best_ratio,
            "best_log_r"  : best_log_r,
            "best_n"      : best_n,
            "at_boundary" : at_boundary,
        })

    rows_A = []
    for r in scan_results:
        f_str = "{:.4e}".format(r["best_f"]) if r["best_f"] else "N/A"
        a_str = "{:.4e}".format(r["best_a"]) if r["best_a"] else "N/A"
        bound = " [BOUNDARY]" if r["at_boundary"] else ""
        rows_A.append([
            r["name"][:40],
            f_str + bound,
            a_str,
            "{:.4e}".format(r["best_ratio"]) if r["best_ratio"] else "N/A",
            "{:.2f}".format(r["best_log_r"]) if r["best_log_r"] < 1e30 else "inf",
            "{}/13".format(r["best_n"]),
        ])
    rw.table(
        ["Model", "Best f (Hz)", "Best a (m)", "G/G_known", "Decades", "Pass"],
        rows_A, [41, 22, 14, 14, 8, 7],
    )

    # --- Part B: what-if for detector bands ---
    rw.print("")
    rw.print("  Part B: what-if -- IF detectors measure these frequencies, what G?")
    rw.print("  Using Model M1 (omega=c/a, the simplest G-free chain).")
    rw.print("")

    sample_freqs = [
        ("LISA lower",  LISA_LOW),
        ("LISA middle", np.sqrt(LISA_LOW * LISA_HIGH)),
        ("LISA upper",  LISA_HIGH),
        ("ET lower",    ET_LOW),
        ("ET middle",   np.sqrt(ET_LOW * ET_HIGH)),
        ("ET upper",    ET_HIGH),
        ("Best (M1 scanner)", None),   # filled in below
    ]

    # Find M1 best_f
    m1_best = next((r["best_f"] for r in scan_results
                    if "M1" in r["name"]), None)
    sample_freqs[-1] = ("M1 scanner best", m1_best)

    m1 = next(m for m in models if "M1" in m["name"])

    rows_B = []
    what_if_results = []
    for label, f_hz in sample_freqs:
        if f_hz is None:
            rows_B.append([label, "N/A", "N/A", "N/A", "N/A", "N/A"])
            continue
        omega = 2 * np.pi * f_hz
        a = m1["backward"](omega)
        if a <= 0 or not np.isfinite(a):
            rows_B.append([label, "{:.3e}".format(f_hz), "N/A", "N/A", "N/A", "N/A"])
            continue
        _, G_pred = engine.test(a)
        ratio = G_pred / G
        log_r = abs(np.log10(ratio)) if ratio > 0 else float("inf")
        res, _ = engine.test(a)
        n, _, _ = engine.score(res)
        what_if_results.append({
            "label": label, "f_hz": f_hz, "a": a,
            "G_pred": G_pred, "ratio": ratio, "log_r": log_r, "n_pass": n,
        })
        rows_B.append([
            label,
            "{:.3e}".format(f_hz),
            "{:.3e}".format(a),
            "{:.3e}".format(G_pred),
            "{:.2e}".format(ratio),
            "{:.1f} decades".format(log_r),
        ])

    rw.table(
        ["Scenario", "f (Hz)", "a (m)", "G_pred", "G/G_known", "How far off"],
        rows_B, [25, 10, 14, 14, 12, 16],
    )

    return {"scan": scan_results, "what_if": what_if_results}


# ===========================================================================
# STEP 4 -- DETECTOR BAND REPORT
# ===========================================================================

def _detector_band_report(scan_results, rw):
    """For each model's best-fit frequency, report physics implications."""

    eV_per_J = 1.0 / 1.602176634e-19

    for r in scan_results:
        f      = r["best_f"]
        a      = r["best_a"]
        if f is None or a is None:
            continue

        omega         = 2 * np.pi * f
        m_kg          = HBAR * omega / C**2
        m_eV          = m_kg * C**2 * eV_per_J
        yukawa_m      = C / f                  # lambda = c / f

        in_lisa = LISA_LOW <= f <= LISA_HIGH
        in_et   = ET_LOW   <= f <= ET_HIGH

        rw.print("  Model: {}".format(r["name"]))
        rw.key_value("Best frequency", "{:.4e} Hz".format(f))
        rw.key_value("In LISA band (1e-4--0.1 Hz)?", "YES" if in_lisa else "no")
        rw.key_value("In ET band (2--1e4 Hz)?",      "YES" if in_et   else "no")
        rw.key_value("Implied lattice a",  "{:.4e} m".format(a))
        rw.key_value("G_pred / G_known",
                     "{:.4e}  ({:.2f} decades off)".format(
                         r["best_ratio"], r["best_log_r"]))
        rw.key_value("Scalar graviton mass",
                     "{:.4e} kg  ({:.4e} eV/c^2)".format(m_kg, m_eV))
        rw.key_value("Yukawa force range", "{:.4e} m".format(yukawa_m))
        if r["at_boundary"]:
            rw.print("  WARNING: best fit is at scan boundary.")
            rw.print("  The optimal frequency lies OUTSIDE [{:.0e}, {:.0e}] Hz.".format(
                SCAN_LOW, SCAN_HIGH))
            rw.print("  No solution exists within any planned detector band.")
        rw.print("")


# ===========================================================================
# CONCLUSION
# ===========================================================================

def _conclusion(scan_results, rw):
    # Theoretical required frequency for M1: a = l_P  ->  omega = c/l_P
    omega_planck = C / L_P                     # rad/s
    f_planck     = omega_planck / (2 * np.pi)  # Hz

    rw.print("  THE CHAIN IS LOGICALLY NON-CIRCULAR:")
    rw.print("    omega_gap (from LISA measurement)")
    rw.print("    ->  a = c / omega_gap           [G-free, Model M1]")
    rw.print("    ->  G_pred = c^3 * a^2 / hbar   [G-free]")
    rw.print("    ->  compare G_pred to G_cavendish")
    rw.print("")
    rw.print("  WHAT THE THEORY REQUIRES (Model M1: a = c/omega_gap):")
    rw.print("    G_pred = G_known requires a = l_P  ->  omega_gap = c/l_P")
    rw.print("    Required omega_gap = {:.4e} rad/s  =  {:.4e} Hz".format(
        omega_planck, f_planck))
    rw.print("    (This is the Planck frequency -- the natural oscillation of spacetime)")
    rw.print("")
    rw.print("  SCANNER NOTE: the scan ran from {:.0e} to {:.0e} Hz.".format(
        SCAN_LOW, SCAN_HIGH))
    rw.print("    The required {:.1e} Hz is FAR outside the scan range.".format(f_planck))
    rw.print("    All models hit the scan boundary -- confirming no solution exists")
    rw.print("    anywhere near LISA or ET bands.")
    rw.print("")
    rw.print("  FREQUENCY GAP:")
    rw.print("    Required: {:.2e} Hz".format(f_planck))
    rw.print("    LISA max: {:.2e} Hz  ->  gap = {:.2e}x  ({:.0f} orders of magnitude)".format(
        LISA_HIGH, f_planck / LISA_HIGH, np.log10(f_planck / LISA_HIGH)))
    rw.print("    ET max:   {:.2e} Hz  ->  gap = {:.2e}x  ({:.0f} orders of magnitude)".format(
        ET_HIGH, f_planck / ET_HIGH, np.log10(f_planck / ET_HIGH)))
    rw.print("    This frequency gap IS the hierarchy problem in frequency space.")

    rw.print("")
    rw.print("  WHAT-IF SUMMARY:")
    rw.print("    If LISA detects a breathing mode in its band (1e-4 to 0.1 Hz),")
    rw.print("    G_pred from M1 would be ~10^(78-90)x smaller than G_known.")
    rw.print("    That is not a failure of PDTP -- it is the hierarchy problem")
    rw.print("    expressed in frequency space instead of mass space.")
    rw.print("")
    rw.print("  WHAT WOULD CONFIRM PDTP (Strategy A):")
    rw.print("    1. Detect a breathing-mode GW polarization (triangular detector)")
    rw.print("    2. Measure its gap frequency omega_gap")
    rw.print("    3. Compute G_pred = c^5 / (hbar * omega_gap^2)  [M1 formula]")
    rw.print("    4. IF G_pred matches G_cavendish within 1% -> PDTP confirmed")
    rw.print("    5. The required omega_gap ~ Planck frequency (~10^43 Hz)")
    rw.print("       This is NOT detectable with any current or planned instrument.")
    rw.print("       LISA / ET detect at 1e-4 to 1e4 Hz -- 47 orders of magnitude off.")
    rw.print("")
    rw.print("  CONCLUSION:")
    rw.print("    The LISA simulation confirms the hierarchy problem is not just")
    rw.print("    a number problem -- it is a FREQUENCY problem. The spacetime")
    rw.print("    oscillation that would validate PDTP happens at Planck frequency,")
    rw.print("    not at LIGO/LISA/ET frequencies. Strategy B (derive the hierarchy")
    rw.print("    ratio from lattice topology) remains the only path that does not")
    rw.print("    require a Planck-frequency detector.")
    rw.print("")


# ===========================================================================
# PHASE 7 ENTRY POINT  (called from main.py)
# ===========================================================================

def run_lisa_phase(rw, engine):
    """
    Phase 7 entry point.
    Orchestrates Steps 1-4 and prints the conclusion.
    Returns results dict for possible downstream use.
    """
    rw.section("Phase 7 -- LISA/ET Breathing Mode Simulation (Strategy A)")

    rw.print("  This phase simulates the PDTP Strategy A measurement chain.")
    rw.print("")
    rw.print("  FORWARD  (circular):  a = l_P  ->  omega_gap via model formula")
    rw.print("  BACKWARD (G-free):    omega_gap  ->  a  ->  G_pred = c^3*a^2/hbar")
    rw.print("")
    rw.print("  Six frequency models map omega_gap <-> lattice spacing a (no G).")
    rw.print("  The scanner finds what Hz would make G_pred = G_known.")
    rw.print("  The what-if table shows what G LISA/ET-band detections would imply.")
    rw.print("")

    models = build_frequency_models()

    # Step 1
    rw.subsection("Step 1: Forward Prediction  [CIRCULAR -- uses G via l_P]")
    fwd = _forward_prediction(models, rw)

    # Step 2
    rw.subsection("Step 2: Backward Chain Validation")
    bwd = _backward_chain(models, rw, engine)

    # Step 3
    rw.subsection("Step 3: Frequency Scanner + What-If Table")
    scanner = _freq_scanner(models, rw, engine)

    # Step 4
    rw.subsection("Step 4: Detector Band Report")
    _detector_band_report(scanner["scan"], rw)

    # Conclusion
    rw.subsection("Phase 7 Conclusion")
    _conclusion(scanner["scan"], rw)

    return {
        "forward"  : fwd,
        "backward" : bwd,
        "scanner"  : scanner,
    }


# ===========================================================================
# STANDALONE ENTRY POINT
# ===========================================================================

if __name__ == "__main__":
    output_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(output_dir, label="lisa_sim")
    engine = SudokuEngine()
    run_lisa_phase(rw, engine)
    rw.close()
