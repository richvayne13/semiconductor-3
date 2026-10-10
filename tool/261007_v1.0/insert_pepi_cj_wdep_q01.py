# -*- coding: utf-8 -*-
"""
insert_pepi_cj_wdep_q01.py
사용자 질문: "상부 p-에피층은 저농도로 접합커패시턴스억제한다는데 알고리즘이 저농도면 공핍층폭커져서 접합커패시턴스작아지는거이거맞아?"
대시보드 최상단 Q01로 신규 추가하고, 기존 71개 질문을 Q02~Q72로 시프트 (총 72개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (웨이퍼 제조 & 접합 물리)",
    "title": "상부 P- 에피층의 저농도 도핑이 접합 커패시턴스(Cj)를 낮추는 물리적 메커니즘 (Wdep 확장과 P/P+ 에피 웨이퍼)",
    "nav_title": "P- 에피층 저농도 도핑으로 Cj 낮추는 메커니즘 (Wdep 반비례)",
    "summary": [
        "<strong>질문하신 알고리즘이 100% 완벽하게 맞습니다!</strong>: <strong>[P- 에피층 저농도($N_A$ 감소) ➔ 전하 중성을 맞추기 위해 공핍층 폭 확장($W_{dep}$ 증가) ➔ 평행판 유전체 두께 증가로 접합 커패시턴스 급감($C_j$ 감소)]</strong>이라는 인과관계는 반도체 소자 물리에서 완전히 참(True)입니다.",
        "<strong>전하 중성 원리 ($W_{dep} \\propto 1/\\sqrt{N_A}$)</strong>: $N^+$ 드레인과 맞닿은 $P^-$ 에피층은 도펀트 밀도가 희박하기 때문에, $N^+$ 측의 양전하와 균형을 이루기 위해 실리콘 내부로 훨씬 더 넓고 깊은 영역까지 공핍화되어야 음전하를 채울 수 있습니다($W_{dep} \\approx \\sqrt{2\\epsilon_s V_{bi}/qN_A}$).",
        "<strong>평행판 커패시터 모델 ($C_j = \\epsilon_s / W_{dep}$)</strong>: 공핍층은 전하가 없는 부도체 절연막 역할을 합니다. 평행판 커패시터 공식($C = \\epsilon A / d$)에서 두 도체 판 사이의 간격($d = W_{dep}$)이 넓어지는 것과 동일하므로 접합 커패시턴스 $C_j$가 반비례하여 획기적으로 줄어듭니다.",
        "<strong>P/P+ 에피 웨이퍼의 존재 이유 (속도와 래치업 방지의 황금 조화)</strong>: 상부 $P^-$ 층은 저농도로 만들어 $C_j$를 극소화해 스위칭 속도($\\tau = RC_j$)를 높이고, 하부 $P^+$ 기판은 초고농도로 만들어 기판 저항($R_{sub}$)을 0으로 수렴시켜 CMOS 래치업(Latch-up)을 완벽히 박멸합니다."
    ],
    "svg_title": "📊 [P- 에피층 도핑과 접합 커패시턴스 메커니즘] 저농도 Wdep 확장과 P/P+ 에피 웨이퍼 구조",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: High Doping vs Low Doping Depletion Width & Capacitance -->
  <rect x="20" y="25" width="375" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="48" fill="#38bdf8" font-size="12" font-weight="800">1. 도핑 농도에 따른 공핍층 폭(Wdep)과 Cj의 반비례 관계</text>

  <!-- High Doping Case (Narrow Wdep, High Cj) -->
  <g transform="translate(35, 60)">
    <rect x="0" y="0" width="345" height="110" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="12" y="18" fill="#f87171" font-size="9.5" font-weight="700">❌ 고농도 기판 (N+ / P+ 접합: NA 높음)</text>

    <!-- N+ Drain -->
    <rect x="20" y="28" width="80" height="40" fill="#10b981" rx="2"/>
    <text x="35" y="52" fill="#ffffff" font-size="9" font-weight="700">N+ Drain</text>

    <!-- Narrow Depletion Layer -->
    <rect x="100" y="28" width="35" height="40" fill="#f59e0b" opacity="0.8"/>
    <text x="104" y="48" fill="#ffffff" font-size="7.5" font-weight="800">좁은 Wdep</text>
    <line x1="100" y1="72" x2="135" y2="72" stroke="#f59e0b" stroke-width="2"/>
    <text x="106" y="82" fill="#f59e0b" font-size="7.5">d 작음</text>

    <!-- P+ Substrate -->
    <rect x="135" y="28" width="190" height="40" fill="#1e3a8a" opacity="0.7"/>
    <text x="170" y="52" fill="#bfdbfe" font-size="9" font-weight="700">P+ Substrate (NA 고농도)</text>

    <text x="12" y="100" fill="#fca5a5" font-size="8">• 전하가 빽빽함 ➔ 조금만 파고들어도 중성 달성 ➔ W_dep 좁음 ➔ C_j 폭증 (속도 저하)</text>
  </g>

  <!-- Low Doping Case (Wide Wdep, Low Cj) -->
  <g transform="translate(35, 185)">
    <rect x="0" y="0" width="345" height="145" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="12" y="18" fill="#34d399" font-size="9.5" font-weight="700">✔ 저농도 에피층 (N+ / P- 접합: 질문하신 알고리즘!)</text>

    <!-- N+ Drain -->
    <rect x="20" y="28" width="80" height="40" fill="#10b981" rx="2"/>
    <text x="35" y="52" fill="#ffffff" font-size="9" font-weight="700">N+ Drain</text>

    <!-- Wide Depletion Layer -->
    <rect x="100" y="28" width="110" height="40" fill="#38bdf8" opacity="0.6"/>
    <text x="120" y="48" fill="#ffffff" font-size="8.5" font-weight="800">넓은 Wdep (공핍층 대폭 확장!)</text>
    <line x1="100" y1="72" x2="210" y2="72" stroke="#38bdf8" stroke-width="2.5"/>
    <text x="135" y="82" fill="#38bdf8" font-size="8" font-weight="700">d 대폭 증가!</text>

    <!-- P- Epi Layer -->
    <rect x="210" y="28" width="115" height="40" fill="#1e3a8a" opacity="0.4"/>
    <text x="225" y="52" fill="#93c5fd" font-size="8.5" font-weight="700">P- Epi (저농도)</text>

    <text x="12" y="103" fill="#6ee7b7" font-size="8.5" font-weight="700">★ 핵심 수식: W_dep ∝ 1/√(NA) ➔ d 증가 ➔ C_j = ε_s / W_dep 급감!</text>
    <text x="12" y="118" fill="#cbd5e1" font-size="8">• 전하가 희박하여 멀리까지 공핍화되어야 음전하 확보 ➔ 공핍층 폭 확장</text>
    <text x="12" y="132" fill="#94a3b8" font-size="7.5">• RC 지연 시간(τ = R·Cj) 단축으로 트랜지스터 스위칭 클록 비약적 상승</text>
  </g>

  <!-- Right: P/P+ Epi Wafer Cross Section -->
  <rect x="410" y="25" width="350" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
  <text x="425" y="48" fill="#f59e0b" font-size="12" font-weight="800">2. P/P+ 에피 웨이퍼(Epi Wafer)의 황금 구조</text>

  <!-- Cross section drawing -->
  <g transform="translate(425, 62)">
    <!-- Top P- Epi Layer -->
    <rect x="0" y="0" width="320" height="100" rx="4" fill="#0f2942" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="12" y="18" fill="#38bdf8" font-size="10" font-weight="800">상부 P- 에피층 (P- Epi Layer, 두께 2~5μm, 저농도)</text>

    <!-- MOSFET on Epi Layer -->
    <rect x="80" y="28" width="40" height="14" fill="#6366f1" rx="1"/>
    <text x="88" y="38" fill="#ffffff" font-size="7.5">Gate</text>
    <rect x="35" y="42" width="35" height="18" fill="#10b981" rx="1"/>
    <text x="40" y="54" fill="#ffffff" font-size="7">Source</text>
    <rect x="130" y="42" width="35" height="18" fill="#10b981" rx="1"/>
    <text x="135" y="54" fill="#ffffff" font-size="7">Drain</text>

    <!-- Deep wide depletion under drain -->
    <path d="M 130 60 Q 147 85 165 60 Z" fill="#38bdf8" opacity="0.5"/>
    <text x="180" y="55" fill="#38bdf8" font-size="8" font-weight="700">광활한 Wdep ➔ Cj 극소화!</text>

    <text x="12" y="90" fill="#93c5fd" font-size="8">• 역할: 트랜지스터 형성, Cj 최소화로 초고속 스위칭 및 항복전압(BV) 향상</text>

    <!-- Bottom P+ Substrate -->
    <rect x="0" y="108" width="320" height="110" rx="4" fill="#1e1b4b" stroke="#a855f7" stroke-width="1.5"/>
    <text x="12" y="126" fill="#c084fc" font-size="10" font-weight="800">하부 P+ 벌크 기판 (P+ Bulk Substrate, 고농도 Boron)</text>
    <text x="12" y="146" fill="#f8fafc" font-size="8.5">• <tspan fill="#fca5a5" font-weight="700">기판 저항:</tspan> R_sub 극소화 (비저항 &lt; 0.01 Ω·cm, 초전도체 수준)</text>
    <text x="12" y="162" fill="#f8fafc" font-size="8.5">• <tspan fill="#34d399" font-weight="700">래치업(Latch-up) 방멸:</tspan> 기생 BJT 베이스-에미터 전위 상승 차단</text>
    <text x="12" y="178" fill="#f8fafc" font-size="8.5">• <tspan fill="#fbbf24" font-weight="700">노이즈 흡수:</tspan> 기판 노이즈 및 알파 입자 소프트 에러(SER) 방어</text>
    <text x="12" y="196" fill="#cbd5e1" font-size="7.5">• 만약 기판 전체가 P-면? ➔ 래치업 발생으로 칩 전소!</text>
    <text x="12" y="210" fill="#cbd5e1" font-size="7.5">• 만약 기판 전체가 P+면? ➔ Cj 폭증으로 칩 속도 바닥!</text>

    <!-- Summary Box -->
    <rect x="0" y="226" width="320" height="32" rx="4" fill="#1e293b"/>
    <text x="10" y="246" fill="#38bdf8" font-size="8.5" font-weight="800">💡 결론: 상부 P-(Cj 절감/속도) + 하부 P+(래치업 방어/안정성)</text>
  </g>
</svg>"""
}

