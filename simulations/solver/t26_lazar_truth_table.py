#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
t26_lazar_truth_table.py -- TODO_04 T26, Part 135
=======================================================================
Bob Lazar truth table (decoupling phenomenology). Per T26's own effort
estimate ("Low-medium, mostly literature review + PDTP mapping"), this
is NOT a heavy new-derivation script -- it recomputes, independently and
numerically, three quantities that are needed to answer T26's Key
Question 3 (energy budget) and Key Question 2 (field-generator mapping),
using ONLY already-established PDTP formulas (Part 28b/29/33/34/61/71).

No new PDTP Original equations are introduced here. SymPy symbolic
verification is not applicable -- every quantity below is a numeric
evaluation of an already-derived closed-form formula (Part 71 Sec 2-5),
not a new algebraic identity. Per CLAUDE.md: "If SymPy cannot verify a
result... document why explicitly" -- this is that documentation.

What THIS script adds beyond a re-quote of Part 71:
1. omega_gap and f_gap re-derived independently from (c, hbar, G) rather
   than copied from coupling_constant_g.md, then compared to the current-
   technology coherent-oscillator ceiling (~1e15 Hz, Phase 7 motivation
   text) to get an exact frequency-gap ratio (Part 71/Phase 7 only give
   the rounded "~10^27" figure).
2. E_layer (the boundary-layer decoupling energy, Joules) is computed for
   the first time as an explicit number -- Part 71 Sec 3.3 gives all the
   intermediate quantities (N_layer, Delta_E) but never multiplies them
   out to a final Joule figure.
3. The Z3 three-source cancellation (Part 71 Sec 5.1-5.2, "three emitters
   at 120 degrees give exactly zero average coupling at the centre") is
   re-verified numerically here for several phi values (RECHECK discipline
   -- Part 71's own doc states one symbolic argument; this checks it holds
   numerically for phi swept over [0, 2*pi), not just asserted).

Output: DATA only. Interpretation in docs/research/lazar_truth_table.md.
"""

import cmath
import math

# ===========================================================================
# CONSTANTS (SI, CODATA-consistent; matches coupling_constant_g.md)
# ===========================================================================
C = 2.998e8          # m/s
HBAR = 1.055e-34      # J*s
G = 6.674e-11         # m^3/(kg*s^2)
M_PLANCK_KG = 2.176e-8  # kg (Planck mass = PDTP's m_cond, Part 33/35)


def derive_omega_gap():
    """omega_gap = g = sqrt(c^5/(hbar*G)) [Eq 6a, Part 33; coupling_constant_g.md].
    Re-derived here from fundamental constants, independent of any stored value."""
    omega_gap = math.sqrt(C**5 / (HBAR * G))
    f_gap = omega_gap / (2 * math.pi)
    return {'omega_gap_rad_s': omega_gap, 'f_gap_Hz': f_gap}


def compute_frequency_gap_ratio(f_gap_hz, f_current_tech_hz=1e15):
    """Ratio of the Planck-scale gap frequency to the highest coherent
    oscillator frequency in current technology. f_current_tech_hz = 1e15 Hz
    matches the Phase 7 motivation text's own reference figure (optical/near-UV
    coherent sources); this function just makes the ratio explicit and precise
    rather than the rounded '~10^27' already quoted in TODO_04.md."""
    ratio = f_gap_hz / f_current_tech_hz
    return {'ratio': ratio, 'log10_ratio': math.log10(ratio)}


def compute_boundary_layer_energy(mass_kg=1.0, radius_m=0.062):
    """Re-derive Part 71 Sec 2-3's boundary-layer decoupling energy chain
    from scratch, for a sphere of given mass/radius, and carry it through
    to a final Joule number (Part 71 stops at N_layer, never states E_layer).
    Formulas [DERIVED, Part 71]:
      Delta_E   = m_Planck*c^2 / (2*sqrt(2))            (Eq 4, per-oscillator)
      xi        = l_Planck / sqrt(2)                     (healing length, Part 34)
      a_0       = l_Planck                                (lattice spacing, Part 34, n=1/l_P^3)
      N_layer   = (4*pi*r^2 * xi) / a_0^3
      E_layer   = N_layer * Delta_E
      E_bulk    = M*c^2 / (2*sqrt(2))                     (Eq 8, whole-object bulk decoupling)
    """
    l_planck = math.sqrt(HBAR * G / C**3)
    delta_E = M_PLANCK_KG * C**2 / (2 * math.sqrt(2))   # J, per oscillator
    xi = l_planck / math.sqrt(2)
    a0 = l_planck
    surface_area = 4 * math.pi * radius_m**2
    v_layer = surface_area * xi
    n_layer = v_layer / a0**3
    e_layer = n_layer * delta_E
    e_bulk = mass_kg * C**2 / (2 * math.sqrt(2))
    return {
        'l_planck_m': l_planck, 'delta_E_J': delta_E, 'xi_m': xi, 'a0_m': a0,
        'surface_area_m2': surface_area, 'v_layer_m3': v_layer,
        'n_layer': n_layer, 'e_layer_J': e_layer, 'e_bulk_J': e_bulk,
    }


def verify_z3_cancellation(phi_values=None):
    """Numerically re-verify Part 71 Sec 5.1-5.2: three oscillators at 0,
    2*pi/3, 4*pi/3 sum to exactly zero, and <alpha> = (1/3)*Re(exp(-i*phi)*sum)
    is exactly zero for EVERY phi (not just asserted symbolically) -- this is
    the RECHECK-required numeric sweep Part 71's own doc does not show."""
    if phi_values is None:
        phi_values = [k * math.pi / 6 for k in range(12)]   # 0..11*pi/6

    psi = [cmath.exp(1j * 2 * math.pi * k / 3) for k in range(3)]
    vector_sum = sum(psi)

    alphas = []
    for phi in phi_values:
        avg_alpha = (1.0 / 3.0) * (cmath.exp(-1j * phi) * vector_sum).real
        alphas.append(avg_alpha)

    max_abs_alpha = max(abs(a) for a in alphas)
    return {
        'psi_sum_abs': abs(vector_sum),
        'phi_values_tested': len(phi_values),
        'max_abs_average_coupling': max_abs_alpha,
        'zero_for_all_phi': max_abs_alpha < 1e-12,
    }


