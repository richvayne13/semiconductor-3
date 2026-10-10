# -*- coding: utf-8 -*-
"""
insert_hybrid_bonding_q01.py
사용자 질문: "하이브리드본딩에서 절연체와 금속패드를 한평면에연마한뒤 다이와다이를 연결한다는게 무슨뜻인지 그림과 자세한설명해줘 그리고 sio2간분자결합하고 열처리하여 cu가 부풀며 cu-cu원자확산으로 금속결합완성 이말이무슨말이야"
대시보드 최상단 Q01로 신규 추가하고, 기존 76개 질문을 Q02~Q77로 시프트 (총 77개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (첨단 3D 패키징 & 본딩)",
    "title": "하이브리드 본딩(Hybrid Bonding)의 완전 해부: 동일 평면 연마, SiO2 친수성 분자결합, Cu 열팽창 원자확산 메커니즘",
    "nav_title": "하이브리드 본딩의 원리 (동일평면 연마, SiO2결합, Cu열팽창)",
    "summary": [
        "<strong>'동일 평면에 연마한다'의 물리적 의미</strong>: 다마신(Damascene) 공정으로 SiO₂ 절연막 속에 매립된 구리(Cu) 패드를 CMP(화학기계적연마)로 <strong>원자 단위(0.5nm 이하 거칠기)로 평탄화</strong>하는 것입니다. 이때 상대적으로 무른 Cu가 <strong>2~5nm 살짝 파이게(Dishing 디싱) 제어</strong>하여, 본딩 시 SiO₂ 절연막이 먼저 빈틈없이 닿도록 세팅합니다.",
        "<strong>1단계: SiO₂ 간 분자 결합 (상온 친수성 수소결합 ➔ 공유결합)</strong>: 플라즈마로 표면에 실란올기(Si-OH)를 형성한 뒤 상온에서 맞대면, <strong>물 분자의 수소결합(Si-OH···HO-Si)이 웨이퍼 전체로 번지며 자발적으로 접착</strong>됩니다. 150~200℃로 살짝 데우면 물(H₂O)이 탈수 축합되어 단단한 <strong>Si-O-Si 공유결합</strong>으로 영구 밀봉됩니다.",
        "<strong>2단계: Cu가 부풀어 오르는 원리 (열팽창계수 CTE 30배 차이)</strong>: 300~400℃ 고온 열처리를 가하면, <strong>Cu의 열팽창계수(17 ppm/℃)가 SiO₂(0.5 ppm/℃)보다 30배 이상 크기 때문에</strong> Cu가 팝콘처럼 팽창(부풀어 오름)하여 2~5nm의 디싱 틈새를 100% 꽉 채우며 엄청난 압축 응력으로 맞부딪힙니다.",
        "<strong>Cu-Cu 원자확산 및 금속결합 완성</strong>: 고온·고압 상태에서 계면의 구리 원자들이 서로의 격자로 뛰어넘어 이동(고상 원자확산)하고 결정립이 합쳐지면서(Grain Growth), <strong>두 구리 패드 사이의 경계선이 완전히 사라진 일체형 금속 결정</strong>으로 영구 결합됩니다 (솔더 범프 제로, 피치 1㎛ 이하, 저항 90% 절감)."
    ],
    "svg_title": "📊 [하이브리드 본딩 4단계 반응 시퀀스] 디싱 연마 ➔ SiO2 수소/공유결합 ➔ Cu 열팽창 ➔ Cu-Cu 원자확산 일체화",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left Side: Step 1 (CMP with Dishing) & Step 2 (Room Temp SiO2 Bonding) -->
  <rect x="20" y="25" width="375" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="48" fill="#38bdf8" font-size="12" font-weight="800">1. CMP 연마(디싱) &amp; 상온 SiO₂ 친수성 결합</text>

  <!-- Step 1: Dishing CMP profile -->
  <g transform="translate(35, 60)">
    <rect x="0" y="0" width="345" height="120" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="12" y="18" fill="#38bdf8" font-size="9.5" font-weight="700">■ 1단계: 초평탄 CMP &amp; Cu 의도적 디싱 (2~5nm)</text>

    <!-- Top Die before touch (flipped) -->
    <rect x="15" y="28" width="95" height="20" fill="#0284c7" rx="1"/>
    <text x="25" y="42" fill="#ffffff" font-size="8">SiO₂ 절연체</text>
    <rect x="110" y="31" width="125" height="17" fill="#d97706" rx="1"/>
    <text x="125" y="43" fill="#fef3c7" font-size="8.5" font-weight="800">Cu Pad (2~5nm 들어감)</text>
    <rect x="235" y="28" width="95" height="20" fill="#0284c7" rx="1"/>

    <!-- Gap illustration -->
    <line x1="110" y1="52" x2="235" y2="52" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,2"/>
    <text x="135" y="62" fill="#ef4444" font-size="8" font-weight="700">미세 틈새 (Dishing Gap)</text>

    <!-- Bottom Die -->
    <rect x="15" y="68" width="95" height="20" fill="#0284c7" rx="1"/>
    <rect x="110" y="71" width="125" height="17" fill="#d97706" rx="1"/>
    <rect x="235" y="68" width="95" height="20" fill="#0284c7" rx="1"/>

    <text x="12" y="105" fill="#cbd5e1" font-size="8">• Cu가 튀어나오면 SiO₂가 못 붙으므로, 일부러 Cu를 2~5nm 파이게 깎음!</text>
  </g>

  <!-- Step 2: Room Temp SiO2 bonding -->
  <g transform="translate(35, 190)">
    <rect x="0" y="0" width="345" height="140" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="12" y="18" fill="#34d399" font-size="9.5" font-weight="700">■ 2단계: 상온 SiO₂ 친수성 본딩 (분자결합)</text>

    <!-- SiO2 bonded tightly -->
    <rect x="15" y="28" width="95" height="40" fill="#0369a1" rx="2"/>
    <text x="25" y="52" fill="#ffffff" font-size="8.5" font-weight="800">Si-O-Si 공유결합</text>
    
    <!-- Cu Pad with gap -->
    <rect x="110" y="28" width="125" height="18" fill="#d97706"/>
    <rect x="110" y="47" width="125" height="21" fill="#d97706"/>
    <line x1="110" y1="46" x2="235" y2="46" stroke="#fbbf24" stroke-width="2"/>
    <text x="130" y="44" fill="#fbbf24" font-size="7.5">Cu 사이 미세 틈</text>

    <!-- Right SiO2 bonded -->
    <rect x="235" y="28" width="95" height="40" fill="#0369a1" rx="2"/>

    <text x="12" y="86" fill="#a7f3d0" font-size="8.5" font-weight="700">★ 상온: Si-OH···HO-Si 수소결합 파동 ➔ 200℃ Si-O-Si 영구 결합!</text>
    <text x="12" y="102" fill="#cbd5e1" font-size="8">• 접착제(언더필) 없이 절연막끼리 완벽히 밀봉 (진공/기밀 유지)</text>
    <text x="12" y="118" fill="#94a3b8" font-size="7.5">• 이 단계에서 Cu 패드는 아직 맞닿지 않고 미세하게 떠 있는 상태임</text>
  </g>

  <!-- Right Side: Step 3 (Thermal Expansion) & Step 4 (Atomic Diffusion) -->
  <rect x="410" y="25" width="350" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
  <text x="425" y="48" fill="#f59e0b" font-size="12" font-weight="800">2. Cu 열팽창(부풂) &amp; 원자확산 금속결합 완성</text>

  <!-- Step 3 & 4 combined into annealing process -->
  <g transform="translate(425, 60)">
    <rect x="0" y="0" width="320" height="135" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1"/>
    <text x="12" y="18" fill="#fbbf24" font-size="9.5" font-weight="800">■ 3단계: 300~400℃ 열처리 ➔ Cu 열팽창 (부풀어 오름)</text>

    <!-- Expanded Cu Pad in tight contact under high compressive stress -->
    <rect x="20" y="28" width="80" height="46" fill="#0369a1" rx="1"/>
    <text x="30" y="55" fill="#ffffff" font-size="8">SiO₂</text>

    <!-- Cu Expansion bulging -->
    <rect x="100" y="28" width="120" height="46" fill="#ea580c" rx="1"/>
    <text x="110" y="46" fill="#ffffff" font-size="8.5" font-weight="800">Cu 팽창 (CTE=17)</text>
    <text x="110" y="60" fill="#fef08a" font-size="7.5">엄청난 압축 압력 밀착!</text>

    <rect x="220" y="28" width="80" height="46" fill="#0369a1" rx="1"/>
    <text x="240" y="55" fill="#ffffff" font-size="8">SiO₂</text>

    <text x="12" y="90" fill="#fde047" font-size="8.5" font-weight="700">★ 열팽창계수(CTE) 차이의 마법:</text>
    <text x="12" y="104" fill="#cbd5e1" font-size="8">• Cu(17 ppm/℃) vs SiO₂(0.5 ppm/℃) ➔ Cu가 30배 더 팽창!</text>
    <text x="12" y="118" fill="#cbd5e1" font-size="8">• 2~5nm 디싱 틈새를 꽉 채우고 위아래 Cu가 쾅 부딪치며 밀착</text>
  </g>

  <!-- Step 4: Atomic Diffusion & Seamless Joint -->
  <g transform="translate(425, 205)">
    <rect x="0" y="0" width="320" height="125" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1.2"/>
    <text x="12" y="18" fill="#34d399" font-size="9.5" font-weight="800">■ 4단계: Cu-Cu 원자확산 (경계면 소멸 &amp; 단일 결정립)</text>

    <!-- Fully unified Cu pad -->
    <rect x="20" y="26" width="80" height="40" fill="#0369a1"/>
    <rect x="100" y="26" width="120" height="40" fill="#b45309" stroke="#f59e0b" stroke-width="1"/>
    <text x="108" y="45" fill="#ffffff" font-size="8.5" font-weight="900">완벽한 일체형 Cu 전극</text>
    <text x="115" y="57" fill="#86efac" font-size="7.5">경계선 0 (Zero Boundary)</text>
    <rect x="220" y="26" width="80" height="40" fill="#0369a1"/>

    <text x="12" y="82" fill="#6ee7b7" font-size="8.5" font-weight="700">★ 고상 원자확산 (Interdiffusion &amp; Grain Growth):</text>
    <text x="12" y="96" fill="#cbd5e1" font-size="8">• 구리 원자가 경계를 넘어 이동 ➔ 경계면이 사라지고 한 몸이 됨</text>
    <text x="12" y="110" fill="#93c5fd" font-size="7.5">• 솔더 범프 제로, 접촉 저항 90% 절감, 피치 &lt; 1μm 초고밀도 달성!</text>
  </g>
</svg>"""
}

