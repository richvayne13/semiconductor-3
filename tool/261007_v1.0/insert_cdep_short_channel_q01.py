# -*- coding: utf-8 -*-
"""
insert_cdep_short_channel_q01.py
사용자 질문: "채널이 짧아지면 공핍커패시턴스가 왜 올라가?"
대시보드 최상단 Q01로 신규 추가하고, 기존 78개 질문을 Q02~Q79로 시프트 (총 79개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (단채널 효과 · 소자 커패시턴스 물리)",
    "title": "채널이 짧아지면 공핍 커패시턴스(Cdep)가 왜 올라갈까? (Halo 도핑, 2D 전하 분할, SS 악화 메커니즘)",
    "nav_title": "채널이 짧아지면 공핍 커패시턴스가 왜 올라갈까? (Cdep 증가 원리)",
    "summary": [
        "<strong>1. 펀치스루 억제를 위한 고농도 도핑 (데나드 스케일링 & Halo)</strong>: 채널 길이($L$)가 줄어들 때 소스-드레인 간 단락(Punchthrough) 및 DIBL을 막기 위해 <strong>채널/기판 도핑 농도($N_A$)를 강제로 높이거나 국소 Halo 도핑을 주입</strong>합니다. 공핍층 두께는 $W_{dep} = \\sqrt{\\frac{2\\epsilon_{si}(2\\phi_B)}{q N_A}}$이므로, <strong>도핑 농도 $N_A$가 증가하면 공핍층이 얇아져 단위 면적당 공핍 커패시턴스($C_{dep} = \\frac{\\epsilon_{si}}{W_{dep}} \\propto \\sqrt{N_A}$)가 직접 상승</strong>합니다.",
        "<strong>2. 2차원 전하 분할 (Charge Sharing)과 실효 두께 축소</strong>: 단채널에서는 소스와 드레인 접합 공핍층이 채널 중앙으로 깊숙이 침범합니다. 게이트 아래 공핍 전하를 소스/드레인이 나누어 부담하면서, 2차원 전계 효과로 인해 <strong>게이트가 바라보는 실효 공핍층 두께($W_{dep,eff}$)가 장채널보다 얇아지는 효과(Thinning)</strong>가 발생하여 유효 $C_{dep}$가 상승합니다.",
        "<strong>3. 에지/측벽 기생 접합 커패시턴스의 상대적 비중 폭증</strong>: $L$이 줄어들면 채널 면적($W \\times L$)은 축소되어 총 게이트 산화막 커패시턴스($C_{ox,total}$)는 줄어들지만, <strong>소스/드레인 측벽 접합 공핍 커패시턴스($C_{j,sw}$)는 줄어들지 않아</strong> 전체 소자에서 공핍층 기생 커패시턴스가 차지하는 비중과 간섭이 극적으로 커집니다.",
        "<strong>치명적 결과: 서브스레시홀드 스윙(SS) 악화</strong>: 정전용량 전압 분배 비율인 $m = 1 + \\frac{C_{dep}}{C_{ox}}$에서 <strong>$C_{dep}$가 증가하면 $SS = 60 \\times m \\text{ [mV/dec]}$가 70~100mV/dec로 치솟아</strong> 트랜지스터를 끌 때의 오프 누설전류(Off-leakage)가 폭발합니다 (FinFET/GAA 무도핑 채널 도입의 결정적 이유)."
    ],
    "svg_title": "📊 [공핍 커패시턴스 Cdep 상승 3대 메커니즘] (A) Halo 도핑과 Wdep 축소 | (B) 2D 전하 분할(Charge Sharing) | (C) 용량 분배기와 SS 악화",
    "svg": """<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Doping Scaling & Wdep Thinning -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 스케일링 &amp; Halo 고농도 도핑</text>

    <!-- Long Channel Case -->
    <g transform="translate(15, 42)">
      <rect width="270" height="110" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="16" fill="#94a3b8" font-size="9" font-weight="700">1. 장채널 (Long-L): 저농도 기판 (NA 낮음)</text>
      <!-- Gate -->
      <rect x="75" y="25" width="120" height="12" fill="#64748b" rx="2"/>
      <text x="110" y="34" fill="#fff" font-size="7.5">Gate (L 크다)</text>
      <!-- Substrate -->
      <rect x="25" y="37" width="220" height="60" fill="#047857" opacity="0.6"/>
      <!-- Depletion region (Thick) -->
      <rect x="40" y="37" width="190" height="32" fill="#0284c7" opacity="0.4" stroke="#38bdf8" stroke-dasharray="2,2"/>
      <text x="75" y="56" fill="#e0f2fe" font-size="8.5" font-weight="700">두꺼운 공핍층 (W_dep 크다)</text>
      <text x="75" y="68" fill="#bae6fd" font-size="7.5">➔ C_dep = ε/W_dep [낮음 (안정)]</text>
    </g>

    <!-- Short Channel Case with Halo -->
    <g transform="translate(15, 162)">
      <rect width="270" height="135" rx="5" fill="#1e293b" stroke="#ef4444"/>
      <text x="12" y="16" fill="#f87171" font-size="9" font-weight="800">2. 단채널 (Short-L): 펀치스루 방어용 고농도 도핑!</text>
      <!-- Gate -->
      <rect x="100" y="25" width="70" height="12" fill="#ef4444" rx="2"/>
      <text x="116" y="34" fill="#fff" font-size="7.5">Gate (L 짧음)</text>
      <!-- Source / Drain -->
      <rect x="45" y="37" width="45" height="32" fill="#f59e0b" rx="2"/>
      <text x="56" y="54" fill="#000" font-size="7.5" font-weight="800">Source</text>
      <rect x="180" y="37" width="45" height="32" fill="#f59e0b" rx="2"/>
      <text x="193" y="54" fill="#000" font-size="7.5" font-weight="800">Drain</text>
      <!-- Halo P+ pockets -->
      <circle cx="95" cy="55" r="14" fill="#a855f7" opacity="0.6"/>
      <circle cx="175" cy="55" r="14" fill="#a855f7" opacity="0.6"/>
      <text x="96" y="80" fill="#d8b4fe" font-size="7.5" font-weight="700">Halo 고농도 도핑 (NA ↑)</text>
      <!-- Thin Depletion layer -->
      <rect x="90" y="37" width="90" height="15" fill="#0284c7" opacity="0.6" stroke="#ef4444" stroke-width="1.5"/>
      <text x="96" y="47" fill="#fff" font-size="7.5" font-weight="800">W_dep 급감!</text>
      <text x="12" y="102" fill="#fca5a5" font-size="8">• NA 증가로 공핍층 두께 W_dep 강제 축소!</text>
      <text x="12" y="118" fill="#fde047" font-size="8.5" font-weight="800">★ C_dep = ε_si / W_dep ∝ √(NA) ➔ 급상승!</text>
    </g>

    <!-- Formula Box -->
    <rect x="15" y="310" width="270" height="96" rx="6" fill="#0b1329" stroke="#334155"/>
    <text x="25" y="330" fill="#38bdf8" font-size="9" font-weight="800">수식으로 증명하는 물리적 관계:</text>
    <text x="25" y="350" fill="#cbd5e1" font-size="8.5">W_dep = √[ (2ε_si · 2φ_B) / (q · NA) ]</text>
    <text x="25" y="370" fill="#fde047" font-size="8.5" font-weight="700">C_dep = ε_si / W_dep = √[ (q ε_si NA) / (2φ_B) ]</text>
    <text x="25" y="392" fill="#a5f3fc" font-size="8">L 축소 ➔ NA 강제 상향 ➔ W_dep 축소 ➔ C_dep 상승!</text>
  </g>

  <!-- PANEL B: 2D Charge Sharing & Field Coupling -->
  <g transform="translate(340, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 2D 전하 분할 (Charge Sharing 모델)</text>

    <!-- Charge Sharing Diagram -->
    <g transform="translate(15, 42)">
      <rect width="280" height="175" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#34d399" font-size="9.5" font-weight="700">야우(Yau)의 2차원 사다리꼴 전하 분할</text>

      <!-- Gate Oxide & Gate -->
      <rect x="50" y="32" width="180" height="10" fill="#475569" rx="1"/>
      <text x="110" y="40" fill="#fff" font-size="7">Gate Electrode</text>
      <rect x="50" y="42" width="180" height="4" fill="#a855f7"/>

      <!-- Source / Drain Depletion Regions -->
      <!-- Source -->
      <rect x="20" y="46" width="45" height="45" fill="#f59e0b"/>
      <text x="30" y="70" fill="#000" font-size="8" font-weight="800">Source</text>
      <!-- Drain -->
      <rect x="215" y="46" width="45" height="45" fill="#f59e0b"/>
      <text x="228" y="70" fill="#000" font-size="8" font-weight="800">Drain</text>

      <!-- Trapezoidal Depletion Region controlled by Gate -->
      <!-- Source depletion quarter circle -->
      <path d="M 65 46 A 35 35 0 0 1 65 110 L 20 110 L 20 46 Z" fill="#ef4444" opacity="0.3"/>
      <!-- Drain depletion quarter circle -->
      <path d="M 215 46 A 45 45 0 0 0 215 125 L 260 125 L 260 46 Z" fill="#ef4444" opacity="0.3"/>

      <!-- Gate Controlled Trapezoid in Center -->
      <polygon points="65,46 215,46 185,100 95,100" fill="#0284c7" opacity="0.6" stroke="#38bdf8"/>
      <text x="100" y="72" fill="#fff" font-size="8" font-weight="800">게이트 제어 전하 Q_G</text>
      <text x="85" y="86" fill="#bae6fd" font-size="7.5">(채널이 짧으면 면적 급감!)</text>

      <!-- Overlap arrow -->
      <text x="12" y="132" fill="#fca5a5" font-size="8">• S/D 공핍층이 채널 아래로 깊숙이 침범(빨간 영역)</text>
      <text x="12" y="146" fill="#cbd5e1" font-size="8">• 게이트가 통제하는 공핍 전하 Q_G의 사다리꼴 폭 축소</text>
      <text x="12" y="160" fill="#fde047" font-size="8">• 소스/드레인 2D 전계에 의해 실효 W_dep,eff 감소</text>
    </g>

    <!-- Fringing / Lateral Capacitance Box -->
    <g transform="translate(15, 230)">
      <rect width="280" height="176" rx="6" fill="#0b1329" stroke="#334155"/>
      <text x="12" y="18" fill="#34d399" font-size="9" font-weight="800">★ 2차원 프린징 전계와 측벽 커패시턴스 효과:</text>
      <text x="12" y="38" fill="#cbd5e1" font-size="8.5">1. 수직 1차원 전계 가정 붕괴:</text>
      <text x="20" y="52" fill="#94a3b8" font-size="7.8">단채널에서는 소스/드레인에서 나온 수평 전기선이</text>
      <text x="20" y="64" fill="#94a3b8" font-size="7.8">채널 중앙의 장벽을 무너뜨림 (DIBL).</text>

      <text x="12" y="84" fill="#cbd5e1" font-size="8.5">2. 측벽 접합 커패시턴스(Cj,sw)의 상대적 비중 폭증:</text>
      <text x="20" y="98" fill="#94a3b8" font-size="7.8">채널 면적(W×L)이 줄어도 접합 깊이(Xj)에 의한</text>
      <text x="20" y="110" fill="#94a3b8" font-size="7.8">측벽 공핍층은 그대로 남아 상대적 비율이 치솟음!</text>

      <text x="12" y="130" fill="#fde047" font-size="8.5" font-weight="700">3. 결과: 단위 면적당 유효 Cdep,eff 상승!</text>
      <text x="20" y="144" fill="#a7f3d0" font-size="8">Cdep,eff = dQ_dep / dψ_s 에서 소스/드레인의 전하 변조가</text>
      <text x="20" y="158" fill="#a7f3d0" font-size="8">더해져 게이트 전위 변화당 전하 민감도가 극대화됨.</text>
    </g>
  </g>

  <!-- PANEL C: Voltage Divider & Subthreshold Swing (SS) -->
  <g transform="translate(670, 20)">
    <rect width="290" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) 용량 분배기와 서브스레시홀드 스윙(SS)</text>

    <!-- Circuit Diagram of Capacitive Divider -->
    <g transform="translate(15, 42)">
      <rect width="260" height="145" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="12" y="18" fill="#fde047" font-size="9" font-weight="700">정전용량 전압 분배 회로 (Capacitive Divider)</text>

      <!-- Gate Node -->
      <circle cx="130" cy="32" r="4" fill="#38bdf8"/>
      <text x="140" y="35" fill="#38bdf8" font-size="8" font-weight="700">Gate (VG)</text>
      <!-- Line to Cox -->
      <line x1="130" y1="36" x2="130" y2="48" stroke="#cbd5e1" stroke-width="1.5"/>

      <!-- Cox Capacitor -->
      <rect x="110" y="48" width="40" height="14" fill="#0284c7" rx="1"/>
      <text x="118" y="59" fill="#fff" font-size="8" font-weight="800">Cox</text>
      <line x1="130" y1="62" x2="130" y2="76" stroke="#cbd5e1" stroke-width="1.5"/>

      <!-- Surface Potential Node psi_s -->
      <circle cx="130" cy="76" r="4" fill="#10b981"/>
      <text x="142" y="80" fill="#34d399" font-size="8" font-weight="800">표면 전위 ψs</text>
      <line x1="130" y1="80" x2="130" y2="92" stroke="#cbd5e1" stroke-width="1.5"/>

      <!-- Cdep Capacitor -->
      <rect x="110" y="92" width="40" height="14" fill="#ef4444" rx="1"/>
      <text x="116" y="103" fill="#fff" font-size="8" font-weight="800">Cdep ↑</text>
      <line x1="130" y1="106" x2="130" y2="118" stroke="#cbd5e1" stroke-width="1.5"/>

      <!-- Ground / Body Node -->
      <line x1="118" y1="118" x2="142" y2="118" stroke="#cbd5e1" stroke-width="2"/>
      <text x="148" y="122" fill="#94a3b8" font-size="7.5">Body (GND)</text>

      <!-- Divider formula -->
      <text x="12" y="137" fill="#fde047" font-size="8" font-weight="700">전압 분배율: ∂ψs / ∂VG = Cox / (Cox + Cdep)</text>
    </g>

    <!-- Impact on SS & Leakage -->
    <g transform="translate(15, 200)">
      <rect width="260" height="206" rx="6" fill="#0b1329" stroke="#ef4444"/>
      <text x="12" y="18" fill="#f87171" font-size="9.5" font-weight="800">치명적 결과: SS 급증 및 오프 누설전류 폭발</text>

      <text x="12" y="38" fill="#fde047" font-size="9" font-weight="800">■ 서브스레시홀드 스윙 공식:</text>
      <text x="18" y="55" fill="#ffffff" font-size="9">SS = 2.3 (kT/q) · [ 1 + (Cdep / Cox) ]</text>

      <text x="12" y="76" fill="#cbd5e1" font-size="8">• Cdep가 작을수록(0에 가까울수록):</text>
      <text x="20" y="90" fill="#34d399" font-size="8">➔ 이상적 한계치 SS = 60 mV/dec (스위치 예리함)</text>

      <text x="12" y="108" fill="#fca5a5" font-size="8">• 단채널로 Cdep가 급상승하면:</text>
      <text x="20" y="122" fill="#ef4444" font-size="8" font-weight="700">➔ SS = 80~100 mV/dec로 악화! (게이트 제어 상실)</text>
      <text x="20" y="136" fill="#cbd5e1" font-size="7.8">➔ 트랜지스터 끌 때 문턱하 누설전류 I_off 수백 배 폭증!</text>

      <rect x="10" y="152" width="240" height="44" rx="4" fill="#1e293b" stroke="#38bdf8"/>
      <text x="16" y="168" fill="#38bdf8" font-size="8" font-weight="800">💡 차세대 해결책: FinFET &amp; GAA 3D 채널</text>
      <text x="16" y="184" fill="#cbd5e1" font-size="7.5">도핑 없이 게이트가 전면 포위 ➔ Cdep 극소화, SS 60 복원!</text>
    </g>
  </g>
