# -*- coding: utf-8 -*-
"""
split_euv_stress_al_cu_into_3_topics.py
3개 질문을 각각 독립된 전용 주제(Q01, Q02, Q03)로 분리하고,
기존 Q02~Q93(92개)을 Q04~Q95로 시프트하여 총 95개 질문 백과사전을 구축합니다.
"""

import sys
import re

TOPIC_1 = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (노광 및 포토 공정 · EUV 광학계 반사 미러 전용 이유와 Mo/Si 브래그 원리)",
    "title": "EUV 장비 광학계가 미러(반사경)로만 구성된 이유 (13.5nm 광자 흡수, 굴절률 한계, Mo/Si 브래그 반사)",
    "nav_title": "EUV 장비 광학계가 미러로만 구성된 이유",
    "summary": [
        "<strong>1. 극한의 광자 에너지($91.8\\,\\text{eV}$)와 모든 물질의 100% 흡수</strong>: 13.5nm 극자외선(EUV)은 연X선에 준하는 초단파장으로, 유리·석영($\\text{SiO}_2$)·공기(질소/산소) 등 지구상의 모든 물질의 내각 전자를 들뜨게 하여 100% 흡수 소멸되므로 빛을 통과시키는 굴절 렌즈가 원천 불가능합니다.",
        "<strong>2. 매질 간 굴절률 차이 소멸 ($n \\approx 1$)</strong>: EUV 파장 대역에서는 모든 물질의 굴절률이 진공(1.0)과 거의 같은 $0.999$ 수준에 수렴하여, 스넬의 법칙에 의해 빛을 꺾고 모으는 굴절 렌즈 제작 자체가 물리 법칙상 성립하지 않습니다.",
        "<strong>3. 유일한 해법: Mo/Si 40~50쌍 브래그 다층 박막 반사경 (Bragg Mirror)</strong>: 단일 금속 반사율(1% 미만)을 극복하기 위해 몰리브덴(Mo, 2.8nm, 전자밀도 높음)과 실리콘(Si, 4.1nm, 스페이서)을 원자 단위로 40~50쌍 교대 증착하여 브래그 보강 간섭($2d\\sin\\theta = \\lambda$)으로 약 68%의 기적적인 반사율을 구현합니다.",
        "<strong>4. 광량 손실 트레이드오프와 수백W 광원 필연성</strong>: 거울 1개당 반사율 68%는 32%가 흡수 손실됨을 의미하며, 마스크와 11개 미러를 거치면 웨이퍼 도달 광량은 $(0.68)^{11} \\approx 1.5\\%$에 불과합니다. 이를 극복하기 위해 초고진공($10^{-7}\\,\\text{mbar}$) 챔버와 주석(Sn) 플라즈마 광원이 필수적입니다."
    ],
    "svg_title": "📊 [EUV 반사 미러 광학계 핵심 다이어그램] (A) 13.5nm 광자 흡수 및 굴절률 한계 | (B) Mo/Si 브래그 다층 반사경 보강 간섭 | (C) 11개 반사경 광량 감쇠 및 웨이퍼 도달",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Why Refraction Lens is Impossible -->
  <g transform="translate(20, 20)">
    <rect width="295" height="420" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.2"/>
    <text x="16" y="26" fill="#f87171" font-size="12" font-weight="800">■ (A) 투과 굴절 렌즈 사용 불가 이유</text>

    <!-- Sub-box 1: 91.8 eV photon absorption -->
    <g transform="translate(15, 42)">
      <rect width="265" height="115" rx="5" fill="#1e293b" stroke="#ef4444"/>
      <text x="10" y="18" fill="#fca5a5" font-size="8.8" font-weight="800">1. 초고에너지 광자 ($h\nu = 91.8\text{ eV}$)</text>
      <text x="10" y="34" fill="#cbd5e1" font-size="7.5">• 13.5nm는 연X선(Soft X-ray)에 근접한 초단파장</text>
      <text x="10" y="48" fill="#cbd5e1" font-size="7.5">• 유리, 석영(SiO₂), 물, 공기(N₂, O₂) 전 물질에 흡수</text>
      <text x="10" y="62" fill="#fde047" font-size="7.8" font-weight="800">➔ 빛이 렌즈를 뚫지 못하고 표면에서 100% 열로 소멸!</text>
      <text x="10" y="78" fill="#cbd5e1" font-size="7.2">• 공기조차 빛을 흡수하므로 광학계 전체가</text>
      <text x="10" y="92" fill="#38bdf8" font-size="7.5" font-weight="800">   10⁻⁷ mbar 초고진공(High Vacuum) 유지 필수!</text>
      <text x="10" y="106" fill="#94a3b8" font-size="7">• 투과율 T = exp(-α·t) → 두께 1㎛만 지나도 T ≈ 0</text>
    </g>

    <!-- Sub-box 2: Refractive index n ~ 1 -->
    <g transform="translate(15, 168)">
      <rect width="265" height="115" rx="5" fill="#1e293b" stroke="#f59e0b"/>
      <text x="10" y="18" fill="#fbbf24" font-size="8.8" font-weight="800">2. 굴절률 차이 상실 (n ≈ 1 - δ, δ ≪ 1)</text>
      <text x="10" y="34" fill="#cbd5e1" font-size="7.5">• 진공(n=1.0)과 매질(n≈0.999)의 차이가 없음</text>
      <text x="10" y="48" fill="#cbd5e1" font-size="7.5">• 스넬의 법칙(n₁sinθ₁ = n₂sinθ₂) 작동 불가</text>
      <text x="10" y="64" fill="#fde047" font-size="7.8" font-weight="800">➔ 렌즈 형상을 아무리 깎아도 빛이 꺾이지 않음!</text>
      <text x="10" y="80" fill="#cbd5e1" font-size="7.2">• 굴절 렌즈로는 초점을 맺는 것 자체가 물리적 불가능</text>
      <text x="10" y="94" fill="#a7f3d0" font-size="7.5">• 유일한 대안: 거울을 통한 반사(Reflection) 방식</text>
      <text x="10" y="107" fill="#94a3b8" font-size="7">• 하지만 일반 금속 표면 반사율도 1% 미만!</text>
    </g>

    <!-- Sub-box 3: Summary -->
    <rect x="15" y="295" width="265" height="110" rx="5" fill="#0b1329" stroke="#ef4444"/>
    <text x="20" y="316" fill="#f87171" font-size="9" font-weight="800">💡 결론: 투과 렌즈는 전멸!</text>
    <text x="20" y="334" fill="#cbd5e1" font-size="7.5">• ArF(193nm)까지 쓰던 석영 렌즈 뭉치 폐기</text>
    <text x="20" y="350" fill="#cbd5e1" font-size="7.5">• 100% 반사 거울(Mirror) 시스템 채택 필연</text>
    <text x="20" y="368" fill="#fde047" font-size="7.8" font-weight="800">➔ 빛을 반사시키는 특수 브래그 미러 개발 착수</text>
    <text x="20" y="386" fill="#cbd5e1" font-size="7.2">• ASML과 칼 자이스(Zeiss)의 20년 합작 연구</text>
  </g>

  <!-- PANEL B: Mo/Si Bragg Multilayer Mirror -->
  <g transform="translate(330, 20)">
    <rect width="320" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (B) Mo/Si 브래그 다층 박막 반사경 원리</text>

    <!-- Diagram -->
    <g transform="translate(15, 42)">
      <rect width="290" height="195" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">브래그 보강 간섭 (2d sinθ = λ, d ≈ 6.9nm)</text>

      <!-- Multilayer stack visual -->
      <g transform="translate(15, 28)">
        <rect x="0" y="0" width="140" height="105" rx="3" fill="#0b1329" stroke="#334155"/>
        <!-- Layers -->
        <rect x="5" y="8" width="130" height="8" fill="#94a3b8"/><text x="12" y="15" fill="#000" font-size="6" font-weight="800">Mo 몰리브덴 (2.8nm, 전자 밀도 높음)</text>
        <rect x="5" y="18" width="130" height="8" fill="#38bdf8"/><text x="12" y="25" fill="#000" font-size="6" font-weight="800">Si 실리콘 (4.1nm, 스페이서)</text>
        <rect x="5" y="28" width="130" height="8" fill="#94a3b8"/>
        <rect x="5" y="38" width="130" height="8" fill="#38bdf8"/>
        <rect x="5" y="48" width="130" height="8" fill="#94a3b8"/>
        <rect x="5" y="58" width="130" height="8" fill="#38bdf8"/>
        <rect x="5" y="68" width="130" height="8" fill="#94a3b8"/>
        <rect x="5" y="78" width="130" height="8" fill="#38bdf8"/>
        <text x="32" y="98" fill="#cbd5e1" font-size="7">40 ~ 50쌍 정밀 적층 구조</text>

        <!-- Ray tracing -->
        <path d="M 160 10 L 80 32" stroke="#f43f5e" stroke-width="2.2" marker-end="url(#arrowRed1)"/>
        <text x="155" y="12" fill="#f43f5e" font-size="7.2" font-weight="800">EUV 빛 입사</text>
        <path d="M 80 32 L 160 55" stroke="#34d399" stroke-width="2.2" marker-end="url(#arrowGreen1)"/>
        <text x="150" y="68" fill="#34d399" font-size="7.5" font-weight="800">위상 일치 보강간섭 반사!</text>
        <text x="150" y="80" fill="#fde047" font-size="7.2" font-weight="800">(반사율 R ≈ 68~70%)</text>
      </g>

      <text x="12" y="152" fill="#cbd5e1" font-size="7.5">• 각 층 계면에서 극소량 반사된 파동들이 같은 위상으로 중첩</text>
      <text x="12" y="166" fill="#cbd5e1" font-size="7.5">• 40~50쌍이 합쳐져 총 반사율 **약 68%** 기적적 달성!</text>
      <text x="12" y="180" fill="#94a3b8" font-size="7.2">• 표면 거칠기 0.1nm(원자 1개) 이하 극초평탄 가공(Carl Zeiss)</text>
    </g>

    <!-- Key equations -->
    <g transform="translate(15, 248)">
      <rect width="290" height="157" rx="6" fill="#0b1329" stroke="#38bdf8"/>
      <text x="12" y="18" fill="#38bdf8" font-size="8.8" font-weight="800">핵심 파라미터 및 설계 스펙</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="7.5">• 주기 두께: d = d_Mo + d_Si = 2.8 + 4.1 = 6.9 nm</text>
      <text x="12" y="50" fill="#cbd5e1" font-size="7.5">• 2d ≈ 13.8 nm ≈ EUV 파장 13.5 nm 완벽 공명</text>
      <text x="12" y="66" fill="#fde047" font-size="7.8" font-weight="800">• Mo: 전자 밀도 높아 프레넬 반사 유도 (굴절률 변조)</text>
      <text x="12" y="80" fill="#a7f3d0" font-size="7.5">• Si: EUV 흡수율이 낮아 빛을 투과시키는 스페이서</text>
      <text x="12" y="96" fill="#cbd5e1" font-size="7.5">• 캡핑층: Ru(루테늄, 2nm) ➔ 산화 및 탄소 오염 방어</text>
      <text x="12" y="112" fill="#fca5a5" font-size="7.2">• 열팽창 변형 억제: 저열팽창 유리(Zerodur) 기판 적용</text>
      <text x="12" y="128" fill="#94a3b8" font-size="7">• 피코미터(pm) 단위 능동 형상 보정 액추에이터 탑재</text>
    </g>
  </g>

  <!-- PANEL C: 11 Mirror Train & Power Decay -->
  <g transform="translate(665, 20)">
    <rect width="295" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (C) 11개 반사경 광량 감쇠와 웨이퍼 도달</text>

    <!-- Mirror train box -->
    <g transform="translate(15, 42)">
      <rect width="265" height="195" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">광학 경로: 11개 미러 통과 시 광량 손실</text>

      <!-- Formula representation -->
      <g transform="translate(10, 28)">
        <rect width="245" height="52" rx="4" fill="#0b1329" stroke="#ef4444"/>
        <text x="10" y="18" fill="#f87171" font-size="8" font-weight="800">반사율 68% 거울 11개 연속 통과:</text>
        <text x="10" y="34" fill="#fde047" font-size="8.5" font-weight="900">웨이퍼 도달 광량 = (0.68)¹¹ ≈ 1.5% !!</text>
        <text x="10" y="46" fill="#cbd5e1" font-size="6.8">(광원에서 나온 빛의 98.5%가 도중에 소멸됨)</text>
      </g>

      <text x="10" y="96" fill="#cbd5e1" font-size="7.2">• 조명계(Illuminator): 5~6개 반사 미러</text>
      <text x="10" y="108" fill="#cbd5e1" font-size="7.2">• 마스크(Reticle): 반사형 Mo/Si 마스크 (R ≈ 65%)</text>
      <text x="10" y="120" fill="#cbd5e1" font-size="7.2">• 투영계(POB): 6개 반사 미러 (High-NA는 8~10개)</text>
      <text x="10" y="136" fill="#fde047" font-size="7.5" font-weight="800">➔ 최종 웨이퍼에 닿는 빛은 고작 1~2% 수준!</text>
      <text x="10" y="150" fill="#cbd5e1" font-size="7.2">• 포토레지스트(PR)를 충분히 감광시키려면</text>
      <text x="10" y="164" fill="#38bdf8" font-size="7.5" font-weight="800">   초기 광원 출력이 수백 W 이상이어야 함!</text>
      <text x="10" y="178" fill="#94a3b8" font-size="7">• Sn(주석) 방울에 CO₂ 레이저 5만번/초 타격 플라즈마</text>
    </g>

    <!-- Key takeaways -->
    <g transform="translate(15, 248)">
      <rect width="265" height="157" rx="6" fill="#0b1329" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="8.8" font-weight="800">🎯 핵심 면접/학습 정리</text>
      <text x="12" y="36" fill="#38bdf8" font-size="7.8" font-weight="800">Q. 왜 렌즈 대신 미러만 쓰나요?</text>
      <text x="16" y="50" fill="#cbd5e1" font-size="7.2">A. 13.5nm EUV는 모든 물질에 100% 흡수되고</text>
      <text x="16" y="62" fill="#cbd5e1" font-size="7.2">   굴절률 n≈1이라 굴절 렌즈가 원천 불가능합니다.</text>
      <text x="12" y="80" fill="#38bdf8" font-size="7.8" font-weight="800">Q. 거울의 반사율은 어떻게 올렸나요?</text>
      <text x="16" y="94" fill="#cbd5e1" font-size="7.2">A. Mo/Si 40~50쌍 브래그 다층 박막을 원자 단위로</text>
      <text x="16" y="106" fill="#cbd5e1" font-size="7.2">   증착하여 보강 간섭으로 68% 반사율을 구현했습니다.</text>
      <text x="12" y="124" fill="#fde047" font-size="7.8" font-weight="800">Q. 광원 출력이 왜 그렇게 중요한가요?</text>
      <text x="16" y="138" fill="#cbd5e1" font-size="7.2">A. 11개 미러를 거치면 광량이 1.5%만 남아 웨이퍼를</text>
      <text x="16" y="150" fill="#cbd5e1" font-size="7.2">   노광하려면 300~500W급 초고출력 광원이 필수입니다.</text>
    </g>
  </g>

  <!-- Markers -->
  <defs>
    <marker id="arrowRed1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#f43f5e" />
    </marker>
    <marker id="arrowGreen1" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#34d399" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- SECTION 1: EUV Mirror Optics Detailed Master Lecture -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 13.5nm 극자외선(EUV)의 물리적 본질과 투과 굴절 렌즈의 절대적 불가능성
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            기존의 DUV(심자외선, ArF 액침 193nm) 노광 장비는 수십 장의 거대한 합성 석영(Fused Silica, $\text{SiO}_2$) 및 형석($\text{CaF}_2$) 굴절 렌즈를 조합하여 빛을 모으고 축소 투영했습니다. 
            하지만 <strong>파장이 13.5nm로 짧아진 EUV(극자외선) 노광기에서는 굴절 렌즈가 단 1장도 존재하지 않으며, 100% 반사 미러(Reflective Mirror)로만 광학계를 구성</strong>합니다. 이는 단순한 기술적 선택이 아닌 자연계의 물리 법칙 때문입니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #ef4444; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#f87171; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ① 모든 물질에 100% 흡수되는 극한의 광자 에너지 ($E = h\nu = 91.8\,\text{eV}$)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              13.5nm 파장의 광자는 에너지가 $91.8\,\text{eV}$에 달합니다. 가시광선($2\sim 3\,\text{eV}$)이나 DUV($6.4\,\text{eV}$)와 달리, **연X선(Soft X-ray)** 영역에 해당하는 초고에너지입니다.
              이 에너지는 유리, 석영, 물뿐만 아니라 대기 중의 질소($\text{N}_2$), 산소($\text{O}_2$) 등 지구상에 존재하는 거의 모든 원자의 안쪽 껍질 전자를 단숨에 이온화(광전 효과)시키는 에너지입니다.
              <br>• 석영 렌즈에 쏘면 빛이 렌즈를 통과하지 못하고 렌즈 표면 수 나노미터 깊이에서 100% 흡수되어 열로 소멸합니다.
              <br>• 심지어 공기 분자조차 EUV 광자를 즉각 흡수하므로, EUV 노광 장비 내부 전체는 **$10^{-7}\sim 10^{-9}\,\text{mbar}$ 수준의 초고진공(Ultra-High Vacuum)** 상태를 유지해야 합니다.
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #facc15; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#facc15; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ② 물질의 굴절률이 진공(1.0)에 극도로 수렴 ($\tilde{n} \approx 1 - \delta - i\beta$, $\delta \sim 10^{-3}$)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              렌즈가 빛을 모으려면 진공과 렌즈 매질 사이의 굴절률 차이($\Delta n$)가 존재하여 빛이 꺾여야 합니다(스넬의 법칙).
              하지만 EUV 대역에서는 모든 물질의 복소 굴절률 실수부($n = 1 - \delta$)에서 감쇄 상수 $\delta$가 $10^{-3}\sim 10^{-4}$에 불과하여 **진공과 렌즈의 굴절률이 사실상 1.0으로 똑같습니다.**
              빛이 꺾이지 않으므로 렌즈 곡면을 아무리 정밀하게 연마해도 초점을 맺을 수 있는 굴절 렌즈 자체가 물리적으로 불가능합니다.
            </p>
          </div>

          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin:24px 0 12px 0; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 유일한 돌파구: Mo/Si 브래그 다층 박막 반사경 (Bragg Multilayer Reflector)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            투과가 불가능하므로 반사(Reflection)를 이용해야 하지만, 일반적인 금속 거울(은, 알루미늄 등)조차 EUV 대역에서는 수직 입사 반사율이 1% 미만에 불과합니다. 
            이를 극복하기 위해 발명된 것이 바로 **Mo(몰리브덴)과 Si(실리콘)을 교대로 40~50쌍 적층한 브래그 다층 박막 거울**입니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:800; margin-bottom:6px;">
              브래그 회절 조건 ($2d\sin\theta = \lambda$)과 보강 간섭
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              • <strong>Mo 층 (두께 약 2.8nm)</strong>: 전자 밀도가 높아 EUV 파장에서 프레넬 반사를 일으키는 '산란체' 역할을 합니다.
              <br>• <strong>Si 층 (두께 약 4.1nm)</strong>: 13.5nm EUV에 대한 흡수율이 낮아 빛을 투과시키는 '스페이서(Spacer)' 역할을 합니다.
              <br>• 한 쌍의 두께(주기 $d$)는 $2.8 + 4.1 = 6.9\,\text{nm}$이며, 수직 입사($\theta \approx 90^\circ$) 시 $2d \approx 13.8\,\text{nm} \approx 13.5\,\text{nm}$ 조건을 만족합니다.
              <br>• 각 층 계면에서 반사된 극미량(0.1% 미만)의 파동들이 **정확히 위상이 일치(In-phase)하여 보강 간섭**을 일으키며, 40~50쌍이 쌓이면 이론적 한계에 근접한 **약 68~70%의 반사율**을 만들어냅니다.
            </p>
          </div>

          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin:24px 0 12px 0; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 반사경 11개의 연쇄 통과와 광량 손실: 수백 W 광원이 필수적인 이유
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            Mo/Si 브래그 미러의 반사율 68%는 기적적인 수치이지만, 역으로 생각하면 **거울 1개에 부딪힐 때마다 빛의 32%가 흡수되어 사라진다**는 뜻입니다.
          </p>

          <div style="background:#1e293b; padding:16px 20px; border-radius:8px; margin-bottom:16px;">
            <h4 style="color:#fde047; font-size:0.98rem; font-weight:800; margin-bottom:8px;">
              웨이퍼 도달 광량 계산 ($R = 0.68$, 11개 미러 통과 시):
            </h4>
            <p style="color:#f87171; font-size:1.05rem; font-weight:800; margin-bottom:8px;">
              $$\text{Transmission} = (0.68)^{11} \approx 0.0145 \quad (1.45\%)$$
            </p>
            <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7;">
              조명계 미러(5~6개), 반사형 마스크(1개), 투영계 미러(6개)를 거치고 나면 **광원에서 출발한 EUV 에너지의 98.5% 이상이 미러에 흡수되어 사라지고, 고작 1.5% 미만의 빛만 웨이퍼에 도달**합니다!
              <br>만약 광원의 출력이 약하면 웨이퍼 1장을 굽는 노광 시간(Dwell time)이 너무 길어져 생산성(웨이퍼 처리량, WPH)이 파탄 납니다.
              <br>이것이 바로 ASML이 고순도 주석(Sn) 액적을 초당 5만 번 떨어뜨리고 $20\,\text{kW}$급 $\text{CO}_2$ 레이저로 2차례 타격해 수만 도의 플라즈마를 발생시켜 **300W~500W급 초고출력 EUV 광원**을 개발하는 데 20년과 수조 원을 쏟아부은 핵심 이유입니다.
            </p>
          </div>
        </div>
    """
}

TOPIC_2 = {
    "id": "q-02",
    "num": "02",
    "badge": "⭐ 최신 질문 (박막 증착 공정 & 소자 물리 · 박막 응력의 본질과 정밀 제어, 스트레인 공학)",
    "title": "박막 응력(Thin Film Stress)이란 무엇이고 이를 제어하는 방식은 무엇인가? (인장 vs 압축, 스트레인 공학)",
    "nav_title": "박막 응력이란 무엇이고 이를 제어하는 방식은 무엇인가",
    "summary": [
        "<strong>1. 박막 응력(Thin Film Stress)의 본질</strong>: 웨이퍼 위에 박막(CVD, PVD, ALD 등)을 증착할 때, 기판과 박막 간 열팽창계수 불일치(열 응력, Thermal Stress)와 격자 결함·결정립 경계·불순물(내재 응력, Intrinsic Stress)로 인해 계면에 축적되는 기계적 탄성 변형력(단위: MPa~GPa)입니다.",
        "<strong>2. 2대 응력 형태와 웨이퍼 휨(Warpage) 불량</strong>: 박막이 수축하려는 <strong>인장 응력(Tensile Stress, +)</strong>은 웨이퍼를 오목(Smile)하게 휘게 만들어 막 균열(Cracking)을 유발하고, 팽창하려는 <strong>압축 응력(Compressive Stress, −)</strong>은 볼록(Frown)하게 휘게 만들어 박막 들뜸/박리(Delamination)를 유발합니다.",
        "<strong>3. 박막 응력 정밀 제어 3대 공정 기법</strong>: ① 스퍼터링 공정 압력 및 기판 바이어스 튜닝(Atomic Peening 효과로 압축/인장 전환 및 제로 응력 박막 구현), ② PECVD 가스비($\\text{SiH}_4/\\text{NH}_3$) 및 Dual-Frequency RF 파워비 제어로 결합 밀도 조절, ③ 고온 어닐링 열처리를 통한 결정립 재배열 및 잔류 응력 완화.",
        "<strong>4. 소자 물리적 반전: 스트레인 엔지니어링(Strain Engineering)</strong>: 응력을 불량이 아닌 트랜지스터 성능 극대화 무기로 역이용하여, NMOS 채널에는 인장 응력(Tensile SiN 캡핑)을 가해 $\\mu_n$을 2배 높이고, PMOS 채널에는 압축 응력(e-SiGe 소스/드레인)을 가해 $\\mu_p$를 2배 폭증시킵니다."
    ],
    "svg_title": "📊 [박막 응력 및 제어 기술 다이어그램] (A) 인장(Tensile) vs 압축(Compressive) 응력과 웨이퍼 휨 | (B) 스퍼터링/PECVD 공정 파라미터 제어 | (C) CMOS 스트레인 엔지니어링 응용",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Tensile vs Compressive Stress -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.2"/>
    <text x="16" y="26" fill="#f87171" font-size="12" font-weight="800">■ (A) 박막 응력의 2대 형태와 웨이퍼 휨</text>

    <!-- Sub 1: Tensile Stress -->
    <g transform="translate(15, 42)">
      <rect width="270" height="170" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="12" y="18" fill="#f87171" font-size="9" font-weight="800">1. 인장 응력 (Tensile Stress, σ &gt; 0)</text>
      
      <!-- Visual Smile Wafer -->
      <g transform="translate(20, 26)">
        <rect width="230" height="75" rx="4" fill="#0b1329" stroke="#334155"/>
        <path d="M 25 35 Q 115 62 205 35" stroke="#38bdf8" stroke-width="5" fill="none"/>
        <path d="M 25 30 Q 115 57 205 30" stroke="#ef4444" stroke-width="2.5" fill="none"/>
        <text x="35" y="22" fill="#ef4444" font-size="7.5" font-weight="800">박막이 수축하려 당김 (←  →)</text>
        <text x="90" y="68" fill="#cbd5e1" font-size="7">Si 웨이퍼 기판</text>
      </g>

      <text x="12" y="118" fill="#cbd5e1" font-size="7.5">• <strong>웨이퍼 형상</strong>: 오목하게 휨 (Smile / Bowl 형태)</text>
      <text x="12" y="132" fill="#fca5a5" font-size="7.5">• <strong>주요 불량</strong>: 박막 균열(Crack), 배선 단선, 초점 이탈</text>
      <text x="12" y="146" fill="#fde047" font-size="7.8" font-weight="800">• <strong>소자 응용</strong>: NMOS 채널에 인장 가하면 전자 이동도 ↑</text>
      <text x="12" y="160" fill="#94a3b8" font-size="7">• 원인: 박막 열팽창계수(α_f) &gt; 기판(α_s) 냉각 시 수축</text>
    </g>

    <!-- Sub 2: Compressive Stress -->
    <g transform="translate(15, 225)">
      <rect width="270" height="175" rx="6" fill="#1e293b" stroke="#3b82f6"/>
      <text x="12" y="18" fill="#60a5fa" font-size="9" font-weight="800">2. 압축 응력 (Compressive Stress, σ &lt; 0)</text>
      
      <!-- Visual Frown Wafer -->
      <g transform="translate(20, 26)">
        <rect width="230" height="75" rx="4" fill="#0b1329" stroke="#334155"/>
        <path d="M 25 55 Q 115 28 205 55" stroke="#38bdf8" stroke-width="5" fill="none"/>
        <path d="M 25 50 Q 115 23 205 50" stroke="#3b82f6" stroke-width="2.5" fill="none"/>
        <text x="35" y="22" fill="#60a5fa" font-size="7.5" font-weight="800">박막이 팽창하려 밂 (→  ←)</text>
        <text x="90" y="68" fill="#cbd5e1" font-size="7">Si 웨이퍼 기판</text>
      </g>

      <text x="12" y="118" fill="#cbd5e1" font-size="7.5">• <strong>웨이퍼 형상</strong>: 볼록하게 휨 (Frown / Dome 형태)</text>
      <text x="12" y="132" fill="#93c5fd" font-size="7.5">• <strong>주요 불량</strong>: 박막 들뜸/박리(Peeling), 주름(Buckling)</text>
      <text x="12" y="146" fill="#fde047" font-size="7.8" font-weight="800">• <strong>소자 응용</strong>: PMOS 채널에 압축 가하면 정공 이동도 ↑</text>
      <text x="12" y="160" fill="#94a3b8" font-size="7">• 원인: 고에너지 이온 충돌로 원자가 강제 격자 패킹됨</text>
    </g>
  </g>

  <!-- PANEL B: Thin Film Stress Control Methods -->
  <g transform="translate(335, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 박막 응력 정밀 제어 3대 공정 기법</text>

    <!-- Method 1: Sputtering Atomic Peening -->
    <g transform="translate(15, 42)">
      <rect width="280" height="115" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" fill="#38bdf8" font-size="8.8" font-weight="800">① 스퍼터링 공정 압력 &amp; Atomic Peening</text>
      <text x="10" y="34" fill="#cbd5e1" font-size="7.5">• <strong>낮은 챔버 압력 (High Vacuum)</strong>:</text>
      <text x="16" y="48" fill="#cbd5e1" font-size="7.2">가스 충돌 없이 고에너지 입자가 박막 타격 (Atomic Peening)</text>
      <text x="16" y="60" fill="#60a5fa" font-size="7.5" font-weight="800">➔ 원자 충진 밀도 극대화 → 압축 응력(Compressive) 형성</text>
      <text x="10" y="76" fill="#cbd5e1" font-size="7.5">• <strong>높은 챔버 압력 (Low Vacuum)</strong>:</text>
      <text x="16" y="90" fill="#cbd5e1" font-size="7.2">기체 산란으로 에너지 손실, 다공성 막 형성</text>
      <text x="16" y="104" fill="#f87171" font-size="7.5" font-weight="800">➔ 막 수축 경향 → 인장 응력(Tensile)으로 전이 (0 제어!)</text>
    </g>

    <!-- Method 2: PECVD Dual RF -->
    <g transform="translate(15, 168)">
      <rect width="280" height="115" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" fill="#38bdf8" font-size="8.8" font-weight="800">② PECVD 반응가스비 &amp; Dual-Frequency RF</text>
      <text x="10" y="34" fill="#cbd5e1" font-size="7.5">• SiH₄ / NH₃ / N₂ 가스 비율을 변경하여 Si-N 결합수 조절</text>
      <text x="10" y="50" fill="#cbd5e1" font-size="7.5">• <strong>Dual Frequency RF 혼합비 제어</strong>:</text>
      <text x="16" y="64" fill="#cbd5e1" font-size="7.2">- 고주파(13.56 MHz): 플라즈마 밀도 및 화학 라디칼 생성</text>
      <text x="16" y="78" fill="#cbd5e1" font-size="7.2">- 저주파(350 kHz): 이온이 전기장 반응 ➔ 박막 강타(Ion Bombard)</text>
      <text x="10" y="96" fill="#fde047" font-size="7.8" font-weight="800">➔ 저주파 파워 비율을 높이면 인장에서 압축으로 자유 전환!</text>
      <text x="10" y="108" fill="#94a3b8" font-size="7">• 막 내부의 수소(H) 함량 정밀 제어로 응력 튜닝</text>
    </g>

    <!-- Method 3: Post Annealing -->
    <g transform="translate(15, 295)">
      <rect width="280" height="110" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" fill="#38bdf8" font-size="8.8" font-weight="800">③ 고온 포스트 어닐링 (Thermal Annealing)</text>
      <text x="10" y="34" fill="#cbd5e1" font-size="7.5">• 증착 후 고온 열처리로 내부 점결함(Defect) 및 공공 제거</text>
      <text x="10" y="50" fill="#cbd5e1" font-size="7.5">• 결정립(Grain) 재배열 및 성장으로 잔류 응력 완화</text>
      <text x="10" y="66" fill="#a7f3d0" font-size="7.8" font-weight="800">• 스토니 공식(Stoney Eq) 기반 곡률 반경(R) 실시간 피드백</text>
      <text x="10" y="82" fill="#cbd5e1" font-size="7.2">• 레이저 빔 반사각으로 웨이퍼 휨 측정 후 공정 조건 튜닝</text>
      <text x="10" y="98" fill="#fde047" font-size="7.2">➔ 두께 비례 응력 누적 방지: 다층 복합 박막 교대 적층</text>
    </g>
  </g>

  <!-- PANEL C: Strain Engineering -->
  <g transform="translate(660, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="12" font-weight="800">■ (C) 반전: 스트레인 공학 (Strain Engineering)</text>

    <!-- Concept box -->
    <g transform="translate(15, 42)">
      <rect width="270" height="175" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. NMOS: 인장 응력 (Tensile Strain SiN)</text>
      <rect x="15" y="26" width="240" height="58" rx="4" fill="#0b1329" stroke="#ef4444"/>
      <text x="22" y="42" fill="#f87171" font-size="8" font-weight="800">게이트 위에 Tensile SiN 질화막 캡핑 증착</text>
      <text x="22" y="56" fill="#cbd5e1" font-size="7.2">• 채널 방향으로 실리콘 원자 격자를 좌우로 당김</text>
      <text x="22" y="70" fill="#34d399" font-size="7.8" font-weight="800">➔ 전도대 밸리 분할로 유효질량(m*)↓, 전자 이동도 50%↑!</text>

      <text x="12" y="104" fill="#fde047" font-size="8.8" font-weight="800">2. PMOS: 압축 응력 (Embedded SiGe S/D)</text>
      <rect x="15" y="112" width="240" height="54" rx="4" fill="#0b1329" stroke="#3b82f6"/>
      <text x="22" y="128" fill="#60a5fa" font-size="8" font-weight="800">소스/드레인 영역에 격자 큰 SiGe 에피 성장</text>
      <text x="22" y="142" fill="#cbd5e1" font-size="7.2">• 실리콘 채널을 양옆에서 강하게 쥐어짜 압축</text>
      <text x="22" y="156" fill="#34d399" font-size="7.8" font-weight="800">➔ 정공 유효질량 감소 및 밴드 분할, 정공 이동도 100%↑!</text>
    </g>

    <!-- Takeaway Summary -->
    <g transform="translate(15, 230)">
      <rect width="270" height="175" rx="6" fill="#0b1329" stroke="#f59e0b"/>
      <text x="12" y="18" fill="#fbbf24" font-size="9" font-weight="800">🎯 박막 응력 제어의 양면성 총정리</text>
      <text x="12" y="38" fill="#38bdf8" font-size="7.8" font-weight="800">■ 불량 방지 관점 (반도체 수율):</text>
      <text x="16" y="52" fill="#cbd5e1" font-size="7.2">• 웨이퍼 휨(Warpage)이 심하면 노광 DOF 초점 이탈</text>
      <text x="16" y="64" fill="#cbd5e1" font-size="7.2">• 인장 응력 과다 ➔ 박막 균열 및 크랙 발생</text>
      <text x="16" y="76" fill="#cbd5e1" font-size="7.2">• 압축 응력 과다 ➔ 박막 들뜸(Peeling) 및 들림</text>
      <text x="16" y="88" fill="#fde047" font-size="7.5" font-weight="800">➔ 공정 압력·RF비 제어로 'Zero Stress' 지향!</text>

      <text x="12" y="110" fill="#38bdf8" font-size="7.8" font-weight="800">■ 소자 성능 관점 (구동 전류 혁신):</text>
      <text x="16" y="124" fill="#cbd5e1" font-size="7.2">• 90nm 노드 이후 물리적 게이트 산화막 축소 한계</text>
      <text x="16" y="136" fill="#a7f3d0" font-size="7.5" font-weight="800">• 의도적으로 국소 응력을 채널에 인가 (Strain Engineering)</text>
      <text x="16" y="148" fill="#cbd5e1" font-size="7.2">• 전자·정공 이동도를 1.5~2배 폭증시켜 Ion 구동 전류 개선</text>
      <text x="16" y="162" fill="#fde047" font-size="7.5" font-weight="800">➔ 스트레스는 '통제하면 독, 활용하면 특효약'!</text>
    </g>
  </g>
</svg>""",
    "lecture": r"""
        <!-- SECTION 2: Thin Film Stress Detailed Master Lecture -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 박막 응력(Thin Film Stress)의 기원과 본질 (열 응력 vs 내재 응력)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체 공정에서 수백 $\text{nm}$에서 수 $\mu\text{m}$ 두께의 박막(산화막, 질화막, 금속막 등)을 웨이퍼 기판 위에 증착하면, 박막과 기판의 경계면에는 서로를 당기거나 밀어내려는 거대한 <strong>기계적 탄성 변형력(Stress, $\sigma$)</strong>이 형성됩니다. 이 응력은 기가파스칼($\text{GPa}$) 수준에 달해 다이아몬드 수준의 압력에 해당합니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:800; margin-bottom:6px;">
              박막 응력을 발생시키는 2대 물리적 요인
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              1. <strong>열 응력 (Thermal Stress, $\sigma_{th}$)</strong>:
              <br>박막 증착은 고온($300\sim 800^\circ\text{C}$)에서 이루어집니다. 증착 후 상온($25^\circ\text{C}$)으로 식는 과정에서 실리콘 기판의 열팽창계수($\alpha_{si} \approx 2.6 \times 10^{-6}/\text{K}$)와 박막 재료의 열팽창계수($\alpha_f$)가 서로 달라 수축률 차이로 인해 발생합니다:
              $$\sigma_{th} = \frac{E_f}{1 - \nu_f} (\alpha_s - \alpha_f)(T_{dep} - T_{room})$$
              2. <strong>내재 응력 (Intrinsic Stress, $\sigma_i$)</strong>:
              <br>온도 변화와 무관하게 박막이 성장하는 순간 원자 단위 결함, 결정립 경계(Grain Boundary) 형성, 공공(Vacancy), 불순물 혼입 및 상변화 과정에서 발생하는 고유한 구조적 응력입니다.
            </p>
          </div>

          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin:24px 0 12px 0; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 인장 응력(Tensile) vs 압축 응력(Compressive) 비교와 웨이퍼 휨(Warpage)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            박막 응력은 작용하는 힘의 방향에 따라 크게 인장(+)과 압축(-)으로 양분되며, 웨이퍼의 거시적인 휨 형상과 불량 모드를 결정짓습니다.
          </p>

          <div style="overflow-x:auto; margin-bottom:16px;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">구분</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">박막의 힘의 방향</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">웨이퍼 휨 형태 (Warpage)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">주요 공정 불량</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">트랜지스터 응용</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#f87171;">인장 응력 (Tensile, $\sigma > 0$)</td>
                  <td style="padding:10px 14px;">박막이 원래보다 <strong>수축하려는 힘</strong> (안쪽으로 당김)</td>
                  <td style="padding:10px 14px; font-weight:800; color:#f87171;">오목하게 휨 (Smile / Bowl 형태)</td>
                  <td style="padding:10px 14px;">박막 균열(Cracking), 금속 배선 단선, 초점 심도(DOF) 불량</td>
                  <td style="padding:10px 14px; font-weight:800; color:#34d399;"><strong>NMOS 채널</strong> 전자 이동도 50% 향상</td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">압축 응력 (Compressive, $\sigma < 0$)</td>
                  <td style="padding:10px 14px;">박막이 원래보다 <strong>팽창하려는 힘</strong> (바깥으로 밂)</td>
                  <td style="padding:10px 14px; font-weight:800; color:#38bdf8;">볼록하게 휨 (Frown / Dome 형태)</td>
                  <td style="padding:10px 14px;">박막 들뜸(Peeling/Delamination), 막 주름(Buckling)</td>
                  <td style="padding:10px 14px; font-weight:800; color:#34d399;"><strong>PMOS 채널</strong> 정공 이동도 100% 향상</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin:24px 0 12px 0; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 박막 응력의 정밀 제어 3대 기법과 스트레인 공학
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            웨이퍼가 50$\mu\text{m}$ 이상 휘어지면 노광 장비에서 초점 심도(DOF)를 맞추지 못해 패턴이 뭉개지거나, CMP 연마 시 중심부와 에지의 막 두께가 달라집니다. 따라서 공정 엔지니어는 응력을 정밀 제어해야 합니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#34d399; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ① 스퍼터링 공정 압력 및 Atomic Peening 효과를 통한 응력 튜닝
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              스퍼터링 챔버의 Ar 가스 압력을 낮추면, 타깃에서 튕겨 나온 고에너지 원자들이 다른 기체와 충돌 없이 직진하여 박막 표면을 망치질하듯 강하게 때립니다(**Atomic Peening**). 이로 인해 막 내부 원자가 강제로 빽빽하게 밀어넣어지며 **압축 응력(Compressive)**이 발생합니다.
              <br>반대로 Ar 가스 압력을 높이면 입자들이 공중에서 산란되어 에너지를 잃고 성기게 쌓여 **인장 응력(Tensile)**으로 전환됩니다. 이 둘이 교차하는 최적 압력점을 찾아 **'Zero-stress(무응력)'** 박막을 구현합니다.
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #facc15; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#facc15; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ② PECVD Dual-Frequency RF 파워와 가스비 조절
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              PECVD로 SiN(질화막) 절연막을 증착할 때, 고주파(HF, 13.56MHz)는 플라즈마 화학 반응을 일으키고 저주파(LF, 350kHz)는 무거운 이온을 웨이퍼로 가속시킵니다.
              저주파 RF 파워 비율을 높이면 이온 충돌이 거세져 막이 치밀해지며 압축 응력으로 이동하고, $\text{SiH}_4/\text{NH}_3$ 가스 비율을 조절해 Si-H 결합과 N-H 결합 수를 제어하여 인장 응력 박막을 자유자재로 합성합니다.
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #8b5cf6; padding:16px 20px; border-radius:0 8px 8px 0;">
            <h4 style="color:#c084fc; font-size:1rem; font-weight:800; margin-bottom:6px;">
              ③ 스트레인 엔지니어링 (Strain Engineering): 불량을 기적으로 바꾼 소자 혁신
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              90nm 노드 이후 게이트 절연막 두께($t_{ox}$)가 양자 터널링 한계에 부딪혔을 때, 인텔은 응력을 소자 채널에 일부러 가해 성능을 끌어올리는 기술을 도입했습니다:
              <br>• <strong>NMOS</strong>: 게이트 상단에 강한 인장 응력을 가진 SiN 막(Tensile Capping)을 덮어 채널 격자를 수평으로 늘립니다. 실리콘 전도대 밸리의 에너지 축퇴가 깨져 전자의 유효 질량($m^*$)이 가벼워지고 밸리 간 산란이 줄어 **전자 이동도($\mu_n$)가 50% 이상 급증**합니다.
              <br>• <strong>PMOS</strong>: 소스와 드레인 실리콘을 파내고 실리콘보다 격자 상수가 4% 큰 SiGe(실리콘-게르마늄)을 선택적 에피 성장(e-SiGe)시킵니다. 커다란 SiGe가 채널 실리콘을 양옆에서 쥐어짜는 강한 압축 응력을 가해 가전자대 중정공/경정공 밴드를 분할하여 **정공 이동도($\mu_p$)를 2배 폭증**시킵니다!
            </p>
          </div>
        </div>
    """
}

