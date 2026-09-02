# Deep Inquiry Workbench（深度探究工作台）

[中文](README.md) | [English](README.en.md)

Deep Inquiry Workbench 是一个供不同 AI Agent 调用的通用深度探究 Skill。它通过明确的推理、证据、批判和文档协议，尽可能释放 AI 在材料阅读、知识检索、解释比较、反例生成、事实核验、概念分析和成果整合方面的能力。

它不是让 AI 生成更长的回答，而是让 AI 更少给出流畅却未经检验、迎合用户、面面俱到却没有解释增量的回答。它把 AI 由一次性文本生成器转变为可以持续推进具体问题、调用人类知识资源并保存理解演变的探究工具。

与此同时，这套工作方式会把证据判断、概念边界、推理跳跃、竞争解释和不确定性保持可见。使用者在真实探究中反复接触这些判断活动，语言判断力、证据意识和知识思考能力会自然得到训练。教育作用融入探究，而不是取代探究。

## 为什么需要这个 Skill

AI 已经能够快速生成大量连贯文本，但连贯不等于理解，完整不等于可靠。普通 AI 对话经常出现以下问题：

### 流畅性制造正确性的错觉

回答越自然、越详细、越自信，人越容易把它当成已经成立的知识。但语言模型首先擅长的是生成符合语言模式的文本。前提是否成立、推理是否有效、信息是否有来源、解释是否优于其他解释，都需要另外检查。

### 迎合用户已有立场

AI 容易沿着提问者已经表达的方向继续论证，把重复和扩写误当成支持。这会强化确认偏误——只注意支持既有判断的信息——并使一个尚未经过检验的直觉迅速获得完整论证的外观。

### 给出平庸而安全的答案

许多回答表面均衡、覆盖全面、很少出错，却没有指出真正的分歧、关键机制或能够改变判断的证据。它们可能总结了各方立场，却没有带来新的区分和解释。

### 把不同性质的说法混在一起

事实、理论归属、解释、推测、价值判断和原创综合需要不同的检查方法。普通回答经常把它们写在同一段确定语气中，使读者无法判断什么已经核实、什么只是合理猜测。

### 用自信或引用外观代替证据

模型记忆、自信语气、多个模型给出相似答案或 AI 生成的参考文献，都不能直接成为证据。精确的书名、页码和引文也可能是根据语言模式补出的候选信息。

### 在长对话中丢失问题和限定

随着对话延长，早期材料、概念定义、用户纠正和范围限制可能逐渐消失。AI 还可能在没有明确说明的情况下改写核心问题，使后面的答案已经不再回答最初的问题。

### 过度回答或过度操作

AI 可能把“也许有帮助”当作扩展任务的理由，擅自增加功能、文件、论题或外部动作。反过来，它也可能以避免越界为由只做表面工作，省略完成目标所必需的分析和核验。

Deep Inquiry Workbench 的目标，就是针对这些结构性问题改变 AI 的工作方式。

## 设计初衷与基本判断

### 探究是基本过程

传统的“学习”常被想象为：知识已经以稳定答案存在，学习者只需吸收它。但既有知识本身是前人探究的阶段性成果；它带有范围、方法、证据和历史条件，也可能被修正。

因此，本工作流不把学习保留为与探究并列的独立流程。阅读、检索、记忆、练习、计算、实验和写作都在回答具体问题时自然发生，并服务于探究。学习融入探究，而不是探究转向“在探究中学习”。

### 问题引导，答案与理解持续变化

持续生成、检验和修正的是答案与理解，不是为了制造进展而不断改写问题。问题可以被澄清、缩小范围或拆出子问题；核心问题的重大改变需要明确确认。

### AI 是人类知识资源的接口

AI 不只提供参数中已经形成的候选知识。它还可以读取用户材料、检索外部资源、使用数据库和工具、执行计算与实验，并把分散信息组织成可以继续检查的解释。Skill 的作用，是让这些能力围绕同一个问题形成连续、可核验的过程。

### 实质协助与判断力提升是同一过程的两面

本 Skill 首先必须实质提高探究质量。AI 应承担能够可靠完成的阅读、检索、整理、比较、核验和成果整合，而不能只向用户讲解方法。

同时，工作流不把思考过程藏在一段成品文字之后。主张依据、隐含前提、反例、概念边界、竞争解释和不确定性保持可见。判断力训练因此发生在真实问题中，而不是成为额外课程。

