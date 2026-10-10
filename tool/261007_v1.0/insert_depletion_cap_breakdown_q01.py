# -*- coding: utf-8 -*-
"""
insert_depletion_cap_breakdown_q01.py
사용자 질문: "depletion capacitance는 어떻게구성이되는지알려줘 s/d와 바디가만나서생기는 접합커페시턴스, 그리고 또뭐가있어?"
대시보드 최상단 Q01로 신규 추가하고, 기존 82개 질문을 Q02~Q83으로 시프트 (총 83개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 커패시턴스 총론 · 공핍층 해부)",
    "title": "MOSFET에서 Depletion Capacitance(공핍 커패시턴스)는 어떻게 구성될까? (S/D 접합 Cap 외에 또 무엇이 있을까?)",
    "nav_title": "공핍 커패시턴스의 구성 (S/D 접합Cap 외에 채널, 측벽, 폴리 공핍)",
    "summary": [
        "<strong>1. 공핍 커패시턴스의 3대 핵심 구성</strong>: MOSFET 내부에서 공간 전하 공핍층(Depletion Region)에 의해 생기는 정전용량은 질문자님이 언급하신 <strong>① 소스/드레인 접합 공핍 커패시턴스($C_j$)</strong> 외에도, <strong>② 게이트 직하부 채널 표면 공핍 커패시턴스($C_{dep,ch}$)</strong>, 그리고 <strong>③ 폴리실리콘 게이트 내부 공핍 커패시턴스($C_{poly}$)</strong> 등으로 정밀하게 구성됩니다.",
        "<strong>2. 게이트 직하부 채널 공핍 커패시턴스 ($C_{dep,ch}$)</strong>: 게이트 산화막 바로 아래 실리콘 표면에 형성되는 수직 공핍층 용량입니다. 게이트 산화막($C_{ox}$)과 <strong>직렬(Series)</strong>로 연결되어 게이트 전압 분배 손실을 일으키며, <strong>문턱전압($V_{th}$)과 서브스레시홀드 스윙($SS = 60(1 + C_{dep,ch}/C_{ox})$)을 결정하는 핵심 인자</strong>입니다.",
        "<strong>3. S/D 접합 커패시턴스($C_j$)의 세부 해부</strong>: 단순히 하나가 아니라 <strong>바닥면 접합($C_{j,bottom}$)</strong>과 <strong>측벽면 접합($C_{j,sw}$)</strong>으로 나뉩니다. 특히 채널 쪽 측벽은 Halo 고농도 도핑과 맞닿아 $W_{dep}$가 얇고 용량이 크며, 회로의 <strong>RC 지연 시간(충방전 속도)과 동적 소비전력($fCV^2$)을 결정</strong>합니다.",
        "<strong>4. 폴리 게이트 공핍층 ($C_{poly}$) 및 에지 공핍</strong>: 금속 게이트(HKMG) 이전의 폴리실리콘 게이트에서는 전극 내부 계면에도 캐리어가 고갈되어 $C_{poly}$가 생겨 유효 산화막 두께(EOT)를 $0.3\\sim0.5\\text{nm}$ 손해 보았습니다. 현대 반도체는 HKMG, SOI, FinFET/GAA를 통해 이 모든 공핍 용량들을 극한으로 제거해 왔습니다."
    ],
    "svg_title": "📊 [MOSFET 공핍 커패시턴스 총괄 해부도] (A) 소자 단면 내 공핍층 위치 지도 | (B) 회로 등가 모델과 역할 구분 | (C) 차세대 소자의 공핍Cap 제거 기술",
    "svg": """<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Anatomical Cross Section of all Depletion Capacitances -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 소자 단면 내 공핍층(Depletion) 지도</text>

    <!-- Transistor Cross Section -->
    <g transform="translate(15, 42)">
      <rect width="270" height="260" rx="6" fill="#1e293b" stroke="#334155"/>

      <!-- Poly Gate Electrode -->
      <rect x="85" y="20" width="100" height="35" fill="#475569" rx="2"/>
      <text x="110" y="36" fill="#fff" font-size="8">Poly / Metal Gate</text>
      <!-- C_poly Layer (inside gate bottom) -->
      <rect x="85" y="45" width="100" height="8" fill="#ec4899" opacity="0.8"/>
      <text x="96" y="52" fill="#fff" font-size="6.5" font-weight="800">③ C_poly (게이트 공핍층)</text>

      <!-- Gate Oxide -->
      <rect x="85" y="55" width="100" height="6" fill="#a855f7"/>
      <text x="112" y="60" fill="#fff" font-size="5.5">Gate Oxide (Cox)</text>

      <!-- Silicon Surface Depletion Layer (C_dep,ch) -->
      <rect x="85" y="61" width="100" height="20" fill="#38bdf8" opacity="0.6"/>
      <text x="92" y="74" fill="#000" font-size="7.5" font-weight="900">① 채널 공핍층 (C_dep,ch)</text>

      <!-- Source / Drain Regions -->
      <rect x="20" y="61" width="60" height="45" fill="#f59e0b" rx="2"/>
      <text x="32" y="85" fill="#000" font-size="8" font-weight="800">Source (N+)</text>

      <rect x="190" y="61" width="60" height="45" fill="#f59e0b" rx="2"/>
      <text x="204" y="85" fill="#000" font-size="8" font-weight="800">Drain (N+)</text>

      <!-- S/D Sidewall Depletion (C_j,sw) -->
      <rect x="80" y="61" width="5" height="45" fill="#ef4444" opacity="0.8"/>
      <rect x="185" y="61" width="5" height="45" fill="#ef4444" opacity="0.8"/>
      <text x="40" y="118" fill="#ef4444" font-size="7" font-weight="800">②-B 측벽 공핍층 (C_j,sw)</text>

      <!-- S/D Bottom Depletion (C_j,bot) -->
      <rect x="20" y="106" width="65" height="15" fill="#ef4444" opacity="0.6"/>
      <rect x="185" y="106" width="65" height="15" fill="#ef4444" opacity="0.6"/>
      <text x="40" y="132" fill="#f87171" font-size="7" font-weight="800">②-A 바닥 접합 공핍층 (C_j,bot)</text>

      <!-- P-Substrate (Body) -->
      <rect x="20" y="142" width="230" height="105" fill="#047857" opacity="0.2"/>
      <text x="100" y="180" fill="#34d399" font-size="8.5" font-weight="700">P-Well / P-Substrate (Body)</text>

      <!-- Callout markers -->
      <line x1="135" y1="81" x2="135" y2="105" stroke="#38bdf8" stroke-width="1.5"/>
      <text x="95" y="116" fill="#38bdf8" font-size="7.5">W_dep,ch (채널 공핍 폭)</text>
    </g>

    <!-- Legend Summary Box -->
    <rect x="15" y="312" width="270" height="96" rx="6" fill="#0b1329" stroke="#334155"/>
    <text x="22" y="330" fill="#38bdf8" font-size="8.8" font-weight="800">공핍 커패시턴스 3대 영역 요약:</text>
    <text x="22" y="348" fill="#38bdf8" font-size="8">• ① 채널 공핍 Cap: 게이트 직하부 표면 (SS 지배)</text>
    <text x="22" y="365" fill="#f87171" font-size="8">• ② S/D 접합 Cap: 바닥(C_j,bot) + 측벽(C_j,sw)</text>
    <text x="22" y="382" fill="#ec4899" font-size="8">• ③ 폴리 게이트 Cap: 게이트 전극 내부 계면</text>
    <text x="22" y="399" fill="#fde047" font-size="8">• ④ 2D 프린징/오버랩: S/D 에지와 게이트 사이</text>
  </g>

  <!-- PANEL B: Circuit Roles & Physical Formula Comparison -->
  <g transform="translate(340, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 회로적 역할: 직렬 분배 vs 병렬 부하</text>

    <!-- Series vs Parallel Circuit Diagram -->
    <g transform="translate(15, 42)">
      <rect width="280" height="175" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="9" font-weight="800">1. 회로 연결 방식의 결정적 차이</text>

      <!-- Left: Gate series divider -->
      <g transform="translate(10, 30)">
        <text x="10" y="14" fill="#38bdf8" font-size="8" font-weight="800">[게이트 직렬 분배망]</text>
        <circle cx="50" cy="24" r="3" fill="#fff"/>
        <text x="58" y="27" fill="#fff" font-size="7">Gate (VG)</text>
        <line x1="50" y1="27" x2="50" y2="35" stroke="#94a3b8"/>
        <rect x="35" y="35" width="30" height="10" fill="#a855f7"/>
        <text x="40" y="43" fill="#fff" font-size="6.5">Cox</text>
        <line x1="50" y1="45" x2="50" y2="55" stroke="#94a3b8"/>
        <circle cx="50" cy="55" r="3" fill="#10b981"/>
        <text x="58" y="58" fill="#10b981" font-size="7">ψs</text>
        <line x1="50" y1="58" x2="50" y2="68" stroke="#94a3b8"/>
        <rect x="35" y="68" width="30" height="10" fill="#38bdf8"/>
        <text x="36" y="76" fill="#000" font-size="6">C_dep,ch</text>
        <line x1="50" y1="78" x2="50" y2="88" stroke="#94a3b8"/>
        <line x1="40" y1="88" x2="60" y2="88" stroke="#fff" stroke-width="1.5"/>
        <text x="65" y="91" fill="#94a3b8" font-size="7">Body</text>
        <text x="5" y="108" fill="#bae6fd" font-size="7">• Cox와 C_dep,ch 직렬 연결</text>
        <text x="5" y="120" fill="#38bdf8" font-size="7.5" font-weight="700">➔ 전압 분배 손실 유발 (SS 악화)</text>
      </g>

      <!-- Right: S/D parallel load -->
      <g transform="translate(150, 30)">
        <text x="10" y="14" fill="#f87171" font-size="8" font-weight="800">[S/D 병렬 기생 부하]</text>
        <circle cx="50" cy="24" r="3" fill="#f59e0b"/>
        <text x="58" y="27" fill="#f59e0b" font-size="7">Drain (VD)</text>
        <line x1="50" y1="27" x2="50" y2="48" stroke="#94a3b8"/>
        <rect x="35" y="48" width="30" height="16" fill="#ef4444"/>
        <text x="40" y="59" fill="#fff" font-size="6.5" font-weight="800">C_j (접합)</text>
        <line x1="50" y1="64" x2="50" y2="88" stroke="#94a3b8"/>
        <line x1="40" y1="88" x2="60" y2="88" stroke="#fff" stroke-width="1.5"/>
        <text x="65" y="91" fill="#94a3b8" font-size="7">Body (GND)</text>
        <text x="5" y="108" fill="#fca5a5" font-size="7">• 드레인 단자에 직접 병렬 접지</text>
        <text x="5" y="120" fill="#f87171" font-size="7.5" font-weight="700">➔ RC 신호 지연 &amp; 동적 전력 낭비</text>
      </g>
    </g>

    <!-- Formula & Impact Detail Box -->
    <g transform="translate(15, 228)">
      <rect width="280" height="178" rx="6" fill="#0b1329" stroke="#334155"/>
      <text x="12" y="18" fill="#34d399" font-size="9" font-weight="800">2. 두 공핍 커패시턴스의 수식과 특성 비교</text>

      <text x="12" y="38" fill="#38bdf8" font-size="8.5" font-weight="700">■ 채널 공핍 용량 (C_dep,ch):</text>
      <text x="20" y="52" fill="#cbd5e1" font-size="7.8">C_dep,ch = ε_si / W_dep,ch = √ [ (q ε_si NA) / (2ψs) ]</text>
      <text x="20" y="65" fill="#cbd5e1" font-size="7.8">➔ SS = 60 · (1 + C_dep,ch / Cox) 결정 인자!</text>

      <text x="12" y="86" fill="#f87171" font-size="8.5" font-weight="700">■ S/D 접합 공핍 용량 (C_j):</text>
      <text x="20" y="100" fill="#cbd5e1" font-size="7.8">C_j = C_j0 / [ 1 + (V_R / V_bi) ]^m (역방향 전압 함수)</text>
      <text x="20" y="113" fill="#cbd5e1" font-size="7.8">➔ 바닥면(C_j,bot) + 측벽면(C_j,sw)의 합</text>
      <text x="20" y="126" fill="#cbd5e1" font-size="7.8">➔ τ = R_on · (C_gate + C_inter + C_j) 딜레이 주범!</text>

      <text x="12" y="148" fill="#fde047" font-size="8">• C_dep,ch는 '스위칭 예리함(누설)'을 제어하고,</text>
      <text x="12" y="162" fill="#fde047" font-size="8">• C_j는 '스위칭 동작 속도(RC)'를 제어합니다!</text>
    </g>
  </g>

  <!-- PANEL C: Technological Elimination Roadmap -->
  <g transform="translate(670, 20)">
    <rect width="290" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) 반도체 업계의 공핍Cap 박멸 로드맵</text>

    <!-- Elimination 1: C_j elimination via SOI -->
    <g transform="translate(15, 42)">
      <rect width="260" height="110" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="12" y="18" fill="#fde047" font-size="9" font-weight="800">1. S/D 접합 Cap(C_j)의 박멸 ➔ SOI</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="8">• 벌크: S/D 바닥 P-N 접합으로 C_j 거대</text>
      <text x="12" y="52" fill="#38bdf8" font-size="8.2" font-weight="700">★ SOI (Silicon-On-Insulator) 기술 도입:</text>
      <text x="20" y="66" fill="#cbd5e1" font-size="7.5">S/D 밑바닥에 두꺼운 SiO₂ BOX 산화막 배치</text>
      <text x="20" y="80" fill="#a7f3d0" font-size="7.5">➔ P-N 접합면 자체를 물리적으로 소멸!</text>
      <text x="20" y="94" fill="#34d399" font-size="8" font-weight="800">➔ C_j 90% 제거로 회로 속도 20~30% 폭등</text>
    </g>

    <!-- Elimination 2: C_dep,ch elimination via FinFET / GAA -->
    <g transform="translate(15, 160)">
      <rect width="260" height="115" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="9" font-weight="800">2. 채널 공핍 Cap(C_dep,ch) 극소화 ➔ FinFET/GAA</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="8">• 벌크: SCE 막으려 고도핑 ➔ C_dep,ch 폭증 ➔ SS 악화</text>
      <text x="12" y="52" fill="#38bdf8" font-size="8.2" font-weight="700">★ FD-SOI, FinFET, GAA 나노시트 도입:</text>
      <text x="20" y="66" fill="#cbd5e1" font-size="7.5">바디를 5nm 초박막으로 깎고 3면·4면 게이트 포위</text>
      <text x="20" y="80" fill="#a7f3d0" font-size="7.5">➔ 무도핑 채널 실현 + 바디 완전 공핍화!</text>
      <text x="20" y="96" fill="#34d399" font-size="8" font-weight="800">➔ C_dep,ch ≈ 0 수렴! SS ≈ 60 mV/dec 복원</text>
    </g>

    <!-- Elimination 3: C_poly elimination via HKMG -->
    <g transform="translate(15, 285)">
      <rect width="260" height="120" rx="6" fill="#0b1329" stroke="#ec4899"/>
      <text x="12" y="18" fill="#f472b6" font-size="9" font-weight="800">3. 폴리 공핍 Cap(C_poly) 박멸 ➔ HKMG</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="8">• 폴리실리콘 게이트: 계면 공핍층 C_poly 발생</text>
      <text x="20" y="50" fill="#fca5a5" font-size="7.5">➔ 유효 EOT 0.4nm 손해, 구동 전류 저하</text>
      <text x="12" y="66" fill="#fde047" font-size="8.2" font-weight="700">★ HKMG (High-k Metal Gate) 도입:</text>
      <text x="20" y="80" fill="#cbd5e1" font-size="7.5">게이트를 반도체가 아닌 순수 금속(Metal)으로 대체</text>
      <text x="20" y="94" fill="#a7f3d0" font-size="7.5">➔ 자유전자가 무한대이므로 C_poly = ∞ (공핍층 0nm!)</text>
      <text x="20" y="108" fill="#34d399" font-size="8" font-weight="800">➔ 게이트 공핍 효과 100% 완전 박멸!</text>
    </g>
  </g>
