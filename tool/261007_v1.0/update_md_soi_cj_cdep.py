# -*- coding: utf-8 -*-
"""
update_md_soi_cj_cdep.py
Update 261007_semiconductor_sce_master.md to reflect 81 questions (insert Q01, shift Q01..Q80 -> Q02..Q81).
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update counts
text = re.sub(r'최신순으로 1번부터 \d+번까지', '최신순으로 1번부터 81번까지', text)
text = re.sub(r'총 \d+대 Q&A', '총 81대 Q&A', text)
text = re.sub(r'최신순 \d+대 Q&A', '최신순 81대 Q&A', text)

# Shift existing Q 01..Q 80 in table rows
for n in range(80, 0, -1):
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
new_row = """| **Q 01** | **SOI로 없애는 기생Cap은 접합Cap(Cj)일까 공핍Cap(Cdep)일까?** ⭐ [최신 1번] | 'Body와 S/D 분리' 문맥의 구조적 대상은 소스/드레인 접합 커패시턴스($C_j$), 그러나 $C_j$의 물리적 작동 메커니즘 자체가 P-N 접합 공핍 영역의 $C_{dep,pn}$임 (이름=Cj, 물리실체=Cdep), S/D 바닥이 BOX 산화막에 닿아 P-N 접합면 자체를 물리적으로 소멸시켜 기생 용량 90% 제거(속도 20~30% 향상), 게이트 아래 채널 $C_{dep,ch}$(SS 인자)와의 명확한 구분 및 FD-SOI의 2중 제거 혜택 |"""

# Insert new_row right after table header
header_needle = "| :---: | :--- | :--- |\n"
pos = text.find(header_needle)
if pos != -1:
    insert_pos = pos + len(header_needle)
    text = text[:insert_pos] + new_row + "\n" + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated 261007_semiconductor_sce_master.md to 81 questions!")