TOPIC_3 = {
    "id": "q-03",
    "num": "03",
    "badge": "⭐ 최신 질문 (BEOL 금속 배선 공정 · Al vs Cu 물성 비교, 건식 식각 한계와 듀얼 다마신 혁신)",
    "title": "알루미늄(Al)과 구리(Cu)를 사용했을 때 장단점 완전 비교 (비저항, EM 신뢰성, 듀얼 다마신 공정)",
    "nav_title": "알루미늄과 구리를 사용했을 때 장단점",
    "summary": [
        "<strong>1. 전기적 비저항 및 RC 지연 ($1.7$ vs $2.7\\,\\mu\\Omega\\cdot\\text{cm}$)</strong>: 구리(Cu)는 알루미늄(Al) 대비 비저항이 약 40% 낮아 고밀도 미세 배선에서 RC 신호 지연을 획기적으로 줄이고 고주파 클록 주파수 달성을 가능하게 합니다.",
        "<strong>2. 일렉트로마이그레이션(EM) 신뢰성의 압도적 차이</strong>: Cu는 녹는점($1085^\\circ\\text{C}$)이 Al($660^\\circ\\text{C}$)보다 훨씬 높아 원자 결합 에너지가 강하며, 고전류 밀도에서 전자 바람에 의한 금속 원자 이동(단선 및 쇼트) 저항성이 10~100배 우수합니다.",
        "<strong>3. 식각 공정의 결정적 한계와 듀얼 다마신(Dual Damascene)</strong>: Al은 휘발성 $\\text{AlCl}_3$를 형성해 RIE 플라즈마 건식 식각이 쉬운 반면, Cu는 상온에서 휘발성 반응물이 없어 건식 식각이 불가능합니다. 이로 인해 절연막에 트렌치/비아를 먼저 파고 구리를 도금한 뒤 연마하는 듀얼 다마신 CMP 공정이 도입되었습니다.",
        "<strong>4. 산화 특성 및 배리어 요건에 따른 현대적 분업</strong>: Cu는 Si 및 $\\text{SiO}_2$로 급격히 확산되어 Ta/TaN 배리어가 필수적이며 다공성 산화막으로 부식에 취약합니다. 반면 Al은 치밀한 자가보호 산화막($\\text{Al}_2\\text{O}_3$)을 형성하므로 외부 본딩 패드(Top Metal Pad)에 표준으로 사용되어 상호 보완적으로 공존합니다."
    ],
    "svg_title": "📊 [알루미늄 vs 구리 배선 종합 비교 다이어그램] (A) 전기적 물성 및 EM 신뢰성 대결 | (B) 패터닝 공정 방식 (감산 식각 vs 듀얼 다마신) | (C) 현대 반도체 내 역할 분담",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Physical Properties & Reliability -->
  <g transform="translate(20, 20)">
    <rect width="295" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 전기적 물성과 EM 신뢰성 대결</text>

    <!-- Resistivity Card -->
    <g transform="translate(15, 42)">
      <rect width="265" height="115" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 비저항 (Resistivity) &amp; RC 지연시간</text>
      <text x="10" y="34" fill="#cbd5e1" font-size="7.5">• <strong>알루미늄 (Al)</strong>: ρ = 2.7 μΩ·cm</text>
      <text x="16" y="48" fill="#f87171" font-size="7.2">미세화 시 저항 급증 → 신호 지연(RC Delay) 병목 심각</text>
      <text x="10" y="66" fill="#cbd5e1" font-size="7.5">• <strong>구리 (Cu)</strong>: ρ = 1.7 μΩ·cm</text>
      <text x="16" y="80" fill="#34d399" font-size="7.8" font-weight="800">Al 대비 비저항 약 40% 감소! (초고속 신호 전송)</text>
      <text x="10" y="98" fill="#cbd5e1" font-size="7.2">• 고속 CPU/GPU 클록 주파수 한계 돌파의 1등 공신</text>
      <text x="10" y="110" fill="#94a3b8" font-size="7">• 은(Ag, 1.6) 다음으로 지구상 2위의 전도체</text>
    </g>

    <!-- EM Reliability Card -->
    <g transform="translate(15, 168)">
      <rect width="265" height="130" rx="5" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="18" fill="#fde047" font-size="8.8" font-weight="800">2. 일렉트로마이그레이션 (EM 신뢰성)</text>
      <text x="10" y="34" fill="#cbd5e1" font-size="7.5">• 고전류 밀도에서 '전자 바람'에 원자가 밀리는 현상</text>
      <text x="10" y="50" fill="#fca5a5" font-size="7.5">• <strong>알루미늄 (Al)</strong>: 융점 660℃</text>
      <text x="16" y="64" fill="#cbd5e1" font-size="7.2">낮은 녹는점으로 원자 이동 활발 ➔ 보이드(단선), 힐록(쇼트)</text>
      <text x="10" y="82" fill="#34d399" font-size="7.5" font-weight="800">• <strong>구리 (Cu)</strong>: 융점 1085℃</text>
      <text x="16" y="96" fill="#34d399" font-size="7.5" font-weight="800">높은 융점으로 금속 원자 결합 강력 (활성화 에너지 2배!)</text>
      <text x="10" y="112" fill="#fde047" font-size="7.8" font-weight="800">➔ 동일 전류에서 Cu가 Al 대비 EM 수명 10~100배 우수!</text>
      <text x="10" y="124" fill="#94a3b8" font-size="7">• 미세 배선의 고전류 밀도(10⁶ A/cm²) 버티는 유일한 해법</text>
    </g>

    <!-- Barrier & Diffusion -->
    <rect x="15" y="310" width="265" height="95" rx="5" fill="#0b1329" stroke="#38bdf8"/>
    <text x="18" y="328" fill="#38bdf8" font-size="8.5" font-weight="800">3. 실리콘/산화막 확산성 (치명적 단점)</text>
    <text x="18" y="344" fill="#cbd5e1" font-size="7.2">• Al: Si-Al 반응(스파이킹) 방지용 TiN으로 충분</text>
    <text x="18" y="358" fill="#f87171" font-size="7.5" font-weight="800">• Cu: Si와 SiO₂ 내부로 초고속 확산 (Deep Level Trap 유발)</text>
    <text x="18" y="372" fill="#fde047" font-size="7.5" font-weight="800">➔ Ta/TaN 배리어 메탈로 4면을 완전히 포위 밀봉 필수!</text>
    <text x="18" y="388" fill="#cbd5e1" font-size="7">• 배리어 미흡 시 소자 누설전류 폭발로 칩 전체 폐기</text>
  </g>

  <!-- PANEL B: Patterning Process (RIE vs Dual Damascene) -->
  <g transform="translate(330, 20)">
    <rect width="320" height="420" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.2"/>
    <text x="16" y="26" fill="#f87171" font-size="12" font-weight="800">■ (B) 패터닝 공정 혁신 (감산 식각 vs 다마신)</text>

    <!-- Sub 1: Al Subtractive RIE -->
    <g transform="translate(15, 42)">
      <rect width="290" height="155" rx="6" fill="#1e293b" stroke="#34d399"/>
      <text x="12" y="18" fill="#34d399" font-size="8.8" font-weight="800">1. Al 공정: 감산 방식 (Subtractive RIE 식각)</text>
      
      <!-- Visual flow -->
      <g transform="translate(10, 26)">
        <rect width="270" height="56" rx="4" fill="#0b1329" stroke="#334155"/>
        <text x="10" y="16" fill="#cbd5e1" font-size="7.2">[Al 전면 증착] ➔ [포토레지스트 패터닝] ➔ [플라즈마 RIE 식각]</text>
        <text x="10" y="32" fill="#34d399" font-size="7.5" font-weight="800">★ 건식 식각 가능 이유: 휘발성 AlCl₃ (끓는점 180℃)</text>
        <text x="10" y="46" fill="#cbd5e1" font-size="7">반응 부산물이 기체로 기화되어 챔버 밖으로 쉽게 날아감!</text>
      </g>

      <text x="12" y="98" fill="#cbd5e1" font-size="7.5">• 장점: 배선 형성 공정이 단순하고 직관적임</text>
      <text x="12" y="112" fill="#cbd5e1" font-size="7.5">• 식각 후 절연막(ILD)을 틈새에 채우는 방식</text>
      <text x="12" y="126" fill="#fca5a5" font-size="7.5">• 한계: 미세 배선에서 Aspect Ratio 증가로 절연막 갭필 불량</text>
      <text x="12" y="140" fill="#94a3b8" font-size="7">• 0.18㎛ 이하 초미세 노드에서는 적용 불가능</text>
    </g>

    <!-- Sub 2: Cu Dual Damascene -->
    <g transform="translate(15, 208)">
      <rect width="290" height="198" rx="6" fill="#1e293b" stroke="#ef4444"/>
      <text x="12" y="18" fill="#f87171" font-size="8.8" font-weight="800">2. Cu 공정: 듀얼 다마신 (Dual Damascene + CMP)</text>
      
      <!-- Visual flow -->
      <g transform="translate(10, 26)">
        <rect width="270" height="68" rx="4" fill="#0b1329" stroke="#ef4444"/>
        <text x="10" y="16" fill="#fca5a5" font-size="7.2" font-weight="800">★ 구리는 플라즈마 건식 식각이 불가능! (CuCl 융점 &gt; 400℃)</text>
        <text x="10" y="30" fill="#cbd5e1" font-size="7">상온에서 구리 염화물이 증발하지 않아 찌꺼기로 표면에 들러붙음</text>
        <text x="10" y="46" fill="#fde047" font-size="7.5" font-weight="800">➔ 해법: '도랑(Trench/Via)을 먼저 파고 구리를 채운다!'</text>
        <text x="10" y="60" fill="#cbd5e1" font-size="6.8">(상감 기법: 금속을 파내는 대신 바탕을 파고 메우는 혁신)</text>
      </g>

      <text x="12" y="110" fill="#cbd5e1" font-size="7.5">• <strong>다마신 4대 단계</strong>:</text>
      <text x="18" y="124" fill="#cbd5e1" font-size="7.2">① 절연막에 비아(Via) 및 트렌치(Trench) 식각</text>
      <text x="18" y="136" fill="#cbd5e1" font-size="7.2">② Ta/TaN 배리어 및 Cu 씨앗층(Seed) 증착</text>
      <text x="18" y="148" fill="#cbd5e1" font-size="7.2">③ 전기도금(ECD)으로 구리를 과잉 충진</text>
      <text x="18" y="160" fill="#38bdf8" font-size="7.5" font-weight="800">④ 화학기계적 연마(CMP)로 표면 잉여 구리 완벽 제거</text>
      <text x="12" y="178" fill="#fde047" font-size="7.8" font-weight="800">➔ IBM이 1997년 최초 상용화한 현대 반도체의 표준 배선 기법!</text>
      <text x="12" y="190" fill="#94a3b8" font-size="7">• 비아와 트렌치를 한 번에 채워 공정 수 절감 (듀얼 다마신)</text>
    </g>
  </g>

  <!-- PANEL C: Coexistence & Modern Strategy -->
  <g transform="translate(665, 20)">
    <rect width="295" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="16" y="26" fill="#fbbf24" font-size="12" font-weight="800">■ (C) 현대 반도체 칩에서 두 금속의 분업</text>

    <!-- Comparison Table in Panel C -->
    <g transform="translate(15, 42)">
      <rect width="265" height="185" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">산화막 특성 및 부식 내구성 대결</text>

      <g transform="translate(10, 26)">
        <rect width="245" height="68" rx="4" fill="#0b1329" stroke="#34d399"/>
        <text x="8" y="16" fill="#34d399" font-size="8" font-weight="800">■ 알루미늄 (Al): 자가보호 산화막</text>
        <text x="14" y="32" fill="#cbd5e1" font-size="7.2">• 공기 노출 즉시 3~4nm의 치밀한 Al₂O₃ 산화막 자생</text>
        <text x="14" y="46" fill="#cbd5e1" font-size="7.2">• 산소가 내부로 침투하지 못해 추가 부식 완전 차단!</text>
        <text x="14" y="60" fill="#34d399" font-size="7.5" font-weight="800">➔ 패키징 와이어 본딩 패드로 최고의 내구성 발휘</text>
      </g>

      <g transform="translate(10, 102)">
        <rect width="245" height="72" rx="4" fill="#0b1329" stroke="#ef4444"/>
        <text x="8" y="16" fill="#f87171" font-size="8" font-weight="800">■ 구리 (Cu): 다공성 산화막</text>
        <text x="14" y="32" fill="#cbd5e1" font-size="7.2">• 구리 산화물(CuO, Cu₂O)은 틈새가 많은 다공성 구조</text>
        <text x="14" y="46" fill="#cbd5e1" font-size="7.2">• 산소가 계속 파고들어 내부 구리가 끝없이 산화·부식</text>
        <text x="14" y="60" fill="#fca5a5" font-size="7.5" font-weight="800">➔ 공기 중에 노출되는 최상단 패드로는 부적합!</text>
      </g>
    </g>

    <!-- Modern Architecture -->
    <g transform="translate(15, 238)">
      <rect width="265" height="168" rx="6" fill="#0b1329" stroke="#f59e0b"/>
      <text x="12" y="18" fill="#fbbf24" font-size="8.8" font-weight="800">★ 현대 반도체의 스마트 분업 전략</text>

      <text x="12" y="38" fill="#38bdf8" font-size="8" font-weight="800">1. 내부 다층 배선 (M1 ~ M10 이상): 100% Cu</text>
      <text x="18" y="52" fill="#cbd5e1" font-size="7.2">• 칩 내부의 고밀도 트랜지스터 연결</text>
      <text x="18" y="64" fill="#cbd5e1" font-size="7.2">• 듀얼 다마신 공정 + Low-k 절연막(SiCOH)</text>
      <text x="18" y="76" fill="#34d399" font-size="7.5" font-weight="800">➔ 최고 속도(RC↓)와 고전류 신뢰성(EM↑) 담당</text>

      <text x="12" y="98" fill="#fde047" font-size="8" font-weight="800">2. 최상층 본딩 패드 (Top Metal Pad): Al</text>
      <text x="18" y="112" fill="#cbd5e1" font-size="7.2">• 외부 패키지 본딩 와이어(Au/Cu wire)와 접합되는 창구</text>
      <text x="18" y="124" fill="#cbd5e1" font-size="7.2">• 공기 노출 시 자가보호 Al₂O₃ 덕분에 부식에 무적</text>
      <text x="18" y="136" fill="#cbd5e1" font-size="7.2">• 와이어 본딩 시 기계적 압착 접착력이 탁월</text>
      <text x="12" y="156" fill="#a7f3d0" font-size="7.8" font-weight="800">➔ 내부 고속도로는 Cu, 외부 관문은 Al의 아름다운 공존!</text>
    </g>
  </g>
</svg>""",
    "lecture": r"""
        <!-- SECTION 3: Aluminum vs Copper Detailed Master Lecture -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 반도체 배선의 역사적 전환과 구리(Cu)의 필연성
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체 금속 배선(Interconnect)은 1960년대 집적회로 발명 이래 1990년대 후반(0.18$\mu$m 노드)까지 <strong>알루미늄(Al)</strong>이 독점적 표준이었습니다. 
            하지만 트랜지스터 크기가 나노미터 단위로 축소되면서 소자 자체의 스위칭 속도보다 <strong>신호가 금속선을 통과할 때 걸리는 RC 지연 시간($\tau = R \times C$)이 칩 전체 속도를 갉아먹는 치명적인 병목 현상</strong>이 발생했습니다. 
            이를 타파하기 위해 1997년 IBM이 업계 최초로 **구리(Cu) 배선 기술**을 발표하며 반도체 배선 혁명이 시작되었습니다.
          </p>

          <div style="overflow-x:auto; margin-bottom:16px;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">비교 지표</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">알루미늄 (Al)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">구리 (Cu)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">반도체 관점 핵심 의미</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">비저항 (Resistivity)</td>
                  <td style="padding:10px 14px; color:#f87171;">$2.7\,\mu\Omega\cdot\text{cm}$</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:800;">$1.7\,\mu\Omega\cdot\text{cm}$</td>
                  <td style="padding:10px 14px;"><strong>Cu가 저항 40% 낮음</strong> ➔ RC 신호 지연 단축, 클록 주파수 향상</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">융점 (Melting Point)</td>
                  <td style="padding:10px 14px; color:#f87171;">$660^\circ\text{C}$</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:800;">$1085^\circ\text{C}$</td>
                  <td style="padding:10px 14px;">Cu의 원자간 결합력 훨씬 견고 ➔ 열적 내구성 탁월</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">일렉트로마이그레이션 (EM)</td>
                  <td style="padding:10px 14px; color:#f87171;">취약 (활성화 에너지 $0.5\sim 0.7\,\text{eV}$)</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:800;">압도적 우수 ($0.9\sim 1.1\,\text{eV}$)</td>
                  <td style="padding:10px 14px;">동일 전류 밀도에서 <strong>Cu의 수명이 10~100배 길어</strong> 단선 방지</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">건식 RIE 플라즈마 식각</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:800;"><strong>매우 쉬움</strong> ($\text{AlCl}_3$ 증기압 높음)</td>
                  <td style="padding:10px 14px; color:#f87171; font-weight:800;"><strong>물리적 불가</strong> (상온 휘발성 염화물 부재)</td>
                  <td style="padding:10px 14px;">Al은 감산 식각 가능 vs <strong>Cu는 다마신(Damascene) 필수</strong></td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">실리콘 및 절연막 확산</td>
                  <td style="padding:10px 14px;">확산 완만 (Ti/TiN으로 충분)</td>
                  <td style="padding:10px 14px; color:#f87171;">극도로 빠름 (소자 파괴자)</td>
                  <td style="padding:10px 14px;"><strong>Cu는 Ta/TaN 4면 배리어 메탈 필수</strong> (공정 난이도 상승)</td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#fde047;">공기 노출 시 자가산화</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:800;">치밀한 $\text{Al}_2\text{O}_3$ 형성 (부식 완전 방어)</td>
                  <td style="padding:10px 14px; color:#f87171;">다공성 $\text{CuO}$ 형성 (지속적 산화 부식)</td>
                  <td style="padding:10px 14px;"><strong>최상단 본딩 패드는 Al이 표준</strong>으로 유지되는 이유</td>
                </tr>
              </tbody>
            </table>
          </div>

          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin:24px 0 12px 0; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 결정적 공정 차이: 왜 구리는 식각하지 않고 '도랑을 파서 채우는가?' (다마신 혁신)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            금속 배선을 만들 때 알루미늄은 금속을 먼저 평평하게 깔고 필요 없는 부분을 염소($\text{Cl}_2$) 플라즈마로 깎아내는 <strong>감산 식각(Subtractive Etch)</strong>을 씁니다.
            그 이유는 염소와 알루미늄이 만나 생기는 $\text{AlCl}_3$가 끓는점이 $180^\circ\text{C}$로 낮아 플라즈마 챔버의 열과 진공에 의해 가스로 기화되어 날아가기 때문입니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #ef4444; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#f87171; font-size:1rem; font-weight:800; margin-bottom:6px;">
              구리의 치명적 난제: 휘발성 화합물의 부재 ($\text{CuCl}$ 끓는점 $> 1400^\circ\text{C}$)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              반면 구리는 염소 플라즈마와 반응하면 $\text{CuCl}$이나 $\text{CuCl}_2$를 만드는데, 이 화합물들은 끓는점이 $1400^\circ\text{C}$ 이상으로 너무 높아 상온에서 증발하지 않는 끈적끈적한 고체로 표면에 달라붙어 플라즈마 식각이 원천적으로 불가능합니다!
              <br>이 문제를 해결하기 위해 반도체 엔지니어들은 고대 상감 기법(Damascene)에서 영감을 얻었습니다:
              <br><strong>"구리를 깎아낼 수 없다면, 절연막에 도랑(Trench)과 구멍(Via)을 먼저 파놓고, 그 안에 구리를 전기도금으로 부어 넣은 뒤, 위로 튀어나온 잉여 구리를 기계적으로 갈아내자(CMP)!"</strong>
              <br>이것이 바로 현대 반도체 백엔드 공정(BEOL)의 핵심인 **듀얼 다마신(Dual Damascene)** 공정입니다.
            </p>
          </div>

          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin:24px 0 12px 0; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 현대 칩에서의 공존과 역할 분담: 내부 초고속 Cu vs 외부 관문 Al
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            그렇다면 알루미늄은 완전히 사라졌을까요? 아닙니다. 두 금속은 각자의 고유한 물성에 맞게 완벽한 분업을 이루고 있습니다:
          </p>

          <div style="background:#1e293b; padding:16px 20px; border-radius:8px;">
            <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:20px; margin:0;">
              <li><strong style="color:#38bdf8;">내부 미세 다층 배선 (M1 ~ M10 이상)</strong>:
                <br>초고속 신호 전송과 높은 전류 밀도를 견뎌야 하므로 **100% 구리(Cu) 듀얼 다마신 공정**과 Low-k 절연막을 적용합니다. Ta/TaN 배리어 메탈로 구리의 확산을 완벽히 틀어막습니다.
              </li>
              <li><strong style="color:#fde047;">최상단 본딩 패드 (Top Metal Pad)</strong>:
                <br>외부 패키지와 본딩 와이어로 연결되는 최상단 패드는 **알루미늄(Al)**이 표준으로 사용됩니다. 구리는 공기 중에 두면 다공성 녹이 슬어 부식되지만, 알루미늄은 공기에 닿는 순간 원자 단위로 치밀한 $\text{Al}_2\text{O}_3$ 자가보호 산화막을 형성해 부식을 영구 차단하며, 와이어 본딩 압착 시 접합 신뢰성이 월등하기 때문입니다.
              </li>
            </ul>
          </div>
        </div>
    """
}

def update_html_file(file_path):
    print(f"Reading {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing topics Q02..Q93 to Q04..Q95 (old_n -> old_n + 2)
    # We do it descending from 93 down to 2
    for old_n in range(93, 1, -1):
        new_n = old_n + 2
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

    # Step 2: Remove old single combined Q01 nav-item and section
    # Remove nav item
    html = re.sub(
        r'<li class="nav-item"><a href="#q-01" class="nav-link"><span class="nav-num">01</span><span class="nav-text">.*?</span></a></li>\n?',
        '',
        html
    )

    # Remove old Q01 section
    html = re.sub(
        r'<!-- Q 01 : EUV 광학계의 반사 미러 전용 이유, 박막 응력.*?-->\s*<section class="topic-section latest-card-highlight" id="q-01">.*?</section>\s*(?=<!-- Q 0[1-4]|\s*<section)',
        '',
        html,
        flags=re.DOTALL
    )

    # Step 3: Insert 3 new nav items at the top of nav-list
    new_nav_items = (
        f'      <li class="nav-item"><a href="#{TOPIC_1["id"]}" class="nav-link"><span class="nav-num">{TOPIC_1["num"]}</span><span class="nav-text">{TOPIC_1["nav_title"]}</span></a></li>\n'
        f'      <li class="nav-item"><a href="#{TOPIC_2["id"]}" class="nav-link"><span class="nav-num">{TOPIC_2["num"]}</span><span class="nav-text">{TOPIC_2["nav_title"]}</span></a></li>\n'
        f'      <li class="nav-item"><a href="#{TOPIC_3["id"]}" class="nav-link"><span class="nav-num">{TOPIC_3["num"]}</span><span class="nav-text">{TOPIC_3["nav_title"]}</span></a></li>\n'
    )
    nav_list_pos = html.find('<ul class="nav-list" id="navList">')
    if nav_list_pos != -1:
        insert_nav = nav_list_pos + len('<ul class="nav-list" id="navList">\n')
        html = html[:insert_nav] + new_nav_items + html[insert_nav:]

    # Step 4: Build 3 new section blocks
    def make_section(topic, is_latest=False):
        cls = "topic-section latest-card-highlight" if is_latest else "topic-section"
        summary_lis = "\n".join([f"          <li>{s}</li>" for s in topic["summary"]])
        return f"""
    <!-- Q {topic['num']} : {topic['title']} -->
    <section class="{cls}" id="{topic['id']}">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q {topic['num']}</span>
          <span class="latest-tag">{topic['badge']}</span>
          <h2 class="topic-title">{topic['title']}</h2>
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
            {topic['svg_title']}
          </div>
          {topic['svg']}
        </div>
        {topic['lecture']}
      </div>
    </section>
"""

    all_3_sections = make_section(TOPIC_1, is_latest=True) + make_section(TOPIC_2, is_latest=False) + make_section(TOPIC_3, is_latest=False)

    main_header_end = html.find("</header>")
    if main_header_end != -1:
        insert_sec = main_header_end + len("</header>")
        html = html[:insert_sec] + "\n" + all_3_sections + html[insert_sec:]

    # Step 5: Update header text description to 95 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 'EUV 미러 광학계(Q01) / 박막 응력 제어(Q02) / Al vs Cu 배선(Q03)'이 위치하며, 총 95개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    for p in [r"C:\Work\반도체3\result\261007_v1.0\index.html", r"C:\Work\반도체3\index.html"]:
        update_html_file(p)
    print("All HTML files processed!")
