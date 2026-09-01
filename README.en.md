# Deep Inquiry Workbench

[中文](README.md) | [English](README.en.md)

Deep Inquiry Workbench is a deep-inquiry workflow that can be used by different AI agents. Through explicit reasoning, evidence, and documentation protocols, it expands what AI can do in analysis, search, comparison, verification, and knowledge integration. It helps anyone investigate an important, difficult, or open question by continually generating, testing, and revising answers and understanding, while preserving the state of the inquiry in a dynamic Markdown workspace that can be opened locally.

It has two closely connected purposes. First, it uses the AI's abilities in analysis, search, comparison, verification, and organization to make real progress on a person's inquiry. Second, its visible practices of evidence assessment, concept clarification, counterexample testing, and direction-setting help the person improve language judgment and the quality of their thinking about knowledge. This educational effect is built into the inquiry; it does not replace the inquiry itself.

Users do not need to decide whether their question belongs to the humanities, science, technology, everyday life, or another field. The workflow does not require a dedicated user interface.

## Core Position

This project treats inquiry as the basic process.

Traditional “learning” is often imagined as absorbing stable knowledge that already exists. Yet existing knowledge is itself the provisional result of earlier inquiry. It has a scope, methods, evidence, and historical conditions, and it may later be revised.

For that reason, this workflow does not keep learning as a separate process alongside inquiry. Reading, searching, remembering, practicing, calculating, experimenting, and writing occur naturally when they are needed to answer a concrete question. What changes over time is the answer and the understanding. The question guides the process, and major changes to it require explicit confirmation.

In this process, AI is both a generative inquiry tool and an interface to existing human knowledge. The workflow enables it to draw on prior knowledge, external sources, and available tools; generate candidate explanations; inspect reasoning; compare evidence; preserve the evolution of ideas; and turn scattered information into understanding that can be tested and revised further.

## How the Two Purposes Work Together

The Skill is first of all an engineering tool. It must improve the actual quality of inquiry rather than merely teach methods. The AI should perform the reading, searching, structural analysis, comparison of explanations, search for counterexamples, calculation, verification, and synthesis that it can reliably perform. This frees the user's attention from repetitive information work so it can be used to define the question, compare directions, and form judgments.

At the same time, the workflow does not hide the thinking process behind a polished answer. The support for claims, jumps in reasoning, boundaries of concepts, competing explanations, uncertainty, and choices of direction remain visible. By repeatedly engaging with those acts of judgment in real inquiries, users can strengthen their language judgment, evidence awareness, and ability to think about knowledge.

This educational function is not a separate course, and it should not turn every response into a lecture about method. It is integrated into the inquiry and serves the inquiry. If an educational explanation does not change the current understanding or action, it should not displace the substantive work.

## Faithful Execution: Neither Underperform nor Overstep

The Skill treats precise controllability as an operational rule for the agent, not merely as a conversational style. The AI should resemble a powerful vehicle with accurate controls: as its capabilities increase, it must understand the goal and boundaries more precisely and use its abilities fully within them.

- When the goal is clear, the agent proactively performs the necessary reading, analysis, execution, verification, and workspace updates.
- “Avoiding overreach” is not an excuse to omit necessary work.
- “This might be helpful” is not permission to add deliverables, features, files, refactoring, external actions, or adjacent tasks.
- Any expansion that changes the deliverable, main goal, affected scope, cost, risk, or external state must first be decided by the user.
- After a correction, the agent should absorb it into subsequent action rather than repeatedly apologizing, restating prohibitions, or listing irrelevant things it did not do.

Faithfulness is therefore neither literal passivity nor an attempt to produce a supposedly “more complete” result on its own initiative. It means using the AI's abilities fully within a clear goal and authorized scope while ensuring that each action remains responsive to the task at hand.

## Problems It Addresses

Ordinary chat often breaks down in three ways:

1. Answers accumulate in chronological order, while the discussion grows without becoming a structure that can support continued work.
2. The AI forgets earlier constraints or quietly changes the user's original question in later turns.
3. Fluent writing, unverified information, interpretation, and factual evidence become mixed together.

