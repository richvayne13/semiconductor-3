# -*- coding: utf-8 -*-
"""
update_md_charge_sharing.py
Update 261007_semiconductor_sce_master.md to reflect 85 questions (insert Q01, shift Q01..Q84 -> Q02..Q85).
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update counts
text = re.sub(r'최신순으로 1번부터 \d+번까지', '최신순으로 1번부터 85번까지', text)
text = re.sub(r'총 \d+대 Q&A', '총 85대 Q&A', text)
text = re.sub(r'최신순 \d+대 Q&A', '최신순 85대 Q&A', text)

# Shift existing Q 01..Q 84 in table rows
for n in range(84, 0, -1):
    old_str = f"Q {n:02d}"
    new_str = f"Q {n+1:02d}"
    if n == 1:
        text = re.sub(
            r'\| \*\*Q 01\*\* \| \*\*(.*?)\*\* ⭐ \[최신 1번\] \| (.*?) \|',
            rf'| **{new_str}** | **\1** | \2 |',
            text
        )
    else:
        text = text.replace(f"| **{old_str}** |", f"| **{new_str}** |")

# New row for Q 01
new_row = """| **Q 01** | **2차원 전하 분할(Charge Sharing)과 실효 두께 축소(Thinning) 상세** ⭐ [최신 1번] | 야우(Yau)의 사다리꼴 전하 분할 기하 모델, S/D 4분원 접합 침범으로 게이트 유효 전하 $Q_{B,eff} = Q_{B,1D}(1 - \\Delta L/2L)$ 축소, 게이트 면적($W \\times L$) 기준 평균 환산 두께 $W_{dep,eff} = W_{dep}(1 - \\Delta L/2L)$ 얇아짐(Thinning)의 수학적 유도, 분모 감소로 유효 $C_{dep,eff} = \\frac{\\epsilon}{W_{dep,eff}}$ 가파른 상승 및 $SS = 60(1 + C_{dep,eff}/C_{ox})$ 악화 메커니즘 |"""

# Insert new_row right after table header
header_needle = "| :---: | :--- | :--- |\n"
pos = text.find(header_needle)
if pos != -1:
    insert_pos = pos + len(header_needle)
    text = text[:insert_pos] + new_row + "\n" + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated 261007_semiconductor_sce_master.md to 85 questions!")
