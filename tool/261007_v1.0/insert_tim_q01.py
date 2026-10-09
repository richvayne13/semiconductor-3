# -*- coding: utf-8 -*-
"""
insert_tim_q01.py
사용자 질문: "TIM은 열폭주를줄이는핵심소재인데 뭐의줄인말이야"
대시보드 최상단 Q01로 신규 추가하고, 기존 67개 질문을 Q02~Q68로 시프트 (총 68개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (반도체 패키징 & 열 관리)",
    "title": "TIM은 열폭주를 줄이는 핵심 소재인데 뭐의 줄인말이야? (Thermal Interface Material과 열 계면 저항)",
    "nav_title": "TIM(Thermal Interface Material)의 정의와 열폭주 억제 메커니즘",
    "summary": [
        "<strong>TIM의 약어 및 정의</strong>: <strong>Thermal Interface Material</strong>의 줄임말로, 우리말로는 <strong>'열 계면(界面) 재료'</strong> 또는 <strong>'열 전달 계면 물질'</strong>이라고 부릅니다. 반도체 발열원(다이)과 방열판 사이의 접촉 계면에 도포되는 핵심 열전도성 소재입니다.",
        "<strong>존재 이유 (공기의 치명적 단열 효과 방지)</strong>: 실리콘 다이와 금속 방열판은 거울처럼 매끄러워 보이지만 마이크로(㎛) 단위로 확대하면 수많은 요철(Roughness)이 존재합니다. 둘을 그냥 맞대면 틈새에 <strong>열전도율이 0.026 W/(m·K)에 불과한 공기 주머니(Air Pockets)</strong>가 갇혀 거대한 단열벽이 형성되고 칩이 타버립니다.",
        "<strong>열 계면 저항 극소화</strong>: TIM은 공기보다 열전도율이 수십~수천 배 높은 물질(그리스, 젤, 액체금속, 인듐 솔더 등)로 미세 틈새를 100% 빈틈없이 채워 <strong>접촉 열저항($R_{th}$)과 결합선 두께(BLT, Bond Line Thickness)를 극소화</strong>하여 열을 즉각 배출시킵니다.",
        "<strong>패키징 계층별 분류</strong>: 실리콘 다이와 금속 덮개(IHS) 사이를 채우는 <strong>TIM 1</strong>(고전도성 인듐 솔더/액체금속), IHS와 외부 쿨러 사이를 메우는 <strong>TIM 2</strong>(써멀 그리스), 덮개 없이 쿨러와 직결하는 <strong>TIM 1.5 (Direct Die)</strong>로 나뉩니다."
    ],
    "svg_title": "📊 [TIM(Thermal Interface Material) 미세 접촉면 & 패키징 구조도] 공기 단열층 제거 및 계층별(TIM1·TIM2) 열전달",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: Microscopic Interface Comparison (Without vs With TIM) -->
  <rect x="20" y="25" width="375" height="320" rx="8" fill="#0f172a" stroke="#f43f5e" stroke-width="1.2"/>
  <text x="35" y="48" fill="#f43f5e" font-size="12" font-weight="800">1. 미시적 접촉 계면: TIM 유무에 따른 열 병목 비교</text>

  <!-- Top: Without TIM (Air pockets acting as thermal insulator) -->
  <g transform="translate(35, 60)">
    <rect x="0" y="0" width="345" height="115" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="12" y="18" fill="#f87171" font-size="10.5" font-weight="700">❌ TIM이 없을 때: 공기 주머니에 의한 열폭주(Thermal Runaway)</text>
    
    <!-- Rough Heat Sink (Copper) -->
    <path d="M 15 30 Q 35 25 55 33 T 95 28 T 135 34 T 175 27 T 215 32 T 255 26 T 295 33 L 330 30 L 330 45 L 15 45 Z" fill="#b45309"/>
    <text x="20" y="42" fill="#fef3c7" font-size="8.5" font-weight="600">히트스프레더 / 방열판 (구리 요철면)</text>

    <!-- Air Gaps (Insulator) -->
    <rect x="15" y="45" width="315" height="18" fill="#450a0a"/>
    <circle cx="50" cy="54" r="6" fill="#7f1d1d"/>
    <text x="44" y="57" fill="#fca5a5" font-size="7.5">공기</text>
    <circle cx="120" cy="54" r="7" fill="#7f1d1d"/>
    <text x="114" y="57" fill="#fca5a5" font-size="7.5">공기</text>
    <circle cx="210" cy="54" r="6" fill="#7f1d1d"/>
    <text x="204" y="57" fill="#fca5a5" font-size="7.5">공기</text>
    <circle cx="280" cy="54" r="7" fill="#7f1d1d"/>
    <text x="274" y="57" fill="#fca5a5" font-size="7.5">공기</text>
    <text x="140" y="57" fill="#ef4444" font-size="8.5" font-weight="800">미세 공기층 (k = 0.026 W/m·K 극악의 단열재!)</text>

    <!-- Rough Silicon Die -->
    <path d="M 15 63 Q 40 68 65 60 T 115 66 T 165 59 T 215 65 T 265 61 T 315 67 L 330 63 L 330 85 L 15 85 Z" fill="#1e3a8a"/>
    <text x="20" y="80" fill="#bfdbfe" font-size="8.5" font-weight="600">실리콘 다이 (반도체 칩 표면 요철)</text>
    
    <text x="12" y="103" fill="#fca5a5" font-size="8">• 실제 접촉면적 단 1~2% 불과 ➔ 열이 방출되지 못해 칩 소손 위험</text>
  </g>

  <!-- Bottom: With TIM -->
  <g transform="translate(35, 185)">
    <rect x="0" y="0" width="345" height="145" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="12" y="18" fill="#34d399" font-size="10.5" font-weight="700">✔ TIM 도포 후: 계면 미세 틈새 100% 충진 & 초고속 열전도</text>

    <!-- Heat Sink -->
    <rect x="15" y="28" width="315" height="18" fill="#b45309" rx="2"/>
    <text x="22" y="41" fill="#fef3c7" font-size="8.5">금속 방열판 (Heat Sink, k ≈ 400 W/m·K)</text>

    <!-- TIM Layer -->
    <rect x="15" y="47" width="315" height="22" fill="#047857" rx="1"/>
    <text x="45" y="62" fill="#a7f3d0" font-size="9" font-weight="800">TIM 층 충진 (써멀 그리스/인듐/액체금속: k = 3 ~ 86 W/m·K)</text>

    <!-- Heat Flux Arrows -->
    <line x1="60" y1="85" x2="60" y2="35" stroke="#fbbf24" stroke-width="2.5" marker-end="url(#arrow)"/>
    <line x1="120" y1="85" x2="120" y2="35" stroke="#fbbf24" stroke-width="2.5"/>
    <line x1="180" y1="85" x2="180" y2="35" stroke="#fbbf24" stroke-width="2.5"/>
    <line x1="240" y1="85" x2="240" y2="35" stroke="#fbbf24" stroke-width="2.5"/>
    <line x1="300" y1="85" x2="300" y2="35" stroke="#fbbf24" stroke-width="2.5"/>

    <!-- Silicon Die -->
    <rect x="15" y="70" width="315" height="22" fill="#1e3a8a" rx="2"/>
    <text x="22" y="85" fill="#bfdbfe" font-size="8.5">실리콘 다이 발열원 (TDP 500~700W 핫스팟)</text>

    <text x="12" y="108" fill="#6ee7b7" font-size="8.5" font-weight="700">★ 핵심 원리: BLT(결합선 두께) 극소화 + 접촉 열저항(Rth) 제거</text>
    <text x="12" y="123" fill="#cbd5e1" font-size="8">• 열저항 수식: R_th = BLT / (k_TIM × A) + R_contact1 + R_contact2</text>
    <text x="12" y="136" fill="#94a3b8" font-size="7.5">• 공기 대비 열전도도 100~3,000배 향상으로 급격한 열폭주 완벽 차단</text>
  </g>

  <!-- Right: Packaging Layer Hierarchy (TIM 1 vs TIM 2) -->
  <rect x="410" y="25" width="350" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="425" y="48" fill="#38bdf8" font-size="12" font-weight="800">2. 반도체 패키징 계층별 TIM 분류 (TIM 1 vs TIM 2)</text>

  <!-- Package Stack Diagram -->
  <g transform="translate(425, 62)">
    <!-- Heat Sink / Water Cooler -->
    <rect x="0" y="0" width="320" height="32" rx="4" fill="#334155" stroke="#94a3b8" stroke-width="1"/>
    <text x="55" y="20" fill="#f8fafc" font-size="10" font-weight="800">외부 쿨러 / 수랭 쿨링 블록 (Heat Sink)</text>

    <!-- TIM 2 Layer -->
    <rect x="25" y="34" width="270" height="16" fill="#3b82f6" rx="2"/>
    <text x="35" y="46" fill="#ffffff" font-size="8.5" font-weight="800">TIM 2 (사용자/조립용 써멀 그리스, k ≈ 3~12 W/m·K)</text>

    <!-- IHS (Integrated Heat Spreader) -->
    <rect x="15" y="52" width="290" height="28" fill="#d97706" rx="3"/>
    <text x="50" y="70" fill="#ffffff" font-size="10" font-weight="800">히트스프레더 (IHS: 니켈 도금 구리 뚜껑)</text>

    <!-- TIM 1 Layer -->
    <rect x="50" y="82" width="220" height="16" fill="#ec4899" rx="2"/>
    <text x="58" y="94" fill="#ffffff" font-size="8.5" font-weight="800">TIM 1 (제조사 칩 내부: 인듐 솔더 sTIM / 액체금속)</text>

    <!-- Silicon Die (CPU/GPU/HBM) -->
    <rect x="70" y="100" width="180" height="26" fill="#1d4ed8" rx="2"/>
    <text x="85" y="117" fill="#ffffff" font-size="9.5" font-weight="800">실리콘 다이 (반도체 칩 코어)</text>

    <!-- Underfill / Substrate -->
    <rect x="40" y="128" width="240" height="14" fill="#059669" rx="2"/>
    <text x="75" y="139" fill="#ffffff" font-size="8">언더필 (Underfill) &amp; 마이크로 범프</text>

    <!-- Package Substrate -->
    <rect x="10" y="144" width="300" height="18" fill="#1e293b" stroke="#475569" stroke-width="1" rx="2"/>
    <text x="80" y="157" fill="#cbd5e1" font-size="8.5">패키지 기판 (Package Substrate)</text>

    <!-- BGA Solder Balls -->
    <g fill="#94a3b8">
      <circle cx="30" cy="168" r="4"/><circle cx="60" cy="168" r="4"/><circle cx="90" cy="168" r="4"/>
      <circle cx="120" cy="168" r="4"/><circle cx="150" cy="168" r="4"/><circle cx="180" cy="168" r="4"/>
      <circle cx="210" cy="168" r="4"/><circle cx="240" cy="168" r="4"/><circle cx="270" cy="168" r="4"/>
    </g>
    <text x="110" y="180" fill="#64748b" font-size="7.5">BGA 솔더볼 (메인보드 연결)</text>

    <!-- Explanatory Table -->
    <rect x="0" y="188" width="320" height="74" rx="4" fill="#1e293b"/>
    <text x="10" y="204" fill="#38bdf8" font-size="9" font-weight="800">■ TIM 1과 TIM 2의 결정적 차이</text>
    <text x="10" y="220" fill="#f472b6" font-size="8.5">• TIM 1: 칩 제조사 전용 (인듐 솔더 k=86 W/m·K, 칩 소손 방지)</text>
    <text x="10" y="235" fill="#60a5fa" font-size="8.5">• TIM 2: 쿨러 장착용 (써멀 컴파운드, 교체 용이성, 유연성)</text>
    <text x="10" y="250" fill="#34d399" font-size="8.5">• TIM 1.5: IHS 없이 다이에 쿨러 직접 밀착 (Direct Die, 극단 냉각)</text>
  </g>
</svg>"""
}

