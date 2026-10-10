# -*- coding: utf-8 -*-
import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update title / count
content = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A\)",
    r"## 2. 사용자 질문 기반 목차 (최신순 89대 Q&A)",
    content
)

# Shift existing Q 01 ~ Q 88 to Q 02 ~ Q 89
for old_n in range(88, 0, -1):
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
    "| **Q 01** | **MOS Cap의 동작 특성 완전 정복 (축적·평탄대·공핍·반전 4대 영역, 에너지 밴드, C-V 거동)** ⭐ [최신 1번] | "
    "표면 전위($\\psi_s$)에 따른 4대 동작 영역: ① 축적($\\psi_s < 0$, 정공 결집, $C=C_{ox}$), ② 평탄대($\\psi_s=0$, 밴드 휨 제로, $C_{FB}$), "
    "③ 공핍($0<\\psi_s<2\\phi_B$, 정공 퇴출 및 공핍층 확장으로 $C$ 지속 하강), ④ 반전($\\psi_s \\ge 2\\phi_B$, 전자 반전층 형성, $W_{dep,max}$ 고정), "
    "반전 영역 C-V 3대 주파수 분기: 저주파(LF, $C_{ox}$ 복원) vs 고주파(HF, $C_{min}$ 정체) vs 깊은 공핍(Deep Depletion, $C$ 급락), "
    "실무 C-V 진단 파라미터($t_{ox}, V_{FB}, Q_f, N_A, D_{it}$) 추출 원리 해부 |\n"
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
