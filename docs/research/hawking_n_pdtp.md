# Hawking Temperature with n_PDTP = 1/alpha — T7 / Part 111

**Status:** DONE (CONSTRUCTIVE NEGATIVE + one PDTP Original)
**Part:** 111 | **Phase:** 79 | **Date:** 2026-05-17
**Script:** `simulations/solver/t7_hawking_n_pdtp.py`
**Log:** `simulations/solver/outputs/hawking_n_pdtp_<ts>.txt`
**SymPy:** 5/5 PASS | **Sudoku:** 12/12 PASS
**Verdict:** T_H^PDTP = T_H^GR — the PDTP refractive index does not modify
the Hawking temperature. New PDTP formulation of κ in terms of n (Eq 111.4).

---

## Plain English Summary

In PDTP, spacetime near a black hole acts like an optical medium with a
refractive index n = 1/α that grows without bound as you approach the horizon
(α → 0, n → ∞). You might expect this to dramatically change Hawking radiation.

It does not — and the reason is instructive.

Hawking radiation depends on the **surface gravity κ**, which measures how
steeply the gravitational potential drops near the horizon. In PDTP, the
potential is α², and its gradient ∂_r(α²) = r_S/r² is perfectly finite at
r = r_S even though α itself → 0. The temperature therefore stays the same.

The deeper reason: n = 1/α affects how fast the *phase* of a wave oscillates
near the horizon (the phase velocity c_phase = c/n → 0). But Hawking radiation
is set by how fast *information* propagates — the group velocity c_group = c_s = c,
which PDTP always keeps equal to c (Part 34). Phase and group velocity decouple
near the horizon, and the temperature follows the group velocity.

**What is new:** Expressing κ in terms of n gives a clean PDTP reformulation:
κ = (c²/2)|∂_r(1/n²)|_{r_S}. This states that the surface gravity equals the
gradient of n⁻² at the horizon — the rate at which the medium becomes
transparent again moving away from the black hole.

---

## 1. Setup

PDTP refractive index (Part 98, Eq 108.1):
```
n(r) = 1/α(r),    α(r) = sqrt(1 − r_S/r),    r_S = 2GM/c²
```

Profile near horizon:

| r/r_S | α | n = 1/α | c_phase/c |
|-------|---|---------|-----------|
| 1.01 | 0.100 | 10.05 | 0.100 |
| 1.10 | 0.302 | 3.32 | 0.302 |
| 2.00 | 0.707 | 1.41 | 0.707 |
| 10.0 | 0.949 | 1.054 | 0.949 |

As r → r_S: α → 0, n → ∞, c_phase → 0. The phase velocity vanishes at the horizon.

---

## 2. Surface Gravity from the Lapse Function

**Eq 111.2** [Part 98, ESTABLISHED]:
```
α(r) = sqrt(1 − r_S/r),    α² = 1 − r_S/r
```

**Eq 111.3** [DERIVED, SymPy S1–S2]:
```
∂_r(α²) = r_S/r²

At r = r_S:    ∂_r(α²)|_{r_S} = r_S/r_S² = 1/r_S   (finite)

κ = (c²/2)|∂_r(α²)|_{r_S} = c²/(2r_S)
```

Key observation: even though α → 0 at the horizon, its **square** α² has a
finite, non-zero gradient there. The surface gravity κ is therefore finite and
equal to the standard GR result.

For a 1-solar-mass black hole:
- r_S = 2.95 km
- κ = 1.52×10¹³ m/s² = 1.55×10¹² g

---

## 3. Surface Gravity in Terms of n (PDTP Original)

Since α = 1/n, we have α² = 1/n². Therefore:

**Eq 111.4** [PDTP Original, SymPy S3]:
```
κ = (c²/2)|∂_r(1/n²)|_{r_S}
```

This is an equivalent formulation of Eq 111.3, expressed purely in terms of
the PDTP refractive index. It says:

> The surface gravity is the gradient of n⁻² at the horizon.

Since 1/n² = 1 − r_S/r, this gradient is 1/r_S — same as before.

