# AGENTS — Deep Inquiry Workbench repository contract

[English](AGENTS.md) | [中文](AGENTS.zh-CN.md)

## Separate repository maintenance from user inquiries

This file governs maintenance of the Deep Inquiry Workbench repository. `SKILL.md` governs product behavior. Each end-user inquiry project's `workspace.md` stores that inquiry's runtime state. Do not conflate the three layers.

## Canonical authority

- `SKILL.md`: product behavior protocol;
- `resources/workspace_template.md`: workspace structure contract;
- `resources/user_guide.md`: user collaboration contract;
- `evals/`: observable behavioral tests;
- `SECURITY.md`: external-content, authorization, and trust boundary;
- `PROJECT_STATUS.md`: repository-maintenance operational resume.

AI may analyze, draft, test, and prepare PRs. Changes to human navigation rights, authorization boundaries, workspace schema/guide contracts, core behavior protocol, security boundary, license, or publication state require explicit maintainer authority.

## Stack

AHICP uses a lightweight functional mapping and does not create duplicate Content Core / Framework / Argument Map structures. PPF records lifecycle state only: the repository source is public, but Web deployment is disabled/not-authorized, provider is null, and `website.yaml publish=false`.

Do not record unmerged parallel product PR content as already adopted current state.
