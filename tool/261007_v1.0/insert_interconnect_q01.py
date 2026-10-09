# -*- coding: utf-8 -*-
"""
insert_interconnect_q01.py
사용자 질문: "반도체에서 INTERCONNECT 고속다층배선이 뭔지 그림으로알려줘"
대시보드 최상단 Q01로 신규 추가하고, 기존 64개 질문을 Q02~Q65로 시프트 (총 65개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (BEOL 다층배선 & 고속화)",
    "title": "반도체에서 INTERCONNECT 고속다층배선이 뭔지 그림으로 알려줘",
    "nav_title": "반도체 INTERCONNECT 고속다층배선 구조와 원리",
    "summary": [
        "<strong>인터커넥트(Interconnect, 다층 금속 배선)</strong>는 실리콘 기판 위에 만들어진 수백억 개의 독립된 트랜지스터들을 전기적으로 연결하여 하나의 지능형 칩(CPU/GPU/NPU)으로 완성하는 <strong>'반도체의 3차원 입체 고속도로망'</strong>입니다.",
        "<strong>피라미드형 3단계 계층 구조</strong>: 하부 <strong>로컬 배선(M1~M3)</strong>은 이웃 트랜지스터를 촘촘히 잇고, 중간 <strong>세미글로벌(M4~M8)</strong>은 회로 블록을 연결하며, 최상층 <strong>글로벌 배선(Top Metal)</strong>은 굵고 넓은 구리 배선으로 칩 전체에 전력(VDD/VSS)과 고속 클록(Clock)을 저항 손실 없이 배분합니다.",
        "<strong>인터커넥트 병목과 RC 지연($\\tau = R \\cdot C$)</strong>: 공정이 미세화될수록 트랜지스터 자체의 스위칭 지연은 줄어들지만, 배선 폭 축소로 배선 저항($R$)과 인접선 간 기생 커패시턴스($C$)가 폭증하므로, <strong>구리(Cu, 저저항) + Low-k(저유전율) + 듀얼 다마신(Dual Damascene)</strong>으로 고속화를 달성합니다.",
        "차세대 2nm 이하 공정에서는 신호 배선과 전원 배선의 간섭을 끊어내기 위해, 웨이퍼 뒷면으로 전력선을 빼내는 <strong>후면 전력 공급망(BSPDN / Backside Power Delivery)</strong>으로 배선 병목을 돌파하고 있습니다."
    ],
    "svg_title": "📊 [반도체 고속 다층 인터커넥트 단면 입체도] Local / Semi-Global / Global 계층 구조 & RC 딜레이",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: Multi-level Interconnect Cross-Section Diagram -->
  <rect x="20" y="25" width="385" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="48" fill="#38bdf8" font-size="12" font-weight="800">1. 다층 금속 배선(BEOL) 3차원 계층 단면도</text>

  <!-- Global Metals (Top: M10~M12) -->
  <rect x="35" y="60" width="355" height="42" rx="4" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5"/>
  <rect x="50" y="66" width="135" height="28" fill="#d97706" rx="3"/>
  <text x="65" y="84" fill="#ffffff" font-size="10" font-weight="800">Global Cu (VDD/GND)</text>
  <rect x="210" y="66" width="160" height="28" fill="#d97706" rx="3"/>
  <text x="225" y="84" fill="#ffffff" font-size="10" font-weight="800">Global Clock Bus (저R)</text>
  <text x="35" y="58" fill="#fbbf24" font-size="8.5"></text>

  <!-- Vias down -->
  <rect x="100" y="102" width="20" height="15" fill="#f59e0b"/>
  <rect x="280" y="102" width="20" height="15" fill="#f59e0b"/>

  <!-- Semi-Global Metals (Middle: M4~M8) -->
  <rect x="35" y="117" width="355" height="42" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2"/>
  <rect x="45" y="123" width="70" height="22" fill="#0284c7" rx="2"/>
  <rect x="130" y="123" width="80" height="22" fill="#0284c7" rx="2"/>
  <rect x="230" y="123" width="70" height="22" fill="#0284c7" rx="2"/>
  <rect x="320" y="123" width="60" height="22" fill="#0284c7" rx="2"/>
  <text x="50" y="138" fill="#ffffff" font-size="9" font-weight="700">M6 (블록간 신호선: 중간 두께 & 중간 피치)</text>

  <!-- Vias down -->
  <rect x="75" y="159" width="14" height="14" fill="#38bdf8"/>
  <rect x="165" y="159" width="14" height="14" fill="#38bdf8"/>
  <rect x="260" y="159" width="14" height="14" fill="#38bdf8"/>

  <!-- Local Metals (Bottom: M1~M3) -->
  <rect x="35" y="173" width="355" height="40" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="1.2"/>
  <rect x="45" y="179" width="35" height="18" fill="#059669" rx="1.5"/>
  <rect x="90" y="179" width="35" height="18" fill="#059669" rx="1.5"/>
  <rect x="135" y="179" width="35" height="18" fill="#059669" rx="1.5"/>
  <rect x="180" y="179" width="35" height="18" fill="#059669" rx="1.5"/>
  <rect x="225" y="179" width="35" height="18" fill="#059669" rx="1.5"/>
  <rect x="270" y="179" width="35" height="18" fill="#059669" rx="1.5"/>
  <rect x="315" y="179" width="35" height="18" fill="#059669" rx="1.5"/>
  <text x="50" y="192" fill="#ffffff" font-size="8.5" font-weight="700">M1~M2 (극미세 로컬 배선, 피치 ~20nm)</text>

  <!-- MOL: Tungsten Plugs (Middle of Line) -->
  <rect x="52" y="213" width="12" height="18" fill="#94a3b8"/>
  <rect x="142" y="213" width="12" height="18" fill="#94a3b8"/>
  <rect x="232" y="213" width="12" height="18" fill="#94a3b8"/>
  <rect x="322" y="213" width="12" height="18" fill="#94a3b8"/>
  <text x="80" y="226" fill="#94a3b8" font-size="8.5">MOL 콘택트 플러그 (텅스텐 W / 몰리브덴 Mo)</text>

  <!-- FEOL: Transistors on Silicon -->
  <rect x="35" y="231" width="355" height="45" rx="3" fill="#0b1120" stroke="#64748b"/>
  <!-- FinFET fins -->
  <rect x="50" y="240" width="30" height="25" fill="#ef4444" rx="2"/>
  <rect x="140" y="240" width="30" height="25" fill="#ef4444" rx="2"/>
  <rect x="230" y="240" width="30" height="25" fill="#ef4444" rx="2"/>
  <rect x="320" y="240" width="30" height="25" fill="#ef4444" rx="2"/>
  <text x="95" y="256" fill="#fca5a5" font-size="9" font-weight="800">FEOL 트랜지스터 층 (FinFET / GAA 나노시트)</text>

  <!-- Annotations at bottom -->
  <rect x="35" y="285" width="355" height="50" rx="4" fill="#1e293b"/>
  <text x="45" y="302" fill="#38bdf8" font-size="9.5" font-weight="700">★ 계층 구조의 본질: '피라미드형 두께 스케일링'</text>
  <text x="45" y="318" fill="#cbd5e1" font-size="8.5">• 하부(M1): 촘촘한 트랜지스터 배선 (고밀도 우선, 높은 R 감수)</text>
  <text x="45" y="330" fill="#fbbf24" font-size="8.5">• 상부(Top): 장거리 고속 신호/전력선 (두껍고 넓어 R·RC지연 극소화)</text>

  <!-- Right: RC Delay Bottleneck & Dual Damascene -->
  <rect x="420" y="25" width="340" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
  <text x="435" y="48" fill="#10b981" font-size="12" font-weight="800">2. RC 지연 병목과 듀얼 다마신 고속화 혁신</text>

  <!-- Box 1: RC Bottleneck Law -->
  <rect x="435" y="60" width="310" height="110" rx="4" fill="#1e293b"/>
  <text x="445" y="78" fill="#f87171" font-size="10.5" font-weight="700">인터커넥트 병목 (Interconnect Bottleneck)</text>
  <text x="445" y="98" fill="#38bdf8" font-size="11.5" font-weight="800">신호 지연 시간: τ = R_wire · C_wire</text>
  <text x="445" y="116" fill="#cbd5e1" font-size="9">• 트랜지스터 크기 축소 ➔ 게이트 지연은 급감 (속도↑)</text>
  <text x="445" y="131" fill="#f87171" font-size="9">• 배선 선폭 축소 ➔ 배선 저항(R) 폭증 + 커패시턴스(C) 증가</text>
  <text x="445" y="146" fill="#fbbf24" font-size="9.5" font-weight="700">➔ 현대 반도체 성능의 70%는 배선 지연이 좌우!</text>

  <!-- Box 2: 3 Major Solutions -->
  <rect x="435" y="180" width="310" height="155" rx="4" fill="#1e293b"/>
  <text x="445" y="198" fill="#10b981" font-size="10.5" font-weight="700">고속 다층 배선 3대 핵심 솔루션</text>
  <text x="445" y="218" fill="#f59e0b" font-size="10" font-weight="700">1) Al ➔ Cu 전면 교체 (구리 다마신 공정)</text>
  <text x="445" y="233" fill="#cbd5e1" font-size="8.5">• 비저항 40% 절감 (1.7 vs 2.7 μΩ·cm), 일렉트로마이그레이션 극복</text>
  <text x="445" y="253" fill="#38bdf8" font-size="10" font-weight="700">2) Low-k 절연막 도입 (SiCOH, k < 2.5)</text>
  <text x="445" y="268" fill="#cbd5e1" font-size="8.5">• 배선 사이 기생 정전용량(C)을 깎아 신호 혼선(Crosstalk) 차단</text>
  <text x="445" y="288" fill="#a855f7" font-size="10" font-weight="700">3) 차세대: 후면 전력 공급망 (BSPDN / PowerVia)</text>
  <text x="445" y="303" fill="#cbd5e1" font-size="8.5">• 웨이퍼 앞면은 고속 신호선 전용, 뒷면은 전원 공급 전용 분리</text>
  <text x="445" y="318" fill="#34d399" font-size="8.5">➔ 전압 강하(IR-Drop) 30% 개선, 클록 속도 15% 추가 향상</text>
</svg>""",
    "lecture": r"""<h3>1. 반도체 인터커넥트(Interconnect)란 무엇인가?</h3>
<p>트랜지스터를 '도시의 개별 주택'에 비유한다면, <strong>인터커넥트(Interconnect, 상호연결 배선)는 집과 집, 빌딩과 공장을 연결하는 '도시 전체의 입체 도로 및 전력 통신망'</strong>입니다.</p>
<ul>
  <li>최신 첨단 반도체(예: 엔비디아 Blackwell GPU, 애플 A18, 인텔 CPU)에는 실리콘 기판 표면에 <strong>수백억~천억 개 이상의 트랜지스터</strong>가 집적됩니다.</li>
  <li>하지만 트랜지스터 혼자서는 아무런 연산도 할 수 없습니다. 이 트랜지스터들이 전선으로 엮여 AND, OR, 메모리 레지스터, 산술논리연산장치(ALU)를 구성해야 비로소 하나의 칩이 작동합니다.</li>
  <li>이 수천억 개의 연결선을 1층에만 깔면 면적이 부족하여 칩 크기가 수 미터로 커져야 하므로, <strong>아파트처럼 위로 12~20층까지 층층이 쌓아 올린 3차원 금속 배선 시스템</strong>을 **'고속 다층 배선(Multi-Level Metallization / Interconnect)'**이라 부릅니다.</li>
</ul>

<h3>2. 왜 위로 갈수록 굵어지는가? (피라미드형 3단계 계층 구조)</h3>
<p>다층 배선 단면 전자현미경(TEM) 사진을 보면, 아래층은 머리카락 수만 분의 1로 가늘고 빽빽하지만, <strong>위층으로 올라갈수록 배선이 거대해지는 피라미드 구조</strong>를 띱니다:</p>

<h4>① 로컬 배선 (Local Interconnect: M1 ~ M3)</h4>
<ul>
  <li><strong>역할</strong>: 바로 이웃한 트랜지스터들의 게이트, 소스, 드레인을 연결하는 단거리 모세혈관.</li>
  <li><strong>특징</strong>: 집적도가 생명이므로 선폭이 $20\,\text{nm}$ 미만으로 극도로 좁습니다. 선폭이 좁아 저항($R$)이 높지만, 이동 거리가 수백 nm로 매우 짧아 저항 손실이 소자에 큰 영향을 주지 않습니다.</li>
</ul>

<h4>② 세미 글로벌 배선 (Semi-Global Interconnect: M4 ~ M8)</h4>
<ul>
  <li><strong>역할</strong>: 코어(Core), 캐시 메모리(SRAM), 연산기 등 기능 블록과 블록 사이를 연결하는 간선 도로.</li>
  <li><strong>특징</strong>: 중간 정도의 두께와 선폭을 가지며, 적절한 저항과 밀도를 절충합니다.</li>
</ul>

<h4>③ 글로벌 배선 (Global Interconnect: Top Metal / M9 ~ M15+)</h4>
<ul>
  <li><strong>역할</strong>: 칩 전체에 거대한 전원(VDD)과 접지(VSS)를 공급하고, 칩 전체의 심장 박동 역할을 하는 <strong>초고속 클록 신호(Clock Tree)</strong>를 1cm 이상의 장거리로 전달하는 고속도로망.</li>
  <li><strong>특징</strong>: 선폭과 두께를 하부 배선 대비 <strong>수십 배 크고 두껍게(Thick & Wide Metal)</strong> 제작합니다. 장거리를 달려도 <strong>배선 저항($R = \rho \frac{L}{A}$)을 극소화</strong>하여 전압 강하(IR Drop)와 신호 왜곡을 완벽히 차단합니다.</li>
</ul>

<h3>3. '인터커넥트 병목(Interconnect Bottleneck)'과 RC 지연</h3>
<p>과거에는 반도체 속도를 트랜지스터 자체의 켜고 끄는 속도(게이트 지연, $\tau_{gate}$)가 결정했습니다.<br>
그러나 선폭이 10nm 이하로 미세화되면서 치명적인 물리적 역전 현상이 일어났습니다:</p>

<div class="formula-box">$$\tau_{\text{wire}} = R_{\text{wire}} \times C_{\text{wire}} = \left( \rho \frac{L}{W \cdot t} \right) \times \left( \epsilon \frac{L \cdot t}{S} \right) = \rho \epsilon \frac{L^2}{W \cdot S}$$</div>
<ul>
  <li>트랜지스터가 작아지면 트랜지스터 속도는 빨라집니다 ($\tau_{gate} \downarrow$).</li>
  <li>하지만 배선 폭($W$)과 간격($S$)이 줄어들면, <strong>배선 저항($R$)은 단면적 감소로 급증</strong>하고 <strong>인접 배선 간 기생 커패시턴스($C$)는 간격 축소로 급증</strong>합니다.</li>
  <li>그 결과 <strong>배선 신호 전달 지연($RC$ 지연)이 칩 전체 지연의 70% 이상을 차지</strong>하는 **'인터커넥트 병목'**이 도래했습니다.</li>
</ul>

<h3>4. 인터커넥트 고속화를 위한 3대 혁신 기술</h3>

<h4>① 알루미늄(Al)에서 구리(Cu)로의 전면 교체 (듀얼 다마신 공정)</h4>
<p>과거의 알루미늄($2.7\,\mu\Omega\cdot\text{cm}$)을 버리고, 비저항이 40% 낮은 <strong>구리($1.7\,\mu\Omega\cdot\text{cm}$)</strong>를 도입했습니다. 구리는 식각이 불가능하여, 절연막에 도랑(트렌치)과 구멍(비아)을 먼저 파고 구리를 도금한 뒤 깎아내는 <strong>듀얼 다마신(Dual Damascene) 공정</strong>이 반도체 다층 배선의 표준이 되었습니다.</p>

<h4>② Low-k (저유전율) 절연막 도입</h4>
<p>배선과 배선 사이에 채우는 절연막으로 기존 $\text{SiO}_2$($k \approx 4.0$) 대신, 탄소와 수소를 첨가한 다공성 <strong>SiCOH ($k \approx 2.2 \sim 2.5$)</strong>를 적용하여 배선 간 정전용량($C$)을 깎아내고 신호 간섭(Crosstalk 노이즈)을 차단했습니다.</p>

<h4>③ 차세대 궁극의 혁신: 후면 전력 공급망 (BSPDN / Backside Power Delivery)</h4>
<p>신호선과 전원선이 앞면에 뒤엉켜 생기는 병목을 해결하기 위해, 인텔(PowerVia)과 TSMC(A16), 삼성이 2nm 공정부터 도입하는 혁신입니다.<br>
웨이퍼를 극도로 얇게 연마한 뒤 <strong>굵은 전원선(Power Rail)을 웨이퍼 뒷면(Backside)으로 완전히 분리</strong>시킵니다. 앞면은 순수 고속 신호선만 100% 빽빽하게 깔아 <strong>신호 속도를 15% 이상 높이고 칩 면적을 20% 이상 절감</strong>합니다.</p>"""
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 64 topics (q-64 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(64, 0, -1):
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
    old_desc_part = "총 64개 질문으로 구성되어 있습니다."
    new_desc_part = "최상단에는 '반도체 INTERCONNECT 고속다층배선 구조' 및 '도핑농도와 공핍층 Cj 로직'이 위치하며, 총 65개 질문으로 구성되어 있습니다."
    if old_desc_part in html:
        html = html.replace(old_desc_part, new_desc_part)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 interconnect topic!")
