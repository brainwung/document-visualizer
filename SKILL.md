---
name: document-visualizer
description: Use when Codex needs to convert a provided document, note, report, paper, markdown data file, or structure/flow diagram into a single polished HTML/SVG visual explainer or long image using the documented styles. Do not use for general slide decks, freeform marketing graphics, standalone data analysis, or arbitrary charting unless the user explicitly asks for document-based visualisation.
---

# Document Visualizer

一个文档可视化设计系统 skill：先把用户提供的源材料整理成可信的信息模型，再从风格目录中选择合适的视觉模板，产出清晰、完整、可读性高的单页 HTML 或 SVG 图文排版。

这不是通用 PPT、海报或数据分析 skill。它只处理“有源材料支撑的文档可视化”。`CATALOG.md` 用来选择版式/风格，`RULES.md` 给出所有输出必须遵守的硬规则，`templates/<slug>/design.md` 提供具体风格的视觉规范，`assets/html/base.html` 提供可复用 HTML 工程骨架。

## 使用时机

- 用户给出文档、笔记、会议纪要、发言转写、论文、技术方案、PRD、结构化数据、结构图或流程图，并希望整理成单页图文视觉、长图或文档配图。
- 用户明确说使用 `document-visualizer`。
- 用户需要论文讲解、会议纪要整理、技术方案可视化、结构图重绘、流程图重绘、数据复盘长图或 HTML/SVG 可视化页面。
- 如果用户要完整 PPT deck、品牌海报、纯 UI 页面、无源材料的数据分析或开放式图表生成，应优先使用更合适的 skill；只有用户明确要求“把这份材料做成一页 PPT 尺寸视觉稿”时，才用本 skill 输出单页 PPT 尺寸 HTML/SVG。

## 工作流程

1. **确认输入和决策状态。**
   - 如果用户没有上传、粘贴或指定任何源材料，不要开始制作。先让用户上传/粘贴资料；如果用户只是想看风格示例，再让用户选择一个风格。
   - 如果用户已经提供资料但没有指定格式和风格，先分析资料类型，再推荐输出格式和 1 个主风格方案，必要时给 1-2 个备选；等待用户确认后再制作。
   - 如果用户已经明确指定格式和风格，视为已确认，可以直接进入制作；只有明显不匹配时先说明风险并请求确认。
   - 推荐不等于执行。除非用户已经明确做出选择，否则不要在推荐之后直接生成最终 HTML/SVG。

2. **读取源材料。**
   - 识别文件类型和可用内容。
   - 提取标题层级、章节、表格、图示、日期、人物、实体、指标、决策、风险和待办。
   - 如果源材料是图片结构图或流程图，先提取可识别的节点、连线、方向、分组、层级和疑似文字。
   - 如果内容提取不完整，先说明缺失部分，再进入设计。

3. **建立信息模型。**
   - 生成简洁的文档大纲。
   - 区分事实、分析、假设和待确认问题。
   - 保留源文档中的关键数字、标签、日期和原始措辞。
   - 不编造数据；没有来源支撑的推断必须标为假设。
   - 对 OCR 不确定、关系不清或被遮挡的图中内容，标为“疑似”或“未识别”，不要自行补全。

4. **推荐输出格式和风格。**
   - 阅读 [`RULES.md`](RULES.md)，了解信息完整性、版式、字体、颜色和 QA 的硬规则。
   - 阅读 [`CATALOG.md`](CATALOG.md)，根据源材料结构和用户目标推荐输出格式（长图 HTML、单页 SVG、16:9 单页、结构图重绘等）和风格。
   - 推荐时给出：资料类型、推荐格式、推荐风格、推荐理由、可选备选。保持简短，等待用户确认。
   - 如果用户已经指定风格或参考样式，优先尊重用户指定。
   - 用户确认后，只打开选中的一个 [`templates/<slug>/design.md`](templates/)；不要为了比较同时打开多个风格模板。

5. **制作输出。**
   - 从 `assets/html/base.html` 复制单页 HTML 骨架，按所选模板组织版式，但不要照搬示例内容。
   - 模板规范和已沉淀示例是质量基线，不是可随意偏离的灵感板。不得临时改成泛 dashboard、营销 hero、随机彩卡或与选定风格明显不同的版式。
   - 当 SVG 难以稳定处理长文本换行或复杂预览时，优先使用 HTML/CSS。
   - 如果用户要求 PPT，只输出适合幻灯片尺寸的单页 SVG/HTML 页面；不要把本 skill 扩展成完整演示文稿制作流程。
   - 核心文字尽量保留为真实文本，不转成路径或图片。

6. **验证并迭代。**
   - 按 [`RULES.md`](RULES.md) 的 QA 清单检查输出。
   - SVG 输出运行 [`scripts/svg_check.py`](scripts/svg_check.py)。
   - HTML 输出运行 [`scripts/html_check.py`](scripts/html_check.py)，并优先用浏览器检查宽度、溢出、模块对齐、文字层级和占位内容。
   - Skill 本身更新后运行 [`scripts/skill_check.py`](scripts/skill_check.py)，检查 frontmatter、文件结构和关键引用。
   - 用户明确要求“先不要渲染 PNG”或“先直接出 HTML”时，不要生成最终图片。

7. **交付。**
   - 说明源文档结构摘要、推荐/选择的视觉策略、生成的文件路径、关键假设/缺失信息、已执行的验证。
   - 如果是可切换风格的内容，告诉用户后续可以换用 catalogue 里的其他风格重新渲染。

## 文件

- [`RULES.md`](RULES.md)：所有文档可视化输出的硬规则和 QA 清单。每次使用都要读。
- [`CATALOG.md`](CATALOG.md)：版式/风格目录。用它选择一个合适模板。
- [`templates/<slug>/design.md`](templates/)：每个风格自己的视觉规范和适用场景。
- [`assets/html/base.html`](assets/html/base.html)：HTML 长图/单页视觉的基础工程模板。
- [`scripts/svg_check.py`](scripts/svg_check.py)：基础 SVG 检查脚本。
- [`scripts/html_check.py`](scripts/html_check.py)：HTML 输出静态检查脚本。
- [`scripts/skill_check.py`](scripts/skill_check.py)：skill 包结构与 frontmatter 检查脚本。