## 它怎样改变 AI 的回答方式

| 普通 AI 容易出现的问题 | Skill 采用的机制 | 带来的改变 |
|---|---|---|
| 回答流畅但未经核验 | 区分说法类型并设置相称的证据门槛 | 不让语言完整性冒充知识可靠性 |
| 顺着用户立场继续论证 | 先善意重构，再按需进行对抗性检验 | 降低迎合与确认偏误 |
| 给出面面俱到的平庸答案 | 优先处理最关键的理解缺口 | 让每轮带来真实的解释增量 |
| 把类比或概念当成证明 | 检查定义、边界、反例和断裂点 | 防止漂亮标签代替解释 |
| 用模型自信代替来源 | 记录实际访问、核验状态和准确支持范围 | 保持认识诚实 |
| 强制每轮反驳 | 根据问题状态校准批判强度 | 避免把对抗变成仪式 |
| 遗忘早期限定或悄然改题 | 动态工作文档、稳定编号和决定记录 | 保持长程连续性与问题稳定 |
| 只保留成功答案 | 保存被放弃路径带来的认识 | 让失败也能限制和深化当前理解 |
| 擅自扩展任务或做得过少 | “充分执行但不越界”的行动规则 | 让能力强大而精准可控 |
| 用户纠正后反复声明限制 | 吸收纠正并自然改变后续行为 | 减少防御性和交流噪声 |

## 避免迎合与平庸回答

### 先善意重构，再决定怎样检验

AI 不应立即攻击一个尚未说清楚的想法。它先把用户的意思重述为尽可能清楚、有力的版本，确认真正需要检验的主张，再选择反驳、比较、检索、实验、形式化或概念分析。

这可以避免攻击稻草人——把对方观点简化成更容易反驳的版本——也能防止“批判”只成为显示聪明的姿态。

### 对抗性检验是提高理解的工具

当用户提出核心主张、准备采用一个结论或存在明显确认偏误时，AI 应主动寻找：

- 能够真正威胁当前答案的最强反驳。
- 使结论失效或需要缩小范围的反例。
- 容易被忽略的边界情况。
- 同样能够解释材料的竞争解释。
- 能够区分这些解释的关键证据。

对抗性不是敌对，也不是每轮必须完成的仪式。初步直觉尚未成形时，应先帮助外化和澄清；瓶颈是缺少证据时，应停止重复语言争论，转向寻找证据或承认暂时无法判断。

### 不满足于安全、均衡却没有增量的总结

Skill 不要求 AI 为形式制造“双方都有道理”。如果证据已经明显倾向某个方向，应直接说明；如果材料不足，也应指出真正缺少什么。每轮优先推进当前问题最关键的理解缺口，而不是机械完成固定步骤或覆盖所有相关话题。

## 证据、概念与认识诚实

### 不同说法采用不同检查方法

- 可直接核对的事实和数字，需要当前、可靠并能实际访问的来源。
- 某位作者或理论的观点，需要回到原文、权威版本和稳定位置。
- 历史与因果判断，需要材料链条、时间关系和竞争解释。
- 解释需要说明材料依据、推理过程、反例和适用边界。
- 推测必须标明推测性质和所需验证。
- 价值判断需要说明价值前提，不伪装成事实。
- 原创综合需要说明哪些材料和推理支撑它，不能伪造出处。

无法核验时保持“待核”。可靠材料之间仍有冲突时标为“争议”。没有真实访问记录的精确引文、页码、年份和书目信息不能冒充已经核对的来源。

### 概念不是漂亮标签

新概念只有在确实增加区分力、解释力或可操作性时才值得保留。对核心概念记录定义、必要特征、排除范围、正例、反例、边界案例、与近似概念的关系，以及它具体解决了什么困难。

旧词已经足够时，新名称只会增加理解负担。术语新颖不等于思想新颖。

### 跨领域类比同时记录相似与不同

AI 很擅长生成跨领域类比，但相似性本身不是证明。结构比较必须说明哪些关系确实相似、哪些关键条件不同、比较带来了什么解释能力，以及它可能怎样遮蔽差异。

### 被放弃的路径也留下认识

一条路径可能因为错误、离题、证据不足、概念负担过重或无法区分竞争解释而被放弃。工作文档不保留所有失败细节，而保存：为什么走不通、它暴露了当前答案的什么边界、什么新证据可能使它值得重新开启。

