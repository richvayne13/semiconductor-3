# -*- coding: utf-8 -*-
"""
update_md_precursor.py
Updates result/261007_v1.0/261007_semiconductor_sce_master.md to reflect 96 Q&A topics.
Shifts Q01..Q95 to Q02..Q96, and adds new Q01 for Precursor vs Reactive Species.
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update header count
text = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A\)",
    "## 2. 사용자 질문 기반 목차 (최신순 96대 Q&A)",
    text
)

# Step 1: Shift existing Q01..Q95 to Q02..Q96 (descending)
for old_n in range(95, 0, -1):
    new_n = old_n + 1
    old_str = f"Q {old_n:02d}"
    new_str = f"Q {new_n:02d}"
    text = text.replace(f"| **{old_str}** |", f"| **{new_str}** |")

# Step 2: Remove [최신 1번] tag from old Q01 (now Q02) if present
text = text.replace("⭐ [최신 1번]", "")

# Step 3: Insert new Q01 row
row_q01 = "| **Q 01** | **반응종(Reactive Species)과 전구체(Precursor)는 똑같은 말일까? (개념 정의, 원료 vs 활성 입자, ALD/CVD/식각 메커니즘 비교)** ⭐ [최신 1번] | 전구체(박막을 형성할 골격 원소를 품고 투입되는 안정된 출발 원료 분자, 예: TMA, SiH4) vs 반응종(열/플라즈마로 쪼개져 홑전자를 갖고 맹렬한 반응성을 띤 초단수명 활성 입자, 예: O*, H*, F* 라디칼 및 이온)의 본질적 차이, ALD 3자 협업(전구체 흡착 ➔ 퍼지 ➔ 반응가스(Reactant) 투입 ➔ 플라즈마 반응종 활성화로 리간드 치환 및 박막 형성), 건식 식각 및 애싱 공정에서의 반응종 역할 해부 |\n"

table_header = "| :---: | :--- | :--- |\n"
header_pos = text.find(table_header)
if header_pos != -1:
    insert_pos = header_pos + len(table_header)
    text = text[:insert_pos] + row_q01 + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 261007_semiconductor_sce_master.md to 96 topics successfully!")
