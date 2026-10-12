# -*- coding: utf-8 -*-
"""
update_md_sheath_creation.py
Updates result/261007_v1.0/261007_semiconductor_sce_master.md to reflect 101 Q&A topics.
Shifts Q01..Q100 to Q02..Q101, and adds new Q01 for Sheath Creation.
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update header count
text = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A.*?\)",
    "## 2. 사용자 질문 기반 목차 (최신순 101대 Q&A 대기록)",
    text
)

# Step 1: Shift existing Q01..Q100 to Q02..Q101 (descending)
for old_n in range(100, 0, -1):
    new_n = old_n + 1
    old_str = f"Q {old_n:02d}"
    new_str = f"Q {new_n:02d}"
    text = text.replace(f"| **{old_str}** |", f"| **{new_str}** |")

# Step 2: Remove [최신 1번] tag from old Q01 (now Q02)
text = text.replace("⭐ [최신 1번]", "")

# Step 3: Insert new Q01 row
row_q01 = "| **Q 01** | **쉬스(Sheath) 영역이 생기는 것은 플라즈마 생성 과정 중 하나일까? (인과관계, 벽면 경계층의 본질, 연속 유지의 필수 루프)** ⭐ [최신 1번] | 인과관계와 기능적 역할의 엄밀한 구분: 플라즈마 형성 결과로서의 벽면 접촉 경계층(Boundary Layer, ve >> vi 전자 선행 탈출) vs 자속 방전(Self-sustained) 지속 생성 엔진으로서의 필수성, 전자의 무한 탈출을 막아 내부 준중성(ne ≈ ni)을 사수하는 플라즈마 자기방어 전위 장벽, 쉬스 전압강하 기반 이온 가속 ➔ 2차 전자 방출(γ) ➔ 기체 충돌 전리(α)의 영구 생성 루프 가동 타임라인 해부 |\n"

table_header = "| :---: | :--- | :--- |\n"
header_pos = text.find(table_header)
if header_pos != -1:
    insert_pos = header_pos + len(table_header)
    text = text[:insert_pos] + row_q01 + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 261007_semiconductor_sce_master.md to 101 topics successfully!")
