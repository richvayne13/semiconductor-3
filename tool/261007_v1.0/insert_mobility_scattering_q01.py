# -*- coding: utf-8 -*-
"""
insert_mobility_scattering_q01.py
사용자 질문: "채널농도를 올리면 전자이동도는왜떨어져?"
대시보드 최상단 Q01로 신규 추가하고, 기존 62개 질문을 Q02~Q63으로 시프트 (총 63개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 물리 & 캐리어 수송)",
    "title": "채널농도를 올리면 전자이동도는 왜 떨어져?",
    "summary": [
        "채널 농도(P형 억셉터 도핑 $N_A$)를 높이면 전자의 주행을 방해하는 <strong>두 가지 핵심 산란(Scattering) 메커니즘</strong>이 동시에 폭증하여 이동도($\\mu_n = \\frac{q\\tau}{m^*}$)가 급격히 떨어집니다.",
        "<strong>① 이온화 불순물 산란 (Ionized Impurity Scattering)</strong>: 실리콘 격자에 박힌 <strong>음이온 붕소 원자($B^-$)</strong> 밀도가 증가하여, 지나가는 전자($e^-$)가 <strong>쿨롱 척력</strong>으로 인해 이리저리 튕겨 나가며 평균 자유 시간($\\tau$)이 급감합니다.",
        "<strong>② 수직 유효 전계($\\mathcal{E}_{eff}$) 증가에 따른 표면 거칠기 산란 (Surface Roughness Scattering)</strong>: 공핍전하량($|Q_{dep}| \\propto \\sqrt{N_A}$) 증가로 게이트 수직 전계가 강해져, 전자가 원자 수준에서 울퉁불퉁한 <strong>산화막-실리콘 계면 벽에 강하게 짓눌린 채 긁히며 이동</strong>하기 때문입니다 ($\\mu_{sr} \\propto \\mathcal{E}_{eff}^{-2}$).",
        "마티센의 법칙($\\frac{1}{\\mu} = \\frac{1}{\\mu_{phonon}} + \\frac{1}{\\mu_{imp}} + \\frac{1}{\\mu_{sr}}$)에 의해 이동도가 떨어지면 구동 전류($I_{on}$)와 스위칭 속도가 둔화되므로, 현대 FinFET 및 GAA는 채널에 불순물을 아예 넣지 않는 <strong>'무도핑 채널(Undoped Channel)'</strong>로 진화했습니다."
    ],
    "svg_title": "📊 [채널 농도와 전자 이동도 역학] 쿨롱 척력 산란 & 게이트 수직 전계에 의한 표면 거칠기 마찰",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: 2 Microscopic Scattering Mechanisms -->
  <rect x="20" y="25" width="375" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="50" fill="#38bdf8" font-size="12.5" font-weight="800">1. 이동도 저하의 2대 미시적 충돌 메커니즘</text>

  <!-- Box 1: Coulomb Scattering -->
  <rect x="35" y="65" width="345" height="120" rx="4" fill="#1e293b"/>
  <text x="45" y="85" fill="#f87171" font-size="11" font-weight="700">① 이온화 불순물 쿨롱 산란 (Ionized Impurity)</text>
  <!-- Electron path deflected by B- ions -->
  <circle cx="160" cy="125" r="10" fill="#ef4444" opacity="0.8"/>
  <text x="153" y="129" fill="#ffffff" font-size="11" font-weight="900">B⁻</text>
  <circle cx="260" cy="140" r="10" fill="#ef4444" opacity="0.8"/>
  <text x="253" y="144" fill="#ffffff" font-size="11" font-weight="900">B⁻</text>

  <!-- Deflected electron path -->
  <path d="M 50 120 L 135 122 L 175 100 L 235 155 L 290 120 L 360 125" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,2"/>
  <circle cx="60" cy="120" r="4" fill="#38bdf8"/>
  <text x="68" y="115" fill="#38bdf8" font-size="9.5">전자 (e⁻)</text>
  <text x="45" y="172" fill="#cbd5e1" font-size="9.5">• B⁻ 음이온 밀도(NA) 증가 ➔ 쿨롱 척력으로 궤도 꺾임</text>

  <!-- Box 2: Surface Roughness Scattering -->
  <rect x="35" y="195" width="345" height="135" rx="4" fill="#1e293b"/>
  <text x="45" y="215" fill="#fbbf24" font-size="11" font-weight="700">② 표면 거칠기 산란 (Surface Roughness)</text>
  <!-- Oxide wall bumpy -->
  <path d="M 50 235 Q 70 240 90 235 Q 110 230 130 235 Q 150 240 170 235 Q 190 230 210 235 Q 230 240 250 235 Q 270 230 290 235 Q 310 240 330 235 Q 350 230 370 235" fill="none" stroke="#64748b" stroke-width="3"/>
  <text x="280" y="230" fill="#94a3b8" font-size="8.5">SiO₂ / Si 계면 요철</text>

  <!-- Strong vertical field E_eff -->
  <line x1="120" y1="285" x2="120" y2="245" stroke="#ef4444" stroke-width="2"/>
  <line x1="220" y1="285" x2="220" y2="245" stroke="#ef4444" stroke-width="2"/>
  <text x="135" y="275" fill="#ef4444" font-size="9" font-weight="800">강한 수직 전계 E_eff (NA↑로 증가)</text>
  <!-- Electron scraping -->
  <path d="M 50 245 L 85 242 L 130 246 L 190 241 L 260 247 L 360 242" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <text x="45" y="305" fill="#cbd5e1" font-size="9.5">• 강한 수직 전계에 눌려 원자벽에 긁히며 이동</text>
  <text x="45" y="320" fill="#f87171" font-size="9.5">• 고전계 영역에서 이동도 급추락 (μ_sr ∝ E_eff⁻²)</text>

  <!-- Right: Mobility Curve & Matthiessen's Law -->
  <rect x="410" y="25" width="350" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
  <text x="425" y="50" fill="#10b981" font-size="12.5" font-weight="800">2. 마티센의 법칙 & 도핑 농도별 이동도 곡선</text>

  <rect x="425" y="65" width="320" height="110" rx="4" fill="#1e293b"/>
  <text x="435" y="85" fill="#fbbf24" font-size="11" font-weight="700">마티센의 법칙 (Matthiessen's Rule)</text>
  <text x="435" y="110" fill="#38bdf8" font-size="12" font-weight="800">1/μ_eff = 1/μ_phonon + 1/μ_imp + 1/μ_sr</text>
  <text x="435" y="132" fill="#cbd5e1" font-size="9.5">• μ_phonon: 격자 진동 산란 (온도 의존)</text>
  <text x="435" y="148" fill="#f87171" font-size="9.5">• μ_imp: 이온화 불순물 산란 (NA 증가 시 급감!)</text>
  <text x="435" y="165" fill="#f59e0b" font-size="9.5">• μ_sr: 표면 거칠기 산란 (NA 증가 ➔ E_eff 증가로 급감!)</text>

  <!-- Graph -->
  <rect x="425" y="185" width="320" height="145" rx="4" fill="#1e293b"/>
  <text x="435" y="205" fill="#10b981" font-size="11" font-weight="700">★ 공학적 결론과 최신 극복 기술</text>
  <text x="435" y="225" fill="#f87171" font-size="10" font-weight="700">문제점: 이동도(μn) 저하 ➔ 구동전류 Ion 급감</text>
  <text x="435" y="242" fill="#cbd5e1" font-size="9.5">• Ion = 1/2 · μn · Cox · (W/L) · (VGS - Vth)²</text>
  <text x="435" y="260" fill="#38bdf8" font-size="10.5" font-weight="700">해결책 1) Retrograde Well:</text>
  <text x="445" y="276" fill="#cbd5e1" font-size="9">표면은 저농도(μn 사수) + 지하만 고농도(펀치스루 방어)</text>
  <text x="435" y="295" fill="#34d399" font-size="10.5" font-weight="700">해결책 2) FinFET & GAA 무도핑 채널 (Undoped):</text>
  <text x="445" y="312" fill="#cbd5e1" font-size="9">게이트가 3~4면 포위 ➔ 채널에 도핑 0개! 산란 박멸</text>
</svg>""",
    "lecture": r"""<h3>1. 본질적 정의: 이동도($\mu$)를 결정하는 것은 '평균 충돌 시간($\tau$)'</h3>
<p>전자의 전계 내 이동도 공식은 $\mu = \frac{q \tau}{m^*}$ 입니다 ($q$: 전하량, $m^*$: 유효 질량).<br>
여기서 $q$와 $m^*$는 고유 물리 상수이므로, <strong>이동도($\mu$)의 크기는 전자가 다른 장애물과 충돌하지 않고 자유롭게 달릴 수 있는 시간(평균 자유 시간, Mean Free Time $\tau$)에 100% 비례</strong>합니다.<br>
채널 도핑 농도($N_A$)를 올리면 전자의 주행을 가로막는 장애물이 폭증하여 $\tau$가 급감하므로 전자 이동도가 뚝 떨어집니다.</p>

<h3>2. 왜 채널 농도를 올리면 이동도가 떨어지는가? (3대 물리적 메커니즘)</h3>

<h4>① 이온화 불순물 산란 (Ionized Impurity Scattering / 쿨롱 충돌)</h4>
<p>NMOS 채널의 농도를 올린다는 것은, 실리콘 격자 내에 <strong>음이온화된 붕소 억셉터($B^-$)의 개수 밀도를 늘리는 것</strong>을 의미합니다.</p>
<ul>
  <li>전도 채널을 달리는 전자($e^-$)는 음(-)전하를 띠고 있습니다.</li>
  <li>전자가 이동하다가 실리콘 격자 곳곳에 빽빽하게 박혀있는 붕소 음이온($B^-$)을 마주치면, <strong>동일한 음전하 간의 쿨롱 척력(Coulomb Repulsion)</strong>에 의해 궤도가 강하게 꺾여 튕겨 나갑니다.</li>
  <li>불순물 이온의 밀도($N_A$)가 높을수록 전자는 몇 나노미터도 가지 못하고 계속해서 척력에 부딪히며 지그재그로 방황하게 되므로, 유효 속도와 이동도($\mu_{imp} \propto \frac{T^{3/2}}{N_A}$)가 곤두박질칩니다.</li>
</ul>

<h4>② 수직 유효 전계($\mathcal{E}_{eff}$) 증가로 인한 표면 거칠기 산란 (Surface Roughness Scattering)</h4>
<p>가우스 법칙에 의해, 게이트 산화막 아래 실리콘 표면의 수직 전기장($\mathcal{E}_{eff}$)은 공핍 전하량에 비례합니다:</p>
<div class="formula-box">$$\mathcal{E}_{eff} \approx \frac{|Q_{dep}| + \frac{1}{2}|Q_{inv}|}{\epsilon_s}$$</div>
<ul>
  <li>앞서 배웠듯이 공핍전하량은 $|Q_{dep}| = \sqrt{2q\epsilon_s N_A (2\phi_B)}$ 로서 도핑 농도 $N_A$의 제곱근에 비례합니다.</li>
  <li>채널 농도($N_A$)를 높이면 $|Q_{dep}|$가 급증하여, 게이트가 실리콘 표면을 수직으로 내리누르는 <strong>수직 유효 전계($\mathcal{E}_{eff}$)가 극도로 강력</strong>해집니다.</li>
  <li>전기장이 전자를 게이트 쪽으로 강하게 밀착시키기 때문에, 전자들은 <strong>산화막과 실리콘 계면의 울퉁불퉁한 원자 벽($\text{Si}-\text{SiO}_2$ 요철)에 바짝 붙은 채 이동</strong>해야 합니다.</li>
  <li>원자 단위의 계면 거칠기에 긁히면서 진행하므로 <strong>표면 거칠기 산란(Surface Roughness Scattering)</strong>이 폭증하며, 이 산란에 의한 이동도는 전계의 제곱에 반비례하여 급감합니다 ($\mu_{sr} \propto \mathcal{E}_{eff}^{-2}$).</li>
</ul>

<h4>③ 마티센의 법칙 (Matthiessen's Rule)에 의한 종합 이동도 폭락</h4>
<p>반도체 채널 내에서 전자가 겪는 총 유효 이동도는 각 산란 성분의 역수 합으로 결정됩니다:</p>
<div class="formula-box">$$\frac{1}{\mu_{eff}} = \frac{1}{\mu_{phonon}} + \frac{1}{\mu_{imp}} + \frac{1}{\mu_{sr}}$$</div>
<p>채널 농도($N_A$)를 올리면 <strong>$\mu_{imp}$(쿨롱 산란)</strong>와 <strong>$\mu_{sr}$(표면 거칠기 산란)</strong>이 동시에 급감하므로, 전체 유효 이동도 $\mu_{eff}$는 피할 수 없이 수직 낙하합니다.</p>

<div class="analogy-card">
  <div class="analogy-title">직관적 비유: '빙판길 자갈밭과 강풍'</div>
  <div class="analogy-desc">스케이트 선수가 매끄러운 빙판길(진성 실리콘)을 달릴 때는 속도가 빠르지만, 빙판 위에 자갈(불순물 이온 $B^-$)을 빽빽하게 깔아놓으면(이온화 불순물 산란) 발이 걸려 속도가 느려집니다.<br>
거기에 더해 위에서 아래로 짓누르는 거대한 태풍(강한 수직 전계 $\mathcal{E}_{eff}$)까지 불어와 선수가 울퉁불퉁한 벽면에 바짝 붙어 몸을 긁히며 달려야 한다면(표면 거칠기 산란), 주행 속도(전자 이동도)는 완전히 바닥을 칠 수밖에 없습니다.</div>
</div>

<h3>3. 공학적 딜레마와 최신 극복 기술</h3>
<p>전자 이동도($\mu_n$)가 떨어지면 구동 전류 공식($I_{on} \propto \mu_n$)에 의해 <strong>트랜지스터의 속도가 느려지고 칩의 처리 성능이 저하</strong>됩니다. 이를 극복하기 위해 현대 반도체 공학은 다음과 같이 진화했습니다:</p>
<ol>
  <li><strong>Retrograde Well (역역방향 웰 도핑)</strong>:
    <p>전자가 실제로 지나가는 표면 채널($0\sim5\,\text{nm}$)은 $N_A$를 낮추어 이동도($\mu_n$)를 보존하고, 전자가 다니지 않는 지하 수십 nm 깊이에만 $N_A$를 높여 펀치스루를 차단합니다.</p>
  </li>
  <li><strong>FinFET & GAA 나노시트의 '무도핑 채널(Undoped Channel)' 혁신</strong>:
    <p>평면 트랜지스터는 단채널 효과를 막기 위해 채널에 불순물을 억지로 많이 넣어야만 했습니다.<br>
    하지만 3차원 FinFET(3면 게이트)과 GAA(4면 게이트)는 구조 자체가 채널을 완벽하게 포위하므로, <strong>채널 영역에 불순물을 단 1개도 넣지 않는 무도핑(Undoped Si) 채널</strong>을 사용할 수 있게 되었습니다. 불순물 산란이 완전히 사라지면서 전자가 마치 고속도로를 달리듯 극대화된 이동도로 질주할 수 있게 된 것입니다.</p>
  </li>
</ol>"""
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 62 topics (q-62 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(62, 0, -1):
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
    old_desc_part = "총 62개 질문으로 구성되어 있습니다."
    new_desc_part = "최상단에는 '채널농도와 전자이동도 저하 메커니즘' 및 '공핍전하량 역학'이 위치하며, 총 63개 질문으로 구성되어 있습니다."
    if old_desc_part in html:
        html = html.replace(old_desc_part, new_desc_part)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 mobility scattering topic!")
