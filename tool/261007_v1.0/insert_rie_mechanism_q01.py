# -*- coding: utf-8 -*-
"""
insert_rie_mechanism_q01.py
사용자 질문:
"[꼬리 1-1]. RIE의 메커니즘에 대해서 설명해주세요.
...
이거 rie라는건 이온충돌로약화시킨다음에 radical이 흡착되어반응하는거야? radical이랑 etchant랑 다른건가 
순서가 etchant가 타겟으로이동해흡착 -> 이온충돌로 결합약화시킴 -> etchant와 radical과 반응? radical의역할이뭐야"

기존 101개 질문을 Q02~Q102로 시프트하고, 최상단 Q01에 신규 등록 (총 102개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (건식 식각 & RIE 메커니즘 · etchant와 radical의 관계, 이온-라디칼 시너지 순서 해부)",
    "title": "RIE 식각 메커니즘의 실체: etchant와 radical의 차이, 이온 충돌과 화학 반응의 순서 및 라디칼의 역할 완전 해부",
    "nav_title": "RIE 메커니즘: etchant와 radical의 관계 및 순서",
    "summary": [
        "<strong>1. etchant와 radical은 다른 물질일까?</strong>: 아닙니다! etchant(식각제)는 식각 반응을 일으키는 물질 전체를 포괄하는 '기능적 총칭'이며, RIE에서 화학적 식각을 주도하는 <strong>실질적인 etchant의 핵심 정체가 바로 '라디칼(Radical, 예: $\\text{F}^*, \\text{Cl}^*$)'</strong>입니다. 즉 본문의 'etchant = 라디칼'로 이해하시면 100% 일치합니다.",
        "<strong>2. 이온 충돌과 라디칼 반응의 순서 (동시 시너지 메커니즘)</strong>: 엄밀히는 나노초 단위로 동시에 일어나는 '이온 보조 화학 식각(Ion-enhanced Chemical Etching)'입니다. 텍스트의 6단계 서술은 <strong>'① 라디칼(etchant)의 표면 흡착 ➔ ② 수직 이온 충돌로 격자 결합 약화 및 탈착 에너지 공급 ➔ ③ 흡착된 라디칼과의 결합으로 휘발성 부산물($\\text{SiF}_4$) 생성 및 탈착'</strong>의 표준 모델을 설명한 것입니다.",
        "<strong>3. 라디칼(Radical)의 결정적 역할: 화학적 식각과 높은 선택비(Selectivity)</strong>: 홑전자를 가져 반응성이 극도로 높으며, 실리콘 원자와 결합하여 상온 진공에서 기화되어 날아갈 수 있는 <strong>'휘발성 반응 부산물(Volatile Byproduct, $\\text{SiF}_4, \\text{SiCl}_4$)'을 만들어내는 화학적 주인공</strong>입니다.",
        "<strong>4. 이온(Ion)과의 환상적인 분업 (Coburn & Winters 시너지)</strong>: 라디칼 혼자서는 식각 속도가 느리고 사방으로 깎아 먹는 등방성(Isotropic)이 되지만, 시스 전계로 수직 가속된 양이온이 <strong>바닥면만 선택적으로 때려 결합을 부수고 반응 속도를 10배 폭증시킴으로써 완벽한 수직 비등방성(Anisotropic) 패턴</strong>을 완성합니다."
    ],
    "svg_title": "📊 [RIE 메커니즘 및 이온-라디칼 시너지 종합 분석 다이어그램] (A) Etchant의 정체와 라디칼(Radical) 생성 | (B) RIE 6단계 표면 반응 사이클 | (C) Coburn-Winters 시너지 효과 (식각률 10배 폭발)",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Etchant vs Radical Relationship -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) Etchant(식각제)와 Radical의 관계</text>

    <!-- Definition box -->
    <g transform="translate(15, 38)">
      <rect width="270" height="205" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 개념의 포함 관계 (식각제 ⊃ 라디칼)</text>

      <!-- Visual Hierarchy -->
      <g transform="translate(15, 28)">
        <rect width="240" height="52" rx="4" fill="#0b1329" stroke="#38bdf8"/>
        <text x="10" y="18" fill="#38bdf8" font-size="8" font-weight="800">식각제 (Etchant) : 포괄적 상위 개념</text>
        <text x="16" y="32" fill="#cbd5e1" font-size="7">• 타깃을 깎아내는 모든 화학종을 통칭</text>
        <text x="16" y="44" fill="#cbd5e1" font-size="7">• 기체 분자, 반응성 물질 전체의 기능적 명칭</text>
      </g>

      <!-- Downward arrow -->
      <path d="M 135 83 L 135 95" stroke="#fde047" stroke-width="2" marker-end="url(#arrowYellowR)"/>

      <g transform="translate(15, 98)">
        <rect width="240" height="92" rx="4" fill="#0b1329" stroke="#10b981"/>
        <text x="10" y="18" fill="#34d399" font-size="8.2" font-weight="800">★ 라디칼 (Radical, 예: F*, Cl*) : 실질적 주인공!</text>
        <text x="16" y="34" fill="#cbd5e1" font-size="7.2">• 플라즈마에서 CF₄ 분자가 쪼개져 생성된</text>
        <text x="16" y="48" fill="#fde047" font-size="7.5" font-weight="800">   홑전자(Unpaired e⁻)를 가진 극초반응성 중성종</text>
        <text x="16" y="62" fill="#cbd5e1" font-size="7.2">• RIE에서 실제로 실리콘과 반응하는</text>
        <text x="16" y="76" fill="#a7f3d0" font-size="7.5" font-weight="800">   '진짜 화학적 식각제(Etchant)'가 바로 라디칼!</text>
      </g>
    </g>

    <!-- Takeaway -->
    <g transform="translate(15, 252)">
      <rect width="270" height="153" rx="5" fill="#0b1329" stroke="#38bdf8"/>
      <text x="12" y="18" fill="#38bdf8" font-size="8.8" font-weight="800">💡 둘이 다른 건가요? ➔ 아닙니다!</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="7.5">• <strong>Etchant는 '역할'을 부르는 말</strong> (의사)</text>
      <text x="12" y="50" fill="#cbd5e1" font-size="7.5">• <strong>Radical은 '물질의 실체'를 부르는 말</strong> (홍길동)</text>
      <text x="12" y="68" fill="#fde047" font-size="7.8" font-weight="800">➔ "식각제(Etchant)라는 역할을 수행하는 핵심</text>
      <text x="18" y="82" fill="#fde047" font-size="7.8" font-weight="800">    물질의 실체가 바로 라디칼(Radical)입니다!"</text>
      <text x="12" y="102" fill="#cbd5e1" font-size="7.2">• 본문의 "etchant 물질이 표면에 흡착" =</text>
      <text x="18" y="115" fill="#34d399" font-size="7.5" font-weight="800">   "라디칼(F*)이 표면에 흡착"과 100% 동일한 의미!</text>
      <text x="12" y="134" fill="#94a3b8" font-size="6.8">• CF₄ 플라즈마 ➔ F* 라디칼(화학 식각) + CF₃⁺ 이온(물리 가속)</text>
    </g>
  </g>

  <!-- PANEL B: 6-Step Surface Mechanism -->
  <g transform="translate(335, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) RIE 6단계 표면 메커니즘과 순서</text>

    <!-- Mechanism steps -->
    <g transform="translate(15, 38)">
      <rect width="280" height="215" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">표면 반응의 실제 순서와 상호작용</text>

      <!-- Step 1 & 2 -->
      <g transform="translate(10, 26)">
        <rect width="260" height="42" rx="3" fill="#0b1329" stroke="#38bdf8"/>
        <text x="8" y="14" fill="#38bdf8" font-size="7.5" font-weight="800">1~2단계: 라디칼(Etchant, F*)의 표면 확산 및 흡착</text>
        <text x="14" y="26" fill="#cbd5e1" font-size="6.8">• 플라즈마 벌크에서 생성된 F* 라디칼이 기판 표면으로 확산</text>
        <text x="14" y="37" fill="#cbd5e1" font-size="6.8">• 실리콘 표면의 댕글링 본드에 화학 흡착 (Si-F 형성)</text>
      </g>

      <!-- Step 3 & 4 (Core!) -->
      <g transform="translate(10, 72)">
        <rect width="260" height="52" rx="3" fill="#0b1329" stroke="#ef4444"/>
        <text x="8" y="14" fill="#f87171" font-size="7.5" font-weight="800">3~4단계: 수직 이온 충돌(Ion Bombardment) 결합 약화</text>
        <text x="14" y="27" fill="#fde047" font-size="7" font-weight="800">★ 핵심: 수직 입사된 양이온(CF₃⁺)이 Si-Si 결합을 쾅 강타!</text>
        <text x="14" y="39" fill="#cbd5e1" font-size="6.8">• 결합이 약해진 틈새로 흡착된 F* 라디칼이 침투하여 급속 반응</text>
        <text x="14" y="49" fill="#a7f3d0" font-size="6.8">• 휘발성 화합물(SiF₄, 끓는점 −86℃ 기체)을 순간 생성!</text>
      </g>

      <!-- Step 5 & 6 -->
      <g transform="translate(10, 128)">
        <rect width="260" height="42" rx="3" fill="#0b1329" stroke="#10b981"/>
        <text x="8" y="14" fill="#34d399" font-size="7.5" font-weight="800">5~6단계: 휘발성 화합물 탈착(Desorption) 및 진공 배출</text>
        <text x="14" y="26" fill="#cbd5e1" font-size="6.8">• 기체 상태가 된 SiF₄가 표면에서 떨어져 나와 진공 펌프로 배출</text>
        <text x="14" y="37" fill="#34d399" font-size="7" font-weight="800">➔ 실리콘 원자가 기체로 증발하여 사라짐 = '식각 완료!'</text>
      </g>

      <text x="12" y="185" fill="#fde047" font-size="7.5" font-weight="800">★ 순서 요약: 라디칼 흡착 ➔ 이온 충돌 결합약화 ➔</text>
      <text x="12" y="198" fill="#fde047" font-size="7.5" font-weight="800">   흡착 라디칼과 반응하여 SiF₄ 생성 ➔ 탈착 배출!</text>
      <text x="12" y="210" fill="#94a3b8" font-size="6.8">(실제로는 이온 충돌과 라디칼 반응이 수 피코초 단위로 동시 발생)</text>
    </g>

    <!-- Role of Radical Box -->
    <g transform="translate(15, 260)">
      <rect width="280" height="145" rx="5" fill="#0b1329" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="8.8" font-weight="800">🎯 라디칼(Radical)의 결정적 역할</text>
      <text x="12" y="36" fill="#fde047" font-size="7.8" font-weight="800">1. "휘발성 화합물(기체)을 만드는 화학적 요리사"</text>
      <text x="18" y="50" fill="#cbd5e1" font-size="7.2">• 고체 Si를 기체 SiF₄로 바꾸려면 불소(F*)가 달라붙어야 함</text>
      <text x="18" y="62" fill="#cbd5e1" font-size="7.2">• 이온 혼자 때리면(스퍼터링) 원자가 튀어 옆벽에 도로 붙음</text>
      <text x="12" y="80" fill="#38bdf8" font-size="7.8" font-weight="800">2. "높은 선택비(Selectivity) 보장"</text>
      <text x="18" y="94" fill="#cbd5e1" font-size="7.2">• 화학적 성질에 따라 원하는 막(Si)만 골라서 반응</text>
      <text x="18" y="106" fill="#cbd5e1" font-size="7.2">• 하부 절연막(SiO₂)이나 마스크(PR)는 손상 최소화</text>
      <text x="12" y="124" fill="#a7f3d0" font-size="7.5" font-weight="800">➔ 화학적 반응(Radical) + 물리적 직진성(Ion)의 결합 = RIE!</text>
    </g>
  </g>

  <!-- PANEL C: Coburn-Winters Synergy -->
  <g transform="translate(660, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="12" font-weight="800">■ (C) Coburn &amp; Winters 시너지 (식각률 10배)</text>

    <!-- Synergy Graph -->
    <g transform="translate(15, 38)">
      <rect width="270" height="235" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">전설적인 1979년 실증 실험 (XeF₂ + Ar⁺ on Si)</text>

      <!-- Graph Axes -->
      <g transform="translate(25, 30)">
        <line x1="15" y1="130" x2="225" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
        <line x1="15" y1="130" x2="15" y2="15" stroke="#94a3b8" stroke-width="1.5"/>
        <text x="200" y="142" fill="#94a3b8" font-size="7">시간 (Time)</text>
        <text x="8" y="12" fill="#94a3b8" font-size="7">식각률</text>

        <!-- Region 1: Only XeF2 gas (radical proxy) -->
        <path d="M 15 115 L 75 115" stroke="#38bdf8" stroke-width="2"/>
        <text x="25" y="105" fill="#38bdf8" font-size="6.5">① 라디칼만 투입</text>
        <text x="25" y="125" fill="#94a3b8" font-size="6">(느림: ~5 Å/min)</text>

        <!-- Region 2: Both Ar+ ion and XeF2 gas together! -->
        <path d="M 75 115 L 75 35 L 155 35" stroke="#ef4444" stroke-width="2.5"/>
        <text x="82" y="28" fill="#f87171" font-size="7.5" font-weight="900">② 이온 + 라디칼 동시 인가!</text>
        <text x="82" y="48" fill="#fde047" font-size="7.5" font-weight="800">★ 식각 속도 10배 폭증!!</text>
        <text x="82" y="60" fill="#a7f3d0" font-size="6.5">(~55 Å/min, 시너지 폭발)</text>

        <!-- Region 3: Turn off XeF2, only Ar+ ions -->
        <path d="M 155 35 L 155 120 L 215 120" stroke="#f59e0b" stroke-width="2"/>
        <text x="160" y="108" fill="#fbbf24" font-size="6.5">③ 이온만 투입</text>
        <text x="160" y="128" fill="#94a3b8" font-size="6">(물리 스퍼터링 ~2 Å/min)</text>
      </g>

      <text x="12" y="185" fill="#cbd5e1" font-size="7.2">• 1 + 1 = 2 가 아니라, **1 + 1 = 10** 이 되는 마법!</text>
      <text x="12" y="198" fill="#cbd5e1" font-size="7.2">• 이온의 충격이 라디칼의 화학 반응을 기하급수적으로 촉진</text>
      <text x="12" y="212" fill="#fde047" font-size="7.5" font-weight="800">➔ 이것이 바로 RIE가 고속 + 수직 식각을 달성하는 원리!</text>
      <text x="12" y="226" fill="#94a3b8" font-size="6.8">• 측벽은 이온이 안 때리므로 안 깎임 (수직 비등방성 달성)</text>
    </g>

    <!-- Final Takeaway -->
    <g transform="translate(15, 280)">
      <rect width="270" height="125" rx="6" fill="#0b1329" stroke="#f59e0b"/>
      <text x="12" y="16" fill="#fbbf24" font-size="8.8" font-weight="800">💡 1초 요약 교통정리</text>
      <text x="12" y="34" fill="#38bdf8" font-size="7.5" font-weight="800">1. etchant와 radical은 같은 것인가?</text>
      <text x="16" y="47" fill="#cbd5e1" font-size="7">➔ 네! etchant(식각제)의 진짜 알맹이가 radical입니다.</text>
      <text x="12" y="65" fill="#34d399" font-size="7.5" font-weight="800">2. 순서가 어떻게 되나요?</text>
      <text x="16" y="78" fill="#cbd5e1" font-size="7">➔ 라디칼 흡착 ➔ 수직 이온 충돌 결합 약화 ➔</text>
      <text x="16" y="90" fill="#cbd5e1" font-size="7">    흡착 라디칼과 반응(SiF₄) ➔ 탈착 배출!</text>
      <text x="12" y="108" fill="#fde047" font-size="7.5" font-weight="800">3. 라디칼의 역할: "기화 부산물을 만드는 화학 요리사!"</text>
    </g>
  </g>

  <!-- Markers -->
  <defs>
    <marker id="arrowYellowR" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#facc15" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- SECTION 1: Etchant vs Radical Distinction -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. etchant와 radical은 다른 건가요? (개념의 포함 관계)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            결론부터 말씀드리면, <strong>둘은 별개의 다른 물질이 아닙니다!</strong>
            두 단어의 관계는 <strong>'직업(역할)'</strong>과 <strong>'사람(실체)'</strong>의 관계와 같습니다:
          </p>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
            <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 18px; border-radius:0 8px 8px 0;">
              <h4 style="color:#38bdf8; font-size:0.95rem; font-weight:800; margin-bottom:6px;">
                ① 에천트 (Etchant, 식각제) = '역할'
              </h4>
              <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
                표면을 화학적으로 깎아내는 모든 반응성 물질을 통칭하는 <strong>포괄적인 기능적 명칭</strong>입니다.
                (비유하자면 사람의 직업인 **'의사'**에 해당합니다.)
              </p>
            </div>
            <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 18px; border-radius:0 8px 8px 0;">
              <h4 style="color:#34d399; font-size:0.95rem; font-weight:800; margin-bottom:6px;">
                ② 라디칼 (Radical) = '물질의 실체'
              </h4>
              <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
                플라즈마에 의해 분자가 쪼개져 홑전자를 가진 **극초반응성 중성 입자의 실체($\text{F}^*, \text{Cl}^*$)**입니다.
                (비유하자면 수술을 집도하는 의사의 본명인 **'홍길동'**에 해당합니다.)
              </p>
            </div>
          </div>

          <div style="background:#1e293b; padding:14px 18px; border-radius:8px; margin-bottom:18px;">
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7; margin:0;">
              💡 <strong>질문자님 텍스트의 독해법</strong>:
              질문 본문에서 <em>"plasma 내의 etchant 물질이 확산되어 target 표면으로 이동한다"</em>고 할 때, 그 <strong>'etchant 물질'의 정체가 바로 '라디칼(Radical)'</strong>입니다!
              따라서 본문에서 etchant와 radical을 따로 쓴 것은 "식각제(etchant) 역할을 하는 라디칼(radical) 물질"을 문맥상 표현한 것입니다.
            </p>
          </div>
        </div>

        <!-- SECTION 2: Exact Sequence & Mechanism -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fde047; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 이온 충돌과 라디칼 반응의 순서는 어떻게 되는 걸까?
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            질문자님께서 물으신 <em>"순서가 etchant가 타겟으로 이동해 흡착 ➔ 이온 충돌로 결합 약화시킴 ➔ etchant와 radical과 반응?"</em>에 대해 표면 화학의 실제 과정을 순서대로 명쾌하게 맞춰 드립니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:800; margin-bottom:8px;">
              RIE의 표준 6단계 표면 반응 시퀀스 (정확한 교통정리)
            </h4>
            <ol style="color:#cbd5e1; font-size:0.9rem; line-height:1.85; padding-left:20px; margin:0;">
              <li><strong>1단계 (생성)</strong>: 플라즈마 방전으로 주입된 기체($\text{CF}_4$)가 쪼개져 <strong>라디칼($\text{F}^*$, 식각제)</strong>과 <strong>양이온($\text{CF}_3^+, \text{Ar}^+$)</strong>이 생성됩니다.</li>
              <li><strong>2단계 (확산 및 흡착)</strong>: 라디칼($\text{F}^*$)이 기체 층을 통해 확산하여 실리콘(Si) 타깃 표면으로 이동한 뒤 표면에 달라붙습니다(화학 흡착, Adsorption). ➔ <em>표면에 $\text{Si-F}$ 결합층 형성</em></li>
              <li><strong>3단계 (수직 이온 충돌)</strong>: 음극 시스 전계로 수직 가속된 양이온($\text{CF}_3^+$)이 표면을 쾅 강타합니다(Ion Bombardment). ➔ <em>단단한 $\text{Si-Si}$ 격자 결합이 끊어지고 약화됨</em></li>
              <li><strong>4단계 (화학 반응)</strong>: 결합이 약해진 틈새로 흡착되어 있던 라디칼($\text{F}^*$)이 실리콘 원자와 맹렬하게 결합하여 **상온에서 기체가 되는 휘발성 화합물($\text{SiF}_4$, 끓는점 $-86^\circ\text{C}$)**을 만듭니다.</li>
              <li><strong>5단계 (탈착 Desorption)</strong>: 생성된 $\text{SiF}_4$는 기체 분자이므로 고체 표면에 머물지 못하고 표면에서 저절로 떨어져 나옵니다(탈착). ➔ <strong>실리콘 원자가 기체로 증발하여 사라짐(식각 완료)!</strong></li>
              <li><strong>6단계 (배출 Exhaust)</strong>: 기체 층으로 나온 $\text{SiF}_4$ 부산물이 진공 펌프를 통해 챔버 밖으로 빠져나갑니다.</li>
            </ol>
          </div>

          <div style="background:#1e293b; padding:14px 18px; border-radius:8px; margin-bottom:18px;">
            <p style="color:#fde047; font-size:0.9rem; line-height:1.7; margin:0;">
              ★ <strong>동시성의 실체</strong>:
              이해를 돕기 위해 1~6단계로 순서를 나누었지만, 실제 나노초 단위에서는 **라디칼의 흡착과 이온의 충돌이 표면에서 거의 동시에 쉬지 않고 맞물려 일어납니다.**
              이온이 결합을 깨뜨리는 순간 흡착된 라디칼이 낚아채듯 기체($\text{SiF}_4$)로 만들어 날려버리는 것입니다!
            </p>
          </div>
        </div>

        <!-- SECTION 3: The True Role of Radical -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#10b981; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 라디칼(Radical)의 진짜 역할은 무엇일까?
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            질문자님께서 물으신 <strong>"radical의 역할이 뭐야?"</strong>에 대한 핵심 답변은 다음과 같습니다:
          </p>

          <div style="background:#0f172a; border-left:4px solid #facc15; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#facc15; font-size:1rem; font-weight:800; margin-bottom:6px;">
              역할 ① 고체 원자를 기체로 바꾸어 날려버리는 '화학적 요리사'
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              고체 상태인 실리콘(Si)은 녹는점이 $1,414^\circ\text{C}$에 달해 상온에서 절대 기체로 날아가지 않습니다.
              만약 이온만 때린다면(물리적 스퍼터링), 실리콘 원자가 튕겨 나갔다가 바로 옆 벽면에 다시 들러붙어 버립니다(재증착 문제).
              <br>하지만 **라디칼($\text{F}^*$)이 달라붙으면 실리콘을 상온에서도 펄펄 끓는 기체인 $\text{SiF}_4$(끓는점 $-86^\circ\text{C}$)로 변환시켜 챔버 밖으로 영구 배출**시킵니다.
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:800; margin-bottom:6px;">
              역할 ② 식각 선택비(Selectivity)를 보장하는 '화학적 눈'
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              이온 충돌은 물리적 망치질이라 실리콘이든 마스크(PR)든 산화막이든 무차별로 깨뜨립니다.
              반면 **라디칼은 화학적 선택성을 가지고 있어, 원하는 막질(Si)과만 특이적으로 반응하고 마스크나 하부 절연막은 건드리지 않아 칩의 수율을 사수**합니다.
            </p>
          </div>
        </div>

        <!-- SECTION 4: Coburn-Winters Synergy -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. 이온과 라디칼의 환상적인 시너지: 왜 둘 다 있어야 할까? (Coburn & Winters)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            1979년 IBM의 코번(Coburn)과 윈터스(Winters)는 RIE의 원리를 밝혀낸 전설적인 실험을 진행했습니다:
          </p>

          <div style="background:#1e293b; padding:16px 20px; border-radius:8px;">
            <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.85; padding-left:20px; margin:0;">
              <li><strong>라디칼만 넣었을 때 ($\text{XeF}_2$)</strong>: 실리콘 표면과 반응하지만 속도가 $5\,\text{Å/min}$로 너무 느리고, 사방으로 깎아 먹어 옆구리가 파이는 <strong>등방성(Isotropic) 불량</strong>이 발생합니다.</li>
              <li><strong>이온만 넣었을 때 ($\text{Ar}^+$)</strong>: 물리적 망치질만으로는 단단한 결합이 잘 안 깎여 속도가 $2\,\text{Å/min}$에 불과합니다.</li>
              <li><strong>라디칼과 이온을 '동시에' 넣었을 때 (RIE)</strong>:
                <br>식각 속도가 $5 + 2 = 7$이 되는 것이 아니라, <strong>$55\,\text{Å/min}$로 10배 폭발</strong>했습니다!
                <br>수직으로 내려꽂히는 이온이 바닥면의 결합만 때려 부수어 라디칼과의 반응 속도를 10배 끌어올리기 때문에, <strong>옆면은 안 깎이고 바닥만 수직으로 칼같이 파고 내려가는 '완벽한 수직 비등방성(Anisotropic) RIE'</strong>가 완성되는 것입니다!
              </li>
            </ul>
          </div>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 101 topics (q-101 down to q-01) by +1
    for old_n in range(101, 0, -1):
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

    # Step 4: Update header description to 102 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 'RIE 메커니즘: etchant와 radical의 관계 및 순서(Q01)'가 위치하며, 총 102개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 RIE Mechanism topic!")
