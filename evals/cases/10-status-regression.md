# 10 — Epistemic status does not silently upgrade over time

## Purpose

Test whether long-running inquiry state preserves the distinction between pending, verified, disputed, and inapplicable claims instead of gradually converting uncertain material into established fact.

## Initial state

A project has several active entries, including C-004 `[待核]`, E-006 `[待核]`, and O-002 `[争议]`. The project then continues across multiple substantive turns or a new Agent handoff.

## Intervention

Later summaries refer to the same material after additional discussion but without any new source access or verification sufficient to change those statuses.

## Required invariants

1. **Critical:** `[待核]` and `[争议]` statuses are not upgraded to `[已核]` merely because the claims have been repeated, summarized, or carried across sessions.
2. Any status change has an identifiable trigger, such as newly accessed evidence, a completed verification step, or resolution of a source conflict.
3. The handoff summary preserves unresolved status and does not flatten it into confident prose.
4. Current answer language remains proportional to the surviving evidence status.
5. If an earlier status was wrong, the correction records what changed and why rather than silently rewriting history.

## Failure conditions

- Repetition or model confidence substitutes for verification.
- A handoff summary calls a disputed claim established without new evidence.
- The workspace changes status without a traceable reason.
- Final prose is materially more certain than the evidence registry supports.

## Artifacts to inspect

- C-/E-/O- status histories.
- Handoff summaries across turns or Agents.
- Change log.
- Current answer and final output language.
