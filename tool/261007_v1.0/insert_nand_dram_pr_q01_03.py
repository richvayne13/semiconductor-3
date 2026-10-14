# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# We will define the 3 topics: Q01, Q02, Q03
TOPIC_Q01 = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (비휘발성 메모리 & 소자 물리 · F-N 터널링과 전하 저장 메커니즘 완전 해부)",
    "title": "NAND 플래시 메모리의 기본 동작 원리: 플로팅 게이트(FG) vs 전하 트랩(CTF), 프로그램·소거·읽기 메커니즘 및 3D V-NAND 적층 구조 총정리",
    "nav_title": "NAND 플래시 메모리의 기본 동작 원리",
    "summary": [
        "<strong>1. 셀 구조의 본질 (1-Transistor 전하 저장 소자)</strong>: MOSFET 게이트 절연막 사이에 전하를 영구히 가두는 저장소(Floating Gate 또는 CTF 질화막 트랩)를 삽입한 비휘발성(Non-volatile) 메모리입니다. 전원이 꺼져도 갇힌 전자가 유지되어 데이터를 보존합니다.",
        "<strong>2. 프로그램(Write/Program) 메커니즘: F-N 터널링</strong>: 컨트롤 게이트(CG)에 높은 양전압($V_{pgm} \\approx 18 \\sim 20\\,\\text{V}$)을 인가하여 터널 산화막($\\text{SiO}_2$)에 $10\\,\\text{MV/cm}$ 이상의 초고전계를 형성합니다. 이로 인해 기판 채널의 전자가 에너지 장벽을 직접 뚫고 지나가는 <strong>파울러-노드하임(Fowler-Nordheim) 터널링</strong>으로 전하저장층에 주입되며, 셀의 문턱전압($V_{th}$)이 오른쪽으로 증가하여 데이터 '0'이 기록됩니다.",
        "<strong>3. 소거(Erase) 메커니즘: 벌크 일괄 방출</strong>: 기판(P-well)에 고전압($\\approx 20\\,\\text{V}$)을 인가하고 CG를 $0\\,\\text{V}$로 두어 역방향 F-N 터널링으로 전자를 기판으로 배출합니다. 문턱전압($V_{th}$)이 음의 전압으로 낮아져 데이터 '1'(소거 상태)이 되며, 셀 구조상 블록(Block) 단위로 일괄 소거됩니다.",
        "<strong>4. 읽기(Read) 메커니즘: 전류 도통 여부 판별</strong>: 선택된 워드라인에 프로그램 상태와 소거 상태의 $V_{th}$ 사이 전압($V_{read}$)을 인가합니다. 소거 셀('1')은 켜져 비트라인(BL)에 전류가 흐르고(On-cell), 프로그램 셀('0')은 꺼져 전류가 차단(Off-cell)되는 차이를 감지합니다.",
        "<strong>5. FG에서 CTF 및 3D V-NAND로의 진화</strong>: 2D 미세화 한계로 도체 FG 간의 기생 커패시턴스 간섭(Cross-talk) 및 터널 산화막 누설(SILC)이 발생하자, 절연체 질화막($\\text{Si}_3\\text{N}_4$)에 전하를 국소 포획하는 <strong>CTF(Charge Trap Flash)</strong>와 수직 원통형 채널로 적층하는 <strong>3D V-NAND</strong>로 패러다임이 전환되었습니다."
    ],
    "svg_title": "📊 [NAND 플래시 메모리 동작 원리 종합 아키텍처 다이어그램] (A) 플로팅게이트(FG) vs CTF 셀 구조 및 에너지 밴드 F-N 터널링 | (B) Program / Erase / Read 3대 동작 모드 및 Vth 천이 분포 | (C) 3D V-NAND GAA 원통형 채널 및 워드라인 슬릿 구조",
    "svg": r'''<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: FG vs CTF Structure & Band Diagram -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 셀 구조: FG vs CTF &amp; F-N 터널링</text>

    <!-- FG Cell Cross section -->
    <g transform="translate(15, 42)">
      <rect width="125" height="180" rx="6" fill="#1e293b" stroke="#475569"/>
      <text x="15" y="18" fill="#fde047" font-size="9" font-weight="800">1) 2D 플로팅 게이트(FG)</text>
      <!-- Control Gate -->
      <rect x="15" y="28" width="95" height="18" rx="2" fill="#3b82f6"/>
      <text x="24" y="41" fill="#ffffff" font-size="7.5" font-weight="700">Control Gate (Poly/W)</text>
      <!-- IPD (Blocking Oxide) -->
      <rect x="15" y="48" width="95" height="12" fill="#64748b"/>
      <text x="32" y="57" fill="#f1f5f9" font-size="6.5">IPD (ONO 유전막)</text>
      <!-- Floating Gate -->
      <rect x="15" y="62" width="95" height="24" rx="2" fill="#f59e0b" stroke="#d97706"/>
      <text x="20" y="77" fill="#0f172a" font-size="7.5" font-weight="800">Floating Gate (도체 Poly)</text>
      <!-- Tunnel Oxide -->
      <rect x="15" y="88" width="95" height="10" fill="#94a3b8"/>
      <text x="24" y="96" fill="#0f172a" font-size="6">Tunnel Oxide (SiO2)</text>
      <!-- Substrate -->
      <rect x="15" y="100" width="95" height="65" rx="3" fill="#334155"/>
      <rect x="15" y="100" width="22" height="20" fill="#059669"/>
      <text x="18" y="114" fill="#ffffff" font-size="6.5" font-weight="700">Source</text>
      <rect x="88" y="100" width="22" height="20" fill="#059669"/>
      <text x="92" y="114" fill="#ffffff" font-size="6.5" font-weight="700">Drain</text>
      <text x="40" y="130" fill="#cbd5e1" font-size="7">P-Substrate</text>
      <text x="18" y="155" fill="#f87171" font-size="6.5">⚠️ 간섭(Cross-talk) &amp; 누설</text>
    </g>

    <!-- CTF Cell Cross section -->
    <g transform="translate(155, 42)">
      <rect width="130" height="180" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="9" font-weight="800">2) 3D CTF (Charge Trap)</text>
      <!-- Control Gate -->
      <rect x="15" y="28" width="100" height="18" rx="2" fill="#3b82f6"/>
      <text x="26" y="41" fill="#ffffff" font-size="7.5" font-weight="700">Metal Gate (W/TiN)</text>
      <!-- Blocking Oxide (High-k) -->
      <rect x="15" y="48" width="100" height="12" fill="#0284c7"/>
      <text x="24" y="57" fill="#f1f5f9" font-size="6.5">Blocking (Al2O3/SiO2)</text>
      <!-- Trapping Layer (Si3N4) -->
      <rect x="15" y="62" width="100" height="24" rx="2" fill="#8b5cf6" stroke="#6d28d9"/>
      <text x="18" y="77" fill="#ffffff" font-size="7.2" font-weight="800">Trap Layer (절연체 SiN)</text>
      <!-- Tunnel Oxide -->
      <rect x="15" y="88" width="100" height="10" fill="#94a3b8"/>
      <text x="26" y="96" fill="#0f172a" font-size="6">Tunnel Oxide (SiO2)</text>
      <!-- Substrate/Channel -->
      <rect x="15" y="100" width="100" height="65" rx="3" fill="#334155"/>
      <text x="25" y="125" fill="#a7f3d0" font-size="7" font-weight="700">Macaroni Polysilicon</text>
      <text x="20" y="140" fill="#34d399" font-size="6.8">전하가 국소 Trap에 포박!</text>
      <text x="18" y="155" fill="#38bdf8" font-size="6.5">✅ 결함 발생해도 누설 방지</text>
    </g>

    <!-- F-N Tunneling Energy Band -->
    <g transform="translate(15, 235)">
      <rect width="270" height="170" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.5" font-weight="800">3) F-N 터널링 (수직 초고전계 &gt; 10MV/cm)</text>
      <!-- Conduction Band Diagram -->
      <path d="M 25 110 L 70 110 L 70 45 L 140 135 L 140 85 L 250 85" fill="none" stroke="#38bdf8" stroke-width="2"/>
      <text x="30" y="135" fill="#cbd5e1" font-size="7">Substrate</text>
      <text x="85" y="70" fill="#fca5a5" font-size="7">삼각 전위 장벽</text>
      <!-- Electron Tunneling Path -->
      <circle cx="50" cy="105" r="4" fill="#ef4444"/>
      <path d="M 55 105 Q 85 105 155 105" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3" marker-end="url(#arrowRed)"/>
      <text x="160" y="75" fill="#fde047" font-size="7.5" font-weight="700">Trap/FG 축적</text>
      <text x="60" y="155" fill="#a7f3d0" font-size="7">F-N Tunneling: $J_{FN} \propto E_{ox}^2 \exp(-B/E_{ox})$</text>
    </g>
  </g>

  <!-- PANEL B: Program, Erase, Read & Vth Shift -->
  <g transform="translate(340, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#10b981" font-size="12" font-weight="800">■ (B) 3대 동작: Program / Erase / Read</text>

    <!-- Operation Modes Table/Graphic -->
    <g transform="translate(15, 42)">
      <rect width="270" height="195" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 바이어스 조건 및 전하 거동</text>

      <!-- Program Mode -->
      <rect x="10" y="28" width="250" height="48" rx="4" fill="#0f172a" stroke="#3b82f6"/>
      <text x="18" y="44" fill="#60a5fa" font-size="7.5" font-weight="800">① 프로그램 (Program / Write '0')</text>
      <text x="18" y="58" fill="#cbd5e1" font-size="6.8">• Gate: +18~20V (Vpgm) | Channel: 0V (GND)</text>
      <text x="18" y="70" fill="#93c5fd" font-size="6.8">• 전자 주입 ➔ 채널 전자 축적 억제 ➔ Vth 상승(우측 이동)</text>

      <!-- Erase Mode -->
      <rect x="10" y="82" width="250" height="48" rx="4" fill="#0f172a" stroke="#ef4444"/>
      <text x="18" y="98" fill="#f87171" font-size="7.5" font-weight="800">② 소거 (Erase / Write '1') - Block 단위</text>
      <text x="18" y="112" fill="#cbd5e1" font-size="6.8">• Gate: 0V | P-Well(Sub): +20V (Verase)</text>
      <text x="18" y="124" fill="#fca5a5" font-size="6.8">• 전자 방출 ➔ 채널 반전 용이 ➔ Vth 하강(좌측 음전압)</text>

      <!-- Read Mode -->
      <rect x="10" y="136" width="250" height="48" rx="4" fill="#0f172a" stroke="#10b981"/>
      <text x="18" y="152" fill="#34d399" font-size="7.5" font-weight="800">③ 읽기 (Read / Sensing)</text>
      <text x="18" y="166" fill="#cbd5e1" font-size="6.8">• 선택 WL: Vread (0~4V) | 비선택 WL: Vpass (6~8V)</text>
      <text x="18" y="178" fill="#a7f3d0" font-size="6.8">• 소거 셀('1'): On(전류 흐름) | 프로그램 셀('0'): Off(차단)</text>
    </g>

    <!-- Vth Distribution Graphic -->
    <g transform="translate(15, 248)">
      <rect width="270" height="157" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">2. 문턱전압(Vth) 이동과 읽기 윈도우 마진</text>

      <!-- Axis -->
      <line x1="25" y1="120" x2="250" y2="120" stroke="#64748b" stroke-width="1.5"/>
      <text x="235" y="132" fill="#cbd5e1" font-size="7">Vth [V]</text>
      <line x1="120" y1="35" x2="120" y2="125" stroke="#475569" stroke-width="1" stroke-dasharray="2,2"/>
      <text x="112" y="132" fill="#fde047" font-size="7">0V</text>

      <!-- Erase Curve ('1') -->
      <path d="M 40 120 Q 75 40 110 120" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="2"/>
      <text x="65" y="75" fill="#34d399" font-size="8" font-weight="800">소거 ('1')</text>
      <text x="50" y="88" fill="#a7f3d0" font-size="6.5">Vth &lt; 0V (On)</text>

      <!-- Program Curve ('0') -->
      <path d="M 160 120 Q 195 40 230 120" fill="rgba(239, 68, 68, 0.25)" stroke="#ef4444" stroke-width="2"/>
      <text x="185" y="75" fill="#f87171" font-size="8" font-weight="800">프로그램 ('0')</text>
      <text x="175" y="88" fill="#fca5a5" font-size="6.5">Vth &gt; 0V (Off)</text>

      <!-- Vread Reference line -->
      <line x1="135" y1="40" x2="135" y2="120" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3,2"/>
      <text x="127" y="35" fill="#fbbf24" font-size="7.5" font-weight="800">Vread</text>
    </g>
  </g>

  <!-- PANEL C: NAND String & 3D V-NAND Structure -->
  <g transform="translate(660, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="12" font-weight="800">■ (C) 3D V-NAND 수직 적층 &amp; NAND 스트링</text>

    <!-- NAND String Schematic -->
    <g transform="translate(15, 42)">
      <rect width="270" height="175" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 직렬 연결 NAND String (비트라인 공유)</text>

      <!-- String Diagram -->
      <line x1="50" y1="35" x2="50" y2="160" stroke="#38bdf8" stroke-width="3"/>
      <text x="65" y="38" fill="#38bdf8" font-size="7.5" font-weight="800">Bit Line (BL)</text>
      <circle cx="50" cy="45" r="5" fill="#0284c7"/>
      <text x="65" y="48" fill="#cbd5e1" font-size="7">SSL (String Select Line)</text>

      <circle cx="50" cy="70" r="5" fill="#8b5cf6"/>
      <text x="65" y="73" fill="#cbd5e1" font-size="7">WL 31 (Vpass 인가)</text>

      <circle cx="50" cy="95" r="6" fill="#ef4444" stroke="#fde047" stroke-width="2"/>
      <text x="65" y="98" fill="#fde047" font-size="7.5" font-weight="800">WL Selected (Vread 인가!)</text>

      <circle cx="50" cy="120" r="5" fill="#8b5cf6"/>
      <text x="65" y="123" fill="#cbd5e1" font-size="7">WL 0 (Vpass 인가)</text>

      <circle cx="50" cy="145" r="5" fill="#0284c7"/>
      <text x="65" y="148" fill="#cbd5e1" font-size="7">GSL (Ground Select Line)</text>
      <text x="65" y="162" fill="#10b981" font-size="7.5" font-weight="800">Common Source Line (CSL)</text>
    </g>

    <!-- 3D V-NAND Macaroni Cylinder Architecture -->
    <g transform="translate(15, 228)">
      <rect width="270" height="177" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">2. 3D V-NAND 수직 홀 (Macaroni 구조)</text>

      <!-- Vertical Cross-section of Macaroni Hole -->
      <g transform="translate(30, 25)">
        <!-- Layers: Wordlines alternating with SiO2 -->
        <rect x="0" y="5" width="210" height="16" fill="#2563eb" rx="2"/>
        <text x="8" y="17" fill="#ffffff" font-size="7">Wordline Layer N (W Gate)</text>
        <rect x="0" y="24" width="210" height="8" fill="#475569"/>
        <rect x="0" y="34" width="210" height="16" fill="#2563eb" rx="2"/>
        <text x="8" y="46" fill="#ffffff" font-size="7">Wordline Layer N-1 (W Gate)</text>
        <rect x="0" y="52" width="210" height="8" fill="#475569"/>
        <rect x="0" y="62" width="210" height="16" fill="#2563eb" rx="2"/>
        <text x="8" y="74" fill="#ffffff" font-size="7">Wordline Layer N-2 (W Gate)</text>

        <!-- Vertical Hole Cutout through the center -->
        <rect x="125" y="0" width="50" height="90" fill="#0b1120" stroke="#fde047" stroke-width="1"/>
        <!-- Blocking Oxide -->
        <line x1="128" y1="0" x2="128" y2="90" stroke="#0284c7" stroke-width="2"/>
        <!-- SiN Trap layer -->
        <line x1="133" y1="0" x2="133" y2="90" stroke="#8b5cf6" stroke-width="3"/>
        <!-- Tunnel Oxide -->
        <line x1="138" y1="0" x2="138" y2="90" stroke="#94a3b8" stroke-width="2"/>
        <!-- Poly-Si Channel (Macaroni) -->
        <rect x="142" y="0" width="8" height="90" fill="#10b981"/>
        <!-- Core Oxide Insulator (Center) -->
        <rect x="150" y="0" width="22" height="90" fill="#334155"/>
        <text x="152" y="48" fill="#cbd5e1" font-size="6" transform="rotate(90, 155, 48)">Core SiO2</text>
      </g>
      <text x="25" y="145" fill="#fde047" font-size="7.5" font-weight="700">★ 300단+ 초고단 수직 적층 핵심 기술:</text>
      <text x="25" y="158" fill="#a7f3d0" font-size="6.8">• HARC 홀 식각(에스펙트비 &gt; 70:1), COP(Cell Over Peri)</text>
      <text x="25" y="168" fill="#cbd5e1" font-size="6.8">• 스트링 간 결합 완벽 차단 &amp; TLC/QLC 다중 비트 저장</text>
    </g>
  </g>
</svg>''',
    "content": """
        <!-- SECTION 1: Fundamental Concept & Cell Physics -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. NAND 플래시 메모리의 기본 정의와 셀 구조
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:14px;">
            <strong>NAND 플래시 메모리(NAND Flash Memory)</strong>는 전원이 차단되어도 데이터가 지워지지 않는 <strong>비휘발성(Non-volatile) 반도체 메모리</strong>입니다.
            DRAM이 1개의 트랜지스터와 1개의 커패시터(1T-1C)로 이루어진 반면, NAND 플래시는 <strong>단 1개의 트랜지스터(1-Transistor) 자체에 전하를 가두어 데이터를 저장</strong>하므로 칩 면적당 집적도(Density)가 극도로 뛰어납니다.
          </p>

          <div style="background:#1e293b; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:800; margin-bottom:6px;">
              💡 핵심 소자 구조: 제어 게이트(CG)와 전하저장층(Charge Storage Layer)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7; margin:0;">
              일반 MOSFET은 <code>게이트 전극 - 게이트 산화막(SiO2) - 채널(Si)</code>의 구조이지만, NAND 셀은 게이트 절연막 사이에 전자를 반영구적으로 가두는 <strong>'전하저장층'</strong>이 추가로 삽입되어 있습니다:
              <br>• <strong>제어 게이트 (Control Gate, CG)</strong>: 외부에서 프로그램/소거/읽기 전압을 직접 인가하는 최상부 전극 (Word Line에 연결).
              <br>• <strong>블로킹 산화막 (Blocking Oxide, IPD)</strong>: 전하저장층에 갇힌 전자가 제어 게이트 쪽으로 새어나가지 못하도록 막는 차단막.
              <br>• <strong>전하저장층</strong>: 2D의 <strong>플로팅 게이트(Floating Gate, 도체 폴리실리콘)</strong> 또는 3D의 <strong>CTF(Charge Trap Flash, 절연체 질화막 Si3N4)</strong>.
              <br>• <strong>터널 산화막 (Tunnel Oxide)</strong>: 채널과 전하저장층 사이에서 전자가 터널링하는 초박막 산화막 (약 7~8 nm 두께의 극박막).
            </p>
          </div>
        </div>

        <!-- SECTION 2: 3 Major Operations (Program, Erase, Read) -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#10b981; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. NAND 플래시 3대 동작 메커니즘 완전 해부 (Program / Erase / Read)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:14px;">
            NAND 플래시의 데이터 쓰기, 지우기, 읽기는 <strong>터널 산화막에 걸리는 수직 전계에 의한 양자역학적 파울러-노드하임(Fowler-Nordheim, F-N) 터널링</strong>과 채널 문턱전압($V_{th}$) 이동을 기반으로 완벽하게 제어됩니다:
          </p>

          <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; padding:18px; margin-bottom:16px;">
            <h4 style="color:#60a5fa; font-size:1.05rem; font-weight:800; margin-bottom:8px;">
              ① 프로그램 동작 (Program / Write): F-N 터널링을 통한 전자 주입 ➔ 데이터 '0'
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.8; padding-left:20px; margin:0;">
              <li><strong>전압 조건</strong>: 제어 게이트(CG, 선택된 Word Line)에 <strong>약 $+18 \sim +20\,\text{V}$의 매우 높은 양전압($V_{pgm}$)</strong>을 인가하고, 채널(기판)은 $0\,\text{V}$로 유지합니다.</li>
              <li><strong>물리 메커니즘</strong>: 터널 산화막에 $10\,\text{MV/cm}$ 이상의 극도로 강한 수직 전계가 걸려 산화막의 전도대 에너지 장벽이 삼각 쐐기 모양으로 심하게 기울어집니다. 채널의 전자들이 얇아진 장벽을 양자역학적으로 뚫고 지나가는 <strong>F-N 터널링</strong>이 발생하여 전하저장층(FG/CTF)으로 쏟아져 들어갑니다.</li>
              <li><strong>소자 결과</strong>: 전하저장층에 음전하(전자)가 축적되면 제어 게이트가 채널을 켜기 위해 더 높은 양전압을 걸어주어야 하므로, <strong>셀의 문턱전압($V_{th}$)이 오른쪽(고전압 방향)으로 크게 증가</strong>합니다. 이 상태를 <strong>데이터 '0'</strong>으로 정의합니다.</li>
            </ul>
          </div>

          <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; padding:18px; margin-bottom:16px;">
            <h4 style="color:#f87171; font-size:1.05rem; font-weight:800; margin-bottom:8px;">
              ② 소거 동작 (Erase): 역방향 F-N 터널링을 통한 전자 방출 ➔ 데이터 '1' (블록 단위)
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.8; padding-left:20px; margin:0;">
              <li><strong>전압 조건</strong>: 기판(P-well 또는 3D 채널 홀)에 <strong>약 $+20\,\text{V}$의 고전압($V_{erase}$)</strong>을 가하고, 제어 게이트(CG)는 $0\,\text{V}$로 접지합니다.</li>
              <li><strong>물리 메커니즘</strong>: 프로그램과 반대 방향의 강한 수직 전계가 형성되어, 전하저장층에 갇혀 있던 전자들이 터널 산화막을 뚫고 기판으로 탈출합니다.</li>
              <li><strong>소자 결과</strong>: 전하저장층의 음전하가 비워지므로 채널 형성이 매우 쉬워져 <strong>문턱전압($V_{th}$)이 음수($V_{th} < 0\,\text{V}$) 방향으로 복귀</strong>합니다. 이 상태를 <strong>데이터 '1'</strong>이라 부릅니다.</li>
              <li><strong>블록 단위 소거</strong>: 기판(P-Well)을 수천 개의 셀이 한꺼번에 공유하므로, 개별 바이트나 페이지 단위로 지울 수 없고 <strong>반드시 블록(Block, 수 MB 단위) 전체를 한 번에 지워야만 하는 구조적 특징</strong>을 가집니다.</li>
            </ul>
          </div>

          <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; padding:18px;">
            <h4 style="color:#34d399; font-size:1.05rem; font-weight:800; margin-bottom:8px;">
              ③ 읽기 동작 (Read): 비트라인 전류 도통 여부 센싱
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.8; padding-left:20px; margin:0;">
              <li><strong>전압 조건</strong>:
                <br>• <strong>선택된 워드라인</strong>: 소거 상태 $V_{th}(<0\,\text{V})$와 프로그램 상태 $V_{th}(>0\,\text{V})$의 중간 기준 전압인 <strong>$V_{read} \approx 0 \sim 3\,\text{V}$</strong>를 인가합니다.
                <br>• <strong>비선택 워드라인들</strong>: 프로그램된 셀이든 소거된 셀이든 상관없이 무조건 켜지도록 가장 높은 $V_{th}$보다 높은 <strong>패스 전압($V_{pass} \approx 6 \sim 8\,\text{V}$)</strong>을 일괄 인가합니다.</li>
              <li><strong>판별 메커니즘</strong>:
                <br>• 선택된 셀이 <strong>소거 셀('1')</strong>인 경우: $V_{th} < V_{read}$이므로 트랜지스터가 켜져(On-cell) 비트라인에서 소스 라인으로 전류가 흐르고, 페이지 버퍼가 '1'로 판정합니다.
                <br>• 선택된 셀이 <strong>프로그램 셀('0')</strong>인 경우: $V_{th} > V_{read}$이므로 트랜지스터가 꺼져(Off-cell) 전류가 흐르지 않고, 페이지 버퍼가 '0'으로 판정합니다.</li>
            </ul>
          </div>
        </div>

        <!-- SECTION 3: 3D V-NAND Evolution & Engineering Solutions -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 2D 플래너의 한계와 3D V-NAND 혁신 기술
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:14px;">
            10nm급 이하 평면(2D) NAND에서는 이웃 셀 간 거리가 10nm 이하로 좁혀지면서 <strong>도체 플로팅 게이트 간의 정전기적 간섭(Cross-talk)</strong>과 터널 산화막에 작은 결함만 생겨도 전자 전체가 새어나가는 <strong>누설 스트레스(SILC)</strong>로 인해 물리적 스케일링이 중단되었습니다. 이를 극복한 3대 혁신이 바로 <strong>CTF, 수직 적층(3D V-NAND), 다중 비트 저장(TLC/QLC)</strong>입니다:
          </p>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px;">
            <div style="background:#1e293b; padding:16px; border-radius:8px; border-top:3px solid #38bdf8;">
              <h4 style="color:#38bdf8; font-size:0.95rem; font-weight:800; margin-bottom:6px;">① CTF (Charge Trap Flash)</h4>
              <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.65; margin:0;">
                전도성 다결정 실리콘 대신 <strong>부도체 질화막($\text{Si}_3\text{N}_4$)</strong>을 사용하여, 전하가 개별 원자 결함(Trap Site)에 격리 포박됩니다. 산화막에 핀홀 결함이 생겨도 해당 지점의 전자만 빠져나가고 나머지 전자는 그대로 유지되어 <strong>누설에 극도로 강인</strong>합니다.
              </p>
            </div>
            <div style="background:#1e293b; padding:16px; border-radius:8px; border-top:3px solid #10b981;">
              <h4 style="color:#10b981; font-size:0.95rem; font-weight:800; margin-bottom:6px;">② 3D V-NAND &amp; Macaroni Channel</h4>
              <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.65; margin:0;">
                평면 미세화 대신 <strong>워드라인을 수직으로 200~300단 이상 쌓아 올린 후 수직 구멍(Channel Hole)을 한 번에 뚫는 HARC 식각</strong>을 적용합니다. 채널 내부를 비워 산화막을 채우고 원통형 폴리실리콘 박막으로 채널을 둘러싸는 <strong>마카로니(Macaroni) 원통형 GAA 구조</strong>로 단채널 효과를 완벽 제어합니다.
              </p>
            </div>
            <div style="background:#1e293b; padding:16px; border-radius:8px; border-top:3px solid #fbbf24;">
              <h4 style="color:#fbbf24; font-size:0.95rem; font-weight:800; margin-bottom:6px;">③ 다중 비트 기술 (SLC ➔ MLC ➔ TLC ➔ QLC)</h4>
              <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.65; margin:0;">
                단일 셀 내 전하 주입량을 <strong>ISPP(Incremental Step Pulse Programming)</strong>로 정밀 제어하여, 문턱전압 상태를 1개 셀당 16개($2^4$, QLC)의 초정밀 윈도우로 쪼개어 저장 용량을 4배 폭증시킵니다.
              </p>
            </div>
          </div>
        </div>
    """
}

