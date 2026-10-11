# -*- coding: utf-8 -*-
"""
insert_precursor_vs_reactive_species_q01.py
사용자 질문:
"반응종이랑 전구체랑 똑같은말이야?"

기존 95개 질문을 Q02~Q96으로 시프트하고, 최상단 Q01에 신규 등록 (총 96개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (반도체 공정 화학 · 전구체(Precursor) vs 반응종(Reactive Species) vs 반응가스(Reactant) 완전 해부)",
    "title": "반응종(Reactive Species)과 전구체(Precursor)는 똑같은 말일까? (개념 정의, 원료 vs 활성 입자, ALD/CVD/식각 메커니즘 비교)",
    "nav_title": "반응종과 전구체는 똑같은 말일까?",
    "summary": [
        "<strong>1. 결론: 똑같은 말이 아니며, 전혀 다른 범주의 개념입니다!</strong>: 전구체(Precursor)는 최종 박막을 이룰 핵심 원소(Si, Ti, Al 등)를 품고 투입되는 <strong>안정된 상태의 '출발 원료 화합물'</strong>인 반면, 반응종(Reactive Species)은 열·플라즈마 등의 에너지를 받아 화학 반응을 직접 일으키는 <strong>극도로 불안정하고 에너지가 높은 '활성 입자(라디칼, 이온, 여기 상태 분자 등)'</strong>를 통칭합니다.",
        "<strong>2. 전구체(Precursor, 前驅體)의 본질</strong>: 박막의 뼈대가 될 중심 금속/반도체 원자에 유기 리간드가 결합된 비교적 안정된 분자(예: $\\text{SiH}_4$, $\text{TiCl}_4$, $\\text{TMA}$)로, 상온/공정 온도에서 일정한 증기압을 가져 기체 상태로 챔버에 이송되어 웨이퍼 표면에 화학 흡착(Adsorption)합니다.",
        "<strong>3. 반응종(Reactive Species, 反應種)의 본질</strong>: 화학 결합이 쪼개져 홑전자(Unpaired Electron)를 가진 라디칼($\\text{O}^*$, $\\text{H}^*$, $\\text{F}^*$)이나 이온($\\text{Ar}^+$, $\\text{CF}_3^+$)처럼, 수명이 수 $\\mu\\text{s}\\sim\\text{ms}$로 극히 짧고 반응성이 폭발적이어서 닿는 순간 리간드를 떼어내거나 식각/산화 반응을 일으킵니다.",
        "<strong>4. 반응가스(Reactant)와의 혼동 주의 (ALD 공정 3자 관계)</strong>: ALD 공정에서 1단계로 공급하는 것은 <strong>전구체(Precursor)</strong>, 2단계로 공급하는 짝꿍은 <strong>반응가스/반응체(Reactant, 예: $\\text{H}_2\\text{O}, \\text{O}_3, \\text{NH}_3$)</strong>이며, 이 반응가스가 플라즈마나 열로 쪼개져 만들어진 활성 알맹이가 바로 <strong>반응종(Reactive Species)</strong>입니다."
    ],
    "svg_title": "📊 [전구체 vs 반응종 vs 반응가스 핵심 개념 비교 다이어그램] (A) 전구체(출발 원료 분자) | (B) 반응종(고에너지 활성 입자) | (C) 반도체 ALD/CVD 박막 반응 메커니즘",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Precursor (전구체) -->
  <g transform="translate(20, 20)">
    <rect width="295" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 전구체 (Precursor, 前驅體)</text>

    <!-- Definition Card -->
    <g transform="translate(15, 42)">
      <rect width="265" height="120" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 개념: 박막의 뼈대를 담은 출발 원료 분자</text>
      <text x="10" y="34" fill="#cbd5e1" font-size="7.5">• <strong>어원</strong>: Pre(앞선) + Cursor(달리는 자) = 원료 물질</text>
      <text x="10" y="48" fill="#cbd5e1" font-size="7.5">• 박막의 최종 원소(Si, Ti, Al, Hf 등)를 보유</text>
      <text x="10" y="62" fill="#cbd5e1" font-size="7.5">• <strong>상태</strong>: 상온/챔버 조건에서 비교적 <strong>화학적 안정</strong></text>
      <text x="10" y="78" fill="#38bdf8" font-size="7.8" font-weight="800">➔ 기화기(Canister)에서 기체화되어 챔버로 투입</text>
      <text x="10" y="94" fill="#cbd5e1" font-size="7.2">• 중심 원소 + 휘발성을 주는 유기/무기 리간드(Ligand)</text>
      <text x="10" y="108" fill="#94a3b8" font-size="7">• 예: SiH₄, TEOS, TiCl₄, TMA (Al(CH₃)₃), TDMAH</text>
    </g>

    <!-- Structural Diagram -->
    <g transform="translate(15, 172)">
      <rect width="265" height="125" rx="5" fill="#0b1329" stroke="#38bdf8"/>
      <text x="10" y="18" fill="#38bdf8" font-size="8.5" font-weight="800">전구체의 전형적 구조 (예: TMA)</text>

      <!-- TMA molecule illustration -->
      <g transform="translate(130, 68)">
        <!-- Center Al -->
        <circle cx="0" cy="0" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="-7" y="4" fill="#fff" font-size="9" font-weight="900">Al</text>
        <!-- Ligands CH3 -->
        <line x1="0" y1="-16" x2="0" y2="-36" stroke="#94a3b8" stroke-width="2"/>
        <circle cx="0" cy="-38" r="12" fill="#334155" stroke="#64748b"/>
        <text x="-9" y="-35" fill="#cbd5e1" font-size="7">CH₃</text>

        <line x1="-14" y1="8" x2="-32" y2="24" stroke="#94a3b8" stroke-width="2"/>
        <circle cx="-38" cy="28" r="12" fill="#334155" stroke="#64748b"/>
        <text x="-47" y="31" fill="#cbd5e1" font-size="7">CH₃</text>

        <line x1="14" y1="8" x2="32" y2="24" stroke="#94a3b8" stroke-width="2"/>
        <circle cx="38" cy="28" r="12" fill="#334155" stroke="#64748b"/>
        <text x="29" y="31" fill="#cbd5e1" font-size="7">CH₃</text>
      </g>
      <text x="15" y="116" fill="#cbd5e1" font-size="7.2">★ 중심 원소(Al)는 박막에 남고, 리간드(CH₃)는 떨어져 나감</text>
    </g>

    <!-- Key Role -->
    <rect x="15" y="307" width="265" height="98" rx="5" fill="#1e293b" stroke="#334155"/>
    <text x="12" y="18" fill="#fde047" font-size="8.5" font-weight="800">💡 전구체의 반도체 핵심 요건</text>
    <text x="12" y="34" fill="#cbd5e1" font-size="7.2">• 적절한 증기압 (기화되어 챔버 이송 용이)</text>
    <text x="12" y="48" fill="#cbd5e1" font-size="7.2">• 열적 안정성 (챔버 날아가는 도중 자가분해 방지)</text>
    <text x="12" y="62" fill="#a7f3d0" font-size="7.5" font-weight="800">• 자기제한 흡착 (ALD에서 표면 1개 층만 화학 흡착)</text>
    <text x="12" y="76" fill="#cbd5e1" font-size="7.2">• 반응 부산물의 휘발성 (배출 용이, 박막 잔류 불순물 0)</text>
    <text x="12" y="90" fill="#94a3b8" font-size="7">• 부식성 및 독성 낮을수록 생산 라인 유리</text>
  </g>

  <!-- PANEL B: Reactive Species (반응종) -->
  <g transform="translate(330, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.2"/>
    <text x="16" y="26" fill="#f87171" font-size="12" font-weight="800">■ (B) 반응종 (Reactive Species, 反應種)</text>

    <!-- Definition Card -->
    <g transform="translate(15, 42)">
      <rect width="280" height="120" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 개념: 에너지를 받아 활성화된 불안정 입자</text>
      <text x="10" y="34" fill="#cbd5e1" font-size="7.5">• <strong>어원</strong>: Reactive(반응성 높은) + Species(화학 입자 종)</text>
      <text x="10" y="48" fill="#cbd5e1" font-size="7.5">• <strong>본질</strong>: 열, 플라즈마, 광자 등으로 분자가 쪼개져 생성</text>
      <text x="10" y="64" fill="#f87171" font-size="7.8" font-weight="800">➔ 홑전자(라디칼) 또는 전하(이온)를 띤 극초반응 상태!</text>
      <text x="10" y="80" fill="#cbd5e1" font-size="7.2">• <strong>수명</strong>: 수 마이크로초(μs) ~ 밀리초(ms) 수준으로 극히 찰나</text>
      <text x="10" y="94" fill="#cbd5e1" font-size="7.2">• 닿는 즉시 화학 결합을 깨거나 재배열 (엄청난 활성 에너지)</text>
      <text x="10" y="108" fill="#94a3b8" font-size="7">• 예: O*, H*, N*, Cl*, F* 라디칼 / Ar⁺, CF₃⁺ 이온</text>
    </g>

    <!-- 3 Types of Reactive Species -->
    <g transform="translate(15, 172)">
      <rect width="280" height="125" rx="5" fill="#0b1329" stroke="#ef4444"/>
      <text x="10" y="18" fill="#f87171" font-size="8.5" font-weight="800">반응종의 3대 핵심 형태</text>

      <g transform="translate(10, 26)">
        <rect width="260" height="28" rx="3" fill="#1e293b"/>
        <text x="8" y="18" fill="#fbbf24" font-size="7.5" font-weight="800">① 중성 라디칼 (Radical, 예: O*, F*, OH*)</text>
        <text x="160" y="18" fill="#cbd5e1" font-size="6.8">홑전자 보유, 화학반응 주도</text>
      </g>
      <g transform="translate(10, 58)">
        <rect width="260" height="28" rx="3" fill="#1e293b"/>
        <text x="8" y="18" fill="#38bdf8" font-size="7.5" font-weight="800">② 반응성 이온 (Ion, 예: Ar⁺, Cl⁺, CF₃⁺)</text>
        <text x="160" y="18" fill="#cbd5e1" font-size="6.8">전기장 가속, 물리적 타격</text>
      </g>
      <g transform="translate(10, 90)">
        <rect width="260" height="28" rx="3" fill="#1e293b"/>
        <text x="8" y="18" fill="#a7f3d0" font-size="7.5" font-weight="800">③ 준안정 여기 분자 (Metastable, 예: Ar*, N₂*)</text>
        <text x="175" y="18" fill="#cbd5e1" font-size="6.8">에너지 전이 매개체</text>
      </g>
    </g>

    <!-- Deposition vs Etch Role -->
    <rect x="15" y="307" width="280" height="98" rx="5" fill="#1e293b" stroke="#334155"/>
    <text x="12" y="18" fill="#fde047" font-size="8.5" font-weight="800">💡 반응종의 공정별 활약</text>
    <text x="12" y="34" fill="#38bdf8" font-size="7.2">• <strong>PECVD/PEALD (증착)</strong>: 라디칼이 저온에서 리간드를 분해</text>
    <text x="18" y="46" fill="#cbd5e1" font-size="6.8">(열 에너지가 부족해도 반응종의 활성에너지로 박막 합성)</text>
    <text x="12" y="62" fill="#f87171" font-size="7.2">• <strong>플라즈마 건식 식각 (Etch)</strong>: F*, Cl* 라디칼이 박막과 화학반응</text>
    <text x="18" y="74" fill="#cbd5e1" font-size="6.8">(휘발성 SiF₄ 생성) + 이온(CF₃⁺)의 수직 물리 충돌로 비등방 식각</text>
    <text x="12" y="90" fill="#a7f3d0" font-size="7.2">• <strong>플라즈마 애싱 (Ashing)</strong>: O* 라디칼이 PR(탄소)을 CO₂로 태움</text>
  </g>

  <!-- PANEL C: ALD/CVD Interaction (전구체 + 반응가스 + 반응종) -->
  <g transform="translate(655, 20)">
    <rect width="305" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (C) 반도체 ALD 공정에서의 상호작용</text>

    <!-- 4-Step ALD Flow Visual -->
    <g transform="translate(15, 42)">
      <rect width="275" height="195" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">ALD 공정 4단계와 3자 역할 구분</text>

      <!-- Step 1 -->
      <g transform="translate(10, 28)">
        <rect width="255" height="36" rx="3" fill="#0b1329" stroke="#38bdf8"/>
        <text x="8" y="14" fill="#38bdf8" font-size="7.5" font-weight="800">1단계: 전구체(Precursor, TMA) 주입</text>
        <text x="14" y="27" fill="#cbd5e1" font-size="6.8">➔ 웨이퍼 표면에 Al-CH₃가 1원자층 자기포화 흡착</text>
      </g>
      <!-- Step 2 -->
      <g transform="translate(10, 68)">
        <rect width="255" height="34" rx="3" fill="#0b1329" stroke="#64748b"/>
        <text x="8" y="14" fill="#94a3b8" font-size="7.5" font-weight="800">2단계: 퍼지 (Purge, N₂ / Ar)</text>
        <text x="14" y="26" fill="#cbd5e1" font-size="6.8">➔ 반응하지 않고 남은 잉여 전구체 분자 진공 배출</text>
      </g>
      <!-- Step 3 -->
      <g transform="translate(10, 106)">
        <rect width="255" height="46" rx="3" fill="#0b1329" stroke="#10b981"/>
        <text x="8" y="14" fill="#34d399" font-size="7.5" font-weight="800">3단계: 반응가스(Reactant, H₂O/O₃) or 반응종(O*)</text>
        <text x="14" y="27" fill="#cbd5e1" font-size="6.8">• Thermal ALD: 안정된 반응가스(H₂O)가 열로 반응</text>
        <text x="14" y="39" fill="#fde047" font-size="6.8">• PEALD: 플라즈마로 만든 초강력 산소 라디칼(O*) 반응종 주입!</text>
      </g>
      <!-- Step 4 -->
      <g transform="translate(10, 156)">
        <rect width="255" height="32" rx="3" fill="#0b1329" stroke="#f59e0b"/>
        <text x="8" y="13" fill="#fbbf24" font-size="7.5" font-weight="800">4단계: 리간드 치환 및 최종 박막 (Al₂O₃) 완성</text>
        <text x="14" y="25" fill="#cbd5e1" font-size="6.8">➔ CH₄ 부산물 배출 후 순수한 Al-O 단원자층 증착</text>
      </g>
    </g>

    <!-- Contrast Table / Summary -->
    <g transform="translate(15, 248)">
      <rect width="275" height="157" rx="6" fill="#0b1329" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="8.8" font-weight="800">🎯 최종 1초 요약 대조표</text>
      <text x="12" y="36" fill="#38bdf8" font-size="7.8" font-weight="800">■ 전구체 (Precursor):</text>
      <text x="20" y="50" fill="#cbd5e1" font-size="7.2">• "박막의 뼈대 원소를 담아 넣는 <strong>안정된 출발 재료</strong>"</text>
      <text x="20" y="62" fill="#cbd5e1" font-size="7.2">• 비유: 요리의 '신선한 생고기(원재료)'</text>

      <text x="12" y="80" fill="#f87171" font-size="7.8" font-weight="800">■ 반응종 (Reactive Species):</text>
      <text x="20" y="94" fill="#cbd5e1" font-size="7.2">• "에너지를 받아 화학 반응을 때리는 <strong>불안정 활성 입자</strong>"</text>
      <text x="20" y="106" fill="#cbd5e1" font-size="7.2">• 비유: 고기를 지글지글 굽는 '불꽃과 열기(에너지 전달체)'</text>

      <text x="12" y="124" fill="#fde047" font-size="7.8" font-weight="800">■ 반응가스 (Reactant):</text>
      <text x="20" y="138" fill="#cbd5e1" font-size="7.2">• 전구체의 짝꿍 물질 (예: 산화제 O₃, 질화제 NH₃)</text>
      <text x="20" y="150" fill="#a7f3d0" font-size="7.2">➔ 반응가스가 플라즈마로 쪼개지면 '반응종'이 됨!</text>
    </g>
  </g>
</svg>""",
    "lecture": r"""
        <!-- SECTION 1: Fundamental Distinction -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 결론부터: '전구체'와 '반응종'은 절대 똑같은 말이 아닙니다!
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체 박막 증착(CVD, ALD)이나 플라즈마 식각(Dry Etching) 공정을 공부할 때 두 용어가 함께 등장하여 혼동하기 쉽지만, 둘은 <strong>물리적 성격, 존재 상태, 그리고 공정 내에서의 역할이 완전히 다른 범주의 개념</strong>입니다:
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ① 전구체 (Precursor, 前驅體): "박막을 이룰 원소를 배달하는 안정된 출발 물질"
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              • <strong>어원</strong>: '앞설 전(前)', '몰 구(驅)'를 써서, 최종 생성물이 되기 <strong>이전 단계에서 앞서 달려가는 물질</strong>이라는 뜻입니다. 영어 Precursor(Pre- + Cursor) 역시 '선구자, 선행 물질'을 의미합니다.
              <br>• <strong>본질</strong>: 최종적으로 박막에 남아야 할 주원소(Si, Al, Ti, Hf 등)를 품고 있는 <strong>화학적으로 안정된 완제품 분자</strong>입니다.
              <br>• 상온 또는 적당한 가열 상태에서 캐니스터(Canister) 용기에 액체나 기체로 보관되며, 일정한 증기압을 갖고 기화되어 배관을 타고 챔버 안으로 온전한 분자 형태로 날아갑니다.
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #ef4444; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:18px;">
            <h4 style="color:#f87171; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ② 반응종 (Reactive Species, 反應種): "에너지를 받아 극도로 흥분한 초단수명 활성 입자"
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              • <strong>어원</strong>: 반응성(Reactive)을 가진 화학적 입자의 종류(Species)를 뜻합니다.
              <br>• <strong>본질</strong>: 열에너지, 강한 전기장, RF 플라즈마, 자외선(UV) 등의 외력을 받아 결합이 깨지거나 전자가 들떠서 <strong>화학 반응을 즉각적으로 일으킬 수 있는 극도로 불안정한 전이 상태 입자(라디칼, 이온 등)</strong>를 통칭합니다.
              <br>• <strong>수명</strong>: 수명이 수 마이크로초($\mu\text{s}$)에서 수 밀리초($\text{ms}$)에 불과하여 용기에 담아 보관하거나 운반할 수 없습니다. <strong>오직 챔버 내부에서 실시간으로 생성되어 반응하고 즉시 소멸</strong>합니다.
            </p>
          </div>

          <div style="background:#1e293b; padding:16px 20px; border-radius:8px; margin-bottom:20px;">
            <h4 style="color:#fde047; font-size:0.98rem; font-weight:800; margin-bottom:8px;">
              🍳 직관적인 일상 요리 비유
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; margin:0;">
              스테이크를 굽는 상황에 비유하면 아주 명쾌합니다:
              <br>• <strong>전구체(Precursor)</strong>: 식탁에 올릴 최종 요리가 되기 위해 정육점에서 사 온 <strong>'신선한 소고기 덩어리(원재료 분자)'</strong>입니다. 냉장고에 보관할 수 있고 안정적입니다.
              <br>• <strong>반응가스(Reactant)</strong>: 고기와 결합할 <strong>'소금, 버터, 공기 중의 산소(부원료 분자)'</strong>입니다.
              <br>• <strong>반응종(Reactive Species)</strong>: 프라이팬 밑에서 뿜어져 나오는 <strong>'지글지글한 가스 불꽃과 복사열(화학 결합을 깨는 고에너지 활성 인자)'</strong>입니다. 불꽃 자체는 고기가 아니지만, 불꽃이 닿아야 비로소 소고기가 익어 스테이크가 됩니다!
            </p>
          </div>
        </div>

        <!-- SECTION 2: Detailed Chemistry -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 한눈에 비교하는 전구체 vs 반응종 물성 대조표
          </h3>
          <div style="overflow-x:auto; margin-bottom:20px;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">비교 항목</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">전구체 (Precursor)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">반응종 (Reactive Species)</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">화학적 상태</td>
                  <td style="padding:10px 14px;">안정한 중성 분자 (Molecule)</td>
                  <td style="padding:10px 14px; color:#f87171; font-weight:800;">불안정한 라디칼, 이온, 여기 상태 분자</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">존재 수명</td>
                  <td style="padding:10px 14px;">반영구적 (캐니스터에 장기 보관 가능)</td>
                  <td style="padding:10px 14px; color:#f87171; font-weight:800;">수 $\mu\text{s} \sim \text{ms}$ (순간 생성 후 즉시 충돌 소멸)</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">발생 위치</td>
                  <td style="padding:10px 14px;">외부 기화기에서 발생시켜 배관으로 투입</td>
                  <td style="padding:10px 14px;">챔버 내부 플라즈마 방전 또는 고온 표면에서 생성</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">반도체 내 역할</td>
                  <td style="padding:10px 14px;">최종 박막의 골격 원소(Si, Ti, Al 등) 공급</td>
                  <td style="padding:10px 14px;">리간드 분해, 산화/질화 환원 반응 구동, 물리/화학 식각</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">대표 예시</td>
                  <td style="padding:10px 14px;">$\text{SiH}_4, \text{TEOS}, \text{TiCl}_4, \text{TMA}, \text{TDMAH}$</td>
                  <td style="padding:10px 14px;">$\text{O}^*, \text{H}^*, \text{N}^*, \text{F}^*, \text{CF}_3^*, \text{Ar}^+, \text{Cl}^+$</td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">주 적용 공정</td>
                  <td style="padding:10px 14px;">CVD, ALD 등 **증착(Deposition) 공정 전용**</td>
                  <td style="padding:10px 14px;">PECVD, PEALD뿐 아니라 **건식 식각(Etch), 애싱(Ashing)** 등 전방위</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- SECTION 3: Common Confusion Points -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 왜 두 단어가 헷갈릴까? ('반응가스 Reactant'와의 혼동 해소)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            학습자들이 가장 많이 혼동하는 이유는 **"반응가스(Reactant)"**라는 개념과 **"반응종(Reactive Species)"**이라는 단어의 발음이 비슷하기 때문입니다.
            ALD(원자층 증착) 공정의 표준 메커니즘을 보면 3자의 관계가 아주 깔끔하게 정리됩니다:
          </p>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ALD에서의 3자 협업: TMA + H₂O(or O* 플라즈마) ➔ Al₂O₃ 박막 증착
            </h4>
            <ol style="color:#cbd5e1; font-size:0.9rem; line-height:1.8; padding-left:20px; margin:0;">
              <li><strong>전구체(Precursor) 주입</strong>: 알루미늄을 머금은 $\text{TMA}(\text{Al}(\text{CH}_3)_3)$ 증기를 넣습니다. 웨이퍼 표면의 -OH 작용기와 만나 화학 흡착하며 메탄($\text{CH}_4$) 하나를 뱉고 자기포화(Self-limiting)됩니다.</li>
              <li><strong>퍼지(Purge)</strong>: 반응하지 않은 잉여 전구체 분자를 질소($\text{N}_2$) 가스로 불어내어 챔버 밖으로 배출합니다.</li>
              <li><strong>반응가스(Reactant) 또는 반응종(Reactive Species) 투입</strong>:
                <br>• <strong>열 ALD (Thermal ALD)</strong>: 안정된 분자 형태의 산화제 가스인 **$\text{H}_2\text{O}$ 또는 $\text{O}_3$(반응가스)**를 넣어 고온 열로 리간드($-\text{CH}_3$)를 떼어냅니다.
                <br>• <strong>플라즈마 ALD (PEALD)</strong>: 산소($\text{O}_2$) 가스에 플라즈마 방전을 걸어 산소 분자를 쪼갠 **초활성 산소 라디칼($\text{O}^*$, 반응종)**을 만들어 때려 넣습니다! 반응종의 에너지가 워낙 높아 상온~저온($100^\circ\text{C}$ 이하)에서도 순식간에 알루미늄 산화막($\text{Al}_2\text{O}_3$)이 완성됩니다.
              </li>
              <li><strong>퍼지(Purge)</strong>: 반응 부산물로 떨어져 나온 메탄 가스를 배출하고 단원자층 증착을 끝냅니다.</li>
            </ol>
          </div>

          <div style="background:#0f172a; border-left:4px solid #f59e0b; padding:16px 20px; border-radius:0 8px 8px 0;">
            <h4 style="color:#fbbf24; font-size:1rem; font-weight:800; margin-bottom:6px;">
              💡 핵심 요약 공식
            </h4>
            <p style="color:#cbd5e1; font-size:0.92rem; line-height:1.75; margin:0;">
              • <strong>전구체(Precursor)</strong> = 박막을 만들 뼈대 원소를 담은 **안정된 원료 분자**<br>
              • <strong>반응가스(Reactant)</strong> = 전구체와 반응하도록 넣어주는 **짝꿍 가스(산화제, 질화제 등)**<br>
              • <strong>반응종(Reactive Species)</strong> = 반응가스나 원료가 플라즈마/열로 쪼개져 맹렬한 반응성을 갖게 된 **초단수명 활성 알맹이(라디칼, 이온)**
            </p>
          </div>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 95 topics (q-95 down to q-01) by +1
    for old_n in range(95, 0, -1):
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

    # Step 4: Update header description to 96 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 '반응종과 전구체의 본질적 차이(Q01)'가 위치하며, 총 96개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Precursor vs Reactive Species topic!")
