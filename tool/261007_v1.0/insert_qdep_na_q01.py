# -*- coding: utf-8 -*-
"""
insert_qdep_na_q01.py
사용자 질문: "공핍전하량은 채널부근농도에 의해 결정되ㅣㄴ다는데 이게무슨뜻이야 NMOS로치면 채널부근농도면 P농도말하는건가"
대시보드 최상단 Q01로 신규 추가하고, 기존 61개 질문을 Q02~Q62로 시프트 (총 62개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 물리 & NMOS 채널)",
    "title": "공핍전하량이 채널 부근 농도에 의해 결정된다는 게 무슨 뜻이야? (NMOS의 P 도핑 농도 NA)",
    "nav_title": "공핍전하량이 채널 부근 농도에 의해 결정된다는 게 무슨 뜻이야?",
    "summary": [
        "질문자님의 직관이 100% 정확합니다! NMOS에서 전자가 흐르는 채널이 만들어지는 바탕 기판은 <strong>P형 실리콘 기판(또는 P-Well)</strong>이므로, '채널 부근 농도'는 바로 <strong>P형 억셉터 불순물(붕소, Boron)의 도핑 농도($N_A$)</strong>를 의미합니다.",
        "게이트에 양(+)의 전압을 걸면 채널 자리의 가벼운 정공($h^+$)들은 기판 아래로 도망가고, 실리콘 뼈대에 단단히 고정된 <strong>붕소 음이온($B^-$)</strong>들만 남아 음전하 영역을 형성하는데, 이 고정 전하의 총량이 <strong>공핍전하량($|Q_{dep}| = \\sqrt{2q\\epsilon_s N_A (2\\phi_B)}$)</strong>입니다.",
        "게이트가 전자를 모아 도통 채널(반전층)을 형성하기 전에 먼저 <strong>'공핍층 음이온 전하($Q_{dep}$)를 전기적으로 중화시키는 숙제'</strong>를 끝내야 하므로, 채널 부근의 P 도핑 농도($N_A$)가 높을수록 숙제량이 많아져 문턱전압($V_{th}$)이 비례하여 높아집니다.",
        "따라서 채널 표면 부근의 P 도핑 농도($N_A$)를 1나노미터 단위로 정밀 조절하는 것이 트랜지스터가 켜지는 시점($V_{th}$)과 전자 이동도($\\mu_n$), 기판 지하 펀치스루 방어를 조율하는 최핵심 설계 기법입니다."
    ],
    "svg_title": "📊 [NMOS 게이트 하부 공핍층 메커니즘] P형 기판(NA)의 정공 퇴출 ➔ 고정 붕소 음이온(B⁻) 전하 Qdep 형성",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: NMOS Cross-section & Depletion Charge Formation -->
  <rect x="20" y="25" width="375" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="50" fill="#38bdf8" font-size="12.5" font-weight="800">1. NMOS 게이트 전압 인가 시 공핍층 형성</text>

  <!-- Gate stack -->
  <rect x="110" y="65" width="180" height="25" fill="#334155" rx="3" stroke="#94a3b8"/>
  <text x="145" y="82" fill="#ffffff" font-size="11" font-weight="700">게이트 전극 (VG > 0)</text>
  <rect x="110" y="90" width="180" height="8" fill="#38bdf8" opacity="0.8"/>
  <text x="155" y="97" fill="#0f172a" font-size="7.5" font-weight="800">게이트 산화막 (Tox, Cox)</text>

  <!-- Silicon Substrate (P-type) -->
  <rect x="40" y="98" width="335" height="150" rx="4" fill="#1e293b"/>
  <text x="50" y="115" fill="#94a3b8" font-size="10">P형 실리콘 기판 (억셉터 농도 NA)</text>

  <!-- Source / Drain N+ -->
  <rect x="40" y="98" width="60" height="45" fill="#0284c7" opacity="0.6" rx="2"/>
  <text x="48" y="125" fill="#ffffff" font-size="10" font-weight="800">소스 N⁺</text>
  <rect x="300" y="98" width="75" height="45" fill="#0284c7" opacity="0.6" rx="2"/>
  <text x="312" y="125" fill="#ffffff" font-size="10" font-weight="800">드레인 N⁺</text>

  <!-- Depletion Region under gate -->
  <rect x="100" y="98" width="200" height="60" fill="#f59e0b" opacity="0.15" stroke="#f59e0b" stroke-dasharray="3,3"/>
  <!-- Fixed Boron negative ions B- -->
  <circle cx="130" cy="115" r="7" fill="#ef4444" opacity="0.8"/>
  <text x="126" y="119" fill="#ffffff" font-size="9" font-weight="900">-</text>
  <circle cx="170" cy="115" r="7" fill="#ef4444" opacity="0.8"/>
  <text x="166" y="119" fill="#ffffff" font-size="9" font-weight="900">-</text>
  <circle cx="210" cy="115" r="7" fill="#ef4444" opacity="0.8"/>
  <text x="206" y="119" fill="#ffffff" font-size="9" font-weight="900">-</text>
  <circle cx="250" cy="115" r="7" fill="#ef4444" opacity="0.8"/>
  <text x="246" y="119" fill="#ffffff" font-size="9" font-weight="900">-</text>

  <circle cx="150" cy="138" r="7" fill="#ef4444" opacity="0.8"/>
  <text x="146" y="142" fill="#ffffff" font-size="9" font-weight="900">-</text>
  <circle cx="190" cy="138" r="7" fill="#ef4444" opacity="0.8"/>
  <text x="186" y="142" fill="#ffffff" font-size="9" font-weight="900">-</text>
  <circle cx="230" cy="138" r="7" fill="#ef4444" opacity="0.8"/>
  <text x="226" y="142" fill="#ffffff" font-size="9" font-weight="900">-</text>

  <text x="135" y="152" fill="#f59e0b" font-size="9.5" font-weight="700">고정 붕소 음이온 공간 전하 Qdep</text>

  <!-- Pushed Holes -->
  <line x1="170" y1="165" x2="170" y2="195" stroke="#34d399" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="230" y1="165" x2="230" y2="195" stroke="#34d399" stroke-width="2"/>
  <text x="140" y="210" fill="#34d399" font-size="10" font-weight="700">정공(h⁺)들은 척력에 밀려 기판 아래로 도망</text>

  <!-- Depth dimension line -->
  <line x1="305" y1="98" x2="305" y2="158" stroke="#fbbf24" stroke-width="1.5"/>
  <text x="312" y="150" fill="#fbbf24" font-size="9.5">Wdep,max</text>

  <!-- Bottom Explanatory card -->
  <rect x="35" y="255" width="345" height="75" rx="4" fill="#1e293b"/>
  <text x="45" y="273" fill="#fbbf24" font-size="10" font-weight="700">★ 핵심 포인트: "채널 부근 농도"의 실체</text>
  <text x="45" y="290" fill="#cbd5e1" font-size="9">• NMOS는 전자가 흐르지만, 바탕 기판은 P형(NA) 실리콘!</text>
  <text x="45" y="305" fill="#f87171" font-size="9">• 남겨진 음이온들(B⁻)의 개수 밀도가 바로 P 도핑 농도 NA</text>
  <text x="45" y="320" fill="#34d399" font-size="9">• 따라서 공핍전하량 |Qdep|는 NA에 의해 100% 결정됨</text>

  <!-- Right: Mathematical Derivation & Vth Equation -->
  <rect x="410" y="25" width="350" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
  <text x="425" y="50" fill="#10b981" font-size="12.5" font-weight="800">2. 수식 관계: NA ➔ Qdep ➔ 문턱전압 Vth</text>

  <rect x="425" y="65" width="320" height="85" rx="4" fill="#1e293b"/>
  <text x="435" y="85" fill="#f59e0b" font-size="11" font-weight="700">① 최대 공핍층 폭 & 공핍전하량 공식</text>
  <text x="435" y="105" fill="#38bdf8" font-size="11" font-weight="700">Wdep,max = √[ 2 · εs · (2φB) / (q · NA) ]</text>
  <text x="435" y="128" fill="#34d399" font-size="11.5" font-weight="800">|Qdep| = q · NA · Wdep,max = √[ 2 · q · εs · NA · (2φB) ]</text>
  <text x="435" y="143" fill="#cbd5e1" font-size="8.5">• εs: 실리콘 유전율, φB = (kT/q)ln(NA/ni)</text>

  <rect x="425" y="160" width="320" height="90" rx="4" fill="#1e293b"/>
  <text x="435" y="180" fill="#a855f7" font-size="11" font-weight="700">② 문턱전압(Vth)과 공핍전하의 숙제</text>
  <text x="435" y="202" fill="#fbbf24" font-size="12" font-weight="800">Vth = VFB + 2φB + |Qdep| / Cox</text>
  <text x="435" y="222" fill="#cbd5e1" font-size="9.5">• 게이트가 전자를 끌어와 채널을 켜기 전에,</text>
  <text x="435" y="238" fill="#f87171" font-size="9.5">  음이온 전하(|Qdep|)를 상쇄시킬 전압(|Qdep|/Cox)을 먼저 소모!</text>

  <rect x="425" y="260" width="320" height="70" rx="4" fill="#1e293b"/>
  <text x="435" y="278" fill="#38bdf8" font-size="10.5" font-weight="700">③ 공학적 결론 (NA 엔지니어링)</text>
  <text x="435" y="295" fill="#cbd5e1" font-size="9.5">• NA ↑ ➔ |Qdep| ↑ ➔ Vth 증가 (켜기 어려워짐)</text>
  <text x="435" y="312" fill="#cbd5e1" font-size="9.5">• NA ↓ ➔ |Qdep| ↓ ➔ Vth 감소 (켜기 쉬워지나 펀치스루 위험)</text>
  <text x="435" y="325" fill="#34d399" font-size="8.5">➔ 따라서 표면 NA와 지하 NA를 다르게 설계(Retrograde)</text>
</svg>""",
    "lecture": r"""<h3>1. 질문의 본질: "NMOS인데 왜 채널 부근 농도가 P 농도인가요?"</h3>
<p>질문자님의 의문과 직관은 <strong>반도체 물리에서 가장 헷갈리기 쉬우면서도 핵심을 찌르는 지점</strong>입니다. 결론부터 명쾌하게 말씀드리면:</p>
<blockquote>
  <strong>"네, 100% 맞습니다! NMOS에서 채널 부근 농도는 기판의 P형 억셉터 도핑 농도($N_A$)를 말합니다."</strong>
</blockquote>
<p>왜 그런지 NMOS의 구조적 메커니즘을 짚어보겠습니다:</p>
<ul>
  <li><strong>소스/드레인</strong>은 전자가 가득 찬 <strong>$N^+$ 영역</strong>입니다.</li>
  <li>하지만 그 사이에 전자가 건너갈 다리(채널)가 놓일 <strong>바탕 기판(Substrate / P-Well)은 P형 실리콘($N_A$)</strong>입니다.</li>
  <li>평상시(게이트 전압 $V_G = 0$)에는 P형 기판에 다수 캐리어인 <strong>정공($h^+$)</strong>과 실리콘 격자에 단단히 박혀 못 움직이는 <strong>붕소 음이온($B^-$)</strong>이 공존하고 있어, 소스와 드레인 사이의 전자가 P형 기판의 전위 장벽에 막혀 건너가지 못합니다 (오프 상태).</li>
</ul>

<h3>2. 게이트에 (+) 전압을 걸었을 때 일어나는 2단계 물리 변화</h3>

<h4>[1단계] 정공 퇴출과 공핍층 형성 (음이온만 덩그러니 남음)</h4>
<p>NMOS를 켜기 위해 게이트에 양(+)의 전압을 걸면($V_G > 0$):</p>
<ol>
  <li>게이트 전극의 양전하와 기판의 정공($h^+$) 사이에 <strong>전기적 척력(밀어내는 힘)</strong>이 작용합니다.</li>
  <li>움직일 수 있는 가벼운 정공($h^+$)들은 기판 깊은 곳(바닥)으로 도망쳐 내려갑니다.</li>
  <li>정공이 떠난 자리(게이트 산화막 바로 아래 실리콘 표면)에는, 실리콘 원자 뼈대에 공유 결합으로 단단히 묶여 <strong>도망가지 못하는 억셉터 붕소 음이온($B^-$)들만 덩그러니 남게 됩니다</strong>.</li>
  <li>캐리어(전자, 정공)가 모두 고갈되어 텅 비어버린 이 영역을 <strong>공핍층(Depletion Region)</strong>이라 부르며, 여기에 갇힌 고정 음이온들의 총 전하량이 바로 <strong>공핍전하량($Q_{dep}$)</strong>입니다.</li>
</ol>

<h4>[2단계] 반전층(Inversion Layer, N 채널) 형성</h4>
<p>게이트 전압을 문턱전압($V_{th}$) 이상으로 더 높여주면, 비로소 소스/드레인에서 전도 전자들이 실리콘 표면으로 끌려와 얇은 <strong>전자 반전층(N 채널)</strong>을 형성하고 전류가 흐르기 시작합니다 (온 상태).</p>

<h3>3. 수식으로 보는 공핍전하량($Q_{dep}$)과 도핑 농도($N_A$)의 관계</h3>
<p>푸아송 방정식($\frac{d^2\phi}{dx^2} = -\frac{\rho}{\epsilon_s} = \frac{q N_A}{\epsilon_s}$)을 2번 적분하면, 표면 전위가 강반전 문턱($2\phi_B$)에 도달했을 때의 최대 공핍층 폭($W_{dep,max}$)과 단위 면적당 공핍 전하량($|Q_{dep}|$)이 유도됩니다:</p>
<div class="formula-box">$$W_{dep,max} = \sqrt{\frac{2 \epsilon_s (2\phi_B)}{q N_A}}$$</div>
<div class="formula-box">$$|Q_{dep}| = q \cdot N_A \cdot W_{dep,max} = \sqrt{2 q \epsilon_s N_A (2\phi_B)}$$</div>
<p>여기서 $\phi_B = \frac{k_B T}{q} \ln\left(\frac{N_A}{n_i}\right)$ 입니다.<br>
공식을 보면 $q$, $\epsilon_s$, $n_i$는 모두 물리적 상수이므로, <strong>공핍전하량 $|Q_{dep}|$의 크기를 결정하는 유일한 물리 변수는 채널 부근의 P형 도핑 농도 $N_A$뿐</strong>입니다!</p>

<div class="analogy-card">
  <div class="analogy-title">직관적 비유: '의자와 손님, 그리고 게이트의 숙제'</div>
  <div class="analogy-desc">P형 기판은 바닥에 볼트로 고정된 '음이온 의자($B^-$)'에 손님인 '정공($h^+$)'이 앉아있는 상태입니다. 게이트가 (+) 전압을 걸면 손님(정공)들이 쫓겨나고 <strong>'빈 의자($B^-$)들만 덩그러니 남은 방'</strong>이 공핍층입니다.<br>
게이트가 새로운 손님인 '전자(N 채널)'를 초대해 잔치를 열려면, 방에 남아있는 빈 의자들의 음전하($Q_{dep}$)를 먼저 상쇄시켜야 합니다. 즉, <strong>의자가 많을수록(P 농도 $N_A$가 높을수록) 게이트가 해야 할 숙제량($Q_{dep}$)이 커집니다!</strong></div>
</div>

<h3>4. 이것이 문턱전압($V_{th}$)을 결정하는 원리</h3>
<p>MOSFET의 문턱전압 공식은 다음과 같습니다:</p>
<div class="formula-box">$$V_{th} = V_{FB} + 2\phi_B + \frac{|Q_{dep}|}{C_{ox}}$$</div>
<ul>
  <li>$\frac{|Q_{dep}|}{C_{ox}}$ 항은 게이트가 반전층 전자를 모으기 전에, <strong>채널 자리의 고정 음이온 전하($|Q_{dep}|$)를 상쇄시키는 데 소모해야 하는 전압</strong>입니다.</li>
  <li><strong>채널 부근의 P 농도($N_A$)가 높으면</strong> $\rightarrow$ 공간에 갇힌 붕소 음이온 수가 많아져 $|Q_{dep}|$가 커짐 $\rightarrow$ 게이트가 음이온들을 제어하는 데 더 큰 전압을 써야 하므로 <strong>문턱전압($V_{th}$)이 상승</strong>합니다.</li>
  <li><strong>채널 부근의 P 농도($N_A$)가 낮으면</strong> $\rightarrow$ 음이온 수가 적어 $|Q_{dep}|$가 작아짐 $\rightarrow$ 적은 전압으로도 쉽게 켜져 <strong>문턱전압($V_{th}$)이 하강</strong>합니다.</li>
</ul>

<h3>5. 현대 반도체의 채널 엔지니어링: 왜 깊이별로 농도를 다르게 할까?</h3>
<p>과거에는 기판 전체의 $N_A$가 균일했지만, 최선단 공정에서는 <strong>채널 깊이에 따라 $N_A$를 다르게 설계(Retrograde Well / Counter Doping)</strong>합니다:</p>
<ol>
  <li><strong>실리콘 최표면 ($0 \sim 5\,\text{nm}$)</strong>: $N_A$ 농도를 의도적으로 낮춥니다. 불순물 산란을 줄여 전자의 이동도($\mu_n$)를 높이고 구동 전류($I_{on}$)를 극대화하며, $V_{th}$를 적절히 낮춥니다.</li>
  <li><strong>표면 바로 아래 지하 ($10 \sim 30\,\text{nm}$)</strong>: $N_A$ 농도를 급격히 높인 고농도 피크($P^+$ Pocket)를 만듭니다. 드레인의 공핍층이 기판 지하로 뻗어 나와 소스와 닿는 <strong>벌크 펀치스루(Punchthrough)를 원천 차단</strong>합니다.</li>
</ol>"""
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 61 topics (q-61 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(61, 0, -1):
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
    old_desc_part = "총 61개 질문으로 구성되어 있습니다."
    new_desc_part = "최상단에는 '공핍전하량과 채널부근 P농도 NA' 및 '면저항 역학'이 위치하며, 총 62개 질문으로 구성되어 있습니다."
    if old_desc_part in html:
        html = html.replace(old_desc_part, new_desc_part)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Qdep NA topic!")
