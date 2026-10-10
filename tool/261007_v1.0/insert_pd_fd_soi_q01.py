# -*- coding: utf-8 -*-
"""
insert_pd_fd_soi_q01.py
사용자 질문: "soi에서 부분공핍과 완전공핍이 뜻하는건뭐야?"
대시보드 최상단 Q01로 신규 추가하고, 기존 81개 질문을 Q02~Q82로 시프트 (총 82개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (첨단 SOI 소자 물리 · PD vs FD)",
    "title": "SOI에서 부분 공핍(PD-SOI)과 완전 공핍(FD-SOI)이 뜻하는 것은 무엇일까? (Tsi vs Wdep, 플로팅 바디, 킹크 효과, 무도핑 혁명)",
    "nav_title": "SOI에서 부분공핍(PD)과 완전공핍(FD)이 뜻하는 것은? (원리, FBE, Kink)",
    "summary": [
        "<strong>1. 물리적 정의의 절대 기준: 실리콘 박막 두께($T_{si}$) vs 최대 공핍층 폭($W_{dep,max}$)</strong>: 게이트 전압 인가 시 수직으로 뻗어나가는 공핍층 폭과 상부 실리콘 박막의 두께 관계에 의해 결정됩니다.",
        "<strong>2. 부분 공핍 (PD-SOI, Partially Depleted)</strong>: <strong>$T_{si} > W_{dep,max}$</strong> ($T_{si} \\approx 50 \\sim 150\\text{nm}$). 실리콘 층이 두꺼워 공핍층이 바닥(BOX 산화막)에 닿지 못하고, 하부에 <strong>전하가 고이는 중성 실리콘 영역(Neutral Floating Body)</strong>이 남아있습니다. 이로 인해 정공($h^+$)이 축적되어 문턱전압이 떨어지고 전류가 비정상적으로 꺾여 오르는 <strong>플로팅 바디 효과(FBE) 및 킹크 효과(Kink Effect)</strong>가 발생하는 한계가 있습니다.",
        "<strong>3. 완전 공핍 (FD-SOI, Fully Depleted)</strong>: <strong>$T_{si} < W_{dep,max}$</strong> ($T_{si} \\approx 5 \\sim 7\\text{nm}$). 실리콘 박막을 극도로 얇게 깎아, <strong>공핍층이 바닥 BOX 산화막까지 100% 관통하여 채널 바디 전체가 완전히 비워진 상태</strong>입니다. 중성 영역 자체가 사라져 플로팅 바디/킹크 효과가 원천 박멸됩니다.",
        "<strong>4. FD-SOI의 3대 결정적 우위</strong>: ① 기생 공핍 커패시턴스가 극소화($C_{dep} \\approx 0$)되어 <strong>서브스레시홀드 스윙이 이상치인 $SS \\approx 60\\text{mV/dec}$로 복원</strong>됩니다. ② 단채널을 구조적으로 막으므로 <strong>무도핑 채널(Undoped)</strong>을 적용해 캐리어 이동도($\\mu$)가 폭등하고 무작위 도펀트 요동(RDF)이 0%가 됩니다. ③ BOX 하부 기판 전압으로 문턱전압을 실시간 튜닝하는 <strong>백 바이어스(Back Biasing)</strong> 초저전력 제어가 가능합니다."
    ],
    "svg_title": "📊 [PD-SOI vs FD-SOI 완전 해부] (A) 실리콘 두께와 공핍층 단면 비교 | (B) 플로팅 바디 효과와 킹크(Kink) 곡선 | (C) 소자 특성 및 백바이어스 비교",
    "svg": """<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Structural Cross Section Comparison -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 물리 구조: T_si vs W_dep 비교</text>

    <!-- Sub-case 1: PD-SOI -->
    <g transform="translate(15, 42)">
      <rect width="270" height="135" rx="5" fill="#1e293b" stroke="#f59e0b"/>
      <text x="10" y="16" fill="#fbbf24" font-size="9" font-weight="800">1. PD-SOI (부분 공핍): T_si &gt; W_dep</text>
      <!-- Gate -->
      <rect x="90" y="24" width="90" height="10" fill="#64748b" rx="1"/>
      <text x="122" y="32" fill="#fff" font-size="7">Gate</text>
      <!-- S / D -->
      <rect x="25" y="34" width="50" height="42" fill="#f59e0b" rx="1"/>
      <text x="35" y="58" fill="#000" font-size="7.5" font-weight="800">Source</text>
      <rect x="195" y="34" width="50" height="42" fill="#f59e0b" rx="1"/>
      <text x="207" y="58" fill="#000" font-size="7.5" font-weight="800">Drain</text>
      <!-- Depletion layer (partial) -->
      <rect x="75" y="34" width="120" height="18" fill="#0284c7" opacity="0.6"/>
      <text x="95" y="47" fill="#fff" font-size="7.5" font-weight="800">공핍층 (W_dep)</text>
      <!-- Neutral Region (Floating Body) -->
      <rect x="75" y="52" width="120" height="24" fill="#ef4444" opacity="0.6"/>
      <text x="82" y="67" fill="#fef08a" font-size="8" font-weight="800">⚠️ 중성 영역 (Floating Body)</text>
      <!-- BOX -->
      <rect x="25" y="76" width="220" height="22" fill="#334155" stroke="#475569" stroke-dasharray="2,2"/>
      <text x="75" y="91" fill="#94a3b8" font-size="7.5">매립 산화막 (Buried Oxide, BOX)</text>
      <text x="10" y="112" fill="#fca5a5" font-size="7.5">• 두꺼운 실리콘 (T_si ≈ 100nm) ➔ 공핍층이 바닥 못 닿음</text>
      <text x="10" y="126" fill="#ef4444" font-size="7.8" font-weight="700">➔ 정공(h+)이 갇히며 플로팅 바디 효과(FBE) 발생!</text>
    </g>

    <!-- Sub-case 2: FD-SOI -->
    <g transform="translate(15, 188)">
      <rect width="270" height="135" rx="5" fill="#1e293b" stroke="#10b981"/>
      <text x="10" y="16" fill="#34d399" font-size="9" font-weight="800">2. FD-SOI (완전 공핍): T_si &lt; W_dep</text>
      <!-- Gate -->
      <rect x="90" y="24" width="90" height="10" fill="#38bdf8" rx="1"/>
      <text x="122" y="32" fill="#000" font-size="7">Gate</text>
      <!-- S / D -->
      <rect x="25" y="34" width="50" height="16" fill="#f59e0b" rx="1"/>
      <text x="35" y="46" fill="#000" font-size="7.5" font-weight="800">Source</text>
      <rect x="195" y="34" width="50" height="16" fill="#f59e0b" rx="1"/>
      <text x="207" y="46" fill="#000" font-size="7.5" font-weight="800">Drain</text>
      <!-- Fully Depleted Channel -->
      <rect x="75" y="34" width="120" height="16" fill="#10b981" rx="1"/>
      <text x="82" y="46" fill="#fff" font-size="7.5" font-weight="800">100% 완전 공핍층! (T_si ≈ 6nm)</text>
      <!-- BOX -->
      <rect x="25" y="50" width="220" height="35" fill="#334155" stroke="#10b981" stroke-dasharray="2,2"/>
      <text x="65" y="72" fill="#38bdf8" font-size="8.5" font-weight="700">얇은 매립 산화막 (UTBOX ≈ 25nm)</text>
      <!-- Substrate for Back Bias -->
      <rect x="25" y="85" width="220" height="15" fill="#1e293b"/>
      <text x="75" y="96" fill="#cbd5e1" font-size="7">Back-Gate 기판 (V_back 조절)</text>
      <text x="10" y="112" fill="#a7f3d0" font-size="7.5">★ 바디 전체가 100% 비워짐! 중성 영역 = 0</text>
      <text x="10" y="126" fill="#34d399" font-size="7.8" font-weight="700">➔ FBE / Kink 원천 박멸, 완벽한 게이트 제어권 장악</text>
    </g>

    <!-- Formula Box -->
    <rect x="15" y="334" width="270" height="72" rx="6" fill="#0b1329" stroke="#334155"/>
    <text x="22" y="354" fill="#38bdf8" font-size="8.8" font-weight="800">공학적 기준 조건 공식:</text>
    <text x="22" y="372" fill="#fde047" font-size="8.2">• PD-SOI: T_si &gt; W_dep,max ➔ 중성 플로팅 바디 잔류</text>
    <text x="22" y="389" fill="#34d399" font-size="8.2" font-weight="700">• FD-SOI: T_si &lt; W_dep,max ➔ 바디 전체 100% 완전 공핍화</text>
  </g>

  <!-- PANEL B: Floating Body Effect and Kink Phenomenon -->
  <g transform="translate(340, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 플로팅 바디 효과(FBE)와 킹크(Kink) 곡선</text>

    <!-- Kink Effect I-V Curve Graph -->
    <g transform="translate(15, 42)">
      <rect width="280" height="165" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="9.5" font-weight="800">I_D - V_DS 출력 특성 곡선의 킹크 현상</text>
      <!-- Axes -->
      <line x1="35" y1="135" x2="255" y2="135" stroke="#64748b" stroke-width="1.5"/>
      <text x="235" y="148" fill="#94a3b8" font-size="8">V_DS</text>
      <line x1="35" y1="135" x2="35" y2="30" stroke="#64748b" stroke-width="1.5"/>
      <text x="18" y="38" fill="#94a3b8" font-size="8">I_D</text>

      <!-- Normal / FD-SOI curve (Flat saturation) -->
      <path d="M 35 135 Q 60 75 110 75 L 245 75" fill="none" stroke="#10b981" stroke-width="2.5"/>
      <text x="155" y="68" fill="#34d399" font-size="8" font-weight="700">FD-SOI: 정상 포화 곡선</text>

      <!-- PD-SOI curve with KINK -->
      <path d="M 35 135 Q 60 75 110 75 L 140 75 Q 165 72 185 52 L 245 48" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4,2"/>
      <!-- Circle on Kink point -->
      <circle cx="170" cy="65" r="5" fill="#f59e0b"/>
      <text x="145" y="44" fill="#ef4444" font-size="8" font-weight="800">⚡ 킹크(Kink) 발생점!</text>
      <text x="145" y="98" fill="#fca5a5" font-size="7.5">V_B 상승 ➔ V_th 강하 ➔ I_D 급증</text>

      <text x="12" y="156" fill="#cbd5e1" font-size="7.5">• 드레인 전압 상승 시 충돌 이온화로 생성된 정공 축적</text>
    </g>

    <!-- Step-by-Step FBE Mechanism -->
    <g transform="translate(15, 218)">
      <rect width="280" height="188" rx="6" fill="#0b1329" stroke="#334155"/>
      <text x="12" y="18" fill="#38bdf8" font-size="9" font-weight="800">■ PD-SOI 플로팅 바디 4단계 악순환 시퀀스:</text>

      <text x="12" y="38" fill="#cbd5e1" font-size="8.2">1. <strong>충돌 이온화 (Impact Ionization)</strong>:</text>
      <text x="20" y="52" fill="#94a3b8" font-size="7.6">드레인 고전계에서 전자-정공 쌍(EHP) 대량 생성</text>

      <text x="12" y="70" fill="#cbd5e1" font-size="8.2">2. <strong>정공(Hole) 갇힘 (Charge Accumulation)</strong>:</text>
      <text x="20" y="84" fill="#94a3b8" font-size="7.6">바디 접지가 없어 정공이 하부 중성 영역에 고임</text>

      <text x="12" y="102" fill="#cbd5e1" font-size="8.2">3. <strong>바디 전위 상승 ➔ 문턱전압 강하</strong>:</text>
      <text x="20" y="116" fill="#fca5a5" font-size="7.6">V_body ↑ ➔ 기판 바이어스 효과로 V_th ↓ 급락!</text>

      <text x="12" y="134" fill="#ef4444" font-size="8.2" font-weight="700">4. <strong>전류 왜곡(Kink) &amp; 이력 현상(History Effect)</strong>:</text>
      <text x="20" y="148" fill="#fca5a5" font-size="7.6">전류가 꺾여 솟구치고, 이전 동작 상태에 따라 지연 시간 변동!</text>

      <text x="12" y="172" fill="#34d399" font-size="8.2" font-weight="800">★ FD-SOI는 중성 바디가 0이므로 이 모든 악순환 100% 종식!</text>
    </g>
  </g>

  <!-- PANEL C: FD-SOI Advantages and Back Biasing Tuning -->
  <g transform="translate(670, 20)">
    <rect width="290" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) FD-SOI 성능 우위 &amp; 백 바이어스 혁신</text>

    <!-- SS Restoration Box -->
    <g transform="translate(15, 42)">
      <rect width="260" height="110" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="12" y="18" fill="#fde047" font-size="9" font-weight="800">1. 서브스레시홀드 스윙(SS) 이상치 복원</text>
      <text x="12" y="36" fill="#ffffff" font-size="9">SS = 60 · [ 1 + (C_dep / C_ox) ]</text>
      <text x="12" y="54" fill="#cbd5e1" font-size="8">• PD-SOI: 부분 공핍 커패시턴스로 SS ≈ 75~85 mV/dec</text>
      <text x="12" y="70" fill="#34d399" font-size="8.5" font-weight="700">• FD-SOI: 바디 완전 공핍 ➔ C_dep ≈ 0 수렴!</text>
      <text x="12" y="88" fill="#86efac" font-size="8.5" font-weight="800">➔ SS ≈ 60 mV/dec (이상적 한계치) 달성!</text>
      <text x="12" y="102" fill="#bae6fd" font-size="7.5">오프 누설전류(I_off) 수천 분의 일로 급감</text>
    </g>

    <!-- Undoped Channel & RDF Elimination -->
    <g transform="translate(15, 160)">
      <rect width="260" height="110" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="9" font-weight="800">2. 무도핑 채널(Undoped) 실현</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="8">• 박막 바디 기하 구조로 SCE 완벽 통제</text>
      <text x="12" y="52" fill="#cbd5e1" font-size="8">➔ 채널에 불순물 도핑 제로 (무도핑 채널!)</text>
      <text x="12" y="70" fill="#fde047" font-size="8.5" font-weight="700">① 쿨롱 산란 제거: 전자/정공 이동도(μ) 급상승</text>
      <text x="12" y="88" fill="#fde047" font-size="8.5" font-weight="700">② RDF(무작위 도펀트 요동) 산포 오차 0% 박멸</text>
      <text x="12" y="102" fill="#a7f3d0" font-size="7.5">초미세 공정 수율 및 소자 균일도 극대화</text>
    </g>

    <!-- Back Biasing Revolutionary Control -->
    <g transform="translate(15, 278)">
      <rect width="260" height="128" rx="6" fill="#0b1329" stroke="#38bdf8"/>
      <text x="12" y="18" fill="#38bdf8" font-size="9" font-weight="800">3. 백 바이어스 (Back Biasing) 전압 튜닝</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="7.8">얇은 BOX(25nm)를 통해 기판 전압으로 Vt 실시간 제어:</text>

      <rect x="10" y="46" width="240" height="34" rx="3" fill="#1e293b" stroke="#34d399"/>
      <text x="16" y="60" fill="#34d399" font-size="8" font-weight="700">■ 순방향 (Forward Back Bias, FBB):</text>
      <text x="16" y="73" fill="#cbd5e1" font-size="7.5">Vt 낮춤 ➔ 동작 속도 2배 가속 (터보 부스트 모드)</text>

      <rect x="10" y="85" width="240" height="34" rx="3" fill="#1e293b" stroke="#38bdf8"/>
      <text x="16" y="99" fill="#38bdf8" font-size="8" font-weight="700">■ 역방향 (Reverse Back Bias, RBB):</text>
      <text x="16" y="112" fill="#cbd5e1" font-size="7.5">Vt 높임 ➔ 누설전류 99% 차단 (초저전력 슬립 모드)</text>
    </g>
  </g>
