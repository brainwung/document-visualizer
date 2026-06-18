# Document Visualizer Style Catalogue

用这个目录选择输出风格。每个风格在 `templates/<slug>/design.md` 里保存规则，并在 `assets/styles/<slug>.png` 保留一张预览图。后续扩展新风格时，新增一个 template 目录和一张预览图即可。

## Styles

| Style | Output | Best For | Vibe | Preview | Read |
| --- | --- | --- | --- | --- | --- |
| Minimalist（极简风） | 1080px HTML long image | 发言总结、培训讲义、会议长文提炼、演讲笔记、段落型报告 | 极简、段落讲义、清晰完整、可读性高 | [`assets/styles/minimalist.png`](assets/styles/minimalist.png) | [`templates/minimalist/design.md`](templates/minimalist/design.md) |

## How To Choose

1. **先看用户是否指定风格。** 如果指定 `minimalist` / 极简风，就读取对应模板。
2. **未指定时默认使用 Minimalist。** 它适合大多数中文文档、发言总结和讲义型长图。
3. **尊重用户参考图。** 如果用户给了参考样式，先判断是否仍可落在 Minimalist 规则内；不能时再新增风格模板。
4. **不要把示例当固定模板。** 预览图只展示大致风格，内容组织仍要基于源材料。
5. **后续扩展。** 新增风格时，添加 `templates/<new-style>/design.md` 和 `assets/styles/<new-style>.png`，并在本 catalogue 中加一行，不要把新风格直接塞进 `SKILL.md`。
