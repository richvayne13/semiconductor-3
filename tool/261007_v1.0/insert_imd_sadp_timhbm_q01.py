# -*- coding: utf-8 -*-
"""
insert_imd_sadp_timhbm_q01.py
사용자 질문:
1. "imd가 뭐의줄인말이야"
2. "스페이서를 마스크로 활용해 피치를 줄인느기술이라는게 무슨뜻인지 설명해줘"
3. "tim이 hbm안에서 어떻게구성되어있는지 그림으로 그려줘 방열판과 칩표면 사이 미세공기를 채워 열저항을 극소화한다는데 이거설명해주고 그림에표시해줘"
4. "옆에 왼쪽 목차서랍 여닫을수있게해줘 닫으면 본문이 커지게해주고"

대시보드 최상단 Q01로 신규 추가하고, 기존 77개 질문을 Q02~Q78로 시프트 (총 78개 질문 백과사전).
좌측 목차 서랍 여닫기(토글 접기/열기 및 본문 전체화면 확장) UI 기능 구현.
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (BEOL 배선 · 다중 패터닝 · 첨단 패키징)",
    "title": "IMD(금속간 절연막)의 정의 · 스페이서 피치 분할(SADP) 원리 · HBM 패키지 TIM 미세공기 충진 메커니즘",
    "nav_title": "IMD 정의, 스페이서 피치분할(SADP), HBM TIM 미세공기 충진",
    "summary": [
        "<strong>IMD (Inter-Metal Dielectric, 금속간 절연막)</strong>: 금속 배선 층간(M1-M2, M2-M3 등) 및 배선 라인 사이를 절연하는 유전체입니다. FEOL과 M1 사이를 격리하는 <strong>ILD(Inter-Layer Dielectric)와 구분</strong>되며, 배선 미세화에 따른 기생 커패시턴스($C_{inter}$)를 줄여 신호 지연($RC$ Delay)과 크로스토크(Crosstalk)를 억제하기 위해 <strong>Low-k($k < 2.5$, SiCOH 등) 소재</strong>를 필수 적용합니다.",
        "<strong>스페이서를 마스크로 활용한 피치 분할 (SADP, Self-Aligned Double Patterning)</strong>: 리소그래피 노광 빛의 파장 해상도 한계(Rayleigh Limit)를 우회하기 위해, 희생 패턴(Core/Mandrel) 측벽에 균일한 두께의 <strong>스페이서를 Conformal 증착 후 수직 에치백</strong>하여 측벽만 남기고 희생 패턴을 제거합니다. <strong>원래 1개 패턴 자리에 2개의 스페이서 마스크가 남아 피치를 정확히 1/2(밀도 2배)로 분할</strong>하며, 자체 정렬(Self-Aligned)되어 오버레이 에러가 없습니다.",
        "<strong>HBM 내 TIM(Thermal Interface Material)의 위치와 역할</strong>: 실리콘 인터포저 위 HBM 16단 스택 및 GPU 칩 표면과 상부 방열판(IHS/Cold Plate) 사이에 얇게 도포됩니다.",
        "<strong>미세 공기 충진과 열저항 극소화 메커니즘</strong>: 눈에 보이지 않는 금속과 실리콘 표면의 미세 요철(Micro-roughness)로 인해 그냥 맞대면 <strong>단열재 수준의 공기($k_{air} \\approx 0.026 \\text{ W/m}\\cdot\\text{K}$)</strong>가 갇혀 접촉 열저항($R_{th}$)이 폭발합니다. 유동성 TIM($k \\approx 3 \\sim 80 \\text{ W/m}\\cdot\\text{K}$)이 <strong>미세 공기 주머니를 100% 밀어내고 빈틈을 완전 충진(Air Displacement)</strong>하여 열을 고속도로처럼 방열판으로 전도 방출합니다."
    ],
    "svg_title": "📊 [3대 핵심 구조 해부도] (A) BEOL 배선 속 IMD vs ILD | (B) SADP 스페이서 피치 1/2 분할 5단계 | (C) HBM 패키지 TIM 미세공기 충진 확대도",
    "svg": """<svg viewBox="0 0 980 480" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="480" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: IMD vs ILD Structure -->
  <g transform="translate(20, 20)">
    <rect width="295" height="440" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) IMD vs ILD 배선 계층 비교</text>

    <!-- Metal 3 -->
    <rect x="25" y="45" width="245" height="22" rx="4" fill="#0284c7"/>
    <text x="110" y="60" fill="#ffffff" font-size="10" font-weight="700">Metal 3 (Cu 배선)</text>

    <!-- IMD 2 -->
    <rect x="25" y="72" width="245" height="50" rx="4" fill="#1e293b" stroke="#0ea5e9" stroke-dasharray="3,2"/>
    <text x="85" y="94" fill="#38bdf8" font-size="10" font-weight="800">IMD (Inter-Metal Dielectric)</text>
    <text x="85" y="110" fill="#94a3b8" font-size="8.5">• Low-k (SiCOH, k &lt; 2.5)</text>
    <rect x="55" y="72" width="20" height="50" fill="#ea580c"/>
    <text x="59" y="100" fill="#fff" font-size="8">Via2</text>
    <rect x="220" y="72" width="20" height="50" fill="#ea580c"/>
    <text x="224" y="100" fill="#fff" font-size="8">Via2</text>

    <!-- Metal 2 -->
    <rect x="25" y="127" width="245" height="22" rx="4" fill="#0284c7"/>
    <text x="110" y="142" fill="#ffffff" font-size="10" font-weight="700">Metal 2 (Cu 배선)</text>

    <!-- IMD 1 -->
    <rect x="25" y="154" width="245" height="50" rx="4" fill="#1e293b" stroke="#0ea5e9" stroke-dasharray="3,2"/>
    <text x="85" y="176" fill="#38bdf8" font-size="10" font-weight="800">IMD (M1-M2 절연막)</text>
    <text x="85" y="192" fill="#94a3b8" font-size="8.5">• C_inter 기생용량 극소화</text>
    <rect x="135" y="154" width="25" height="50" fill="#ea580c"/>
    <text x="139" y="182" fill="#fff" font-size="8">Via1</text>

    <!-- Metal 1 -->
    <rect x="25" y="209" width="245" height="22" rx="4" fill="#0284c7"/>
    <text x="85" y="224" fill="#ffffff" font-size="10" font-weight="700">Metal 1 (M1: BEOL 시작점)</text>

    <!-- ILD -->
    <rect x="25" y="236" width="245" height="58" rx="4" fill="#1e293b" stroke="#a855f7" stroke-dasharray="3,2"/>
    <text x="85" y="258" fill="#c084fc" font-size="10" font-weight="800">ILD (Inter-Layer Dielectric)</text>
    <text x="85" y="274" fill="#cbd5e1" font-size="8.5">• 트랜지스터 ↔ M1 분리 (BPSG/SiO₂)</text>
    <rect x="60" y="236" width="18" height="58" fill="#64748b"/>
    <text x="63" y="268" fill="#fff" font-size="8">W-Plug</text>
    <rect x="210" y="236" width="18" height="58" fill="#64748b"/>
    <text x="213" y="268" fill="#fff" font-size="8">W-Plug</text>

    <!-- FEOL Transistors -->
    <rect x="25" y="299" width="245" height="42" rx="4" fill="#047857"/>
    <rect x="90" y="303" width="30" height="15" fill="#f59e0b"/>
    <rect x="175" y="303" width="30" height="15" fill="#f59e0b"/>
    <text x="96" y="314" fill="#000" font-size="7.5" font-weight="700">Gate</text>
    <text x="181" y="314" fill="#000" font-size="7.5" font-weight="700">Gate</text>
    <text x="95" y="333" fill="#ffffff" font-size="9" font-weight="700">Si Substrate (FEOL 소자 영역)</text>

    <!-- Summary Box -->
    <rect x="15" y="350" width="265" height="76" rx="6" fill="#0b1329" stroke="#334155"/>
    <text x="25" y="369" fill="#38bdf8" font-size="9" font-weight="800">★ 핵심 요약 차이점:</text>
    <text x="25" y="386" fill="#cbd5e1" font-size="8.5">• ILD: 기판 소자(게이트)와 M1 사이 절연</text>
    <text x="25" y="402" fill="#cbd5e1" font-size="8.5">• IMD: M1-M2 등 금속 배선 층간 절연</text>
    <text x="25" y="418" fill="#fde047" font-size="8">• IMD는 RC 딜레이 방지 위해 Low-k 필수!</text>
  </g>

  <!-- PANEL B: SADP Spacer Pitch Splitting -->
  <g transform="translate(330, 20)">
    <rect width="320" height="440" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 스페이서 피치 분할 (SADP 원리)</text>

    <!-- Step 1: Mandrel formation -->
    <g transform="translate(15, 38)">
      <rect width="290" height="65" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="16" fill="#38bdf8" font-size="9" font-weight="700">1단계: 희생 Core(Mandrel) 패터닝 (피치 P₀)</text>
      <!-- Substrate -->
      <rect x="15" y="48" width="260" height="10" fill="#334155"/>
      <!-- Mandrel 1 & 2 -->
      <rect x="50" y="24" width="45" height="24" fill="#f59e0b" rx="2"/>
      <text x="56" y="39" fill="#000" font-size="8" font-weight="800">Mandrel</text>
      <rect x="180" y="24" width="45" height="24" fill="#f59e0b" rx="2"/>
      <text x="186" y="39" fill="#000" font-size="8" font-weight="800">Mandrel</text>
      <!-- Pitch line -->
      <line x1="50" y1="21" x2="180" y2="21" stroke="#38bdf8" stroke-width="1.2"/>
      <text x="105" y="18" fill="#38bdf8" font-size="8">피치 P₀</text>
    </g>

    <!-- Step 2: Conformal Spacer ALD -->
    <g transform="translate(15, 110)">
      <rect width="290" height="65" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="16" fill="#34d399" font-size="9" font-weight="700">2단계: ALD Conformal 스페이서 균일 증착</text>
      <rect x="15" y="48" width="260" height="10" fill="#334155"/>
      <!-- Spacer film over mandrel 1 -->
      <rect x="36" y="22" width="73" height="26" fill="#10b981" rx="2"/>
      <rect x="50" y="26" width="45" height="22" fill="#f59e0b"/>
      <!-- Spacer film over mandrel 2 -->
      <rect x="166" y="22" width="73" height="26" fill="#10b981" rx="2"/>
      <rect x="180" y="26" width="45" height="22" fill="#f59e0b"/>
      <text x="245" y="38" fill="#6ee7b7" font-size="7.5">균일 두께 ws</text>
    </g>

    <!-- Step 3: Vertical RIE Etchback -->
    <g transform="translate(15, 182)">
      <rect width="290" height="65" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="16" fill="#facc15" font-size="9" font-weight="700">3단계: 수직 비등방성 RIE 에치백 (측벽만 잔류)</text>
      <rect x="15" y="48" width="260" height="10" fill="#334155"/>
      <!-- Mandrel 1 with spacers -->
      <rect x="36" y="24" width="14" height="24" fill="#10b981"/>
      <rect x="50" y="24" width="45" height="24" fill="#f59e0b"/>
      <rect x="95" y="24" width="14" height="24" fill="#10b981"/>
      <!-- Mandrel 2 with spacers -->
      <rect x="166" y="24" width="14" height="24" fill="#10b981"/>
      <rect x="180" y="24" width="45" height="24" fill="#f59e0b"/>
      <rect x="225" y="24" width="14" height="24" fill="#10b981"/>
      <!-- Down arrows -->
      <text x="125" y="36" fill="#facc15" font-size="8">↓↓ RIE 수직식각</text>
    </g>

    <!-- Step 4 & 5: Strip Mandrel & Pitch Halved -->
    <g transform="translate(15, 254)">
      <rect width="290" height="85" rx="5" fill="#1e293b" stroke="#10b981"/>
      <text x="10" y="16" fill="#4ade80" font-size="9" font-weight="800">4 &amp; 5단계: 희생막 제거 ➔ 피치 1/2 분할 완성!</text>
      <rect x="15" y="60" width="260" height="10" fill="#334155"/>
      <!-- 4 spacers remaining -->
      <rect x="36" y="32" width="14" height="28" fill="#10b981" rx="1"/>
      <rect x="95" y="32" width="14" height="28" fill="#10b981" rx="1"/>
      <rect x="166" y="32" width="14" height="28" fill="#10b981" rx="1"/>
      <rect x="225" y="32" width="14" height="28" fill="#10b981" rx="1"/>
      <!-- Pitch line 1/2 -->
      <line x1="36" y1="28" x2="95" y2="28" stroke="#4ade80" stroke-width="1.2"/>
      <text x="50" y="25" fill="#4ade80" font-size="8" font-weight="800">P₀ / 2</text>
      <line x1="95" y1="28" x2="166" y2="28" stroke="#4ade80" stroke-width="1.2"/>
      <text x="118" y="25" fill="#4ade80" font-size="8" font-weight="800">P₀ / 2</text>
      <text x="12" y="80" fill="#bbf7d0" font-size="8.5 font-weight=700">★ 1개 희생선 ➔ 양 측벽 2개 라인! 밀도 2배, 피치 50% 축소</text>
    </g>

    <!-- Pitch Split Summary Box -->
    <rect x="15" y="350" width="290" height="76" rx="6" fill="#0b1329" stroke="#334155"/>
    <text x="25" y="369" fill="#34d399" font-size="9" font-weight="800">★ 자가정렬(Self-Aligned)의 결정적 이점:</text>
    <text x="25" y="386" fill="#cbd5e1" font-size="8.5">• 빛의 회절 한계(Rayleigh Limit) 물리적 극복</text>
    <text x="25" y="402" fill="#cbd5e1" font-size="8.5">• 스페이서 두께(선폭)는 ALD 원자 단위로 제어</text>
    <text x="25" y="418" fill="#fde047" font-size="8.5">• 2번 노광(LELE)과 달리 오버레이(틀어짐) 에러 제로</text>
  </g>

  <!-- PANEL C: HBM TIM Structure & Micro-gap Filling -->
  <g transform="translate(665, 20)">
    <rect width="295" height="440" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) HBM TIM &amp; 미세공기 충진 메커니즘</text>

    <!-- Top Heat Sink / IHS -->
    <rect x="20" y="42" width="255" height="30" rx="3" fill="#475569"/>
    <text x="45" y="61" fill="#f8fafc" font-size="10" font-weight="700">금속 방열판 (Heat Sink / IHS 구리 덮개)</text>

    <!-- TIM Layer -->
    <rect x="20" y="76" width="255" height="14" fill="#f59e0b" rx="2"/>
    <text x="80" y="87" fill="#000000" font-size="9" font-weight="800">TIM 층 (Thermal Interface Material)</text>

    <!-- HBM Stack & GPU -->
    <g transform="translate(20, 94)">
      <!-- HBM 16-Stack -->
      <rect x="0" y="0" width="135" height="105" rx="3" fill="#1e293b" stroke="#38bdf8"/>
      <text x="10" y="15" fill="#38bdf8" font-size="8.5" font-weight="800">HBM 16단 적층 스택</text>
      <!-- DRAM layers -->
      <line x1="5" y1="22" x2="130" y2="22" stroke="#475569"/>
      <line x1="5" y1="30" x2="130" y2="30" stroke="#475569"/>
      <line x1="5" y1="38" x2="130" y2="38" stroke="#475569"/>
      <line x1="5" y1="46" x2="130" y2="46" stroke="#475569"/>
      <line x1="5" y1="54" x2="130" y2="54" stroke="#475569"/>
      <text x="32" y="70" fill="#94a3b8" font-size="8">16 × DRAM Dies</text>
      <text x="25" y="84" fill="#fbbf24" font-size="7.5">TSV 관통전극 + MR-MUF</text>
      <rect x="5" y="90" width="125" height="12" fill="#0284c7" rx="1"/>
      <text x="40" y="99" fill="#fff" font-size="7.5">Base Die (Logic)</text>

      <!-- GPU Die -->
      <rect x="145" y="0" width="110" height="105" rx="3" fill="#1e293b" stroke="#a855f7"/>
      <text x="160" y="20" fill="#c084fc" font-size="9" font-weight="800">로직 다이 (GPU)</text>
      <text x="165" y="45" fill="#94a3b8" font-size="8">초고발열 코어</text>
      <text x="160" y="65" fill="#ef4444" font-size="8" font-weight="700">TDP 700W+ 열원</text>
      <text x="155" y="85" fill="#cbd5e1" font-size="7.5">핫스팟 집중 발생</text>
    </g>

    <!-- Substrate / Interposer -->
    <rect x="20" y="203" width="255" height="12" rx="2" fill="#334155"/>
    <text x="75" y="212" fill="#cbd5e1" font-size="7.5">2.5D 실리콘 인터포저 &amp; 패키지 기판</text>

    <!-- Microscopic Zoom Section: The Core Explanation -->
    <g transform="translate(15, 222)">
      <rect width="265" height="204" rx="6" fill="#0b1329" stroke="#f59e0b" stroke-width="1.2"/>
      <text x="10" y="16" fill="#fde047" font-size="9.5" font-weight="800">🔍 계면 미세 요철(Micro-roughness) 현미경 확대</text>

      <!-- Sub-case 1: WITHOUT TIM (Air Trap = Insulation) -->
      <g transform="translate(10, 24)">
        <rect width="118" height="110" rx="4" fill="#1e293b" stroke="#ef4444"/>
        <text x="8" y="14" fill="#ef4444" font-size="8" font-weight="800">[TIM 미도포: 공기 트랩]</text>
        <!-- Heat Sink rough surface -->
        <path d="M 10 24 L 25 35 L 45 22 L 65 37 L 85 23 L 108 34 L 108 20 L 10 20 Z" fill="#64748b"/>
        <!-- Air gaps inside valleys -->
        <rect x="10" y="35" width="98" height="28" fill="#1e293b"/>
        <circle cx="35" cy="48" r="6" fill="#ef4444" opacity="0.4"/>
        <text x="25" y="51" fill="#fca5a5" font-size="7">공기</text>
        <circle cx="75" cy="46" r="7" fill="#ef4444" opacity="0.4"/>
        <text x="65" y="49" fill="#fca5a5" font-size="7">Air Gap</text>
        <!-- Chip rough surface -->
        <path d="M 10 63 L 30 52 L 50 65 L 75 51 L 95 64 L 108 53 L 108 72 L 10 72 Z" fill="#0284c7"/>
        <text x="8" y="86" fill="#fca5a5" font-size="7.5">• 공기 k=0.026 W/mK (단열재)</text>
        <text x="8" y="98" fill="#ef4444" font-size="7.5" font-weight="700">➔ 접촉 열저항 R_th 폭발! 열폭주</text>
      </g>

      <!-- Sub-case 2: WITH TIM (Air Displaced = Perfect Conduction) -->
      <g transform="translate(136, 24)">
        <rect width="118" height="110" rx="4" fill="#1e293b" stroke="#10b981"/>
        <text x="8" y="14" fill="#34d399" font-size="8" font-weight="800">[TIM 도포: 100% 충진]</text>
        <!-- Heat Sink rough surface -->
        <path d="M 10 24 L 25 35 L 45 22 L 65 37 L 85 23 L 108 34 L 108 20 L 10 20 Z" fill="#64748b"/>
        <!-- TIM perfectly fills between -->
        <rect x="10" y="32" width="98" height="34" fill="#f59e0b"/>
        <text x="22" y="50" fill="#000" font-size="8" font-weight="900">TIM 완전 충진!</text>
        <!-- Chip rough surface -->
        <path d="M 10 63 L 30 52 L 50 65 L 75 51 L 95 64 L 108 53 L 108 72 L 10 72 Z" fill="#0284c7"/>
        <text x="8" y="86" fill="#86efac" font-size="7.5">• TIM k=3~80 W/mK 고전도</text>
        <text x="8" y="98" fill="#34d399" font-size="7.5" font-weight="700">➔ R_th 극소화! 열 고속 방출</text>
      </g>

      <!-- Formula -->
      <rect x="10" y="140" width="244" height="54" rx="4" fill="#0f172a" stroke="#475569"/>
      <text x="18" y="156" fill="#fbbf24" font-size="8.5" font-weight="800">접촉 열저항 공식: R_th = BLT / (k_TIM × A)</text>
      <text x="18" y="172" fill="#cbd5e1" font-size="7.5">• BLT(두께) 극소화 + 공기 주머니 배출(Air Displacement)</text>
      <text x="18" y="186" fill="#cbd5e1" font-size="7.5">• HBM 적층 칩의 핫스팟 제거 및 수명/속도 확보 필수재!</text>
    </g>
  </g>
