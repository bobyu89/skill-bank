# MDS Scheduling Reference (public baseline — verify current RAI manual)

Quick-reference tables backing SKILL.md. Day 1 = date of admission (or start
of Medicare Part A stay for PPS). All figures are the widely published MDS 3.0
baseline; the current RAI manual (Chapter 2) is authoritative.

## PPS (Medicare Part A / PDPM)

| Assessment | ARD window | Effect | If late |
|---|---|---|---|
| 5-Day | Days 1–8 of Part A stay | Sets PDPM classification for entire stay (absent IPA) | Default rate for days not covered by a timely assessment |
| IPA (optional) | Any day facility chooses | New classification effective from ARD forward | n/a (optional) |
| Part A PPS Discharge | End of Part A stay (resident remains) | Closes SNF QRP data collection for the stay | QRP data completeness impact |

Notes:
- The 5-Day may be combined with the OBRA Admission when windows overlap; the
  combined ARD must satisfy both windows (i.e., days 1–8).
- An interrupted stay (return within the interruption window) continues the
  original stay — no new 5-Day. Verify current interrupted-stay policy.

## OBRA (all residents, all payers)

| Assessment | Timing rule | Comprehensive? |
|---|---|---|
| Admission | Completed by day 14 | Yes (CAAs by day 14 (V0200B2); care plan within 7 days after CAA completion (V0200C2)) |
| Quarterly | ARD ≤ 92 days after previous OBRA ARD | No |
| Annual | ARD ≤ 366 days after most recent comprehensive ARD (and ≤ 92 days after last OBRA of any type) | Yes |
| Significant Change (SCSA) | Completed ≤ 14 days after determination of significant change | Yes (resets comprehensive clock) |
| Significant Correction of Prior Comprehensive (SCPA) | Completed ≤ 14 days after determining a significant error in a prior comprehensive | Yes |
| Significant Correction of Prior Quarterly (SCQA) | ARD ≤ 14 days after determining a significant error in a prior quarterly | No |

Typical steady-state cycle: Admission → Quarterly → Quarterly → Quarterly →
Annual → repeat, interrupted by SCSAs as clinically indicated.

## Discharge / entry tracking

| Record | Timing |
|---|---|
| Discharge assessment (return anticipated / not anticipated) | ARD = discharge date; complete within 14 days after the ARD (Z0500B ≤ ARD + 14) |
| Death in facility tracking | Complete within 14 days of death |
| Entry tracking record | On each admission/reentry |

## Encoding & submission (baseline)

- Encode within 7 days of completion date.
- Submit to CMS (iQIES) within 14 days of completion date.
- Track acceptance in the Final Validation Report — a submitted-but-rejected
  record is not submitted.

## Day-counting examples

- Admitted **2026-03-02** → day 1 = 3/2; day 8 (last 5-Day ARD) = **3/9**;
  day 14 (OBRA Admission completion) = **3/15**.
- Prior quarterly ARD **2026-01-10** → next OBRA ARD due by 1/10 + 92 days =
  **2026-04-12**.
- Last comprehensive ARD **2025-06-20** → annual ARD due by + 366 days =
  **2026-06-21** (but still constrained by the 92-day quarterly rule).

## PBJ baseline deadlines

See the PBJ table in SKILL.md (federal fiscal quarters, due 45 days after
quarter end). Confirm each cycle on CMS's PBJ page — dates shift for
weekends/holidays and occasional extensions.