</svg>""",
    "lecture": r"""
        <!-- Section 1: Clear Concept & Definitions -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 부분 공핍(PD-SOI)과 완전 공핍(FD-SOI)의 핵심 물리적 정의
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            SOI(Silicon-On-Insulator) 기술은 실리콘 기판 위에 절연막인 <strong>매립 산화막(BOX: Buried Oxide, $\text{SiO}_2$)</strong>을 깔고, 그 위에 얇은 활성 실리콘 박막(Top Silicon Film, 두께 $T_{si}$)을 얹어 트랜지스터를 제작하는 첨단 구조입니다.<br>
            이때 <strong>'부분 공핍'</strong>과 <strong>'완전 공핍'</strong>을 가르는 유일하고 절대적인 물리적 기준은 바로 <strong>"상부 실리콘 박막 두께($T_{si}$)가 게이트가 형성할 수 있는 최대 공핍층 폭($W_{dep,max}$)보다 두꺼운가, 얇은가?"</strong>입니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:18px;">
            <h4 style="color:#38bdf8; font-size:1.05rem; font-weight:800; margin-bottom:8px;">💡 한 줄 직관 판정 공식</h4>
            <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:18px;">
              <li><strong>PD-SOI (Partially Depleted SOI, 부분 공핍)</strong> : <strong>$T_{si} > W_{dep,max}$</strong><br>
                실리콘 박막이 두꺼워($T_{si} \approx 50 \sim 150\,\text{nm}$) 게이트 전압을 아무리 걸어도 공핍층이 바닥(BOX 산화막)에 닿지 못하고, 하부에 <strong>공핍되지 않은 중성 실리콘 영역(Floating Body)</strong>이 남아있는 상태입니다.
              </li>
              <li><strong>FD-SOI (Fully Depleted SOI, 완전 공핍)</strong> : <strong>$T_{si} < W_{dep,max}$</strong><br>
                실리콘 박막을 극도로 얇게 깎아($T_{si} \approx 5 \sim 7\,\text{nm}$) 게이트 전압 인가 시 <strong>공핍층이 바닥 BOX 산화막까지 100% 관통하여 채널 바디 전체가 완전히 비워진(Fully Depleted) 상태</strong>입니다.
              </li>
            </ul>
          </div>
        </div>

        <!-- Section 2: In-Depth PD-SOI & Floating Body Issues -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 부분 공핍(PD-SOI)의 치명적 한계: 플로팅 바디 효과(FBE)와 킹크(Kink) 현상
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            초기 반도체 업계(1990~2000년대)는 극도로 얇은 실리콘 웨이퍼를 만들기 어려워 두께가 두꺼운 <strong>PD-SOI</strong>를 주로 사용했습니다. 하지만 PD-SOI에는 치명적인 소자 결함들이 뒤따랐습니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#f87171; margin:14px 0 8px;">■ 플로팅 바디 효과 (Floating Body Effect, FBE)</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:10px;">
            벌크 Si에서는 기판 바닥이 접지(Ground)에 연결되어 있어 전위가 안정적입니다. 하지만 PD-SOI에서는 하부의 중성 실리콘 영역이 사방이 절연막(BOX와 필드 산화막)으로 둘러싸여 전기적으로 둥둥 떠 있는 <strong>'플로팅 바디(Floating Body)'</strong> 상태가 됩니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#fde047; margin:14px 0 8px;">■ 킹크 효과 (Kink Effect)의 물리 발생 과정</h4>
          <ol style="color:#cbd5e1; font-size:0.9rem; line-height:1.8; padding-left:22px; margin-bottom:12px;">
            <li><strong>충돌 이온화 (Impact Ionization)</strong>: 높은 드레인 전압($V_{DS}$) 하에서 전자가 드레인 근처의 강한 전계에 의해 실리콘 원자와 충돌하며 전자-정공 쌍(EHP)을 생성합니다.</li>
            <li><strong>정공 축적 (Hole Accumulation)</strong>: 전자는 드레인으로 쉽게 빠져나가지만, 생성된 정공($h^+$)들은 갈 곳이 없어 하부의 중성 플로팅 바디 영역에 갇혀 축적됩니다.</li>
            <li><strong>바디 전위 상승 ($V_B \uparrow$)</strong>: 양전하인 정공이 쌓이면서 바디 전위가 양(+)의 방향으로 상승합니다.</li>
            <li><strong>문턱전압 강하 ($V_{th} \downarrow$) 및 킹크 발생</strong>: 기판 바이어스 효과(Body Effect)에 의해 문턱전압이 갑자기 뚝 떨어지며, 드레인 전류($I_D$) 곡선이 평탄하게 포화되지 못하고 **중간에서 비정상적으로 꺾여 솟구치는 킹크(Kink) 현상**이 발생합니다.</li>
            <li><strong>이력 현상 (History Effect)</strong>: 트랜지스터가 이전에 켜져 있었는지 꺼져 있었는지에 따라 바디에 축적된 전하량이 달라져 회로의 스위칭 지연 시간(Delay)이 매번 바뀌는 치명적인 불안정성을 초래합니다.</li>
          </ol>
        </div>

        <!-- Section 3: In-Depth FD-SOI Revolution -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 완전 공핍(FD-SOI)의 위대한 혁신: 왜 현대 반도체는 FD-SOI로 가는가?
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            실리콘 박막 두께를 원자 단위로 제어할 수 있는 스마트 컷(Smart Cut) 기술이 완성되면서, 바디 두께를 $5 \sim 7\,\text{nm}$로 극도로 얇게 만든 <strong>FD-SOI</strong>가 탄생하였습니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:800; margin-bottom:8px;">🚀 FD-SOI가 이룩한 4대 기술 혁명</h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.8; padding-left:18px;">
              <li><strong>1. 플로팅 바디 & 킹크 효과 100% 원천 박멸</strong>: 정공이 고일 수 있는 중성 영역(Neutral Region) 자체가 물리적으로 존재하지 않으므로, 충돌 이온화가 일어나도 정공이 축적되지 않고 소스로 즉시 빠져나가 킹크 효과와 이력 현상이 완벽히 소멸합니다.</li>
              <li><strong>2. 서브스레시홀드 스윙 이상치 복원 ($SS \approx 60\,\text{mV/dec}$)</strong>: 바디 전체가 공핍화되어 게이트가 체감하는 기생 공핍 커패시턴스가 거의 0에 수렴($C_{dep} \approx 0$)하므로, 상온 열역학 한계치인 $60\,\text{mV/dec}$의 칼날 같은 온/오프 스위칭을 달성하여 오프 누설전류를 극소화합니다.</li>
              <li><strong>3. 무도핑 채널(Undoped Channel) 실현</strong>: 박막의 기하학적 구조만으로 단채널 효과를 100% 차단하므로 채널에 불순물 도핑을 할 필요가 없습니다. 쿨롱 산란이 사라져 전자 이동도($\mu$)가 급상승하고, 나노 공정 최대의 적인 무작위 도펀트 요동(RDF) 불량이 0%가 됩니다.</li>
              <li><strong>4. 초저전력 백 바이어스 (Back Biasing) 제어</strong>: 얇은 매립 산화막(UTBOX, 약 $25\,\text{nm}$) 하부의 기판 전압을 조절하여, 전자기기가 고성능이 필요할 때는 문턱전압을 낮춰 동작 속도를 2배 높이고(Forward Back Bias), 대기 상태일 때는 문턱전압을 높여 누설전류를 99% 잠그는(Reverse Back Bias) 동적 튜닝이 가능합니다.</li>
            </ul>
          </div>
        </div>

        <!-- Section 4: Summary Table -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.15rem; font-weight:800; color:#e2e8f0; margin-bottom:12px;">
            4. PD-SOI vs FD-SOI 핵심 요약 비교 정리표
          </h3>
          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">비교 항목</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">부분 공핍 (PD-SOI)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">완전 공핍 (FD-SOI)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">물리적 의미 및 차이점</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">두께 조건식</td>
                  <td style="padding:10px 14px; color:#f59e0b;">$T_{si} > W_{dep,max}$ ($50 \sim 150\,\text{nm}$)</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">$T_{si} < W_{dep,max}$ ($5 \sim 7\,\text{nm}$)</td>
                  <td style="padding:10px 14px;">공핍층이 바닥 BOX에 닿는가 여부</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#f87171;">중성 바디 영역</td>
                  <td style="padding:10px 14px; color:#ef4444; font-weight:700;">존재함 (Floating Body)</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">물리적으로 완전 소멸 (None)</td>
                  <td style="padding:10px 14px;">정공이 갇힐 공간의 유무</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fbbf24;">플로팅 바디 / 킹크 효과</td>
                  <td style="padding:10px 14px; color:#ef4444;">심각함 (Kink, History Effect)</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">원천 박멸 (0%)</td>
                  <td style="padding:10px 14px;">전류 왜곡 및 지연 시간 산포 발생 여부</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">서브스레시홀드 스윙 (SS)</td>
                  <td style="padding:10px 14px;">$SS \approx 75 \sim 85\,\text{mV/dec}$</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">$SS \approx 60\,\text{mV/dec}$ (이상치)</td>
                  <td style="padding:10px 14px;">$C_{dep} \approx 0$ 달성으로 스위칭 칼날화</td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#10b981;">채널 도핑 여부</td>
                  <td style="padding:10px 14px;">도핑 필수 (불순물 산란, RDF)</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">무도핑 채널 (Undoped)</td>
                  <td style="padding:10px 14px;">이동도 $\mu$ 극대화 및 공정 산포 0%</td>
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

    # Step 1: Shift existing 81 topics (q-81 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(81, 0, -1):
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

    # Step 4: Update header description to 82 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 'SOI에서 부분공핍(PD)과 완전공핍(FD)이 뜻하는 것은? (원리, FBE, Kink)'이 위치하며, 총 82개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 PD-SOI vs FD-SOI topic!")
