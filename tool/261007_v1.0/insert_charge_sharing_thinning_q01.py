# -*- coding: utf-8 -*-
"""
insert_charge_sharing_thinning_q01.py
사용자 질문:
"2. 2차원 전하 분할 (Charge Sharing)과 실효 두께 축소: 단채널에서는 소스와 드레인 접합 공핍층이 채널 중앙으로 깊숙이 침범합니다. 게이트 아래 공핍 전하를 소스/드레인이 나누어 부담하면서, 2차원 전계 효과로 인해 게이트가 바라보는 실효 공핍층 두께(Wdep,eff)가 장채널보다 얇아지는 효과(Thinning)가 발생하여 유효 Cdep가 상승합니다. 이거좀 자세히설명해줘"

대시보드 최상단 Q01로 신규 추가하고, 기존 84개 질문을 Q02~Q85로 시프트 (총 85개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (단채널 소자 물리 · 2D 전하 분할 심층 분석)",
    "title": "2차원 전하 분할(Charge Sharing)과 실효 공핍층 두께 축소(Thinning) 메커니즘 상세 해부: 왜 Wdep,eff가 얇아지고 Cdep가 상승할까?",
    "nav_title": "2차원 전하 분할(Charge Sharing)과 실효 두께 축소(Thinning) 상세",
    "summary": [
        "<strong>1. 야우(Yau)의 2차원 기하학적 전하 분할 모델</strong>: 장채널에서는 게이트 아래 공핍 전하가 100% 게이트 수직 전계에 의해 제어되는 직사각형($L \\times W_{dep}$) 모양입니다. 그러나 단채널에서는 <strong>소스와 드레인 접합 공핍층이 채널 중앙으로 4분원 형태로 깊숙이 침범</strong>하여, 게이트 직하부 전하 중 양쪽 귀퉁이를 소스와 드레인의 빌트인 전위가 대신 떠받칩니다. 이로 인해 <strong>게이트가 순수하게 지탱해야 하는 전하 영역이 '사다리꼴(Trapezoid)'로 깎여나갑니다</strong>.",
        "<strong>2. 실효 두께 축소(Thinning)가 발생하는 기하학적 원리</strong>: 게이트의 물리적 길이는 여전히 $L$이지만, 게이트가 감당하는 전하량은 사다리꼴 면적으로 줄어들었습니다($Q_{B,eff} = Q_{B,1D} \\times [1 - \\Delta L/(2L)]$). 이를 게이트 길이 $L$ 전체에 걸쳐 균등하게 펼쳐 평균 두께를 환산한 것이 바로 <strong>실효 공핍층 두께 $W_{dep,eff} = W_{dep} \\times [1 - \\Delta L/(2L)] < W_{dep}$</strong>이며, <strong>원래 1차원 두께보다 수학적으로 얇아지는 효과(Thinning)</strong>가 나타납니다.",
        "<strong>3. 유효 공핍 커패시턴스($C_{dep,eff}$)가 상승하는 수식 도도</strong>: 등가 평행판 커패시턴스는 두께에 반비례($C = \\frac{\\epsilon}{W}$)하므로, 분모인 실효 두께 $W_{dep,eff}$가 얇아지면서 <strong>단위 면적당 유효 공핍 커패시턴스는 $C_{dep,eff} = \\frac{\\epsilon_{si}}{W_{dep,eff}} = \\frac{C_{dep,1D}}{1 - \\Delta L/(2L)}$로 가파르게 급상승</strong>합니다.",
        "<strong>4. 2차원 수평 전계 침투(DIBL)와 SS 악화의 결말</strong>: 드레인의 수평 전기력선이 채널 중앙 장벽을 낮추며 소스/드레인 측면 전하 변조가 게이트 전위에 2차원적으로 결합됩니다. 이 $C_{dep,eff}$ 상승으로 인해 정전용량 전압 분배 손실이 커지며 <strong>서브스레시홀드 스윙($SS = 60[1 + C_{dep,eff}/C_{ox}]$)이 80~110mV/dec로 치솟고 대기 누설전류가 폭증</strong>하게 됩니다."
    ],
    "svg_title": "📊 [2D 전하 분할과 실효 두께 축소 완전 해부] (A) 야우의 사다리꼴 전하 분할 모델 | (B) 실효 두께 Wdep,eff 축소와 Cdep 상승 유도 | (C) 2D 전계 침투와 SS 악화",
    "svg": """<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Yau's Charge Sharing Geometric Model -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 야우(Yau)의 사다리꼴 전하 분할</text>

    <!-- Detailed Charge Sharing Diagram -->
    <g transform="translate(15, 42)">
      <rect width="270" height="240" rx="6" fill="#1e293b" stroke="#334155"/>

      <!-- Gate Electrode -->
      <rect x="50" y="20" width="170" height="12" fill="#475569" rx="1"/>
      <text x="105" y="29" fill="#fff" font-size="7.5">Gate Electrode (L)</text>
      <rect x="50" y="32" width="170" height="4" fill="#a855f7"/>

      <!-- Source / Drain Regions -->
      <rect x="15" y="36" width="35" height="45" fill="#f59e0b" rx="1"/>
      <text x="20" y="62" fill="#000" font-size="7.5" font-weight="800">Source</text>
      <rect x="220" y="36" width="35" height="45" fill="#f59e0b" rx="1"/>
      <text x="226" y="62" fill="#000" font-size="7.5" font-weight="800">Drain</text>

      <!-- Full 1D Rectangle Depletion outline (dashed) -->
      <rect x="50" y="36" width="170" height="70" fill="none" stroke="#64748b" stroke-dasharray="3,2"/>
      <text x="180" y="116" fill="#94a3b8" font-size="7">원래 1차원 공핍층 (L × W_dep)</text>

      <!-- Source Depletion Quarter Circle (controlled by Source) -->
      <path d="M 50 36 A 55 55 0 0 1 50 120 L 15 120 L 15 36 Z" fill="#ef4444" opacity="0.35"/>
      <text x="20" y="132" fill="#fca5a5" font-size="7">소스 분할 전하</text>

      <!-- Drain Depletion Quarter Circle (controlled by Drain) -->
      <path d="M 220 36 A 65 65 0 0 0 220 130 L 255 130 L 255 36 Z" fill="#ef4444" opacity="0.35"/>
      <text x="195" y="142" fill="#fca5a5" font-size="7">드레인 분할 전하</text>

      <!-- Gate-controlled Trapezoid (Blue) -->
      <polygon points="50,36 220,36 185,106 85,106" fill="#0284c7" opacity="0.6" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="92" y="70" fill="#fff" font-size="8.5" font-weight="900">게이트 제어 전하 (QB,eff)</text>
      <text x="105" y="85" fill="#e0f2fe" font-size="8" font-weight="700">[사다리꼴 형태!]</text>

      <!-- Trapezoid dimensions -->
      <line x1="50" y1="16" x2="220" y2="16" stroke="#38bdf8" stroke-width="1.2"/>
      <text x="115" y="13" fill="#38bdf8" font-size="7.5">윗변 = L</text>
      <line x1="85" y1="112" x2="185" y2="112" stroke="#38bdf8" stroke-width="1.2"/>
      <text x="120" y="122" fill="#38bdf8" font-size="7.5">아랫변 = L' &lt; L</text>

      <!-- Depth arrow -->
      <line x1="225" y1="36" x2="225" y2="106" stroke="#facc15" stroke-width="1.2"/>
      <text x="230" y="75" fill="#facc15" font-size="7.5">W_dep</text>

      <!-- S/D encroachment annotations -->
      <text x="10" y="170" fill="#cbd5e1" font-size="7.8">• S/D 4분원 공핍층이 채널 중앙으로 침범 (빨간 영역)</text>
      <text x="10" y="184" fill="#cbd5e1" font-size="7.8">• 양쪽 귀퉁이 전하는 S/D 빌트인 전위가 대신 지탱!</text>
      <text x="10" y="198" fill="#fde047" font-size="8" font-weight="800">➔ 게이트가 순수 통제하는 전하는 사다리꼴로 깎임</text>
      <text x="10" y="212" fill="#a5f3fc" font-size="7.8">• 평균 유효 길이 L_avg = L · [ 1 - ΔL / (2L) ]</text>
      <text x="10" y="226" fill="#a5f3fc" font-size="7.8">• 게이트 유효 전하량: QB,eff = QB,1D · [ 1 - ΔL / (2L) ]</text>
    </g>

    <!-- Summary Box -->
    <rect x="15" y="295" width="270" height="112" rx="6" fill="#0b1329" stroke="#334155"/>
    <text x="22" y="315" fill="#38bdf8" font-size="9" font-weight="800">핵심 기하학적 정리:</text>
    <text x="22" y="333" fill="#cbd5e1" font-size="8">• 직사각형 면적 = L × W_dep (장채널)</text>
    <text x="22" y="350" fill="#fde047" font-size="8.2" font-weight="700">• 사다리꼴 면적 = L_avg × W_dep &lt; L × W_dep (단채널)</text>
    <text x="22" y="368" fill="#cbd5e1" font-size="8">• 게이트가 지탱할 전하가 줄어 문턱전압 강하 (Vt 롤오프)</text>
    <text x="22" y="385" fill="#34d399" font-size="8">• 이 사다리꼴 전하가 '실효 두께 축소'의 출발점!</text>
  </g>

  <!-- PANEL B: Derivation of Wdep,eff Thinning and Cdep Increase -->
  <g transform="translate(340, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 실효 두께(Wdep,eff) 축소와 Cdep 상승</text>

    <!-- Step 1: Definition of Wdep,eff -->
    <g transform="translate(15, 42)">
      <rect width="280" height="155" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="9" font-weight="800">1. 실효 공핍층 두께(Wdep,eff)란 무엇인가?</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="8">• 게이트의 물리적 면적은 여전히 (W × L)입니다.</text>
      <text x="12" y="50" fill="#cbd5e1" font-size="8">• 하지만 게이트가 지탱하는 전하는 사다리꼴 전하량 QB,eff:</text>
      <text x="20" y="66" fill="#ffffff" font-size="8.8">QB,eff = q · NA · [ L_avg · W_dep ] · W</text>
      <text x="12" y="84" fill="#cbd5e1" font-size="8">• 이를 게이트 전체 길이 L 기준으로 '평균 환산 두께'를 정의:</text>
      <text x="20" y="100" fill="#34d399" font-size="9.5" font-weight="800">W_dep,eff ≡ |QB,eff| / (q · NA · L · W)</text>
      <text x="20" y="118" fill="#86efac" font-size="9" font-weight="700">= W_dep × ( L_avg / L ) = W_dep × [ 1 - ΔL / (2L) ]</text>
      <text x="12" y="136" fill="#fde047" font-size="8.2" font-weight="800">★ 1 - ΔL/(2L) &lt; 1 이므로 ➔ W_dep,eff &lt; W_dep ! (Thinning!)</text>
    </g>

    <!-- Step 2: Why Cdep Increases -->
    <g transform="translate(15, 208)">
      <rect width="280" height="198" rx="6" fill="#0b1329" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="9.5" font-weight="800">2. 실효 두께가 얇아지면 왜 Cdep가 올라가는가?</text>
      <text x="12" y="38" fill="#cbd5e1" font-size="8">• 단위 면적당 유효 공핍 커패시턴스 평행판 정의:</text>
      <text x="20" y="55" fill="#ffffff" font-size="9">C_dep,eff = ε_si / W_dep,eff</text>

      <text x="12" y="75" fill="#cbd5e1" font-size="8">• W_dep,eff 공식 대입:</text>
      <text x="20" y="94" fill="#fde047" font-size="9" font-weight="800">C_dep,eff = ε_si / [ W_dep · (1 - ΔL / 2L) ]</text>
      <text x="20" y="112" fill="#38bdf8" font-size="9" font-weight="800">= C_dep,1D / [ 1 - ΔL / (2L) ] &gt; C_dep,1D</text>

      <rect x="10" y="126" width="260" height="60" rx="4" fill="#1e293b" stroke="#34d399"/>
      <text x="16" y="142" fill="#a7f3d0" font-size="8" font-weight="800">💡 물리적 통찰 (직관적 이해):</text>
      <text x="16" y="156" fill="#cbd5e1" font-size="7.5">사다리꼴로 깎여 전하가 차지하는 실효 깊이가 얇아졌으므로,</text>
      <text x="16" y="170" fill="#fde047" font-size="7.8" font-weight="700">분모(두께)가 작아져 단위 면적당 정전용량은 가파르게 상승!</text>
    </g>
  </g>

  <!-- PANEL C: 2D Field Coupling (DIBL) & Subthreshold Swing Impact -->
  <g transform="translate(670, 20)">
    <rect width="290" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) 2D 전계 침투와 SS 악화 메커니즘</text>

    <!-- 2D Field Coupling -->
    <g transform="translate(15, 42)">
      <rect width="260" height="155" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="12" y="18" fill="#fde047" font-size="9" font-weight="800">1. 드레인 수평 전계 침투 (DIBL 결합)</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="8">• 장채널: 게이트 수직 전계(Ey)만 존재</text>
      <text x="12" y="50" fill="#ef4444" font-size="8">• 단채널: 드레인 수평 전계(Ex)가 채널 중앙 관통!</text>

      <!-- Lateral field lines visual -->
      <rect x="20" y="58" width="220" height="40" fill="#0b1329" rx="3"/>
      <line x1="200" y1="78" x2="60" y2="78" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,2"/>
      <text x="75" y="73" fill="#fca5a5" font-size="7.5">드레인 수평 전기선 침투 ➔➔</text>
      <text x="75" y="89" fill="#fde047" font-size="7.5">에너지 장벽 강하 (DIBL 발생)</text>

      <text x="12" y="114" fill="#cbd5e1" font-size="7.8">• 게이트 표면 전위(ψs) 변화 시 S/D 경계면의</text>
      <text x="12" y="127" fill="#cbd5e1" font-size="7.8">  2차원 측면 전하 변조가 결합되어,</text>
      <text x="12" y="142" fill="#38bdf8" font-size="8" font-weight="800">➔ C_dep,eff = ∂Q_total / ∂ψs 가 추가 폭등!</text>
    </g>

    <!-- Subthreshold Swing Impact -->
    <g transform="translate(15, 208)">
      <rect width="260" height="198" rx="6" fill="#0b1329" stroke="#ef4444"/>
      <text x="12" y="18" fill="#f87171" font-size="9.5" font-weight="800">2. 서브스레시홀드 스윙(SS) 폭등의 대재앙</text>

      <text x="12" y="38" fill="#ffffff" font-size="9">SS = 60 · [ 1 + (C_dep,eff / C_ox) ]  [mV/dec]</text>

      <text x="12" y="58" fill="#cbd5e1" font-size="8">• 1차원 장채널:</text>
      <text x="20" y="72" fill="#34d399" font-size="8">W_dep 두꺼움 ➔ C_dep 낮음 ➔ SS ≈ 65~70 mV/dec</text>

      <text x="12" y="90" fill="#fca5a5" font-size="8">• 2차원 단채널 (전하 분할 + 실효 두께 축소):</text>
      <text x="20" y="104" fill="#ef4444" font-size="8.2" font-weight="800">W_dep,eff 얇아짐 ➔ C_dep,eff 급상승!</text>
      <text x="20" y="118" fill="#f87171" font-size="8">➔ SS = 85 ~ 110 mV/dec 로 치솟음!</text>

      <rect x="10" y="132" width="240" height="54" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <text x="16" y="148" fill="#38bdf8" font-size="8" font-weight="800">■ 치명적 결과: 오프 누설전류(I_off) 폭발</text>
      <text x="16" y="162" fill="#cbd5e1" font-size="7.5">• 게이트가 채널 전위를 장악하지 못해 스위치 누설!</text>
      <text x="16" y="174" fill="#a7f3d0" font-size="7.5">• 3D FinFET/GAA 무도핑 채널 도입의 결정적 이유</text>
    </g>
  </g>
