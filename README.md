# Skill Bank

SKILL 收藏庫，依功能與用途分類，目前共 447 個。

**找 SKILL 的方法**：在本頁用 Ctrl/Cmd + F 搜尋關鍵字（中文用途、英文名稱、原始說明都在表格裡），或從下方分類進去。

本頁由 `scripts/build_index.py` 依 `sources.json` 產生，請勿手動編輯。略過未存的大型素材列在 [SKIPPED.md](SKIPPED.md)。

## 分類總覽

| 分類 | 收什麼 | 數量 |
|---|---|---|
| [研究／學術](#研究學術-research-academic) | 文獻搜尋、論文寫作、APA、統計、EBP、報告指引、同儕審查 | 0 |
| [臨床／護理](#臨床護理-clinical-nursing) | 臨床照護、護理紀錄、個案報告、考試與臨床教學 | 0 |
| [技術／開發](#技術開發-tech-dev) | 程式開發、AI/Agent、MCP、自動化、資料分析 | 5 |
| [創意／設計](#創意設計-creative-design) | 插畫、視覺設計、UI、簡報、品牌、logo、影像 prompt | 199 |
| [動畫／影片](#動畫影片-animation-video) | 程式化影片、AI 影片、網頁動效、動畫製作 | 140 |
| [3D／遊戲](#3d遊戲-3d-gamedev) | 3D 建模與物件、遊戲引擎、遊戲開發與 mod | 95 |
| [寫作／溝通](#寫作溝通-writing-communication) | 一般寫作、電子報、內部溝通、語氣潤飾、翻譯 | 2 |
| [效率／工作流](#效率工作流-productivity-workflow) | 筆記、知識管理、排程、文件格式處理 | 4 |
| [思考／學習](#思考學習-thinking-learning) | 批判思考、學習方法、哲學、決策框架 | 2 |

## 研究／學術 (`research-academic`)

尚無。

## 臨床／護理 (`clinical-nursing`)

尚無。

## 技術／開發 (`tech-dev`)

| 名稱 | 數量 | 用途 | 關鍵字 | 來源 | 存入日期 |
|---|---|---|---|---|---|
| [anthropics](#tech-dev-anthropics) | 5 | Anthropic 官方：Claude API、MCP 伺服器開發、SKILL 製作、網頁測試、複雜 artifact | claude api, mcp, skill-creator, playwright | [anthropics/skills](https://github.com/anthropics/skills) `2c5958e`（Apache-2.0） | 2026-11-13 |

<a id="tech-dev-anthropics"></a>

### anthropics（5 個）

Anthropic 官方：Claude API、MCP 伺服器開發、SKILL 製作、網頁測試、複雜 artifact。資料夾：[`skills/tech-dev/anthropics`](skills/tech-dev/anthropics)

| SKILL | 原始說明 |
|---|---|
| [claude-api](skills/tech-dev/anthropics/claude-api/SKILL.md) | Reference for the Claude API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model migration. TRIGGER — read BEFORE openin… |
| [mcp-builder](skills/tech-dev/anthropics/mcp-builder/SKILL.md) | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers… |
| [skill-creator](skills/tech-dev/anthropics/skill-creator/SKILL.md) | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run… |
| [web-artifacts-builder](skills/tech-dev/anthropics/web-artifacts-builder/SKILL.md) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts… |
| [webapp-testing](skills/tech-dev/anthropics/webapp-testing/SKILL.md) | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots,… |

## 創意／設計 (`creative-design`)

| 名稱 | 數量 | 用途 | 關鍵字 | 來源 | 存入日期 |
|---|---|---|---|---|---|
| [anthropics](#creative-design-anthropics) | 6 | Anthropic 官方：前端設計、畫布視覺、演算法藝術、品牌規範、主題配色、Slack GIF | frontend, canvas, 海報, 品牌, 主題 | [anthropics/skills](https://github.com/anthropics/skills) `2c5958e`（Apache-2.0） | 2026-11-13 |
| [architecture-diagram-generator](#creative-design-architecture-diagram-generator) | 1 | 描述系統就產出乾淨的架構圖（HTML/SVG） | 架構圖, diagram | [Cocoon-AI/architecture-diagram-generator](https://github.com/Cocoon-AI/architecture-diagram-generator) `4b9087d`（MIT） | 2026-11-13 |
| [beautiful-html-templates](skills/creative-design/beautiful-html-templates/AGENTS.md) | 1 | 34 套 HTML 簡報模板；依場合與氛圍挑候選、做封面預覽、再套入內容 | HTML 簡報, slide deck, pitch | [zarazhangrui/beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates) `e5e204f`（MIT） | 2026-11-13 |
| [guizang-ppt-skill](skills/creative-design/guizang-ppt-skill/SKILL.md) | 1 | 歸藏 PPT：雜誌風與瑞士風的 HTML 簡報 | 簡報, 雜誌風, swiss style | [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) `93d21bf`（AGPL-3.0） | 2026-11-13 |
| [hallmark](#creative-design-hallmark) | 1 | 讓設計不像 AI 做的：有辨識度的版面與視覺 | 反 AI 味, 版面, 視覺風格 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) `04977e1`（MIT） | 2026-11-13 |
| [huashu-design](skills/creative-design/huashu-design/SKILL.md) | 1 | 花叔設計：一句話產出完整設計（高保真原型、簡報、動畫、資訊圖） | 一句話出設計, 原型, 簡報, 動畫 | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) `e8d1148`（MIT） | 2026-11-13 |
| [impeccable](skills/creative-design/impeccable/SKILL.md) | 1 | 前端設計品質工具：polish、bolder、critique、audit 等指令，避免 AI 味的介面 | /polish, /bolder, /critique, UI 打磨 | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) `c4cd192`（Apache-2.0） | 2026-11-13 |
| [logo-design](skills/creative-design/logo-design/SKILL.md) | 1 | 從 brief 到 SVG logo 再到品牌指南 | logo, SVG, 品牌指南 | [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) `bbf31e5`（MIT） | 2026-11-13 |
| [nothing-design-skill](#creative-design-nothing-design-skill) | 1 | Nothing 風格：單色、點陣字的 UI | 單色, dot-matrix, UI 風格 | [dominikmartn/nothing-design-skill](https://github.com/dominikmartn/nothing-design-skill) `6bec3c7`（MIT） | 2026-11-13 |
| [open-design](#creative-design-open-design) | 169 | open-design 設計工作區內建的 SKILL 大全：簡報、海報、社群圖卡、動效、Figma、影像生成等 | 設計, 簡報, 圖卡, figma, 影像生成 | [nexu-io/open-design](https://github.com/nexu-io/open-design) `e427ad9`（Apache-2.0） | 2026-11-13 |
| [stitch-skills](#creative-design-stitch-skills) | 16 | Google Stitch 的 UI 設計 SKILL：設計、建置、工具三組 | stitch, UI 設計, design system | [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) `0337446`（Apache-2.0） | 2026-11-13 |

<a id="creative-design-anthropics"></a>

### anthropics（6 個）

Anthropic 官方：前端設計、畫布視覺、演算法藝術、品牌規範、主題配色、Slack GIF。資料夾：[`skills/creative-design/anthropics`](skills/creative-design/anthropics)

| SKILL | 原始說明 |
|---|---|
| [algorithmic-art](skills/creative-design/anthropics/algorithmic-art/SKILL.md) | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic… |
| [brand-guidelines](skills/creative-design/anthropics/brand-guidelines/SKILL.md) | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelin… |
| [canvas-design](skills/creative-design/anthropics/canvas-design/SKILL.md) | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other sta… |
| [frontend-design](skills/creative-design/anthropics/frontend-design/SKILL.md) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't re… |
| [slack-gif-creator](skills/creative-design/anthropics/slack-gif-creator/SKILL.md) | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Sl… |
| [theme-factory](skills/creative-design/anthropics/theme-factory/SKILL.md) | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can ap… |

<a id="creative-design-architecture-diagram-generator"></a>

### architecture-diagram-generator（1 個）

描述系統就產出乾淨的架構圖（HTML/SVG）。資料夾：[`skills/creative-design/architecture-diagram-generator`](skills/creative-design/architecture-diagram-generator)

| SKILL | 原始說明 |
|---|---|
| [architecture-diagram](skills/creative-design/architecture-diagram-generator/architecture-diagram/SKILL.md) | Create polished dark-themed architecture diagrams as self-contained HTML+SVG files. Use when the user asks for system, infrastructure, cloud, security, or network topology diagram… |

<a id="creative-design-hallmark"></a>

### hallmark（1 個）

讓設計不像 AI 做的：有辨識度的版面與視覺。資料夾：[`skills/creative-design/hallmark`](skills/creative-design/hallmark)

| SKILL | 原始說明 |
|---|---|
| [hallmark](skills/creative-design/hallmark/hallmark/SKILL.md) | Design skill for websites and new pages that look designed, not generated. Use when the user asks to build or design something new, or names Hallmark. Never use it on an existing… |

<a id="creative-design-nothing-design-skill"></a>

### nothing-design-skill（1 個）

Nothing 風格：單色、點陣字的 UI。資料夾：[`skills/creative-design/nothing-design-skill`](skills/creative-design/nothing-design-skill)

| SKILL | 原始說明 |
|---|---|
| [nothing-design](skills/creative-design/nothing-design-skill/nothing-design/SKILL.md) | This skill should be used when the user explicitly says "Nothing style", "Nothing design", "/nothing-design", or directly asks to use/apply the Nothing design system. NEVER trigge… |

<a id="creative-design-open-design"></a>

### open-design（169 個）

open-design 設計工作區內建的 SKILL 大全：簡報、海報、社群圖卡、動效、Figma、影像生成等。資料夾：[`skills/creative-design/open-design`](skills/creative-design/open-design)

| SKILL | 原始說明 |
|---|---|
| [8-bit-orbit-video-template](skills/creative-design/open-design/8-bit-orbit-video-template/SKILL.md) | Hyperframes-based video template for retro pixel deck motion design. Use when users want a high-fidelity, multi-scene HTML-to-video composition with advanced transitions, interact… |
| [ad-creative](skills/creative-design/open-design/ad-creative/SKILL.md) | Generate and iterate ad creative including headlines, descriptions, and primary text. Useful for paid social and search ad iteration. |
| [after-hours-editorial-template](skills/creative-design/open-design/after-hours-editorial-template/SKILL.md) | Luxury dark-editorial HyperFrames template for three-page cinematic storyboards, inspired by haute couture title cards and magazine chapter spreads. Use when the user asks for pre… |
| [agent-browser](skills/creative-design/open-design/agent-browser/SKILL.md) | Browser automation CLI for AI agents. Use when the user needs to inspect, test, or automate browser behavior: navigating pages, filling forms, clicking buttons, taking screenshots… |
| [ai-music-album](skills/creative-design/open-design/ai-music-album/SKILL.md) | Full-lifecycle AI music album production — concept, lyric drafting, track sequencing, and export. Useful for indie album experiments and brand soundtracks. |
| [algorithmic-art](skills/creative-design/open-design/algorithmic-art/SKILL.md) | Create generative art using p5.js with seeded randomness so every render is reproducible. Useful for procedural posters, motion-style stills, and artistic frame studies. |
| [animate](skills/creative-design/open-design/animate/SKILL.md) | Implement purposeful interface animations: easing, springs, interruption, exits, and reduced motion. Use on existing components or an accepted UI brief; this is not a video templa… |
| [apple-hig](skills/creative-design/open-design/apple-hig/SKILL.md) | Apple Human Interface Guidelines as 14 agent skills covering platforms, foundations, components, patterns, inputs, and technologies for iOS, macOS, visionOS, watchOS, and tvOS. |
| [article-magazine](skills/creative-design/open-design/article-magazine/SKILL.md) | Huashu / huashu-md-html-inspired magazine article layout for turning Markdown or notes into a polished long-form HTML essay. |
| [artifacts-builder](skills/creative-design/open-design/artifacts-builder/SKILL.md) | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). |
| [brainstorming](skills/creative-design/open-design/brainstorming/SKILL.md) | Transform rough ideas into fully-formed designs through structured questioning and alternative exploration. Useful early in concept work. |
| [brand-extract](skills/creative-design/open-design/brand-extract/SKILL.md) | Extract a complete Brand Kit from a live website by driving the in-app browser. Use when a brand-extraction project opens with a site in the Browser tab, or when the user asks to… |
| [brand-guidelines](skills/creative-design/open-design/brand-guidelines/SKILL.md) | Apply Anthropic's official brand colors and typography to artifacts for consistent visual identity and professional design standards. A reference for shaping your own. |
| [brandkit](skills/creative-design/open-design/brandkit/SKILL.md) | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. Trained for minimalist, cinem… |
| [industrial-brutalist-ui](skills/creative-design/open-design/brutalist-skill/SKILL.md) | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian color, analog degradation effects… |
| [canvas-design](skills/creative-design/open-design/canvas-design/SKILL.md) | Create beautiful visual art in PNG and PDF documents using design philosophy and aesthetic principles for posters, illustrations, and static pieces. |
| [card-twitter](skills/creative-design/open-design/card-twitter/SKILL.md) | Twitter quote or data card designed to pair with a post. |
| [card-xiaohongshu](skills/creative-design/open-design/card-xiaohongshu/SKILL.md) | Xiaohongshu-style knowledge cards, arranged as a swipeable multi-card carousel. |
| [chat-motion-overlay](skills/creative-design/open-design/chat-motion-overlay/SKILL.md) | Generate configurable chat motion overlays from a transcript or screenshot, including plain bubble scenes, app-style chat containers, optional device frames, preset or uploaded av… |
| [color-expert](skills/creative-design/open-design/color-expert/SKILL.md) | Color science expert skill with 286K words of reference material covering OKLCH/OKLAB, palette generation, accessibility/contrast, color naming, pigment mixing, and historical col… |
| [competitive-ads-extractor](skills/creative-design/open-design/competitive-ads-extractor/SKILL.md) | Extract and analyze competitors' ads from ad libraries to understand messaging and creative approaches that resonate. |
| [copywriting](skills/creative-design/open-design/copywriting/SKILL.md) | Write and rewrite marketing copy for landing pages, homepages, and ads. Useful as a copy chief partner during launches. |
| [creative-director](skills/creative-design/open-design/creative-director/SKILL.md) | AI creative director with recursive self-assessment: 20+ methodologies (SIT, TRIZ, Bisociation, SCAMPER, Synectics), 3-axis evaluation calibrated against Cannes/D&AD/HumanKind, 5-… |
| [d3-visualization](skills/creative-design/open-design/d3-visualization/SKILL.md) | Teaches the agent to produce D3 charts and interactive data visualizations. A comprehensive D3.js skill with examples across chart types and techniques giving the agent expert-lev… |
| [data-report](skills/creative-design/open-design/data-report/SKILL.md) | Turns CSV, Excel, or JSON data into a polished visual report page. |
| [deck-guizang-editorial](skills/creative-design/open-design/deck-guizang-editorial/SKILL.md) | Editorial magazine meets e-ink: 10 layouts and 5 palettes (Ink, Indigo Porcelain, Forest Ink, Kraft Paper, Dune). |
| [deck-open-slide-canvas](skills/creative-design/open-design/deck-open-slide-canvas/SKILL.md) | Locked 1920x1080 canvas deck with React component-level free composition, not bound to a fixed template. |
| [deck-swiss-international](skills/creative-design/open-design/deck-swiss-international/SKILL.md) | 16-column grid, one saturated accent, and 22 locked layouts (Klein Blue, Lemon, Mint, Safety Orange). |
| [design-brief](skills/creative-design/open-design/design-brief/SKILL.md) | Parse a structured design brief written in I-Lang protocol format into a concrete design spec. Eliminates ambiguity from vague requests like "make it professional" by requiring ex… |
| [design-consultation](skills/creative-design/open-design/design-consultation/SKILL.md) | Build a complete design system from scratch with creative risks and realistic product mockups. Useful for kickoff workshops and brand-from-zero work. |
| [design-md](skills/creative-design/open-design/design-md/SKILL.md) | Create and manage DESIGN.md files. Useful for capturing design direction, tokens, and visual rules in a single source of truth. |
| [design-review](skills/creative-design/open-design/design-review/SKILL.md) | Designer Who Codes: visual audit then fixes with atomic commits and before/after screenshots. Useful for tightening shipped UI before launch. |
| [digits-fintech-swiss-template](skills/creative-design/open-design/digits-fintech-swiss-template/SKILL.md) | Swiss-grid fintech deck template in black / warm paper / neon-lime contrast. Use when users ask for premium data-story slides with strict modular layout, bold numeric cards, restr… |
| [doc](skills/creative-design/open-design/doc/SKILL.md) | Read, create, and edit .docx documents with formatting and layout fidelity via OpenAI's document skill. |
| [doc-kami-parchment](skills/creative-design/open-design/doc-kami-parchment/SKILL.md) | Warm parchment canvas (#f5f4ed), monochrome ink-blue accent (#1B365D), one serif family, and editorial-grade typography. |
| [docx](skills/creative-design/open-design/docx/SKILL.md) | Create, edit, and analyze Word documents with tracked changes, comments, and formatting. Useful for design briefs, copy docs, and review-ready deliverables. |
| [domain-name-brainstormer](skills/creative-design/open-design/domain-name-brainstormer/SKILL.md) | Generate creative domain name ideas and check availability across multiple TLDs including .com, .io, .dev, and .ai. |
| [ecommerce-image-workflow](skills/creative-design/open-design/ecommerce-image-workflow/SKILL.md) | Reference-product ecommerce image workflow for generating a compact set of product-faithful main, feature, and lifestyle images from real product reference photos. V1 requires upl… |
| [editorial-burgundy-principles-template](skills/creative-design/open-design/editorial-burgundy-principles-template/SKILL.md) | Editorial studio deck template in burgundy / blush / muted-gold palette. Use when users ask for premium manifesto or culture slides with pill tags, large typographic statements, p… |
| [emil-design-eng](skills/creative-design/open-design/emil-design-eng/SKILL.md) | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great. |
| [emilkowalski-motion](skills/creative-design/open-design/emilkowalski-motion/SKILL.md) | Motion-design follow-up skill inspired by Emil Kowalski's animation guidance. Use after an interface exists to add tasteful micro-interactions, state transitions, and page motion… |
| [enhance-prompt](skills/creative-design/open-design/enhance-prompt/SKILL.md) | Improve prompts with design specs and UI/UX vocabulary. Useful for design-to-code workflows and clarifying requests for visual output. |
| [export-download-debugging](skills/creative-design/open-design/export-download-debugging/SKILL.md) | Diagnose and fix browser, preview, or Electron export/download failures, especially image export issues involving Save As, Blob/Data URLs, the File System Access API, createWritab… |
| [fal-3d](skills/creative-design/open-design/fal-3d/SKILL.md) | Generate 3D models from text or images via fal.ai. Useful for game assets, AR previews, product mockups, and concept sculpting. |
| [fal-generate](skills/creative-design/open-design/fal-generate/SKILL.md) | Generate images and videos using fal.ai AI models. Production-grade catalogue covering Flux, SDXL, ideogram, and other community-hosted endpoints. |
| [fal-image-edit](skills/creative-design/open-design/fal-image-edit/SKILL.md) | AI-powered image editing with style transfer, background removal, object removal, and inpainting via fal.ai hosted models. |
| [fal-kling-o3](skills/creative-design/open-design/fal-kling-o3/SKILL.md) | Generate images and videos with Kling O3 — Kling's most powerful model family — via fal.ai. |
| [fal-lip-sync](skills/creative-design/open-design/fal-lip-sync/SKILL.md) | Create talking head videos and lip sync audio to video via fal.ai. Useful for explainer avatars, multilingual dubbing previews, and social cuts. |
| [fal-realtime](skills/creative-design/open-design/fal-realtime/SKILL.md) | Real-time and streaming AI image generation via fal.ai. Suited for moodboard exploration, draft variations, and rapid creative iteration. |
| [fal-restore](skills/creative-design/open-design/fal-restore/SKILL.md) | Restore and fix image quality — deblur, denoise, fix faces, and restore old documents using fal.ai's hosted restoration models. |
| [fal-train](skills/creative-design/open-design/fal-train/SKILL.md) | Train custom AI models (LoRA) on fal.ai for personalized image generation tailored to a brand, character, or style. |
| [fal-tryon](skills/creative-design/open-design/fal-tryon/SKILL.md) | Virtual try-on — see how clothes look on a person via fal.ai's hosted try-on models. Useful for ecommerce, lookbooks, and styling experiments. |
| [fal-upscale](skills/creative-design/open-design/fal-upscale/SKILL.md) | Upscale and enhance image and video resolution using AI super-resolution models hosted on fal.ai. |
| [fal-video-edit](skills/creative-design/open-design/fal-video-edit/SKILL.md) | Edit existing videos using AI — remix style, upscale, remove background, and add audio via fal.ai's hosted video models. |
| [fal-vision](skills/creative-design/open-design/fal-vision/SKILL.md) | Analyze images — segment objects, detect, run OCR, describe, and answer visual questions via fal.ai vision models. |
| [faq-page](skills/creative-design/open-design/faq-page/SKILL.md) | A Frequently Asked Questions (FAQ) page with collapsible accordion sections, search functionality, and category filtering. Use when the brief asks for "FAQ", "help center", "quest… |
| [field-notes-editorial-template](skills/creative-design/open-design/field-notes-editorial-template/SKILL.md) | Editorial "Field Notes" report template with soft paper background, serif hero typography, rounded pastel insight cards, and a retention chart panel. Use when users ask for a prem… |
| [figma-code-connect-components](skills/creative-design/open-design/figma-code-connect-components/SKILL.md) | Connect Figma design components to code components using Code Connect so design-system updates flow into the codebase automatically. |
| [figma-create-design-system-rules](skills/creative-design/open-design/figma-create-design-system-rules/SKILL.md) | Generate project-specific design system rules for Figma-to-code workflows. Useful for capturing tokens, naming, and lint rules in one source. |
| [figma-create-new-file](skills/creative-design/open-design/figma-create-new-file/SKILL.md) | Create a new blank Figma Design or FigJam file. Useful as the first step in scripted design-system or workshop workflows. |
| [figma-generate-design](skills/creative-design/open-design/figma-generate-design/SKILL.md) | Build or update screens in Figma from code or description using design system components. Translate app pages into Figma using design tokens. |
| [figma-generate-library](skills/creative-design/open-design/figma-generate-library/SKILL.md) | Build or update a professional-grade design system library in Figma from a codebase. Useful for keeping the Figma source of truth in sync with shipped components. |
| [figma-implement-design](skills/creative-design/open-design/figma-implement-design/SKILL.md) | Translate Figma designs into production-ready code with 1:1 visual fidelity. Useful for handing off Figma frames straight to a frontend agent. |
| [figma-use](skills/creative-design/open-design/figma-use/SKILL.md) | Run Figma Plugin API scripts for canvas writes, inspections, variables, and design-system work. Prerequisite for every other Figma skill in this catalogue. |
| [flutter-animating-apps](skills/creative-design/open-design/flutter-animating-apps/SKILL.md) | Implement animated effects, transitions, and motion in Flutter apps. Useful for native iOS/Android motion design. |
| [frame-data-chart-nyt](skills/creative-design/open-design/frame-data-chart-nyt/SKILL.md) | NYT-newsroom typography, staggered reveal animation, and editorial-grade charts (line, bar, or range band). |
| [frame-flowchart-sticky](skills/creative-design/open-design/frame-flowchart-sticky/SKILL.md) | SVG curve connectors, sticky-note nodes, and cursor interaction with a whiteboard-brainstorm feel. |
| [frame-glitch-title](skills/creative-design/open-design/frame-glitch-title/SKILL.md) | Digital glitch, chromatic offset, and data-corruption title frame for video transitions or cyberpunk heroes. |
| [frame-light-leak-cinema](skills/creative-design/open-design/frame-light-leak-cinema/SKILL.md) | Film light leaks, grain, 16:9 letterbox, and large serif type for cinematic openings or chapter cards. |
| [frame-liquid-bg-hero](skills/creative-design/open-design/frame-liquid-bg-hero/SKILL.md) | WebGL-style fluid displacement background with a quote overlay, suited to video intros, landing heroes, or posters. |
| [frame-logo-outro](skills/creative-design/open-design/frame-logo-outro/SKILL.md) | Segmented logo assembly, glow bloom, and tagline reveal for video outros or brand closing frames. |
| [frame-macos-notification](skills/creative-design/open-design/frame-macos-notification/SKILL.md) | Realistic macOS notification banner with app icon, title, and body, suited to video overlays or product teasers. |
| [frontend-design](skills/creative-design/open-design/frontend-design/SKILL.md) | Create distinctive, production-grade frontend interfaces with strong visual direction, polished typography, considered layout, and working HTML/CSS/JS or framework code. Use for w… |
| [frontend-dev](skills/creative-design/open-design/frontend-dev/SKILL.md) | Full-stack frontend with cinematic animations, AI-generated media via MiniMax API, and generative art. Useful for hero pages and showcase sites. |
| [frontend-skill](skills/creative-design/open-design/frontend-skill/SKILL.md) | Create visually strong landing pages, websites, and app UIs with restrained composition. OpenAI's production frontend playbook. |
| [frontend-slides](skills/creative-design/open-design/frontend-slides/SKILL.md) | Generate animation-rich HTML presentations with visual style previews. Useful for online keynotes, embedded talks, and interactive briefs. |
| [full-page-screenshot](skills/creative-design/open-design/full-page-screenshot/SKILL.md) | Capture full-page screenshots of web pages via Chrome DevTools Protocol with zero dependencies. Useful for portfolios, case studies, and audit reports. |
| [gif-sticker-maker](skills/creative-design/open-design/gif-sticker-maker/SKILL.md) | Convert photos into animated GIF stickers in Funko Pop / Pop Mart style via the MiniMax API. Useful for personalized chat stickers and avatar packs. |
| [gpt-taste](skills/creative-design/open-design/gpt-tasteskill/SKILL.md) | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide editorial typography (bans 6-line wrap… |
| [gsap-core](skills/creative-design/open-design/gsap-core/SKILL.md) | Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, prefers-reduced-motion). Use when the user… |
| [gsap-frameworks](skills/creative-design/open-design/gsap-frameworks/SKILL.md) | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user wants animation in Vue, Nuxt, Svelte, Sve… |
| [gsap-performance](skills/creative-design/open-design/gsap-performance/SKILL.md) | Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching. Use when optimizing GSAP animations, reducing jank, or when the user asks a… |
| [gsap-plugins](skills/creative-design/open-design/gsap-plugins/SKILL.md) | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG and physics plugins, CustomEa… |
| [gsap-react](skills/creative-design/open-design/gsap-react/SKILL.md) | Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. Use when the user wants animation in React or Next.js, or asks about GSAP with React, useGSAP, or clea… |
| [gsap-scrolltrigger](skills/creative-design/open-design/gsap-scrolltrigger/SKILL.md) | Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. Use when building or recommending scroll-based animation, parallax, pinned sections, or… |
| [gsap-timeline](skills/creative-design/open-design/gsap-timeline/SKILL.md) | Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback. Use when sequencing animations, choreographing keyframes, or when the user asks about a… |
| [gsap-utils](skills/creative-design/open-design/gsap-utils/SKILL.md) | Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe. Use when the user asks about gsap.utils, clamp, mapRange, random,… |
| [hand-drawn-diagrams](skills/creative-design/open-design/hand-drawn-diagrams/SKILL.md) | Generate hand-drawn Excalidraw diagrams from a prompt — animated SVG, hosted edit link, and PNG export. Works with Claude Code, Codex, Gemini CLI, and any agent supporting standar… |
| [hatch-pet](skills/creative-design/open-design/hatch-pet/SKILL.md) | Create, repair, validate, preview, and package Codex-compatible animated pet spritesheets from character art, screenshots, generated images, or visual references. Use when a user… |
| [html-ppt-retro-quarterly-review](skills/creative-design/open-design/html-ppt-retro-quarterly-review/SKILL.md) | Retro Quarterly Review presentation template in a bold blue + orange editorial language. Use when users ask for a high-impact quarterly review / roadmap deck with heavyweight slab… |
| [huashu-art-motion](skills/creative-design/open-design/huashu-art-motion/SKILL.md) | 辅助艺术动画与解说任务：35 种艺术风格配方、9 种解说语法、分镜与确定性 Canvas 绘制工具。按宿主时间轴实现，素材与导出使用宿主能力。 |
| [image-enhancer](skills/creative-design/open-design/image-enhancer/SKILL.md) | Improve image and screenshot quality by enhancing resolution, sharpness, and clarity for professional presentations and documentation. |
| [image-to-code](skills/creative-design/open-design/image-to-code-skill/SKILL.md) | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, then implement the website t… |
| [imagegen](skills/creative-design/open-design/imagegen/SKILL.md) | Generate and edit images using OpenAI's Image API for project assets — UI mockups, icons, illustrations, social cards, and visual references. |
| [imagegen-frontend-mobile](skills/creative-design/open-design/imagegen-frontend-mobile/SKILL.md) | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobile products. Prioritizes clea… |
| [imagegen-frontend-web](skills/creative-design/open-design/imagegen-frontend-web/SKILL.md) | Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate horizontal image FOR EVERY se… |
| [imagen](skills/creative-design/open-design/imagen/SKILL.md) | Generate images using Google Gemini's image generation API for UI mockups, icons, illustrations, and visual assets. |
| [impeccable-design-polish](skills/creative-design/open-design/impeccable-design-polish/SKILL.md) | Follow-up design polish skill inspired by Impeccable. Use after a web or HTML artifact exists to audit, critique, polish, animate, harden, and prepare the page for a live/share pa… |
| [library-curator](skills/creative-design/open-design/library-curator/SKILL.md) | Search the OD Library (the global asset registry) and apply matching assets into the current project mid-task. Use when the user asks to reuse an image they captured/uploaded earl… |
| [login-flow](skills/creative-design/open-design/login-flow/SKILL.md) | Mobile login and authentication flow screens |
| [marketing-psychology](skills/creative-design/open-design/marketing-psychology/SKILL.md) | Apply psychological principles and behavioral science to copy and design. Useful for tightening hooks, framing, and pricing presentation. |
| [minimalist-ui](skills/creative-design/open-design/minimalist-skill/SKILL.md) | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows. |
| [minimax-docx](skills/creative-design/open-design/minimax-docx/SKILL.md) | Professional DOCX document creation and editing using OpenXML SDK. Useful for branded reports, polished proposals, and template-based authoring. |
| [minimax-pdf](skills/creative-design/open-design/minimax-pdf/SKILL.md) | Generate, fill, and reformat PDFs with a token-based design system and 15 cover styles. Useful for branded PDFs, e-guides, and reports. |
| [mockup-device-3d](skills/creative-design/open-design/mockup-device-3d/SKILL.md) | Static iPhone and MacBook 3D-style showcase with real HTML embedded on screens, glass-lens refraction, and 360-degree turntable composition. |
| [motion-design](skills/creative-design/open-design/motion-design/SKILL.md) | Apply motion craft to an active task: refine a brief, beat map, visual continuity, typography, pacing, and timeline implementation. Use when planning or improving motion graphics;… |
| [motion-lab](skills/creative-design/open-design/motion-lab/SKILL.md) | 为当前网页或组件查找、选型和改造动效。包含 160 个案例的 HTML/CSS/JS、参数与中英文索引，覆盖基础、文字、交互和高级动效。 |
| [nanobanana-ppt](skills/creative-design/open-design/nanobanana-ppt/SKILL.md) | AI-powered PPT generation with document analysis and styled images via the NanoBanana stack. Combines image generation with structured deck output. |
| [od-next-media-inputs](skills/creative-design/open-design/od-next-media-inputs/SKILL.md) | Prepare required media inputs within an existing OD Next plan. Reuse capability evidence, acquire and measure assets efficiently, and resolve asynchronous jobs without removing re… |
| [oil-motion](skills/creative-design/open-design/oil-motion/SKILL.md) | 处理视频和序列帧，编译滚动、指针、拖动与状态驱动的网页动效；内含本地媒体处理脚本和运行时。新素材生成使用宿主工具。 |
| [full-output-enforcement](skills/creative-design/open-design/output-skill/SKILL.md) | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any task requiring exhaus… |
| [paywall-upgrade-cro](skills/creative-design/open-design/paywall-upgrade-cro/SKILL.md) | Design and optimize upgrade screens, paywalls, and upsell modals. Useful for SaaS conversion design and pricing-page experiments. |
| [pdf](skills/creative-design/open-design/pdf/SKILL.md) | Extract text, create PDFs, and handle forms. Useful for press releases, branded one-pagers, and printable design deliverables. |
| [pixelbin-media](skills/creative-design/open-design/pixelbin-media/SKILL.md) | Generate and edit images and videos with an 85+ API portfolio and build visually appealing website pages via Pixelbin. |
| [plan-design-review](skills/creative-design/open-design/plan-design-review/SKILL.md) | Senior Designer review: rates each design dimension 0-10, explains what a 10 looks like, and flags AI Slop signals. Useful as a gate before merging UI work. |
| [platform-design](skills/creative-design/open-design/platform-design/SKILL.md) | 300+ design rules from Apple HIG, Material Design 3, and WCAG 2.2 for cross-platform apps. Useful when shipping a single design across iOS, Android, and the web. |
| [poster-hero](skills/creative-design/open-design/poster-hero/SKILL.md) | Vertical poster or Moments-style share image with strong visual impact. |
| [ppt-keynote](skills/creative-design/open-design/ppt-keynote/SKILL.md) | Apple Keynote-quality slides, one card per screen, with keyboard left/right navigation. |
| [pptx](skills/creative-design/open-design/pptx/SKILL.md) | Read, generate, and adjust PowerPoint slides, layouts, and templates. Useful for executive decks, training material, and product reviews. |
| [pptx-generator](skills/creative-design/open-design/pptx-generator/SKILL.md) | Create and edit PowerPoint presentations from scratch with PptxGenJS — MiniMax's production-tested deck pipeline. |
| [pptx-html-fidelity-audit](skills/creative-design/open-design/pptx-html-fidelity-audit/SKILL.md) | Audit a python-pptx export against its source HTML deck, identify layout/content drift (footer overflow, cropped content, missing italic/em, lost styling, off-rhythm spacing), and… |
| [pr-feedback-quality-gate](skills/creative-design/open-design/pr-feedback-quality-gate/SKILL.md) | Safely track pull request feedback, resolve review comments or merge conflicts, validate fixes, and use a read-only cross-review before committing or pushing follow-up changes. |
| [redesign-existing-projects](skills/creative-design/open-design/redesign-skill/SKILL.md) | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards without breaking functionality… |
| [reference-design-contract](skills/creative-design/open-design/reference-design-contract/SKILL.md) | Turn vague taste, screenshots, URLs, product notes, or "make it feel like this" references into a grounded DESIGN.md plus an implementation handoff. Use it before prototypes, deck… |
| [release-notes-one-pager](skills/creative-design/open-design/release-notes-one-pager/SKILL.md) | Release notes one-page HTML with highlights, Added, Fixed, Breaking changes, Known issues, and Upgrade note. Writes explicit "None" style sections whenever the user does not provi… |
| [remotion](skills/creative-design/open-design/remotion/SKILL.md) | Programmatic video creation with React. Useful for branded explainers, social cuts, dashboards-to-video, and reproducible motion graphics. |
| [replicate](skills/creative-design/open-design/replicate/SKILL.md) | Discover, compare, and run AI models using Replicate's API. Strong fit for image, audio, and video generation pipelines that swap models frequently. |
| [research-decision-room](skills/creative-design/open-design/research-decision-room/SKILL.md) | Turn messy user research notes, interviews, support tickets, surveys, and product context into an evidence-backed decision room: a single HTML artifact with an evidence ledger, th… |
| [resume-modern](skills/creative-design/open-design/resume-modern/SKILL.md) | Modern minimal resume, single A4 page, ready for print or PDF export. |
| [review-animations](skills/creative-design/open-design/review-animations/SKILL.md) | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to flagging; approval is earned. |
| [screenshot](skills/creative-design/open-design/screenshot/SKILL.md) | Capture desktop, app windows, or pixel regions across OS platforms. Useful for marketing screenshots, design reviews, and bug reports. |
| [screenshots-marketing](skills/creative-design/open-design/screenshots-marketing/SKILL.md) | Generate marketing screenshots with Playwright. Useful for landing-page hero shots, App Store screenshots, and changelog visuals. |
| [shadcn-ui](skills/creative-design/open-design/shadcn-ui/SKILL.md) | Build UI components with shadcn/ui. Pairs with the Stitch design loop to ship structured, accessible components quickly. |
| [shader-dev](skills/creative-design/open-design/shader-dev/SKILL.md) | GLSL shader techniques for ray marching, fluid simulation, particle systems, and procedural generation. Useful for hero visuals and motion stills. |
| [slack-gif-creator](skills/creative-design/open-design/slack-gif-creator/SKILL.md) | Create animated GIFs optimized for Slack with validators for size constraints and composable animation primitives. |
| [slides](skills/creative-design/open-design/slides/SKILL.md) | Create and edit .pptx presentation decks with PptxGenJS. Useful for sales decks, kickoff briefs, and design-system showcases. |
| [social-reddit-card](skills/creative-design/open-design/social-reddit-card/SKILL.md) | Realistic Reddit post card with vote rail and comment count, suited to video overlays or story sharing. |
| [social-spotify-card](skills/creative-design/open-design/social-spotify-card/SKILL.md) | Spotify Now Playing-style card with album art, progress bar, and playback controls, suited to video overlays or personal homepages. |
| [social-x-post-card](skills/creative-design/open-design/social-x-post-card/SKILL.md) | Realistic X post card with engagement metrics (likes, reposts, views), suited to video overlays or shareable image cards. |
| [high-end-visual-design](skills/creative-design/open-design/soft-skill/SKILL.md) | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel expensive. Blocks all the comm… |
| [sora](skills/creative-design/open-design/sora/SKILL.md) | Generate, remix, and manage short video clips via OpenAI's Sora API. Useful for cinematic shots, b-roll, and rapid concept video iteration. |
| [speech](skills/creative-design/open-design/speech/SKILL.md) | Generate spoken audio from text using OpenAI's API with built-in voices. Useful for narrated explainers, lecture audio, and quick voiceover tracks. |
| [stitch-loop](skills/creative-design/open-design/stitch-loop/SKILL.md) | Iterative design-to-code feedback loop. Critique → adjust → ship cycle for tightening visual fidelity between brief and built UI. |
| [stitch-design-taste](skills/creative-design/open-design/stitch-skill/SKILL.md) | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography, calibrated color, asy… |
| [swiftui-design](skills/creative-design/open-design/swiftui-design/SKILL.md) | SwiftUI 前端设计 skill — anti AI-slop rules, design direction advisor, brand asset protocol, and five-dimension review. Works with Claude Code, Cursor, Codex, and OpenCode. |
| [swiss-creative-mode-template](skills/creative-design/open-design/swiss-creative-mode-template/SKILL.md) | Swiss-inspired creative-mode presentation template skill with bold editorial typography, high-contrast geometric cards, interactive slide navigation, theme switching, hotspot over… |
| [swiss-user-research-video-template](skills/creative-design/open-design/swiss-user-research-video-template/SKILL.md) | Swiss-style user-research narrative template in warm-paper editorial aesthetics. Use when users ask for a premium research deck or story-first live artifact with minimalist typogr… |
| [design-taste-frontend](skills/creative-design/open-design/taste-skill/SKILL.md) | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look template… |
| [design-taste-frontend-v1](skills/creative-design/open-design/taste-skill-v1/SKILL.md) | The original v1 taste-skill, preserved for projects depending on its exact behavior. The current default is `design-taste-frontend` (v2 experimental), which is a substantial rewri… |
| [theme-factory](skills/creative-design/open-design/theme-factory/SKILL.md) | Apply professional font and color themes to artifacts including slides, docs, reports, and HTML landing pages. Ships 10 pre-set themes. |
| [threejs](skills/creative-design/open-design/threejs/SKILL.md) | Three.js skills for creating 3D elements and interactive experiences in the browser — scenes, materials, controls, and post-processing. |
| [ui-animation](skills/creative-design/open-design/ui-animation/SKILL.md) | Implement, review, and measure UI motion. Reconstruct easing, springs and gestures from a recording using bundled frame extraction, tracking and curve-fitting tools when available. |
| [ui-skills](skills/creative-design/open-design/ui-skills/SKILL.md) | Opinionated, evolving constraints to guide agents when building interfaces. Useful for keeping output coherent across many small UI pieces. |
| [ui-ux-pro-max](skills/creative-design/open-design/ui-ux-pro-max/SKILL.md) | Catalog-only UI/UX Pro Max entry. The full upstream templates, data, and search workflow are not bundled in OpenDesign. |
| [venice-audio-music](skills/creative-design/open-design/venice-audio-music/SKILL.md) | Music generation queueing, retrieval, and completion endpoints via Venice.ai. Suited for jingles, background loops, and prototype scoring. |
| [venice-audio-speech](skills/creative-design/open-design/venice-audio-speech/SKILL.md) | Text-to-speech models, voices, formats, and streaming via Venice.ai. Useful for narration, voiceover, and conversational agent voices. |
| [venice-image-edit](skills/creative-design/open-design/venice-image-edit/SKILL.md) | Image edits, upscaling, and background removal via the Venice.ai API. |
| [venice-image-generate](skills/creative-design/open-design/venice-image-generate/SKILL.md) | Image generation endpoints and available styles via the Venice.ai API. |
| [venice-video](skills/creative-design/open-design/venice-video/SKILL.md) | Video generation and transcription workflows via the Venice.ai API. |
| [vfx-text-cursor](skills/creative-design/open-design/vfx-text-cursor/SKILL.md) | Cursor light trail, chromatic rays, and directional flares for word-by-word quote reveals in video intros. |
| [video-downloader](skills/creative-design/open-design/video-downloader/SKILL.md) | Download videos from YouTube and other platforms for offline viewing, editing, or archival with support for various formats and quality options. |
| [video-hyperframes](skills/creative-design/open-design/video-hyperframes/SKILL.md) | Hyperframes / Remotion-compatible continuous frame animation with autoplay support. |
| [web-artifacts-builder](skills/creative-design/open-design/web-artifacts-builder/SKILL.md) | Build complex claude.ai HTML artifacts with React and Tailwind. Anthropic's reference workflow for shipping rich, embeddable artifacts. |
| [web-clone](skills/creative-design/open-design/web-clone/SKILL.md) | 网站复刻 / 克隆方法论。USE WHEN 用户说 复刻网站、克隆网站、clone website、抄个站、仿站、 照着这个站做一个、reproduce site、还原某个网页效果、把这个站搬下来改成我的、 复刻某个交互/WebGL/Canvas/Three.js 效果。提供「先拿真源码 → 判路径 → 逆向拆解 → 搭工程 → 替换内容」的可移植决策树，… |
| [web-design-guidelines](skills/creative-design/open-design/web-design-guidelines/SKILL.md) | Review UI code for Web Interface Guidelines compliance by the Vercel engineering team. Covers layout, typography, color, motion, and accessibility for product UI. |
| [weread-year-in-review-video-template](skills/creative-design/open-design/weread-year-in-review-video-template/SKILL.md) | WeRead-inspired HyperFrames video template for vertical annual reading reports, personal reading dashboards, book-note recaps, and shareable year-in-review stories. Use when users… |
| [wpds](skills/creative-design/open-design/wpds/SKILL.md) | WordPress Design System. Apply WordPress's official design tokens, typography, and component patterns to themes and sites. |
| [writing-guidelines](skills/creative-design/open-design/writing-guidelines/SKILL.md) | Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style", "audit prose", "review docs voice and tone", or "check this page ag… |
| [youtube-clipper](skills/creative-design/open-design/youtube-clipper/SKILL.md) | YouTube clip generation and editing with automated workflows — pull source video, slice highlights, add captions, and export. |

<a id="creative-design-stitch-skills"></a>

### stitch-skills（16 個）

Google Stitch 的 UI 設計 SKILL：設計、建置、工具三組。資料夾：[`skills/creative-design/stitch-skills`](skills/creative-design/stitch-skills)

| SKILL | 原始說明 |
|---|---|
| [stitch-build/skills/stitch::react-components](skills/creative-design/stitch-skills/stitch-build/skills/react-components/SKILL.md) | Converts Stitch designs into modular Vite and React components, or syncs/updates existing React components to align with the latest Stitch designs, using system-level networking a… |
| [stitch-build/skills/stitch::react-native](skills/creative-design/stitch-skills/stitch-build/skills/react-native/SKILL.md) | Convert Stitch HTML designs to React Native components, or syncs/updates existing native components to align with the latest Stitch designs, using StyleSheet. |
| [stitch-build/skills/react-vite-dashboard](skills/creative-design/stitch-skills/stitch-build/skills/react-vite-dashboard/SKILL.md) | Convert Stitch designs into production React + Vite dashboards with TanStack Query, accessible tokens from DESIGN.md, and Web3-ready patterns (ethers/viem). |
| [stitch-build/skills/remotion](skills/creative-design/stitch-skills/stitch-build/skills/remotion/SKILL.md) | Generate walkthrough videos from Stitch projects using Remotion with smooth transitions, zooming, and text overlays |
| [stitch-build/skills/shadcn-ui](skills/creative-design/stitch-skills/stitch-build/skills/shadcn-ui/SKILL.md) | Expert guidance for integrating and building applications with shadcn/ui components, including component discovery, installation, customization, and best practices. |
| [stitch-design/skills/stitch::code-to-design](skills/creative-design/stitch-skills/stitch-design/skills/code-to-design/SKILL.md) | Convert frontend code (Vite, React, Angular, Vue, etc.) to a Stitch Design by chaining static HTML extraction, design system extraction, and file upload. **ALWAYS** use this skill… |
| [stitch-design/skills/stitch::extract-design-md](skills/creative-design/stitch-skills/stitch-design/skills/extract-design-md/SKILL.md) | Extract a comprehensive design system (DESIGN.md) directly from frontend source code — React, Vue, Svelte, Angular, plain HTML/CSS, or any web framework. Analyzes component files,… |
| [stitch-design/skills/stitch::extract-static-html](skills/creative-design/stitch-skills/stitch-design/skills/extract-static-html/SKILL.md) | Extract self-contained static HTML from a built web application or React components by inlining CSS and images. Use this skill whenever you need to capture a specific UI state, sh… |
| [stitch-design/skills/stitch::generate-design](skills/creative-design/stitch-skills/stitch-design/skills/generate-design/SKILL.md) | Generate new screens from text prompts or images, edit existing screens with prompts and design system tokens, and generate design variants using Stitch MCP. Includes prompt enhan… |
| [stitch-design/skills/stitch::manage-design-system](skills/creative-design/stitch-skills/stitch-design/skills/manage-design-system/SKILL.md) | Manage design systems in Stitch using MCP tools. Includes retrieval of assets, creating/updating design systems in Stitch, and applying them to screens. |
| [stitch-design/skills/stitch::upload-to-stitch](skills/creative-design/stitch-skills/stitch-design/skills/upload-to-stitch/SKILL.md) | Upload local assets (images, mockups, extracted HTML, design markdown) to a Stitch project. ALWAYS use this skill when you need to upload visual assets, HTML pages, or design docs… |
| [stitch-utilities/skills/design-md](skills/creative-design/stitch-skills/stitch-utilities/skills/design-md/SKILL.md) | Analyze Stitch projects and synthesize a semantic design system into DESIGN.md files |
| [stitch-utilities/skills/enhance-prompt](skills/creative-design/stitch-skills/stitch-utilities/skills/enhance-prompt/SKILL.md) | Transforms vague UI ideas into polished, Stitch-optimized prompts. Enhances specificity, adds UI/UX keywords, injects design system context, and structures output for better gener… |
| [stitch-utilities/skills/site-md](skills/creative-design/stitch-skills/stitch-utilities/skills/site-md/SKILL.md) | Analyze a project description or site requirements and synthesize a project constitution into SITE.md for the Stitch Build Loop |
| [stitch-utilities/skills/stitch-loop](skills/creative-design/stitch-skills/stitch-utilities/skills/stitch-loop/SKILL.md) | Teaches agents to iteratively build websites using Stitch with an autonomous baton-passing loop pattern |
| [stitch-utilities/skills/taste-design](skills/creative-design/stitch-skills/stitch-utilities/skills/taste-design/SKILL.md) | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography, calibrated color, asy… |

## 動畫／影片 (`animation-video`)

| 名稱 | 數量 | 用途 | 關鍵字 | 來源 | 存入日期 |
|---|---|---|---|---|---|
| [anything2explainer](skills/animation-video/anything2explainer/SKILL.md) | 1 | 給主題就產出解說影片（Remotion 模板） | 解說影片, explainer | [Vincentwei1021/anything2explainer](https://github.com/Vincentwei1021/anything2explainer) `0b85f6c`（自訂授權（見 LICENSE）） | 2026-11-13 |
| [claude-animated-shorts](skills/animation-video/claude-animated-shorts/SKILL.md) | 1 | 3D 世界風格的卡通短影音製作流程 | 短影音, 卡通, 3D | [mromidev/claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts) `e3b817b`（MIT） | 2026-11-13 |
| [garden-skills](#animation-video-garden-skills) | 6 | 動態 showreel、網頁影片簡報、網頁設計工程、美化文章、GPT 生圖、知識庫檢索 | showreel, 影片簡報, 網頁設計 | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) `08150e7`（MIT） | 2026-11-13 |
| [gsap-skills](#animation-video-gsap-skills) | 8 | GSAP 官方：核心、timeline、ScrollTrigger、外掛、React、效能 | gsap, easing, scroll 動畫 | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) `aed9cfd`（MIT） | 2026-11-13 |
| [hyperframes](#animation-video-hyperframes) | 15 | HeyGen HyperFrames：寫 HTML 產出影片；含官方 SKILL 與專案內部的剪輯手法 SKILL | HTML 轉影片, 字幕, 轉場 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) `ff687fe`（Apache-2.0） | 2026-11-13 |
| [motion](skills/animation-video/motion/SKILL.md) | 1 | Motion（前 Framer Motion）與 CSS 動畫：最佳實務、文件與範例搜尋、CSS spring、效能稽核 | motion/react, framer-motion, CSS spring, UI 動畫 | [motiondivision/ai-kit](https://github.com/motiondivision/ai-kit) `1e42494`（MIT） | 2026-11-13 |
| [oil-motion](skills/animation-video/oil-motion/SKILL.md) | 1 | 跟隨捲動與滑鼠的網頁動畫 | scroll 動畫, 滑鼠互動 | [oil-oil/oil-motion](https://github.com/oil-oil/oil-motion) `07e31f2`（MIT） | 2026-11-13 |
| [openmontage](#animation-video-openmontage) | 92 | OpenMontage 影片工作室用到的全部 SKILL：AI 影片生成、配音、字幕、Manim、Three.js、GSAP、Remotion 等 | AI 影片, TTS, manim, threejs, ffmpeg | [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage) `fecb9a1`（AGPL-3.0） | 2026-11-13 |
| [pixelfx](skills/animation-video/pixelfx/SKILL.md) | 1 | 244 種以程式寫成的像素特效 | pixel 特效, shader, canvas | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx) `5294518`（MIT） | 2026-11-13 |
| [remotion](#animation-video-remotion) | 13 | Remotion 官方：用 React 做影片（建立、畫面與動畫、字幕、地圖、輸出、升級、授權） | remotion, react 影片, 字幕, render | [remotion-dev/skills](https://github.com/remotion-dev/skills) v4.0.543 `7e541aa`（見 remotion-license） | 2026-11-13 |
| [video-shotcraft](skills/animation-video/video-shotcraft/SKILL.md) | 1 | 電影感的產品宣傳影片（Remotion 模板與分鏡打磨流程） | 產品宣傳片, 分鏡, remotion | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) `6700db2`（Apache-2.0） | 2026-11-13 |

<a id="animation-video-garden-skills"></a>

### garden-skills（6 個）

動態 showreel、網頁影片簡報、網頁設計工程、美化文章、GPT 生圖、知識庫檢索。資料夾：[`skills/animation-video/garden-skills`](skills/animation-video/garden-skills)

| SKILL | 原始說明 |
|---|---|
| [beautiful-article](skills/animation-video/garden-skills/beautiful-article/SKILL.md) | 把用户提供的素材（网页 URL / PDF / DOCX / Markdown / 纯文本 / 截图 / 粘贴材料）编辑、设计成一篇美丽的、可离线打开和分享的**单文件 HTML 网页文章**。基于 reacticle 组件协议：不手写裸 HTML/CSS，而用语义组件 + 受主题约束的 Raw 自由层；按 source→规划→双确认→生成→终审→修复的小… |
| [gpt-image-2](skills/animation-video/garden-skills/gpt-image-2/SKILL.md) | 面向 GPT Image 2 的图像生成 / 编辑技能。可在 3 种环境下使用：(A) Garden 本地模式，通过 OpenAI 兼容接口直接出图并落盘；(B) Host-Native 模式，把本 Skill 当作提示词工程指引，把渲染好的 prompt 交给宿主 Agent 自带的图像工具出图；(C) Advisor 模式，宿主无任何图像工具时退化为高… |
| [kb-retriever](skills/animation-video/garden-skills/kb-retriever/SKILL.md) | 面向本地知识库目录的检索和问答助手。核心流程：(1)分层索引导航 (2)遇到PDF/Excel时必须先读取references学习处理方法 (3)处理文件后再检索。按文件类型组合使用 grep、Read、pdfplumber、pandas 进行渐进式检索，避免整文件加载。用户问题涉及"从知识库目录回答问题/检索信息/查资料"时使用。 |
| [motion-showreel](skills/animation-video/garden-skills/motion-showreel/SKILL.md) | 用代码制作图形、文字或界面动画视频，输出 MP4 和可编辑源码，最长 20 分钟。适用于动效作品集、产品片、UI 动效、动态排版、Logo 片头、生成艺术与讲解视频；支持独立选择 BGM/音效来源、用户口播，以及用用户提供的口播稿通过 TTS 合成语音。不用于实拍制作、写实人物生成或一般视频剪辑。 |
| [web-design-engineer](skills/animation-video/garden-skills/web-design-engineer/SKILL.md) | Build or redesign polished browser-rendered visual artifacts with HTML/CSS/JavaScript/React: pages, dashboards, prototypes, slide decks, animations, UI mockups, and data visualiza… |
| [web-video-presentation](skills/animation-video/garden-skills/web-video-presentation/SKILL.md) | 把一篇文章或口播稿，做成"看起来像视频"的点击驱动 16:9 网页演示，可选合成口播音频。流程：原始文章 → **一次产出**口播稿 + outline 开发计划 → 用户**一次对齐** 5 件事（稿子 / outline / 主题 / 素材 / 开发模式）→ 网页开发（逐章 / 顺序 / 并行）→ 可选音频合成（provider-agnostic：内置… |

<a id="animation-video-gsap-skills"></a>

### gsap-skills（8 個）

GSAP 官方：核心、timeline、ScrollTrigger、外掛、React、效能。資料夾：[`skills/animation-video/gsap-skills`](skills/animation-video/gsap-skills)

| SKILL | 原始說明 |
|---|---|
| [gsap-core](skills/animation-video/gsap-skills/gsap-core/SKILL.md) | Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, prefers-reduced-motion). Use when the user… |
| [gsap-frameworks](skills/animation-video/gsap-skills/gsap-frameworks/SKILL.md) | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user wants animation in Vue, Nuxt, Svelte, Sve… |
| [gsap-performance](skills/animation-video/gsap-skills/gsap-performance/SKILL.md) | Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching. Use when optimizing GSAP animations, reducing jank, or when the user asks a… |
| [gsap-plugins](skills/animation-video/gsap-skills/gsap-plugins/SKILL.md) | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG and physics plugins, CustomEa… |
| [gsap-react](skills/animation-video/gsap-skills/gsap-react/SKILL.md) | Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. Use when the user wants animation in React or Next.js, or asks about GSAP with React, useGSAP, or clea… |
| [gsap-scrolltrigger](skills/animation-video/gsap-skills/gsap-scrolltrigger/SKILL.md) | Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. Use when building or recommending scroll-based animation, parallax, pinned sections, or… |
| [gsap-timeline](skills/animation-video/gsap-skills/gsap-timeline/SKILL.md) | Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback. Use when sequencing animations, choreographing keyframes, or when the user asks about a… |
| [gsap-utils](skills/animation-video/gsap-skills/gsap-utils/SKILL.md) | Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe. Use when the user asks about gsap.utils, clamp, mapRange, random,… |

<a id="animation-video-hyperframes"></a>

### hyperframes（15 個）

HeyGen HyperFrames：寫 HTML 產出影片；含官方 SKILL 與專案內部的剪輯手法 SKILL。資料夾：[`skills/animation-video/hyperframes`](skills/animation-video/hyperframes)

| SKILL | 原始說明 |
|---|---|
| [claude-skills/captions-overlay](skills/animation-video/hyperframes/claude-skills/captions-overlay/SKILL.md) | Overlay doctrine for captions in HyperFrames videos — the caption MODEL (drop / rail / embed) and the rule that captions are an OVERLAY composited on top of the film, never a rese… |
| [claude-skills/changelog-video](skills/animation-video/hyperframes/claude-skills/changelog-video/SKILL.md) | Turn a weekly changelog .md into a finished branded changelog video (square 1080, ~45-60s, Annie VO, animated brand background, mock-UI visualizations, lowkey captions). Use when… |
| [claude-skills/cut-the-curve](skills/animation-video/hyperframes/claude-skills/cut-the-curve/SKILL.md) | The technique catalog: five velocity-matched SEAMS (zoom-through, INVERSE zoom-through, cut-the-curve, waterfall cut, rack-focus blur-cut) plus the two in-scene techniques — water… |
| [claude-skills/motion-doctrine](skills/animation-video/hyperframes/claude-skills/motion-doctrine/SKILL.md) | GATEWAY — load FIRST before composing any HyperFrames animation or video. The high-level motion law that makes a multi-scene video feel like ONE continuous camera move instead of… |
| [claude-skills/oversized-cursor](skills/animation-video/hyperframes/claude-skills/oversized-cursor/SKILL.md) | House-style oversized macOS cursor technique for HyperFrames launch videos. Load whenever a scene involves cursors or a pointer-led action, when kicking off a UI scene, when ignit… |
| [claude-skills/seam-craft](skills/animation-video/hyperframes/claude-skills/seam-craft/SKILL.md) | Render-correctness doctrine for scene-to-scene seams in HyperFrames launch videos — the prerequisites that make transitions composite correctly on the master timeline. Load when a… |
| [skills/figma](skills/animation-video/hyperframes/skills/figma/SKILL.md) | Bring Figma into a HyperFrames video - rendered assets, brand tokens, components, storyboard frames as reconstructed motion (frames read as states, not slides), shaders and connec… |
| [skills/hyperframes](skills/animation-video/hyperframes/skills/hyperframes/SKILL.md) | Read first to make, edit, animate or render any video with HyperFrames (HTML rendered to video), including launch films, explainers, music videos, charts, maps, vertical clips, ti… |
| [skills/hyperframes-cli](skills/animation-video/hyperframes/skills/hyperframes-cli/SKILL.md) | HyperFrames CLI - scaffold, check frames, edit timelines, preview, render, share and project history; read JSON and recover from failures. |
| [skills/hyperframes-registry](skills/animation-video/hyperframes/skills/hyperframes-registry/SKILL.md) | About 450 ready-made HyperFrames blocks and components installed as editable source - transitions, overlays, titles, kinetic type, captions, charts, map overlays, 3D, camera moves… |
| [skills/media-use](skills/animation-video/hyperframes/skills/media-use/SKILL.md) | Get or make any media for a HyperFrames video - music, sound effects, images, icons, logos, voiceover, avatar and generated video, transcripts, cutouts, colour grades and looks -… |
| [skills/remotion-to-hyperframes](skills/animation-video/hyperframes/skills/remotion-to-hyperframes/SKILL.md) | Bring existing video code or footage into HyperFrames and verify it frame by frame against the original - Remotion first, also Motion Canvas, Lottie, Three.js, p5.js, canvas or pl… |
| [skills/reverse-any-video](skills/animation-video/hyperframes/skills/reverse-any-video/SKILL.md) | Rebuild any video file as an editable HyperFrames project - motion graphics, talking heads, live action or AI-generated footage - checked against the original frame by frame. Use… |
| [skills/slideshow](skills/animation-video/hyperframes/skills/slideshow/SKILL.md) | Build a HyperFrames slideshow to present live - slides, fragment reveals, branching hotspots and presenter mode with speaker notes, served by `hyperframes present` - or turn an ex… |
| [skills/style-sampling](skills/animation-video/hyperframes/skills/style-sampling/SKILL.md) | Make a new episode in a proven video style - Collage Explainer, Finance Explainer, Animated Science Explainer, 3D Brand Explainer, 3D True Crime - on the person's topic. Use for "… |

<a id="animation-video-openmontage"></a>

### openmontage（92 個）

OpenMontage 影片工作室用到的全部 SKILL：AI 影片生成、配音、字幕、Manim、Three.js、GSAP、Remotion 等。資料夾：[`skills/animation-video/openmontage`](skills/animation-video/openmontage)

| SKILL | 原始說明 |
|---|---|
| [3d-asset-generation](skills/animation-video/openmontage/3d-asset-generation/SKILL.md) | Generate, reconstruct, inspect, and route production 3D assets for OpenMontage worlds using Atlas Cloud, fal.ai, licensed catalogs, and Blender. |
| [acestep](skills/animation-video/openmontage/acestep/SKILL.md) | AI music generation with ACE-Step 1.5 — background music, vocal tracks, covers, stem extraction for video production. Use when generating music, soundtracks, jingles, or working w… |
| [agents](skills/animation-video/openmontage/agents/SKILL.md) | Build voice AI agents with ElevenLabs. Use when creating voice assistants, customer service bots, interactive voice characters, or any real-time voice conversation experience. |
| [ai-video-gen](skills/animation-video/openmontage/ai-video-gen/SKILL.md) | Generate AI videos from text prompts using multiple provider gateways. Use when: (1) Generating videos from text descriptions, (2) Creating AI-generated video clips for content pr… |
| [atlas-cloud](skills/animation-video/openmontage/atlas-cloud/SKILL.md) | Generate or edit images and videos through the Atlas Cloud gateway. Use for Atlas-hosted Seedance 2.5/2.0, Gemini Omni Flash, MiniMax H3, Seedream 5.0, GPT Image 2, Nano Banana 2,… |
| [avatar-video](skills/animation-video/openmontage/avatar-video/SKILL.md) | Create AI avatar videos with precise control over avatars, voices, scripts, scenes, and backgrounds using HeyGen's v2 API. Use when: (1) Choosing a specific avatar and voice for a… |
| [azure-speech-to-text](skills/animation-video/openmontage/azure-speech-to-text/SKILL.md) | Transcribe audio to text using Azure AI Speech (Fast Transcription REST API). Use when converting audio/video to text, generating subtitles, or processing spoken content in OpenMo… |
| [azure-text-to-speech](skills/animation-video/openmontage/azure-text-to-speech/SKILL.md) | Generate neural narration audio using Azure AI Speech (REST text-to-speech). Use when synthesizing voiceovers or narration in OpenMontage. Optional cloud TTS provider — preferred… |
| [beautiful-mermaid](skills/animation-video/openmontage/beautiful-mermaid/SKILL.md) | Render Mermaid diagrams as SVG and PNG using the Beautiful Mermaid library. Use when the user asks to render a Mermaid diagram. |
| [bfl-api](skills/animation-video/openmontage/bfl-api/SKILL.md) | BFL FLUX API integration guide covering endpoints, async polling patterns, rate limiting, error handling, webhooks, and regional endpoints with Python and TypeScript code examples. |
| [canvas-procedural-animation](skills/animation-video/openmontage/canvas-procedural-animation/SKILL.md) | Use p5.js/canvas for local procedural character effects: particles, weather, squash/stretch, walk cycles, and environmental motion. |
| [character-animation-qa](skills/animation-video/openmontage/character-animation-qa/SKILL.md) | Review local character animation with schema checks, Playwright browser previews, frame sampling, and FFmpeg/ffprobe final output checks. |
| [character-rigging](skills/animation-video/openmontage/character-rigging/SKILL.md) | Build data-driven 2D character rigs for local animation: parts, pivots, layers, constraints, views, and reusable rig packages. |
| [comfyui](skills/animation-video/openmontage/comfyui/SKILL.md) | Use when working with ComfyUI workflows in OpenMontage, including comfyui_image/comfyui_video/comfyui_music, custom workflow_json/workflow_path inputs, output_node selection, miss… |
| [create-video](skills/animation-video/openmontage/create-video/SKILL.md) | Create videos from a text prompt using HeyGen's Video Agent. Use when: (1) Creating a video from a description or idea, (2) Generating explainer, demo, or marketing videos from a… |
| [d3-viz](skills/animation-video/openmontage/d3-viz/SKILL.md) | Creating interactive data visualisations using d3.js. This skill should be used when creating custom charts, graphs, network diagrams, geographic visualisations, or any complex SV… |
| [dashscope](skills/animation-video/openmontage/dashscope/SKILL.md) | DashScope (Alibaba Cloud Bailian / 阿里云百炼) integration — image generation (qwen-image-2.0-pro), text-to-speech (qwen3-tts-flash), and ASR with word-level timestamps (qwen3-asr-flas… |
| [doubao-tts](skills/animation-video/openmontage/doubao-tts/SKILL.md) | Generate Mandarin and multilingual narration with Volcengine Doubao Speech 2.0. Use when creating Chinese voiceovers, when the user prefers Doubao/Volcengine/火山引擎/豆包 TTS, or when… |
| [elevenlabs](skills/animation-video/openmontage/elevenlabs/SKILL.md) | Generate AI voiceovers, sound effects, and music using ElevenLabs APIs. Use when creating audio content for videos, podcasts, or games. Triggers include generating voiceovers, nar… |
| [faceswap](skills/animation-video/openmontage/faceswap/SKILL.md) | Swap faces in a video using AI via the HeyGen API. Use when: (1) Replacing a face in a video with another face, (2) Face swapping from a source image onto a target video, (3) Crea… |
| [ffmpeg](skills/animation-video/openmontage/ffmpeg/SKILL.md) | Video and audio processing with FFmpeg. Use for format conversion, resizing, compression, audio extraction, and preparing assets for Remotion. Triggers include converting GIF to M… |
| [fish-audio-tts](skills/animation-video/openmontage/fish-audio-tts/SKILL.md) | Generate expressive, multilingual narration with fish.audio (S1 / S2-generation models) and reuse cloned voices via reference_id. Use when the user prefers fish.audio/Fish Audio T… |
| [flux-best-practices](skills/animation-video/openmontage/flux-best-practices/SKILL.md) | Comprehensive guide for BFL FLUX image generation models. Covers prompting, T2I, I2I, structured JSON, hex colors, typography, multi-reference editing, and model-specific best pra… |
| [framer-motion](skills/animation-video/openmontage/framer-motion/SKILL.md) | Use when implementing Disney's 12 animation principles with Framer Motion in React applications |
| [gemini-omni](skills/animation-video/openmontage/gemini-omni/SKILL.md) | Generate and conversationally edit short videos with stable Google Gemini Omni Flash (`gemini-omni-1.1-flash`). Use when: (1) iterating on a clip with natural-language edits inste… |
| [grok-media](skills/animation-video/openmontage/grok-media/SKILL.md) | xAI Grok image and video generation guide covering authentication, endpoints, prompt structure, image editing, reference-image video, and async polling. |
| [gsap-core](skills/animation-video/openmontage/gsap-core/SKILL.md) | Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, prefers-reduced-motion). Use when the user… |
| [gsap-frameworks](skills/animation-video/openmontage/gsap-frameworks/SKILL.md) | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user wants animation in Vue, Nuxt, Svelte, Sve… |
| [gsap-performance](skills/animation-video/openmontage/gsap-performance/SKILL.md) | Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching. Use when optimizing GSAP animations, reducing jank, or when the user asks a… |
| [gsap-plugins](skills/animation-video/openmontage/gsap-plugins/SKILL.md) | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG and physics plugins, CustomEa… |
| [gsap-react](skills/animation-video/openmontage/gsap-react/SKILL.md) | Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. Use when the user wants animation in React or Next.js, or asks about GSAP with React, useGSAP, or clea… |
| [gsap-scrolltrigger](skills/animation-video/openmontage/gsap-scrolltrigger/SKILL.md) | Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. Use when building or recommending scroll-based animation, parallax, pinned sections, or… |
| [gsap-timeline](skills/animation-video/openmontage/gsap-timeline/SKILL.md) | Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback. Use when sequencing animations, choreographing keyframes, or when the user asks about a… |
| [gsap-utils](skills/animation-video/openmontage/gsap-utils/SKILL.md) | Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe. Use when the user asks about gsap.utils, clamp, mapRange, random,… |
| [heygen](skills/animation-video/openmontage/heygen/SKILL.md) | [DEPRECATED] Use `create-video` for prompt-based video generation or `avatar-video` for precise avatar/scene control. This legacy skill combines both workflows — the newer focused… |
| [hyperframes](skills/animation-video/openmontage/hyperframes/SKILL.md) | READ THIS FIRST for any request to make, create, edit, animate, or render a video, animation, or motion graphic — a promo, explainer, captioned clip, title card, overlay, or any c… |
| [hyperframes-animation](skills/animation-video/openmontage/hyperframes-animation/SKILL.md) | All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven runtime adapters (G… |
| [hyperframes-cli](skills/animation-video/openmontage/hyperframes-cli/SKILL.md) | HyperFrames CLI dev loop. Use when running npx hyperframes init, add, catalog, capture, lint, validate, inspect, layout, snapshot, preview, play, render, publish, lambda, doctor,… |
| [hyperframes-core](skills/animation-video/openmontage/hyperframes-core/SKILL.md) | The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="clip"`, tracks, sub-compositions, varia… |
| [hyperframes-creative](skills/animation-video/openmontage/hyperframes-creative/SKILL.md) | Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narration, beat planning, audio-reactive visual… |
| [hyperframes-media](skills/animation-video/openmontage/hyperframes-media/SKILL.md) | Audio and media assets for HyperFrames compositions, produced by one shared audio engine (`scripts/audio.mjs`) — multi-provider TTS (HeyGen / ElevenLabs / Kokoro local), backgroun… |
| [hyperframes-registry](skills/animation-video/openmontage/hyperframes-registry/SKILL.md) | Install and wire registry blocks and components into HyperFrames compositions. Use when running hyperframes add, installing a block or component, wiring an installed item into ind… |
| [kling-official](skills/animation-video/openmontage/kling-official/SKILL.md) | Official Kling direct API guidance for OpenMontage providers. Use before calling `kling_official_video`, `kling_official_image`, `kling_tts`, `kling_avatar`, or `kling_lip_sync`. |
| [lottie-bodymovin](skills/animation-video/openmontage/lottie-bodymovin/SKILL.md) | Use when implementing Disney's 12 animation principles with Lottie animations exported from After Effects |
| [ltx2](skills/animation-video/openmontage/ltx2/SKILL.md) | AI video generation with LTX-2.3 22B — text-to-video, image-to-video clips for video production. Use when generating video clips, animating images, creating b-roll, animated backg… |
| [lyria](skills/animation-video/openmontage/lyria/SKILL.md) | Generate and validate music with Google Lyria through the Gemini Interactions API. Use before calling OpenMontage `google_music`, designing Lyria 3.5 or Clip prompts, using image-… |
| [manim-composer](skills/animation-video/openmontage/manim-composer/SKILL.md) | Trigger when: (1) User wants to create an educational/explainer video, (2) User has a vague concept they want visualized, (3) User mentions "3b1b style" or "explain like 3Blue1Bro… |
| [manimce-best-practices](skills/animation-video/openmontage/manimce-best-practices/SKILL.md) | Trigger when: (1) User mentions "manim" or "Manim Community" or "ManimCE", (2) Code contains `from manim import *`, (3) User runs `manim` CLI commands, (4) Working with Scene, Mat… |
| [manimgl-best-practices](skills/animation-video/openmontage/manimgl-best-practices/SKILL.md) | Trigger when: (1) User mentions "manimgl" or "ManimGL" or "3b1b manim", (2) Code contains `from manimlib import *`, (3) User runs `manimgl` CLI commands, (4) Working with Interact… |
| [media-use](skills/animation-video/openmontage/media-use/SKILL.md) | Agent Media OS — resolve any media need (BGM, SFX, image, icon) into a frozen local file + ledger record. One verb (`resolve`) handles the full cascade — project cache, global cac… |
| [minimax-h3](skills/animation-video/openmontage/minimax-h3/SKILL.md) | Generate MiniMax H3 (Hailuo 3.0) video through the official MiniMax v2 API, fal.ai, Runway, ComfyUI Partner Nodes, or local open weights in ComfyUI. Use for 4-15 second 2K clips,… |
| [motion-graphics](skills/animation-video/openmontage/motion-graphics/SKILL.md) | Use when the user wants a short, design-led motion graphic where motion is the message: kinetic typography, stat or number count-up, chart/data-viz hit, logo sting, brand lockup,… |
| [music](skills/animation-video/openmontage/music/SKILL.md) | Generate music using ElevenLabs Music API. Use when creating instrumental tracks, songs with lyrics, background music, jingles, or any AI-generated music composition. Supports pro… |
| [music-to-video](skills/animation-video/openmontage/music-to-video/SKILL.md) | Use when the user has a music track (an audio file, or a video to pull audio from) and wants a beat-synced HyperFrames video, calm to hard-hitting. The music drives everything: on… |
| [pika-h3-flex](skills/animation-video/openmontage/pika-h3-flex/SKILL.md) | Generate 3-15 second video with native synchronized audio using Pika H3 Flex through the Pika API (`pika_video`). Use for text-to-video, first/last-frame conditioning, and referen… |
| [playwright-recording](skills/animation-video/openmontage/playwright-recording/SKILL.md) | Record browser interactions as video using Playwright. Use for capturing demo videos, app walkthroughs, and UI flows for Remotion videos. Triggers include recording a demo, captur… |
| [pose-library-design](skills/animation-video/openmontage/pose-library-design/SKILL.md) | Design reusable 2D character pose libraries, action cycles, and expression states for data-driven animation. |
| [provider-model-refresh](skills/animation-video/openmontage/provider-model-refresh/SKILL.md) | Use the September 2026 image, video, speech and Avatar V adapters with explicit model/host contracts. |
| [provider-refresh-oct23](skills/animation-video/openmontage/provider-refresh-oct23/SKILL.md) | API contracts and production routing for the October 23, 2026 provider refresh. |
| [remotion](skills/animation-video/openmontage/remotion/SKILL.md) | Toolkit-specific Remotion patterns — custom transitions, shared components, and project conventions. For core Remotion framework knowledge (hooks, animations, rendering, etc.), se… |
| [remotion-best-practices](skills/animation-video/openmontage/remotion-best-practices/SKILL.md) | Best practices for Remotion - Video creation in React |
| [remotion-to-hyperframes](skills/animation-video/openmontage/remotion-to-hyperframes/SKILL.md) | Port an existing Remotion (React) composition to HyperFrames HTML. Use ONLY when the user explicitly asks to port/convert/migrate/translate a Remotion source. Do NOT use: (a) auth… |
| [seedance-2-0](skills/animation-video/openmontage/seedance-2-0/SKILL.md) | Generate cinematic clips with ByteDance Seedance 2.0 — the preferred premium video model in OpenMontage when a paid gateway is configured. Use when: (1) producing trailers, teaser… |
| [seedance-2-5](skills/animation-video/openmontage/seedance-2-5/SKILL.md) | Generate 4-30 second cinematic video with ByteDance Seedance 2.5 through fal.ai, Volcengine Ark, Runway, or ComfyUI Partner Nodes. Use for long single generations, synchronized au… |
| [setup-api-key](skills/animation-video/openmontage/setup-api-key/SKILL.md) | Guides users through setting up an ElevenLabs API key for ElevenLabs MCP tools. Use when the user needs to configure an ElevenLabs API key, when ElevenLabs tools fail due to missi… |
| [sound-effects](skills/animation-video/openmontage/sound-effects/SKILL.md) | Generate sound effects from text descriptions using ElevenLabs. Use when creating sound effects, generating audio textures, producing ambient sounds, cinematic impacts, UI sounds,… |
| [speech-to-text](skills/animation-video/openmontage/speech-to-text/SKILL.md) | Transcribe audio to text using ElevenLabs Scribe v2. Use when converting audio/video to text, generating subtitles, transcribing meetings, or processing spoken content. |
| [svg-character-animation](skills/animation-video/openmontage/svg-character-animation/SKILL.md) | Animate SVG character rigs with GSAP, CSS transforms, Remotion frame control, and HyperFrames-compatible browser previews. |
| [synthetic-screen-recording](skills/animation-video/openmontage/synthetic-screen-recording/SKILL.md) | Synthetic terminal-style screen recording guidance for Remotion `TerminalScene`. |
| [tailwind-design-system](skills/animation-video/openmontage/tailwind-design-system/SKILL.md) | Build scalable design systems with Tailwind CSS v4, design tokens, component libraries, and responsive patterns. Use when creating component libraries, implementing design systems… |
| [text-to-speech](skills/animation-video/openmontage/text-to-speech/SKILL.md) | HeyGen native Voice1 and catalog speech, voice discovery, timestamps, and streaming. |
| [threejs-animation](skills/animation-video/openmontage/threejs-animation/SKILL.md) | Three.js animation - keyframe animation, skeletal animation, morph targets, animation mixing. Use when animating objects, playing GLTF animations, creating procedural motion, or b… |
| [threejs-fundamentals](skills/animation-video/openmontage/threejs-fundamentals/SKILL.md) | Three.js scene setup, cameras, renderer, Object3D hierarchy, coordinate systems. Use when setting up 3D scenes, creating cameras, configuring renderers, managing object hierarchie… |
| [threejs-geometry](skills/animation-video/openmontage/threejs-geometry/SKILL.md) | Three.js geometry creation - built-in shapes, BufferGeometry, custom geometry, instancing. Use when creating 3D shapes, working with vertices, building custom meshes, or optimizin… |
| [threejs-interaction](skills/animation-video/openmontage/threejs-interaction/SKILL.md) | Three.js interaction - raycasting, controls, mouse/touch input, object selection. Use when handling user input, implementing click detection, adding camera controls, or creating i… |
| [threejs-lighting](skills/animation-video/openmontage/threejs-lighting/SKILL.md) | Three.js lighting - light types, shadows, environment lighting. Use when adding lights, configuring shadows, setting up IBL, or optimizing lighting performance. |
| [threejs-loaders](skills/animation-video/openmontage/threejs-loaders/SKILL.md) | Three.js asset loading - GLTF, textures, images, models, async patterns. Use when loading 3D models, textures, HDR environments, or managing loading progress. |
| [threejs-materials](skills/animation-video/openmontage/threejs-materials/SKILL.md) | Three.js materials - PBR, basic, phong, shader materials, material properties. Use when styling meshes, working with textures, creating custom shaders, or optimizing material perf… |
| [threejs-postprocessing](skills/animation-video/openmontage/threejs-postprocessing/SKILL.md) | Three.js post-processing - EffectComposer, bloom, DOF, screen effects. Use when adding visual effects, color grading, blur, glow, or creating custom screen-space shaders. |
| [threejs-shaders](skills/animation-video/openmontage/threejs-shaders/SKILL.md) | Three.js shaders - GLSL, ShaderMaterial, uniforms, custom effects. Use when creating custom visual effects, modifying vertices, writing fragment shaders, or extending built-in mat… |
| [threejs-textures](skills/animation-video/openmontage/threejs-textures/SKILL.md) | Three.js textures - texture types, UV mapping, environment maps, texture settings. Use when working with images, UV coordinates, cubemaps, HDR environments, or texture optimizatio… |
| [threejs-world-generation](skills/animation-video/openmontage/threejs-world-generation/SKILL.md) | Build deterministic, editable, free-viewpoint Three.js worlds from text or structured briefs. Use for cinematic 3D terrain, semantic regions, procedural biomes, explicit landmarks… |
| [vercel-composition-patterns](skills/animation-video/openmontage/vercel-composition-patterns/SKILL.md) | React composition patterns that scale. Use when refactoring components with boolean prop proliferation, building flexible component libraries, or designing reusable APIs. Triggers… |
| [vercel-react-best-practices](skills/animation-video/openmontage/vercel-react-best-practices/SKILL.md) | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optim… |
| [video-download](skills/animation-video/openmontage/video-download/SKILL.md) | Download video and audio from YouTube and 1000+ sites using yt-dlp. No API keys needed. Use when: (1) Downloading a video from YouTube or other sites, (2) Extracting audio from a… |
| [video-edit](skills/animation-video/openmontage/video-edit/SKILL.md) | Edit videos locally using ffmpeg. Trim, concat, resize, speed, overlay, extract audio, compress, and convert. Use when: (1) Trimming or cutting video segments, (2) Concatenating m… |
| [video-toolkit](skills/animation-video/openmontage/video-toolkit/SKILL.md) | Create professional videos autonomously using claude-code-video-toolkit — AI voiceovers, image generation, music, talking heads, and Remotion rendering. |
| [video-translate](skills/animation-video/openmontage/video-translate/SKILL.md) | Translate and dub existing videos into multiple languages using HeyGen. Use when: (1) Translating a video into another language, (2) Dubbing video content with lip-sync, (3) Creat… |
| [video-understand](skills/animation-video/openmontage/video-understand/SKILL.md) | Understand video content locally using ffmpeg frame extraction and Whisper transcription. No API keys needed. Use when: (1) Understanding what a video contains, (2) Transcribing v… |
| [visual-style](skills/animation-video/openmontage/visual-style/SKILL.md) | Create, extract, and apply portable visual design systems via visual-style.md files. Use when: (1) Creating a visual-style.md design system from scratch, (2) Extracting a visual s… |
| [web-design-guidelines](skills/animation-video/openmontage/web-design-guidelines/SKILL.md) | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practi… |
| [website-to-video](skills/animation-video/openmontage/website-to-video/SKILL.md) | Capture a general website/URL and turn it into a HyperFrames video (site tour, showcase, or social clip from the site's own visuals). Uses headless Chrome screenshots + brand asse… |

<a id="animation-video-remotion"></a>

### remotion（13 個）

Remotion 官方：用 React 做影片（建立、畫面與動畫、字幕、地圖、輸出、升級、授權）。資料夾：[`skills/animation-video/remotion`](skills/animation-video/remotion)

| SKILL | 原始說明 |
|---|---|
| [remotion-best-practices](skills/animation-video/remotion/remotion-best-practices/SKILL.md) | Router for all Remotion skills |
| [remotion-captions](skills/animation-video/remotion/remotion-captions/SKILL.md) | Transcribing, displaying and animating captions |
| [remotion-create](skills/animation-video/remotion/remotion-create/SKILL.md) | Create a new Remotion video |
| [remotion-docs](skills/animation-video/remotion/remotion-docs/SKILL.md) | Search Remotion documentation |
| [remotion-interactivity](skills/animation-video/remotion/remotion-interactivity/SKILL.md) | Structures Remotion markup so layers, timing and styles are editable in Remotion Studio. Use when writing a new composition or restructuring existing markup. |
| [remotion-license](skills/animation-video/remotion/remotion-license/SKILL.md) | Find Remotion license information, FAQs, terms, and where to buy a license. |
| [remotion-maps](skills/animation-video/remotion/remotion-maps/SKILL.md) | Remotion Map animation knowledge |
| [remotion-markup](skills/animation-video/remotion/remotion-markup/SKILL.md) | Content, animation and effects best practices |
| [remotion-multimedia](skills/animation-video/remotion/remotion-multimedia/SKILL.md) | Interacting with Mediabunny |
| [remotion-render](skills/animation-video/remotion/remotion-render/SKILL.md) | Export a Remotion video |
| [remotion-saas](skills/animation-video/remotion/remotion-saas/SKILL.md) | Build an app with Remotion |
| [remotion-studio](skills/animation-video/remotion/remotion-studio/SKILL.md) | Preview a Remotion video |
| [remotion-upgrade](skills/animation-video/remotion/remotion-upgrade/SKILL.md) | Upgrade Remotion, and related packages |

## 3D／遊戲 (`3d-gamedev`)

| 名稱 | 數量 | 用途 | 關鍵字 | 來源 | 存入日期 |
|---|---|---|---|---|---|
| [anatomy](skills/3d-gamedev/anatomy/SKILL.md) | 1 | 把任何點子做成可互動的 3D 物件 | 3D 物件, three.js | [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) `1482e84`（MIT） | 2026-11-13 |
| [gamedev-skills](#3d-gamedev-gamedev-skills) | 79 | 遊戲開發 SKILL 大全：Godot、Unity、Unreal、網頁引擎、遊戲類型、各職能、工作流 | godot, unity, unreal, three.js, 遊戲設計 | [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) `c6ca6c4`（Apache-2.0） | 2026-11-13 |
| [unity-mcp](#3d-gamedev-unity-mcp) | 2 | 讓 Claude 操作 Unity 編輯器；另含 Blender 轉 Unity 流程 | unity, mcp, blender | [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) `e2fd09c`（MIT） | 2026-11-13 |
| [universal-modder](#3d-gamedev-universal-modder) | 13 | 替自己擁有的 PC 遊戲做 mod：偵查、逆向、素材管線、發佈 | 遊戲 mod, 逆向工程 | [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder) `3c4ac6c`（MIT） | 2026-11-13 |

<a id="3d-gamedev-gamedev-skills"></a>

### gamedev-skills（79 個）

遊戲開發 SKILL 大全：Godot、Unity、Unreal、網頁引擎、遊戲類型、各職能、工作流。資料夾：[`skills/3d-gamedev/gamedev-skills`](skills/3d-gamedev/gamedev-skills)

| SKILL | 原始說明 |
|---|---|
| [disciplines/ai-behavior-trees-utility-ai](skills/3d-gamedev/gamedev-skills/disciplines/ai-behavior-trees-utility-ai/SKILL.md) | Engine-neutral behavior tree and utility AI code for NPCs in any language: Blackboard, reactive composites, decorators and response-curve scoring. Use when an enemy keeps chasing… |
| [disciplines/audio-design](skills/3d-gamedev/gamedev-skills/disciplines/audio-design/SKILL.md) | Engine-neutral game audio technique: bus layout, volume sliders in decibels, loudness, ducking music under dialogue, adaptive music and SFX variation, with Godot, Unity and FMOD/W… |
| [disciplines/camera-systems](skills/3d-gamedev/gamedev-skills/disciplines/camera-systems/SKILL.md) | Builds and tunes game cameras, engine-neutral with Godot and Cinemachine 3 mappings: 2D follow with deadzone and look-ahead, third-person orbit, first-person look and split-screen… |
| [disciplines/create-game-assets](skills/3d-gamedev/gamedev-skills/disciplines/create-game-assets/SKILL.md) | Plans, generates or sources, and validates consistent game art: style guides, sprites, pixel art, tilesets, icons and textures, with QA and licence records. Use when making or AI-… |
| [disciplines/dialogue-systems](skills/3d-gamedev/gamedev-skills/disciplines/dialogue-systems/SKILL.md) | Builds engine-neutral branching dialogue with Ink, Yarn Spinner or a small JSON graph runner: lines, choices, conditions, variables and localization IDs. Use for NPC conversations… |
| [disciplines/game-ai](skills/3d-gamedev/gamedev-skills/disciplines/game-ai/SKILL.md) | Designs engine-neutral enemy and NPC AI: picks FSM, behavior tree, utility or GOAP, and builds perception, steering and A* pathfinding. Use for patrol and chase, "find a path to t… |
| [disciplines/game-feel](skills/3d-gamedev/gamedev-skills/disciplines/game-feel/SKILL.md) | Adds engine-neutral juice to a working mechanic: trauma-based screen shake, hit-stop, eased tweens, squash and stretch, and knockback. Use when the game feels flat, weightless or… |
| [disciplines/game-ui-ux](skills/3d-gamedev/gamedev-skills/disciplines/game-ui-ux/SKILL.md) | Engine-neutral design rules for game HUDs and menus: anchors and containers, scaling, safe areas, gamepad focus, HUDs driven by events instead of polling, and accessibility minimu… |
| [disciplines/input-systems](skills/3d-gamedev/gamedev-skills/disciplines/input-systems/SKILL.md) | Engine-neutral input architecture with Godot InputMap code: named actions, stick deadzones, buffered presses and rebinding with conflict checks. Use for controller support or a re… |
| [disciplines/level-design](skills/3d-gamedev/gamedev-skills/disciplines/level-design/SKILL.md) | Engine-neutral level design with Godot checks: player metrics from the real controller, key and ability gating with a soft-lock check, and pacing. Use when laying out a level or m… |
| [disciplines/performance-optimization](skills/3d-gamedev/gamedev-skills/disciplines/performance-optimization/SKILL.md) | Finds and fixes game frame-rate problems by measurement in Godot, Unity, Unreal or Roblox: CPU- vs GPU-bound, then the biggest fix (draw calls, pooling, GC spikes). Use for low FP… |
| [disciplines/physics-tuning](skills/3d-gamedev/gamedev-skills/disciplines/physics-tuning/SKILL.md) | Engine-neutral physics tuning with Godot checks: fixed timestep and interpolation, CCD against tunnelling, damping, solver iterations and collision layer matrices. Use when bodies… |
| [disciplines/procedural-gen](skills/3d-gamedev/gamedev-skills/disciplines/procedural-gen/SKILL.md) | Engine-neutral procedural generation in Python with Godot and Unity mappings: seeded RNG, dungeon layouts, wave function collapse, noise terrain and loot tables. Use for a dungeon… |
| [disciplines/save-systems](skills/3d-gamedev/gamedev-skills/disciplines/save-systems/SKILL.md) | Engine-neutral save and load with Godot and Python code: what to serialize, slots and autosave, atomic writes and versioned migration. Use for save/load or a continue button, or s… |
| [disciplines/shader-programming](skills/3d-gamedev/gamedev-skills/disciplines/shader-programming/SKILL.md) | Engine-neutral shader technique in GLSL with HLSL equivalents: how dissolve, outline, fresnel rim and post effects work, and porting GLSL to HLSL. Use when the math of an effect i… |
| [ebitengine/ebitengine-game](skills/3d-gamedev/gamedev-skills/ebitengine/ebitengine-game/SKILL.md) | Creates, debugs and packages 2D games in Go with Ebitengine v2: a play-and-retry loop, input, pixel-art scaling, text, audio and desktop, WASM or mobile builds. Use when go.mod re… |
| [genres/card-game](skills/3d-gamedev/gamedev-skills/genres/card-game/SKILL.md) | Designs card games and deckbuilders in any engine: cards as data with one effect interpreter, deck zones, a trigger stack and seeded shuffles. Use for a Slay the Spire- or Balatro… |
| [genres/fps-shooter](skills/3d-gamedev/gamedev-skills/genres/fps-shooter/SKILL.md) | Designs first-person shooter combat in any engine: hitscan vs projectiles, time-to-kill, damage falloff, recoil patterns, ADS sensitivity and lag-compensated hits. Use for a Doom-… |
| [genres/platformer](skills/3d-gamedev/gamedev-skills/genres/platformer/SKILL.md) | Designs 2D platformers in any engine: jump feel (coyote time, jump buffering, variable height, fall gravity, corner correction), wall jumps, hazards, checkpoints and one-way platf… |
| [genres/puzzle](skills/3d-gamedev/gamedev-skills/genres/puzzle/SKILL.md) | Designs grid and logic puzzle games in any engine: match-3 cascades, Sokoban pushing, unique-solution grids (nonogram, Sudoku), exact undo and solver-checked levels. Use for a Can… |
| [genres/roguelike](skills/3d-gamedev/gamedev-skills/genres/roguelike/SKILL.md) | Designs run-based roguelikes and roguelites in any engine: run structure, permadeath, meta-progression, seeded and daily runs, turn order and symmetric field of view. Use for NetH… |
| [genres/rpg](skills/3d-gamedev/gamedev-skills/genres/rpg/SKILL.md) | Designs RPG progression and combat numbers in any engine: stats with a modifier stack, XP curves, damage formulas, items and equipment (slots, rarity, affixes) and quests. Use for… |
| [genres/survival-crafting](skills/3d-gamedev/gamedev-skills/genres/survival-crafting/SKILL.md) | Designs survival-crafting loops in any engine: gathering, recipes and tech trees, carry weight, spoilage, hunger and temperature, and base building. Use for a Minecraft-, Valheim-… |
| [genres/tower-defense](skills/3d-gamedev/gamedev-skills/genres/tower-defense/SKILL.md) | Designs tower defense games in any engine: lane and maze pathing, wave pacing, targeting priorities, armoured and flying counters, and the gold economy, with a wave-curve checker.… |
| [genres/visual-novel](skills/3d-gamedev/gamedev-skills/genres/visual-novel/SKILL.md) | Builds visual novels and choice-driven stories in Ren'Py or any engine: routes and endings, save-anywhere, backlog, skip-read-only and typewriter text. Use for a VN or dating sim,… |
| [godot/godot-2d-movement](skills/3d-gamedev/gamedev-skills/godot/godot-2d-movement/SKILL.md) | Godot 4.7 CharacterBody2D movement in GDScript: platformer run and jump, top-down 8-direction motion, slopes and one-way platforms, with a headless landing test. Use when a 2D con… |
| [godot/godot-3d-essentials](skills/3d-gamedev/gamedev-skills/godot/godot-3d-essentials/SKILL.md) | Godot 4.7 3D scene setup: Camera3D, lights, WorldEnvironment (sky, ambient, tonemap, fog), StandardMaterial3D, GridMap and local vs global transforms, with a headless scene check.… |
| [godot/godot-animation](skills/3d-gamedev/gamedev-skills/godot/godot-animation/SKILL.md) | Godot 4.7 animation APIs: AnimationPlayer, AnimationTree state machines, AnimatedSprite2D and create_tween() Tweens, with a headless state test. Use when travel() does nothing, an… |
| [godot/godot-audio](skills/3d-gamedev/gamedev-skills/godot/godot-audio/SKILL.md) | Godot 4.7 audio APIs: AudioStreamPlayer 2D and 3D, the bus layout, AudioServer volume and mute, polyphony, looping imports and playback position for beat sync. Use when wiring SFX… |
| [godot/godot-csharp](skills/3d-gamedev/gamedev-skills/godot/godot-csharp/SKILL.md) | C# and .NET in Godot 4.7: partial node classes, the PascalCase lifecycle, [Export] and [Signal], signals as C# events, the .csproj and calling GDScript. Use for .cs scripts in God… |
| [godot/godot-export](skills/3d-gamedev/gamedev-skills/godot/godot-export/SKILL.md) | Exports Godot 4.7 projects: templates, export_presets.cfg for desktop, Web and Android, command-line exports and web COOP/COEP headers. Use on "No export template found", a blank… |
| [godot/godot-gdscript](skills/3d-gamedev/gamedev-skills/godot/godot-gdscript/SKILL.md) | GDScript 2.0 for Godot 4.7: static typing, @export and @onready, await and coroutines, and porting 3.x code. Use for .gd parse errors ("Cannot infer the type"), a coroutine that n… |
| [godot/godot-gdscript-headless-testing](skills/3d-gamedev/gamedev-skills/godot/godot-gdscript-headless-testing/SKILL.md) | Runs Godot 4.7 GDScript tests with godot --headless and a SceneTree runner that exits non-zero on failure, so CI can gate merges. Owns Godot tests in CI. Use for GitHub Actions jo… |
| [godot/godot-multiplayer](skills/3d-gamedev/gamedev-skills/godot/godot-multiplayer/SKILL.md) | Godot 4.7 high-level multiplayer: ENet host and join, @rpc with rpc_id(), MultiplayerSpawner and MultiplayerSynchronizer, with a two-instance headless test. Use for online or LAN… |
| [godot/godot-nodes-scenes](skills/3d-gamedev/gamedev-skills/godot/godot-nodes-scenes/SKILL.md) | Godot 4.7 scene-tree structure: reusable .tscn scenes, instantiate(), autoloads and a checker for broken res:// paths and uids. Use when spawning bullets or enemies, or on "Node n… |
| [godot/godot-physics](skills/3d-gamedev/gamedev-skills/godot/godot-physics/SKILL.md) | Godot 4.7 physics API in 2D and 3D: body and Area types, collision_layer and mask bits, Area signals for hurtboxes, RayCast and space queries, and Jolt (3D default since 4.6). Use… |
| [godot/godot-resources](skills/3d-gamedev/gamedev-skills/godot/godot-resources/SKILL.md) | Godot 4.7 data-driven design with custom Resources: class_name and @export fields, .tres files, shared references vs duplicate_deep(), uids and threaded loading. Use for items, st… |
| [godot/godot-shaders](skills/3d-gamedev/gamedev-skills/godot/godot-shaders/SKILL.md) | Godot 4.7 Shading Language syntax and pipeline: canvas_item, spatial and particle shaders, built-ins, ShaderMaterial wiring, a headless compile check and 3.x porting. Use for a .g… |
| [godot/godot-signals-groups](skills/3d-gamedev/gamedev-skills/godot/godot-signals-groups/SKILL.md) | Godot 4.7 signals and node groups: typed signals, connect() with Callables, one-shot and deferred connections, event-bus autoloads and call_group broadcasts. Use when nodes must t… |
| [godot/godot-tilemap](skills/3d-gamedev/gamedev-skills/godot/godot-tilemap/SKILL.md) | Godot 4.7 tile maps with TileMapLayer and TileSet: atlas sources, data layers, terrain autotiling and set_cell or local_to_map at runtime. Use for 2D tile levels in Godot, tiles w… |
| [godot/godot-ui-control](skills/3d-gamedev/gamedev-skills/godot/godot-ui-control/SKILL.md) | Godot 4.7 Control-node API for menus and HUDs: anchors, Containers, Theme and StyleBox, focus neighbours and stretch settings, with a headless layout check. Use when Godot UI over… |
| [other-engines/bevy-ecs](skills/3d-gamedev/gamedev-skills/other-engines/bevy-ecs/SKILL.md) | Builds and debugs Bevy 0.20 games in Rust: components, Query and Commands systems, schedules, States, observers and headless tests. Use when Cargo.toml depends on bevy, on a B0001… |
| [other-engines/defold-core](skills/3d-gamedev/gamedev-skills/other-engines/defold-core/SKILL.md) | Builds and debugs Defold 1.14 games in Lua: collections, game objects, input focus, msg.post messaging, factories, collection proxies and Bob builds. Use for .collection or .scrip… |
| [other-engines/love2d-core](skills/3d-gamedev/gamedev-skills/other-engines/love2d-core/SKILL.md) | Builds and debugs LÖVE (Love2D) 11.x games in Lua: main.lua callbacks, conf.lua, fixed steps, crisp pixel-art scaling, love.filesystem saves and a scripted run. Use when main.lua… |
| [other-engines/pygame-core](skills/3d-gamedev/gamedev-skills/other-engines/pygame-core/SKILL.md) | Builds and debugs 2D games in Python with pygame-ce (imported as pygame): the event-update-draw loop, delta time, Surfaces and Rects, Sprite groups and headless tests. Use when co… |
| [other-engines/roblox-characters](skills/3d-gamedev/gamedev-skills/other-engines/roblox-characters/SKILL.md) | Roblox player characters: CharacterAdded lifecycle, Humanoid and HumanoidRootPart, R6, R15 and custom rigs, respawn and Tools. Use when a character script breaks after respawn, an… |
| [other-engines/roblox-datastores](skills/3d-gamedev/gamedev-skills/other-engines/roblox-datastores/SKILL.md) | Roblox DataStoreService persistence: load on join, save on leave and BindToClose, UpdateAsync vs SetAsync, session locking and OrderedDataStore leaderboards. Use for lost player d… |
| [other-engines/roblox-luau](skills/3d-gamedev/gamedev-skills/other-engines/roblox-luau/SKILL.md) | Roblox Luau scripting and code structure: services, Instances, Script vs LocalScript vs ModuleScript, the task library and typed Luau, with selene and luau-lsp checks. Use when a… |
| [other-engines/roblox-networking](skills/3d-gamedev/gamedev-skills/other-engines/roblox-networking/SKILL.md) | Roblox client-server networking and anti-exploit: RemoteEvent and RemoteFunction contracts, server authority, rate limits, hit validation and replication. Use when a remote trusts… |
| [other-engines/roblox-physics](skills/3d-gamedev/gamedev-skills/other-engines/roblox-physics/SKILL.md) | Roblox physics and spatial queries: assemblies, constraints, collision groups, Raycast and Shapecast, and network ownership. Use when parts fall through or jitter, Touched is unre… |
| [other-engines/roblox-simulator-economy](skills/3d-gamedev/gamedev-skills/other-engines/roblox-simulator-economy/SKILL.md) | Roblox simulator, tycoon and idle-game economies in Luau: upgrade cost curves, income per second, rebirth pacing, big-number formatting and paid-egg odds, with a Lune calculator.… |
| [other-engines/roblox-studio-workflow](skills/3d-gamedev/gamedev-skills/other-engines/roblox-studio-workflow/SKILL.md) | Safely edits an existing Roblox place or Rojo project: finds the source of truth and proves changes with the right test mode or Studio MCP (execute_luau). Use when an agent edits… |
| [other-engines/roblox-ui](skills/3d-gamedev/gamedev-skills/other-engines/roblox-ui/SKILL.md) | Roblox UI with ScreenGui and PlayerGui: ResetOnSpawn, UDim2 scale and offset, UIListLayout flex, safe areas, StyleSheet, gamepad selection and touch controls. Use for Roblox HUDs,… |
| [unity/unity-animation](skills/3d-gamedev/gamedev-skills/unity/unity-animation/SKILL.md) | Unity 6.3 LTS character animation with the Animator (Mecanim): states and transitions, blend trees, Avatar Mask layers, root motion and humanoid IK. Use for SetTrigger wiring, a t… |
| [unity/unity-build-pipeline](skills/3d-gamedev/gamedev-skills/unity/unity-build-pipeline/SKILL.md) | Builds and ships Unity 6.3 LTS players: Build Profiles, IL2CPP vs Mono, managed stripping with link.xml, scripted BuildPlayer, Addressables and CI or headless builds. Use when aut… |
| [unity/unity-build-size](skills/3d-gamedev/gamedev-skills/unity/unity-build-size/SKILL.md) | Finds and shrinks what makes a Unity 6.3 LTS build too big: Build Report reading, uncompressed textures, glTFast models, PCM audio and per-platform levers. Use when an APK, AAB, W… |
| [unity/unity-csharp-scripting](skills/3d-gamedev/gamedev-skills/unity/unity-csharp-scripting/SKILL.md) | Writes and fixes Unity 6.3 LTS C# gameplay scripts: MonoBehaviour lifecycle, serialization, .meta/GUID discipline and command-line tests. Use for new or renamed .cs files, "Missin… |
| [unity/unity-input-system](skills/3d-gamedev/gamedev-skills/unity/unity-input-system/SKILL.md) | Wires Unity 6.3 LTS player input with the Input System package: .inputactions assets, action maps, PlayerInput and control schemes. Use when input does nothing or fires under a me… |
| [unity/unity-navmesh](skills/3d-gamedev/gamedev-skills/unity/unity-navmesh/SKILL.md) | Unity 6.3 LTS pathfinding with the AI Navigation package: NavMeshSurface baking, NavMeshAgent, NavMeshLink jumps and runtime rebakes. Use when a Unity enemy should chase or patrol… |
| [unity/unity-physics](skills/3d-gamedev/gamedev-skills/unity/unity-physics/SKILL.md) | Unity 6.3 LTS physics in 3D and 2D: Rigidbody and Rigidbody2D, forces and linearVelocity, the layer collision matrix and raycasts. Use when an object falls through the floor, OnTr… |
| [unity/unity-scriptableobjects](skills/3d-gamedev/gamedev-skills/unity/unity-scriptableobjects/SKILL.md) | Unity 6.3 LTS data and decoupling with ScriptableObjects: CreateAssetMenu config assets, shared runtime variables, event channels and .asset files made from code. Use for replacin… |
| [unity/unity-tilemap-2d](skills/3d-gamedev/gamedev-skills/unity/unity-tilemap-2d/SKILL.md) | Unity 6.3 LTS 2D tilemaps: the Tile Palette, Tilemap Collider 2D with a Composite Collider, Rule Tiles and runtime SetTile. Use for painting or generating a tile level, seams betw… |
| [unreal/unreal-behavior-trees](skills/3d-gamedev/gamedev-skills/unreal/unreal-behavior-trees/SKILL.md) | Unreal Engine 5 (UE 5.8) NPC AI with Behavior Trees, Blackboards, EQS and StateTree: decorators with Observer Aborts, C++ BTTask nodes and running trees from an AIController. Use… |
| [unreal/unreal-blueprints](skills/3d-gamedev/gamedev-skills/unreal/unreal-blueprints/SKILL.md) | Unreal Engine 5 (UE 5.8) Blueprint visual scripting: Blueprint Classes vs the Level Blueprint, Event Graph, and Cast, Interfaces and Event Dispatchers. Use for BP graphs, how one… |
| [unreal/unreal-cpp-gameplay](skills/3d-gamedev/gamedev-skills/unreal/unreal-cpp-gameplay/SKILL.md) | Unreal Engine 5 (UE 5.8) C++ gameplay code: UCLASS and UPROPERTY reflection, the Gameplay Framework, GC-safe pointers, Build.cs and command-line builds. Use for GENERATED_BODY, Li… |
| [unreal/unreal-enhanced-input](skills/3d-gamedev/gamedev-skills/unreal/unreal-enhanced-input/SKILL.md) | Unreal Engine 5 (UE 5.8) player input with Enhanced Input: Input Actions (IA_), Mapping Contexts (IMC_), ETriggerEvent bindings and remappable keys. Use when wiring move, look or… |
| [unreal/unreal-niagara](skills/3d-gamedev/gamedev-skills/unreal/unreal-niagara/SKILL.md) | Unreal Engine 5 (UE 5.8) Niagara VFX: systems, emitters, User parameters, spawning from C++ or Blueprints, bounds and GPU vs CPU sim. Use for any Unreal particle effect, NS_ asset… |
| [unreal/unreal-packaging](skills/3d-gamedev/gamedev-skills/unreal/unreal-packaging/SKILL.md) | Packages and ships Unreal Engine 5 (UE 5.8) projects: Shipping builds, cooking, pak/IoStore and RunUAT BuildCookRun with UAT and cook log reading. Use for a packaged game with a b… |
| [web-engines/phaser-arcade-physics](skills/3d-gamedev/gamedev-skills/web-engines/phaser-arcade-physics/SKILL.md) | Phaser 4 Arcade Physics movement and collision: bodies, velocity, gravity, colliders vs overlaps, groups and bullet pools. Use for a Phaser platformer or top-down controller, or a… |
| [web-engines/phaser-core](skills/3d-gamedev/gamedev-skills/web-engines/phaser-core/SKILL.md) | Sets up and debugs Phaser 4 games (and pinned Phaser 3.90): Game config, Scene lifecycle, the loader, scene transitions and Phaser 3 to 4 migration. Use when code imports phaser,… |
| [web-engines/pixijs-rendering](skills/3d-gamedev/gamedev-skills/web-engines/pixijs-rendering/SKILL.md) | Builds and debugs 2D browser game rendering with PixiJS v8: async init, Assets loading, the Container and Sprite scene graph, pointer dragging and v7-to-v8 migration. Use when a g… |
| [web-engines/threejs-gltf-loading](skills/3d-gamedev/gamedev-skills/web-engines/threejs-gltf-loading/SKILL.md) | Loads glTF/GLB models into three.js r187 and plays their animations: GLTFLoader, DRACO, Meshopt and KTX2 decoders, AnimationMixer cross-fades and SkeletonUtils clones. Use when a… |
| [web-engines/threejs-materials-lighting](skills/3d-gamedev/gamedev-skills/web-engines/threejs-materials-lighting/SKILL.md) | Lights and shades three.js r187 scenes: standard, physical and unlit materials, lights, shadows, HDR environment lighting and tone mapping. Use when a mesh renders black or washed… |
| [web-engines/threejs-scene-setup](skills/3d-gamedev/gamedev-skills/web-engines/threejs-scene-setup/SKILL.md) | Sets up and debugs a plain three.js r187 game or 3D scene: import maps, Scene, PerspectiveCamera and WebGLRenderer, setAnimationLoop with Timer, resize, OrbitControls and WebGPURe… |
| [workflows/game-docs](skills/3d-gamedev/gamedev-skills/workflows/game-docs/SKILL.md) | Writes and maintains a game's design docs: a one-page GDD with a feature index and short feature notes, kept true to the code by a link and status checker. Use for "draft a GDD",… |
| [workflows/game-jam](skills/3d-gamedev/gamedev-skills/workflows/game-jam/SKILL.md) | Plans and ships a game jam entry against a fixed deadline: reads the jam rules, scopes to the clock, keeps a cut list and checks the build before submitting. Use for Ludum Dare, G… |
| [workflows/itch-publish](skills/3d-gamedev/gamedev-skills/workflows/itch-publish/SKILL.md) | Publishes and updates games on itch.io with the butler CLI: butler push to user/game:channel, channel platform tags, HTML5 builds, --userversion and CI uploads. Use for "upload to… |
| [workflows/prototype-fast](skills/3d-gamedev/gamedev-skills/workflows/prototype-fast/SKILL.md) | Builds a throwaway playable prototype in about an hour to answer one question, usually "is this mechanic fun?": a one-question brief, a greybox, a debug HUD, a playtest and a keep… |
| [workflows/steam-publish](skills/3d-gamedev/gamedev-skills/workflows/steam-publish/SKILL.md) | Publishes or updates a game on Steam with Steamworks and SteamPipe: depots, app_build .vdf scripts, steamcmd uploads, beta branches, SetLive, store review and Coming Soon. Use for… |

<a id="3d-gamedev-unity-mcp"></a>

### unity-mcp（2 個）

讓 Claude 操作 Unity 編輯器；另含 Blender 轉 Unity 流程。資料夾：[`skills/3d-gamedev/unity-mcp`](skills/3d-gamedev/unity-mcp)

| SKILL | 原始說明 |
|---|---|
| [blender-to-unity](skills/3d-gamedev/unity-mcp/blender-to-unity/SKILL.md) | Hand off a model from Blender (via BlenderMCP) into Unity (via MCP for Unity) — export the current Blender model, import it through import_model_file, and place it in the open sce… |
| [unity-mcp-orchestrator](skills/3d-gamedev/unity-mcp/unity-mcp-skill/SKILL.md) | Orchestrate Unity Editor via MCP (Model Context Protocol) tools and resources. Use when working with Unity projects through MCP for Unity - creating/modifying GameObjects, editing… |

<a id="3d-gamedev-universal-modder"></a>

### universal-modder（13 個）

替自己擁有的 PC 遊戲做 mod：偵查、逆向、素材管線、發佈。資料夾：[`skills/3d-gamedev/universal-modder`](skills/3d-gamedev/universal-modder)

| SKILL | 原始說明 |
|---|---|
| [asset-pipeline](skills/3d-gamedev/universal-modder/asset-pipeline/SKILL.md) | Turn generated or hand-made art into exactly what a game engine loads. Covers sprite cutout, trim and nearest-neighbour fitting to frame sizes, pixelation to a palette, sprite she… |
| [blitz3d-decomp](skills/3d-gamedev/universal-modder/blitz3d-decomp/SKILL.md) | Decompile a Blitz3D game to readable Blitz source with B3DDecomp and port what it does to another engine. Covers SCP - Containment Breach-era and other .bb games, B3DDecomp, Blitz… |
| [fal-assets](skills/3d-gamedev/universal-modder/fal-assets/SKILL.md) | Generate game assets with fal (fal.ai) through the fal MCP server, the `um fal` CLI (REST) or `fal api`. Covers sprites and icons with transparent backgrounds, consistent variants… |
| [game-automation](skills/3d-gamedev/universal-modder/game-automation/SKILL.md) | Launch, see and drive a real game so an agent can test its own mods. Covers launching via Steam or the exe, windowed mode at a fixed size, screenshots of the game window (GPU-safe… |
| [game-recon](skills/3d-gamedev/universal-modder/game-recon/SKILL.md) | Figure out how a specific installed game can be modded, before writing any mod code. Covers where it's installed, the engine and version, managed vs native code, anti-cheat, loade… |
| [game-research-websearch](skills/3d-gamedev/universal-modder/game-research-websearch/SKILL.md) | Research a game, engine or modding technique on the open web with archive-aware, rate-limit-safe searches — Wayback Machine/archive.today for dead forums (XeNTaX, Zenhax, old thre… |
| [mashup-mods](skills/3d-gamedev/universal-modder/mashup-mods/SKILL.md) | Build cross-game mashups and total conversions, the "Minecraft inside Elden Ring" or "skateboarding in MW2" kind. Covers passthrough mods (two games running at once and exchanging… |
| [mod-any-game](skills/3d-gamedev/universal-modder/mod-any-game/SKILL.md) | Mod a PC game the user owns, taking an idea to working in the real game and recorded. It covers new items, weapons, enemies, bosses, units, civilizations, mechanics, art, sound, V… |
| [port-a-mod](skills/3d-gamedev/universal-modder/port-a-mod/SKILL.md) | Port an existing mod to a newer game version or another mod loader while keeping its behaviour, values and quirks. Typical cases are an old Forge 1.7.10 or 1.12 Minecraft mod movi… |
| [publish-mod](skills/3d-gamedev/universal-modder/publish-mod/SKILL.md) | Package and release a finished game mod. Covers the pre-release lint (no game files, decompiled code or leaked keys), README and install steps, credits and AI disclosure, versioni… |
| [reverse-engineering](skills/3d-gamedev/universal-modder/reverse-engineering/SKILL.md) | Read how a game actually works so a mod can hook it. Decompile .NET/Mono (ILSpy), IL2CPP (Cpp2IL, Il2CppDumper), Java (Vineflower) and native code (Ghidra, IDA, via MCP servers);… |
| [share-field-notes](skills/3d-gamedev/universal-modder/share-field-notes/SKILL.md) | Search and contribute to the shared AI-modding knowledge base, where field notes record how specific games were modded, decompiled or reverse-engineered (exact versions, route, en… |
| [showcase-video](skills/3d-gamedev/universal-modder/showcase-video/SKILL.md) | Record and cut a short showcase video of a game mod, or a compilation of clips, ready to post on X/YouTube. Records the game window with only the game's own audio, picks moments f… |

## 寫作／溝通 (`writing-communication`)

| 名稱 | 數量 | 用途 | 關鍵字 | 來源 | 存入日期 |
|---|---|---|---|---|---|
| [anthropics](#writing-communication-anthropics) | 2 | Anthropic 官方：文件共筆流程、內部溝通文稿 | 共筆, 公告, 週報 | [anthropics/skills](https://github.com/anthropics/skills) `2c5958e`（Apache-2.0） | 2026-11-13 |

<a id="writing-communication-anthropics"></a>

### anthropics（2 個）

Anthropic 官方：文件共筆流程、內部溝通文稿。資料夾：[`skills/writing-communication/anthropics`](skills/writing-communication/anthropics)

| SKILL | 原始說明 |
|---|---|
| [doc-coauthoring](skills/writing-communication/anthropics/doc-coauthoring/SKILL.md) | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs, or similar structu… |
| [internal-comms](skills/writing-communication/anthropics/internal-comms/SKILL.md) | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some… |

## 效率／工作流 (`productivity-workflow`)

| 名稱 | 數量 | 用途 | 關鍵字 | 來源 | 存入日期 |
|---|---|---|---|---|---|
| [anthropics](#productivity-workflow-anthropics) | 4 | Anthropic 官方：Word、PDF、PowerPoint、Excel 檔案處理 | docx, pdf, pptx, xlsx | [anthropics/skills](https://github.com/anthropics/skills) `2c5958e`（Apache-2.0） | 2026-11-13 |

<a id="productivity-workflow-anthropics"></a>

### anthropics（4 個）

Anthropic 官方：Word、PDF、PowerPoint、Excel 檔案處理。資料夾：[`skills/productivity-workflow/anthropics`](skills/productivity-workflow/anthropics)

| SKILL | 原始說明 |
|---|---|
| [docx](skills/productivity-workflow/anthropics/docx/SKILL.md) | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files). Triggers include: any mention of 'Word do… |
| [pdf](skills/productivity-workflow/anthropics/pdf/SKILL.md) | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, split… |
| [pptx](skills/productivity-workflow/anthropics/pptx/SKILL.md) | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, pars… |
| [xlsx](skills/productivity-workflow/anthropics/xlsx/SKILL.md) | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .xltx, .… |

## 思考／學習 (`thinking-learning`)

| 名稱 | 數量 | 用途 | 關鍵字 | 來源 | 存入日期 |
|---|---|---|---|---|---|
| [anthropics](#thinking-learning-anthropics) | 2 | Anthropic 官方：academy-guide、discernment-nudge | 學習, 判斷 | [anthropics/skills](https://github.com/anthropics/skills) `2c5958e`（Apache-2.0） | 2026-11-13 |

<a id="thinking-learning-anthropics"></a>

### anthropics（2 個）

Anthropic 官方：academy-guide、discernment-nudge。資料夾：[`skills/thinking-learning/anthropics`](skills/thinking-learning/anthropics)

| SKILL | 原始說明 |
|---|---|
| [academy-guide](skills/thinking-learning/anthropics/academy-guide/SKILL.md) | Stop and check this skill before finishing any reply to a question about how to use Claude or a Claude product — it recommends matching courses, tutorials, and use cases from Clau… |
| [discernment-nudge](skills/thinking-learning/anthropics/discernment-nudge/SKILL.md) | After you give a substantive answer or draft that the user may act on — advice or recommendations, drafted artifacts such as goals, plans, pitches, proposals, or emails, estimates… |

## 參考資源（不是 SKILL）

以下是軟體、函式庫或 MCP 伺服器本身，repo 裡沒有可存的 SKILL，只記錄連結備查。

| 資源 | 是什麼 | 備註 | 記錄日期 |
|---|---|---|---|
| [godotengine/godot](https://github.com/godotengine/godot) | 開源 2D／3D 遊戲引擎 | 相關 SKILL 見 `3d-gamedev/gamedev-skills/godot` | 2026-11-13 |
| [opentoonz/opentoonz](https://github.com/opentoonz/opentoonz) | 開源 2D 動畫製作軟體 |  | 2026-11-13 |
| [juliangarnier/anime](https://github.com/juliangarnier/anime) | Anime.js，JavaScript 動畫函式庫 |  | 2026-11-13 |
| [motiondivision/motion](https://github.com/motiondivision/motion) | Motion 動畫函式庫本體，[450+ 官方範例](https://motion.dev/examples) | 對應的 SKILL 已存為 `motion` | 2026-11-13 |
| [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | Blender MCP：讓 Claude 操作 Blender 的 MCP 伺服器與外掛 | 是 MCP 伺服器，repo 內沒有 SKILL | 2026-11-13 |
