/**
 * generate-review-docx.js
 * 
 * 審稿報告 Word 文件生成模板。
 * Claude 在執行審稿時參考此檔案的結構與 docx-js 用法，
 * 動態填入審稿內容後產生 .docx 文件。
 * 
 * 使用前確認：npm install -g docx
 * 驗證：python /mnt/skills/public/docx/scripts/office/validate.py output.docx
 * 
 * ===== 使用方式 =====
 * 此檔案為「模板參考」，Claude 在審稿時應：
 * 1. 讀取此檔案了解排版結構
 * 2. 將 REVIEW_DATA 區塊替換為實際審稿內容
 * 3. 執行 node 生成 .docx
 * 4. validate → present_files
 */

const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  HeadingLevel, AlignmentType, BorderStyle, WidthType, ShadingType,
  LevelFormat, PageBreak, Header, Footer, PageNumber
} = require("docx");

// ===== REVIEW_DATA（Claude 填入實際審稿內容）=====
const REVIEW_DATA = {
  // 論文基本資訊
  paperTitle: "[論文標題]",
  authors: "[作者列表]",
  journal: "[目標期刊]",
  reviewDate: new Date().toISOString().split("T")[0],

  // Summary
  summary: "[3-5 句話總評]",

  // Scores
  scores: {
    novelty:      { score: 0, weight: 0.30, rationale: "[一句話理由]" },
    methodology:  { score: 0, weight: 0.30, rationale: "[一句話理由]" },
    significance: { score: 0, weight: 0.25, rationale: "[一句話理由]" },
    clarity:      { score: 0, weight: 0.15, rationale: "[一句話理由]" },
  },

  // Strengths
  strengths: [
    { id: "S1", title: "[亮點標題]", detail: "[具體說明]" },
    { id: "S2", title: "[亮點標題]", detail: "[具體說明]" },
    { id: "S3", title: "[亮點標題]", detail: "[具體說明]" },
  ],

  // Major Issues
  majorIssues: [
    { id: "M1", title: "[問題標題]", location: "[Section/Table/Figure/Page]", problem: "[具體描述]", suggestion: "[改進方向]" },
  ],

  // Minor Issues
  minorIssues: [
    { id: "m1", title: "[問題標題]", location: "[位置]", problem: "[描述]", suggestion: "[建議]" },
  ],

  // Recommendation: "Accept" | "Minor Revision" | "Major Revision" | "Reject"
  recommendation: "Major Revision",
  recommendationRationale: "[判定理由]",
  overrideNote: null, // 若與決策矩陣不一致，填入 override 說明
};

// ===== 色彩常數 =====
const COLORS = {
  primary: "1B4F72",
  accent: "2E86C1",
  dark: "2C3E50",
  gray: "7F8C8D",
  white: "FFFFFF",
  // Score colors
  scoreGreen: "27AE60",
  scoreYellow: "F39C12",
  scoreRed: "E74C3C",
  bgGreen: "D5F5E3",
  bgYellow: "FEF9E7",
  bgRed: "FADBD8",
  bgBlue: "D6EAF8",
  bgGray: "F2F3F4",
  // Recommendation colors
  recAccept: "27AE60",
  recMinor: "2E86C1",
  recMajor: "E67E22",
  recReject: "E74C3C",
};

function getScoreColor(score) {
  if (score >= 4) return COLORS.scoreGreen;
  if (score >= 3) return COLORS.scoreYellow;
  return COLORS.scoreRed;
}

function getScoreBg(score) {
  if (score >= 4) return COLORS.bgGreen;
  if (score >= 3) return COLORS.bgYellow;
  return COLORS.bgRed;
}

function getRecColor(rec) {
  const map = { "Accept": COLORS.recAccept, "Minor Revision": COLORS.recMinor, "Major Revision": COLORS.recMajor, "Reject": COLORS.recReject };
  return map[rec] || COLORS.gray;
}

function getRecBg(rec) {
  const map = { "Accept": COLORS.bgGreen, "Minor Revision": COLORS.bgBlue, "Major Revision": COLORS.bgYellow, "Reject": COLORS.bgRed };
  return map[rec] || COLORS.bgGray;
}

// ===== 排版工具函式 =====
const border = { style: BorderStyle.SINGLE, size: 1, color: "BDC3C7" };
const borders = { top: border, bottom: border, left: border, right: border };
const cellPad = { top: 80, bottom: 80, left: 120, right: 120 };

function txt(text, opts = {}) {
  return new TextRun({ text, font: "Arial", size: 22, ...opts });
}

function para(runs, opts = {}) {
  return new Paragraph({
    children: Array.isArray(runs) ? runs : [runs],
    spacing: { after: 120, line: 276, ...(opts.spacing || {}) },
    ...opts,
  });
}

