# -*- coding: utf-8 -*-
"""
insert_usj_cj_cdep_q01.py
사용자 질문: "usj는 ldd쪽 접합깊이낮게해서 sce막는거잖아 그러면 기생cap을줄이는게 Cj를 줄이는거맞지? 설마 Cdep도 줄이는건가?"
대시보드 최상단 Q01로 신규 추가하고, 기존 68개 질문을 Q02~Q69로 시프트 (총 69개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 물리 & 커패시턴스)",
    "title": "USJ가 줄이는 기생 커패시턴스는 Cj인가 Cdep인가? (접합 커패시턴스와 채널 공핍 커패시턴스의 물리적 구분)",
    "nav_title": "USJ가 줄이는 커패시턴스는 Cj인가 Cdep인가? (접합 vs 공핍 구분)",
    "summary": [
        "<strong>핵심 결론 (Cj는 대폭 감소, Cdep는 직접 감소하지 않음)</strong>: 질문하신 내용이 정확히 맞습니다! USJ(Ultra-Shallow Junction)가 획기적으로 줄여주는 기생 커패시턴스는 <strong>S/D p-n 접합 커패시턴스 $C_j$(특히 측면 접합 성분 $C_{j,sw}$)와 게이트-드레인 오버랩 커패시턴스 $C_{ov}$</strong>이며, <strong>게이트 하부 채널 공핍 커패시턴스 $C_{dep}$는 줄이지 않습니다.</strong>",
        "<strong>Cj가 줄어드는 물리적 수식 메커니즘</strong>: S/D 접합 커패시턴스는 바닥면 성분과 측면 둘레 성분의 합($C_j = C_{j,bot} A_{bot} + C_{j,sw} P X_j$)입니다. USJ로 접합 깊이 $X_j$를 10nm 이하로 극단적으로 얕게 만들면, <strong>측면 접합 단면적($A_{side} = W \times X_j$)이 수직으로 압축되어 측면 접합 커패시턴스 $C_{j,sw}$가 급감</strong>하여 회로의 RC 지연을 획기적으로 개선합니다.",
        "<strong>Cdep가 줄어들지 않는 이유 (위치와 도핑의 차이)</strong>: $C_{dep}$는 S/D 접합부가 아니라 <strong>'게이트 절연막 바로 아래 채널 표면'에 형성되는 수직 공핍층 커패시턴스($C_{dep} = \epsilon_{si}/W_{dep,ch}$)</strong>입니다. 이는 채널 영역의 기판 도핑 농도($N_A$)에 의해 결정되는 고유 물리량이므로, 측면 S/D의 접합 깊이($X_j$)를 얕게 한다고 해서 $C_{dep}$ 자체가 줄어들지는 않습니다.",
        "<strong>전하 분할(Charge Sharing) 왜곡과의 혼동 주의</strong>: USJ가 SCE/DIBL을 억제하는 것은 $C_{dep}$를 줄여서가 아니라, 깊은 드레인 공핍층이 채널 밑바닥으로 파고들어 게이트의 전하 통제권을 빼앗는 <strong>'기생 전하 분할 면적($\Delta Q_{dep}$)'을 기하학적으로 원천 차단</strong>하기 때문입니다. (만약 $C_j$와 $C_{dep}$를 둘 다 줄이는 기술을 떠올리셨다면 그것은 벌크 USJ가 아닌 <strong>FD-SOI</strong> 기술입니다)."
    ],
    "svg_title": "📊 [USJ 소자 단면 및 기생 커패시턴스 성분 분해] 측면 접합 커패시턴스(Cj,sw) 극소화 vs 채널 공핍 커패시턴스(Cdep)",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: Deep Junction vs USJ (Cj Mechanism) -->
  <rect x="20" y="25" width="375" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="48" fill="#38bdf8" font-size="12" font-weight="800">1. S/D 접합 깊이(Xj)에 따른 Cj,sw 비교</text>

  <!-- Deep Junction (Old) -->
  <g transform="translate(35, 60)">
    <rect x="0" y="0" width="345" height="120" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="12" y="18" fill="#f87171" font-size="10.5" font-weight="700">❌ 기존 깊은 접합 (Deep Junction, Xj 큼)</text>

    <!-- Gate -->
    <rect x="135" y="25" width="75" height="15" fill="#6366f1" rx="2"/>
    <text x="155" y="36" fill="#ffffff" font-size="8.5" font-weight="700">Gate</text>
    <rect x="135" y="40" width="75" height="4" fill="#38bdf8"/>

    <!-- P-Substrate -->
    <rect x="15" y="44" width="315" height="55" fill="#1e3a8a" opacity="0.6"/>
    
    <!-- Deep N+ S/D -->
    <rect x="15" y="44" width="75" height="45" fill="#10b981" rx="2"/>
    <text x="35" y="68" fill="#ffffff" font-size="9" font-weight="700">Source (N+)</text>
    <rect x="255" y="44" width="75" height="45" fill="#10b981" rx="2"/>
    <text x="275" y="68" fill="#ffffff" font-size="9" font-weight="700">Drain (N+)</text>

    <!-- Deep Sidewall Junction Area (Huge Cj,sw) -->
    <line x1="90" y1="44" x2="90" y2="89" stroke="#f43f5e" stroke-width="3"/>
    <line x1="255" y1="44" x2="255" y2="89" stroke="#f43f5e" stroke-width="3"/>
    <text x="96" y="70" fill="#f43f5e" font-size="8" font-weight="800">깊은 Xj (측면 면적 과다)</text>
    
    <!-- Severe Depletion Penetration into channel -->
    <path d="M 255 44 Q 210 70 255 89" fill="none" stroke="#fbbf24" stroke-width="1.8" stroke-dasharray="3,2"/>
    <text x="150" y="80" fill="#fbbf24" font-size="7.5">심각한 DIBL 침범</text>

    <text x="12" y="110" fill="#fca5a5" font-size="8">• C_j,sw ∝ X_j 대폭 증가 ➔ 기생 부하 커패시턴스 폭증, 스위칭 지연 심화</text>
  </g>

  <!-- Ultra Shallow Junction (USJ) -->
  <g transform="translate(35, 190)">
    <rect x="0" y="0" width="345" height="140" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="12" y="18" fill="#34d399" font-size="10.5" font-weight="700">✔ 초얕은 접합 USJ (Ultra-Shallow Junction, Xj 극소)</text>

    <!-- Gate & Spacer -->
    <rect x="135" y="25" width="75" height="15" fill="#6366f1" rx="2"/>
    <text x="155" y="36" fill="#ffffff" font-size="8.5" font-weight="700">Gate</text>
    <rect x="135" y="40" width="75" height="4" fill="#38bdf8"/>
    <rect x="115" y="25" width="20" height="19" fill="#64748b"/>
    <rect x="210" y="25" width="20" height="19" fill="#64748b"/>

    <!-- P-Substrate -->
    <rect x="15" y="44" width="315" height="60" fill="#1e3a8a" opacity="0.6"/>

    <!-- USJ LDD Extension (Very shallow Xj < 10nm) -->
    <rect x="95" y="44" width="40" height="10" fill="#34d399" rx="1"/>
    <text x="98" y="52" fill="#064e3b" font-size="7" font-weight="800">USJ</text>
    <rect x="210" y="44" width="40" height="10" fill="#34d399" rx="1"/>
    <text x="215" y="52" fill="#064e3b" font-size="7" font-weight="800">USJ</text>

    <!-- Deep S/D away from gate -->
    <rect x="15" y="44" width="80" height="40" fill="#10b981" rx="2"/>
    <rect x="250" y="44" width="80" height="40" fill="#10b981" rx="2"/>

    <!-- Minimized Sidewall Area -->
    <line x1="135" y1="44" x2="135" y2="54" stroke="#38bdf8" stroke-width="3"/>
    <line x1="210" y1="44" x2="210" y2="54" stroke="#38bdf8" stroke-width="3"/>
    <text x="145" y="52" fill="#38bdf8" font-size="8" font-weight="800">Xj &lt; 10nm</text>

    <text x="12" y="112" fill="#6ee7b7" font-size="8.5" font-weight="700">★ C_j,sw 절감: 측면 접합 면적(W × Xj) 극소화로 기생 Cj 대폭 축소!</text>
    <text x="12" y="127" fill="#cbd5e1" font-size="8">• 측면 확산 억제로 게이트 오버랩 커패시턴스 C_ov 동반 감소</text>
  </g>

  <!-- Right: Clear Distinction between Cj and Cdep -->
  <rect x="410" y="25" width="350" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
  <text x="425" y="48" fill="#f59e0b" font-size="12" font-weight="800">2. Cj(접합 커패시턴스) vs Cdep(채널 공핍 커패시턴스)</text>

  <!-- Distinction Table / Diagram -->
  <g transform="translate(425, 62)">
    <!-- Box 1: Cj -->
    <rect x="0" y="0" width="320" height="110" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="12" y="20" fill="#38bdf8" font-size="10.5" font-weight="800">[1] 기생 접합 커패시턴스 (Cj)</text>
    <text x="12" y="38" fill="#f8fafc" font-size="9">• <tspan fill="#fca5a5" font-weight="700">위치:</tspan> Source / Drain 과 기판 사이의 p-n 접합면</text>
    <text x="12" y="54" fill="#f8fafc" font-size="9">• <tspan fill="#fca5a5" font-weight="700">공식:</tspan> C_j = C_j,bot · A_bot + <tspan fill="#38bdf8" font-weight="700">C_j,sw · (P × X_j)</tspan></text>
    <text x="12" y="70" fill="#34d399" font-size="9" font-weight="700">• USJ의 영향: 100% 직접 감소! (X_j 축소 ➔ C_j,sw 급감)</text>
    <text x="12" y="86" fill="#cbd5e1" font-size="8">• 회로 영향: 드레인 노드의 기생 RC 지연 시간(τ = R·Cj) 단축</text>
    <text x="12" y="100" fill="#94a3b8" font-size="7.5">• 드레인-게이트 오버랩 커패시턴스(C_ov)도 함께 감소</text>

    <!-- Box 2: Cdep -->
    <rect x="0" y="120" width="320" height="110" rx="6" fill="#1e293b" stroke="#fbbf24" stroke-width="1"/>
    <text x="12" y="140" fill="#fbbf24" font-size="10.5" font-weight="800">[2] 채널 공핍 커패시턴스 (Cdep)</text>
    <text x="12" y="158" fill="#f8fafc" font-size="9">• <tspan fill="#fca5a5" font-weight="700">위치:</tspan> 게이트 절연막 바로 아래 '채널(Channel) 영역'</text>
    <text x="12" y="174" fill="#f8fafc" font-size="9">• <tspan fill="#fca5a5" font-weight="700">공식:</tspan> C_dep = ε_si / W_dep,ch (채널 수직 공핍층)</text>
    <text x="12" y="190" fill="#f87171" font-size="9" font-weight="700">• USJ의 영향: 직접 감소하지 않음! (N_A가 결정)</text>
    <text x="12" y="206" fill="#cbd5e1" font-size="8">• 회로 영향: 서브스레숄드 스윙 SS ≈ 60(1 + C_dep/C_ox) 결정</text>
    <text x="12" y="220" fill="#94a3b8" font-size="7.5">• USJ는 C_dep 크기가 아니라 S/D 공핍층의 채널 침범(Charge Sharing)을 차단함</text>

    <!-- Bottom summary alert -->
    <rect x="0" y="240" width="320" height="28" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="10" y="258" fill="#34d399" font-size="8.5" font-weight="800">💡 둘 다 줄이는 기술 = 벌크 USJ가 아니라 'FD-SOI' 기술임!</text>
  </g>
</svg>"""
}

