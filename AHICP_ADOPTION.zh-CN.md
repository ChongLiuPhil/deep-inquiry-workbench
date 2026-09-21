# Current AHICP / Inquiry Publishing Stack Adoption — Deep Inquiry Workbench

本项目采用 current AHICP 作为仓库维护协议入口，同时保留产品自身的 Skill/workspace/eval 权威结构。

## Stack v2 revisions

- AHICP template: `02d0b3c02ca23073c760b6e0f761a468e0235a1c`; project adopted: `ed5a60b1016497472072db108072ace59bcdb65d`
- PPF template: `9a6005de85f032095e36eea03fda317e73126538`; project adopted: `e660b48fb216c28c8faa1f0fe2d0816401e1de2c`
- Vault template: `592c6e2e938f995b7b3e7df07a72f7f1e2c50c5a`; project adopted: `79d64b12275a5cc7c09236b144bf4213fa7afc5e`
- Starter source revision: `05857086e240cbd269eae91af8419ea0921c01fa`

## Functional mapping

| Stack role | Project-native authority |
| --- | --- |
| Product protocol | `SKILL.md` |
| User workspace contract | `resources/workspace_template.md` |
| User collaboration guide | `resources/user_guide.md` |
| Behavioral tests | `evals/` |
| Security/trust boundary | `SECURITY.md` |
| Repository operational resume | `PROJECT_STATUS.md` |

不创建重复的 research Content Core、Framework Status、Argument Map 或用户 inquiry Working Memory。最终用户 inquiry 的运行时权威仍是各自项目根目录下的 `workspace.md`。

## Publication lifecycle

- repository source: public
- Web publication/provider: disabled / not-authorized / null
- GitHub Pages: inactive
- GitHub Releases observed during adoption: none
- `website.yaml publish=false`: Academic Vault/homepage change not authorized

Stack adoption 不改变许可证，不新增 Web surface，也不把 public repository visibility 解释成自动发布授权。
