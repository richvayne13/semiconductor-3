# -*- coding: utf-8 -*-
"""
insert_sheet_resistance_carrier_q01.py
사용자 질문: "면저항은 도핑농도가 커지면 캐리어밀도가 커져 감소한다는데 여기서 도핑농도는 p기판의도핑농도고 캐리어밀도도 p야?"
대시보드 최상단 Q01로 신규 추가하고, 기존 72개 질문을 Q02~Q73으로 시프트 (총 73개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 물리 & 저항 기초)",
    "title": "면저항 공식에서 도핑농도와 캐리어밀도는 P기판과 정공(p)을 말하는 것일까? (P형 vs N형 영역별 물리적 실체)",
    "nav_title": "면저항의 도핑농도와 캐리어밀도는 P기판과 정공(p)을 뜻할까?",
    "summary": [
        "<strong>P형 기판을 다룰 때는 질문하신 내용이 100% 맞습니다!</strong>: 웨이퍼 기판(P-Substrate)이나 P형 에피층의 면저항을 이야기할 때, <strong>도핑농도는 P형 억셉터 농도($N_A$, 붕소)이고 캐리어 밀도도 정공(Hole)의 밀도 $p$</strong>를 뜻하는 것이 정확히 맞습니다 ($p \\approx N_A$).",
        "<strong>면저항 공식은 P형과 N형 모두에 적용되는 보편 법칙</strong>: 면저항 공식($R_s = 1 / q \\cdot \\text{캐리어밀도} \\cdot \\mu \\cdot t$)은 특정 영역에 국한되지 않는 일반 물리 법칙입니다. <strong>'내가 지금 저항을 측정하고자 하는 바로 그 영역의 다수 캐리어'</strong>가 공식의 주인공이 됩니다.",
        "<strong>N형 영역(예: NMOS 드레인/소스 N+)에서는 전자($n$)</strong>: 만약 NMOS 트랜지스터의 소스/드레인($N^+$) 면저항을 잰다면, 도핑농도는 도너 농도($N_D$, 비소/인)가 되고 <strong>캐리어 밀도는 전자 밀도 $n$</strong>이 됩니다 ($n \\approx N_D$, $R_s = 1 / q N_D \\mu_n t$).",
        "<strong>완전 이온화(Complete Ionization)의 전제</strong>: 상온(~300K)에서는 주입된 불순물 원자가 100% 열에너지로 이온화되므로, P형에서는 [억셉터 도핑농도 $N_A$ = 정공 밀도 $p$], N형에서는 [도너 도핑농도 $N_D$ = 전자 밀도 $n$]이라는 1:1 대응 관계가 완벽히 성립합니다."
    ],
    "svg_title": "📊 [P형 vs N형 반도체의 면저항과 캐리어 대응 관계] 전도 메커니즘과 MOSFET 소자 내 영역별 캐리어 구분",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: P-type vs N-type Carrier & Doping Mapping -->
  <rect x="20" y="25" width="375" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="48" fill="#38bdf8" font-size="12" font-weight="800">1. P형 vs N형: 도핑 농도와 캐리어 밀도 매핑</text>

  <!-- P-type Box -->
  <g transform="translate(35, 60)">
    <rect x="0" y="0" width="345" height="120" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="12" y="18" fill="#38bdf8" font-size="10.5" font-weight="800">[1] P형 영역 (P-기판, P-에피, P+ 소스/드레인)</text>
    
    <text x="12" y="38" fill="#f8fafc" font-size="9">• <tspan fill="#fbbf24" font-weight="700">도핑 불순물:</tspan> 3족 원소 억셉터 (Acceptor, 붕소 B)</text>
    <text x="12" y="54" fill="#f8fafc" font-size="9">• <tspan fill="#fbbf24" font-weight="700">도핑 농도:</tspan> <tspan fill="#34d399" font-weight="700">NA [cm⁻³]</tspan> (Acceptor Concentration)</text>
    <text x="12" y="70" fill="#f8fafc" font-size="9">• <tspan fill="#fbbf24" font-weight="700">주요 캐리어:</tspan> <tspan fill="#38bdf8" font-weight="700">정공 (Hole, p)</tspan> ➔ 완전 이온화 시 <tspan fill="#34d399" font-weight="800">p ≈ NA</tspan></text>
    <text x="12" y="86" fill="#cbd5e1" font-size="8.5">• 전도도 수식: σ_p = q · p · μ_p ≈ q · NA · μ_p</text>
    <text x="12" y="104" fill="#38bdf8" font-size="9" font-weight="700">★ 면저항: R_s = 1 / (q · NA · μ_p · t) [Ω/sq]</text>
  </g>

  <!-- N-type Box -->
  <g transform="translate(35, 190)">
    <rect x="0" y="0" width="345" height="140" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="12" y="18" fill="#34d399" font-size="10.5" font-weight="800">[2] N형 영역 (NMOS N+ 드레인/소스, N-Well)</text>

    <text x="12" y="38" fill="#f8fafc" font-size="9">• <tspan fill="#fbbf24" font-weight="700">도핑 불순물:</tspan> 5족 원소 도너 (Donor, 인 P, 비소 As)</text>
    <text x="12" y="54" fill="#f8fafc" font-size="9">• <tspan fill="#fbbf24" font-weight="700">도핑 농도:</tspan> <tspan fill="#34d399" font-weight="700">ND [cm⁻³]</tspan> (Donor Concentration)</text>
    <text x="12" y="70" fill="#f8fafc" font-size="9">• <tspan fill="#fbbf24" font-weight="700">주요 캐리어:</tspan> <tspan fill="#10b981" font-weight="700">전자 (Electron, n)</tspan> ➔ 완전 이온화 시 <tspan fill="#34d399" font-weight="800">n ≈ ND</tspan></text>
    <text x="12" y="86" fill="#cbd5e1" font-size="8.5">• 전도도 수식: σ_n = q · n · μ_n ≈ q · ND · μ_n</text>
    <text x="12" y="104" fill="#10b981" font-size="9" font-weight="700">★ 면저항: R_s = 1 / (q · ND · μ_n · t) [Ω/sq]</text>
    <text x="12" y="124" fill="#94a3b8" font-size="7.5">※ 전자의 이동도(μ_n)가 정공(μ_p)보다 약 2.5~3배 커서 동일 농도 시 N형 R_s가 더 낮음</text>
  </g>

  <!-- Right: Real MOSFET Structure showing Where Rs is measured -->
  <rect x="410" y="25" width="350" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
  <text x="425" y="48" fill="#f59e0b" font-size="12" font-weight="800">2. 실제 반도체 소자 내 영역별 캐리어와 면저항</text>

  <!-- Diagram of MOSFET Regions -->
  <g transform="translate(425, 62)">
    <!-- Gate -->
    <rect x="95" y="10" width="80" height="18" fill="#6366f1" rx="2"/>
    <text x="100" y="23" fill="#ffffff" font-size="8">N+ Poly Gate (n, ND)</text>
    <rect x="95" y="28" width="80" height="4" fill="#38bdf8"/>

    <!-- P-Substrate Background -->
    <rect x="0" y="32" width="320" height="110" rx="3" fill="#1e3a8a" opacity="0.6"/>
    <text x="20" y="125" fill="#93c5fd" font-size="9" font-weight="800">P-기판 (P-Substrate: 캐리어 = 정공 p, 도핑 = NA)</text>

    <!-- N+ Source & Drain -->
    <rect x="15" y="32" width="65" height="32" fill="#10b981" rx="2"/>
    <text x="25" y="52" fill="#ffffff" font-size="8.5" font-weight="700">N+ Source</text>
    <text x="20" y="74" fill="#6ee7b7" font-size="7.5">캐리어: 전자(n)</text>
    <text x="20" y="86" fill="#fef08a" font-size="7">도핑: ND (비소)</text>

    <!-- N+ Drain -->
    <rect x="190" y="32" width="65" height="32" fill="#10b981" rx="2"/>
    <text x="205" y="52" fill="#ffffff" font-size="8.5" font-weight="700">N+ Drain</text>
    <text x="195" y="74" fill="#6ee7b7" font-size="7.5">캐리어: 전자(n)</text>
    <text x="195" y="86" fill="#fef08a" font-size="7">도핑: ND (비소)</text>

    <!-- Channel Depletion -->
    <rect x="95" y="32" width="80" height="15" fill="#f59e0b" opacity="0.3"/>
    <text x="110" y="44" fill="#fde68a" font-size="7.5">반전층 채널</text>

    <!-- Explanatory Table Box -->
    <rect x="0" y="150" width="320" height="100" rx="4" fill="#1e293b"/>
    <text x="10" y="168" fill="#38bdf8" font-size="9" font-weight="800">■ 실무 핵심 정리: "내가 어디를 재는가?"</text>
    <text x="10" y="185" fill="#cbd5e1" font-size="8.5">• <tspan fill="#93c5fd" font-weight="700">기판 저항 잴 때:</tspan> 도핑은 붕소(NA), 캐리어는 <tspan fill="#38bdf8" font-weight="700">정공(p)</tspan> (질문 맞음!)</text>
    <text x="10" y="202" fill="#cbd5e1" font-size="8.5">• <tspan fill="#6ee7b7" font-weight="700">S/D 저항 잴 때:</tspan> 도핑은 인/비소(ND), 캐리어는 <tspan fill="#10b981" font-weight="700">전자(n)</tspan></text>
    <text x="10" y="219" fill="#cbd5e1" font-size="8.5">• <tspan fill="#fca5a5" font-weight="700">PMOS S/D 잴 때:</tspan> 도핑은 붕소(NA), 캐리어는 <tspan fill="#38bdf8" font-weight="700">정공(p)</tspan></text>
    <text x="10" y="236" fill="#fbbf24" font-size="8.5">• 결론: "면저항 공식의 캐리어는 측정 대상 영역에 따라 달라진다!"</text>
  </g>
</svg>"""
}