NEW_TOPIC["lecture"] = """
<h3>1. TIM의 완벽한 영문 명칭과 직관적 개념</h3>
<p>
<strong>TIM</strong>은 <strong>Thermal Interface Material</strong>의 약어입니다.
우리말로는 <strong>'열 계면(界面) 재료'</strong> 또는 <strong>'열 전달 계면 물질'</strong>이라고 부릅니다.
단어 그대로 <strong>'열(Thermal)'</strong>이 이동하는 서로 다른 두 물체의 <strong>'경계면(Interface)'</strong>에 채워 넣는 <strong>'물질(Material)'</strong>을 뜻합니다.
</p>
<p>
고성능 반도체(CPU, GPU, HBM 등)가 동작할 때 수백 와트(W)의 전력이 순식간에 열로 변환됩니다.
이 열을 외부 방열판(Heat Sink)이나 수랭 쿨러로 전달하지 못하면 칩 내부 온도가 순식간에 100℃를 넘어 소자가 영구 파괴되는 <strong>열폭주(Thermal Runaway)</strong>가 발생합니다.
TIM은 이 열을 방열판으로 막힘없이 고속 전달하는 <strong>열전도의 핵심 징검다리</strong>입니다.
</p>

<h3>2. 왜 TIM이 없으면 칩이 타버릴까? (미세 표면 거칠기와 공기의 치명적 단열벽)</h3>
<p>
많은 분들이 <em>"구리로 만든 단단한 방열판을 실리콘 칩 위에 꽉 눌러놓으면 금속끼리 맞닿았으니 열이 잘 빠져나가지 않을까?"</em>라고 생각합니다.
하지만 물리적 현실은 정반대입니다.
</p>

<div style="background:#0f172a; border-left:4px solid #ef4444; padding:15px; margin:16px 0; border-radius:0 8px 8px 0;">
  <strong style="color:#f87171;">💡 미세 표면 거칠기(Roughness)와 공기 단열벽의 메커니즘:</strong><br>
  1. <strong>미세 요철의 존재</strong>: 아무리 거울처럼 완벽하게 연마(Polishing)된 실리콘 칩과 구리 방열판이라도, 전자현미경이나 마이크로미터(㎛) 단위로 확대해보면 지리산 산맥처럼 울퉁불퉁한 미세 요철(Surface Roughness)이 솟아 있습니다.<br>
  2. <strong>접촉 면적의 한계</strong>: 두 고체를 맞대면 산봉우리 끝부분만 닿기 때문에, <strong>실제 물리적으로 닿는 면적은 전체 표면적의 1~2%</strong>에 불과합니다.<br>
  3. <strong>나머지 98%는 공기 주머니(Air Voids)</strong>: 닿지 않는 나머지 98%의 미세 계곡에는 주변 공기가 갇히게 됩니다.<br>
  4. <strong>공기(Air)의 열전도율</strong>: 공기의 열전도율은 고작 <strong>0.026 W/(m·K)</strong>입니다. 패딩 점퍼나 스티로폼이 따뜻한 이유가 바로 공기층을 품고 있는 최고의 단열재이기 때문입니다! 즉, <strong>방열판 사이에 공기라는 단열벽을 쳐놓은 꼴</strong>이 되어 열이 전혀 빠져나가지 못하고 칩 내부 온도가 치솟아 열폭주가 일어납니다.
</div>

<h3>3. TIM의 열물리 공식: 열 계면 저항(Thermal Interface Resistance)</h3>
<p>
TIM의 성능과 냉각 효율은 푸리에 열전도 법칙(Fourier's Law)에 기반한 <strong>총 열저항 네트워크($R_{th}$)</strong>로 정량화됩니다:
</p>
<div style="text-align:center; padding:12px; background:#111827; border-radius:8px; margin:15px 0; font-size:1.1rem; color:#38bdf8; font-weight:700;">
  $$R_{th, interface} = \frac{\text{BLT}}{k_{TIM} \times A} + R_{contact, 1} + R_{contact, 2}$$
</div>
<ul>
  <li><strong>BLT (Bond Line Thickness, 결합선 두께)</strong>: 실리콘 다이와 방열판 사이의 간격(두께)입니다. 두께가 얇을수록 열이 지나가는 거리가 줄어드므로 저항이 감소합니다. 따라서 TIM은 얇게 펴 발라질수록 우수합니다.</li>
  <li><strong>$k_{TIM}$ (TIM의 고유 열전도율, W/m·K)</strong>: 소재의 고유 특성입니다. 공기($0.026$)보다 수백~수천 배 높은 소재(3 ~ 86 W/m·K)를 사용합니다.</li>
  <li><strong>$R_{contact}$ (접촉 열저항)</strong>: TIM 소재가 고체 표면에 얼마나 잘 젖어 들어(Wetting) 미세 틈새를 기포 없이 완벽히 메우는가에 따라 결정됩니다. 점도가 너무 높아 틈새를 못 채우면 접촉 저항이 증가합니다.</li>
</ul>

<h3>4. 반도체 패키징에서의 TIM 계층 분류 (TIM 1 vs TIM 2 vs TIM 1.5)</h3>
<p>
패키징 산업에서는 TIM이 적용되는 위치에 따라 규격화하여 부릅니다:
</p>
<table style="width:100%; border-collapse:collapse; margin:15px 0; font-size:0.9rem;">
  <thead>
    <tr style="background:#1e293b; color:#38bdf8;">
      <th style="padding:10px; border:1px solid #334155;">구분</th>
      <th style="padding:10px; border:1px solid #334155;">적용 위치</th>
      <th style="padding:10px; border:1px solid #334155;">주요 소재 및 요구 특성</th>
      <th style="padding:10px; border:1px solid #334155;">대표 적용 사례</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#ec4899;">TIM 1</td>
      <td style="padding:10px; border:1px solid #334155;">실리콘 다이(Die) ↔ 히트스프레더(IHS) 덮개 사이</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>인듐 솔더(sTIM, k≈86)</strong>, 갈륨 기반 액체금속(k≈40~70), 고성능 에폭시. 반영구적 신뢰성 필수 (교체 불가).</td>
      <td style="padding:10px; border:1px solid #334155;">고성능 CPU 뚜따(Delid) 방지용 솔더링, 엔비디아 서버용 GPU 내부</td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#3b82f6;">TIM 2</td>
      <td style="padding:10px; border:1px solid #334155;">히트스프레더(IHS) ↔ 외부 방열판(쿨러) 사이</td>
      <td style="padding:10px; border:1px solid #334155;"><strong>써멀 그리스(Thermal Grease, k≈3~12)</strong>, 써멀 패드. 분해 및 재도포 용이성, 절연성 중요.</td>
      <td style="padding:10px; border:1px solid #334155;">PC 조립 시 쿨러 장착 직전에 바르는 회색 써멀 구리스</td>
    </tr>
    <tr>
      <td style="padding:10px; border:1px solid #334155; font-weight:700; color:#10b981;">TIM 1.5</td>
      <td style="padding:10px; border:1px solid #334155;">실리콘 다이(Die) ↔ 외부 쿨러 직결 (Direct Die)</td>
      <td style="padding:10px; border:1px solid #334155;">IHS 뚜껑을 생략하고 칩 다이에 쿨러를 직접 얹음. 고성능 PCM, 액체금속 적용.</td>
      <td style="padding:10px; border:1px solid #334155;">노트북 GPU, 플레이스테이션 5 (PS5 액체금속), 커스텀 수랭 튜닝</td>
    </tr>
  </tbody>
</table>

<h3>5. TIM 소재의 5대 종류와 특성 비교</h3>
<ul>
  <li><strong>써멀 그리스 (Thermal Paste / Grease)</strong>: 실리콘 오일에 알루미나($Al_2O_3$), 산화아연($ZnO$), 은(Ag) 등 고열전도성 세라믹/금속 미세 입자를 섞은 젤 형태. 가장 대중적이며 취급이 안전함 ($k = 3 \sim 12\text{ W/m}\cdot\text{K}$).</li>
  <li><strong>인듐 솔더 (sTIM, Solder TIM)</strong>: 칩 다이 위에 순수 인듐(Indium) 금속 박막을 깔고 열로 녹여 구리 뚜껑과 영구 융합 결합시킴. 열전도율이 <strong>86 W/(m·K)</strong>에 달해 초고발열 칩의 열을 광속으로 방출함.</li>
  <li><strong>상변화 물질 (PCM, Phase Change Material)</strong>: 상온에서는 고체 패드 형태라 작업이 편하고, 칩이 작동해 45~50℃로 데워지면 액체로 녹아 미세 요철 틈새로 침투함. 신뢰성이 매우 높아 차량용 반도체 및 최신 AI 가속기에 각광.</li>
  <li><strong>써멀 패드 (Thermal Pad / Gap Pad)</strong>: 두께가 있는 실리콘 고무 시트 형태. 전원부 모스펫(VRM)이나 GDDR 메모리처럼 부품 간 높낮이 단차가 큰 곳의 간극을 메우는 데 사용 ($k = 1 \sim 6\text{ W/m}\cdot\text{K}$).</li>
  <li><strong>액체금속 (Liquid Metal)</strong>: 갈륨, 인듐, 주석 합금(갈린스탄 등)으로 상온에서 액체 상태를 유지하는 금속. 열전도율이 <strong>40 ~ 73 W/(m·K)</strong>로 극도로 높으나, 전기가 통하는 전도체라 쇼트(Short) 위험이 크고 알루미늄을 부식시키는 화학적 취약점이 있음.</li>
</ul>

<h3>6. 차세대 AI 반도체(TDP 700W~1000W)와 HBM에서의 TIM 기술 과제</h3>
<p>
엔비디아 H100, B200 등 AI 가속기는 단일 칩 전력 소모가 <strong>700W ~ 1,000W</strong>를 돌파하고 있습니다.
다리미 한 개가 손톱만 한 칩 위에서 펄펄 끓고 있는 수준입니다.
이로 인해 TIM 분야에서도 혁신 기술이 필수가 되었습니다:
</p>
<ol>
  <li><strong>펌프아웃(Pump-out) 방지</strong>: 칩이 켜지고 꺼질 때마다 열팽창과 수축이 반복되면서 계면 사이의 써멀 구리스가 바깥으로 밀려 나가는 현상입니다. 장기 구동 시 칩 중앙에 에어 포켓이 생겨 발열이 치솟으므로, 고점도 PCM이나 솔더링 소재로 교체되고 있습니다.</li>
  <li><strong>HBM과 GPU 간 높이 단차 극복</strong>: 실리콘 인터포저 위에 GPU와 8~12개의 HBM 스택이 나란히 올라가는데, 미세한 높이 오차(Warpage 및 수 ㎛ 단차)가 발생합니다. 하나의 방열판으로 이들을 모두 고르게 덮으려면 두께 편차를 흡수하면서도 초고열전도를 유지하는 맞춤형 TIM 설계가 필수적입니다.</li>
  <li><strong>탄소 기반 신소재(탄소나노튜브 CNT, 그래핀 하이브리드 TIM)</strong>: 이론상 수천 W/(m·K)의 열전도도를 자랑하는 탄소나노튜브를 수직 정렬하여 TIM 내부 매트릭스에 통합하는 차세대 패키징 R&D가 활발히 진행 중입니다.</li>
</ol>
"""

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 67 topics (q-67 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(67, 0, -1):
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
        r"최상단에는 'TIM(Thermal Interface Material)의 정의와 열폭주 억제 메커니즘'이 위치하며, 총 68개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 TIM topic!")
