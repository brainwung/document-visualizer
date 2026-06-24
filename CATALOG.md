# Document Visualizer Style Catalogue

用这个目录选择输出风格。每个风格在 `templates/<slug>/design.md` 里保存规则；如果已有稳定预览图，则放在 `assets/styles/<slug>.png`。后续扩展新风格时，新增一个 template 目录，并按需补充预览图。

## Styles

| Style | Output | Best For | Vibe | Preview | Read |
| --- | --- | --- | --- | --- | --- |
| Minimalist（极简风） | 1080px HTML/SVG single visual | 发言总结、培训讲义、会议长文提炼、演讲笔记、段落型报告 | 极简、段落讲义、清晰完整、可读性高 | [`assets/styles/minimalist.png`](assets/styles/minimalist.png) | [`templates/minimalist/design.md`](templates/minimalist/design.md) |
| Minimalist Dark（极简深色风） | 1080px HTML/SVG single visual | 深色模式文档长图、数据报告、账号复盘、技术总结、会议纪要 | 深色、极简、高对比、低装饰、数据友好 | [`assets/styles/minimalist-dark.png`](assets/styles/minimalist-dark.png) | [`templates/minimalist-dark/design.md`](templates/minimalist-dark/design.md) |
| Soft Blocks（柔彩模块风） | 1080px HTML/SVG single visual | 数据复盘、文档总结、方案拆解、活动信息、产品说明、结构图/流程图 | 柔彩块面、浅背景、圆角模块、现代信息面板 | [`assets/styles/soft-blocks.png`](assets/styles/soft-blocks.png) | [`templates/soft-blocks/design.md`](templates/soft-blocks/design.md) |

## How To Choose

1. **无资料先停下。** 如果用户没有上传、粘贴或指定源材料，先让用户提供资料；如果用户只是要风格示例，再让用户选择风格。
2. **先看用户是否指定风格。** 如果指定 `minimalist` / 极简风，就读取对应模板；如果指定 `minimalist-dark` / 极简深色风 / 深色模式，就读取深色模板；如果指定 `soft-blocks` / 柔彩模块风 / dashboard 风 / 多色块面风，就读取柔彩模块模板。
3. **有资料但未指定时先推荐，等待确认。** 根据源材料类型推荐输出格式和风格，例如“资料类型：数据复盘；推荐格式：1080px 长图 HTML；推荐风格：Soft Blocks；理由：适合 KPI、趋势和 Top 列表”。推荐后等待用户决定，不要直接执行。
4. **多风格比较只做预览。** 如果用户想同时看多种风格，只生成轻量预览图或预览级 HTML，用同一份源内容和同一信息层级对比视觉差异；不要同时制作 3 个完整成品 HTML。
5. **最终只打磨一个风格。** 用户选定后，只读取并执行一个风格模板，把完整 HTML/SVG 的结构、样式和验证集中做好。
6. **尊重用户参考图。** 如果用户给了参考样式，先判断是否仍可落在现有风格规则内；不能时再新增风格模板。
7. **不要把示例当固定模板，也不要脱离示例质量基线。** 内容组织必须基于源材料，但视觉语言、间距、层级、颜色和模块承载方式必须遵守选中模板；不要临时变成泛 dashboard、营销 hero 或随机彩卡。
8. **守住边界。** 本 catalogue 只服务文档可视化；完整 PPT deck、泛海报、纯 UI 页面或无源材料数据分析应使用其他 skill。
9. **后续扩展。** 新增风格时，添加 `templates/<new-style>/design.md` 和 `assets/styles/<new-style>.png`，并在本 catalogue 中加一行，不要把新风格直接塞进 `SKILL.md`。

## Recommendation Matrix

| 源材料类型 | 推荐风格 | 原因 |
| --- | --- | --- |
| 发言总结、培训讲义、会议长文、段落型报告 | Minimalist | 以连续阅读和段落层级为主，适合白底讲义式长图。 |
| 论文讲解、研究方法、实验流程 | Minimalist | 适合 claim-evidence、方法流程、结论解释；若用户要求更现代模块化，可改用 Soft Blocks。 |
| 数据复盘、年度报告、账号报告、业务指标 | Soft Blocks | 更适合 KPI、趋势、Top 列表和模块化信息面板；若用户要求极简正式感，可用 Minimalist 的数据页规则。 |
| 产品说明、方案拆解、活动信息、模块化报告 | Soft Blocks | 内容天然可拆成多个信息块，适合柔彩块面和现代 dashboard 观感。 |
| 结构图、流程图、组织架构、系统关系图 | Soft Blocks | 更适合用色块分组、节点层级和少量连线承接复杂结构；严肃讲义场景可用 Minimalist。 |
| 深色模式输出、暗色技术总结、暗色数据报告 | Minimalist Dark | 用户明确要求暗色或使用场景需要深色界面时优先使用。 |
| 会议纪要、决策/待办/风险清单 | Minimalist | 默认适合清晰记录和行动项；如果强调看板式分组，可推荐 Soft Blocks。 |
