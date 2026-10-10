# -*- coding: utf-8 -*-
"""
update_md_depletion_cap.py
Update 261007_semiconductor_sce_master.md to reflect 83 questions (insert Q01, shift Q01..Q82 -> Q02..Q83).
"""

import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Update counts
text = re.sub(r'최신순으로 1번부터 \d+번까지', '최신순으로 1번부터 83번까지', text)
text = re.sub(r'총 \d+대 Q&A', '총 83대 Q&A', text)
text = re.sub(r'최신순 \d+대 Q&A', '최신순 83대 Q&A', text)

# Shift existing Q 01..Q 82 in table rows
for n in range(82, 0, -1):
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
new_row = """| **Q 01** | **공핍 커패시턴스의 구성 (S/D 접합Cap 외에 채널, 측벽, 폴리 공핍)** ⭐ [최신 1번] | MOSFET 내부 공핍 커패시턴스 3대 영역 해부: ① 게이트 직하부 채널 표면 공핍층($C_{dep,ch}$, $C_{ox}$와 직렬 연결되어 $SS$ 및 $V_{th}$ 결정), ② 소스/드레인 접합 공핍층($C_j$, 바닥면 $C_{j,bot}$과 측벽면 $C_{j,sw}$의 병렬 접지 부하, RC 딜레이 지배), ③ 폴리실리콘 게이트 내부 공핍층($C_{poly}$, EOT 손실의 원인), 반도체 업계의 공핍Cap 박멸 기술(SOI, FinFET/GAA 무도핑 채널, HKMG 금속 게이트) |"""

# Insert new_row right after table header
header_needle = "| :---: | :--- | :--- |\n"
pos = text.find(header_needle)
if pos != -1:
    insert_pos = pos + len(header_needle)
    text = text[:insert_pos] + new_row + "\n" + text[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated 261007_semiconductor_sce_master.md to 83 questions!")
