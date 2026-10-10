# -*- coding: utf-8 -*-
"""
update_md_body_thickness.py
Update 261007_semiconductor_sce_master.md to reflect 80 questions (insert Q01, shift Q01..Q79 -> Q02..Q80).
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update counts
text = re.sub(r'최신순으로 1번부터 \d+번까지', '최신순으로 1번부터 80번까지', text)
text = re.sub(r'총 \d+대 Q&A', '총 80대 Q&A', text)
text = re.sub(r'최신순 \d+대 Q&A', '최신순 80대 Q&A', text)

# Shift existing Q 01..Q 79 in table rows
for n in range(79, 0, -1):
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
new_row = """| **Q 01** | **Body Thickness(바디 두께)가 얇아져야 하는 이유 (스케일 길이, 누설 차단)** ⭐ [최신 1번] | 스케일 길이 공식($\\lambda = \\sqrt{\\frac{\\epsilon_{si}}{2\\epsilon_{ox}} t_{ox} T_{body}}$)에서 $t_{ox}$ 터널링 한계 봉착 시 $L \\ge 3\\lambda$ 만족을 위한 유일한 $T_{body}$ 축소 필연성, 벌크 게이트 사각지대 지하 펀치스루 누설 경로의 기하학적 원천 박멸, 완전 공핍화(FD)로 $C_{dep} \\approx 0$ 및 $SS \\approx 60\\,\\text{mV/dec}$ 이상치 복원, 무도핑 채널(Undoped) 실현으로 쿨롱 산란 제거($\\mu \\uparrow$) 및 무작위 도펀트 요동(RDF) 편차 0% 박멸 |"""

# Insert new_row right after table header
header_needle = "| :---: | :--- | :--- |\n"
pos = text.find(header_needle)
if pos != -1:
    insert_pos = pos + len(header_needle)
    text = text[:insert_pos] + new_row + "\n" + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated 261007_semiconductor_sce_master.md to 80 questions!")
