# -*- coding: utf-8 -*-
"""
update_md_mocvd.py
Updates result/261007_v1.0/261007_semiconductor_sce_master.md to reflect 98 Q&A topics.
Shifts Q01..Q97 to Q02..Q98, and adds new Q01 for MOCVD & III-V/Ge.
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update header count
text = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A\)",
    "## 2. 사용자 질문 기반 목차 (최신순 98대 Q&A)",
    text
)

# Step 1: Shift existing Q01..Q97 to Q02..Q98 (descending)
for old_n in range(97, 0, -1):
    new_n = old_n + 1
    old_str = f"Q {old_n:02d}"
    new_str = f"Q {new_n:02d}"
    text = text.replace(f"| **{old_str}** |", f"| **{new_str}** |")

# Step 2: Remove [최신 1번] tag from old Q01 (now Q02)
text = text.replace("⭐ [최신 1번]", "")

# Step 3: Insert new Q01 row
row_q01 = "| **Q 01** | **MOCVD의 미래 비전과 3-5족(III-V)·Ge 고이동도 채널 완전 정복 (호칭 가이드, Post-Si 로직, GaN 전력, 실리콘 포토닉스)** ⭐ [최신 1번] | 구두 호칭 가이드('삼오족 반도체' 및 '쓰리 파이브 반도체' 100% 표준), Post-Si 한계 돌파용 InGaAs/InAs(NMOS 전자 이동도 25배↑) 및 Ge(PMOS 정공 이동도 4.4배↑) 고이동도 채널 물리, MOCVD 유기금속 에피택시의 원리와 MBE 대비 대량 양산성 우위, 3대 미래 비전(초고속 로직 CFET 이종 집적, GaN-on-Si 전력 반도체, CPO 실리콘 포토닉스 레이저 광원) 해부 |\n"

table_header = "| :---: | :--- | :--- |\n"
header_pos = text.find(table_header)
if header_pos != -1:
    insert_pos = header_pos + len(table_header)
    text = text[:insert_pos] + row_q01 + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 261007_semiconductor_sce_master.md to 98 topics successfully!")
