"""
T68 (g-units audit), Part 61/62 pass -- SymPy verification of the phi_-
local mass formula's units bug, traced to its exact source in
reversed_higgs.py's verify_mass_formula() (Part 62).

Reproduces:
1. The CODE's actual computation: omega = sqrt(2*OMEGA_P*Phi), then
   E_code = hbar*omega (treating OMEGA_P = m_P*c^2/hbar directly as "g").
2. The CORRECTED computation, following Part 128/T51's field-equation
   result (extended here to full SI): [g] = 1/length^2 = omega_gap^2/c^2,
   so kappa^2 = 2*g*Phi = 2*omega_gap^2*Phi/c^2 (kappa = reduced Compton
   wavenumber, 1/length), and E_correct = hbar*c*kappa (NOT hbar*omega
   directly -- kappa is not itself a frequency).
3. Verifies symbolically that E_correct / E_code = sqrt(omega_gap) EXACTLY
   (no leftover c-dependence), and confirms this reproduces the already-
   cited "4.5e14 GeV" Earth-surface endpoint from "105 eV" (T68's filing
   note), while showing the log10 swing is ~21.6 orders, not the ~42
   orders stated in phi_minus_local_mass_and_crossover.md Sec 7.

Output DATA only -- interpretation lives in docs/research/g_units_audit_scoping.md.
"""

import sympy as sp

# ---------------------------------------------------------------------
# Part 1: Symbolic derivation
# ---------------------------------------------------------------------

def symbolic_derivation():
    hbar, c, omega_gap, Phi = sp.symbols('hbar c omega_gap Phi', positive=True)

    # CODE's actual formula (reversed_higgs.py lines 505-507, 520-521):
    #   omega_code = sqrt(2 * omega_gap * Phi)      [OMEGA_P used directly as "g"]
    #   E_code = hbar * omega_code
    omega_code = sp.sqrt(2 * omega_gap * Phi)
    E_code = hbar * omega_code

    # CORRECTED formula, following Part 128's field-equation result
    # extended to this potential-curvature route (same underlying g, same
    # Lagrangian L = g*cos(psi-phi) -> [g] = 1/length^2 = omega_gap^2/c^2):
    #   kappa^2 = 2 * g_correct * Phi = 2 * (omega_gap^2/c^2) * Phi
    #   E_correct = hbar * c * kappa   (kappa is 1/length, NOT a frequency;
    #                                   the E=hbar*omega shortcut does NOT
    #                                   apply directly to kappa)
    g_correct = omega_gap**2 / c**2
    kappa_sq = 2 * g_correct * Phi
    kappa = sp.sqrt(kappa_sq)
    E_correct = hbar * c * kappa

    ratio = sp.simplify(E_correct / E_code)
    ratio_expected = sp.sqrt(omega_gap)

    residual = sp.simplify(ratio - ratio_expected)

    return {
        'E_code': E_code,
        'E_correct': sp.simplify(E_correct),
        'ratio_E_correct_over_E_code': ratio,
        'ratio_matches_sqrt_omega_gap': residual == 0,
        'residual': residual,
    }


# ---------------------------------------------------------------------
# Part 2: Numerical check against the already-cited endpoint numbers
# ---------------------------------------------------------------------

HBAR = 1.054571817e-34   # J*s
C = 2.99792458e8         # m/s
G_NEWT = 6.67430e-11     # m^3/(kg*s^2)
M_EARTH = 5.972e24       # kg
R_EARTH = 6.371e6        # m
EV_J = 1.602176634e-19   # eV -> J
GEV_EV = 1e9

M_PLANCK = (HBAR * C / G_NEWT) ** 0.5   # kg
OMEGA_GAP = M_PLANCK * C**2 / HBAR      # 1/s, Part 94's omega_P


def numerical_check():
    Phi_earth = G_NEWT * M_EARTH / (R_EARTH * C**2)

    # Code's formula
    omega_code = (2.0 * OMEGA_GAP * Phi_earth) ** 0.5
    E_code_J = HBAR * omega_code
    E_code_eV = E_code_J / EV_J

    # Corrected formula
    g_correct = OMEGA_GAP**2 / C**2
    kappa = (2.0 * g_correct * Phi_earth) ** 0.5
    E_correct_J = HBAR * C * kappa
    E_correct_eV = E_correct_J / EV_J
    E_correct_GeV = E_correct_eV / GEV_EV

    ratio_computed = E_correct_eV / E_code_eV
    ratio_predicted = OMEGA_GAP ** 0.5

    swing_log10_correct = sp.log(ratio_computed, 10).evalf()
    swing_log10_stated_in_doc = 42  # phi_minus_local_mass_and_crossover.md Sec 7 claim

    return {
        'Phi_earth': Phi_earth,
        'omega_gap': OMEGA_GAP,
        'E_code_eV': E_code_eV,
        'E_correct_eV': E_correct_eV,
        'E_correct_GeV': E_correct_GeV,
        'ratio_computed': ratio_computed,
        'ratio_predicted_sqrt_omega_gap': ratio_predicted,
        'ratio_check_close': abs(ratio_computed - ratio_predicted) / ratio_predicted < 1e-6,
        'swing_orders_of_magnitude_actual': float(swing_log10_correct),
        'swing_orders_of_magnitude_doc_claim': swing_log10_stated_in_doc,
    }


if __name__ == "__main__":
    print("=" * 78)
    print("T68 Part 61/62: phi_- local mass formula -- units bug, symbolic + numeric")
    print("=" * 78)
    print()
    sym = symbolic_derivation()
    print("E_code     =", sym['E_code'])
    print("E_correct  =", sym['E_correct'])
    print("Ratio E_correct/E_code (simplified) =", sym['ratio_E_correct_over_E_code'])
    print("Matches sqrt(omega_gap) exactly?    =", sym['ratio_matches_sqrt_omega_gap'],
          "(residual =", sym['residual'], ")")
    print()
    num = numerical_check()
    print("Numerical check (Earth surface):")
    print("  Phi_earth            = %.4e" % num['Phi_earth'])
    print("  omega_gap            = %.4e rad/s" % num['omega_gap'])
    print("  E_code (as literally coded)   = %.3e eV" % num['E_code_eV'])
    print("  E_correct (fixed)             = %.3e eV = %.3e GeV" %
          (num['E_correct_eV'], num['E_correct_GeV']))
    print("  ratio E_correct/E_code, computed  = %.4e" % num['ratio_computed'])
    print("  ratio predicted = sqrt(omega_gap) = %.4e" % num['ratio_predicted_sqrt_omega_gap'])
    print("  ratios match to 1e-6?             =", num['ratio_check_close'])
    print()
    print("  Swing, log10(ratio), ACTUAL   = %.2f orders of magnitude" %
          num['swing_orders_of_magnitude_actual'])
    print("  Swing, as stated in phi_minus_local_mass_and_crossover.md Sec 7 = %d orders"
          % num['swing_orders_of_magnitude_doc_claim'])
    print("  -> doc's '~42 orders' does NOT match either the symbolic or the")
    print("     numeric result (~21.6 orders); doc's own ENDPOINT numbers")
    print("     (105 eV -> ~4.5e14 GeV) DO match the corrected formula above.")