def compute_e115_gap():
    """Quote (not re-derive -- already independently verified in T37 /
    isotope_stability.py / Part 107) the SEMF baseline gap for Z=115.
    Re-derivation would duplicate an already-checked script; instead this
    function packages the cited numbers for use in the Sudoku-style summary
    table below, with their source made explicit."""
    return {
        'longest_lived_Z115_isotope_A': 315,   # N=200, Part 107
        'longest_lived_half_life_s': 11.0,
        'stability_target_half_life_s': 3.15e16,   # ~10^9 years, "stable" benchmark
        'gap_orders_of_magnitude': 29,
        'binding_energy_needed_MeV': (9.0, 15.0),
        'source': 'Part 107 / T37, docs/research/isotope_stability.md',
    }


def main():
    print("=" * 78)
    print("T26 (Part 135): Bob Lazar Truth Table -- Quantitative Support Checks")
    print("=" * 78)

    r1 = derive_omega_gap()
    print(f"\n[1] omega_gap = sqrt(c^5/(hbar*G)) = {r1['omega_gap_rad_s']:.4e} rad/s")
    print(f"    f_gap = omega_gap/(2*pi)        = {r1['f_gap_Hz']:.4e} Hz")

    r2 = compute_frequency_gap_ratio(r1['f_gap_Hz'])
    print(f"\n[2] f_gap / f_current_tech(1e15 Hz) = {r2['ratio']:.4e}")
    print(f"    log10(ratio)                     = {r2['log10_ratio']:.2f}  (~10^27, matches Phase 7 note)")

    r3 = compute_boundary_layer_energy(mass_kg=1.0, radius_m=0.062)
    print(f"\n[3] Boundary-layer decoupling energy (1 kg sphere, r=6.2 cm):")
    print(f"    Delta_E (per oscillator) = {r3['delta_E_J']:.4e} J")
    print(f"    N_layer (oscillator count) = {r3['n_layer']:.4e}")
    print(f"    E_layer (TOTAL)          = {r3['e_layer_J']:.4e} J")
    print(f"    E_bulk (whole-object)    = {r3['e_bulk_J']:.4e} J  (= 35% of Mc^2)")
    print(f"    Reference: Sun's total lifetime energy output ~ 1e44 J")
    print(f"    Reference: observable universe mass-energy ~ 1e69-1e70 J")
    print(f"    E_layer / (universe mass-energy ~1e70 J) = {r3['e_layer_J']/1e70:.4e}")

    r4 = verify_z3_cancellation()
    print(f"\n[4] Z3 three-source cancellation (3 emitters at 120 deg):")
    print(f"    |sum of 3 unit vectors|          = {r4['psi_sum_abs']:.4e}  (exact 0 expected)")
    print(f"    phi values swept                 = {r4['phi_values_tested']}")
    print(f"    max |<alpha>| over all phi tested = {r4['max_abs_average_coupling']:.4e}")
    print(f"    Zero for all phi tested          = {r4['zero_for_all_phi']}")

    r5 = compute_e115_gap()
    print(f"\n[5] Element 115 stability gap (quoted, Part 107/T37):")
    print(f"    Longest-lived Z=115 (SEMF baseline): A={r5['longest_lived_Z115_isotope_A']}, "
          f"T_half = {r5['longest_lived_half_life_s']} s")
    print(f"    Gap to 'stable' benchmark        = {r5['gap_orders_of_magnitude']} orders of magnitude")
    print(f"    Binding energy needed             = {r5['binding_energy_needed_MeV']} MeV")

    print("\n" + "=" * 78)
    print("Summary: energy-budget check is a clear, large-margin NEGATIVE")
    print("(E_layer exceeds even the observable universe's mass-energy by many")
    print("orders of magnitude, for a 1 kg test object); Z3 three-source")
    print("cancellation is an exact, re-verified DERIVED structural match to")
    print("the 'three emitters' claim, but a topological coincidence, not")
    print("evidence. Full interpretation in lazar_truth_table.md.")
    print("=" * 78)


if __name__ == '__main__':
    main()
