# -*- coding: utf-8 -*-
"""
update_md_plasma_loss.py
Updates result/261007_v1.0/261007_semiconductor_sce_master.md to reflect 104 Q&A topics.
Shifts Q01..Q103 to Q02..Q104, and adds new Q01 for Plasma Loss Mechanism.
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update header count
text = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A.*?\)",
    "## 2. 사용자 질문 기반 목차 (최신순 104대 Q&A 대기록)",
    text
)

# Step 1: Shift existing Q01..Q103 to Q02..Q104 (descending)
for old_n in range(103, 0, -1):
    new_n = old_n + 1
    old_str = f"Q {old_n:02d}"
    new_str = f"Q {new_n:02d}"
    text = text.replace(f"| **{old_str}** |", f"| **{new_str}** |")

# Step 2: Remove [최신 1번] tag from old Q01 (now Q02)
text = text.replace("⭐ [최신 1번]", "")

# Step 3: Insert new Q01 row
row_q01 = "| **Q 01** | **플라즈마의 소멸(Loss) 메커니즘과 전자 손실의 실체: '기체 원자 충돌 미흡' vs '양이온 재결합' 오류 교정 및 벽면 손실(Wall Loss) 완전 해부** ⭐ [최신 1번] | 원문 서술의 개념 오류 교정(전자가 양이온과 충돌하지 못해서가 아니라 '중성 기체 원자와 이온화 충돌하여 증식하지 못하고 Anode/벽면으로 흡수'되는 것이 전자 손실의 본질), 전자-양이온 충돌의 역설(양이온과 충돌하면 손실을 막는 게 아니라 둘 다 중성 원자로 소멸하는 체적 재결합 Recombination 현상임), 반도체 약전리 플라즈마 밀도 특성(중성 기체가 99.99%로 이온보다 10만 배 압도적), 플라즈마 소멸의 2대 축(99% 이상을 지배하는 벽면 표면 손실 Wall Loss vs 저압서 극소한 체적 재결합 Volume Recombination), 정상 상태 유지 방정식(생성률 = 소멸률 평형 및 압력 강하 시 파센 좌측 한계 방전 꺼짐) 해부 |\n"

table_header = "| :---: | :--- | :--- |\n"
header_pos = text.find(table_header)
if header_pos != -1:
    insert_pos = header_pos + len(table_header)
    text = text[:insert_pos] + row_q01 + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 261007_semiconductor_sce_master.md to 104 topics successfully!")