</svg>""",
    "lecture": r"""
        <!-- Section 1: Introduction and Problem Statement -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 질문의 핵심 정리: 전하 분할이 왜 '실효 두께 축소'와 'Cdep 상승'으로 이어질까?
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            질문자님께서 질문하신 문장은 반도체 소자 물리학에서 가장 핵심적인 단채널 효과 모델인 <strong>야우(Yau)의 2차원 전하 분할 모델(Charge Sharing Model)</strong>의 정수를 담고 있습니다.<br>
            <em>"공핍 전하를 소스와 드레인이 나누어 갖는데, 왜 게이트가 바라보는 실효 두께($W_{dep,eff}$)가 얇아진다고 표현하며, 왜 그 결과 공핍 커패시턴스($C_{dep}$)가 올라가는가?"</em>라는 물리적 인과관계를 단계별로 완벽히 분해해 드리겠습니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:18px;">
            <h4 style="color:#38bdf8; font-size:1.05rem; font-weight:800; margin-bottom:8px;">💡 인과관계 4단계 로직 요약</h4>
            <ol style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:18px;">
              <li><strong>[현상]</strong> 소스/드레인 접합 공핍층이 채널 중앙으로 침범하여, 게이트 직하부 전하의 양쪽 귀퉁이를 가로채어 지탱함.</li>
              <li><strong>[기하학]</strong> 게이트가 순수하게 제어해야 하는 전하 영역이 직사각형($L \times W_{dep}$)에서 <strong>'사다리꼴(Trapezoid)'</strong>로 축소됨.</li>
              <li><strong>[실효 두께]</strong> 줄어든 사다리꼴 전하량을 게이트 길이 $L$ 전체에 걸쳐 평균 두께로 환산하면, <strong>실효 두께 $W_{dep,eff} = W_{dep}(1 - \frac{\Delta L}{2L}) < W_{dep}$로 얇아지는 효과(Thinning)</strong>가 발생함.</li>
              <li><strong>[커패시턴스]</strong> 등가 평행판 커패시턴스는 두께에 반비례($C = \frac{\epsilon}{W}$)하므로, 분모인 실효 두께가 얇아져 <strong>유효 공핍 커패시턴스($C_{dep,eff}$)는 역수로 치솟아 상승</strong>하게 됨!</li>
            </ol>
          </div>
        </div>

        <!-- Section 2: Yau's Charge Sharing Model Details -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 메커니즘 ① : 직사각형에서 사다리꼴로의 기하학적 전하 분할
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            트랜지스터의 게이트 아래 공핍 전하를 전계의 출처별로 분리해 보겠습니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#fde047; margin:14px 0 8px;">■ 장채널 (Long-channel, 1차원 모델)</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:10px;">
            게이트 길이 $L$이 공핍층 폭보다 압도적으로 길 때($L \gg W_{dep}$), 소스와 드레인 가장자리의 영향은 전체 면적 대비 0.1% 미만으로 무시할 수 있습니다.<br>
            게이트 산화막 아래 형성된 공핍 영역은 완벽한 **직사각형($L \times W_{dep}$)**이며, 이 영역 내의 모든 고정 이온 전하($Q_{B,1D} = -q N_A W L W_{dep}$)는 100% 게이트 전압($V_G$)의 수직 전계에 의해서만 통제됩니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#38bdf8; margin:14px 0 8px;">■ 단채널 (Short-channel, 2차원 사다리꼴 분할)</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:10px;">
            하지만 게이트 길이 $L$이 수십 나노미터 수준으로 짧아지면, 소스($X_j$)와 드레인($X_j$)의 P-N 접합 공핍층이 4분원 형태로 채널 내부로 깊숙이 파고듭니다:
          </p>
          <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:20px; margin-bottom:12px;">
            <li>소스 쪽 4분원 공핍 전하는 소스의 빌트인 전위($V_{bi}$)가 지탱합니다.</li>
            <li>드레인 쪽 4분원 공핍 전하는 드레인 전위($V_{bi} + V_{DS}$)가 지탱합니다.</li>
            <li>그 결과, 게이트 바로 아래에 있는 공핍 전하 중 **양쪽 귀퉁이의 전하를 소스와 드레인이 대신 가로채어 지탱(Charge Sharing)**해 줍니다!</li>
            <li>따라서 **게이트가 온전히 책임져야 하는 순수 공핍 전하 영역은 '사다리꼴(Trapezoid)'**이 됩니다:
              <br>• 사다리꼴 윗변 = 게이트 길이 $L$
              <br>• 사다리꼴 아랫변 = $L' = L - \Delta L < L$
              <br>• 사다리꼴의 평균 유효 길이:
              $$L_{avg} = \frac{L + L'}{2} = L \left( 1 - \frac{\Delta L}{2L} \right) < L$$
            </li>
          </ul>
        </div>

        <!-- Section 3: Why Wdep,eff Thins and Cdep Increases -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 메커니즘 ② : 실효 두께 축소(Thinning)의 수학적 유도와 $C_{dep}$ 상승
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            이제 질문하신 **"왜 실효 두께($W_{dep,eff}$)가 얇아진다고 하며, 왜 $C_{dep}$가 올라가는가?"**를 수학적으로 엄밀히 유도해 보겠습니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#fde047; margin:14px 0 8px;">■ Step 1 : 실효 공핍층 두께($W_{dep,eff}$)의 수학적 정의</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:10px;">
            게이트 전극의 물리적 면적은 여전히 $(W \times L)$입니다. 하지만 게이트가 실제로 제어하는 총 공핍 전하량 $Q_{B,eff}$는 사다리꼴 부피에 해당합니다:
            $$|Q_{B,eff}| = q N_A \cdot [L_{avg} \times W_{dep}] \cdot W = q N_A L W_{dep} \left( 1 - \frac{\Delta L}{2L} \right) \cdot W$$
            게이트 관점에서 '물리적 면적($W \times L$)'으로 나눈 **등가 평균 공핍층 두께**를 **실효 공핍층 두께($W_{dep,eff}$)**라고 정의합니다:
            $$W_{dep,eff} \equiv \frac{|Q_{B,eff}|}{q N_A L W} = W_{dep} \times \frac{L_{avg}}{L} = W_{dep} \times \left( 1 - \frac{\Delta L}{2L} \right)$$
            여기서 $\left( 1 - \frac{\Delta L}{2L} \right) < 1$ 이므로, <strong>실효 두께 $W_{dep,eff}$는 원래 1차원 공핍층 두께 $W_{dep}$보다 항상 얇아집니다!</strong> 이것을 소자 물리학에서 **공핍층 실효 박막화(Depletion Layer Thinning Effect)**라고 부릅니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#34d399; margin:14px 0 8px;">■ Step 2 : 유효 공핍 커패시턴스($C_{dep,eff}$)의 상승 유도</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            단위 면적당 유효 공핍 커패시턴스는 게이트 면적당 공핍층 두께에 반비례하는 평행판 모델로 표현됩니다:
            $$C_{dep,eff} = \frac{\epsilon_{si}}{W_{dep,eff}} = \frac{\epsilon_{si}}{W_{dep} \left( 1 - \frac{\Delta L}{2L} \right)} = \frac{C_{dep,1D}}{1 - \frac{\Delta L}{2L}}$$
            분모인 $\left( 1 - \frac{\Delta L}{2L} \right)$이 1보다 작기 때문에, **유효 공핍 커패시턴스 $C_{dep,eff}$는 장채널의 $C_{dep,1D}$보다 명백하게 상승(증가)**하게 됩니다!
          </p>
        </div>

        <!-- Section 4: 2D Field Coupling and SS Degradation -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#ef4444; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. 메커니즘 ③ : 2차원 수평 전계 침투(DIBL)와 서브스레시홀드 스윙(SS) 폭등
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            기하학적 사다리꼴 효과 외에도, **드레인의 2차원 수평 전계 침투**가 유효 커패시턴스를 한 번 더 증폭시킵니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#fde047; margin:14px 0 8px;">■ DIBL에 의한 측면 정전용량 결합 (Capacitive Coupling)</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:10px;">
            단채널에서는 드레인에 인가된 양(+)의 전압에서 뿜어져 나오는 수평 전기력선이 채널 중앙으로 깊숙이 관통합니다(**DIBL: Drain-Induced Barrier Lowering**).<br>
            이로 인해 게이트 전압이 표면 전위($\psi_s$)를 조금만 흔들어도, 게이트 직하부뿐만 아니라 **소스와 드레인의 측면 공핍층 경계 전하가 2차원적으로 함께 출렁거리며 결합**됩니다:
            $$C_{dep,2D} = \frac{\partial Q_{total}}{\partial \psi_s} = C_{dep,ch} + C_{d-coupling}$$
            드레인 정전용량 결합 성분이 채널 노드에 병렬로 더해져 유효 $C_{dep}$가 기하학적 계산치보다도 훨씬 가파르게 치솟습니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#f87171; margin:14px 0 8px;">■ 최종 파국: 서브스레시홀드 스윙(SS) 악화와 대기 누설전류 폭발</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            게이트 산화막 커패시터($C_{ox}$)와 공핍 커패시터($C_{dep,eff}$)의 직렬 전압 분배 회로에서:
            $$\frac{\partial \psi_s}{\partial V_G} = \frac{C_{ox}}{C_{ox} + C_{dep,eff}} = \frac{1}{1 + \frac{C_{dep,eff}}{C_{ox}}}$$
            $$SS = \ln(10) \frac{kT}{q} \left( 1 + \frac{C_{dep,eff}}{C_{ox}} \right) \approx 60 \times \left( 1 + \frac{C_{dep,eff}}{C_{ox}} \right) \text{ [mV/dec]}$$
            * $W_{dep,eff}$ 축소(Thinning)로 인해 **분자인 $C_{dep,eff}$가 폭증**하므로, 게이트 전압의 전달 효율이 급격히 떨어집니다.
            * 결과적으로 **$SS$가 정상치인 $65\,\text{mV/dec}$에서 $85 \sim 110\,\text{mV/dec}$ 이상으로 치솟아**, 트랜지스터를 꺼도 전류가 완전히 닫히지 않는 **치명적인 오프 누설전류($I_{off}$) 폭발**이 발생하게 됩니다!
          </p>
        </div>

        <!-- Section 5: Summary Table -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.15rem; font-weight:800; color:#e2e8f0; margin-bottom:12px;">
            5. 핵심 요약 비교 정리표
          </h3>
          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">구분 단계</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">1차원 장채널 (Long-L)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">2차원 단채널 (Short-L)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">물리적 의미 및 수식</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">1. 전하 영역 형태</td>
                  <td style="padding:10px 14px;">직사각형 ($L \times W_{dep}$)</td>
                  <td style="padding:10px 14px; color:#fde047; font-weight:700;">사다리꼴 ($L_{avg} \times W_{dep}$)</td>
                  <td style="padding:10px 14px;">S/D 4분원 공핍층이 양 귀퉁이 전하를 가로챔 (Charge Sharing)</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#34d399;">2. 게이트 유효 전하 ($Q_B$)</td>
                  <td style="padding:10px 14px;">$|Q_{B,1D}| = q N_A L W_{dep} W$</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">$|Q_{B,eff}| = |Q_{B,1D}| \cdot (1 - \frac{\Delta L}{2L})$</td>
                  <td style="padding:10px 14px;">게이트가 지탱할 전하 감소 ➔ <strong>문턱전압 강하 (Vt Roll-off)</strong></td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fbbf24;">3. 실효 두께 ($W_{dep,eff}$)</td>
                  <td style="padding:10px 14px;">$W_{dep,eff} = W_{dep}$ (일정)</td>
                  <td style="padding:10px 14px; color:#ef4444; font-weight:700;">$W_{dep,eff} = W_{dep} \cdot (1 - \frac{\Delta L}{2L}) < W_{dep}$</td>
                  <td style="padding:10px 14px;">게이트 길이 $L$ 기준 평균 두께 환산 시 <strong>두께 축소 (Thinning)</strong></td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#f87171;">4. 유효 커패시턴스 ($C_{dep}$)</td>
                  <td style="padding:10px 14px;">$C_{dep,1D} = \epsilon_{si} / W_{dep}$</td>
                  <td style="padding:10px 14px; color:#ef4444; font-weight:700;">$C_{dep,eff} = \frac{C_{dep,1D}}{1 - \Delta L / (2L)} > C_{dep,1D}$</td>
                  <td style="padding:10px 14px;">분모(실효 두께) 감소로 인해 <strong>유효 Cdep 가파르게 상승</strong></td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#c084fc;">5. 최종 소자 영향</td>
                  <td style="padding:10px 14px; color:#34d399;">$SS \approx 65 \sim 70\,\text{mV/dec}$ (우수)</td>
                  <td style="padding:10px 14px; color:#ef4444; font-weight:700;">$SS \approx 85 \sim 110\,\text{mV/dec}$ (악화)</td>
                  <td style="padding:10px 14px;">게이트 제어력 상실 ➔ <strong>오프 누설전류($I_{off}$) 폭발</strong></td>
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

    # Step 1: Shift existing 84 topics (q-84 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(84, 0, -1):
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

    # Step 4: Update header description to 85 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 '2차원 전하 분할(Charge Sharing)과 실효 두께 축소(Thinning) 상세'이 위치하며, 총 85개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Charge Sharing and Thinning topic!")
