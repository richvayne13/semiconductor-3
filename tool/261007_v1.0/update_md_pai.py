# -*- coding: utf-8 -*-
with open(r'result\261007_v1.0\261007_semiconductor_sce_master.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update counts 75 -> 76
content = content.replace('최신순 75대 Q&A', '최신순 76대 Q&A')
content = content.replace('1번부터 75번까지 배치', '1번부터 76번까지 배치')

import re
lines = content.splitlines()
new_lines = []
for line in lines:
    if line.strip().startswith('| **Q 01** |'):
        # Add new Q 01 line before shifting
        new_q01 = '| **Q 01** | **완만한 도핑의 Cj 감소 원리와 PAI(사전 비정질화) 기술** ⭐ [최신 1번] | 경사 접합($\\rho = qax$) 전하 중성으로 $W_{dep} \\propto a^{-1/3}$ 확장 및 $C_j \\downarrow$, PAI(Pre-Amorphization Implantation) 무거운 Ge 사전 주입으로 표면 비정질화(a-Si), 붕소(B) 채널링 원천 차단, SPER 고상 에피 재결정화, USJ 초얕은 접합 |'
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
