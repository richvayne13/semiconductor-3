# -*- coding: utf-8 -*-
"""
update_md_split_topics.py
Updates result/261007_v1.0/261007_semiconductor_sce_master.md to reflect 95 Q&A topics.
Splits Q01 into Q01 (EUV), Q02 (Stress), Q03 (Al vs Cu), and shifts Q02..Q93 to Q04..Q95.
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update header
text = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A\)",
    "## 2. 사용자 질문 기반 목차 (최신순 95대 Q&A)",
    text
)

# Step 1: Shift existing Q02..Q93 to Q04..Q95 (in descending order)
for old_n in range(93, 1, -1):
    new_n = old_n + 2
    old_str = f"Q {old_n:02d}"
    new_str = f"Q {new_n:02d}"
    text = text.replace(f"| **{old_str}** |", f"| **{new_str}** |")

# Step 2: Remove old combined Q01 row
text = re.sub(
    r'\| \*\*Q 01\*\* \| \*\*EUV 광학계의 반사 미러 전용 이유, 박막 응력.*?\|\n',
    '',
    text
)

# Step 3: Insert 3 new rows for Q01, Q02, Q03 right after the table header
row_q01 = "| **Q 01** | **EUV 장비 광학계가 미러(반사경)로만 구성된 이유 (13.5nm 광자 흡수, 굴절률 한계, Mo/Si 브래그 반사)** ⭐ [최신 1번] | EUV(13.5nm, 91.8eV) 초고에너지 광자의 모든 물질 100% 흡수 및 굴절률(n≈1) 한계로 투과 렌즈 불가 ➔ 초고진공 Mo/Si(40~50쌍) 브래그 다층 반사 미러(반사율 68%) 광학계, 11개 미러 통과 시 광량 손실((0.68)¹¹≈1.5%)을 극복하기 위한 수백W급 주석(Sn) 플라즈마 광원 |\n"
row_q02 = "| **Q 02** | **박막 응력(Thin Film Stress)이란 무엇이고 이를 제어하는 방식은 무엇인가? (인장 vs 압축, 스트레인 공학)** | 박막 응력 2대 형태: 인장(Tensile, 웨이퍼 오목 휨 ➔ 균열/크랙) vs 압축(Compressive, 웨이퍼 볼록 휨 ➔ 들뜸/박리), 스퍼터링 공정 압력(Atomic Peening)/PECVD Dual-RF/어닐링을 통한 무응력(Zero-stress) 제어, NMOS 인장 SiN 캡핑(전자 이동도 50%↑) 및 PMOS 압축 e-SiGe(정공 이동도 100%↑) 스트레인 엔지니어링 |\n"
row_q03 = "| **Q 03** | **알루미늄(Al)과 구리(Cu)를 사용했을 때 장단점 완전 비교 (비저항, EM 신뢰성, 듀얼 다마신 공정)** | 비저항(Al 2.7 vs Cu 1.7 μΩ·cm)으로 인한 RC 지연 40% 단축, 녹는점 차이(660℃ vs 1085℃)에 따른 EM 신뢰성 10~100배 향상, 건식 플라즈마 식각 가능 여부(Al RIE 가능 vs Cu 휘발성 화합물 부재로 불가) ➔ 듀얼 다마신(Dual Damascene) 및 CMP 공정 혁신, Ta/TaN 배리어 메탈 필수성, 최상층 패드(Al) vs 내부 고속 배선(Cu) 분업 |\n"

table_header = "| :---: | :--- | :--- |\n"
header_pos = text.find(table_header)
if header_pos != -1:
    insert_pos = header_pos + len(table_header)
    text = text[:insert_pos] + row_q01 + row_q02 + row_q03 + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated 261007_semiconductor_sce_master.md successfully!")
