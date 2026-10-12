# -*- coding: utf-8 -*-
"""
insert_sheath_creation_q01.py
사용자 질문:
"그럼 쉬스영역이생기는건 플라즈마생성과정중하나인거지"

기존 100개 질문을 Q02~Q101로 시프트하고, 최상단 Q01에 신규 등록 (총 101개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (플라즈마 경계 물리 · 쉬스(Sheath)는 플라즈마 생성 과정일까? 경계층 형성과 자속 순환의 인과관계)",
    "title": "쉬스(Sheath) 영역이 생기는 것은 플라즈마 생성 과정 중 하나일까? (인과관계, 벽면 경계층의 본질, 연속 유지의 필수 루프)",
    "nav_title": "쉬스 형성은 플라즈마 생성 과정 중 하나일까?",
    "summary": [
        "<strong>1. 인과관계의 정확한 정리: '결과물'이자 '지속적 생성의 필수 엔진'입니다!</strong>: 엄밀한 발생 순서로 보면 쉬스(Sheath)는 플라즈마를 만들기 위한 사전 단계가 아니라, 기체가 이온화되어 플라즈마가 형성된 직후 <strong>'플라즈마가 고체 벽면(전극)과 만났을 때 전자의 빠른 속도($v_e \\gg v_i$) 때문에 필연적으로 생겨나는 경계층(Boundary Layer)'</strong>입니다.",
        "<strong>2. 하지만 '플라즈마를 계속 유지하고 재생산하는 과정'에는 핵심 단계가 맞습니다!</strong>: 일단 점화되어 쉬스가 생긴 이후부터는, 쉬스의 가파른 전압 강하가 양이온을 가속하고 2차 전자를 뽑아내어 새로운 플라즈마를 끊임없이 만들어내므로(타운센드 연쇄 충돌 전리), <strong>'플라즈마 자속 방전(생성 순환) 사이클의 절대적인 핵심 단계'</strong>로 작동합니다.",
        "<strong>3. 플라즈마의 자기방어막 (전자를 가두는 전위 장벽)</strong>: 쉬스가 없다면 가벼운 전자들이 벽으로 전부 빠져나가 플라즈마가 1초도 안 되어 꺼집니다. 전자가 빠져나간 자리에 양이온 껍질(쉬스)이 형성되어 음(-)의 전위 장벽을 세움으로써 <strong>나머지 전자들의 탈출을 억제하고 플라즈마 내부의 준중성($n_e \\approx n_i$)을 지켜내는 물리적 방어벽</strong>입니다.",
        "<strong>4. 쉬스 형성의 시계열 3단계</strong>: ① <strong>초기 점화(Ignition)</strong>: 강한 전계로 극소수 전자가 기체를 때려 초기 플라즈마 생성 ➔ ② <strong>쉬스 탄생</strong>: 전자의 빠른 속도로 벽면 흡수 및 양이온 공간전하층 형성 ➔ ③ <strong>연속 재생산</strong>: 쉬스 전압강하로 이온 가속 ➔ 2차 전자 방출 ➔ 새로운 플라즈마 무한 연속 생성."
    ],
    "svg_title": "📊 [쉬스(Sheath) 형성의 물리적 인과관계 및 플라즈마 자속 순환 다이어그램] (A) 플라즈마 접촉과 쉬스 경계층 탄생 | (B) 쉬스의 2대 역할 (전자 감금 장벽 vs 이온 가속기) | (C) 시계열 생성·유지 순환 사이클",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Cause & Effect (Why Sheath forms) -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 쉬스 형성의 인과관계 (원인 ➔ 결과)</text>

    <!-- Step visual -->
    <g transform="translate(15, 38)">
      <rect width="270" height="205" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 플라즈마가 벽과 만나는 순간</text>

      <!-- Plasma bulk -->
      <rect x="20" y="32" width="230" height="65" fill="#0284c7" opacity="0.3" stroke="#38bdf8" stroke-dasharray="2,2"/>
      <text x="28" y="48" fill="#38bdf8" font-size="7.5" font-weight="800">1) 플라즈마 형성 (이온과 전자의 바다)</text>
      <text x="28" y="62" fill="#cbd5e1" font-size="6.8">• 전자 속도: v_e = (8kT_e/πm_e)¹/² ≈ 10⁶ m/s (초고속)</text>
      <text x="28" y="74" fill="#cbd5e1" font-size="6.8">• 이온 속도: v_i = (8kT_i/πm_i)¹/² ≈ 10³ m/s (느림)</text>
      <text x="28" y="88" fill="#f87171" font-size="7.2" font-weight="800">➔ 전자가 이온보다 1,000배 빠르게 벽으로 탈출!</text>

      <!-- Fast electron escaping -->
      <path d="M 80 97 L 80 135" stroke="#f43f5e" stroke-width="2" marker-end="url(#arrowRedSh)"/>
      <path d="M 190 97 L 190 135" stroke="#f43f5e" stroke-width="2" marker-end="url(#arrowRedSh)"/>
      <text x="100" y="115" fill="#f87171" font-size="7" font-weight="800">전자 대량 탈출 (벽 흡수)</text>

      <!-- Sheath forms in between -->
      <rect x="20" y="138" width="230" height="42" fill="#f43f5e" opacity="0.25"/>
      <text x="28" y="152" fill="#fca5a5" font-size="7.5" font-weight="800">2) 쉬스(Sheath) 탄생 : 무거운 이온만 남음</text>
      <text x="28" y="166" fill="#cbd5e1" font-size="6.8">• 벽면 바로 앞에 양(+)의 공간전하층 형성</text>
      <text x="28" y="176" fill="#fde047" font-size="7" font-weight="800">➔ 플라즈마가 벽과 만났을 때 생기는 '경계층'!</text>

      <!-- Wall -->
      <rect x="20" y="180" width="230" height="15" fill="#475569" stroke="#64748b"/>
      <text x="80" y="191" fill="#fff" font-size="7.5" font-weight="800">챔버 벽면 / 전극 표면</text>
    </g>

    <!-- Physical Explanation -->
    <g transform="translate(15, 252)">
      <rect width="270" height="153" rx="5" fill="#0b1329" stroke="#38bdf8"/>
      <text x="12" y="18" fill="#38bdf8" font-size="8.8" font-weight="800">💡 결론: 쉬스는 무엇인가?</text>
      <text x="12" y="34" fill="#cbd5e1" font-size="7.5">• <strong>순서상</strong>: 플라즈마가 생겨서 쉬스가 생긴 것!</text>
      <text x="12" y="48" fill="#cbd5e1" font-size="7.5">• <strong>비유</strong>: 물을 컵에 담았을 때 컵 벽면에 표면장력으로</text>
      <text x="18" y="60" fill="#cbd5e1" font-size="7.2">생기는 '메니스커스(경계면)'와 같습니다.</text>
      <text x="12" y="78" fill="#fde047" font-size="7.8" font-weight="800">• <strong>우주 공간의 플라즈마는?</strong></text>
      <text x="18" y="91" fill="#cbd5e1" font-size="7.2">벽면이 없는 태양이나 오로라는 쉬스가 없습니다!</text>
      <text x="18" y="104" fill="#a7f3d0" font-size="7.2">오직 <strong>'진공 챔버라는 그릇에 담길 때만'</strong> 쉬스가 생깁니다.</text>
      <text x="12" y="122" fill="#34d399" font-size="7.5" font-weight="800">➔ 즉, 쉬스는 '플라즈마의 벽면 경계층'입니다!</text>
      <text x="12" y="138" fill="#94a3b8" font-size="6.8">• 하지만 인공 챔버에서는 이 쉬스가 '연속 생성 엔진'이 됨!</text>
    </g>
  </g>

  <!-- PANEL B: Dual Role of Sheath -->
  <g transform="translate(335, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 쉬스의 2대 역할 (방어벽 vs 가속기)</text>

    <!-- Role 1: Electron Confinement Barrier -->
    <g transform="translate(15, 38)">
      <rect width="280" height="98" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="16" fill="#38bdf8" font-size="8.2" font-weight="800">역할 1. 전자의 탈출을 막는 '음전위 방어벽'</text>
      <text x="10" y="32" fill="#cbd5e1" font-size="7.2">• 전자가 계속 빠져나가면 플라즈마는 1ms 만에 소멸</text>
      <text x="10" y="46" fill="#cbd5e1" font-size="7.2">• 쉬스에 형성된 강한 전압 강하(음전위 장벽)가</text>
      <text x="16" y="58" fill="#34d399" font-size="7.5" font-weight="800">남은 전자들을 플라즈마 벌크 안으로 밀어 넣어 가둠!</text>
      <text x="10" y="74" fill="#fde047" font-size="7.5" font-weight="800">➔ 플라즈마 내부를 '전기적 중성(준중성)'으로 지켜냄</text>
      <text x="10" y="88" fill="#94a3b8" font-size="6.8">• 플라즈마의 생명 유지 장치 (Self-confinement)</text>
    </g>

    <!-- Role 2: Ion Accelerator for Secondary Electrons -->
    <g transform="translate(15, 144)">
      <rect width="280" height="105" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="16" fill="#f87171" font-size="8.2" font-weight="800">역할 2. 새로운 플라즈마를 만드는 '이온 가속기'</text>
      <text x="10" y="32" fill="#cbd5e1" font-size="7.2">• 질문자님이 정확히 짚어주신 바로 그 기능!</text>
      <text x="10" y="46" fill="#cbd5e1" font-size="7.2">• 쉬스의 전압 강하가 양이온을 음극으로 강타시킴</text>
      <text x="10" y="60" fill="#fca5a5" font-size="7.2">• <strong>이온 충돌 ➔ 2차 전자 방출 ➔ 기체 충돌 전리</strong></text>
      <text x="10" y="76" fill="#fde047" font-size="7.5" font-weight="800">➔ 꺼져가는 플라즈마에 계속 새 전자를 공급하는 엔진!</text>
      <text x="10" y="92" fill="#a7f3d0" font-size="7.2">• 쉬스가 없으면 새로운 이온화가 일어나지 않아 꺼짐!</text>
    </g>

    <!-- Summary Box -->
    <g transform="translate(15, 257)">
      <rect width="280" height="148" rx="5" fill="#0b1329" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="8.8" font-weight="800">질문자님의 생각이 맞다고 볼 수 있는 이유</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="7.5">• <strong>"쉬스가 생겨야 비로소 플라즈마가 계속 생성된다"</strong></text>
      <text x="18" y="49" fill="#cbd5e1" font-size="7.2">라는 관점에서는 <strong>'생성 및 유지 과정의 핵심 부품'</strong>이 맞습니다!</text>
      <text x="12" y="66" fill="#fde047" font-size="7.8" font-weight="800">• 1회성 생성이 아닌, '지속적 재생산(자속 방전)'을 위해서는</text>
      <text x="18" y="79" fill="#cbd5e1" font-size="7.2">쉬스의 형성이 없이는 불가능하기 때문입니다.</text>
      <text x="12" y="97" fill="#38bdf8" font-size="7.5" font-weight="800">• 결론: 쉬스는</text>
      <text x="18" y="110" fill="#a7f3d0" font-size="7.2">① 플라즈마가 벽과 만났을 때 생기는 <strong>경계층</strong>이자,</text>
      <text x="18" y="123" fill="#fde047" font-size="7.2">② 플라즈마를 연속 생성시키는 <strong>재생산 발전기</strong>입니다!</text>
    </g>
  </g>

  <!-- PANEL C: Complete Timeline Flow -->
  <g transform="translate(660, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="12" font-weight="800">■ (C) 플라즈마 생성·유지 타임라인</text>

    <!-- Timeline Steps -->
    <g transform="translate(15, 38)">
      <rect width="270" height="255" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">발생 순서로 보는 3단계 시계열</text>

      <!-- Stage 1 -->
      <g transform="translate(10, 26)">
        <rect width="250" height="60" rx="4" fill="#0b1329" stroke="#38bdf8"/>
        <text x="8" y="14" fill="#38bdf8" font-size="7.8" font-weight="800">1단계: 초기 점화 (Breakdown &amp; Ignition)</text>
        <text x="14" y="28" fill="#cbd5e1" font-size="7">• 외부 강전계로 우주선/잔류 전자 가속</text>
        <text x="14" y="42" fill="#cbd5e1" font-size="7">• 중성 기체 1차 충돌 ➔ 극소수 플라즈마 생성</text>
        <text x="14" y="54" fill="#94a3b8" font-size="6.8">(아직 쉬스는 형성되지 않은 순간! t = 0~수 ns)</text>
      </g>

      <!-- Stage 2 -->
      <g transform="translate(10, 94)">
        <rect width="250" height="64" rx="4" fill="#0b1329" stroke="#f59e0b"/>
        <text x="8" y="14" fill="#fbbf24" font-size="7.8" font-weight="800">2단계: 쉬스(Sheath) 탄생 (경계층 형성)</text>
        <text x="14" y="28" fill="#cbd5e1" font-size="7">• 가벼운 전자가 벽면으로 쏟아져 빠져나감</text>
        <text x="14" y="42" fill="#fca5a5" font-size="7">• 벽 앞에 양이온 공간전하 쉬스 형성</text>
        <text x="14" y="56" fill="#fde047" font-size="7.2" font-weight="800">➔ 급격한 전위 강하(V_sheath) 자동 유도!</text>
      </g>

      <!-- Stage 3 -->
      <g transform="translate(10, 166)">
        <rect width="250" height="78" rx="4" fill="#0b1329" stroke="#10b981"/>
        <text x="8" y="14" fill="#34d399" font-size="7.8" font-weight="800">3단계: 연속 재생산 가동 (자속 방전 유지)</text>
        <text x="14" y="28" fill="#cbd5e1" font-size="7">• 쉬스 전압강하로 이온 가속 ➔ 음극 충돌</text>
        <text x="14" y="42" fill="#cbd5e1" font-size="7">• 2차 전자 방출 ➔ 시스 재가속 ➔ 충돌 전리 눈사태</text>
        <text x="14" y="56" fill="#34d399" font-size="7.5" font-weight="800">➔ 플라즈마가 꺼지지 않고 무한히 지속 생성됨!</text>
        <text x="14" y="70" fill="#a7f3d0" font-size="6.8">(반도체 에칭과 스퍼터링이 작동하는 정상 상태)</text>
      </g>
    </g>

    <!-- Bottom takeaway -->
    <g transform="translate(15, 302)">
      <rect width="270" height="103" rx="6" fill="#0b1329" stroke="#f59e0b"/>
      <text x="12" y="16" fill="#fbbf24" font-size="8.8" font-weight="800">🎯 최종 판정 가이드</text>
      <text x="12" y="32" fill="#cbd5e1" font-size="7.2">• "쉬스는 플라즈마 생성 과정인가요?"</text>
      <text x="12" y="46" fill="#34d399" font-size="7.5" font-weight="800">➔ "플라즈마가 '연속해서 유지·생성되는 순환 과정'</text>
      <text x="12" y="58" fill="#34d399" font-size="7.5" font-weight="800">    의 필수 핵심 메커니즘이 맞습니다!"</text>
      <text x="12" y="74" fill="#cbd5e1" font-size="7.2">• 엄밀히는 '플라즈마의 벽면 경계층'이지만, 챔버에서는</text>
      <text x="12" y="86" fill="#fde047" font-size="7.2">쉬스가 없으면 지속 생성이 불가능하기 때문입니다.</text>
    </g>
  </g>

  <!-- Markers -->
  <defs>
    <marker id="arrowRedSh" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#f43f5e" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- SECTION 1: Exact Cause and Effect -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 질문자님의 의문에 대한 명쾌한 답변: 인과관계와 기능의 구분
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            질문자님의 질문인 <strong>"그럼 쉬스 영역이 생기는 건 플라즈마 생성 과정 중 하나인 거지?"</strong>에 대해 결론부터 말씀드리면,
            <strong>"네, 플라즈마가 꺼지지 않고 '계속 생성·유지되는 순환 과정(자속 방전)'의 관점에서는 핵심 단계가 100% 맞습니다!"</strong>
          </p>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            다만, 물리학적인 <strong>'발생 순서(인과관계)'</strong>와 <strong>'기능적 역할'</strong>을 나누어 보면 훨씬 더 깊고 정확한 이해가 완성됩니다:
          </p>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
            <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 18px; border-radius:0 8px 8px 0;">
              <h4 style="color:#38bdf8; font-size:0.95rem; font-weight:800; margin-bottom:6px;">
                ① 인과관계 관점: 플라즈마의 '결과물'
              </h4>
              <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
                플라즈마가 먼저 생겨야 ➔ 전자가 빠른 속도로 벽면으로 도망치고 ➔ 그 결과로 벽면 앞에 양이온만 남아 <strong>'쉬스(경계층)'라는 껍질이 부산물처럼 형성</strong>됩니다.
                (우주 공간처럼 벽이 없는 곳에서는 플라즈마는 있어도 쉬스는 없습니다.)
              </p>
            </div>
            <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 18px; border-radius:0 8px 8px 0;">
              <h4 style="color:#34d399; font-size:0.95rem; font-weight:800; margin-bottom:6px;">
                ② 자속 방전 관점: 플라즈마의 '연속 생성 엔진'
              </h4>
              <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
                하지만 반도체 챔버 안에서 플라즈마가 켜진 이후부터는, <strong>쉬스가 없으면 양이온 가속도, 2차 전자 방출도, 새로운 기체 전리도 불가능</strong>합니다.
                즉, <strong>'플라즈마를 연속해서 계속 만들어내는 발전기'</strong> 역할을 쉬스가 도맡게 됩니다!
              </p>
            </div>
          </div>
        </div>

        <!-- SECTION 2: Why Sheath is Essential for Plasma Survival -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fde047; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 쉬스(Sheath)가 없으면 왜 플라즈마가 1초도 못 살고 죽을까?
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            질문자님께서 생각하신 대로 "쉬스가 생성 과정의 핵심"이라고 부를 수밖에 없는 결정적인 이유는, <strong>쉬스가 플라즈마의 수명을 지키고 새로운 전자를 낳는 2가지 핵심 역할</strong>을 하기 때문입니다:
          </p>

          <div style="background:#0f172a; border-left:4px solid #facc15; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#facc15; font-size:1rem; font-weight:800; margin-bottom:6px;">
              역할 1: 전자의 무한 탈출을 막는 '음전위 감금 장벽'
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              전자는 질량이 너무 가벼워 상온에서도 초속 수백 km로 날아다닙니다. 만약 쉬스가 생기지 않는다면 모든 전자가 순식간에 금속 벽면에 닿아 흡수 소멸되고 플라즈마는 순식간에 꺼집니다.
              <br>하지만 전자가 초기에 빠져나가며 벽 앞에 양이온 공간전하층(쉬스)을 형성하는 순간, **플라즈마 벌크보다 벽면의 전위가 훨씬 낮아지는 '음(-)의 전위 장벽'**이 세워집니다.
              <br>이 장벽 때문에 에너지가 아주 큰 극소수 전자를 제외한 나머지 99%의 전자들은 벽으로 가지 못하고 **플라즈마 내부로 튕겨 돌아와 갇히게 되며, 플라즈마의 전기적 중성(준중성)이 유지**됩니다!
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:800; margin-bottom:6px;">
              역할 2: 새로운 플라즈마를 끊임없이 공급하는 '2차 전자 발전기'
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              전자를 가두는 동시에, 쉬스에 걸린 가파른 전압 강하($V_{sheath}$)는 무거운 양이온을 음극으로 강하게 때려 박습니다.
              <br>이 충격으로 음극 표면에서 튕겨 나온 **2차 전자(Secondary Electron)**가 다시 쉬스 전계를 타고 플라즈마 안으로 튀어 들어가며 새로운 기체 원자를 때려 **'새로운 양이온과 전자'를 지속적으로 복제·생성**해냅니다.
            </p>
          </div>
        </div>

        <!-- SECTION 3: Timeline Summary -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#c084fc; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 한눈에 보는 시간 순서 (Timeline)
          </h3>
          <div style="background:#1e293b; padding:16px 20px; border-radius:8px;">
            <ol style="color:#cbd5e1; font-size:0.92rem; line-height:1.85; padding-left:20px; margin:0;">
              <li><strong style="color:#38bdf8;">1단계 (점화 Ignition, t = 0)</strong>: 외부 RF 전압이 걸려 극소수의 씨앗 전자가 가속되며 중성 기체를 쳐서 최초의 플라즈마 생성 시작.</li>
              <li><strong style="color:#fde047;">2단계 (쉬스 형성, t = 수 ns)</strong>: 전자가 빛의 속도로 벽으로 도망치면서 벽면 바로 앞에 전자가 텅 빈 양이온 공간전하층(쉬스)이 생겨남. ➔ <strong>급격한 전압 강하 발생</strong>!</li>
              <li><strong style="color:#34d399;">3단계 (정상 상태 자속 방전, t > 수 μs)</strong>: 형성된 쉬스의 전압강하로 이온이 가속되고 2차 전자가 뿜어져 나와 **플라즈마를 영구히 연속 생성하는 순환 루프 완성**!</li>
            </ol>
          </div>
        </div>

        <!-- SECTION 4: Final Takeaway -->
        <div style="margin-top:24px; background:#0f172a; border-left:4px solid #f59e0b; padding:16px 20px; border-radius:0 8px 8px 0;">
          <h4 style="color:#fbbf24; font-size:1rem; font-weight:800; margin-bottom:6px;">
            💡 결론: 질문자님의 말씀이 정답인 이유
          </h4>
          <p style="color:#cbd5e1; font-size:0.92rem; line-height:1.75; margin:0;">
            따라서 질문자님께서 말씀하신 <strong>"쉬스 영역이 생기는 건 플라즈마 생성 과정 중 하나"</strong>라는 생각은, 
            <strong>"플라즈마가 꺼지지 않고 스스로 계속해서 새로운 전하를 생성하고 유지하는 '자속 방전 순환 체계'의 절대적인 필수 단계"</strong>라는 점에서 완벽히 타당하고 훌륭한 통찰입니다!
          </p>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 100 topics (q-100 down to q-01) by +1
    for old_n in range(100, 0, -1):
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

    # Step 4: Update header description to 101 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 '쉬스 형성은 플라즈마 생성 과정 중 하나일까?(Q01)'가 위치하며, 총 101개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Sheath Creation topic!")
