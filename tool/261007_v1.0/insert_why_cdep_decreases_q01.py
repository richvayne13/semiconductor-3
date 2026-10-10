# -*- coding: utf-8 -*-
"""
insert_why_cdep_decreases_q01.py
사용자 질문: "body가 얇아지면 왜 Cdep가 작아져"
대시보드 최상단 Q01로 신규 추가하고, 기존 83개 질문을 Q02~Q84로 시프트 (총 84개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 커패시턴스 물리 · FD-SOI 핵심)",
    "title": "Body(바디 두께)가 얇아지면 왜 Cdep(공핍 커패시턴스)가 작아질까? (C = dQ/dV 본질, 전하 포화, BOX 직렬 결합)",
    "nav_title": "Body가 얇아지면 왜 Cdep가 작아질까? (C=dQ/dV 본질, BOX 직렬)",
    "summary": [
        "<strong>1. 직관의 역설 해소 ('C = ε/d' 평행판 공식의 함정)</strong>: 두께($d$)가 얇아지면 커패시턴스가 커져야 할 것 같지만, 커패시턴스의 물리학적 진짜 정의는 <strong>'전압이 변할 때 전하량이 얼마나 변하는가($C = \\frac{dQ}{dV}$)'</strong>입니다. 바디가 얇아져 바디 전체가 100% 완전 공핍화(Fully Depleted)되면, 바디 내부의 공핍 전하는 $Q_{dep} = q N_A T_{body}$로 <strong>이미 한계치에 도달해 꽁꽁 얼어붙듯 고정(Saturated & Fixed)</strong>됩니다.",
        "<strong>2. 추가 전하 변조의 소멸 (dQ/dψ ≈ 0)</strong>: 게이트 전압을 더 올려도 바디 안에 더 이상 밀어낼 캐리어나 이온화될 원자가 물리적으로 남아있지 않으므로, <strong>전압 변화에 따른 공핍 전하의 변화량($\\frac{dQ_{dep}}{d\\psi_s}$)이 거의 '0'으로 수렴</strong>하여 $C_{dep} \\approx 0$이 됩니다.",
        "<strong>3. 두꺼운 매립 산화막(BOX)과의 직렬 연결 효과</strong>: FD-SOI에서는 얇은 실리콘 바디 밑에 <strong>두껍고($t_{BOX} \\gg W_{dep}$) 유전율이 3배 낮은($\\epsilon_{ox} = 3.9$) 매립 산화막(BOX)이 직렬</strong>로 깔려 있습니다. 등가 정전용량 공식 $\\frac{1}{C_{eff}} = \\frac{T_{si}}{\\epsilon_{si}} + \\frac{t_{BOX}}{\\epsilon_{ox}}$에 의해 작은 BOX 정전용량이 전체를 지배하여 <strong>등가 커패시턴스가 기존 벌크 대비 수십 분의 1로 급감</strong>합니다.",
        "<strong>4. 무도핑 채널(Undoped Channel) 실현</strong>: 바디가 얇아지면 기하학적 구조만으로 단채널 효과를 100% 막아내므로 <strong>채널에 불순물 도핑을 전혀 하지 않습니다($N_A \\approx 0$)</strong>. 공간 전하 자체가 없으므로 $Q_{dep} = 0 \\implies C_{dep} = 0$이 되어 <strong>서브스레시홀드 스윙이 이상치인 $SS \\approx 60\\text{mV/dec}$로 완벽 복원</strong>됩니다."
    ],
    "svg_title": "📊 [바디 축소 시 Cdep 감소 메커니즘] (A) 커패시턴스의 본질(C = dQ/dψ)과 전하 포화 | (B) BOX 산화막 직렬 결합 모델 | (C) 무도핑 채널과 SS 60 복원",
    "svg": """<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: The Physics of C = dQ/dV and Charge Saturation -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 커패시턴스의 본질: C = dQ/dψ</text>

    <!-- Sub-case 1: Thick Bulk (Charge can increase freely) -->
    <g transform="translate(15, 42)">
      <rect width="270" height="135" rx="5" fill="#1e293b" stroke="#ef4444"/>
      <text x="10" y="16" fill="#f87171" font-size="9" font-weight="800">1. 벌크(Bulk): 공핍층이 무한히 팽창 가능</text>
      <!-- Gate -->
      <rect x="85" y="24" width="100" height="10" fill="#64748b" rx="1"/>
      <text x="120" y="32" fill="#fff" font-size="7">Gate</text>
      <!-- Depletion Region growing with VG -->
      <rect x="40" y="36" width="190" height="35" fill="#0284c7" opacity="0.6"/>
      <text x="85" y="56" fill="#fff" font-size="8" font-weight="800">W_dep(VG) 계속 증가 가능</text>
      <!-- Deep Bulk -->
      <rect x="40" y="71" width="190" height="35" fill="#047857" opacity="0.3"/>
      <text x="80" y="90" fill="#94a3b8" font-size="7.5">기판에 실리콘 원자 무한 공급</text>
      <!-- Arrows -->
      <text x="10" y="118" fill="#fca5a5" font-size="7.5">• VG 증가 ➔ 공핍 전하 Q_dep가 계속 불어남 (dQ &gt; 0)</text>
      <text x="10" y="130" fill="#fde047" font-size="8" font-weight="800">➔ C_dep = dQ_dep / dψs = ε_si / W_dep (큼!)</text>
    </g>

    <!-- Sub-case 2: Ultra-Thin Body (FD-SOI: Charge Saturated!) -->
    <g transform="translate(15, 188)">
      <rect width="270" height="140" rx="5" fill="#1e293b" stroke="#10b981"/>
      <text x="10" y="16" fill="#34d399" font-size="9" font-weight="800">2. 박막 바디 (FD-SOI): 전하가 이미 포화 고정!</text>
      <!-- Gate -->
      <rect x="85" y="24" width="100" height="10" fill="#38bdf8" rx="1"/>
      <text x="120" y="32" fill="#000" font-size="7">Gate</text>
      <!-- Ultra-thin silicon fully depleted -->
      <rect x="40" y="36" width="190" height="15" fill="#10b981" rx="1"/>
      <text x="50" y="47" fill="#fff" font-size="7.5" font-weight="900">T_body ≈ 5nm (100% 완전 공핍화!)</text>
      <!-- BOX Barrier -->
      <rect x="40" y="53" width="190" height="40" fill="#334155" stroke="#10b981" stroke-dasharray="2,2"/>
      <text x="65" y="76" fill="#38bdf8" font-size="8" font-weight="700">BOX 산화막 계면 (벽에 막힘!)</text>
      <!-- Text explanation -->
      <text x="10" y="106" fill="#a7f3d0" font-size="7.5">★ 실리콘이 5nm뿐이라 더 이상 비울 전하가 없음!</text>
      <text x="10" y="120" fill="#cbd5e1" font-size="7.5">• Q_dep = q · NA · T_body (최대치로 상한선 고정!)</text>
      <text x="10" y="134" fill="#34d399" font-size="8" font-weight="800">➔ dQ_dep / dψs ≈ 0 ➔ C_dep ≈ 0 수렴!</text>
    </g>

    <!-- Formula Summary Box -->
    <rect x="15" y="338" width="270" height="68" rx="6" fill="#0b1329" stroke="#334155"/>
    <text x="22" y="358" fill="#38bdf8" font-size="8.8" font-weight="800">직관의 역설 해소 핵심:</text>
    <text x="22" y="375" fill="#cbd5e1" font-size="8">• 커패시턴스는 전하량 자체가 아니라 '변화율(dQ/dV)'!</text>
    <text x="22" y="392" fill="#fde047" font-size="8">• 전하가 벽에 부딪혀 고정되므로 C_dep = 0!</text>
  </g>

  <!-- PANEL B: Series Combination with Thick BOX Oxide -->
  <g transform="translate(340, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 매립 산화막(BOX) 직렬 연결 모델</text>

    <!-- Capacitor Series Circuit Diagram -->
    <g transform="translate(15, 42)">
      <rect width="280" height="175" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="9.5" font-weight="800">FD-SOI의 3중 직렬 커패시터 등가 회로</text>

      <g transform="translate(40, 30)">
        <!-- Gate Node -->
        <circle cx="100" cy="15" r="3" fill="#fff"/>
        <text x="110" y="18" fill="#fff" font-size="7.5">Gate (VG)</text>
        <line x1="100" y1="18" x2="100" y2="28" stroke="#94a3b8"/>

        <!-- Cox -->
        <rect x="80" y="28" width="40" height="10" fill="#a855f7"/>
        <text x="88" y="36" fill="#fff" font-size="7">Cox (산화막)</text>
        <line x1="100" y1="38" x2="100" y2="48" stroke="#94a3b8"/>

        <!-- C_si (Thin silicon body) -->
        <rect x="80" y="48" width="40" height="10" fill="#10b981"/>
        <text x="86" y="56" fill="#000" font-size="7" font-weight="800">C_si (5nm)</text>
        <line x1="100" y1="58" x2="100" y2="68" stroke="#94a3b8"/>

        <!-- C_BOX (Thick oxide) -->
        <rect x="75" y="68" width="50" height="14" fill="#38bdf8"/>
        <text x="79" y="78" fill="#000" font-size="7.5" font-weight="800">C_BOX (두껍다!)</text>
        <line x1="100" y1="82" x2="100" y2="95" stroke="#94a3b8"/>

        <!-- Substrate GND -->
        <line x1="90" y1="95" x2="110" y2="95" stroke="#fff" stroke-width="1.5"/>
        <text x="115" y="98" fill="#94a3b8" font-size="7">Substrate</text>
      </g>

      <text x="12" y="150" fill="#cbd5e1" font-size="8">■ 바디 등가 용량: 1/C_body = (T_si/ε_si) + (t_BOX/ε_ox)</text>
      <text x="12" y="165" fill="#fde047" font-size="8.5" font-weight="700">➔ 두꺼운 t_BOX와 낮은 ε_ox(3.9)가 직렬을 지배!</text>
    </g>

    <!-- Formula & Explanation Box -->
    <g transform="translate(15, 228)">
      <rect width="280" height="178" rx="6" fill="#0b1329" stroke="#334155"/>
      <text x="12" y="18" fill="#34d399" font-size="9" font-weight="800">★ 왜 직렬 연결에서 전체 용량이 작아질까?</text>
      <text x="12" y="38" fill="#cbd5e1" font-size="8.5">• 두 커패시터가 직렬로 연결되면:</text>
      <text x="20" y="54" fill="#ffffff" font-size="9">C_total = (C_si · C_BOX) / (C_si + C_BOX)</text>
      
      <text x="12" y="74" fill="#cbd5e1" font-size="8.2">• 직렬 합성 용량은 둘 중 **'더 작은 쪽'보다 작아짐**!</text>
      <text x="12" y="92" fill="#bae6fd" font-size="8">• BOX 산화막 두께 t_BOX ≈ 25~100nm로 매우 두꺼움:</text>
      <text x="20" y="106" fill="#38bdf8" font-size="8">➔ C_BOX = ε_ox / t_BOX (극도로 작은 값!)</text>

      <text x="12" y="126" fill="#cbd5e1" font-size="8">• 결과적으로 게이트가 바라보는 바디 용량은:</text>
      <text x="20" y="142" fill="#fde047" font-size="8.8" font-weight="800">C_body,eff ≈ C_BOX ≪ C_dep,bulk</text>
      <text x="12" y="162" fill="#a7f3d0" font-size="8">➔ 기존 벌크 공핍 용량 대비 10분의 1 이하로 폭락!</text>
    </g>
  </g>

  <!-- PANEL C: Undoped Channel & Subthreshold Swing Idealization -->
  <g transform="translate(670, 20)">
    <rect width="290" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) 무도핑 채널과 SS 60mV/dec 복원</text>

    <!-- Undoped Channel Concept -->
    <g transform="translate(15, 42)">
      <rect width="260" height="120" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="12" y="18" fill="#fde047" font-size="9" font-weight="800">1. 바디가 얇아지면 도핑을 뺄 수 있다!</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="8">• 벌크: 펀치스루 막으려 고농도 도핑 (NA ↑)</text>
      <text x="20" y="50" fill="#fca5a5" font-size="7.5">➔ 공간 전하 많아짐 ➔ C_dep 커짐 ➔ SS 악화</text>

      <text x="12" y="68" fill="#34d399" font-size="8.2" font-weight="700">★ 얇은 바디 (FinFET / GAA / FD-SOI):</text>
      <text x="20" y="82" fill="#cbd5e1" font-size="7.5">기하학적 5nm 구조만으로 펀치스루 100% 차단!</text>
      <text x="20" y="96" fill="#a7f3d0" font-size="8" font-weight="800">➔ 채널에 도핑 불필요 (무도핑 채널 NA ≈ 0)</text>
      <text x="20" y="110" fill="#38bdf8" font-size="7.8">➔ 도펀트가 없으므로 Q_dep = 0 ➔ C_dep = 0!</text>
    </g>

    <!-- Subthreshold Swing Impact -->
    <g transform="translate(15, 172)">
      <rect width="260" height="135" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="9.5" font-weight="800">2. 서브스레시홀드 스윙(SS)의 기적</text>
      <text x="12" y="38" fill="#ffffff" font-size="9">SS = 60 · [ 1 + (C_dep / C_ox) ]  [mV/dec]</text>

      <text x="12" y="58" fill="#cbd5e1" font-size="8">• C_dep가 클 때 (벌크):</text>
      <text x="20" y="72" fill="#ef4444" font-size="8">SS = 80~100 mV/dec (스위치 둔함, 누설 폭증)</text>

      <text x="12" y="92" fill="#a7f3d0" font-size="8">• C_dep ≈ 0 일 때 (박막 바디):</text>
      <text x="20" y="106" fill="#34d399" font-size="8.5" font-weight="800">SS = 60 · (1 + 0) = 60 mV/dec (이상치!)</text>
      <text x="12" y="122" fill="#bae6fd" font-size="7.5">게이트 전압이 걸리는 족족 표면 전위가 100% 전달됨</text>
    </g>

    <!-- Summary Takeaway Box -->
    <rect x="15" y="320" width="260" height="86" rx="6" fill="#0b1329" stroke="#334155"/>
    <text x="18" y="340" fill="#fbbf24" font-size="8.8" font-weight="800">최종 물리적 핵심 3줄 정리:</text>
    <text x="18" y="358" fill="#cbd5e1" font-size="7.8">1. 바디가 얇으면 전하가 상한선에 고정 ➔ dQ/dψ = 0</text>
    <text x="18" y="373" fill="#cbd5e1" font-size="7.8">2. 두꺼운 BOX 산화막 직렬 연결 ➔ 합성 용량 급감</text>
    <text x="18" y="388" fill="#34d399" font-size="8" font-weight="700">3. 무도핑 채널 실현 ➔ 공핍 전하 자체가 0!</text>
  </g>
