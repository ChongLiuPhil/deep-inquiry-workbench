# AGENTS — Deep Inquiry Workbench 仓库协作契约

[English](AGENTS.md) | [中文](AGENTS.zh-CN.md)

## 仓库维护与用户探究分离

本文件约束 Deep Inquiry Workbench 仓库维护；`SKILL.md` 约束 Skill 的产品行为；最终用户每个探究项目中的 `workspace.md` 保存该探究的运行时状态。不得混淆三者。

## Canonical authority

- `SKILL.md`：产品行为协议；
- `resources/workspace_template.md`：工作文档结构契约；
- `resources/user_guide.md`：用户协作契约；
- `evals/`：可观察行为测试；
- `SECURITY.md`：外部内容、授权与信任边界；
- `PROJECT_STATUS.md`：仓库维护的 operational resume。

AI 可以分析、起草、测试与准备 PR，但改变导航权、授权边界、workspace schema/guide contract、核心行为协议、security boundary、许可或发布状态需要明确 maintainer authority。

## Stack

AHICP 采用 lightweight functional mapping，不复制第二套 Content Core / Framework / Argument Map。PPF 只记录发布生命周期；当前 repository public，但 Web deployment disabled/not-authorized，provider 为 null，`website.yaml publish=false`。

并行产品 PR 的内容不得在尚未合并前被 Stack 文件提前写成当前已采用状态。
