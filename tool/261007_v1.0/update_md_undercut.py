# -*- coding: utf-8 -*-
with open(r'result\261007_v1.0\261007_semiconductor_sce_master.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update counts 73 -> 74
content = content.replace('최신순 73대 Q&A', '최신순 74대 Q&A')
content = content.replace('1번부터 73번까지 배치', '1번부터 74번까지 배치')

import re
lines = content.splitlines()
new_lines = []
for line in lines:
    if line.strip().startswith('| **Q 01** |'):
        # Add new Q 01 line before shifting
        new_q01 = '| **Q 01** | **언더컷(Undercut)이란 무엇인가? (원리, 문제점, GAA 응용)** ⭐ [최신 1번] | 마스크 하부 수평 침식 식각, 등방성 식각($R_L > 0$), CD 선폭 손실 및 패턴 붕괴(Collapse), RIE 및 측벽 보호막(Passivation) 방어, 3nm GAA 나노시트 선택적 SiGe 수평 식각(이너 스페이서 형성) |'
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
