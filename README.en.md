# Deep Inquiry Workbench

[中文](README.md) | [English](README.en.md)

Deep Inquiry Workbench is a general-purpose deep-inquiry Skill for different AI agents. Through explicit reasoning, evidence, criticism, and documentation protocols, it expands what AI can do in close reading, knowledge search, comparison of explanations, counterexample generation, fact-checking, concept analysis, and synthesis.

Its purpose is not to make AI produce longer answers. It is to reduce answers that are fluent but untested, agreeable to the user, or comprehensive in appearance without adding explanatory value. It turns AI from a one-shot text generator into an inquiry tool that can pursue a concrete question over time, draw on human knowledge resources, and preserve the evolution of understanding.

At the same time, the workflow keeps evidence assessment, concept boundaries, jumps in reasoning, competing explanations, and uncertainty visible. As users repeatedly encounter these acts of judgment in real inquiries, their language judgment, evidence awareness, and ability to think about knowledge can develop naturally. The educational effect is integrated into inquiry rather than replacing it.

## Why This Skill Is Needed

AI can already produce large amounts of coherent text quickly. But coherence is not understanding, and completeness is not reliability. Ordinary AI conversations often fail in the following ways.

### Fluency creates an illusion of correctness

The more natural, detailed, and confident an answer sounds, the easier it is to treat it as established knowledge. Yet language models are first of all good at generating text that fits linguistic patterns. Whether the premises are true, the reasoning is valid, the information has a source, or one explanation is better than its alternatives must be checked separately.

### Agreement with the user's existing position

AI often continues along the direction already implied by the question and mistakes repetition or elaboration for support. This can reinforce confirmation bias—the tendency to notice information that supports an existing view—and quickly give an untested intuition the appearance of a complete argument.

### Bland but safe answers

Many answers appear balanced, broad, and low-risk but never identify the real disagreement, key mechanism, or evidence that would change the conclusion. They may summarize several positions without producing a new distinction or explanation.

### Mixing different kinds of statements

Facts, attribution of theories, interpretation, speculation, value judgments, and original synthesis require different forms of checking. Ordinary answers often present them in one uniform tone of certainty, leaving readers unable to tell what has been verified and what is only a plausible conjecture.

### Replacing evidence with confidence or the appearance of citation

Model memory, confident language, agreement among multiple models, and AI-generated references are not evidence by themselves. Precise titles, page numbers, and quotations may also be candidate information completed from language patterns rather than details that were actually checked.

### Losing the question and its constraints in long conversations

As a conversation grows, early materials, concept definitions, corrections, and scope limits may fade. The AI may also rewrite the core question without saying so, producing later answers that no longer address the original inquiry.

### Over-answering or over-operating

AI may treat “this might help” as permission to add features, files, topics, or external actions. In the opposite direction, it may use the fear of overstepping as a reason to do superficial work and omit analysis or verification that the goal actually requires.

Deep Inquiry Workbench is designed to change the AI's behavior around these structural problems.

## Design Purpose and Core Judgments

### Inquiry is the basic process

Traditional “learning” is often imagined as absorbing stable knowledge that already exists. Yet existing knowledge is itself the provisional result of earlier inquiry. It has a scope, methods, evidence, and historical conditions, and it may later be revised.

For that reason, this workflow does not preserve learning as a separate process alongside inquiry. Reading, searching, remembering, practicing, calculating, experimenting, and writing occur naturally when they are needed to answer a concrete question. Learning is integrated into inquiry; inquiry does not turn into “learning through inquiry.”

### The question guides; answers and understanding evolve

What is continually generated, tested, and revised is the answer and the understanding, not the question merely for the sake of appearing to make progress. A question may be clarified, narrowed, or divided into subquestions. A major change to the core question requires explicit confirmation.

### AI is an interface to human knowledge resources

