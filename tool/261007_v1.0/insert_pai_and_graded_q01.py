# -*- coding: utf-8 -*-
"""
insert_pai_and_graded_q01.py
사용자 질문: "도핑농도를 갈수록 완만하게하면 공핍층넓어지는원리, cj감소하는원리 pai기술이 뭐야?"
대시보드 최상단 Q01로 신규 추가하고, 기존 75개 질문을 Q02~Q76으로 시프트 (총 76개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (이온주입 공정 & 접합 물리)",
    "title": "도핑을 완만하게 할 때 공핍층(Wdep) 확장과 Cj 감소 원리 & PAI(사전 비정질화 이온주입) 기술 완전 정복",
    "nav_title": "완만한 도핑의 Cj 감소 원리와 PAI(사전 비정질화) 기술",
    "summary": [
        "<strong>완만한 경사 도핑의 공핍층 확장 및 Cj 감소</strong>: 급준 접합 대비 농도 경사가 완만하면($\\rho = qax$) 계면 부근의 공간 전하 밀도가 희박해져, 전하 중성($Q^+=Q^-$)을 만족하기 위해 <strong>공핍층이 실리콘 깊숙이 넓게 벌어집니다($W_{dep} \\propto a^{-1/3}$)</strong>. 공핍층 폭은 평행판 커패시터의 유전체 두께($d$)이므로 <strong>$C_j = \\epsilon_s / W_{dep}$에 의해 기생 커패시턴스가 획기적으로 감소</strong>합니다.",
        "<strong>PAI(Pre-Amorphization Implantation)의 정의</strong>: 가벼운 붕소($B$) 이온을 주입하기 전에, 무거운 <strong>게르마늄($Ge$)이나 실리콘($Si$) 이온을 먼저 때려 넣어 표면 단결정 실리콘을 '비정질(Amorphous) 실리콘'으로 미리 부숴놓는 사전 공정</strong>입니다.",
        "<strong>PAI의 도입 목적 (채널링 Channeling 원천 봉쇄)</strong>: 단결정 실리콘의 원자 기둥 사이로 이온이 저항 없이 깊숙이 침투하는 '채널링 현상'을 랜덤 비정질 구조로 원천 차단하여, <strong>불순물이 표면 10nm 이내에만 얌전하게 멈추는 초얕은 접합(USJ, Ultra-Shallow Junction)을 완성</strong>합니다.",
        "<strong>SPER 고상 에피 재결정화</strong>: 붕소 주입 후 급속 열처리(RTA/LSA)를 가하면, 파괴되지 않은 하부 단결정을 씨앗(Seed) 삼아 비정질층이 원자 단위로 정렬되며 <strong>완벽한 단결정으로 되돌아오는 SPER(Solid Phase Epitaxial Regrowth)</strong>가 일어납니다."
    ],
    "svg_title": "📊 [경사 접합의 Wdep 확장 & PAI 이온주입 원리도] 전하 중성 삼각형 모델 및 Ge 사전 비정질화 채널링 방지",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: Graded Junction Wdep & Cj mechanism -->
  <rect x="20" y="25" width="375" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="48" fill="#38bdf8" font-size="12" font-weight="800">1. 완만한 도핑(경사 접합) ➔ Wdep 확장 ➔ Cj 감소</text>

  <g transform="translate(35, 60)">
    <!-- Abrupt vs Graded comparison -->
    <rect x="0" y="0" width="345" height="120" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="12" y="18" fill="#f87171" font-size="9.5" font-weight="700">■ 급준 접합 (Abrupt) vs 경사 접합 (Graded)</text>

    <!-- Graded space charge triangle -->
    <path d="M 50 65 L 172 25 L 172 65 Z" fill="#38bdf8" opacity="0.6"/>
    <path d="M 172 65 L 172 105 L 294 65 Z" fill="#f59e0b" opacity="0.6"/>
    <line x1="30" y1="65" x2="315" y2="65" stroke="#94a3b8" stroke-width="1.5"/>
    <line x1="172" y1="20" x2="172" y2="110" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,2"/>
    <text x="165" y="16" fill="#cbd5e1" font-size="7.5">x=0</text>
    <text x="75" y="55" fill="#ffffff" font-size="8" font-weight="800">+Q (완만)</text>
    <text x="220" y="80" fill="#ffffff" font-size="8" font-weight="800">-Q (완만)</text>

    <text x="50" y="115" fill="#38bdf8" font-size="8">◄─── W_dep 대폭 확장 (밑변 늚) ───►</text>
  </g>

  <g transform="translate(35, 190)">
    <rect x="0" y="0" width="345" height="140" rx="6" fill="#1e293b"/>
    <text x="12" y="18" fill="#38bdf8" font-size="9.5" font-weight="700">■ 핵심 물리 알고리즘 요약</text>
    <text x="12" y="36" fill="#cbd5e1" font-size="8.5">• 전하 밀도 기울기 a 작음 ➔ 계면 근처 이온 밀도 희박</text>
    <text x="12" y="52" fill="#cbd5e1" font-size="8.5">• 전하 중성 면적을 채우려면 삼각형 밑변(W_dep)이 넓어져야 함</text>
    <text x="12" y="70" fill="#f59e0b" font-size="9" font-weight="800">• 푸아송 적분: W_dep = [12ε_s(V_bi - V) / (q·a)]^(1/3)</text>
    <text x="12" y="88" fill="#34d399" font-size="9" font-weight="800">• 평행판 모델: C_j = ε_s · A / W_dep ➔ C_j 대폭 감소!</text>
    <text x="12" y="104" fill="#93c5fd" font-size="8">• S/D LDD 영역의 기생 부하 커패시턴스 및 RC 지연 획기적 개선</text>
    <text x="12" y="118" fill="#94a3b8" font-size="7.5">• 전계 피크(E_max) 완화로 애벌랜치 항복전압(BV) 및 HCI 내구성 향상</text>
  </g>

  <!-- Right: PAI (Pre-Amorphization Implantation) -->
  <rect x="410" y="25" width="350" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
  <text x="425" y="48" fill="#10b981" font-size="12" font-weight="800">2. PAI(사전 비정질화)의 원리와 채널링 방지</text>

  <!-- PAI 3-step sequence -->
  <g transform="translate(425, 62)">
    <!-- Step 1: Without PAI (Channeling Disaster) -->
    <rect x="0" y="0" width="320" height="65" rx="4" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
    <text x="10" y="14" fill="#f87171" font-size="8" font-weight="700">❌ PAI 미적용: 단결정 원자 격자 ➔ 채널링(Channeling) 폭망</text>
    <line x1="20" y1="22" x2="20" y2="48" stroke="#f59e0b" stroke-width="2"/>
    <line x1="40" y1="22" x2="40" y2="48" stroke="#f59e0b" stroke-width="2"/>
    <line x1="60" y1="22" x2="60" y2="60" stroke="#ef4444" stroke-width="3"/>
    <text x="75" y="35" fill="#fca5a5" font-size="7.5">가벼운 B 이온이 원자 터널을 타고</text>
    <text x="75" y="47" fill="#fca5a5" font-size="7.5">지하 깊숙이 침투 (Xj 통제 불가!)</text>

    <!-- Step 2: PAI Applied (Ge+ creates a-Si) -->
    <rect x="0" y="72" width="320" height="75" rx="4" fill="#1e293b" stroke="#10b981" stroke-width="1"/>
    <text x="10" y="86" fill="#34d399" font-size="8" font-weight="700">✔ 1단계 PAI (Ge⁺ 사전 주입): 표면 비정질화 (a-Si 형성)</text>
    <rect x="15" y="93" width="70" height="22" fill="#047857" rx="1"/>
    <text x="22" y="107" fill="#a7f3d0" font-size="7.5" font-weight="800">비정질층 (a-Si)</text>
    <rect x="15" y="117" width="70" height="22" fill="#1e3a8a" opacity="0.6"/>
    <text x="25" y="130" fill="#93c5fd" font-size="7">단결정 Si 기판</text>
    <text x="95" y="103" fill="#cbd5e1" font-size="7.5">• 무거운 Ge 이온이 격자를 깨뜨림</text>
    <text x="95" y="117" fill="#34d399" font-size="7.5">• 원자 터널(회랑) 완전 붕괴 ➔ 랜덤 벽</text>
    <text x="95" y="131" fill="#fef08a" font-size="7.5">• 붕소 주입 시 표면 10nm에서 정지!</text>

    <!-- Step 3: SPER Anneal -->
    <rect x="0" y="154" width="320" height="95" rx="4" fill="#1e293b"/>
    <text x="10" y="170" fill="#38bdf8" font-size="8.5" font-weight="800">■ 2단계 SPER 열처리 (고상 에피 재결정화)</text>
    <text x="10" y="188" fill="#cbd5e1" font-size="8">• RTA/레이저 열처리: 하부 단결정을 씨앗 삼아 단결정 복원</text>
    <text x="10" y="204" fill="#cbd5e1" font-size="8">• EOR(End-of-Range) 결함: 비정질 경계면 잔류 결함 제어</text>
    <text x="10" y="220" fill="#34d399" font-size="8.5" font-weight="700">★ 결과: 초얕은 접합(USJ, Xj &lt; 10nm) 완벽 실현 ➔ SCE 방어!</text>
    <text x="10" y="236" fill="#94a3b8" font-size="7.5">• PMOS p-n 접합 깊이를 극소화하여 DIBL 및 펀치스루 박멸</text>
  </g>
</svg>"""
}