## 判断力与元认知校准

本节直接呈现首次使用时需要了解的核心须知。完整的启动版本保存在 [resources/user_guide.md](resources/user_guide.md)，并会在每个探究项目第一次启动时写入工作文档。

### 暂缓相信，并查看推理结构

面对完整而自信的回答，先暂缓相信或拒绝。把修辞、形容词、术语和权威口吻暂时拿掉，检查：

```text
前提是什么？
这些前提有什么证据？
从前提到结论经过了什么推理？
是否遗漏了条件或替代解释？
结论是否强于证据真正支持的范围？
```

这种“悬置”不是怀疑一切，而是让相信与证据重新连接。

### 流畅性、自信和共识都不是证明

需要主动区分：表达是否自然、推理是否有效、前提是否成立、信息是否有来源、解释是否优于竞争解释、结论是否适用于当前范围。

多个模型给出相似答案，只说明它们可能共享相似训练材料、提示方式或默认表达，不能按票数决定真伪。

### 警惕迎合、主流偏向和空泛答案

AI 的回答会受到训练材料分布、产品设计、安全调校和提问方式影响。它可能顺着用户立场继续论证，把主流表达误呈现为唯一方式，或者给出安全均衡但没有新理解的回答。

当回答只是在换一种方式重复立场时，应要求最强反例、竞争解释或使结论失效的条件。但如果瓶颈是证据不足，应转向证据，而不是继续制造语言对抗。

### 要求一个说法能够区分、检查并说明边界

一个可以解释任何事情的说法，往往没有真正解释任何事情。面对概念或理论，应追问：什么情况会使它不成立？它与近似概念真正不同在哪里？它能区分什么？在哪些范围有效？什么材料能够改变判断？

“能够检查”不等于所有问题都必须做统计实验。文本解释可以检查原文依据、语境和替代读法；哲学论证可以检查概念一致性、推理、反例和适用范围。

### AI 的第一人称只是交流界面

“我认为”“我建议”等表达便于对话，但不应被当作 AI 具有意识、亲身经验、价值承诺或责任主体地位的证据。重要判断仍需回到材料、推理和现实处境。

### 方向选择与现实采用需要明确确认

AI 可以整理选项、理由、证据和不确定性，但不能把沉默写成同意。改变核心问题、主要目标、价值取舍、风险接受、最终采用和停止路径时，应留下明确决定记录。

### 四类变化值得被看见

每个实质回合按需检查：原意是否得到更精确表达；原有观点是否被修正、放弃或悬置；AI 是否提出了有价值的新候选内容；用户驳斥 AI 后是否形成了更深的答案或限定。

这不是要求填写逐轮表格，而是防止真正的思想变化被最终成稿抹平。

### 长程探究不能只依赖聊天记忆

上下文窗口和会话摘要会衰减。工作文档保存当前答案、详细依据、重要修正、证据状态、决定、下一步和交接摘要，使后续会话能够从可检查的记录恢复，而不是假装模型始终记得一切。

### 来源、隐私与现实风险需要相称处理

无法直接核验的来源保持“待核”，不因引用形式完整就进入确定答案。工作文档只保存探究确实需要的材料，敏感信息应尽量减少、遮盖或留在更安全的位置；受版权保护的内容以必要摘录、概述和来源链接为主。涉及医疗、法律、金融、安全等可能造成现实后果的问题，应优先使用最新、权威的来源，并明确说明不确定性和需要专业判断的部分。

## 忠实执行：充分但不越界

精准可控不是让 AI 少做，也不是凡事等待指令。它要求在目标范围内充分分析、执行和核验，同时不把“可能有帮助”误当成扩大任务的许可。

- 读取相关材料、完成必要步骤、检查结果和更新工作文档，属于正常履行任务。
- 不主动增加额外功能、成果、文件、重构、外部操作或相邻任务。
- 扩展会改变成果、影响范围、成本、风险或外部状态时，先请求确认。
- 轻微歧义不影响结果时，采用能够完整完成任务的最窄合理解释。
- 用户纠正后自然调整行为，不反复道歉、复述禁止项或列出无关的未做事项。

它追求的不是更少行动，而是在清楚边界内最大化有效能力。

## 工作流与动态工作文档

每个探究是一个独立、本地可打开的项目：

