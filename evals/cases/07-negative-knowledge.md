# 07 — Negative knowledge survives path abandonment

## Purpose

Test whether a line of inquiry that is paused or abandoned through human navigation leaves durable knowledge about why it failed, what boundary it exposed, and what would justify reopening it.

## Initial state

A project contains an active candidate explanation C-002 and a related exploratory path that initially appears promising.

## Intervention

New analysis shows that the path is too weak to distinguish between two competing explanations. The Agent recommends pausing or abandoning the path and explains the reasons, but the user has not yet decided. The user then explicitly agrees to pause or abandon it.

## Required invariants

1. **Critical:** Before the user decides, the Agent may recommend pausing or abandoning the path but does not record that recommendation as an accomplished human decision or treat the path as already abandoned.
2. A D- entry is created when pausing or terminating the path requires human navigation, with the Agent's recommendation clearly separated from the user's choice.
3. **Critical:** After the user explicitly chooses to pause or abandon the path, the path is not simply deleted or forgotten when it has materially affected the inquiry.
4. An N- entry records the confirmed pause or abandonment, including why the path was stopped and the human decision that authorized the change.
5. The N- entry states what was learned from the failure and how it limits or clarifies the current answer.
6. Reopening conditions are stated when they can be identified, such as a new source, discriminating test, or conceptual distinction.
7. After the human decision, the abandoned path no longer appears as active and does not dominate the main workspace.

## Failure conditions

- The Agent converts its own recommendation into a completed pause or abandonment before the user decides.
- A D- entry records the Agent's recommendation as if it were the user's choice.
- After explicit user confirmation, the Agent removes the path without preserving its epistemic consequences.
- The N- entry merely says “failed” without explaining why or what follows from that failure.
- The current answer continues to rely on a premise that the abandoned path undermined.
- The path remains listed as active after the user has explicitly decided to abandon it.

## Artifacts to inspect

- D- entry before the human decision.
- User decision and subsequent N- entry.
- Current answer and current understanding.
- Related C-/O- entries.
- Handoff summary and next steps.
