# -*- coding: utf-8 -*-
"""
update_md_sputtering.py
Updates result/261007_v1.0/261007_semiconductor_sce_master.md to reflect 99 Q&A topics.
Shifts Q01..Q98 to Q02..Q99, and adds new Q01 for Sputtering.
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update header count
text = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A\)",
    "## 2. 사용자 질문 기반 목차 (최신순 99대 Q&A)",
    text
)

# Step 1: Shift existing Q01..Q98 to Q02..Q99 (descending)
for old_n in range(98, 0, -1):
    new_n = old_n + 1
    old_str = f"Q {old_n:02d}"
    new_str = f"Q {new_n:02d}"
    text = text.replace(f"| **{old_str}** |", f"| **{new_str}** |")

# Step 2: Remove [최신 1번] tag from old Q01 (now Q02)
text = text.replace("⭐ [최신 1번]", "")

# Step 3: Insert new Q01 row
row_q01 = "| **Q 01** | **스퍼터링(Sputtering)이란 무엇인가? (PVD 물리적 원리, 당구공 충돌 모델, 마그네트론 스퍼터링, CVD/ALD 대비 장단점)** ⭐ [최신 1번] | Ar⁺ 이온의 음극 타깃 충돌 및 운동량 전달(Momentum Transfer, 당구공 충돌 모델), 스퍼터링 수율(Yield, Y) 결정 4대 인자(이온 에너지, 입사각, 결합에너지, 질량비), 영구자석 N-S 배치로 전자를 가두는 마그네트론(E×B 드리프트)의 이온화율 100배 혁신, CVD/ALD 대비 재료 유연성(고융점 금속/합금 증착 및 우수한 접착력) vs 단차 도포성(Step Coverage) 한계, 구리 시드층(Cu Seed) 및 배리어 메탈(Ta/TaN, Ti/TiN) 핵심 응용 |\n"

table_header = "| :---: | :--- | :--- |\n"
header_pos = text.find(table_header)
if header_pos != -1:
    insert_pos = header_pos + len(table_header)
    text = text[:insert_pos] + row_q01 + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 261007_semiconductor_sce_master.md to 99 topics successfully!")