The Skill addresses these problems with a continuously maintained `workspace.md`. The document is organized by questions and themes. It preserves the current answer, current understanding, claims, evidence, counterexamples, abandoned paths, confirmed decisions, next steps, and handoff state.

## Core Capabilities

- **Question governance:** The question guides the inquiry. The AI may clarify wording, narrow scope, and create subquestions, but a change to the core question requires explicit confirmation.
- **Evolving answers and understanding:** Answers and understanding are continually generated, tested, and revised. The workflow does not repeatedly rewrite the question merely to create an appearance of progress.
- **Different standards for different kinds of claims:** Facts, attribution of theories, interpretations, speculation, value judgments, and original synthesis are kept distinct and checked in ways appropriate to each.
- **Calibrated criticism:** The agent first reconstructs a view fairly, then uses strong objections, counterexamples, boundary cases, or competing explanations when they can improve understanding. Criticism is a tool, not a ritual required in every turn.
- **Concept formation and testing:** A new concept is retained only when it adds real power to distinguish, explain, or guide action. Its definition, boundaries, positive and negative examples, and formation history are recorded.
- **Learning from abandoned paths:** The workspace records why a path failed, what limitation it exposed, and what future condition might justify reopening it, rather than preserving only successful answers.
- **Explicit decision records:** Changes to the core question, main goal, value tradeoffs, risk acceptance, and final adoption require explicit confirmation and are preserved as D-entries. Silence is not treated as consent.
- **Long-term continuity:** State is written to a local workspace so that a new session or agent can continue without relying on the original chat window.
- **Precisely controlled execution:** The agent works fully within the user's defined goal without underperforming or adding work on its own. Corrections are incorporated naturally rather than repeated as defensive disclaimers.

## Why No Dedicated UI Is Required

The workspace itself is the persistent interface:

- It is ordinary Markdown and can be opened in any local editor.
- The user can edit it directly, and the agent must read the latest version before writing again.
- A new session or another agent can restore the inquiry from the document.
- Every response reports whether the document was updated, what changed, and its absolute path.
- If the environment is not writable, the agent must report the failure and provide recoverable content rather than pretending the save succeeded.

Platforms that support local file links can open the document directly. Other platforms can still display its absolute path.

## Plain Language by Default

The Skill assumes by default that the human participant has no specialist background in the current field. Chat responses, workspace content, and final deliverables should use ordinary and direct language first.

- Do not use professional jargon or school-specific terminology when ordinary words are accurate.
- When a technical term is necessary, explain it immediately in everyday language at its first appearance.
- Spell out an abbreviation the first time and explain its purpose.
- Do not present long strings of theories, people, or terms from multiple fields.
- Do not substitute a label for an explanation of how something happens, what supports it, and why it matters.
- Give the central meaning first, then add precise detail and sources as needed.

Plain language does not mean sacrificing accuracy. Important conditions, exceptions, uncertainty, and counterexamples remain present. The goal is to avoid imposing the additional burden of specialist language on the user.

## When to Use It

Good uses include:

- Understanding an everyday, social, theoretical, or practical question in depth.
- Comparing competing explanations or possible solutions.
- Investigating scientific, technical, humanistic, or cross-disciplinary questions.
- Integrating reading, literature, data, or existing materials into an ongoing inquiry.
- Developing concepts, testing arguments, organizing evidence, or producing a report.
- Preserving long-term thinking across sessions or agents.

It is usually unnecessary for:

- A question for which one simple fact is sufficient.
- A clearly specified task that only needs execution.
- One-time translation, proofreading, formatting, or stylistic editing.
- Ordinary questions that do not require depth or persistent state.

The user may still invoke the Skill explicitly for any task.

## Workflow

### First Start

Each inquiry is a self-contained local project. If the user specifies an existing project directory, the agent uses it. Otherwise, the agent creates a short topic directory in the location selected by the user or in the current workspace:

```text
<topic-project-directory>/
├── workspace.md
├── materials/       # Materials the user asks to bring into the project
├── attachments/     # Longer evidence, search, calculation, or experiment records
└── outputs/         # Reports, plans, and finished drafts
```