NEW_TOPIC["lecture"] = """
<h3>1. 결론: USJ가 줄이는 것은 $C_j$(접합 커패시턴스)가 100% 맞습니다!</h3>
<p>
질문하신 내용의 직관이 매우 정확합니다.
<strong>USJ(Ultra-Shallow Junction, 초얕은 접합)</strong> 공정을 도입했을 때 기생 커패시턴스가 감소하는 것은 
<strong>소스/드레인 영역의 'p-n 접합 커패시턴스($C_j$)'와 '오버랩 커패시턴스($C_{ov}$)'</strong>를 줄이는 것이 맞으며,
<strong>게이트 바로 아래 채널 영역의 '공핍 커패시턴스($C_{dep}$)' 자체를 줄이는 것은 아닙니다.</strong>
</p>

<h3>2. USJ가 $C_j$를 획기적으로 줄이는 물리적 메커니즘</h3>
<p>
트랜지스터의 소스/드레인($N^+$)과 기판($P\text{-sub}$) 사이에 형성되는 전체 접합 커패시턴스($C_j$)는 
단순히 바닥면적만으로 결정되지 않고, <strong>바닥면(Bottom) 성분과 측면 둘레(Sidewall) 성분의 합</strong>으로 정의됩니다:
</p>

<div style="text-align:center; padding:12px; background:#111827; border-radius:8px; margin:15px 0; font-size:1.05rem; color:#38bdf8; font-weight:700;">
  $$C_j = C_{j,bottom} \times A_{bottom} + C_{j,sw} \times (P_{periphery} \times X_j)$$
</div>

<ul>
  <li><strong>바닥 접합 커패시턴스 ($C_{j,bottom} \times A_{bottom}$)</strong>: 드레인 영역의 가로 $\times$ 세로 평면 바닥 면적에 비례합니다.</li>
  <li><strong>측면 접합 커패시턴스 ($C_{j,sw} \times P_{periphery} \times X_j$)</strong>: 드레인의 수직 측면 벽이 기판/채널과 맞닿는 면적에 비례합니다. 여기서 <strong>측면 단면적은 채널 폭($W$) $\times$ 접합 깊이($X_j$)</strong>입니다!</li>
</ul>

<div style="background:#0f172a; border-left:4px solid #10b981; padding:15px; margin:16px 0; border-radius:0 8px 8px 0;">
  <strong style="color:#34d399;">💡 USJ가 기생 커패시턴스를 깎아내는 2대 경로:</strong><br>
  1. <strong>측면 접합 면적의 극소화 ($C_{j,sw} \downarrow$)</strong>: 접합 깊이 $X_j$를 수십 nm에서 10nm 미만으로 초얕게 깎아내면, 드레인 측면이 기판과 마주 보는 면적이 수직으로 압축되므로 <strong>측면 기생 접합 커패시턴스($C_{j,sw}$)가 수직 낙하</strong>합니다.<br>
  2. <strong>게이트-드레인 오버랩 커패시턴스 축소 ($C_{ov} \downarrow$)</strong>: 이온주입 후 열처리 시 도펀트가 옆으로 퍼지는 측면 확산 거리($\Delta L \approx 0.7 X_j$)도 $X_j$가 얕아질수록 함께 줄어듭니다. 따라서 게이트 전극 밑으로 기어 들어오는 면적이 줄어들어 <strong>밀러 효과(Miller Effect)를 유발하는 치명적인 오버랩 커패시턴스($C_{ov}$)도 함께 격감</strong>합니다.<br>
  ➔ <strong>결과</strong>: 드레인 노드의 기생 부하 커패시턴스가 크게 줄어들어, 회로의 충방전 지연 시간($\tau = R \cdot C$)이 대폭 개선되어 <strong>칩의 동작 주파수(Clock Speed)가 대폭 상승</strong>합니다.
</div>

<h3>3. 그렇다면 왜 $C_{dep}$(채널 공핍 커패시턴스)는 줄어들지 않을까?</h3>
<p>
반도체 소자 물리에서 기호가 비슷하여 혼동하기 쉽지만, <strong>$C_j$와 $C_{dep}$는 위치와 지배 메커니즘이 완전히 다릅니다.</strong>
</p>

<table style="width:100%; border-collapse:collapse; margin:15px 0; font-size:0.9rem;">
  <thead>
    <tr style="background:#1e293b; color:#38bdf8;">
      <th style="padding:10px; border:1px solid #334155;">비교 항목</th>
      <th style="padding:10px; border:1px solid #334155;">기생 접합 커패시턴스 ($C_j$)</th>
      <th style="padding:10px; border:1px solid #334155;">채널 공핍 커패시턴스 ($C_{dep}$ 또는 $C_d$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#38bdf8;">물리적 위치</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>소스/드레인 ($N^+$) ↔ 기판 ($P$) 접합부</strong></td>
      <td style="padding:10px; border:1px solid #334155;"><strong>게이트 산화막 바로 아래 '채널(Channel)' 영역</strong></td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#f59e0b;">결정 공식</td>
      <td style="padding:10px; border:1px solid #334155;">$C_j = \frac{\epsilon_{si} A_{junction}}{W_{dep,junction}}$ ($X_j$에 직접 의존)</td>
      <td style="padding:10px; border:1px solid #334155;">$C_{dep} = \frac{\epsilon_{si}}{W_{dep,channel}} = \sqrt{\frac{q \epsilon_{si} N_A}{4 \phi_B}}$</td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#10b981;">주요 결정 인자</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>접합 깊이($X_j$)</strong>, S/D 면적, 도핑 농도 경사</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>채널 기판 도핑 농도($N_A$)</strong>, 게이트 전압</td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#ec4899;">USJ 적용 시 변화</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>직접적으로 대폭 감소 ($C_{j,sw} \downarrow$)</strong></td>
      <td style="padding:10px; border:1px solid #334155;"><strong>직접적인 변화 없음 (불변)</strong></td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#cbd5e1;">회로적 영향</td>
      <td style="padding:10px; border:1px solid #334155;">드레인 스위칭 속도 및 기생 RC 지연</td>
      <td style="padding:10px; border:1px solid #334155;">서브스레숄드 스윙 $SS = 60(1 + \frac{C_{dep}}{C_{ox}})$ 및 문턱전압</td>
    </tr>
  </tbody>
</table>

<p>
보시다시피 $C_{dep}$는 게이트 아래 채널의 수직 공핍층 두께($W_{dep,channel}$)와 채널 도핑 농도($N_A$)에 의해 결정되는 값입니다.
트랜지스터 옆구리에 있는 S/D의 접합 깊이($X_j$)를 얕게 깎는다고 해서, <strong>게이트 한가운데 채널 밑바닥의 $C_{dep}$ 수식 자체가 줄어드는 것은 물리적으로 아닙니다.</strong>
</p>

<h3>4. 왜 "USJ가 채널 쪽 공핍층을 줄인다"는 느낌이 들었을까? (전하 분할 Charge Sharing)</h3>
<p>
질문자께서 <em>"혹시 $C_{dep}$도 줄어드는 것 아닌가?"</em>라고 생각하신 데에는 아주 합리적인 소자 물리적 배경이 있습니다.
바로 <strong>'전하 분할 모델(Charge Sharing Model / Yau Model)'</strong> 때문입니다!
</p>

<div style="background:#0f172a; border-left:4px solid #f59e0b; padding:15px; margin:16px 0; border-radius:0 8px 8px 0;">
  <strong style="color:#fbbf24;">★ 전하 분할(Charge Sharing) 관점에서의 정리:</strong><br>
  • <strong>접합이 깊을 때 ($X_j$ 큼)</strong>: 드레인의 p-n 접합 공핍층이 게이트 아래 채널 밑바닥 깊숙한 곳까지 둥글게 파고들어 결합합니다. 드레인이 채널 공핍 전하($Q_{dep}$)의 상당 부분을 가로채 감당해버리므로 게이트의 지배력이 상실되고 문턱전압이 주저앉습니다($V_{th}$ roll-off, DIBL).<br>
  • <strong>USJ를 적용할 때 ($X_j$ 초얕음)</strong>: 접합이 얕기 때문에 드레인 공핍층이 채널 밑바닥으로 파고들지 못하고 표면 근처에만 얌전하게 갇힙니다.<br>
  • <strong>차이점 정리</strong>: 이것은 <strong>채널의 $C_{dep}$라는 커패시터 크기 자체를 줄인 것이 아니라, 드레인 공핍층이 채널 전하를 빼앗는 '도둑질(Charge Sharing 침범 면적)'을 물리적으로 막아낸 것</strong>입니다!
</div>

<h3>5. $C_j$와 $C_{dep}$를 "둘 다" 동시에 줄이는 기술은 무엇인가? ➔ FD-SOI</h3>
<p>
만약 <em>"어디선가 접합 커패시턴스($C_j$)도 줄이고 채널 공핍 커패시턴스($C_{dep}$)도 줄여서 성능을 극한으로 올린다"</em>는 설명을 보셨다면,
그것은 일반 벌크 실리콘의 USJ가 아니라 바로 <strong>FD-SOI (Fully Depleted Silicon-On-Insulator)</strong> 기술입니다:
</p>
<ol>
  <li><strong>$C_j$ 획기적 절감</strong>: 소스/드레인이 밑바닥의 두꺼운 절연체 산화막(BOX, $\text{SiO}_2$)에 닿아 있어 바닥면 p-n 접합 자체가 사라지므로 $C_j$가 80% 이상 소멸합니다.</li>
  <li><strong>$C_{dep} \approx 0$ 극소화</strong>: 채널 실리콘 두께가 6~10nm로 극도로 얇아 채널 전체가 게이트 전압에 의해 완전히 공핍화(Fully Depleted)되고, 그 밑에 유전율이 낮은 BOX 산화막이 직렬로 연결되어 채널 공핍 커패시턴스가 거의 0에 수렴합니다 ($C_{dep} \to 0$).</li>
  <li><strong>결과</strong>: $SS = 60 \left(1 + \frac{C_{dep}}{C_{ox}}\right) \approx \mathbf{60\text{ mV/dec}}$라는 이상적인 스위칭 특성을 달성합니다.</li>
</ol>

<h3>6. 핵심 한 줄 요약</h3>
<blockquote style="border-left:4px solid #38bdf8; padding-left:12px; color:#e2e8f0; font-weight:600; margin:15px 0;">
"USJ(Ultra-Shallow Junction)는 드레인 측면 단면적($W \times X_j$)을 극소화하여 <strong>기생 접합 커패시턴스 $C_j$(특히 측면 $C_{j,sw}$)와 게이트 오버랩 커패시턴스 $C_{ov}$를 줄이는 기술</strong>이 100% 맞으며, 게이트 하부 채널의 <strong>공핍 커패시턴스 $C_{dep}$ 자체를 줄이지는 않는다!</strong> (단, S/D 공핍층이 채널을 침범하는 Charge Sharing은 원천 봉쇄함)"
</blockquote>
"""

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 68 topics (q-68 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(68, 0, -1):
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
        r"최상단에는 'USJ가 줄이는 커패시턴스는 Cj인가 Cdep인가? (접합 vs 공핍 구분)'이 위치하며, 총 69개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 USJ Cj vs Cdep topic!")
