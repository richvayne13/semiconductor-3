# -*- coding: utf-8 -*-
"""
insert_mrmuf_emc_ncf_q01.py
사용자 질문: "mrmuf에서 emc는 원래 ncf에서 원래 뭐였어?뭘대체한거야"
대시보드 최상단 Q01로 신규 추가하고, 기존 69개 질문을 Q02~Q70으로 시프트 (총 70개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (HBM 첨단 패키징)",
    "title": "MR-MUF의 EMC는 기존 TC-NCF에서 무엇이었고 뭘 대체한 것일까? (NCF 필름 대체 및 방열 메커니즘)",
    "nav_title": "MR-MUF의 EMC는 원래 NCF에서 뭘 대체한 거야? (NCF vs EMC 비교)",
    "summary": [
        "<strong>핵심 대체 대상 (NCF 필름 자체를 완벽히 대체!)</strong>: TC-NCF에서 층과 층 사이에 일일이 끼워 넣던 <strong>고체 절연 필름인 'NCF(Non-Conductive Film)' 자체를 액상 EMC가 완전히 대체</strong>했습니다. 즉, 필름을 깔지 않고 범프만 맞댄 채 한 번에 구운 뒤(Mass Reflow), 액상 EMC를 틈새로 밀어 넣어 굳힌 것입니다.",
        "<strong>'이원화된 2중 공정'을 '단일 공정(MUF)'으로 통합</strong>: 기존 TC-NCF는 [다이 틈새: NCF 필름] + [외부 껍데기: 일반 EMC 몰딩]이라는 서로 다른 두 가지 재료와 공정을 썼지만, MR-MUF는 <strong>특수 고열전도 액상 EMC 딱 하나로 틈새 채우기(Underfill)와 외부 껍데기 포장(Molding)을 한 번에 동시 해결(Molded Underfill)</strong>했습니다.",
        "<strong>대체한 결정적 이유 ①: 열전도율 2.5배 폭증</strong>: NCF는 고체 필름이라 세라믹 방열 필러(Silica Filler)를 많이 넣으면 필름이 딱딱해져 범프가 뚫고 지나가지 못합니다($k \approx 0.2 \sim 0.4\text{ W/m}\cdot\text{K}$). 반면 MR-MUF용 액상 EMC는 액체 상태로 주입되므로 방열 필러를 80~90%까지 듬뿍 채울 수 있어 <strong>열전도율이 2~2.5배 이상($k \approx 1.5 \sim 2.5\text{ W/m}\cdot\text{K}$) 압도적</strong>입니다.",
        "<strong>대체한 결정적 이유 ②: 열 충격 누적 및 휨(Warpage) 해소</strong>: TC-NCF는 16단 적층 시 16번을 일일이 고온·고압으로 누르고 굽는(TC) 과정을 반복하여 웨이퍼가 휘고 공정 시간이 수십 배 걸립니다. MR-MUF는 한 번에 오븐에서 전부 솔더링한 후 액상 EMC를 한 방에 쏴서 굳히므로 <strong>열 스트레스가 적고 생산 속도가 혁신적으로 빠릅니다.</strong>"
    ],
    "svg_title": "📊 [HBM 접합 공정 비교: TC-NCF vs MR-MUF] NCF 고체 필름과 액상 EMC(Molded Underfill)의 구조적 차이",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: TC-NCF Process & Structure -->
  <rect x="20" y="25" width="375" height="320" rx="8" fill="#0f172a" stroke="#f43f5e" stroke-width="1.2"/>
  <text x="35" y="48" fill="#f43f5e" font-size="12" font-weight="800">1. 기존 TC-NCF 방식: 고체 NCF 필름 적층</text>

  <g transform="translate(35, 60)">
    <!-- Dies with NCF Film -->
    <rect x="0" y="0" width="345" height="150" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    
    <!-- Die 3 -->
    <rect x="20" y="15" width="305" height="22" fill="#1e3a8a" rx="2"/>
    <text x="120" y="30" fill="#93c5fd" font-size="9" font-weight="700">DRAM Core Die #3</text>

    <!-- NCF Film Layer 2 -->
    <rect x="20" y="38" width="305" height="14" fill="#f43f5e" rx="1"/>
    <text x="95" y="49" fill="#ffffff" font-size="8.5" font-weight="800">고체 NCF 필름 (방열 필러 적음, k≈0.3)</text>
    <circle cx="50" cy="45" r="3.5" fill="#f59e0b"/><circle cx="150" cy="45" r="3.5" fill="#f59e0b"/><circle cx="250" cy="45" r="3.5" fill="#f59e0b"/>

    <!-- Die 2 -->
    <rect x="20" y="53" width="305" height="22" fill="#1e3a8a" rx="2"/>
    <text x="120" y="68" fill="#93c5fd" font-size="9" font-weight="700">DRAM Core Die #2</text>

    <!-- NCF Film Layer 1 -->
    <rect x="20" y="76" width="305" height="14" fill="#f43f5e" rx="1"/>
    <text x="95" y="87" fill="#ffffff" font-size="8.5" font-weight="800">고체 NCF 필름 (층마다 열압착 TC 본딩)</text>
    <circle cx="50" cy="83" r="3.5" fill="#f59e0b"/><circle cx="150" cy="83" r="3.5" fill="#f59e0b"/><circle cx="250" cy="83" r="3.5" fill="#f59e0b"/>

    <!-- Die 1 -->
    <rect x="20" y="91" width="305" height="22" fill="#1e3a8a" rx="2"/>
    <text x="120" y="106" fill="#93c5fd" font-size="9" font-weight="700">DRAM Core Die #1 (Base)</text>

    <!-- Outer Mold (Secondary step) -->
    <rect x="5" y="120" width="335" height="22" fill="#475569" rx="2"/>
    <text x="40" y="135" fill="#e2e8f0" font-size="8.5">별도 2차 공정: 외벽만 감싸는 일반 EMC 몰딩</text>
  </g>

  <!-- Explanatory points TC-NCF -->
  <g transform="translate(35, 222)">
    <rect x="0" y="0" width="345" height="110" rx="6" fill="#1e293b"/>
    <text x="10" y="18" fill="#f87171" font-size="9.5" font-weight="700">■ TC-NCF의 구조적 한계</text>
    <text x="10" y="34" fill="#cbd5e1" font-size="8.5">• 재료 2원화: 틈새는 NCF 필름 + 외벽은 일반 EMC</text>
    <text x="10" y="50" fill="#fca5a5" font-size="8.5">• 열전도 취약: 필름 특성상 실리카 필러 함량 한계(k ≈ 0.3)</text>
    <text x="10" y="66" fill="#cbd5e1" font-size="8.5">• 공정 병목: 16단 적층 시 16번 고온/가압(TC) ➔ 열 충격 누적</text>
    <text x="10" y="82" fill="#fca5a5" font-size="8.5">• 휨(Warpage) 발생으로 고적층(12~16단) 수율 저하</text>
    <text x="10" y="98" fill="#94a3b8" font-size="8">• 방열 전용 더미 범프를 많이 깔기 어려움</text>
  </g>

  <!-- Right: MR-MUF Process & Structure -->
  <rect x="410" y="25" width="350" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
  <text x="425" y="48" fill="#10b981" font-size="12" font-weight="800">2. 혁신 MR-MUF 방식: 액상 EMC 일괄 주입</text>

  <g transform="translate(425, 60)">
    <!-- Container representing single EMC surrounding everything -->
    <rect x="0" y="0" width="320" height="150" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <text x="12" y="16" fill="#6ee7b7" font-size="8.5" font-weight="800">★ 단일 액상 EMC가 틈새(Underfill) + 외벽(Molding) 동시 충진!</text>

    <!-- Die 3 -->
    <rect x="25" y="24" width="270" height="22" fill="#1e3a8a" rx="2"/>
    <text x="105" y="38" fill="#93c5fd" font-size="9" font-weight="700">DRAM Core Die #3</text>

    <!-- Liquid EMC filled Gap with high filler -->
    <g fill="#10b981">
      <circle cx="50" cy="51" r="3.5" fill="#f59e0b"/><circle cx="100" cy="51" r="3.5" fill="#f59e0b"/>
      <circle cx="150" cy="51" r="3.5" fill="#f59e0b"/><circle cx="200" cy="51" r="3.5" fill="#f59e0b"/>
      <circle cx="250" cy="51" r="3.5" fill="#f59e0b"/>
    </g>
    <text x="45" y="55" fill="#a7f3d0" font-size="7.5" font-weight="800">액상 고열전도 EMC 침투 (k = 1.5 ~ 2.5 W/m·K! 방열 2.5배)</text>

    <!-- Die 2 -->
    <rect x="25" y="60" width="270" height="22" fill="#1e3a8a" rx="2"/>
    <text x="105" y="74" fill="#93c5fd" font-size="9" font-weight="700">DRAM Core Die #2</text>

    <!-- Liquid EMC filled Gap -->
    <g fill="#10b981">
      <circle cx="50" cy="87" r="3.5" fill="#f59e0b"/><circle cx="100" cy="87" r="3.5" fill="#f59e0b"/>
      <circle cx="150" cy="87" r="3.5" fill="#f59e0b"/><circle cx="200" cy="87" r="3.5" fill="#f59e0b"/>
      <circle cx="250" cy="87" r="3.5" fill="#f59e0b"/>
    </g>
    <text x="65" y="91" fill="#fef08a" font-size="7.5" font-weight="700">더미 범프 2배 배치 (방열 고속도로 확보)</text>

    <!-- Die 1 -->
    <rect x="25" y="96" width="270" height="22" fill="#1e3a8a" rx="2"/>
    <text x="105" y="110" fill="#93c5fd" font-size="9" font-weight="700">DRAM Core Die #1 (Base)</text>

    <!-- Mass Reflow + Injection Tag -->
    <rect x="15" y="124" width="290" height="20" fill="#047857" rx="3"/>
    <text x="25" y="138" fill="#ffffff" font-size="8.5" font-weight="800">1회 일괄 오븐 솔더링 (Mass Reflow) ➔ 액상 EMC 1회 주입</text>
  </g>

  <!-- Explanatory points MR-MUF -->
  <g transform="translate(425, 222)">
    <rect x="0" y="0" width="320" height="110" rx="6" fill="#1e293b"/>
    <text x="10" y="18" fill="#34d399" font-size="9.5" font-weight="700">■ MR-MUF의 결정적 혁신 (대체 효과)</text>
    <text x="10" y="34" fill="#38bdf8" font-size="8.5">• NCF 필름 완전 퇴출: 필름 붙이는 번거로움 삭제</text>
    <text x="10" y="50" fill="#34d399" font-size="8.5">• 열전도율 2.5배 향상: 실리카 필러 80% 고농도 충진</text>
    <text x="10" y="66" fill="#cbd5e1" font-size="8.5">• 생산성 혁명: 16단을 한 방에 굽고 액상 EMC로 한 번에 충진</text>
    <text x="10" y="82" fill="#38bdf8" font-size="8.5">• 보이드 제로 &amp; 압도적 열 방출로 HBM3E 시장 독점 달성</text>
    <text x="10" y="98" fill="#fef08a" font-size="8">• 방열 더미 범프(Dummy Bump)를 2배 이상 촘촘히 탑재 가능</text>
  </g>
</svg>"""
}