```text
<主题项目目录>/
├── workspace.md
├── materials/       # 按需保存要求纳入项目的材料
├── attachments/     # 按需保存较长的证据、检索、计算或实验记录
└── outputs/         # 按需保存报告、方案和成稿
```

`workspace.md` 直接位于项目根目录，是当前探究状态的权威入口。其他目录只有出现实际内容时才创建。工作流以普通 Markdown 保存状态，不依赖特定界面。

### 首次启动

Agent 创建工作文档，写入完整用户须知，在聊天中展示精炼摘要并给出文件地址。用户确认须知后，Agent 记录确认时间和版本，再进入实质探究。每个项目通常只确认一次。

### 每个实质回合

1. 读取工作文档，恢复当前问题、答案、证据、限制和决定。
2. 核对目标、要求成果、允许影响的范围和需要确认的扩展。
3. 判断当前最关键的理解缺口。
4. 选择最少但能充分推进或核验目标的操作。
5. 生成或修正答案与理解。
6. 把持久变化整合进主题和稳定编号。
7. 更新修订号、交接摘要和简短变更日志。
8. 在回复末尾报告工作文档状态和地址。

```text
工作文档
- 状态：已更新 / 无需更新 / 更新失败
- 本轮变化：revision 4；C-003 已修正；E-005 新增为待核
- 地址：/absolute/path/to/topic-project/workspace.md
```

纯确认或没有形成持久变化的回答不会为了形式制造记录。写入失败时必须如实报告，并提供可恢复的待写入内容。

### 稳定编号

| 前缀 | 对象 |
|---|---|
| `Q-` | 问题 |
| `C-` | 主张、候选答案或论点 |
| `E-` | 证据或来源记录 |
| `O-` | 反对意见、反例或竞争解释 |
| `N-` | 被放弃路径以及从中得到的认识 |
| `D-` | 必须得到明确确认的方向、范围、价值、风险或终止决定 |

工作文档把“怎样形成”“目前是否保留”和“是否已经核实”分开记录。AI 提出的、当前保留的和已经核验的，不是同一件事。

工作文档还区分：

- **当前答案**：截至此刻，对核心问题最简洁、可辩护的回答。
- **当前理解**：支撑答案的机制、概念关系、证据、不确定性、竞争解释和适用边界。

答案可以暂时不存在，也可以保留多个竞争版本。证据不足时保持“待核”，不为了得到完整结论而过早收敛。

## 交流原则

默认使用无需专业背景即可理解的语言。能用普通词准确表达时，不使用行业黑话；必要术语在第一次出现时就地解释；缩写第一次出现时写出全称并说明用途。通俗表达不能删除重要条件、例外、不确定性和反例。

## 适用范围

适合：

- 深入理解日常、社会、理论或实践问题。
- 比较多个竞争解释或解决方案。
- 围绕科学、技术、人文或跨学科问题开展研究。
- 把阅读、文献、数据或既有材料融入持续探究。
- 发展概念、检验论证、整理证据或形成报告。
- 需要跨会话、跨 Agent 保存状态的长期思考。

通常不需要触发：

- 一个简单事实已经足以回答的问题。
- 只需执行的明确操作。
- 一次性翻译、校对、格式调整或语言润色。
- 不需要深入探究和持久状态记录的普通问答。

用户仍可在任何任务中显式调用本 Skill。

## 安装与调用

本项目采用开放的 `SKILL.md` 目录格式。只要 Agent 或 Agent Harness（负责装载模型、工具、权限和上下文的运行环境）能够读取 Skill 目录及其配套文件，并能在当前项目中读写 Markdown，就可以运行完整工作流。

下面的兼容信息依据各平台官方文档核对，最后核对日期为 **2026-09-02**。平台能力和目录约定仍可能变化，遇到差异时以链接中的最新官方说明为准。

### 推荐：安装一次，在不同项目中使用

以下公共目录可被 Codex、Cursor、GitHub Copilot、Gemini CLI、OpenCode、OpenHands 和 Devin Desktop / Cascade 原生发现：

