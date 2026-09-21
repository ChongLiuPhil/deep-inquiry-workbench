# START HERE — Deep Inquiry Workbench 仓库接管入口

[English](START_HERE.md) | [中文](START_HERE.zh-CN.md)

这是维护 **Deep Inquiry Workbench 仓库本身** 的零上下文入口，不是某个用户探究项目的 `workspace.md`。

## 最小读取顺序

1. `AHICP_MANIFEST.yaml`
2. `AHICP_CONTEXT_INTERFACE.yaml`
3. `PROJECT_STATUS.md`
4. `AGENTS.zh-CN.md`
5. 按任务读取 `SKILL.md`、workspace template、user guide、evals、SECURITY 或 publication metadata

## 权威边界

- 产品行为协议：`SKILL.md`
- 用户探究工作文档结构：`resources/workspace_template.md`
- 用户协作须知：`resources/user_guide.md`
- 行为回归测试：`evals/`
- 信任边界：`SECURITY.md`
- 仓库维护状态：`PROJECT_STATUS.md`

仓库的 `PROJECT_STATUS.md` 不替代最终用户项目中的 `workspace.md`；两者属于不同层级。

## 发布边界

仓库本身已公开，但当前没有 GitHub Pages 或其他 Web provider。`website.yaml publish=false` 继续表示 Academic Vault / 学术主页新增发布未获授权。公开源码存在不等于授权另建网站、自动发布或变更许可。
