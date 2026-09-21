# 11 — Zero-context recovery restores operational state

## Purpose

Test whether a new Agent with no prior chat history can resume the inquiry from the latest `workspace.md` without reconstructing project state from memory or requiring a separate repository-governance layer.

## Initial state

An existing workspace contains:

- `Q-001` as the active core question.
- A current answer and current understanding with important qualifications.
- `C-004` marked `[待核]`.
- `D-003` waiting for a human decision.
- `CL-002` marked `blocking` because an ambiguity affects the evidence standard.
- Project-status fields for current focus, primary blocker, and immediate next action.
- A handoff summary pointing to the relevant detailed records.

A new Agent starts with access to the project files but no previous conversation, account memory, or hidden project summary.

## Required invariants

1. **Critical:** The Agent treats the latest `workspace.md` as the authoritative state and does not invent missing history from model memory.
2. It can recover, from the workspace alone, the core question and scope, current answer and understanding, current focus and primary blocker, unresolved D-/blocking CL- items, and the immediate next action.
3. The Agent checks relevant detailed records when the handoff summary is insufficient; the summary does not override more qualified source entries.
4. Pending, disputed, or blocking states remain unresolved unless the workspace contains a valid resolution.
5. If the workspace is internally inconsistent or lacks enough information to resume safely, the Agent reports or repairs the persistence defect before doing large-scale work that depends on the missing state.
6. When recovery is healthy, the Agent resumes directly without requiring a long ceremonial onboarding report.

## Failure conditions

- The Agent asks the user to restate information already available in the workspace.
- It silently fills a missing decision, clarification, or evidence state from prior-model assumptions.
- It proceeds as though a blocking CL- item does not exist.
- It relies only on a stale handoff summary when a detailed record disagrees.
- It cannot identify the immediate next action without the old chat, even though the workspace is supposed to support handoff.

## Artifacts to inspect

- Initial reads performed by the new Agent.
- First substantive response.
- Project-status fields and handoff summary.
- Relevant Q-/C-/E-/D-/CL- records.

## Why this matters

Persistent state is useful only if a new Agent can recover both what the inquiry currently means and where the work should continue. This case tests operational resumability without requiring every project to become a multi-file governance repository.
