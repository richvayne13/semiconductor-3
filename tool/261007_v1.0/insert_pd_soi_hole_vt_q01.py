# -*- coding: utf-8 -*-
"""
insert_pd_soi_hole_vt_q01.py
사용자 질문:
"pd-soi에서 채널아래 쌓인정공들의 양전하영역은 왜 vt를낮추는걸까 로직이궁금해"

대시보드 최상단 Q01로 신규 추가하고, 기존 86개 질문을 Q02~Q87로 시프트 (총 87개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (PD-SOI 플로팅 바디 · 양전하 정공 축적에 따른 Vt 강하 로직)",
    "title": "PD-SOI에서 채널 아래 쌓인 정공(양전하)은 왜 Vt를 낮출까? (바디 전위 상승과 장벽 붕괴 로직)",
    "nav_title": "PD-SOI 채널 아래 쌓인 정공이 Vt 낮추는 로직",
    "summary": [
        "<strong>1. 정공 축적과 바디 전위 상승 ($V_B > 0$)</strong>: 드레인 핀치오프 강전계에서 충격 이온화(Impact Ionization)로 생성된 정공($h^+$)들이 절연체(BOX)와 접합 장벽에 갇혀 플로팅 바디에 축적되면서 <strong>바디 전위가 양(+)으로 부유 상승($V_{BS} > 0$)</strong>합니다.",
        "<strong>2. 로직 ① 바디 효과 수식 역전</strong>: 벌크에서는 바디 역바이어스로 $V_{th}$가 높아지지만, PD-SOI에서는 정공 누적으로 바디에 <strong>'순방향 바이어스'</strong>가 걸리는 효과가 발생하여 $V_{th} = V_{FB} + 2\\phi_F + \\frac{\\sqrt{2\\epsilon q N_A (2\\phi_F - V_B)}}{C_{ox}}$ 공식에 의해 <strong>루트 항($2\\phi_F - V_B$)이 감소하면서 $V_{th}$가 직접 강하</strong>합니다.",
        "<strong>3. 로직 ② 소스-채널 전위 장벽 강하 (Barrier Lowering)</strong>: 채널 아래 양전하 층이 형성되면 채널 영역의 전위가 상향 편향되어 <strong>소스($N^+$) 전자가 채널로 넘어오지 못하게 가로막던 전위 장벽(Built-in Potential Barrier)이 주저앉아</strong> 낮은 게이트 전압에서도 전자가 쉽게 주입됩니다.",
        "<strong>4. 치명적 결과(Kink 현상)와 해결책(FD-SOI)</strong>: $V_{th}$가 낮아지면 드레인 전류가 비정상적으로 꺾여 치솟는 <strong>킹크 효과(Kink Effect)</strong>와 소자 이력 현상(History Effect)이 발생합니다. 이를 근본적으로 해결하기 위해 중성 바디 자체를 없앤 <strong>완전공핍형 FD-SOI</strong>로 기술이 진화했습니다."
    ],
    "svg_title": "📊 [PD-SOI 플로팅 바디 정공 축적 & Vt 강하 메커니즘] (A) 정공 갇힘과 바디 전위 상승 | (B) Vt 강하 3대 물리 로직 | (C) 킹크 효과와 FD-SOI 솔루션",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Hole Trapping Mechanism in PD-SOI -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 충격 이온화와 정공 갇힘 메커니즘</text>

    <!-- Transistor Structure -->
    <g transform="translate(15, 42)">
      <rect width="270" height="235" rx="6" fill="#1e293b" stroke="#334155"/>

      <!-- Gate -->
      <rect x="65" y="16" width="140" height="12" fill="#475569" rx="1"/>
      <text x="108" y="25" fill="#fff" font-size="7.5">Gate (VG)</text>
      <rect x="65" y="28" width="140" height="4" fill="#a855f7"/>

      <!-- Source & Drain -->
      <rect x="20" y="32" width="45" height="50" fill="#f59e0b" rx="1"/>
      <text x="28" y="60" fill="#000" font-size="8" font-weight="800">Source (N+)</text>
      <rect x="205" y="32" width="45" height="50" fill="#f59e0b" rx="1"/>
      <text x="216" y="60" fill="#000" font-size="8" font-weight="800">Drain (N+)</text>

      <!-- Gate Depletion Layer (PD-SOI: partially depleted) -->
      <rect x="65" y="32" width="140" height="25" fill="#10b981" opacity="0.35"/>
      <text x="85" y="47" fill="#a7f3d0" font-size="7.5">게이트 공핍층 (W_dep)</text>

      <!-- Neutral Floating Body (Under depletion layer) -->
      <rect x="65" y="57" width="140" height="35" fill="#dc2626" opacity="0.25" stroke="#ef4444" stroke-dasharray="2,2"/>
      <text x="75" y="70" fill="#fca5a5" font-size="8" font-weight="800">중성 바디 (Neutral Body)</text>
      <text x="80" y="83" fill="#fecaca" font-size="7.2">[도망칠 곳 없는 플로팅 고립]</text>

      <!-- Impact Ionization at Drain -->
      <circle cx="198" cy="45" r="9" fill="#ef4444" opacity="0.7"/>
      <text x="193" y="48" fill="#fff" font-size="8" font-weight="900">💥</text>
      <text x="145" y="30" fill="#fbbf24" font-size="7" font-weight="700">드레인 고전계 ➔ 충격 이온화</text>

      <!-- Electron and Hole flow -->
      <path d="M 195 40 L 215 40" stroke="#38bdf8" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
      <text x="202" y="36" fill="#38bdf8" font-size="6.5">e⁻ ➔ 드레인</text>

      <path d="M 190 50 Q 170 70 140 72" stroke="#f43f5e" stroke-width="2" stroke-dasharray="2,2" fill="none"/>
      <text x="145" y="66" fill="#f43f5e" font-size="7" font-weight="800">h⁺ (정공 이동)</text>

      <!-- Accumulated holes (+) inside body -->
      <g fill="#ef4444" font-size="8" font-weight="900">
        <text x="85" y="85">⊕</text><text x="105" y="85">⊕</text><text x="125" y="85">⊕</text>
        <text x="95" y="77">⊕</text><text x="115" y="77">⊕</text><text x="135" y="77">⊕</text>
      </g>

      <!-- BOX Oxide Layer -->
      <rect x="15" y="92" width="240" height="18" fill="#0284c7" opacity="0.6"/>
      <text x="55" y="105" fill="#fff" font-size="8" font-weight="800">매몰 산화막 (Buried Oxide, BOX) 절연벽!</text>

      <!-- Bottom Substrate -->
      <rect x="15" y="110" width="240" height="20" fill="#334155"/>
      <text x="90" y="123" fill="#94a3b8" font-size="7.5">기판 웨이퍼 (Substrate)</text>

      <!-- Summary text inside card -->
      <text x="10" y="148" fill="#cbd5e1" font-size="7.5">1. 드레인 전자-원자 격자 충돌 ➔ EHP 생성</text>
      <text x="10" y="162" fill="#cbd5e1" font-size="7.5">2. 전자는 드레인으로 흡수, 정공(h⁺)은 채널 아래 밀려남</text>
      <text x="10" y="176" fill="#cbd5e1" font-size="7.5">3. 바닥(BOX)과 양옆(S/D) 장벽에 갇혀 정공 대량 축적!</text>
      <text x="10" y="190" fill="#fde047" font-size="7.8" font-weight="800">➔ 플로팅 바디 전위가 양(+)으로 급상승: V_body &gt; 0</text>
    </g>

    <!-- Bottom summary box -->
    <rect x="15" y="295" width="270" height="112" rx="6" fill="#0b1329" stroke="#38bdf8"/>
    <text x="22" y="315" fill="#38bdf8" font-size="9" font-weight="800">🔑 정공이 축적되는 구조적 핵심:</text>
    <text x="22" y="333" fill="#cbd5e1" font-size="7.8">• 벌크 MOS: 기판 콘택트로 정공이 즉시 빠져나감</text>
    <text x="22" y="348" fill="#f87171" font-size="7.8">• PD-SOI: 바닥 BOX 산화막 때문에 바디 콘택트 없음!</text>
    <text x="22" y="364" fill="#cbd5e1" font-size="7.8">• 갈 곳 없는 정공이 바디에 갇혀 '양전하 저수지' 형성</text>
    <text x="22" y="380" fill="#fde047" font-size="8" font-weight="800">➔ 이것이 바로 플로팅 바디 효과(Floating Body Effect)</text>
    <text x="22" y="396" fill="#a5f3fc" font-size="7.5">이제 이 양전하가 왜 Vt를 낮추는지 (B)에서 해부합니다!</text>
  </g>

  <!-- PANEL B: 3 Logics of Vt Lowering -->
  <g transform="translate(340, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 양전하가 Vt를 낮추는 3대 물리 로직</text>

    <!-- Logic 1: Body Effect Formula -->
    <g transform="translate(15, 42)">
      <rect width="280" height="112" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="10" y="16" fill="#38bdf8" font-size="8.8" font-weight="800">로직 ① 바디 효과 공식의 '순방향 역전'</text>
      <text x="10" y="32" fill="#cbd5e1" font-size="7.5">벌크 MOS는 바디가 접지라 V_SB ≥ 0 이지만,</text>
      <text x="10" y="46" fill="#fde047" font-size="7.8" font-weight="800">PD-SOI는 정공 덕분에 V_body &gt; 0 (순방향 바디 바이어스!)</text>

      <rect x="8" y="54" width="264" height="26" rx="3" fill="#0b1329" stroke="#334155"/>
      <text x="14" y="70" fill="#ffffff" font-size="7.8">Vt = V_th0 + γ [ √(2φF - V_body) - √(2φF) ]</text>

      <text x="10" y="94" fill="#cbd5e1" font-size="7.5">• V_body &gt; 0 이므로 루트 내부 (2φF - V_body) 값이 축소!</text>
      <text x="10" y="106" fill="#34d399" font-size="7.8" font-weight="800">➔ 바디 효과 항이 마이너스(-)가 되어 Vt 직접 강하! (ΔVt &lt; 0)</text>
    </g>

    <!-- Logic 2: Energy Barrier Lowering -->
    <g transform="translate(15, 162)">
      <rect width="280" height="116" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="10" y="16" fill="#fbbf24" font-size="8.8" font-weight="800">로직 ② 소스-채널 전위 장벽 강하 (Barrier Lowering)</text>
      <text x="10" y="32" fill="#cbd5e1" font-size="7.5">• 소스(N+) 전자가 채널(P)로 못 넘어가게 막는 빌트인 장벽</text>
      <text x="10" y="46" fill="#cbd5e1" font-size="7.5">• 바디에 양전하(⊕)가 쌓이면 채널 전위가 위로 번쩍 들림!</text>

      <!-- Mini Energy Barrier Diagram -->
      <g transform="translate(15, 52)">
        <path d="M 10 32 L 60 32 Q 120 5 180 32 L 230 32" stroke="#64748b" stroke-width="1.5" fill="none"/>
        <text x="110" y="14" fill="#94a3b8" font-size="7">원래 장벽</text>
        <path d="M 10 32 L 60 32 Q 120 18 180 32 L 230 32" stroke="#f43f5e" stroke-width="2" fill="none"/>
        <text x="110" y="27" fill="#f43f5e" font-size="7.5" font-weight="800">낮아진 장벽! (V_B &gt; 0)</text>
      </g>

      <text x="10" y="98" fill="#cbd5e1" font-size="7.5">• 장벽이 주저앉으니 게이트 전압을 조금만 줘도</text>
      <text x="10" y="110" fill="#fde047" font-size="7.8" font-weight="800">➔ 소스 전자가 채널로 쏟아져 들어옴! ➔ Vt가 낮아짐!</text>
    </g>

    <!-- Logic 3: Depletion Charge Shrinkage -->
    <g transform="translate(15, 286)">
      <rect width="280" height="120" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="10" y="16" fill="#f87171" font-size="8.8" font-weight="800">로직 ③ 게이트가 치워야 할 공핍 전하(|Qdep|) 축소</text>
      <text x="10" y="32" fill="#cbd5e1" font-size="7.5">• Vt = V_FB + 2φF + |Q_dep| / C_ox</text>
      <text x="10" y="48" fill="#cbd5e1" font-size="7.5">• 바디가 스스로 양(+) 전위를 띄니 공핍층 폭이 얇아짐:</text>
      <text x="20" y="63" fill="#ffffff" font-size="7.8">W_dep = √[ 2ε(2φF - V_body) / (q NA) ] ↓</text>
      <text x="10" y="80" fill="#cbd5e1" font-size="7.5">• 게이트가 채널을 켤 때 치워야 하는 고정 음이온 부담(|Qdep|) 감소</text>
      <text x="10" y="96" fill="#fca5a5" font-size="7.5">• 산화막에 걸어주어야 할 전압(Vox = |Qdep|/Cox)이 대폭 절감!</text>
      <text x="10" y="112" fill="#34d399" font-size="7.8" font-weight="800">➔ 따라서 훨씬 낮은 게이트 전압(Vt 하강)에서 반전층 형성!</text>
    </g>
  </g>

  <!-- PANEL C: Circuit Consequence & Solution -->
  <g transform="translate(670, 20)">
    <rect width="290" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) 치명적 킹크 효과와 FD-SOI의 해법</text>

    <!-- Consequence: Kink Effect -->
    <g transform="translate(15, 42)">
      <rect width="260" height="160" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="10" y="16" fill="#f87171" font-size="8.8" font-weight="800">1. 치명적 부작용: 킹크 효과 (Kink Effect)</text>

      <!-- ID-VD Graph with Kink -->
      <g transform="translate(15, 24)">
        <line x1="15" y1="75" x2="215" y2="75" stroke="#94a3b8" stroke-width="1.2"/>
        <line x1="15" y1="75" x2="15" y2="5" stroke="#94a3b8" stroke-width="1.2"/>
        <text x="220" y="78" fill="#94a3b8" font-size="6.5">V_DS</text>
        <text x="8" y="10" fill="#94a3b8" font-size="6.5">I_D</text>

        <!-- Normal curve (dashed) -->
        <path d="M 15 75 Q 40 40 80 35 L 210 33" stroke="#64748b" stroke-width="1.2" stroke-dasharray="2,2" fill="none"/>
        <text x="140" y="28" fill="#94a3b8" font-size="6.5">정상 포화 특성</text>

        <!-- Kinked curve (solid pink) -->
        <path d="M 15 75 Q 40 40 80 35 L 110 34 Q 130 30 160 14 L 210 10" stroke="#f43f5e" stroke-width="2" fill="none"/>
        <circle cx="130" cy="30" r="3" fill="#fbbf24"/>
        <text x="110" y="46" fill="#fde047" font-size="7.5" font-weight="800">⚡ 킹크 굴곡 (Kink Point)</text>
        <text x="135" y="10" fill="#f43f5e" font-size="7" font-weight="800">Vt 하강 ➔ 전류 급증!</text>
      </g>

      <text x="10" y="116" fill="#cbd5e1" font-size="7.5">• V_DS 상승 ➔ 충격 이온화 ➔ 정공 누적 (V_B ↑)</text>
      <text x="10" y="130" fill="#fde047" font-size="7.5" font-weight="800">• Vt가 뚝 떨어져 드레인 전류(ID)가 계단식 급증!</text>
      <text x="10" y="144" fill="#cbd5e1" font-size="7.2">• 아날로그 출력 저항(rout) 붕괴 및 이력 현상(Hysteresis)</text>
    </g>

    <!-- Ultimate Solution: FD-SOI -->
    <g transform="translate(15, 210)">
      <rect width="260" height="195" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="10" y="16" fill="#34d399" font-size="8.8" font-weight="800">2. 궁극의 솔루션: FD-SOI (완전공핍)</text>

      <rect x="8" y="26" width="244" height="65" rx="4" fill="#0b1329" stroke="#334155"/>
      <text x="14" y="42" fill="#38bdf8" font-size="7.5" font-weight="800">■ PD-SOI: T_si &gt; W_dep (중성 바디 존재)</text>
      <text x="24" y="55" fill="#f87171" font-size="7">• 정공이 갇힐 방(중성 바디)이 있어 문제 발생</text>
      <text x="14" y="70" fill="#10b981" font-size="7.5" font-weight="800">■ FD-SOI: T_si &lt; W_dep (5~7nm 극박막)</text>
      <text x="24" y="83" fill="#34d399" font-size="7">• 바디 100% 완전 공핍 ➔ 정공이 갇힐 방 원천 소멸!</text>

      <text x="10" y="106" fill="#cbd5e1" font-size="7.5">• 정공이 축적될 장소가 없으므로 V_body 상승 0%!</text>
      <text x="10" y="120" fill="#cbd5e1" font-size="7.5">• 킹크 효과(Kink) 및 Vt 요동 원천 박멸</text>
      <text x="10" y="134" fill="#fde047" font-size="7.8" font-weight="800">• C_dep ≈ 0 실현으로 SS ≈ 60 mV/dec 복원!</text>
      <text x="10" y="150" fill="#a7f3d0" font-size="7.5">• 기판 후면(Back-gate) 전압 제어로 동적 Vt 튜닝</text>

      <rect x="8" y="162" width="244" height="24" rx="3" fill="#064e3b" stroke="#10b981"/>
      <text x="14" y="178" fill="#a7f3d0" font-size="7.5" font-weight="800">🎯 결론: 정공 갇힘의 부작용이 FD-SOI를 낳음!</text>
    </g>
  </g>

  <!-- Arrow marker definition -->
  <defs>
    <marker id="arrowBlue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#38bdf8" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- Section 1: Introduction to Hole Accumulation -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 왜 하필 정공(양전하)들이 채널 아래(바디)에 쌓일까? (구조적 고립)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            PD-SOI(Partially Depleted SOI)의 핵심은 실리콘 박막 두께($T_{si}$)가 게이트 최대 공핍층 폭($W_{dep}$)보다 두꺼워($T_{si} > W_{dep}$), 
            <strong>게이트 공핍층 아래에 전하가 중성인 실리콘 층(Neutral Body, 중성 바디)이 고스란히 남아있다는 점</strong>입니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:18px;">
            <h4 style="color:#38bdf8; font-size:1.05rem; font-weight:800; margin-bottom:8px;">⚡ 정공이 갇히는 3단계 프로세스</h4>
            <ol style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:18px;">
              <li><strong>충격 이온화(Impact Ionization)에 의한 EHP 생성</strong>: 드레인에 높은 전압($V_{DS}$)이 인가되면 드레인 근처 핀치오프 강전계에서 가속된 전자가 실리콘 원자 격자와 정면 충돌하여 전자-정공 쌍(EHP)을 대량 방출합니다.</li>
              <li><strong>캐리어의 분리와 이동</strong>: 생성된 전자는 양의 전압이 걸린 드레인($+V_D$)으로 빨려 들어가지만, **양전하를 띤 정공($h^+$)은 드레인 전계에 의해 밀려나 채널 아래 전위가 가장 낮은 중성 바디 영역으로 탈출**합니다.</li>
              <li><strong>도망칠 곳 없는 플로팅 고립(Trapping)</strong>:
                <br>• 바닥은 절연체인 **매몰 산화막(BOX)**이 막고 있고,
                <br>• 양옆은 소스/드레인($N^+$)과의 P-N 접합 역방향/빌트인 장벽이 가로막고 있으며,
                <br>• 일반 벌크 MOS와 달리 **바디 콘택트(Body Contact) 전극이 외부와 연결되어 있지 않습니다(Floating Body)**.
              </li>
            </ol>
          </div>
          <p style="font-size:0.92rem; line-height:1.7; color:#fde047;">
            ★ 결과: 갈 곳 없는 수억 개의 정공들이 중성 바디에 갇혀 **'양전하 저수지'**를 형성하고, 이로 인해 **플로팅 바디 전위가 0V에서 양(+)의 전위로 부유 상승($V_{body} > 0$, $V_{BS} > 0$)**하게 됩니다!
          </p>
        </div>

        <!-- Section 2: 3 Logics of Vt Lowering -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 채널 아래 쌓인 양전하가 Vt를 낮추는 3가지 물리적 로직
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:14px;">
            질문자님께서 가장 궁금해하신 <em>"왜 양전하 영역이 $V_{th}$를 낮출까?"</em>에 대한 물리적 메커니즘을 3가지 상호 보완적 관점으로 명쾌하게 분해해 드립니다.
          </p>

          <!-- Logic 1 -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:16px; border:1px solid #334155;">
            <h4 style="color:#38bdf8; font-size:1.02rem; font-weight:800; margin-bottom:8px;">
              로직 ① [교과서 수식 관점] 바디 효과(Body Effect)의 순방향 역전
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7; margin-bottom:10px;">
              일반 벌크 MOSFET에서는 기판(바디)이 소스에 비해 0V이거나 역바이어스($V_{SB} \ge 0$)가 걸려 문턱전압이 높아지는 것이 일반적입니다. 하지만 PD-SOI에서는 정공들이 바디 전위를 강제로 띄워 <strong>소스에 대해 양(+)의 바디 전압($V_{BS} > 0$, 즉 $V_{SB} < 0$)이라는 순방향 바디 바이어스(Forward Body Bias)</strong>를 형성합니다.
            </p>
            <div style="background:#0b1329; padding:12px; border-radius:6px; font-family:monospace; color:#f8fafc; font-size:0.92rem; margin-bottom:10px;">
              $$V_{th} = V_{th0} + \gamma \left( \sqrt{2\phi_F - V_{BS}} - \sqrt{2\phi_F} \right)$$
            </div>
            <p style="color:#e2e8f0; font-size:0.9rem; line-height:1.7;">
              $V_{BS} > 0$이 대입되면 루트 내부의 $(2\phi_F - V_{BS})$ 항이 $(2\phi_F)$보다 작아집니다! 
              따라서 뒤쪽의 바디 효과 항 전체가 음수($-$)가 되면서, <strong>문턱전압 $V_{th}$는 원래 값보다 직접적으로 깎여서 낮아집니다 ($\Delta V_{th} < 0$)</strong>.
            </p>
          </div>

          <!-- Logic 2 -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:16px; border:1px solid #334155;">
            <h4 style="color:#fbbf24; font-size:1.02rem; font-weight:800; margin-bottom:8px;">
              로직 ② [에너지 밴드 관점] 소스-채널 전위 장벽 강하 (Potential Barrier Lowering)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7; margin-bottom:10px;">
              NMOS가 꺼져 있는 이유는 소스($N^+$)에 가득 차 있는 전자들이 채널($P$)로 넘어오지 못하도록 **P형 기판의 높은 전위 장벽(Built-in Potential Barrier, $q\Phi_B$)**이 가로막고 있기 때문입니다.
            </p>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.7; padding-left:20px;">
              <li>채널 바로 아래에 정공들(양전하, $\oplus$)이 빽빽하게 모여들면, 그 양전하들이 채널 쪽으로 상향 전기력선을 뿜어냅니다.</li>
              <li>정전기적 유도에 의해 채널 내부의 전위(Potential)가 붕 뜨게 되고, <strong>전자 입장에서 바라본 전도대 에너지 장벽($E_c$)이 아래로 푹 주저앉습니다(Barrier Lowering)</strong>.</li>
              <li>장벽이 주저앉았으니, 게이트가 굳이 높은 전압을 걸어 채널을 강제로 당겨주지 않아도 **훨씬 작은 게이트 전압에서 소스의 전자들이 채널로 쏟아져 들어오게 됩니다**. 즉, 트랜지스터가 훨씬 쉽게 켜지므로 $V_{th}$가 낮아진 것입니다.</li>
            </ul>
          </div>

          <!-- Logic 3 -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:16px; border:1px solid #334155;">
            <h4 style="color:#f87171; font-size:1.02rem; font-weight:800; margin-bottom:8px;">
              로직 ③ [전하 보존 관점] 게이트가 치워야 할 공핍 전하($|Q_{dep}|$) 숙제 감소
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7; margin-bottom:10px;">
              게이트가 트랜지스터를 켠다(Strong Inversion)는 것은 게이트 아래 실리콘 표면의 양전하(정공)를 밀어내어 <strong>음이온 공핍층($|Q_{dep}| = q N_A W_{dep}$)을 만들고, 그 공간 전하를 지탱하기 위해 게이트 산화막에 전압($V_{ox} = |Q_{dep}|/C_{ox}$)을 걸어주는 것</strong>을 뜻합니다:
            </p>
            <div style="background:#0b1329; padding:12px; border-radius:6px; font-family:monospace; color:#f8fafc; font-size:0.92rem; margin-bottom:10px;">
              $$V_{th} = V_{FB} + 2\phi_F + \frac{|Q_{dep}|}{C_{ox}}$$
            </div>
            <p style="color:#e2e8f0; font-size:0.9rem; line-height:1.7;">
              그런데 바디 자체가 양(+)의 전위를 띄게 되면($V_B > 0$), 게이트와 바디 사이의 유효 전압차가 줄어들어 <strong>공핍층 두께($W_{dep} = \sqrt{\frac{2\epsilon(2\phi_F - V_B)}{q N_A}}$)가 얇아집니다</strong>.
              <br>공핍층이 얇아졌으니 게이트가 부담해야 하는 고정 음이온 전하량 $|Q_{dep}|$가 현저히 줄어들고, 따라서 산화막에 걸어주어야 할 전압 부담이 대폭 줄어들어 <strong>$V_{th}$가 크게 낮아지게 되는 것</strong>입니다!
            </p>
          </div>
        </div>

        <!-- Section 3: Consequence (Kink Effect) -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. Vt가 낮아지는 게 좋은 게 아니다? 치명적 '킹크 효과(Kink Effect)'
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            일반적으로 $V_{th}$가 낮아지면 전류가 잘 흘러 좋을 것 같지만, 이 현상은 **의도치 않게 드레인 전압($V_{DS}$)에 따라 트랜지스터의 $V_{th}$가 제멋대로 널뛰는 치명적 결함**을 유발합니다:
          </p>

          <div style="background:#0f172a; border-left:4px solid #ef4444; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#f87171; font-size:1rem; font-weight:800; margin-bottom:8px;">■ 킹크 효과(Kink Effect)의 메커니즘</h4>
            <ol style="color:#cbd5e1; font-size:0.9rem; line-height:1.8; padding-left:18px;">
              <li>드레인 전압($V_{DS}$)을 서서히 높이면 특정 임계 전압에서 갑자기 충격 이온화가 촉발됩니다.</li>
              <li>정공이 바디에 쌓이며 $V_B$가 급상승하고, 방금 배운 로직에 의해 $V_{th}$가 뚝 떨어집니다.</li>
              <li>게이트 전압은 그대로인데 $V_{th}$가 떨어졌으니 실효 게이트 전압($V_{GS} - V_{th}$)이 커져 **드레인 전류($I_D$)가 계단식으로 팍 꺾여 치솟는 킹크(Kink, 굴곡) 현상**이 발생합니다.</li>
              <li>만약 바디 전위가 $0.6\sim 0.7\,\text{V}$까지 오르면, 소스($N^+$)-바디($P$)-드레인($N^+$)으로 이어지는 **기생 NPN BJT가 완전히 켜져(Latch-up 직전)** 제어가 불가능한 폭주 전류가 흐릅니다.</li>
              <li>또한 정공이 쌓이고 빠져나가는 속도 차이 때문에 이전 동작 상태에 따라 소자 특성이 바뀌는 **이력 현상(History Effect / Hysteresis)**이 발생해 회로 타이밍 설계를 마비시킵니다.</li>
            </ol>
          </div>
        </div>

        <!-- Section 4: Evolution to FD-SOI -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#10b981; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. 결론 및 궁극의 솔루션: 왜 FD-SOI로 진화했는가?
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            엔지니어들은 이 정공 축적 문제를 해결하기 위해 처음에는 바디 옆구리에 구멍을 뚫어 전극을 연결하는 **Body Contact(바디 접촉)** 기술을 썼으나, 면적이 20~30% 늘어나고 레이아웃이 복잡해지는 한계에 부딪혔습니다.
          </p>
          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0;">
            <h4 style="color:#34d399; font-size:1.05rem; font-weight:800; margin-bottom:8px;">🚀 궁극의 해법: FD-SOI (완전공핍형 SOI)</h4>
            <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:18px;">
              <li><strong>중성 바디의 원천 박멸</strong>: 실리콘 박막 두께를 $5\sim 7\,\text{nm}$ 수준으로 극도로 얇게 깎아버려, 바디 전체가 100% 게이트 공핍층이 되도록 만들었습니다 ($T_{si} < W_{dep}$).</li>
              <li><strong>정공이 갇힐 방이 없음</strong>: 정공이 축적될 중성 영역 자체가 아예 존재하지 않으므로, 충격 이온화가 발생하더라도 정공이 갇히지 못하고 즉시 소스로 쓸려나가 재결합 소멸합니다.</li>
              <li><strong>플로팅 바디 효과 & 킹크 완전 박멸</strong>: 바디 전위 상승($V_B \uparrow$)과 그로 인한 $V_{th}$ 롤링, 이력 현상이 100% 원천 박멸되었습니다.</li>
              <li><strong>이상적 특성 확보</strong>: 공핍 커패시턴스가 0에 수렴($C_{dep} \approx 0$)하여 $SS \approx 60\,\text{mV/dec}$의 이론적 한계에 도달하고, 기판 후면(Back-gate) 전압을 이용해 $V_{th}$를 자유자재로 컨트롤하는 현대 FD-SOI의 전성기를 열게 되었습니다.</li>
            </ul>
          </div>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 86 topics (q-86 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(86, 0, -1):
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

    # Step 4: Update header description to 87 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 'PD-SOI 채널 아래 쌓인 정공이 Vt 낮추는 로직'이 위치하며, 총 87개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 PD-SOI Hole Vt Lowering topic!")