NEW_TOPIC["lecture"] = r"""
<h3>1. 결론부터 명쾌하게: "질문하신 상황에서는 100% 맞고, 대상에 따라 달라집니다!"</h3>
<p>
질문하신 두 가지 물음에 대해 정확한 팩트를 정리해 드리면 다음과 같습니다:
</p>
<div style="background:#0f172a; border-left:4px solid #10b981; padding:15px; margin:16px 0; border-radius:0 8px 8px 0;">
  <strong style="color:#34d399; font-size:1.05rem;">💡 질문에 대한 직접적 답변:</strong><br>
  1. <strong>"도핑농도는 P기판의 도핑농도인가요?"</strong><br>
  &nbsp;&nbsp;👉 <strong>P형 웨이퍼 기판의 면저항을 잴 때는 $N_A$(억셉터 도핑농도)가 맞습니다!</strong> 하지만 만약 NMOS의 소스/드레인($N^+$) 영역의 면저항을 잴 때는 도너 도핑농도($N_D$)가 됩니다. 즉, <strong>"내가 지금 저항을 측정하고자 하는 바로 그 영역의 불순물 농도"</strong>를 뜻합니다.<br><br>
  2. <strong>"캐리어 밀도도 정공(p)인가요?"</strong><br>
  &nbsp;&nbsp;👉 <strong>네, P형 영역에서는 캐리어 밀도가 100% 정공($p$)이 맞습니다!</strong> ($p \approx N_A$). 반대로 N형 영역에서는 캐리어 밀도가 <strong>전자($n$)</strong>가 됩니다 ($n \approx N_D$).
</div>

<h3>2. 면저항의 미시적 물리 수식: 옴의 법칙에서 출발</h3>
<p>
면저항($R_s$)은 추상적인 공식이 아니라, 물질 고유의 <strong>비저항($\rho$)</strong>을 박막의 <strong>두께($t$)</strong>로 나눈 값입니다:
</p>
<div style="text-align:center; padding:12px; background:#111827; border-radius:8px; margin:15px 0; font-size:1.1rem; color:#38bdf8; font-weight:700;">
  $$R_s = \frac{\rho}{t} = \frac{1}{\sigma \cdot t}$$
</div>
<p>
여기서 물질이 전기를 얼마나 잘 통과시키는가를 나타내는 <strong>전도도($\sigma$, Conductivity)</strong>의 일반식은 다음과 같습니다:
</p>
<div style="text-align:center; padding:10px; background:#111827; border-radius:8px; margin:12px 0; font-size:1.05rem; color:#f59e0b; font-weight:700;">
  $$\sigma = q \cdot (n \cdot \mu_n + p \cdot \mu_p)$$
</div>
<ul>
  <li>$q$: 기본 전하량 ($1.6 \times 10^{-19}\text{ C}$)</li>
  <li>$n, p$: 각각 전자(Electron)와 정공(Hole)의 부피당 <strong>캐리어 밀도 ($\text{cm}^{-3}$)</strong></li>
  <li>$\mu_n, \mu_p$: 전자와 정공의 <strong>이동도 ($\text{cm}^2/\text{V}\cdot\text{s}$)</strong></li>
</ul>

<h3>3. 영역별 도핑과 캐리어의 1:1 매핑 (완전 이온화 Complete Ionization)</h3>
<p>
상온(300K)의 반도체에서는 주입한 불순물 원자가 실온의 열에너지만으로도 100% 전자를 내놓거나 정공을 만듭니다. 이를 <strong>'완전 이온화'</strong>라고 부릅니다.
</p>

<h4>① P형 반도체 영역을 잴 때 (P-기판, P-에피, P+ 소스/드레인)</h4>
<ul>
  <li><strong>주입 불순물</strong>: 3족 원소인 붕소(Boron, $B$) 등의 <strong>억셉터(Acceptor)</strong></li>
  <li><strong>도핑 농도</strong>: $N_A$ [$\text{cm}^{-3}$]</li>
  <li><strong>다수 캐리어</strong>: 억셉터가 전자를 받아들이면서 만들어낸 <strong>정공(Hole, $p$)</strong></li>
  <li>정공의 밀도가 전자의 밀도보다 압도적으로 많으므로 ($p \gg n$), 전자 성분은 0으로 무시됩니다:
    $$\sigma \approx q \cdot p \cdot \mu_p \approx q \cdot \mathbf{N_A} \cdot \mu_p$$
  </li>
  <li>따라서 <strong>P형 영역의 면저항</strong>은 질문하신 대로 정확히 정공($p$)과 억셉터($N_A$)로 표현됩니다:
    $$\mathbf{R_{s, P-type} = \frac{1}{q \cdot N_A \cdot \mu_p \cdot t}}$$
  </li>
</ul>

<h4>② N형 반도체 영역을 잴 때 (N+ 소스/드레인, N-Well, N+ 폴리 게이트)</h4>
<ul>
  <li><strong>주입 불순물</strong>: 5족 원소인 인(P), 비소(As) 등의 <strong>도너(Donor)</strong></li>
  <li><strong>도핑 농도</strong>: $N_D$ [$\text{cm}^{-3}$]</li>
  <li><strong>다수 캐리어</strong>: 도너가 자유롭게 방출한 <strong>전자(Electron, $n$)</strong></li>
  <li>전자의 밀도가 정공보다 압도적이므로 ($n \gg p$), 정공 성분을 무시합니다:
    $$\sigma \approx q \cdot n \cdot \mu_n \approx q \cdot \mathbf{N_D} \cdot \mu_n$$
  </li>
  <li>따라서 <strong>N형 영역의 면저항</strong>은 전자($n$)와 도너($N_D$)로 표현됩니다:
    $$\mathbf{R_{s, N-type} = \frac{1}{q \cdot N_D \cdot \mu_n \cdot t}}$$
  </li>
</ul>

<h3>4. 반도체 칩에서 면저항을 측정하는 실제 4대 영역 비교표</h3>
<table style="width:100%; border-collapse:collapse; margin:15px 0; font-size:0.9rem;">
  <thead>
    <tr style="background:#1e293b; color:#38bdf8;">
      <th style="padding:10px; border:1px solid #334155;">측정 대상 영역</th>
      <th style="padding:10px; border:1px solid #334155;">영역 타입</th>
      <th style="padding:10px; border:1px solid #334155;">도핑 농도 의미</th>
      <th style="padding:10px; border:1px solid #334155;">캐리어 밀도 실체</th>
      <th style="padding:10px; border:1px solid #334155;">주요 목적</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#38bdf8;">베어 웨이퍼 기판 (Bare Wafer)</td>
      <td style="padding:10px; border:1px solid #334155;">P-type (통상)</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>기판 붕소 농도 ($N_A$)</strong></td>
      <td style="padding:10px; border:1px solid #334155;"><strong>정공 밀도 ($p$)</strong> 👈 <em>질문하신 상황!</em></td>
      <td style="padding:10px; border:1px solid #334155;">웨이퍼 입고 검사 (4-Point Probe)</td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#10b981;">NMOS 소스/드레인</td>
      <td style="padding:10px; border:1px solid #334155;">N+ type</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>비소/인 농도 ($N_D$)</strong></td>
      <td style="padding:10px; border:1px solid #334155;"><strong>전자 밀도 ($n$)</strong></td>
      <td style="padding:10px; border:1px solid #334155;">S/D 기생 직렬 저항($R_{SD}$) 극소화</td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#ec4899;">PMOS 소스/드레인</td>
      <td style="padding:10px; border:1px solid #334155;">P+ type</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>붕소 농도 ($N_A$)</strong></td>
      <td style="padding:10px; border:1px solid #334155;"><strong>정공 밀도 ($p$)</strong></td>
      <td style="padding:10px; border:1px solid #334155;">PMOS 구동 전류($I_{on}$) 향상</td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#f59e0b;">살리사이드 (NiSi, CoSi2)</td>
      <td style="padding:10px; border:1px solid #334155;">금속성 화합물</td>
      <td style="padding:10px; border:1px solid #334155;">불순물 도핑 개념 없음</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>금속의 자유 전자 ($n_{free}$)</strong></td>
      <td style="padding:10px; border:1px solid #334155;">접촉 저항을 수 $\Omega/\text{sq}$ 이하로 격감</td>
    </tr>
  </tbody>
</table>

<h3>5. 핵심 요약 (1줄 정리)</h3>
<blockquote style="border-left:4px solid #38bdf8; padding-left:12px; color:#e2e8f0; font-weight:600; margin:15px 0;">
"P형 기판이나 P형 층을 다룰 때는 <strong>도핑농도는 붕소 농도($N_A$)이고 캐리어 밀도도 정공($p$)이 100% 맞습니다!</strong>  
다만 면저항 공식 자체는 보편적인 법칙이므로, N형 영역(NMOS S/D 등)을 잴 때는 도핑농도가 $N_D$, 캐리어 밀도가 전자($n$)로 바뀝니다!"
</blockquote>
"""

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 72 topics (q-72 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(72, 0, -1):
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
        r"최상단에는 '면저항의 도핑농도와 캐리어밀도는 P기판과 정공(p)을 뜻할까?'이 위치하며, 총 73개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Sheet Resistance Carrier topic!")
