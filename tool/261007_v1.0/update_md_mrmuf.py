# -*- coding: utf-8 -*-
with open(r'result\261007_v1.0\261007_semiconductor_sce_master.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update counts 69 -> 70
content = content.replace('최신순 69대 Q&A', '최신순 70대 Q&A')
content = content.replace('1번부터 69번까지 배치', '1번부터 70번까지 배치')

import re
lines = content.splitlines()
new_lines = []
for line in lines:
    if line.strip().startswith('| **Q 01** |'):
        # Add new Q 01 line before shifting
        new_q01 = '| **Q 01** | **MR-MUF에서 EMC는 원래 NCF에서 뭐였고 뭘 대체한 거야?** ⭐ [최신 1번] | NCF(고체 비전도성 필름) 완전 대체, 2중 공정(NCF 언더필+외벽 일반 EMC)을 단일 액상 EMC로 통합(Molded Underfill), 고밀도 세라믹 필러(열전도도 2.5배 향상), 방열 더미 범프 수직 고속도로, HBM3E 열 관리 |'
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
