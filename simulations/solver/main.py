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
   16. Physical beta       — Wilson loops at beta=6.0; scaling window; GPU needed for N>=16 (Part 41)
   17. SU(3) gauge struct  — 8 gluons as normal modes; AF negative; SU(2) structural (Open Problem #1)
   18. Scalar backreaction — T_mu_nu^phi; vacuum zero (U(1) shift); excited -> dark energy w(z)
   19. Hierarchy ratio    — R=alpha_G/alpha_EM; PDTP identity R=1/(n^2*alpha_EM); paths A/B/C fail
   20. BH topological     — r=0 replaced by vortex core xi=l_P/sqrt(2); Penrose evaded by lattice
   21. Hawking info paradox — W=winding as information; topology protects; Resolution A (phase correlations)
   22. BH evaporation endpoint — complete evaporation; S<1 bit; t_evap~T_P; E_final/M c^2=8*pi
   23. Weak coupling g_W — doubly underdetermined (alpha_EM + sin^2(theta_W) both free)
   24. W and Z boson masses — Higgs mechanism; v = 246.22 GeV is 3rd free parameter (Part 49)
   25. Chirality — Z2 vortex winding = chirality; maximal A=-1 automatic; vacuum choice free (Part 50)
   26. Three generations — radial vortex modes n_r=0,1,2; lepton universality derived (Part 51)
   27. Coupling constants — beta functions derived; alpha_EM=1/137 underdetermined (Part 52)
   28. Z3-Koide — Z3 center derives Koide Q=2/3; delta=sqrt(2) from equal partition (Part 53)
   29. Cosmo constant — FCC: rho_Lambda ~ rho_Planck*(l_P/L_H)^2; CKN bound; L_H free (Part 54)
   30. Two-phase Lagrangian — +cos/-cos EL derivation; biharmonic gravity; phi_- new field (Part 61)
   31. Reversed Higgs — phi_- environment-dependent mass; chameleon comparison; hollow shell test (Part 62)
   32. Two-phase re-derivation — 16/16 tests: all single-phase results reproduced (Part 63)
   33. Temperature in PDTP — XY model identification; T_c ~ T_Planck; alpha(T) derived (Part 64)
   34. Chirality refractive — condensate birefringence; n_eff split; confinement derived (Part 65)
   35. Quantum geometry — quantum metric in PDTP Lagrangian; D_geom scaling; GP vortex (Part 66)
   36. White comparison — NR limit D=hbar/(2m); constitutive profile; biharmonic parallel (Part 67)
   37. Cosmo constant v2 — Two-phase FCC; Omega_beat=2/3; phi_- vacuum energy (Part 68)
   38. Scale selection — cosine-Gordon phi_-; all scales ~ l_P; H_0 free (Part 69)
   39. Xi_cc+ baryon — LHCb benchmark; constituent + string + hyperfine (Part 70)
   40. Leidenfrost — decoupling analogue; phi_- screening; Z3 topology (Part 71)
   41. Full T_mu_nu — all components; conservation law; SymPy verified (Part 72)
   42. Emergent metric — g_mu_nu in closed form; PG = Schwarzschild; PPN gamma=beta=1 (Part 73)
   43. Einstein from PDTP — Sakharov/Jacobson/frustration routes; Case B partial; DOF gap (Part 74)
   44. SU(3) tensor metric — g_mu_nu = Tr(dU_dag dU); NOT pure gauge; 2 TT modes; PSD constraint (Part 75)
   45. SU(3) Einstein recovery — 8*pi*G coefficient; auto-Lorenz; matter coupling; PSD obs; nonlinear (Part 75b)
   46. SU(3) graviton validation — gauge exclusion; Fierz-Pauli; Isaacson; Bianchi; metric generality (Part 76)
   47-53. SU(3) dim transmutation, extremal condensate, alpha_EM FCC, dispersion,
          wave audit, Koide re-examine, N_eff Sakharov (Parts 77-83)
   54. Tetrad resolution — B3 FCC: SU(3) replaces tetrad for linearized gravity (Part 84)
   55. CP violation — B4 FCC: L5 two-phase gives real CP; Sakharov cond. 2 derived (Part 85)
   56. Nonlinear Einstein — B2 FCC: sigma model NEGATIVE; entropy+Jacobson PARTIAL (Part 86)
   57. Cosmo constant A3 — B3 FCC: CONFIRMED FREE PARAM; Lambda=g*phi_-_vac^2; DESI w(z) (Part 87)
   58. Hubble tension C1 — C1 FCC: all 5 mechanisms NEGATIVE; phi_-^4 missing term; DESI test (Part 88)
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
from su3_physical_beta import run_su3_physical_beta_phase
from su3_gauge_structure import run_su3_gauge_structure_phase
from scalar_backreaction import run_scalar_backreaction_phase
from hierarchy_ratio import run_hierarchy_phase
from bh_topological_defect import run_bh_topological_phase
from hawking_info_paradox import run_hawking_info_phase
from bh_evaporation_endpoint import run_bh_endpoint_phase
from weak_coupling_gw import run_weak_coupling_phase
from wz_boson_masses import run_wz_boson_phase
from chirality_parity import run_chirality_phase
from three_generations import run_three_generations_phase
from coupling_constants import run_coupling_constants_phase
from koide_z3 import run_koide_z3_phase
from cosmo_constant import run_cosmo_constant_phase
from two_phase_lagrangian import run_two_phase_lagrangian
from reversed_higgs import run_reversed_higgs
from two_phase_rederivation import run_two_phase_rederivation
from temperature_pdtp import run_temperature_phase
from chirality_refractive import run_chirality_refractive_phase
from quantum_geometry import run_quantum_geometry_phase
from white_comparison import run_white_comparison_phase
from cosmo_constant_v2 import run_cosmo_constant_v2_phase
from scale_selection import run_scale_selection_phase
from xicc_baryon import run_xicc_baryon_phase
from leidenfrost_decoupling import run_leidenfrost_phase
from stress_energy_full import run_stress_energy_full_phase
from emergent_metric import run_emergent_metric_phase
from einstein_from_pdtp import run_einstein_from_pdtp_phase
from su3_tensor_metric import run_su3_tensor_metric_phase
from su3_einstein_recovery import run_su3_einstein_recovery_phase
from su3_graviton_validation import run_su3_graviton_validation_phase
from su3_dim_transmutation import run_su3_dim_transmutation_phase
from extremal_condensate import run_extremal_condensate_phase
from alpha_em_fcc import run_alpha_em_fcc_phase
from dispersion_two_phase import run_dispersion_two_phase
from wave_audit_g import run_wave_audit_g
from koide_reexamine import run_koide_reexamine
from neff_sakharov import run_neff_sakharov
from tetrad_resolution import run_tetrad_resolution
from cp_violation import run_cp_violation
from nonlinear_einstein import run_nonlinear_einstein
from cosmo_constant_a3 import run_cosmo_constant_a3
from hubble_tension_c1 import run_hubble_tension_phase


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
    # Phase 16: Physical Beta Lattice (Part 41)
    # ------------------------------------------------------------------
    run_su3_physical_beta_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 17: SU(3) Gauge Structure (Open Problem #1)
    # ------------------------------------------------------------------
    run_su3_gauge_structure_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 18: Scalar Sector Backreaction (Open Problem #2)
    # ------------------------------------------------------------------
    run_scalar_backreaction_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 19: Hierarchy Ratio (Part 44)
    # ------------------------------------------------------------------
    run_hierarchy_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 20: BH Singularity as Topological Defect (Part 45)
    # ------------------------------------------------------------------
    run_bh_topological_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 21: Hawking Information Paradox in PDTP Condensate (Part 46)
    # ------------------------------------------------------------------
    run_hawking_info_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 22: Black Hole Evaporation Endpoint (Part 47)
    # ------------------------------------------------------------------
    run_bh_endpoint_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 23: Weak Coupling Strength g_W (Part 48)
    # ------------------------------------------------------------------
    run_weak_coupling_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 24: W and Z Boson Masses (Part 49)
    # ------------------------------------------------------------------
    run_wz_boson_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 25: Chirality and Parity Violation (Part 50)
    # ------------------------------------------------------------------
    run_chirality_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 26: Three Generations of Fermions (Part 51)
    # ------------------------------------------------------------------
    run_three_generations_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 27: Coupling Constant Values (Part 52)
    # ------------------------------------------------------------------
    run_coupling_constants_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 28: Z3 Phase Positions and the Koide Formula (Part 53)
    # ------------------------------------------------------------------
    run_koide_z3_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 29: Cosmological Constant -- Forced Checklist Check (Part 54)
    # ------------------------------------------------------------------
    run_cosmo_constant_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 30: Two-Phase Lagrangian Derivation (Part 61)
    # ------------------------------------------------------------------
    run_two_phase_lagrangian(rw, engine)

    # ------------------------------------------------------------------
    # Phase 31: Reversed Higgs -- Environment-Dependent Mass (Part 62)
    # ------------------------------------------------------------------
    run_reversed_higgs(rw, engine)

    # ------------------------------------------------------------------
    # Phase 32: Two-Phase Re-derivation of ALL Results (Part 63)
    # ------------------------------------------------------------------
    run_two_phase_rederivation(rw, engine)

    # ------------------------------------------------------------------
    # Phase 33: Temperature in PDTP (Part 64)
    # ------------------------------------------------------------------
    run_temperature_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 34: Chirality from Condensate Refractive Index (Part 65)
    # ------------------------------------------------------------------
    run_chirality_refractive_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 35: Quantum Geometry in PDTP Condensate (Part 66)
    # ------------------------------------------------------------------
    run_quantum_geometry_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 36: White et al. (2026) Comparison (Part 67)
    # ------------------------------------------------------------------
    run_white_comparison_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 37: Cosmological Constant Two-Phase (Part 68)
    # ------------------------------------------------------------------
    run_cosmo_constant_v2_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 38: Scale-Selection Mechanism (Part 69)
    # ------------------------------------------------------------------
    run_scale_selection_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 39: Xi_cc+ Baryon Benchmark (Part 70)
    # ------------------------------------------------------------------
    run_xicc_baryon_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 40: Leidenfrost Decoupling Analogue (Part 71)
    # ------------------------------------------------------------------
    run_leidenfrost_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 41: Full Stress-Energy Tensor T_mu_nu (Part 72)
    # ------------------------------------------------------------------
    run_stress_energy_full_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 42: Emergent Metric g_mu_nu in Closed Form (Part 73)
    # ------------------------------------------------------------------
    run_emergent_metric_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 43: Einstein Equations from PDTP Lagrangian (Part 74)
    # ------------------------------------------------------------------
    run_einstein_from_pdtp_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 44: SU(3) Tensor Metric Construction (Part 75)
    # ------------------------------------------------------------------
    run_su3_tensor_metric_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 45: SU(3) Einstein Recovery (Part 75b)
    # ------------------------------------------------------------------
    run_su3_einstein_recovery_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 46: SU(3) Graviton Validation (Part 76)
    # ------------------------------------------------------------------
    run_su3_graviton_validation_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 47: SU(3) Dimensional Transmutation (Part 77)
    # ------------------------------------------------------------------
    run_su3_dim_transmutation_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 48: Extremal Condensate -- 4 Paths for A1 (Part 78)
    # ------------------------------------------------------------------
    run_extremal_condensate_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 49: Fine-Structure Constant FCC (Part 79)
    # ------------------------------------------------------------------
    run_alpha_em_fcc_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 50: Dispersion Re-examination with Two-Phase (Part 80)
    # ------------------------------------------------------------------
    run_dispersion_two_phase(rw, engine)

    # ------------------------------------------------------------------
    # Phase 51: Wave Effects Audit -- G as Combination Effect (Part 81)
    # ------------------------------------------------------------------
    run_wave_audit_g(rw, engine)

    # ------------------------------------------------------------------
    # Phase 52: Koide Circularity Re-examination (Part 82, D4)
    # ------------------------------------------------------------------
    run_koide_reexamine(rw, engine)

    # ------------------------------------------------------------------
    # Phase 53: N_eff = 6*pi Gap in Sakharov Formula (Part 83, B1)
    # ------------------------------------------------------------------
    run_neff_sakharov(rw, engine)

    # ------------------------------------------------------------------
    # Phase 54: Tetrad from SU(3) -- B3 FCC Resolution (Part 84)
    # ------------------------------------------------------------------
    run_tetrad_resolution(rw, engine)

    # ------------------------------------------------------------------
    # Phase 55: CP Violation in PDTP (Part 85, B4 FCC)
    # ------------------------------------------------------------------
    run_cp_violation(rw, engine)

    # ------------------------------------------------------------------
    # Phase 56: Full Nonlinear Einstein Equation (Part 86, B2 FCC)
    # ------------------------------------------------------------------
    run_nonlinear_einstein(rw, engine)

    # ------------------------------------------------------------------
    # Phase 57: Cosmological Constant -- A3 FCC (Part 87)
    # ------------------------------------------------------------------
    run_cosmo_constant_a3(rw, engine)

    # ------------------------------------------------------------------
    # Phase 58: Hubble Tension -- C1 FCC (Part 88)
    # ------------------------------------------------------------------
    run_hubble_tension_phase(rw, engine)

    # ------------------------------------------------------------------
    # Done
    # ------------------------------------------------------------------
    rw.close()


if __name__ == "__main__":
    main()
