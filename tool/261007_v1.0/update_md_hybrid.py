# -*- coding: utf-8 -*-
with open(r'result\261007_v1.0\261007_semiconductor_sce_master.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update counts 76 -> 77
content = content.replace('최신순 76대 Q&A', '최신순 77대 Q&A')
content = content.replace('1번부터 76번까지 배치', '1번부터 77번까지 배치')

import re
lines = content.splitlines()
new_lines = []
for line in lines:
    if line.strip().startswith('| **Q 01** |'):
        # Add new Q 01 line before shifting
        new_q01 = '| **Q 01** | **하이브리드 본딩의 원리 (동일평면 연마, SiO2결합, Cu열팽창)** ⭐ [최신 1번] | CMP 초평탄화 및 의도적 Cu 디싱(2~5nm), 상온 친수성 SiO₂ 수소결합 ➔ Si-O-Si 공유결합, Cu 열팽창계수(CTE 17 vs 0.5) 30배 차이로 틈새 채움, 고온 Cu-Cu 고상 원자확산 및 단일 결정립 성장(Grain Growth), 무범프 3D 패키징 |'
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
