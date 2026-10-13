# -*- coding: utf-8 -*-
"""
update_md_rie_mechanism.py
Updates result/261007_v1.0/261007_semiconductor_sce_master.md to reflect 102 Q&A topics.
Shifts Q01..Q101 to Q02..Q102, and adds new Q01 for RIE Mechanism.
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update header count
text = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A.*?\)",
    "## 2. 사용자 질문 기반 목차 (최신순 102대 Q&A 대기록)",
    text
)

# Step 1: Shift existing Q01..Q101 to Q02..Q102 (descending)
for old_n in range(101, 0, -1):
    new_n = old_n + 1
    old_str = f"Q {old_n:02d}"
    new_str = f"Q {new_n:02d}"
    text = text.replace(f"| **{old_str}** |", f"| **{new_str}** |")

# Step 2: Remove [최신 1번] tag from old Q01 (now Q02)
text = text.replace("⭐ [최신 1번]", "")

# Step 3: Insert new Q01 row
row_q01 = "| **Q 01** | **RIE 식각 메커니즘의 실체: etchant와 radical의 차이, 이온 충돌과 화학 반응의 순서 및 라디칼의 역할 완전 해부** ⭐ [최신 1번] | etchant(식각을 수행하는 기능적 역할 총칭)와 radical(홑전자를 가진 실질적 화학 반응 알맹이 F*, Cl*)의 동일체 관계, RIE 6단계 표면 시퀀스(라디칼 확산·흡착 ➔ 수직 이온 충돌에 의한 결합 약화 ➔ 흡착 라디칼과 반응하여 상온 기체 SiF₄ 생성 ➔ 탈착 및 배출), 라디칼의 핵심 역할(고체 Si를 휘발성 기체로 바꾸는 화학적 요리사이자 고선택비 보장), 이온-라디칼 동시 인가 시 식각 속도 10배 폭발 및 수직 비등방성 달성(Coburn & Winters 1979 시너지) 해부 |\n"

table_header = "| :---: | :--- | :--- |\n"
header_pos = text.find(table_header)
if header_pos != -1:
    insert_pos = header_pos + len(table_header)
    text = text[:insert_pos] + row_q01 + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 261007_semiconductor_sce_master.md to 102 topics successfully!")