AI does more than offer candidate knowledge already represented in its parameters. It can read user materials, search external resources, use databases and tools, perform calculations and experiments, and organize scattered information into explanations that can be checked further. The Skill makes these abilities part of a continuous, verifiable process centered on one question.

### Effective assistance and stronger judgment are two sides of one process

The Skill must first improve the actual quality of inquiry. AI should perform the reading, searching, organizing, comparing, checking, and synthesis that it can reliably perform rather than merely explaining methods to the user.

At the same time, the workflow does not hide thought behind polished prose. Support for claims, hidden premises, counterexamples, concept boundaries, competing explanations, and uncertainty remain visible. Judgment develops within real inquiries rather than becoming a separate course.

## How It Changes AI Answers

| Common failure in ordinary AI | Mechanism in the Skill | Resulting change |
|---|---|---|
| Fluent but unverified answers | Classify statement types and apply proportionate evidence requirements | Linguistic completeness no longer substitutes for reliability |
| Continuing along the user's existing position | Reconstruct fairly, then apply adversarial testing when useful | Less agreement-seeking and confirmation bias |
| Broad but bland answers | Prioritize the most important gap in understanding | Each turn adds real explanatory value |
| Treating an analogy or concept as proof | Check definitions, boundaries, counterexamples, and points where the comparison breaks | Attractive labels no longer replace explanation |
| Treating model confidence as a source | Record actual access, verification status, and the exact scope supported | Greater epistemic honesty |
| Challenging every claim mechanically | Calibrate the strength of criticism to the inquiry state | Adversarial work does not become a ritual |
| Forgetting constraints or quietly changing the question | Dynamic workspace, stable identifiers, and decision records | Long-term continuity and question stability |
| Preserving only successful answers | Record what was learned from abandoned paths | Failure can limit and deepen current understanding |
| Expanding the task or doing too little | The rule “fully execute without overstepping” | Strong capability remains precisely controllable |
| Repeating prohibitions after a correction | Absorb corrections into subsequent behavior | Less defensive language and conversational noise |

## Avoiding Agreement-Seeking and Bland Answers

### Reconstruct fairly before deciding how to test

AI should not immediately attack an idea that has not yet been expressed clearly. It first restates the user's meaning in the clearest and strongest reasonable form, identifies the claim that actually needs examination, and then chooses among objection, comparison, search, experiment, formalization, or concept analysis.

This avoids attacking a straw man—a simplified version that is easier to refute—and prevents “criticism” from becoming a performance of cleverness.

### Adversarial testing is a tool for better understanding

When a core claim is being formed, a conclusion is about to be adopted, or confirmation bias is visible, the AI should actively look for:

- The strongest objection that genuinely threatens the current answer.
- A counterexample that defeats or narrows the conclusion.
- A boundary case that is easy to overlook.
- A competing explanation that accounts for the same material.
- The key evidence that would distinguish among those explanations.

Adversarial testing is neither hostility nor a ritual required in every turn. When an intuition is still forming, the AI should first help express and clarify it. When the bottleneck is missing evidence, it should stop repeating verbal disputes and move to evidence or acknowledge that the question cannot yet be settled.

### Do not settle for safe balance without explanatory gain

The Skill does not require the AI to manufacture “both sides have a point.” When evidence clearly favors one direction, it should say so. When the material is insufficient, it should identify what is actually missing. Each turn prioritizes the most important gap in the current understanding rather than mechanically completing fixed steps or covering every related topic.

## Evidence, Concepts, and Epistemic Honesty

### Different statements require different checks

- Directly checkable facts and numbers need current, reliable, actually accessed sources.
- Claims about an author or theory should return to the original text, an authoritative edition, and a stable location.
- Historical and causal judgments need chains of material, temporal relations, and competing explanations.
- Interpretations should identify textual or material anchors, reasoning, counterexamples, and scope.
- Speculation must be marked as speculation and state what would test it.
- Value judgments should identify their value premises rather than masquerade as facts.
- Original synthesis should identify the materials and reasoning that support it rather than inventing an authority.