TOPIC_Q02 = {
    "id": "q-02",
    "num": "02",
    "badge": "⭐ 최신 질문 (휘발성 메모리 & 커패시터 물리 · 전하 공유와 센스 앰프 증폭 메커니즘 완전 해부)",
    "title": "DRAM의 기본 동작 원리: 1T-1C 셀 구조, 쓰기·읽기(전하 공유 Charge Sharing)·재충전(Refresh) 메커니즘 및 커패시터(Cs) 확보 초미세 공정 기술",
    "nav_title": "DRAM 동작원리",
    "summary": [
        "<strong>1. 셀 구조의 본질 (1T-1C 전하 축적 소자)</strong>: 1개의 스위칭 트랜지스터(Access Transistor)와 1개의 전하 저장 커패시터(Storage Capacitor, $C_s$)로 구성된 휘발성(Volatile) 메모리입니다. 커패시터에 충전된 전하량($Q = C_s \\cdot V$)으로 1비트의 데이터('1' vs '0')를 판별합니다.",
        "<strong>2. 쓰기(Write) 동작</strong>: 워드라인(WL)에 전압을 가해 접근 트랜지스터를 켠 뒤, 비트라인(BL)에 $V_{DD}$('1') 또는 $0\\,\\text{V}$('0')를 가하여 커패시터 $C_s$를 완전히 충전하거나 방전시킵니다.",
        "<strong>3. 읽기(Read)의 본질: 전하 공유(Charge Sharing)와 파괴적 읽기</strong>: 비트라인을 $\\frac{1}{2}V_{DD}$로 사전 충전(Pre-charge)한 후 WL을 켭니다. 커패시터($C_s$)와 비트라인 기생 커패시터($C_{BL}$) 간의 전하 재분배로 인해 생기는 미세 전압차 $\\Delta V = \\frac{C_s}{C_s + C_{BL}}(V_{cell} - \\frac{1}{2}V_{DD})$($\\approx 100 \\sim 200\\,\\text{mV}$)를 고감도 <strong>센스 앰프(Sense Amplifier)</strong>가 $V_{DD}$와 $0\\,\\text{V}$로 완전 풀 스윙(Full-swing) 증폭합니다. 이 과정에서 커패시터 전하가 비트라인으로 방출되는 <strong>파괴적 읽기(Destructive Read)</strong>가 일어나므로, 증폭 직후 즉시 원래 셀로 전하를 재저장(Restore)합니다.",
        "<strong>4. 재충전(Refresh)의 절대적 필요성</strong>: 커패시터는 소스/드레인 접합 누설($I_{junction}$), 트랜지스터 서브스레숄드 누설($I_{sub}$), 유전막 터널링 누설 등으로 인해 수십 ms 내에 전하가 자연 소실됩니다. 따라서 JEDEC 표준에 따라 통상 64ms 이내에 모든 셀을 주기적으로 다시 읽고 써주는 <strong>리프레시(Refresh) 동작이 필수</strong>입니다.",
        "<strong>5. 초미세 공정 핵심 과제: 셀 커패시턴스($C_s \\ge 25\\,\\text{fF}$) 사수</strong>: 10nm 선단 공정으로 갈수록 셀 면적이 축소되어 센싱 마진이 바닥납니다. 이를 극복하기 위해 종횡비 50:1 이상의 <strong>3차원 원통형 필라(Pillar) 커패시터, ZAZ($\\text{ZrO}_2/\\text{Al}_2\\text{O}_3/\\text{ZrO}_2$) High-k 유전체, TiN 메탈 전극, 매몰형 워드라인(BCAT)</strong>이 필수적으로 적용됩니다."
    ],
    "svg_title": "📊 [DRAM 셀 동작 원리 및 센스 앰프 증폭 다이어그램] (A) 1T-1C 등가 회로 및 3대 누설 전류 경로 | (B) 전하 공유(Charge Sharing) 수식 & Sense Amp 차동 증폭 래치 | (C) 3차원 High-AR 실린더 커패시터 및 ZAZ 유전막 구조",
    "svg": r'''<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: 1T-1C Equivalent Circuit & Leakage Paths -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 1T-1C 셀 등가회로 &amp; 누설 경로</text>

    <!-- Circuit Schematic -->
    <g transform="translate(15, 42)">
      <rect width="270" height="210" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 셀 회로 구성: Access NMOS + Storage Cs</text>

      <!-- Bitline Wire (Vertical) -->
      <line x1="45" y1="35" x2="45" y2="185" stroke="#38bdf8" stroke-width="2.5"/>
      <text x="25" y="30" fill="#38bdf8" font-size="8" font-weight="800">Bit Line (BL)</text>

      <!-- Access Transistor -->
      <circle cx="105" cy="110" r="28" fill="#0f172a" stroke="#60a5fa" stroke-width="1.5"/>
      <!-- S/D Connections -->
      <line x1="45" y1="110" x2="85" y2="110" stroke="#38bdf8" stroke-width="2"/>
      <line x1="125" y1="110" x2="180" y2="110" stroke="#f59e0b" stroke-width="2"/>
      <!-- Gate WL Wire (Vertical through Transistor) -->
      <line x1="105" y1="45" x2="105" y2="90" stroke="#a855f7" stroke-width="2.5"/>
      <text x="80" y="42" fill="#c084fc" font-size="8" font-weight="800">Word Line (WL)</text>
      <!-- Gate plate -->
      <line x1="95" y1="92" x2="115" y2="92" stroke="#c084fc" stroke-width="3"/>

      <!-- Storage Node & Capacitor Cs -->
      <text x="145" y="102" fill="#fde047" font-size="7" font-weight="700">Storage Node (SN)</text>
      <!-- Capacitor Plates -->
      <line x1="180" y1="95" x2="180" y2="125" stroke="#f59e0b" stroke-width="3.5"/>
      <line x1="190" y1="95" x2="190" y2="125" stroke="#10b981" stroke-width="3.5"/>
      <!-- Plate Voltage Wire -->
      <line x1="190" y1="110" x2="245" y2="110" stroke="#10b981" stroke-width="2"/>
      <text x="200" y="103" fill="#34d399" font-size="7.5" font-weight="800">Plate (Vdd/2)</text>
      <text x="175" y="142" fill="#fde047" font-size="8" font-weight="800">Cs ≥ 25fF</text>
    </g>

    <!-- 3 Major Leakage Mechanisms (Why Refresh Needed) -->
    <g transform="translate(15, 260)">
      <rect width="270" height="145" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="12" y="18" fill="#f87171" font-size="8.8" font-weight="800">2. 커패시터 전하 누설 3대 경로 (자연 방전!)</text>
      <text x="15" y="38" fill="#fca5a5" font-size="7.2">• <strong>I_sub (Subthreshold Leakage)</strong>: WL Off 상태에서 채널 누설</text>
      <text x="15" y="56" fill="#fca5a5" font-size="7.2">• <strong>I_junction (Junction Leakage)</strong>: Storage Node 접합 공핍층 누설</text>
      <text x="15" y="74" fill="#fca5a5" font-size="7.2">• <strong>I_dielectric (유전막 누설)</strong>: 커패시터 박막 양자 터널링 전류</text>
      <rect x="12" y="90" width="245" height="42" rx="4" fill="#450a0a"/>
      <text x="20" y="106" fill="#fde047" font-size="7.5" font-weight="800">⚠️ 방치 시 수십 ms 내 데이터 소실!</text>
      <text x="20" y="122" fill="#cbd5e1" font-size="7">➔ 해결책: <strong>주기적 Refresh (JEDEC 64ms 이내 재충전)</strong></text>
    </g>
  </g>

  <!-- PANEL B: Read Operation & Charge Sharing Formula -->
  <g transform="translate(340, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#10b981" font-size="12" font-weight="800">■ (B) 읽기(Read)의 본질: 전하 공유 &amp; 센싱</text>

    <!-- Step-by-Step Read Cycle -->
    <g transform="translate(15, 42)">
      <rect width="270" height="200" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 읽기 동작 4단계 사이클 (파괴적 읽기!)</text>

      <!-- Step 1 -->
      <rect x="10" y="26" width="250" height="38" rx="4" fill="#0f172a" stroke="#38bdf8"/>
      <text x="16" y="40" fill="#38bdf8" font-size="7.2" font-weight="800">① 프리차지 (Pre-charge)</text>
      <text x="16" y="54" fill="#cbd5e1" font-size="6.8">• BL 및 /BL을 Vdd/2 (통상 0.6V)로 충전 후 플로팅</text>

      <!-- Step 2 -->
      <rect x="10" y="68" width="250" height="40" rx="4" fill="#0f172a" stroke="#f59e0b"/>
      <text x="16" y="82" fill="#fbbf24" font-size="7.2" font-weight="800">② 전하 공유 (Charge Sharing)</text>
      <text x="16" y="96" fill="#cbd5e1" font-size="6.8">• WL 활성화 ➔ Cs 전하가 BL로 방출되어 미세 전위차 발생</text>

      <!-- Step 3 -->
      <rect x="10" y="112" width="250" height="40" rx="4" fill="#0f172a" stroke="#10b981"/>
      <text x="16" y="126" fill="#34d399" font-size="7.2" font-weight="800">③ 센스 앰프 증폭 (Sense Amp Amplification)</text>
      <text x="16" y="140" fill="#cbd5e1" font-size="6.8">• 크로스커플 래치가 ΔV(100~200mV)를 Vdd vs 0V로 풀 스윙</text>

      <!-- Step 4 -->
      <rect x="10" y="156" width="250" height="36" rx="4" fill="#0f172a" stroke="#c084fc"/>
      <text x="16" y="170" fill="#c084fc" font-size="7.2" font-weight="800">④ 재저장 (Restore / Auto-Rewrite)</text>
      <text x="16" y="184" fill="#cbd5e1" font-size="6.8">• 풀 스윙 전압이 트랜지스터를 통해 원래 커패시터 재충전</text>
    </g>

    <!-- Charge Sharing Math Equation & Waveform -->
    <g transform="translate(15, 252)">
      <rect width="270" height="153" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">2. 전하 공유 핵심 수식 (Signal Margin)</text>
      <rect x="15" y="28" width="240" height="42" rx="4" fill="#0b1329" stroke="#38bdf8"/>
      <text x="25" y="46" fill="#38bdf8" font-size="9" font-weight="900">$$\Delta V_{BL} = \frac{C_s}{C_s + C_{BL}} \left(V_{cell} - \frac{V_{DD}}{2}\right)$$</text>
      <text x="25" y="62" fill="#a7f3d0" font-size="7">• Cs: 셀 커패시턴스 (~25fF) | C_BL: 비트라인 기생 (~100fF)</text>

      <!-- Waveform preview -->
      <path d="M 25 110 L 80 110 L 120 95 L 240 75" fill="none" stroke="#10b981" stroke-width="2"/>
      <text x="155" y="90" fill="#34d399" font-size="7" font-weight="700">Data '1' (BL ➔ Vdd)</text>
      <path d="M 25 110 L 80 110 L 120 125 L 240 145" fill="none" stroke="#ef4444" stroke-width="2"/>
      <text x="155" y="140" fill="#f87171" font-size="7" font-weight="700">Data '0' (BL ➔ 0V)</text>
      <line x1="25" y1="110" x2="240" y2="110" stroke="#64748b" stroke-dasharray="2,2"/>
      <text x="30" y="105" fill="#fde047" font-size="6.5">Vdd/2 Precharge</text>
    </g>
  </g>

  <!-- PANEL C: Capacitor Scaling & Advanced DRAM Technology -->
  <g transform="translate(660, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="12" font-weight="800">■ (C) 초미세 DRAM 커패시터 공학</text>

    <!-- High-AR 3D Pillar Capacitor Diagram -->
    <g transform="translate(15, 42)">
      <rect width="270" height="210" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 초고종횡비(Aspect Ratio &gt; 50:1) 필라 커패시터</text>

      <!-- 3D Pillar Cross-section -->
      <g transform="translate(40, 28)">
        <!-- Bottom Electrode (Pillar TiN) -->
        <rect x="30" y="15" width="25" height="135" fill="#f59e0b" rx="2" stroke="#d97706"/>
        <text x="18" y="85" fill="#ffffff" font-size="6.5" transform="rotate(-90, 18, 85)">Bottom TiN</text>
        <!-- Dielectric Layer (ZAZ) around Pillar -->
        <rect x="25" y="12" width="35" height="141" fill="none" stroke="#38bdf8" stroke-width="2"/>
        <text x="65" y="55" fill="#38bdf8" font-size="7" font-weight="800">ZAZ High-k</text>
        <text x="65" y="68" fill="#cbd5e1" font-size="6.2">(ZrO2-Al2O3-ZrO2)</text>
        <!-- Top Electrode (TiN / Poly) -->
        <rect x="18" y="8" width="49" height="149" fill="none" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3,2"/>
        <text x="75" y="105" fill="#34d399" font-size="7">Top Electrode</text>
        <!-- Pillar Height callout -->
        <line x1="12" y1="15" x2="12" y2="150" stroke="#fde047" stroke-width="1.5"/>
        <text x="2" y="85" fill="#fde047" font-size="7.5" font-weight="800" transform="rotate(-90, 2, 85)">Height ~1.2µm</text>
      </g>
      <text x="140" y="160" fill="#fca5a5" font-size="6.5">⚠️ 쓰러짐(Toppling) 방지:</text>
      <text x="140" y="172" fill="#cbd5e1" font-size="6.5">지지대(Supporter 질화막)</text>
    </g>

    <!-- Advanced Scaling Techniques -->
    <g transform="translate(15, 260)">
      <rect width="270" height="145" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">2. 선단 10nm급 DRAM 혁신 공정 기술</text>
      <text x="15" y="38" fill="#60a5fa" font-size="7.2">• <strong>BCAT (Buried Channel Array Tr)</strong>: 트랜지스터를 기판 아래 매몰</text>
      <text x="15" y="56" fill="#34d399" font-size="7.2">• <strong>High-k Metal Gate (HKMG)</strong>: 센스앰프 및 페리 회로 고속화</text>
      <text x="15" y="74" fill="#fbbf24" font-size="7.2">• <strong>EUV 10nm 패터닝</strong>: 멀티패터닝 오버레이 마진 확보</text>
      <text x="15" y="92" fill="#c084fc" font-size="7.2">• <strong>3D DRAM / 4F² 셀</strong>: 수직 채널 트랜지스터(VCT) 연구</text>
      <rect x="12" y="106" width="245" height="28" rx="3" fill="#0f172a"/>
      <text x="18" y="124" fill="#a7f3d0" font-size="6.8">★ 핵심: 면적 축소에도 <strong>Cs ≥ 25fF 절대 사수!</strong></text>
    </g>
  </g>
</svg>''',
    "content": """
        <!-- SECTION 1: DRAM Fundamental Cell Structure -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. DRAM의 기본 정의와 1T-1C 셀 구조
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:14px;">
            <strong>DRAM(Dynamic Random Access Memory)</strong>은 데이터를 전하(Charge) 형태로 커패시터에 저장하는 고속 휘발성(Volatile) 메모리입니다.
            SRAM이 6개의 트랜지스터(6T)를 사용하여 면적이 큰 반면, DRAM은 <strong>단 1개의 접근 트랜지스터(Access Transistor)와 1개의 저장 커패시터(Storage Capacitor, $C_s$)로 구성된 '1T-1C' 구조</strong>를 채택하여 고속성과 초고집적도를 동시에 달성했습니다.
          </p>

          <div style="background:#1e293b; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:800; margin-bottom:6px;">
              💡 1T-1C 소자 구성 요소와 역할
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7; margin:0;">
              • <strong>워드라인 (Word Line, WL)</strong>: 접근 트랜지스터의 게이트 전극에 연결되어, 행(Row) 단위로 셀의 스위치를 켜고 끄는 제어선입니다.
              <br>• <strong>비트라인 (Bit Line, BL)</strong>: 접근 트랜지스터의 드레인에 연결되어, 커패시터와 데이터를 주고받거나 센싱하는 열(Column) 데이터선입니다.
              <br>• <strong>스토리지 커패시터 ($C_s$)</strong>: 접근 트랜지스터의 소스(Storage Node)에 연결되어, $Q = C_s \cdot V$의 전하를 물리적으로 저장하는 부품입니다. 반대편 플레이트 전극에는 통상 $\frac{1}{2}V_{DD}$의 전압이 걸려 있습니다.
            </p>
          </div>
        </div>

        <!-- SECTION 2: 3 Major Operations (Write, Read, Refresh) -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#10b981; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. DRAM 동작 메커니즘 완전 해부 (쓰기 / 읽기 / 재충전)
          </h3>

          <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; padding:18px; margin-bottom:16px;">
            <h4 style="color:#60a5fa; font-size:1.05rem; font-weight:800; margin-bottom:8px;">
              ① 쓰기 동작 (Write): 커패시터 충전 및 방전
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.8; padding-left:20px; margin:0;">
              <li><strong>과정</strong>:
                <br>1) 비트라인(BL)에 데이터 '1'을 쓸 경우 $V_{DD}$ 전압을, 데이터 '0'을 쓸 경우 $0\,\text{V}$ 전압을 드라이버가 인가합니다.
                <br>2) 워드라인(WL)에 하이 전압($V_{PP} > V_{DD} + V_{th}$)을 인가하여 접근 트랜지스터를 켭니다.
                <br>3) 트랜지스터 채널을 통해 전류가 흘러 커패시터 $C_s$가 $V_{DD}$로 완충('1')되거나 $0\,\text{V}$로 방전('0')됩니다.
                <br>4) 워드라인을 꺼서 트랜지스터를 닫으면, 스토리지 노드가 고립(Floating)되어 전하가 커패시터에 갇히게 됩니다.</li>
            </ul>
          </div>

          <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; padding:18px; margin-bottom:16px;">
            <h4 style="color:#34d399; font-size:1.05rem; font-weight:800; margin-bottom:8px;">
              ② 읽기 동작 (Read): 전하 공유(Charge Sharing) &amp; 파괴적 읽기 복구
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.8; padding-left:20px; margin:0;">
              <li><strong>1단계 - 프리차지 (Pre-charge)</strong>: 읽기 전, 비트라인(BL)과 기준선 역할을 하는 상보 비트라인(/BL)을 전원 전압의 절반인 <strong>$\frac{1}{2}V_{DD}$</strong>로 사전 충전한 후 플로팅(고립)시킵니다.</li>
              <li><strong>2단계 - 전하 공유 (Charge Sharing)</strong>: 워드라인(WL)을 켜면, 셀 커패시터($C_s$)에 갇혀 있던 전하와 비트라인의 거대한 기생 커패시터($C_{BL}$) 사이에 전하 재분배가 일어납니다. 이로 인해 비트라인 전압이 미세하게 변화합니다:
                <div style="background:#1e293b; padding:10px 16px; border-radius:6px; margin:8px 0; text-align:center; font-weight:800; color:#38bdf8;">
                  $$\Delta V_{BL} = \frac{C_s}{C_s + C_{BL}} \left( V_{cell} - \frac{1}{2}V_{DD} \right)$$
                </div>
                • 데이터 '1'($V_{cell} = V_{DD}$) 저장 셀: 비트라인 전압이 $\frac{1}{2}V_{DD}$보다 약 $+100 \sim 200\,\text{mV}$ 상승!
                <br>• 데이터 '0'($V_{cell} = 0\,\text{V}$) 저장 셀: 비트라인 전압이 $\frac{1}{2}V_{DD}$보다 약 $-100 \sim 200\,\text{mV}$ 하강!</li>
              <li><strong>3단계 - 센스 앰프 증폭 (Sense Amp Latch)</strong>: 교차 결합 인버터(Cross-coupled Inverter)로 구성된 차동 센스 앰프가 BL과 /BL 사이의 불과 $150\,\text{mV}$ 차이를 순식간에 감지하여 <strong>한쪽을 $V_{DD}$, 반대쪽을 $0\,\text{V}$로 완전 풀 스윙(Full-swing) 증폭</strong>합니다.</li>
              <li><strong>4단계 - 재저장 (Restore)</strong>: 전하 공유 과정에서 셀 커패시터의 전하가 비트라인으로 방출되었으므로(파괴적 읽기, Destructive Read), 센스 앰프가 $V_{DD}$ 또는 $0\,\text{V}$로 증폭한 전압을 열려 있는 트랜지스터를 통해 <strong>원래 커패시터로 즉시 재충전</strong>하여 데이터를 원상 복구합니다.</li>
            </ul>
          </div>

          <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; padding:18px;">
            <h4 style="color:#f87171; font-size:1.05rem; font-weight:800; margin-bottom:8px;">
              ③ 재충전 동작 (Refresh): 왜 DRAM은 주기적으로 전하를 다시 채워야 하는가?
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; margin:0;">
              커패시터는 절연막으로 둘러싸여 있지만 완전한 이상적 부품이 아닙니다.
              스토리지 노드 접합부의 누설 전류($I_{junction}$), 트랜지스터 채널의 오프 상태 미세 누설 전류($I_{subthreshold}$), 유전막을 통과하는 양자 터널링 누설 등으로 인해 <strong>커패시터에 저장된 전하는 상온에서 수십~수백 밀리초(ms) 이내에 자연 소실</strong>됩니다.
              <br>➔ 따라서 DRAM 컨트롤러는 데이터 유실을 방지하기 위해 <strong>JEDEC 표준에 규정된 시간(통상 64ms) 내에 칩 내부의 모든 셀 행(Row)을 순차적으로 강제로 읽고 재저장(Restore)하는 '리프레시(Refresh)' 명령</strong>을 반복 수행해야 합니다.
            </p>
          </div>
        </div>

        <!-- SECTION 3: Deep Sub-micron Scaling Issues -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 선단 10nm급 DRAM의 커패시터($C_s$) 확보 공학 기술
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:14px;">
            DRAM 미세화의 최대 난제는 셀 평면 면적($A$)이 급감함에도 불구하고, 전하 공유 센싱 마진($\Delta V$)과 리프레시 시간(Retention time) 유지를 위해 <strong>셀당 최소 커패시턴스를 반드시 $C_s \ge 25\,\text{fF/cell}$ 이상 사수해야 한다는 점</strong>입니다 ($C = \varepsilon A / d$).
            이를 극복하기 위해 글로벌 반도체 기업들은 다음 4대 한계 돌파 기술을 적용하고 있습니다:
          </p>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px;">
            <div style="background:#1e293b; padding:16px; border-radius:8px; border-top:3px solid #38bdf8;">
              <h4 style="color:#38bdf8; font-size:0.95rem; font-weight:800; margin-bottom:6px;">① 3차원 필라(Pillar)/실린더 구조</h4>
              <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.65; margin:0;">
                평면 면적이 좁으므로 수직 높이를 $1.2 \sim 1.5\,\mu\text{m}$까지 높여 <strong>종횡비(Aspect Ratio)가 50:1 이상에 달하는 3D 기둥 구조</strong>로 유효 표면적($A$)을 수십 배 확장합니다. 기둥이 쓰러지는 것을 막기 위해 중간에 질화막 서포터(Supporter)를 다단 형성합니다.
              </p>
            </div>
            <div style="background:#1e293b; padding:16px; border-radius:8px; border-top:3px solid #10b981;">
              <h4 style="color:#10b981; font-size:0.95rem; font-weight:800; margin-bottom:6px;">② ZAZ High-k 초박막 유전체</h4>
              <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.65; margin:0;">
                물리적 두께($d$)를 얇게 하면서 누설 전류를 억제하기 위해 유전율($\varepsilon_r$)이 30~40에 달하는 <strong>$\text{ZrO}_2 - \text{Al}_2\text{O}_3 - \text{ZrO}_2$ (ZAZ) 다층 원자층 증착(ALD) 박막</strong>을 적용합니다. 중간의 $\text{Al}_2\text{O}_3$ 밴드갭이 전자 터널링을 차단합니다.
              </p>
            </div>
            <div style="background:#1e293b; padding:16px; border-radius:8px; border-top:3px solid #fbbf24;">
              <h4 style="color:#fbbf24; font-size:0.95rem; font-weight:800; margin-bottom:6px;">③ BCAT (매몰형 채널 트랜지스터)</h4>
              <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.65; margin:0;">
                워드라인 게이트를 실리콘 기판 내부로 깊숙이 파묻는 <strong>Buried Channel Array Transistor</strong> 기술을 적용하여 실효 채널 길이를 확보함으로써 단채널 효과와 기판 누설 전류($I_{sub}$)를 원천 차단합니다.
              </p>
            </div>
          </div>
        </div>
    """
}

