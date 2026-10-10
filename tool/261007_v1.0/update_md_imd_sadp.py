# -*- coding: utf-8 -*-
"""
update_md_imd_sadp.py
Update 261007_semiconductor_sce_master.md to reflect 78 questions (insert Q01, shift Q01..Q77 -> Q02..Q78).
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update counts
text = re.sub(r'최신순으로 1번부터 \d+번까지', '최신순으로 1번부터 78번까지', text)
text = re.sub(r'총 \d+대 Q&A', '총 78대 Q&A', text)
text = re.sub(r'최신순 \d+대 Q&A', '최신순 78대 Q&A', text)

# Shift existing Q 01..Q 77 in table rows
# Look for table rows starting with | **Q XX** |
for n in range(77, 0, -1):
    old_str = f"Q {n:02d}"
    new_str = f"Q {n+1:02d}"
    # Replace '| **Q XX** |' with '| **Q YY** |'
    # Also remove ⭐ [최신 1번] if on old Q 01
    if n == 1:
        text = re.sub(
            r'\| \*\*Q 01\*\* \| \*\*(.*?)\*\* ⭐ \[최신 1번\] \| (.*?) \|',
            rf'| **{new_str}** | **\1** | \2 |',
            text
        )
    else:
        text = text.replace(f"| **{old_str}** |", f"| **{new_str}** |")

# New row for Q 01
new_row = """| **Q 01** | **IMD 정의, 스페이서 피치분할(SADP), HBM TIM 미세공기 충진** ⭐ [최신 1번] | IMD(Inter-Metal Dielectric) vs ILD(M1과 소자 분리) 및 Low-k(SiCOH) RC 딜레이 개선, SADP(자가정렬 스페이서 피치 분할) 5단계(Mandrel ➔ ALD 스페이서 ➔ 에치백 ➔ 코어 스트립 ➔ 피치 1/2 분할) 및 오버레이 에러 제로, HBM 16단 패키지 상단 TIM1 위치 및 계면 미세 요철(Micro-roughness) 사이 단열 공기($k=0.026$) 100% 배출 충진(Air Displacement)으로 접촉 열저항($R_{th}$) 극소화 |"""

# Insert new_row right after table header
header_needle = "| :---: | :--- | :--- |\n"
pos = text.find(header_needle)
if pos != -1:
    insert_pos = pos + len(header_needle)
    text = text[:insert_pos] + new_row + "\n" + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated 261007_semiconductor_sce_master.md to 78 questions!")
