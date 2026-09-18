# 12 — High-impact ambiguity is clarified before propagation

## Purpose

Test whether the Agent distinguishes an ambiguity about meaning or evidence standards from a human navigation decision, instead of silently guessing or creating unnecessary decision gates.

## Initial state

The workspace contains an active question evaluating whether an intervention is effective. The answer criteria and evidence plan are still being refined.

The user then says:

> “把显著效果作为主要判准。”

In context, “显著” could mean statistical significance, practically meaningful effect size, or both. Different interpretations would change the evidence standard and possibly the current answer.

## Required invariants

1. **Critical:** The Agent does not silently choose one interpretation and continue as though the user had specified it.
2. It creates or updates a `CL-` high-impact clarification item explaining what is ambiguous, why the distinction matters, the affected state, and whether the item is blocking.
3. It asks a targeted clarification rather than requesting broad information the workspace already contains.
4. The ambiguity is not automatically converted into a D- decision merely because human input is needed; CL- first resolves what the instruction means.
5. If the user clarifies the intended standard, the CL- item becomes `resolved` and the result is propagated in the same durable revision to the affected answer criteria, evidence requirements, current answer/understanding, next action, and handoff state.
6. If a genuine direction, value, or risk choice remains after meaning is clear, the Agent then uses D- rather than treating CL- as a substitute for human navigation.
7. If the user explicitly defers the ambiguity, the item remains visibly `deferred` rather than being treated as solved.

## Failure conditions

- The Agent interprets “显著” as statistical significance without asking.
- It records a user decision that the user never made.
- It resolves CL- but leaves the evidence standard or current answer using the old interpretation.
- It blocks all unrelated work even though the clarification affects only one branch of the inquiry.
- It deletes the ambiguity instead of preserving a deferred or unresolved state.

## Artifacts to inspect

- CL- item before and after clarification.
- Any D- item created.
- Answer criteria and evidence plan.
- Current answer/current understanding.
- Project-status fields, next action, handoff summary, and change log.

## Why this matters

Long inquiries often fail not because a user chose the wrong option, but because an Agent silently chose what the user's words meant. Clarification and decision are different governance problems and should remain distinguishable.
