# -*- coding: utf-8 -*-
"""
insert_graded_junction_cj_q01.py
사용자 질문: "도핑농도를 완만하게 하면 공핍층넓어져 CJ감소하는로직"
대시보드 최상단 Q01로 신규 추가하고, 기존 63개 질문을 Q02~Q64로 시프트 (총 64개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 물리 & 접합 역학)",
    "title": "도핑농도를 완만하게 하면 공핍층 넓어져 Cj 감소하는 로직",
    "nav_title": "도핑농도를 완만하게 하면 공핍층 넓어져 Cj 감소하는 로직",
    "summary": [
        "<strong>전하 중성 원리($Q^+ = Q^-$)와 희박한 계면 전하</strong>: 농도가 절벽처럼 꺾이는 급준 접합(Step)은 조금만 파고들어도 전하가 가득 차 공핍층($W_{dep}$)이 좁지만, 완만한 경사 접합(Graded)은 계면 부근의 도펀트 밀도가 매우 낮아 필요한 전하량을 확보하기 위해 <strong>공핍층이 양옆으로 훨씬 더 깊고 넓게 확장($W_{dep} \\uparrow$)</strong>되어야 합니다.",
        "<strong>푸아송 방정식 유도 ($W_{dep} \\propto a^{-1/3}$)</strong>: 농도 기울기 $a = \\frac{dN}{dx}$가 완만할수록($a \\downarrow$), 푸아송 2차 적분에 의해 유도되는 공핍층 폭 $W_{dep} = \\left[\\frac{12\\epsilon_s (V_{bi}-V)}{q a}\\right]^{1/3}$ 공식의 분모가 작아져 <strong>공핍층 폭($W_{dep}$)이 수학적으로 명백하게 증가</strong>합니다.",
        "<strong>평행판 커패시터 모델 ($C_j = \\frac{\\epsilon_s A}{W_{dep}}$)</strong>: 접합 커패시턴스는 유전체 역할을 하는 공핍층 폭($W_{dep}$)에 역비례하므로, <strong>공핍층이 넓어지면 양극판 사이의 거리가 멀어지는 것과 완벽히 같아 기생 커패시턴스($C_j$)가 획기적으로 급감</strong>합니다.",
        "<strong>고속 회로 RC 지연 극복</strong>: MOSFET 소스/드레인 접합에서 $C_j$는 신호 스위칭 지연($\\tau \\approx R C_j$)의 주범이므로, 접합부에 완만한 농도 경사(Graded Junction)를 설계하여 $C_j$를 깎아내면 칩의 최대 동작 주파수($f_{max}$)가 비약적으로 상승합니다."
    ],
    "svg_title": "📊 [경사 접합과 공핍층 폭 역학] 급준 접합 vs 완만 경사 접합의 전하 적분 & Cj = ε/Wdep 감소 메커니즘",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: Step vs Graded Junction Charge Profile -->
  <rect x="20" y="25" width="375" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="50" fill="#38bdf8" font-size="12.5" font-weight="800">1. 급준 접합 vs 완만 경사 접합의 공간 전하 비교</text>

  <!-- Step Junction Box -->
  <rect x="35" y="65" width="345" height="120" rx="4" fill="#1e293b"/>
  <text x="45" y="83" fill="#f87171" font-size="10.5" font-weight="700">① 급준 접합 (Step / Abrupt Junction)</text>
  <!-- Step Profile graphic -->
  <rect x="130" y="95" width="45" height="35" fill="#ef4444" opacity="0.6"/>
  <rect x="175" y="95" width="45" height="35" fill="#0284c7" opacity="0.6"/>
  <line x1="175" y1="90" x2="175" y2="135" stroke="#ffffff" stroke-width="1.5"/>
  <text x="145" y="117" fill="#ffffff" font-size="9" font-weight="800">- qNA</text>
  <text x="185" y="117" fill="#ffffff" font-size="9" font-weight="800">+ qND</text>
  <line x1="130" y1="138" x2="220" y2="138" stroke="#fbbf24" stroke-width="2"/>
  <text x="145" y="152" fill="#fbbf24" font-size="9" font-weight="700">W_step (좁음)</text>
  <text x="45" y="172" fill="#cbd5e1" font-size="9.5">• 고농도가 계면까지 유지 ➔ 좁은 폭으로도 전하 충족</text>

  <!-- Graded Junction Box -->
  <rect x="35" y="195" width="345" height="135" rx="4" fill="#1e293b"/>
  <text x="45" y="213" fill="#34d399" font-size="10.5" font-weight="700">② 완만 경사 접합 (Linearly Graded: ρ = q · a · x)</text>
  <!-- Graded Triangle graphic -->
  <polygon points="90,265 175,265 175,235" fill="#ef4444" opacity="0.5"/>
  <polygon points="175,265 260,265 175,295" fill="#0284c7" opacity="0.5"/>
  <line x1="175" y1="225" x2="175" y2="305" stroke="#ffffff" stroke-width="1.5"/>
  <text x="120" y="258" fill="#ffffff" font-size="8.5">희박한 전하</text>
  <text x="195" y="278" fill="#ffffff" font-size="8.5">희박한 전하</text>
  <line x1="90" y1="310" x2="260" y2="310" stroke="#34d399" stroke-width="2.5"/>
  <text x="135" y="324" fill="#34d399" font-size="9.5" font-weight="800">W_graded (훨씬 넓음!)</text>
  <text x="270" y="260" fill="#fbbf24" font-size="9.5">기울기 a = dN/dx</text>
  <text x="270" y="275" fill="#cbd5e1" font-size="8.5">• 계면 농도 낮아</text>
  <text x="270" y="288" fill="#34d399" font-size="8.5">  넓게 퍼져야 균형!</text>

  <!-- Right: Mathematical Law & Capacitance Reduction -->
  <rect x="410" y="25" width="350" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
  <text x="425" y="50" fill="#10b981" font-size="12.5" font-weight="800">2. 수학적 유도 & Cj 감소 핵심 메커니즘</text>

  <rect x="425" y="65" width="320" height="110" rx="4" fill="#1e293b"/>
  <text x="435" y="85" fill="#fbbf24" font-size="11" font-weight="700">푸아송 방정식 유도: 공핍층 폭 공식</text>
  <text x="435" y="108" fill="#38bdf8" font-size="12" font-weight="800">W_graded = [ 12 · εs · (Vbi - V) / (q · a) ] ^ (1/3)</text>
  <text x="435" y="130" fill="#cbd5e1" font-size="9.5">• a (도핑 농도 기울기)가 완만할수록 (a ↓)</text>
  <text x="435" y="148" fill="#34d399" font-size="10.5" font-weight="700">➔ 분모 감소로 공핍층 폭(W)이 대폭 확장!</text>
  <text x="435" y="165" fill="#cbd5e1" font-size="9">(급준 접합 W ∝ V^1/2 대비 완만 접합 W ∝ V^1/3)</text>

  <rect x="425" y="185" width="320" height="145" rx="4" fill="#1e293b"/>
  <text x="435" y="205" fill="#f59e0b" font-size="11" font-weight="700">기생 접합 커패시턴스 Cj 급감 원리</text>
  <text x="435" y="230" fill="#ef4444" font-size="13" font-weight="900">Cj = εs · A / Wdep   (평행판 모델)</text>
  <text x="435" y="252" fill="#cbd5e1" font-size="9.5">• Wdep: 유전체 두께 (커패시터 양 극판 간격)</text>
  <text x="435" y="270" fill="#38bdf8" font-size="10" font-weight="700">★ 결론: Wdep가 2배 넓어지면 ➔ Cj는 50%로 절반 폭락!</text>
  <text x="435" y="292" fill="#34d399" font-size="9.5">공학적 이점: 인버터 스위칭 지연(RC Delay) 극소화</text>
  <text x="435" y="310" fill="#fbbf24" font-size="9">➔ S/D LDD 경사 접합 설계로 칩 동작 속도 극대화</text>
</svg>""",
    "lecture": r"""<h3>1. 핵심 질문의 출발: 도핑을 완만하게 하면 왜 공핍층이 넓어지는가?</h3>
<p>이 원리의 가장 밑바닥에는 물리 법칙인 <strong>'전하 중성 조건(Charge Neutrality Condition, $Q^+ = Q^-$)'</strong>이 자리잡고 있습니다.</p>
<ul>
  <li><strong>급준 접합 (Step Junction)</strong>: 계면($x=0$) 바로 옆부터 $N_A$, $N_D$라는 높은 농도의 불순물이 꽉 차 있습니다. 따라서 아주 좁은 폭($W_{dep}$)만 공핍화되어도 전위차를 지탱할 충분한 전하량이 순식간에 모입니다.</li>
  <li><strong>완만한 경사 접합 (Linearly Graded Junction)</strong>: 계면 부근의 도핑 농도 차이가 $N_D - N_A = a \cdot x$ ($a$: 농도 기울기) 형태로 서서히 증가합니다. 계면 근처의 불순물 밀도가 0에 가깝기 때문에, <strong>동일한 전위차($V_{bi}-V$)를 지탱할 고정 공간 전하량을 확보하려면 실리콘 깊은 곳까지 훨씬 더 넓게 공핍층을 확장($W_{dep} \uparrow$)해야만</strong> 전하 균형이 맞춰집니다.</li>
</ul>

<h3>2. 수식으로 보는 푸아송 방정식(Poisson's Eq) 유도</h3>

<h4>① 완만 경사 접합의 전하 밀도와 전계 유도</h4>
<p>농도 기울기를 $a = \frac{dN}{dx}$라 하면, 공간 전하 밀도는 $\rho(x) = q \cdot a \cdot x$ 입니다.<br>
푸아송 방정식 $\frac{d^2\phi}{dx^2} = -\frac{\rho(x)}{\epsilon_s} = -\frac{q a x}{\epsilon_s}$를 경계 조건($x = \pm W/2$에서 $\mathcal{E}=0$)에 맞춰 적분하면 최대 전계와 빌트인 전위차가 도출됩니다:</p>
<div class="formula-box">$$\mathcal{E}(x) = -\frac{q a}{2\epsilon_s} \left[ \left(\frac{W}{2}\right)^2 - x^2 \right]$$</div>
<div class="formula-box">$$V_{bi} - V = \int_{-W/2}^{W/2} \mathcal{E}(x) dx = \frac{q a W^3}{12 \epsilon_s}$$</div>

<h4>② 공핍층 폭($W_{dep}$) 수식 정리</h4>
<p>위 식을 공핍층 폭 $W$에 관해 풀면 완만 경사 접합의 핵심 공식이 완성됩니다:</p>
<div class="formula-box">$$W_{dep} = \left[ \frac{12 \epsilon_s (V_{bi} - V)}{q \cdot a} \right]^{1/3}$$</div>
<p><strong>수식의 분모에 농도 기울기 $a$가 위치</strong>합니다!<br>
도핑 농도를 완만하게 만든다는 것은 **기울기 $a$를 작게($a \downarrow$) 만든다는 뜻**이므로, <strong>분모가 작아져 공핍층 폭 $W_{dep}$는 수학적으로 명확하게 크게 증가</strong>합니다.</p>

<h3>3. 공핍층 폭($W_{dep}$)이 넓어지면 왜 접합 커패시턴스($C_j$)가 줄어드는가?</h3>
<p>p-n 접합은 두 개의 전도 영역(P형, N형 중성 영역) 사이에 절연체 역할을 하는 공핍층이 끼어있는 <strong>평행판 커패시터(Parallel-Plate Capacitor)</strong>와 완벽하게 동일합니다:</p>
<div class="formula-box">$$C_j = \frac{\epsilon_s \cdot A}{W_{dep}}$$</div>
<ul>
  <li>$\epsilon_s$: 실리콘 유전율 (상수)</li>
  <li>$A$: 접합 단면적</li>
  <li>$W_{dep}$: 유전체 두께이자 양 극판 사이의 물리적 거리</li>
</ul>
<p>커패시턴스는 두 전하 극판 사이의 거리($W_{dep}$)에 정확히 <strong>반비례</strong>합니다.<br>
따라서 도핑 농도를 완만하게 하여 <strong>공핍층 폭($W_{dep}$)이 2배로 넓어지면, 기생 접합 커패시턴스($C_j$)는 정확히 절반($50\%$)으로 급감</strong>합니다.</p>

<div class="analogy-card">
  <div class="analogy-title">직관적 비유: '양극판을 멀리 떼어놓는 원리'</div>
  <div class="analogy-desc">자석 두 개(양전하와 음전하)를 바짝 붙여놓으면(급준 접합, 좁은 $W_{dep}$) 서로를 강하게 끌어당겨 정전용량($C_j$)이 매우 커집니다.<br>
하지만 자석 사이에 두꺼운 스펀지(완만한 도핑으로 넓어진 공핍층 $W_{dep}$)를 끼워 두 자석 사이의 거리를 멀리 떼어놓으면, 서로를 붙잡는 힘(정전 결합력)이 약해져 커패시턴스($C_j$)가 뚝 떨어지는 것과 같습니다.</div>
</div>

<h3>4. 반도체 회로에서의 공학적 가치: RC 지연 극복과 고속화</h3>
<p>MOSFET의 소스/드레인과 기판 사이의 접합 커패시턴스($C_j$)는 <strong>인버터 회로가 0에서 1로 스위칭할 때마다 충전하고 방전해야 하는 불필요한 기생 짐(Parasitic Load)</strong>입니다.</p>
<ul>
  <li>신호 전파 지연 시간: $\tau_{delay} \approx R_{channel} \times (C_{gate} + C_j + C_{wire})$</li>
  <li>$C_j$가 크면 충방전 시간이 길어져 칩의 동작 클록 주파수($f_{max}$)를 올릴 수 없습니다.</li>
  <li>따라서 현대 반도체는 소스/드레인 접합 경계면에 **LDD(Lightly Doped Drain) 및 완만한 도핑 프로파일(Graded Junction Profile)**을 설계함으로써, $C_j$를 획기적으로 낮추어 고속 스위칭과 저전력 동작을 달성합니다.</li>
</ul>"""
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 63 topics (q-63 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(63, 0, -1):
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
    old_desc_part = "총 63개 질문으로 구성되어 있습니다."
    new_desc_part = "최상단에는 '도핑농도 완화 시 공핍층 확장 및 Cj 감소 로직' 및 '채널농도와 전자이동도'가 위치하며, 총 64개 질문으로 구성되어 있습니다."
    if old_desc_part in html:
        html = html.replace(old_desc_part, new_desc_part)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 graded junction Cj topic!")
