# -*- coding: utf-8 -*-
"""
insert_permittivity_high_k_q01.py
사용자 질문:
"유전율이 뭐야 유전율이높다는게뭘뜻ㅎ"

대시보드 최상단 Q01로 신규 추가하고, 기존 89개 질문을 Q02~Q90으로 시프트 (총 90개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (전자기학 및 소자 기초 · 유전율의 본질과 High-k/Low-k 양대 축)",
    "title": "유전율(Permittivity, ε)이란 무엇인가? 유전율이 높다는 것의 물리적 의미와 반도체 응용",
    "nav_title": "유전율의 본질과 유전율이 높다는 것의 의미",
    "summary": [
        "<strong>1. 유전율(Permittivity, $\\epsilon$)의 본질적 물리 정의</strong>: '전기(電)를 유도(誘)하여 품는 정도'라는 뜻으로, 외부 전기장을 가했을 때 절연 물질 내부의 원자/분자가 <strong>'전기적 분극(Polarization, $P$)'을 일으켜 전기 에너지를 저장하고 외부 전기장을 완화(스크리닝)하는 능력</strong>의 척도입니다.",
        "<strong>2. 유전율이 높다는 것의 3대 물리적 본질</strong>: ① <strong>분극($P$)이 극도로 잘 일어남</strong> (전기적 충격을 흡수하는 스펀지 역할), ② <strong>같은 전압에서 전하를 끌어당겨 저장하는 능력(정전용량 $C = \\frac{\\epsilon A}{d}$)이 비례하여 폭증함</strong>, ③ <strong>전하들 사이의 쿨롱 인력/척력($F = \\frac{1}{4\\pi\\epsilon}\\frac{q_1 q_2}{r^2}$)을 대폭 약화시킴</strong> (전기력선 차폐).",
        "<strong>3. 반도체 게이트의 High-k 혁명 (FEOL)</strong>: 트랜지스터 게이트 절연막에는 유전율이 높은 소재(High-k, $\\text{HfO}_2, k \\approx 25$)를 씁니다. 물리적 두께($t_{phys}$)를 두껍게 유지하여 양자 터널링 누설전류를 원천 차단하면서도, 등가 산화막 두께($EOT = t_{phys} \\frac{k_{SiO2}}{k_{high-k}}$)를 1nm 이하로 줄여 게이트 정전용량($C_{ox}$)과 채널 장악력을 극대화합니다.",
        "<strong>4. 반도체 배선의 Low-k 정반대 전략 (BEOL)</strong>: 반대로 금속 배선 층간 절연막(IMD/ILD)에는 유전율이 가장 낮은 소재(Low-k, $\\text{SiCOH}, k < 2.5$)를 씁니다. 배선 간 기생 커패시턴스를 극소화하여 신호 지연($\\tau = RC$), 동적 소비 전력($P = C V^2 f$), 신호 간섭(Crosstalk)을 억제하기 위함입니다."
    ],
    "svg_title": "📊 [유전율의 본질과 반도체 응용 다이어그램] (A) 분극(Polarization) 메커니즘 | (B) 유전율이 높을 때의 3대 물리적 효과 | (C) High-k vs Low-k 반도체 양대 전략",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Polarization Mechanism Visualized -->
  <g transform="translate(20, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 유전율의 물리적 실체: 전기적 분극</text>

    <!-- Capacitor with Dielectric Diagram -->
    <g transform="translate(15, 42)">
      <rect width="280" height="235" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">평행판 사이의 유전체 분극 (Polarization)</text>

      <!-- Positive Plate -->
      <rect x="20" y="32" width="16" height="150" fill="#ef4444" rx="2"/>
      <text x="24" y="55" fill="#fff" font-size="10" font-weight="900">+</text>
      <text x="24" y="85" fill="#fff" font-size="10" font-weight="900">+</text>
      <text x="24" y="115" fill="#fff" font-size="10" font-weight="900">+</text>
      <text x="24" y="145" fill="#fff" font-size="10" font-weight="900">+</text>
      <text x="24" y="170" fill="#fff" font-size="10" font-weight="900">+</text>

      <!-- Negative Plate -->
      <rect x="244" y="32" width="16" height="150" fill="#3b82f6" rx="2"/>
      <text x="248" y="55" fill="#fff" font-size="12" font-weight="900">−</text>
      <text x="248" y="85" fill="#fff" font-size="12" font-weight="900">−</text>
      <text x="248" y="115" fill="#fff" font-size="12" font-weight="900">−</text>
      <text x="248" y="145" fill="#fff" font-size="12" font-weight="900">−</text>
      <text x="248" y="170" fill="#fff" font-size="12" font-weight="900">−</text>

      <!-- Dielectric Material inside -->
      <rect x="42" y="32" width="196" height="150" fill="#0369a1" opacity="0.3" stroke="#38bdf8" stroke-dasharray="2,2"/>
      <text x="95" y="46" fill="#7dd3fc" font-size="7.5" font-weight="800">유전체 (Dielectric, ε = k ε₀)</text>

      <!-- Dipoles aligned inside -->
      <!-- Row 1 -->
      <g transform="translate(55, 60)">
        <rect width="36" height="18" rx="8" fill="#1e293b" stroke="#f43f5e"/>
        <text x="6" y="13" fill="#38bdf8" font-size="8" font-weight="900">−</text>
        <text x="22" y="13" fill="#ef4444" font-size="8" font-weight="900">+</text>
      </g>
      <g transform="translate(105, 60)">
        <rect width="36" height="18" rx="8" fill="#1e293b" stroke="#f43f5e"/>
        <text x="6" y="13" fill="#38bdf8" font-size="8" font-weight="900">−</text>
        <text x="22" y="13" fill="#ef4444" font-size="8" font-weight="900">+</text>
      </g>
      <g transform="translate(155, 60)">
        <rect width="36" height="18" rx="8" fill="#1e293b" stroke="#f43f5e"/>
        <text x="6" y="13" fill="#38bdf8" font-size="8" font-weight="900">−</text>
        <text x="22" y="13" fill="#ef4444" font-size="8" font-weight="900">+</text>
      </g>

      <!-- Row 2 -->
      <g transform="translate(55, 95)">
        <rect width="36" height="18" rx="8" fill="#1e293b" stroke="#f43f5e"/>
        <text x="6" y="13" fill="#38bdf8" font-size="8" font-weight="900">−</text>
        <text x="22" y="13" fill="#ef4444" font-size="8" font-weight="900">+</text>
      </g>
      <g transform="translate(105, 95)">
        <rect width="36" height="18" rx="8" fill="#1e293b" stroke="#f43f5e"/>
        <text x="6" y="13" fill="#38bdf8" font-size="8" font-weight="900">−</text>
        <text x="22" y="13" fill="#ef4444" font-size="8" font-weight="900">+</text>
      </g>
      <g transform="translate(155, 95)">
        <rect width="36" height="18" rx="8" fill="#1e293b" stroke="#f43f5e"/>
        <text x="6" y="13" fill="#38bdf8" font-size="8" font-weight="900">−</text>
        <text x="22" y="13" fill="#ef4444" font-size="8" font-weight="900">+</text>
      </g>

      <!-- Row 3 -->
      <g transform="translate(55, 130)">
        <rect width="36" height="18" rx="8" fill="#1e293b" stroke="#f43f5e"/>
        <text x="6" y="13" fill="#38bdf8" font-size="8" font-weight="900">−</text>
        <text x="22" y="13" fill="#ef4444" font-size="8" font-weight="900">+</text>
      </g>
      <g transform="translate(105, 130)">
        <rect width="36" height="18" rx="8" fill="#1e293b" stroke="#f43f5e"/>
        <text x="6" y="13" fill="#38bdf8" font-size="8" font-weight="900">−</text>
        <text x="22" y="13" fill="#ef4444" font-size="8" font-weight="900">+</text>
      </g>
      <g transform="translate(155, 130)">
        <rect width="36" height="18" rx="8" fill="#1e293b" stroke="#f43f5e"/>
        <text x="6" y="13" fill="#38bdf8" font-size="8" font-weight="900">−</text>
        <text x="22" y="13" fill="#ef4444" font-size="8" font-weight="900">+</text>
      </g>

      <!-- Electric field arrows -->
      <line x1="45" y1="165" x2="235" y2="165" stroke="#ef4444" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="75" y="160" fill="#ef4444" font-size="7" font-weight="800">외부 전계 E₀ (우측 향함)</text>

      <line x1="205" y1="175" x2="75" y2="175" stroke="#38bdf8" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
      <text x="85" y="185" fill="#38bdf8" font-size="7" font-weight="800">유전체 반대 전계 E_ind (좌측 향함)</text>

      <!-- Bottom equation in diagram -->
      <text x="12" y="202" fill="#fde047" font-size="7.8" font-weight="800">★ 내부 실효 전계: E_net = E₀ - E_ind = E₀ / k</text>
      <text x="12" y="215" fill="#cbd5e1" font-size="7.2">• 외부 전계를 유전체가 반대 방향으로 버텨서 깎아줌!</text>
      <text x="12" y="226" fill="#a7f3d0" font-size="7.2">• 전속밀도 공식: D = ε₀ E + P = ε E</text>
    </g>

    <!-- Bottom summary box -->
    <rect x="15" y="295" width="280" height="112" rx="6" fill="#0b1329" stroke="#38bdf8"/>
    <text x="22" y="315" fill="#38bdf8" font-size="9" font-weight="800">💡 유전(誘電)의 한자적 본질:</text>
    <text x="22" y="333" fill="#cbd5e1" font-size="7.8">• <strong>유(誘, 꾈 유)</strong> + <strong>전(電, 번개 전)</strong> = '전기를 유도하여 품는다'</text>
    <text x="22" y="348" fill="#cbd5e1" font-size="7.8">• 전기가 통하는 도체(Conductor)가 아니라,</text>
    <text x="22" y="364" fill="#cbd5e1" font-size="7.8">• 전기가 안 통하면서 <strong>내부 분극으로 전하를 품는 절연체</strong>!</text>
    <text x="22" y="380" fill="#fde047" font-size="8" font-weight="800">➔ 유전율은 '전기적 에너지를 흡수·저장하는 스펀지의 성능'</text>
    <text x="22" y="396" fill="#a5f3fc" font-size="7.5">스펀지가 물을 많이 빨아들이듯, 유전율이 높으면 전하를 꽉 품습니다!</text>
  </g>

  <!-- PANEL B: 3 Physical Meanings of High Permittivity -->
  <g transform="translate(350, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 유전율이 높다는 것의 3대 물리적 의미</text>

    <!-- Meaning 1: Huge Polarization -->
    <g transform="translate(15, 42)">
      <rect width="280" height="112" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="10" y="16" fill="#38bdf8" font-size="8.8" font-weight="800">1. 분극(Polarization) 능력이 엄청나게 탁월하다!</text>
      <text x="10" y="32" fill="#cbd5e1" font-size="7.5">• 전기장을 가했을 때 원자핵과 전자가 강력하게 늘어남</text>
      <text x="10" y="46" fill="#cbd5e1" font-size="7.5">• 외부에서 가한 전계를 내부에서 반대 쌍극자로 강력히 차폐</text>

      <rect x="8" y="54" width="264" height="26" rx="3" fill="#0b1329" stroke="#334155"/>
      <text x="14" y="70" fill="#ffffff" font-size="7.8">P = (ε_r - 1) ε₀ E  (k가 클수록 분극 밀도 P 폭증!)</text>

      <text x="10" y="94" fill="#cbd5e1" font-size="7.5">• 전기적 충격을 내부에서 부드럽게 흡수해 주는</text>
      <text x="10" y="106" fill="#fde047" font-size="7.8" font-weight="800">➔ 최고의 '전기적 에어백 / 전계 쿠션' 역할을 수행함!</text>
    </g>

    <!-- Meaning 2: Charge Storage Capacity -->
    <g transform="translate(15, 162)">
      <rect width="280" height="116" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="10" y="16" fill="#fbbf24" font-size="8.8" font-weight="800">2. 전하 저장 능력(커패시턴스 C)이 폭발적으로 커진다!</text>
      <text x="10" y="32" fill="#cbd5e1" font-size="7.5">• 평행판 커패시터 공식: C = ε A / d = k ε₀ A / d</text>
      <text x="10" y="46" fill="#cbd5e1" font-size="7.5">• 유전율이 10배 높으면? ➔ 똑같은 면적/두께에서 용량 10배!</text>

      <rect x="8" y="54" width="264" height="26" rx="3" fill="#0b1329" stroke="#334155"/>
      <text x="14" y="70" fill="#ffffff" font-size="7.8">Q = C V = (k ε₀ A / d) V  (같은 전압에서 전하 Q 폭증!)</text>

      <text x="10" y="94" fill="#cbd5e1" font-size="7.5">• 유전체 표면의 반대전하가 전극 전하를 강하게 끌어당겨 구속</text>
      <text x="10" y="106" fill="#34d399" font-size="7.8" font-weight="800">➔ 같은 전압을 걸어도 엄청난 양의 전하를 저수지처럼 보관!</text>
    </g>

    <!-- Meaning 3: Coulomb Force Weakening -->
    <g transform="translate(15, 286)">
      <rect width="280" height="120" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="10" y="16" fill="#f87171" font-size="8.8" font-weight="800">3. 두 전하 사이의 쿨롱 힘(인력/척력)을 크게 약화시킨다!</text>
      <text x="10" y="32" fill="#cbd5e1" font-size="7.5">• 쿨롱의 법칙: F = (1 / 4πε) · (q₁ q₂ / r²)</text>
      <text x="10" y="46" fill="#cbd5e1" font-size="7.5">• 유전율(ε)이 분모에 있으므로, 힘이 1/k로 급감!</text>

      <rect x="8" y="54" width="264" height="28" rx="3" fill="#0b1329" stroke="#334155"/>
      <text x="14" y="72" fill="#fde047" font-size="7.5" font-weight="800">★ 대표 사례: 물(H₂O, k ≈ 80)이 소금을 녹이는 비결!</text>

      <text x="10" y="96" fill="#cbd5e1" font-size="7.2">• 진공 대비 Na⁺와 Cl⁻ 사이의 결합력이 1/80로 뚝 떨어짐</text>
      <text x="10" y="110" fill="#a5f3fc" font-size="7.5" font-weight="800">➔ 전하들이 서로를 덜 끌어당기고 자유롭게 해리됨!</text>
    </g>
  </g>

  <!-- PANEL C: High-k vs Low-k in Semiconductors -->
  <g transform="translate(680, 20)">
    <rect width="280" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) 반도체의 양대 전략: High-k vs Low-k</text>

    <!-- Strategy 1: High-k in Gate -->
    <g transform="translate(15, 42)">
      <rect width="250" height="165" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="10" y="16" fill="#38bdf8" font-size="8.8" font-weight="800">1. 게이트의 선택: High-k (고유전율)</text>
      <text x="10" y="30" fill="#cbd5e1" font-size="7.2">• 위치: 트랜지스터 게이트 절연막 (FEOL)</text>
      <text x="10" y="42" fill="#cbd5e1" font-size="7.2">• 소재: HfO₂ (k ≈ 25) vs 과거 SiO₂ (k = 3.9)</text>

      <rect x="8" y="50" width="234" height="42" rx="3" fill="#0b1329" stroke="#334155"/>
      <text x="12" y="65" fill="#fde047" font-size="7.5" font-weight="800">EOT = t_phys × (k_SiO₂ / k_high-k)</text>
      <text x="12" y="80" fill="#a7f3d0" font-size="7.2">물리적 두께 4nm 유지 ➔ 전기적 EOT는 0.6nm 실현!</text>

      <text x="10" y="106" fill="#cbd5e1" font-size="7.2">★ 목적: 두 마리 토끼 동시 사냥</text>
      <text x="14" y="118" fill="#34d399" font-size="7.2">① 두꺼워서 양자 터널링 누설전류(I_leak) 차단!</text>
      <text x="14" y="130" fill="#34d399" font-size="7.2">② 높은 k로 게이트 정전용량(C_ox)은 거대하게 유지!</text>
      <text x="10" y="148" fill="#fde047" font-size="7.5" font-weight="800">➔ 인텔 45nm HKMG 혁명의 주인공!</text>
    </g>

    <!-- Strategy 2: Low-k in Interconnect -->
    <g transform="translate(15, 220)">
      <rect width="250" height="185" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="10" y="16" fill="#f87171" font-size="8.8" font-weight="800">2. 배선의 선택: Low-k (저유전율)</text>
      <text x="10" y="30" fill="#cbd5e1" font-size="7.2">• 위치: 구리 금속 배선 층간 절연막 IMD (BEOL)</text>
      <text x="10" y="42" fill="#cbd5e1" font-size="7.2">• 소재: SiCOH, 다공성 실리카 (k &lt; 2.5)</text>

      <rect x="8" y="50" width="234" height="42" rx="3" fill="#0b1329" stroke="#334155"/>
      <text x="12" y="65" fill="#f87171" font-size="7.5" font-weight="800">RC 지연 공식: τ = R_wire × C_wire</text>
      <text x="12" y="80" fill="#cbd5e1" font-size="7.2">C_wire = ε_IMD · A / d ➔ k를 낮춰야 속도 향상!</text>

      <text x="10" y="106" fill="#cbd5e1" font-size="7.2">★ 목적: 배선 기생 용량의 철저한 박멸</text>
      <text x="14" y="120" fill="#a5f3fc" font-size="7.2">① 신호 전파 지연시간(RC Delay) 극소화</text>
      <text x="14" y="134" fill="#a5f3fc" font-size="7.2">② 동적 소비 전력(P = C V² f) 절감</text>
      <text x="14" y="148" fill="#a5f3fc" font-size="7.2">③ 배선 간 신호 간섭(Crosstalk 노이즈) 방지</text>
      <text x="10" y="168" fill="#fde047" font-size="7.5" font-weight="800">➔ 게이트는 High-k, 배선은 Low-k가 철칙!</text>
    </g>
  </g>

  <!-- Arrow marker definition -->
  <defs>
    <marker id="arrowRed" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#ef4444" />
    </marker>
    <marker id="arrowBlue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#38bdf8" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- Section 1: Definition of Permittivity -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 유전율(Permittivity, $\epsilon$)의 본질적 물리 정의
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            유전율을 직관적으로 이해하려면 단어의 어원부터 살펴보는 것이 가장 좋습니다:
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:18px;">
              <li><strong>한자어 유전(誘電)</strong>: <strong>꾈 유(誘)</strong>자에 <strong>번개 전(電)</strong>자를 씁니다. 즉, '전기(전하)를 유도하여 유전체 내부에 품고 저장하는 정도'를 뜻합니다.</li>
              <li><strong>영어 Permittivity</strong>: '허용하다(Permit)'에서 파생되었습니다. '외부 전기장(전기력선)이 물질 내부를 통과하도록 얼마나 허용하며, 그 과정에서 전하 분극을 일으켜 에너지를 저장하는가'를 의미합니다.</li>
              <li><strong>수학적 정의</strong>: 진공의 유전율을 $\epsilon_0 \approx 8.854 \times 10^{-12}\,\text{F/m}$라 할 때, 물질의 유전율은 **$\epsilon = \epsilon_r \epsilon_0 = k \epsilon_0$**로 표현합니다. 여기서 진공 대비 몇 배나 전하를 잘 품는가를 나타내는 비율 $k$($\epsilon_r$)를 **'비유전율'** 또는 **'유전상수(Dielectric Constant)'**라고 부릅니다.</li>
            </ul>
          </div>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1;">
            쉽게 비유하자면, <strong>유전체는 '전기적 에너지를 빨아들이는 스펀지'</strong>입니다. 유전율이 높다는 것은 스펀지가 물을 엄청나게 많이 빨아들이듯이, **외부 전기에 반응하여 물질 내부에서 엄청난 양의 전기 에너지를 흡수하고 저장한다**는 뜻입니다.
          </p>
        </div>

        <!-- Section 2: What Does High Permittivity Mean? -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 유전율이 높다는 것은 무엇을 뜻하는가? (3대 물리적 효과)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:14px;">
            어떤 절연 물질의 유전율($k$)이 높다는 것은 전자기학적으로 다음 3가지 현상이 강력하게 일어난다는 뜻입니다.
          </p>

          <!-- Effect 1: Polarization -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:14px; border-left:4px solid #38bdf8;">
            <h4 style="color:#38bdf8; font-size:1.02rem; font-weight:800; margin-bottom:6px;">
              ① 분극(Polarization, $P$)이 엄청나게 잘 일어난다! (전기적 쿠션/스펀지)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              외부에서 전기장($E_0$)을 걸어주면, 물질 내부의 원자핵(+)과 전자구름(-)이 서로 반대 방향으로 쏠리며 수억 개의 미세한 쌍극자(Dipole)가 일제히 정렬합니다.
              <br>이 쌍극자들은 외부 전계와 정반대 방향의 내부 유도 전계($E_{ind}$)를 만들어내어, **물질 내부의 실제 알짜 전계를 $E_{net} = E_0 / k$로 크게 깎아내고 완화(스크리닝)**시킵니다.
              <br>➔ 즉, 외부의 강한 전기적 충격을 내부에서 부드럽게 흡수해 주는 **최고의 '전기적 에어백'** 역할을 수행합니다.
            </p>
          </div>

          <!-- Effect 2: Capacitance Increase -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:14px; border-left:4px solid #facc15;">
            <h4 style="color:#facc15; font-size:1.02rem; font-weight:800; margin-bottom:6px;">
              ② 전하 저장 능력(커패시턴스, $C$)이 비례하여 폭증한다! (전하 저수지 확장)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              평행판 커패시터 공식 $C = \frac{\epsilon A}{d} = \frac{k \epsilon_0 A}{d}$에서 보듯, 유전율 $k$가 10배 높은 물질을 집어넣으면 똑같은 면적과 두께에서 **저장할 수 있는 정전용량($C$)이 정확히 10배로 폭증**합니다.
              <br>유전체 표면에 정렬된 반대 전하들이 금속 전극에 모여 있는 전하들을 꽉 붙잡아주기 때문에, **동일한 전압($V$)을 걸어도 훨씬 더 많은 전하량($Q = CV$)을 가둘 수 있는 거대한 저수지**가 됩니다.
            </p>
          </div>

          <!-- Effect 3: Coulomb Force Weakening -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:14px; border-left:4px solid #f87171;">
            <h4 style="color:#f87171; font-size:1.02rem; font-weight:800; margin-bottom:6px;">
              ③ 두 전하 사이의 쿨롱 힘(인력/척력)을 크게 약화시킨다! (차폐 효과)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              쿨롱의 법칙 $F = \frac{1}{4\pi\epsilon} \frac{q_1 q_2}{r^2}$에서 유전율($\epsilon$)은 분모에 위치합니다. 따라서 유전율이 높은 매질 속에서는 **두 전하가 서로를 잡아당기거나 밀어내는 힘이 $1/k$로 급격히 줄어듭니다**.
              <br>• <strong>대표적 일상 사례</strong>: 물($\text{H}_2\text{O}$)의 유전율은 $k \approx 80$으로 매우 높습니다. 이 때문에 소금($\text{NaCl}$)을 물에 넣으면 $\text{Na}^+$와 $\text{Cl}^-$ 사이의 강력한 이온 결합력이 1/80로 줄어들어 소금이 물에 순식간에 녹아 해리되는 것입니다!
            </p>
          </div>
        </div>

        <!-- Section 3: Semiconductor Application (High-k vs Low-k) -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 반도체 산업에서의 결정적 응용: High-k vs Low-k 양대 전략
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체 칩 안에서는 위치에 따라 <strong>"유전율이 무조건 높아야 하는 곳(High-k)"</strong>과 <strong>"유전율이 무조건 낮아야 하는 곳(Low-k)"</strong>이 극명하게 갈립니다.
          </p>

          <div style="overflow-x:auto; margin-bottom:16px;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">구분</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">High-k (고유전율 소재)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">Low-k (저유전율 소재)</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">적용 위치</td>
                  <td style="padding:10px 14px;"><strong>트랜지스터 게이트 절연막 (FEOL)</strong><br>DRAM 셀 스토리지 커패시터</td>
                  <td style="padding:10px 14px;"><strong>금속 배선 층간 절연막 IMD/ILD (BEOL)</strong><br>구리 배선 사이의 절연 재료</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">대표 물질</td>
                  <td style="padding:10px 14px;">$\text{HfO}_2$ (하프늄 산화막, $k \approx 20\sim 25$)<br>$\text{ZrO}_2$ ($k \approx 30\sim 40$)</td>
                  <td style="padding:10px 14px;">$\text{SiCOH}$ ($k \approx 2.5\sim 2.7$)<br>다공성 탄소 함유 산화막 ($k < 2.2$)</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">도입 목적</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;"><strong>정전용량($C_{ox}$) 극대화 + 누설전류 차단</strong><br>물리적 두께($t_{phys}$)를 두껍게 하여 양자 터널링을 막으면서도 등가 두께($EOT$)를 1nm 이하로 축소</td>
                  <td style="padding:10px 14px; color:#f87171; font-weight:700;"><strong>기생 정전용량($C_{wire}$) 극소화</strong><br>배선 간 신호 지연($\tau = RC$) 단축, 동적 소비전력($P = C V^2 f$) 절감, 신호 간섭(Crosstalk) 방지</td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">핵심 수식</td>
                  <td style="padding:10px 14px;">$EOT = t_{phys} \times \frac{k_{SiO2}}{k_{high-k}}$<br>($k$가 클수록 전기적 EOT 축소!)</td>
                  <td style="padding:10px 14px;">$\tau = R_{wire} \times C_{wire} \propto k_{IMD}$<br>($k$가 작을수록 반도체 동작 속도 급증!)</td>
                </tr>
              </tbody>
            </table>
          </div>
          <p style="font-size:0.92rem; line-height:1.7; color:#fde047;">
            ★ 요약: <strong>"트랜지스터 게이트는 채널을 꽉 쥐어야 하므로 High-k를 쓰고, 신호가 지나가는 배선 사이는 신호가 새거나 느려지면 안 되므로 Low-k를 쓴다!"</strong>라고 기억하시면 완벽합니다.
          </p>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 89 topics (q-89 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(89, 0, -1):
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

    # Step 4: Update header description to 90 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 '유전율의 본질과 유전율이 높다는 것의 의미'이 위치하며, 총 90개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Permittivity topic!")
