# -*- coding: utf-8 -*-
"""
insert_why_high_permittivity_good_q01.py
사용자 질문:
"유전율은 소재가얼마나전하를가지고있는지를 나타내는건데 왜 이게 높아야 좋은거야"

대시보드 최상단 Q01로 신규 추가하고, 기존 90개 질문을 Q02~Q91로 시프트 (총 91개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 물리 본질 · 유전율이 높아야 좋은 이유와 트레이드오프)",
    "title": "유전율은 전하를 품는 능력인데, 왜 이게 높아야 좋을까? (게이트 장악력, 터널링 차단, DRAM 축소)",
    "nav_title": "유전율이 왜 높아야 좋은 걸까?",
    "summary": [
        "<strong>1. \"무조건 높아야 좋은 것은 아니다!\" (위치별 정반대)</strong>: 금속 배선(BEOL)에서는 유전율이 높으면 기생 용량이 커져 신호 지연($RC$)과 소비전력이 폭증하므로 무조건 낮아야(Low-k) 합니다. 유전율이 높아야 절대적으로 유리한 곳은 <strong>트랜지스터 게이트 절연막</strong>과 <strong>DRAM 스토리지 커패시터</strong>입니다.",
        "<strong>2. 이유 ① 게이트의 채널 지배력(장악력) 극대화</strong>: $Q_{inv} = C_{ox}(V_{GS} - V_{th})$에서 $C_{ox} = \\frac{\\epsilon_{ox}}{t_{ox}}$이므로, 유전율이 높으면 <strong>낮은 게이트 전압($V_{GS}$)으로도 채널에 막대한 전자를 끌어당겨 구동 전류($I_{on}$)를 폭발시키고 드레인의 간섭(DIBL)을 완벽 차단</strong>할 수 있습니다.",
        "<strong>3. 이유 ② 두께와 정전용량의 분리 (양자 터널링 누설 차단)</strong>: 전통적 $\\text{SiO}_2$는 $C_{ox}$를 키우려다 두께가 $1\\text{nm}$ 이하로 얇아져 전자가 절연막을 뚫고 새는 직통 터널링 누설전류가 터졌습니다. High-k($\\text{HfO}_2, k \\approx 25$)를 쓰면 <strong>물리적 두께는 $3\\sim 4\\text{nm}$로 두껍게 세워 누설을 원천 차단하면서도, 전기적으로는 6배 강력한 커패시턴스($EOT \\approx 0.6\\text{nm}$)를 발휘하는 마법</strong>이 가능해집니다.",
        "<strong>4. 이유 ③ 초미세 DRAM 메모리 셀의 데이터 보존</strong>: DRAM 셀 면적이 좁아져도 0과 1을 판별하려면 최소 $25\\,\\text{fF}$의 전하가 필수적입니다. 좁쌀만 한 바닥 면적에서 충분한 전하량을 가두어 데이터 유실(Refresh 주기 악화)을 막기 위해 높은 유전율 소재가 필수적입니다."
    ],
    "svg_title": "📊 [유전율이 높아야 좋은 이유 다이어그램] (A) 게이트 채널 장악력 극대화 | (B) 양자 터널링 차단과 EOT 혁신 | (C) 반도체 위치별 High-k vs Low-k 득실 비교",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Channel Gate Control & Drive Current -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 이유 ① 게이트 채널 장악력 극대화</text>

    <!-- MOSFET Inversion Channel Diagram -->
    <g transform="translate(15, 42)">
      <rect width="270" height="235" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="9" font-weight="800">게이트 전압에 대한 채널 전하 유인력</text>

      <!-- Gate electrode -->
      <rect x="50" y="30" width="170" height="15" fill="#475569" rx="2"/>
      <text x="100" y="41" fill="#fff" font-size="8">Gate 전극 (+VG)</text>

      <!-- Gate Oxide (High-k) -->
      <rect x="50" y="47" width="170" height="12" fill="#a855f7" rx="1"/>
      <text x="75" y="56" fill="#fff" font-size="7.5" font-weight="800">High-k 유전체 (ε_ox ↑↑)</text>

      <!-- Powerful induced charges -->
      <!-- Positive bound charge on top of oxide, negative on bottom -->
      <g fill="#38bdf8" font-size="7" font-weight="900">
        <text x="55" y="70">−</text><text x="75" y="70">−</text><text x="95" y="70">−</text>
        <text x="115" y="70">−</text><text x="135" y="70">−</text><text x="155" y="70">−</text>
        <text x="175" y="70">−</text><text x="195" y="70">−</text>
      </g>
      <text x="70" y="82" fill="#38bdf8" font-size="7.8" font-weight="800">초고밀도 2D 반전층 전자 (Q_inv ↑↑)</text>

      <!-- Source and Drain -->
      <rect x="15" y="50" width="35" height="50" fill="#f59e0b" rx="1"/>
      <text x="18" y="78" fill="#000" font-size="7.5" font-weight="800">Source</text>
      <rect x="220" y="50" width="35" height="50" fill="#f59e0b" rx="1"/>
      <text x="225" y="78" fill="#000" font-size="7.5" font-weight="800">Drain</text>

      <!-- Huge Current Flow -->
      <path d="M 50 92 L 220 92" stroke="#10b981" stroke-width="4" marker-end="url(#arrowGreen)"/>
      <text x="90" y="106" fill="#34d399" font-size="8.5" font-weight="900">막대한 구동 전류 (I_on ↑↑)</text>

      <!-- Silicon Substrate -->
      <rect x="15" y="115" width="240" height="110" fill="#0284c7" opacity="0.15" rx="4"/>
      <text x="22" y="130" fill="#fde047" font-size="8" font-weight="800">★ 물리적 공식으로 보는 이득:</text>
      <text x="22" y="146" fill="#ffffff" font-size="8">Q_inv = C_ox (V_GS - V_th) = (ε_ox / t_ox) ΔV</text>
      <text x="22" y="162" fill="#cbd5e1" font-size="7.5">• 유전율(ε)이 높으면 적은 전압(0.7V)으로도</text>
      <text x="22" y="176" fill="#a7f3d0" font-size="7.5">• 채널에 수억 개의 전자를 강력하게 빨아들임!</text>
      <text x="22" y="190" fill="#cbd5e1" font-size="7.5">• 드레인이 채널을 뺏으려는 DIBL 누설 차단</text>
      <text x="22" y="206" fill="#fca5a5" font-size="7.5">• 서브스레시홀드 스윙 SS 개선 ➔ 칼 같은 On/Off!</text>
    </g>

    <!-- Bottom summary box -->
    <rect x="15" y="295" width="270" height="112" rx="6" fill="#0b1329" stroke="#38bdf8"/>
    <text x="22" y="315" fill="#38bdf8" font-size="9" font-weight="800">🎯 핵심 포인트 ①</text>
    <text x="22" y="333" fill="#cbd5e1" font-size="7.8">• 트랜지스터 게이트는 <strong>'스위치 손잡이'</strong>입니다.</text>
    <text x="22" y="348" fill="#cbd5e1" font-size="7.8">• 유전율이 낮으면 손잡이에 힘이 없어 채널이 안 켜짐</text>
    <text x="22" y="364" fill="#cbd5e1" font-size="7.8">• 유전율이 높으면 살짝만 돌려도 <strong>채널이 번쩍 켜짐!</strong></text>
    <text x="22" y="380" fill="#fde047" font-size="8" font-weight="800">➔ 스마트폰 동작 속도(Ion) 폭증 + 저전력 구동 실현</text>
    <text x="22" y="396" fill="#a5f3fc" font-size="7.5">하지만 진짜 기적은 (B)의 '두께 마법'에서 나옵니다!</text>
  </g>

  <!-- PANEL B: Quantum Tunneling Suppression & EOT -->
  <g transform="translate(340, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 이유 ② 양자 터널링 차단과 두께의 마법</text>

    <!-- Comparison: SiO2 vs High-k -->
    <g transform="translate(15, 42)">
      <rect width="280" height="175" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="16" fill="#fde047" font-size="8.8" font-weight="800">과거의 위기(SiO₂) vs High-k의 구원</text>

      <!-- Case 1: Ultra thin SiO2 -->
      <g transform="translate(10, 26)">
        <rect width="260" height="65" rx="4" fill="#0b1329" stroke="#ef4444"/>
        <text x="10" y="16" fill="#f87171" font-size="8" font-weight="800">1. 전통 SiO₂ (k = 3.9)의 한계 봉착:</text>
        <text x="10" y="30" fill="#cbd5e1" font-size="7.2">• Cox 늘리려다 물리적 두께를 1.0nm (원자 3~4개)까지 깎음</text>
        <text x="10" y="44" fill="#ef4444" font-size="7.5" font-weight="800">➔ 전자가 벽을 뚫고 새는 양자 직통 터널링 폭발! (누설전류↑↑)</text>
        <text x="10" y="58" fill="#fca5a5" font-size="7">칩이 뜨거워져 녹아내리는 위기 도래 (2000년대 초반)</text>
      </g>

      <!-- Case 2: Thick High-k HfO2 -->
      <g transform="translate(10, 98)">
        <rect width="260" height="70" rx="4" fill="#0b1329" stroke="#10b981"/>
        <text x="10" y="16" fill="#34d399" font-size="8" font-weight="800">2. High-k (HfO₂, k ≈ 25)의 구원:</text>
        <text x="10" y="30" fill="#cbd5e1" font-size="7.2">• 물리적 두께를 3.5nm로 3.5배나 두껍게 성벽처럼 쌓음!</text>
        <text x="10" y="44" fill="#34d399" font-size="7.5" font-weight="800">➔ 두꺼우니 전자가 절대 못 뚫음! (터널링 누설 99.9% 차단!)</text>
        <text x="10" y="58" fill="#fde047" font-size="7.5" font-weight="800">➔ 유전율이 6배 높아 전기적 두께는 EOT = 0.55nm 실현!</text>
      </g>
    </g>

    <!-- Formula Box -->
    <g transform="translate(15, 228)">
      <rect width="280" height="178" rx="6" fill="#0b1329" stroke="#10b981"/>
      <text x="12" y="18" fill="#38bdf8" font-size="9" font-weight="800">★ 등가 산화막 두께 (EOT) 공식</text>

      <rect x="8" y="28" width="264" height="34" rx="4" fill="#1e293b" stroke="#334155"/>
      <text x="18" y="49" fill="#fde047" font-size="9.5" font-weight="800">EOT = t_phys × ( k_SiO₂ / k_high-k )</text>

      <text x="12" y="78" fill="#cbd5e1" font-size="7.8">• <strong>물리적 두께(t_phys)</strong>: 전자가 뚫지 못하게 두꺼울수록 좋음</text>
      <text x="12" y="92" fill="#cbd5e1" font-size="7.8">• <strong>전기적 두께(EOT)</strong>: 게이트가 채널을 쥐려면 얇을수록 좋음</text>
      
      <text x="12" y="112" fill="#34d399" font-size="8.2" font-weight="800">★ 유전율(k)이 높아야만 두 마리 토끼를 다 잡는다!</text>
      <text x="12" y="128" fill="#cbd5e1" font-size="7.5">• "벽은 3.5nm로 두껍게 세워 전자가 못 새어나가게 막고,"</text>
      <text x="12" y="142" fill="#cbd5e1" font-size="7.5">• "전기력은 0.5nm짜리 얇은 막처럼 채널을 꽉 쥐는 기적!"</text>
      <text x="12" y="162" fill="#fde047" font-size="8" font-weight="800">➔ 이것이 반도체 업계가 High-k에 목숨 거는 이유입니다.</text>
    </g>
  </g>

  <!-- PANEL C: Where is it good? Where is it bad? -->
  <g transform="translate(670, 20)">
    <rect width="290" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) 유전율의 양면성: 어디서 좋고 어디서 나쁜가?</text>

    <!-- Good Region: Gate & DRAM -->
    <g transform="translate(15, 42)">
      <rect width="260" height="160" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="10" y="16" fill="#38bdf8" font-size="8.8" font-weight="800">▲ 유전율이 무조건 높아야 하는 곳 (High-k)</text>
      
      <text x="10" y="32" fill="#fde047" font-size="8" font-weight="700">1. 트랜지스터 게이트 절연막 (FEOL)</text>
      <text x="18" y="45" fill="#cbd5e1" font-size="7.2">• 구동력 Ion 극대화 + 터널링 누설 차단</text>
      <text x="18" y="57" fill="#a7f3d0" font-size="7.2">• HfO₂, ZrO₂ (k ≈ 20~25)</text>

      <text x="10" y="74" fill="#fde047" font-size="8" font-weight="700">2. DRAM 1T-1C 스토리지 커패시터</text>
      <text x="18" y="87" fill="#cbd5e1" font-size="7.2">• 셀 바닥 면적이 줄어도 25fF 전하량 보존 필수</text>
      <text x="18" y="99" fill="#cbd5e1" font-size="7.2">• 전하가 부족하면 1비트 데이터가 증발(소실)됨!</text>
      <text x="18" y="111" fill="#a7f3d0" font-size="7.2">• High-k로 작은 면적에 막대한 전하 가둠</text>

      <rect x="8" y="122" width="244" height="28" rx="3" fill="#0b1329" stroke="#38bdf8"/>
      <text x="14" y="138" fill="#38bdf8" font-size="7.5" font-weight="800">➔ 전하를 가두고 제어해야 하는 곳 = High-k!</text>
    </g>

    <!-- Bad Region: Interconnect -->
    <g transform="translate(15, 215)">
      <rect width="260" height="190" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="10" y="16" fill="#f87171" font-size="8.8" font-weight="800">▼ 유전율이 높으면 재앙인 곳 (Low-k 필수!)</text>

      <text x="10" y="32" fill="#fca5a5" font-size="8" font-weight="700">1. 구리 금속 배선 층간 절연막 IMD (BEOL)</text>
      <text x="18" y="46" fill="#cbd5e1" font-size="7.2">• 배선 사이 유전율이 높으면? ➔ 기생용량 C 폭증!</text>
      <text x="18" y="60" fill="#ef4444" font-size="7.5" font-weight="800">➔ 신호 지연 τ = RC 급증 (칩 속도 거북이로 전락)</text>
      <text x="18" y="74" fill="#ef4444" font-size="7.5" font-weight="800">➔ 동적 전력 P = C V² f 폭발 (스마트폰 배터리 광탈)</text>
      <text x="18" y="88" fill="#cbd5e1" font-size="7.2">• 배선끼리 신호가 섞이는 크로스토크 노이즈 폭증</text>

      <rect x="8" y="102" width="244" height="42" rx="3" fill="#0b1329" stroke="#ef4444"/>
      <text x="14" y="118" fill="#fca5a5" font-size="7.5" font-weight="800">➔ 배선에서는 유전율이 높으면 독약!</text>
      <text x="14" y="132" fill="#cbd5e1" font-size="7.2">공기(k=1)처럼 유전율이 낮은 Low-k(k&lt;2.5) 필수!</text>

      <rect x="8" y="152" width="244" height="28" rx="3" fill="#064e3b" stroke="#10b981"/>
      <text x="14" y="170" fill="#a7f3d0" font-size="7.5" font-weight="800">💡 결론: 게이트는 High-k, 배선은 Low-k가 정답!</text>
    </g>
  </g>

  <!-- Arrow marker definition -->
  <defs>
    <marker id="arrowGreen" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#10b981" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- Section 1: Direct Answer to User's Question -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 질문자님의 질문에 대한 직격 답변: "무조건 높다고 좋은 것이 아닙니다!"
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            질문자님께서 <em>"유전율은 소재가 얼마나 전하를 품고 있는지를 나타내는 건데, 왜 이게 높아야 좋은 거야?"</em>라고 물어보셨습니다. 
            매우 날카롭고 본질적인 의문입니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #f59e0b; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:18px;">
            <h4 style="color:#fbbf24; font-size:1.05rem; font-weight:800; margin-bottom:8px;">⚡ 반도체 엔지니어의 핵심 반전:</h4>
            <p style="color:#cbd5e1; font-size:0.92rem; line-height:1.8;">
              <strong>"반도체에서 유전율이 무조건 높아야 좋은 것은 절대로 아닙니다! 위치에 따라 완전히 정반대입니다."</strong><br>
              • <strong>전하를 가두고 채널을 제어해야 하는 곳(게이트, DRAM)</strong>: 유전율이 높을수록(High-k) 좋습니다.<br>
              • <strong>신호가 고속으로 지나가는 길목(금속 배선 사이)</strong>: 유전율이 높으면 전하를 머금어 신호가 느려지고 배터리가 닳으므로 무조건 낮아야(Low-k) 좋습니다.
            </p>
          </div>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1;">
            그렇다면 질문자님께서 궁금해하신 <strong>"게이트 절연막과 커패시터에서는 왜 유전율이 높아야 좋을까?"</strong>에 대해 그 결정적인 3가지 이유를 해부해 드리겠습니다.
          </p>
        </div>

        <!-- Section 2: Why High Permittivity is Good in Gate -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 게이트 절연막에서 유전율이 높아야 하는 2대 이유
          </h3>

          <!-- Reason 1: Gate Control -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:14px; border-left:4px solid #38bdf8;">
            <h4 style="color:#38bdf8; font-size:1.02rem; font-weight:800; margin-bottom:6px;">
              이유 ① 게이트의 채널 지배력(장악력)을 극대화하여 트랜지스터를 힘차게 켠다!
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:18px;">
              <li>트랜지스터에서 게이트는 수도꼭지의 손잡이입니다. 게이트에 전압을 살짝 걸었을 때 채널 표면에 전자들이 우르르 끌려와야 전류($I_{on}$)가 시원하게 흐릅니다.</li>
              <li>채널에 모이는 전자 전하량 공식: <strong>$Q_{inv} = C_{ox} (V_{GS} - V_{th}) = \left(\frac{\epsilon_{ox}}{t_{ox}}\right) \Delta V$</strong></li>
              <li>유전율($\epsilon_{ox}$)이 높으면 게이트 커패시턴스($C_{ox}$)가 거대해지므로, **아주 낮은 게이트 전압(0.7V)만 걸어주어도 채널에 막대한 양의 전자를 강력하게 유치**할 수 있습니다.</li>
              <li>그 결과 트랜지스터의 스위칭 속도가 번개처럼 빨라지고, 꺼졌을 때와 켜졌을 때의 차이가 분명해져 누설전류(DIBL)를 압도적으로 틀어막을 수 있습니다.</li>
            </ul>
          </div>

          <!-- Reason 2: Quantum Tunneling and EOT -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:14px; border-left:4px solid #10b981;">
            <h4 style="color:#10b981; font-size:1.02rem; font-weight:800; margin-bottom:6px;">
              이유 ② 양자역학적 터널링 누설전류 차단 (두께와 전기력의 분리 마법!)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; margin-bottom:10px;">
              이것이 바로 반도체 역사상 가장 위대한 혁신인 **High-k 도입(2007년 인텔 45nm)**의 진짜 이유입니다:
            </p>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:18px;">
              <li>과거에는 유전율이 낮은 전통 소재인 $\text{SiO}_2$($k = 3.9$)를 썼습니다. $C_{ox} = \frac{\epsilon}{t}$에서 $C_{ox}$를 키우려면 두께($t$)를 얇게 깎는 수밖에 없었습니다.</li>
              <li>그런데 두께가 $1.2\,\text{nm}$(원자 4개 두께) 이하로 얇아지자, **전자들이 벽을 양자역학적으로 뚫고 게이트로 그냥 새어버리는 직통 터널링 누설전류(Direct Tunneling Leakage)**가 폭증하여 칩이 뜨겁게 타버리는 물리적 한계에 부딪혔습니다.</li>
              <li><strong>여기서 유전율이 6배 높은 $\text{HfO}_2$($k \approx 25$)를 쓰면 기적이 일어납니다</strong>:
                <br>• 물리적 두께($t_{phys}$)는 $3.5\,\text{nm}$로 **3배 이상 두껍게 쌓아 전자가 벽을 뚫지 못하게 완벽 차단**합니다!
                <br>• 그러면서도 유전율이 6배나 높기 때문에, 전기적으로는 $\text{SiO}_2$를 $0.55\,\text{nm}$로 얇게 깎은 것과 똑같이 강력한 정전용량을 발휘합니다 ($EOT = 3.5 \times \frac{3.9}{25} \approx 0.55\,\text{nm}$).
              </li>
              <li>➔ 즉, **"물리적으로는 두껍게 세워 전자가 새는 것을 막고, 전기적으로는 얇은 것처럼 강력한 힘을 발휘하게 만드는 마법"**을 부리기 위해 유전율이 높아야 하는 것입니다!</li>
            </ul>
          </div>
        </div>

        <!-- Section 3: Why High Permittivity in DRAM -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. DRAM 메모리 셀에서 유전율이 높아야 하는 이유
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            DRAM은 트랜지스터 1개와 커패시터 1개(1T-1C)로 이루어진 방에 전하를 채워두고 1인지 0인지를 기억합니다:
          </p>
          <div style="background:#0f172a; border-left:4px solid #ef4444; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:18px;">
              <li>메모리 용량이 커질수록(16Gb ➔ 32Gb) 셀 1개의 바닥 면적($A$)은 좁쌀보다 수만 배 작아집니다.</li>
              <li>그런데 감지 증폭기(Sense Amplifier)가 데이터를 오류 없이 읽어내려면, 셀 1개당 **최소 $20\sim 25\,\text{fF}$ 이상의 정전용량($C = \frac{\epsilon A}{d}$)**이 무조건 확보되어야 합니다.</li>
              <li>바닥 면적($A$)이 줄어드는데 정전용량($C$)을 유지하려면, **유전율($\epsilon$)이 극도로 높은 소재($\text{ZrO}_2, \text{TiO}_2, \text{SrTiO}_3$)를 전극 사이에 욱여넣는 수밖에 없습니다**.</li>
              <li>유전율이 높아야 좁은 공간에서도 전하를 꽉 채워 넣어 데이터가 증발(소실)하는 참사를 막을 수 있습니다.</li>
            </ul>
          </div>
        </div>

        <!-- Section 4: Where High Permittivity is a Disaster -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#ef4444; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. 반대로, 유전율이 높으면 재앙이 되는 곳: 금속 배선 (BEOL)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            만약 구리 배선 사이의 절연막(IMD)에 유전율이 높은 소재를 쓰면 어떻게 될까요?
          </p>
          <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:22px; margin-bottom:14px;">
            <li>배선 사이의 불필요한 기생 커패시턴스($C_{wire} = \frac{\epsilon A}{d}$)가 폭발적으로 커집니다.</li>
            <li>신호가 전달되는 지연 시간 **$\tau = R_{wire} \times C_{wire}$**가 급증하여 컴퓨터 연산 속도가 거북이로 전락합니다.</li>
            <li>동적 소비 전력 **$P = C V^2 f$**가 폭증하여 스마트폰 배터리가 순식간에 방전되고 칩이 뜨겁게 달아오릅니다.</li>
            <li>따라서 금속 배선 사이에는 유전율이 공기($k=1$)처럼 최대한 낮은 **Low-k 재료($k < 2.5$)**를 필사적으로 넣고 있습니다.</li>
          </ul>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 90 topics (q-90 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(90, 0, -1):
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

    # Step 4: Update header description to 91 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 '유전율이 왜 높아야 좋은 걸까?'이 위치하며, 총 91개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Why High Permittivity is Good topic!")
