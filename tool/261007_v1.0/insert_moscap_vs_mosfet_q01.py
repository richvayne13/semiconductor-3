# -*- coding: utf-8 -*-
"""
insert_moscap_vs_mosfet_q01.py
사용자 질문:
"mos cap와 mosfet의 차이"

대시보드 최상단 Q01로 신규 추가하고, 기존 87개 질문을 Q02~Q88로 시프트 (총 88개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 기본 물리 · MOS Cap vs MOSFET 본질 비교)",
    "title": "MOS Cap(모스 커패시터)과 MOSFET의 본질적 차이 (구조, 반전층 공급원, C-V 거동 비교)",
    "nav_title": "MOS Cap과 MOSFET의 본질적 차이",
    "summary": [
        "<strong>1. 단자 수 및 구조적 차이 (2단자 수동 vs 4단자 능동 스위치)</strong>: MOS Cap은 게이트-기판(2단자)만 존재하는 수동 정전용량 소자이며 수평 전류 통로가 없는 반면, MOSFET은 게이트 하부 양쪽에 고농도 소스/드레인($N^+$) 접합이 구비되어 수평 전류($I_{DS}$)를 On/Off 제어하는 4단자 능동 스위치입니다.",
        "<strong>2. 반전층 캐리어 공급원의 결정적 차이 (열 생성 vs S/D 직접 공급)</strong>: MOS Cap은 반전층 형성 시 소스/드레인이 없어 느린 '열적 전자-정공 쌍 생성(Thermal EHP Generation, $\\tau \\sim \\text{ms}$)'에만 의존합니다. 반면 MOSFET은 소스/드레인이라는 거대한 '전자 저수지'에서 피코초($\\text{ps}$) 단위로 전자를 즉각 공급받습니다.",
        "<strong>3. C-V 특성 곡선의 고주파(HF) 거동 차이</strong>: MOS Cap은 고주파(100kHz~1MHz) 측정 시 소수 캐리어(전자)가 교류 신호를 따라가지 못해 반전 영역에서 커패시턴스가 최솟값($C_{min}$)에 머무릅니다. 반면 MOSFET은 소스/드레인이 전자를 즉각 대어주므로 고주파에서도 반전 용량이 산화막 용량($C_{ox}$)으로 100% 완전 회복됩니다.",
        "<strong>4. 주요 역할과 응용 분야</strong>: MOS Cap은 팹(FAB) 공정 계측($t_{ox}$, $V_{FB}$, 계면트랩 $D_{it}$, 도핑농도 추출) 및 DRAM 1T-1C 스토리지 커패시터로 쓰이고, MOSFET은 현대 모든 CPU, GPU, AP의 기본 논리 게이트 및 증폭 소자로 쓰입니다."
    ],
    "svg_title": "📊 [MOS Cap vs MOSFET 비교 다이어그램] (A) 2단자 vs 4단자 구조 비교 | (B) 반전층 전자 공급 메커니즘 차이 | (C) C-V 특성 곡선 고주파(HF) 거동 차이",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Structural Comparison -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 단자 수 및 구조 비교</text>

    <!-- Sub-panel A1: MOS Cap -->
    <g transform="translate(15, 42)">
      <rect width="270" height="155" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="9" font-weight="800">1. MOS Cap (2단자 수동 소자)</text>

      <!-- Gate terminal -->
      <line x1="135" y1="24" x2="135" y2="34" stroke="#38bdf8" stroke-width="2"/>
      <circle cx="135" cy="24" r="3" fill="#38bdf8"/>
      <text x="142" y="26" fill="#38bdf8" font-size="7.5" font-weight="800">Gate (V_G)</text>

      <!-- Gate electrode -->
      <rect x="50" y="34" width="170" height="12" fill="#475569" rx="1"/>
      <text x="100" y="43" fill="#fff" font-size="7.5">Metal / Poly-Si</text>

      <!-- Oxide -->
      <rect x="50" y="46" width="170" height="6" fill="#a855f7"/>
      <text x="102" y="51" fill="#fff" font-size="6">Oxide (SiO₂)</text>

      <!-- P-Substrate -->
      <rect x="50" y="52" width="170" height="60" fill="#0284c7" opacity="0.3"/>
      <text x="85" y="85" fill="#bae6fd" font-size="8" font-weight="700">P-type Substrate (Si)</text>
      <text x="88" y="98" fill="#fca5a5" font-size="7.2">★ Source / Drain 없음!</text>

      <!-- Body contact -->
      <rect x="50" y="112" width="170" height="8" fill="#475569"/>
      <line x1="135" y1="120" x2="135" y2="130" stroke="#94a3b8" stroke-width="2"/>
      <circle cx="135" cy="130" r="3" fill="#94a3b8"/>
      <text x="142" y="132" fill="#94a3b8" font-size="7.5">Body (Ground)</text>

      <text x="12" y="146" fill="#cbd5e1" font-size="7.2">• 수평 전류(I_DS) 통로 전무 (I_DC = 0)</text>
    </g>

    <!-- Sub-panel A2: MOSFET -->
    <g transform="translate(15, 208)">
      <rect width="270" height="195" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="9" font-weight="800">2. MOSFET (4단자 능동 스위치)</text>

      <!-- Gate terminal -->
      <line x1="135" y1="24" x2="135" y2="34" stroke="#38bdf8" stroke-width="2"/>
      <circle cx="135" cy="24" r="3" fill="#38bdf8"/>
      <text x="142" y="26" fill="#38bdf8" font-size="7.5" font-weight="800">Gate (V_G)</text>

      <!-- Gate & Oxide -->
      <rect x="80" y="34" width="110" height="12" fill="#475569" rx="1"/>
      <rect x="80" y="46" width="110" height="6" fill="#a855f7"/>

      <!-- Source & Drain -->
      <rect x="25" y="52" width="55" height="42" fill="#f59e0b" rx="1"/>
      <text x="32" y="75" fill="#000" font-size="8" font-weight="800">Source (N+)</text>
      <circle cx="45" cy="40" r="3" fill="#f59e0b"/>
      <line x1="45" y1="40" x2="45" y2="52" stroke="#f59e0b" stroke-width="2"/>
      <text x="25" y="35" fill="#f59e0b" font-size="7">S 단자</text>

      <rect x="190" y="52" width="55" height="42" fill="#f59e0b" rx="1"/>
      <text x="198" y="75" fill="#000" font-size="8" font-weight="800">Drain (N+)</text>
      <circle cx="225" cy="40" r="3" fill="#f59e0b"/>
      <line x1="225" y1="40" x2="225" y2="52" stroke="#f59e0b" stroke-width="2"/>
      <text x="220" y="35" fill="#f59e0b" font-size="7">D 단자</text>

      <!-- Channel in P-Sub -->
      <rect x="80" y="52" width="110" height="42" fill="#0284c7" opacity="0.3"/>
      <text x="105" y="76" fill="#a7f3d0" font-size="8" font-weight="800">채널 영역 (L)</text>

      <!-- Substrate bottom -->
      <rect x="25" y="94" width="220" height="24" fill="#0284c7" opacity="0.4"/>
      <rect x="25" y="118" width="220" height="8" fill="#475569"/>
      <line x1="135" y1="126" x2="135" y2="136" stroke="#94a3b8" stroke-width="2"/>
      <circle cx="135" cy="136" r="3" fill="#94a3b8"/>
      <text x="142" y="138" fill="#94a3b8" font-size="7.5">Body 단자 (B)</text>

      <!-- Current flow arrow -->
      <path d="M 75 65 L 195 65" stroke="#ef4444" stroke-width="2" marker-end="url(#arrowRed)"/>
      <text x="95" y="60" fill="#f87171" font-size="7.5" font-weight="800">전자 이동 ➔ I_DS</text>

      <text x="12" y="160" fill="#cbd5e1" font-size="7.2">• 고농도 N+ S/D 접합 구비 (전자 저수지 역할!)</text>
      <text x="12" y="174" fill="#fde047" font-size="7.5" font-weight="800">• 게이트 전압으로 수평 전류 I_DS 스위칭 제어</text>
    </g>
  </g>

  <!-- PANEL B: Carrier Supply Mechanism in Inversion -->
  <g transform="translate(340, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 반전층(Inversion) 전자 공급원 비교</text>

    <!-- MOS Cap Mechanism -->
    <g transform="translate(15, 42)">
      <rect width="280" height="175" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="10" y="18" fill="#f87171" font-size="9" font-weight="800">1. MOS Cap: 느린 '열 생성(Thermal Generation)'</text>

      <rect x="8" y="28" width="264" height="65" rx="4" fill="#0b1329" stroke="#334155"/>
      <text x="14" y="44" fill="#cbd5e1" font-size="7.8">• 소스/드레인이 없으므로 전자를 빌려올 곳이 없음!</text>
      <text x="14" y="58" fill="#fca5a5" font-size="7.8">• 실리콘 원자 격자의 열진동으로 생성되는</text>
      <text x="20" y="72" fill="#ffffff" font-size="8" font-weight="800">열적 전자-정공 쌍 (Thermal EHP) 생성에만 의존!</text>
      <text x="14" y="86" fill="#fbbf24" font-size="7.5">• 생성 수명시간: τ_gen ≈ 100 μs ~ 10 ms (매우 느림!)</text>

      <text x="10" y="108" fill="#cbd5e1" font-size="7.8">★ 고주파 AC 전압(100 kHz ~ 1 MHz) 인가 시:</text>
      <text x="16" y="122" fill="#f87171" font-size="7.8">• 전압은 1초에 100만 번 진동하는데, 전자는 못 태어남!</text>
      <text x="16" y="136" fill="#cbd5e1" font-size="7.5">• 반전층 전자가 AC 신호에 전혀 응답하지 못함</text>
      <text x="16" y="152" fill="#fde047" font-size="7.8" font-weight="800">➔ 고주파에서 커패시턴스가 C_min에 묶여버림!</text>
      <text x="16" y="166" fill="#94a3b8" font-size="7.2">(전자가 못 따라와 공핍층 두께만 늘었다 줄었다 함)</text>
    </g>

    <!-- MOSFET Mechanism -->
    <g transform="translate(15, 228)">
      <rect width="280" height="178" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="10" y="18" fill="#34d399" font-size="9" font-weight="800">2. MOSFET: S/D '초고속 직접 공급(Reservoir)'</text>

      <rect x="8" y="28" width="264" height="65" rx="4" fill="#0b1329" stroke="#334155"/>
      <text x="14" y="44" fill="#cbd5e1" font-size="7.8">• 채널 양옆에 고농도 N+ Source/Drain 접합 밀착!</text>
      <text x="14" y="58" fill="#38bdf8" font-size="7.8">• 10²⁰ cm⁻³ 이상의 막대한 전자 저수지(Reservoir)</text>
      <text x="20" y="72" fill="#ffffff" font-size="8" font-weight="800">게이트 전압이 변하면 전자가 S/D에서 즉각 유입/유출!</text>
      <text x="14" y="86" fill="#a7f3d0" font-size="7.5">• 공급 응답시간: τ_transit ≈ 피코초 (ps 단위, 광속!)</text>

      <text x="10" y="108" fill="#cbd5e1" font-size="7.8">★ 고주파 AC 전압(1 MHz 이상) 인가 시:</text>
      <text x="16" y="122" fill="#34d399" font-size="7.8">• S/D에서 전자가 번개처럼 밀려들어와 AC 신호 완벽 추종!</text>
      <text x="16" y="136" fill="#cbd5e1" font-size="7.5">• 반전층 전자가 게이트 전하를 100% 온전히 스크리닝</text>
      <text x="16" y="152" fill="#fde047" font-size="8" font-weight="800">➔ 고주파에서도 C가 C_ox로 100% 완전 회복!</text>
      <text x="16" y="168" fill="#a5f3fc" font-size="7.2">★ 이것이 MOS Cap과 MOSFET의 가장 본질적인 물리 차이!</text>
    </g>
  </g>

  <!-- PANEL C: C-V Characteristics Comparison -->
  <g transform="translate(670, 20)">
    <rect width="290" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) C-V 특성 곡선의 결정적 차이</text>

    <!-- C-V Curve Graph -->
    <g transform="translate(15, 42)">
      <rect width="260" height="235" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" fill="#fde047" font-size="8.8" font-weight="800">C-V 곡선 (P형 기판 기준 NMOS)</text>

      <!-- Axes -->
      <line x1="25" y1="180" x2="245" y2="180" stroke="#94a3b8" stroke-width="1.2"/>
      <line x1="120" y1="180" x2="120" y2="30" stroke="#94a3b8" stroke-width="1.2"/>
      <text x="235" y="192" fill="#94a3b8" font-size="7">V_G</text>
      <text x="110" y="25" fill="#94a3b8" font-size="7">0 V</text>
      <text x="8" y="35" fill="#94a3b8" font-size="7">Cap</text>

      <!-- Cox line -->
      <line x1="25" y1="50" x2="245" y2="50" stroke="#64748b" stroke-dasharray="2,2"/>
      <text x="2" y="53" fill="#38bdf8" font-size="7.5" font-weight="800">C_ox</text>

      <!-- Cmin line -->
      <line x1="25" y1="140" x2="245" y2="140" stroke="#64748b" stroke-dasharray="2,2"/>
      <text x="2" y="143" fill="#f87171" font-size="7.5" font-weight="800">C_min</text>

      <!-- Regions -->
      <text x="35" y="42" fill="#94a3b8" font-size="7">축적(Acc)</text>
      <text x="90" y="170" fill="#94a3b8" font-size="7">공핍(Dep)</text>
      <text x="175" y="170" fill="#94a3b8" font-size="7">반전(Inv)</text>

      <!-- Curve 1: MOS Cap High Frequency (HF, stays at Cmin) -->
      <path d="M 30 50 L 75 50 Q 120 70 145 140 L 240 140" stroke="#ef4444" stroke-width="2" fill="none"/>
      <text x="155" y="152" fill="#f87171" font-size="7.5" font-weight="800">① MOS Cap 고주파 (HF)</text>

      <!-- Curve 2: MOS Cap Low Frequency (LF, recovers to Cox) -->
      <path d="M 30 50 L 75 50 Q 120 70 145 140 Q 180 140 210 60 L 240 50" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="3,3" fill="none"/>
      <text x="150" y="85" fill="#38bdf8" font-size="7.2">② MOS Cap 저주파 (LF)</text>

      <!-- Curve 3: MOSFET (HF & LF both recover to Cox!) -->
      <path d="M 30 50 L 75 50 Q 120 70 145 140 Q 170 140 195 55 L 240 50" stroke="#10b981" stroke-width="2.5" fill="none"/>
      <text x="145" y="42" fill="#34d399" font-size="7.8" font-weight="900">③ MOSFET (HF/LF 모두 Cox!)</text>

      <text x="12" y="202" fill="#cbd5e1" font-size="7.2">• 축적 영역: 다수캐리어(정공) 반응으로 모두 C_ox</text>
      <text x="12" y="214" fill="#cbd5e1" font-size="7.2">• 공핍 영역: 공핍층(W_dep) 확장으로 모두 C 하강</text>
      <text x="12" y="226" fill="#fde047" font-size="7.5" font-weight="800">• 반전 영역: S/D 유무에 따라 고주파 거동 완전 분기!</text>
    </g>

    <!-- Application Summary -->
    <g transform="translate(15, 288)">
      <rect width="260" height="118" rx="6" fill="#0b1329" stroke="#f59e0b"/>
      <text x="10" y="18" fill="#fbbf24" font-size="8.8" font-weight="800">★ 응용 및 실무 용도 비교</text>

      <text x="10" y="34" fill="#38bdf8" font-size="7.8" font-weight="800">■ MOS Cap의 역할:</text>
      <text x="10" y="48" fill="#cbd5e1" font-size="7.2">• FAB 공정 모니터링 (t_ox, V_FB, D_it, N_A 계측)</text>
      <text x="10" y="60" fill="#cbd5e1" font-size="7.2">• DRAM 1T-1C 스토리지 커패시터, Varactor</text>

      <text x="10" y="78" fill="#34d399" font-size="7.8" font-weight="800">■ MOSFET의 역할:</text>
      <text x="10" y="92" fill="#cbd5e1" font-size="7.2">• CPU, GPU, AP의 초고속 CMOS 논리 스위치</text>
      <text x="10" y="106" fill="#cbd5e1" font-size="7.2">• 아날로그 전압/전류 증폭기 (Amplifier)</text>
    </g>
  </g>

  <!-- Arrow marker definition -->
  <defs>
    <marker id="arrowRed" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#ef4444" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- Section 1: Overview of Fundamental Differences -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 개요: MOS Cap과 MOSFET의 핵심 4대 차이점 요약
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체 공학을 공부할 때 <strong>MOS Cap(Metal-Oxide-Semiconductor Capacitor)</strong>을 먼저 배우고 그 뒤에 <strong>MOSFET</strong>을 배우는 이유는, 
            MOSFET의 심장부가 바로 MOS Cap이기 때문입니다. 하지만 두 소자는 구조, 캐리어 공급 메커니즘, 동작 모드에서 매우 결정적인 물리적 차이를 가집니다.
          </p>

          <div style="overflow-x:auto; margin-bottom:16px;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">비교 항목</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">MOS Cap (모스 커패시터)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">MOSFET (모스펫 전계효과트랜지스터)</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">① 단자 수 및 구성</td>
                  <td style="padding:10px 14px;"><strong>2단자 (Gate, Body)</strong><br>수평 단자 없음</td>
                  <td style="padding:10px 14px;"><strong>4단자 (Gate, Drain, Source, Body)</strong><br>고농도 소스/드레인($N^+$) 접합 구비</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">② 소자 분류 및 기능</td>
                  <td style="padding:10px 14px;"><strong>수동 소자 (Passive)</strong><br>정전용량 충·방전, 수평 직류 전류 없음 ($I_{DS}=0$)</td>
                  <td style="padding:10px 14px;"><strong>능동 소자 (Active)</strong><br>게이트 전압으로 수평 직류 전류($I_{DS}$)를 On/Off 제어·증폭</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">③ 반전층 전자 공급원<br>(가장 결정적 차이!)</td>
                  <td style="padding:10px 14px; color:#f87171; font-weight:700;"><strong>열적 전자-정공 쌍 생성 (Thermal EHP)</strong><br>응답 속도 매우 느림 ($\tau \sim \text{ms}$)</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;"><strong>소스/드레인($N^+$) 전자 저수지</strong><br>피코초($\text{ps}$) 단위 초고속 직접 주입</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">④ 고주파(HF) C-V 반전 용량</td>
                  <td style="padding:10px 14px; color:#f87171;">전자가 AC 신호를 못 따라와 <strong>$C_{min}$에 정체</strong></td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:800;">S/D 공급 덕분에 고주파에서도 <strong>$C_{ox}$로 100% 회복</strong></td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">⑤ 주요 실무 응용</td>
                  <td style="padding:10px 14px;">• 팹 공정 계측 ($t_{ox}, V_{FB}, D_{it}, N_A$ 역산)<br>• DRAM 1T-1C 메모리 셀 스토리지 커패시터</td>
                  <td style="padding:10px 14px;">• 초고속 디지털 마이크로프로세서 (CMOS 로직)<br>• 아날로그 RF 고주파 증폭기 (LNA, PA)</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Section 2: Carrier Supply Mechanism -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 물리적 본질: 반전층(Inversion) 전자는 어디서 오는가?
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            P형 실리콘 기판 위에 게이트 전압($V_G > V_{th}$)을 걸어 전자를 끌어모으는 **강반전(Strong Inversion)** 상태를 만들 때, 
            <strong>"그 전자가 대체 어디서 튀어나오는가?"</strong>가 두 소자의 동작을 완전히 가르는 분수령입니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #ef4444; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#f87171; font-size:1.02rem; font-weight:800; margin-bottom:8px;">
              ■ MOS Cap: "빌려올 곳이 없어 스스로 태어나야 한다" (열 생성의 한계)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              MOS Cap에는 게이트 아래에 소스나 드레인이 없습니다. P형 기판 내부에는 다수캐리어인 정공만 바글바글하고, 전자(소수캐리어)는 거의 전무($n_p \approx n_i^2 / N_A \approx 10^3\,\text{cm}^{-3}$)합니다.
              <br>따라서 반전층을 채울 전자는 <strong>오직 실리콘 원자 격자의 열진동에 의해 전자-정공 쌍이 자발적으로 찢어지는 '열 생성(Thermal EHP Generation, SRH Generation)'</strong>에만 의존해야 합니다.
              <br>• 문제점: 이 열 생성 과정은 수 마이크로초에서 수 밀리초($\tau_{gen} \sim 10^{-4} \sim 10^{-2}\,\text{s}$)나 걸리는 **매우 느린 화학반응과 같은 물리 과정**입니다.
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:18px;">
            <h4 style="color:#34d399; font-size:1.02rem; font-weight:800; margin-bottom:8px;">
              ■ MOSFET: "옆집에 전자가 무한대로 쌓여 있다" (S/D 초고속 직통 공급)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              MOSFET은 채널 바로 양옆에 비소(As)나 인(P)으로 고농도 도핑된 **$N^+$ Source와 Drain($n \approx 10^{20}\,\text{cm}^{-3}$)**이 맞닿아 있습니다.
              <br>게이트 전압이 양(+)으로 올라가 채널 표면의 전위가 당겨지는 순간, <strong>소스와 드레인이라는 거대한 전자 저수지(Reservoir)에서 전자들이 피코초($\tau \sim 10^{-12}\,\text{s}$) 단위의 광속으로 채널에 밀려들어옵니다</strong>.
              <br>• 따라서 MOSFET은 게이트 전압이 아무리 초고속(수 GHz)으로 변하더라도 반전층 전자를 실시간으로 공급하고 회수할 수 있습니다.
            </p>
          </div>
        </div>

        <!-- Section 3: C-V Characteristics -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. C-V 특성 곡선에서의 고주파(HF) 거동 차이 완벽 해부
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            이 캐리어 공급원의 차이는 소자의 <strong>C-V(용량-전압) 특성 곡선</strong>에서 가장 극적인 차이를 만들어냅니다.
          </p>

          <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:22px; margin-bottom:14px;">
            <li><strong>1. 축적 영역 ($V_G < V_{FB}$)</strong>:
              <br>P형 기판의 다수캐리어인 정공($p$)들이 산화막 계면으로 모여듭니다. 정공은 기판 어디에나 풍부하므로 유전완화 시간($\tau \sim 10^{-14}\,\text{s}$) 만에 즉각 반응합니다. 따라서 <strong>MOS Cap과 MOSFET 모두 주파수와 무관하게 산화막 정전용량 $C_{ox}$</strong>를 나타냅니다.
            </li>
            <li><strong>2. 공핍 영역 ($V_{FB} < V_G < V_{th}$)</strong>:
              <br>게이트 양전압이 정공들을 기판 속으로 밀어내어 공핍층 폭($W_{dep}$)이 넓어집니다. 산화막 용량($C_{ox}$)과 공핍층 용량($C_{dep}$)이 직렬 연결($1/C = 1/C_{ox} + 1/C_{dep}$)되므로, <strong>두 소자 모두 $C$가 점점 감소</strong>합니다.
            </li>
            <li><strong>3. 반전 영역 ($V_G > V_{th}$) ➔ 분기점!</strong>:
              <br>• <strong>MOS Cap 저주파 (LF, ~10Hz)</strong>: 전압 신호가 천천히 변하므로 열 생성된 전자들이 신호를 따라갑니다. 전자가 게이트 전하를 스크리닝하여 $C$가 다시 **$C_{ox}$로 회복**됩니다.
              <br>• <strong>MOS Cap 고주파 (HF, 100kHz~1MHz)</strong>: 신호가 너무 빨라 열 생성 속도가 못 따라갑니다. 전자가 AC 전하 변조를 전혀 감당하지 못하므로, 공핍층 최대 폭($W_{dep,max}$)만 반응하여 **커패시턴스가 최솟값인 $C_{min}$에 그대로 갇혀버립니다**.
              <br>• <strong>MOSFET (고주파 HF에서도!)</strong>: 고주파 AC 신호가 걸려도 **소스/드레인($N^+$)에서 전자가 즉각 채널로 쏟아져 들어오므로, 고주파에서도 커패시턴스가 $C_{ox}$로 100% 온전히 솟구쳐 오릅니다!**
            </li>
          </ul>
        </div>

        <!-- Section 4: Engineering Applications -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#ef4444; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. 실무 응용: 왜 두 소자를 각각 따로 쓰는가?
          </h3>
          <div style="background:#0f172a; border-left:4px solid #f59e0b; padding:16px 20px; border-radius:0 8px 8px 0;">
            <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:18px;">
              <li><strong>MOS Cap의 독보적 가치 (진단 도구)</strong>:
                <br>구조가 단순(패턴 1개)하여 웨이퍼 스크라이브 라인(Test Element Group, TEG)에 항상 심어놓습니다. C-V 측정을 통해 **산화막 실제 두께($t_{ox}$), 평탄대 전압($V_{FB}$), 실리콘 기판 도핑 농도($N_A$), 계면 결함 밀도($D_{it}$), 산화막 고정 전하($Q_f$)** 등 공정의 모든 물리 파라미터를 비파괴적으로 정밀 진단하는 최고의 계측 소자입니다.
              </li>
              <li><strong>MOSFET의 독보적 가치 (컴퓨팅의 심장)</strong>:
                <br>게이트에 걸리는 전압으로 소스-드레인 사이의 수평 전류($I_{DS}$)를 On/Off 시키는 3단자 전압 제어 스위치입니다. 0과 1을 판별하는 디지털 인버터, 낸드 플래시 제어, 고성능 AI GPU 연산 코어의 100%가 MOSFET으로 구동됩니다.
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

    # Step 1: Shift existing 87 topics (q-87 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(87, 0, -1):
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

    # Step 4: Update header description to 88 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 'MOS Cap과 MOSFET의 본질적 차이'이 위치하며, 총 88개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 MOS Cap vs MOSFET topic!")
