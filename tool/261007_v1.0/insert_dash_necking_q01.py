# -*- coding: utf-8 -*-
"""
insert_dash_necking_q01.py
사용자 질문: "네킹공정을통해 열충격전위를 밖으로 배출시켜 단결정확보한다는게 직관적으로 이해가안감"
대시보드 최상단 Q01로 신규 추가하고, 기존 70개 질문을 Q02~Q71로 시프트 (총 71개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (웨이퍼 제조 & 결정학)",
    "title": "대시 네킹(Dash Necking)으로 열충격 전위를 밖으로 배출시켜 무전위 단결정을 확보하는 원리 (사선 활주면과 자유 표면 소멸)",
    "nav_title": "네킹공정을 통해 열충격 전위를 밖으로 배출시키는 원리 (사선 소멸)",
    "summary": [
        "<strong>결정학적 핵심 비밀 (전위는 수직이 아니라 '사선'으로 자란다!)</strong>: 실리콘 다이아몬드 결정 격자에서 전위(Dislocation, 원자 배열 결함)는 결정 성장 방향(수직)과 나란하게 내려가지 않고, <strong>약 54.7° 기울어진 {111} 슬립면(Slip Plane, 미끄럼면)을 따라 대각선 사선으로 전파</strong>됩니다.",
        "<strong>'자유 표면(Free Surface) 소멸' 메커니즘</strong>: 잉곳 굵기가 두꺼우면 사선으로 뻗는 전위가 내부에서 끝없이 이어지지만, 직경을 <strong>2~3mm 수준으로 극단적으로 가늘게(Necking) 쥐어짜면</strong> 사선으로 뻗어나가던 전위선이 불과 몇 밀리미터도 못 가서 <strong>웨이퍼 외벽(바깥 공기/아르곤과 맞닿은 표면)에 부딪혀 소멸(Termination)</strong>하고 밖으로 빠져나갑니다.",
        "<strong>열충격(Thermal Shock)의 기원</strong>: 상온(~25℃)의 종자 결정(Seed)을 1420℃의 펄펄 끓는 실리콘 융액에 담그는 순간 극심한 열충격($\Delta T \approx 1400^\circ\text{C}$)으로 수만 개의 전위가 발생하지만, 대시 네킹을 거치며 이 전위들이 100% 외벽으로 탈출합니다.",
        "<strong>고속 인상 속도(Pull Rate) 시너지</strong>: 직경을 2~3mm로 좁힌 상태에서 잉곳을 빠르게 위로 뽑아 올리면(수 mm/min), 결정 성장 속도가 전위의 증식 속도보다 빨라져 결함이 하부로 전파되지 못하고 <strong>네킹 끝단 아래로는 결함이 단 1개도 없는 '100% 무전위 단결정(Zero Dislocation)'</strong> 상태가 완성됩니다."
    ],
    "svg_title": "📊 [대시 네킹(Dash Necking) 원리 단면도] {111} 사선 슬립면과 초슬림 직경(2~3mm)에 의한 전위 외벽 배출",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: Thick vs Thin Necking Mechanism (Why Thin expels dislocations) -->
  <rect x="20" y="25" width="375" height="320" rx="8" fill="#0f172a" stroke="#f43f5e" stroke-width="1.2"/>
  <text x="35" y="48" fill="#f43f5e" font-size="12" font-weight="800">1. 직경 크기에 따른 전위의 전파 vs 외벽 소멸 비교</text>

  <!-- Thick Crystal (Failure to expel) -->
  <g transform="translate(35, 60)">
    <rect x="0" y="0" width="165" height="150" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="10" y="18" fill="#f87171" font-size="9" font-weight="700">❌ 직경이 굵을 때 (50~100mm)</text>
    
    <!-- Thick body -->
    <rect x="15" y="25" width="135" height="95" fill="#334155" opacity="0.7"/>
    <text x="30" y="40" fill="#cbd5e1" font-size="7.5">외벽까지 거리가 너무 멂!</text>

    <!-- Dislocation traveling diagonally and staying inside -->
    <line x1="25" y1="30" x2="110" y2="110" stroke="#ef4444" stroke-width="2.5"/>
    <line x1="45" y1="28" x2="135" y2="105" stroke="#ef4444" stroke-width="2.5"/>
    <line x1="15" y1="60" x2="85" y2="118" stroke="#ef4444" stroke-width="2.5"/>
    <text x="15" y="135" fill="#fca5a5" font-size="8">전위가 내부에서 계속 증식 ➔ 다결정</text>
  </g>

  <!-- Dash Necking (Success to expel) -->
  <g transform="translate(210, 60)">
    <rect x="0" y="0" width="170" height="150" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="10" y="18" fill="#34d399" font-size="9" font-weight="700">✔ 대시 네킹 (직경 2~3mm 극소화)</text>
    
    <!-- Thin neck -->
    <rect x="70" y="25" width="30" height="95" fill="#047857" opacity="0.6"/>
    <text x="62" y="40" fill="#a7f3d0" font-size="7.5">폭 2~3mm</text>

    <!-- Seed at top -->
    <rect x="55" y="22" width="60" height="10" fill="#64748b" rx="1"/>

    <!-- Dislocation shooting diagonally out of the surface -->
    <line x1="72" y1="35" x2="100" y2="60" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="100" cy="60" r="3" fill="#ef4444"/>
    <text x="105" y="63" fill="#fbbf24" font-size="7" font-weight="700">표면 탈출!</text>

    <line x1="85" y1="45" x2="70" y2="72" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="70" cy="72" r="3" fill="#ef4444"/>
    <text x="12" y="74" fill="#fbbf24" font-size="7" font-weight="700">표면 탈출!</text>

    <line x1="75" y1="65" x2="100" y2="92" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="100" cy="92" r="3" fill="#ef4444"/>

    <!-- Pure crystal at bottom of neck -->
    <rect x="70" y="100" width="30" height="20" fill="#10b981"/>
    <text x="10" y="135" fill="#6ee7b7" font-size="8">★ 100% 무전위 단결정 코어 완성!</text>
  </g>

  <!-- Bottom explanation box -->
  <g transform="translate(35, 222)">
    <rect x="0" y="0" width="345" height="110" rx="6" fill="#1e293b"/>
    <text x="10" y="18" fill="#38bdf8" font-size="9.5" font-weight="700">■ 왜 얇게 만들면 전위가 밖으로 빠져나가는가?</text>
    <text x="10" y="35" fill="#cbd5e1" font-size="8.5">• 전위는 수직이 아니라 {111} 슬립면을 따라 54.7° 사선으로 진행</text>
    <text x="10" y="52" fill="#34d399" font-size="8.5">• 굵기가 2~3mm로 좁으면 사선 전위선이 순식간에 외벽 표면에 도달</text>
    <text x="10" y="69" fill="#fbbf24" font-size="8.5">• 자유 표면(Free Surface)에 닿는 순간 결정 변형 에너지가 풀리며 소멸!</text>
    <text x="10" y="86" fill="#cbd5e1" font-size="8.5">• 고속 인상 속도(수 mm/min)로 전위가 아래로 번지는 속도를 압도</text>
    <text x="10" y="102" fill="#94a3b8" font-size="7.5">• 윌리엄 대시(William Dash) 박사가 1958년 발명한 기적의 무전위 공법</text>
  </g>

  <!-- Right: Full CZ Ingot Growth Sequence -->
  <rect x="410" y="25" width="350" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="425" y="48" fill="#38bdf8" font-size="12" font-weight="800">2. 초크랄스키(CZ) 단결정 성장 4단계 시퀀스</text>

  <!-- Process steps drawing -->
  <g transform="translate(425, 62)">
    <!-- Stage 1: Seed Dip -->
    <rect x="0" y="0" width="75" height="80" rx="4" fill="#1e293b"/>
    <text x="5" y="15" fill="#f87171" font-size="8" font-weight="700">1) 씨드 접촉</text>
    <rect x="25" y="22" width="25" height="25" fill="#64748b"/>
    <text x="12" y="38" fill="#ffffff" font-size="7">Seed (25℃)</text>
    <rect x="5" y="55" width="65" height="20" fill="#dc2626" rx="2"/>
    <text x="10" y="68" fill="#fef08a" font-size="7">용융액 1420℃</text>
    <text x="5" y="93" fill="#fca5a5" font-size="7">극심한 열충격 전위</text>

    <!-- Stage 2: Dash Necking -->
    <rect x="80" y="0" width="75" height="80" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="1.2"/>
    <text x="85" y="15" fill="#34d399" font-size="8" font-weight="700">2) 대시 네킹</text>
    <rect x="105" y="22" width="25" height="10" fill="#64748b"/>
    <line x1="117" y1="32" x2="117" y2="60" stroke="#10b981" stroke-width="4"/>
    <text x="85" y="50" fill="#34d399" font-size="6.5">2~3mm</text>
    <rect x="85" y="60" width="65" height="15" fill="#dc2626" rx="2"/>
    <text x="85" y="93" fill="#34d399" font-size="7">사선 전위 외벽 배출</text>

    <!-- Stage 3: Crown / Shoulder -->
    <rect x="160" y="0" width="75" height="80" rx="4" fill="#1e293b"/>
    <text x="165" y="15" fill="#38bdf8" font-size="8" font-weight="700">3) 숄더(어깨)</text>
    <polygon points="197,25 170,60 225,60" fill="#0284c7"/>
    <rect x="165" y="60" width="65" height="15" fill="#dc2626" rx="2"/>
    <text x="165" y="93" fill="#93c5fd" font-size="7">직경 300mm로 확장</text>

    <!-- Stage 4: Body Growth -->
    <rect x="240" y="0" width="75" height="80" rx="4" fill="#1e293b"/>
    <text x="245" y="15" fill="#a855f7" font-size="8" font-weight="700">4) 직동부 성장</text>
    <rect x="245" y="25" width="65" height="35" fill="#6366f1" rx="2"/>
    <rect x="245" y="60" width="65" height="15" fill="#dc2626" rx="2"/>
    <text x="245" y="93" fill="#c7d2fe" font-size="7">완벽한 무전위 잉곳</text>
  </g>

  <!-- Right Side Detailed Table -->
  <g transform="translate(425, 175)">
    <rect x="0" y="0" width="320" height="155" rx="6" fill="#1e293b"/>
    <text x="12" y="20" fill="#38bdf8" font-size="10" font-weight="800">■ 대시 네킹(Dash Necking) 핵심 파라미터</text>
    
    <text x="12" y="40" fill="#f8fafc" font-size="8.5">• <tspan fill="#fbbf24" font-weight="700">네킹 직경:</tspan> 2 ~ 3 mm (성인 새끼손가락 굵기보다 얇음)</text>
    <text x="12" y="58" fill="#f8fafc" font-size="8.5">• <tspan fill="#fbbf24" font-weight="700">네킹 길이:</tspan> 50 ~ 100 mm (충분한 사선 배출 거리 확보)</text>
    <text x="12" y="76" fill="#f8fafc" font-size="8.5">• <tspan fill="#fbbf24" font-weight="700">인상 속도:</tspan> 고속 인상 (약 3 ~ 6 mm/min, 결함 증식 추월)</text>
    <text x="12" y="94" fill="#f8fafc" font-size="8.5">• <tspan fill="#fbbf24" font-weight="700">인장 하중:</tspan> 2~3mm의 얇은 목이 무려 300~500kg의</text>
    <text x="20" y="110" fill="#cbd5e1" font-size="8.5">초거대 300mm 실리콘 잉곳 무게를 버텨냄 (실리콘 공유결합의 힘!)</text>
    <text x="12" y="130" fill="#34d399" font-size="8.5" font-weight="700">• 결과: 직경 300mm 전체가 '원자 결함 0개' 단결정으로 복제</text>
    <text x="12" y="146" fill="#94a3b8" font-size="7.5">• 전위가 남아있으면 다결정화(Multi-crystal)되어 전량 폐기됨</text>
  </g>
</svg>"""
}

