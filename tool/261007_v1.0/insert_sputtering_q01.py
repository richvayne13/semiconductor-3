# -*- coding: utf-8 -*-
"""
insert_sputtering_q01.py
사용자 질문:
"sputtering이뭐야"

기존 98개 질문을 Q02~Q99로 시프트하고, 최상단 Q01에 신규 등록 (총 99개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (박막 증착 공학 & PVD · 스퍼터링(Sputtering)의 물리적 원리와 마그네트론 기술, 반도체 응용)",
    "title": "스퍼터링(Sputtering)이란 무엇인가? (PVD 물리적 원리, 당구공 충돌 모델, 마그네트론 스퍼터링, CVD/ALD 대비 장단점)",
    "nav_title": "스퍼터링(Sputtering)이란 무엇인가",
    "summary": [
        "<strong>1. 스퍼터링의 물리적 본질과 당구공 충돌 모델</strong>: 화학 반응을 거치지 않는 대표적인 <strong>물리적 기상 증착(PVD, Physical Vapor Deposition)</strong> 방식으로, 진공 챔버에 불활성 아르곤(Ar) 가스를 넣고 플라즈마를 띄운 뒤, 음극 타깃(Target)에 강한 음(-)의 전압을 걸어 가속된 $\\text{Ar}^+$ 이온이 타깃 원자를 당구공처럼 강타하여 튕겨내고(Momentum Transfer), 튕겨 나온 원자가 마주 보는 웨이퍼 표면에 증착되는 원리입니다.",
        "<strong>2. 스퍼터링 수율(Sputtering Yield, Y)의 핵심 변수</strong>: 입사된 $\\text{Ar}^+$ 이온 1개당 튕겨 나오는 타깃 원자의 개수를 의미하며, 입사 이온의 가속 에너지($V_{dc}$), 입사 각도, 타깃 원자 간의 표면 결합 에너지($U_s$), 그리고 충돌 이온과 타깃 원자의 질량비에 의해 결정됩니다.",
        "<strong>3. 마그네트론 스퍼터링(Magnetron Sputtering)의 혁신</strong>: 단순 DC 스퍼터링의 낮은 이온화율과 기판 열 손상을 극복하기 위해 타깃 배면에 영구자석(N-S)을 배치하여 로런츠 힘($\\vec{E} \\times \\vec{B}$)으로 전자를 타깃 표면에 나선형으로 가두어 주행 경로를 100배 이상 연장함으로써, 저압에서도 고밀도 플라즈마와 고속 증착을 구현한 반도체 양산 표준 기술입니다.",
        "<strong>4. CVD/ALD 대비 뚜렷한 장단점과 반도체 응용</strong>: 화학 전구체가 필요 없어 텅스텐(W), 탄탈럼(Ta) 등 고융점 금속이나 다원계 합금을 원래 조성비 그대로 저온 증착할 수 있고 접착력이 우수하지만, 입자의 직진성 때문에 고종횡비 트렌치에서의 단차 도포성(Step Coverage)이 취약합니다. 이에 따라 구리 전기도금용 시드층(Cu Seed Layer) 및 배리어 메탈(Ti/TiN, Ta/TaN) 형성에 주로 사용됩니다."
    ],
    "svg_title": "📊 [스퍼터링(Sputtering) 및 마그네트론 PVD 종합 메커니즘 다이어그램] (A) 원자 단위 당구공 충돌 물리 | (B) 마그네트론 스퍼터링 챔버 구조 | (C) 박막 증착 3대 방식(PVD vs CVD vs ALD) 비교",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Atomic Billiard Collision Mechanism -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 원자 단위 당구공 충돌 물리 메커니즘</text>

    <!-- Collision Schematic -->
    <g transform="translate(15, 38)">
      <rect width="270" height="200" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">운동량 전달 (Momentum Transfer)</text>

      <!-- Plasma Region -->
      <rect x="15" y="28" width="240" height="35" rx="3" fill="#0284c7" opacity="0.25"/>
      <text x="25" y="48" fill="#38bdf8" font-size="8" font-weight="800">Ar 플라즈마 영역 (Ar ➔ Ar⁺ + e⁻)</text>

      <!-- Fast Ar+ Ion rushing down -->
      <circle cx="80" cy="50" r="9" fill="#ef4444" stroke="#fca5a5" stroke-width="1.5"/>
      <text x="73" y="53" fill="#fff" font-size="7.5" font-weight="900">Ar⁺</text>
      <path d="M 80 62 L 110 115" stroke="#ef4444" stroke-width="2.5" marker-end="url(#arrowRedS)"/>
      <text x="95" y="82" fill="#f87171" font-size="7" font-weight="800">고속 가속 (수백 eV)</text>

      <!-- Target Surface & Collision Cascade -->
      <rect x="15" y="125" width="240" height="65" rx="3" fill="#334155" stroke="#64748b"/>
      <text x="25" y="140" fill="#cbd5e1" font-size="7.5" font-weight="800">음극 타깃 표면 (Target Lattice: Cu, Ti, Ta, W)</text>

      <!-- Target Atoms -->
      <circle cx="95" cy="155" r="7" fill="#64748b"/>
      <circle cx="115" cy="155" r="7" fill="#f59e0b" stroke="#fbbf24"/>
      <circle cx="135" cy="155" r="7" fill="#64748b"/>
      <circle cx="105" cy="172" r="7" fill="#64748b"/>
      <circle cx="125" cy="172" r="7" fill="#64748b"/>

      <!-- Sputtered target atoms knocked out -->
      <path d="M 115 148 L 160 85" stroke="#fbbf24" stroke-width="2" marker-end="url(#arrowYellowS)"/>
      <circle cx="165" cy="80" r="7" fill="#f59e0b" stroke="#fbbf24"/>
      <text x="145" y="70" fill="#fbbf24" font-size="7.2" font-weight="800">튀어나가는 타깃 원자</text>
      <text x="145" y="82" fill="#cbd5e1" font-size="6.8">(Sputtered Atoms, 1~10 eV)</text>
    </g>

    <!-- Key Parameters Box -->
    <g transform="translate(15, 248)">
      <rect width="270" height="157" rx="5" fill="#0b1329" stroke="#38bdf8"/>
      <text x="12" y="18" fill="#38bdf8" font-size="8.8" font-weight="800">스퍼터링 수율 (Sputtering Yield, Y)</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="7.5">• <strong>정의</strong>: Y = (튕겨나온 원자 수) / (입사한 Ar⁺ 이온 수)</text>
      <text x="12" y="52" fill="#fde047" font-size="7.8" font-weight="800">■ 수율을 결정짓는 4대 핵심 인자:</text>
      <text x="18" y="66" fill="#cbd5e1" font-size="7.2">① 입사 이온 에너지: 전압(V_dc) 높을수록 수율 증가</text>
      <text x="18" y="79" fill="#cbd5e1" font-size="7.2">② 입사 각도: 비스듬히(45°~60°) 칠 때 수율 극대화</text>
      <text x="18" y="92" fill="#cbd5e1" font-size="7.2">③ 원자 결합력(U_s): 타깃 원자 결합 셀수록 수율 저하</text>
      <text x="18" y="105" fill="#cbd5e1" font-size="7.2">④ 질량비(M_i / M_t): 질량이 비슷할수록 에너지 전달 최대</text>
      <text x="12" y="124" fill="#a7f3d0" font-size="7.5" font-weight="800">➔ 화학 반응(CVD)이 아닌 순수 운동에너지 전달의 승리!</text>
      <text x="12" y="139" fill="#94a3b8" font-size="7">• 당구에서 수구(흰공)가 목적구를 쳐서 밖으로 튕겨내는 원리</text>
    </g>
  </g>

  <!-- PANEL B: Magnetron Sputtering System -->
  <g transform="translate(335, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 마그네트론 스퍼터링 챔버 구조</text>

    <!-- Chamber Schematic -->
    <g transform="translate(15, 38)">
      <rect width="280" height="205" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">영구자석(N-S) 배치를 통한 전자 포획 (E × B)</text>

      <!-- Magnets behind target -->
      <rect x="40" y="28" width="40" height="15" fill="#ef4444" stroke="#f87171"/>
      <text x="53" y="40" fill="#fff" font-size="8" font-weight="900">N</text>
      <rect x="120" y="28" width="40" height="15" fill="#3b82f6" stroke="#60a5fa"/>
      <text x="134" y="40" fill="#fff" font-size="8" font-weight="900">S</text>
      <rect x="200" y="28" width="40" height="15" fill="#ef4444" stroke="#f87171"/>
      <text x="213" y="40" fill="#fff" font-size="8" font-weight="900">N</text>

      <!-- Cathode Target -->
      <rect x="25" y="47" width="230" height="16" rx="2" fill="#f59e0b" stroke="#fbbf24"/>
      <text x="65" y="59" fill="#000" font-size="8" font-weight="900">음극 타깃 (Cathode Target, −500V)</text>

      <!-- Magnetic field lines (curves) -->
      <path d="M 60 63 Q 90 92 140 63" stroke="#38bdf8" stroke-width="1.8" fill="none" stroke-dasharray="3,3"/>
      <path d="M 220 63 Q 190 92 140 63" stroke="#38bdf8" stroke-width="1.8" fill="none" stroke-dasharray="3,3"/>
      <text x="95" y="80" fill="#38bdf8" font-size="7" font-weight="800">자력선 B</text>

      <!-- High density plasma ring (E x B drift) -->
      <ellipse cx="90" cy="85" rx="24" ry="10" fill="#10b981" opacity="0.4" stroke="#34d399"/>
      <ellipse cx="190" cy="85" rx="24" ry="10" fill="#10b981" opacity="0.4" stroke="#34d399"/>
      <text x="45" y="103" fill="#34d399" font-size="7" font-weight="800">고밀도 전자 트랩 플라즈마 레이스로드</text>

      <!-- Downward Sputtered Flux -->
      <path d="M 70 108 L 70 150" stroke="#fde047" stroke-width="1.8" marker-end="url(#arrowYellowS)"/>
      <path d="M 140 108 L 140 150" stroke="#fde047" stroke-width="1.8" marker-end="url(#arrowYellowS)"/>
      <path d="M 210 108 L 210 150" stroke="#fde047" stroke-width="1.8" marker-end="url(#arrowYellowS)"/>
      <text x="85" y="132" fill="#fde047" font-size="7" font-weight="800">타깃 금속 원자 비행 플럭스</text>

      <!-- Anode Substrate / Wafer -->
      <rect x="45" y="155" width="190" height="12" rx="2" fill="#38bdf8"/>
      <text x="95" y="164" fill="#000" font-size="7.5" font-weight="900">웨이퍼 기판 (Anode / Ground)</text>
      <rect x="25" y="169" width="230" height="15" rx="2" fill="#475569" stroke="#64748b"/>
      <text x="85" y="180" fill="#cbd5e1" font-size="7.2" font-weight="800">하부 히터 / 척 (0V / Bias)</text>
      <text x="15" y="198" fill="#cbd5e1" font-size="6.8">Ar 가스 유입 (1~10 mTorr) + 터보 진공 배기계</text>
    </g>

    <!-- Magnetron Advantage Box -->
    <g transform="translate(15, 252)">
      <rect width="280" height="153" rx="5" fill="#0b1329" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="8.8" font-weight="800">마그네트론(Magnetron) 도입의 기적</text>
      <text x="12" y="34" fill="#cbd5e1" font-size="7.5">• <strong>전자의 주행거리 100배 연장</strong>: 로런츠 힘에 의해 전자가 타깃 표면 근처에서 나선형 나선 운동(Cycloid Motion)</text>
      <text x="12" y="52" fill="#fde047" font-size="7.8" font-weight="800">• <strong>Ar 가스 이온화율 대폭 폭증</strong> (0.1% ➔ 5~10%)</text>
      <text x="12" y="68" fill="#cbd5e1" font-size="7.2">• <strong>초저압(수 mTorr) 공정 실현</strong>: 공기 분자 산란 방지</text>
      <text x="12" y="82" fill="#38bdf8" font-size="7.5" font-weight="800">• <strong>웨이퍼 열 손상 원천 차단</strong>: 전자가 웨이퍼로 날아가지 않고 타깃 쪽에 묶여 기판 가열 방지</text>
      <text x="12" y="98" fill="#cbd5e1" font-size="7.2">• 고속 증착률(Deposition Rate) 확보로 반도체 양산 표준 등극</text>
      <text x="12" y="114" fill="#fca5a5" font-size="7">• 타깃 침식(Erosion) 편중(레이스로드 홈 파임)은 회전 자석으로 해결</text>
      <text x="12" y="130" fill="#94a3b8" font-size="7">• 변형: 고주파 RF 마그네트론(절연체용), 반응성(Reactive) 스퍼터링</text>
    </g>
  </g>

  <!-- PANEL C: Comparison with CVD & ALD -->
  <g transform="translate(660, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="12" font-weight="800">■ (C) 박막 증착 3대 방식 비교 &amp; 응용</text>

    <!-- Comparison Table -->
    <g transform="translate(15, 38)">
      <rect width="270" height="235" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">PVD(스퍼터링) vs CVD vs ALD 대결</text>

      <g transform="translate(10, 26)">
        <rect width="250" height="42" rx="3" fill="#0b1329"/>
        <text x="8" y="14" fill="#38bdf8" font-size="7.5" font-weight="800">1. 증착 메커니즘 &amp; 반응성:</text>
        <text x="14" y="26" fill="#cbd5e1" font-size="6.8">• PVD: 100% 물리적 충돌 (화학반응 X, 불순물 극소)</text>
        <text x="14" y="38" fill="#cbd5e1" font-size="6.8">• CVD/ALD: 기체 전구체 표면 화학 반응 (열/플라즈마)</text>
      </g>
      <g transform="translate(10, 74)">
        <rect width="250" height="42" rx="3" fill="#0b1329"/>
        <text x="8" y="14" fill="#f87171" font-size="7.5" font-weight="800">2. 단차 도포성 (Step Coverage):</text>
        <text x="14" y="26" fill="#fca5a5" font-size="6.8">• PVD: 불량 (직진성 탓에 트렌치 바닥/측벽 얇음)</text>
        <text x="14" y="38" fill="#34d399" font-size="6.8">• CVD: 우수  |  ALD: 100% 완벽 (Conformal)</text>
      </g>
      <g transform="translate(10, 122)">
        <rect width="250" height="42" rx="3" fill="#0b1329"/>
        <text x="8" y="14" fill="#34d399" font-size="7.5" font-weight="800">3. 재료 선택의 유연성 (최대 강점!):</text>
        <text x="14" y="26" fill="#34d399" font-size="6.8">• PVD: 고융점 금속(W, Ta, Ti), 다원계 합금 무제한 증착</text>
        <text x="14" y="38" fill="#cbd5e1" font-size="6.8">• CVD/ALD: 기화 가능한 전구체가 없으면 증착 불가</text>
      </g>
      <g transform="translate(10, 170)">
        <rect width="250" height="34" rx="3" fill="#0b1329"/>
        <text x="8" y="14" fill="#fbbf24" font-size="7.5" font-weight="800">4. 증착 속도 &amp; 기판 온도:</text>
        <text x="14" y="26" fill="#cbd5e1" font-size="6.8">PVD: 빠름 &amp; 상온 증착 가능  vs  ALD: 단원자층(느림)</text>
      </g>
      <g transform="translate(10, 210)">
        <rect width="250" height="20" rx="2" fill="#0b1329"/>
        <text x="8" y="14" fill="#a7f3d0" font-size="7" font-weight="800">5. 접착력 (Adhesion): PVD가 높은 입자에너지로 우수</text>
      </g>
    </g>

    <!-- Semiconductor Application Decision Guide -->
    <g transform="translate(15, 280)">
      <rect width="270" height="125" rx="6" fill="#0b1329" stroke="#f59e0b"/>
      <text x="12" y="16" fill="#fbbf24" font-size="8.8" font-weight="800">🎯 반도체 FAB 스퍼터링의 필수 역할</text>
      <text x="12" y="34" fill="#38bdf8" font-size="7.5" font-weight="800">■ 배선 공정 (BEOL Interconnect):</text>
      <text x="16" y="47" fill="#cbd5e1" font-size="7">• Cu 전기도금(ECD)을 위한 구리 시드층(Cu Seed) PVD</text>
      <text x="16" y="59" fill="#cbd5e1" font-size="7">• 구리 확산 방지용 Ta/TaN 배리어 메탈 증착</text>
      <text x="12" y="77" fill="#34d399" font-size="7.5" font-weight="800">■ 오믹 콘택트 &amp; 살리사이드 (FEOL Contact):</text>
      <text x="16" y="90" fill="#cbd5e1" font-size="7">• Ti/TiN 배리어 및 살리사이드(Co, Ni, Ti) 금속 증착</text>
      <text x="16" y="104" fill="#fde047" font-size="7.2" font-weight="800">➔ "금속 박막과 씨앗층을 심는 반도체의 영원한 기둥!"</text>
    </g>
  </g>

  <!-- Markers -->
  <defs>
    <marker id="arrowRedS" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#ef4444" />
    </marker>
    <marker id="arrowYellowS" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#f59e0b" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- SECTION 1: Fundamental Concept of Sputtering -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 스퍼터링(Sputtering)이란 무엇인가? (원자 단위 당구공 충돌 모델)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            스퍼터링(Sputtering)은 반도체 제조에서 금속 배선, 접촉층, 확산 방지막 등을 만들 때 가장 널리 쓰이는 <strong>대표적인 물리적 기상 증착(PVD, Physical Vapor Deposition) 기술</strong>입니다.
            화학 반응을 통해 박막을 합성하는 CVD나 ALD와 달리, 스퍼터링은 **'순수한 물리적 운동량 보존 법칙(Momentum Transfer)'**으로 막을 형성합니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:800; margin-bottom:6px;">
              당구공 충돌에 빗댄 스퍼터링 4단계 메커니즘
            </h4>
            <ol style="color:#cbd5e1; font-size:0.9rem; line-height:1.8; padding-left:20px; margin:0;">
              <li><strong>플라즈마 방전</strong>: 고진공 챔버에 불활성 기체인 아르곤($\text{Ar}$)을 주입하고 전압을 걸어 전자 충돌로 아르곤 양이온($\text{Ar}^+$)과 전자를 생성합니다.</li>
              <li><strong>고속 이온 가속</strong>: 증착하고자 하는 금속 덩어리인 <strong>타깃(Target, 음극 Cathode)</strong>에 $-500\sim -1,000\,\text{V}$의 강한 음의 전압을 인가합니다. 양전하를 띤 $\text{Ar}^+$ 이온이 강한 전기장에 이끌려 음극 타깃 표면으로 무서운 속도로 돌진합니다.</li>
              <li><strong>원자 충돌 연쇄 (Collision Cascade)</strong>: $\text{Ar}^+$ 이온이 타깃 표면의 원자 격자를 강타합니다. 마치 당구대에서 <strong>흰색 수구($\text{Ar}^+$)가 모여 있는 목적구(타깃 금속 원자)를 강하게 쳐서 흩어놓는 것처럼</strong>, 충돌 에너지가 타깃 내부 원자들 사이에 전달됩니다.</li>
              <li><strong>타깃 원자 방출 및 기판 증착</strong>: 입사 충격 에너지가 타깃 원자 표면의 결합 에너지($U_s$, 수 $\text{eV}$)를 넘어서면, 타깃 원자가 튕겨져 나와(Sputtered Atoms) 진공 공간을 날아가 마주 보고 있는 웨이퍼(Anode) 표면에 쌓여 균일한 박막을 형성합니다.</li>
            </ol>
          </div>
        </div>

        <!-- SECTION 2: Physics of Sputtering Yield -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fde047; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 스퍼터링 공정의 핵심 물리 지표: 스퍼터링 수율 (Sputtering Yield, Y)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            스퍼터링 공정의 속도와 효율을 지배하는 가장 핵심적인 파라미터는 <strong>스퍼터링 수율($Y$)</strong>입니다:
          </p>
          <div style="background:#1e293b; padding:16px 20px; border-radius:8px; margin-bottom:16px;">
            <p style="color:#fde047; font-size:1.05rem; font-weight:800; margin-bottom:8px;">
              $$Y = \frac{\text{튕겨져 나온 타깃 원자 수 (Ejected Atoms)}}{\text{입사된 } \text{Ar}^+ \text{ 이온 수 (Incident Ions)}}$$
            </p>
            <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
              통상적인 금속의 스퍼터링 수율은 $0.5 \sim 3.0$ 수준입니다. 즉, $\text{Ar}^+$ 이온 1개가 타깃을 칠 때 대략 1~3개의 금속 원자가 튕겨져 나옵니다.
            </p>
          </div>

          <div style="overflow-x:auto; margin-bottom:18px;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">영향 인자</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">물리적 거동 메커니즘</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">공정 엔지니어링 포인트</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">① 입사 이온 에너지 ($E_{ion}$)</td>
                  <td style="padding:10px 14px;">임계 에너지($E_{th} \sim 20\text{eV}$) 이하에서는 방출 불가. 수백 eV까지 $Y \propto \sqrt{E}$로 증가하나, 수 keV를 넘어가면 이온이 타깃 내부로 깊이 박혀(Ion Implantation) 오히려 수율 감소</td>
                  <td style="padding:10px 14px;">타깃 음극 전압($V_{dc}$)을 $300\sim 800\,\text{V}$ 최적 영역으로 설정</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">② 입사 각도 ($\theta$)</td>
                  <td style="padding:10px 14px;">수직 입사($0^\circ$)보다 비스듬히 입사할 때($45^\circ\sim 60^\circ$) 운동량이 표면 방향으로 굴절되어 수율 극대화</td>
                  <td style="padding:10px 14px;">타깃 침식 프로파일 형상과 플라즈마 시스 만곡 제어</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">③ 표면 결합 에너지 ($U_s$)</td>
                  <td style="padding:10px 14px;">타깃 재료의 승화열(Sublimation Energy)에 반비례 ($Y \propto 1/U_s$). 결합이 단단한 고융점 금속(W, Ta)은 수율이 낮고, Au, Ag, Cu는 수율 높음</td>
                  <td style="padding:10px 14px;">재료별 증착 속도(Deposition Rate) 보정 파워 설정</td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">④ 질량비 ($M_i / M_t$)</td>
                  <td style="padding:10px 14px;">충돌 이온과 타깃 원자의 질량이 비슷할 때 탄성 충돌 에너지 전달 계수($\gamma = \frac{4 M_1 M_2}{(M_1+M_2)^2}$)가 1에 가까워져 최대</td>
                  <td style="padding:10px 14px;">무거운 타깃(W 등) 증착 시 더 무거운 불활성 가스($\text{Kr, Xe}$) 사용 검토</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- SECTION 3: Magnetron Sputtering Revolution -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#10b981; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 마그네트론 스퍼터링 (Magnetron Sputtering): 양산화의 결정적 혁신
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            초기의 단순한 직류(DC) 스퍼터링은 아르곤 가스의 이온화율이 0.1% 미만에 불과하여 증착 속도가 너무 느렸고, 높은 전압으로 인해 전자가 웨이퍼를 직접 때려 <strong>기판 온도가 수백 도까지 치솟아 소자가 파괴되는 치명적 결함</strong>이 있었습니다. 
            이를 완벽히 해결한 기술이 바로 **마그네트론 스퍼터링(Magnetron Sputtering)**입니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:800; margin-bottom:6px;">
              로런츠 힘($\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})$)과 전자 트랩
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              • 타깃 바로 뒷면에 영구자석(중앙 N극, 외곽 S극)을 배치하면 타깃 표면에 아치형의 수평 자계($\vec{B}$)가 형성됩니다.
              <br>• 타깃에서 튕겨 나온 2차 전자는 수직 전기장($\vec{E}$)과 수평 자기장($\vec{B}$)이 직교하는 환경에서 **$\vec{E} \times \vec{B}$ 드리프트 운동**을 하며 타깃 표면 주위를 원형 궤도로 맴돌며(Cycloid Motion) 갇히게 됩니다.
              <br>• <strong>효과</strong>: 전자가 웨이퍼로 날아가지 않고 타깃 근처에서 수천 번 회전하며 아르곤 가스를 집중 타격하므로, **플라즈마 밀도가 10~100배 폭증**하고 **증착 속도가 비약적으로 향상**되며 **웨이퍼는 차가운 상태를 유지**합니다.
            </p>
          </div>
        </div>

        <!-- SECTION 4: Pros, Cons, and Semiconductor Applications -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. 스퍼터링의 장단점 및 반도체 FAB 핵심 응용처
          </h3>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
            <div style="background:#0f172a; border:1px solid #34d399; border-radius:8px; padding:16px;">
              <h4 style="color:#34d399; font-size:0.95rem; font-weight:800; margin-bottom:8px;">👍 스퍼터링의 독보적 강점</h4>
              <ul style="color:#cbd5e1; font-size:0.85rem; line-height:1.7; padding-left:16px; margin:0;">
                <li><strong>모든 금속/합금 증착 가능</strong>: 녹는점이 $3,000^\circ\text{C}$가 넘는 W, Ta, Mo나 다원계 합금(Al-0.5%Cu 등)도 타깃 조성비 그대로 증착 가능 (CVD 전구체 불필요)</li>
                <li><strong>우수한 박막 접착력(Adhesion)</strong>: 튕겨 나온 원자의 에너지가 $1\sim 10\,\text{eV}$로 열증착($0.1\,\text{eV}$)보다 10~100배 높아 기판 표면에 박히듯 결합</li>
                <li><strong>저온 공정</strong>: 웨이퍼 가열 없이 상온에서도 고품질 금속막 증착 가능 (BEOL 열예산 보존)</li>
              </ul>
            </div>
            <div style="background:#0f172a; border:1px solid #ef4444; border-radius:8px; padding:16px;">
              <h4 style="color:#f87171; font-size:0.95rem; font-weight:800; margin-bottom:8px;">👎 스퍼터링의 물리적 한계</h4>
              <ul style="color:#cbd5e1; font-size:0.85rem; line-height:1.7; padding-left:16px; margin:0;">
                <li><strong>단차 도포성(Step Coverage) 취약</strong>: 원자가 직선으로 날아오기 때문에 종횡비가 깊은 트렌치/비아 구멍의 측벽과 바닥에는 막이 거의 쌓이지 않는 섀도잉(Shadowing) 발생</li>
                <li><strong>타깃 소모 및 비용</strong>: 값비싼 고순도 금속 타깃이 중앙부만 도넛 모양으로 깎여(Erosion Track) 소모율 한계 존재</li>
              </ul>
            </div>
          </div>

          <div style="background:#1e293b; padding:16px 20px; border-radius:8px;">
            <h4 style="color:#38bdf8; font-size:0.95rem; font-weight:800; margin-bottom:6px;">
              💡 현대 반도체 FAB에서의 핵심 용도
            </h4>
            <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.75; margin:0;">
              • <strong>구리(Cu) 전기도금용 시드층 (Cu Seed Layer)</strong>: 절연막 트렌치에 전기도금을 하려면 전기가 통하는 얇은 구리막이 먼저 깔려 있어야 합니다. 이 구리 시드층을 까는 핵심 공정이 바로 PVD 스퍼터링입니다.<br>
              • <strong>확산 방지막 및 라이너 (Ta/TaN, Ti/TiN Barrier)</strong>: 구리가 실리콘으로 침투하는 것을 막는 배리어 메탈을 스퍼터링으로 초박막 형성합니다.<br>
              • <strong>오믹 콘택트 살리사이드(Salicide)</strong>: 소스/드레인 표면에 접촉 저항을 낮추기 위해 Ni, Co, Ti 금속을 스퍼터링 증착한 후 열처리하여 실리사이드를 형성합니다.
            </p>
          </div>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 98 topics (q-98 down to q-01) by +1
    for old_n in range(98, 0, -1):
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

    # Step 4: Update header description to 99 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 '스퍼터링이란 무엇인가(Q01)'가 위치하며, 총 99개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Sputtering topic!")