</svg>""",
    "lecture": r"""
        <!-- Section 1: Overview of Depletion Capacitance Family -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. MOSFET의 공핍 커패시턴스(Depletion Capacitance) 전체 지도
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체 소자에서 <strong>공핍 커패시턴스(Depletion Capacitance)</strong>란, 자유 캐리어(전자, 정공)가 밀려나고 고정된 이온화 불순물(도펀트) 공간 전하만 남은 <strong>공핍 영역(Depletion Region)이 유전체(절연체) 역할을 하여 형성되는 모든 정전용량</strong>을 의미합니다.<br>
            질문자님께서 정확히 짚어주신 <strong>'소스/드레인과 바디가 만나서 생기는 접합 커패시턴스($C_j$)'</strong> 외에도, MOSFET 내부에는 다음과 같은 핵심 공핍 커패시턴스들이 얽혀 있습니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:18px;">
            <h4 style="color:#38bdf8; font-size:1.05rem; font-weight:800; margin-bottom:8px;">💡 MOSFET 4대 공핍 커패시턴스 총괄 요약</h4>
            <ol style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:18px;">
              <li><strong>① 게이트 직하부 채널 표면 공핍 커패시턴스 ($C_{dep,ch}$)</strong> : 게이트 산화막 아래 채널 표면에 수직으로 형성되는 공핍층 (문턱전압 $V_{th}$ 및 $SS$ 결정).</li>
              <li><strong>② 소스/드레인-바디 접합 공핍 커패시턴스 ($C_j$)</strong> : $N^+$ S/D와 P-기판 사이 P-N 접합 다이오드 공핍층 (바닥면 $C_{j,bot}$과 측벽면 $C_{j,sw}$로 구성, RC 딜레이 지배).</li>
              <li><strong>③ 폴리실리콘 게이트 내부 공핍 커패시턴스 ($C_{poly}$)</strong> : 폴리실리콘 게이트 전극 내부 계면에서 캐리어가 고갈되어 생기는 공핍층 (EOT 손실의 원인).</li>
              <li><strong>④ 게이트-S/D 오버랩 및 에지 프린징 공핍 커패시턴스 ($C_{ov,dep}$)</strong> : 게이트 끝단과 S/D 확산층이 겹치는 경계면의 2차원 프린징 공핍층.</li>
            </ol>
          </div>
        </div>

        <!-- Section 2: Detailed Breakdown of C_dep,ch -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 게이트 직하부 채널 공핍 커패시턴스 ($C_{dep,ch}$): 스위칭을 지배하는 인자
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체 물리 교재에서 아무런 접두사 없이 그냥 기호로 **$C_{dep}$**라고 쓸 때 십중팔구 지칭하는 대상이 바로 이 **채널 표면 공핍 커패시턴스**입니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#fde047; margin:14px 0 8px;">■ 형성 원리와 물리 수식</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:10px;">
            게이트에 양(+)의 전압을 걸면, P형 기판의 다수 캐리어인 정공들이 바닥으로 쫓겨나면서 게이트 산화막 바로 아래 실리콘 표면에 음이온($B^-$) 공간 전하층인 **수직 공핍층($W_{dep,ch}$)**이 형성됩니다:
            $$C_{dep,ch} = \frac{\epsilon_{si}}{W_{dep,ch}} = \sqrt{\frac{q \epsilon_{si} N_A}{2\psi_s}}$$
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#38bdf8; margin:14px 0 8px;">■ 소자에 미치는 결정적 영향: 직렬 전압 분배기</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            이 $C_{dep,ch}$는 게이트 산화막 커패시턴스($C_{ox}$)와 **직렬(Series)**로 연결됩니다. 게이트 전압이 채널 표면 전위($\psi_s$)를 끌어올릴 때 전압을 갉아먹는 분배기 손실을 일으킵니다:
            $$\frac{\partial \psi_s}{\partial V_G} = \frac{C_{ox}}{C_{ox} + C_{dep,ch}} = \frac{1}{1 + \frac{C_{dep,ch}}{C_{ox}}}$$
            따라서 트랜지스터를 끌 때 스위치가 얼마나 날카롭게 꺼지는가를 결정하는 **서브스레시홀드 스윙 공식($SS = 60(1 + C_{dep,ch}/C_{ox})\,\text{mV/dec}$)**의 분자가 바로 이 녀석입니다!
          </p>
        </div>

        <!-- Section 3: Deep Anatomy of Junction Capacitance C_j -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#f87171; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 소스/드레인 접합 커패시턴스 ($C_j$): 바닥면($C_{j,bot}$)과 측벽면($C_{j,sw}$)의 해부
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            질문자님께서 말씀해주신 접합 커패시턴스($C_j$) 역시 실제 반도체 모델링(BSIM 등)에서는 <strong>기하학적 위치에 따라 엄격하게 2가지</strong>로 나누어 계산합니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #ef4444; padding:14px 18px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.8; padding-left:18px;">
              <li><strong>1. 바닥면 접합 커패시턴스 ($C_{j,bottom}$)</strong>:
                <br>• 소스/드레인의 밑바닥 수평 평면($A = W \times L_{S/D}$)과 P-기판이 만나는 영역.
                <br>• $C_{j,bot} = \frac{\epsilon_{si} A}{W_{dep,bot}}$ (벌크에서는 면적이 넓어 전체 용량의 대다수 차지).
              </li>
              <li><strong>2. 측벽면 접합 커패시턴스 ($C_{j,sw}$, Sidewall)</strong>:
                <br>• 소스/드레인의 수직 테두리(STI 소자 분리막 측벽 및 게이트 채널 측벽)와 기판이 만나는 둘레($P_{perimeter}$) 영역.
                <br>• $C_{j,sw} = \frac{\epsilon_{si} (P \cdot X_j)}{W_{dep,sw}}$
                <br>• <strong>★ 채널 쪽 측벽의 위험성</strong>: 채널 쪽 측벽은 단채널 억제용 **고농도 Halo 도핑($N_A \uparrow$)**과 맞닿아 있어 공핍층 두께가 극도로 얇고 단위 면적당 커패시턴스가 비정상적으로 높습니다!
              </li>
            </ul>
          </div>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1;">
            이 $C_j$는 드레인 단자에 <strong>병렬(Parallel)</strong>로 접지되어, 회로가 신호를 주고받을 때마다 전하를 충방전해야 하는 기생 부하로 작용하여 **칩 동작 속도(RC 딜레이 $\tau = R_{on} C_j$)를 갉아먹는 주범**입니다.
          </p>
        </div>

        <!-- Section 4: Poly Depletion and Technological Solutions -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. 숨겨진 복병: 폴리 게이트 공핍층 ($C_{poly}$)과 반도체 기술의 박멸 역사
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            마지막으로 과거 반도체를 괴롭혔던 또 하나의 대표적인 공핍 커패시턴스는 **폴리실리콘 게이트 내부의 공핍층($C_{poly}$)**입니다.
          </p>
          <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:20px; margin-bottom:14px;">
            <li><strong>게이트 공핍 효과 (Gate Depletion Effect)</strong>: 폴리실리콘은 금속이 아니라 고농도 도핑된 반도체입니다. 게이트에 강한 전압을 걸면 게이트 산화막과 맞닿은 폴리실리콘 전극 내부 계면에서도 다수 캐리어가 고갈되어 **$0.3 \sim 0.5\,\text{nm}$ 두께의 공핍층($W_{poly}$)**이 생겨납니다.</li>
            <li>이 $C_{poly}$가 게이트 산화막($C_{ox}$)과 직렬로 더해져 유효 산화막 두께($EOT$)를 늘려버리고 구동 전류를 20% 이상 떨어뜨렸습니다.</li>
          </ul>

          <div style="background:#090d1a; border:1px solid #10b981; border-radius:10px; padding:16px; margin-top:16px;">
            <h4 style="color:#34d399; font-size:0.95rem; font-weight:800; margin-bottom:8px;">🚀 인류가 이 공핍 커패시턴스들을 없애온 역사 (종합 솔루션)</h4>
            <ol style="color:#cbd5e1; font-size:0.88rem; line-height:1.75; padding-left:18px; margin-bottom:0;">
              <li><strong>S/D 바닥 $C_j$ 제거</strong> ➔ <strong>SOI 기술</strong> (S/D 밑에 SiO₂ BOX 산화막을 깔아 P-N 접합면 자체를 물리적으로 소멸).</li>
              <li><strong>채널 $C_{dep,ch}$ 극소화</strong> ➔ <strong>FD-SOI, FinFET, GAA</strong> (채널을 5nm로 깎고 3면·4면 전면 게이트 포위로 무도핑 채널 실현 ➔ $C_{dep,ch} \approx 0$, $SS \approx 60\,\text{mV/dec}$ 복원).</li>
              <li><strong>게이트 $C_{poly}$ 제거</strong> ➔ <strong>HKMG (High-k Metal Gate)</strong> (게이트를 반도체가 아닌 순수 금속으로 대체하여 자유전자를 무한대로 확보 ➔ $C_{poly} = \infty$, 공핍층 0nm 완벽 박멸).</li>
            </ol>
          </div>
        </div>

        <!-- Section 5: Summary Comparison Table -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.15rem; font-weight:800; color:#e2e8f0; margin-bottom:12px;">
            5. MOSFET 3대 공핍 커패시턴스 비교 정리표
          </h3>
          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">공핍 커패시턴스 종류</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">물리적 형성 위치</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">회로적 결합 방식</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">소자에 미치는 영향 &amp; 해결 기술</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">① 채널 표면 공핍 Cap ($C_{dep,ch}$)</td>
                  <td style="padding:10px 14px;">게이트 산화막 직하부 실리콘 채널</td>
                  <td style="padding:10px 14px; color:#fde047; font-weight:700;">$C_{ox}$와 직렬 연결</td>
                  <td style="padding:10px 14px;">$V_{th}$ 및 $SS$ 결정 (전압 손실 유발) ➔ <strong>FD-SOI / FinFET 무도핑 채널로 극소화</strong></td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#f87171;">② S/D 접합 공핍 Cap ($C_j$)</td>
                  <td style="padding:10px 14px;">소스/드레인과 바디 기판 사이 (바닥+측벽)</td>
                  <td style="padding:10px 14px; color:#f87171; font-weight:700;">드레인 단자에 병렬 접지</td>
                  <td style="padding:10px 14px;">RC 지연 시간(충방전 속도 저하) &amp; 전력 낭비 ➔ <strong>SOI BOX 산화막으로 90% 제거</strong></td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#ec4899;">③ 폴리 게이트 공핍 Cap ($C_{poly}$)</td>
                  <td style="padding:10px 14px;">폴리실리콘 게이트 전극 내부 계면</td>
                  <td style="padding:10px 14px; color:#fde047; font-weight:700;">$C_{ox}$와 직렬 연결</td>
                  <td style="padding:10px 14px;">유효 EOT 두께 증가 &amp; 전류 구동력 저하 ➔ <strong>HKMG 금속 게이트로 100% 박멸</strong></td>
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

    # Step 1: Shift existing 82 topics (q-82 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(82, 0, -1):
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

    # Step 4: Update header description to 83 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 '공핍 커패시턴스의 구성 (S/D 접합Cap 외에 채널, 측벽, 폴리 공핍)'이 위치하며, 총 83개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Depletion Capacitance Breakdown topic!")