`workspace.md` is located directly in the project root. The other directories are created only when they contain real files. All persistent files and subsequent agent updates remain inside the project directory.

The agent writes the complete user guide into the workspace, shows a concise summary in chat, and provides the file path. Substantive inquiry begins only after the user replies “I acknowledge” or gives an equally clear confirmation.

The first-start guide is not an ordinary disclaimer. It ensures that the user knows that fluency is not correctness; model output is candidate material; the AI may agree too readily with existing views or reflect biases in its training material; important changes of direction and real-world adoption require explicit confirmation; and the workflow will expose evidence gaps, hidden assumptions, counterexamples, and uncertainty. Each project normally requires confirmation only once.

### Every Substantive Turn

The agent:

1. Reads the workspace to restore the current state.
2. Checks the current goal, requested deliverable, authorized scope, and any expansion requiring a new decision.
3. Identifies the most important gap in the current understanding.
4. Chooses the smallest set of actions that can fully advance or verify the goal.
5. Generates or revises the answer and understanding.
6. Integrates durable changes into the appropriate themes and stable identifiers.
7. Updates the revision number, handoff summary, and concise change log.
8. Ends the response with a workspace receipt.

Receipt format:

```text
Workspace
- Status: updated / no update needed / update failed
- Changes this turn: revision 4; C-003 revised; E-005 added as pending verification
- Path: /absolute/path/to/topic-project/workspace.md
```

“No update needed” is a real state. Pure confirmation, explanation of the protocol, or a response that creates no durable change does not add noise merely to satisfy a form.

## Document Model

The workspace uses stable identifiers:

| Prefix | Object |
|---|---|
| `Q-` | Question |
| `C-` | Claim, candidate answer, or argument |
| `E-` | Evidence or source record |
| `O-` | Objection, counterexample, or competing explanation |
| `N-` | An abandoned path and what was learned from its failure |
| `D-` | A decision about direction, scope, values, risk, or stopping that requires explicit confirmation |

Questions and answers are managed separately. The core question normally remains stable while answers, explanations, evidence status, and boundaries of application may change. A major reframing of the question requires an explicitly confirmed `D-` decision.

The workspace also separates how an item was formed, whether it is currently retained, and whether it has been verified. “Suggested by AI,” “currently retained,” and “verified” are not treated as the same status.

It further distinguishes:

- **Current answer:** The most concise defensible response to the core question at this point.
- **Current understanding:** The mechanisms, concept relationships, evidence, uncertainty, competing explanations, and boundaries that support the answer.

An answer may not yet exist, or multiple competing versions may remain active. When evidence is insufficient, the relevant item stays marked as pending verification rather than being forced into a complete conclusion.

## Evidence and Criticism

The project does not mechanically challenge every sentence or require every turn to end with an open question. After reconstructing a position fairly, the agent selects what the current bottleneck requires:

- Logical review.
- A strong objection or counterexample.
- Comparison of competing explanations.
- Concept clarification.
- External search and evidence verification.
- A thought experiment, calculation, or test.
- Abandoning an unproductive path or integrating a deliverable.

Different statements require different checks. Facts and numbers need reliable sources. A claim about an author's view should return to the original text. An interpretation should identify its material support, reasoning, counterexamples, and scope. A value judgment should state the values on which it depends. The model's internal memory, confident wording, agreement among multiple models, and AI-generated citations are not evidence by themselves.

The workflow does not impose fixed research stages. Each turn first determines whether the current gap lies in an unclear question, an ambiguous concept, missing evidence, competing explanations, broken reasoning, a value choice, or the integration of a deliverable. It then selects the few actions most likely to add understanding. When essential evidence is unavailable, the relevant conclusion is paused rather than concealed with additional prose.

## Repository Structure

```text
deep-inquiry-workbench/
├── SKILL.md
├── README.md
├── README.en.md
├── LICENSE
├── NOTICE
├── CONTRIBUTING.md
└── resources/
    ├── user_guide.md
    └── workspace_template.md
```

