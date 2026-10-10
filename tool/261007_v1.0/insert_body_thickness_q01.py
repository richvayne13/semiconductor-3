# -*- coding: utf-8 -*-
"""
insert_body_thickness_q01.py
사용자 질문: "body thickness가 얇아져야하는이유가뭐야"
대시보드 최상단 Q01로 신규 추가하고, 기존 79개 질문을 Q02~Q80으로 시프트 (총 80개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 스케일링 · UTB / FinFET / GAA 물리)",
    "title": "Body Thickness(바디 두께)가 얇아져야 하는 결정적 이유: 스케일 길이(λ), 지하 누설 차단, 완전 공핍화와 무도핑 혁명",
    "nav_title": "Body Thickness(바디 두께)가 얇아져야 하는 이유 (스케일 길이, 누설 차단)",
    "summary": [
        "<strong>1. 자연 스케일 길이(Scale Length $\\lambda$) 축소와 게이트 제어력 극대화</strong>: 단채널 효과를 억제하려면 게이트 길이 $L \\ge 3\\lambda$를 만족해야 합니다. 스케일 길이 공식 $\\lambda = \\sqrt{\\frac{\\epsilon_{si}}{2\\epsilon_{ox}} t_{ox} T_{body}}$에서, 산화막 두께($t_{ox}$)가 양자 터널링 한계(EOT)로 더 이상 얇아질 수 없기 때문에 <strong>채널 미세화($L \\downarrow$)를 가능하게 하는 유일한 열쇠는 바디 두께($T_{body}$)를 얇게 만드는 것</strong>입니다.",
        "<strong>2. 지하 펀치스루(Subsurface Punchthrough) 누설 경로의 물리적 박멸</strong>: 두꺼운 벌크 기판에서는 게이트 전계가 미치지 못하는 깊은 바닥 경로를 통해 소스-드레인 간 누설전류가 흐릅니다. 바디 두께를 수 나노미터($T_{body} \\approx 5\\text{nm}$)로 얇게 깎아내면 <strong>게이트의 통제권을 벗어나는 지하 공간 자체가 물리적으로 사라져 누설 통로가 원천 차단</strong>됩니다.",
        "<strong>3. 완전 공핍화(Fully Depleted)로 $C_{dep} \\approx 0$ 달성 및 $SS \\approx 60\\text{mV/dec}$ 복원</strong>: 바디가 공핍층 폭보다 얇아지면 채널 전체가 완전히 비워져(Fully Depleted) 기생 공핍 커패시턴스($C_{dep}$)가 극소화됩니다. 이로써 <strong>서브스레시홀드 스윙($SS$)이 이상적인 열역학적 한계치인 $60\\text{mV/dec}$에 도달</strong>하여 오프 누설전류가 획기적으로 줄어듭니다.",
        "<strong>4. 무도핑 채널(Undoped Channel) 실현 (이동도 급증 & RDF 제거)</strong>: 바디 두께 조절만으로 단채널을 완벽히 억제할 수 있으므로 <strong>채널에 불순물 도핑을 할 필요가 없습니다</strong>. 이온화 불순물 쿨롱 산란이 사라져 전자 이동도($\\mu$)와 구동 전류($I_{on}$)가 폭등하며, 원자 개수 편차로 인한 무작위 도펀트 요동(RDF) 불량이 100% 해결됩니다."
    ],
    "svg_title": "📊 [바디 두께 축소의 3대 물리 메커니즘] (A) 지하 펀치스루 경로 차단 | (B) 자연 스케일 길이(λ) 수식 원리 | (C) 완전공핍화(FD)와 무도핑 혁명",
    "svg": """<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Bulk Thick Body vs Ultra-Thin Body (UTB) Leakage Path -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 지하 누설 경로의 물리적 박멸</text>

    <!-- Sub-case 1: Thick Body (Bulk) -->
    <g transform="translate(15, 42)">
      <rect width="270" height="135" rx="5" fill="#1e293b" stroke="#ef4444"/>
      <text x="10" y="16" fill="#f87171" font-size="9" font-weight="800">1. 두꺼운 바디 (Thick Bulk): 지하 펀치스루 발생</text>
      <!-- Gate -->
      <rect x="90" y="25" width="90" height="12" fill="#64748b" rx="2"/>
      <text x="115" y="34" fill="#fff" font-size="7.5">Gate</text>
      <!-- S / D -->
      <rect x="25" y="37" width="50" height="40" fill="#f59e0b" rx="2"/>
      <text x="35" y="60" fill="#000" font-size="7.5" font-weight="800">Source</text>
      <rect x="195" y="37" width="50" height="40" fill="#f59e0b" rx="2"/>
      <text x="207" y="60" fill="#000" font-size="7.5" font-weight="800">Drain</text>
      <!-- Bulk Substrate (Thick) -->
      <rect x="75" y="37" width="120" height="85" fill="#047857" opacity="0.3"/>
      <!-- Leakage Arrow in deep bulk -->
      <path d="M 75 95 Q 135 115 195 95" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4,2"/>
      <text x="85" y="112" fill="#ef4444" font-size="8" font-weight="800">지하 누설 경로 (Punchthrough)</text>
      <text x="10" y="130" fill="#fca5a5" font-size="7.5">• 게이트 전계가 닿지 않는 깊은 바닥으로 전류 누설!</text>
    </g>

    <!-- Sub-case 2: Ultra-Thin Body (FD-SOI / FinFET / GAA) -->
    <g transform="translate(15, 188)">
      <rect width="270" height="135" rx="5" fill="#1e293b" stroke="#10b981"/>
      <text x="10" y="16" fill="#34d399" font-size="9" font-weight="800">2. 초박막 바디 (UTB / FinFET): 누설 통로 원천 제거</text>
      <!-- Gate -->
      <rect x="90" y="25" width="90" height="12" fill="#38bdf8" rx="2"/>
      <text x="115" y="34" fill="#000" font-size="7.5" font-weight="800">Gate</text>
      <!-- Ultra-thin Silicon Channel (T_body ~ 5nm) -->
      <rect x="25" y="37" width="220" height="15" fill="#10b981" rx="1"/>
      <text x="100" y="48" fill="#fff" font-size="7.5" font-weight="800">T_body ≈ 5nm (극박막)</text>
      <!-- S / D -->
      <rect x="25" y="37" width="50" height="15" fill="#f59e0b"/>
      <text x="32" y="48" fill="#000" font-size="7.5" font-weight="800">Source</text>
      <rect x="195" y="37" width="50" height="15" fill="#f59e0b"/>
      <text x="204" y="48" fill="#000" font-size="7.5" font-weight="800">Drain</text>
      <!-- Buried Oxide (BOX Insulator) -->
      <rect x="25" y="52" width="220" height="65" fill="#334155" stroke="#475569" stroke-dasharray="2,2"/>
      <text x="65" y="85" fill="#94a3b8" font-size="8.5" font-weight="700">매립 산화막 (Buried Oxide, SiO₂)</text>
      <text x="60" y="102" fill="#38bdf8" font-size="7.5">절연벽이 지하를 완벽 차단! (No Bulk)</text>
      <text x="10" y="128" fill="#a7f3d0" font-size="7.5">★ 누설 통로 자체가 존재할 수 없음! 게이트 100% 장악</text>
    </g>

    <!-- Summary Box -->
    <rect x="15" y="332" width="270" height="74" rx="6" fill="#0b1329" stroke="#334155"/>
    <text x="22" y="352" fill="#38bdf8" font-size="8.8" font-weight="800">기하학적 봉쇄의 결론:</text>
    <text x="22" y="369" fill="#cbd5e1" font-size="8">• 게이트 사정거리 안에 채널 전체를 강제 감금!</text>
    <text x="22" y="385" fill="#fde047" font-size="8">• DIBL 감소, 문턱전압 롤오프 완벽 억제</text>
    <text x="22" y="399" fill="#a5f3fc" font-size="7.8">• 평면 벌크 ➔ FD-SOI, FinFET, GAA 진화의 제1원리</text>
  </g>

  <!-- PANEL B: Natural Scale Length (lambda) and Gate Control -->
  <g transform="translate(340, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 자연 스케일 길이(λ) 물리 법칙</text>

    <!-- Scale Length Formula Box -->
    <g transform="translate(15, 42)">
      <rect width="280" height="120" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="9" font-weight="800">스케일 길이 (Scale Length λ) 공식 유도</text>
      <text x="12" y="38" fill="#ffffff" font-size="9.5">λ_DG = √ [ (ε_si / 2ε_ox) · t_ox · T_body ]</text>
      <text x="12" y="58" fill="#cbd5e1" font-size="8">• 단채널 억제 조건 (설계 불문율):</text>
      <text x="25" y="74" fill="#38bdf8" font-size="9" font-weight="800">L_gate ≥ 3 ~ 4 × λ</text>
      <text x="12" y="94" fill="#cbd5e1" font-size="8">• 게이트 길이 L이 20nm ➔ 10nm ➔ 3nm로 줄어들려면</text>
      <text x="12" y="108" fill="#fde047" font-size="8.5" font-weight="700">➔ λ도 비례해서 반드시 작아져야만 함!</text>
    </g>

    <!-- Why T_body is the ONLY knob left -->
    <g transform="translate(15, 172)">
      <rect width="280" height="125" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="9.5" font-weight="800">왜 하필 'T_body'를 줄여야만 하는가?</text>
      <text x="12" y="38" fill="#fca5a5" font-size="8">1. 산화막 두께(t_ox) 축소의 물리적 한계:</text>
      <text x="20" y="52" fill="#cbd5e1" font-size="7.8">• t_ox &lt; 1nm 미만 시 양자역학적 직류 터널링 폭발!</text>
      <text x="20" y="65" fill="#cbd5e1" font-size="7.8">• High-k(HfO₂)를 써도 EOT 축소는 ~0.7nm에서 벽에 부딪힘.</text>

      <text x="12" y="83" fill="#a7f3d0" font-size="8">2. 인류에게 남은 유일한 조절 손잡이: T_body!</text>
      <text x="20" y="98" fill="#fde047" font-size="8" font-weight="700">• T_body를 얇게 깎을수록 λ ∝ √(T_body) 로 급감!</text>
      <text x="20" y="112" fill="#38bdf8" font-size="8">• 극초단 게이트(L &lt; 15nm)에서도 게이트 통제력 완벽 유지</text>
    </g>

    <!-- Multi-gate Field Coupling (Volume Inversion) -->
    <g transform="translate(15, 306)">
      <rect width="280" height="100" rx="6" fill="#0b1329" stroke="#334155"/>
      <text x="12" y="18" fill="#38bdf8" font-size="9" font-weight="800">★ 전계 중첩과 볼륨 인버전 (Volume Inversion):</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="8">• FinFET(양면) 및 GAA(4면)에서 T_body가 얇아지면</text>
      <text x="12" y="50" fill="#cbd5e1" font-size="8">  양쪽 게이트 전계가 채널 중심부에서 서로 결합(Coupling)!</text>
      <text x="12" y="66" fill="#cbd5e1" font-size="8">• 표면뿐 아니라 바디 한가운데 전체로 전류가 흐름</text>
      <text x="12" y="82" fill="#34d399" font-size="8.5" font-weight="700">➔ 표면 거칠기 산란 회피 + 전류 구동력(Ion) 폭등!</text>
    </g>
  </g>

  <!-- PANEL C: Fully Depleted (FD) and Undoped Channel Revolution -->
  <g transform="translate(670, 20)">
    <rect width="290" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) 완전공핍화(FD) &amp; 무도핑 혁명</text>

    <!-- Fully Depleted Box -->
    <g transform="translate(15, 42)">
      <rect width="260" height="120" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="12" y="18" fill="#fde047" font-size="9" font-weight="800">1. 완전 공핍화 (Fully Depleted, FD)</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="8">• T_body &lt; W_dep 일 때 채널 전체가 완전 공핍화!</text>
      <text x="12" y="52" fill="#cbd5e1" font-size="8">• 공핍 전하 Q_dep가 0에 가깝게 고정</text>
      <text x="12" y="68" fill="#fde047" font-size="8.5" font-weight="700">➔ 기생 공핍 커패시턴스 C_dep ≈ 0 달성!</text>
      <text x="12" y="86" fill="#a7f3d0" font-size="8.5">■ 서브스레시홀드 스윙 이상치 복원:</text>
      <text x="20" y="104" fill="#34d399" font-size="9" font-weight="800">SS = 60 · (1 + C_dep/Cox) ➔ 60 mV/dec (완벽!)</text>
    </g>

    <!-- Undoped Channel Box -->
    <g transform="translate(15, 172)">
      <rect width="260" height="125" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="9.5" font-weight="800">2. 무도핑 채널 (Undoped Channel) 실현</text>
      <text x="12" y="38" fill="#cbd5e1" font-size="8">• 기존 벌크: SCE 막으려 고농도 도핑 (NA ↑)</text>
      <text x="20" y="52" fill="#fca5a5" font-size="7.8">➔ 불순물 산란으로 이동도 폭락, RDF 결함 발생</text>

      <text x="12" y="72" fill="#a7f3d0" font-size="8">• 박막 바디: 구조만으로 SCE를 100% 차단하므로</text>
      <text x="20" y="88" fill="#fde047" font-size="8.5" font-weight="700">➔ 채널에 불순물 도핑 불필요 (무도핑 채널!)</text>
      <text x="20" y="104" fill="#cbd5e1" font-size="7.8">① 쿨롱 산란 제거 ➔ 전자 이동도(μ) 극대화</text>
      <text x="20" y="118" fill="#cbd5e1" font-size="7.8">② RDF(무작위 도펀트 요동) 산포 오차 0% 박멸!</text>
    </g>

    <!-- Trade-off / Caution Box -->
    <g transform="translate(15, 306)">
      <rect width="260" height="100" rx="6" fill="#0b1329" stroke="#ef4444"/>
      <text x="12" y="18" fill="#f87171" font-size="9" font-weight="800">⚠️ 너무 얇을 때의 한계 (T_body &lt; 4nm):</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="7.8">1. 양자 구속 효과(Quantum Confinement):</text>
      <text x="20" y="48" fill="#94a3b8" font-size="7.5">밴드갭 Eg 증가 및 유효질량 변화 ➔ Vt 요동</text>
      <text x="12" y="64" fill="#cbd5e1" font-size="7.8">2. 기생 소스/드레인 저항(R_sd) 급증:</text>
      <text x="20" y="76" fill="#94a3b8" font-size="7.5">단면적 축소로 저항 커짐 ➔ Raised S/D 필수</text>
      <text x="12" y="90" fill="#fde047" font-size="7.5">★ 황금 두께: T_body ≈ 5~7nm에서 최적화!</text>
    </g>
  </g>
