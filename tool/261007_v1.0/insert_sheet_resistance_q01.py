# -*- coding: utf-8 -*-
"""
insert_sheet_resistance_q01.py
사용자 질문: "면저항은 도핑농도가 커지면 캐리어밀도가 커져 감소하는 이유?"
대시보드 최상단 Q01로 신규 추가하고, 기존 60개 질문을 Q02~Q61로 시프트 (총 61개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 물리 & 저항 역학)",
    "title": "면저항은 도핑농도가 커지면 캐리어밀도가 커져 감소하는 이유?",
    "summary": [
        "순수 실리콘(진성 반도체)은 상온에서 캐리어 농도가 $n_i \\approx 1.5 \\times 10^{10}\\,\\text{cm}^{-3}$에 불과해 부도체에 가깝지만, 불순물을 주입하면 상온 열에너지($26\\,\\text{meV}$)에 의해 도펀트가 거의 100% 완전 이온화되어 전도 전자(N형)나 정공(P형)을 폭발적으로 방출합니다.",
        "미시적 드리프트 전류 밀도 공식($J = q n v_d = q n \\mu \\mathcal{E} = \\sigma \\mathcal{E}$)에 따라, 전류를 수송하는 <strong>캐리어 밀도($n, p$)가 도핑 농도($N$)에 비례하여 수백만~수십억 배 증가</strong>하므로 <strong>전기 전도도($\\sigma = q N \\mu$)가 수직 상승</strong>합니다.",
        "비저항($\\rho = 1/\\sigma$)과 2차원 박막의 면저항($R_s = \\rho/t = \\frac{1}{q N \\mu t}$)은 전도도에 정확히 역비례하므로, <strong>전하를 나르는 '일꾼(캐리어)'의 수가 늘어날수록 통로의 저항이 반비례하여 급격히 감소</strong>합니다.",
        "다만 도핑 농도가 $10^{18}\\,\\text{cm}^{-3}$를 넘는 초고농도에서는 전자가 이온화된 불순물 원자핵과 부딪히는 <strong>이온화 불순물 산란(Ionized Impurity Scattering)</strong>으로 이동도($\\mu$)가 깎이기 때문에, 저항 감소율이 점차 둔화되는 비선형성(Irvin Curve)을 나타냅니다."
    ],
    "svg_title": "📊 [도핑 농도와 면저항 역학] 도펀트 완전 이온화 ➔ 캐리어 밀도 폭증 ➔ 전도도 상승 & 면저항 감소 원리",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: Atomic & Carrier Generation Mechanism -->
  <rect x="20" y="25" width="365" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="50" fill="#38bdf8" font-size="12.5" font-weight="800">1. 미시적 메커니즘: 도펀트 이온화 & 캐리어 폭증</text>

  <!-- Intrinsic vs Doped Box -->
  <rect x="35" y="65" width="335" height="110" rx="4" fill="#1e293b"/>
  <text x="45" y="85" fill="#94a3b8" font-size="11" font-weight="700">[진성 실리콘: 부도체 상태]</text>
  <text x="45" y="103" fill="#cbd5e1" font-size="10">• 진성 캐리어: ni ≈ 1.5 × 10¹⁰ cm⁻³ (극소량)</text>
  <text x="45" y="120" fill="#f87171" font-size="10">• 자유 전자/정공 결핍 ➔ 전류 거의 안 흐름 (고저항)</text>

  <text x="45" y="145" fill="#34d399" font-size="11" font-weight="700">[도핑 후 실리콘: 완전 이온화 (상온 300K)]</text>
  <text x="45" y="163" fill="#cbd5e1" font-size="10">• 5가 인(P) 도핑 ➔ P⁺ 고정이온 + 자유 전자(e⁻) 방출</text>

  <!-- Formula Card -->
  <rect x="35" y="185" width="335" height="145" rx="4" fill="#1e293b"/>
  <text x="45" y="205" fill="#fbbf24" font-size="11" font-weight="700">전도도 & 면저항 핵심 물리 공식</text>
  <text x="45" y="228" fill="#38bdf8" font-size="12" font-weight="800">σ = q · n · μ ≈ q · N · μ   (전기도도 폭증!)</text>
  <text x="45" y="252" fill="#34d399" font-size="12" font-weight="800">Rs = ρ / t = 1 / ( q · N · μ · t )</text>
  <text x="45" y="275" fill="#cbd5e1" font-size="9.5">• q: 기본 전하량 (1.6 × 10⁻¹⁹ C)</text>
  <text x="45" y="292" fill="#cbd5e1" font-size="9.5">• N: 도핑 농도 (캐리어 밀도 n에 직결, 분모 위치)</text>
  <text x="45" y="310" fill="#f59e0b" font-size="9.5">• t: 박막 두께 또는 접합 깊이(Xj)</text>
  <text x="45" y="325" fill="#34d399" font-size="9">➔ N 증가 시 분모 급증 ➔ 면저항(Rs) 급격히 감소!</text>

  <!-- Right: Resistance Curve & Scattering Tradeoff -->
  <rect x="400" y="25" width="360" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
  <text x="415" y="50" fill="#10b981" font-size="12.5" font-weight="800">2. 도핑 농도(N) vs 면저항(Rs) 거동 & 산란 효과</text>

  <!-- Graph frame -->
  <rect x="415" y="65" width="330" height="155" rx="4" fill="#1e293b"/>
  <!-- Axis -->
  <line x1="440" y1="200" x2="725" y2="200" stroke="#64748b" stroke-width="1.2"/>
  <line x1="440" y1="80" x2="440" y2="200" stroke="#64748b" stroke-width="1.2"/>
  <text x="660" y="215" fill="#94a3b8" font-size="9.5">도핑 농도 N (log)</text>
  <text x="420" y="78" fill="#94a3b8" font-size="9.5">면저항 Rs</text>

  <!-- Rs curve (Decreasing curve) -->
  <path d="M 450 90 Q 480 120 530 165 Q 600 185 710 192" fill="none" stroke="#ef4444" stroke-width="2.5"/>
  <text x="480" y="105" fill="#ef4444" font-size="10" font-weight="800">면저항 Rs 곡선 (급감)</text>

  <!-- Mobility curve (Decreasing due to scattering) -->
  <path d="M 450 130 Q 520 132 580 155 Q 640 180 710 188" fill="none" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="590" y="145" fill="#38bdf8" font-size="9.5">이동도 μ 저하</text>

  <rect x="415" y="230" width="330" height="100" rx="4" fill="#1e293b"/>
  <text x="425" y="248" fill="#fbbf24" font-size="10.5" font-weight="700">★ 핵심 요약 및 비선형성 원인 (Irvin Curve)</text>
  <text x="425" y="266" fill="#cbd5e1" font-size="9.5">1) 저/중농도: 캐리어 수(N) 폭증 ➔ Rs가 반비례하며 수직 하강</text>
  <text x="425" y="284" fill="#f87171" font-size="9.5">2) 고농도(N > 10¹⁸): 이온화 불순물 산란 ➔ 이동도(μ) 감소</text>
  <text x="425" y="301" fill="#34d399" font-size="9.5">   ➔ N이 커져도 μ가 깎여 Rs 감소 기울기가 완만해짐</text>
  <text x="425" y="318" fill="#38bdf8" font-size="9.5">3) 초미세 공정: t(Xj) 축소로 Rs 폭증 ➔ Salicide(NiSi) 보상</text>
</svg>""",
    "lecture": r"""<h3>1. 본질적 출발점: 왜 순수 실리콘은 전기가 안 통하는가?</h3>
<p>실리콘(Si)은 최외각 전자 4개가 이웃한 4개의 실리콘 원자와 빈틈없이 공유 결합(Covalent Bond)을 이루고 있습니다. 절대영도(0K)에서는 전도대에 자유 전자가 단 하나도 없어 완벽한 부도체입니다.<br>
상온(300K)에서도 열에너지로 결합이 깨져 생성되는 진성 캐리어 농도는 $n_i \approx 1.5 \times 10^{10}\,\text{cm}^{-3}$에 불과합니다. 실리콘 원자 밀도가 $5 \times 10^{22}\,\text{cm}^{-3}$이므로, 원자 약 <strong>3조 개당 1개꼴</strong>로만 전자가 존재하는 셈이어서 전기가 거의 흐르지 않습니다.</p>

<h3>2. 도핑과 '완전 이온화(Complete Ionization)': 일꾼(캐리어)의 폭발적 증원</h3>
<p>여기에 5가 원소인 인(P)이나 비소(As)를 도핑하면, 4개의 전자는 공유 결합에 참여하고 <strong>남는 1개의 여분 전자가 원자 주위를 헐겁게 돕니다</strong>.</p>
<ul>
  <li>이 여분 전자의 결합 에너지(이온화 에너지 $E_d$)는 불과 약 $0.045\,\text{eV}$ ($45\,\text{meV}$)로 매우 작습니다.</li>
  <li>상온(300K)에서의 열에너지($k_B T \approx 0.0259\,\text{eV} = 26\,\text{meV}$)만으로도 도펀트의 거의 100%가 에너지를 얻어 전도대로 전자를 내뿜는 <strong>완전 이온화(Complete Ionization)</strong>가 일어납니다.</li>
  <li>따라서 도핑 농도를 $N_D = 10^{17}\,\text{cm}^{-3}$로 설정하면, 자유 전자 농도 $n \approx N_D$가 되어 진성 상태보다 <strong>전하를 나르는 캐리어가 1,000만 배 폭증</strong>합니다.</li>
</ul>

<h3>3. 수식으로 보는 전도도($\sigma$) 상승과 면저항($R_s$) 감소</h3>

<h4>① 미시적 옴의 법칙 (Microscopic Ohm's Law)</h4>
<p>외부에서 전기장 $\mathcal{E}$를 가했을 때, 전자들이 이동하는 평균 드리프트 속도는 $v_d = \mu \mathcal{E}$입니다 ($\mu$: 이동도).<br>
단위 면적을 통과하는 전류 밀도 $J$는 단위 부피당 전하량($q \cdot n$)과 속도($v_d$)의 곱이므로 다음과 같이 유도됩니다:</p>
<div class="formula-box">$$J = q \cdot n \cdot v_d = q \cdot n \cdot (\mu \mathcal{E}) = (q \cdot n \cdot \mu) \mathcal{E}$$</div>
<p>옴의 법칙 $J = \sigma \mathcal{E}$와 비교하면, 전기 전도도 $\sigma$는 다음과 같습니다:</p>
<div class="formula-box">$$\sigma = q \cdot n \cdot \mu_n + q \cdot p \cdot \mu_p \approx q \cdot N \cdot \mu$$</div>
<p>즉, <strong>전기 전도도($\sigma$)는 전류를 나르는 캐리어 밀도($N$)에 정비례하여 수직 상승</strong>합니다.</p>

<h4>② 비저항($\rho$)과 면저항($R_s$)의 역비례 관계</h4>
<p>비저항($\rho$)은 전도도의 역수입니다 ($\rho = \frac{1}{\sigma}$).<br>
반도체 웨이퍼 표면이나 접합층처럼 두께 $t$가 정해진 2차원 박막 구조에서는 3차원 부피 저항 대신 <strong>면저항($R_s$, Sheet Resistance, 단위: $\Omega/\text{sq}$)</strong>을 정의합니다:</p>
<div class="formula-box">$$R_s = \frac{\rho}{t} = \frac{1}{\sigma \cdot t} = \frac{1}{q \cdot N \cdot \mu \cdot t}$$</div>
<p>분모에 도핑 농도($N$)가 위치하므로, <strong>도핑 농도가 커질수록 분모가 급격히 커져 면저항($R_s$)은 정비례하여 급감</strong>합니다.</p>

<div class="analogy-card">
  <div class="analogy-title">직관적 비유: '물류 도로와 화물차'</div>
  <div class="analogy-desc">도로 폭과 길이(박막 두께 $t$ 및 소자 크기)가 동일할 때, 물건을 나르는 화물차(캐리어 $n$)가 1대뿐일 때는 물류 이동(전류)이 극히 적어 체증/저항이 높지만, 화물차를 수백만 대(도핑 농도 $N$) 투입하면 시간당 쏟아지는 물동량(전류)이 압도적으로 늘어나 저항이 바닥으로 떨어지는 것과 같습니다.</div>
</div>

<h3>4. 왜 완벽한 반비례가 아닌가? (이온화 불순물 산란의 비선형성)</h3>
<p>수식상으로는 도핑 농도 $N$을 10배 올리면 면저항 $R_s$가 정확히 $1/10$로 떨어져야 할 것 같지만, 실제 실험 곡선(Irvin Curve)을 보면 <strong>고농도로 갈수록 저항 감소율이 둔화</strong>됩니다.</p>
<ul>
  <li>전자가 이동할 때 실리콘 원자 격자의 진동과 부딪히는 <strong>격자 산란(Lattice Scattering)</strong> 외에도,</li>
  <li>도핑 농도가 $10^{18}\,\text{cm}^{-3}$ 이상으로 높아지면 실리콘 격자 곳곳에 박힌 (+) 또는 (-)의 <strong>이온화된 불순물 이온($P^+, B^-$)과의 쿨롱 정전기 인력/척력</strong>에 의해 전자 궤도가 꺾이는 <strong>이온화 불순물 산란(Ionized Impurity Scattering)</strong>이 극심해집니다.</li>
  <li>그 결과 캐리어의 이동도($\mu$)가 급감하게 되며, 분모에서 $N$의 증가분을 $\mu$의 감소분이 상쇄하여 고농도 영역에서는 면저항의 감소 기울기가 완만해집니다.</li>
</ul>

<h3>5. 초미세 반도체에서의 최신 공학적 이슈</h3>
<p>단채널 효과(DIBL, 펀치스루)를 방어하기 위해 소스/드레인 접합 깊이($t = X_j$)를 $10\,\text{nm}$ 이하로 극도로 얇게(USJ) 만들면, 분모의 $t$가 너무 작아져 <strong>면저항($R_s$)이 천문학적으로 폭증</strong>합니다.<br>
이를 상쇄하기 위해 공정 엔지니어들은 다음의 2가지 필살기를 적용합니다:</p>
<ol>
  <li><strong>고체 용해도 한계($10^{20}\,\text{cm}^{-3}$)까지 도핑 농도($N$) 극대화</strong>: 얇아진 $t$를 분모의 $N$으로 최대한 메웁니다.</li>
  <li><strong>살리사이드(Salicide) 및 Raised S/D</strong>: 도핑된 실리콘 표면에 전도도가 압도적으로 높은 니켈 실리사이드(NiSi)를 형성하여 전기가 실리사이드 층으로 우회하여 흐르게 만듭니다.</li>
</ol>"""
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 60 topics (q-60 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(60, 0, -1):
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
    new_nav_item = f'      <li class="nav-item"><a href="#{NEW_TOPIC["id"]}" class="nav-link"><span class="nav-num">{NEW_TOPIC["num"]}</span><span class="nav-text">{NEW_TOPIC["title"]}</span></a></li>\n'
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
    old_desc_part = "총 60개 질문으로 구성되어 있습니다."
    new_desc_part = "최상단에는 '면저항과 도핑농도/캐리어밀도 역학' 및 'doping profile이 왜중요해?'가 위치하며, 총 61개 질문으로 구성되어 있습니다."
    if old_desc_part in html:
        html = html.replace(old_desc_part, new_desc_part)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 sheet resistance topic!")