</svg>""",
    "lecture": r"""
        <!-- Section 1: The Intuitive Paradox -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 직관의 역설: "평행판 공식(C = ε/d)대로라면 두께가 얇아지면 커져야 하는 것 아닌가?"
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체 물리를 공부할 때 거의 모든 엔지니어가 마주하는 가장 혼란스러운 순간이 바로 이 지점입니다:<br>
            <em>"평행판 커패시터 공식 $C = \frac{\epsilon A}{d}$에서 두께($d$)가 얇아지면 분모가 작아지니까 커패시턴스는 커져야 맞지 않나? 왜 FD-SOI나 FinFET에서는 바디 두께($T_{body}$)를 $5\,\text{nm}$로 얇게 만들면 $C_{dep}$가 작아진다고(0에 가까워진다고) 할까?"</em>
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:18px;">
            <h4 style="color:#38bdf8; font-size:1.05rem; font-weight:800; margin-bottom:8px;">💡 인지부조화를 단번에 깨부수는 핵심 진실</h4>
            <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:18px;">
              <li><strong>함정</strong>: 평행판 공식 $C = \epsilon/d$는 **"두께 $d$ 양단에 전하가 자유롭게 축적되고 이동할 수 있을 때"**만 성립합니다.</li>
              <li><strong>물리학적 본질</strong>: 커패시턴스의 진짜 정의는 전하량 자체가 아니라 **'전압이 변할 때 전하량이 얼마나 변하는가'($C = \frac{dQ}{dV}$)**입니다!</li>
              <li>바디가 얇아져 실리콘 바디 전체가 이미 100% 비워진 **완전 공핍(Fully Depleted)** 상태가 되면, <strong>더 이상 게이트 전압을 올려도 바디 안에 추가로 비울 수 있는 캐리어나 이온이 물리적으로 단 하나도 남아있지 않습니다!</strong></li>
              <li>따라서 전압이 변해도 공핍 전하량이 변하지 않으므로($\frac{dQ_{dep}}{d\psi_s} \approx 0$), <strong>유효 공핍 커패시턴스는 0에 수렴</strong>하게 됩니다!</li>
            </ul>
          </div>
        </div>

        <!-- Section 2: Mechanism 1 - Charge Saturation -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 메커니즘 ① : 공핍 전하의 상한선 고정과 $dQ/d\psi \approx 0$ (전하 포화)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            두꺼운 벌크 실리콘과 얇은 박막 바디(FD-SOI)에서 일어나는 전하 변화를 수식으로 비교해 보면 이유가 명확해집니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#f87171; margin:14px 0 8px;">■ 벌크(Bulk) 트랜지스터 : 전하가 계속 늘어남 (dQ > 0)</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:10px;">
            벌크 실리콘은 기판 깊이가 무한히 깊습니다. 게이트 전압($V_G$)을 높여 표면 전위($\psi_s$)가 올라가면, 공핍층이 실리콘 깊은 곳으로 점점 더 깊게 파고듭니다:
            $$Q_{dep}(\psi_s) = \sqrt{2q \epsilon_{si} N_A \psi_s}$$
            표면 전위가 변할 때 공핍 전하량도 계속 변하므로 미분값(커패시턴스)이 존재합니다:
            $$C_{dep} = \frac{dQ_{dep}}{d\psi_s} = \sqrt{\frac{q \epsilon_{si} N_A}{2\psi_s}} = \frac{\epsilon_{si}}{W_{dep}} > 0$$
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#34d399; margin:14px 0 8px;">■ 박막 바디(FD-SOI) : 전하량이 최대치로 꽁꽁 얼어붙음 (dQ = 0!)</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            하지만 실리콘 바디 두께가 $T_{body} \approx 5\,\text{nm}$로 극도로 얇은 FD-SOI에서는, 게이트 전압을 조금만 걸어도 공핍층이 실리콘 바닥(BOX 산화막 계면)에 즉시 도달해 버립니다.<br>
            바디 안의 모든 실리콘 원자가 이미 100% 공핍되었으므로, 바디 내 총 공핍 전하량은 **바디 부피 안의 불순물 총량으로 상한선에 도달하여 고정(Saturated)**됩니다:
            $$Q_{dep} = q N_A T_{body} = \text{상수 (Constant!)}$$
            이제 게이트 전압을 $1\text{V}$, $2\text{V}$ 더 올려도 바디 안에서 추가로 생겨날 공핍 전하가 단 하나도 없습니다. 따라서:
            $$C_{dep} = \frac{dQ_{dep}}{d\psi_s} = \frac{d(q N_A T_{body})}{d\psi_s} = 0 !$$
            이것이 바로 바디가 얇아지면 $C_{dep}$가 0으로 줄어드는 제1의 물리적 원리입니다.
          </p>
        </div>

        <!-- Section 3: Mechanism 2 - Series Coupling with BOX -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 메커니즘 ② : 두껍고 저유전율인 매립 산화막(BOX)과의 직렬 연결 효과
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            설령 바디 아래의 전하 변조를 고려하더라도, 구조적으로 **두꺼운 매립 산화막(BOX)이 직렬로 결합**되어 전체 정전용량을 극단적으로 떨어뜨립니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #f59e0b; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#fbbf24; font-size:1rem; font-weight:800; margin-bottom:8px;">💡 직렬 합성 커패시터의 법칙: "작은 놈이 전체를 지배한다"</h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; margin-bottom:8px;">
              게이트 아래 실리콘 바디($T_{si}$) 밑에는 두꺼운 절연막인 매립 산화막($t_{BOX} \approx 25 \sim 100\,\text{nm}$)이 깔려 있습니다. 채널 표면에서 기판까지의 등가 정전용량은 실리콘 용량과 산화막 용량의 **직렬 합성(Series Combination)**입니다:
              $$\frac{1}{C_{body,eff}} = \frac{1}{C_{si}} + \frac{1}{C_{BOX}} = \frac{T_{si}}{\epsilon_{si}} + \frac{t_{BOX}}{\epsilon_{ox}}$$
              $$C_{body,eff} = \frac{1}{\frac{T_{si}}{\epsilon_{si}} + \frac{t_{BOX}}{\epsilon_{ox}}}$$
            </p>
            <ul style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; padding-left:18px;">
              <li>BOX 산화막 두께($t_{BOX}$)는 수십 $\text{nm}$로 실리콘 공핍층보다 훨씬 두껍습니다.</li>
              <li>산화막의 유전율($\epsilon_{ox} = 3.9$)은 실리콘($\epsilon_{si} = 11.7$)보다 3배나 낮습니다.</li>
              <li>따라서 $\frac{t_{BOX}}{\epsilon_{ox}}$ 항이 분모를 압도하여, <strong>전체 등가 용량은 극도로 작은 $C_{BOX}$ 값보다도 더 작아집니다!</strong></li>
              <li>$$C_{body,eff} \approx C_{BOX} \ll C_{dep,bulk}$$</li>
            </ul>
          </div>
        </div>

        <!-- Section 4: Mechanism 3 - Undoped Channel Revolution -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#ef4444; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. 메커니즘 ③ : 무도핑 채널(Undoped Channel) 실현 ($N_A \approx 0 \implies Q_{dep} = 0$)
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            실제 최신 공정(FinFET, GAA 나노시트, FD-SOI)에서는 한 걸음 더 나아가 **채널에 도펀트를 아예 넣지 않습니다**.
          </p>
          <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:22px; margin-bottom:14px;">
            <li><strong>벌크의 딜레마</strong>: 펀치스루를 막으려면 고농도 도핑($N_A \uparrow$)을 해야 했고, 이온화된 불순물($B^-$) 공간 전하가 바글바글하여 공핍 전하($Q_{dep}$)와 공핍 용량($C_{dep}$)이 클 수밖에 없었습니다.</li>
            <li><strong>박막 바디의 승리</strong>: 바디 두께를 $5\,\text{nm}$로 얇게 만들면, 기하학적 구조만으로 지하 누설 통로를 100% 틀어막을 수 있습니다. 따라서 **채널에 불순물 도핑을 할 필요가 없습니다 (Undoped Channel, $N_A \approx 0$)**!</li>
            <li><strong>결과</strong>: 채널 안에 고정 이온 전하 자체가 아예 없으므로, **공핍 전하량 $Q_{dep} \approx 0$**이며, 따라서 **공핍 커패시턴스는 수학적으로 완벽한 $0$**에 도달합니다!</li>
          </ul>

          <div style="background:#090d1a; border:1px solid #10b981; border-radius:10px; padding:16px; margin-top:16px;">
            <h4 style="color:#34d399; font-size:0.95rem; font-weight:800; margin-bottom:8px;">🚀 $C_{dep} \approx 0$이 가져오는 궁극의 보상: 서브스레시홀드 스윙 이상치 복원</h4>
            <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.75; margin-bottom:0;">
              $$SS = \ln(10) \frac{kT}{q} \left( 1 + \frac{C_{dep}}{C_{ox}} \right) \xrightarrow{C_{dep} \to 0} 60\,\text{mV/dec}$$
              바디가 얇아져 $C_{dep}$가 0으로 사라지면, 게이트 전압이 채널 표면 전위에 손실 없이 100% 직결됩니다 ($\frac{\partial \psi_s}{\partial V_G} = 1$).<br>
              이로써 상온 물리 한계치인 **$SS = 60\,\text{mV/dec}$의 칼날 같은 온/오프 스위칭**을 달성하여, 트랜지스터를 끌 때 대기 누설전류를 수천 분의 일로 완벽히 차단하게 됩니다!
            </p>
          </div>
        </div>

        <!-- Section 5: Summary Comparison Table -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.15rem; font-weight:800; color:#e2e8f0; margin-bottom:12px;">
            5. 핵심 요약 비교 정리표
          </h3>
          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">관점 및 요인</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">두꺼운 바디 (벌크 Planar)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">초박막 바디 (FD-SOI / FinFET)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">Cdep가 작아지는 물리적 이유</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">1. 전하 변조 ($dQ/d\psi$)</td>
                  <td style="padding:10px 14px;">전압 따라 공핍층 깊숙이 팽창 ($dQ > 0$)</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">$Q_{dep} = qN_A T_{body}$로 고정 포화</td>
                  <td style="padding:10px 14px;">추가로 비울 전하가 없어 <strong>$dQ/d\psi \approx 0$ 달성</strong></td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#f59e0b;">2. 하부 절연막 직렬 결합</td>
                  <td style="padding:10px 14px;">실리콘 기판 자체에 공핍층 형성</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">두꺼운 매립 산화막(BOX) 직렬 연결</td>
                  <td style="padding:10px 14px;">작은 $C_{BOX}$가 직렬을 지배해 <strong>등가 용량 급감</strong></td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#10b981;">3. 채널 불순물 도핑</td>
                  <td style="padding:10px 14px;">펀치스루 억제용 고도핑 ($N_A \uparrow$)</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">무도핑 채널 실현 ($N_A \approx 0$)</td>
                  <td style="padding:10px 14px;">공핍 전하 $Q_{dep}$ 자체가 없어 <strong>$C_{dep} \approx 0$</strong></td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#f87171;">4. 서브스레시홀드 스윙</td>
                  <td style="padding:10px 14px; color:#ef4444;">$SS \approx 80 \sim 100\,\text{mV/dec}$ (누설 심각)</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">$SS \approx 60\,\text{mV/dec}$ (이상적 한계치)</td>
                  <td style="padding:10px 14px;">전압 손실 제로 ➔ <strong>스위칭 칼날화 &amp; 대기전력 차단</strong></td>
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

    # Step 1: Shift existing 83 topics (q-83 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(83, 0, -1):
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

    # Step 4: Update header description to 84 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 'Body가 얇아지면 왜 Cdep가 작아질까? (C=dQ/dV 본질, BOX 직렬)'이 위치하며, 총 84개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Why Cdep decreases topic!")
