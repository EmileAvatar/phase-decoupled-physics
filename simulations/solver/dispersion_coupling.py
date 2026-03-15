#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dispersion_coupling.py -- Phase 19: Coupling Running as Condensate Dispersion (Idea E, Part 57)
================================================================================================
TASK (from TODO_02.md, Idea E):
  Reframe coupling constant running as condensate dispersion.
  Different excitation modes (spin-0, spin-1, spin-2) have different
  dispersion relations -> different effective couplings at different energies.
  GUT convergence = non-dispersive regime (all modes at same speed).

THE PHYSICS
-----------
In a BEC/superfluid, excitations have the Bogoliubov dispersion relation:

  omega^2 = c_s^2 * k^2 + (hbar*k^2 / (2*m))^2

  Source: Bogoliubov (1947); Pitaevskii & Stringari (2003) Ch. 7

  Two regimes:
  - Low k (k << 1/xi): omega ~ c_s * k  (phonon, linear, universal)
  - High k (k >> 1/xi): omega ~ hbar*k^2/(2m)  (free particle, quadratic)

  The transition scale is the healing length: xi = hbar / (m * c_s)

For PDTP (c_s = c, from Part 34), the condensate has THREE types of excitations:

  1. BREATHING MODE (spin-0, scalar):
     - Massive: omega^2 = c^2*k^2 + omega_gap^2
     - omega_gap = m_cond*c^2/hbar (Part 33)
     - This is the GRAVITY channel
     - Dispersion: v_g = c * sqrt(1 - (omega_gap/omega)^2)

  2. TRANSVERSE MODE (spin-2, tensor):
     - Massless in PDTP if angular forces give mu=kappa (Part 28)
     - omega = c * k (no gap)
     - These are gravitational waves (+ and x polarizations)

  3. GAUGE MODE (spin-1, vector):
     - From gauging U(1) or SU(3) symmetry
     - Massless (omega = c*k) for unbroken symmetries (EM, QCD gluons)
     - Massive after symmetry breaking (W, Z bosons): omega^2 = c^2*k^2 + m_W^2*c^4/hbar^2

THE PRISM ANALOGY
-----------------
White light enters a prism -> all colors travel at same speed (vacuum).
Inside the prism: different frequencies travel at different speeds (dispersion).
After the prism: colors are separated by angle.

GUT scale = "white light" (all couplings equal, no dispersion)
Low energy = "after the prism" (couplings have separated)

The question: does PDTP condensate dispersion reproduce the OBSERVED separation
pattern (alpha_G << alpha_EM << alpha_s)?

DISPERSION -> COUPLING CONNECTION
---------------------------------
In a medium, the effective coupling between excitations depends on
how well they propagate. A mode that is strongly dispersed (v_g << c)
couples more weakly over long distances. The effective coupling at
energy E for a mode with gap omega_gap is:

  alpha_eff(E) = alpha_0 * v_g(E) / c
              = alpha_0 * sqrt(1 - (E_gap/E)^2)     for E > E_gap
              = 0                                      for E < E_gap

This is speculative but physically motivated: a slower mode has less
"reach" and therefore couples more weakly at long range.

SUDOKU CHECKS (10 tests)
-------------------------
S1:  At GUT scale: all modes at v_g ~ c (couplings converge)
S2:  At low energy: gravity mode strongly dispersed (alpha_G << 1)
S3:  At low energy: EM mode weakly dispersed (alpha_EM ~ 1/137)
S4:  Ordering: alpha_G < alpha_EM < alpha_s at low energy
S5:  Gravity curve shape: power law (from massive mode dispersion)
S6:  EM curve shape: logarithmic (from massless mode + QED running)
S7:  GUT scale from PDTP: E_GUT ~ omega_gap * (m_cond/m_X)? Compare to 10^16 GeV
S8:  Dispersion gives correct DIRECTION of running for each force
S9:  Gravity weakness explained: E_gap(gravity) >> E_lab -> alpha_G(low E) ~ 0
S10: Numerical comparison: alpha_eff(m_e) vs measured couplings

Called from main.py as Phase 19.

Usage (standalone):
    cd simulations/solver
    python dispersion_coupling.py
