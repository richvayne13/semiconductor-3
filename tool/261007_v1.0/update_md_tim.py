# -*- coding: utf-8 -*-
with open(r'result\261007_v1.0\261007_semiconductor_sce_master.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update counts 67 -> 68
content = content.replace('최신순 67대 Q&A', '최신순 68대 Q&A')
content = content.replace('1번부터 67번까지 배치', '1번부터 68번까지 배치')

import re
lines = content.splitlines()
new_lines = []
for line in lines:
    if line.strip().startswith('| **Q 01** |'):
        # Add new Q 01 line before shifting
        new_q01 = '| **Q 01** | **TIM은 열폭주를 줄이는 핵심 소재인데 뭐의 줄인말이야?** ⭐ [최신 1번] | Thermal Interface Material(열 계면 재료), 미세 표면 거칠기(공기 단열벽 $k=0.026$ 제거), 접촉 열저항($R_{th}$) 극소화, 계층별 TIM1(다이-IHS 인듐솔더) vs TIM2(IHS-쿨러 그리스), 차세대 700W+ AI가속기 방열 |'
        new_lines.append(new_q01)
        # Shift existing Q 01
        shifted = line.replace('**Q 01**', '**Q 02**').replace('⭐ [최신 1번]', '')
        new_lines.append(shifted)
    elif re.match(r'\|\s*\*\*Q\s+(\d+)\*\*\s*\|', line):
        m = re.match(r'\|\s*\*\*Q\s+(\d+)\*\*\s*\|(.*)', line)
        qnum = int(m.group(1)) + 1
        rest = m.group(2)
        new_lines.append(f'| **Q {qnum:02d}** |{rest}')
    else:
        new_lines.append(line)

with open(r'result\261007_v1.0\261007_semiconductor_sce_master.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines) + '\n')
print('Successfully updated master md')
