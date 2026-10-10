# -*- coding: utf-8 -*-
with open(r'result\261007_v1.0\261007_semiconductor_sce_master.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update counts 72 -> 73
content = content.replace('최신순 72대 Q&A', '최신순 73대 Q&A')
content = content.replace('1번부터 72번까지 배치', '1번부터 73번까지 배치')

import re
lines = content.splitlines()
new_lines = []
for line in lines:
    if line.strip().startswith('| **Q 01** |'):
        # Add new Q 01 line before shifting
        new_q01 = '| **Q 01** | **면저항의 도핑농도와 캐리어밀도는 P기판과 정공(p)을 뜻할까?** ⭐ [최신 1번] | P기판 잴 때는 붕소(NA)와 정공(p) 100% 일치, N형(NMOS S/D 등) 잴 때는 비소/인(ND)과 전자(n), 보편 공식 $\\sigma = q(n\\mu_n + p\\mu_p)$, 완전 이온화($p \\approx N_A, n \\approx N_D$), 영역별 측정 실무 |'
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