TOPIC_Q03 = {
    "id": "q-03",
    "num": "03",
    "badge": "⭐ 최신 질문 (포토리소그래피 & 고분자 화학 · 감광액 용해도 변화와 해상도 완전 비교)",
    "title": "포토레지스트(PR) 비교: Positive PR과 Negative PR의 화학적 반응 메커니즘, 현상액 용해도, 팽윤(Swelling) 왜곡 및 패턴 프로파일 완전 정복",
    "nav_title": "POSITIVE PR과 NEGATIVE PR의 차이",
    "summary": [
        "<strong>1. 핵심 정의와 극성(Tone)의 본질</strong>: 노광(빛 조사)된 영역이 현상액에 녹아 제거되면 <strong>Positive PR(포지티브 감광액)</strong>, 반대로 노광된 영역이 굳어서 남아있고 미노광 영역이 씻겨 나가면 <strong>Negative PR(네거티브 감광액)</strong>입니다.",
        "<strong>2. 화학 반응 메커니즘의 차이</strong>: Positive PR은 빛을 받아 고분자 주사슬이 끊어지거나(Chain Scission) 광산발생제(PAG)가 발생시킨 산($\\text{H}^+$)에 의해 불용성 보호기가 탈리되어 친수성(-COOH)으로 바뀌며 <strong>현상액 가용성(Soluble)</strong>으로 전환됩니다. 반면 Negative PR은 빛에 의해 단량체들이 결합하는 <strong>광가교 반응(Cross-linking)</strong>이 일어나 거대한 3차원 그물망 고분자가 되며 <strong>현상액 불용성(Insoluble)</strong>으로 굳어집니다.",
        "<strong>3. 해상도(Resolution)의 결정적 차이: 팽윤 현상(Swelling) 부재 vs 존재</strong>: Negative PR은 현상 시 유기용매 현상액이 고분자 가교망 사이로 스며들어 부풀어 오르는 <strong>팽윤 현상(Swelling)</strong>이 발생하여 미세 선폭이 왜곡되고 인접 패턴과 붙어버립니다. 반면 Positive PR은 팽윤 없이 표면부터 깨끗하게 깎여 녹아 나가므로 <strong>극미세 패턴 해상도에서 압도적 우위</strong>를 점합니다.",
        "<strong>4. 단면 프로파일(Profile) 차이</strong>: 빛이 입사할 때 상부 흡수로 인해 상부 노광량이 하부보다 많습니다. 따라서 Positive PR은 상부가 더 많이 깎여 수직에 가까운 <strong>포지티브 테이퍼($88^\\circ \\sim 90^\\circ$)</strong>를 형성하여 식각 마스크로 이상적입니다. 반면 Negative PR은 상부가 더 단단히 굳고 바닥 쪽이 덜 굳어 아래쪽이 파고드는 <strong>언더컷(Undercut) / 리버스 테이퍼</strong>를 형성합니다.",
        "<strong>5. 공정 적용 분야</strong>: Positive PR은 DUV/ArF/EUV 선단 반도체 패터닝 공정의 95% 이상을 독점하고 있으며, Negative PR은 두꺼운 막이 필요한 패키징 범프/RDL 형성, MEMS, 리프트오프(Lift-off) 공정 및 EUV 미세 콘택홀을 위한 <strong>NTD(Negative Tone Development)</strong> 공정에 특화 적용됩니다."
    ],
    "svg_title": "📊 [Positive PR vs Negative PR 메커니즘 및 패턴 프로파일 종합 비교 다이어그램] (A) 노광-현상 화학적 거동 및 용해도 역전 | (B) 단면 형상(Positive Taper vs Undercut) & 팽윤(Swelling) 왜곡 | (C) 포토 공정 적용 스펙트럼",
    "svg": r'''<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Positive PR Mechanism -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) Positive PR (빛 받은 곳 용해!)</text>

    <!-- Photolithography Steps for Positive PR -->
    <g transform="translate(15, 42)">
      <rect width="270" height="180" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 노광 및 현상 공정 단계</text>

      <!-- Step 1: Exposure with Mask -->
      <g transform="translate(15, 26)">
        <text x="0" y="10" fill="#cbd5e1" font-size="7.5" font-weight="700">[1] 노광 (UV/DUV Exposure)</text>
        <!-- Mask: Cr absorber in middle -->
        <rect x="25" y="16" width="30" height="6" fill="#64748b"/>
        <rect x="85" y="16" width="30" height="6" fill="#64748b"/>
        <text x="60" y="22" fill="#fde047" font-size="6">Open</text>
        <!-- UV Light Rays -->
        <line x1="62" y1="2" x2="62" y2="28" stroke="#fde047" stroke-width="1.5" stroke-dasharray="2,2"/>
        <line x1="72" y1="2" x2="72" y2="28" stroke="#fde047" stroke-width="1.5" stroke-dasharray="2,2"/>
        <!-- PR Layer -->
        <rect x="15" y="28" width="110" height="20" fill="#38bdf8" rx="2"/>
        <rect x="55" y="28" width="30" height="20" fill="#fde047" fill-opacity="0.6"/>
        <text x="58" y="41" fill="#0f172a" font-size="6" font-weight="800">노광 영역</text>
        <!-- Substrate -->
        <rect x="15" y="48" width="110" height="8" fill="#475569"/>
      </g>

      <!-- Step 2: Development Result -->
      <g transform="translate(15, 95)">
        <text x="0" y="10" fill="#cbd5e1" font-size="7.5" font-weight="700">[2] 현상 완료 (Development by TMAH)</text>
        <!-- Substrate -->
        <rect x="15" y="45" width="110" height="8" fill="#475569"/>
        <!-- Left PR block -->
        <polygon points="15,45 20,20 50,20 53,45" fill="#38bdf8"/>
        <!-- Right PR block -->
        <polygon points="87,45 90,20 120,20 125,45" fill="#38bdf8"/>
        <!-- Hole in the middle -->
        <text x="58" y="38" fill="#fde047" font-size="6.5" font-weight="800">녹아서 제거!</text>
        <text x="58" y="48" fill="#38bdf8" font-size="6">마스크와 동일 패턴</text>
      </g>
      <text x="15" y="168" fill="#a7f3d0" font-size="7">★ 핵심: 빛 받은 곳이 산성화되어 씻겨 나감!</text>
    </g>

    <!-- Chemical Mechanism Card -->
    <g transform="translate(15, 232)">
      <rect width="270" height="175" rx="6" fill="#1e293b" stroke="#38bdf8"/>
      <text x="12" y="18" fill="#38bdf8" font-size="8.8" font-weight="800">2. 화학 반응: 탈보호(Deprotection) 반응</text>
      <text x="15" y="38" fill="#fde047" font-size="7.5" font-weight="700">• 화학증폭형(CAR) 감광액 원리:</text>
      <text x="20" y="54" fill="#cbd5e1" font-size="7">① <strong>PAG + $h\nu$ ➔ $\text{H}^+$ (산 발생)</strong></text>
      <text x="20" y="70" fill="#cbd5e1" font-size="7">② <strong>PEB(가열)</strong>: 산이 촉매로 보호기 분해</text>
      <text x="20" y="86" fill="#cbd5e1" font-size="7">③ <strong>t-BOC/Acetal 탈리 ➔ 카복실산(-COOH) 생성</strong></text>
      <text x="20" y="102" fill="#cbd5e1" font-size="7">④ 소수성 불용 ➔ <strong>친수성 가용성으로 대전환!</strong></text>
      <rect x="12" y="116" width="245" height="48" rx="4" fill="#0b1329"/>
      <text x="20" y="132" fill="#34d399" font-size="7.5" font-weight="800">✅ 팽윤(Swelling) 없음 ➔ 초미세 해상도 압승!</text>
      <text x="20" y="146" fill="#93c5fd" font-size="7">• DUV, ArF 침액, EUV 선단 공정 절대 표준</text>
    </g>
  </g>

  <!-- PANEL B: Negative PR Mechanism -->
  <g transform="translate(340, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.2"/>
    <text x="16" y="26" fill="#ef4444" font-size="12" font-weight="800">■ (B) Negative PR (빛 받은 곳 불용화!)</text>

    <!-- Photolithography Steps for Negative PR -->
    <g transform="translate(15, 42)">
      <rect width="270" height="180" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 노광 및 현상 공정 단계</text>

      <!-- Step 1: Exposure -->
      <g transform="translate(15, 26)">
        <text x="0" y="10" fill="#cbd5e1" font-size="7.5" font-weight="700">[1] 동일 마스크 노광</text>
        <rect x="25" y="16" width="30" height="6" fill="#64748b"/>
        <rect x="85" y="16" width="30" height="6" fill="#64748b"/>
        <line x1="62" y1="2" x2="62" y2="28" stroke="#fde047" stroke-width="1.5" stroke-dasharray="2,2"/>
        <line x1="72" y1="2" x2="72" y2="28" stroke="#fde047" stroke-width="1.5" stroke-dasharray="2,2"/>
        <rect x="15" y="28" width="110" height="20" fill="#ef4444" rx="2"/>
        <rect x="55" y="28" width="30" height="20" fill="#fbbf24" fill-opacity="0.7"/>
        <text x="58" y="41" fill="#0f172a" font-size="6" font-weight="800">가교 경화</text>
        <rect x="15" y="48" width="110" height="8" fill="#475569"/>
      </g>

      <!-- Step 2: Development Result -->
      <g transform="translate(15, 95)">
        <text x="0" y="10" fill="#cbd5e1" font-size="7.5" font-weight="700">[2] 현상 완료 (미노광부 용해)</text>
        <rect x="15" y="45" width="110" height="8" fill="#475569"/>
        <!-- Only middle PR block remains! Inverted pattern -->
        <polygon points="50,45 46,20 94,20 90,45" fill="#ef4444"/>
        <text x="53" y="36" fill="#ffffff" font-size="6.5" font-weight="800">경화되어 잔류!</text>
        <text x="18" y="38" fill="#94a3b8" font-size="6">씻겨 나감</text>
        <text x="96" y="38" fill="#94a3b8" font-size="6">씻겨 나감</text>
      </g>
      <text x="15" y="168" fill="#fca5a5" font-size="7">★ 핵심: 빛 받은 곳이 그물망으로 굳어 남음!</text>
    </g>

    <!-- Chemical Mechanism & Swelling Issue -->
    <g transform="translate(15, 232)">
      <rect width="270" height="175" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="12" y="18" fill="#f87171" font-size="8.8" font-weight="800">2. 광가교(Cross-linking)와 팽윤(Swelling)</text>
      <text x="15" y="38" fill="#fde047" font-size="7.5" font-weight="700">• 화학 가교 메커니즘:</text>
      <text x="20" y="54" fill="#cbd5e1" font-size="7">① 선형 폴리머 + 가교제 + 광산발생제</text>
      <text x="20" y="70" fill="#cbd5e1" font-size="7">② 노광 부위 ➔ <strong>3차원 그물망 고분자 형성</strong></text>
      <text x="20" y="86" fill="#cbd5e1" font-size="7">③ 분자량 폭증 ➔ 유기용매 현상액에 불용화</text>
      <rect x="12" y="100" width="245" height="62" rx="4" fill="#450a0a"/>
      <text x="20" y="116" fill="#fca5a5" font-size="7.5" font-weight="800">⚠️ 치명적 한계: 팽윤 현상 (Swelling)</text>
      <text x="20" y="130" fill="#fca5a5" font-size="6.8">• 현상액 용매가 고분자 사이로 침투해 부풀어 오름!</text>
      <text x="20" y="144" fill="#cbd5e1" font-size="6.8">• 미세 선폭 왜곡, 패턴 쓰러짐 ➔ <strong>선단 미세화 불가</strong></text>
      <text x="20" y="156" fill="#fde047" font-size="6.8">• 단, 접착력·내화학성·후막 형성력은 우수!</text>
    </g>
  </g>

  <!-- PANEL C: Profile & Comprehensive Comparison -->
  <g transform="translate(660, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#fbbf24" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="12" font-weight="800">■ (C) 단면 프로파일 및 종합 특성 비교</text>

    <!-- Side-by-side Profiles -->
    <g transform="translate(15, 42)">
      <rect width="270" height="150" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 단면 프로파일 형상 (빛 흡수 불균일 기인)</text>

      <!-- Positive Profile -->
      <g transform="translate(15, 28)">
        <rect x="0" y="60" width="110" height="6" fill="#475569"/>
        <!-- Positive Taper Profile: Narrower at top, wider at bottom -->
        <polygon points="10,60 16,10 50,10 56,60" fill="#38bdf8"/>
        <text x="15" y="80" fill="#38bdf8" font-size="7.5" font-weight="800">Positive Taper</text>
        <text x="10" y="94" fill="#cbd5e1" font-size="6.5">• 상부 노광량 많아 더 깎임</text>
        <text x="10" y="106" fill="#a7f3d0" font-size="6.5">• 각도 88°~90° (수직성 우수)</text>
        <text x="10" y="118" fill="#fde047" font-size="6.5">✅ 식각 마스크에 이상적</text>
      </g>

      <!-- Negative Profile -->
      <g transform="translate(145, 28)">
        <rect x="0" y="60" width="110" height="6" fill="#475569"/>
        <!-- Negative Profile: Undercut, wider at top, narrower at bottom -->
        <polygon points="20,60 10,10 55,10 45,60" fill="#ef4444"/>
        <text x="15" y="80" fill="#f87171" font-size="7.5" font-weight="800">Undercut (역테이퍼)</text>
        <text x="10" y="94" fill="#cbd5e1" font-size="6.5">• 상부 경화 심하고 바닥 덜 굳음</text>
        <text x="10" y="106" fill="#fca5a5" font-size="6.5">• 하부 파고드는 언더컷 형성</text>
        <text x="10" y="118" fill="#fbbf24" font-size="6.5">✅ Lift-off 박리에 유리</text>
      </g>
    </g>

    <!-- Comparison Summary Table -->
    <g transform="translate(15, 202)">
      <rect width="270" height="205" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">2. 핵심 성능 5대 지표 맞비교 표</text>

      <g transform="translate(10, 28)">
        <!-- Table Header -->
        <rect width="250" height="18" fill="#0f172a" rx="2"/>
        <text x="8" y="13" fill="#cbd5e1" font-size="7" font-weight="800">비교 항목</text>
        <text x="80" y="13" fill="#38bdf8" font-size="7" font-weight="800">Positive PR</text>
        <text x="170" y="13" fill="#f87171" font-size="7" font-weight="800">Negative PR</text>

        <!-- Row 1: Resolution -->
        <line x1="0" y1="36" x2="250" y2="36" stroke="#334155"/>
        <text x="8" y="31" fill="#fde047" font-size="6.8" font-weight="700">해상도</text>
        <text x="80" y="31" fill="#38bdf8" font-size="6.8">★ 압도적 우수 (팽윤X)</text>
        <text x="170" y="31" fill="#cbd5e1" font-size="6.8">열세 (팽윤 현상)</text>

        <!-- Row 2: Adhesion -->
        <line x1="0" y1="54" x2="250" y2="54" stroke="#334155"/>
        <text x="8" y="49" fill="#fde047" font-size="6.8" font-weight="700">기판 접착력</text>
        <text x="80" y="49" fill="#cbd5e1" font-size="6.8">보통 (HMDS 프라이머)</text>
        <text x="170" y="49" fill="#34d399" font-size="6.8">★ 매우 우수</text>

        <!-- Row 3: Etch Resistance -->
        <line x1="0" y1="72" x2="250" y2="72" stroke="#334155"/>
        <text x="8" y="67" fill="#fde047" font-size="6.8" font-weight="700">내화학성/내식각</text>
        <text x="80" y="67" fill="#cbd5e1" font-size="6.8">양호</text>
        <text x="170" y="67" fill="#34d399" font-size="6.8">★ 가교로 매우 단단</text>

        <!-- Row 4: Developer -->
        <line x1="0" y1="90" x2="250" y2="90" stroke="#334155"/>
        <text x="8" y="85" fill="#fde047" font-size="6.8" font-weight="700">현상액 종류</text>
        <text x="80" y="85" fill="#cbd5e1" font-size="6.8">수용성 알칼리 (TMAH)</text>
        <text x="170" y="85" fill="#cbd5e1" font-size="6.8">유기용매 (자일렌 등)</text>

        <!-- Row 5: Profile -->
        <line x1="0" y1="108" x2="250" y2="108" stroke="#334155"/>
        <text x="8" y="103" fill="#fde047" font-size="6.8" font-weight="700">단면 프로파일</text>
        <text x="80" y="103" fill="#38bdf8" font-size="6.8">수직 테이퍼 (88°~90°)</text>
        <text x="170" y="103" fill="#f87171" font-size="6.8">언더컷 (역테이퍼)</text>

        <!-- Row 6: Applications -->
        <line x1="0" y1="126" x2="250" y2="126" stroke="#334155"/>
        <text x="8" y="121" fill="#fde047" font-size="6.8" font-weight="700">주요 공정</text>
        <text x="80" y="121" fill="#38bdf8" font-size="6.8">선단 DUV/EUV 패터닝</text>
        <text x="170" y="121" fill="#cbd5e1" font-size="6.8">패키징, 범프, RDL</text>
      </g>
      <text x="15" y="195" fill="#38bdf8" font-size="6.8">💡 EUV 최신 트렌드: 유기용매 현상으로 고해상도를 얻는 <strong>NTD 기술</strong></text>
    </g>
  </g>
</svg>''',
    "content": """
        <!-- SECTION 1: Fundamental Concept & Polarities -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 포토레지스트(PR)의 정의와 포지티브 vs 네거티브 극성(Tone)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:14px;">
            <strong>포토레지스트(Photoresist, PR)</strong>는 빛(자외선, DUV, EUV 등)을 받았을 때 화학 구조가 변하여 현상액(Developer)에 대한 용해도(Solubility)가 달라지는 감광성 고분자 재료입니다.
            포토마스크를 통해 빛을 선택적으로 조사한 뒤 현상액을 뿌렸을 때 <strong>어느 부위가 씻겨 나가고 어느 부위가 남느냐</strong>에 따라 포지티브와 네거티브로 명확히 나뉩니다:
          </p>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin-bottom:16px;">
            <div style="background:#1e293b; border-left:4px solid #38bdf8; padding:16px; border-radius:0 8px 8px 0;">
              <h4 style="color:#38bdf8; font-size:1rem; font-weight:800; margin-bottom:6px;">① Positive PR (양화 감광액)</h4>
              <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
                • <strong>빛을 받은(노광된) 영역</strong>이 화학적으로 분해되어 현상액에 <strong>용해(Soluble)</strong>되어 씻겨 나갑니다.
                <br>• <strong>빛을 받지 않은(미노광) 영역</strong>이 기판 위에 그대로 잔류합니다.
                <br>• 결과: <strong>포토마스크의 차광 패턴과 100% 동일한 형태의 PR 패턴</strong>이 웨이퍼에 형성됩니다.
              </p>
            </div>
            <div style="background:#1e293b; border-left:4px solid #ef4444; padding:16px; border-radius:0 8px 8px 0;">
              <h4 style="color:#f87171; font-size:1rem; font-weight:800; margin-bottom:6px;">② Negative PR (음화 감광액)</h4>
              <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
                • <strong>빛을 받은(노광된) 영역</strong>이 광가교 결합으로 굳어져 현상액에 <strong>불용화(Insoluble)</strong>되어 남습니다.
                <br>• <strong>빛을 받지 않은(미노광) 영역</strong>이 현상액에 녹아 씻겨 나갑니다.
                <br>• 결과: <strong>포토마스크 차광 패턴과 흑백이 반전된 형태(음화)</strong>로 PR 패턴이 형성됩니다.
              </p>
            </div>
          </div>
        </div>

        <!-- SECTION 2: Chemical Mechanisms & Swelling Physics -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#10b981; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 화학적 반응 메커니즘과 해상도(Resolution)를 가르는 '팽윤 현상'
          </h3>

          <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; padding:18px; margin-bottom:16px;">
            <h4 style="color:#38bdf8; font-size:1.05rem; font-weight:800; margin-bottom:8px;">
              [1] Positive PR 화학 메커니즘: 탈보호(Deprotection) 반응
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; margin:0;">
              현대 선단 공정(KrF, ArF, EUV)의 Positive PR은 거의 100% <strong>화학증폭형(Chemically Amplified Resist, CAR)</strong> 구조를 따릅니다:
              <br>1) <strong>광산발생제(PAG)</strong>: 노광 시 광자를 흡수한 PAG가 극소량의 산(Acid, $\text{H}^+$)을 발생시킵니다.
              <br>2) <strong>PEB (노광 후 열처리)</strong>: 약 $100 \sim 120^\circ\text{C}$로 가열하면 발생한 산($\text{H}^+$)이 촉매가 되어 고분자 베이스 수지에 붙어 있던 소수성 보호기(Protecting Group, 예: t-BOC)를 연속적으로 수백 번 떼어내는 연쇄 탈보호 반응을 일으킵니다.
              <br>3) <strong>용해도 전환</strong>: 소수성(현상액 불용)이었던 수지가 친수성 카복실산($-\text{COOH}$)과 페놀성 수산기($-\text{OH}$)로 전환되어, 약알칼리 현상액(2.38% TMAH 수용액)에 <strong>팽윤 없이 표면부터 깨끗하게 녹아 나갑니다.</strong>
            </p>
          </div>

          <div style="background:#0f172a; border:1px solid #1e293b; border-radius:10px; padding:18px; margin-bottom:16px;">
            <h4 style="color:#f87171; font-size:1.05rem; font-weight:800; margin-bottom:8px;">
              [2] Negative PR 화학 메커니즘: 광가교(Cross-linking)와 치명적 팽윤(Swelling)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; margin:0;">
              Negative PR은 선형 고분자(Polymer Chain)와 가교제(Cross-linker), 감광제(Sensitizer)로 구성됩니다:
              <br>1) <strong>광가교 반응</strong>: 빛을 받으면 활성화된 가교제가 선형 고분자 사슬들 사이를 3차원 그물망 형태로 단단하게 엮어 묶어버립니다. 분자량이 기하급수적으로 폭증하여 현상액(유기용매)에 완전히 녹지 않는 불용성 플라스틱 덩어리로 변합니다.
              <br>2) <strong>치명적 한계: 팽윤 현상(Swelling Effect)</strong>:
              가교된 3차원 그물망 사이로 유기용매 현상액 분자가 스며들면서 <strong>PR 패턴이 젤리처럼 퉁퉁 부풀어 오르는 현상</strong>이 발생합니다. 현상 후 건조될 때 부풀었던 패턴이 수축하면서 선폭이 비뚤어지거나 뭉개지고, 인접한 미세 패턴들끼리 서로 달라붙는 가교 브릿지 불량(Pattern Bridging)이 발생합니다.
              <br>➔ <strong>이 팽윤 현상 때문에 Negative PR은 0.5µm 이하의 미세 패터닝 공정에서 완전히 퇴출</strong>당했습니다!
            </p>
          </div>
        </div>

        <!-- SECTION 3: Profile Comparison & Modern Engineering Trends -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 단면 프로파일(Profile) 차이와 현대 반도체 공정 적용 스펙트럼
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:14px;">
            빛이 감광액 상부에서 바닥으로 침투할 때 비어-램버트 법칙에 의해 아래로 갈수록 빛이 흡수되어 감쇠합니다. 즉, <strong>항상 상부 표면의 노광량이 바닥 쪽 노광량보다 큽니다.</strong> 이 물리적 현상으로 인해 정반대의 단면 프로파일이 형성됩니다:
          </p>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:16px; margin-bottom:16px;">
            <div style="background:#1e293b; padding:16px; border-radius:8px;">
              <h4 style="color:#38bdf8; font-size:0.95rem; font-weight:800; margin-bottom:6px;">① Positive PR의 포지티브 테이퍼 ($88^\circ \sim 90^\circ$)</h4>
              <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.65; margin:0;">
                상부가 빛을 더 많이 받아 더 넓게 녹고 아래쪽은 상대적으로 덜 녹아 <strong>사다리꼴(바닥이 살짝 넓거나 완벽한 수직) 형상</strong>을 이룹니다. 이 형상은 후속 건식 식각(RIE) 공정 시 플라즈마 이온 폭격에 대해 마스크의 하부 치수를 안전하게 방어해 주므로 <strong>식각 마스크로서 가장 이상적인 프로파일</strong>입니다.
              </p>
            </div>
            <div style="background:#1e293b; padding:16px; border-radius:8px;">
              <h4 style="color:#f87171; font-size:0.95rem; font-weight:800; margin-bottom:6px;">② Negative PR의 언더컷 / 리버스 테이퍼 (Undercut)</h4>
              <p style="color:#cbd5e1; font-size:0.85rem; line-height:1.65; margin:0;">
                상부는 빛을 많이 받아 단단히 가교되지만, 바닥 쪽은 빛이 부족하여 덜 굳어 현상 시 바닥이 더 많이 파여 나갑니다. 역삼각형의 <strong>처마(Overhang) 및 언더컷</strong>이 형성되어 식각 마스크로는 부적합하지만, 금속을 증착한 후 PR을 녹여내는 <strong>리프트오프(Lift-off) 공정에서는 금속막이 단절되어 박리가 쉬우므로 완벽한 솔루션</strong>이 됩니다.
              </p>
            </div>
          </div>

          <div style="background:#0f172a; border-left:4px solid #fbbf24; padding:16px 20px; border-radius:0 8px 8px 0;">
            <h4 style="color:#fbbf24; font-size:1rem; font-weight:800; margin-bottom:6px;">
              💡 최신 첨단 노광 기술: NTD (Negative Tone Development)의 화려한 부활
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7; margin:0;">
              전통적인 Negative PR은 팽윤 때문에 사라졌지만, 최근 ArF Immersion 및 EUV의 <strong>극미세 콘택홀(Contact Hole) 및 트렌치(Trench) 형성</strong>에서는 <strong>NTD 기술</strong>이 핵심 표준으로 자리잡았습니다.
              <br>• 재료는 팽윤이 없는 Positive CAR 수지를 그대로 사용하되, 현상액을 수용액(TMAH) 대신 <strong>유기용매(예: n-부틸 아세테이트, n-BA)</strong>로 바꿉니다.
              <br>• 그러면 극성이 역전되어 <strong>빛을 받지 않은 비노광부가 유기용매에 녹아 나가고, 빛을 받아 극성이 바뀐 노광부가 남아 네거티브 톤으로 작동</strong>합니다.
              <br>• 마스크 상의 밝은 고립 패턴을 조사하므로 광학적 명암비(Optical Contrast)가 대폭 향상되어 <strong>EUV 콘택홀의 CD 균일도(CDU)를 획기적으로 개선</strong>할 수 있습니다!
            </p>
          </div>
        </div>
    """
}