NEW_TOPIC["lecture"] = r"""
<h3>1. 질문의 핵심 분해</h3>
<p>
질문자께서 두 가지 핵심 반도체 소자/공정 원리를 질문해 주셨습니다:
</p>
<ol>
  <li><strong>"도핑 농도를 완만하게 하면 왜 공핍층($W_{dep}$)이 넓어지고 접합 커패시턴스($C_j$)가 줄어들까?"</strong></li>
  <li><strong>"반도체 공정에서 PAI(사전 비정질화 이온주입) 기술이란 무엇인가?"</strong></li>
</ol>
<p>
이 두 가지는 첨단 반도체 트랜지스터에서 **단채널 효과(SCE)를 방어하고 기생 RC 지연을 극소화**하기 위해 반드시 함께 이해해야 하는 핵심 메커니즘입니다.
</p>

---

<h3>2. Part 1: 도핑 농도가 완만할 때 $W_{dep}$가 넓어지고 $C_j$가 줄어드는 원리</h3>

<h4>① 공간 전하 밀도와 전하 중성 삼각형 모델</h4>
<p>
접합면($x=0$)을 기준으로 도핑 농도가 급격히 변하는 '급준 접합(Abrupt Junction)'과 달리, 
도핑 농도가 거리에 따라 비례하여 완만하게 증가하는 **'경사 접합(Linearly Graded Junction)'**의 전하 밀도는 다음과 같습니다:
</p>
<div style="text-align:center; padding:10px; background:#111827; border-radius:8px; margin:12px 0; font-size:1.1rem; color:#38bdf8; font-weight:700;">
  $$\rho(x) = q \cdot a \cdot x \quad (a\text{ : 도핑 농도 기울기, Slope})$$
</div>
<ul>
  <li><strong>기울기 $a$가 완만하다(작다)는 의미</strong>: 접합면 근처의 불순물 이온 밀도가 아주 희박하다는 뜻입니다.</li>
  <li><strong>전하 중성 원리 ($Q^+ = Q^-$)</strong>: p-n 접합 양단에 형성되는 총 전하량(전하 밀도 그래프의 면적)은 무조건 같아야 합니다.</li>
  <li><strong>기하학적 삼각형 면적의 원리</strong>:
    $$\text{총 전하량 } Q = \frac{1}{2} \times \text{높이}(q a x_0) \times \text{밑변}(x_0) = \frac{1}{2} q a x_0^2$$
    기울기 $a$가 완만해서 높이가 낮아지면, <strong>동일한 전하량을 확보하기 위해 필연적으로 밑변(공핍층 깊이 $x_0$)이 실리콘 깊숙이 넓게 벌어져야만 합니다!</strong>
  </li>
</ul>

<h4>② 푸아송 방정식 유도와 $C_j$ 반비례</h4>
<p>
푸아송 방정식을 2번 적분하여 유도한 경사 접합의 공핍층 폭 공식은 다음과 같습니다:
</p>
<div style="text-align:center; padding:10px; background:#111827; border-radius:8px; margin:12px 0; font-size:1.1rem; color:#f59e0b; font-weight:700;">
  $$W_{dep} = \left[ \frac{12 \epsilon_s (V_{bi} - V)}{q \cdot \mathbf{a}} \right]^{1/3} \propto \mathbf{a^{-1/3}}$$
</div>
<ul>
  <li>도핑 기울기 $a$가 완만해질수록($a \downarrow$) 분모가 작아지므로 <strong>공핍층 폭은 급격하게 확장($W_{dep} \uparrow$)</strong>됩니다.</li>
  <li>공핍층은 자유 전하가 없는 절연체이므로 <strong>평행판 커패시터 모델($C = \epsilon A / d$)</strong>이 적용됩니다:
    $$C_j = \frac{\epsilon_s A}{\mathbf{W_{dep}}}$$
  </li>
  <li>따라서 공핍층 유전체 간격($W_{dep}$)이 넓어지므로 **접합 커패시턴스는 획기적으로 급감($C_j \downarrow$)**하게 됩니다!</li>
</ul>

---

<h3>3. Part 2: PAI (Pre-Amorphization Implantation) 기술이란 무엇인가?</h3>

<h4>① PAI의 탄생 배경: 가벼운 붕소(Boron)의 채널링(Channeling) 악몽</h4>
<p>
PMOS 트랜지스터의 소스/드레인 확산층을 만들기 위해 3족 불순물인 <strong>붕소(Boron, $B$)</strong>를 이온주입합니다.
그런데 붕소는 원자번호 5번으로 원자량이 11밖에 안 되는 **극도로 가볍고 작은 원자**입니다.
</p>
<div style="background:#1e1b4b; border:1px solid #4338ca; border-radius:8px; padding:14px; margin:14px 0;">
  <strong style="color:#a5b4fc;">⚠️ 채널링(Channeling) 현상의 재앙:</strong><br>
  • 단결정 실리콘은 원자들이 규칙적으로 격자를 이루고 있어, 정면에서 바라보면 원자 기둥 사이에 텅 빈 공간(회랑, Tunnel)이 길게 뚫려 있습니다.<br>
  • 가벼운 붕소 이온을 쏘면, 이 원자 터널 사이를 미끄러지듯 통과하면서 아무런 충돌 없이 <strong>원래 목표했던 깊이보다 3~5배 이상 지하 깊숙이 뚫고 들어가 버립니다(채널링 현상).</strong><br>
  • 그 결과 접합 깊이($X_j$)가 깊어져 드레인 공핍층이 채널 밑으로 침범하여 **단채널 효과(DIBL, 펀치스루)가 폭발**해 트랜지스터가 망가집니다.
</div>

<h4>② PAI(사전 비정질화)의 3단계 해결 시퀀스</h4>
<p>
이 문제를 해결하기 위해 고안된 천재적인 기술이 바로 <strong>PAI(Pre-Amorphization Implantation)</strong>입니다.
<em>"단결정에 원자 터널이 있어서 붕소가 깊이 들어간다면, 붕소를 쏘기 전에 터널을 먼저 다 부숴버리면 어떨까?"</em>라는 아이디어입니다!
</p>

```
========================================================================================
                          [PAI 공정의 3단계 메커니즘]
========================================================================================

  [1단계: PAI 공정 (사전 비정질화)]
  • 붕소를 쏘기 '직전'에, 무거운 게르마늄(Ge⁺)이나 실리콘(Si⁺) 이온을 표면에 먼저 때려 박음.
  • 무거운 Ge 원자가 실리콘 원자 격자를 쾅쾅 쳐서 격자 배열을 완전히 박살냄.
  • ──▶ 표면 수십 nm 두께의 단결정이 [비정질 실리콘(a-Si, Amorphous)] 층으로 변함!
         (원자 터널이 완전히 무너져 랜덤한 벽돌담으로 바뀜)

  [2단계: 붕소(Boron) 초저에너지 이온주입]
  • 비정질 실리콘 층 위에 가벼운 붕소(B) 이온을 주입함.
  • 터널(채널링 경로)이 없으므로, 붕소가 비정질 벽에 부딪혀 [표면 10nm 이내]에 얌전하게 멈춤!
  • ──▶ 채널링 없는 이상적인 초얕은 접합(USJ, Ultra-Shallow Junction) 프로파일 달성!

  [3단계: SPER 열처리 (고상 에피 재결정화)]
  • 비정질 상태 그대로는 전기가 안 통하므로, 600~1000℃의 급속 열처리(RTA / 레이저 어닐링)를 가함.
  • 깨지지 않고 남아있는 '하부 단결정 기판'을 씨앗(Seed) 삼아, 비정질 원자들이 다시 단결정으로 정렬됨!
  • ──▶ [SPER : Solid Phase Epitaxial Regrowth (고상 에피 성장)]로 완벽한 단결정 복원!
```

<h4>③ PAI의 부작용과 극복: EOR (End-of-Range) 결함 제어</h4>
<p>
PAI 공정에도 하나의 난제가 있습니다. 무거운 $Ge$ 이온이 멈춘 비정질층과 단결정층의 경계면 깊이에 격자 결함이 뭉쳐서 생기는 **EOR(End-of-Range) 결함**입니다.
</p>
<ul>
  <li>EOR 결함이 공핍층 안에 걸치면 **접합 누설 전류(Junction Leakage)**가 증가합니다.</li>
  <li>이를 해결하기 위해 현대 반도체 공정에서는 주입 에너지를 극도로 낮추고, 1밀리초(ms) 만에 표면만 순간 가열하는 **LSA(Laser Spike Annealing, 레이저 스파이크 어닐링)**를 결합하여 EOR 결함을 깨끗이 소멸시킵니다.</li>
</ul>

---

<h3>4. 최종 핵심 요약</h3>

1. **완만한 도핑 (경사 접합)**:  
   접합면 근처의 전하 밀도가 희박하여 전하 중성을 맞추기 위해 **공핍층 폭이 넓어지고($W_{dep} \uparrow$), 평행판 간격 증가로 접합 커패시턴스가 급감($C_j \downarrow$)**하여 RC 지연을 단축시킵니다.
2. **PAI (사전 비정질화 이온주입)**:  
   가벼운 붕소($B$)가 원자 터널을 뚫고 깊이 들어가는 **채널링(Channeling)을 막기 위해**, 무거운 $Ge$ 이온으로 표면을 **비정질 실리콘(a-Si)으로 미리 부숴놓은 뒤 붕소를 10nm 이내로 얕게 가두고 SPER 열처리로 단결정을 복원하는 최첨단 USJ 제조 기술**입니다!
"""

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 75 topics (q-75 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(75, 0, -1):
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
        r"최상단에는 '완만한 도핑의 Cj 감소 원리와 PAI(사전 비정질화) 기술'이 위치하며, 총 76개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 PAI and Graded Junction topic!")
