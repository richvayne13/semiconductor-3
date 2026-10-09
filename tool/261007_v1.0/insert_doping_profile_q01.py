# -*- coding: utf-8 -*-
"""
insert_doping_profile_q01.py
사용자 질문: "doping profile이 왜중요해?"
대시보드 최상단 Q01로 신규 추가하고, 기존 59개 질문을 Q02~Q60으로 시프트 (총 60개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 물리 & 이온주입)",
    "title": "doping profile이 왜중요해?",
    "summary": [
        "도핑 프로파일(Doping Profile)은 <strong>'불순물이 실리콘 깊이($x$) 및 수평 방향에 따라 어떻게 농도 분포를 이루고 있는가($C(x)$)'</strong>를 나타내는 공간적 함수이며, 단순히 불순물의 총량(Dose)보다 <strong>소자의 물리적 동작을 지배하는 결정적 변수</strong>입니다.",
        "<strong>초얕은 접합 깊이($X_j$)와 급준도(Abruptness)</strong>: 프로파일의 깊이가 얕고 급격할수록 드레인 전계 침투(DIBL)와 지하 펀치스루를 차단하여 단채널 효과(SCE)를 방어할 수 있습니다.",
        "<strong>기생 커패시턴스($C_j$)와 스위칭 속도 트레이드오프</strong>: 접합부의 농도 기울기(Gradient)가 완만할수록 공핍층 폭($W_{dep}$)이 넓어져 기생 접합 커패시턴스가 감소하므로 고속 스위칭과 RC 지연 개선에 유리합니다.",
        "<strong>오믹 콘택트 vs 쇼트키 장벽 제어</strong>: 금속 배선 접촉 계면 최표면에서 $10^{20}\\,\\text{cm}^{-3}$ 이상의 고농도 프로파일을 형성해야만 공핍층이 $2\\,\\text{nm}$ 이하로 얇아져 양자역학적 터널링 오믹 콘택트가 가능해집니다."
    ],
    "svg_title": "📊 [도핑 프로파일 엔지니어링의 본질] 깊이별 농도 분포 $C(x)$가 소자 특성을 지배하는 메커니즘",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: Doping Profile Shape & Physical Parameters -->
  <rect x="20" y="25" width="365" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="50" fill="#38bdf8" font-size="12.5" font-weight="800">1. 도핑 프로파일 C(x)의 기하학적 파라미터</text>

  <!-- Coordinate axis -->
  <line x1="50" y1="230" x2="360" y2="230" stroke="#64748b" stroke-width="1.5"/>
  <line x1="50" y1="70" x2="50" y2="230" stroke="#64748b" stroke-width="1.5"/>
  <text x="320" y="250" fill="#94a3b8" font-size="10">깊이 x (Depth)</text>
  <text x="30" y="80" fill="#94a3b8" font-size="10">농도 C(x)</text>

  <!-- Background NB line -->
  <line x1="50" y1="205" x2="360" y2="205" stroke="#ef4444" stroke-width="1.2" stroke-dasharray="3,3"/>
  <text x="270" y="200" fill="#ef4444" font-size="9.5">기판 농도 (NB)</text>

  <!-- Profile A: Steep (Ultra-Shallow) -->
  <path d="M 50 85 Q 100 88 120 150 Q 130 190 140 205" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Profile B: Broad (Deep & Gentle) -->
  <path d="M 50 110 Q 150 115 220 160 Q 250 185 280 205" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,2"/>

  <!-- Annotations -->
  <circle cx="140" cy="205" r="4" fill="#38bdf8"/>
  <text x="110" y="222" fill="#38bdf8" font-size="10" font-weight="800">Xj (급준/초얕음)</text>

  <circle cx="280" cy="205" r="4" fill="#f59e0b"/>
  <text x="250" y="222" fill="#f59e0b" font-size="10" font-weight="800">Xj (완만/깊음)</text>

  <rect x="35" y="260" width="335" height="70" rx="4" fill="#1e293b"/>
  <text x="45" y="278" fill="#38bdf8" font-size="10" font-weight="700">① 급준 프로파일 (Steep, 청색 실선):</text>
  <text x="45" y="293" fill="#cbd5e1" font-size="9">• 얕은 Xj ➔ 단채널 효과(DIBL, Punch) 완벽 차단</text>
  <text x="45" y="308" fill="#f59e0b" font-size="10" font-weight="700">② 완만 프로파일 (Graded, 황색 점선):</text>
  <text x="45" y="323" fill="#cbd5e1" font-size="9">• 전계 완화(HCI 억제) & 공핍층 확장 ➔ 기생 Cj 감소</text>

  <!-- Right: 4 Pillars of Doping Profile Engineering -->
  <rect x="400" y="25" width="360" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
  <text x="415" y="50" fill="#10b981" font-size="12.5" font-weight="800">2. 도핑 프로파일이 결정하는 4대 소자 특성</text>

  <rect x="415" y="65" width="330" height="60" rx="4" fill="#1e293b"/>
  <text x="425" y="83" fill="#38bdf8" font-size="10.5" font-weight="700">1) 문턱전압(Vth) & 표면 캐리어 이동도</text>
  <text x="425" y="100" fill="#cbd5e1" font-size="9.5">• 채널 표면 농도가 Vth 결정 ($Q_{dep} \\propto \\sqrt{N_A}$)</text>
  <text x="425" y="115" fill="#34d399" font-size="9.5">• Retrograde 웰: 표면 저농도(이동도↑) + 지하 고농도(펀치스루 방어)</text>

  <rect x="415" y="132" width="330" height="60" rx="4" fill="#1e293b"/>
  <text x="425" y="150" fill="#f59e0b" font-size="10.5" font-weight="700">2) 단채널 효과(SCE) 방어와 초얕은 접합(USJ)</text>
  <text x="425" y="167" fill="#cbd5e1" font-size="9.5">• 접합 깊이($X_j$) 10nm 이하 축소로 드레인 전계 침투 차단</text>
  <text x="425" y="182" fill="#38bdf8" font-size="9.5">• 수평 급준도(nm/dec) 확보로 실효 채널 길이($L_{eff}$) 사수</text>

  <rect x="415" y="199" width="330" height="60" rx="4" fill="#1e293b"/>
  <text x="425" y="217" fill="#a855f7" font-size="10.5" font-weight="700">3) 기생 접합 커패시턴스(Cj) & 고주파 RC 지연</text>
  <text x="425" y="234" fill="#cbd5e1" font-size="9.5">• 접합부 농도 경사도($a = dN/dx$) 조절로 $W_{dep}$ 제어</text>
  <text x="425" y="249" fill="#a855f7" font-size="9.5">• $C_j = \\epsilon / W_{dep}$ 극소화 ➔ 인버터 스위칭 속도 극대화</text>

  <rect x="415" y="266" width="330" height="65" rx="4" fill="#1e293b"/>
  <text x="425" y="284" fill="#ef4444" font-size="10.5" font-weight="700">4) 오믹 콘택트 터널링 저항(Rc) 극소화</text>
  <text x="425" y="301" fill="#cbd5e1" font-size="9.5">• 최표면 축퇴 도핑($N > 10^{20}\\text{cm}^{-3}$) ➔ 쇼트키 장벽 폭 < 2nm</text>
  <text x="425" y="316" fill="#10b981" font-size="9.5">• 양자 터널링 유도로 접촉 저항($R_c$) 수십 Ω 이하 구현</text>
</svg>""",
    "lecture": r"""<h3>1. '도즈(Dose)'와 '도핑 프로파일(Doping Profile)'의 본질적 차이</h3>
<p>초보 엔지니어는 종종 "불순물을 많이 넣었는가, 적게 넣었는가(도즈량 $\Phi$ $[\text{cm}^{-2}]$)"에만 집중하지만, 반도체 물리에서 실제로 소자의 성능을 지배하는 것은 <strong>"불순물이 실리콘 깊이($x$)와 수평 방향으로 어떤 모양을 그리며 분포하는가(도핑 프로파일 $C(x)$ $[\text{cm}^{-3}]$)"</strong>입니다.</p>
<ul>
  <li><strong>도즈량(Dose)</strong>: 단위 면적당 주입된 총 불순물 원자 수(적분값: $\Phi = \int C(x) dx$)에 불과합니다.</li>
  <li><strong>도핑 프로파일(Profile)</strong>: 피크 위치(투영 사정거리 $R_p$), 분포 폭($\Delta R_p$), 접합 깊이($X_j$), 그리고 표면과 계면에서의 <strong>농도 기울기(Gradient, $\frac{dC}{dx}$)</strong>를 포함하는 입체적인 설계도입니다.</li>
</ul>

<h3>2. 도핑 프로파일이 결정적으로 중요한 5대 물리적 이유</h3>

<h4>① 단채널 효과(SCE) 억제와 초얕은 접합(USJ)</h4>
<p>채널 길이가 수십 나노미터로 짧아질 때, 소스/드레인(S/D)의 접합 깊이($X_j$)가 깊으면 드레인의 공핍 영역이 기판 깊은 곳을 통해 소스 쪽으로 쉽게 침범합니다(Charge Sharing 및 Punchthrough).<br>
도핑 프로파일의 <strong>접합 깊이($X_j$)를 10nm 이하로 극도로 얕게(Ultra-Shallow Junction)</strong> 만들고, 농도가 급격히 떨어지는 <strong>초급준 프로파일(Abrupt Profile: 수 nm/dec)</strong>을 형성해야만 게이트가 채널 전체를 완전하게 장악할 수 있습니다.</p>

<h4>② 문턱전압($V_{th}$) 제어와 캐리어 이동도 트레이드오프</h4>
<p>트랜지스터의 문턱전압 공식에서 공핍 전하량 $Q_{dep}$는 채널 표면 부근의 도핑 농도에 의해 결정됩니다 ($Q_{dep} = \sqrt{2q\epsilon_s N_A (2\phi_B)}$).<br>
과거처럼 균일한 도핑을 하면 $V_{th}$를 맞추기 위해 채널 농도를 높여야 했고, 이는 <strong>이온화 불순물 산란(Ionized Impurity Scattering)</strong>으로 전자 이동도($\mu$)를 심각하게 갉아먹었습니다.<br>
현대 반도체는 <strong>역역방향 웰(Retrograde Well) 프로파일</strong>을 적용하여, <strong>표면은 저농도로 유지해 전자 이동도($I_{on}$)를 극대화</strong>하고, <strong>채널 바로 아래 지하 수십 nm 지점에 고농도 피크를 배치하여 펀치스루를 차단</strong>하는 입체 프로파일 엔지니어링을 사용합니다.</p>

<h4>③ 기생 접합 커패시턴스($C_j$)와 스위칭 지연(RC Delay) 극복</h4>
<p>S/D과 기판 사이의 p-n 접합은 기생 커패시터로 동작합니다 ($C_j = \frac{\epsilon_s}{W_{dep}}$).<br>
도핑 프로파일이 계단형(Step Junction)으로 너무 급격하면 공핍층 폭($W_{dep}$)이 좁아져 $C_j$가 급증하고, 이는 인버터 회로의 충방전 속도를 늦춰 칩의 동작 주파수($f_{max}$)를 떨어뜨립니다.<br>
따라서 접합부의 도핑 농도 기울기(Gradient)를 완만하게 조절하는 <strong>경사 접합(Graded Junction) 프로파일</strong>을 통해 공핍층을 넓혀 기생 커패시턴스를 낮추는 최적화가 필수적입니다.</p>

<h4>④ 핫 캐리어 열화(HCI) 및 GIDL 누설 전류 제어 (LDD의 존재 이유)</h4>
<p>드레인 단의 도핑 프로파일이 $N^+$로 급격하면 푸아송 방정식($\frac{d\mathcal{E}}{dx} = \frac{qN}{\epsilon}$)에 의해 드레인 모서리에 초고전계 피크가 발생합니다. 이 전계 피크가 핫 캐리어 인젝션(HCI)과 게이트 유도 드레인 누설(GIDL)을 폭발시킵니다.<br>
이를 막기 위해 저농도 $N^-$ 영역을 완만한 프로파일로 삽입하는 <strong>LDD(Lightly Doped Drain) 프로파일</strong>을 설계하여 전계 피크를 완화합니다.</p>

<h4>⑤ 금속-실리콘 접촉 저항($R_c$)의 양자역학적 터널링 구현</h4>
<p>금속 배선과 소스/드레인이 만나는 최상부 표면에서는 쇼트키 전위 장벽($\Phi_B$)이 형성되어 전류가 흐르기 어렵습니다.<br>
표면 최외각 $1\sim2\,\text{nm}$ 영역의 도핑 프로파일을 $10^{20}\,\text{cm}^{-3}$ 이상의 고농도(축퇴 도핑)로 끌어올리면, 전위 장벽의 두께가 $2\,\text{nm}$ 이하로 얇아져 전자가 장벽을 뚫고 지나가는 <strong>양자역학적 전계 방출(Field Emission, 터널링 오믹 콘택트)</strong>이 일어납니다. 이를 통해 수십 옴 단위의 초저저항 콘택트를 완성할 수 있습니다.</p>

<h3>3. 마스터 총평</h3>
<p>도핑 프로파일은 반도체 소자에서 <strong>"건물의 철근 구조"</strong>와 같습니다. 불순물 원자의 3차원 위치와 농도 기울기($\nabla C$)를 1나노미터 단위로 정밀하게 제어하지 못하면, 아무리 첨단 EUV 노광과 하이케이 절연막을 써도 트랜지스터의 구동 속도, 누설 전류, 수율 마진을 단 하나도 확보할 수 없습니다.</p>"""
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 59 topics (q-59 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(59, 0, -1):
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
    old_desc_part = "총 59개 질문으로 구성되어 있습니다."
    new_desc_part = "최상단에는 'doping profile이 왜중요해?' 및 증착 4대 주제가 위치하며, 총 60개 질문으로 구성되어 있습니다."
    if old_desc_part in html:
        html = html.replace(old_desc_part, new_desc_part)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 doping profile topic!")
