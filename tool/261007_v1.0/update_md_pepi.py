# -*- coding: utf-8 -*-
with open(r'result\261007_v1.0\261007_semiconductor_sce_master.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update counts 71 -> 72
content = content.replace('최신순 71대 Q&A', '최신순 72대 Q&A')
content = content.replace('1번부터 71번까지 배치', '1번부터 72번까지 배치')

import re
lines = content.splitlines()
new_lines = []
for line in lines:
    if line.strip().startswith('| **Q 01** |'):
        # Add new Q 01 line before shifting
        new_q01 = '| **Q 01** | **P- 에피층 저농도 도핑으로 Cj 낮추는 메커니즘 (Wdep 반비례)** ⭐ [최신 1번] | 질문 알고리즘 100% 일치 ($N_A \\downarrow \\implies W_{dep} \\uparrow \\implies C_j \\downarrow$), 전하 중성 조건($Q^+=Q^-$), 평행판 커패시터 모델($C_j = \\epsilon_s/W_{dep}$), RC 지연 단축, P/P+ 에피 웨이퍼(상부 속도 + 하부 래치업 방어) |'
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
