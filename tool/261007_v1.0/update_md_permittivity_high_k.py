# -*- coding: utf-8 -*-
import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update title / count
content = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A\)",
    r"## 2. 사용자 질문 기반 목차 (최신순 90대 Q&A)",
    content
)

# Shift existing Q 01 ~ Q 89 to Q 02 ~ Q 90
for old_n in range(89, 0, -1):
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
    "| **Q 01** | **유전율(Permittivity, ε)이란 무엇인가? 유전율이 높다는 것의 물리적 의미와 반도체 응용** ⭐ [최신 1번] | "
    "'전기(電)를 유도(誘)하여 품는 정도', 외부 전기장 하에서 전기적 분극(Polarization, $P$)을 일으켜 전기 에너지를 저장하고 외부 전계를 완화(스크리닝)하는 능력, "
    "유전율이 높다는 것의 3대 본질: ① 분극력 극대화(전기적 스펀지/에어백), ② 전하 저장 용량($C = \\epsilon A/d$) 비례 폭증, "
    "③ 쿨롱 힘($F \\propto 1/\\epsilon$) 약화(전하 간 상호작용 차폐), "
    "반도체 FEOL의 High-k($\\text{HfO}_2$, EOT 1nm 이하 축소로 $C_{ox} \\uparrow$ 및 터널링 차단) vs "
    "BEOL의 Low-k($\\text{SiCOH}$, RC 지연 및 누화 노이즈 차단) 양대 전략 비교 |\n"
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
