# -*- coding: utf-8 -*-
import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update title / count
content = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A\)",
    r"## 2. 사용자 질문 기반 목차 (최신순 93대 Q&A)",
    content
)

# Shift existing Q 01 ~ Q 92 to Q 02 ~ Q 93
for old_n in range(92, 0, -1):
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
    "| **Q 01** | **EUV 광학계의 반사 미러 전용 이유, 박막 응력(Stress) 제어 원리, Al vs Cu 배선 장단점 완전 정복** ⭐ [최신 1번] | "
    "EUV(13.5nm, 91.8eV) 초고에너지 광자의 모든 물질 100% 흡수 및 굴절률(n≈1) 한계로 투과 렌즈 불가 ➔ 초고진공 Mo/Si(40~50쌍) 브래그 다층 반사 미러(반사율 68%) 광학계, "
    "박막 응력의 2대 형태: 인장(Tensile, 웨이퍼 오목 휨 ➔ 균열) vs 압축(Compressive, 웨이퍼 볼록 휨 ➔ 박리) 및 "
    "스퍼터링 압력(Atomic Peening)/PECVD Dual-RF/어닐링/스트레인 공학 제어, "
    "Al vs Cu 배선: 비저항(2.7 vs 1.7)과 EM 신뢰성 차이 및 건식 식각 가능 여부(Al RIE 가능 vs Cu 다마신/CMP 필수)와 확산 방지막(Ta/TaN) 비교 |\n"
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
