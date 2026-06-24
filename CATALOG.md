# Document Visualizer Style Catalogue

用这个目录选择输出风格。每个风格在 `templates/<slug>/design.md` 里保存规则；如果已有稳定预览图，则放在 `assets/styles/<slug>.png`。后续扩展新风格时，新增一个 template 目录，并按需补充预览图。

## Styles

| Style | Output | Best For | Vibe | Preview | Read |
| --- | --- | --- | --- | --- | --- |
| Minimalist（极简风） | 1080px HTML long image | 发言总结、培训讲义、会议长文提炼、演讲笔记、段落型报告 | 极简、段落讲义、清晰完整、可读性高 | [`assets/styles/minimalist.png`](assets/styles/minimalist.png) | [`templates/minimalist/design.md`](templates/minimalist/design.md) |
| Minimalist Dark（极简深色风） | 1080px HTML long image | 深色模式文档长图、数据报告、账号复盘、技术总结、会议纪要 | 深色、极简、高对比、低装饰、数据友好 | 待生成 | [`templates/minimalist-dark/design.md`](templates/minimalist-dark/design.md) |
| Soft Blocks（柔彩模块风） | 1080px HTML long image | 数据复盘、文档总结、方案拆解、活动信息、产品说明、模块化报告 | 柔彩块面、浅背景、圆角模块、现代信息面板 | 待生成 | [`templates/soft-blocks/design.md`](templates/soft-blocks/design.md) |

## How To Choose

1. **先看用户是否指定风格。** 如果指定 `minimalist` / 极简风，就读取对应模板；如果指定 `minimalist-dark` / 极简深色风 / 深色模式，就读取深色模板；如果指定 `soft-blocks` / 柔彩模块风 / dashboard 风 / 多色块面风，就读取柔彩模块模板。
2. **未指定时默认使用 Minimalist。** 它适合大多数中文文档、发言总结和讲义型长图。只有用户明确要求深色模式或输出场景需要暗色界面时，才使用 Minimalist Dark。
3. **尊重用户参考图。** 如果用户给了参考样式，先判断是否仍可落在 Minimalist 规则内；不能时再新增风格模板。
4. **想和 Minimalist 拉开差异时可选择 Soft Blocks。** 当内容适合被拆成多个信息模块，且用户希望使用柔和彩色块面、圆角模块和现代 dashboard 观感时，优先考虑 `soft-blocks`。
5. **不要把示例当固定模板。** 预览图只展示大致风格，内容组织仍要基于源材料。
6. **后续扩展。** 新增风格时，添加 `templates/<new-style>/design.md` 和 `assets/styles/<new-style>.png`，并在本 catalogue 中加一行，不要把新风格直接塞进 `SKILL.md`。