</svg>""",
    "lecture": r"""
        <!-- Section 1: Introduction -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 반도체 스케일링의 지상 과제: 왜 바디 두께($T_{body}$)를 얇게 깎아야만 할까?
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            현대 첨단 반도체 소자인 <strong>FD-SOI(완전공핍형 SOI)</strong>의 실리콘 박막 두께($T_{si}$), <strong>FinFET</strong>의 핀 폭($W_{fin}$), 그리고 3nm 이하 <strong>GAA(Gate-All-Around) 나노시트</strong>의 두께($T_{ns}$)를 살펴보면 공통적으로 <strong>$5 \sim 7\,\text{nm}$ 수준으로 극도로 얇게</strong> 제작됩니다.<br>
            왜 반도체 소자 설계자들은 공정 난이도가 극도로 치솟음에도 불구하고 바디 두께(Body Thickness, $T_{body}$)를 이토록 얇게 만들어야만 했을까요?
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:14px 18px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:700; margin-bottom:8px;">💡 마스터 4대 핵심 결론 요약</h4>
            <ol style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:18px;">
              <li><strong>스케일 길이($\lambda$) 축소</strong>: 단채널 억제 조건($L \ge 3\lambda$)에서 산화막 두께($t_{ox}$) 축소가 물리적 한계에 부딪혔으므로, 게이트 길이($L$)를 줄일 수 있는 유일한 변수가 $T_{body}$ 축소이기 때문입니다.</li>
              <li><strong>지하 펀치스루 누설 경로 박멸</strong>: 게이트 전계의 손길이 닿지 않는 깊은 기판 바닥 영역을 물리적으로 없애버려 소스-드레인 단락 누설을 100% 차단합니다.</li>
              <li><strong>완전 공핍화(Fully Depleted)로 $C_{dep} \approx 0$화</strong>: 공핍층 기생 커패시턴스를 없애 서브스레시홀드 스윙($SS$)을 이상치인 $60\,\text{mV/dec}$로 복원합니다.</li>
              <li><strong>무도핑 채널(Undoped Channel) 실현</strong>: 불순물 도핑 없이도 단채널을 막을 수 있어, 쿨롱 산란을 없애 전자 이동도($\mu$)를 극대화하고 무작위 도펀트 요동(RDF) 불량을 제거합니다.</li>
            </ol>
          </div>
        </div>

        <!-- Section 2: Scale Length Law -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 메커니즘 ① : 자연 스케일 길이(Scale Length $\lambda$)의 물리 법칙
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            MOSFET에서 게이트 전압이 채널 전위를 얼마나 지배적으로 장악하고, 드레인 전압의 수평 전계 침투(DIBL)를 얼마나 효과적으로 차단하는가를 정량화한 척도가 바로 **자연 스케일 길이(Natural Scale Length, $\lambda$)**입니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#fde047; margin:14px 0 8px;">■ 스케일 길이 공식과 미세화 설계의 불문율</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:10px;">
            이중 게이트(Double-Gate) 및 박막 바디 소자에서 푸아송 방정식을 풀면 유도되는 스케일 길이는 다음과 같습니다:
            $$\lambda = \sqrt{\frac{\epsilon_{si}}{2\epsilon_{ox}} t_{ox} T_{body}}$$
            소자가 극심한 단채널 효과(DIBL, 문턱전압 롤오프, 펀치스루) 없이 정상적인 온/오프 스위치로 작동하려면 다음 조건을 반드시 만족해야 합니다:
            $$L_{gate} \ge 3 \sim 4 \times \lambda$$
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#38bdf8; margin:14px 0 8px;">■ 산화막 한계(EOT Limit)와 인류에게 남은 유일한 해법</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            게이트 길이 $L$을 $20\,\text{nm} \rightarrow 10\,\text{nm} \rightarrow 3\,\text{nm}$로 줄이려면 $\lambda$ 역시 필연적으로 줄어들어야 합니다.<br>
            하지만 게이트 산화막 두께($t_{ox}$)는 양자역학적 직류 터널링(Direct Tunneling)으로 인한 게이트 누설전류 폭발 때문에 $1\,\text{nm}$ 이하로 줄일 수 없습니다(High-k 물질을 적용한 등가산화막두께 EOT도 약 $0.7\,\text{nm}$ 수준에서 물리적 벽에 부딪힘).<br>
            따라서 <strong>스케일 길이 공식에서 $\lambda$를 줄일 수 있는 인류에게 남은 유일한 조절 손잡이는 바로 바디 두께($T_{body}$)</strong>입니다!
            $$T_{body} \downarrow \implies \lambda \propto \sqrt{T_{body}} \downarrow \implies \text{더 짧은 게이트 길이 } L \text{ 구현 가능!}$$
          </p>
        </div>

        <!-- Section 3: Subsurface Leakage Elimination -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 메커니즘 ② : 지하 펀치스루(Subsurface Punchthrough) 누설 통로의 기하학적 박멸
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            벌크(Bulk) 평면 트랜지스터의 구조적 비극은 **"바디가 너무 두껍다"**는 사실에 있었습니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #f59e0b; padding:14px 18px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#fbbf24; font-size:1rem; font-weight:700; margin-bottom:8px;">💡 지하 누설(Subsurface Leakage)이란 무엇인가?</h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:18px;">
              <li>게이트 바로 밑 표면 채널은 게이트의 강력한 수직 전계에 의해 전류가 잘 닫힙니다.</li>
              <li>하지만 게이트에서 멀리 떨어진 **기판 깊은 곳(Bulk Subsurface 영역)**은 게이트의 전계가 미치지 못하는 사각지대입니다.</li>
              <li>드레인에 전압이 걸리면, 전자가 게이트의 통제를 받지 않는 **기판 깊은 지하 경로를 우회하여 소스에서 드레인으로 몰래 새어나가는 펀치스루(Punchthrough)**가 발생합니다.</li>
            </ul>
          </div>

          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            그러나 바디 두께를 $5\,\text{nm}$ 수준으로 극도로 얇게 깎아내고 그 밑에 절연체(매립 산화막 BOX 또는 에어갭)를 깔아버리면, <strong>"게이트의 통제권을 벗어나는 지하 공간 자체가 물리적으로 지구상에서 사라집니다."</strong><br>
            전자가 이동할 수 있는 모든 통로가 게이트의 유효 사정거리 안에 강제로 감금되므로, 지하 누설 경로가 원천 봉쇄되어 오프 상태 누설전류가 수천 분의 일로 급감합니다.
          </p>
        </div>

        <!-- Section 4: Fully Depleted and Undoped Channel Revolution -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#ef4444; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. 메커니즘 ③ : 완전 공핍화(FD)로 $C_{dep} \approx 0$화 & 무도핑 채널의 기적
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            바디 두께가 얇아지면 소자의 정전용량 모델과 캐리어 수송 특성에 일대 혁명이 일어납니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#fde047; margin:14px 0 8px;">■ 완전 공핍화(Fully Depleted)와 $SS \approx 60\,\text{mV/dec}$ 달성</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:10px;">
            바디 두께 $T_{body}$가 최대 공핍층 폭 $W_{dep}$보다 얇아지면($T_{body} < W_{dep}$), 채널 내부의 모든 자유 캐리어가 밀려나 **바디 전체가 100% 완전 공핍화**됩니다.<br>
            이때 공핍 전하($Q_{dep} = q N_A T_{body}$)가 고정되고, 하부 매립 산화막(BOX)의 작은 정전용량과 직렬 연결되면서 **기생 공핍 커패시턴스($C_{dep}$)가 거의 0에 수렴**하게 됩니다:
            $$SS = 2.3 \frac{kT}{q} \left( 1 + \frac{C_{dep}}{C_{ox}} \right) \xrightarrow{C_{dep} \to 0} 60\,\text{mV/dec (이상적 한계치!)}$$
            게이트 전압이 걸리는 족족 표면 전위가 100% 온전히 따라 움직이므로, 문턱전압 이하에서 스위칭이 칼날처럼 예리해집니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#34d399; margin:14px 0 8px;">■ 무도핑 채널(Undoped Channel) 실현의 2대 축복</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            기존 벌크 소자에서는 단채널 효과를 막기 위해 기판에 고농도 불순물을 억지로 쑤셔 넣어야만 했습니다. 하지만 바디가 얇아지면 **기하학적 구조만으로 단채널을 완벽히 막아내므로 채널에 불순물 도핑을 전혀 하지 않아도 됩니다(Undoped Channel)**:
          </p>
          <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:20px; margin-bottom:14px;">
            <li><strong>1. 전자/정공 이동도($\mu$) 폭등</strong>: 이온화 불순물 산란(Ionized Impurity Scattering)의 원인인 고정 이온($B^-, As^+$)이 채널에 단 하나도 없으므로 캐리어가 산란 없이 고속 질주하여 구동 전류($I_{on}$)가 획기적으로 상승합니다.</li>
            <li><strong>2. 무작위 도펀트 요동(RDF: Random Dopant Fluctuation) 완전 박멸</strong>: 나노 채널 내에 불순물이 5개 들어가느냐 10개 들어가느냐에 따라 문턱전압($V_{th}$)이 들쭉날쭉하던 치명적인 공정 편차 불량이 도펀트 제로화로 인해 100% 근절됩니다.</li>
          </ul>
        </div>

        <!-- Section 5: Engineering Limitations and Sweet Spot -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#e2e8f0; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            5. 그렇다면 무한정 얇게 만들면 좋을까? (한계와 최적의 황금 두께)
          </h3>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            바디 두께가 $T_{body} < 4\,\text{nm}$ 이하로 지나치게 얇아지면 다음과 같은 양자역학적/공학적 부작용이 폭발합니다:
          </p>
          <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:20px; margin-bottom:14px;">
            <li><strong>양자 구속 효과 (Quantum Confinement)</strong>: 전자가 갇힌 양자 우물 폭이 원자 단위로 좁아지면서 실리콘의 유효 밴드갭($E_g$)이 넓어지고 문턱전압($V_{th}$)이 가파르게 상승하여 회로 설계가 왜곡됩니다.</li>
            <li><strong>원자 1개 층(Monolayer) 두께 편차 민감도</strong>: 웨이퍼 상에서 원자 1~2개 층($\approx 0.3\,\text{nm}$)의 두께 오차만 생겨도 문턱전압이 수십 $\text{mV}$씩 요동칩니다.</li>
            <li><strong>기생 소스/드레인 저항($R_{sd}$) 폭증</strong>: 단면적이 실오라기처럼 좁아져 직렬 기생 저항이 폭발하므로, S/D 부위만 선택적으로 두껍게 에피택셜 성장시키는 **Raised Source/Drain (RSD)** 공정이 필수화됩니다.</li>
          </ul>
          <p style="font-size:0.92rem; line-height:1.7; color:#fde047;">
            ★ 따라서 현대 첨단 공정(FinFET, GAA 나노시트, FD-SOI)에서는 단채널 차단 효과를 극대화하면서도 양자 부작용과 저항 폭증을 피할 수 있는 <strong>$T_{body} \approx 5 \sim 7\,\text{nm}$를 최적의 골든 스팟(Golden Spot)</strong>으로 엄격히 제어하고 있습니다.
          </p>
        </div>

        <!-- Section 6: Summary Table -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.15rem; font-weight:800; color:#e2e8f0; margin-bottom:12px;">
            6. 핵심 요약 비교 정리표
          </h3>
          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">비교 항목</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">두꺼운 바디 (벌크 Planar)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">초박막 바디 (UTB / FinFET / GAA)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">바디 두께 축소가 가져온 물리적 혁신</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">스케일 길이 ($\lambda$)</td>
                  <td style="padding:10px 14px;">$\lambda$가 커서 단채널 억제 불가</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">$\lambda \propto \sqrt{T_{body}}$ 극소화 달성</td>
                  <td style="padding:10px 14px;">$L_{gate} \ge 3\lambda$ 만족 ➔ <strong>극초단 게이트 미세화 가능</strong></td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#f59e0b;">지하 누설 (Punchthrough)</td>
                  <td style="padding:10px 14px; color:#ef4444;">게이트 사각지대 지하 누설 심각</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">누설 공간 자체를 물리적으로 제거</td>
                  <td style="padding:10px 14px;">채널 전 영역이 게이트 사정권 안 ➔ <strong>오프 누설전류 박멸</strong></td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#a855f7;">공핍 커패시턴스 ($C_{dep}$)</td>
                  <td style="padding:10px 14px;">부분 공핍, 도핑 증가로 $C_{dep}$ 상승</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">완전 공핍화로 $C_{dep} \approx 0$화</td>
                  <td style="padding:10px 14px;"><strong>서브스레시홀드 스윙 $SS \approx 60\,\text{mV/dec}$ 이상치 복원</strong></td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#10b981;">채널 도핑 및 이동도</td>
                  <td style="padding:10px 14px; color:#ef4444;">고농도 도핑 필수 (산란 심각, RDF 산포)</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">무도핑 채널 (Undoped Channel) 실현</td>
                  <td style="padding:10px 14px;">쿨롱 산란 제거 ➔ <strong>이동도 $\mu \uparrow$, RDF 편차 0% 해결</strong></td>
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

    # Step 1: Shift existing 79 topics (q-79 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(79, 0, -1):
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

    # Step 4: Update header description to 80 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 'Body Thickness(바디 두께)가 얇아져야 하는 이유 (스케일 길이, 누설 차단)'이 위치하며, 총 80개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Body Thickness topic!")
