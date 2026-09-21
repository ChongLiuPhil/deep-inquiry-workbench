# START HERE — Deep Inquiry Workbench repository entry

[English](START_HERE.md) | [中文](START_HERE.zh-CN.md)

This is the zero-context entry for maintaining the **Deep Inquiry Workbench repository itself**. It is not an end user's inquiry `workspace.md`.

## Minimum read order

1. `AHICP_MANIFEST.yaml`
2. `AHICP_CONTEXT_INTERFACE.yaml`
3. `PROJECT_STATUS.md`
4. `AGENTS.zh-CN.md`
5. selectively read `SKILL.md`, the workspace template, user guide, evals, SECURITY, or publication metadata for the task

## Authority boundary

- product behavior protocol: `SKILL.md`
- user inquiry workspace contract: `resources/workspace_template.md`
- user collaboration guide: `resources/user_guide.md`
- behavioral regression tests: `evals/`
- trust boundary: `SECURITY.md`
- repository maintenance state: `PROJECT_STATUS.md`

Repository `PROJECT_STATUS.md` does not replace the `workspace.md` authority inside an end user's inquiry project.

## Publication boundary

The source repository is already public, but there is no GitHub Pages or other Web provider. `website.yaml publish=false` still means no new Academic Vault/homepage publication is authorized. Public source availability does not itself authorize a separate website, automatic publication, or license change.
