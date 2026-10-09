# -*- coding: utf-8 -*-
"""
insert_hbm_16stack_2048bit_q01.py
사용자 질문: "나 아직 HBM에서 16단적층 2048BIT 이게 그림상으로 이해가안돼 대역폭이뭐고 비트수가뭐고 버스선이뭐고 자세히알려줘"
대시보드 최상단 Q01로 신규 추가하고, 기존 66개 질문을 Q02~Q67로 시프트 (총 67개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (HBM 심층 구조 & 대역폭)",
    "title": "HBM 16단 적층과 2048-bit 버스선, 대역폭 개념 완전 정복 (그림 해설)",
    "nav_title": "HBM 16단 적층과 2048-bit 버스선, 대역폭 개념 완전 정복",
    "summary": [
        "<strong>비트 수(Bus Width, 버스 폭)</strong>는 <strong>'동시에 데이터를 실어 나르는 도로의 차선 수'</strong>이며, <strong>2048-bit</strong>는 GPU와 HBM 사이에 물리적인 구리 전선(버스선)이 <strong>실제로 2048가닥</strong>이나 깔려 있어 한 번에 2048개의 0과 1을 동시에 쏟아붓는다는 뜻입니다 (일반 GDDR은 32차선, DDR5는 64차선).",
        "<strong>대역폭(Bandwidth = 차선 수 × 주파수 × 2)</strong>은 <strong>'1초 동안 쏟아져 나오는 데이터의 총 부피(초당 전송량, TB/s)'</strong>입니다. 차선이 32개뿐이면 차들을 미친 듯이 과속(초고클록)시켜야 해서 발열이 폭증하지만, HBM은 2048차선 초대형 고속도로를 깔아 적당한 속도로도 <strong>초당 3TB 이상의 데이터를 폭포수처럼 전송</strong>합니다.",
        "<strong>16단 적층(16-High Stacking)</strong>은 DRAM 다이 16장을 두께 약 30㎛(머리카락의 1/3)로 얇게 갈아낸 뒤 <strong>16층 아파트처럼 위로 차곡차곡 쌓은 물리적 구조</strong>입니다. 옆으로 늘어놓지 않고 위로 쌓아 면적을 극소화하고 GPU와의 물리적 거리를 극단적으로 단축시킵니다.",
        "<strong>수직 관통 엘리베이터(TSV)</strong>: 16개 층마다 수만 개의 미세 구멍을 뚫어 구리 기둥(TSV)을 박아 16층부터 1층 베이스 다이까지 직결하며, 실리콘 인터포저를 통해 2048개의 신호선이 GPU와 초광대역으로 통신합니다."
    ],
    "svg_title": "📊 [HBM 16단 적층 & 2048-bit 버스 아키텍처] 16층 수직 TSV 엘리베이터 & 2048차선 대역폭 비교",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: 16-High Stacking Architecture Diagram -->
  <rect x="20" y="25" width="380" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="48" fill="#38bdf8" font-size="12" font-weight="800">1. HBM4 16단 수직 적층 (16-High Stack) 구조</text>

  <!-- 16 Stack DRAM Dies representation -->
  <!-- 16 layers sketched -->
  <g transform="translate(180, 58)">
    <!-- Dies 16 to 1 stacked -->
    <!-- Loop-like layers -->
    <rect x="0" y="0" width="200" height="7" fill="#38bdf8" rx="1"/>
    <text x="205" y="7" fill="#94a3b8" font-size="8">16층 (Top Die)</text>
    <rect x="0" y="9" width="200" height="7" fill="#0284c7" rx="1"/>
    <rect x="0" y="18" width="200" height="7" fill="#38bdf8" rx="1"/>
    <rect x="0" y="27" width="200" height="7" fill="#0284c7" rx="1"/>
    <rect x="0" y="36" width="200" height="7" fill="#38bdf8" rx="1"/>
    <rect x="0" y="45" width="200" height="7" fill="#0284c7" rx="1"/>
    <rect x="0" y="54" width="200" height="7" fill="#38bdf8" rx="1"/>
    <rect x="0" y="63" width="200" height="7" fill="#0284c7" rx="1"/>
    <rect x="0" y="72" width="200" height="7" fill="#38bdf8" rx="1"/>
    <rect x="0" y="81" width="200" height="7" fill="#0284c7" rx="1"/>
    <rect x="0" y="90" width="200" height="7" fill="#38bdf8" rx="1"/>
    <rect x="0" y="99" width="200" height="7" fill="#0284c7" rx="1"/>
    <rect x="0" y="108" width="200" height="7" fill="#38bdf8" rx="1"/>
    <rect x="0" y="117" width="200" height="7" fill="#0284c7" rx="1"/>
    <rect x="0" y="126" width="200" height="7" fill="#38bdf8" rx="1"/>
    <rect x="0" y="135" width="200" height="7" fill="#0284c7" rx="1"/>
    <text x="205" y="142" fill="#94a3b8" font-size="8">1층 DRAM Core</text>

    <!-- Vertical TSV Columns piercing all 16 layers -->
    <line x1="30" y1="0" x2="30" y2="145" stroke="#f59e0b" stroke-width="2.5"/>
    <line x1="70" y1="0" x2="70" y2="145" stroke="#f59e0b" stroke-width="2.5"/>
    <line x1="120" y1="0" x2="120" y2="145" stroke="#f59e0b" stroke-width="2.5"/>
    <line x1="170" y1="0" x2="170" y2="145" stroke="#f59e0b" stroke-width="2.5"/>

    <!-- Base Logic Die (Buffer) -->
    <rect x="0" y="146" width="200" height="18" fill="#10b981" rx="2"/>
    <text x="35" y="159" fill="#ffffff" font-size="9" font-weight="800">Base Logic Die (제어 완충 기저 다이)</text>
  </g>

  <!-- Left Annotation for GPU & TSV -->
  <!-- AI GPU on Interposer -->
  <rect x="35" y="125" width="115" height="75" fill="#6366f1" rx="4"/>
  <text x="55" y="160" fill="#ffffff" font-size="12" font-weight="900">AI GPU</text>
  <text x="45" y="180" fill="#c7d2fe" font-size="9">(H100 / B200)</text>

  <!-- 2.5D Silicon Interposer (Substrate) -->
  <rect x="35" y="228" width="350" height="20" fill="#334155" stroke="#38bdf8" stroke-width="1.5" rx="2"/>
  <text x="45" y="242" fill="#38bdf8" font-size="9.5" font-weight="800">2.5D 실리콘 인터포저: 2048가닥 버스선 (선폭 &lt; 1μm)</text>

  <!-- High speed bus line connecting GPU and HBM -->
  <line x1="150" y1="210" x2="180" y2="230" stroke="#f59e0b" stroke-width="3"/>
  <line x1="90" y1="200" x2="90" y2="228" stroke="#38bdf8" stroke-width="2"/>
  <line x1="280" y1="222" x2="280" y2="228" stroke="#f59e0b" stroke-width="2"/>

  <!-- Explanatory note at bottom -->
  <rect x="35" y="258" width="350" height="75" rx="4" fill="#1e293b"/>
  <text x="45" y="275" fill="#fbbf24" font-size="10" font-weight="700">★ 16단 적층의 본질:</text>
  <text x="45" y="291" fill="#cbd5e1" font-size="8.5">• DRAM 16장을 30μm 두께로 갈아내 16층 빌딩처럼 수직 적층</text>
  <text x="45" y="306" fill="#34d399" font-size="8.5">• 수천 개 TSV(황색 기둥)가 16층을 수직 관통하는 초고속 엘리베이터!</text>
  <text x="45" y="322" fill="#38bdf8" font-size="8.5">• 평면 분산 배치 대비 면적 90% 절감 & 신호 이동거리 극소화</text>

  <!-- Right: 2048-bit Bus Width & Bandwidth Analogy -->
  <rect x="415" y="25" width="345" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
  <text x="430" y="48" fill="#10b981" font-size="12" font-weight="800">2. 2048-BIT 버스선과 대역폭(Bandwidth) 비유</text>

  <!-- Comparison Box: GDDR vs HBM4 -->
  <rect x="430" y="60" width="315" height="115" rx="4" fill="#1e293b"/>
  <text x="440" y="78" fill="#f87171" font-size="10.5" font-weight="700">[GDDR6: 32-bit 좁은 도로의 한계]</text>
  <text x="440" y="96" fill="#cbd5e1" font-size="9">• 차선 수: 32차선 (물리 전선 32가닥)</text>
  <text x="440" y="110" fill="#fca5a5" font-size="9">• 대역폭 늘리려 차를 시속 300km(초고주파)로 과속 ➔ 발열 폭발</text>
  <text x="440" y="126" fill="#34d399" font-size="10.5" font-weight="700">[HBM4: 2048-bit 초대형 고속도로]</text>
  <text x="440" y="144" fill="#cbd5e1" font-size="9">• 차선 수: 2048차선 (동시에 2048개 데이터 쏟아짐)</text>
  <text x="440" y="160" fill="#38bdf8" font-size="9">• 시속 100km로 안전하게 달려도 1초에 3TB 화물 쏟아냄!</text>

  <!-- Bandwidth Formula Card -->
  <rect x="430" y="185" width="315" height="150" rx="4" fill="#1e293b"/>
  <text x="440" y="205" fill="#fbbf24" font-size="11" font-weight="800">대역폭(Bandwidth) 공식과 물리적 의미</text>
  <text x="440" y="228" fill="#34d399" font-size="12" font-weight="800">대역폭 = 버스 폭(차선 수) × 클록 주파수 × 2(DDR)</text>

  <text x="440" y="250" fill="#38bdf8" font-size="10" font-weight="700">• HBM3: 1024-bit × 6.4 Gbps ÷ 8 = 819 GB/s</text>
  <text x="440" y="268" fill="#ef4444" font-size="10" font-weight="700">• HBM4: 2048-bit × 10 Gbps ÷ 8 = 2.5 ~ 3.3 TB/s !!</text>
  <text x="440" y="288" fill="#cbd5e1" font-size="8.5">• 비트 수: 한 번에 건너가는 데이터 선로의 가닥 수</text>
  <text x="440" y="302" fill="#cbd5e1" font-size="8.5">• 버스선: 인터포저 표면에 새겨진 실제 2048가닥 구리선</text>
  <text x="440" y="318" fill="#10b981" font-size="9" font-weight="800">➔ 대역폭: 1초 동안 쏟아져 나오는 데이터의 총 부피(물동량)</text>
</svg>""",
    "lecture": r"""<h3>1. 가장 직관적인 비유: '고속도로 차선'과 '물류 트럭'</h3>
<p>머릿속에 다음 그림 하나만 먼저 떠올려보세요:</p>
<ul>
  <li><strong>비트 수 (Bit 수 = 버스 폭 / Bus Width)</strong>:
    <br><strong>"데이터가 지나갈 수 있는 도로의 차선 수"</strong>입니다.
    1-bit는 0 또는 1이라는 데이터 상자 1개입니다. 32-bit는 32차선 도로이고, <strong>2048-bit는 무려 2048차선으로 뚫린 태평양 같은 초대형 고속도로</strong>입니다.</li>
  <li><strong>버스선 (Bus Line)</strong>:
    <br><strong>"실제로 도로에 깔려 있는 구리 전선의 가닥 수"</strong>입니다.
    2048-bit라는 것은 말로만 그런 것이 아니라, GPU와 HBM 사이에 데이터를 주고받는 <strong>실제 구리 전선이 물리적으로 2048가닥</strong>이 연결되어 있다는 뜻입니다.</li>
  <li><strong>클록 (Clock Frequency / 동작 속도)</strong>:
    <br><strong>"트럭들이 달리는 주행 속도 (시속)"</strong>입니다. 1초에 신호가 몇 번 깜빡이며 데이터를 실어 나르는지를 나타냅니다.</li>
  <li><strong>대역폭 (Bandwidth)</strong>:
    <br><strong>"1초 동안 톨게이트를 통과하여 쏟아져 나오는 화물의 총 부피(초당 전송량, GB/s 또는 TB/s)"</strong>입니다.</li>
</ul>

<div class="data-table-wrap">
  <table class="data-table">
    <thead>
      <tr>
        <th>메모리 종류</th>
        <th>버스 폭 (차선 수)</th>
        <th>동작 속도 (차량 속도)</th>
        <th>1초당 쏟아지는 대역폭 (물동량)</th>
        <th>물리적 특성 및 한계</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>일반 PC (DDR5)</strong></td>
        <td><strong>64-bit</strong> (64차선)</td>
        <td>보통 속도</td>
        <td>약 <strong>50 ~ 60 GB/s</strong></td>
        <td>사무용/게임용 PC 표준</td>
      </tr>
      <tr>
        <td><strong>그래픽카드 (GDDR6)</strong></td>
        <td><strong>32-bit</strong> (32차선 좁은 길)</td>
        <td>초고속 질주 (시속 300km)</td>
        <td>약 <strong>80 ~ 90 GB/s</strong></td>
        <td>차선이 좁아 과속(초고주파)해야 함 ➔ 발열 폭발로 한계 도달</td>
      </tr>
      <tr>
        <td><strong>HBM3E</strong></td>
        <td><strong>1024-bit</strong> (1024차선)</td>
        <td>적당한 속도 (시속 100km)</td>
        <td>약 <strong>1.2 TB/s</strong> (초당 1200GB!)</td>
        <td>차선이 1024개라 천천히 달려도 엄청난 양 쏟아짐</td>
      </tr>
      <tr>
        <td><strong>HBM4 (차세대)</strong></td>
        <td><strong>2048-bit</strong> (2048차선 활주로!)</td>
        <td>안정적 고속 주행</td>
        <td>약 <strong>2.5 ~ 3.3 TB/s</strong> (초당 3000GB 이상!)</td>
        <td>차선 수를 2배로 확장하여 AI GPU의 갈증을 완벽 해결</td>
      </tr>
    </tbody>
  </table>
</div>

<h3>2. 수식으로 이해하는 대역폭 (Bandwidth) 공식</h3>
<div class="formula-box">$$\text{대역폭(Bandwidth)} = \frac{\text{버스 폭 (Bit 수)} \times \text{동작 주파수 (Data Rate)} \times 2(\text{DDR})}{8 \text{ (Byte 환산)}}$$</div>
<ul>
  <li>GDDR은 버스 폭이 32개밖에 안 되기 때문에 대역폭을 늘리려면 주파수(클록)를 미친 듯이 올려야 하고, 이는 전기적 저항 발열 때문에 한계에 부딪혔습니다.</li>
  <li>반면 <strong>HBM4는 버스 폭을 2048-bit로 2배 넓혀버렸기 때문에</strong>, 주파수를 무리하게 올리지 않고도 1초에 <strong>FHD 영화 800편 분량의 데이터($3\,\text{TB}$)를 단 1초 만에 쏟아부을 수 있는 것</strong>입니다.</li>
</ul>

<h3>3. 16단 적층(16-High Stacking)이란 그림상으로 어떻게 생긴 것인가?</h3>
<p>DRAM 칩 16장을 평면 바닥에 나란히 늘어놓는다고 상상해 보세요:</p>
<ol>
  <li><strong>바닥에 늘어놓을 때의 문제점</strong>:
    <br>기판 면적이 손바닥만큼 커지고, 맨 끝에 있는 DRAM은 GPU와의 거리가 멀어져 신호가 오가는 데 한참 걸립니다(레이턴시 지연). 또한 2048가닥의 전선이 바닥에서 서로 엉키고 교차하여 신호 혼선(Crosstalk)이 발생합니다.</li>
  <li><strong>16층 빌딩으로 위로 쌓는 원리</strong>:
    <br>DRAM 웨이퍼를 물리적으로 갈아내어 <strong>두께를 머리카락의 3분의 1 수준인 약 $30\,\mu\text{m}$로 종이처럼 얇게 만듭니다</strong>.
    그리고 이 얇은 DRAM 칩을 <strong>1층부터 16층까지 위로 차곡차곡 포개어 올립니다</strong>. 이것이 바로 <strong>16단 적층(16-High Stacking)</strong>입니다.</li>
  <li><strong>수직 관통 엘리베이터 (TSV: Through-Silicon Via)</strong>:
    <br>아파트 16층에서 1층으로 내려가려면 복도를 빙빙 도는 계단보다 <strong>직통 수직 엘리베이터</strong>를 타는 것이 가장 빠릅니다.
    DRAM 칩 1장마다 수만 개의 미세한 구멍을 뚫고 구리 기둥(TSV)을 채워 넣습니다.
    이 수직 구리 기둥들이 16층부터 1층까지 직통으로 관통하여, 16장의 칩에 저장된 데이터가 수직 엘리베이터를 타고 <strong>단 1나노초도 안 되는 시간에 1층 베이스 다이(Base Logic Die)로 쏟아져 내려옵니다</strong>.</li>
</ol>

<h3>4. 2048가닥의 버스선은 도대체 어디에 깔려 있는가?</h3>
<p>일반 녹색 인쇄회로기판(PCB)은 선폭이 $20\,\mu\text{m}$로 굵어서 2048가닥의 선을 깔면 배선 폭만 손바닥만 해집니다.<br>
이를 해결하기 위해 반도체 노광 공정으로 선폭을 <strong>$1\,\mu\text{m}$ 미만으로 미세하게 깎아 만든 2.5D 실리콘 인터포저(Silicon Interposer)</strong>라는 특수 발판을 깔았습니다.<br>
이 얇은 실리콘 발판 위에 머리카락 수백 분의 1 굵기의 초미세 구리선 <strong>2048가닥</strong>이 자로 잰 듯 반듯하게 깔려 있어, AI GPU와 HBM 베이스 다이를 1대1로 초고속 직결하고 있습니다.</p>

<h3>5. 한 줄 마스터 요약</h3>
<blockquote>
  <strong>"16단 적층은 16층 아파트처럼 DRAM을 위로 얇게 쌓아 초고속 수직 엘리베이터(TSV)로 뚫어놓은 것이고, 2048-bit는 GPU와 HBM 사이에 데이터를 콸콸 쏟아붓는 도로 차선(구리 배선)이 2048가닥이나 뚫려 있어 초당 3TB의 데이터 폭포수(대역폭)를 뿜어내는 구조입니다!"</strong>
</blockquote>"""
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 66 topics (q-66 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(66, 0, -1):
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
    old_desc_part = "총 66개 질문으로 구성되어 있습니다."
    new_desc_part = "최상단에는 'HBM 16단 적층과 2048-bit 버스선, 대역폭 개념 완전 정복'이 위치하며, 총 67개 질문으로 구성되어 있습니다."
    if old_desc_part in html:
        html = html.replace(old_desc_part, new_desc_part)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 HBM 16-stack topic!")