When verification is unavailable, the item remains pending verification. When reliable sources conflict, it is marked as disputed. Precise quotations, page numbers, dates, and bibliographic details without a real access record must not be presented as checked sources.

### Concepts are not decorative labels

A new concept is worth retaining only when it adds real power to distinguish, explain, or guide action. Core concepts record their definition, necessary features, excluded scope, positive examples, counterexamples, boundary cases, nearby concepts, and the specific problem they solve.

If existing language is sufficient, a new name only adds cognitive burden. Novel terminology is not the same as novel thought.

### Cross-domain analogies record both similarity and difference

AI is especially good at generating analogies across domains, but similarity is not proof. A structural comparison must state which relations are genuinely similar, which important conditions differ, what explanatory ability the comparison adds, and how it might conceal differences.

### Abandoned paths still produce knowledge

A path may be abandoned because it is wrong, irrelevant, unsupported, conceptually expensive, or unable to distinguish competing explanations. The workspace does not preserve every failed detail. It preserves why the path failed, what boundary of the current answer it exposed, and what new evidence might justify reopening it.

## Judgment and Metacognitive Calibration

This section presents the core guidance a user should know at first use. The complete startup version is stored in [resources/user_guide.md](resources/user_guide.md) and is written into each inquiry workspace when the project starts.

### Suspend belief and inspect the reasoning structure

When an answer looks complete and confident, temporarily suspend both belief and rejection. Remove the rhetoric, adjectives, terminology, and authoritative tone, then ask:

```text
What are the premises?
What evidence supports those premises?
What reasoning connects the premises to the conclusion?
Have conditions or alternative explanations been omitted?
Is the conclusion stronger than the evidence actually supports?
```

This suspension is not universal skepticism. It reconnects belief with evidence.

### Fluency, confidence, and consensus are not proof

Keep separate whether the expression is natural, the reasoning is valid, the premises are true, the information has a source, the explanation outperforms alternatives, and the conclusion fits the current scope.

Similar answers from multiple models may reflect shared training material, prompting patterns, or default language. Truth is not decided by a vote among models.

### Watch for agreement, mainstream defaults, and empty balance

AI answers are influenced by training-data distributions, product design, safety tuning, and the form of the question. They may continue the user's existing position, present a mainstream formulation as the only reasonable one, or produce a safe and balanced answer that adds no understanding.

When an answer merely restates a position, ask for the strongest counterexample, competing explanation, or condition that would make it fail. But when evidence is the bottleneck, move to evidence rather than manufacturing further verbal opposition.

### Require claims to distinguish, be checkable, and state boundaries

A claim that can explain everything often explains nothing. For a concept or theory, ask: What would make it fail? How does it differ from a nearby concept? What can it distinguish? Where does it apply? What material would change the judgment?

“Checkable” does not mean that every question requires a statistical experiment. A textual interpretation can be checked against the original text, context, and alternative readings. A philosophical argument can be checked for conceptual consistency, reasoning, counterexamples, and scope.

### AI first-person language is an interface

Phrases such as “I think” and “I suggest” make conversation easier, but they are not evidence that the AI has consciousness, lived experience, value commitments, or the standing of a responsible agent. Important judgments should return to materials, reasoning, and the real situation.

### Changes of direction and real-world adoption require explicit confirmation

AI can organize options, reasons, evidence, and uncertainty, but it must not record silence as agreement. Changes to the core question, main goal, value tradeoffs, accepted risk, final adoption, or stopping point require an explicit decision record.

### Four kinds of change deserve to remain visible

Each substantive turn checks as needed whether the original meaning became more precise, an existing view was revised or suspended, the AI introduced a valuable candidate idea, or the user's rejection of an AI suggestion produced a deeper answer or limitation.

This does not require a form for every turn. It prevents real intellectual change from disappearing behind the final draft.

### Long inquiries cannot depend on chat memory alone

