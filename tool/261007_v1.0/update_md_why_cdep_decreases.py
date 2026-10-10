# -*- coding: utf-8 -*-
"""
update_md_why_cdep_decreases.py
Update 261007_semiconductor_sce_master.md to reflect 84 questions (insert Q01, shift Q01..Q83 -> Q02..Q84).
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update counts
text = re.sub(r'최신순으로 1번부터 \d+번까지', '최신순으로 1번부터 84번까지', text)
text = re.sub(r'총 \d+대 Q&A', '총 84대 Q&A', text)
text = re.sub(r'최신순 \d+대 Q&A', '최신순 84대 Q&A', text)

# Shift existing Q 01..Q 83 in table rows
for n in range(83, 0, -1):
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
new_row = """| **Q 01** | **Body가 얇아지면 왜 Cdep가 작아질까? (C=dQ/dV 본질, BOX 직렬)** ⭐ [최신 1번] | 평행판 공식($C = \\epsilon/d$) 오해 해소, 커패시턴스의 물리적 정의($C = dQ/d\\psi$), 얇은 바디에서 100% 완전 공핍화 시 공핍 전하량 한계 고정($Q_{dep} = qN_A T_{body}$)으로 전하 변조 소멸($dQ/d\\psi \\approx 0$), 두껍고 저유전율인 매립 산화막(BOX)과의 직렬 연결($1/C_{eff} = T_{si}/\\epsilon_{si} + t_{BOX}/\\epsilon_{ox}$)로 등가 용량 급감, 무도핑 채널($N_A \\approx 0$) 실현으로 $C_{dep} \\approx 0$ 및 $SS \\approx 60\\,\\text{mV/dec}$ 복원 |"""

# Insert new_row right after table header
header_needle = "| :---: | :--- | :--- |\n"
pos = text.find(header_needle)
if pos != -1:
    insert_pos = pos + len(header_needle)
    text = text[:insert_pos] + new_row + "\n" + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated 261007_semiconductor_sce_master.md to 84 questions!")