</svg>""",
    "lecture": """
        <!-- Section 1: Introduction & The Core Puzzle -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 직관의 함정과 질문의 본질: "채널이 짧아지는데 왜 공핍 커패시턴스($C_{dep}$)가 올라갈까?"
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체를 처음 공부할 때 흔히 빠지는 직관적 함정이 있습니다:<br>
            <em>"채널 길이($L$)가 짧아지면 트랜지스터 면적($W \times L$)이 줄어드니까, 커패시터 평행판 면적이 줄어들어 정전용량(커패시턴스)도 줄어들어야 하는 것 아닌가?"</em><br>
            하지만 실제 단채널 트랜지스터의 소자 물리를 들여다보면 <strong>단위 면적당 공핍 커패시턴스($C_{dep}$) 및 유효 공핍 커패시턴스는 오히려 급격히 '상승(증가)'</strong>합니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:14px 18px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:700; margin-bottom:8px;">💡 핵심 결론 한 줄 요약</h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              채널이 짧아지면 단채널 효과(Punchthrough, DIBL)로 인해 소자와 드레인이 맞닿아 무너지는 것을 막기 위해 <strong>공학적으로 채널/기판 도핑 농도($N_A$)를 극단적으로 올리거나 Halo(Pocket) 고농도 도핑을 주입</strong>합니다. 도핑 농도가 올라가면 공핍층 두께($W_{dep}$)가 얇아지므로, <strong>$C_{dep} = \frac{\epsilon_{si}}{W_{dep}} \propto \sqrt{N_A}$ 공식에 의해 공핍 커패시턴스가 상승</strong>하게 됩니다! 여기에 소스/드레인의 2차원 전하 분할(Charge Sharing) 효과가 겹쳐 실효 공핍 커패시턴스가 더욱 커집니다.
            </p>
          </div>
        </div>

        <!-- Section 2: Mechanism 1 - Scaling & Doping Concentration Increase -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 메커니즘 ① : 데나드 스케일링 법칙과 Halo 도핑에 의한 $W_{dep}$ 축소
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            트랜지스터의 채널 길이($L$)를 줄일 때 가장 먼저 발생하는 치명적인 단채널 효과는 <strong>펀치스루(Punchthrough)</strong>입니다. 소스의 공핍층과 드레인의 공핍층이 채널 중앙에서 서로 맞닿아 게이트의 통제를 벗어나 전류가 제멋대로 흐르는 현상입니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#fde047; margin:14px 0 8px;">■ 데나드 스케일링 룰 (Dennard's Scaling Rule)</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            펀치스루를 막으려면 소스와 드레인의 공핍층 폭을 강제로 억누르고 줄여야 합니다. 이를 위한 유일한 방법은 **채널 및 기판의 도핑 농도($N_A$)를 비례해서 높이는 것**입니다:
            $$L \rightarrow \frac{L}{\kappa} \implies N_A \rightarrow \kappa \times N_A \quad (\kappa > 1)$$
            또한 현대 미세 공정에서는 채널 양 끝 접합부 부근에 고농도 P형 불순물을 집중 주입하는 **헤일로(Halo / Pocket) 도핑**을 필수적으로 사용합니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#38bdf8; margin:14px 0 8px;">■ 도핑 농도($N_A$)와 공핍 커패시턴스($C_{dep}$)의 물리 수식 유도</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:10px;">
            MOS 구조에서 최대 공핍층 두께($W_{dep,max}$) 공식은 푸아송 방정식에 의해 다음과 같이 결정됩니다:
            $$W_{dep} = \sqrt{\frac{2\epsilon_{si}(2\phi_B)}{q N_A}} \propto \frac{1}{\sqrt{N_A}}$$
            여기서 도핑 농도 $N_A$가 증가하면 고정 전하(Space Charge) 밀도가 높아져 전하 중성 조건을 금방 만족하므로 <strong>공핍층 두께($W_{dep}$)가 급격히 얇아집니다</strong>.
          </p>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            단위 면적당 공핍 커패시턴스는 절연체 역할을 하는 공핍층의 두께에 반비례하는 평행판 커패시터 모델을 따릅니다:
            $$C_{dep} = \frac{\epsilon_{si}}{W_{dep}} = \sqrt{\frac{q \epsilon_{si} N_A}{2\phi_B}} \propto \sqrt{N_A}$$
            따라서 **채널이 짧아질수록 도핑 농도 $N_A$를 높여야만 하고, 이에 따라 공핍층 두께 $W_{dep}$가 얇아져 공핍 커패시턴스 $C_{dep}$는 필연적으로 상승**하게 됩니다!
          </p>
        </div>

        <!-- Section 3: Mechanism 2 - 2D Charge Sharing and Effective Depletion Layer Thinning -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 메커니즘 ② : 2차원 전하 분할(Charge Sharing)과 실효 두께 축소
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            도핑 농도를 동일하게 유지한다고 가정하더라도, 순수한 <strong>기하학적 2차원 전계 효과(2D Field Effect)</strong>만으로도 유효 공핍 커패시턴스가 상승합니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #f59e0b; padding:14px 18px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#fbbf24; font-size:1rem; font-weight:700; margin-bottom:8px;">💡 야우의 전하 분할 모델 (Yau's Charge Sharing Model)</h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:18px;">
              <li><strong>장채널(Long Channel)</strong>: 채널 아래의 공핍 전하($Q_{dep}$)는 100% 게이트 전압($V_G$)에 의해서만 통제됩니다. 소스와 드레인의 가장자리 전하 침범은 무시할 수 있을 정도로 작습니다.</li>
              <li><strong>단채널(Short Channel)</strong>: 소스와 드레인 접합 공핍층($X_j$)이 채널 내부로 깊숙이 파고듭니다. 게이트 아래에 존재하는 전체 공핍 전하 중 양쪽 끝부분은 소스와 드레인의 빌트인 전위($V_{bi}$)와 드레인 전압($V_D$)이 대신 지탱해 줍니다(전하 공유).</li>
              <li><strong>실효 공핍층 두께 축소 ($W_{dep,eff} \downarrow$)</strong>: 게이트가 제어해야 하는 전하의 기하학적 형태가 직사각형에서 사다리꼴(Trapezoid)로 좁아지며, 드레인의 수평 전기선이 채널 중앙의 에너지 장벽을 끌어내립니다(DIBL). 그 결과 게이트 전위 관점에서 바라보는 <strong>실효 공핍층 폭($W_{dep,eff}$)이 장채널보다 얇아진 것과 동일한 효과</strong>가 발생합니다.</li>
              <li>유효 공핍 커패시턴스는 $C_{dep,eff} = \frac{dQ_{dep}}{d\psi_s}$로 정의되는데, 소스와 드레인의 2차원 전계 침투로 인해 표면 전위 $\psi_s$의 변화에 대한 전하 응답성이 왜곡되어 **유효 $C_{dep}$가 장채널 대비 크게 상승**합니다.</li>
            </ul>
          </div>

          <h4 style="font-size:1rem; font-weight:700; color:#38bdf8; margin:14px 0 8px;">■ 측벽 접합 공핍 커패시턴스($C_{j,sw}$)의 상대적 비중 폭증</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            트랜지스터의 총 커패시턴스 관점에서 보면, 게이트 산화막 면적($W \times L$)에 비례하는 게이트 커패시턴스는 $L$이 줄어듦에 따라 정직하게 감소합니다. 하지만 **소스/드레인의 측벽 접합 공핍 커패시턴스($C_{j,sw} \propto W \times X_j$)는 채널 길이 $L$과 무관하게 그대로 유지**됩니다. 따라서 **전체 소자 용량 중에서 공핍층이 유발하는 기생 커패시턴스의 비율이 압도적으로 커지는 현상**이 발생합니다.
          </p>
        </div>

        <!-- Section 4: Severe Consequences - SS Degradation & Why FinFET/GAA Emerged -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#ef4444; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. $C_{dep}$ 상승이 초래하는 치명적 대재앙: 서브스레시홀드 스윙(SS) 악화와 3D FinFET/GAA로의 진화
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            공핍 커패시턴스($C_{dep}$)가 올라가는 것이 왜 반도체 소자에서 그토록 치명적인 문제일까요? 그 해답은 **정전용량 전압 분배 회로(Capacitive Voltage Divider)**에 있습니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#fde047; margin:14px 0 8px;">■ 게이트와 공핍층의 전압 분배 (Body Effect & Body Factor)</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:10px;">
            게이트에 전압 $V_G$를 가했을 때, 채널 표면의 전위 $\psi_s$를 끌어올리는 효율은 게이트 산화막 커패시터($C_{ox}$)와 공핍층 커패시터($C_{dep}$)의 직렬 분배비로 결정됩니다:
            $$\frac{\partial \psi_s}{\partial V_G} = \frac{C_{ox}}{C_{ox} + C_{dep}} = \frac{1}{1 + \frac{C_{dep}}{C_{ox}}} = \frac{1}{m}$$
            이상적인 트랜지스터라면 게이트 전압을 $1\text{V}$ 걸었을 때 채널 표면 전위도 $1\text{V}$ 그대로 움직여야 합니다 ($\frac{\partial \psi_s}{\partial V_G} = 1$). 그러려면 **$C_{dep} \rightarrow 0$**이어야 합니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#f87171; margin:14px 0 8px;">■ 서브스레시홀드 스윙(SS)의 악화와 누설전류 폭발</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            드레인 전류를 10배(1 decade) 변화시키는 데 필요한 게이트 전압을 나타내는 지표인 $SS$ 공식은 다음과 같습니다:
            $$SS = \ln(10) \frac{kT}{q} \left( 1 + \frac{C_{dep}}{C_{ox}} \right) \approx 60 \times \left( 1 + \frac{C_{dep}}{C_{ox}} \right) \text{ [mV/dec]}$$
            * **장채널 (낮은 $C_{dep}$)**: $\frac{C_{dep}}{C_{ox}}$ 비율이 작아 상온에서 $SS \approx 65 \sim 70\text{ mV/dec}$로 이상적인 스위칭 특성을 가집니다.
            * **단채널 (상승한 $C_{dep}$)**: 도핑 증가와 2D 전하 분할로 **$C_{dep}$가 폭증하면서 $SS$가 $85 \sim 110\text{ mV/dec}$ 이상으로 급격히 악화**됩니다!
            * **결과**: 트랜지스터를 'OFF' 상태로 두어도 게이트가 채널을 완전히 닫지 못해 **대기 누설전류(Off-state Leakage Current, $I_{off}$)가 수백 배 폭증**하고, 칩이 뜨거워져 배터리가 광속으로 소모됩니다.
          </p>

          <div style="background:#090d1a; border:1px solid #10b981; border-radius:10px; padding:16px; margin-top:16px;">
            <h4 style="color:#34d399; font-size:0.95rem; font-weight:800; margin-bottom:8px;">🚀 인류가 찾아낸 궁극의 해결책: FinFET, GAA, 그리고 FD-SOI</h4>
            <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin-bottom:0;">
              평면(Planar) MOSFET에서는 단채널 효과를 막으려 도핑을 올렸더니 $C_{dep}$가 올라가 $SS$가 망가지는 딜레마에 빠졌습니다. 이를 타파하기 위해:<br>
              1. <strong>FD-SOI</strong>: 실리콘 채널 박막 두께($t_{si}$)를 극단적으로 얇게 깎아 공핍층 전하를 원천 차단함으로써 $C_{dep} \approx 0$ 달성.<br>
              2. <strong>FinFET & GAA (나노시트)</strong>: 게이트가 핀(Fin)의 3면, 나노시트의 4면을 완전히 감싸(Gate-All-Around) 기하학적 정전 제어력을 극대화하여, **채널에 불순물 도핑을 전혀 하지 않는 '무도핑 채널(Undoped Channel)'**을 실현! 무도핑이므로 $C_{dep}$가 최소화되어 $SS \approx 60\text{ mV/dec}$의 이상적인 스위칭을 완벽히 복원하였습니다.
            </p>
          </div>
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
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">구분 요인</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">장채널 (Long-L)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">단채널 (Short-L)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">Cdep 및 소자 특성 영향</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">기판/채널 도핑 농도 ($N_A$)</td>
                  <td style="padding:10px 14px;">저농도 균일 도핑</td>
                  <td style="padding:10px 14px; color:#ef4444; font-weight:700;">고농도 기판 도핑 &amp; 국소 Halo 도핑</td>
                  <td style="padding:10px 14px;">$W_{dep} \propto 1/\sqrt{N_A}$ 축소 ➔ <strong>$C_{dep} \propto \sqrt{N_A}$ 직접 상승</strong></td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#34d399;">2차원 전하 분할 (Charge Sharing)</td>
                  <td style="padding:10px 14px;">1차원 수직 전계 지배 (게이트가 100% 제어)</td>
                  <td style="padding:10px 14px; color:#f59e0b;">S/D 공핍층 채널 침범 (2D 전계 간섭, DIBL)</td>
                  <td style="padding:10px 14px;">게이트 유효 $W_{dep,eff}$ 왜곡 축소 ➔ <strong>유효 $C_{dep,eff}$ 추가 상승</strong></td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fbbf24;">측벽 접합 커패시턴스 비율</td>
                  <td style="padding:10px 14px;">채널 면적 대비 무시할 수 있는 수준</td>
                  <td style="padding:10px 14px;">채널 면적($W \times L$) 급감으로 상대적 비중 폭증</td>
                  <td style="padding:10px 14px;">소자 전체 정전용량 중 <strong>공핍층 기생 성분 기여도 급상승</strong></td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#f87171;">서브스레시홀드 스윙 ($SS$)</td>
                  <td style="padding:10px 14px; color:#34d399;">$SS \approx 65 \sim 70\text{ mV/dec}$ (우수)</td>
                  <td style="padding:10px 14px; color:#ef4444; font-weight:700;">$SS \approx 85 \sim 110\text{ mV/dec}$ (악화)</td>
                  <td style="padding:10px 14px;">게이트 제어력 상실, <strong>오프 누설전류($I_{off}$) 폭발</strong></td>
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

    # Step 1: Shift existing 78 topics (q-78 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(78, 0, -1):
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

    # Step 4: Update header description to 79 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 '채널이 짧아지면 공핍 커패시턴스가 왜 올라갈까? (Cdep 증가 원리)'이 위치하며, 총 79개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Cdep Short Channel topic!")