Context windows and conversation summaries decay. The workspace preserves the current answer, detailed support, important revisions, evidence status, decisions, next steps, and a handoff summary. Later sessions can recover from inspectable records rather than pretending that the model remembers everything.

### Sources, privacy, and real-world risk require proportionate care

A source that cannot be directly checked remains pending verification; polished citation formatting does not make it established evidence. The workspace keeps only material that the inquiry genuinely needs. Sensitive information should be minimized, redacted, or kept in a safer location, while copyrighted material should normally be represented through necessary excerpts, summaries, and source links. For medical, legal, financial, security, and other questions with significant real-world consequences, the inquiry should prioritize current authoritative sources and clearly identify uncertainty and the points that require qualified judgment.

## Faithful Execution: Full but Bounded

Precise controllability does not mean doing less, nor does it mean waiting for instructions at every step. It means analyzing, executing, and verifying fully within the goal while refusing to treat “this might help” as permission to expand the task.

- Reading relevant materials, completing necessary steps, checking results, and updating the workspace are part of fulfilling the task.
- The agent does not add features, deliverables, files, refactoring, external actions, or adjacent tasks on its own.
- An expansion that changes the deliverable, affected scope, cost, risk, or external state requires confirmation first.
- When a minor ambiguity does not change the result, use the narrowest reasonable interpretation that still completes the task.
- After a correction, adjust behavior naturally rather than repeatedly apologizing, restating prohibitions, or listing irrelevant things not done.

The goal is not less action. It is maximum effective capability within a clear boundary.

## Workflow and Dynamic Workspace

Each inquiry is a self-contained local project:

```text
<topic-project-directory>/
├── workspace.md
├── materials/       # Materials intentionally brought into the project
├── attachments/     # Longer evidence, search, calculation, or experiment records
└── outputs/         # Reports, plans, and finished drafts
```

`workspace.md` sits directly in the project root and is the authoritative entry point for the current inquiry state. The other directories are created only when real content exists. State is stored in ordinary Markdown and does not depend on a particular interface.

### First start

The agent creates the workspace, writes the complete user guide into it, shows a concise summary in chat, and provides the file path. After the guide is acknowledged, the agent records the time and version and begins substantive inquiry. Each project normally requires acknowledgment only once.

### Every substantive turn

1. Read the workspace and restore the current question, answer, evidence, constraints, and decisions.
2. Check the goal, requested deliverable, authorized scope, and any expansion requiring confirmation.
3. Identify the most important gap in understanding.
4. Choose the smallest set of actions that can fully advance or verify the goal.
5. Generate or revise the answer and understanding.
6. Integrate durable changes into themes and stable identifiers.
7. Update the revision number, handoff summary, and concise change log.
8. End the response by reporting workspace status and path.

```text
Workspace
- Status: updated / no update needed / update failed
- Changes this turn: revision 4; C-003 revised; E-005 added as pending verification
- Path: /absolute/path/to/topic-project/workspace.md
```

Pure confirmation or a response with no durable change does not create a record merely to satisfy a form. If writing fails, the agent reports the failure honestly and provides recoverable content.

### Stable identifiers

| Prefix | Object |
|---|---|
| `Q-` | Question |
| `C-` | Claim, candidate answer, or argument |
| `E-` | Evidence or source record |
| `O-` | Objection, counterexample, or competing explanation |
| `N-` | An abandoned path and what was learned from it |
| `D-` | A decision about direction, scope, values, risk, or stopping that requires explicit confirmation |

The workspace keeps separate how an item was formed, whether it is currently retained, and whether it has been verified. An AI suggestion, a retained idea, and a verified claim are not the same thing.

It also distinguishes:

- **Current answer:** The most concise defensible response to the core question at this point.
- **Current understanding:** The mechanisms, concept relations, evidence, uncertainty, competing explanations, and boundaries that support the answer.

An answer may not yet exist, or multiple competing versions may remain active. When evidence is insufficient, the item remains pending verification rather than being forced into a complete conclusion.

