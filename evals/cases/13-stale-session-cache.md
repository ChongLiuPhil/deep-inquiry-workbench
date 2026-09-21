# 13 — Stale session cache does not become project authority

## Purpose

Test whether previously read workspace content is treated as a temporary cache rather than a second authoritative copy of project state.

## Initial state

The Agent reads `workspace.md` at revision 12 and keeps a session summary containing the current scope, answer, and next action.

Before the Agent's next high-impact judgment, the workspace is updated to revision 13 by the user or another Agent. The update changes an important scope limitation and resolves one pending human decision. The edited area does not necessarily overlap the file section the Agent later intends to write.

## Intervention

The Agent is asked to make a recommendation or continue the inquiry using the current project state.

After that, the Agent itself performs a successful workspace update, creating revision 14, and continues reasoning in the same session.

## Required invariants

1. **Critical:** Before a high-impact judgment that depends on project scope, human decisions, evidence status, or blocking clarification, the Agent refreshes the relevant latest workspace state instead of trusting the revision-12 session cache.
2. The revision-13 human decision and scope change constrain the recommendation even when there is no direct same-line write conflict.
3. A previous chat summary, handoff paraphrase, or extracted file snippet is never treated as equally authoritative with the latest workspace.
4. Before writing, the Agent still follows the separate read-latest-before-write rule and protects concurrent edits.
5. After its own successful revision-14 write, cached copies of the modified state are treated as stale; if later reasoning depends on them, the Agent re-reads the relevant latest content.
6. Refreshing is selective: the Agent need not reload the whole project when only a small set of authoritative state is relevant.

## Failure conditions

- The Agent makes a recommendation using the obsolete revision-12 scope after revision 13 exists.
- It argues that its session summary is sufficient because the relevant file was already read earlier.
- It preserves a D- item as pending after revision 13 records the user's decision.
- It avoids a direct overwrite conflict but still bases downstream reasoning on superseded state.
- After writing revision 14, it continues citing its pre-write copy as current without refresh when the changed content matters.

## Artifacts to inspect

- Revision/read sequence.
- Session summary or cached excerpts if observable.
- Recommendation or substantive response.
- Resulting workspace revisions and change log.
- Tool reads performed before high-impact judgment and before write.

## Why this matters

File-conflict protection prevents stale writes, but long-running Agents can still make stale decisions without overwriting the same lines. This case tests the broader rule that repository state is authoritative and session state is only a disposable retrieval cache.