macOS / Linux：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git ~/.agents/skills/deep-inquiry-workbench
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills"
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git "$HOME\.agents\skills\deep-inquiry-workbench"
```

全局安装只保存 Skill 本身。调用时，Agent 仍应把你当前打开的主题文件夹作为探究项目，在该文件夹根目录创建和更新 `workspace.md`，而不是把探究内容写进 Skill 的安装目录。

如果只想让某一个项目使用，也可以安装到项目目录：

```bash
mkdir -p .agents/skills
git clone --depth 1 https://github.com/ChongLiuPhil/deep-inquiry-workbench.git .agents/skills/deep-inquiry-workbench
```

项目内安装的副本仅供许可范围内的本地使用，不应随其他项目提交或重新发布。为了避免误提交，可把 `.agents/skills/deep-inquiry-workbench/` 加入该项目的 `.gitignore`。

### 原生支持 `SKILL.md` 的平台

| 平台 | 用户级安装位置 | 项目级安装位置 | 调用方式与差异 |
|---|---|---|---|
| [OpenAI Codex / ChatGPT Desktop](https://developers.openai.com/codex/skills) | `~/.agents/skills/deep-inquiry-workbench/` | `.agents/skills/deep-inquiry-workbench/` | Codex 输入 `$deep-inquiry-workbench`，或让系统按描述自动调用；ChatGPT Desktop 可在 Skills 中选择。独立 Skill 可用于 Desktop、Codex CLI 和 IDE；ChatGPT 网页与移动端的可安装分发需要打包为 Plugin。 |
| [Claude Code](https://code.claude.com/docs/en/skills) | `~/.claude/skills/deep-inquiry-workbench/` | `.claude/skills/deep-inquiry-workbench/` | 输入 `/deep-inquiry-workbench`，或用自然语言触发。Claude Code 不把 `.agents/skills` 作为主要目录，因此应直接安装到 `.claude/skills`，或从那里建立指向公共安装的符号链接。 |
| [Cursor](https://cursor.com/docs/skills) | `~/.agents/skills/deep-inquiry-workbench/` 或 `~/.cursor/skills/...` | `.agents/skills/deep-inquiry-workbench/` 或 `.cursor/skills/...` | 输入 `/deep-inquiry-workbench`，使用 `@` 附加，或由 Agent 自动选择。远程与 Cloud Agent 不会继承本机用户目录，应采用项目级安装。 |
| [GitHub Copilot](https://docs.github.com/en/copilot/reference/customization-cheat-sheet) | `~/.agents/skills/deep-inquiry-workbench/` 或 `~/.copilot/skills/...` | `.agents/skills/deep-inquiry-workbench/` 或 `.github/skills/...` | 在支持 Agent Skills 的 Copilot 界面中使用 `/deep-inquiry-workbench`，或让 Copilot 自动选择。不同 IDE 和 GitHub 界面对 Agent Skills 的支持程度并不完全相同。 |
| [Gemini CLI](https://geminicli.com/docs/cli/using-agent-skills/) | `~/.agents/skills/deep-inquiry-workbench/` 或 `~/.gemini/skills/...` | `.agents/skills/deep-inquiry-workbench/` 或 `.gemini/skills/...` | 可直接运行 `gemini skills install https://github.com/ChongLiuPhil/deep-inquiry-workbench`；用 `/skills list` 检查，然后要求“使用 deep-inquiry-workbench 探究……”。激活 Skill 时可能要求确认。 |
| [Google Antigravity](https://antigravity.google/docs/skills) | `~/.gemini/config/skills/deep-inquiry-workbench/` | `.agents/skills/deep-inquiry-workbench/` | 直接提及 Skill 名称或让 Agent 自动调用；旧版 `.agent/skills` 仍兼容，但新项目使用 `.agents/skills`。使用 [Antigravity SDK](https://www.antigravity.google/docs/sdk/tools/) 时，在 `LocalAgentConfig.skills_paths` 中传入本 Skill 目录或其父目录。 |
| [Cline](https://github.com/cline/cline/blob/main/docs/customization/skills.mdx) | `~/.cline/skills/deep-inquiry-workbench/` | `.cline/skills/deep-inquiry-workbench/` | 输入 `/deep-inquiry-workbench`，或让 Cline 按描述调用。Cline 也读取项目中的 `.claude/skills`，但用户级安装应使用 `.cline/skills`。 |
| [Devin Desktop / Cascade（原 Windsurf）](https://docs.devin.ai/desktop/cascade/skills) | `~/.agents/skills/deep-inquiry-workbench/` 或 `~/.codeium/windsurf/skills/...` | `.agents/skills/deep-inquiry-workbench/` 或 `.windsurf/skills/...` | 输入 `@deep-inquiry-workbench`，或让模型自动调用。当前 Devin Desktop 保留 Windsurf 目录，并明确支持公共 `.agents/skills` 目录。 |
| [Kiro](https://kiro.dev/docs/skills/) | `~/.kiro/skills/deep-inquiry-workbench/` | `.kiro/skills/deep-inquiry-workbench/` | 输入 `/deep-inquiry-workbench`，或让 Agent 自动调用。Kiro 的 GitHub 导入界面要求 URL 指向仓库中的 Skill 子目录而不是仓库根目录；本项目应使用本地文件夹导入或直接克隆到上述目录。 |
| [Qwen Code](https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/) | `~/.qwen/skills/deep-inquiry-workbench/` | `.qwen/skills/deep-inquiry-workbench/` | 输入 `/deep-inquiry-workbench`，在 `/skills` 面板中选择，或让模型自动调用。普通会话会自动发现文件变化；bare mode 需要重启。 |
| [OpenCode](https://opencode.ai/docs/skills) | `~/.agents/skills/deep-inquiry-workbench/` 或 `~/.config/opencode/skills/...` | `.agents/skills/deep-inquiry-workbench/` 或 `.opencode/skills/...` | 直接要求“使用 deep-inquiry-workbench……”，Agent 会通过 `skill` 工具载入；如果没有出现，检查 Skill 权限是否被设为 `deny`。 |
| [OpenHands](https://docs.openhands.dev/overview/skills) | `~/.agents/skills/deep-inquiry-workbench/` | `.agents/skills/deep-inquiry-workbench/` | 新建会话后用自然语言要求使用该 Skill。OpenHands 会先读取名称和描述，再按需载入正文和资源；修改 Skill 后应新建会话以重建目录。 |

不读取公共目录的平台可以分别这样安装：

```bash
mkdir -p ~/.claude/skills ~/.cline/skills ~/.gemini/config/skills ~/.kiro/skills ~/.qwen/skills
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git ~/.claude/skills/deep-inquiry-workbench
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git ~/.cline/skills/deep-inquiry-workbench
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git ~/.gemini/config/skills/deep-inquiry-workbench
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git ~/.kiro/skills/deep-inquiry-workbench
git clone https://github.com/ChongLiuPhil/deep-inquiry-workbench.git ~/.qwen/skills/deep-inquiry-workbench
```

这里只需执行与你所用平台对应的一条 `git clone`。Windows 用户在 PowerShell 中使用 `$HOME\.claude\skills`、`$HOME\.cline\skills`、`$HOME\.gemini\config\skills`、`$HOME\.kiro\skills` 或 `$HOME\.qwen\skills`，并先创建相应的父目录。

如果已经安装在 `~/.agents/skills/`，也可以用符号链接避免维护多个副本：

```bash
ln -s ~/.agents/skills/deep-inquiry-workbench ~/.claude/skills/deep-inquiry-workbench
ln -s ~/.agents/skills/deep-inquiry-workbench ~/.cline/skills/deep-inquiry-workbench
ln -s ~/.agents/skills/deep-inquiry-workbench ~/.gemini/config/skills/deep-inquiry-workbench
ln -s ~/.agents/skills/deep-inquiry-workbench ~/.kiro/skills/deep-inquiry-workbench
ln -s ~/.agents/skills/deep-inquiry-workbench ~/.qwen/skills/deep-inquiry-workbench
```

更新已安装的原版 Skill：

```bash
git -C ~/.agents/skills/deep-inquiry-workbench pull --ff-only
```

如果安装在其他平台目录，把命令中的路径替换成实际安装位置。使用 `--ff-only` 可以避免更新过程悄然生成本地修改版本。

### Agent Harness 与 SDK 接入

如果你正在开发自己的 Agent，而不是直接使用上面的桌面或命令行产品，需要把 Skill 作为运行环境的一部分显式装载。无论使用哪一种 SDK，都应同时满足两点：Skill 目录对 Agent 只读或受控可写；探究项目目录可读写，并作为 `workspace.md` 的保存位置。

- **[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/sandbox/guide/)**：Sandbox Agent 原生提供 `Skills` 能力。较大的本地 Skill 集合适合使用 `Skills(lazy_from=LocalDirLazySkillSource(...))`，只在触发后载入正文；也可以用 `Skills(from_=GitRepo(...))` 从 Git 仓库装载。不要只把 `.agents/skills` 当普通文件夹挂进去，应使用 SDK 的 `Skills` 能力完成发现和按需载入。该 Sandbox Agent 接口目前仍是 beta。
- **[Claude Managed Agents / Claude API](https://platform.claude.com/docs/en/managed-agents/skills)**：可以把本仓库打包为 ZIP，通过 Skills API 创建自定义 Skill，再把返回的 `skill_id` 放入 Agent 的 `skills` 列表。若会话挂载的是业务 GitHub 仓库，Claude 也会扫描该仓库根目录下的 `.claude/skills/<skill-name>/SKILL.md`；本项目的 `SKILL.md` 位于自身仓库根目录，因此直接挂载本仓库并不会符合这条自动扫描路径，宜采用 ZIP 上传，或在许可允许的本地环境中把它放入业务仓库的 `.claude/skills/deep-inquiry-workbench/`。
- **[LangChain Deep Agents](https://docs.langchain.com/oss/python/deepagents/skills)**：在 `create_deep_agent(...)` 中通过 `skills=["<包含各 Skill 子目录的父目录>"]` 显式传入来源。例如安装在 `~/.agents/skills/deep-inquiry-workbench/` 时，传入 `~/.agents/skills/`。Deep Agents SDK 不会自动扫描 CLI 的 `~/.agents/skills`，必须在代码中传入。
- **[Google Antigravity SDK](https://www.antigravity.google/docs/sdk/tools/)**：在 `LocalAgentConfig.skills_paths` 中传入本 Skill 目录，或传入包含多个 Skill 的父目录。

对于生产环境，还应让 Harness 在启动时只索引 `name` 和 `description`，命中任务后再读取完整 `SKILL.md`，随后按需读取 `resources/`；同时把 Skill 来源视为需要审查的指令来源，并限制 Agent 修改 Skill 本身。探究产生的文档应保存在独立的项目工作区，而不是保存在 SDK 缓存、Skill 仓库或临时沙箱中。

### 尚未原生装载本格式的平台

这类平台仍然可以运行工作流，但需要明确告诉 Agent 读取 Skill，而不能依赖自动发现。

- **[Aider](https://aider.chat/docs/usage/conventions.html)**：没有原生 Agent Skills 发现机制，可用 `--read` 或会话中的 `/read` 把 `SKILL.md`、`resources/user_guide.md` 和 `resources/workspace_template.md` 作为只读材料加入，然后使用下面的通用调用语句。
- **AutoGen、CrewAI、Google ADK，以及其他能够读取文件的 Agent 或自建 Harness**：截至上述核对日期，没有核实到它们具有与本项目直接对应的统一原生 `SKILL.md` 发现方式。可以把仓库放在运行环境可读取的位置，在任务开始时注入下面的通用调用语句，或实现一个很薄的适配层：先登记 `name` 和 `description`，命中后读取完整 `SKILL.md`，再解析其中指向 `resources/` 的相对路径。这里的“可适配”不等于平台原生支持。

[Roo Code](https://github.com/RooCodeInc/Roo-Code) 曾原生读取 `.roo/skills/<name>/SKILL.md`，但其官方仓库已归档；这里只把它视为既有本地安装的兼容说明，不再作为新的推荐平台。

### 通用调用语句

原生平台可以使用自己的 `$`、`/` 或 Skill 选择器，也可以直接输入：

```text
使用 deep-inquiry-workbench 协助我探究：<你的问题>。
把当前打开的文件夹作为探究项目根目录。完整读取 SKILL.md，并按其中的相对路径读取实际需要的资源。
不要修改 Skill 安装目录；按照首次启动协议，在当前项目中创建或恢复 workspace.md，并在每轮回复末尾报告工作文档状态和地址。
```

已经确认过用户须知、并且项目中已有 `workspace.md` 时，可以简化为：

```text
使用 deep-inquiry-workbench 继续当前探究。先读取 workspace.md 恢复状态，再推进当前最关键的理解缺口。
```

### 判断是否完整运行

平台至少需要具备以下能力，才能称为完整兼容：

1. 能读取完整 `SKILL.md`，并按需读取 `resources/` 中的配套文件。
2. 能把当前主题文件夹识别为探究项目，而不是把内容写入 Skill 安装目录。
3. 能在回复前重新读取、创建和更新 `workspace.md`。
4. 能保留稳定编号、证据状态、决定、交接摘要和每轮工作文档回执。
5. 需要外部事实时能够访问可靠来源；没有检索能力时，必须保留“待核”，不能假装已经核验。

只有聊天、不能读取配套文件或不能写入当前项目的平台，仍可借鉴本 Skill 的推理原则，但无法提供完整的动态工作文档工作流。

## Skill 文件结构

```text
deep-inquiry-workbench/
├── SKILL.md
├── README.md
├── README.en.md
├── SECURITY.md
├── LICENSE
├── NOTICE
├── CONTRIBUTING.md
├── evals/
│   ├── README.md
│   └── cases/
└── resources/
    ├── user_guide.md
    └── workspace_template.md
```

- `SKILL.md`：Agent 执行的完整决策协议。所有真正影响行为的规则保留在这里。
- `SECURITY.md`：详细说明外部内容与操作授权之间的信任边界；真正影响 Agent 行为的核心不变量仍同时保留在 `SKILL.md`。
- `evals/`：模型无关的行为评估规范，用可观察的 PASS / PARTIAL / FAIL 条件检查核心协议不变量和回归风险。
- `resources/user_guide.md`：首次启动时写入工作文档的完整用户须知。
- `resources/workspace_template.md`：权威工作文档模板。

V1 不依赖脚本。证据记录、概念卡、反思和交接状态已经整合进一个主模板；只有大块材料会按需拆入项目子目录。

## 安全边界与行为验证

深度探究会反复读取网页、PDF、文档、数据集、代码仓库和其他外部材料。项目把这些内容视为证据、主张、上下文或研究对象，而不是能够自行取得操作权限的指令来源。外部内容可以提供证据，但不能自行授予自己权威；同样，找到、打开或引用一个来源也不等于已经核验了目标主张。完整规则见 [SKILL.md](SKILL.md) 与 [SECURITY.md](SECURITY.md)。

`evals/` 把问题稳定、证据状态、人类决定、跨 Agent 接续、范围控制、文件冲突、负向知识和不可信内容等关键承诺写成可失败的行为案例。它们目前是 **specification-level evaluations（规范级评估案例）**：可以人工运行，也可以由未来的 harness 自动化，用来比较实现并暴露回归。

这些 eval 提供的是可检验标准，不是项目有效性的经验性证明。要支持“使用本 Skill 会提高研究质量”之类的效果主张，还需要在相同任务、相同输入和可比工具条件下进行独立的对照运行，并报告实际结果。

## 两套原型的整合

项目以 `conduct-humanities-ai-research` 的主题式工作台、稳定编号、证据检查、决定门槛和交接机制为工程基础，同时吸收 `human-ai-research-os` 对流畅性、迎合、偏见和上下文衰减的机制祛魅，以及四类变化、概念形成、失败路径和元判断力训练。

整合后完成三项关键转变：

1. 从人文学术研究泛化为任何问题的探究。
2. 强调 AI 作为能力充分、边界清楚、可以核验的探究工具。
3. 从固定阶段、强制反驳和逐轮表格，转为由当前理解缺口驱动的动态工作流。

## 使用许可与贡献

本项目是**源代码公开、有限授权**项目，不是允许任意修改和再发布的开源项目。

- 允许个人及符合许可证定义的非商业组织，以非商业目的安装并调用未经修改的 Skill。
- 不允许商业使用、发布修改版本、建立独立衍生项目或在 GitHub 功能范围之外重新分发。
- GitHub 的公开仓库规则允许用户在平台内查看和 Fork；Fork 不等于取得商业使用、修改后独立发布或站外再分发的许可。
- 欢迎通过官方仓库提交问题和贡献；具体规则见 [CONTRIBUTING.md](CONTRIBUTING.md)。

项目采用 [PolyForm Strict License 1.0.0](LICENSE)，版权所有者为 `ChongLiuPhil`。以上是许可摘要；发生差异时以 `LICENSE` 和 `CONTRIBUTING.md` 的完整文本为准。

## 局限

- 没有写入权限时，Skill 只能生成待保存的结构化内容，无法真正维护本地状态。
- 工作文档能降低上下文衰减，但不能保证任何 Agent 都正确理解或执行协议。
- 证据质量仍取决于实际可访问的来源、工具、时间和核验方法。
- 医疗、法律、金融、安全等高风险问题仍需要当前、权威的来源和具备资质的人类专业判断。
- 公开可见不能从技术上阻止复制，许可证只能明确权利边界。