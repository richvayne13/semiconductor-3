# -*- coding: utf-8 -*-
"""
insert_moscap_op_characteristics_q01.py
사용자 질문:
"mos cap 의 동작특성"

대시보드 최상단 Q01로 신규 추가하고, 기존 88개 질문을 Q02~Q89로 시프트 (총 89개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 기본 물리 · MOS Cap 4대 동작 영역 및 C-V 주파수 특성)",
    "title": "MOS Cap의 동작 특성 완전 정복 (축적·평탄대·공핍·반전 4대 영역, 에너지 밴드, C-V 거동)",
    "nav_title": "MOS Cap의 동작 특성 완전 정복",
    "summary": [
        "<strong>1. 4대 동작 영역과 표면 전위($\\psi_s$) 구분</strong>: 게이트 전압($V_G$)에 따라 ① 축적(Accumulation, $\\psi_s < 0$, 다수캐리어 정공 결집, $C = C_{ox}$), ② 평탄대(Flat-Band, $\\psi_s = 0$, 밴드 휨 제로, $C_{FB}$), ③ 공핍(Depletion, $0 < \\psi_s < 2\\phi_B$, 정공 퇴출 및 공핍층 $W_{dep}$ 확장으로 $C$ 지속 하강), ④ 반전(Inversion, $\\psi_s \\ge 2\\phi_B$, 소수캐리어 전자의 2차원 반전층 형성, $W_{dep} = W_{dep,max}$ 고정)의 4단계로 동작합니다.",
        "<strong>2. 반전 영역의 C-V 3대 주파수 분기</strong>: 소스/드레인이 없어 소수캐리어(전자)의 열 생성 속도($\\tau_{gen} \\sim \\text{ms}$)에 의존하므로, ① 저주파(LF)에서는 전자가 신호를 따라와 $C_{ox}$로 복원되지만, ② 고주파(HF, 100kHz~1MHz)에서는 전자가 못 따라와 최소 용량($C_{min} = \\frac{C_{ox}C_{dep,max}}{C_{ox}+C_{dep,max}}$)에 묶이며, ③ 고속 직류 전압 스위핑 시 전자가 생길 틈이 없어 $C_{min}$ 아래로 추락하는 깊은 공핍(Deep Depletion)이 발생합니다.",
        "<strong>3. 에너지 밴드와 공간 전하 분포의 변화</strong>: 게이트 전압에 따라 페르미 준위($E_F$)와 진성 준위($E_i$)의 상대적 위치가 바뀌며, 반도체 측 공간 전하는 축적 정공($Q_{acc}$) ➔ 고정 수락체 음이온($Q_{dep} = -q N_A W_{dep}$) ➔ 반전 전자($Q_{inv}$)로 연속 변환됩니다.",
        "<strong>4. 팹(FAB) 공정 계측 파라미터 추출의 핵심 도구</strong>: 실무에서는 C-V 곡선의 축적 용량에서 산화막 두께($t_{ox}$), 수평 이동량($\\Delta V = V_{FB}$)에서 산화막 고정전하($Q_f$)와 일함수차($\\Phi_{ms}$), 공핍 기울기에서 기판 도핑 농도($N_A$), 곡선 늘어짐(Stretch-out)에서 계면 트랩 밀도($D_{it}$)를 완벽하게 역산해냅니다."
    ],
    "svg_title": "📊 [MOS Cap 동작 특성 종합 다이어그램] (A) 4대 동작 영역 에너지 밴드 | (B) C-V 특성 곡선과 주파수 분기(LF/HF/Deep Depletion) | (C) 실무 C-V 진단 파라미터 추출",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: 4 Operating Regions & Energy Band Diagrams -->
  <g transform="translate(20, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 4대 동작 영역 &amp; 에너지 밴드 (P형 기판)</text>

    <!-- Region 1: Accumulation -->
    <g transform="translate(15, 42)">
      <rect width="280" height="84" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="16" fill="#fde047" font-size="8.5" font-weight="800">① 축적 (Accumulation, VG &lt; VFB, ψs &lt; 0)</text>
      <!-- Mini Band -->
      <g transform="translate(10, 22)">
        <rect x="0" y="5" width="25" height="45" fill="#475569" rx="1"/>
        <text x="5" y="30" fill="#fff" font-size="7">Gate</text>
        <rect x="25" y="5" width="15" height="45" fill="#a855f7" opacity="0.8"/>
        <!-- Ec, Ev bending up -->
        <path d="M 40 12 Q 70 12 120 22" stroke="#38bdf8" stroke-width="1.8" fill="none"/>
        <path d="M 40 45 Q 70 45 120 55" stroke="#38bdf8" stroke-width="1.8" fill="none"/>
        <!-- Ef line -->
        <line x1="40" y1="48" x2="120" y2="48" stroke="#facc15" stroke-dasharray="2,2"/>
        <text x="125" y="25" fill="#38bdf8" font-size="6.5">Ec</text>
        <text x="125" y="57" fill="#38bdf8" font-size="6.5">Ev</text>
        <!-- Holes (+) -->
        <circle cx="48" cy="48" r="2.5" fill="#ef4444"/>
        <circle cx="56" cy="49" r="2.5" fill="#ef4444"/>
        <text x="150" y="22" fill="#cbd5e1" font-size="7.5">• 밴드 위로 휘어짐 (상향)</text>
        <text x="150" y="34" fill="#cbd5e1" font-size="7.5">• 다수캐리어 정공(h⁺) 계면 결집</text>
        <text x="150" y="46" fill="#34d399" font-size="8" font-weight="800">➔ C = C_ox (주파수 무관)</text>
      </g>
    </g>

    <!-- Region 2: Flat-Band -->
    <g transform="translate(15, 134)">
      <rect width="280" height="84" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="16" fill="#38bdf8" font-size="8.5" font-weight="800">② 평탄대 (Flat-Band, VG = VFB, ψs = 0)</text>
      <!-- Mini Band -->
      <g transform="translate(10, 22)">
        <rect x="0" y="5" width="25" height="45" fill="#475569" rx="1"/>
        <rect x="25" y="5" width="15" height="45" fill="#a855f7" opacity="0.8"/>
        <!-- Perfectly flat bands -->
        <line x1="40" y1="18" x2="120" y2="18" stroke="#38bdf8" stroke-width="1.8"/>
        <line x1="40" y1="50" x2="120" y2="50" stroke="#38bdf8" stroke-width="1.8"/>
        <line x1="40" y1="44" x2="120" y2="44" stroke="#facc15" stroke-dasharray="2,2"/>
        <text x="125" y="21" fill="#38bdf8" font-size="6.5">Ec</text>
        <text x="125" y="53" fill="#38bdf8" font-size="6.5">Ev</text>
        <text x="150" y="22" fill="#cbd5e1" font-size="7.5">• 밴드 휘어짐 전무 (ψs = 0)</text>
        <text x="150" y="34" fill="#cbd5e1" font-size="7.5">• 공간 전하 밀도 = 0</text>
        <text x="150" y="46" fill="#fde047" font-size="8" font-weight="800">➔ C_FB = Cox||(ε/L_D)</text>
      </g>
    </g>

    <!-- Region 3: Depletion -->
    <g transform="translate(15, 226)">
      <rect width="280" height="84" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="16" fill="#fbbf24" font-size="8.5" font-weight="800">③ 공핍 (Depletion, VFB &lt; VG &lt; Vth, 0 &lt; ψs &lt; 2φB)</text>
      <!-- Mini Band -->
      <g transform="translate(10, 22)">
        <rect x="0" y="5" width="25" height="45" fill="#475569" rx="1"/>
        <rect x="25" y="5" width="15" height="45" fill="#a855f7" opacity="0.8"/>
        <!-- Bands bending down -->
        <path d="M 40 32 Q 70 20 120 18" stroke="#38bdf8" stroke-width="1.8" fill="none"/>
        <path d="M 40 64 Q 70 52 120 50" stroke="#38bdf8" stroke-width="1.8" fill="none"/>
        <line x1="40" y1="45" x2="120" y2="45" stroke="#facc15" stroke-dasharray="2,2"/>
        <text x="125" y="21" fill="#38bdf8" font-size="6.5">Ec</text>
        <text x="125" y="53" fill="#38bdf8" font-size="6.5">Ev</text>
        <text x="150" y="22" fill="#cbd5e1" font-size="7.5">• 정공 쫓겨남 ➔ 공핍층(W) 형성</text>
        <text x="150" y="34" fill="#cbd5e1" font-size="7.5">• 고정 수락체 음이온(B⁻) 노출</text>
        <text x="150" y="46" fill="#f87171" font-size="8" font-weight="800">➔ C = Cox||Cdep (지속 하강!)</text>
      </g>
    </g>

    <!-- Region 4: Inversion -->
    <g transform="translate(15, 318)">
      <rect width="280" height="92" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="16" fill="#34d399" font-size="8.5" font-weight="800">④ 반전 (Inversion, VG ≥ Vth, ψs ≥ 2φB)</text>
      <!-- Mini Band -->
      <g transform="translate(10, 22)">
        <rect x="0" y="5" width="25" height="45" fill="#475569" rx="1"/>
        <rect x="25" y="5" width="15" height="45" fill="#a855f7" opacity="0.8"/>
        <!-- Heavy band bending down -->
        <path d="M 40 45 Q 60 22 120 18" stroke="#38bdf8" stroke-width="1.8" fill="none"/>
        <path d="M 40 77 Q 60 54 120 50" stroke="#38bdf8" stroke-width="1.8" fill="none"/>
        <line x1="40" y1="42" x2="120" y2="42" stroke="#facc15" stroke-dasharray="2,2"/>
        <!-- Inversion electrons (●) -->
        <circle cx="43" cy="44" r="2.5" fill="#38bdf8"/>
        <circle cx="48" cy="44" r="2.5" fill="#38bdf8"/>
        <text x="125" y="21" fill="#38bdf8" font-size="6.5">Ec</text>
        <text x="125" y="53" fill="#38bdf8" font-size="6.5">Ev</text>
        <text x="150" y="20" fill="#cbd5e1" font-size="7.5">• 표면에 2차원 전자층(반전층) 형성</text>
        <text x="150" y="32" fill="#cbd5e1" font-size="7.5">• 공핍층 최대 폭(W_max) 고정</text>
        <text x="150" y="44" fill="#fde047" font-size="7.8" font-weight="800">➔ 주파수별 거동 분기! (B 참조)</text>
      </g>
    </g>
  </g>

  <!-- PANEL B: C-V Characteristics Curve & Frequency Regimes -->
  <g transform="translate(350, 20)">
    <rect width="320" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) C-V 특성 곡선 &amp; 3대 주파수 분기</text>

    <!-- Graph Box -->
    <g transform="translate(15, 42)">
      <rect width="290" height="235" rx="6" fill="#1e293b" stroke="#334155"/>

      <!-- Axes -->
      <line x1="30" y1="185" x2="275" y2="185" stroke="#94a3b8" stroke-width="1.2"/>
      <line x1="100" y1="185" x2="100" y2="25" stroke="#94a3b8" stroke-width="1.2"/>
      <text x="260" y="197" fill="#94a3b8" font-size="7.5">Gate Voltage (VG)</text>
      <text x="88" y="20" fill="#94a3b8" font-size="7">0 V</text>
      <text x="10" y="30" fill="#94a3b8" font-size="7.5">Cap (C)</text>

      <!-- Cox line -->
      <line x1="30" y1="45" x2="275" y2="45" stroke="#64748b" stroke-dasharray="2,2"/>
      <text x="5" y="48" fill="#38bdf8" font-size="8" font-weight="800">C_ox</text>

      <!-- CFB line -->
      <line x1="30" y1="75" x2="275" y2="75" stroke="#64748b" stroke-dasharray="1,2"/>
      <text x="5" y="78" fill="#facc15" font-size="7">C_FB</text>

      <!-- Cmin line -->
      <line x1="30" y1="135" x2="275" y2="135" stroke="#64748b" stroke-dasharray="2,2"/>
      <text x="5" y="138" fill="#f87171" font-size="8" font-weight="800">C_min</text>

      <!-- Marks on V-axis -->
      <line x1="75" y1="183" x2="75" y2="187" stroke="#cbd5e1"/>
      <text x="65" y="198" fill="#cbd5e1" font-size="7">V_FB</text>
      <line x1="160" y1="183" x2="160" y2="187" stroke="#cbd5e1"/>
      <text x="155" y="198" fill="#cbd5e1" font-size="7">V_th</text>

      <!-- Regions labels -->
      <text x="35" y="36" fill="#94a3b8" font-size="7">축적</text>
      <text x="105" y="175" fill="#94a3b8" font-size="7">공핍</text>
      <text x="210" y="175" fill="#94a3b8" font-size="7">강반전</text>

      <!-- Curve 1: Low Frequency (LF, blue dash) -->
      <path d="M 30 45 L 60 45 Q 85 55 110 95 Q 135 135 160 135 Q 195 135 225 55 L 270 45" stroke="#38bdf8" stroke-width="2" stroke-dasharray="3,3" fill="none"/>
      <text x="200" y="65" fill="#38bdf8" font-size="7.5" font-weight="800">① 저주파 (LF, ~10Hz)</text>
      <text x="200" y="76" fill="#a5f3fc" font-size="6.8">전자가 AC 추종 ➔ Cox 복원!</text>

      <!-- Curve 2: High Frequency (HF, red solid) -->
      <path d="M 30 45 L 60 45 Q 85 55 110 95 Q 135 135 160 135 L 270 135" stroke="#ef4444" stroke-width="2.5" fill="none"/>
      <text x="165" y="125" fill="#f87171" font-size="7.8" font-weight="800">② 고주파 (HF, 100kHz~1MHz)</text>
      <text x="165" y="148" fill="#fca5a5" font-size="6.8">전자가 못 따라옴 ➔ C_min 정체</text>

      <!-- Curve 3: Deep Depletion (purple dash-dot) -->
      <path d="M 160 135 Q 195 145 235 165 L 270 178" stroke="#c084fc" stroke-width="2" stroke-dasharray="4,2" fill="none"/>
      <text x="180" y="165" fill="#c084fc" font-size="7.2" font-weight="800">③ 깊은 공핍 (Deep Depletion)</text>
      <text x="195" y="176" fill="#e9d5ff" font-size="6.5">고속 전압 스윕 시 C 추락!</text>
    </g>

    <!-- Regime Explanation -->
    <g transform="translate(15, 288)">
      <rect width="290" height="118" rx="6" fill="#0b1329" stroke="#334155"/>
      <text x="10" y="18" fill="#fde047" font-size="8.8" font-weight="800">★ 반전층 주파수 3대 분기 핵심 물리</text>
      <text x="10" y="34" fill="#cbd5e1" font-size="7.5">1. 저주파 (LF): 열 생성 시간(τ_gen ≈ ms) &gt; 신호 주기</text>
      <text x="18" y="47" fill="#38bdf8" font-size="7.2">➔ 전자가 게이트 교류 전하를 스크리닝하여 C = C_ox 회복!</text>
      <text x="10" y="62" fill="#cbd5e1" font-size="7.5">2. 고주파 (HF): 신호 주기(μs) &lt;&lt; 열 생성 시간(ms)</text>
      <text x="18" y="75" fill="#f87171" font-size="7.2">➔ 전자가 교류 변조에 반응 불가, 공핍층만 반응 ➔ C = C_min</text>
      <text x="10" y="90" fill="#cbd5e1" font-size="7.5">3. 깊은 공핍 (Deep Dep): DC 전압을 극도로 빠르게 올림</text>
      <text x="18" y="103" fill="#c084fc" font-size="7.2">➔ 전자가 생성될 틈이 없어 W_dep가 한계 없이 확장 ➔ C 급락!</text>
    </g>
  </g>

  <!-- PANEL C: Real Device Parameters Extraction -->
  <g transform="translate(690, 20)">
    <rect width="270" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) 실무 C-V 진단 &amp; 파라미터 추출</text>

    <!-- Diagnostic Shifts -->
    <g transform="translate(15, 42)">
      <rect width="240" height="175" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="16" fill="#38bdf8" font-size="8.8" font-weight="800">1. 실제 C-V 곡선의 비이상적 변형</text>

      <!-- Mini shift graph -->
      <g transform="translate(10, 24)">
        <line x1="15" y1="75" x2="215" y2="75" stroke="#94a3b8" stroke-width="1"/>
        <line x1="80" y1="75" x2="80" y2="10" stroke="#94a3b8" stroke-width="1"/>
        <!-- Ideal curve -->
        <path d="M 20 20 L 45 20 Q 80 25 110 65 L 205 65" stroke="#64748b" stroke-width="1.5" stroke-dasharray="2,2" fill="none"/>
        <text x="120" y="30" fill="#94a3b8" font-size="6.5">이상적 곡선 (Ideal)</text>

        <!-- Shifted curve (due to Qf) -->
        <path d="M 10 20 L 25 20 Q 55 25 85 65 L 180 65" stroke="#ef4444" stroke-width="1.8" fill="none"/>
        <line x1="110" y1="65" x2="85" y2="65" stroke="#fbbf24" stroke-width="1.5" marker-end="url(#arrowYellow)"/>
        <text x="35" y="14" fill="#ef4444" font-size="7" font-weight="800">좌측 평행이동 (ΔV_FB)</text>
        <text x="85" y="78" fill="#fde047" font-size="6.5">Q_f &gt; 0 (양전하)</text>
      </g>

      <text x="10" y="112" fill="#cbd5e1" font-size="7.5">• 수평 이동량: ΔV_FB = Φ_ms - Q_f / C_ox</text>
      <text x="10" y="126" fill="#fde047" font-size="7.5" font-weight="800">➔ 산화막 고정전하(Q_f) 정밀 역산!</text>
      <text x="10" y="140" fill="#cbd5e1" font-size="7.5">• 곡선 늘어짐 (Stretch-out): 계면트랩(D_it)</text>
      <text x="10" y="154" fill="#a7f3d0" font-size="7.5">• 전압 왕복 히스테리시스: 가동성 이온(Na⁺)</text>
    </g>

    <!-- FAB extracted parameters list -->
    <g transform="translate(15, 228)">
      <rect width="240" height="178" rx="6" fill="#0b1329" stroke="#f59e0b"/>
      <text x="10" y="18" fill="#fbbf24" font-size="8.8" font-weight="800">2. C-V 측정으로 뽑아내는 5대 물성치</text>

      <text x="10" y="36" fill="#38bdf8" font-size="7.8" font-weight="800">① 산화막 두께 (t_ox):</text>
      <text x="20" y="48" fill="#cbd5e1" font-size="7.2">t_ox = ε_ox / C_ox (축적 용량에서 직접 도출)</text>

      <text x="10" y="64" fill="#38bdf8" font-size="7.8" font-weight="800">② 기판 도핑 농도 (N_A):</text>
      <text x="20" y="76" fill="#cbd5e1" font-size="7.2">1/C² vs V 기울기 및 C_min 값에서 역산</text>

      <text x="10" y="92" fill="#38bdf8" font-size="7.8" font-weight="800">③ 평탄대 전압 (V_FB) 및 일함수차 (Φ_ms):</text>
      <text x="20" y="104" fill="#cbd5e1" font-size="7.2">C_FB 지점의 게이트 전압으로 직접 계측</text>

      <text x="10" y="120" fill="#38bdf8" font-size="7.8" font-weight="800">④ 계면 결함 트랩 밀도 (D_it):</text>
      <text x="20" y="132" fill="#cbd5e1" font-size="7.2">고주파-저주파 C-V 차이 (Terman / 준정적법)</text>

      <text x="10" y="148" fill="#38bdf8" font-size="7.8" font-weight="800">⑤ 산화막 고정 전하 밀도 (Q_f):</text>
      <text x="20" y="160" fill="#cbd5e1" font-size="7.2">이론값 대비 V_FB 이동량으로 비파괴 검증</text>
    </g>
  </g>

  <!-- Arrow marker definition -->
  <defs>
    <marker id="arrowYellow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#fbbf24" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- Section 1: Overview and 4 Operating Regimes -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. MOS Cap의 4대 동작 영역 완전 해부 (P형 기판 NMOS 기준)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            MOS Capacitor는 게이트 전압($V_G$)을 음수($-$)에서 양수($+$)로 점진적으로 증가시킴에 따라 실리콘 계면의 <strong>표면 전위($\psi_s$)와 에너지 밴드가 휘어지며</strong> 다음 4가지 동작 상태를 순차적으로 거칩니다.
          </p>

          <!-- Regime 1: Accumulation -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:14px; border-left:4px solid #fde047;">
            <h4 style="color:#fde047; font-size:1.02rem; font-weight:800; margin-bottom:6px;">
              ① 축적 영역 (Accumulation, $V_G < V_{FB}$, $\psi_s < 0$)
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:18px;">
              <li><strong>물리적 상태</strong>: 게이트에 강한 음(-)의 전압을 걸면, P형 기판의 다수캐리어인 정공($p$, $\oplus$)들이 산화막-실리콘 계면으로 강력하게 끌려옵니다.</li>
              <li><strong>에너지 밴드</strong>: 계면에서 밴드가 위쪽으로 휘어지며($\psi_s < 0$), 페르미 준위($E_F$)가 가전자대($E_v$)에 바짝 달라붙습니다.</li>
              <li><strong>정전용량 거동</strong>: 계면에 얇은 정공 판자(Sheet)가 형성되어 마치 금속 전극처럼 작동합니다. 따라서 반도체 측 공핍층이 전혀 없어 <strong>측정 주파수와 무관하게 산화막 정전용량 $C = C_{ox} = \frac{\epsilon_{ox}}{t_{ox}}$</strong>가 측정됩니다.</li>
            </ul>
          </div>

          <!-- Regime 2: Flat-Band -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:14px; border-left:4px solid #38bdf8;">
            <h4 style="color:#38bdf8; font-size:1.02rem; font-weight:800; margin-bottom:6px;">
              ② 평탄대 상태 (Flat-Band, $V_G = V_{FB}$, $\psi_s = 0$)
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:18px;">
              <li><strong>물리적 상태</strong>: 게이트 전압이 금속-반도체 일함수 차이($\Phi_{ms}$)와 산화막 내부 전하($Q_{ox}$)를 정확하게 상쇄하는 지점입니다.</li>
              <li><strong>에너지 밴드</strong>: 반도체 내부의 밴드가 휘어짐 없이 계면까지 완벽하게 평평(Flat)해집니다 ($\psi_s = 0$).</li>
              <li><strong>정전용량 거동</strong>: 실리콘 표면 전하의 열적 요동 거리를 나타내는 디바이 길이($L_D = \sqrt{\frac{\epsilon_s kT}{q^2 N_A}}$)에 의해 <strong>평탄대 커패시턴스 $C_{FB} = \frac{C_{ox} C_D}{C_{ox} + C_D}$</strong> ($C_D = \frac{\epsilon_s}{L_D}$)가 결정됩니다. 실무에서 $V_{FB}$를 찾아내는 기준점이 됩니다.</li>
            </ul>
          </div>

          <!-- Regime 3: Depletion -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:14px; border-left:4px solid #fbbf24;">
            <h4 style="color:#fbbf24; font-size:1.02rem; font-weight:800; margin-bottom:6px;">
              ③ 공핍 영역 (Depletion, $V_{FB} < V_G < V_{th}$, $0 < \psi_s < 2\phi_B$)
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:18px;">
              <li><strong>물리적 상태</strong>: 게이트에 작은 양(+)의 전압을 걸면, 표면의 정공들이 기판 깊숙이 밀려나 쫓겨납니다. 그 자리에는 움직이지 못하는 음이온 억셉터($B^-$)들만 덩그러니 남아 **공핍층(Depletion Region)**을 형성합니다.</li>
              <li><strong>에너지 밴드</strong>: 밴드가 아래쪽으로 휘어지기 시작합니다 ($0 < \psi_s < 2\phi_B$).</li>
              <li><strong>정전용량 거동</strong>: 산화막 용량($C_{ox}$) 뒤에 유전체 역할을 하는 공핍층 용량($C_{dep} = \frac{\epsilon_s}{W_{dep}}$)이 직렬로 연결됩니다 ($1/C = 1/C_{ox} + 1/C_{dep}$). 게이트 전압을 올릴수록 공핍층 두께($W_{dep} = \sqrt{\frac{2\epsilon_s \psi_s}{q N_A}}$)가 계속 넓어지므로, <strong>전체 정전용량 $C$는 계속 가파르게 하강</strong>합니다.</li>
            </ul>
          </div>

          <!-- Regime 4: Inversion -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:14px; border-left:4px solid #34d399;">
            <h4 style="color:#34d399; font-size:1.02rem; font-weight:800; margin-bottom:6px;">
              ④ 반전 영역 (Inversion, $V_G \ge V_{th}$, $\psi_s \ge 2\phi_B$)
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:18px;">
              <li><strong>물리적 상태</strong>: 게이트 전압이 문턱전압($V_{th}$)을 넘어서면 표면 전위가 $\psi_s \ge 2\phi_B$가 됩니다. 계면의 진성 페르미 준위($E_i$)가 페르미 준위($E_F$) 아래로 내려앉으면서, **표면의 소수캐리어 전자 밀도가 기판의 정공 도핑 농도를 능가($n_s \ge N_A$)**하게 됩니다.</li>
              <li><strong>강반전 핀칭</strong>: 계면에 얇은 전자의 층(반전층, Inversion Layer)이 형성되며, 공핍층 두께는 더 이상 늘어나지 못하고 **최대 공핍 폭($W_{dep,max} = \sqrt{\frac{2\epsilon_s (2\phi_B)}{q N_A}}$)에 고정(Pinning)**됩니다.</li>
              <li><strong>정전용량 거동</strong>: 바로 여기서 **주파수에 따른 극적인 3대 거동 분기**가 발생합니다!</li>
            </ul>
          </div>
        </div>

        <!-- Section 2: Frequency Dependence in Inversion -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#10b981; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. C-V 특성의 핵심: 반전 영역 3대 주파수 분기 (LF vs HF vs Deep Depletion)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            MOS Cap에는 소스/드레인이 없기 때문에 반전층 전자는 오직 **열 생성(Thermal Generation)**으로만 공급됩니다. 이 열 생성 속도($\tau_{gen} \sim \text{ms}$)와 측정 교류(AC) 신호 주파수의 경쟁이 C-V 곡선을 결정합니다.
          </p>

          <div style="overflow-x:auto; margin-bottom:16px;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">주파수 모드</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">측정 조건</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">반전 영역 정전용량 ($C_{inv}$)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">물리적 메커니즘</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">① 저주파 (LF, Quasi-static)</td>
                  <td style="padding:10px 14px;">$f \sim 1 \sim 100\,\text{Hz}$<br>(준정적 C-V)</td>
                  <td style="padding:10px 14px; color:#38bdf8; font-weight:800;">$C = C_{ox}$ 로 회복! ↑</td>
                  <td style="padding:10px 14px;">AC 신호 주기가 열 생성 시간($\tau_{gen}$)보다 훨씬 길어 전자가 실시간으로 생성/재결합하며 AC 전하를 완벽 추종함. 게이트 전하를 계면 전자가 차폐(Screening)하므로 $C_{ox}$ 복원.</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#f87171;">② 고주파 (HF, High-Freq)</td>
                  <td style="padding:10px 14px;">$f \sim 100\,\text{kHz} \sim 1\,\text{MHz}$<br>(표준 계측 주파수)</td>
                  <td style="padding:10px 14px; color:#f87171; font-weight:800;">$C = C_{min}$ 에 정체! ──</td>
                  <td style="padding:10px 14px;">AC 신호 주기($1\,\mu\text{s}$)가 너무 빨라 열 생성 전자가 AC 전하 변조를 전혀 돕지 못함. 반전 전자는 DC 평균값만 유지하고, AC 신호는 공핍층 끝($W_{dep,max}$)에서 다수캐리어(정공)의 출입으로만 지탱되므로 최솟값 $C_{min} = \frac{C_{ox}C_{dep,max}}{C_{ox}+C_{dep,max}}$에 묶임.</td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#c084fc;">③ 깊은 공핍 (Deep Depletion)</td>
                  <td style="padding:10px 14px;">초고속 DC 게이트 전압 스윕<br>($dV_G/dt$ 극대화)</td>
                  <td style="padding:10px 14px; color:#c084fc; font-weight:800;">$C < C_{min}$ 아래로 추락! ↓↓</td>
                  <td style="padding:10px 14px;">게이트 DC 전압을 너무 빨리 올려 전자가 생성될 틈조차 주지 않음. 반전층이 아예 형성되지 못하고 전하 보존을 위해 공핍층 폭($W_{dep}$)이 최대 한계를 뚫고 비정상적으로 계속 확장되어 커패시턴스가 끝없이 폭락함. (CCD 이미지 센서, DRAM 전하 충전 원리)</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Section 3: Engineering Extraction -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 반도체 FAB 실무: C-V 곡선 하나로 모든 것을 진단하는 원리
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            현대 반도체 팹(FAB)에서 웨이퍼 테스트 패턴(TEG)에 MOS Cap을 필수적으로 넣는 이유는, **단 한 번의 C-V 측정으로 수많은 핵심 공정 변수를 비파괴적으로 정밀 역산**할 수 있기 때문입니다:
          </p>

          <div style="background:#0f172a; border-left:4px solid #f59e0b; padding:16px 20px; border-radius:0 8px 8px 0;">
            <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:18px;">
              <li><strong>1. 산화막 두께 ($t_{ox}$)</strong>: 축적 영역의 최대 용량 $C_{ox}$로부터 $t_{ox} = \frac{\epsilon_{ox} A}{C_{ox}}$로 $\text{Å}$ 단위 두께를 즉시 추출.</li>
              <li><strong>2. 기판 도핑 농도 ($N_A$)</strong>: 공핍 영역의 $1/C^2$ 대 $V_G$ 그래프의 기울기($\frac{d(1/C^2)}{dV} = \frac{2}{q \epsilon_s A^2 N_A}$)로부터 실리콘 기판 농도 역산.</li>
              <li><strong>3. 평탄대 전압 ($V_{FB}$) & 산화막 고정전하 ($Q_f$)</strong>: 이론적 C-V 곡선 대비 실제 C-V 곡선이 좌우로 수평 이동한 양($\Delta V_{FB} = \Phi_{ms} - \frac{Q_f}{C_{ox}}$)을 측정하여 양전하 결함($Q_f$) 정밀 평가.</li>
              <li><strong>4. 계면 트랩 밀도 ($D_{it}$)</strong>: 계면 결함 준위가 전하를 포획/방출하면서 C-V 곡선이 완만하게 옆으로 늘어지는 **스트레치 아웃(Stretch-out)** 현상을 고주파-저주파 비교법(High-Low method)으로 정량화.</li>
              <li><strong>5. 가동성 이온 오염 ($Q_m$, $Na^+, K^+$)</strong>: 전압을 양방향으로 왕복 스위핑할 때 발생하는 **이력 곡선(Hysteresis Loop)** 폭을 재어 공정 챔버의 금속 오염 유무를 실시간 감시.</li>
            </ul>
          </div>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 88 topics (q-88 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(88, 0, -1):
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

    # Step 4: Update header description to 89 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 'MOS Cap의 동작 특성 완전 정복'이 위치하며, 총 89개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 MOS Cap Operating Characteristics topic!")
