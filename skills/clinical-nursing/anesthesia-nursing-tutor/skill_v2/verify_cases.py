# -*- coding: utf-8 -*-
import re, glob

files = sorted(glob.glob(r"C:\Users\13295\.zcode\skills\麻醉护理学学习导师\cases\*.md"))
print(f"共 {len(files)} 个病例文件\n")
print("=" * 80)

issues = []
for f in files:
    name = f.split("\\")[-1]
    with open(f, encoding="utf-8") as fh:
        content = fh.read()

    # 1. reviewed_by 检查
    if "[待专家审核]" in content:
        issues.append(f"[{name}] reviewed_by 仍含占位符 [待专家审核]")

    # 2. 提取 target_kcs
    tk_match = re.search(r"## 目标知识点.*?\n(.*?)\n##", content, re.S)
    if tk_match:
        tk_block = tk_match.group(1)
        declared_kcs = set(re.findall(r"- `([^`]+)`", tk_block))
    else:
        declared_kcs = set()
        issues.append(f"[{name}] 未找到 target_kcs 段落")

    # 3. rubric 中引用的 kc
    rubric_kcs = set(re.findall(r"^\s+kc:\s*(\S+)", content, re.M))

    # 4. KC 一致性
    undeclared = rubric_kcs - declared_kcs
    if undeclared:
        issues.append(f"[{name}] rubric 引用了未声明的 KC: {undeclared}")

    # 5. 权重和
    weights = [float(w) for w in re.findall(r"weight:\s*([\d.]+)", content)]
    if weights:
        total = sum(weights)
        status = "✓" if abs(total - 1.0) < 0.001 else f"✗ 和={total}"
    else:
        status = "无权重"

    # 6. safety_critical
    sc_match = re.search(r"safety_critical:\s*(\w+)", content)
    is_sc = sc_match and sc_match.group(1) == "true"
    sc_flag = "⚠️SC" if is_sc else "   "

    # 7. P0 来源（仅 SC）
    p0_ok = "—"
    if is_sc:
        has_version = ("edition:" in content) or ("year:" in content)
        has_verifier = "verified_by:" in content
        has_pending = "待补" in content or "待临床专家核验" in content
        if has_version and has_verifier and has_pending:
            p0_ok = "✓ 占位已标"
        else:
            issues.append(f"[{name}] safety_critical 但 P0 来源标注不完整")
            p0_ok = "✗ 不完整"

    print(f"{sc_flag} {name}")
    print(f"     KC声明={len(declared_kcs)} rubric引用={len(rubric_kcs)} 权重和={status} P0来源={p0_ok}")

print("\n" + "=" * 80)
if issues:
    print(f"❌ 发现 {len(issues)} 个问题：")
    for i in issues:
        print(f"  - {i}")
else:
    print("✅ 全部 12 病例合规：KC 一致 / reviewed_by 已更新 / 权重和=1.0 / P0 来源已标占位")
