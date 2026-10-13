# -*- coding: utf-8 -*-
"""
insert_macro_loading_radical_q01.py
사용자 질문:
"[꼬리 1.2]. Pattern 크기가 큰 곳에서 Etch Uniformity가 저하되는 것을 개선시키기 위한 방법에 대해서 말씀해보세요.
Etch 공정시 Pattern의 크기에 따라 박막 표면으로 확산된 단위 면적당 반응종의 농도차이가 발생할 수 있습니다. 그로 인해, Etching Uniformity가 저하되는 이슈를 Macro Loading Effect라고 합니다. 이를 개선시키기 위해서는 압력을 높여야 합니다. 그리고 Bias Power를 감소시켜 충분한 반응종을 공급하여 Pattern 면적 전체에 균일하게 반응할 수 있도록 함으로써 Macro Loading Effect를 완화시킬 수 있습니다.

여기서 반응종이 라디컬이야?"

기존 102개 질문을 Q02~Q103으로 시프트하고, 최상단 Q01에 신규 등록 (총 103개 질문 백과사전 완성).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (건식 식각 & 로딩 이펙트 · 반응종과 라디칼의 실체, 패턴 크기별 식각 불균일 개선 원리)",
    "title": "매크로 로딩 이펙트(Macro Loading Effect)와 라디칼(Radical)의 역할: 패턴 크기별 식각 불균일 원인 및 압력·바이어스 제어 메커니즘 완전 해부",
    "nav_title": "매크로 로딩 이펙트: 반응종(라디칼)과 식각 불균일 개선",
    "summary": [
        "<strong>1. 반응종이 라디칼인가요? ➔ 100% 맞습니다!</strong>: 플라즈마 식각에서 화학적 반응을 주도하는 반응종(Reactive Species)의 실체는 바로 <strong>'중성 라디칼(Neutral Radicals, 예: $\\text{F}^*, \\text{Cl}^*$)'</strong>입니다. 이온은 전계에 의해 수직 직진하지만, 라디칼은 전하가 없어 오직 <strong>'확산(Diffusion)'</strong>으로만 이동하므로 표면 소모율에 따른 국소 농도 차이가 발생합니다.",
        "<strong>2. 매크로 로딩 이펙트(Macro Loading Effect)의 발생 원리: 반응종 고갈(Depletion)</strong>: 오픈 패턴(큰 패턴, 넓은 개구율)은 반응해야 할 실리콘 면적이 넓어 라디칼을 막대하게 소모합니다. 플라즈마 벌크로부터 공급되는 확산 속도보다 표면 소모 속도가 더 빠르면 국소적으로 <strong>'라디칼 고갈(Reactant Depletion)'</strong>이 일어나 식각률(Etch Rate)이 뚝 떨어지게 됩니다.",
        "<strong>3. 압력(Pressure)을 높이는 물리적 이유: 라디칼 절대 공급량 폭증</strong>: 챔버 압력을 높이면 반응 가스 분자 밀도가 증가하고 전자 충돌 빈도가 급증하여 플라즈마 내 <strong>단위 부피당 라디칼 생성량(공급량)이 폭발적으로 증가</strong>합니다. 쏟아부어 주는 라디칼의 절대량이 많아지므로 오픈 패턴의 국소적 고갈을 메워주어 패턴 간 농도 편차를 줄입니다.",
        "<strong>4. 바이어스 파워(Bias Power)를 낮추는 물리적 이유: 소모 속도 제어와 확산 평형 확보</strong>: 과도한 바이어스는 이온 보조 반응을 폭증시켜 '물질 전달 율속(Diffusion limited)' 상태를 유발합니다. 바이어스 파워를 줄이면 표면 반응 속도가 완화되어 라디칼이 국소 고갈되지 않고 패턴 표면 전체로 골고루 퍼져 확산 평형을 이룰 수 있게 되어 <strong>Etch Uniformity가 극적으로 향상</strong>됩니다.",
        "<strong>5. 현업 공정 실무 솔루션: 더미 패턴(Dummy Pattern)과 가스 분사 튜닝</strong>: 실제 반도체 양산에서는 레이아웃 설계 시 넓은 빈 공간에 더미 패턴을 배치하여 <strong>웨이퍼 전면의 식각 패턴 밀도(Pattern Density)를 균등화</strong>하며, 멀티존 가스 샤워헤드(Multi-zone Showerhead)로 취약 영역의 가스 유량을 개별 튜닝합니다."
    ],
    "svg_title": "📊 [매크로 로딩 이펙트 및 반응종(라디칼) 거동 종합 분석 다이어그램] (A) 패턴 크기별 라디칼 농도 고갈 및 식각 불균일 | (B) 반응종의 실체: 중성 라디칼의 확산 거동 ($J = -D \\nabla n$) | (C) 개선 메커니즘 3대 핵심 해법 (압력↑, 바이어스↓, 더미 패턴)",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Macro Loading Phenomenon -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.2"/>
    <text x="16" y="26" fill="#f87171" font-size="12" font-weight="800">■ (A) 매크로 로딩 이펙트: 국소 고갈 현상</text>

    <!-- Visual Wafer Surface -->
    <g transform="translate(15, 40)">
      <rect width="270" height="205" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">패턴 크기에 따른 라디칼 농도 프로파일</text>

      <!-- Bulk Plasma zone -->
      <rect x="15" y="28" width="240" height="24" rx="4" fill="#1e1b4b" stroke="#818cf8"/>
      <text x="25" y="44" fill="#a5b4fc" font-size="7.5" font-weight="700">벌크 플라즈마 영역 (균일한 라디칼 농도 C₀)</text>

      <!-- Diffusion arrows -->
      <path d="M 60 55 L 60 85" stroke="#facc15" stroke-width="2" stroke-dasharray="3,2" marker-end="url(#arrowYellow)"/>
      <path d="M 200 55 L 200 85" stroke="#facc15" stroke-width="2" stroke-dasharray="3,2" marker-end="url(#arrowYellow)"/>

      <!-- Surface Cross Section -->
      <!-- Wide Open Area (Left) -->
      <rect x="25" y="130" width="100" height="25" fill="#334155" stroke="#475569"/>
      <text x="32" y="146" fill="#94a3b8" font-size="7.2">넓은 오픈 패턴 (Open)</text>
      <!-- Shallower etched pit -->
      <path d="M 25 155 L 25 168 L 125 168 L 125 155" fill="none" stroke="#ef4444" stroke-width="2"/>
      <text x="32" y="182" fill="#ef4444" font-size="7.5" font-weight="800">▼ 얕은 식각 (낮은 ER!)</text>

      <!-- Dense / Small Area (Right) -->
      <!-- Mask blocks -->
      <rect x="155" y="125" width="25" height="30" fill="#047857" stroke="#10b981"/>
      <text x="158" y="142" fill="#a7f3d0" font-size="6">PR 마스크</text>
      <rect x="195" y="125" width="25" height="30" fill="#047857" stroke="#10b981"/>
      <text x="198" y="142" fill="#a7f3d0" font-size="6">PR 마스크</text>
      <rect x="235" y="125" width="25" height="30" fill="#047857" stroke="#10b981"/>
      <!-- Deeply etched narrow holes -->
      <path d="M 180 155 L 180 178 L 195 178 L 195 155" fill="none" stroke="#38bdf8" stroke-width="2"/>
      <path d="M 220 155 L 220 178 L 235 178 L 235 155" fill="none" stroke="#38bdf8" stroke-width="2"/>
      <text x="175" y="196" fill="#38bdf8" font-size="7.5" font-weight="800">▲ 깊은 식각 (높은 ER!)</text>

      <!-- Concentration curve overlay -->
      <path d="M 25 110 Q 75 125 125 110 Q 155 95 245 92" fill="none" stroke="#fde047" stroke-width="2.2"/>
      <text x="35" y="105" fill="#f87171" font-size="7" font-weight="800">라디칼 급격 고갈 (C_min)</text>
      <text x="165" y="88" fill="#34d399" font-size="7" font-weight="800">라디칼 농도 풍부 (C_high)</text>
    </g>

    <!-- Explanation Box -->
    <g transform="translate(15, 255)">
      <rect width="270" height="150" rx="5" fill="#0b1329" stroke="#ef4444"/>
      <text x="12" y="18" fill="#f87171" font-size="8.8" font-weight="800">⚠️ 고갈(Depletion) 메커니즘</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="7.5">• <strong>오픈 영역</strong>: 노출 실리콘 면적이 넓음</text>
      <text x="16" y="50" fill="#cbd5e1" font-size="7.2">➔ 표면 라디칼 소모량 급증 ($R_{cons} \gg R_{diff}$)</text>
      <text x="16" y="64" fill="#fde047" font-size="7.5" font-weight="800">➔ 표면 라디칼 농도 고갈 ➔ 식각률(ER) 저하!</text>
      <text x="12" y="82" fill="#cbd5e1" font-size="7.5">• <strong>밀집 영역</strong>: 실리콘 노출 면적이 좁음</text>
      <text x="16" y="96" fill="#cbd5e1" font-size="7.2">➔ 라디칼 소모량 적음 ➔ 표면 농도 풍부</text>
      <text x="16" y="110" fill="#38bdf8" font-size="7.5" font-weight="800">➔ 라디칼 공급 원활 ➔ 식각률(ER) 상대적 높음!</text>
      <text x="12" y="132" fill="#fbbf24" font-size="7.5" font-weight="800">결과: 패턴 크기에 따른 심각한 Etch Non-uniformity!</text>
    </g>
  </g>

  <!-- PANEL B: Nature of Reactive Species (Radical) -->
  <g transform="translate(335, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (B) 반응종의 실체: 왜 라디칼인가?</text>

    <!-- Ion vs Radical Comparison Box -->
    <g transform="translate(15, 40)">
      <rect width="280" height="205" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 플라즈마 내 입자의 이동 거동 비교</text>

      <!-- Ions Behavior -->
      <g transform="translate(10, 26)">
        <rect width="260" height="65" rx="4" fill="#0b1329" stroke="#ef4444"/>
        <text x="10" y="16" fill="#f87171" font-size="7.8" font-weight="800">① 양이온 (Ions: CF₃⁺, Ar⁺) : Drift 거동</text>
        <text x="16" y="32" fill="#cbd5e1" font-size="7">• 전하(+q) 보유 ➔ 시스 전계(E)에 의해 수직 가속</text>
        <text x="16" y="46" fill="#cbd5e1" font-size="7">• 드리프트 속도($v = \mu E$)로 기판에 수직 강타</text>
        <text x="16" y="58" fill="#94a3b8" font-size="6.8">➔ 패턴 면적 차이에 의한 확산 농도 구배 없음</text>
      </g>

      <!-- Radicals Behavior -->
      <g transform="translate(10, 100)">
        <rect width="260" height="92" rx="4" fill="#0b1329" stroke="#10b981"/>
        <text x="10" y="16" fill="#34d399" font-size="8" font-weight="800">② 라디칼 (Radicals: F*, Cl*) : Diffusion 거동 ★</text>
        <text x="16" y="32" fill="#fde047" font-size="7.5" font-weight="800">★ 전하 없음(q=0, 중성) ➔ 전기장 영향 전혀 없음!</text>
        <text x="16" y="46" fill="#cbd5e1" font-size="7.2">• 오직 분자 농도 차이에 의한 **확산(Diffusion)**으로 이동</text>
        <text x="16" y="60" fill="#a7f3d0" font-size="7.2">  픽의 확산 법칙: J = -D ∇n (농도 높은 곳 ➔ 낮은 곳)</text>
        <text x="16" y="74" fill="#fde047" font-size="7.2" font-weight="800">➔ 표면 소모 속도가 빠르면 확산 지연으로 국소 농도 저하!</text>
        <text x="16" y="86" fill="#38bdf8" font-size="7" font-weight="800">➔ 질문의 '반응종'은 바로 이 중성 라디칼을 의미!</text>
      </g>
    </g>

    <!-- Definitive Q&A Box -->
    <g transform="translate(15, 255)">
      <rect width="280" height="150" rx="5" fill="#0b1329" stroke="#38bdf8"/>
      <text x="12" y="18" fill="#38bdf8" font-size="8.8" font-weight="800">💡 사용자 질문 직격 답변</text>
      <text x="12" y="38" fill="#fde047" font-size="8.2" font-weight="800">"여기서 반응종이 라디컬이야?"</text>
      <text x="12" y="58" fill="#a7f3d0" font-size="8" font-weight="800">➔ 네, 100% 맞습니다!</text>
      <text x="12" y="76" fill="#cbd5e1" font-size="7.5">• 반도체 식각에서 '확산하여 화학 반응을 일으키는</text>
      <text x="16" y="90" fill="#cbd5e1" font-size="7.5">  단위 면적당 반응종'은 <strong>중성 라디칼</strong>을 지칭합니다.</text>
      <text x="12" y="110" fill="#cbd5e1" font-size="7.5">• 이온은 전기장에 끌려오므로 '확산 농도 차이'라는</text>
      <text x="16" y="124" fill="#cbd5e1" font-size="7.5">  표현을 쓰지 않고, <strong>라디칼에만 확산 농도를 적용</strong>합니다.</text>
      <text x="12" y="142" fill="#fbbf24" font-size="7" font-weight="800">용어 일치: 본문의 반응종 = 중성 라디칼 (Neutral Radical)</text>
    </g>
  </g>

  <!-- PANEL C: Solution Mechanisms -->
  <g transform="translate(660, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (C) 로딩 개선 메커니즘 3대 핵심</text>

    <!-- Solutions List -->
    <g transform="translate(15, 40)">
      <rect width="270" height="235" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">공정 및 설계 제어 솔루션</text>

      <!-- Solution 1: Pressure Increase -->
      <g transform="translate(10, 26)">
        <rect width="250" height="60" rx="4" fill="#0b1329" stroke="#38bdf8"/>
        <text x="8" y="14" fill="#38bdf8" font-size="7.5" font-weight="800">1. 챔버 압력(Pressure) 증가 : 공급량 폭증</text>
        <text x="12" y="28" fill="#cbd5e1" font-size="6.8">• 기체 밀도(N) 증가 ➔ 전자-기체 충돌 빈도 급증</text>
        <text x="12" y="40" fill="#fde047" font-size="7" font-weight="800">➔ 라디칼 생성률(G) 대폭 증가로 절대 공급량 보충</text>
        <text x="12" y="52" fill="#cbd5e1" font-size="6.8">• 오픈 영역의 국소 고갈 웅덩이를 채워 농도 평탄화</text>
      </g>

      <!-- Solution 2: Bias Power Decrease -->
      <g transform="translate(10, 92)">
        <rect width="250" height="68" rx="4" fill="#0b1329" stroke="#f59e0b"/>
        <text x="8" y="14" fill="#fbbf24" font-size="7.5" font-weight="800">2. 바이어스 파워(Bias Power) 감소 : 소모 속도 제어</text>
        <text x="12" y="28" fill="#cbd5e1" font-size="6.8">• 과도한 바이어스 ➔ 이온 보조 폭증 (소모 > 공급)</text>
        <text x="12" y="42" fill="#fde047" font-size="7" font-weight="800">➔ 바이어스 감소 시 표면 반응 속도를 적절히 낮춤</text>
        <text x="12" y="55" fill="#cbd5e1" font-size="6.8">• 라디칼이 순간 고갈되지 않고 패턴 전체로 퍼져</text>
        <text x="12" y="66" fill="#a7f3d0" font-size="6.8">  확산 평형(Reaction-limited)을 이룰 여유 확보!</text>
      </g>

      <!-- Solution 3: Dummy Pattern -->
      <g transform="translate(10, 166)">
        <rect width="250" height="60" rx="4" fill="#0b1329" stroke="#10b981"/>
        <text x="8" y="14" fill="#34d399" font-size="7.5" font-weight="800">3. 더미 패턴(Dummy Pattern) 삽입 : 밀도 균등화</text>
        <text x="12" y="28" fill="#cbd5e1" font-size="6.8">• 오픈 영역에 비동작 더미 패턴을 촘촘히 배치</text>
        <text x="12" y="41" fill="#fde047" font-size="7" font-weight="800">➔ 웨이퍼 전면의 개구율(Pattern Density)을 균일화</text>
        <text x="12" y="54" fill="#cbd5e1" font-size="6.8">➔ 설계 레이아웃 차원에서 로딩 발생 자체를 원천 차단</text>
      </g>
    </g>

    <!-- Takeaway Summary -->
    <g transform="translate(15, 285)">
      <rect width="270" height="120" rx="6" fill="#0b1329" stroke="#10b981"/>
      <text x="12" y="16" fill="#34d399" font-size="8.8" font-weight="800">💡 엔지니어의 핵심 요약 공식</text>
      <text x="12" y="34" fill="#fde047" font-size="7.5" font-weight="800">반응종 = 중성 라디칼 (Radical)</text>
      <text x="12" y="52" fill="#cbd5e1" font-size="7">• 압력↑ : 라디칼을 더 많이 찍어내 공급 (Supply Up)</text>
      <text x="12" y="70" fill="#cbd5e1" font-size="7">• 바이어스↓ : 급하게 다 쓰지 말고 골고루 쓰게 조절</text>
      <text x="12" y="88" fill="#cbd5e1" font-size="7">• 더미 패턴 : 깎을 면적을 웨이퍼 전체에서 동일화</text>
      <text x="12" y="106" fill="#38bdf8" font-size="7.5" font-weight="800">➔ 매크로 로딩 완화로 완벽한 식각 균일도(Uniformity) 달성!</text>
    </g>
  </g>

  <!-- Markers -->
  <defs>
    <marker id="arrowYellow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#facc15" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- SECTION 1: Radical Identity Confirmation -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 여기서 반응종이 라디칼인가요? (명쾌한 확인 및 물리적 이유)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            <strong>네, 100% 맞습니다!</strong><br>
            질문자님께서 제시하신 문장의 <em>"박막 표면으로 확산된 단위 면적당 반응종"</em>에서 <strong>'반응종(Reactive Species)'의 실체는 바로 '중성 라디칼(Neutral Radicals, 예: $\text{F}^*, \text{Cl}^*$)'</strong>입니다.
          </p>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
            <div style="background:#0f172a; border-left:4px solid #ef4444; padding:16px 18px; border-radius:0 8px 8px 0;">
              <h4 style="color:#f87171; font-size:0.95rem; font-weight:800; margin-bottom:6px;">
                ① 양이온 ($\text{CF}_3^+, \text{Ar}^+$) : 전계 드리프트 (Drift)
              </h4>
              <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
                전하($+q$)를 띠고 있어 음극 쉬스(Sheath)의 강력한 수직 전기장에 의해 기판으로 직진 가속($v = \mu E$)합니다.
                전기장에 이끌려 쏟아지므로 기판 위 패턴 형상이나 개구율에 상관없이 웨이퍼 전면에 균일하게 내리꽂히며, <strong>'농도 구배에 따른 확산' 현상을 겪지 않습니다.</strong>
              </p>
            </div>
            <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 18px; border-radius:0 8px 8px 0;">
              <h4 style="color:#34d399; font-size:0.95rem; font-weight:800; margin-bottom:6px;">
                ② 중성 라디칼 ($\text{F}^*, \text{Cl}^*$) : 기체 확산 (Diffusion) ★
              </h4>
              <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
                홑전자를 가졌지만 <strong>전기적으로 중성($q=0$)</strong>입니다. 따라서 전기장의 영향을 전혀 받지 않으며, 오직 <strong>농도 구배에 따른 무작위 기체 확산($J = -D \nabla n$)</strong>으로만 기판 표면에 도달합니다.
                표면 소모율에 따라 농도 차이가 그대로 노출되므로, <strong>로딩 이펙트의 주범이자 핵심 반응종</strong>이 됩니다.
              </p>
            </div>
          </div>

          <div style="background:#1e293b; padding:14px 18px; border-radius:8px; margin-bottom:18px;">
            <p style="color:#fde047; font-size:0.9rem; line-height:1.7; margin:0;">
              💡 <strong>용어 정리</strong>: 반도체 건식 식각 텍스트나 학술 논문에서 <em>"반응종(Reactive Species)"</em> 또는 <em>"반응성 기체(Reactive Gas)"</em>가 표면으로 <em>"확산(Diffusion)"</em>한다고 기술되어 있다면, 이는 <strong>예외 없이 100% '중성 라디칼(Radical)'을 의미</strong>합니다.
            </p>
          </div>
        </div>

        <!-- SECTION 2: Macro Loading Mechanism -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fde047; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 매크로 로딩 이펙트(Macro Loading Effect)의 발생 원리와 패턴 크기의 관계
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            왜 패턴의 크기(또는 패턴 밀도/개구율)에 따라 식각 균일도(Etch Uniformity)가 저하될까요?
            그 핵심 메커니즘은 <strong>'국소적 라디칼 소모량과 공급 속도의 불균형(Reactant Depletion)'</strong>에 있습니다:
          </p>

          <div style="background:#0f172a; border-left:4px solid #ef4444; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#f87171; font-size:1rem; font-weight:800; margin-bottom:8px;">
              (1) 넓은 오픈 패턴 영역 (Large Open Area, 낮은 패턴 밀도)
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.85; padding-left:20px; margin:0;">
              <li><strong>넓은 반응 면적</strong>: 식각되어 날아가야 할 실리콘(Target)의 면적이 매우 광활합니다.</li>
              <li><strong>엄청난 라디칼 소모율</strong>: 단위 시간당 표면에서 소모되는 라디칼($\text{F}^*$)의 양($R_{consumption}$)이 막대합니다.</li>
              <li><strong>국소 고갈 (Local Depletion) 발생</strong>: 벌크 플라즈마에서 기판 표면으로 공급되는 확산 속도($R_{diffusion}$)보다 표면에서 삼켜버리는 소모 속도가 더 빠르면, <strong>표면 바로 위 기체 층의 라디칼 농도가 고갈(Starvation)</strong>됩니다.</li>
              <li><strong>결과</strong>: 반응할 라디칼이 부족하여 <strong>식각 속도(Etch Rate)가 뚝 떨어집니다!</strong></li>
            </ul>
          </div>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:800; margin-bottom:8px;">
              (2) 고립되거나 좁은 패턴 영역 (Dense / Small Pattern Area, 높은 마스크 밀도)
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.85; padding-left:20px; margin:0;">
              <li><strong>좁은 반응 면적</strong>: 대부분의 면적이 마스크(PR, 하드마스크)로 덮여 있어 노출된 실리콘 면적이 아주 작습니다.</li>
              <li><strong>적은 라디칼 소모율</strong>: 단위 시간당 표면에서 소모되는 라디칼 양이 매우 적습니다.</li>
              <li><strong>풍부한 라디칼 농도 유지</strong>: 공급되는 라디칼에 비해 소모가 적으므로 표면 부근의 라디칼 농도가 여전히 높게 유지됩니다.</li>
              <li><strong>결과</strong>: 라디칼이 충분하므로 <strong>식각 속도(Etch Rate)가 상대적으로 빠릅니다!</strong></li>
            </ul>
          </div>

          <div style="background:#1e293b; padding:14px 18px; border-radius:8px; margin-bottom:18px;">
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7; margin:0;">
              📌 <strong>종합 현상</strong>: 동일한 웨이퍼인데도 <strong>패턴이 넓은 곳은 천천히 파이고, 패턴이 좁고 고립된 곳은 쑥 깊게 파이는 심각한 식각 불균일도(Etch Non-uniformity)</strong>가 발생하며, 이를 바로 <strong>'매크로 로딩 이펙트(Macro Loading Effect)'</strong>라고 부릅니다.
            </p>
          </div>
        </div>

        <!-- SECTION 3: Why Increase Pressure & Decrease Bias Power -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#10b981; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 개선 방법의 물리적 원리: 왜 압력을 높이고 바이어스를 줄일까?
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            사용자분께서 제시하신 답변(압력 증가, 바이어스 파워 감소)이 왜 매크로 로딩을 해결하는지 물리적 인과관계를 완벽하게 정리해 드립니다:
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:800; margin-bottom:6px;">
              해법 ① 압력(Pressure)을 높이는 이유: 라디칼 절대 공급량의 대폭 증대 (Supply ↑)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              챔버 압력을 올리면 반응 가스($\text{CF}_4, \text{Cl}_2$ 등)의 분자 밀도($N$)가 증가합니다.
              이에 따라 플라즈마 내 고에너지 전자와 가스 분자 간의 충돌 빈도($\text{Electron-impact dissociation}$)가 비약적으로 상승하여, <strong>단위 부피당 생성되는 중성 라디칼($\text{F}^*$)의 절대량이 폭발적으로 증가</strong>합니다.
              <br>➔ 오픈 영역에서 라디칼을 아무리 게걸스럽게 소모하더라도, 위에서 쏟아부어 주는 공급량이 압도적으로 많아지면 <strong>국소 고갈(Depletion) 웅덩이가 채워져 패턴 크기별 라디칼 농도 편차가 급감</strong>하게 됩니다.
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #fbbf24; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#fbbf24; font-size:1rem; font-weight:800; margin-bottom:6px;">
              해법 ② 바이어스 파워(Bias Power)를 낮추는 이유: 소모 속도 제어 및 확산 평형 확보 (Reaction-limited 전이)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              바이어스 파워가 너무 높으면 시스 전압($V_{dc}$)이 커져 이온 충돌 에너지가 폭증합니다. 이온이 표면 결합을 너무 빠르게 부수어 놓으면 흡착된 라디칼이 표면에 닿자마자 빛의 속도로 반응하여 날아가 버립니다.
              이때는 공급이 소모를 따라가지 못하는 <strong>'물질 전달 율속(Diffusion / Mass-transfer Limited)' 상태</strong>가 되어 로딩 이펙트가 극대화됩니다.
              <br>➔ 반대로 <strong>바이어스 파워를 줄이면</strong>, 이온 보조 반응 속도가 적절히 진정되어 라디칼이 국소적으로 순간 고갈되지 않고 패턴 표면 전체로 골고루 퍼져 확산 평형을 이룰 수 있는 시간적 여유를 갖게 됩니다 (<strong>'표면 반응 율속(Reaction-limited)' 영역으로 이동</strong>). 그 결과 패턴 크기 간 식각 속도 편차가 크게 줄어듭니다!
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:800; margin-bottom:6px;">
              해법 ③ 현업 실무 엔지니어의 핵심 비기: 더미 패턴(Dummy Pattern) 삽입 & 샤워헤드 제어
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:20px; margin:0;">
              <li><strong>더미 패턴(Dummy Pattern)</strong>: 공정 파라미터 튜닝만으로는 한계가 있을 때, 칩 설계(Layout CAD) 단계에서 넓은 오픈 영역에 전기적으로 동작하지 않는 더미 패턴을 채워 넣음으로써 <strong>웨이퍼 전면의 식각 면적 비율(Pattern Density / Open Area Ratio)을 균일하게 평탄화</strong>합니다. (매크로 로딩의 근본 원인 제거!)</li>
              <li><strong>가스 유량(Flow Rate) 증가</strong>: 총 가스 유량을 높여 챔버 내 체류 시간(Residence Time)을 단축시키고 신선한 라디칼을 지속 공급합니다.</li>
              <li><strong>멀티존 샤워헤드(Multi-zone Showerhead)</strong>: 웨이퍼 센터와 에지, 또는 특정 패턴 영역별로 가스 주입량을 차등 분사하여 공간적 균일도를 맞춥니다.</li>
            </ul>
          </div>
        </div>

        <!-- SECTION 4: Comparative Breakdown of Loading Effects -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. 로딩 이펙트의 3가지 유형 한눈에 비교 (글로벌 vs 매크로 vs 마이크로/ARDE)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체 공정에서 '로딩 이펙트'는 스케일에 따라 세 가지로 명확히 구분되며, 이를 정확히 구별하면 완벽한 공정 통찰력을 갖추게 됩니다:
          </p>

          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; color:#cbd5e1; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#f8fafc; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:1px solid #334155;">구분</th>
                  <th style="padding:10px 14px; border-bottom:1px solid #334155;">공간 스케일</th>
                  <th style="padding:10px 14px; border-bottom:1px solid #334155;">주요 원인 메커니즘</th>
                  <th style="padding:10px 14px; border-bottom:1px solid #334155;">해결 솔루션</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:800; color:#38bdf8;">글로벌 로딩 (Global Loading)</td>
                  <td style="padding:10px 14px;">웨이퍼 ~ 배치 전체 ($> 300\,\text{mm}$)</td>
                  <td style="padding:10px 14px;">웨이퍼 1장당 전체 식각 면적 차이, 장비 내 웨이퍼 투입 매수 차이로 인한 챔버 전체 라디칼 소모</td>
                  <td style="padding:10px 14px;">총 가스 유량 증대, 챔버 압력 및 소스 파워 보정</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b; background:rgba(56, 189, 248, 0.05);">
                  <td style="padding:10px 14px; font-weight:800; color:#facc15;">매크로 로딩 (Macro Loading) ★<br><small style="color:#94a3b8;">(본 질문의 주제!)</small></td>
                  <td style="padding:10px 14px;">다이(Die) 내 패턴 ($> \mu\text{m} \sim \text{mm}$)</td>
                  <td style="padding:10px 14px;"><strong>오픈 패턴 vs 밀집 패턴 간 식각 면적 차이</strong>로 인한 표면 부근 라디칼 국소 고갈 (Depletion)</td>
                  <td style="padding:10px 14px;"><strong>압력 증가(공급↑), 바이어스 감소(소모 조절), 더미 패턴 삽입</strong></td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:800; color:#34d399;">마이크로 로딩 (Micro Loading)<br><small style="color:#94a3b8;">/ ARDE 현상</small></td>
                  <td style="padding:10px 14px;">개별 패턴 내부 ($< 100\,\text{nm}$)</td>
                  <td style="padding:10px 14px;">트렌치/비아홀의 종횡비(Aspect Ratio)가 깊어질수록 구멍 바닥으로 라디칼/이온이 도달하기 어려움 (Knudsen 확산 저하)</td>
                  <td style="padding:10px 14px;">고에너지 수직 이온 직진성 강화, 가스 펄싱(ALE 공정), 압력 강하(이온 산란 감소)</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 102 topics (q-102 down to q-01) by +1
    for old_n in range(102, 0, -1):
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

    # Step 4: Update header description to 103 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 '매크로 로딩 이펙트: 반응종(라디칼)과 식각 불균일 개선(Q01)'이 위치하며, 총 103개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Macro Loading and Radical topic!")