</svg>""",
    "lecture": """
        <!-- Section 1: IMD -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. IMD(Inter-Metal Dielectric)란 무엇인가? (정의, 역할, ILD와의 차이점)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체 공정에서 <strong>IMD</strong>는 <strong>Inter-Metal Dielectric(금속간 절연막)</strong>의 줄임말입니다. 트랜지스터 상부에 수직으로 다층 적층되는 구리(Cu) 또는 알루미늄(Al) 금속 배선(BEOL, Back-End of Line) 계층에서, <strong>금속 배선 층과 층 사이(예: Metal 1 ↔ Metal 2, Metal 2 ↔ Metal 3), 그리고 동일 평면 상의 배선 라인들 사이를 물리적·전기적으로 격리하는 절연막</strong>을 의미합니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:14px 18px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:700; margin-bottom:8px;">💡 반도체 엔지니어가 반드시 구분해야 하는 ILD vs IMD의 경계</h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.7; padding-left:18px;">
              <li><strong>ILD (Inter-Layer Dielectric, 층간 절연막)</strong>: 실리콘 기판 상의 <strong>트랜지스터(MOSFET Gate, Source/Drain 등 FEOL) 영역과 최초의 1차 금속 배선(Metal 1) 사이</strong>를 분리하는 절연막입니다. 트랜지스터의 고온 열처리 공정을 견뎌야 하며, 주로 BPSG, USG(Undoped Silicate Glass), SiN 등이 사용되고 텅스텐(W) 콘택트 플러그가 이를 관통합니다.</li>
              <li><strong>IMD (Inter-Metal Dielectric, 금속간 절연막)</strong>: <strong>Metal 1 이상의 금속 배선들 사이</strong>를 채우는 절연막입니다. Cu 다마신 공정으로 Via와 배선을 절연하며, <strong>Low-k(저유전율) 특성이 칩의 신호 속도를 결정짓는 핵심</strong>입니다.</li>
            </ul>
          </div>

          <h4 style="font-size:1rem; font-weight:700; color:#fde047; margin:14px 0 8px;">■ IMD에서 Low-k(저유전율) 박막이 절대적으로 중요한 이유 (RC 지연 공식)</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            선폭이 미세화됨에 따라 배선 간 간격($d$)이 극도로 좁아지면서, 금속선 사이의 기생 커패시턴스($C_{inter}$)가 폭발적으로 증가합니다:
            $$\tau = R_{metal} \times C_{IMD} \quad \left( C_{IMD} = \epsilon_0 k \frac{A}{d} \right)$$
            기존 $\\text{SiO}_2$($k \\approx 4.0$)를 그대로 쓰면 신호 지연($RC$ Delay)과 옆 라인으로 신호가 번지는 크로스토크(Crosstalk 노이즈)로 인해 칩 동작 속도가 심각하게 제한됩니다. 따라서 반도체 업계는 탄소(C)와 수소(H)를 도핑하여 밀도를 낮춘 <strong>SiCOH(Carbon-doped Oxide, $k \\approx 2.5 \\sim 3.0$)</strong> 및 나노 기공을 뚫은 <strong>Porous Low-k($k &lt; 2.2$)</strong> 절연막을 IMD로 적극 채택하고 있습니다.
          </p>
        </div>

        <!-- Section 2: Spacer Pitch Splitting -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 스페이서를 마스크로 활용해 피치를 줄이는 기술(SADP)이란 무슨 뜻인가?
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            질문자님께서 질문하신 기술은 반도체 미세 패터닝의 금자탑인 <strong>SADP (Self-Aligned Double Patterning, 자가정렬 2중 패터닝)</strong> 및 <strong>SAQP (Self-Aligned Quadruple Patterning, 4중 패터닝)</strong>를 의미합니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:14px 18px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:700; margin-bottom:8px;">💡 왜 빛(노광기)으로 직접 안 그리고 '스페이서'를 마스크로 쓸까?</h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7; margin-bottom:6px;">
              노광 장비(ArFi 193nm 액침 리소그래피)의 분해능은 레일리 공식($R = k_1 \\frac{\\lambda}{\\text{NA}}$)에 의해 단일 노광으로 그릴 수 있는 최소 피치(Pitch = 선폭 + 간격)가 약 <strong>80nm 수준으로 물리적으로 제한</strong>됩니다. EUV가 도입되기 전, 10nm/7nm급 미세 회로를 구현하기 위해 <strong>'노광 장비의 빛으로는 넓은 패턴을 그리고, 박막 증착과 식각으로 물리적 1/2 피치를 만들어내는 묘수'</strong>가 개발되었는데, 이것이 바로 스페이서 피치 분할입니다.
            </p>
          </div>

          <h4 style="font-size:1rem; font-weight:700; color:#fde047; margin:14px 0 8px;">■ 스페이서 피치 분할의 5단계 정밀 메커니즘</h4>
          <ol style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:22px; margin-bottom:14px;">
            <li><strong>1단계: 희생 Mandrel(코어) 형성</strong>: 기존 노광 장비로 구현 가능한 넓은 피치($P_0$)로 희생 패턴(주로 비정질 탄소 ACL 또는 폴리실리콘)을 형성합니다.</li>
            <li><strong>2단계: Conformal Spacer 박막 증착</strong>: <strong>ALD(원자층 증착)</strong> 기술을 이용해 희생 패턴의 상단, 바닥, 그리고 <strong>수직 측벽(Sidewall) 전체에 Å(옹스트롬) 단위로 극도로 균일한 절연막($\\text{SiO}_2$ 또는 $\\text{Si}_3\\text{N}_4$)을 얇게 코팅</strong>합니다. 이때 증착한 스페이서의 두께($t_{spacer}$)가 <strong>최종 회로의 선폭(CD)</strong>이 됩니다!</li>
            <li><strong>3단계: 수직 비등방성 RIE 에치백 (Etch-Back)</strong>: 수직 방향으로만 이온을 내리꽂는 이방성 플라즈마 건식 식각을 가합니다. 수평면(상단과 바닥)에 덮여 있던 스페이서는 전부 깎여 나가고, <strong>희생 패턴의 양쪽 수직 측벽에 달라붙어 있던 스페이서 기둥만 고스란히 남습니다</strong>.</li>
            <li><strong>4단계: 희생 Mandrel 선택적 제거 (Stripping)</strong>: 스페이서는 건드리지 않고 중앙의 희생막만 선택적으로 화학 식각(Wet/Dry Strip)하여 제거합니다.</li>
            <li><strong>5단계: 피치 1/2 분할 완성 (Double Patterning)</strong>: 원래 1개의 희생 패턴이 있던 자리에 <strong>양쪽 측벽에 남은 2개의 얇은 스페이서 라인이 새로운 하드마스크가 됩니다!</strong> 라인 수가 2배로 증가하면서 <strong>피치는 정확히 절반($P_0 / 2$)으로 축소</strong>됩니다. (이 과정을 한 번 더 반복하면 피치가 1/4로 줄어드는 SAQP가 됩니다.)</li>
          </ol>

          <p style="font-size:0.92rem; line-height:1.7; color:#a7f3d0;">
            ★ <strong>'Self-Aligned(자가정렬)'의 의미</strong>: 마스크를 2번 찍는 LELE(Litho-Etch-Litho-Etch) 방식은 두 번의 노광 간 위치가 조금만 틀어져도 심각한 오버레이 에러(Overlay Error)가 발생합니다. 반면 SADP는 <strong>희생 패턴의 물리적 측벽에 스페이서가 스스로 붙어서 정렬되므로 오버레이 정렬 오차가 수학적으로 '0'</strong>이며, ALD의 완벽한 두께 제어 덕분에 극도의 선폭 균일도(CD Uniformity)를 달성합니다.
          </p>
        </div>

        <!-- Section 3: TIM in HBM -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. HBM 안에서 TIM은 어떻게 구성되어 있고, 미세 공기를 채워 열저항을 극소화한다는 것은 무슨 뜻인가?
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            <strong>TIM(Thermal Interface Material, 열계면물질)</strong>은 HBM 및 AI 가속기(GPU/NPU) 패키징에서 칩의 열폭주를 방지하는 최전선 방열 소재입니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#38bdf8; margin:14px 0 8px;">■ HBM 패키지 내 TIM의 물리적 구성 위치</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            HBM은 2.5D 실리콘 인터포저 위에 GPU와 나란히 실장되며, 베이스 다이 위에 DRAM 다이가 12단~16단으로 높게 쌓여 있습니다. 이 전체 패키지를 덮는 거대한 구리 합금 덮개(IHS: Integrated Heat Spreader) 또는 수랭 쿨러(Liquid Cold Plate)가 상단에 체결됩니다.<br>
            이때 <strong>TIM(통상 TIM 1)은 HBM 스택의 최상단 실리콘 다이(Top DRAM Die)의 윗면, 그리고 GPU 다이의 윗면과 금속 방열판(IHS/Cold Plate)의 밑면 '바로 사이'에 도포</strong>됩니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #f59e0b; padding:14px 18px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#fbbf24; font-size:1rem; font-weight:700; margin-bottom:8px;">💡 "방열판과 칩 표면 사이 미세공기를 채워 열저항을 극소화한다"의 물리적 진실</h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:18px;">
              <li><strong>1. 표면의 미세 거칠기 (Microscopic Roughness)</strong>: 아무리 기계적으로 거울처럼 반짝이게 연마한 실리콘 칩과 금속 방열판이라도, 전자현미경으로 확대해 보면 수 마이크로미터($\\mu\\text{m}$) 단위의 <strong>울퉁불퉁한 산(Peak)과 골짜기(Valley) 요철</strong>이 존재합니다.</li>
              <li><strong>2. 고체 맞대기 시 발생하는 '공기 트랩(Air Pockets)'의 비극</strong>: 두 고체를 그냥 맞대면, 뾰족한 산 끝부분만 닿으므로 <strong>실제 물리적 접촉 면적은 전체의 1~2%에 불과</strong>하며, 나머지 98%는 <strong>'갇힌 미세 공기(Air Gap)'</strong>가 차지합니다.</li>
              <li><strong>3. 정지 공기의 열전도율 비극 ($k_{air} \\approx 0.026 \\text{ W/m}\\cdot\\text{K}$)</strong>: 정지된 공기는 스티로폼이나 유리섬유 수준의 <strong>'완벽한 단열재'</strong>입니다! 이 공기 틈새가 열의 흐름을 꽉 가로막으면서 접촉 계면의 열저항($R_{th}$)이 수십 배로 폭등하여, HBM의 온도가 100℃를 넘어 DRAM 데이터가 지워지고 GPU가 스로틀링(다운)에 빠집니다.</li>
              <li><strong>4. TIM의 공기 밀어내기 충진 (Air Displacement)</strong>: 유동성이 있는 페이스트, 액상 겔, 상변화물질(PCM), 또는 고열전도성 인듐(Indium) 솔더($k \\approx 3 \\sim 86 \\text{ W/m}\\cdot\\text{K}$)를 도포하고 압력을 가하면, <strong>미세 요철 골짜기 사이로 파고들어 갇혀 있던 공기를 100% 밖으로 밀어내며 빈틈을 꽉 채웁니다</strong>.</li>
              <li><strong>5. 열전도율 100~3,000배 급증</strong>: 단열 공기($0.026$)가 고열전도체 TIM($3\\sim86$)으로 대체되면서, 계면 접촉 열저항 공식:
                $$R_{th,contact} = \\frac{\\text{BLT}}{k_{TIM} \\times A} + R_{c1} + R_{c2}$$
                에서 열저항이 극소화되어 HBM 내부에서 생성된 막대한 열이 고속도로를 탄 것처럼 방열판으로 쏜살같이 전도 방출됩니다.</li>
            </ul>
          </div>
        </div>

        <!-- Section 4: Comprehensive Comparison Table -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.15rem; font-weight:800; color:#e2e8f0; margin-bottom:12px;">
            4. 핵심 요약 비교 정리표
          </h3>
          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">구분 항목</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">핵심 정의 및 위치</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">극복하는 물리적 한계</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">핵심 소재 / 기술 원리</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">IMD (금속간 절연막)</td>
                  <td style="padding:10px 14px;">BEOL Metal 1 이상 배선 계층 사이 및 라인 간 격리 절연막</td>
                  <td style="padding:10px 14px;">배선 간 기생 커패시턴스($C_{inter}$) 폭증으로 인한 $RC$ 딜레이 및 크로스토크</td>
                  <td style="padding:10px 14px;">Low-k 박막 (SiCOH, Porous organosilicate, $k &lt; 2.5$)</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#34d399;">스페이서 피치 분할 (SADP)</td>
                  <td style="padding:10px 14px;">희생 패턴(Core) 측벽 스페이서를 하드마스크로 활용해 피치를 1/2로 분할</td>
                  <td style="padding:10px 14px;">빛의 파장 회절 한계(Rayleigh Limit) 및 LELE의 오버레이 정렬 오차</td>
                  <td style="padding:10px 14px;">ALD 원자층 증착(선폭 제어) + 수직 이방성 RIE 에치백 + 자가정렬</td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#fbbf24;">HBM 패키지 TIM</td>
                  <td style="padding:10px 14px;">HBM 상단 실리콘 다이 / GPU 표면과 금속 방열판(IHS/Cold Plate) 접촉 계면</td>
                  <td style="padding:10px 14px;">미세 요철 사이 갇힌 단열 공기($k_{air}=0.026$)로 인한 접촉 열저항 폭발 및 열폭주</td>
                  <td style="padding:10px 14px;">Air Displacement(공기 완전 배출), 인듐 솔더/PCM/열전도 그리스 ($k=3\\sim86$)</td>
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

    # Step 1: Shift existing 77 topics (q-77 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(77, 0, -1):
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

    # Step 4: Add collapsible drawer CSS and floating button / collapse button
    # Add transition to aside & main in CSS if not present
    if "/* 좌측 사이드바 토글 및 본문 확장 스타일 */" not in html:
        old_aside_css = """    /* 좌측 사이드바: 질문 리스트 */
    aside {"""
        new_aside_css = """    /* 좌측 사이드바 토글 및 본문 확장 스타일 */
    body.sidebar-collapsed aside {
      transform: translateX(-100%);
    }

    body.sidebar-collapsed main {
      margin-left: 0;
      max-width: 100%;
      padding: 40px 80px 100px;
    }

    .drawer-toggle-btn {
      background: rgba(30, 41, 59, 0.85);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: #38bdf8;
      border-radius: 6px;
      padding: 5px 11px;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s ease;
      white-space: nowrap;
    }
    .drawer-toggle-btn:hover {
      background: #0284c7;
      color: #ffffff;
      border-color: #38bdf8;
    }

    .drawer-float-open-btn {
      position: fixed;
      top: 18px;
      left: 18px;
      z-index: 99;
      background: #0f172a;
      border: 1.5px solid #38bdf8;
      color: #38bdf8;
      border-radius: 8px;
      padding: 8px 16px;
      font-size: 0.88rem;
      font-weight: 800;
      cursor: pointer;
      display: none;
      align-items: center;
      gap: 7px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
      transition: all 0.2s ease;
    }
    .drawer-float-open-btn:hover {
      background: #38bdf8;
      color: #0f172a;
      transform: translateY(-2px);
      box-shadow: 0 6px 25px rgba(56, 189, 248, 0.4);
    }
    body.sidebar-collapsed .drawer-float-open-btn {
      display: inline-flex;
    }

    /* 좌측 사이드바: 질문 리스트 */
    aside {
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);"""
        html = html.replace(old_aside_css, new_aside_css)

        # Also add transition to main
        old_main_css = """    main {
      margin-left: 380px;
      flex: 1;
      padding: 40px 60px 100px;
      max-width: 1250px;
    }"""
        new_main_css = """    main {
      margin-left: 380px;
      flex: 1;
      padding: 40px 60px 100px;
      max-width: 1250px;
      transition: margin-left 0.3s cubic-bezier(0.4, 0, 0.2, 1), max-width 0.3s cubic-bezier(0.4, 0, 0.2, 1), padding 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }"""
        html = html.replace(old_main_css, new_main_css)

    # Step 5: Inject buttons in HTML
    if '<button id="sidebarFloatOpenBtn"' not in html:
        float_btn_html = '  <!-- 목차 서랍 열기 플로팅 버튼 (서랍 접혔을 때 표시) -->\n  <button id="sidebarFloatOpenBtn" class="drawer-float-open-btn" title="목차 펼치기"><span>📑</span> <span>목차 열기</span></button>\n\n  <aside'
        html = html.replace('  <!-- 좌측 내비게이션 바: 질문자님의 실제 질문들이 탭 제목으로 배치! -->\n  <aside', '  <!-- 좌측 내비게이션 바: 질문자님의 실제 질문들이 탭 제목으로 배치! -->\n' + float_btn_html)

    if '<button id="sidebarCollapseBtn"' not in html:
        old_header = """    <div class="sidebar-header">
      <h1>반도체 3 Q&A 백과사전</h1>
      <p>질문하신 순서의 역순(최신순)으로 정렬된 탭</p>
    </div>"""
        new_header = """    <div class="sidebar-header">
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <h1>반도체 3 Q&A 백과사전</h1>
        <button id="sidebarCollapseBtn" class="drawer-toggle-btn" title="목차 서랍 닫기">◀ 목차 접기</button>
      </div>
      <p>질문하신 순서의 역순(최신순)으로 정렬된 탭</p>
    </div>"""
        html = html.replace(old_header, new_header)

    # Step 6: Add JS for toggling sidebar drawer
    if 'sidebarCollapseBtn' not in html or 'sidebarFloatOpenBtn' not in html:
        pass
    else:
        if '/* 목차 서랍 토글 스크립트 */' not in html:
            toggle_js = """
    // 목차 서랍 여닫기 (토글 & 본문 확장)
    const sidebarCollapseBtn = document.getElementById('sidebarCollapseBtn');
    const sidebarFloatOpenBtn = document.getElementById('sidebarFloatOpenBtn');

    if (sidebarCollapseBtn) {
      sidebarCollapseBtn.addEventListener('click', () => {
        document.body.classList.add('sidebar-collapsed');
        localStorage.setItem('sidebar_collapsed', 'true');
      });
    }

    if (sidebarFloatOpenBtn) {
      sidebarFloatOpenBtn.addEventListener('click', () => {
        document.body.classList.remove('sidebar-collapsed');
        localStorage.setItem('sidebar_collapsed', 'false');
      });
    }

    if (localStorage.getItem('sidebar_collapsed') === 'true') {
      document.body.classList.add('sidebar-collapsed');
    }
"""
            html = html.replace("</script>", toggle_js + "  </script>")

    # Step 7: Update header description
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 'IMD 정의, 스페이서 피치분할(SADP), HBM TIM 미세공기 충진'이 위치하며, 총 78개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 IMD, SADP, and TIM topics and Collapsible Sidebar Drawer!")