NEW_TOPIC["lecture"] = r"""
<h3>1. 결론: 질문하신 인과관계 알고리즘이 100% 완벽하게 맞습니다!</h3>
<p>
질문자께서 짚으신 논리 흐름:
</p>
<div style="text-align:center; padding:14px; background:#0f172a; border:2px solid #10b981; border-radius:8px; margin:15px 0; font-size:1.05rem; color:#34d399; font-weight:700;">
  P- 에피층 저농도 도핑 ($N_A \downarrow$)  
  $\implies$ 공핍층 폭 확장 ($W_{dep} \uparrow$)  
  $\implies$ 평행판 유전체 간격 증가로 접합 커패시턴스 급감 ($C_j \downarrow$)
</div>
<p>
이 알고리즘은 반도체 소자 물리의 핵심 원리이며, 수식적으로나 물리적으로 <strong>완전무결하게 참(True)</strong>입니다.
</p>

<h3>2. [물리적 유도 1] 왜 도핑 농도가 낮으면 공핍층 폭($W_{dep}$)이 넓어질까?</h3>
<p>
드레인 영역($N^+$)과 기판($P^-$)이 맞닿아 있는 p-n 접합을 생각해 보겠습니다.
열평형 상태나 역방향 바이어스 상태에서 p-n 접합은 반드시 <strong>'전하 중성 조건(Charge Neutrality Condition)'</strong>을 만족해야 합니다:
</p>
<div style="text-align:center; padding:10px; background:#111827; border-radius:8px; margin:12px 0; font-size:1.05rem; color:#38bdf8; font-weight:700;">
  $$Q^+ = Q^- \implies q N_D x_n = q N_A x_p$$
</div>
<ul>
  <li>$N^+$ 드레인은 도핑 농도($N_D$)가 엄청나게 높아서, 얇은 두께($x_n$)만으로도 수많은 양전하 이온($As^+$ 또는 $P^+$)이 노출됩니다.</li>
  <li>반대로 맞은편의 <strong>$P^-$ 에피층은 저농도($N_A$ 매우 작음)</strong>입니다. 붕소($B$) 원자가 듬성듬성 드물게 박혀 있습니다.</li>
  <li>$N^+$ 쪽의 막대한 양전하와 똑같은 양의 음전하($B^-$ 고정 음이온)를 맞추려면, <strong>실리콘 내부로 훨씬 더 멀리, 깊은 곳까지 전자들을 쫓아내고 영역을 넓혀야만 필요한 음전하 개수를 겨우 채울 수 있습니다!</strong></li>
</ul>

<p>
이를 푸아송 방정식(Poisson's Equation)으로 적분하여 유도한 비대칭 일방 접합($N^+/P^-$)의 공핍층 폭 공식은 다음과 같습니다:
</p>
<div style="text-align:center; padding:10px; background:#111827; border-radius:8px; margin:12px 0; font-size:1.1rem; color:#f59e0b; font-weight:700;">
  $$W_{dep} \approx x_p \approx \sqrt{\frac{2\epsilon_s (V_{bi} - V)}{q \mathbf{N_A}}} \propto \frac{1}{\sqrt{\mathbf{N_A}}}$$
</div>
<p>
보시다시피 도핑 농도 $N_A$가 분모의 제곱근에 위치하므로, <strong>도핑 농도가 낮을수록($N_A \downarrow$) 공핍층 폭은 급격하게 넓어집니다($W_{dep} \uparrow$).</strong>
</p>

<h3>3. [물리적 유도 2] 왜 공핍층 폭($W_{dep}$)이 넓어지면 접합 커패시턴스($C_j$)가 작아질까?</h3>
<p>
p-n 접합의 공핍층은 움직일 수 있는 자유 캐리어(전자, 정공)가 완전히 사라진 영역이므로, 전기적으로 완벽한 <strong>'부도체 절연막(유전체)'</strong>처럼 동작합니다.
</p>
<p>
따라서 접합 커패시턴스는 고등학교 물리 시간에 배우는 <strong>평행판 커패시터 모델</strong>과 완벽히 동일합니다:
</p>
<div style="text-align:center; padding:10px; background:#111827; border-radius:8px; margin:12px 0; font-size:1.1rem; color:#38bdf8; font-weight:700;">
  $$C = \frac{\epsilon A}{d} \iff C_j = \frac{\epsilon_s A}{\mathbf{W_{dep}}}$$
</div>
<ul>
  <li>두 도체 판 사이의 간격 $d$가 바로 <strong>공핍층 폭($W_{dep}$)</strong>에 해당합니다.</li>
  <li>공핍층 폭($W_{dep}$)이 넓어진다는 것은, <strong>두 전극 판 사이의 절연막 두께가 두꺼워지는 것</strong>과 같습니다.</li>
  <li>절연막이 두꺼워지면 양쪽 전하 간의 정전기적 인력이 약해지므로, <strong>단위 전압당 모이는 전하량(커패시턴스 $C_j$)은 당연히 반비례하여 급감</strong>하게 됩니다!</li>
</ul>

<h3>4. 이것이 반도체 칩 성능에 미치는 결정적 영향: RC 지연 단축</h3>
<p>
트랜지스터가 0에서 1로, 1에서 0으로 스위칭할 때 걸리는 지연 시간($\tau$)과 소모 전력($P$)은 다음과 같습니다:
</p>
<ol>
  <li><strong>동작 속도 폭증 (RC 지연 단축)</strong>:
    $$\tau \propto R_{channel} \times C_{total} = R_{channel} \times (C_{gate} + \mathbf{C_j})$$
    드레인 밑바닥에 깔린 기생 접합 커패시턴스 $C_j$가 줄어들면 드레인 전압을 충·방전하는 데 걸리는 시간이 단축되어 <strong>칩의 동작 주파수(Clock Frequency)가 획기적으로 상승</strong>합니다.
  </li>
  <li><strong>동적 소비 전력 절감</strong>:
    $$P_{dynamic} = \alpha \cdot \mathbf{C_j} \cdot V_{DD}^2 \cdot f$$
    스위칭할 때마다 커패시터를 채우고 비우는 충방전 전력 손실이 크게 줄어들어 발열이 개선됩니다.
  </li>
</ol>

<h3>5. 그런데 왜 기판 전체를 P-로 만들지 않고 "P/P+ 에피 웨이퍼"를 쓸까?</h3>
<p>
여기서 아주 중요한 실무적 의문이 생깁니다:  
<em>"저농도 P-가 그렇게 커패시턴스 줄이는 데 좋다면, 웨이퍼 기판 전체를 그냥 P-로 만들면 되지 왜 굳이 비싼 돈 들여 P+ 기판 위에 P- 에피층을 성장시킨 'P/P+ 에피 웨이퍼'를 쓸까요?"</em>
</p>

<div style="background:#1e1b4b; border:1px solid #4338ca; border-radius:8px; padding:15px; margin:16px 0;">
  <strong style="color:#a5b4fc; font-size:1rem;">⚠️ 기판 전체가 P-일 때 발생하는 재앙: CMOS 래치업(Latch-up)</strong><br>
  • 기판 전체를 저농도($P^-$)로 만들면, 기판의 비저항이 수십 $\Omega\cdot\text{cm}$로 너무 높아져서 <strong>기판 내부 저항($R_{sub}$)이 커집니다.</strong><br>
  • CMOS 회로 내부에는 필연적으로 기생 $p\text{-}n\text{-}p\text{-}n$ 구조(사이리스터/SCR)가 존재합니다.<br>
  • 기판에 미세한 누설 전류나 노이즈가 흐를 때 $I_{sub} \times R_{sub}$ 전압 강하가 발생하여 기생 BJT가 턴온되면, 전원($V_{DD}$)과 접지($GND$) 사이에 무한대의 단락 전류가 쏟아져 들어가는 <strong>'래치업(Latch-up)'이 발생하여 칩이 타버립니다.</strong>
</div>

<h4>[해결책: P/P+ 에피 웨이퍼의 환상적인 분업 구조]</h4>
<table style="width:100%; border-collapse:collapse; margin:15px 0; font-size:0.9rem;">
  <thead>
    <tr style="background:#1e293b; color:#38bdf8;">
      <th style="padding:10px; border:1px solid #334155;">영역</th>
      <th style="padding:10px; border:1px solid #334155;">도핑 농도</th>
      <th style="padding:10px; border:1px solid #334155;">담당하는 핵심 역할</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#38bdf8;">상부 P- 에피층 (두께 2~5㎛)</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>저농도 ($N_A \sim 10^{15}\text{ cm}^{-3}$)</strong></td>
      <td style="padding:10px; border:1px solid #334155;">트랜지스터 형성, <strong>$W_{dep}$ 확장 ➔ $C_j$ 극소화로 초고속 스위칭 달성</strong>, 항복 전압(Breakdown Voltage) 확보</td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#a855f7;">하부 P+ 벌크 기판 (두께 ~700㎛)</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>초고농도 ($N_A > 10^{18}\text{ cm}^{-3}$)</strong></td>
      <td style="padding:10px; border:1px solid #334155;"><strong>기판 저항($R_{sub}$)을 거의 0으로 단락시켜 CMOS 래치업 원천 박멸</strong>, 기판 노이즈 및 알파 입자 소프트 에러 차단</td>
    </tr>
  </tbody>
</table>

<h3>6. 핵심 요약 (1줄 정리)</h3>
<blockquote style="border-left:4px solid #38bdf8; padding-left:12px; color:#e2e8f0; font-weight:600; margin:15px 0;">
"질문하신 내용 그대로, <strong>저농도 P- 에피층은 전하 중성을 맞추기 위해 공핍층을 깊게 파고들게 하여 $W_{dep}$를 넓히고($W_{dep} \propto 1/\sqrt{N_A}$), 이는 평행판 커패시터의 유전체 두께가 두꺼워진 것과 같아 접합 커패시턴스를 획기적으로 낮추는 것($C_j = \epsilon_s/W_{dep} \downarrow$)</strong>이 100% 맞습니다!"
</blockquote>
"""

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 71 topics (q-71 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(71, 0, -1):
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
        r"최상단에는 'P- 에피층 저농도 도핑으로 Cj 낮추는 메커니즘 (Wdep 반비례)'이 위치하며, 총 72개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 P- Epi Cj Wdep topic!")