NEW_TOPIC["lecture"] = """
<h3>1. 한눈에 보는 결론: "NCF 필름 자체를 대체하고, 언더필과 외벽 몰딩을 하나로 통합한 것!"</h3>
<p>
질문하신 내용의 핵심을 명확하게 짚어드리면 다음과 같습니다:
</p>
<div style="background:#0f172a; border-left:4px solid #10b981; padding:15px; margin:16px 0; border-radius:0 8px 8px 0;">
  <strong style="color:#34d399; font-size:1.05rem;">💡 EMC는 NCF 방식에서 무엇을 대체했는가?</strong><br>
  1. <strong>NCF 고체 필름 자체를 완벽히 대체</strong>: TC-NCF에서는 층마다 빵 사이에 치즈를 끼워 넣듯 <strong>고체 필름(NCF, Non-Conductive Film)</strong>을 일일이 붙였습니다. MR-MUF에서는 이 NCF 필름을 아예 없애버리고, <strong>액체 상태의 EMC(Epoxy Molding Compound)를 층간 틈새로 한 번에 흘려 넣어 굳힘</strong>으로써 NCF 필름을 100% 대체했습니다.<br>
  2. <strong>'2개의 재료와 공정'을 '1개의 단일 재료와 공정'으로 대체</strong>:<br>
  &nbsp;&nbsp;• <strong>기존 TC-NCF</strong>: [층간 틈새: NCF 필름] + [외부 외피: 일반 EMC 몰딩] ➔ 2가지 재료, 2단계 별도 공정.<br>
  &nbsp;&nbsp;• <strong>MR-MUF</strong>: <strong>특수 고열전도 액상 EMC 딱 하나</strong>로 [층간 틈새 언더필(Underfill)]과 [외부 껍데기 몰딩(Molding)]을 동시에 원샷 해결! (그래서 이름이 <strong>Molded Underfill = MUF</strong>입니다).
</div>

<h3>2. 기존 TC-NCF의 구조와 치명적인 약점</h3>
<p>
HBM 초기와 삼성전자/마이크론이 주로 채택했던 <strong>TC-NCF(Thermal Compression Non-Conductive Film)</strong> 방식은 다음과 같이 만들어집니다:
</p>
<ol>
  <li>웨이퍼 뒷면에 두께 수 마이크로미터($\mu\text{m}$)의 <strong>고체 NCF 필름</strong>을 미리 테이프처럼 붙여서 자릅니다.</li>
  <li>DRAM 다이 1장을 올린 뒤, 위에서 히팅 헤드로 강한 열과 압력을 가합니다(<strong>Thermal Compression</strong>).</li>
  <li>NCF 필름이 순간적으로 부드러워지면서 마이크로 범프가 필름을 뚫고 지나가 아래 다이의 패드와 맞닿아 납땜(본딩)됩니다.</li>
  <li><strong>문제점</strong>: 16단 적층을 하려면 <strong>이 굽고 누르는 작업을 16번 연속으로 반복</strong>해야 합니다!</li>
</ol>

<div style="background:#1e1b4b; border:1px solid #4338ca; border-radius:8px; padding:14px; margin:15px 0;">
  <strong style="color:#a5b4fc;">⚠️ TC-NCF의 3대 한계:</strong><br>
  • <strong>방열 필러 함량의 한계</strong>: 열전도율을 높이려면 실리카($\text{SiO}_2$)나 알루미나 같은 세라믹 가루(방열 필러)를 듬뿍 넣어야 합니다. 하지만 고체 필름인 NCF에 가루를 많이 넣으면 필름이 돌덩이처럼 딱딱해져서 <strong>마이크로 범프가 필름을 뚫고 들어가지 못해 접속 불량(오픈 결함)</strong>이 납니다. 결국 필러를 조금밖에 못 넣어 열전도율이 <strong>0.2 ~ 0.4 W/(m·K)</strong> 수준으로 매우 낮습니다.<br>
  • <strong>열 충격 누적과 휨(Warpage)</strong>: 30㎛로 얇게 갈아낸 웨이퍼에 16번이나 고온·고압을 가하니 실리콘이 버티지 못하고 감자칩처럼 휘어버립니다(Warpage).<br>
  • <strong>생산 시간 병목</strong>: 한 층 한 층 정성껏 눌러줘야 하므로 패키징 장비 통과 시간이 너무 오래 걸립니다.
</div>

<h3>3. SK하이닉스가 개발한 MR-MUF의 혁신 메커니즘</h3>
<p>
SK하이닉스는 <em>"굳이 귀찮고 열도 안 빠지는 고체 필름(NCF)을 층마다 붙여가며 16번이나 눌러야 할까?"</em>라는 발상의 전환을 했습니다.
</p>

```
[MR-MUF 공정 흐름]
1. NCF 필름 없이, 범프 위에 점착제(Flux)만 살짝 발라 DRAM 16장을 탑처럼 헐렁하게 쌓아 올림.
2. 대형 리플로우 오븐에 집어넣어 한 번에 250℃로 가열 (Mass Reflow: 16개 층 전체 범프가 일괄 솔더링됨!).
3. 칩 사이사이에 빈 공간(Gap)이 뻥 뚫려 있는 상태에서 진공 챔버로 이동.
4. 나노 크기의 구형 실리카 필러가 듬뿍 들어간 '특수 액상 EMC'를 콸콸 주입 (Molded Underfill).
5. 모세관 현상과 압력으로 액상 EMC가 16층 틈새 구석구석으로 빨려 들어가 100% 빈틈없이 채워지고 외벽까지 감싸며 굳음.
```

<h3>4. NCF vs MR-MUF용 액상 EMC 심층 비교</h3>

<table style="width:100%; border-collapse:collapse; margin:15px 0; font-size:0.9rem;">
  <thead>
    <tr style="background:#1e293b; color:#38bdf8;">
      <th style="padding:10px; border:1px solid #334155;">비교 항목</th>
      <th style="padding:10px; border:1px solid #334155;">기존 TC-NCF 방식</th>
      <th style="padding:10px; border:1px solid #334155;">MR-MUF 방식 (혁신 대체)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#38bdf8;">틈새 절연 재료</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>NCF (고체 비전도성 필름)</strong></td>
      <td style="padding:10px; border:1px solid #334155;"><strong>고열전도 액상 EMC (Epoxy Molding Compound)</strong></td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#f59e0b;">열전도율 ($k$)</td>
      <td style="padding:10px; border:1px solid #334155;">약 $0.2 \sim 0.4 \text{ W/(m}\cdot\text{K)}$ (취약)</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>약 $1.5 \sim 2.5 \text{ W/(m}\cdot\text{K)}$ (2.5배 이상 우수!)</strong></td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#10b981;">방열 필러 함유율</td>
      <td style="padding:10px; border:1px solid #334155;">필름 유연성 유지 위해 소량만 배합</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>80% ~ 90% 이상 고밀도 세라믹 필러 충진 가능</strong></td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#ec4899;">본딩 공정 방식</td>
      <td style="padding:10px; border:1px solid #334155;">한 층씩 개별 열압착 (16회 반복 TC)</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>오븐에서 1회 일괄 납땜 (Mass Reflow)</strong></td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#a855f7;">재료 및 공정 수</td>
      <td style="padding:10px; border:1px solid #334155;">NCF 필름 + 별도 외벽 EMC (2원화)</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>특수 액상 EMC 1개로 언더필+몰딩 동시 완성</strong></td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#cbd5e1;">더미 범프 (방열 전용)</td>
      <td style="padding:10px; border:1px solid #334155;">범프가 필름을 뚫어야 하므로 배치 제한적</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>방열용 구리 더미 범프를 2배 이상 촘촘히 탑재</strong></td>
    </tr>
  </tbody>
</table>

<h3>5. 엔비디아가 SK하이닉스 HBM3/HBM3E를 선택한 결정적 이유</h3>
<p>
AI GPU(H100, B200)는 700W~1000W의 초고열을 뿜어냅니다.
HBM의 DRAM 셀은 온도가 85℃~105℃를 넘어가면 커패시터에 저장된 전하가 누설되어 데이터가 지워지는 리프레시(Refresh) 불량이 일어납니다.
</p>
<ul>
  <li><strong>TC-NCF의 비극</strong>: NCF 필름의 낮은 열전도도 때문에 12단, 16단 적층 시 중간 층 다이의 열이 밖으로 빠져나가지 못하고 갇혀버려 수율과 동작 속도가 급락했습니다.</li>
  <li><strong>MR-MUF의 압승</strong>: 
    1. 액상 EMC 속에 고열전도성 실리카/알루미나 필러가 빽빽하게 들어차 있어 열을 사방으로 빠르게 분산시킵니다.
    2. 필름을 뚫을 필요가 없으므로 전기 신호가 안 통하는 <strong>'순수 방열용 구리 더미 범프(Dummy Bump)'를 수만 개 더 박아 넣어 열을 아래 베이스 다이로 쏟아내리는 고속도로</strong>를 깔았습니다.
    3. 결과적으로 <strong>동작 온도를 경쟁사 대비 2.5℃~5℃ 이상 낮추고, 패키징 수율을 90% 이상으로 끌어올려</strong> 현재의 AI HBM 독점 신화를 완성했습니다.
</ul>

<h3>6. 핵심 요약 (질문에 대한 명쾌한 1줄 정리)</h3>
<blockquote style="border-left:4px solid #38bdf8; padding-left:12px; color:#e2e8f0; font-weight:600; margin:15px 0;">
"MR-MUF의 액상 EMC는 기존 TC-NCF에서 층마다 끼워 넣던 <strong>'고체 NCF 필름'을 완전히 대체</strong>한 것이며, [층간 틈새 채우기(Underfill)]와 [외벽 보호 포장(Molding)]을 단 하나의 고열전도성 액상 에폭시로 일괄 해결한 혁신 패키징 기술입니다!"
</blockquote>
"""

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 69 topics (q-69 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(69, 0, -1):
        new_n = old_n + 1
        old_str = f"{old_n:02d}"
        new_str = f"{new_n:02d}"

        # In nav-list
        html = re.sub(
            rf'<li class="nav-item"><a href="#q-{old_str}" class="nav-link"><span class="nav-num">{old_str}</span><span class="nav-text">(.*?)</span></a></li>',
            rf'<li class="nav-item"><a href="#q-{new_str}" class="nav-link"><span class="nav-num">{new_str}</span><span class="nav-text">\1</span></a></li>',
            html
        )

        # In topic-section tag
        html = re.sub(
            rf'<section class="([^"]*?)" id="q-{old_str}">',
            rf'<section class="\1" id="q-{new_str}">',
            html
        )

        # In badge
        html = re.sub(
            rf'<span class="topic-badge">Q {old_str}</span>',
            rf'<span class="topic-badge">Q {new_str}</span>',
            html
        )

    # For old Q 01 (now Q 02), remove 'latest-card-highlight' from section class
    html = re.sub(
        r'<section class="topic-section latest-card-highlight" id="q-02">',
        r'<section class="topic-section" id="q-02">',
        html
    )

    # Step 2: Build new nav-item for Q 01
    new_nav_item = f'      <li class="nav-item"><a href="#{NEW_TOPIC["id"]}" class="nav-link"><span class="nav-num">{NEW_TOPIC["num"]}</span><span class="nav-text">{NEW_TOPIC["nav_title"]}</span></a></li>\n'
    nav_list_pos = html.find('<ul class="nav-list" id="navList">')
    if nav_list_pos != -1:
        insert_nav = nav_list_pos + len('<ul class="nav-list" id="navList">\n')
        html = html[:insert_nav] + new_nav_item + html[insert_nav:]

    # Step 3: Build new section for Q 01
    summary_lis = "\n".join([f"          <li>{s}</li>" for s in NEW_TOPIC["summary"]])
    new_section_html = f"""
    <!-- Q 01 : {NEW_TOPIC['title']} -->
    <section class="topic-section latest-card-highlight" id="{NEW_TOPIC['id']}">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q 01</span>
          <span class="latest-tag">{NEW_TOPIC['badge']}</span>
          <h2 class="topic-title">{NEW_TOPIC['title']}</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">강의 핵심 요약 포인트</span>
        <ul class="summary-list">
{summary_lis}
        </ul>
      </div>
      <div class="lecture-content">
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            {NEW_TOPIC['svg_title']}
          </div>
          {NEW_TOPIC['svg']}
        </div>
        {NEW_TOPIC['lecture']}
      </div>
    </section>
"""

    main_header_end = html.find("</header>")
    if main_header_end != -1:
        insert_sec = main_header_end + len("</header>")
        html = html[:insert_sec] + "\n" + new_section_html + html[insert_sec:]

    # Step 4: Update header description
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 'MR-MUF의 EMC는 원래 NCF에서 뭘 대체한 거야? (NCF vs EMC 비교)'이 위치하며, 총 70개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 MR-MUF EMC vs NCF topic!")
