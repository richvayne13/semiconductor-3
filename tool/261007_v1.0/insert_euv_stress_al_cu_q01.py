# -*- coding: utf-8 -*-
"""
insert_euv_stress_al_cu_q01.py
사용자 질문:
"euv 장비광학계가 미러로만 구성된 이유
박막응력이란 무엇이고 이를 제어하는 방식은 무엇인가
알루미늄과 구리를 사용했을 때 장단점"

대시보드 최상단 Q01로 신규 추가하고, 기존 92개 질문을 Q02~Q93으로 시프트 (총 93개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (반도체 3대 핵심 현안 · EUV 반사 광학계 / 박막 응력 제어 / Al vs Cu 배선 비교)",
    "title": "EUV 광학계의 반사 미러 전용 이유, 박막 응력(Stress) 제어 원리, Al vs Cu 배선 장단점 완전 정복",
    "nav_title": "EUV 미러 광학계 · 박막 응력 제어 · Al vs Cu 배선",
    "summary": [
        "<strong>1. EUV(13.5nm) 광학계가 반사 미러로만 구성된 이유</strong>: 13.5nm 극자외선은 광자 에너지가 $91.8\\,\\text{eV}$로 극도로 높아 유리(석영), 공기 등 모든 물질에 100% 흡수되고 굴절률 차이($n \\approx 1$)가 없어 굴절 렌즈가 원천 불가능합니다. 따라서 초고진공에서 Mo/Si(40~50쌍) 브래그 다층 박막의 보강 간섭 반사(반사율 약 68%) 미러 10여 개를 조합한 반사 광학계만을 사용합니다.",
        "<strong>2. 박막 응력(Thin Film Stress)의 본질과 2대 분류</strong>: 기판-박막 간 열팽창계수 불일치(열 응력)와 격자 결함·결정립 성장(내재 응력)으로 발생하며, 박막이 수축하려는 <strong>인장 응력(Tensile, 웨이퍼 오목 휨 ➔ 균열/크랙)</strong>과 팽창하려는 <strong>압축 응력(Compressive, 웨이퍼 볼록 휨 ➔ 들뜸/박리)</strong>으로 나뉩니다.",
        "<strong>3. 박막 응력 제어 및 스트레인 공학 활용</strong>: 스퍼터링 공정 압력 및 기판 바이어스 조절(Atomic Peening으로 응력 제로점 튜닝), PECVD 반응가스비 및 고주파/저주파 RF 혼합 제어, 어닐링 열처리를 통해 제어합니다. 특히 NMOS에는 인장 응력(Tensile SiN), PMOS에는 압축 응력(e-SiGe)을 가해 캐리어 이동도를 2배 높이는 <strong>스트레인 엔지니어링(Strain Engineering)</strong>으로 적극 활용합니다.",
        "<strong>4. 알루미늄(Al) vs 구리(Cu) 금속 배선의 장단점</strong>: Cu는 Al 대비 비저항이 40% 낮고 녹는점이 높아 일렉트로마이그레이션(EM) 신뢰성이 10배 이상 우수하지만, 건식 식각이 불가능하여 <strong>듀얼 다마신(Dual Damascene) 공정과 CMP가 필수</strong>이며 확산 방지막(Ta/TaN)이 요구됩니다. 반면 Al은 RIE 건식 식각이 쉽고 자가산화막($\\text{Al}_2\\text{O}_3$) 덕분에 부식에 강해 최상층 패드 및 레거시 배선에 여전히 쓰입니다."
    ],
    "svg_title": "📊 [반도체 핵심 3대 현안 통합 다이어그램] (A) EUV Mo/Si 다층 반사 미러 광학계 | (B) 박막 응력(Tensile vs Compressive)과 웨이퍼 휨 제어 | (C) Al 배선 vs Cu 배선 물성 및 공정 비교",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: EUV Mirror Optics -->
  <g transform="translate(20, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) EUV 광학계가 미러로만 된 이유</text>

    <!-- Sub-box 1: Refraction Impossible -->
    <g transform="translate(15, 42)">
      <rect width="280" height="80" rx="5" fill="#1e293b" stroke="#ef4444"/>
      <text x="10" y="16" fill="#f87171" font-size="8.5" font-weight="800">1. 투과 굴절 렌즈의 완전한 불가능</text>
      <text x="10" y="32" fill="#cbd5e1" font-size="7.5">• 13.5 nm EUV 빛은 광자 에너지 91.8 eV 초고에너지</text>
      <text x="10" y="46" fill="#cbd5e1" font-size="7.5">• 유리, 석영(SiO₂), 공기(N₂, O₂) 등 모든 물질에 100% 흡수!</text>
      <text x="10" y="60" fill="#fde047" font-size="7.8" font-weight="800">➔ 렌즈를 통과하려 하면 빛이 전부 먹혀 소멸함 (투과율 0%)</text>
      <text x="10" y="74" fill="#94a3b8" font-size="7.2">• 굴절률 n ≈ 1 이라 빛을 꺾을(굴절) 수도 없음</text>
    </g>

    <!-- Sub-box 2: Mo/Si Multilayer Bragg Mirror -->
    <g transform="translate(15, 130)">
      <rect width="280" height="150" rx="5" fill="#1e293b" stroke="#38bdf8"/>
      <text x="10" y="16" fill="#38bdf8" font-size="8.5" font-weight="800">2. 해법: Mo/Si 브래그 다층 반사 미러</text>

      <!-- Multilayer visual -->
      <g transform="translate(15, 26)">
        <rect x="0" y="0" width="130" height="75" rx="3" fill="#0b1329" stroke="#334155"/>
        <!-- Alternating Mo and Si layers -->
        <rect x="5" y="6" width="120" height="6" fill="#94a3b8"/><text x="10" y="11" fill="#000" font-size="5.5" font-weight="800">Mo (2.8nm)</text>
        <rect x="5" y="14" width="120" height="6" fill="#38bdf8"/><text x="10" y="19" fill="#000" font-size="5.5" font-weight="800">Si (4.1nm)</text>
        <rect x="5" y="22" width="120" height="6" fill="#94a3b8"/>
        <rect x="5" y="30" width="120" height="6" fill="#38bdf8"/>
        <rect x="5" y="38" width="120" height="6" fill="#94a3b8"/>
        <rect x="5" y="46" width="120" height="6" fill="#38bdf8"/>
        <text x="45" y="62" fill="#cbd5e1" font-size="6.5">40 ~ 50쌍 교대 적층</text>

        <!-- Incident & reflected EUV rays -->
        <path d="M 150 10 L 80 30" stroke="#f43f5e" stroke-width="2" marker-end="url(#arrowRed)"/>
        <text x="150" y="12" fill="#f43f5e" font-size="7" font-weight="800">EUV 빛 입사</text>
        <path d="M 80 30 L 150 50" stroke="#34d399" stroke-width="2" marker-end="url(#arrowGreen)"/>
        <text x="145" y="60" fill="#34d399" font-size="7" font-weight="800">보강간섭 반사 (68%)</text>
      </g>

      <text x="10" y="115" fill="#cbd5e1" font-size="7.5">• 단일 금속은 반사율 수% ➔ 브래그 보강간섭으로 68% 달성!</text>
      <text x="10" y="128" fill="#fde047" font-size="7.5" font-weight="800">• 11개 미러 통과 시: (0.68)¹¹ ≈ 1.5%만 웨이퍼 도달!</text>
      <text x="10" y="141" fill="#cbd5e1" font-size="7.2">➔ 초고진공(10⁻⁷ mbar) + 수백W 고출력 주석 플라즈마 광원 필수</text>
    </g>

    <!-- Sub-box 3: Takeaway -->
    <rect x="15" y="290" width="280" height="118" rx="5" fill="#0b1329" stroke="#38bdf8"/>
    <text x="22" y="310" fill="#38bdf8" font-size="9" font-weight="800">🎯 EUV 미러 광학계 요약:</text>
    <text x="22" y="328" fill="#cbd5e1" font-size="7.8">• <strong>흡수가 너무 심해 렌즈는 전멸</strong>, 미러만 가능!</text>
    <text x="22" y="344" fill="#cbd5e1" font-size="7.8">• <strong>Mo/Si 50쌍 브래그 반사경</strong>으로 68% 반사율 쟁취</text>
    <text x="22" y="360" fill="#fca5a5" font-size="7.8">• 미러를 거칠 때마다 30%씩 빛이 사라져 광원 출력이 핵심</text>
    <text x="22" y="378" fill="#fde047" font-size="8" font-weight="800">➔ ASML이 20년 동안 1대당 3,000억 원에 만든 이유!</text>
  </g>

  <!-- PANEL B: Thin Film Stress & Control -->
  <g transform="translate(345, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 박막 응력(Stress)과 제어 방식</text>

    <!-- Tensile vs Compressive Graphic -->
    <g transform="translate(15, 42)">
      <rect width="280" height="155" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 박막 응력의 2대 형태와 웨이퍼 휨(Warpage)</text>

      <!-- Tensile (Smile / Bowl) -->
      <g transform="translate(10, 26)">
        <rect width="125" height="118" rx="4" fill="#0b1329" stroke="#ef4444"/>
        <text x="8" y="16" fill="#f87171" font-size="8" font-weight="800">인장 응력 (Tensile, +)</text>
        <!-- Curved wafer (concave, smile) -->
        <path d="M 15 48 Q 62 65 110 48" stroke="#38bdf8" stroke-width="4" fill="none"/>
        <path d="M 15 44 Q 62 61 110 44" stroke="#ef4444" stroke-width="2" fill="none"/>
        <text x="20" y="38" fill="#ef4444" font-size="7">박막 수축 (← → 당김)</text>
        <text x="35" y="80" fill="#cbd5e1" font-size="7.2">• 오목 휨 (Smile)</text>
        <text x="35" y="93" fill="#fca5a5" font-size="7.2">• 균열 / 크랙(Crack)</text>
        <text x="35" y="106" fill="#fde047" font-size="7.2">★ NMOS 이동도↑</text>
      </g>

      <!-- Compressive (Frown / Dome) -->
      <g transform="translate(145, 26)">
        <rect width="125" height="118" rx="4" fill="#0b1329" stroke="#3b82f6"/>
        <text x="8" y="16" fill="#60a5fa" font-size="8" font-weight="800">압축 응력 (Compressive, −)</text>
        <!-- Curved wafer (convex, frown) -->
        <path d="M 15 62 Q 62 45 110 62" stroke="#38bdf8" stroke-width="4" fill="none"/>
        <path d="M 15 58 Q 62 41 110 58" stroke="#3b82f6" stroke-width="2" fill="none"/>
        <text x="20" y="36" fill="#60a5fa" font-size="7">박막 팽창 (→ ← 밂)</text>
        <text x="35" y="80" fill="#cbd5e1" font-size="7.2">• 볼록 휨 (Frown)</text>
        <text x="35" y="93" fill="#93c5fd" font-size="7.2">• 들뜸 / 박리(Peel)</text>
        <text x="35" y="106" fill="#fde047" font-size="7.2">★ PMOS 이동도↑</text>
      </g>
    </g>

    <!-- Control Methods -->
    <g transform="translate(15, 205)">
      <rect width="280" height="200" rx="6" fill="#0b1329" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="9" font-weight="800">2. 박막 응력 정밀 제어 4대 방식</text>

      <text x="12" y="36" fill="#38bdf8" font-size="8" font-weight="800">① 스퍼터링 공정 압력 및 바이어스 조절 (Atomic Peening):</text>
      <text x="20" y="49" fill="#cbd5e1" font-size="7.2">• 압력 낮추면 고에너지 이온 충돌 ➔ 압축 응력으로 이동</text>
      <text x="20" y="61" fill="#cbd5e1" font-size="7.2">• 압력 높이면 산란 증가로 치밀도 저하 ➔ 인장 응력으로 이동 (0 튜닝!)</text>

      <text x="12" y="78" fill="#38bdf8" font-size="8" font-weight="800">② PECVD 가스비 및 Dual Frequency RF 조절:</text>
      <text x="20" y="91" fill="#cbd5e1" font-size="7.2">• SiH₄/NH₃ 비와 고주파(13.56MHz)/저주파(350kHz) 비율 제어</text>
      <text x="20" y="103" fill="#cbd5e1" font-size="7.2">• Si-N 결합 밀도와 수소 함량을 조절해 인장/압축 자유자재 변환</text>

      <text x="12" y="120" fill="#38bdf8" font-size="8" font-weight="800">③ 고온 어닐링 열처리 (Annealing):</text>
      <text x="20" y="133" fill="#cbd5e1" font-size="7.2">• 결정립 재배열 및 내부 결함 치유로 잔류 응력 완화</text>

      <text x="12" y="150" fill="#fde047" font-size="8.2" font-weight="800">④ 긍정적 응용: 스트레인 공학 (Strain Engineering):</text>
      <text x="20" y="164" fill="#a7f3d0" font-size="7.2">• NMOS 채널: 인장 응력 SiN 캡핑 ➔ 전자 이동도(μn) 2배 폭증!</text>
      <text x="20" y="177" fill="#a7f3d0" font-size="7.2">• PMOS 채널: 압축 응력 e-SiGe 심기 ➔ 정공 이동도(μp) 2배 폭증!</text>
    </g>
  </g>

  <!-- PANEL C: Aluminum vs Copper Metallization -->
  <g transform="translate(670, 20)">
    <rect width="290" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) 알루미늄(Al) vs 구리(Cu) 배선 비교</text>

    <!-- Comparison Table / Diagram -->
    <g transform="translate(15, 42)">
      <rect width="260" height="235" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">핵심 물성 및 공정 장단점 대결</text>

      <!-- Row 1: Resistivity -->
      <g transform="translate(10, 26)">
        <rect width="240" height="48" rx="3" fill="#0b1329" stroke="#334155"/>
        <text x="8" y="14" fill="#38bdf8" font-size="7.8" font-weight="800">1. 비저항 (Resistivity) &amp; RC 지연:</text>
        <text x="14" y="28" fill="#cbd5e1" font-size="7">• Al: 2.7 μΩ·cm ➔ 미세 배선에서 RC 지연 심각</text>
        <text x="14" y="41" fill="#34d399" font-size="7.5" font-weight="800">• Cu: 1.7 μΩ·cm ➔ Al 대비 저항 40% 낮음 (초고속!)</text>
      </g>

      <!-- Row 2: Electromigration -->
      <g transform="translate(10, 78)">
        <rect width="240" height="48" rx="3" fill="#0b1329" stroke="#334155"/>
        <text x="8" y="14" fill="#38bdf8" font-size="7.8" font-weight="800">2. 일렉트로마이그레이션 (EM) 신뢰성:</text>
        <text x="14" y="28" fill="#fca5a5" font-size="7">• Al: 녹는점 660℃ ➔ 전자바람에 원자 밀림 (단선/쇼트 취약)</text>
        <text x="14" y="41" fill="#34d399" font-size="7.5" font-weight="800">• Cu: 녹는점 1085℃ ➔ 원자 결합 강력, EM 수명 10~100배 우수!</text>
      </g>

      <!-- Row 3: Etching & Patterning -->
      <g transform="translate(10, 130)">
        <rect width="240" height="48" rx="3" fill="#0b1329" stroke="#334155"/>
        <text x="8" y="14" fill="#f87171" font-size="7.8" font-weight="800">3. 식각 공정 (가장 결정적 차이! ⚡):</text>
        <text x="14" y="28" fill="#34d399" font-size="7">• Al: 휘발성 AlCl₃ 형성 ➔ 건식 RIE 플라즈마 식각 완벽 가능!</text>
        <text x="14" y="41" fill="#ef4444" font-size="7.5" font-weight="800">• Cu: 휘발성 화합물 없어 건식 식각 불가능! (도랑 파고 채움)</text>
      </g>

      <!-- Row 4: Barrier & Oxidation -->
      <g transform="translate(10, 182)">
        <rect width="240" height="46" rx="3" fill="#0b1329" stroke="#334155"/>
        <text x="8" y="13" fill="#38bdf8" font-size="7.8" font-weight="800">4. 확산 방지 및 산화 특성:</text>
        <text x="14" y="27" fill="#cbd5e1" font-size="7">• Al: 자가보호 산화막(Al₂O₃)으로 부식 방어 우수</text>
        <text x="14" y="39" fill="#fde047" font-size="7.2">• Cu: Si/SiO₂로 맹렬히 확산 ➔ Ta/TaN 배리어 4면 포위 필수</text>
      </g>
    </g>

    <!-- Final Takeaway for Panel C -->
    <g transform="translate(15, 285)">
      <rect width="260" height="120" rx="6" fill="#0b1329" stroke="#f59e0b"/>
      <text x="12" y="18" fill="#fbbf24" font-size="8.8" font-weight="800">★ 배선 기술의 현대적 공존과 표준</text>
      <text x="12" y="35" fill="#34d399" font-size="7.8" font-weight="800">■ 고속 다층 배선 (M1 ~ M10): Cu 다마신 표준!</text>
      <text x="20" y="48" fill="#cbd5e1" font-size="7.2">• 낮은 저항과 높은 신뢰성으로 전송 속도 보장</text>
      <text x="20" y="60" fill="#cbd5e1" font-size="7.2">• 도랑 파고 구리 채운 후 CMP로 깎아내는 듀얼 다마신</text>

      <text x="12" y="78" fill="#38bdf8" font-size="7.8" font-weight="800">■ 최상층 패드 (Top Metal Pad): Al 표준!</text>
      <text x="20" y="91" fill="#cbd5e1" font-size="7.2">• 와이어 본딩 접합성 우수 + 공기 중 산화 부식 방어</text>
      <text x="20" y="104" fill="#a7f3d0" font-size="7.2">➔ 내부 고속 고속도로는 Cu, 외부 입출력 관문은 Al!</text>
    </g>
  </g>

  <!-- Arrow marker definitions -->
  <defs>
    <marker id="arrowRed" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#f43f5e" />
    </marker>
    <marker id="arrowGreen" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#34d399" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- SECTION 1: EUV Mirror Optics -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. EUV(13.5nm) 장비 광학계가 굴절 렌즈 없이 '반사 미러'로만 구성된 이유
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            기존의 ArF 액침(Immersion, 193nm) 노광 장비는 빛을 굴절시켜 모으는 거대한 유리/석영(Quartz) 렌즈 뭉치를 사용했습니다. 
            하지만 <strong>13.5nm 파장의 EUV(극자외선)는 투과 렌즈를 단 1개도 쓸 수 없으며, 100% 반사 거울(Mirror)로만 광학계를 구성</strong>해야 합니다. 그 이유는 3가지 물리적 한계 때문입니다:
          </p>

          <div style="background:#0f172a; border-left:4px solid #ef4444; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#f87171; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ① 모든 물질에 100% 흡수되는 극한의 광자 에너지 ($h\nu = 91.8\,\text{eV}$)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              13.5nm 파장의 빛은 가시광선이나 일반 자외선이 아니라 거의 **연X선(Soft X-ray)**에 가깝습니다.
              광자 에너지가 너무 높아 유리, 석영, 물, 공기(질소, 산소) 등 **지구상에 존재하는 거의 모든 물질의 원자 내각 전자(Inner Shell)를 직접 때려 광전 효과로 빛이 100% 흡수 소멸**합니다.
              <br>• 석영 렌즈에 쏘면 빛이 렌즈를 뚫고 나가는 것이 아니라 렌즈 표면에서 전부 먹혀 열로 증발합니다.
              <br>• 심지어 공기 분자조차 빛을 흡수하므로, EUV 챔버 내부는 **$10^{-7}\sim 10^{-9}\,\text{mbar}$ 수준의 초고진공(High Vacuum)**을 유지해야 합니다.
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #facc15; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#facc15; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ② 굴절률이 1에 극도로 수렴 ($n \approx 1 - \delta$, $\delta \sim 10^{-3}$)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              렌즈가 빛을 모으려면 진공과 렌즈 매질 사이의 굴절률 차이($\Delta n$)가 커서 빛이 꺾여야(스넬의 법칙) 합니다.
              하지만 EUV 대역에서는 모든 물질의 굴절률이 진공(1.0)과 거의 같은 $0.999$ 수준에 머물러 **빛을 꺾을 수 있는 굴절 렌즈 자체가 물리적으로 불가능**합니다.
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:18px;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ③ 유일한 해법: Mo/Si 40~50쌍 브래그 다층 박막 반사경 (Bragg Multilayer)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              투과가 안 되니 반사(Reflection)를 써야 하지만, 단일 금속판의 수직 반사율은 1% 미만입니다.
              이를 극복하기 위해 **몰리브덴(Mo, 2.8nm, 전자 밀도 높음)과 실리콘(Si, 4.1nm, 스페이서)을 원자 단위 두께로 40~50쌍 교대로 정밀 증착한 다층 거울**을 발명했습니다.
              각 층 계면에서 반사된 파동들이 **브래그 회절 조건($2d\sin\theta = \lambda$)에 의해 보강 간섭(Constructive Interference)**을 일으켜 기적적으로 **약 68~70%의 반사율**을 만들어냅니다!
            </p>
          </div>
          <p style="font-size:0.92rem; line-height:1.7; color:#fde047;">
            ★ 치명적 트레이드오프: 거울 1개당 반사율이 68%라는 것은 32%가 흡수되어 사라진다는 뜻입니다. EUV 빛이 마스크와 11개의 미러를 통과해 웨이퍼에 도달할 때 남는 광량은 **$(0.68)^{11} \approx 1.5\%$**에 불과합니다! 이 1.5%의 빛으로 웨이퍼를 굽기 위해 주석(Sn) 방울에 고출력 레이저를 쏴서 수백 W급의 플라즈마 광원을 만들어내는 것이 EUV 장비(1대당 3,000억 원)의 핵심 기술입니다.
          </p>
        </div>

        <!-- SECTION 2: Thin Film Stress -->
        <div style="margin-top:32px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 박막 응력(Thin Film Stress)이란 무엇이고 이를 제어하는 방식은 무엇인가?
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            웨이퍼 위에 증착(CVD, PVD, ALD 등) 공정으로 박막을 형성하면, 박막 내부와 실리콘 기판 계면에 **서로를 당기거나 미는 거대한 기계적 탄성 변형력(Stress, 단위: MPa~GPa)**이 축적됩니다.
          </p>

          <div style="overflow-x:auto; margin-bottom:16px;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">응력 구분</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">박막의 경향성</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">웨이퍼 휨 형태 (Warpage)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">주요 불량 및 영향</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#f87171;">인장 응력 (Tensile Stress, +)</td>
                  <td style="padding:10px 14px;">원래 크기보다 <strong>수축하려는 힘</strong> (당김)</td>
                  <td style="padding:10px 14px; font-weight:800; color:#f87171;">오목하게 휨 (Smile / Bowl 형태)</td>
                  <td style="padding:10px 14px;">박막 균열(Cracking), 배선 단선, 초점(DOF) 이탈</td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">압축 응력 (Compressive Stress, −)</td>
                  <td style="padding:10px 14px;">원래 크기보다 <strong>팽창하려는 힘</strong> (밂)</td>
                  <td style="padding:10px 14px; font-weight:800; color:#38bdf8;">볼록하게 휨 (Frown / Dome 형태)</td>
                  <td style="padding:10px 14px;">박막 들뜸(Peeling/Delamination), 주름(Buckling)</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h4 style="color:#fde047; font-size:1.05rem; font-weight:800; margin:16px 0 8px 0;">
            ■ 박막 응력의 4대 제어 및 활용 방식
          </h4>
          <ol style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:20px;">
            <li><strong>스퍼터링 공정 압력 및 기판 바이어스 조절 (Atomic Peening)</strong>:
              <br>• 공정 챔버 압력을 낮추면 타깃에서 튕겨 나온 고에너지 입자가 박막을 때려 치밀하게 압축시킵니다 (압축 응력 증가).
              <br>• 압력을 높이면 가스 충돌로 에너지를 잃어 기공이 생기며 인장 응력으로 이동합니다. 이 둘의 균형점을 찾아 **응력 0(Zero-stress) 박막**을 증착합니다.
            </li>
            <li><strong>PECVD 가스비 및 Dual-Frequency RF 제어</strong>:
              <br>• SiN 절연막 증착 시 $\text{SiH}_4 / \text{NH}_3$ 가스비와 고주파(13.56MHz)/저주파(350kHz) RF 파워 비율을 튜닝하여 막 내부의 수소 함량과 결합 밀도를 조절, 인장과 압축 응력을 정밀 제어합니다.
            </li>
            <li><strong>포스트 어닐링(Annealing) 열처리</strong>:
              <br>• 증착 후 고온 열처리를 거치면 결정립(Grain)이 재배열되고 내부 점결함이 회복되어 잔류 내재 응력이 대폭 완화됩니다.
            </li>
            <li><strong>긍정적 응용: 스트레인 엔지니어링 (Strain Engineering)</strong>:
              <br>• 응력은 불량의 원인이기도 하지만 최첨단 트랜지스터의 성능을 2배 높이는 무기가 됩니다:
              <br>• <strong>NMOS 채널</strong>: 실리콘 원자 격자를 양옆으로 잡아당기는 **인장 응력(Tensile SiN 캡핑)**을 가하면 유효 질량이 감소해 **전자 이동도($\mu_n$)가 최대 50~100% 급증**합니다.
              <br>• <strong>PMOS 채널</strong>: 실리콘보다 원자가 큰 SiGe를 소스/드레인에 임베디드하여 채널을 꽉 쥐어짜는 **압축 응력(Compressive)**을 가하면 **정공 이동도($\mu_p$)가 2배 폭증**합니다!
            </li>
          </ol>
        </div>

        <!-- SECTION 3: Aluminum vs Copper -->
        <div style="margin-top:32px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 알루미늄(Al)과 구리(Cu)를 사용했을 때의 장단점 비교
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체 금속 배선(Interconnect)은 0.18$\mu$m 노드 이전까지 **알루미늄(Al)**이 표준이었으나, 1997년 IBM의 혁신 이후 **구리(Cu)**로 대전환되었습니다. 두 금속의 핵심 장단점은 다음과 같습니다.
          </p>

          <div style="overflow-x:auto; margin-bottom:16px;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">비교 항목</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">알루미늄 (Al)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">구리 (Cu)</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">① 비저항 (Resistivity)</td>
                  <td style="padding:10px 14px; color:#f87171;">$2.7\,\mu\Omega\cdot\text{cm}$ (상대적 높음)</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:800;">$1.7\,\mu\Omega\cdot\text{cm}$ (Al 대비 40% 낮음, RC 딜레이 단축)</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">② 일렉트로마이그레이션 (EM)</td>
                  <td style="padding:10px 14px; color:#f87171;">녹는점($660^\circ\text{C}$)이 낮아 고전류에서 원자가 밀려 단선/쇼트 취약</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:800;">녹는점($1085^\circ\text{C}$)이 높아 원자 결합 강력, EM 수명 10~100배 우수</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">③ 건식 플라즈마 식각 (RIE)<br>(결정적 공정 차이!)</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:800;"><strong>건식 식각 매우 쉬움!</strong><br>휘발성 반응부산물 $\text{AlCl}_3$(끓는점 $180^\circ\text{C}$)이 생겨 가스로 날아감</td>
                  <td style="padding:10px 14px; color:#f87171; font-weight:800;"><strong>건식 식각 불가능! (Hard)</strong><br>휘발성 구리 염화물이 없어 상온에서 플라즈마로 깎아낼 수 없음</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">④ 패터닝 공정 방식</td>
                  <td style="padding:10px 14px;"><strong>감산 방식 (Subtractive)</strong><br>Al 증착 ➔ 포토 ➔ RIE 식각 (공정 단순)</td>
                  <td style="padding:10px 14px;"><strong>듀얼 다마신 (Dual Damascene)</strong><br>절연막에 도랑을 먼저 파고 구리 도금 후 CMP로 연마 (고난도)</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">⑤ 실리콘/산화막 확산성</td>
                  <td style="padding:10px 14px;">스파이킹(Spiking) 방지용 Ti/TiN만으로 충분, $\text{SiO}_2$ 부착력 우수</td>
                  <td style="padding:10px 14px; color:#f87171;">Si와 $\text{SiO}_2$로 미친 듯이 확산해 소자 파괴 ➔ <strong>Ta/TaN 4면 배리어 필수</strong></td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">⑥ 산화 및 부식 내성</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:800;">공기 노출 시 치밀한 자가보호 산화막($\text{Al}_2\text{O}_3, 3\text{nm}$) 형성 ➔ <strong>부식 저항 탁월</strong></td>
                  <td style="padding:10px 14px; color:#f87171;">구리 산화막($\text{CuO}$)이 다공성이라 공기 중에 두면 끝없이 녹슬고 부식됨</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div style="background:#0f172a; border-left:4px solid #f59e0b; padding:16px 20px; border-radius:0 8px 8px 0;">
            <h4 style="color:#fbbf24; font-size:1rem; font-weight:800; margin-bottom:6px;">
              💡 현대 반도체 칩에서 두 금속의 분업 전략
            </h4>
            <p style="color:#cbd5e1; font-size:0.92rem; line-height:1.75;">
              • <strong>내부 미세 다층 배선 (M1 ~ M10 이상)</strong>: 초고속 신호 전송과 신뢰성을 위해 <strong>100% 구리 듀얼 다마신(Cu Damascene)</strong>을 사용합니다.<br>
              • <strong>최상층 본딩 패드 (Top Metal Pad)</strong>: 외부 패키징과 연결되는 맨 위 패드는 자가보호 산화막으로 부식에 강하고 와이어 본딩 접합력이 뛰어난 <strong>알루미늄(Al)</strong>을 여전히 표준으로 사용합니다!
            </p>
          </div>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 92 topics (q-92 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(92, 0, -1):
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

    # Step 4: Update header description to 93 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 'EUV 미러 광학계 · 박막 응력 제어 · Al vs Cu 배선'이 위치하며, 총 93개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 EUV / Stress / Al vs Cu topic!")
