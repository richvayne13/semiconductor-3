# -*- coding: utf-8 -*-
import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update title / count
content = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A\)",
    r"## 2. 사용자 질문 기반 목차 (최신순 91대 Q&A)",
    content
)

# Shift existing Q 01 ~ Q 90 to Q 02 ~ Q 91
for old_n in range(90, 0, -1):
    new_n = old_n + 1
    old_str = f"Q {old_n:02d}"
    new_str = f"Q {new_n:02d}"
    content = re.sub(
        rf"\|\s*\*\*{old_str}\*\*\s*\|",
        f"| **{new_str}** |",
        content
    )

# Remove ⭐ [최신 1번] from old Q 01 (now Q 02)
content = content.replace("⭐ [최신 1번] |", "|")

# Define new Q 01 row
new_q01_row = (
    "| **Q 01** | **유전율은 전하를 품는 능력인데, 왜 이게 높아야 좋을까? (게이트 장악력, 터널링 차단, DRAM 축소)** ⭐ [최신 1번] | "
    "\"무조건 높아야 좋은 것은 아니다!\" (배선 IMD는 Low-k 필수 vs 게이트/DRAM은 High-k 필수), "
    "High-k가 필수적인 3대 이유: ① 게이트 채널 지배력($C_{ox}$) 극대화로 낮은 $V_{GS}$에서도 막대한 구동 전류($I_{on}$) 유치 및 DIBL 차단, "
    "② 두께와 정전용량의 분리(디커플링): 물리적 두께($t_{phys}$)를 $3.5\\text{nm}$로 두껍게 세워 양자 터널링 누설전류를 차단하면서도 전기적 $EOT$를 $0.55\\text{nm}$로 축소하는 마법, "
    "③ 초미세 DRAM 1T-1C 셀에서 좁쌀만 한 바닥 면적에도 데이터 유실을 막는 최소 $25\\,\\text{fF}$ 전하 보존 |\n"
)

# Insert new Q 01 right after header row
header_divider = "| :---: | :--- | :--- |\n"
pos = content.find(header_divider)
if pos != -1:
    insert_pos = pos + len(header_divider)
    content = content[:insert_pos] + new_q01_row + content[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully updated {md_path}")
