# -*- coding: utf-8 -*-
import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update title / count
content = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A\)",
    r"## 2. 사용자 질문 기반 목차 (최신순 88대 Q&A)",
    content
)

# Shift existing Q 01 ~ Q 87 to Q 02 ~ Q 88
for old_n in range(87, 0, -1):
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
    "| **Q 01** | **MOS Cap(모스 커패시터)과 MOSFET의 본질적 차이 (구조, 반전층 공급원, C-V 거동 비교)** ⭐ [최신 1번] | "
    "2단자 수동 정전용량 소자(수평 직류 전류 $I_{DS}=0$) vs 4단자 능동 스위치/증폭기(게이트 전압으로 $I_{DS}$ On/Off 제어), "
    "반전층 캐리어 공급원의 결정적 차이: 열 생성(Thermal EHP Generation, $\\tau \\sim \\text{ms}$)에 의존하는 MOS Cap vs "
    "소스/드레인($N^+$) 전자 저수지에서 피코초($\\text{ps}$) 단위로 즉각 공급하는 MOSFET, "
    "C-V 특성 곡선 고주파(HF) 반전층 분기: 소수캐리어가 못 따라와 $C_{min}$에 정체되는 MOS Cap vs S/D 직접 공급으로 $C_{ox}$로 100% 완전 회복하는 MOSFET, "
    "FAB 공정 진단($t_{ox}, V_{FB}, D_{it}, N_A$ 역산) vs 고성능 CMOS 로직 컴퓨팅 응용 비교 |\n"
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
