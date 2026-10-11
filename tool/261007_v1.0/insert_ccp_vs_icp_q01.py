# -*- coding: utf-8 -*-
"""
insert_ccp_vs_icp_q01.py
사용자 질문:
"ccp와 icp의 차이"

기존 96개 질문을 Q02~Q97로 시프트하고, 최상단 Q01에 신규 등록 (총 97개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (플라즈마 공학 & 식각 공정 · CCP vs ICP 방전 원리와 독립 제어, 산화막 vs 실리콘 식각 비교)",
    "title": "CCP(용량결합)와 ICP(유도결합) 플라즈마의 본질적 차이 (방전 메커니즘, 밀도, 이온 에너지 독립 제어, 절연막 vs 도체 식각)",
    "nav_title": "CCP와 ICP 플라즈마의 본질적 차이",
    "summary": [
        "<strong>1. 방전 메커니즘과 전기장 구조의 차이</strong>: CCP(Capacitively Coupled)는 마주 보는 평행 평판 전극에 RF 전압을 걸어 전극에 수직인 정전기장($E_\\perp$)으로 전자를 가속하고, ICP(Inductively Coupled)는 세라믹 창 위의 RF 코일에 시변 전류를 흘려 패러데이 법칙($\\nabla \\times E = -\\partial B/\\partial t$)에 의해 유도된 수평 회전 전기장($E_\\parallel$)으로 전자를 소용돌이치게 가속합니다.",
        "<strong>2. 플라즈마 밀도와 동작 압력의 극적인 격차</strong>: CCP는 전자가 왕복 운동 중 전극 벽면에 부딪혀 쉽게 소멸하여 밀도가 $10^9 \\sim 10^{10}\\,\\text{cm}^{-3}$로 낮고 $50\\sim 수백\\,\\text{mTorr}$ 중고압에서 동작합니다. 반면 ICP는 전자가 벽에 닿지 않고 챔버 내부를 맴돌며 가스를 지속 이온화하므로 $10^{11} \\sim 10^{12}\\,\\text{cm}^{-3}$의 고밀도(High Density)를 $1\\sim 50\\,\\text{mTorr}$의 초저압에서 유지합니다.",
        "<strong>3. 이온 플럭스(밀도)와 이온 에너지(바이어스)의 독립 제어 (Decoupling)</strong>: CCP는 소스 파워와 바이어스 전압이 단일 회로로 묶여 있어 밀도를 올리면 이온 충돌 에너지(시스 전압)도 덩달아 올라가는 종속 관계입니다(이중 주파수로 일부 완화). 반면 ICP는 상단 안테나 RF(이온 생성 밀도)와 하단 척 RF(이온 가속 에너지)가 구조적으로 100% 분리되어 완벽한 독립 제어가 가능합니다.",
        "<strong>4. 반도체 제조 공정별 핵심 분업</strong>: CCP는 강한 물리적 이온 충격과 두꺼운 시스가 필요한 <strong>산화막/절연막 식각 (Dielectric Etch, $\\text{SiO}_2, \\text{Si}_3\\text{N}_4$, 고종횡비 HARC)</strong> 및 PECVD 증착에 적합하며, ICP는 얇은 게이트 절연막 손상을 방지하고 미세 수직 패턴을 화학적으로 정밀 가공하는 <strong>도체/실리콘/금속 식각 (Conductor Etch, Poly-Si, STI, Metal Gate)</strong>의 절대 표준입니다."
    ],
    "svg_title": "📊 [CCP vs ICP 플라즈마 장비 및 물리 메커니즘 종합 비교 다이어그램] (A) CCP 용량결합 구조 및 정전기장 | (B) ICP 유도결합 구조 및 회전 유도전기장 | (C) 물성 파라미터 및 반도체 공정 맵",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: CCP (Capacitively Coupled Plasma) -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) CCP (용량결합 플라즈마)</text>

    <!-- Chamber Schematic -->
    <g transform="translate(15, 38)">
      <rect width="270" height="195" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">평행 평판 커패시터 정전기장 (E_z)</text>

      <!-- Top Electrode (Powered or Ground) -->
      <rect x="25" y="30" width="220" height="14" rx="2" fill="#64748b" stroke="#94a3b8"/>
      <text x="75" y="41" fill="#fff" font-size="7.5" font-weight="800">상부 전극 (Top Showerhead)</text>

      <!-- Plasma Bulk -->
      <rect x="25" y="55" width="220" height="85" fill="#0284c7" opacity="0.3" stroke="#38bdf8" stroke-dasharray="3,3"/>
      <text x="80" y="98" fill="#38bdf8" font-size="10" font-weight="900">Plasma Bulk (10⁹~10¹⁰ cm⁻³)</text>
      
      <!-- Vertical E-Field arrows -->
      <path d="M 60 48 L 60 135" stroke="#f43f5e" stroke-width="1.8" marker-end="url(#arrowRedC)"/>
      <path d="M 135 48 L 135 135" stroke="#f43f5e" stroke-width="1.8" marker-end="url(#arrowRedC)"/>
      <path d="M 210 48 L 210 135" stroke="#f43f5e" stroke-width="1.8" marker-end="url(#arrowRedC)"/>
      <text x="145" y="70" fill="#f87171" font-size="7" font-weight="800">수직 정전기장 E_z</text>

      <!-- Sheath regions -->
      <rect x="25" y="44" width="220" height="10" fill="#ef4444" opacity="0.25"/>
      <rect x="25" y="130" width="220" height="18" fill="#ef4444" opacity="0.35"/>
      <text x="30" y="143" fill="#fca5a5" font-size="7.2" font-weight="800">강한 시스 (두께 수 mm, 높은 V_bias)</text>

      <!-- Bottom Chuck / Wafer -->
      <rect x="45" y="148" width="180" height="12" rx="2" fill="#38bdf8"/>
      <text x="95" y="157" fill="#0b1120" font-size="7.5" font-weight="900">웨이퍼 (Wafer)</text>
      <rect x="25" y="160" width="220" height="14" rx="2" fill="#475569" stroke="#64748b"/>
      <text x="80" y="171" fill="#cbd5e1" font-size="7.5" font-weight="800">하부 전극 (RF 척 / ESC)</text>

      <!-- RF Source notation -->
      <text x="30" y="188" fill="#cbd5e1" font-size="7">• RF 전압(13.56MHz) 인가 ➔ 전자 왕복 가속</text>
    </g>

    <!-- Characteristics Box -->
    <g transform="translate(15, 242)">
      <rect width="270" height="163" rx="5" fill="#0b1329" stroke="#38bdf8"/>
      <text x="12" y="18" fill="#38bdf8" font-size="8.8" font-weight="800">CCP의 핵심 물리적 특성</text>
      <text x="12" y="35" fill="#cbd5e1" font-size="7.5">• <strong>플라즈마 밀도</strong>: 낮음 ($10^9 \sim 10^{10} \, \text{cm}^{-3}$)</text>
      <text x="12" y="49" fill="#cbd5e1" font-size="7.5">• <strong>동작 압력</strong>: 중고압 ($50 \sim 500 \, \text{mTorr}$)</text>
      <text x="12" y="63" fill="#f87171" font-size="7.5" font-weight="800">• <strong>커플링 종속성</strong>: 밀도와 이온 에너지가 얽힘!</text>
      <text x="18" y="76" fill="#94a3b8" font-size="7">- 파워 올리면 플라즈마 밀도↑ + 바이어스 전압↑ 동시 폭증</text>
      <text x="12" y="92" fill="#fde047" font-size="7.8" font-weight="800">• <strong>강점: 막강한 이온 충돌 에너지 (V_dc 수백~수천V)</strong></text>
      <text x="18" y="105" fill="#cbd5e1" font-size="7.2">- 단단한 산화막(SiO₂, Si₃N₄) 화학결합 분쇄 탁월</text>
      <text x="12" y="121" fill="#34d399" font-size="7.5" font-weight="800">• <strong>주요 용도: 절연막 식각 (Dielectric Etch), PECVD</strong></text>
      <text x="18" y="134" fill="#cbd5e1" font-size="7.2">- VNAND 수십 ㎛ 깊은 구멍 뚫는 HARC 공정 절대 강자</text>
      <text x="12" y="150" fill="#94a3b8" font-size="7">• 개선책: DF-CCP (고주파 HF 60MHz + 저주파 LF 2MHz)</text>
    </g>
  </g>

  <!-- PANEL B: ICP (Inductively Coupled Plasma) -->
  <g transform="translate(335, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) ICP (유도결합 플라즈마)</text>

    <!-- Chamber Schematic -->
    <g transform="translate(15, 38)">
      <rect width="280" height="195" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">패러데이 유도 회전 전기장 (E_θ, B_z)</text>

      <!-- Antenna Coils on top -->
      <rect x="25" y="28" width="230" height="8" rx="2" fill="#f59e0b" stroke="#fbbf24"/>
      <circle cx="65" cy="32" r="6" fill="#ef4444"/><circle cx="115" cy="32" r="6" fill="#ef4444"/><circle cx="165" cy="32" r="6" fill="#ef4444"/><circle cx="215" cy="32" r="6" fill="#ef4444"/>
      <text x="75" y="24" fill="#fbbf24" font-size="7" font-weight="800">RF 안테나 코일 (Source Power)</text>

      <!-- Dielectric Window (Quartz) -->
      <rect x="25" y="40" width="230" height="8" fill="#94a3b8" stroke="#cbd5e1"/>
      <text x="75" y="47" fill="#000" font-size="6.5" font-weight="800">유전체 창 (Quartz / Al₂O₃ Window)</text>

      <!-- Plasma Bulk High Density -->
      <rect x="25" y="55" width="230" height="85" fill="#10b981" opacity="0.35" stroke="#34d399" stroke-dasharray="3,3"/>
      <text x="70" y="98" fill="#34d399" font-size="10" font-weight="900">High-Density Plasma (10¹¹~10¹² cm⁻³)</text>

      <!-- Swirling E-theta path -->
      <ellipse cx="140" cy="95" rx="75" ry="24" fill="none" stroke="#facc15" stroke-width="2" stroke-dasharray="4,3"/>
      <path d="M 215 95 L 215 102" stroke="#facc15" stroke-width="2" marker-end="url(#arrowYellowC)"/>
      <text x="85" y="112" fill="#fde047" font-size="7" font-weight="800">회전 유도전기장 E_θ (벽 충돌 없이 가속!)</text>

      <!-- Thin Sheath -->
      <rect x="25" y="136" width="230" height="8" fill="#ef4444" opacity="0.2"/>
      <text x="30" y="143" fill="#cbd5e1" font-size="6.5">얇은 시스 (저손상)</text>

      <!-- Bottom Chuck / Wafer -->
      <rect x="50" y="146" width="180" height="12" rx="2" fill="#38bdf8"/>
      <text x="100" y="155" fill="#0b1120" font-size="7.5" font-weight="900">웨이퍼 (Wafer)</text>
      <rect x="25" y="158" width="230" height="14" rx="2" fill="#475569" stroke="#64748b"/>
      <text x="80" y="169" fill="#cbd5e1" font-size="7.5" font-weight="800">하부 바이어스 척 (Bias Power)</text>

      <text x="25" y="188" fill="#a7f3d0" font-size="7">★ 상단 코일 = 밀도 결정 / 하단 척 = 이온 가속 에너지 결정</text>
    </g>

    <!-- Characteristics Box -->
    <g transform="translate(15, 242)">
      <rect width="280" height="163" rx="5" fill="#0b1329" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="8.8" font-weight="800">ICP의 핵심 물리적 특성</text>
      <text x="12" y="35" fill="#cbd5e1" font-size="7.5">• <strong>플라즈마 밀도</strong>: 초고밀도 ($10^{11} \sim 10^{12} \, \text{cm}^{-3}$, CCP의 100배!)</text>
      <text x="12" y="49" fill="#cbd5e1" font-size="7.5">• <strong>동작 압력</strong>: 초저압 ($1 \sim 50 \, \text{mTorr}$, 산란 감소 비등방성↑)</text>
      <text x="12" y="63" fill="#34d399" font-size="7.8" font-weight="800">• <strong>독립 제어 (Decoupling) 완벽 구현!</strong></text>
      <text x="18" y="76" fill="#cbd5e1" font-size="7">- 상단 안테나 파워: 플라즈마 밀도 (이온/라디칼 플럭스) 조절</text>
      <text x="18" y="88" fill="#cbd5e1" font-size="7">- 하단 바이어스 파워: 웨이퍼 입사 이온 에너지 (V_dc) 조절</text>
      <text x="12" y="104" fill="#fde047" font-size="7.5" font-weight="800">• <strong>강점: 저손상(Low Damage) + 초미세 수직 식각</strong></text>
      <text x="18" y="117" fill="#cbd5e1" font-size="7.2">- 게이트 옥사이드 등 하부 박막 뚫림(Pinhole) 파괴 원천 차단</text>
      <text x="12" y="133" fill="#38bdf8" font-size="7.5" font-weight="800">• <strong>주요 용도: 실리콘/도체/금속 식각 (Conductor Etch)</strong></text>
      <text x="18" y="146" fill="#cbd5e1" font-size="7.2">- Poly-Si 게이트, STI 트렌치, 메탈 배선, GAA 나노시트</text>
    </g>
  </g>

  <!-- PANEL C: Comparison & Application Map -->
  <g transform="translate(660, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="12" font-weight="800">■ (C) 한눈에 보는 핵심 대조표</text>

    <!-- Contrast Table -->
    <g transform="translate(15, 38)">
      <rect width="270" height="230" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">물성 및 공정 파라미터 대결</text>

      <g transform="translate(10, 26)">
        <rect width="250" height="34" rx="3" fill="#0b1329"/>
        <text x="8" y="14" fill="#38bdf8" font-size="7.2" font-weight="800">1. 플라즈마 밀도 &amp; 압력:</text>
        <text x="14" y="26" fill="#cbd5e1" font-size="6.8">CCP: 10⁹~10¹⁰ cm⁻³ (고압)  vs  ICP: 10¹¹~10¹² cm⁻³ (저압)</text>
      </g>
      <g transform="translate(10, 66)">
        <rect width="250" height="34" rx="3" fill="#0b1329"/>
        <text x="8" y="14" fill="#34d399" font-size="7.2" font-weight="800">2. 독립 제어 (밀도 vs 에너지):</text>
        <text x="14" y="26" fill="#cbd5e1" font-size="6.8">CCP: 결합(종속적)  vs  ICP: 100% 독립 분리 제어</text>
      </g>
      <g transform="translate(10, 106)">
        <rect width="250" height="36" rx="3" fill="#0b1329"/>
        <text x="8" y="14" fill="#f87171" font-size="7.2" font-weight="800">3. 이온 충돌 에너지 &amp; 시스:</text>
        <text x="14" y="27" fill="#cbd5e1" font-size="6.8">CCP: 두껍고 강한 시스(수백V)  vs  ICP: 얇고 조절형 시스</text>
      </g>
      <g transform="translate(10, 148)">
        <rect width="250" height="36" rx="3" fill="#0b1329"/>
        <text x="8" y="14" fill="#fbbf24" font-size="7.2" font-weight="800">4. 대면적 균일도 (Uniformity):</text>
        <text x="14" y="27" fill="#cbd5e1" font-size="6.8">CCP: 전극 면적으로 300mm 균일  vs  ICP: 코일 형상 최적화</text>
      </g>
      <g transform="translate(10, 190)">
        <rect width="250" height="32" rx="3" fill="#0b1329"/>
        <text x="8" y="13" fill="#a7f3d0" font-size="7.2" font-weight="800">5. 챔버 구조 복잡성 &amp; 단가:</text>
        <text x="14" y="25" fill="#cbd5e1" font-size="6.8">CCP: 구조 단순, 저렴  vs  ICP: 유전체창, 안테나, 복잡</text>
      </g>
    </g>

    <!-- Semiconductor Application Decision Guide -->
    <g transform="translate(15, 276)">
      <rect width="270" height="129" rx="6" fill="#0b1329" stroke="#f59e0b"/>
      <text x="12" y="16" fill="#fbbf24" font-size="8.8" font-weight="800">🎯 현업 공정 선택 가이드</text>
      <text x="12" y="32" fill="#38bdf8" font-size="7.5" font-weight="800">■ CCP 선택 기준:</text>
      <text x="16" y="44" fill="#cbd5e1" font-size="7">• "결합 에너지가 큰 막을 깊게 뚫어야 할 때"</text>
      <text x="16" y="56" fill="#cbd5e1" font-size="7">• SiO₂, SiN 산화막 식각, 고종횡비 접촉창(HARC)</text>

      <text x="12" y="74" fill="#34d399" font-size="7.5" font-weight="800">■ ICP 선택 기준:</text>
      <text x="16" y="86" fill="#cbd5e1" font-size="7">• "하부 소자 손상 없이 미세 패턴을 정밀하게 깎을 때"</text>
      <text x="16" y="98" fill="#cbd5e1" font-size="7">• Poly-Si, 금속 게이트, STI, FinFET/GAA 3D 구조</text>
      <text x="16" y="112" fill="#fde047" font-size="7.2" font-weight="800">➔ 고에너지 파괴는 CCP, 정밀 외과의사는 ICP!</text>
    </g>
  </g>

  <!-- Markers -->
  <defs>
    <marker id="arrowRedC" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#f43f5e" />
    </marker>
    <marker id="arrowYellowC" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#facc15" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- SECTION 1: Fundamental Concept & Discharge Mechanism -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 플라즈마 방전의 양대 산맥: CCP와 ICP의 원천적 발생 원리
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체 건식 식각(Dry Etching)과 플라즈마 증착(PECVD) 공정에서 가스를 전기적으로 이온화시켜 플라즈마를 발생시키는 소스(Source)는 크게 <strong>CCP (용량결합 플라즈마)</strong>와 <strong>ICP (유도결합 플라즈마)</strong> 두 가지 방식으로 나뉩니다.
            두 기술의 근본적인 차이는 <strong>"어떤 방향의 전기장(정전기장 vs 유도기장)으로 전자를 가속시켜 중성 기체를 충돌 이온화시키는가?"</strong>에서 출발합니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ① CCP (Capacitively Coupled Plasma, 용량결합 플라즈마)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              • <strong>구조</strong>: 마치 커패시터(축전기)처럼 마주 보는 두 개의 평행 평판 금속 전극(샤워헤드와 하부 정전척) 사이에 웨이퍼를 놓는 구조입니다.
              <br>• <strong>전기장 형태</strong>: RF 고주파 전압이 걸리면 두 전극 사이에 전극 표면에 수직인 <strong>시변 정전기장($E_z = V/d$)</strong>이 형성됩니다.
              <br>• <strong>전자 거동 및 한계</strong>: 전자가 상하로 왕복 운동하며 가스를 때려 이온화시킵니다. 하지만 전자가 위아래 전극 벽면에 정면으로 충돌하여 흡수 소멸(Wall Loss)되기 쉬워, 플라즈마 밀도를 높이는 데 한계가 있습니다.
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:18px;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ② ICP (Inductively Coupled Plasma, 유도결합 플라즈마)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              • <strong>구조</strong>: 챔버 상단의 유전체 창(석영 또는 세라믹) 외벽에 나선형 코일(Antenna)을 감아놓은 구조입니다.
              <br>• <strong>전기장 형태</strong>: RF 코일에 전류가 흐르면 시변 자기장($B_z$)이 생기고, 패러데이 전자기 유도 법칙($\nabla \times E = -\frac{\partial B}{\partial t}$)에 의해 챔버 내부에 <strong>수평으로 소용돌이치는 유도 전기장($E_\theta$)</strong>이 형성됩니다.
              <br>• <strong>전자 거동과 고밀도 달성</strong>: 전자가 전극에 부딪히지 않고 챔버 내부를 맴돌며(Closed Loop) 나선형으로 회전 가속됩니다. 벽면 손실 없이 기체와 수없이 충돌하므로 **CCP보다 10~100배 높은 고밀도 플라즈마($10^{11}\sim 10^{12}\,\text{cm}^{-3}$)**를 달성합니다.
            </p>
          </div>
        </div>

        <!-- SECTION 2: Decoupling and Density/Pressure Tradeoffs -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fde047; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 결정적 차이: 이온 밀도(Flux)와 이온 에너지(Bias)의 독립 제어 (Decoupling)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            식각 엔지니어가 플라즈마 장비를 선택할 때 가장 중요하게 보는 핵심 성능 지표는 <strong>"이온 플럭스(식각 속도를 결정하는 이온 개수)와 이온 에너지(식각 직진성과 물리적 타격력을 결정하는 가속 전압)를 따로따로 조절할 수 있는가?"</strong>입니다.
          </p>

          <div style="overflow-x:auto; margin-bottom:18px;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">비교 항목</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">CCP (용량결합)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">ICP (유도결합)</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">플라즈마 밀도 ($n_e$)</td>
                  <td style="padding:10px 14px;">$10^9 \sim 10^{10} \, \text{cm}^{-3}$ (상대적 저밀도)</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:800;">$10^{11} \sim 10^{12} \, \text{cm}^{-3}$ (고밀도, High-Density)</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">운전 공정 압력</td>
                  <td style="padding:10px 14px;">$50 \sim 500 \, \text{mTorr}$ (중고압)</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:800;">$1 \sim 50 \, \text{mTorr}$ (초저압 운전 가능)</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#f87171;">밀도-에너지 제어성<br>(Decoupling)</td>
                  <td style="padding:10px 14px; color:#f87171;"><strong>종속적 (Coupled)</strong><br>RF 파워를 올리면 플라즈마 밀도와 시스 전압(이온 충격력)이 동시에 상승함</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:800;"><strong>100% 완전 독립 제어 (Decoupled)</strong><br>상단 코일 RF로 밀도 조절 + 하단 척 RF로 이온 충격 가속 전압 완벽 분리</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">시스(Sheath) 전압</td>
                  <td style="padding:10px 14px; font-weight:700; color:#f87171;">두껍고 매우 높음 ($V_{bias} \sim \text{수백 V}$)</td>
                  <td style="padding:10px 14px; color:#34d399;">얇고 하부 바이어스로 자유 조절 ($V_{bias} \sim \text{수십~수백 V}$)</td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">소자 손상 (Damage)</td>
                  <td style="padding:10px 14px; color:#f87171;">높은 이온 충격으로 게이트 산화막 손상 위험 큼</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:800;">저에너지 고밀도 이온화로 <strong>초저손상(Low Damage)</strong></td>
                </tr>
              </tbody>
            </table>
          </div>

          <div style="background:#1e293b; padding:16px 20px; border-radius:8px; margin-bottom:16px;">
            <h4 style="color:#38bdf8; font-size:0.95rem; font-weight:800; margin-bottom:6px;">
              💡 DF-CCP (이중 주파수 CCP)의 탄생 배경
            </h4>
            <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
              단일 주파수 CCP의 종속성 한계를 극복하기 위해, 현대 반도체 장비는 <strong>DF-CCP (Dual-Frequency CCP)</strong>를 도입했습니다. 
              상부 또는 하부에 <strong>초고주파(VHF, 예: 60MHz 또는 100MHz)</strong>를 걸어 전자를 주로 진동시켜 '플라즈마 밀도'를 올리고, 하부에 <strong>저주파(LF, 예: 2MHz 또는 13.56MHz)</strong>를 걸어 무거운 이온을 당기는 '시스 바이어스 전압'을 조절함으로써 CCP에서도 준(準) 독립 제어를 구현하고 있습니다.
            </p>
          </div>
        </div>

        <!-- SECTION 3: Semiconductor Application Division of Labor -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 반도체 FAB 현업에서의 역할 분담: 산화막 식각(CCP) vs 도체 식각(ICP)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체 공정에서는 식각하려는 막질의 화학 결합 강도와 하부 소자의 손상 민감도에 따라 CCP와 ICP 챔버를 명확히 구분하여 사용합니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ■ CCP의 텃밭: 절연막 식각 (Dielectric Etch) 및 HARC 공정
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              • $\text{SiO}_2$나 $\text{Si}_3\text{N}_4$ 같은 절연막은 Si-O 결합 에너지가 $460\,\text{kJ/mol}$에 달해 화학 라디칼만으로는 절대 깎이지 않습니다. 
              강력한 수백 V 이상의 이온이 때려 박아야 결합이 깨지는 <strong>'물리적 스퍼터링 + 화학 반응(Rブラシ)'</strong> 메커니즘이 필수입니다.
              <br>• 특히 3D V-NAND에서 100단~300단 높이(수십 $\mu\text{m}$)의 채널 홀을 수직으로 파고 내려가는 **HARC(High Aspect Ratio Contact) 식각**에서는 바닥까지 이온을 수직으로 총알처럼 꽂아 넣어야 하므로 **강한 고에너지 시스를 형성하는 CCP 장비가 절대적인 주력**입니다.
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ■ ICP의 텃밭: 실리콘/도체/금속 식각 (Conductor & Metal Etch)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              • 폴리실리콘(Poly-Si) 게이트, 텅스텐(W), 금속 배선, 실리콘 기판(STI 트렌치)을 깎을 때는 결합 에너지가 상대적으로 낮고 식각 속도보다 **하부의 수 나노미터 두께 게이트 산화막(Gate Dielectric)을 건드리지 않는 선택비(Selectivity)**가 생명입니다.
              <br>• CCP처럼 센 충격으로 때리면 게이트 산화막이 뚫려 칩 전체가 쇼트 납니다. 따라서 **저에너지 이온을 쓰면서도 고밀도 라디칼로 빠르게 깎고, 초저압($1\sim 10\,\text{mTorr}$)에서 가스 분자 산란 없이 수직 벽면을 정밀하게 형성하는 ICP 장비가 절대 표준**입니다.
            </p>
          </div>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 96 topics (q-96 down to q-01) by +1
    for old_n in range(96, 0, -1):
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

    # Step 4: Update header description to 97 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 'CCP와 ICP 플라즈마의 본질적 차이(Q01)'가 위치하며, 총 97개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 CCP vs ICP topic!")
