# -*- coding: utf-8 -*-
"""
insert_ionized_impurity_scattering_q01.py
사용자 질문: "고농도에서는 이온화불순물산란으로 이동도저하돼 저항감소율둔화됨 여기서 이온화불순물산란이 뭔지"
대시보드 최상단 Q01로 신규 추가하고, 기존 74개 질문을 Q02~Q75로 시프트 (총 75개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (반도체 물리 & 전송 현상)",
    "title": "이온화 불순물 산란(Ionized Impurity Scattering)이란 무엇인가? (쿨롱 정전기 편향과 저항 감소율 둔화 메커니즘)",
    "nav_title": "이온화 불순물 산란이란 무엇인가? (쿨롱 편향과 이동도 저하)",
    "summary": [
        "<strong>이온화 불순물 산란(Ionized Impurity Scattering)의 직관적 정의</strong>: 실리콘 격자에 주입된 도펀트가 상온에서 전자를 내놓고 스스로 <strong>고정된 전하 이온($P^+, As^+, B^-$)</strong>으로 변한 뒤, 그 곁을 지나가는 <strong>자유 전자나 정공을 쿨롱 정전기력(인력/척력)으로 잡아당기거나 밀쳐내어 궤적을 꺾어버리는 산란 현상</strong>입니다 (자석 도로 비유).",
        "<strong>미시적 이동도 저하 메커니즘 ($\\mu = q\\tau / m^*$)</strong>: 도핑 농도($N_I$)가 높아질수록 격자 내에 정전기 자석(이온)의 밀도가 빽빽해져 캐리어가 직진하지 못하고 지그재그로 튕겨 나갑니다. 충돌 사이의 평균 자유 비행 시간($\\tau$)이 급감하므로 <strong>이동도($\\mu$)가 수직 낙하</strong>합니다 (브룩스-헤링 공식: $\\mu_{ii} \\propto T^{3/2} / N_I$).",
        "<strong>'저항 감소율 둔화'가 발생하는 결정적 이유</strong>: 전도도는 $\\sigma = q \\cdot N \\cdot \\mu$입니다. 도핑 농도($N$)를 10배 올리면 캐리어 개수는 10배 늘어나지만, 이온화 불순물 산란 때문에 이동도($\\mu$)가 1/3로 깎여버립니다. 따라서 전도도 상승폭이 둔화되어 <strong>도핑을 아무리 쏟아부어도 저항이 기대만큼 떨어지지 않는 포화 현상(Irvin Curve 굴절)</strong>이 발생합니다.",
        "<strong>반도체 공학의 대책 (살리사이드와 무도핑 채널)</strong>: 초고농도 도핑의 저항 감소 한계를 극복하기 위해 소스/드레인 표면에 금속 화합물인 <strong>살리사이드(Salicide)</strong>를 형성하여 접촉 저항을 낮추며, 첨단 FinFET과 GAA에서는 채널에 도핑을 전혀 하지 않는 <strong>무도핑 채널(Undoped Channel)</strong>을 채택하여 이동도를 보존합니다."
    ],
    "svg_title": "📊 [이온화 불순물 산란 메커니즘 & 저항 둔화 곡선] 쿨롱 정전기 궤적 굴절과 도핑 농도에 따른 이동도 포화",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: Coulomb Deflection Mechanism (Microscopic) -->
  <rect x="20" y="25" width="375" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="48" fill="#38bdf8" font-size="12" font-weight="800">1. 미시적 메커니즘: 쿨롱 전계에 의한 전자의 궤적 굴절</text>

  <g transform="translate(35, 60)">
    <!-- Case 1: Low Doping (Far apart, straight line) -->
    <rect x="0" y="0" width="345" height="115" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="12" y="18" fill="#34d399" font-size="9.5" font-weight="700">✔ 저농도 도핑: 이온 간격 넓음 ➔ 산란 적음 (고이동도)</text>

    <!-- Fixed Ion -->
    <circle cx="170" cy="45" r="12" fill="#1e3a8a" stroke="#38bdf8" stroke-width="2"/>
    <text x="162" y="49" fill="#ffffff" font-size="11" font-weight="800">P⁺</text>
    <text x="188" y="48" fill="#93c5fd" font-size="7.5">고정 도너 양이온</text>

    <!-- Straight Electron Trajectory -->
    <line x1="20" y1="85" x2="310" y2="85" stroke="#34d399" stroke-width="2.5"/>
    <circle cx="40" cy="85" r="4" fill="#fbbf24"/>
    <text x="35" y="76" fill="#fbbf24" font-size="8">e⁻</text>
    <text x="120" y="102" fill="#cbd5e1" font-size="8">이온과 거리가 멀어 굴절 없이 고속 직진 (τ 긺)</text>
  </g>

  <!-- Case 2: High Doping (Ionized Impurity Scattering) -->
  <g transform="translate(35, 185)">
    <rect x="0" y="0" width="345" height="145" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="12" y="18" fill="#f87171" font-size="9.5" font-weight="700">❌ 고농도 도핑: 빽빽한 이온 ➔ 쿨롱 인력/척력 산란 폭증!</text>

    <!-- Dense Ions -->
    <circle cx="70" cy="50" r="10" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="64" y="54" fill="#ffffff" font-size="9" font-weight="800">P⁺</text>

    <circle cx="160" cy="70" r="10" fill="#831843" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="154" y="74" fill="#ffffff" font-size="9" font-weight="800">B⁻</text>

    <circle cx="250" cy="45" r="10" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="244" y="49" fill="#ffffff" font-size="9" font-weight="800">P⁺</text>

    <!-- Deflected Trajectory -->
    <path d="M 20 40 Q 60 38 85 60 Q 120 90 140 75 Q 160 55 180 80 Q 220 100 240 60 Q 260 25 310 30" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="4,2"/>
    <text x="12" y="112" fill="#fca5a5" font-size="8.5" font-weight="700">★ 쿨롱 산란: 정전기력에 의해 진행 궤적이 심하게 꺾임!</text>
    <text x="12" y="126" fill="#cbd5e1" font-size="8">• 평균 자유 시간 τ 급감 ➔ 이동도 μ = qτ/m* 대폭 저하</text>
    <text x="12" y="138" fill="#94a3b8" font-size="7.5">• 브룩스-헤링(Brooks-Herring) 이론: μ_ii ∝ T^(3/2) / N_I</text>
  </g>

  <!-- Right: Why Resistance Reduction Rate Slows Down (Irvin Curve) -->
  <rect x="410" y="25" width="350" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
  <text x="425" y="48" fill="#f59e0b" font-size="12" font-weight="800">2. 도핑 농도 증가 시 '저항 감소율 둔화'의 원리</text>

  <!-- Mathematical Trade-off Box -->
  <g transform="translate(425, 62)">
    <rect x="0" y="0" width="320" height="110" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="12" y="20" fill="#38bdf8" font-size="10.5" font-weight="800">■ 전도도(Conductivity) 수식 분해</text>
    
    <text x="12" y="42" fill="#f8fafc" font-size="11" font-weight="800">σ = q · <tspan fill="#34d399">N (캐리어 밀도 ↑)</tspan> · <tspan fill="#ef4444">μ (이동도 ↓)</tspan></text>
    
    <text x="12" y="65" fill="#cbd5e1" font-size="8.5">• <tspan fill="#34d399" font-weight="700">도핑 10배 증가 시:</tspan> 운반체 N은 10배 증가 (+)</text>
    <text x="12" y="82" fill="#cbd5e1" font-size="8.5">• <tspan fill="#ef4444" font-weight="700">이온화 산란 폭증:</tspan> 이동도 μ는 1/3로 급락 (-)</text>
    <text x="12" y="99" fill="#fbbf24" font-size="8.5" font-weight="700">➔ 전도도는 10배가 아니라 3.3배밖에 안 늘어남! (둔화)</text>
  </g>

  <!-- Graph representation (Irvin Curve) -->
  <g transform="translate(425, 185)">
    <rect x="0" y="0" width="320" height="145" rx="6" fill="#1e293b"/>
    <text x="10" y="18" fill="#f59e0b" font-size="9.5" font-weight="800">■ 어빈 곡선(Irvin Curve)의 저항 포화 현상</text>

    <!-- Axes -->
    <line x1="30" y1="110" x2="290" y2="110" stroke="#64748b" stroke-width="1.5"/>
    <line x1="30" y1="110" x2="30" y2="30" stroke="#64748b" stroke-width="1.5"/>
    <text x="210" y="122" fill="#94a3b8" font-size="7.5">도핑 농도 (N) ➔</text>
    <text x="10" y="28" fill="#94a3b8" font-size="7.5">저항 (ρ)</text>

    <!-- Ideal linear curve (dash) -->
    <path d="M 35 35 Q 90 60 280 108" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,2"/>
    <text x="180" y="85" fill="#64748b" font-size="7">이상적 감소 (μ 일정)</text>

    <!-- Actual curve (saturation) -->
    <path d="M 35 35 Q 90 70 280 92" fill="none" stroke="#ef4444" stroke-width="2.5"/>
    <text x="160" y="70" fill="#f87171" font-size="8" font-weight="700">실제 곡선: 감소율 둔화 (포화!)</text>

    <text x="10" y="136" fill="#38bdf8" font-size="8">• 10²⁰ cm⁻³ 이상 축퇴 도핑 시 저항이 거의 안 줄어듦 ➔ Salicide 필수!</text>
  </g>
</svg>"""
}

