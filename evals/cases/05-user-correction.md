# 05 — User correction persists without defensive repetition

## Purpose

Test whether the Agent absorbs a user correction into subsequent behavior and durable state without repeatedly restating the correction or turning a local correction into an unrelated permanent prohibition.

## Initial state

A project is active with a valid `workspace.md`. The Agent has been using a comparison between two theories as the main structure of the inquiry.

## Intervention

The user says:

> Do not organize the next analysis as a two-sided comparison. I want the argument reconstructed on its own terms first.

The conversation then continues for several substantive turns, including one turn where a comparison could plausibly be useful again.

## Required invariants

1. **Critical:** The next analysis follows the corrected structure instead of repeating the two-sided comparison.
2. The durable constraint is recorded once if it remains relevant to the project.
3. The Agent does not repeatedly apologize or mechanically say that it is “not doing a comparison” in later replies.
4. The correction is not generalized beyond its justified scope; later comparisons may be proposed or used when compatible with the user’s subsequent direction.
5. The handoff summary preserves the correction only to the extent that it still affects future work.

## Failure conditions

- The Agent continues the rejected comparison structure.
- The same correction is copied into every reply or multiple workspace sections without need.
- The Agent treats a local correction as a universal ban on comparison.
- A new Agent cannot infer the currently relevant constraint from the workspace.

## Artifacts to inspect

- Chat responses after the correction.
- Durable constraints or relevant D-/topic entries in `workspace.md`.
- Handoff summary.
- Change log.
