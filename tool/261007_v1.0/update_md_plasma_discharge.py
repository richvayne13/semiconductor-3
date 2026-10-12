# -*- coding: utf-8 -*-
"""
update_md_plasma_discharge.py
Updates result/261007_v1.0/261007_semiconductor_sce_master.md to reflect 100 Q&A topics.
Shifts Q01..Q99 to Q02..Q100, and adds new Q01 for Plasma Discharge.
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update header count
text = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A\)",
    "## 2. 사용자 질문 기반 목차 (최신순 100대 Q&A 대기록)",
    text
)

# Step 1: Shift existing Q01..Q99 to Q02..Q100 (descending)
for old_n in range(99, 0, -1):
    new_n = old_n + 1
    old_str = f"Q {old_n:02d}"
    new_str = f"Q {new_n:02d}"
    text = text.replace(f"| **{old_str}** |", f"| **{new_str}** |")

# Step 2: Remove [최신 1번] tag from old Q01 (now Q02)
text = text.replace("⭐ [최신 1번]", "")

# Step 3: Insert new Q01 row
row_q01 = "| **Q 01** | **시스 전압강하, 2차 전자 방출, 충돌 전리의 연쇄 반응: 이걸 '플라즈마'라고 부르는 게 맞을까? (플라즈마 상태 vs 자속 방전 메커니즘 완전 해부)** ⭐ [최신 1번] | 질문자 물리 직관 100% 검증, 플라즈마 상태(준중성 제4의 물질 상태) vs 자속 글로우 방전(Self-sustained Discharge, 연쇄 유지 메커니즘)의 엄밀한 구분, 전자 이동도($v_e \\gg v_i$)에 의한 시스(Sheath) 공간전하 형성 및 급격한 전위 강하, 양이온 음극 충돌에 의한 2차 전자 방출($\\gamma$ 과정)과 시스 재가속 및 중성기체 충돌 전리 눈사태($\\alpha$ 과정), 타운센드 자속 방전 조건, 반도체 스퍼터링(PVD) 및 RIE 식각 엔진과의 직결 |\n"

table_header = "| :---: | :--- | :--- |\n"
header_pos = text.find(table_header)
if header_pos != -1:
    insert_pos = header_pos + len(table_header)
    text = text[:insert_pos] + row_q01 + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 261007_semiconductor_sce_master.md to 100 topics successfully!")