NEW_TOPIC["lecture"] = r"""
<h3>1. 하이브리드 본딩(Hybrid Bonding)이란? 왜 '하이브리드(혼합)'인가?</h3>
<p>
기존 패키징에서는 칩과 칩을 연결할 때 주석-은 솔더볼(Micro-bump)을 중간에 녹여 붙였습니다. 
하지만 범프는 크기가 크고(피치 10~20㎛), 녹을 때 옆으로 삐져나와 쇼트(합선) 위험이 있어 10㎛ 이하로 줄일 수 없었습니다.
</p>
<p>
<strong>하이브리드 본딩(Hybrid Bonding, 직접 접합 DBI)</strong>은 범프를 아예 없애고(Bumpless), 
<strong>다이(Die)와 다이의 표면을 거울처럼 매끄럽게 맞대어 하나의 칩처럼 직접 융합</strong>시키는 궁극의 3D 패키징 기술입니다.
</p>
<div style="background:#0f172a; border-left:4px solid #38bdf8; padding:14px; margin:15px 0; border-radius:0 8px 8px 0;">
  <strong style="color:#38bdf8; font-size:1.05rem;">💡 왜 '하이브리드(Hybrid, 혼합)'라고 부를까?</strong><br>
  단일 계면에서 <strong>전혀 다른 2가지 종류의 물질이 동시에 결합</strong>하기 때문입니다:<br>
  1. <strong>절연체 ↔ 절연체 결합</strong>: SiO₂ 산화막끼리 분자/공유결합으로 달라붙어 틈새를 영구 밀봉함.<br>
  2. <strong>금속 ↔ 금속 결합</strong>: 구리(Cu) 패드끼리 원자 확산으로 달라붙어 전기를 초고속으로 통하게 함.
</div>

<h3>2. "절연체와 금속패드를 한 평면에 연마한다"의 진짜 의미 (CMP와 디싱 Dishing)</h3>
<p>
반도체 웨이퍼 표면에 절연체(SiO₂)를 깔고 구멍을 파서 구리(Cu)를 채워 넣은 뒤(다마신 공정), 
화학기계적연마(CMP) 장비로 표면을 깎아냅니다.
이때 <strong>단순히 평평하게 만드는 것을 넘어 고도의 물리적 트릭</strong>이 들어갑니다:
</p>
<ul>
  <li><strong>원자 수준의 초평탄도 ($R_q < 0.5\text{ nm}$)</strong>:  
     표면 거칠기가 0.5nm(원자 2~3개 크기) 이하로 거울보다 수만 배 완벽하게 연마되어야만 분자 간 인력이 작용할 수 있습니다.</li>
  <li><strong>의도적인 Cu 디싱 (Dishing, 2~5nm 침하)</strong>:  
     구리(Cu)는 SiO₂ 산화막보다 무르기 때문에 CMP 패드로 깎을 때 살짝 더 많이 깎입니다.  
     공정 엔지니어들은 이 성질을 이용해 <strong>구리 패드의 높이를 SiO₂ 표면보다 '일부러 2~5 나노미터 살짝 낮게(오목하게)'</strong> 만듭니다.</li>
  <li><strong>왜 Cu를 2~5nm 낮게 만들까?</strong>:  
     만약 구리가 단 0.1nm라도 SiO₂보다 위로 툭 튀어나와 있으면, 두 칩을 맞댈 때 구리끼리 먼저 부딪혀서 <strong>주변의 SiO₂ 절연체끼리 맞닿지 못하고 허공에 떠버려(접착 실패 및 보이드 발생)</strong> 칩이 결합되지 않기 때문입니다!</li>
</ul>

<h3>3. "SiO2 간 분자 결합": 상온 수소결합에서 Si-O-Si 공유결합으로</h3>
<p>
연마된 두 칩을 맞대면 어떻게 접착제도 없이 절연체끼리 딱 달라붙을까요?
</p>
<ol>
  <li><strong>플라즈마 활성화 (친수성 표면 형성)</strong>:  
     질소($N_2$)나 산소($O_2$) 플라즈마로 SiO₂ 표면을 때린 뒤 물로 세정하면, 표면에 수많은 <strong>수산화기($-\text{OH}$, 실란올기 $\text{Si-OH}$)</strong>가 자석처럼 돋아납니다.</li>
  <li><strong>상온(25℃) 분자 결합 (수소 결합)</strong>:  
     열이나 압력을 주지 않고, 두 칩을 상온에서 정밀 정렬해 살짝 톡 치면 표면의 물 분자와 $-\text{OH}$기 사이에 <strong>수소 결합(Hydrogen Bonding)</strong>이 형성됩니다. 이 결합 파동이 순식간에 웨이퍼 전체로 퍼져나가며 두 칩이 자발적으로 찰떡처럼 붙습니다.</li>
  <li><strong>탈수 축합 반응 ($\text{Si-O-Si}$ 공유 결합)</strong>:  
     약 150~200℃로 살짝 데우면 수소결합을 하던 물($\text{H}_2\text{O}$)이 기화되어 빠져나가면서, 원자들이 단단한 <strong>실록산 공유결합($\text{Si-O-Si}$)</strong>을 형성합니다. 이제 두 칩의 절연막은 하나의 단단한 유리 덩어리로 영구 융합 밀봉됩니다.</li>
</ol>

<h3>4. "열처리하여 Cu가 부풀며": 열팽창계수(CTE) 30배 차이의 기적</h3>
<p>
절연체(SiO₂)가 완벽히 결합된 시점에서도, <strong>구리 패드끼리는 아까 만들어둔 2~5nm 디싱 틈새 때문에 아직 물리적으로 닿지 않고 살짝 떠 있는 상태</strong>입니다.  
이 틈새를 메우기 위해 온도를 <strong>300℃~400℃</strong>로 올립니다:
</p>
<ul>
  <li><strong>구리(Cu)의 열팽창계수(CTE)</strong>: 약 $17 \text{ ppm/}^\circ\text{C}$</li>
  <li><strong>산화막(SiO₂)의 열팽창계수(CTE)</strong>: 약 $0.5 \text{ ppm/}^\circ\text{C}$</li>
  <li><strong>Cu가 30배 이상 더 팽창함!</strong>: 사방이 팽창하지 않는 SiO₂ 벽으로 꽉 갇혀 있는 상태에서 구리(Cu)만 온도를 받아 엄청난 힘으로 부풀어 오릅니다.</li>
  <li><strong>디싱 틈새 소멸</strong>: 부풀어 오른 위아래 구리 패드가 <strong>2~5nm의 미세 틈새를 순식간에 메우고, 서로를 수백 기압의 강력한 압축 응력으로 밀어붙이며 쾅 맞부딪힙니다!</strong></li>
</ul>

<h3>5. "Cu-Cu 원자확산으로 금속 결합 완성": 경계선이 사라지는 일체화</h3>
<p>
위아래 구리 패드가 초강력 압력으로 맞부딪힌 상태에서 고온이 유지되면:
</p>
<ol>
  <li><strong>고상 원자확산 (Solid-State Interdiffusion)</strong>:  
     350℃의 열에너지와 팽창 압력을 받은 구리 원자들은 엄청난 에너지를 얻어 진동하다가, <strong>경계면의 틈새를 뛰어넘어 상대방 구리 격자 속으로 마구 파고들어 섞입니다.</strong></li>
  <li><strong>결정립 성장 (Grain Growth) & 경계면 소멸</strong>:  
     위쪽 구리의 결정립과 아래쪽 구리의 결정립이 하나로 합쳐지며 자라납니다.  
     결과적으로 <strong>두 개의 분리된 구리 패드 사이에 존재하던 물리적 경계면(Interface Boundary)이 100% 완전히 소멸</strong>해 버립니다!</li>
  <li><strong>최종 상태</strong>:  
     마치 처음부터 하나의 구리 기둥이었던 것처럼 <strong>완벽한 일체형 금속 결합(Metallic Bond)</strong>이 완성되어 전기가 저항 없이 흐르게 됩니다.</li>
</ol>

<h3>6. 핵심 요약 (1줄 정리)</h3>
<blockquote style="border-left:4px solid #38bdf8; padding-left:12px; color:#e2e8f0; font-weight:600; margin:15px 0;">
"하이브리드 본딩이란 구리 패드를 절연막보다 2~5nm 살짝 파이게(Dishing) 깎아 상온에서 SiO₂ 절연막을 먼저 찰떡처럼 분자결합시킨 뒤, 350℃로 가열했을 때 열팽창계수가 30배 큰 구리가 팝콘처럼 부풀어 올라 틈새를 메우고, 고온 원자확산으로 경계면을 지워버려 완벽한 단일 구리 결정으로 융합시키는 최첨단 무범프 3D 패키징 기술입니다!"
</blockquote>
"""

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 76 topics (q-76 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(76, 0, -1):
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
        r"최상단에는 '하이브리드 본딩의 원리 (동일평면 연마, SiO2결합, Cu열팽창)'이 위치하며, 총 77개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Hybrid Bonding topic!")
