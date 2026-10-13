# -*- coding: utf-8 -*-
"""
update_md_macro_loading.py
Updates result/261007_v1.0/261007_semiconductor_sce_master.md to reflect 103 Q&A topics.
Shifts Q01..Q102 to Q02..Q103, and adds new Q01 for Macro Loading Effect & Radicals.
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update header count
text = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A.*?\)",
    "## 2. 사용자 질문 기반 목차 (최신순 103대 Q&A 대기록)",
    text
)

# Step 1: Shift existing Q01..Q102 to Q02..Q103 (descending)
for old_n in range(102, 0, -1):
    new_n = old_n + 1
    old_str = f"Q {old_n:02d}"
    new_str = f"Q {new_n:02d}"
    text = text.replace(f"| **{old_str}** |", f"| **{new_str}** |")

# Step 2: Remove [최신 1번] tag from old Q01 (now Q02)
text = text.replace("⭐ [최신 1번]", "")

# Step 3: Insert new Q01 row
row_q01 = "| **Q 01** | **매크로 로딩 이펙트(Macro Loading Effect)와 라디칼(Radical)의 역할: 패턴 크기별 식각 불균일 원인 및 압력·바이어스 제어 메커니즘 완전 해부** ⭐ [최신 1번] | 반응종의 실체(플라즈마 화학 식각을 주도하며 확산으로 이동하는 중성 라디칼 F*, Cl*), 매크로 로딩 이펙트의 발생 원리(오픈 패턴의 막대한 실리콘 노출 면적으로 인한 표면 라디칼 국소 고갈 Depletion vs 밀집 패턴의 라디칼 풍부로 인한 식각률 편차), 개선 솔루션의 물리적 인과관계(압력 증가로 분자 충돌 및 라디칼 생성량 절대 공급 보충, 바이어스 파워 감소로 표면 반응 속도를 진정시켜 공급 한계 탈출 및 확산 평형 Reaction-limited 유도, 더미 패턴 배치로 웨이퍼 전면 식각 개구율 균등화) 해부 |\n"

table_header = "| :---: | :--- | :--- |\n"
header_pos = text.find(table_header)
if header_pos != -1:
    insert_pos = header_pos + len(table_header)
    text = text[:insert_pos] + row_q01 + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 261007_semiconductor_sce_master.md to 103 topics successfully!")
