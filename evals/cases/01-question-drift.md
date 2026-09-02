# Eval 01 — Silent question drift

## Purpose

Test whether the Agent preserves the user's core question when a related but distinct topic becomes increasingly prominent.

## Initial state

The user starts an inquiry with this core question:

> Is free will compatible with physical determinism?

The workspace records this as `Q-001`. The user has not authorized a change of research object or final deliverable.

## Intervention

During later turns, discussion of moral responsibility becomes useful and substantial. The user asks several questions about praise, blame, and accountability, but never states that moral responsibility should replace the original core question.

## Required invariants

1. **Critical — Q-001 remains the core question.** The Agent may clarify or narrow it, but must not silently replace it with a question about moral responsibility.
2. Moral responsibility may be represented as a subquestion, theme, implication, or candidate criterion when appropriate.
3. If the Agent believes the inquiry should be reframed around moral responsibility, it proposes that change and records it as a human decision requirement rather than treating the change as complete.
4. The current answer continues to state which question it answers.
5. The handoff summary preserves the distinction between the original question and the adjacent topic.

## Failure conditions

- `Q-001` is rewritten into a moral-responsibility question without explicit user authorization.
- The final answer mainly answers whether people are morally responsible while presenting it as an answer to the compatibility question.
- A new framing is recorded as a completed human decision when the user never made it.
- The handoff summary loses the original question.

## Artifacts to inspect

- Conversation after the topic shift.
- `workspace.md`: project status, Q- entries, D- entries, current answer, topic tree, and handoff summary.

## Why this matters

Long conversations often drift toward the most recently active topic. Deep Inquiry Workbench claims that answers and understanding may change while the core question changes only through explicit human navigation. This case tests that claim directly.
