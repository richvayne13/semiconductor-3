# -*- coding: utf-8 -*-
with open(r'result\261007_v1.0\261007_semiconductor_sce_master.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update counts 70 -> 71
content = content.replace('최신순 70대 Q&A', '최신순 71대 Q&A')
content = content.replace('1번부터 70번까지 배치', '1번부터 71번까지 배치')

import re
lines = content.splitlines()
new_lines = []
for line in lines:
    if line.strip().startswith('| **Q 01** |'):
        # Add new Q 01 line before shifting
        new_q01 = '| **Q 01** | **네킹공정을 통해 열충격 전위를 밖으로 배출시키는 원리 (사선 소멸)** ⭐ [최신 1번] | Dash Necking, {111} 슬립면 54.7° 사선 전파, 2~3mm 직경 극소화로 자유 표면(Free Surface) 충돌 및 소멸, 1420℃ 열충격 극복, 무전위 단결정 잉곳, 윌리엄 대시 |'
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
