# -*- coding: utf-8 -*-
"""
update_md_pd_fd_soi.py
Update 261007_semiconductor_sce_master.md to reflect 82 questions (insert Q01, shift Q01..Q81 -> Q02..Q82).
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update counts
text = re.sub(r'최신순으로 1번부터 \d+번까지', '최신순으로 1번부터 82번까지', text)
text = re.sub(r'총 \d+대 Q&A', '총 82대 Q&A', text)
text = re.sub(r'최신순 \d+대 Q&A', '최신순 82대 Q&A', text)

# Shift existing Q 01..Q 81 in table rows
for n in range(81, 0, -1):
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
new_row = """| **Q 01** | **SOI에서 부분공핍(PD)과 완전공핍(FD)이 뜻하는 것은? (원리, FBE, Kink)** ⭐ [최신 1번] | 실리콘 박막 두께($T_{si}$)와 최대 공핍층 폭($W_{dep,max}$)의 비교 기준, PD-SOI($T_{si} > W_{dep}$)의 하부 중성 영역(Neutral Body) 잔류 및 정공 축적으로 인한 플로팅 바디 효과(FBE)와 킹크(Kink) 왜곡, FD-SOI($T_{si} < W_{dep}$, 5~7nm)의 바디 100% 완전 공핍화로 FBE 원천 박멸, $C_{dep} \\approx 0$화로 $SS \\approx 60\\,\\text{mV/dec}$ 복원, 무도핑 채널(Undoped) 실현 및 백 바이어스(Back Bias) 동적 튜닝 혁신 |"""

# Insert new_row right after table header
header_needle = "| :---: | :--- | :--- |\n"
pos = text.find(header_needle)
if pos != -1:
    insert_pos = pos + len(header_needle)
    text = text[:insert_pos] + new_row + "\n" + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated 261007_semiconductor_sce_master.md to 82 questions!")