function hCell(text, width) {
  return new TableCell({
    borders, width: { size: width, type: WidthType.DXA },
    shading: { fill: COLORS.primary, type: ShadingType.CLEAR },
    margins: cellPad,
    children: [para(txt(text, { bold: true, size: 20, color: COLORS.white }), { alignment: AlignmentType.CENTER })],
  });
}

function dCell(runs, width, opts = {}) {
  const children = Array.isArray(runs) ? runs : [txt(runs, { size: 20 })];
  return new TableCell({
    borders, width: { size: width, type: WidthType.DXA },
    margins: cellPad,
    shading: opts.bg ? { fill: opts.bg, type: ShadingType.CLEAR } : undefined,
    children: [para(children)],
  });
}

// ===== 計算加權總分 =====
const scores = REVIEW_DATA.scores;
const weightedTotal = Object.values(scores).reduce((sum, s) => sum + s.score * s.weight, 0);

// ===== 文件結構 =====
const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 36, bold: true, font: "Arial", color: COLORS.primary },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: "Arial", color: COLORS.accent },
        paragraph: { spacing: { before: 280, after: 160 }, outlineLevel: 1 } },
      { id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 24, bold: true, font: "Arial", color: COLORS.dark },
        paragraph: { spacing: { before: 200, after: 120 }, outlineLevel: 2 } },
    ],
  },
  numbering: {
    config: [
      { reference: "bullets", levels: [
        { level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } },
      ]},
    ],
  },
  sections: [
    // ===== 標題頁 =====
    {
      properties: {
        page: {
          size: { width: 11906, height: 16838 }, // A4
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
        },
      },
      children: [
        new Paragraph({ spacing: { before: 2400 }, children: [] }),
        para(txt("Peer Review Report", { size: 52, bold: true, color: COLORS.primary }), { alignment: AlignmentType.CENTER }),
        para(txt("\u5B78\u8853\u8AD6\u6587\u5BE9\u7A3F\u5831\u544A", { size: 32, color: COLORS.accent }), {
          alignment: AlignmentType.CENTER,
          border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: COLORS.accent, space: 12 } },
        }),
        new Paragraph({ spacing: { before: 600 }, children: [] }),
        para(txt(REVIEW_DATA.paperTitle, { size: 26, bold: true, color: COLORS.dark }), { alignment: AlignmentType.CENTER }),
        para(txt(REVIEW_DATA.authors, { size: 22, color: COLORS.gray, italics: true }), { alignment: AlignmentType.CENTER }),
        para(txt(`Target Journal: ${REVIEW_DATA.journal}`, { size: 22, color: COLORS.gray }), { alignment: AlignmentType.CENTER }),
        para(txt(`Review Date: ${REVIEW_DATA.reviewDate}`, { size: 22, color: COLORS.gray }), { alignment: AlignmentType.CENTER }),
        // Recommendation 色塊
        new Paragraph({ spacing: { before: 600 }, children: [] }),
        new Table({
          width: { size: 5000, type: WidthType.DXA },
          columnWidths: [5000],
          rows: [new TableRow({ children: [
            new TableCell({
              borders: { top: border, bottom: border, left: border, right: border },
              width: { size: 5000, type: WidthType.DXA },
              shading: { fill: getRecBg(REVIEW_DATA.recommendation), type: ShadingType.CLEAR },
              margins: { top: 160, bottom: 160, left: 200, right: 200 },
              children: [para([
                txt("Recommendation: ", { size: 28, bold: true, color: COLORS.dark }),
                txt(REVIEW_DATA.recommendation, { size: 28, bold: true, color: getRecColor(REVIEW_DATA.recommendation) }),
              ], { alignment: AlignmentType.CENTER })],
            }),
          ] })],
        }),
      ],
    },
    // ===== 內容頁 =====
    {
      properties: {
        page: {
          size: { width: 11906, height: 16838 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
        },
      },
      headers: {
        default: new Header({ children: [
          para([
            txt(REVIEW_DATA.paperTitle, { size: 16, color: COLORS.gray, italics: true }),
          ], { alignment: AlignmentType.RIGHT }),
        ] }),
      },
      footers: {
        default: new Footer({ children: [
          para([
            txt("AI-Assisted Peer Review Report  |  Page ", { size: 16, color: COLORS.gray }),
            new TextRun({ children: [PageNumber.CURRENT], size: 16, color: COLORS.gray, font: "Arial" }),
          ], { alignment: AlignmentType.CENTER }),
        ] }),
      },
      children: [
        // --- 1. Summary ---
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [txt("1. Summary")] }),
        para(txt(REVIEW_DATA.summary)),

        // --- 2. Scores ---
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [txt("2. Evaluation Scores")] }),
        new Table({
          width: { size: 9026, type: WidthType.DXA },
          columnWidths: [2000, 800, 900, 1100, 4226],
          rows: [
            new TableRow({ children: [
              hCell("Dimension", 2000), hCell("Score", 800), hCell("Weight", 900),
              hCell("Weighted", 1100), hCell("Rationale", 4226),
            ] }),
            ...Object.entries(scores).map(([dim, s]) =>
              new TableRow({ children: [
                dCell(txt(dim.charAt(0).toUpperCase() + dim.slice(1), { size: 20, bold: true }), 2000),
                dCell(txt(String(s.score), { size: 20, bold: true, color: getScoreColor(s.score) }), 800, { bg: getScoreBg(s.score) }),
                dCell(`${(s.weight * 100).toFixed(0)}%`, 900),
                dCell((s.score * s.weight).toFixed(2), 1100),
                dCell(s.rationale, 4226),
              ] })
            ),
            new TableRow({ children: [
              dCell(txt("Weighted Total", { size: 20, bold: true }), 2000),
              dCell(txt(weightedTotal.toFixed(2), { size: 20, bold: true, color: getScoreColor(weightedTotal) }), 800, { bg: getScoreBg(weightedTotal) }),
              dCell("", 900), dCell("", 1100),
              dCell(txt(`Decision matrix suggests: ${REVIEW_DATA.recommendation}`, { size: 20, italics: true }), 4226),
            ] }),
          ],
        }),

        // --- 3. Strengths ---
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [txt("3. Strengths")] }),
        ...REVIEW_DATA.strengths.flatMap(s => [
          new Paragraph({ heading: HeadingLevel.HEADING_3, children: [txt(`${s.id}. ${s.title}`)] }),
          para(txt(s.detail)),
        ]),

        // --- 4. Major Issues ---
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [txt("4. Major Issues")] }),
        ...(REVIEW_DATA.majorIssues.length === 0
          ? [para(txt("No major issues identified.", { italics: true, color: COLORS.scoreGreen }))]
          : REVIEW_DATA.majorIssues.flatMap(issue => [
              new Paragraph({ heading: HeadingLevel.HEADING_3, children: [txt(`${issue.id}. ${issue.title}`)] }),
              para([txt("Location: ", { bold: true }), txt(issue.location)]),
              para([txt("Problem: ", { bold: true }), txt(issue.problem)]),
              para([txt("Suggestion: ", { bold: true }), txt(issue.suggestion)]),
            ])
        ),

        // --- 5. Minor Issues ---
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [txt("5. Minor Issues")] }),
        ...(REVIEW_DATA.minorIssues.length === 0
          ? [para(txt("No minor issues identified.", { italics: true, color: COLORS.scoreGreen }))]
          : REVIEW_DATA.minorIssues.flatMap(issue => [
              new Paragraph({ heading: HeadingLevel.HEADING_3, children: [txt(`${issue.id}. ${issue.title}`)] }),
              para([txt("Location: ", { bold: true }), txt(issue.location)]),
              para([txt("Problem: ", { bold: true }), txt(issue.problem)]),
              para([txt("Suggestion: ", { bold: true }), txt(issue.suggestion)]),
            ])
        ),

        // --- 6. Recommendation ---
        new Paragraph({ heading: HeadingLevel.HEADING_1, children: [txt("6. Recommendation")] }),
        new Table({
          width: { size: 9026, type: WidthType.DXA },
          columnWidths: [9026],
          rows: [new TableRow({ children: [
            new TableCell({
              borders,
              width: { size: 9026, type: WidthType.DXA },
              shading: { fill: getRecBg(REVIEW_DATA.recommendation), type: ShadingType.CLEAR },
              margins: { top: 120, bottom: 120, left: 200, right: 200 },
              children: [
                para(txt(REVIEW_DATA.recommendation, { size: 28, bold: true, color: getRecColor(REVIEW_DATA.recommendation) })),
                para(txt(REVIEW_DATA.recommendationRationale)),
                ...(REVIEW_DATA.overrideNote ? [
                  para([txt("Override Note: ", { bold: true, color: COLORS.recMajor }), txt(REVIEW_DATA.overrideNote)]),
                ] : []),
              ],
            }),
          ] })],
        }),

        // --- 7. 審稿限制聲明 ---
        new Paragraph({ spacing: { before: 400 }, children: [] }),
        para(txt("Disclaimer", { size: 20, bold: true, color: COLORS.gray }), {
          border: { top: { style: BorderStyle.SINGLE, size: 2, color: COLORS.gray, space: 8 } },
        }),
        para(txt(
          "本審稿報告由 AI 輔助產生，存在以下限制：(1) 無法驗證原始數據的真實性；" +
          "(2) 對極度專精的次領域可能缺乏深度判斷；(3) 無法評估圖表的視覺品質細節。" +
          "建議將本報告作為審稿參考，而非最終決定。",
          { size: 18, color: COLORS.gray, italics: true }
        )),
      ],
    },
  ],
});

// ===== 輸出 =====
const outputPath = "/mnt/user-data/outputs/review_report.docx";
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outputPath, buffer);
  console.log(`Done! Saved to ${outputPath}`);
});