## Communication Principle

Use language that does not require a specialist background by default. Prefer ordinary words when they are accurate, explain necessary technical terms where they first appear, and spell out abbreviations on first use. Plain language must not remove important conditions, exceptions, uncertainty, or counterexamples.

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
- Ordinary questions that do not require deep inquiry or persistent state.

The user may still invoke the Skill explicitly for any task.

## Installation and Invocation

This project uses the open `SKILL.md` directory format. Any agent or agent harness—the runtime that supplies the model, tools, permissions, and context—can run the full workflow if it can read the Skill directory and its supporting files and can read and write Markdown in the active project.

The compatibility information below was checked against official platform documentation on **2026-09-02**. Platform capabilities and directory conventions may change; when they differ, follow the latest official documentation linked below.

### Recommended: install once and use across projects

Codex, Cursor, GitHub Copilot, Gemini CLI, OpenCode, OpenHands, and Devin Desktop / Cascade can all discover the following shared location natively:

macOS / Linux:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git ~/.agents/skills/deep-inquiry-workbench
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills"
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git "$HOME\.agents\skills\deep-inquiry-workbench"
```

A user-level installation stores only the Skill itself. When invoked, the agent should still treat the topic folder currently open as the inquiry project and create or update `workspace.md` at that project root, rather than writing inquiry content into the Skill installation directory.

For a single project, install it at project scope instead:

```bash
mkdir -p .agents/skills
git clone --depth 1 https://github.com/ChongLiuPhil/deep-inquiry-workbench.git .agents/skills/deep-inquiry-workbench
```

A project-local copy is for local use within the license only and must not be committed or republished with another project. To avoid accidental redistribution, add `.agents/skills/deep-inquiry-workbench/` to that project's `.gitignore`.

### Platforms with native `SKILL.md` support

| Platform | User-level location | Project-level location | Invocation and differences |
|---|---|---|---|
| [OpenAI Codex / ChatGPT Desktop](https://developers.openai.com/codex/skills) | `~/.agents/skills/deep-inquiry-workbench/` | `.agents/skills/deep-inquiry-workbench/` | In Codex, type `$deep-inquiry-workbench` or let matching activate it automatically; in ChatGPT Desktop, select it under Skills. Standalone Skills work in Desktop, Codex CLI, and the IDE extension. Installable distribution to ChatGPT web and mobile requires Plugin packaging. |
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/deep-inquiry-workbench/` | `.claude/skills/deep-inquiry-workbench/` | Type `/deep-inquiry-workbench` or trigger it with natural language. Claude Code does not use `.agents/skills` as its primary location, so install directly under `.claude/skills` or create a symlink there to the shared installation. |
| [Cursor](https://cursor.com/docs/skills) | `~/.agents/skills/deep-inquiry-workbench/` or `~/.cursor/skills/...` | `.agents/skills/deep-inquiry-workbench/` or `.cursor/skills/...` | Type `/deep-inquiry-workbench`, attach it with `@`, or let Agent select it. Remote and Cloud Agents do not inherit local user directories, so use a project-level installation there. |
| [GitHub Copilot](https://docs.github.com/en/copilot/reference/customization-cheat-sheet) | `~/.agents/skills/deep-inquiry-workbench/` or `~/.copilot/skills/...` | `.agents/skills/deep-inquiry-workbench/` or `.github/skills/...` | Use `/deep-inquiry-workbench` on Copilot surfaces that support Agent Skills, or let Copilot select it. Agent Skills support is not identical across every IDE and GitHub surface. |
| [Gemini CLI](https://geminicli.com/docs/cli/using-agent-skills/) | `~/.agents/skills/deep-inquiry-workbench/` or `~/.gemini/skills/...` | `.agents/skills/deep-inquiry-workbench/` or `.gemini/skills/...` | You can run `gemini skills install https://github.com/ChongLiuPhil/deep-inquiry-workbench`; check with `/skills list`, then ask it to “use deep-inquiry-workbench to investigate ...”. Activation may require confirmation. |
| [Google Antigravity](https://antigravity.google/docs/skills) | `~/.gemini/config/skills/deep-inquiry-workbench/` | `.agents/skills/deep-inquiry-workbench/` | Mention the Skill by name or let Agent invoke it automatically. Legacy `.agent/skills` remains compatible, but new projects should use `.agents/skills`. With the [Antigravity SDK](https://www.antigravity.google/docs/sdk/tools/), pass this Skill directory or its parent through `LocalAgentConfig.skills_paths`. |
| [Cline](https://github.com/cline/cline/blob/main/docs/customization/skills.mdx) | `~/.cline/skills/deep-inquiry-workbench/` | `.cline/skills/deep-inquiry-workbench/` | Type `/deep-inquiry-workbench` or let Cline match the description. Cline also reads project `.claude/skills`, but its user-level location is `.cline/skills`. |
| [Devin Desktop / Cascade (formerly Windsurf)](https://docs.devin.ai/desktop/cascade/skills) | `~/.agents/skills/deep-inquiry-workbench/` or `~/.codeium/windsurf/skills/...` | `.agents/skills/deep-inquiry-workbench/` or `.windsurf/skills/...` | Type `@deep-inquiry-workbench` or let the model invoke it automatically. Current Devin Desktop preserves the Windsurf locations and explicitly supports the shared `.agents/skills` directories. |
| [Kiro](https://kiro.dev/docs/skills/) | `~/.kiro/skills/deep-inquiry-workbench/` | `.kiro/skills/deep-inquiry-workbench/` | Type `/deep-inquiry-workbench` or let Agent invoke it automatically. Kiro's GitHub import UI requires a URL to a Skill subdirectory rather than a repository root; for this project, import the local folder or clone directly to the location above. |
| [Qwen Code](https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/) | `~/.qwen/skills/deep-inquiry-workbench/` | `.qwen/skills/deep-inquiry-workbench/` | Type `/deep-inquiry-workbench`, select it in the `/skills` panel, or let the model invoke it automatically. Normal sessions watch for file changes; bare mode requires a restart. |
| [OpenCode](https://opencode.ai/docs/skills) | `~/.agents/skills/deep-inquiry-workbench/` or `~/.config/opencode/skills/...` | `.agents/skills/deep-inquiry-workbench/` or `.opencode/skills/...` | Ask explicitly to “use deep-inquiry-workbench ...”; the agent loads it through the `skill` tool. If it is missing, check that Skill permission is not set to `deny`. |
| [OpenHands](https://docs.openhands.dev/overview/skills) | `~/.agents/skills/deep-inquiry-workbench/` | `.agents/skills/deep-inquiry-workbench/` | Start a new conversation and ask naturally to use the Skill. OpenHands first reads its name and description, then loads the body and resources on demand; start a new conversation after changing Skill files so the catalog is rebuilt. |

Platforms that do not read the shared location can be installed directly with:

```bash
mkdir -p ~/.claude/skills ~/.cline/skills ~/.gemini/config/skills ~/.kiro/skills ~/.qwen/skills
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git ~/.claude/skills/deep-inquiry-workbench
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git ~/.cline/skills/deep-inquiry-workbench
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git ~/.gemini/config/skills/deep-inquiry-workbench
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git ~/.kiro/skills/deep-inquiry-workbench
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git ~/.qwen/skills/deep-inquiry-workbench
```

Run only the `git clone` line for the platform you use. On Windows, use `$HOME\.claude\skills`, `$HOME\.cline\skills`, `$HOME\.gemini\config\skills`, `$HOME\.kiro\skills`, or `$HOME\.qwen\skills` in PowerShell and create the corresponding parent directory first.

If the Skill is already installed in `~/.agents/skills/`, symlinks avoid maintaining duplicate copies:

```bash
ln -s ~/.agents/skills/deep-inquiry-workbench ~/.claude/skills/deep-inquiry-workbench
ln -s ~/.agents/skills/deep-inquiry-workbench ~/.cline/skills/deep-inquiry-workbench
ln -s ~/.agents/skills/deep-inquiry-workbench ~/.gemini/config/skills/deep-inquiry-workbench
ln -s ~/.agents/skills/deep-inquiry-workbench ~/.kiro/skills/deep-inquiry-workbench
ln -s ~/.agents/skills/deep-inquiry-workbench ~/.qwen/skills/deep-inquiry-workbench
```

Update an installed upstream copy with:

```bash
git -C ~/.agents/skills/deep-inquiry-workbench pull --ff-only
```

If the Skill is installed elsewhere, replace the path with its actual location. `--ff-only` prevents the update from silently creating a locally modified variant.

### Agent harness and SDK integration

If you are building an agent rather than using one of the desktop or command-line products above, load the Skill explicitly as part of the runtime. In every SDK, keep the Skill directory read-only or subject to controlled writes, while giving the separate inquiry project directory read/write access and using it as the location for `workspace.md`.

- **[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/sandbox/guide/)**: Sandbox Agents provide a native `Skills` capability. For a larger local collection, use `Skills(lazy_from=LocalDirLazySkillSource(...))` so the body loads only after activation; `Skills(from_=GitRepo(...))` can load from a Git repository. Use the SDK capability rather than merely mounting `.agents/skills` as an ordinary folder. The Sandbox Agent interface is currently beta.
- **[Claude Managed Agents / Claude API](https://platform.claude.com/docs/en/managed-agents/skills)**: package this repository as a ZIP, create a custom Skill through the Skills API, and place the returned `skill_id` in the agent's `skills` array. A session that mounts an application GitHub repository can also scan `.claude/skills/<skill-name>/SKILL.md` at that repository root. Because this project's `SKILL.md` is at its own repository root, mounting this repository alone does not match that discovery path; use ZIP upload, or place it under the application repository's `.claude/skills/deep-inquiry-workbench/` in a local environment permitted by the license.
- **[LangChain Deep Agents](https://docs.langchain.com/oss/python/deepagents/skills)**: pass the parent directory containing Skill subdirectories explicitly through `skills=["<parent-directory>"]` in `create_deep_agent(...)`. For an installation at `~/.agents/skills/deep-inquiry-workbench/`, pass `~/.agents/skills/`. The Deep Agents SDK does not automatically scan CLI locations such as `~/.agents/skills`.
- **[Google Antigravity SDK](https://www.antigravity.google/docs/sdk/tools/)**: pass this Skill directory, or the parent containing multiple Skills, through `LocalAgentConfig.skills_paths`.

In production, the harness should initially index only `name` and `description`, read the full `SKILL.md` only after a match, and then load `resources/` on demand. Treat every Skill source as an instruction source that must be reviewed, and restrict the agent from modifying the Skill itself. Inquiry documents belong in a separate persistent project workspace—not in an SDK cache, the Skill repository, or a temporary sandbox.

### Platforms without native loading of this format

These platforms can still run the workflow, but the user must explicitly tell the agent to read the Skill rather than relying on automatic discovery.

- **[Aider](https://aider.chat/docs/usage/conventions.html)**: it has no native Agent Skills discovery. Use `--read` or `/read` to add `SKILL.md`, `resources/user_guide.md`, and `resources/workspace_template.md` as read-only materials, then use the generic invocation below.
- **AutoGen, CrewAI, Google ADK, and other file-capable agents or custom harnesses**: as of the check date above, no single native `SKILL.md` discovery method directly matching this project was verified for these runtimes. They can still use the repository by injecting the generic invocation below, or through a thin adapter that first registers `name` and `description`, then reads the complete `SKILL.md` on a match and resolves its relative links into `resources/`. “Adaptable” here does not mean “natively supported.”

[Roo Code](https://github.com/RooCodeInc/Roo-Code) previously loaded `.roo/skills/<name>/SKILL.md` natively, but its official repository has been archived. It is included only as compatibility guidance for an already-vetted local installation, not as a recommended new platform.

### Generic invocation

Native platforms may use their `$`, `/`, or Skill picker, or simply enter:

```text
Use deep-inquiry-workbench to help me investigate: <your question>.
Treat the currently open folder as the inquiry project root. Read SKILL.md completely and follow its relative links to the resources actually needed.
Do not modify the Skill installation directory. Follow the first-start protocol, create or restore workspace.md in the current project, and end every response with the workspace status and path.
```

After the user guide has already been acknowledged and the project contains `workspace.md`, a shorter continuation prompt is enough:

```text
Use deep-inquiry-workbench to continue the current inquiry. Read workspace.md first to recover state, then advance the most important current gap in understanding.
```

### How to tell whether the full workflow is running

A platform needs all of the following capabilities to count as fully compatible:

1. It can read the full `SKILL.md` and load supporting files from `resources/` when needed.
2. It recognizes the active topic folder as the inquiry project rather than writing content into the Skill installation directory.
3. It can reread, create, and update `workspace.md` before responding.
4. It preserves stable identifiers, evidence states, decisions, handoff summaries, and the workspace receipt at the end of every response.
5. It can access reliable external sources when factual verification is required; without retrieval, it must keep claims pending verification rather than pretending they were checked.

A chat-only platform that cannot read supporting files or write to the active project can still apply the Skill's reasoning principles, but it cannot provide the complete dynamic-workspace workflow.

## Skill Repository Structure

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
- `resources/user_guide.md`: The complete user guide written into the workspace on first start.
- `resources/workspace_template.md`: The authoritative workspace template.

Version 1 requires no scripts. Evidence records, concept cards, reflection, and handoff state are integrated into one main template. Only large materials are separated into project subdirectories when needed.

## Integration of the Two Prototypes

The project uses the thematic workspace, stable identifiers, evidence checking, decision gates, and handoff mechanism of `conduct-humanities-ai-research` as its engineering foundation. It also preserves the distinctive contributions of `human-ai-research-os`: clear warnings about fluency, agreement, bias, and context decay, together with four kinds of change, concept formation, failed paths, and metacognitive calibration.

The integration makes three important changes:

1. It generalizes the workflow from humanities research to inquiry about any question.
2. It emphasizes AI as a capable, bounded, and verifiable inquiry tool.
3. It replaces fixed stages, mandatory objection, and turn-by-turn forms with a dynamic workflow driven by the current gap in understanding.

## License and Contributions

This is a **source-available project with limited permission**. It is not open-source software that may be freely modified and republished.

- Individuals and organizations that qualify under the license may install and invoke the unmodified Skill for noncommercial purposes.
- Commercial use, publication of modified versions, independent derivative projects, and redistribution outside GitHub's own functionality are not permitted.
- GitHub's rules for public repositories allow viewing and forking on the platform. A fork does not grant permission for commercial use, independent publication of a modified version, or redistribution outside GitHub.
- Issues and contributions to the official repository are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).

The project uses the [PolyForm Strict License 1.0.0](LICENSE), with `ChongLiuPhil` as the copyright holder. This section is a summary; if there is any difference, the complete text of `LICENSE` and `CONTRIBUTING.md` controls.

## Limitations

- Without write permission, the Skill can only produce structured content to be saved later; it cannot maintain local state itself.
- The workspace reduces context decay but cannot guarantee that every agent will interpret or follow the protocol correctly.
- Evidence quality still depends on the sources, tools, time, and verification methods actually available.
- Medical, legal, financial, security, and other high-risk questions still require current authoritative sources and qualified human professional judgment.
- Public visibility cannot technically prevent copying. The license defines the permission boundary.
