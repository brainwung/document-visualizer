# document-visualizer

`document-visualizer` 是一个面向文档可视化的 Codex Skill。它用于把用户提供的文档、会议纪要、论文、技术方案、PRD、发言转写、结构化数据、结构图或流程图，整理成可信的信息模型，并输出高级、可读、可继续调整的单页 HTML / SVG 图文排版。

它不是通用 PPT、海报或数据分析 skill。核心边界是：必须有源材料，输出以一页长图、文档配图或单页视觉解释为主。

## 适用场景

- 长图、文档配图、单页 HTML/SVG 视觉解释
- 论文讲解、技术方案可视化、会议纪要整理
- 活动信息、产品说明、方案拆解、模块化报告的单页视觉整理
- 数据复盘、账号年度报告、排行榜和时间序列展示
- 结构图、流程图、组织架构图重绘

不适合：

- 完整 PPT deck 制作
- 无源材料的开放式数据分析
- 泛营销海报、品牌视觉或纯 UI 页面设计
- 与文档结构无关的任意图表生成

## 工作流程

1. 读取源材料，提取标题层级、事实、数据、日期、人物、实体和待确认信息。
2. 建立信息模型，区分事实、分析、假设和缺失项。
3. 如果没有源材料，先让用户上传/粘贴资料；如果只是看示例，再让用户选择风格。
4. 如果有资料但没有指定格式和风格，先推荐格式与风格，等待用户确认后再制作。
5. 使用 `assets/html/base.html` 作为 HTML 工程骨架，或按 SVG 规则生成 SVG。
6. 输出 HTML / SVG，并检查溢出、遮挡、对齐、文字层级、颜色和数据来源。

## 当前风格

| Style | Best For | Vibe |
| --- | --- | --- |
| Minimalist（极简风） | 发言总结、培训讲义、会议长文、段落型报告 | 极简、讲义、可读性高 |
| Minimalist Dark（极简深色风） | 深色模式长图、数据报告、技术总结 | 深色、高对比、低装饰 |
| Soft Blocks（柔彩模块风） | 文档总结、方案拆解、活动信息、数据复盘、模块化报告 | 浅背景、柔彩块面、圆角模块、现代信息面板 |

风格规则位于 `templates/<slug>/design.md`，统一硬规则位于 `RULES.md`。

如果用户没有指定风格，skill 会根据文档类型推荐合适的格式和风格，最终是否执行由用户决定。用户已经明确指定格式和风格时，视为已确认。

## 文件结构

```text
document-visualizer/
├── SKILL.md
├── RULES.md
├── CATALOG.md
├── templates/
│   ├── minimalist/
│   ├── minimalist-dark/
│   └── soft-blocks/
├── assets/
│   ├── html/
│   ├── fonts/
│   └── styles/
└── scripts/
    ├── html_check.py
    ├── skill_check.py
    └── svg_check.py
```

## 使用示例

```text
用 document-visualizer 分析这篇论文，做一张论文讲解长图，先出 HTML。
```

```text
用 document-visualizer 基于这个 Markdown 数据做一个年度复盘长图，使用 soft-blocks 风格。
```

```text
用 document-visualizer 把这个会议纪要整理成清晰的决策、待办和风险长图。
```

## 关键原则

- 不编造源文档里没有的数据、日期、负责人、引用或因果解释。
- 数据型文档必须明确单位、口径、分母和时间范围；缺失时标注“未提供”或“未标注”。
- 用户未允许时，不擅自删除、合并或新增数据内容、解释内容和结论内容。
- 除非用户明确要求展示来源、类型、风格、范围等元信息，否则页面中默认不展示这类 meta 区。
- 顶部标题区、说明和下方主要模块网格应共享同一内容宽度。
- 同层级模块应保持一致的承载方式、字号、间距、圆角和数字层级。
- 结构图、流程图和组织架构图应优先保留原图的层级、分组、连线方向、行列位置和对应关系。
- 已沉淀示例和模板规范是质量基线；不要在实际使用中生成明显偏离风格的泛 dashboard、营销 hero 或随机彩卡。
- HTML 输出优先检查横向溢出、文字遮挡、模块对齐、标题层级和占位内容。

## 验证

```bash
python3 scripts/skill_check.py .
python3 scripts/html_check.py path/to/output.html
python3 scripts/svg_check.py path/to/output.svg
```

## 安装

可以从 GitHub 安装：

```text
https://github.com/brainwung/document-visualizer
```
