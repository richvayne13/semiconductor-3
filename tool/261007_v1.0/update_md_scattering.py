# -*- coding: utf-8 -*-
with open(r'result\261007_v1.0\261007_semiconductor_sce_master.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Update counts 74 -> 75
content = content.replace('최신순 74대 Q&A', '최신순 75대 Q&A')
content = content.replace('1번부터 74번까지 배치', '1번부터 75번까지 배치')

import re
lines = content.splitlines()
new_lines = []
for line in lines:
    if line.strip().startswith('| **Q 01** |'):
        # Add new Q 01 line before shifting
        new_q01 = '| **Q 01** | **이온화 불순물 산란이란 무엇인가? (쿨롱 편향과 이동도 저하)** ⭐ [최신 1번] | 고정 전하 이온($P^+, B^-$) 쿨롱 인력/척력 궤적 굴절, 브룩스-헤링 공식($\\mu_{ii} \\propto T^{3/2}/N_I$), $\\sigma = qN\\mu$에서 $N$ 증가 시 $\\mu$ 급락으로 저항 감소율 둔화(어빈 곡선 포화), 살리사이드(Salicide) 필수성 |'
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