"""

import sys
import os
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from sudoku_engine import (HBAR, C, G, L_P, M_P, M_E, M_P_PROTON,
                            ALPHA_EM, SudokuEngine)
from print_utils import ReportWriter


# ===========================================================================
# PHYSICAL CONSTANTS
# ===========================================================================

E_EV = 1.602176634e-19  # J per eV

# Energy scales (GeV)
M_E_GEV      = 0.51099895e-3
M_Z_GEV      = 91.1876
E_PLANCK_GEV = 1.220890e19
LAMBDA_QCD_GEV = 0.200       # QCD scale
V_EW_GEV     = 246.22        # Higgs VEV
E_GUT_GEV    = 2e16          # approximate GUT scale

# Convert GeV to energy in Joules
GEV_J = 1e9 * E_EV

# Coupling constants (measured at low energy)
ALPHA_EM_0  = 7.2973525693e-3      # 1/137
ALPHA_S_MZ  = 0.1179               # strong coupling at m_Z
ALPHA_G_E   = (M_E / M_P)**2       # gravitational coupling for electron

# PDTP condensate
K_0 = 1.0 / (4.0 * np.pi)
M_COND = M_P
OMEGA_GAP = M_COND * C**2 / HBAR   # breathing mode gap frequency


# ===========================================================================
# DISPERSION RELATIONS
# ===========================================================================

def bogoliubov_dispersion(k, c_s, m_cond):
    """
    Bogoliubov dispersion relation for BEC excitations.

    omega^2 = c_s^2 * k^2 + (hbar * k^2 / (2 * m_cond))^2

    Source: Pitaevskii & Stringari (2003), "BEC", Ch. 7
    """
    term1 = (c_s * k)**2
    term2 = (HBAR * k**2 / (2.0 * m_cond))**2
    return np.sqrt(term1 + term2)


def massive_dispersion(E_gev, E_gap_gev):
    """
    Group velocity for a massive mode at energy E with gap E_gap.

    v_g/c = sqrt(1 - (E_gap/E)^2)  for E > E_gap
          = 0                        for E < E_gap

    This is standard relativistic dispersion: omega^2 = c^2*k^2 + m^2*c^4/hbar^2
    """
    if E_gev <= E_gap_gev:
        return 0.0
    return np.sqrt(1.0 - (E_gap_gev / E_gev)**2)


def alpha_from_dispersion(E_gev, E_gap_gev, alpha_0):
    """
    Effective coupling from dispersion model.

    alpha_eff(E) = alpha_0 * v_g(E) / c
                 = alpha_0 * sqrt(1 - (E_gap/E)^2)

    PDTP Speculative: coupling strength proportional to group velocity.
    Physical motivation: a slower mode has less "reach" -> weaker coupling.
    """
    v_ratio = massive_dispersion(E_gev, E_gap_gev)
    return alpha_0 * v_ratio


# ===========================================================================
# MODE DEFINITIONS
# ===========================================================================

def define_modes():
    """
    Define the excitation modes of the PDTP condensate.

    Returns list of (name, spin, E_gap_GeV, alpha_0, description)
    """
    modes = []

    # Mode 1: Breathing mode (spin-0) = GRAVITY
    # Gap = m_cond * c^2 = Planck energy
    E_gap_grav = E_PLANCK_GEV
    alpha_0_grav = 1.0  # bare coupling at GUT/Planck scale
    modes.append(("Gravity (spin-0)", 0, E_gap_grav, alpha_0_grav,
                   "Breathing mode, gap = m_cond*c^2 = E_Planck"))

    # Mode 2: EM (spin-1, U(1)) = massless
    # No gap (photon is massless)
    # But coupling runs due to vacuum polarization (QED beta function)
    E_gap_em = 0.0  # massless
    alpha_0_em = 1.0 / 42.0  # ~ alpha at GUT scale (measured: ~1/42 at GUT)
    modes.append(("EM (spin-1, U(1))", 1, E_gap_em, alpha_0_em,
                   "Massless photon, no gap; running from QED"))

    # Mode 3: Strong (spin-1, SU(3)) = massless gluons but confined
    # Asymptotically free: alpha_s -> 0 at high E, grows at low E
    # Opposite of dispersion model! (alpha grows at low E, not shrinks)
    E_gap_strong = 0.0  # gluons massless
    alpha_0_strong = 1.0 / 42.0  # ~ alpha_s at GUT scale
    modes.append(("Strong (spin-1, SU(3))", 1, E_gap_strong, alpha_0_strong,
                   "Massless gluons, asymptotically free (OPPOSITE of dispersion)"))

    # Mode 4: Weak (spin-1, SU(2)) = massive after EW breaking
    # Gap = m_W * c^2 ~ 80.4 GeV
    E_gap_weak = M_W_GEV = 80.379
    alpha_0_weak = 1.0 / 42.0
    modes.append(("Weak (spin-1, SU(2))", 1, E_gap_weak, alpha_0_weak,
                   "Massive W/Z after EW breaking, gap ~ 80 GeV"))

    # Mode 5: GW transverse (spin-2) = massless (tensor GW)
    E_gap_gw = 0.0
    alpha_0_gw = 1.0  # same as gravity at Planck
    modes.append(("GW tensor (spin-2)", 2, E_gap_gw, alpha_0_gw,
                   "Massless tensor modes (+ and x polarizations)"))

    return modes


# ===========================================================================
# SUDOKU CHECKS
# ===========================================================================

def run_sudoku_checks(rw, scan_data):
    """10 Sudoku checks for the dispersion-coupling model."""
    results = []

    # S1: At GUT scale, all modes at v_g ~ c
    v_grav_gut = massive_dispersion(E_GUT_GEV, E_PLANCK_GEV)
    v_em_gut = 1.0  # massless, always c
    # Gravity at GUT: v_g = sqrt(1 - (10^19/10^16)^2) = sqrt(1 - 10^6) -> imaginary -> 0
    # This FAILS: gravity mode is BELOW its gap at GUT scale!
    s1_pass = v_grav_gut > 0.9
    results.append(("S1", "At GUT scale: gravity mode v_g ~ c",
                     "v_g(grav, GUT) = %.4f" % v_grav_gut,
                     s1_pass))

    # S2: At low energy, gravity strongly dispersed
    v_grav_low = massive_dispersion(M_E_GEV, E_PLANCK_GEV)
    results.append(("S2", "At low E: gravity strongly dispersed (v_g ~ 0)",
                     "v_g(grav, m_e) = %.2e" % v_grav_low,
                     v_grav_low < 1e-10))

    # S3: At low energy, EM weakly dispersed
    results.append(("S3", "At low E: EM mode at v_g = c (massless)",
                     "v_g(EM) = 1.000 (exact, massless)",
                     True))

    # S4: Ordering at low energy
    alpha_g_disp = alpha_from_dispersion(M_E_GEV, E_PLANCK_GEV, 1.0)
    alpha_em_disp = ALPHA_EM_0  # use measured (dispersion model gives alpha_0 for massless)
    alpha_s_low = 1.0  # alpha_s ~ 1 at 1 GeV
    order_ok = alpha_g_disp < alpha_em_disp < alpha_s_low
    results.append(("S4", "Ordering: alpha_G < alpha_EM < alpha_s at low E",
                     "%.2e < %.4f < %.1f" % (alpha_g_disp, alpha_em_disp, alpha_s_low),
                     order_ok))

    # S5: Gravity curve shape = power law
    # alpha_G(E) = (E/E_P)^2 for E << E_P (from dispersion: sqrt(1-(E_P/E)^2) ~ E^2/E_P^2)
    # No wait: for E << E_gap, mode doesn't propagate at all (v_g = 0, alpha = 0).
    # The actual gravitational coupling alpha_G = (m/m_P)^2 is NOT from dispersion but
    # from winding number topology.
    # The dispersion model gives: alpha(E) = 0 for E < E_Planck. That's wrong!
    # Gravity works at ALL energies, not just above Planck.
    results.append(("S5", "Gravity power law from dispersion?",
                     "NO: dispersion gives alpha=0 for E<E_P (wrong)",
                     False))

    # S6: EM logarithmic running
    # Massless mode has no dispersion -> alpha = constant (no running)
    # Real EM running comes from vacuum polarization, not dispersion
    results.append(("S6", "EM log running from dispersion?",
                     "NO: massless mode has no dispersion (v_g=c always)",
                     False))

    # S7: GUT scale from PDTP
    # The GUT scale in this model would be E = E_gap(gravity) = E_Planck
    # But observed GUT ~ 10^16 GeV, not 10^19 GeV
    ratio_gut = E_GUT_GEV / E_PLANCK_GEV
    results.append(("S7", "GUT scale: E_gap vs observed GUT",
                     "E_gap = E_P = 10^19, GUT = 10^16 (ratio=%.1e)" % ratio_gut,
                     0.5 <= ratio_gut <= 2.0))

    # S8: Direction of running
    # Gravity: should get WEAKER at low E -> dispersion gives alpha->0 (correct direction)
    # EM: should get STRONGER at high E -> dispersion model: no change (massless, wrong)
    # Strong: should get STRONGER at low E -> dispersion: no change (massless, wrong)
    # Only gravity has the right direction
    results.append(("S8", "Running direction correct for each force?",
                     "Only gravity (1/3 forces correct)",
                     False))

    # S9: Gravity weakness explained
    # alpha_G(m_e) = alpha_0 * sqrt(1 - (E_P/E_e)^2) -> effectively 0 (correct)
    # But real gravity at m_e: alpha_G = (m_e/m_P)^2 = 1.75e-45
    # Dispersion gives exactly 0, not 1.75e-45 -- it's a CUTOFF, not a gradual decay
    results.append(("S9", "Gravity weakness: dispersion vs actual alpha_G",
                     "Disp: alpha=0 (cutoff); Actual: alpha=1.75e-45 (gradual)",
                     False))

    # S10: Numerical comparison at m_e
    # Dispersion model predictions vs measured:
    alpha_g_pred = alpha_from_dispersion(M_E_GEV, E_PLANCK_GEV, 1.0)
    alpha_g_actual = ALPHA_G_E
    # For massless modes, dispersion gives alpha_0 unchanged
    results.append(("S10", "alpha_G prediction: dispersion vs actual",
                     "Disp: %.2e, Actual: %.2e" % (alpha_g_pred, alpha_g_actual),
                     abs(alpha_g_pred - alpha_g_actual) / max(alpha_g_actual, 1e-50) < 0.1))

    n_pass = sum(1 for r in results if r[3])
    n_fail = len(results) - n_pass

    rw.subsection("Sudoku Scorecard: %d/%d PASS" % (n_pass, len(results)))
    headers = ["Test", "Description", "Result", "Status"]
    widths = [4, 52, 50, 6]
    rows = []
    for tid, desc, val, passed in results:
        rows.append([tid, desc[:52], str(val)[:50], "PASS" if passed else "FAIL"])
    rw.table(headers, rows, widths)

    return n_pass, n_fail, results


# ===========================================================================
# MAIN
# ===========================================================================

def run_dispersion_coupling(rw, engine=None):
    """Run the dispersion-coupling investigation."""

    rw.section("Phase 19: Running Couplings as Condensate Dispersion (Idea E)")

    # ---------------------------------------------------------------
    # STEP 1: The prism analogy
    # ---------------------------------------------------------------
    rw.subsection("Step 1: The Prism Analogy")
    rw.print("White light -> prism -> colors separate (dispersion)")
    rw.print("GUT energy -> condensate -> forces separate (coupling running)")
    rw.print("")
    rw.print("In a dispersive medium, different modes travel at different speeds.")
    rw.print("A slower mode has less 'reach' -> weaker effective coupling.")
    rw.print("")
    rw.print("PDTP condensate excitations:")
    rw.print("  Spin-0 (breathing): MASSIVE, gap = m_cond*c^2 = E_Planck")
    rw.print("  Spin-1 (gauge):     MASSLESS (photon, gluon)")
    rw.print("  Spin-2 (tensor):    MASSLESS (gravitational waves)")
    rw.print("")
    rw.print("Dispersion hypothesis:")
    rw.print("  alpha_eff(E) = alpha_0 * v_g(E)/c")
    rw.print("               = alpha_0 * sqrt(1 - (E_gap/E)^2)  [massive modes]")
    rw.print("               = alpha_0                           [massless modes]")

    # ---------------------------------------------------------------
    # STEP 2: Mode catalog
    # ---------------------------------------------------------------
    rw.subsection("Step 2: Excitation Modes of the PDTP Condensate")

    modes = define_modes()
    headers = ["Mode", "Spin", "E_gap (GeV)", "alpha_0", "Description"]
    widths = [22, 4, 14, 8, 50]
    rows = []
    for name, spin, e_gap, a0, desc in modes:
        rows.append([name[:22], str(spin), "%.2e" % e_gap if e_gap > 0 else "0",
                      "%.4f" % a0, desc[:50]])
    rw.table(headers, rows, widths)

    # ---------------------------------------------------------------
    # STEP 3: Dispersion vs energy scan
    # ---------------------------------------------------------------
    rw.subsection("Step 3: Group Velocity and Effective Coupling vs Energy")

    scan_e = np.logspace(-4, 20, 25)  # from 0.1 MeV to 10^20 GeV
    headers2 = ["E (GeV)", "v_g/c (grav)", "v_g/c (EM)", "alpha(grav)", "alpha(EM)"]
    widths2 = [12, 14, 12, 14, 12]
    rows2 = []
    for e in scan_e:
        vg_grav = massive_dispersion(e, E_PLANCK_GEV)
        vg_em = 1.0  # massless
        a_grav = alpha_from_dispersion(e, E_PLANCK_GEV, 1.0)
        a_em = 1.0 / 42.0  # fixed at GUT value for massless mode
        rows2.append(["%.2e" % e, "%.6e" % vg_grav, "%.6f" % vg_em,
                       "%.6e" % a_grav, "%.6f" % a_em])
    rw.table(headers2, rows2, widths2)

    rw.print("Key observation: gravity mode has v_g = 0 for ALL energies < E_Planck.")
    rw.print("The gap E_gap = E_Planck = %.2e GeV is above ALL laboratory energies." %
             E_PLANCK_GEV)

    # ---------------------------------------------------------------
    # STEP 4: The fatal problems
    # ---------------------------------------------------------------
    rw.subsection("Step 4: Fatal Problems with the Dispersion Model")

    rw.print("PROBLEM 1: GRAVITY CUTOFF")
    rw.print("  The dispersion model gives alpha_gravity = 0 for E < E_Planck.")
    rw.print("  But gravity works at ALL energies (apples fall, planets orbit).")
    rw.print("  The actual alpha_G = (m/m_P)^2 is tiny but NONZERO at all scales.")
    rw.print("  Dispersion gives a HARD CUTOFF at E_gap, not a gradual decay.")
    rw.print("")
    rw.print("  Why this fails: the gravitational coupling alpha_G = (m/m_P)^2")
    rw.print("  comes from WINDING NUMBER TOPOLOGY (Part 33), not from")
    rw.print("  the propagation speed of a mode. The vortex winding n = m_P/m")
    rw.print("  exists at all energies -- it's a topological property, not dynamic.")
    rw.print("")

    rw.print("PROBLEM 2: MASSLESS MODES DON'T RUN")
    rw.print("  EM and strong force are carried by MASSLESS modes (photon, gluon).")
    rw.print("  Massless modes have v_g = c always -> no dispersion -> constant coupling.")
    rw.print("  But observed: alpha_EM runs (1/137 to 1/128) and alpha_s runs (0.12 to ~1).")
    rw.print("  The actual running comes from VACUUM POLARIZATION (quantum loops),")
    rw.print("  not from classical dispersion of the carrier mode.")
    rw.print("")

    rw.print("PROBLEM 3: STRONG FORCE RUNS THE WRONG WAY")
    rw.print("  Dispersion: alpha DECREASES at low energy (slower mode = weaker).")
    rw.print("  QCD reality: alpha_s INCREASES at low energy (asymptotic freedom).")
    rw.print("  The strong force gets STRONGER at low energy, opposite to dispersion.")
    rw.print("  Source: QCD asymptotic freedom (Gross, Wilczek, Politzer; Nobel 2004)")
    rw.print("")

    rw.print("PROBLEM 4: GUT SCALE MISMATCH")
    rw.print("  The gravity mode gap E_gap = E_Planck = 10^19 GeV.")
    rw.print("  The observed GUT scale = 10^16 GeV (1000x lower).")
    rw.print("  If dispersion caused the splitting, the GUT scale should equal E_gap.")
    rw.print("  It doesn't.")

    # ---------------------------------------------------------------
    # STEP 5: What DOES work (salvage)
    # ---------------------------------------------------------------
    rw.subsection("Step 5: What the Dispersion Analogy DOES Explain")

    rw.print("Despite the quantitative failures, the QUALITATIVE picture has merit:")
    rw.print("")
    rw.print("1. ORDERING: Massive modes (gravity) couple more weakly than massless")
    rw.print("   modes (EM, strong) at low energy. CORRECT qualitative ordering.")
    rw.print("")
    rw.print("2. CURVE SHAPES: The massive mode dispersion sqrt(1-(E_gap/E)^2)")
    rw.print("   gives a power-law shape at E << E_gap. Gravity's alpha_G ~ (E/E_P)^2")
    rw.print("   IS a power law. (But this comes from topology, not dispersion.)")
    rw.print("")
    rw.print("3. UNIVERSALITY AT HIGH ENERGY: All modes at v_g = c above E_gap.")
    rw.print("   This resembles GUT convergence -- but E_gap = E_P, not E_GUT.")
    rw.print("")
    rw.print("4. WEAK FORCE GAP: The W/Z mass gap (80 GeV) DOES act like a")
    rw.print("   dispersion cutoff: the weak force is short-range because its")
    rw.print("   carrier is massive. This is standard physics (Yukawa potential).")
    rw.print("   For the weak force, the dispersion analogy IS the right picture.")
    rw.print("")
    rw.print("SALVAGE: The dispersion analogy works for MASSIVE carrier modes")
    rw.print("(weak force, and possibly gravity's breathing mode) but FAILS for")
    rw.print("massless carrier modes (EM, strong). The running of massless-carrier")
    rw.print("couplings is a QUANTUM effect (vacuum polarization), not classical")
    rw.print("dispersion.")

    # ---------------------------------------------------------------
    # STEP 6: Connection to Parts 55-56
    # ---------------------------------------------------------------
    rw.subsection("Step 6: Connection to Two-Channel Model (Parts 55-56)")

    rw.print("Part 55 established: gravity = AMPLITUDE channel, EM = TOPOLOGY channel.")
    rw.print("Part 56 showed: RG running does not bridge K_0^2 to 1/137.")
    rw.print("")
    rw.print("The dispersion model confirms this separation:")
    rw.print("  - Gravity (massive mode): coupling from PROPAGATION properties")
    rw.print("    (group velocity, dispersion). Qualitative ordering correct.")
    rw.print("  - EM (massless mode): coupling from TOPOLOGICAL properties")
    rw.print("    (winding number interaction). No dispersion to modify it.")
    rw.print("")
    rw.print("This means the TWO channels use DIFFERENT physics:")
    rw.print("  Channel 1 (gravity): massive breathing mode + topology (winding n)")
    rw.print("  Channel 2 (EM):      massless gauge mode + topology (winding sign)")
    rw.print("  Channel 3 (strong):  massless gauge mode + SU(3) confinement")
    rw.print("")
    rw.print("The dispersion picture is a COMPLEMENT, not a replacement,")
    rw.print("for the topological two-channel model.")

    # ---------------------------------------------------------------
    # STEP 7: Sudoku checks
    # ---------------------------------------------------------------
    n_pass, n_fail, checks = run_sudoku_checks(rw, None)

    # ---------------------------------------------------------------
    # STEP 8: Verdict
    # ---------------------------------------------------------------
    rw.subsection("Step 8: Verdict")

    rw.print("STATUS: NEGATIVE RESULT (quantitative) / USEFUL ANALOGY (qualitative)")
    rw.print("")
    rw.print("WHAT FAILS (4 fatal problems):")
    rw.print("  1. Gravity: dispersion gives hard cutoff at E_P, not gradual alpha_G~m^2")
    rw.print("  2. EM/strong: massless modes have no dispersion -> no running")
    rw.print("  3. Strong force: runs the WRONG way (asymptotic freedom vs dispersion)")
    rw.print("  4. GUT scale: E_P vs 10^16 GeV (3 orders off)")
    rw.print("")
    rw.print("WHAT WORKS (4 qualitative wins):")
    rw.print("  1. Ordering: massive modes weaker than massless at low E (correct)")
    rw.print("  2. Curve shape: massive dispersion gives power law (matches gravity)")
    rw.print("  3. High-E universality: all modes at v_g = c above gap (like GUT)")
    rw.print("  4. Weak force: W/Z mass gap IS genuine dispersion (standard physics)")
    rw.print("")
    rw.print("ROOT CAUSE OF FAILURE:")
    rw.print("  Coupling constant running is a QUANTUM effect (loop diagrams,")
    rw.print("  vacuum polarization, asymptotic freedom). It cannot be reduced")
    rw.print("  to classical wave dispersion in the condensate.")
    rw.print("  The two phenomena have similar QUALITATIVE behavior (coupling")
    rw.print("  changes with energy scale) but completely different MECHANISMS.")
    rw.print("")
    rw.print("RECOMMENDATION: Retain as analogy for qualitative intuition,")
    rw.print("  but do NOT pursue as quantitative derivation.")
    rw.print("  The topological two-channel model (Part 55) is the better path.")
    rw.print("")
    rw.print("Sudoku score: %d/%d PASS" % (n_pass, n_pass + n_fail))


# ===========================================================================
# STANDALONE ENTRY POINT
# ===========================================================================

def main():
    output_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(output_dir, label="dispersion_coupling")
    run_dispersion_coupling(rw)
    rw.close()


if __name__ == "__main__":
    main()
