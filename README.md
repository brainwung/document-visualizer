# document-visualizer

`document-visualizer` 是一个面向文档可视化的 Codex Skill。它用于把文档、会议纪要、论文、技术方案、PRD、发言转写、网页资料或结构化数据，整理成清晰的信息模型，并输出高级、可读、可继续调整的 SVG / HTML 图文排版。

适合场景：

- 长图海报
- 文档配图
- 技术方案可视化
- 论文讲解图
- 会议纪要整理
- 嘉宾 / 活动介绍页
- PPT 单页或网页 PPT
- 从复杂材料提炼结构、观点、数据和视觉表达

## 核心思路

这个 skill 不是固定模板生成器，而是一套“先整理信息，再选择风格，再排版验证”的工作流。

每次使用时会优先做三件事：

1. 读取和提炼源材料，区分事实、分析、假设和缺失信息。
2. 根据内容结构选择合适的可视化模式和风格。
3. 输出 SVG 或 HTML，并检查溢出、遮挡、层级、对齐、字体和颜色。

## 文件结构

```text
document-visualizer/
├── SKILL.md
├── RULES.md
├── CATALOG.md
├── templates/
│   └── minimalist/
│       └── design.md
├── assets/
│   ├── fonts/
│   └── styles/
└── scripts/
    └── svg_check.py
```

- `SKILL.md`：skill 的入口说明和工作流程。
- `RULES.md`：所有输出必须遵守的通用规则和 QA 清单。
- `CATALOG.md`：风格目录，后续扩展新风格时从这里登记。
- `templates/minimalist/design.md`：当前极简风的具体视觉规范。
- `assets/fonts/`：内置字体，包括 AlibabaPuHuiTi 和 DIN。
- `assets/styles/`：风格预览图。
- `scripts/svg_check.py`：基础 SVG 检查脚本。

## 当前风格

### Minimalist / 极简风

适合中文长图、发言总结、会议纪要、培训讲义、活动介绍和段落型报告。

基础规范：

- 画布宽度默认 1080px。
- 背景：`#F9F9F9`。
- 模块：`#FFFFFF`。
- 主文字：`#333333`。
- 辅助文字：`#666666` / `#999999`。
- 强调色：`#e62828`。
- 柔和强调底：`#ffedeb`。
- 中文字体：AlibabaPuHuiTi。
- 数字字体：DIN。
- 普通正文行高：1.5。
- 间距使用 6px 倍数。

## 使用方法

在 Codex 中直接点名使用：

```text
用 document-visualizer 把这个会议纪要整理成长图，需要清晰、完整、可读性高。
```

```text
用 document-visualizer 分析这篇论文，做一张论文讲解长图，先出 HTML，不要导出 PNG。
```

```text
用 document-visualizer 做一张活动嘉宾长图，包括标题、时间、地点、简介、嘉宾照片、姓名、title 和机构。
```

```text
用 document-visualizer 把这个技术方案画成架构说明图，要求模块关系清楚，适合放到文档里。
```

## 推荐输入

为了输出更稳定，最好提供：

- 源文档、网页链接、截图、Markdown、PDF、Pages、Docx 或纯文本。
- 输出目标：长图、PPT 单页、文档配图、SVG、HTML。
- 尺寸要求：例如 1080px 长图、16:9 PPT、手机端可读。
- 风格倾向：例如 minimalist / 极简风。
- 是否需要先出 HTML 调样式，还是直接生成图片。
- 是否有品牌色、字体、logo 或参考图。

## 工作技巧

### 先 HTML，后导图

长文本、复杂换行、需要反复调样式的内容，优先输出 HTML。等排版确认后，再导出 PNG 或用于其他格式。

### 先定信息层级

不要一开始就堆卡片。先判断：

- 哪些是标题信息。
- 哪些是核心结论。
- 哪些是并列模块。
- 哪些是辅助说明。
- 哪些只是来源或备注。

视觉层级应服务于信息层级。

### 新增模块必须复用已有规范

同一张图里新增模块时，必须沿用已经建立的标题、背景、间距、颜色和层级规则。

例如活动海报里，`Featured Speakers` 和 `Registered Teams` 都是同级模块，那么它们的标题条、右侧辅助文案、标题到内容的距离都应该一致。

### 间距要有层级

常用做法：

- 大模块之间：60px 或 66px。
- 标题到内容：等于内容项之间的 gap，例如 18px。
- 列表项之间：18px、24px 或 30px。
- 模块内部 padding：24px、30px、36px。

不要让大模块间距和卡片内部间距混在一起。

### 资源要本地化

如果页面使用远程图片、logo 或网页素材，建议下载到本地 `assets/` 后再引用，避免预览或导出时丢图。

logo 使用前要检查背景可读性：

- 深色 logo 不要放黑底。
- 白色透明 logo 不要放白底。
- 必要时换用来源页同组里更适合当前底色的版本。

### 检查比截图更重要

HTML 输出至少检查：

- 是否横向溢出。
- 文本是否遮挡或截断。
- 模块宽度是否一致。
- 同级标题样式是否一致。
- 标题到内容的间距是否等于内容项 gap。
- 图片和 logo 是否加载成功。
- 移动端是否还能读清楚。

## 扩展新风格

新增风格时，不要把规则直接塞进 `SKILL.md`。

推荐步骤：

1. 在 `templates/<style-name>/design.md` 新增风格规范。
2. 在 `assets/styles/<style-name>.png` 放一张预览图。
3. 在 `CATALOG.md` 增加一行风格说明。
4. 保持 `RULES.md` 作为所有风格共同遵守的硬规则。

## 安装

可以从 GitHub 安装：

```text
https://github.com/brainwung/document-visualizer
```

如果使用 Codex 的 skill 安装工具，按你的本地安装方式从 GitHub repo 安装即可。

## 注意

- 不编造源文档里没有的数据、日期、负责人或引用。
- 用户要求“先不要渲染 PNG”时，只交付 HTML 或 SVG。
- 用户给出的红框、箭头和批注通常是修改说明，不要保留到最终设计里。
- 真实文本尽量保留为文本，不要转成图片。
