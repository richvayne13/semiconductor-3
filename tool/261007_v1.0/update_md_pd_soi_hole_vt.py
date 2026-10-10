# -*- coding: utf-8 -*-
import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update title / count
content = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A\)",
    r"## 2. 사용자 질문 기반 목차 (최신순 87대 Q&A)",
    content
)

# Shift existing Q 01 ~ Q 86 to Q 02 ~ Q 87
for old_n in range(86, 0, -1):
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
    "| **Q 01** | **PD-SOI에서 채널 아래 쌓인 정공(양전하)은 왜 Vt를 낮출까? (바디 전위 상승과 장벽 붕괴 로직)** ⭐ [최신 1번] | "
    "드레인 핀치오프 강전계 충격 이온화(Impact Ionization)로 생성된 정공($h^+$)들이 BOX 절연벽과 접합 장벽에 갇혀 중성 바디에 누적(플로팅 바디 효과), "
    "바디 전위 양(+)으로 부유 상승($V_{BS} > 0$), Vt 하강 3대 로직: ① 바디 효과 공식 역전($V_{th} = V_{th0} + \\gamma [\\sqrt{2\\phi_F - V_{BS}} - \\sqrt{2\\phi_F}]$, 순방향 바디 바이어스로 루트 항 축소), "
    "② 소스-채널 전위 장벽 강하(Potential Barrier Lowering, 전자 주입 용이), "
    "③ 게이트가 치워야 할 공간 공핍 전하($|Q_{dep}| = \\sqrt{2\\epsilon q N_A (2\\phi_F - V_B)}$) 축소로 산화막 전압 강하($V_{ox}$) 절감, "
    "치명적 킹크 효과(Kink Effect)와 $I_D$ 급증 및 이력 현상(Hysteresis), 중성 바디를 원천 소멸시킨 5~7nm 극박막 FD-SOI로의 진화 |\n"
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
