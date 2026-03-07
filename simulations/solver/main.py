#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py — PDTP Comprehensive Solver (entry point)
===================================================
Orchestrates all phases of the systematic search for a non-circular
derivation of Newton's constant G from particle physics alone.

Usage:
    cd simulations/solver
    python main.py

Or from the repo root:
    python simulations/solver/main.py

Output:
    Console output (all phases)
    Timestamped report file in simulations/solver/outputs/

Phases:
    1. Named candidates   — re-verify Parts 29-32 results + new candidates
    2. Power-law sweep    — 729 combinations of (p1, p2, p3)
    3. Mass-combo sweep   — geometric/harmonic/RMS of all particle-mass pairs/triplets
    4. Analytical         — exact power-law constraint equation
    5. Cross-mode ranking — best non-circular from all phases combined
    6. Final summary      — strategic conclusions
    7. LISA simulation    — breathing mode omega_gap -> G (Strategy A)
    8. Orbital scanner    — n = m_P/m reframe; Planck as excited state? (Strategy B)
    9. Vortex winding     — particle as vortex; n from core condition; A+B unified (Part 33)
   10. Condensate BEC     — self-consistency: c_s=c; m_cond still free; dim. transmutation? (Part 34)
   11. Dim. transmutation — 1-loop RG running of K; Landau pole; exhaustion of perturbative paths (Part 35)
   12. SU(3) extension    — Casimir factors, Z3 vortices, 8 gluons, improved string tension (Part 37)
   13. SU(3) lattice MC   — Wilson action Monte Carlo; Cornell fit; sigma vs sigma_QCD (Part 38)
   14. SU(3) 4D lattice   — 4D Wilson action; Polyakov loops; 4D SC confirms 4% gap closed (Part 39)
   15. Wilson fermions     — hopping expansion; sea quarks reduce sigma; quenched result best (Part 40)
"""

import os
import sys

# Allow running from any directory
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from print_utils import ReportWriter
from sudoku_engine import SudokuEngine
from test_generator import (named_candidates, power_law_candidates,
                             mass_combo_candidates)
from brute_force_runner import (run_phase, run_analytical,
                                compare_modes, final_summary)
from lisa_sim import run_lisa_phase
from orbital_scanner import run_orbital_phase
from vortex_winding import run_vortex_phase
from condensate_selfconsist import run_condensate_phase
from dim_transmutation import run_dim_transmutation_phase
from su3_condensate import run_su3_phase
from su3_lattice import run_su3_lattice_phase
from su3_lattice_4d import run_su3_lattice_4d_phase
from su3_fermion import run_su3_fermion_phase


def main():
    # ------------------------------------------------------------------
    # Setup
    # ------------------------------------------------------------------
    output_dir = os.path.join(_HERE, "outputs")
    rw = ReportWriter(output_dir, label="pdtp_solver")
    engine = SudokuEngine()

    rw.print("  Welcome to the PDTP Comprehensive Solver.")
    rw.print("  This script systematically tests candidate lattice spacings")
    rw.print("  to find a non-circular derivation of Newton's constant G.")
    rw.print("")
    rw.print("  PDTP bridge: K = hbar/(4*pi*c)  [G-free]")
    rw.print("  G_pred = c^3 * a^2 / hbar  [from K and a]")
    rw.print("  Target: G_pred = G_known = 6.67430e-11 m^3 kg^-1 s^-2")
    rw.print("")

    # ------------------------------------------------------------------
    # Phase 1: Named candidates
    # ------------------------------------------------------------------
    named = named_candidates()
    named_results = run_phase(
        "1 — Named Candidates (Parts 29-32 + new)",
        named, engine, rw,
        show_all=True,
        top_n=30,
    )

    # ------------------------------------------------------------------
    # Phase 2: Power-law sweep
    # ------------------------------------------------------------------
    rw.section("Phase 2 — Power-Law Sweep (computing 729 combinations...)")
    rw.print("  Parametric search:  a = l_P * (m_e/m_P)^p1 * (m_p/m_P)^p2 * alpha^p3")
    rw.print("  Each exponent sweeps [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]")
    rw.print("  Total: 9^3 = 729 combinations")
    rw.print("")

    power_cands = power_law_candidates(step=0.5, p_range=(-2, 2))
    power_results = run_phase(
        "2 — Power-Law Results",
        power_cands, engine, rw,
        show_all=False,
        top_n=20,
    )

    # ------------------------------------------------------------------
    # Phase 3: Mass-combination sweep
    # ------------------------------------------------------------------
    rw.section("Phase 3 — Mass-Combination Sweep (generating combinations...)")
    rw.print("  Tests: Compton wavelengths of geometric/harmonic/RMS means")
    rw.print("  of all pairs and triplets from 11 particle masses.")
    rw.print("")

    combo_cands = mass_combo_candidates()
    rw.print("  Generated {} mass-combo candidates".format(len(combo_cands)))
    rw.print("")

    combo_results = run_phase(
        "3 — Mass-Combination Results",
        combo_cands, engine, rw,
        show_all=False,
        top_n=20,
    )

    # ------------------------------------------------------------------
    # Phase 4: Analytical
    # ------------------------------------------------------------------
    run_analytical(rw)

    # ------------------------------------------------------------------
    # Phase 5: Cross-mode comparison
    # ------------------------------------------------------------------
    compare_modes(named_results, power_results, combo_results, rw)

    # ------------------------------------------------------------------
    # Phase 6: Final summary
    # ------------------------------------------------------------------
    final_summary(rw)

    # ------------------------------------------------------------------
    # Phase 7: LISA Breathing Mode Simulation (Strategy A)
    # ------------------------------------------------------------------
    run_lisa_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 8: Orbital Quantization Scanner (Strategy B reframe)
    # ------------------------------------------------------------------
    run_orbital_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 9: Vortex Winding Number (Part 33 -- Strategy A+B unified)
    # ------------------------------------------------------------------
    run_vortex_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 10: Condensate Self-Consistency (Part 34)
    # ------------------------------------------------------------------
    run_condensate_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 11: Dimensional Transmutation (Part 35)
    # ------------------------------------------------------------------
    run_dim_transmutation_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 12: SU(3) Condensate Extension (Part 37)
    # ------------------------------------------------------------------
    run_su3_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 13: SU(3) Lattice Monte Carlo (Part 38)
    # ------------------------------------------------------------------
    run_su3_lattice_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 14: SU(3) 4D Lattice Monte Carlo (Part 39)
    # ------------------------------------------------------------------
    run_su3_lattice_4d_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 15: Wilson Fermions + Quark Mass Renormalisation (Part 40)
    # ------------------------------------------------------------------
    run_su3_fermion_phase(rw, engine)

    # ------------------------------------------------------------------
    # Done
    # ------------------------------------------------------------------
    rw.close()


if __name__ == "__main__":
    main()
