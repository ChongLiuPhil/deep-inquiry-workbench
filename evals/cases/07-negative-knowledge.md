# 07 — Negative knowledge survives path abandonment

## Purpose

Test whether abandoning a line of inquiry produces durable knowledge about why it failed, what boundary it exposed, and what would justify reopening it.

## Initial state

A project contains an active candidate explanation C-002 and a related exploratory path that initially appears promising.

## Intervention

New analysis shows that the path is too weak to distinguish between two competing explanations, so the Agent recommends stopping work on it.

## Required invariants

1. **Critical:** The abandoned path is not simply deleted or forgotten when it has materially affected the inquiry.
2. An N- entry records why the path was abandoned or suspended.
3. The N- entry states what was learned from the failure and how it limits or clarifies the current answer.
4. Reopening conditions are stated when they can be identified, such as a new source, discriminating test, or conceptual distinction.
5. The abandoned path does not dominate the main workspace after it ceases to be active.

## Failure conditions

- The Agent removes the path without preserving its epistemic consequences.
- The N- entry merely says “failed” without explaining why or what follows from that failure.
- The current answer continues to rely on a premise that the abandoned path undermined.
- The path remains listed as active after being abandoned.

## Artifacts to inspect

- N- entry.
- Current answer and current understanding.
- Related C-/O- entries.
- Handoff summary and next steps.
