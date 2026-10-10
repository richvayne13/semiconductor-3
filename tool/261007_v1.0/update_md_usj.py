# -*- coding: utf-8 -*-
with open(r'result\261007_v1.0\261007_semiconductor_sce_master.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update counts 68 -> 69
content = content.replace('최신순 68대 Q&A', '최신순 69대 Q&A')
content = content.replace('1번부터 68번까지 배치', '1번부터 69번까지 배치')

import re
lines = content.splitlines()
new_lines = []
for line in lines:
    if line.strip().startswith('| **Q 01** |'):
        # Add new Q 01 line before shifting
        new_q01 = '| **Q 01** | **USJ가 줄이는 기생 커패시턴스는 Cj인가 Cdep인가? (접합 vs 공핍 구분)** ⭐ [최신 1번] | S/D 측면 접합($C_{j,sw} \propto X_j$) 및 오버랩($C_{ov}$) 100% 직접 감소, 채널 공핍 커패시턴스($C_{dep}=\\epsilon_{si}/W_{dep,ch}$)는 불변, 전하 분할(Charge Sharing 침범) 원천 차단 vs FD-SOI의 동시 절감 비교 |'
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
