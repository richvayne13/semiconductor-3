# -*- coding: utf-8 -*-
import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update title / count
content = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A\)",
    r"## 2. 사용자 질문 기반 목차 (최신순 86대 Q&A)",
    content
)

# Shift existing Q 01 ~ Q 85 to Q 02 ~ Q 86
for old_n in range(85, 0, -1):
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
    "| **Q 01** | **공유 영역을 제외해 공핍층이 작아져서 Depletion Cap이 커진 건가? (질문자 직관 검증)** ⭐ [최신 1번] | "
    "질문자님의 물리적 직관 100% 완벽 검증, 소스/드레인이 가로채어 sharing하는 양쪽 귀퉁이 공핍 영역을 제외하면 게이트 순수 전하가 사다리꼴로 축소, "
    "$L$ 기준 평균 환산 실효 공핍 깊이 $W_{dep,eff}$가 얕아짐(Thinning), 평행판 공식($C = \\epsilon/d$)에서 두께($d = W_{dep,eff}$) 감소로 $C_{dep,eff}$ 상승 메커니즘, "
    "핵심 구분: '총 전하량($Q_{B,eff}$)'은 사다리꼴 축소로 감소($V_{th}$ 롤오프) vs '단위 면적당 커패시턴스($C_{dep,eff}$)'는 실효 두께 축소로 증가($SS$ 악화), "
    "현실에서 $C_{dep}$가 커지는 또 다른 핵심 요인(펀치스루 억제용 고농도 Halo 도핑 $W_{dep} \\propto 1/\\sqrt{N_A}$에 의한 물리적 두께 압축)과의 2대 시너지, "
    "3차원 FinFET/GAA 무도핑 채널 도입 배경 |\n"
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