**Why n → ∞ does not mean κ → ∞:** Although n diverges at r_S, the quantity
1/n² → 0 smoothly, and its gradient is finite. The Hawking temperature depends
on ∂_r(1/n²), not on n itself.

---

## 4. Hawking Temperature: T_H^PDTP = T_H^GR

**Eq 111.5** [DERIVED, SymPy S4]:
```
T_H = ħκ/(2πck_B) = ħc³/(8πGMk_B)   [same as Part 24]
```

For 1 M_sun: T_H = 6.17×10⁻⁸ K.

T_H scales as 1/M (larger black holes are cooler). Verified: T_H(2M)/T_H(M) = 1/2.

---

## 5. Why Phase Velocity Does Not Affect T_H

**Eq 111.6** [ESTABLISHED, Part 98]:
```
c_phase(r) = c·α(r) = c/n(r) → 0   as r → r_S
```

**Eq 111.7** [Part 34, ESTABLISHED]:
```
c_group = c_s = c   (constant everywhere in PDTP)
```

The Hawking mechanism (Unruh 1981 acoustic analogy) depends on the surface
gravity of the acoustic metric:

```
κ_acoustic = (1/2)|∂_r(c_s² − v²)|_{r_S}
```

where v(r) = −c√(r_S/r) is the Painlevé-Gullstrand infall velocity (Part 101)
and c_s = c is the sound speed (Part 34).

Computing at r = r_S:
```
∂_r(c_s² − v²) = ∂_r(c² − c²r_S/r) = c²r_S/r²

At r_S:   c²/r_S

κ_acoustic = c²/(2r_S)   — same as Eq 111.3
```

This derivation uses **c_s = c** (group velocity, Part 34) — not c_phase = c/n.
The refractive index enters c_phase but not the acoustic surface gravity,
which depends only on the gradient of (c_s² − v²).

**Three routes to the same κ:**
1. Lapse gradient: κ = (c²/2)∂_r(α²)|_{r_S}       [Eq 111.3]
2. Refractive index: κ = (c²/2)∂_r(1/n²)|_{r_S}    [Eq 111.4]
3. Acoustic: κ = (1/2)|∂_r(c_s² − v²)|_{r_S}        [Unruh 1981]

All three give κ = c²/(2r_S). Sudoku S09 verifies routes 1 and 3 agree.

---

## 6. Breathing Mode Spectrum Modification

**Eq 111.8** [DERIVED]:
```
Breathing mode emission spectrum:
  n_Planck(ω)   for ω >> ω_gap     (standard Planck)
  suppressed     for ω < ω_gap      (mass gap cutoff)

ω_gap = sqrt(2g_eff) = sqrt(2 × 2.4×10⁻³⁶) ≈ 2.2×10⁻¹⁸ rad/s   [Part 99]
T_cutoff = ħω_gap/k_B ≈ 1.7×10⁻²⁹ K
```

For any astrophysical black hole: T_H >> T_cutoff. For a solar-mass BH:
T_H/T_cutoff ≈ 6×10⁻⁸/10⁻²⁹ ≈ 10²². The breathing mode emission is completely
unsuppressed — the mass gap is utterly negligible at any astrophysical T_H.

**T_H itself is unchanged.** Only the theoretical spectrum shape differs below ω_gap,
which is at a frequency 10²² times below the peak emission frequency.

---

## 7. Two-Phase and Birefringence Checks

**Eq 111.9** [VERIFIED against Part 61]:

Part 61 derived G_eff = 2G_bare (Newton's 3rd law factor). Since laboratory
measurements of Newton's constant give G_N = G_eff (the effective value):

```
T_H = ħc³/(8πG_N M k_B)   [uses G_N = G_eff]
```

The factor-of-2 in G_eff/G_bare does not change T_H in terms of the observed G_N.
If expressed in terms of G_bare: T_H^bare = 2 × T_H^eff — but G_bare is not
directly measurable.

**Birefringence check (T4 cross-check):**

T4 (Part 108) showed that the + and × GW polarizations have different Brewster
angles at density boundaries, due to the TE vs TM nature of the two polarizations.
However, **both polarizations share the same n(r) = 1/α(r) profile**, so both
have the same κ and the same T_H. Birefringence splits Brewster angles but not
Hawking temperatures.

T_H(+) = T_H(×) = 6.17×10⁻⁸ K (1 M_sun).

---

## 8. Sudoku Score: 12/12 PASS

| Test | Description | Result |
|------|-------------|--------|
| S01 | α(r_S) = 0 (horizon condition) | PASS |
| S02 | α(100 r_S) ≈ 1 (asymptotically flat) | PASS |
| S03 | n(1.001 r_S) >> 1 (n → ∞ at horizon) | PASS |
| S04 | κ = c²/(2r_S) from lapse gradient | PASS |
| S05 | κ_n = κ_α (Eqs 111.3 and 111.4 agree) | PASS |
| S06 | T_H(Part 24) = T_H(κ) | PASS |
| S07 | c_phase(r_S) = 0 (Eq 111.6) | PASS |
| S08 | c_group = c_s = c (Eq 111.7, Part 34) | PASS |
| S09 | κ_acoustic = κ_lapse (two routes) | PASS |
| S10 | T_H(2M) = T_H(M)/2 (1/M scaling) | PASS |
| S11 | T_H^PDTP = T_H^GR (Eq 111.5) | PASS |
| S12 | T_H(+) = T_H(×) (birefringence no effect) | PASS |

---

## 9. SymPy Verification: 5/5 PASS

| Check | Statement | Result |
|-------|-----------|--------|
| S1 | ∂_r(α²)\|_{r_S} = 1/r_S | PASS |
| S2 | κ = c²/(2r_S) from S1 | PASS |
| S3 | ∂_r(1/n²)\|_{r_S} = ∂_r(α²)\|_{r_S} | PASS |
| S4 | T_H = ħc³/(8πGMk_B) from κ and r_S = 2GM/c² | PASS |
| S5 | T_H(M)/T_H(2M) = 2 (1/M scaling) | PASS |

---

## 10. Summary of Connections

| Item | Connection |
|------|-----------|
| Part 24 | T_H formula confirmed; κ derivation extended to PDTP framework |
| Part 34 | c_s = c is the key: group velocity unchanged → κ unchanged |
| Part 98 (T1) | n = 1/α derived there; Eq 111.4 is the natural Hawking reformulation |
| Part 101 (T21) | PG infall v(r) = −c√(r_S/r) used in acoustic κ derivation |
| Part 61 | G_eff = 2G_bare — T_H unchanged in terms of observed G_N |
| T4 (Part 108) | Birefringence (+ vs ×) does not split T_H; both share same α(r) |
| T6 (Part 110) | Leidenfrost critical point V″=0 is where n → ∞ and κ would diverge *if* κ depended on n — but it does not (κ depends on ∂n⁻², not n) |

---

## 11. Open Questions

- [ ] Does the PG flow v(r) arise naturally from the PDTP Lagrangian, or is it
  an ansatz? Part 101 showed the linearized flow is 12 orders too small — this
  gap in the derivation is still open.
- [ ] Does the PDTP breathing mode have a modified greybody factor (transmission
  probability) even though T_H is unchanged? This would affect the luminosity
  (total power) of the Hawking emission but not its temperature.
- [ ] Two-phase (T9): the reversed Higgs phi_- mass m² = 2gΦ diverges near matter.
  Does this add a correction to κ that was missed here?

---

## Sources

- **Source:** Part 24 — Hawking temperature derivation T_H = ħc³/(8πGMk_B)
- **Source:** Part 98 (T1) — PDTP refractive index n = 1/α
- **Source:** Part 34 — c_s = c in PDTP condensate
- **Source:** Part 101 (T21) — Painlevé-Gullstrand infall velocity
- **Source:** Part 61 — G_eff = 2G_bare (two-phase Lagrangian)
- **Source:** Unruh (1981), Phys. Rev. Lett. 46 — acoustic Hawking radiation
- **Source:** Visser (1998), Class. Quant. Grav. 15 — acoustic black holes
- **PDTP Original:** Eq 111.4 — surface gravity as gradient of n⁻²:
  κ = (c²/2)|∂_r(1/n²)|_{r_S}
