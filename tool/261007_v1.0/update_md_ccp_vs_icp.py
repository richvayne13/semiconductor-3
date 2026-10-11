# -*- coding: utf-8 -*-
"""
update_md_ccp_vs_icp.py
Updates result/261007_v1.0/261007_semiconductor_sce_master.md to reflect 97 Q&A topics.
Shifts Q01..Q96 to Q02..Q97, and adds new Q01 for CCP vs ICP.
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update header count
text = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A\)",
    "## 2. 사용자 질문 기반 목차 (최신순 97대 Q&A)",
    text
)

# Step 1: Shift existing Q01..Q96 to Q02..Q97 (descending)
for old_n in range(96, 0, -1):
    new_n = old_n + 1
    old_str = f"Q {old_n:02d}"
    new_str = f"Q {new_n:02d}"
    text = text.replace(f"| **{old_str}** |", f"| **{new_str}** |")

# Step 2: Remove [최신 1번] tag from old Q01 (now Q02)
text = text.replace("⭐ [최신 1번]", "")

# Step 3: Insert new Q01 row
row_q01 = "| **Q 01** | **CCP(용량결합)와 ICP(유도결합) 플라즈마의 본질적 차이 (방전 메커니즘, 밀도, 이온 에너지 독립 제어, 절연막 vs 도체 식각)** ⭐ [최신 1번] | 평행평판 수직 정전기장(Ez) vs 코일 유도 수평 회전전기장(Eθ), 플라즈마 밀도(CCP 10⁹~10¹⁰ vs ICP 10¹¹~10¹² cm⁻³)와 운전 압력 차이, 이온 밀도(Flux)와 이온 에너지(Bias)의 결합 종속성(CCP) vs 100% 완전 독립 분리 제어(Decoupling, ICP), 산화막/절연막 식각(Dielectric Etch, HARC, 강한 물리적 충돌 필수 ➔ CCP) vs 실리콘/도체/금속 식각(Conductor Etch, Poly-Si, STI, 초저손상/고선택비 ➔ ICP) 현업 분업 구조 해부 |\n"

table_header = "| :---: | :--- | :--- |\n"
header_pos = text.find(table_header)
if header_pos != -1:
    insert_pos = header_pos + len(table_header)
    text = text[:insert_pos] + row_q01 + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 261007_semiconductor_sce_master.md to 97 topics successfully!")