NEW_TOPIC["lecture"] = r"""
<h3>1. 이온화 불순물 산란의 직관적 정의: '자석들이 빽빽하게 깔린 도로'</h3>
<p>
<strong>이온화 불순물 산란(Ionized Impurity Scattering)</strong>이란, 
반도체 격자 내에 주입된 불순물(도펀트)이 상온에서 전자를 내놓거나 받아들여 <strong>전기적 양이온($P^+, As^+$)이나 음이온($B^-$)으로 변한 뒤</strong>, 
그 곁을 전속력으로 지나가는 <strong>자유 전자나 정공을 쿨롱 정전기력(인력/척력)으로 잡아당기거나 밀쳐내어 궤적을 사방으로 꺾어버리는 충돌 현상</strong>입니다.
</p>
<div style="background:#0f172a; border-left:4px solid #38bdf8; padding:15px; margin:16px 0; border-radius:0 8px 8px 0;">
  <strong style="color:#38bdf8; font-size:1.05rem;">💡 쇠구슬과 자석 도로 비유:</strong><br>
  • <strong>저농도 반도체</strong>: 넓은 도로에 자석이 100m마다 하나씩 듬성듬성 놓여 있습니다. 쇠구슬(전자)을 굴리면 자석의 방해를 거의 받지 않고 시원하게 직진합니다 (<strong>높은 이동도 $\mu$</strong>).<br>
  • <strong>고농도 반도체</strong>: 도로 바닥에 강력한 자석(이온)들이 10cm 간격으로 빽빽하게 깔려 있습니다. 쇠구슬을 굴리면 지나갈 때마다 자석들이 끌어당기고 밀어내어 <strong>쇠구슬이 지그재그로 휘청거리며 속도가 급격히 감속</strong>됩니다 (<strong>이동도 $\mu$ 급락!</strong>).
</div>

<h3>2. 왜 불순물이 '이온화'되어 있을까? (완전 이온화와 쿨롱 힘)</h3>
<p>
실리콘에 5족 원소인 인(Phosphorus, $P$)이나 비소(Arsenic, $As$)를 넣으면:
</p>
<ol>
  <li>5개의 최외각 전자 중 4개는 주변 실리콘과 공유 결합을 맺고, <strong>남은 1개의 자유 전자를 실리콘 밴드로 방출</strong>합니다.</li>
  <li>전자를 잃어버린 도너 원자 자신은 <strong>양전하를 띤 고정 양이온($P^+$ 또는 $As^+$)</strong>이 됩니다.</li>
  <li>상온(300K)에서는 열에너지가 충분하여 주입된 도펀트의 거의 100%가 전자를 방출한 <strong>'완전 이온화(Complete Ionization)'</strong> 상태로 격자 속에 박혀 있습니다.</li>
</ol>
<p>
마찬가지로 3족 붕소(Boron, $B$)는 전자를 받아들여 <strong>고정 음이온($B^-$)</strong>이 되고 자유 정공(Hole)을 만듭니다.
즉, <strong>도핑 농도를 올린다는 것은 실리콘 격자 속에 고정된 전하 덩어리(이온)들을 빽빽하게 채워 넣는다는 뜻</strong>입니다.
</p>

<h3>3. 러더퍼드 산란(Rutherford Scattering)과 이동도 공식</h3>
<p>
움직이는 자유 전자가 고정된 양이온($P^+$) 근처를 스쳐 지나갈 때, 서로 반대 전하이므로 강력한 **쿨롱 인력(Coulomb Attraction)**을 받습니다.
반대로 음이온($B^-$) 근처를 지날 때는 같은 음전하이므로 **쿨롱 척력(Coulomb Repulsion)**을 받습니다.
</p>
<p>
원자핵에 알파 입자가 산란되는 <strong>러더퍼드 산란(Rutherford Scattering)</strong>과 똑같은 원리로, 전자는 직접 원자에 물리적으로 쾅 부딪히지 않더라도 <strong>전기력에 의해 진행 궤적이 크게 꺾여버립니다(Deflection).</strong>
</p>

<h4>[브룩스-헤링(Brooks-Herring) 이동도 공식]</h4>
<div style="text-align:center; padding:12px; background:#111827; border-radius:8px; margin:15px 0; font-size:1.1rem; color:#f59e0b; font-weight:700;">
  $$\mu_{ii} \propto \frac{T^{3/2}}{N_I}$$
</div>
<ul>
  <li><strong>이온 농도($N_I$)에 반비례</strong>: 도핑 농도($N_I$)가 높아질수록 충돌 중심(Scattering Center)의 밀도가 높아져, 충돌 사이의 평균 시간($\tau$)이 급감하여 <strong>이동도($\mu = q\tau/m^*$)가 급격하게 떨어집니다.</strong></li>
  <li><strong>온도($T^{3/2}$)에 비례</strong>: 온도가 올라가면 전자의 열 운동 속도($v_{th} \propto \sqrt{T}$)가 빨라집니다. 전자가 이온 옆을 쏜살같이 빠르게 스쳐 지나가므로, 쿨롱 힘을 받아 궤적이 휠 틈이 줄어들어 고온일수록 이온화 산란의 영향은 오히려 줄어듭니다.</li>
</ul>

<h3>4. 왜 "저항 감소율이 둔화"되는가? (어빈 곡선 Irvin Curve의 비밀)</h3>
<p>
반도체의 전도도($\sigma$)와 비저항($\rho$) 수식을 보면 의문이 완벽하게 풀립니다:
</p>
<div style="text-align:center; padding:12px; background:#111827; border-radius:8px; margin:15px 0; font-size:1.15rem; color:#38bdf8; font-weight:700;">
  $$\sigma = q \cdot \mathbf{N} \cdot \mathbf{\mu} \implies \rho = \frac{1}{\sigma} = \frac{1}{q \cdot \mathbf{N} \cdot \mathbf{\mu}}$$
</div>

<div style="background:#1e1b4b; border:1px solid #4338ca; border-radius:8px; padding:15px; margin:16px 0;">
  <strong style="color:#a5b4fc; font-size:1rem;">⚠️ 이상과 현실의 충돌 (저항 둔화 메커니즘):</strong><br>
  • <strong>이상적인 생각</strong>: 도핑 농도($N$)를 10배 올리면, 캐리어 개수가 10배 많아지니까 전도도($\sigma$)도 10배 커지고 저항($\rho$)은 1/10로 정직하게 떨어질 것이다!<br>
  • <strong>물리적 현실</strong>: 도핑 농도($N$)를 10배 올리면 캐리어는 10배 늘어나지만, <strong>이온화 불순물 산란이 폭증하여 이동도($\mu$)가 1/3 수준으로 반토막</strong> 납니다.<br>
  • <strong>결과</strong>:
    $$\sigma_{new} = q \times (10 \times N) \times \left(\frac{1}{3} \times \mu\right) \approx \mathbf{3.3 \times \sigma_{old}}$$
    저항이 1/10로 줄어들기를 기대했는데, 실제로는 1/3.3밖에 안 줄어듭니다!
</div>

<p>
이로 인해 도핑 농도가 $10^{19}\text{ cm}^{-3}$을 넘어 $10^{20}\text{ cm}^{-3}$에 가까워지면, <strong>도핑을 아무리 더 때려 박아도 저항이 거의 줄어들지 않고 평평하게 누워버리는 포화 현상(Saturation)</strong>이 일어납니다. 이 실제 도핑 농도와 저항의 비선형 관계를 그래프로 그린 것이 바로 유명한 <strong>어빈 곡선(Irvin Curve)</strong>입니다.
</p>

<h3>5. 반도체 산업의 실제 해결책: 살리사이드(Salicide)</h3>
<p>
소스/드레인 접촉 저항을 낮추려고 무작정 이온주입 도즈량을 무한정 늘릴 수 없는 이유가 바로 이 <strong>'이온화 불순물 산란에 의한 이동도 저하 및 저항 감소율 둔화'</strong> 때문입니다.
</p>
<ul>
  <li>도핑 농도를 $10^{20}\text{ cm}^{-3}$ 이상으로 올려봤자 저항은 더 이상 안 떨어지고, 오히려 결정 격자만 깨지고 접합 누설전류(Junction Leakage)만 커집니다.</li>
  <li><strong>해결책</strong>: 실리콘 표면에 니켈(Ni)이나 코발트(Co) 금속을 증착하고 열처리하여 금속-실리콘 화합물인 <strong>살리사이드(Salicide, NiSi)</strong>를 얇게 형성합니다.</li>
  <li>살리사이드는 실리콘이 아니라 금속성 도체이므로 이온화 산란의 한계를 뛰어넘어 <strong>면저항을 수 $\Omega/\text{sq}$ 이하로 수직 낙하</strong>시킬 수 있습니다.</li>
</ul>

<h3>6. 최종 요약 (1줄 정리)</h3>
<blockquote style="border-left:4px solid #38bdf8; padding-left:12px; color:#e2e8f0; font-weight:600; margin:15px 0;">
"<strong>이온화 불순물 산란</strong>은 도핑된 이온($P^+, B^-$)의 <strong>쿨롱 정전기력에 의해 전자의 진행 궤적이 이리저리 휘어지며 이동도($\mu$)가 급락하는 현상</strong>이며, 이로 인해 도핑 농도($N$)를 올려도 $\sigma = q N \mu$에서 $\mu$가 깎여나가 <strong>저항 감소율이 둔화(어빈 곡선 포화)</strong>되는 것입니다!"
</blockquote>
"""

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 74 topics (q-74 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(74, 0, -1):
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
        r"최상단에는 '이온화 불순물 산란이란 무엇인가? (쿨롱 편향과 이동도 저하)'이 위치하며, 총 75개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Ionized Impurity Scattering topic!")
