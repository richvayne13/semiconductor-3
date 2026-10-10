# -*- coding: utf-8 -*-
"""
insert_undercut_q01.py
사용자 질문: "undercut이 뭐야"
대시보드 최상단 Q01로 신규 추가하고, 기존 73개 질문을 Q02~Q74로 시프트 (총 74개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (식각 공정 & 패턴 프로파일)",
    "title": "언더컷(Undercut)이란 무엇인가? (등방성 식각에 의한 마스크 하부 침식과 GAA 이너스페이서 응용)",
    "nav_title": "언더컷(Undercut)이란 무엇인가? (원리, 문제점, GAA 응용)",
    "summary": [
        "<strong>언더컷(Undercut)의 직관적 정의</strong>: 식각(Etching) 공정 중 마스크(감광액 PR 또는 하드마스크)로 덮여 보호되어야 할 <strong>하부 박막이 마스크 밑바닥 안쪽으로 수평 침식되어 파고들어 깎여나가는 현상</strong>입니다 (파도에 밑동이 파인 해안 절벽 비유).",
        "<strong>발생 메커니즘 (등방성 식각 Isotropic)</strong>: 화학적 식각액(습식 식각)이나 화학 라디칼은 방향성 없이 모든 방향으로 동일한 속도로 반응하므로, 아래로 깎여 내려가는 수직 식각 속도($R_V$)만큼 마스크 옆구리를 파고드는 수평 식각 속도($R_L$)가 발생하여 필연적으로 언더컷이 생깁니다.",
        "<strong>미세화 공정에서의 치명적 문제점</strong>: ① 설계한 패턴 폭보다 실제 선폭이 얇아지는 <strong>CD(임계 선폭) 손실</strong>, ② 패턴 밑동이 잘려 기둥이 쓰러지는 <strong>패턴 붕괴(Pattern Collapse)</strong>, ③ 트랜지스터 게이트 길이 편차로 인한 누설전류 폭증을 유발합니다 (➔ 이온 충돌 RIE와 측벽 폴리머 보호막으로 극복).",
        "<strong>최첨단 GAA에서의 의도적 활용 (대반전!)</strong>: 현대 첨단 3nm GAA(Gate-All-Around) 공정에서는 나노시트 사이의 SiGe 희생층을 수평 방향으로만 정밀하게 깎아내는 <strong>'제어된 언더컷(Selective Lateral Etch)'</strong>을 통해 기생 커패시턴스를 막는 <strong>이너 스페이서(Inner Spacer) 공간</strong>을 형성합니다."
    ],
    "svg_title": "📊 [식각 프로파일 비교: 수직 비등방 vs 언더컷 등방 식각] 언더컷 단면 구조와 최신 GAA 나노시트 활용",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: Ideal Anisotropic vs Undercut Profile -->
  <rect x="20" y="25" width="375" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="48" fill="#38bdf8" font-size="12" font-weight="800">1. 식각 단면 프로파일: 비등방성 vs 언더컷(등방성)</text>

  <!-- Top: Ideal Anisotropic Etch -->
  <g transform="translate(35, 60)">
    <rect x="0" y="0" width="345" height="110" rx="6" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="12" y="18" fill="#34d399" font-size="9.5" font-weight="700">✔ 이상적인 수직 식각 (비등방성 Anisotropic, Af ≈ 1)</text>

    <!-- Mask -->
    <rect x="120" y="26" width="100" height="16" fill="#6366f1" rx="2"/>
    <text x="135" y="38" fill="#ffffff" font-size="8.5" font-weight="700">Mask (PR / 하드마스크)</text>

    <!-- Substrate film etched vertically -->
    <rect x="120" y="42" width="100" height="42" fill="#0284c7" rx="1"/>
    <text x="140" y="66" fill="#ffffff" font-size="9" font-weight="700">수직 패턴 (완벽)</text>
    
    <!-- Base Substrate -->
    <rect x="20" y="84" width="305" height="14" fill="#334155" rx="1"/>
    <text x="110" y="94" fill="#94a3b8" font-size="7.5">기판 (Substrate)</text>

    <text x="12" y="104" fill="#6ee7b7" font-size="8">• 수평 식각 RL = 0 ➔ 마스크 폭 = 실제 패턴 폭 (CD 손실 0%)</text>
  </g>

  <!-- Bottom: Undercut Case -->
  <g transform="translate(35, 185)">
    <rect x="0" y="0" width="345" height="145" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="12" y="18" fill="#f87171" font-size="9.5" font-weight="700">❌ 언더컷 발생 (등방성 Isotropic, RL &gt; 0)</text>

    <!-- Mask -->
    <rect x="100" y="26" width="140" height="16" fill="#6366f1" rx="2"/>
    <text x="125" y="38" fill="#ffffff" font-size="8.5" font-weight="700">Mask (너비 140nm)</text>

    <!-- Undercut Film profile (curved concave beneath mask) -->
    <path d="M 125 42 Q 135 63 125 84 L 215 84 Q 205 63 215 42 Z" fill="#ef4444" opacity="0.8"/>
    <text x="142" y="66" fill="#ffffff" font-size="9" font-weight="800">패턴 폭 축소!</text>

    <!-- Undercut Arrows -->
    <line x1="100" y1="52" x2="123" y2="52" stroke="#fbbf24" stroke-width="2"/>
    <polygon points="123,49 128,52 123,55" fill="#fbbf24"/>
    <text x="75" y="48" fill="#fbbf24" font-size="7.5" font-weight="800">언더컷 (ΔL)</text>

    <line x1="240" y1="52" x2="217" y2="52" stroke="#fbbf24" stroke-width="2"/>
    <polygon points="217,49 212,52 217,55" fill="#fbbf24"/>
    <text x="220" y="48" fill="#fbbf24" font-size="7.5" font-weight="800">언더컷 (ΔL)</text>

    <!-- Base Substrate -->
    <rect x="20" y="84" width="305" height="14" fill="#334155" rx="1"/>

    <text x="12" y="108" fill="#fca5a5" font-size="8.5" font-weight="700">★ 언더컷 = 마스크 아래쪽으로 파고든 수평 식각 거리(ΔL)</text>
    <text x="12" y="122" fill="#cbd5e1" font-size="8">• 마스크는 남아있으나 아래 밑동이 파먹혀 선폭(CD)이 심각하게 얇아짐</text>
    <text x="12" y="136" fill="#94a3b8" font-size="7.5">• 심할 경우 마스크가 떨어져 나가거나 패턴이 쓰러지는 대참사(Collapse)</text>
  </g>

  <!-- Right: Where Undercut is Used Intentionally (GAA Inner Spacer) -->
  <rect x="410" y="25" width="350" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
  <text x="425" y="48" fill="#10b981" font-size="12" font-weight="800">2. 첨단 기술에서의 의도적 활용: GAA 이너 스페이서</text>

  <!-- GAA Nanosheet Inner Spacer Diagram -->
  <g transform="translate(425, 65)">
    <!-- Gate Stack Area -->
    <rect x="0" y="0" width="320" height="150" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
    <text x="12" y="18" fill="#38bdf8" font-size="9.5" font-weight="800">GAA 나노시트: SiGe 희생층 수평 선택 언더컷</text>

    <!-- Silicon Nanosheet 3 -->
    <rect x="50" y="28" width="220" height="12" fill="#0284c7" rx="1"/>
    <text x="110" y="37" fill="#ffffff" font-size="7">Si 나노시트 채널 #3</text>

    <!-- Inner Spacer Cavity (Undercut into SiGe) -->
    <rect x="50" y="42" width="25" height="16" fill="#f59e0b" rx="1"/>
    <rect x="245" y="42" width="25" height="16" fill="#f59e0b" rx="1"/>
    <rect x="77" y="42" width="166" height="16" fill="#475569" rx="1"/>
    <text x="95" y="53" fill="#cbd5e1" font-size="7">SiGe 잔여 / 게이트 영역</text>
    <text x="15" y="54" fill="#fbbf24" font-size="7" font-weight="700">언더컷 틈</text>

    <!-- Silicon Nanosheet 2 -->
    <rect x="50" y="60" width="220" height="12" fill="#0284c7" rx="1"/>
    <text x="110" y="69" fill="#ffffff" font-size="7">Si 나노시트 채널 #2</text>

    <!-- Inner Spacer Cavity 2 -->
    <rect x="50" y="74" width="25" height="16" fill="#f59e0b" rx="1"/>
    <rect x="245" y="74" width="25" height="16" fill="#f59e0b" rx="1"/>
    <rect x="77" y="74" width="166" height="16" fill="#475569" rx="1"/>

    <!-- Silicon Nanosheet 1 -->
    <rect x="50" y="92" width="220" height="12" fill="#0284c7" rx="1"/>
    <text x="110" y="101" fill="#ffffff" font-size="7">Si 나노시트 채널 #1</text>

    <text x="12" y="122" fill="#fef08a" font-size="8" font-weight="700">★ 황색 영역: 수평 언더컷으로 파낸 뒤 Low-k 유전체 채움!</text>
    <text x="12" y="136" fill="#93c5fd" font-size="7.5">➔ 게이트와 소스/드레인 간 기생 커패시턴스(C_gd) 극소화 달성</text>
  </g>

  <!-- Explanatory Box -->
  <g transform="translate(425, 222)">
    <rect x="0" y="0" width="320" height="110" rx="6" fill="#1e293b"/>
    <text x="10" y="18" fill="#38bdf8" font-size="9.5" font-weight="800">■ 언더컷(Undercut) 총정리</text>
    <text x="10" y="35" fill="#fca5a5" font-size="8.5">• 일반 공정: 등방성 식각에 의한 불량 (CD 손실, 선폭 붕괴)</text>
    <text x="10" y="52" fill="#6ee7b7" font-size="8.5">• 방어 대책: 플라즈마 RIE + 탄화불소 측벽 보호막(Passivation)</text>
    <text x="10" y="69" fill="#34d399" font-size="8.5">• 최신 응용: GAA 나노시트 릴리즈 &amp; 이너스페이서(Inner Spacer)</text>
    <text x="10" y="86" fill="#cbd5e1" font-size="8.5">• MEMS 구조물 부유(Suspended Structure) 제조 시 필수 기술</text>
    <text x="10" y="102" fill="#94a3b8" font-size="7.5">• 결론: "제어하지 못하면 재앙, 정밀 제어하면 최첨단 무기!"</text>
  </g>
</svg>"""
}