TOPICS = [TOPIC_Q01, TOPIC_Q02, TOPIC_Q03]

def process_file(file_path):
    print(f"Reading {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 104 topics (q-104 down to q-01) by +3 -> to q-107 down to q-04
    for old_n in range(104, 0, -1):
        new_n = old_n + 3
        old_str = f"{old_n:02d}"
        new_str = f"{new_n:02d}"

        # 1.1 In nav-list
        html = re.sub(
            rf'<li class="nav-item"><a href="#q-{old_str}" class="nav-link"><span class="nav-num">{old_str}</span><span class="nav-text">(.*?)</span></a></li>',
            rf'<li class="nav-item"><a href="#q-{new_str}" class="nav-link"><span class="nav-num">{new_str}</span><span class="nav-text">\1</span></a></li>',
            html
        )

        # 1.2 In topic-section tag
        html = re.sub(
            rf'<section class="topic-section([^"]*)" id="q-{old_str}">',
            rf'<section class="topic-section\1" id="q-{new_str}">',
            html
        )

        # 1.3 In topic-badge
        html = re.sub(
            rf'<span class="topic-badge">Q {old_str}</span>',
            rf'<span class="topic-badge">Q {new_str}</span>',
            html
        )

    # Step 2: Remove latest-card-highlight and latest-tag from old q-04
    html = re.sub(
        r'<section class="topic-section latest-card-highlight" id="q-04">',
        r'<section class="topic-section" id="q-04">',
        html
    )
    html = re.sub(
        r'<span class="latest-tag">⭐ 최신 질문.*?</span>\s*',
        r'',
        html,
        count=1
    )

    # Step 3: Build HTML for new topics (Q01, Q02, Q03)
    # Nav items
    nav_html_items = []
    for t in TOPICS:
        nav_html_items.append(
            f'      <li class="nav-item"><a href="#{t["id"]}" class="nav-link"><span class="nav-num">{t["num"]}</span><span class="nav-text">{t["nav_title"]}</span></a></li>'
        )
    new_nav_html = "\n" + "\n".join(nav_html_items)

    # Topic sections
    sections_html = []
    for idx, t in enumerate(TOPICS):
        highlight_cls = " latest-card-highlight" if idx == 0 else ""
        latest_tag_html = f'\n          <span class="latest-tag">{t["badge"]}</span>' if idx == 0 else ""

        summary_items_html = "\n".join([f"          <li>{s}</li>" for s in t["summary"]])

        sec = f"""
    <!-- {t["id"].upper()} : {t["title"]} -->
    <section class="topic-section{highlight_cls}" id="{t["id"]}">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q {t["num"]}</span>{latest_tag_html}
          <h2 class="topic-title">{t["title"]}</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">강의 핵심 요약 포인트</span>
        <ul class="summary-list">
{summary_items_html}
        </ul>
      </div>
      <div class="lecture-content">
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            {t["svg_title"]}
          </div>
          {t["svg"]}
        </div>
{t["content"]}
      </div>
    </section>
"""
        sections_html.append(sec)

    all_new_sections = "\n".join(sections_html)

    # Step 4: Insert new nav items right below <ul class="nav-list" id="navList">
    nav_list_pattern = r'(<ul class="nav-list" id="navList">)'
    html = re.sub(nav_list_pattern, rf'\1{new_nav_html}', html, count=1)

    # Step 5: Insert new sections right before the first topic section (<section class="topic-section" id="q-04">)
    sec_pattern = r'(<!-- Q-04 :|<!-- Q 04 :|<section class="topic-section" id="q-04">)'
    match = re.search(sec_pattern, html)
    if not match:
        print("Error: Could not find q-04 section anchor!")
        sys.exit(1)
    insert_pos = match.start()
    html = html[:insert_pos] + all_new_sections + "\n" + html[insert_pos:]

    # Step 6: Update total questions count in main-desc
    html = re.sub(
        r'총 \d+개 질문으로 구성되어 있습니다',
        r'총 107개 질문으로 구성되어 있습니다',
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}! (New total: 107 questions)")

# Update both files
process_file(r"C:\Work\반도체3\index.html")
process_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
print("All files updated successfully!")