- `SKILL.md`: The complete decision protocol executed by the agent. All rules that materially affect behavior remain here.
- `README.md`: The full Chinese project description, usage guide, and compatibility notes.
- `README.en.md`: The corresponding English version.
- `resources/user_guide.md`: The complete guide written into a workspace at first start.
- `resources/workspace_template.md`: The authoritative workspace template.

Version 1 requires no scripts. Evidence records, concept cards, reflection, and handoff state are integrated into one main template rather than split into several active documents. Large evidence collections, search logs, calculation results, or drafts become attachments only when keeping them in the main workspace would impair readability.

## Installation and Invocation

Install the complete `deep-inquiry-workbench` directory in the Skills directory supported by the target agent. A common local Codex installation is:

```text
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git ~/.codex/skills/deep-inquiry-workbench
```

Explicit invocation:

```text
$deep-inquiry-workbench Help me investigate: Why ...?
```

Natural-language invocation:

```text
Do not give me only a final answer. Help me investigate this question systematically and keep a persistent record of how our understanding changes.
```

Agent platforms differ in automatic Skill discovery, local file links, and write permissions. The full workflow requires an agent that can read the Skill resources and create and update Markdown files in the user's workspace.

## License and Contributions

This is a **source-available project with limited permission**. It is not open-source software that may be freely modified and republished.

- Individuals and organizations that qualify under the license may install and invoke the unmodified Skill for noncommercial purposes.
- Commercial use, publication of modified versions, independent derivative projects, and redistribution outside GitHub's own functionality are not permitted.
- GitHub's rules for public repositories allow viewing and forking on the platform. A fork does not grant permission for commercial use, independent publication of a modified version, or redistribution outside GitHub.
- Issues and contributions to the official repository are welcome. The limited permission to prepare a contribution and the terms for submitted contributions are in [CONTRIBUTING.md](CONTRIBUTING.md).

The project uses the [PolyForm Strict License 1.0.0](LICENSE), with `ChongLiuPhil` as the copyright holder. The license permits noncommercial use but does not grant permission to modify or distribute the project. This section is a summary; if there is any difference, the complete text of `LICENSE` and `CONTRIBUTING.md` controls.

## Continuation Across Agents

A new agent first reads `workspace.md`, then checks the original entries relevant to the current task. The handoff summary is a state snapshot; it does not replace detailed evidence, constraints, or confirmed decisions.

One agent continues the inquiry by default. Additional agents are used only for genuinely independent review, role separation, clearly separable parallel work, or an explicit user request. Agreement among multiple agents is not evidence and is not decided by vote.

## How the Two Prototypes Were Integrated

The project uses the more mature engineering structure of `conduct-humanities-ai-research` as its foundation:

- A workspace organized by themes.
- Stable Q/C/E/O/N/D identifiers.
- Independent status dimensions.
- Evidence checking, explicit decision gates, learning from failed paths, and a handoff summary for new agents.

It also preserves the distinctive contributions of `human-ai-research-os`:

- A first-start guide that develops judgment about AI output.
- Clear warnings about fluency, excessive agreement, bias, and loss of context.
- Records of four kinds of change—confirmation, revision, a valuable candidate introduced by AI, and deeper understanding after the user rejects an AI suggestion—together with the formation of concepts and reasons for abandoning paths.
- Recognition that choosing, revising, and abandoning paths are forms of higher-level cognitive work.

The integration makes three important changes:

1. It generalizes the workflow from humanities research to inquiry about any question.
2. It replaces the idea of an equal AI research partner with an emphasis on AI as a capable, bounded, and verifiable inquiry tool.
3. It replaces fixed stages, mandatory objection, and turn-by-turn forms with a dynamic workflow driven by the current gap in understanding.

## Limitations

- Without write permission, the Skill can only produce a structured update to be saved later; it cannot maintain local state itself.
- The workspace reduces loss of context, but it cannot guarantee that every agent will interpret or follow the protocol correctly.
- Evidence quality still depends on the sources, tools, time, and verification methods that are actually available.
- For medical, legal, financial, security, and other high-risk questions, the workflow does not replace qualified human professional judgment.
- Public visibility cannot technically prevent copying and does not replace legal enforcement. The license defines the permission boundary.