NEW_TOPIC["lecture"] = """
<h3>1. 한눈에 보는 직관적 비유: '좁은 골목길에서 대각선으로 달리는 자동차'</h3>
<p>
<em>"네킹(Necking, 목을 가늘게 만들기)을 한다고 해서 어떻게 전위가 밖으로 빠져나간다는 걸까?"</em><br>
이를 가장 직관적으로 이해하는 비유는 <strong>'좁은 골목길에서 55도 대각선으로 직진하는 자동차'</strong>입니다.
</p>
<div style="background:#0f172a; border-left:4px solid #10b981; padding:15px; margin:16px 0; border-radius:0 8px 8px 0;">
  <strong style="color:#34d399; font-size:1.05rem;">💡 네킹의 직관적 원리:</strong><br>
  • <strong>넓은 광장 (직경 100mm)</strong>: 자동차(전위)가 대각선으로 계속 달려도 광장이 워낙 넓어서 벽(외벽 표면)에 부딪히지 않고 한참 동안 광장 안을 휘젓고 다닙니다.<br>
  • <strong>폭이 2mm인 좁은 골목길 (Dash Necking)</strong>: 골목길이 너무 좁기 때문에, 대각선(55도)으로 달리는 자동차는 <strong>출발하자마자 2~3mm도 못 가서 곧바로 골목길 벽(웨이퍼 바깥 표면)을 들이받고 밖으로 튕겨 나가 소멸</strong>해 버립니다!<br>
  • 바로 이것이 <strong>결정의 굵기를 2~3mm로 극도로 얇게 줄여서 전위를 표면 밖으로 강제 탈출시키는 '대시 네킹'의 본질</strong>입니다.
</div>

<h3>2. 왜 처음에 엄청난 전위(Dislocation)가 생기는가? (열충격의 원인)</h3>
<p>
초크랄스키(CZ) 공정에서는 완전한 단결정 실리콘을 만들기 위해, 미리 만들어 둔 손가락만 한 <strong>씨앗 단결정(Seed Crystal)</strong>을 고온의 실리콘 융액(Melt)에 담급니다.
</p>
<ul>
  <li><strong>극단적인 온도 차이 ($\Delta T \approx 1400^\circ\text{C}$)</strong>: 씨드 결정은 상온(~25℃) 상태이고, 도가니 속 실리콘 쇳물은 <strong>1420℃</strong>로 펄펄 끓고 있습니다.</li>
  <li><strong>열충격(Thermal Shock) 발생</strong>: 차가운 유리잔에 펄펄 끓는 물을 부으면 쩍 하고 금이 가듯, 씨앗 결정이 1420℃ 쇳물에 닿는 순간 엄청난 열응력(Thermal Stress)을 받아 <strong>원자 격자가 어긋나는 수만 개의 선결함(전위, Dislocation)</strong>이 폭발적으로 발생합니다.</li>
  <li><strong>방치할 경우의 파선</strong>: 이 전위들을 제거하지 않고 그대로 잉곳을 굵게 키우면, 결함이 아래로 계속 번져나가 잉곳 전체가 결함투성이인 <strong>다결정(Polycrystalline) 실리콘</strong>으로 변해버려 반도체 웨이퍼로 쓸 수 없게 됩니다.</li>
</ul>

<h3>3. 결정학적 비밀: 전위는 수직이 아니라 '사선(54.7°)'으로 자란다!</h3>
<p>
이 현상을 이해하는 가장 결정적인 열쇠는 <strong>'실리콘 결정에서 전위가 전파되는 기하학적 각도'</strong>입니다.
</p>
<div style="background:#1e1b4b; border:1px solid #4338ca; border-radius:8px; padding:14px; margin:15px 0;">
  <strong style="color:#a5b4fc;">★ {111} 슬립면(Slip Plane)과 54.74° 사선 진행:</strong><br>
  실리콘은 다이아몬드 입방 격자(Diamond Cubic Lattice) 구조를 가집니다.<br>
  원자 결합 에너지가 가장 낮아 전위가 쉽게 미끄러지는 면은 <strong>{111} 면(가장 조밀한 면)</strong>입니다.<br>
  우리가 통상 성장시키는 (100) 방향 잉곳에서 이 {111} 슬립면은 수직 성장 축과 <strong>약 54.74°의 대각선 각도</strong>를 이룹니다.<br>
  즉, <strong>전위는 수직으로 곧게 아래로 자라나는 것이 아니라, 반드시 옆으로 비스듬히 기울어진 '사선(Diagonal)'으로만 전파</strong>됩니다!
</div>

<h3>4. 자유 표면 소멸(Free Surface Termination)의 물리</h3>
<p>
대각선 사선으로 자라나는 전위선이 <strong>결정의 바깥 외벽(Free Surface, 아르곤 가스와 맞닿은 표면)</strong>에 도달하면 무슨 일이 일어날까요?
</p>
<ol>
  <li><strong>변형 에너지의 해소</strong>: 전위(Dislocation)란 결정 내부 원자들이 서로 억지로 비틀려 있는 탄성 변형 에너지(Strain Energy) 덩어리입니다.</li>
  <li><strong>표면 도달 시 종단(Termination)</strong>: 이 어긋난 원자선이 물질이 끝나는 바깥 표면에 도달하는 순간, 더 이상 원자가 없으므로 비틀려 있던 응력이 외부 공간으로 완전히 풀려버립니다.</li>
  <li><strong>영구 소멸</strong>: 표면 밖으로 한번 빠져나온 전위는 다시 내부로 되돌아가지 못하고 <strong>그 자리에서 완전히 소멸(Termination)</strong>되어 사라집니다.</li>
</ol>
<p>
따라서 <strong>직경을 2~3mm로 극도로 얇게(Necking) 유지한 채 몇 센티미터만 아래로 뽑아내면, 사선으로 달리던 모든 전위들이 차례차례 외벽 표면에 머리를 부딪히며 100% 밖으로 탈출</strong>하게 됩니다!
</p>

<h3>5. 인상 속도(Pull Rate)의 마법: 결함보다 빠르게 달리기</h3>
<p>
네킹 공정에서는 단순히 굵기만 줄이는 것이 아니라, <strong>위로 끌어올리는 속도(Pull Rate)를 평소보다 훨씬 빠른 수 mm/min(3~6 mm/min)으로 고속 인상</strong>합니다.
</p>
<ul>
  <li>전위가 격자 내에서 증식하고 이동하는 데에도 물리적인 속도(Dislocation Velocity)가 필요합니다.</li>
  <li>결정을 액체에서 굳혀서 뽑아 올리는 속도가 전위의 이동 속도보다 빠르면, <strong>전위가 새로 굳어지는 결정 아래쪽으로 번져나가지 못하고 위쪽에 갇힌 채 순식간에 외벽으로 튕겨 나가게 됩니다.</strong></li>
</ul>

<h3>6. 윌리엄 대시(William Dash)의 위대한 발견 (1958년)</h3>
<p>
1958년 GE의 <strong>윌리엄 대시(William C. Dash)</strong> 박사가 이 원리를 발견하기 전까지, 전 세계 과학자들은 1400℃의 열충격을 견디고 무전위 단결정을 키우는 것은 불가능하다고 생각했습니다.
</p>
<ul>
  <li>대시 박사는 씨드를 담근 직후 <strong>직경을 2~3mm로 잘록하게 줄여 50~100mm 정도 길게 뽑아내는 간단한 방법(Dash Necking)</strong>만으로 모든 열충격 결함을 밖으로 퇴출시킬 수 있음을 증명했습니다.</li>
  <li><strong>놀라운 물리적 반전</strong>: 사람들은 <em>"겨우 2~3mm 실리콘 목(Neck)이 어떻게 수백 kg짜리 거대 잉곳 무게를 버티겠느냐, 끊어질 것이다"</em>라고 우려했습니다.</li>
  <li>그러나 <strong>결함(전위)이 단 1개도 없는 완벽한 단결정 실리콘의 공유결합 인장 강도는 강철보다 강합니다!</strong> 실제로 이 얇은 3mm의 네킹 부위가 <strong>300~500kg에 달하는 300mm 잉곳의 전체 하중을 거뜬히 지탱</strong>합니다.</li>
</ul>

<h3>7. 최종 요약 (질문에 대한 명쾌한 1줄 정리)</h3>
<blockquote style="border-left:4px solid #38bdf8; padding-left:12px; color:#e2e8f0; font-weight:600; margin:15px 0;">
"전위는 수직이 아니라 <strong>약 55도 대각선(사선)으로 자라기 때문에</strong>, 잉곳 굵기를 2~3mm로 좁히면 <strong>대각선으로 뻗던 전위선들이 몇 mm도 못 가서 외벽 표면(Free Surface)에 부딪혀 밖으로 빠져나와 100% 소멸</strong>하는 것입니다!"
</blockquote>
"""

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 70 topics (q-70 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(70, 0, -1):
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
        r"최상단에는 '네킹공정을 통해 열충격 전위를 밖으로 배출시키는 원리 (사선 소멸)'이 위치하며, 총 71개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Dash Necking topic!")