NEW_TOPIC["lecture"] = r"""
<h3>1. 언더컷(Undercut)의 직관적 정의</h3>
<p>
<strong>언더컷(Undercut)</strong>이란, 반도체 패터닝 및 식각(Etching) 공정에서 
<strong>마스크(Mask, 감광액 PR 또는 하드마스크) 바로 아래쪽의 박막이 마스크 밑바닥 안쪽으로 수평 침식되어 파고들어 깎여나가는 현상</strong> 또는 
그 <strong>수평으로 파고든 깊이(거리 $\Delta L$)</strong>를 의미합니다.
</p>
<div style="background:#0f172a; border-left:4px solid #ef4444; padding:15px; margin:16px 0; border-radius:0 8px 8px 0;">
  <strong style="color:#f87171; font-size:1.05rem;">💡 가장 쉬운 자연 비유: '파도에 깎인 해식애(해안 절벽)'</strong><br>
  바닷가 절벽을 보면 파도가 찰랑이는 바닥 밑동만 옴푹하게 파여 있고, 그 위쪽 바위는 모자처럼 앞으로 툭 튀어나와 있는 모습을 볼 수 있습니다.<br>
  이처럼 <strong>위의 뚜껑(마스크)은 그대로 남아있는데, 그 밑바닥(박막)만 안쪽으로 쏙 파먹혀 들어간 모양</strong>을 반도체 공학에서 <strong>'언더컷(Undercut)'</strong>이라고 부릅니다.
</div>

<h3>2. 왜 언더컷이 생길까? (등방성 식각과 비등방성 계수)</h3>
<p>
언더컷이 발생하는 근본적인 물리/화학적 원인은 <strong>'등방성 식각(Isotropic Etching)'</strong> 때문입니다.
</p>
<ul>
  <li><strong>습식 식각 (Wet Etch) & 화학 라디칼</strong>: 화학 용액이나 플라즈마 속의 중성 라디칼은 특정한 방향이 없습니다. 모든 방향으로 똑같은 속도로 화학 반응을 일으킵니다.</li>
  <li><strong>수평 식각 속도 ($R_L > 0$)</strong>: 화학 물질이 아래로 파고들어 내려가는 속도(수직 식각 속도 $R_V$)와 똑같은 속도로, <strong>마스크 아래 옆구리 쪽으로도 침투하여 파고듭니다(수평 식각 속도 $R_L$).</strong></li>
</ul>

<p>
식각의 방향성을 나타내는 <strong>비등방성 계수($A_f$)</strong> 공식:
</p>
<div style="text-align:center; padding:10px; background:#111827; border-radius:8px; margin:12px 0; font-size:1.1rem; color:#38bdf8; font-weight:700;">
  $$A_f = 1 - \frac{R_L}{R_V}$$
</div>
<ul>
  <li><strong>이상적인 수직 식각 ($A_f = 1$)</strong>: 수평 식각 $R_L = 0$이므로 마스크 모양 그대로 90도 직각 수직벽이 나옵니다 (언더컷 없음).</li>
  <li><strong>등방성 식각 ($A_f \approx 0$)</strong>: 수평 식각 속도와 수직 식각 속도가 같아($R_L \approx R_V$), <strong>수직으로 깎여 내려간 깊이만큼 마스크 아래쪽으로도 깊숙이 파고드는 거대한 언더컷</strong>이 발생합니다.</li>
</ul>

<h3>3. 반도체 미세 공정에서 언더컷이 치명적인 3대 이유</h3>
<ol>
  <li><strong>CD(임계 선폭, Critical Dimension) 손실</strong>:
    <p>
    노광 장비로 10nm 폭의 마스크를 정밀하게 만들어 놓았는데, 언더컷이 양쪽으로 3nm씩 파먹고 들어가면 실제 남는 배선 폭은 4nm로 쪼그라듭니다. 심할 경우 선폭이 0이 되어 배선이 끊어지는 단선 불량이 납니다.
    </p>
  </li>
  <li><strong>패턴 붕괴 (Pattern Collapse) 및 박리 (Peel-off)</strong>:
    <p>
    종횡비(Aspect Ratio, 높이/폭 비율)가 높은 미세 패턴에서 밑동이 깎여나가면 기둥이 무게중심을 잃고 감자칩처럼 옆으로 쓰러지거나(Collapse), 마스크가 웨이퍼에서 훌러덩 벗겨져 날아갑니다.
    </p>
  </li>
  <li><strong>트랜지스터 게이트 길이 편차와 누설 전류</strong>:
    <p>
    트랜지스터 게이트 밑바닥에 언더컷이 생기면 게이트 물리적 길이($L_g$)가 제어 불능 상태로 변합니다. 단채널 효과(SCE)와 문턱전압 편차가 극심해져 웨이퍼 전체 수율이 괴멸합니다.
    </p>
  </li>
</ol>

<h3>4. 언더컷을 막는 반도체 공학의 해결책: 플라즈마 RIE와 측벽 보호막</h3>
<p>
이 언더컷 재앙을 막고 수직 90도 벽을 만들기 위해 탄생한 기술이 바로 <strong>비등방성 건식 식각(RIE, Reactive Ion Etching)</strong>입니다:
</p>
<div style="background:#1e1b4b; border:1px solid #4338ca; border-radius:8px; padding:15px; margin:16px 0;">
  <strong style="color:#a5b4fc; font-size:1rem;">🛡️ 언더컷 방어 2대 메커니즘:</strong><br>
  1. <strong>쉬스 전계에 의한 수직 이온 충돌 (Ion Bombardment)</strong>: 플라즈마 속 양이온을 수직 전계로 웨이퍼 바닥으로만 내리꽂아 수직 방향으로만 결합을 물리적으로 파괴합니다.<br>
  2. <strong>측벽 보호 폴리머 (Passivation Polymer)</strong>: 탄화불소($C_x F_y$) 가스를 함께 넣어 식각과 동시에 패턴 측벽에 얇은 플라스틱 보호막(Teflon-like Film)을 코팅합니다. 바닥은 이온이 때려 부수며 계속 파내려가지만, <strong>옆벽은 이온이 때리지 못해 보호막이 그대로 남아 화학 라디칼의 측면 공격(언더컷)을 철벽 방어</strong>합니다.
</div>

<h3>5. [대반전!] 현대 첨단 반도체에서는 언더컷을 '무기'로 쓴다? (GAA 이너 스페이서)</h3>
<p>
과거에는 언더컷이 무조건 없애야 할 불량이었지만, <strong>현대 최첨단 3nm GAA(Gate-All-Around) 나노시트 공정에서는 언더컷이 없으면 소자를 만들 수 없습니다!</strong>
</p>
<ul>
  <li><strong>Si / SiGe 다층 에피 적층</strong>: 실리콘(채널)과 실리콘게르마늄(희생층)을 시루떡처럼 번갈아 쌓습니다.</li>
  <li><strong>선택적 수평 식각 (Selective Lateral Etch = 의도적 언더컷!)</strong>: 
    실리콘 채널은 털끝 하나 건드리지 않고, <strong>SiGe 희생층의 옆구리만 정확히 수 나노미터(nm) 안쪽으로 파먹어 들어가는 초정밀 언더컷</strong>을 고의로 유도합니다.</li>
  <li><strong>이너 스페이서(Inner Spacer) 형성</strong>:
    언더컷으로 파여서 생긴 빈 틈새 공간에 유전율이 낮은 Low-k 절연막을 채워 넣어 <strong>'이너 스페이서'</strong>를 만듭니다.</li>
  <li><strong>효과</strong>: 게이트 금속과 소스/드레인 사이의 기생 커패시턴스를 획기적으로 차단하여 GAA 트랜지스터의 동작 속도를 극한으로 끌어올립니다.</li>
</ul>

<h3>6. 핵심 요약 (1줄 정리)</h3>
<blockquote style="border-left:4px solid #38bdf8; padding-left:12px; color:#e2e8f0; font-weight:600; margin:15px 0;">
"<strong>언더컷(Undercut)</strong>은 등방성 식각에 의해 <strong>마스크 바로 밑바닥 박막이 수평 안쪽으로 파고들어 깎여나가는 현상</strong>으로, 제어하지 못하면 선폭 손실(CD 손실)과 패턴 붕괴를 일으키는 불량이지만, 첨단 GAA 공정에서는 SiGe를 수평으로 파내어 이너 스페이서를 만드는 핵심 무기로 활용됩니다!"
</blockquote>
"""

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 73 topics (q-73 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(73, 0, -1):
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
        r"최상단에는 '언더컷(Undercut)이란 무엇인가? (원리, 문제점, GAA 응용)'이 위치하며, 총 74개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Undercut topic!")
