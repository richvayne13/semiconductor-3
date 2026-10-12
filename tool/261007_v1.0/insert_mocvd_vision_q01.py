# -*- coding: utf-8 -*-
"""
insert_mocvd_vision_q01.py
사용자 질문:
"MOCVD의 비전에 대해서 설명하세요. 
현재는 MOCVD로 가려하고 있습니다. 그 이유는 Ⅲ-Ⅴ 반도체 때문입니다... 
이거 3-5족 반도체라고해도돼? 뭐라고불러야돼 면접에서"

기존 97개 질문을 Q02~Q98로 시프트하고, 최상단 Q01에 신규 등록 (총 98개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (화합물 반도체 & 차세대 에피택시 · MOCVD의 미래 비전과 3-5족/Ge 고이동도 채널, 표준 호칭 가이드)",
    "title": "MOCVD의 미래 비전과 3-5족(III-V)·Ge 고이동도 채널 완전 정복 (호칭 가이드, Post-Si 로직, GaN 전력, 실리콘 포토닉스)",
    "nav_title": "MOCVD의 비전과 3-5족(III-V)·Ge 채널",
    "summary": [
        "<strong>1. 면접 및 실무 호칭 가이드: '3-5족 반도체'라고 불러도 100% 완벽합니다!</strong>: 구두 표현으로는 <strong>'삼오족 반도체'</strong> 또는 글로벌 표준인 <strong>'쓰리 파이브(Three-Five) 반도체'</strong>가 가장 자연스럽고 널리 쓰이며, 정식 학술/산업 명칭은 <strong>'3-5족 화합물 반도체 (III-V Compound Semiconductor)'</strong>입니다. 처음 언급할 때 '3-5족 화합물 반도체'라고 명확히 짚어주면 전문성을 극대화할 수 있습니다.",
        "<strong>2. Post-Si 한계 돌파: 3-5족(NMOS)과 Ge(PMOS) 고이동도 채널 혁신</strong>: 실리콘(Si)의 물리적 미세화 한계($V_{DD}$ 스케일링 정체)를 극복하기 위해, 전자의 유효 질량이 극도로 가벼워 전자 이동도가 20~25배 높은 <strong>3-5족(InGaAs, InAs)</strong>으로 NMOS를 대체하고, 정공 이동도가 4.4배 높은 <strong>게르마늄(Ge)</strong>으로 PMOS를 대체하여 초저전압($0.5\\,\\text{V}$) 구동과 폭발적인 구동 전류($I_{on}$)를 확보하려는 차세대 비전입니다.",
        "<strong>3. MOCVD(유기금속 화학기상증착)의 본질과 양산성 우위</strong>: 유기금속 전구체(MO, 예: TMGa, TMIn)와 5족 수소화물 가스($\\text{AsH}_3, \\text{PH}_3$)를 고온에서 열분해하여 단결정 박막을 원자층 단위로 성장시키는 에피택시(Epitaxy) 기술입니다. 연구용 MBE(분자선 에피택시) 대비 압도적인 성장 속도와 300mm 대구경 웨이퍼 양산성(Throughput)을 갖춘 유일한 대량 양산 플랫폼입니다.",
        "<strong>4. MOCVD의 3대 미래 비전</strong>: ① <strong>초고속 로직(Logic)</strong>: 3D 적층 CFET 구조에서 Si 기판 위에 InGaAs/Ge 이종 채널을 결합하는 핵심 공정, ② <strong>전력 반도체(Power)</strong>: 전기차와 AI 데이터센터용 GaN-on-Si 고전압/고효율 소자 양산 지배, ③ <strong>실리콘 포토닉스(Photonics)</strong>: 빛을 내지 못하는 Si의 한계를 넘어 CPO 광통신 레이저 광원(InP, GaAs)을 직접 집적하는 필수 장비입니다."
    ],
    "svg_title": "📊 [MOCVD 및 3-5족/Ge 차세대 반도체 종합 아키텍처 다이어그램] (A) 3-5족(InGaAs) & Ge 캐리어 이동도 대결 | (B) MOCVD 단결정 에피택시 메커니즘 | (C) MOCVD 3대 미래 비전 로드맵",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: High Mobility Channel (III-V & Ge vs Si) -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 3-5족 &amp; Ge 고이동도 채널 혁신</text>

    <!-- Mobility Comparison Card -->
    <g transform="translate(15, 38)">
      <rect width="270" height="200" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">캐리어 이동도 (Mobility) 드라마틱한 격차</text>

      <!-- Row 1: Electron Mobility NMOS -->
      <g transform="translate(10, 26)">
        <rect width="250" height="74" rx="4" fill="#0b1329" stroke="#38bdf8"/>
        <text x="8" y="14" fill="#38bdf8" font-size="8" font-weight="800">1. NMOS: 전자 이동도 (μₑ) 대결</text>
        <text x="14" y="28" fill="#cbd5e1" font-size="7.2">• Si (실리콘): 1,400 cm²/V·s (기준)</text>
        <text x="14" y="42" fill="#34d399" font-size="7.5" font-weight="800">• InGaAs: 10,000 ~ 15,000 cm²/V·s (10배↑)</text>
        <text x="14" y="56" fill="#fde047" font-size="7.8" font-weight="900">• InAs (3-5족): 33,000 cm²/V·s (25배 폭증!)</text>
        <text x="14" y="68" fill="#94a3b8" font-size="6.8">➔ 극도로 가벼운 유효질량(m* = 0.02 m₀)으로 총알 주행</text>
      </g>

      <!-- Row 2: Hole Mobility PMOS -->
      <g transform="translate(10, 108)">
        <rect width="250" height="78" rx="4" fill="#0b1329" stroke="#f59e0b"/>
        <text x="8" y="14" fill="#fbbf24" font-size="8" font-weight="800">2. PMOS: 정공 이동도 (μₕ) 대결</text>
        <text x="14" y="28" fill="#cbd5e1" font-size="7.2">• Si (실리콘): 450 cm²/V·s (병목 원인!)</text>
        <text x="14" y="44" fill="#fde047" font-size="7.8" font-weight="900">• Ge (게르마늄): 1,900 cm²/V·s (4.4배 향상!)</text>
        <text x="14" y="58" fill="#a7f3d0" font-size="7.2">• PMOS 채널 면적을 1/4로 줄여 CMOS 대칭 달성</text>
        <text x="14" y="70" fill="#94a3b8" font-size="6.8">➔ Ge의 좁은 밴드갭(0.66eV)과 완만한 유효질량</text>
      </g>
    </g>

    <!-- Post-Si Impact -->
    <g transform="translate(15, 248)">
      <rect width="270" height="157" rx="5" fill="#0b1329" stroke="#38bdf8"/>
      <text x="12" y="18" fill="#38bdf8" font-size="8.8" font-weight="800">소자 성능(Performance) 비약의 메커니즘</text>
      <text x="12" y="36" fill="#fde047" font-size="7.8" font-weight="800">① 저전압 구동 (V_DD 0.7V ➔ 0.5V↓):</text>
      <text x="18" y="49" fill="#cbd5e1" font-size="7.2">• 낮은 전압에서도 막대한 구동 전류(I_on) 확보</text>
      <text x="18" y="61" fill="#cbd5e1" font-size="7.2">• 동적 전력 소모(P ∝ C·V²·f) 대폭 절감!</text>
      <text x="12" y="78" fill="#34d399" font-size="7.8" font-weight="800">② 고주파 테라헤르츠(THz) 스위칭 속도</text>
      <text x="12" y="96" fill="#f87171" font-size="7.8" font-weight="800">③ 극복 과제 (MOCVD의 사명):</text>
      <text x="18" y="109" fill="#cbd5e1" font-size="7.2">• Si 기판과의 거대한 격자 불일치(Lattice Mismatch 4~8%)</text>
      <text x="18" y="121" fill="#cbd5e1" font-size="7.2">• 계면 트랩 밀도(D_it) ➔ 완충층(Buffer) 에피 성장 필수</text>
      <text x="12" y="140" fill="#fde047" font-size="7.5" font-weight="800">➔ 이것을 양산화할 유일한 도구가 바로 MOCVD!</text>
    </g>
  </g>

  <!-- PANEL B: MOCVD Working Principle & Epitaxy -->
  <g transform="translate(335, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) MOCVD 단결정 에피택시 메커니즘</text>

    <!-- Chamber Schematic -->
    <g transform="translate(15, 38)">
      <rect width="280" height="195" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">유기금속(MO) + 수소화물 ➔ 단결정 박막 성장</text>

      <!-- Gas Showerhead / Injector -->
      <rect x="25" y="28" width="230" height="18" rx="3" fill="#0284c7" stroke="#38bdf8"/>
      <text x="35" y="41" fill="#fff" font-size="7.2" font-weight="800">MO 전구체 (TMGa, TMA, TMIn) + Ⅴ족 가스 (AsH₃, PH₃)</text>

      <!-- Boundary layer & Chemical reactions -->
      <g transform="translate(25, 52)">
        <rect width="230" height="75" fill="#0f172a" stroke="#334155"/>
        <text x="10" y="16" fill="#f87171" font-size="7.5" font-weight="800">열분해 반응 (Pyrolysis): 500 ~ 1100℃</text>
        <text x="10" y="30" fill="#cbd5e1" font-size="6.8">Ga(CH₃)₃ (g) + AsH₃ (g) ➔ GaAs (단결정 박막) + 3 CH₄ (g) ↑</text>
        <path d="M 40 40 L 40 65" stroke="#34d399" stroke-width="1.8" marker-end="url(#arrowGreenM)"/>
        <path d="M 115 40 L 115 65" stroke="#34d399" stroke-width="1.8" marker-end="url(#arrowGreenM)"/>
        <path d="M 190 40 L 190 65" stroke="#34d399" stroke-width="1.8" marker-end="url(#arrowGreenM)"/>
        <text x="60" y="55" fill="#a7f3d0" font-size="6.5">표면 이동 및 원자격자 정렬 (Epitaxy)</text>
      </g>

      <!-- Wafer on Heated Susceptor -->
      <rect x="45" y="132" width="190" height="12" rx="2" fill="#38bdf8"/>
      <text x="85" y="141" fill="#000" font-size="7.5" font-weight="900">웨이퍼 기판 (Si / GaAs / SiC)</text>
      <rect x="25" y="146" width="230" height="18" rx="2" fill="#ef4444" stroke="#f87171"/>
      <text x="65" y="158" fill="#fff" font-size="7.5" font-weight="800">고온 서셉터 (Heated Susceptor 1000℃)</text>

      <text x="15" y="180" fill="#cbd5e1" font-size="7">• 회전 척(Rotation)으로 대면적 300mm 웨이퍼 두께 균일도 달성</text>
    </g>

    <!-- MBE vs MOCVD Comparison -->
    <g transform="translate(15, 242)">
      <rect width="280" height="163" rx="5" fill="#0b1329" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="8.8" font-weight="800">왜 MBE 대신 MOCVD로 가는가? (양산성의 승리)</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="7.5">• <strong>MBE (분자선 에피택시)</strong>:</text>
      <text x="18" y="48" fill="#fca5a5" font-size="7">- 초고진공(10⁻¹⁰ Torr), 원자빔 증발 ➔ 연구용 최고 품질</text>
      <text x="18" y="60" fill="#fca5a5" font-size="7">- 단점: 성장 속도 극느림(1㎛/h), 장비 유지보수 지옥, 양산 불가</text>
      <text x="12" y="78" fill="#38bdf8" font-size="7.8" font-weight="800">• <strong>MOCVD (유기금속 화학기상증착)</strong>:</text>
      <text x="18" y="92" fill="#34d399" font-size="7.2" font-weight="800">- 고속 성장(수~수십 ㎛/h) + 원자층 수준 계면 급준도</text>
      <text x="18" y="104" fill="#34d399" font-size="7.2" font-weight="800">- 12인치(300mm) 대구경 웨이퍼 다매엽 동시 양산 지원</text>
      <text x="18" y="118" fill="#cbd5e1" font-size="7.2">- 가스 유량(MFC) 제어만으로 합금 조성비(In, Ga, Al) 자유자재</text>
      <text x="12" y="136" fill="#fde047" font-size="7.8" font-weight="800">➔ "연구실 기술을 공장 대량 양산으로 이끈 유일한 기둥!"</text>
      <text x="12" y="150" fill="#94a3b8" font-size="7">• 글로벌 양산 리더: Aixtron(엑시트론), Veeco(비코)</text>
    </g>
  </g>

  <!-- PANEL C: 3 Future Visions & Nomenclature Guide -->
  <g transform="translate(660, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="12" font-weight="800">■ (C) MOCVD 3대 비전 &amp; 호칭 가이드</text>

    <!-- Nomenclature Box -->
    <g transform="translate(15, 38)">
      <rect width="270" height="105" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="16" fill="#fde047" font-size="8.5" font-weight="800">🗣️ '3-5족' 호칭 및 발음 가이드</text>
      <text x="10" y="32" fill="#38bdf8" font-size="7.5" font-weight="800">Q. 3-5족 반도체라고 해도 되나요?</text>
      <text x="14" y="46" fill="#34d399" font-size="7.5" font-weight="800">➔ 100% 가능하며 가장 표준적인 현업 표현입니다!</text>
      <text x="10" y="62" fill="#cbd5e1" font-size="7.2">• 구두 발음 1: <strong>'삼오족 반도체'</strong> (국내 엔지니어 90% 사용)</text>
      <text x="10" y="74" fill="#cbd5e1" font-size="7.2">• 구두 발음 2: <strong>'쓰리 파이브(Three-Five) 반도체'</strong> (글로벌 표준)</text>
      <text x="10" y="88" fill="#a7f3d0" font-size="7.2">• 최고 추천: <strong>'3-5족 화합물 반도체'</strong>로 서두를 열기!</text>
    </g>

    <!-- 3 Big Future Applications -->
    <g transform="translate(15, 150)">
      <rect width="270" height="255" rx="6" fill="#0b1329" stroke="#f59e0b"/>
      <text x="12" y="18" fill="#fbbf24" font-size="9" font-weight="800">🚀 MOCVD의 3대 미래 킬러 애플리케이션</text>

      <!-- Vision 1 -->
      <g transform="translate(10, 26)">
        <rect width="250" height="66" rx="4" fill="#1e293b"/>
        <text x="8" y="14" fill="#38bdf8" font-size="7.8" font-weight="800">1. 초고속 로직: InGaAs/Ge 이종 CFET</text>
        <text x="14" y="28" fill="#cbd5e1" font-size="7.2">• Si 기판 상부에 InGaAs(NMOS) + 하부에 Ge(PMOS)</text>
        <text x="14" y="40" fill="#cbd5e1" font-size="7.2">• 3D 스택 3차원 트랜지스터로 1nm 이하 노드 제패</text>
        <text x="14" y="54" fill="#34d399" font-size="7.5" font-weight="800">➔ 인텔, TSMC, imec이 로드맵에 공식 선언!</text>
      </g>

      <!-- Vision 2 -->
      <g transform="translate(10, 98)">
        <rect width="250" height="66" rx="4" fill="#1e293b"/>
        <text x="8" y="14" fill="#10b981" font-size="7.8" font-weight="800">2. 전력 반도체: GaN-on-Si 파워 소자</text>
        <text x="14" y="28" fill="#cbd5e1" font-size="7.2">• 전기차 온보드 차저, AI 데이터센터 48V 전력 변환</text>
        <text x="14" y="40" fill="#cbd5e1" font-size="7.2">• 실리콘 대비 전력 효율 10배, 스위칭 주파수 10배</text>
        <text x="14" y="54" fill="#fde047" font-size="7.5" font-weight="800">➔ GaN 에피 성장은 100% MOCVD가 독점 장악!</text>
      </g>

      <!-- Vision 3 -->
      <g transform="translate(10, 170)">
        <rect width="250" height="74" rx="4" fill="#1e293b"/>
        <text x="8" y="14" fill="#f87171" font-size="7.8" font-weight="800">3. 광반도체: 실리콘 포토닉스 &amp; Micro-LED</text>
        <text x="14" y="28" fill="#cbd5e1" font-size="7.2">• Si는 간접천이로 발광 불가 ➔ III-V(InP/GaAs) 광원 필수</text>
        <text x="14" y="40" fill="#cbd5e1" font-size="7.2">• AI 병목 극복할 CPO(Co-Packaged Optics) 빛 통신</text>
        <text x="14" y="54" fill="#cbd5e1" font-size="7.2">• 차세대 AR/VR용 초고밀도 Micro-LED 에피 성장</text>
        <text x="14" y="68" fill="#fde047" font-size="7.2" font-weight="800">➔ 실리콘 칩 위에 빛(Light)을 심는 핵심 인프라!</text>
      </g>
    </g>
  </g>

  <!-- Markers -->
  <defs>
    <marker id="arrowGreenM" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#34d399" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- SECTION 1: Nomenclature Guide -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. '3-5족 반도체'라고 불러도 될까? (면접 및 실무 표준 호칭 완벽 정리)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            결론부터 말씀드리면, <strong>"3-5족 반도체"라고 부르는 것은 100% 맞으며, 현업 엔지니어와 면접관들이 가장 자연스럽고 흔하게 사용하는 표준 구두 표현</strong>입니다. 전혀 걱정하지 않고 당당하게 말씀하셔도 좋습니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:800; margin-bottom:6px;">
              현업과 학계에서 사용하는 3대 표준 호칭과 추천 발음법
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.8; padding-left:20px; margin:0;">
              <li><strong>① "삼오족 화합물 반도체" (가장 추천하는 정석 표현)</strong>:
                <br>답변 서두를 시작할 때 <em>"실리콘의 한계를 극복하기 위한 3-5족(삼오족) 화합물 반도체 채널 기술은..."</em>처럼 풀네임으로 짚어주면 전공자로서의 깊이와 정확성을 즉시 어필할 수 있습니다.
              </li>
              <li><strong>② "삼오족 반도체" (가장 일상적인 현업 실무 표현)</strong>:
                <br>대화가 이어질 때는 굳이 '화합물'을 매번 붙이지 않고 <em>"3-5족 반도체 소재인 InGaAs나 InAs의 경우..."</em>라고 편하게 축약해도 면접관 누구나 찰떡같이 알아듣습니다.
              </li>
              <li><strong>③ "쓰리 파이브(Three-Five) 반도체" (글로벌 기업 / 연구소 표준)</strong>:
                <br>삼성전자 반도체연구소, SK하이닉스 선행소자팀, TSMC, imec 등 첨단 R&D 현장이나 외국계 장비사(어플라이드, 엑시트론 등)에서는 로마자 $\text{III-V}$를 영어 그대로 **'쓰리 파이브 반도체'** 혹은 **'쓰리 파이브 머티리얼'**이라고 부르는 경우가 매우 흔합니다.
              </li>
            </ul>
          </div>
        </div>

        <!-- SECTION 2: Physics of High Mobility Channel -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 왜 3-5족과 Ge인가? (고이동도 채널의 물리적 본질)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            질문자님께서 제시하신 문장에 핵심 통찰이 완벽히 담겨 있습니다. 
            실리콘(Si) 기반 CMOS는 3nm, 2nm GAA(나노시트)를 거치며 게이트 전압($V_{DD}$)을 더 이상 낮추지 못하는 **볼츠만 트래픽($60\,\text{mV/dec}$ 한계)**과 포화 전류 정체에 직면했습니다. 이를 돌파하기 위해 **채널 소재 자체를 실리콘에서 '전자의 고속도로(3-5족)'와 '정공의 고속도로(Ge)'로 바꾸는 패러다임 시프트**가 연구되고 있습니다.
          </p>

          <div style="overflow-x:auto; margin-bottom:16px;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">채널 타깃</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">기존 실리콘 (Si)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">차세대 고이동도 소재</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">물리적 향상 효과</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">NMOS 채널<br>(전자 이동도 $\mu_n$)</td>
                  <td style="padding:10px 14px;">$1,400\,\text{cm}^2/\text{V}\cdot\text{s}$</td>
                  <td style="padding:10px 14px; font-weight:800; color:#34d399;"><strong>InGaAs</strong> ($12,000$)<br><strong>InAs</strong> ($33,000\,\text{cm}^2/\text{V}\cdot\text{s}$)</td>
                  <td style="padding:10px 14px; font-weight:800; color:#fde047;"><strong>10배 ~ 25배 폭증!</strong><br>유효 질량($m^* \approx 0.023 m_0$)이 실리콘($0.19 m_0$)의 1/8 수준으로 빛의 속도 주행</td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#f59e0b;">PMOS 채널<br>(정공 이동도 $\mu_p$)</td>
                  <td style="padding:10px 14px;">$450\,\text{cm}^2/\text{V}\cdot\text{s}$<br>(CMOS 최악의 병목)</td>
                  <td style="padding:10px 14px; font-weight:800; color:#34d399;"><strong>Ge (게르마늄)</strong><br>($1,900\,\text{cm}^2/\text{V}\cdot\text{s}$)</td>
                  <td style="padding:10px 14px; font-weight:800; color:#fde047;"><strong>4.4배 향상!</strong><br>PMOS 채널 폭을 억지로 넓힐 필요 없이 NMOS와 1:1 대칭 고속 스위칭 구현</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div style="background:#1e293b; padding:16px 20px; border-radius:8px; margin-bottom:16px;">
            <h4 style="color:#fde047; font-size:0.95rem; font-weight:800; margin-bottom:6px;">
              💡 고이동도가 소자 성능(Performance)을 폭발시키는 원리
            </h4>
            <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
              전류 공식 $I_{on} \propto \mu \cdot C_{ox} (V_{GS} - V_{th})^2$에서, 이동도($\mu$)가 10~25배 커지면 <strong>게이트 전압($V_{GS}$)을 $0.5\,\text{V}$ 이하로 극단적으로 낮추어도 실리콘보다 훨씬 큰 구동 전류를 뿜어낼 수 있습니다.</strong>
              소비 전력은 전압의 제곱($P \propto V^2$)에 비례하므로, 칩 발열을 획기적으로 줄이면서도 테라헤르츠(THz)급 연산 속도를 달성할 수 있습니다.
            </p>
          </div>
        </div>

        <!-- SECTION 3: What is MOCVD and Why It Matters -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. MOCVD(유기금속 화학기상증착)의 본질과 독보적 양산성
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            3-5족 화합물이나 Ge 같은 이종 물질은 실리콘 기판 위에 증착할 때 격자 상수 불일치로 인해 결정 결함(Dislocation)이 폭발합니다. 이를 극복하고 <strong>원자 격자가 한 치의 흐트러짐 없이 정렬된 완벽한 단결정 박막을 키워내는 공정을 '에피택시(Epitaxy)'</strong>라고 하며, 이를 현실에서 대량 양산할 수 있는 유일한 장비가 바로 **MOCVD**입니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:800; margin-bottom:6px;">
              MOCVD (Metal-Organic Chemical Vapor Deposition)의 반응 원리
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              • <strong>전구체</strong>: 유기금속(MO, 예: 트리메틸갈륨 $\text{TMGa}$, 트리메틸인듐 $\text{TMIn}$)과 5족 수소화물 가스(아르신 $\text{AsH}_3$, 포스핀 $\text{PH}_3$)를 고온 챔버에 주입합니다.
              <br>• <strong>반응식</strong>: $\text{Ga}(\text{CH}_3)_3 + \text{AsH}_3 \xrightarrow{600\sim 800^\circ\text{C}} \text{GaAs (단결정)} + 3\,\text{CH}_4 \uparrow$
              <br>• 기체 분자가 가열된 웨이퍼 표면에서 열분해되면서 메탄 가스는 배출되고, 갈륨과 비소 원자가 기판 격자를 따라 한 층씩 자라나 **원자층 수준의 정밀한 단결정 이종접합(Heterojunction)**을 형성합니다.
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #f59e0b; padding:16px 20px; border-radius:0 8px 8px 0;">
            <h4 style="color:#fbbf24; font-size:1rem; font-weight:800; margin-bottom:6px;">
              MBE(분자선 에피택시) 대비 MOCVD가 선택된 결정적 이유
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              • <strong>MBE</strong>는 초고진공($10^{-10}\,\text{Torr}$)에서 금속을 증발시켜 원자빔을 쏘므로 품질은 극상이지만, 성장 속도가 너무 느리고($\sim 1\,\mu\text{m/h}$) 대구경 12인치(300mm) 웨이퍼 양산이 불가능합니다.
              <br>• 반면 <strong>MOCVD</strong>는 기체 유량 제어로 수 $\mu\text{m/h}$의 고속 성장이 가능하며, 여러 장의 300mm 웨이퍼를 동시에 회전시키며 균일하게 양산(Multi-wafer Throughput)할 수 있는 **지구상 유일한 화합물 반도체 대량 양산 플랫폼**입니다.
            </p>
          </div>
        </div>

        <!-- SECTION 4: 3 Big Future Visions of MOCVD -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#c084fc; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. MOCVD의 3대 미래 비전 (Beyond Silicon의 게임 체인저)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            현재 글로벌 반도체 업계(TSMC, Intel, 삼성전자, imec)에서 MOCVD를 주목하는 미래 비전은 크게 3가지 축으로 전개되고 있습니다:
          </p>

          <ol style="color:#cbd5e1; font-size:0.92rem; line-height:1.85; padding-left:20px; margin:0;">
            <li><strong style="color:#38bdf8;">초미세 로직 CFET (3D Complementary FET) 이종 집적</strong>:
              <br>미래 1nm 이하에서는 NMOS 위에 PMOS를 3차원으로 수직 적층하는 CFET 구조로 진화합니다. 이때 하부 PMOS는 Ge으로, 상부 NMOS는 InGaAs 3-5족으로 에피 성장시키는 초고속 이종 채널 스택 제조에 MOCVD가 필수적으로 요구됩니다.
            </li>
            <li><strong style="color:#10b981;">차세대 전력 반도체 (GaN-on-Si Power Devices)</strong>:
              <br>전기차(EV) 인버터와 AI 데이터센터 전력 공급 장치에서 실리콘 파워 소자를 빠르게 대체하고 있는 질화갈륨(GaN) 반도체는 <strong>100% MOCVD 에피 공정으로 제조</strong>됩니다. 고전압, 고효율, 고주파 전력 혁명의 핵심 인프라입니다.
            </li>
            <li><strong style="color:#f87171;">실리콘 포토닉스 (Silicon Photonics) &amp; CPO 광통신</strong>:
              <br>실리콘은 간접천이 밴드갭을 가져 스스로 빛을 낼 수 없습니다. AI 시대의 전기 배선 병목을 해결하기 위한 '빛(광) 인터커넥트'인 CPO 기술을 구현하려면, 실리콘 칩 위에 직접천이형 3-5족 레이저 다이오드(InP, GaAs)를 MOCVD로 에피 성장시켜 집적해야만 합니다.
            </li>
          </ol>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 97 topics (q-97 down to q-01) by +1
    for old_n in range(97, 0, -1):
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

    # Step 4: Update header description to 98 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 'MOCVD의 비전과 3-5족·Ge 채널(Q01)'이 위치하며, 총 98개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 MOCVD Vision topic!")
