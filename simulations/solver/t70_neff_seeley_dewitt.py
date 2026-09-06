"""
Part 140 (T70): N_eff via spin-weighted Seeley-DeWitt coefficient -- applicability check.

Tests two things:
1. Whether the externally-suggested formula N_eff = N_v + (11/2)*N_f + (1/6)*N_s
   can be found attributed to a citable source (documented as a negative search,
   not computed here -- see the research doc).
2. What N_eff the formula WOULD give if applied to PDTP's field content under
   the (QCD-analogy) reading that treats the 8 "gluons" as vectors and the
   24 matter species as Dirac fermions -- shown for completeness only, since
   the research doc finds this reading structurally unjustified (PDTP's own
   Lagrangian has no gauge field and no spinor field anywhere).

Output DATA only -- no physical interpretation here (see CODING_STANDARDS.md).
Interpretation lives in docs/research/neff_seeley_dewitt_applicability.md.
"""

import math

TARGET_NEFF = 6 * math.pi  # Part 83, Eq 83.1/83.6


def naive_signed_sum(n_v, n_f, n_s):
    """Part 83's original tool: N_eff = sum eps_i * nu_i (each DOF weight = 1,
    fermions negative). Reproduced here for side-by-side comparison only."""
    return n_v - n_f + n_s


def seeley_dewitt_weighted(n_v, n_f, n_s):
    """The externally-suggested spin-weighted formula, applied verbatim.
    N_v = vector bosons, N_f = Dirac fermions, N_s = real scalars."""
    return n_v + (11.0 / 2.0) * n_f + (1.0 / 6.0) * n_s


def g_ind_over_g(n_eff):
    if n_eff == 0:
        return float("inf")
    return TARGET_NEFF / n_eff


def run_scenarios():
    """PDTP field-content scenarios, per Part 83 Section 4, re-scored under
    both formulas. N_f values shown are the QCD-analogy reading (gluons as
    vectors, quark/lepton vortices as Dirac fermions) -- NOT the structurally
    justified reading, which is N_v=0, N_f=0 for all three (see doc)."""
    scenarios = [
        # name,                  N_v(QCD-analogy), N_f(QCD-analogy), N_s
        ("minimal (8 gluons)",              8,  0,  0),
        ("two-phase (+phi+/phi-)",          8,  0,  2),
        ("+matter, quarks only (18)",       8, 18,  2),
        ("+matter, full 24 species",        8, 24,  2),
    ]
    rows = []
    for name, nv, nf, ns in scenarios:
        n_naive = naive_signed_sum(nv, nf, ns)
        n_weighted = seeley_dewitt_weighted(nv, nf, ns)
        rows.append({
            "scenario": name,
            "N_v": nv, "N_f": nf, "N_s": ns,
            "N_eff_naive_signed_sum": n_naive,
            "G_ind/G (naive)": g_ind_over_g(n_naive) if n_naive > 0 else None,
            "N_eff_seeley_dewitt_weighted": n_weighted,
            "G_ind/G (weighted)": g_ind_over_g(n_weighted),
        })
    return rows


def print_report(rows):
    print("=" * 78)
    print("T70 (Part 140): Seeley-DeWitt weighted N_eff -- applicability check")
    print("Target N_eff = 6*pi = %.4f (G_ind/G = 1 exactly)" % TARGET_NEFF)
    print("=" * 78)
    print()
    print("NOTE: N_v and N_f columns use the QCD-ANALOGY reading (gluons as")
    print("vectors, matter vortices as Dirac fermions). The research doc finds")
    print("this reading structurally unjustified -- PDTP's own Lagrangian has")
    print("N_v=0, N_f=0 throughout (nonlinear sigma model, not gauge theory).")
    print("Shown for completeness: what the formula gives even if applied anyway.")
    print()
    header = "%-28s %4s %4s %4s %14s %10s %14s %10s"
    print(header % ("scenario", "N_v", "N_f", "N_s",
                    "N_eff(naive)", "G/G(naive)",
                    "N_eff(SD-wt)", "G/G(wt)"))
    for r in rows:
        g_naive = r["G_ind/G (naive)"]
        g_naive_str = "%.4f" % g_naive if g_naive is not None else "n/a"
        print(header % (
            r["scenario"], r["N_v"], r["N_f"], r["N_s"],
            "%.3f" % r["N_eff_naive_signed_sum"], g_naive_str,
            "%.3f" % r["N_eff_seeley_dewitt_weighted"],
            "%.4f" % r["G_ind/G (weighted)"],
        ))
    print()
    print("Structurally-justified case (N_v=0, N_f=0 always, per the doc):")
    for ns in (8, 10, 34):
        n_eff = seeley_dewitt_weighted(0, 0, ns)
        print("  N_s=%2d (Part 83 scalar count) -> N_eff(SD-weighted)=%.4f, "
              "G_ind/G=%.4f" % (ns, n_eff, g_ind_over_g(n_eff)))
    print()
    print("Compare Part 83's own scalar-only (unweighted, 1-per-scalar) result:")
    for ns in (8, 10, 34):
        print("  N_s=%2d -> N_eff(Part 83 convention)=%.3f, G_ind/G=%.4f"
              % (ns, ns, g_ind_over_g(ns)))


if __name__ == "__main__":
    rows = run_scenarios()
    print_report(rows)
