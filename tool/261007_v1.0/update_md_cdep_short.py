# -*- coding: utf-8 -*-
"""
update_md_cdep_short.py
Update 261007_semiconductor_sce_master.md to reflect 79 questions (insert Q01, shift Q01..Q78 -> Q02..Q79).
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update counts
text = re.sub(r'최신순으로 1번부터 \d+번까지', '최신순으로 1번부터 79번까지', text)
text = re.sub(r'총 \d+대 Q&A', '총 79대 Q&A', text)
text = re.sub(r'최신순 \d+대 Q&A', '최신순 79대 Q&A', text)

# Shift existing Q 01..Q 78 in table rows
for n in range(78, 0, -1):
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
new_row = """| **Q 01** | **채널이 짧아지면 공핍 커패시턴스가 왜 올라갈까? (Cdep 증가 원리)** ⭐ [최신 1번] | 펀치스루 억제용 고농도 도핑($N_A \\uparrow$, Halo) ➔ $W_{dep} \\propto 1/\\sqrt{N_A}$ 축소로 $C_{dep} \\propto \\sqrt{N_A}$ 직접 상승, 2차원 전하 분할(Charge Sharing)로 실효 두께($W_{dep,eff}$) 왜곡 축소 및 유효 $C_{dep}$ 상승, $SS = 60(1 + C_{dep}/C_{ox})$ 악화 및 $I_{off}$ 누설전류 폭발, FinFET/GAA 무도핑 채널 도입 배경 |"""

# Insert new_row right after table header
header_needle = "| :---: | :--- | :--- |\n"
pos = text.find(header_needle)
if pos != -1:
    insert_pos = pos + len(header_needle)
    text = text[:insert_pos] + new_row + "\n" + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated 261007_semiconductor_sce_master.md to 79 questions!")
