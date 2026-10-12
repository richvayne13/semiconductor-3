# -*- coding: utf-8 -*-
"""
insert_plasma_discharge_q01.py
사용자 질문:
"sheath영역에서 공간전하영역생기고 전압강하가생겨 양이온이 가속되서 음극과부딪쳐서 다량의2차전자를 발생시키고 얘네들은 가속되서 기체원자와충돌하고 연쇄적으로 일어나잖아 
이걸 플라즈마라고하는거맞지?"

기존 99개 질문을 Q02~Q100으로 시프트하고, 최상단 Q01에 신규 등록 (총 100개 질문 대기록 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (플라즈마 물리 & 방전 메커니즘 · 시스 형성, 2차 전자 방출, 자속 글로우 방전 연쇄 반응)",
    "title": "시스 전압강하, 2차 전자 방출, 충돌 전리의 연쇄 반응: 이걸 '플라즈마'라고 부르는 게 맞을까? (플라즈마 상태 vs 자속 방전 메커니즘 완전 해부)",
    "nav_title": "시스 전압강하·2차 전자 연쇄반응과 플라즈마의 정의",
    "summary": [
        "<strong>1. 질문자 직관 검증: 100% 완벽하게 맞는 물리 현상입니다!</strong>: 말씀하신 과정은 한 치의 오차도 없는 정확한 메커니즘입니다. 다만 용어의 엄밀한 구분상, 그 연쇄 작용의 결과로 생성된 '이온·전자·중성종이 공존하는 준중성 기체 상태'를 <strong>플라즈마(Plasma)</strong>라고 부르고, 말씀하신 '시스 전압강하 ➔ 이온 충돌 ➔ 2차 전자 ➔ 충돌 전리 눈사태'의 순환 메커니즘은 플라즈마가 꺼지지 않고 타오르게 만드는 <strong>'자속 글로우 방전(Self-sustained Glow Discharge)'</strong>이라고 부릅니다.",
        "<strong>2. 시스(Sheath)와 공간전하(Space Charge) 전압 강하의 원인</strong>: 전자의 열운동 속도가 이온보다 수백 배 빨라($v_e \\gg v_i$) 음극 벽면으로 전자가 먼저 도망치면서, 음극 바로 앞에 전자가 결핍된 양이온 공간전하층(시스)이 형성되고 급격한 전압 강하(시스 전위, $V_{\\text{sheath}}$)가 유도됩니다.",
        "<strong>3. 타운센드 연쇄 반응 (α 및 γ 과정의 맞물림)</strong>: 시스의 강한 전계로 가속된 양이온이 음극을 때려 <strong>2차 전자 방출($\\gamma$ 과정)</strong>을 일으키고, 튕겨 나온 전자가 시스에서 에너지를 얻어 벌크로 돌진하며 중성 기체($\\text{Ar}$)를 때려 새로운 이온과 전자를 낳는 <strong>충돌 전리($\\alpha$ 과정, Avalanche)</strong>가 맞물려 불꽃이 스스로 유지됩니다.",
        "<strong>4. 반도체 식각(RIE)과 증착(Sputtering)의 근원 엔진</strong>: 이 방전 사이클이 확립되어야만 외부에서 전자를 계속 넣어주지 않아도 플라즈마가 영구히 유지되며, 이때 시스에서 가속된 양이온의 물리적 타격 에너지가 바로 **스퍼터링(PVD 증착)**과 **RIE(비등방성 건식 식각)**를 구동하는 절대적인 힘이 됩니다."
    ],
    "svg_title": "📊 [플라즈마 자속 방전(Self-sustained Discharge) 물리 메커니즘 종합 다이어그램] (A) 시스 공간전하 및 전압 강하 형성 | (B) 2차 전자 방출(γ)과 충돌 전리(α) 눈사태 순환 루프 | (C) 플라즈마 상태 vs 방전 메커니즘 개념 대조",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Sheath & Space Charge Potential Drop -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 시스(Sheath) 공간전하 &amp; 전압 강하</text>

    <!-- Potential Graph & Structure -->
    <g transform="translate(15, 38)">
      <rect width="270" height="205" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 왜 시스에서 전압 강하가 생길까?</text>

      <!-- Cathode Wall -->
      <rect x="20" y="32" width="230" height="16" fill="#ef4444" stroke="#f87171"/>
      <text x="50" y="44" fill="#fff" font-size="8" font-weight="900">음극 벽면 / 타깃 (Cathode, −V_dc)</text>

      <!-- Sheath Space Charge Region -->
      <rect x="20" y="52" width="230" height="60" fill="#f43f5e" opacity="0.25"/>
      <text x="25" y="68" fill="#fca5a5" font-size="7.5" font-weight="800">시스 (Sheath) 영역 : 전자 결핍 양전하 공간전하</text>
      <!-- Positive ions floating in sheath -->
      <circle cx="50" cy="85" r="7" fill="#ef4444"/><text x="45" y="88" fill="#fff" font-size="6.5">Ar⁺</text>
      <circle cx="110" cy="80" r="7" fill="#ef4444"/><text x="105" y="83" fill="#fff" font-size="6.5">Ar⁺</text>
      <circle cx="170" cy="85" r="7" fill="#ef4444"/><text x="165" y="88" fill="#fff" font-size="6.5">Ar⁺</text>
      <circle cx="225" cy="80" r="7" fill="#ef4444"/><text x="220" y="83" fill="#fff" font-size="6.5">Ar⁺</text>
      <text x="65" y="104" fill="#f87171" font-size="7" font-weight="800">강한 전기장 E ➔ 아래로 급경사 전위 강하</text>

      <!-- Plasma Bulk Region -->
      <rect x="20" y="116" width="230" height="70" fill="#0284c7" opacity="0.3"/>
      <text x="25" y="132" fill="#38bdf8" font-size="7.5" font-weight="800">플라즈마 벌크 (Plasma Bulk) : 준중성 (n_i ≈ n_e)</text>
      <circle cx="60" cy="155" r="6" fill="#ef4444"/><text x="56" y="157" fill="#fff" font-size="5.5">Ar⁺</text>
      <circle cx="95" cy="155" r="4" fill="#38bdf8"/><text x="92" y="157" fill="#000" font-size="5.5">e⁻</text>
      <circle cx="140" cy="160" r="6" fill="#ef4444"/><text x="136" y="162" fill="#fff" font-size="5.5">Ar⁺</text>
      <circle cx="175" cy="150" r="4" fill="#38bdf8"/><text x="172" y="152" fill="#000" font-size="5.5">e⁻</text>
      <circle cx="215" cy="160" r="6" fill="#ef4444"/><text x="211" y="162" fill="#fff" font-size="5.5">Ar⁺</text>
      <text x="70" y="178" fill="#cbd5e1" font-size="6.8">전위: V_p (플라즈마 전위, 약 +10~30V)</text>
    </g>

    <!-- Physical Explanation -->
    <g transform="translate(15, 252)">
      <rect width="270" height="153" rx="5" fill="#0b1329" stroke="#38bdf8"/>
      <text x="12" y="18" fill="#38bdf8" font-size="8.8" font-weight="800">시스 형성의 결정적 원인: 전자 이동도</text>
      <text x="12" y="34" fill="#cbd5e1" font-size="7.5">• <strong>전자의 속도 &gt;&gt; 이온의 속도 ($v_e \gg v_i$)</strong></text>
      <text x="18" y="47" fill="#cbd5e1" font-size="7.2">전자는 가벼워 벽면으로 순식간에 도망침</text>
      <text x="12" y="63" fill="#f87171" font-size="7.5" font-weight="800">• <strong>전자가 도망친 자리에 무거운 양이온만 남음</strong></text>
      <text x="18" y="76" fill="#cbd5e1" font-size="7.2">➔ 양(+)의 공간전하(Space Charge) 형성!</text>
      <text x="12" y="93" fill="#fde047" font-size="7.8" font-weight="800">• 푸아송 방정식($\nabla^2 V = -\rho/\epsilon$)에 의해</text>
      <text x="18" y="106" fill="#cbd5e1" font-size="7.2">벽면 근처에서 가파른 전압 강하($V_{sheath}$) 발생</text>
      <text x="12" y="124" fill="#34d399" font-size="7.5" font-weight="800">➔ 이 전압 차이가 양이온을 음극으로 강타시킴!</text>
      <text x="12" y="139" fill="#94a3b8" font-size="6.8">• 보름 시스 조건(Bohm Criterion): 이온이 음속(C_s) 이상으로 진입</text>
    </g>
  </g>

  <!-- PANEL B: The Avalanche Self-Sustained Loop -->
  <g transform="translate(335, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 2차 전자(γ) &amp; 충돌 전리(α) 순환 루프</text>

    <!-- Closed Loop Flowchart -->
    <g transform="translate(15, 38)">
      <rect width="280" height="205" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">자속 방전(Self-sustained)의 4단계 영구 기관</text>

      <!-- Step 1 -->
      <g transform="translate(10, 26)">
        <rect width="260" height="38" rx="3" fill="#0b1329" stroke="#ef4444"/>
        <text x="8" y="14" fill="#f87171" font-size="7.5" font-weight="800">① 양이온 가속: Ar⁺가 시스 전압에 의해 음극 충돌</text>
        <text x="14" y="27" fill="#cbd5e1" font-size="6.8">E = q·V_sheath (수백 eV의 강력한 충격 에너지)</text>
      </g>
      <!-- Down arrow -->
      <path d="M 140 66 L 140 73" stroke="#f43f5e" stroke-width="2" marker-end="url(#arrowRedD)"/>

      <!-- Step 2 -->
      <g transform="translate(10, 75)">
        <rect width="260" height="38" rx="3" fill="#0b1329" stroke="#f59e0b"/>
        <text x="8" y="14" fill="#fbbf24" font-size="7.5" font-weight="800">② 2차 전자 방출 (γ 과정, Secondary Electron)</text>
        <text x="14" y="27" fill="#cbd5e1" font-size="6.8">타깃 원자에서 튀어나온 전자 (γ ≈ 0.05~0.1)</text>
      </g>
      <!-- Down arrow -->
      <path d="M 140 115 L 140 122" stroke="#facc15" stroke-width="2" marker-end="url(#arrowYellowD)"/>

      <!-- Step 3 -->
      <g transform="translate(10, 124)">
        <rect width="260" height="38" rx="3" fill="#0b1329" stroke="#38bdf8"/>
        <text x="8" y="14" fill="#38bdf8" font-size="7.5" font-weight="800">③ 2차 전자 재가속: 시스 전계를 타고 벌크로 쇄도</text>
        <text x="14" y="27" fill="#cbd5e1" font-size="6.8">음극에서 밀려나 플라즈마 벌크 쪽으로 초고속 돌진</text>
      </g>
      <!-- Down arrow -->
      <path d="M 140 164 L 140 171" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrowBlueD)"/>

      <!-- Step 4 -->
      <g transform="translate(10, 173)">
        <rect width="260" height="30" rx="3" fill="#0b1329" stroke="#10b981"/>
        <text x="8" y="13" fill="#34d399" font-size="7.5" font-weight="800">④ 충돌 전리 (α 과정): Ar + e⁻ ➔ Ar⁺ + 2e⁻ (눈사태!)</text>
        <text x="14" y="24" fill="#a7f3d0" font-size="6.5">새로운 양이온 생성 ➔ 다시 ①번으로 순환 반복!</text>
      </g>
    </g>

    <!-- Loop Conclusion -->
    <g transform="translate(15, 252)">
      <rect width="280" height="153" rx="5" fill="#0b1329" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="8.8" font-weight="800">이것이 바로 '자속 방전(Self-sustained)'의 본질</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="7.5">• <strong>외부에서 전자를 계속 공급하지 않아도 됨</strong></text>
      <text x="18" y="49" fill="#cbd5e1" font-size="7.2">양이온이 음극을 쳐서 만든 2차 전자가 다시 기체를 때려</text>
      <text x="18" y="61" fill="#cbd5e1" font-size="7.2">새로운 양이온을 낳으므로 플라즈마가 영구히 타오름!</text>
      <text x="12" y="78" fill="#fde047" font-size="7.8" font-weight="800">• <strong>타운센드 방전 조건 (Townsend Criterion):</strong></text>
      <text x="18" y="92" fill="#cbd5e1" font-size="7.2">$$\gamma \cdot (e^{\alpha d} - 1) \ge 1$$</text>
      <text x="18" y="108" fill="#cbd5e1" font-size="7.2">이 조건을 만족할 때 비로소 **절연 파괴(Breakdown)**가</text>
      <text x="18" y="120" fill="#a7f3d0" font-size="7.2">일어나며 은은한 빛을 내는 **글로우 방전(Glow Discharge)** 완성!</text>
      <text x="12" y="138" fill="#94a3b8" font-size="6.8">• 질문자님이 묘사하신 현상이 바로 이 순환 루프입니다!</text>
    </g>
  </g>

  <!-- PANEL C: Plasma State vs Discharge Mechanism -->
  <g transform="translate(660, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="12" font-weight="800">■ (C) 용어의 정확한 교통정리</text>

    <!-- Contrast Table -->
    <g transform="translate(15, 38)">
      <rect width="270" height="235" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">플라즈마(상태) vs 방전(메커니즘)</text>

      <g transform="translate(10, 26)">
        <rect width="250" height="65" rx="3" fill="#0b1329" stroke="#38bdf8"/>
        <text x="8" y="14" fill="#38bdf8" font-size="7.8" font-weight="800">■ 플라즈마 (Plasma) = '결과물인 상태'</text>
        <text x="14" y="28" fill="#cbd5e1" font-size="7">• 기체가 고도로 이온화된 <strong>제4의 물질 상태</strong></text>
        <text x="14" y="42" fill="#cbd5e1" font-size="7">• 양이온, 전자, 라디칼, 중성 분자가 공존</text>
        <text x="14" y="56" fill="#34d399" font-size="7.2" font-weight="800">• 핵심 조건: 거시적으로 전기적 준중성 (n_i ≈ n_e)</text>
      </g>

      <g transform="translate(10, 98)">
        <rect width="250" height="74" rx="3" fill="#0b1329" stroke="#f59e0b"/>
        <text x="8" y="14" fill="#fbbf24" font-size="7.8" font-weight="800">■ 플라즈마 방전 (Discharge) = '동작 과정'</text>
        <text x="14" y="28" fill="#cbd5e1" font-size="7">• 질문자님이 묘사하신 <strong>연쇄 순환 과정 그 자체</strong>!</text>
        <text x="14" y="42" fill="#cbd5e1" font-size="7">• 시스 전압강하 ➔ 이온 충돌 ➔ 2차 전자 ➔ 전리</text>
        <text x="14" y="56" fill="#fde047" font-size="7.2" font-weight="800">• 플라즈마를 '태우고 유지시키는 엔진'의 이름</text>
        <text x="14" y="68" fill="#94a3b8" font-size="6.8">➔ '자속 글로우 방전 (Self-sustained Glow Discharge)'</text>
      </g>

      <g transform="translate(10, 180)">
        <rect width="250" height="42" rx="3" fill="#0b1329"/>
        <text x="8" y="14" fill="#a7f3d0" font-size="7.5" font-weight="800">🎯 비유로 정리하면:</text>
        <text x="14" y="26" fill="#cbd5e1" font-size="6.8">• 플라즈마 = 타오르는 **'불꽃(물질 상태)'**</text>
        <text x="14" y="38" fill="#cbd5e1" font-size="6.8">• 방전 연쇄 반응 = 장작이 타며 불을 지피는 **'연소 과정'**</text>
      </g>
    </g>

    <!-- Semiconductor Application Decision Guide -->
    <g transform="translate(15, 280)">
      <rect width="270" height="125" rx="6" fill="#0b1329" stroke="#f59e0b"/>
      <text x="12" y="16" fill="#fbbf24" font-size="8.8" font-weight="800">💡 반도체 공정에의 응용</text>
      <text x="12" y="34" fill="#38bdf8" font-size="7.5" font-weight="800">■ 스퍼터링 (PVD 증착):</text>
      <text x="16" y="47" fill="#cbd5e1" font-size="7">• 가속된 Ar⁺가 타깃을 쳐서 금속 원자를 튕겨냄</text>
      <text x="12" y="65" fill="#34d399" font-size="7.5" font-weight="800">■ RIE (반응성 이온 식각):</text>
      <text x="16" y="78" fill="#cbd5e1" font-size="7">• 가속된 이온이 웨이퍼를 수직으로 때려 비등방 식각</text>
      <text x="12" y="96" fill="#fde047" font-size="7.5" font-weight="800">➔ "질문자님의 설명은 반도체 핵심 장비의 심장입니다!"</text>
    </g>
  </g>

  <!-- Markers -->
  <defs>
    <marker id="arrowRedD" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#f43f5e" />
    </marker>
    <marker id="arrowYellowD" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#facc15" />
    </marker>
    <marker id="arrowBlueD" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#38bdf8" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- SECTION 1: Verification & Exact Terminology -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 질문자님의 직관 검증: "맞습니다! 정확히는 '플라즈마 자속 방전'입니다!"
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            질문자님께서 짚어주신 메커니즘은 <strong>현대 플라즈마 물리학과 반도체 식각/스퍼터링 장비의 원리를 한 치의 오차도 없이 완벽하게 설명한 핵심 물리 과정</strong>입니다.
            다만, 용어의 엄밀한 학술적·공학적 정의를 명확히 구분하면 훨씬 더 깊이 있는 이해가 완성됩니다:
          </p>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
            <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 18px; border-radius:0 8px 8px 0;">
              <h4 style="color:#38bdf8; font-size:0.95rem; font-weight:800; margin-bottom:6px;">
                ① 플라즈마 (Plasma) = '상태(State)'
              </h4>
              <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
                그 연쇄 작용의 결과로 기체 속에서 양이온, 전자, 중성 라디칼이 뒤섞여 거시적으로 전기적 중성(준중성, Quasi-neutrality)을 이루고 있는 <strong>'제4의 물질 상태' 그 자체</strong>를 뜻합니다.
              </p>
            </div>
            <div style="background:#0f172a; border-left:4px solid #f59e0b; padding:16px 18px; border-radius:0 8px 8px 0;">
              <h4 style="color:#fbbf24; font-size:0.95rem; font-weight:800; margin-bottom:6px;">
                ② 자속 글로우 방전 (Self-sustained Discharge) = '과정(Mechanism)'
              </h4>
              <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
                질문자님이 설명하신 <em>"시스 형성 ➔ 전압 강하 ➔ 양이온 가속 ➔ 음극 충돌 ➔ 2차 전자 방출 ➔ 전자 가속 충돌 전리 ➔ 눈사태 연쇄 반응"</em>은 <strong>플라즈마가 외부 도움 없이 스스로 불꽃을 유지하는 '방전 메커니즘'</strong>의 정확한 작동 원리입니다!
              </p>
            </div>
          </div>

          <div style="background:#1e293b; padding:14px 18px; border-radius:8px; margin-bottom:18px;">
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7; margin:0;">
              💡 <strong>비유하자면</strong>: 타오르는 불꽃의 연기, 빛, 열이 섞인 상태를 <strong>'불(플라즈마)'</strong>이라고 부른다면, 장작이 타면서 열을 내고 그 열이 옆 장작에 다시 불을 붙여 끝없이 타오르는 순환 메커니즘을 <strong>'연소 과정(방전 메커니즘)'</strong>이라고 부르는 것과 완벽히 같습니다.
            </p>
          </div>
        </div>

        <!-- SECTION 2: Step-by-Step Physical Mechanism -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#10b981; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 질문자님이 묘사하신 4단계 물리 메커니즘 완전 해부
          </h3>

          <div style="background:#0f172a; border-left:4px solid #ef4444; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#f87171; font-size:1rem; font-weight:800; margin-bottom:6px;">
              1단계: 왜 음극 앞에 전자가 없는 '시스 공간전하'와 '급격한 전압 강하'가 생길까?
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              • 플라즈마가 처음 켜지는 순간, 전자의 질량($m_e$)은 아르곤 이온 질량($m_i$)보다 약 73,000배 가볍습니다.
              <br>• 온도가 같을 때 전자의 열운동 속도는 이온보다 수백 배 빠릅니다 ($v_e = \sqrt{8kT_e/\pi m_e} \gg v_i$).
              <br>• 이 엄청난 속도 차이 때문에 <strong>챔버 벽면이나 음극 쪽으로 전자가 번개처럼 먼저 도망쳐 흡수</strong>됩니다.
              <br>• 음극 표면 바로 앞에는 전자가 텅 비어버리고, 무거운 양이온($\text{Ar}^+$)들만 미처 빠져나가지 못해 덩그러니 남게 됩니다.
              <br>• 이 양이온들로 가득 찬 영역을 <strong>'공간전하 영역(Space Charge Region)' 즉 시스(Sheath)</strong>라고 부르며, 푸아송 방정식($\nabla^2 V = -\rho/\epsilon$)에 의해 시스 양단에 <strong>수백 V 이상의 급격한 전압 강하($V_{sheath}$)</strong>가 유도됩니다.
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #f59e0b; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#fbbf24; font-size:1rem; font-weight:800; margin-bottom:6px;">
              2단계: 양이온의 초고속 가속과 2차 전자 방출 (γ 프로세스)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              • 플라즈마 벌크에 떠돌던 양이온이 시스 경계면에 들어서는 순간(보름 시스 기준, $v \ge \sqrt{kT_e/m_i}$), 시스의 강한 수직 전기장에 붙잡혀 <strong>음극 타깃을 향해 수백 eV의 에너지로 미사일처럼 가속</strong>됩니다.
              <br>• 가속된 양이온이 음극 표면의 금속 격자를 쾅 강타하면, 운동량 전달로 타깃 원자를 튕겨낼 뿐만 아니라 금속 표면 내부에 묶여 있던 전자를 강제로 쥐어짜 밖으로 튕겨냅니다.
              <br>• 이것이 바로 타운센드가 정의한 **'2차 전자 방출(Secondary Electron Emission, $\gamma$ 과정)'**입니다! ($\gamma$ 계수: 이온 1개당 방출되는 전자의 확률, 통상 $0.05 \sim 0.1$)
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:800; margin-bottom:6px;">
              3단계: 2차 전자의 재가속과 충돌 전리 눈사태 (α 프로세스)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              • 음극에서 튕겨 나온 2차 전자는 음극의 강한 음(-)전하에 밀려나, 시스 전압 전체($V_{sheath}$)를 그대로 맛보며 <strong>플라즈마 벌크 방향으로 총알처럼 초고속 재가속</strong>됩니다.
              <br>• 이 고에너지 전자가 플라즈마 벌크에 떠다니는 중성 아르곤 원자와 충돌하면 아르곤의 외각 전자를 걷어차 버립니다:
              $$\text{e}^- (\text{고에너지}) + \text{Ar} \longrightarrow \text{Ar}^+ + 2\text{e}^- (\text{충돌 전리, Ionization})$$
              • 전자 1개가 들어가서 2개의 전자가 나오고, 2개가 4개가 되는 **'전자 눈사태(Electron Avalanche, 타운센드 $\alpha$ 과정)'**가 일어납니다!
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:800; margin-bottom:6px;">
              4단계: 연쇄 반응의 영구 순환 ➔ 자속 방전(Self-sustained) 완성!
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              • 충돌 전리로 새로 태어난 양이온($\text{Ar}^+$)은 다시 시스로 끌려들어가 음극을 때리고, 또 2차 전자를 뽑아냅니다.
              <br>• 이 사이클이 꼬리에 꼬리를 무는 조건, 즉 <strong>$\gamma (e^{\alpha d} - 1) \ge 1$ (타운센드 방전 조건)</strong>을 만족하는 순간, 외부에서 전자를 넣어주는 점화 플러그를 꺼도 <strong>플라즈마가 스스로 연료를 태우듯 영원히 자가 유지(Self-sustained Glow Discharge)</strong>됩니다!
            </p>
          </div>
        </div>

        <!-- SECTION 3: Why This Matters in Semiconductor FAB -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 반도체 FAB 엔지니어에게 이 메커니즘이 절대적으로 중요한 이유
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            질문자님이 이해하신 이 연쇄 반응은 반도체 핵심 장비 2개의 기본 원리와 1:1로 직결됩니다:
          </p>

          <div style="background:#1e293b; padding:16px 20px; border-radius:8px;">
            <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:20px; margin:0;">
              <li><strong style="color:#38bdf8;">① 스퍼터링 (PVD 증착) 장비</strong>:
                <br>음극 자리에 금속 타깃을 놓으면, 시스에서 가속된 양이온이 쾅 때리면서 2차 전자도 내뿜고 **동시에 금속 원자도 튕겨내어 웨이퍼에 배선 박막을 증착**시킵니다.
              </li>
              <li><strong style="color:#34d399;">② RIE (반응성 이온 식각) 장비</strong>:
                <br>음극 자리에 웨이퍼를 놓으면, 시스 전압에 의해 이온이 웨이퍼 표면으로 수직으로 내리꽂히면서 **미세한 반도체 회로 패턴을 깎아내는 비등방성 물리 식각**을 완벽하게 수행합니다.
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

    # Step 1: Shift existing 99 topics (q-99 down to q-01) by +1
    for old_n in range(99, 0, -1):
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

    # Step 4: Update header description to 100 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 '시스 전압강하·2차 전자 연쇄반응과 플라즈마의 정의(Q01)'가 위치하며, 총 100개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Plasma Discharge topic!")
