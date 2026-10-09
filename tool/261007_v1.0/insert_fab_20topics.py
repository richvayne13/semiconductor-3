# -*- coding: utf-8 -*-
"""
insert_fab_20topics.py
신규 반도체 제조 20개 주제(산화 3개, 노광 3개, 식각 3개, 이온주입 4개, 금속 3개, 패키징 4개)를
기존 34개 질문 대시보드 최상단에 Q01~Q20으로 추가하고, 기존 질문을 Q21~Q54로 시프트하는 스크립트.
"""

import sys
import re

# 20개 주제 메타데이터 및 SVG, 요약, 강의노트 데이터 정의
TOPICS_20 = [
    # 1. 산화 1) 건식/습식 산화의 차이점
    {
        "id": "q-01",
        "num": "01",
        "badge": "⭐ 최신 질문 (산화 1/3)",
        "title": "산화 1) 건식/습식 산화의 차이점 (Dry vs Wet Oxidation)",
        "summary": [
            "<strong>건식 산화(Dry: O₂)</strong>는 반응 속도가 느리지만 결함(Dit)이 적고 치밀하여 고품질 초박막 게이트 절연막에 사용되고, <strong>습식 산화(Wet: H₂O)</strong>는 성장 속도가 5~10배 빠르지만 수소 부생성물로 인해 다공성이어서 두꺼운 마스킹/필드 산화막에 사용됩니다.",
            "수증기(H₂O) 분자는 SiO₂ 박막 내부에서의 고체 용해도(Solubility)가 O₂ 분자보다 약 1,000배 높아 확산 유속(Diffusion Flux)이 압도적으로 크기 때문에 습식 산화의 성장 속도가 훨씬 빠릅니다.",
            "산화막 형성 시 실리콘 원자가 소모되므로, 최종 형성된 SiO₂ 두께의 약 44%는 원래 실리콘 기판 내부로 파고들고 56%는 기판 표면 위로 자라납니다."
        ],
        "svg_title": "📊 [건식 vs 습식 산화] 화학 반응, 성장 속도 및 실리콘 계면 잠식률 비교",
        "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="25" y="30" width="350" height="310" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="40" y="55" fill="#38bdf8" font-size="13" font-weight="800">1. 건식 산화 (Dry Oxidation: Si + O₂ ➔ SiO₂)</text>
  <text x="40" y="80" fill="#cbd5e1" font-size="11">• 산화종: 순수 산소 가스 (O₂)</text>
  <text x="40" y="100" fill="#cbd5e1" font-size="11">• 반응 속도: 매우 느림 (치밀한 박막 형성)</text>
  <text x="40" y="120" fill="#34d399" font-size="11">• 막질: 결함/계면트랩(Dit) 극소, 절연내력 우수</text>
  <text x="40" y="140" fill="#fbbf24" font-size="11">• 용도: 게이트 산화막(과거), 터널 절연막, 라이너</text>
  <rect x="40" y="165" width="320" height="40" fill="#0284c7" opacity="0.6" rx="4"/>
  <text x="130" y="190" fill="#ffffff" font-size="12" font-weight="700">고밀도 치밀한 SiO₂ (얇음)</text>
  <rect x="40" y="205" width="320" height="85" fill="#1e293b" rx="4"/>
  <text x="140" y="250" fill="#94a3b8" font-size="13" font-weight="700">단결정 Si 기판</text>
  <line x1="40" y1="205" x2="360" y2="205" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="45" y="315" fill="#f87171" font-size="10.5">※ 점선: 원래 Si 표면 (두께의 44% 침식)</text>

  <rect x="405" y="30" width="350" height="310" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
  <text x="420" y="55" fill="#f59e0b" font-size="13" font-weight="800">2. 습식 산화 (Wet Oxidation: Si + 2H₂O ➔ SiO₂ + 2H₂)</text>
  <text x="420" y="80" fill="#cbd5e1" font-size="11">• 산화종: 수증기 (H₂O Steam)</text>
  <text x="420" y="100" fill="#cbd5e1" font-size="11">• 반응 속도: 건식 대비 5~10배 초고속</text>
  <text x="420" y="120" fill="#f87171" font-size="11">• 막질: H₂ 가스 방출로 다공성(Porous), Dit 높음</text>
  <text x="420" y="140" fill="#fbbf24" font-size="11">• 용도: 후막 마스킹 절연막, STI 매립, 소자 분리</text>
  <rect x="420" y="165" width="320" height="75" fill="#d97706" opacity="0.6" rx="4"/>
  <text x="500" y="205" fill="#ffffff" font-size="12" font-weight="700">두꺼운 SiO₂ (다공성 수소 결함 포함)</text>
  <rect x="420" y="240" width="320" height="60" fill="#1e293b" rx="4"/>
  <text x="520" y="275" fill="#94a3b8" font-size="13" font-weight="700">단결정 Si 기판</text>
  <line x1="420" y1="205" x2="740" y2="205" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="425" y="315" fill="#f87171" font-size="10.5">※ 빠른 확산(용해도 1,000배) ➔ 두꺼운 후막에 필수</text>
</svg>""",
        "lecture": r"""<h3>1. 건식 산화 vs 습식 산화 상세 비교</h3>
<p>실리콘의 열 산화(Thermal Oxidation)는 800~1100℃의 고온 전기로(Furnace)에서 기판을 산화 가스 분위기에 노출시켜 표면에 직접 양질의 이산화규소(SiO₂)를 성장시키는 공정입니다.</p>
<ul>
  <li><strong>건식 산화 (Dry Oxidation)</strong>: 화학식은 $Si + O_2 \to SiO_2$ 입니다. 산소 분자가 치밀하게 반응하여 결함이나 트랩 밀도($D_{it}$)가 매우 낮은 단단한 절연막을 형성합니다. 다만 속도가 느려 수십 nm 이하의 얇은 박막 형성에 제한적으로 사용됩니다.</li>
  <li><strong>습식 산화 (Wet Oxidation)</strong>: 화학식은 $Si + 2H_2O \to SiO_2 + 2H_2 \uparrow$ 입니다. 수증기 분자는 SiO₂ 막 내에서의 고체 용해도(Solid Solubility)가 산소 분자보다 1000배 이상 높기 때문에 확산 속도가 압도적으로 빠릅니다. 수소($H_2$) 가스가 빠져나가며 미세 기공을 남겨 막질은 다소 거칠지만, 수백 nm 이상의 두꺼운 희생막이나 필드 절연막을 빠르게 만들 때 필수적입니다.</li>
</ul>
<h3>2. 44% 실리콘 잠식(Consumption) 법칙</h3>
<p>실리콘과 이산화규소의 분자 부피 비로 인해, 성장한 산화막 두께를 $t_{ox}$라고 하면 원래 실리콘 기판의 $0.44 t_{ox}$ 두께가 화학적으로 소모되어 산화막 내부로 흡수되고, 상부로 $0.56 t_{ox}$만큼 부풀어 오릅니다.</p>"""
    },

    # 2. 산화 2) 열 예산 (Thermal Budget)
    {
        "id": "q-02",
        "num": "02",
        "badge": "⭐ 최신 질문 (산화 2/3)",
        "title": "산화 2) 열 예산 (Thermal Budget)",
        "summary": [
            "<strong>열 예산(Thermal Budget)</strong>이란 반도체 제조 공정 중 웨이퍼가 겪는 '온도와 시간의 총 누적량(∫ T(t) dt)'을 의미합니다.",
            "초미세 공정에서 과도한 열 예산이 가해지면 주입된 도펀트가 의도치 않게 기판 깊숙이 확산(Redistribution)되어 초얕은 접합(USJ)이 무너지고 극심한 단채널 효과(SCE)가 발생합니다.",
            "따라서 현대 공정은 고온 장시간 전기로(Furnace)를 퇴출하고, 수 초~수 밀리초 단위로 급속 열처리하는 RTA(Rapid Thermal Annealing) 및 레이저 스파이크 어닐링(LSA)으로 열 예산을 극소화합니다."
        ],
        "svg_title": "📊 [열 예산(Thermal Budget) 제어] 퍼니스 vs RTA vs LSA 열 프로파일 및 도펀트 확산",
        "svg": """<svg viewBox="0 0 780 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="360" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <line x1="70" y1="280" x2="420" y2="280" stroke="#64748b" stroke-width="1.5"/>
  <line x1="70" y1="50" x2="70" y2="280" stroke="#64748b" stroke-width="1.5"/>
  <text x="380" y="305" fill="#94a3b8" font-size="11">시간 (t)</text>
  <text x="25" y="60" fill="#94a3b8" font-size="11">온도(℃)</text>
  <path d="M 70 280 L 120 120 L 260 120 L 310 280" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="2"/>
  <text x="150" y="150" fill="#f87171" font-size="11.5" font-weight="700">전통 Furnace (수 시간, 거대 열 예산)</text>
  <path d="M 120 280 L 150 90 L 170 280" fill="rgba(245, 158, 11, 0.3)" stroke="#f59e0b" stroke-width="2"/>
  <text x="175" y="100" fill="#fbbf24" font-size="11" font-weight="700">RTA (수 초)</text>
  <line x1="200" y1="280" x2="202" y2="70" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="210" y="75" fill="#38bdf8" font-size="11" font-weight="700">LSA (밀리초 단위, 극소 열 예산)</text>
  <rect x="450" y="40" width="305" height="280" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="465" y="65" fill="#38bdf8" font-size="12" font-weight="800">열 예산에 따른 접합 깊이(Xj) 변화</text>
  <line x1="470" y1="260" x2="730" y2="260" stroke="#64748b" stroke-width="1.2"/>
  <line x1="470" y1="90" x2="470" y2="260" stroke="#64748b" stroke-width="1.2"/>
  <text x="690" y="280" fill="#94a3b8" font-size="10">깊이 (x)</text>
  <text x="440" y="95" fill="#94a3b8" font-size="10">농도</text>
  <path d="M 470 110 Q 510 120 540 260" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
  <text x="510" y="180" fill="#38bdf8" font-size="10" font-weight="700">초기 주입 (USJ 사수)</text>
  <path d="M 470 140 Q 560 160 680 260" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="580" y="220" fill="#ef4444" font-size="10" font-weight="700">과도 열 예산 ➔ 확산 붕괴</text>
  <text x="465" y="305" fill="#34d399" font-size="10.5">※ 결론: 도펀트 활성화만 시키고 확산은 막는다!</text>
</svg>""",
        "lecture": r"""<h3>1. 열 예산(Thermal Budget)의 개념과 물리적 위협</h3>
<p>열 예산은 고온 환경($T$)에 노출된 시간($t$)의 함수로, 확산 길이 공식 $L_{diff} = 2\sqrt{D \cdot t}$ (여기서 $D = D_0 \exp\left(-\frac{E_a}{k_B T}\right)$)에 의해 결정됩니다. 온도가 높고 시간이 길어질수록 불순물 이온의 열 확산 거리가 지수함수적으로 증가합니다.</p>
<ul>
  <li><strong>접합 프로파일 붕괴</strong>: 기껏 수 keV 저에너지로 주입해 놓은 초얕은 소스/드레인(USJ) 접합이 깊숙이 퍼져버려 게이트 통제력이 상실되고 DIBL과 펀치스루가 발생합니다.</li>
  <li><strong>계면 상호작용 및 스트레스</strong>: 메탈 및 실리사이드 박막의 응집(Agglomeration) 및 열팽창 차이에 의한 크랙이 발생합니다.</li>
</ul>
<h3>2. 열 예산 저감 기술의 진화</h3>
<p>현대 공정은 주입된 이온을 실리콘 격자 자리에 끼워 넣는 전기적 활성화(Activation)와 결정 결함 회복은 달성하되 확산은 원천 차단하기 위해 스파이크 RTA ➔ 레이저 스파이크 어닐링(LSA, 초단파 펄스) 방식을 채택합니다.</p>"""
    },

    # 3. 산화 3) 표면 반응속도 vs. 확산 속도 (Deal-Grove 모델)
    {
        "id": "q-03",
        "num": "03",
        "badge": "⭐ 최신 질문 (산화 3/3)",
        "title": "산화 3) 표면 반응속도 vs. 확산 속도 (Deal-Grove 모델)",
        "summary": [
            "<strong>딜-그로브(Deal-Grove) 모델</strong>은 열 산화막의 성장 속도를 가스 분위기 유속(F₁), 산화막 내부 확산 유속(F₂), Si 계면 화학 반응 유속(F₃)의 연속 평형으로 해석하는 지배 공식입니다.",
            "<strong>초기 박막 단계 (선형 영역: Linear Region)</strong>는 산화막이 얇아 확산 저항이 없으므로 '실리콘 표면의 화학 반응 속도 상수(ks)'가 전체 성장을 지배합니다 ($x_o \approx \frac{B}{A} t$).",
            "<strong>후막 단계 (포물선 영역: Parabolic Region)</strong>는 산화종이 이미 두껍게 형성된 SiO₂ 박막을 통과해야 하므로 '산화막 내부의 확산 속도 계수(Deff)'가 전체 성장을 지배합니다 ($x_o \approx \sqrt{B t}$).",
            "초미세 게이트 산화막(수 nm) 제어 시에는 Deal-Grove 모델의 선형 초기 이상 급속 성장(Initial Fast Oxidation) 현상을 보정하기 위해 Massoud 모델 등이 활용됩니다."
        ],
        "svg_title": "📊 [Deal-Grove 산화 역학 모델] 3대 유속(F1, F2, F3)과 선형-포물선 성장 곡선",
        "svg": """<svg viewBox="0 0 780 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="360" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="25" y="30" width="370" height="300" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="40" y="55" fill="#38bdf8" font-size="12" font-weight="800">1. Deal-Grove 3대 정상상태 유속 (F₁ = F₂ = F₃)</text>
  <rect x="40" y="80" width="100" height="200" fill="#1e293b"/>
  <text x="50" y="180" fill="#94a3b8" font-size="11">기체 가스 (Cg)</text>
  <rect x="140" y="80" width="120" height="200" fill="#0284c7" opacity="0.4"/>
  <text x="155" y="160" fill="#38bdf8" font-size="11">SiO₂ 산화막 (xo)</text>
  <text x="150" y="180" fill="#cbd5e1" font-size="10">확산 유속 F₂ (Deff)</text>
  <rect x="260" y="80" width="110" height="200" fill="#334155"/>
  <text x="275" y="180" fill="#f8fafc" font-size="11">Si 기판 (계면)</text>
  <text x="270" y="200" fill="#f59e0b" font-size="10">반응 유속 F₃ (ks)</text>
  <line x1="90" y1="120" x2="310" y2="120" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3"/>
  <text x="40" y="305" fill="#f87171" font-size="10.5">※ 평형 상태에서 전체 속도는 가장 느린 단계가 율속!</text>

  <rect x="415" y="30" width="340" height="300" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="430" y="55" fill="#38bdf8" font-size="12" font-weight="800">2. 산화막 성장 곡선 (시간 t vs 두께 xo)</text>
  <line x1="450" y1="260" x2="720" y2="260" stroke="#64748b" stroke-width="1.2"/>
  <line x1="450" y1="80" x2="450" y2="260" stroke="#64748b" stroke-width="1.2"/>
  <text x="690" y="280" fill="#94a3b8" font-size="10">시간 (t)</text>
  <text x="420" y="85" fill="#94a3b8" font-size="10">두께</text>
  <path d="M 450 260 L 520 180 Q 600 130 720 110" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
  <text x="460" y="170" fill="#38bdf8" font-size="11" font-weight="700">① 선형 영역 (Linear: ks 지배)</text>
  <text x="460" y="190" fill="#94a3b8" font-size="9.5">xo = (B/A)(t + τ)</text>
  <text x="560" y="100" fill="#10b981" font-size="11" font-weight="700">② 포물선 영역 (Parabolic: Deff 지배)</text>
  <text x="560" y="120" fill="#94a3b8" font-size="9.5">xo² = B · t</text>
  <text x="430" y="305" fill="#34d399" font-size="10.5">두꺼워질수록 산소가 뚫고 들어오기 힘들어 속도 둔화!</text>
</svg>""",
        "lecture": r"""<h3>1. Deal-Grove 수식 체계의 핵심</h3>
<p>산화 반응의 관계식은 다음과 같은 2차 방정식으로 정리됩니다:</p>
<div class="formula-box">$$x_o^2 + A x_o = B(t + \tau)$$</div>
<p>여기서 $B$는 포물선 속도 상수(확산 제어 계수, $B = 2 D_{eff} C^* / N_1$), $B/A$는 선형 속도 상수(표면 반응 제어 계수, $B/A = k_s C^* / N_1$)입니다.</p>
<ul>
  <li><strong>선형 영역 ($x_o \ll A/2$, 초기 단계)</strong>: 산화막이 얇을 때는 $x_o^2$ 항을 무시할 수 있어 $x_o \approx \frac{B}{A}(t + \tau)$ 가 됩니다. 이때 속도는 실리콘 표면의 Si-Si 결합을 끊고 산소와 결합하는 화학 반응 속도 상수($k_s$)가 지배합니다. 결정면 (111)이 (100)보다 원자 밀도가 높아 선형 영역 속도가 더 빠릅니다.</li>
  <li><strong>포물선 영역 ($x_o \gg A/2$, 후막 단계)</strong>: 산화막이 두꺼워지면 $A x_o$ 항을 무시하여 $x_o^2 \approx B t \implies x_o \approx \sqrt{B t}$ 가 됩니다. 산화종($O_2, H_2O$)이 이미 형성된 두꺼운 SiO₂ 격자를 비집고 Si 계면까지 도달해야 하므로 확산 계수($D_{eff}$)가 전체 속도를 지배합니다.</li>
</ul>"""
    },

    # 4. 노광 1) 광학계 기본 수식 (Rayleigh 식)
    {
        "id": "q-04",
        "num": "04",
        "badge": "⭐ 최신 질문 (노광 1/3)",
        "title": "노광 1) 광학계 기본 수식 (Rayleigh 분해능과 초점심도)",
        "summary": [
            "<strong>레일리 분해능(Resolution, R)</strong> 공식은 $R = k_1 \frac{\lambda}{\\text{NA}}$ 이며, 두 패턴을 서로 분리하여 전사할 수 있는 최소 크기(CD)를 의미합니다 (작을수록 고해상도).",
            "<strong>초점심도(DOF: Depth of Focus)</strong> 공식은 $\\text{DOF} = k_2 \frac{\lambda}{\\text{NA}^2}$ 이며, 초점이 맺혀 패턴이 붕괴하지 않고 선명하게 유지되는 렌즈 축 방향의 허용 마진입니다.",
            "미세화를 위해 렌즈 개구수(NA)를 키우면 분해능 R은 선형(1/NA)으로 개선되지만, 공정 윈도우인 초점심도(DOF)는 제곱(1/NA²)으로 급격히 붕괴하는 치명적 공학적 트레이드오프가 존재합니다.",
            "이를 극복하기 위해 파장 자체를 줄이는 액침 ArFi(193nm ➔ 물 굴절률로 NA 1.35) 및 파장 13.5nm의 극자외선(EUV) 도입이 필연적이었습니다."
        ],
        "svg_title": "📊 [Rayleigh 노광 광학계] 파장(λ), 개구수(NA)에 따른 Resolution vs DOF 트레이드오프",
        "svg": """<svg viewBox="0 0 780 350" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="350" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="25" y="30" width="360" height="290" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="40" y="55" fill="#38bdf8" font-size="12" font-weight="800">노광 렌즈계와 개구수(NA = n · sin θ)</text>
  <path d="M 80 80 Q 205 105 330 80 Q 205 55 80 80 Z" fill="#38bdf8" opacity="0.4"/>
  <polygon points="120,80 290,80 205,220" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="1"/>
  <rect x="110" y="220" width="190" height="15" fill="#475569"/>
  <text x="180" y="232" fill="#ffffff" font-size="10">웨이퍼 표면</text>
  <rect x="170" y="200" width="70" height="40" fill="none" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2,2"/>
  <text x="245" y="215" fill="#f59e0b" font-size="10.5" font-weight="700">DOF 마진 허용구간</text>
  <text x="40" y="270" fill="#cbd5e1" font-size="11">• θ 각도가 클수록 ➔ NA 증가 ➔ 미세 패턴 전사</text>
  <text x="40" y="295" fill="#f87171" font-size="11">• 대신 빛이 급격히 꺾여 DOF 구간이 극도로 좁아짐!</text>

  <rect x="405" y="30" width="350" height="290" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="420" y="55" fill="#38bdf8" font-size="12" font-weight="800">핵심 수식 및 미세화 딜레마</text>
  <rect x="420" y="75" width="320" height="60" rx="6" fill="#1e293b"/>
  <text x="435" y="100" fill="#38bdf8" font-size="13" font-weight="800">분해능 (R) = k₁ · (λ / NA)</text>
  <text x="435" y="122" fill="#cbd5e1" font-size="10.5">➔ λ를 줄이거나 NA를 키우면 선폭(R) 축소 (Good)</text>

  <rect x="420" y="145" width="320" height="60" rx="6" fill="#1e293b"/>
  <text x="435" y="170" fill="#f59e0b" font-size="13" font-weight="800">초점심도 (DOF) = k₂ · (λ / NA²)</text>
  <text x="435" y="192" fill="#cbd5e1" font-size="10.5">➔ NA를 2배 키우면 DOF는 1/4로 추락 (공정 위기!)</text>

  <rect x="420" y="215" width="320" height="90" rx="6" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1"/>
  <text x="435" y="235" fill="#10b981" font-size="11" font-weight="700">해결책의 역사적 흐름</text>
  <text x="435" y="255" fill="#cbd5e1" font-size="10">1. 액침 노광: 렌즈-웨이퍼 사이 물(n=1.44) 채워 NA 1.35 달성</text>
  <text x="435" y="275" fill="#cbd5e1" font-size="10">2. EUV 도입: ArF(193nm) 대비 파장을 13.5nm로 1/14 단축!</text>
  <text x="435" y="295" fill="#38bdf8" font-size="10">3. High-NA: 차세대 NA 0.55 아나모픽 광학계 전환</text>
</svg>""",
        "lecture": r"""<h3>1. Rayleigh 공식의 심층 해체</h3>
<p>포토리소그래피에서 빛의 회절 한계(Diffraction Limit)를 설명하는 두 가지 기본 공식입니다:</p>
<div class="formula-box">$$R = k_1 \frac{\lambda}{\text{NA}}, \quad \text{DOF} = k_2 \frac{\lambda}{\text{NA}^2}$$</div>
<ul>
  <li>$\lambda$ (파장): 광원의 파장 (G-line 436nm ➔ I-line 365nm ➔ KrF 248nm ➔ ArF 193nm ➔ EUV 13.5nm).</li>
  <li>$\text{NA} = n \sin\theta$ (개구수): 렌즈가 빛을 모으는 능력. $n$은 매질의 굴절률, $\theta$는 렌즈 반각.</li>
  <li>$k_1, k_2$ (공정 상수): 레지스트 품질, 조명계 및 RET 기술 수준에 따른 계수 (물리적 이론 한계 $k_1 = 0.25$).</li>
</ul>
<h3>2. 공학적 딜레마와 타개책</h3>
<p>NA를 키우면 해상도는 좋아지지만 초점 마진($\text{DOF}$)이 극도로 얇아져 웨이퍼의 미세한 굴곡(Topography)만 있어도 패턴 초점이 나가버립니다. 이를 해결하기 위해 반도체 업계는 웨이퍼 표면을 나노 단위로 평탄화하는 CMP 공정을 극대화함과 동시에 파장 $\lambda$를 13.5nm로 단축하는 EUV로 전환했습니다.</p>"""
    },

    # 5. 노광 2) EUV 관련 핵심 현안
    {
        "id": "q-05",
        "num": "05",
        "badge": "⭐ 최신 질문 (노광 2/3)",
        "title": "노광 2) EUV 관련 핵심 현안 (13.5nm, 반사 광학계, 펠리클, 스토캐스틱)",
        "summary": [
            "<strong>EUV(극자외선, 13.5nm)</strong>는 대기 및 굴절 렌즈(유리)를 포함한 모든 물질에 흡수되므로, 100% 고진공 챔버와 Mo/Si 다층 반사경(Bragg Reflector)으로만 광학계를 구성합니다.",
            "<strong>LPP(Laser-Produced Plasma) 광원</strong>은 초당 5만 번 분사되는 액적 주석(Sn) 방울을 고출력 CO₂ 레이저로 2차 타격하여 고온 플라즈마를 발생시켜 EUV 빛을 뽑아냅니다.",
            "<strong>펠리클(Pellicle)</strong>은 마스크를 파티클로부터 보호하는 초박막(CNT 등)으로, EUV 투과율 90% 이상과 400W 고온 광원 열을 견디는 내구성이 핵심 과제입니다.",
            "<strong>스토캐스틱 결함(Stochastic Defect)</strong>은 광자 에너지가 높아 파장당 도달하는 포톤(Photon) 수가 부족하여 통계적 불균일로 인해 패턴이 끊기거나(Line Broken) 붙는(Micro-bridge) 치명적 나노 불량입니다."
        ],
        "svg_title": "📊 [EUV 노광 시스템 & 핵심 현안] 반사형 마스크 광학계, 펠리클 및 스토캐스틱 불량",
        "svg": """<svg viewBox="0 0 780 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="360" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="25" y="30" width="370" height="300" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="40" y="55" fill="#38bdf8" font-size="12" font-weight="800">EUV 반사형 광학계 메커니즘 (진공 챔버)</text>
  <circle cx="70" cy="100" r="14" fill="#ef4444"/>
  <text x="95" y="105" fill="#f87171" font-size="11" font-weight="700">LPP 주석(Sn) 플라즈마</text>
  <path d="M 60 160 Q 90 180 120 160" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <text x="130" y="170" fill="#94a3b8" font-size="10">Mo/Si 반사경 (반사율 ~68%)</text>
  <rect x="230" y="80" width="120" height="15" fill="#cbd5e1"/>
  <text x="245" y="92" fill="#0f172a" font-size="10" font-weight="800">반사형 마스크</text>
  <line x1="230" y1="105" x2="350" y2="105" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="3,2"/>
  <text x="245" y="120" fill="#fbbf24" font-size="10" font-weight="700">펠리클 (투과율 >90% 사수)</text>
  <path d="M 70 114 L 90 165 L 290 95 L 310 240 L 220 280" fill="none" stroke="#fbbf24" stroke-width="1.5"/>
  <rect x="170" y="280" width="100" height="15" fill="#475569"/>
  <text x="200" y="292" fill="#ffffff" font-size="10">웨이퍼</text>

  <rect x="415" y="30" width="340" height="300" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="430" y="55" fill="#38bdf8" font-size="12" font-weight="800">EUV 4대 핵심 난제 및 현안</text>
  <rect x="430" y="70" width="310" height="52" rx="4" fill="#1e293b"/>
  <text x="440" y="88" fill="#f87171" font-size="11" font-weight="700">1. 광학계 투과율 감쇄 (반사율 68% 한계)</text>
  <text x="440" y="106" fill="#cbd5e1" font-size="10">미러 10여회 반사 시 최종 도달 빛은 초기 출력의 1~2%에 불과</text>
  <rect x="430" y="130" width="310" height="52" rx="4" fill="#1e293b"/>
  <text x="440" y="148" fill="#fbbf24" font-size="11" font-weight="700">2. 펠리클(Pellicle) 내열성</text>
  <text x="440" y="166" fill="#cbd5e1" font-size="10">400W 고출력 EUV 열 흡수 ➔ 800℃ 열 변형 방지 탄소나노튜브(CNT)</text>
  <rect x="430" y="190" width="310" height="52" rx="4" fill="#1e293b"/>
  <text x="440" y="208" fill="#34d399" font-size="11" font-weight="700">3. 스토캐스틱(Stochastic) 결함</text>
  <text x="440" y="226" fill="#cbd5e1" font-size="10">포톤 샷 노이즈(Photon Shot Noise)로 국소적 브릿지/단선 발생</text>
  <rect x="430" y="250" width="310" height="65" rx="4" fill="#1e293b"/>
  <text x="440" y="268" fill="#38bdf8" font-size="11" font-weight="700">4. High-NA (NA 0.33 ➔ 0.55)</text>
  <text x="440" y="286" fill="#cbd5e1" font-size="10">아나모픽(Anamorphic) 렌즈(X축 4배, Y축 8배) 적용으로 마스크 축소비 비대칭</text>
</svg>""",
        "lecture": r"""<h3>1. EUV 반사 광학계와 Mo/Si 브래그 반사경</h3>
<p>13.5nm 파장은 물질 흡수도가 너무 높아 기존 유리 렌즈를 쓸 수 없습니다. 몰리브덴(Mo)과 실리콘(Si)을 교대로 40~50층 쌓은 브래그 다층막 반사경(Bragg Reflector)을 사용하며, 이론적 최대 반사율은 약 68~70% 수준입니다. 거울을 10번 거치면 웨이퍼에 도달하는 빛 에너지가 $(0.68)^{10} \approx 2\%$ 로 급감하므로 극도로 강력한 LPP 광원(350W 이상)이 요구됩니다.</p>
<h3>2. 스토캐스틱 효과(Photon Shot Noise)</h3>
<p>빛 에너지는 $E = h c / \lambda$ 입니다. 파장이 13.5nm로 짧아지면 광자 1개가 갖는 에너지가 ArF(193nm) 대비 약 14배나 큽니다. 같은 광량(Dose)을 쪼여도 도달하는 절대 광자 수가 1/14로 줄어들어, 포토레지스트 내부에서 광자가 불균일하게 흡수되는 포톤 샷 노이즈(Photon Shot Noise)로 인해 선폭 불균일(LER)과 미세 나노 단선/쇼트가 발생하는 치명적 현안이 대두됩니다.</p>"""
    },

    # 6. 노광 3) 리소그래피 미세화 기법
    {
        "id": "q-06",
        "num": "06",
        "badge": "⭐ 최신 질문 (노광 3/3)",
        "title": "노광 3) 리소그래피 미세화 기법 (OPC, OAI, MPT: LELE, SADP)",
        "summary": [
            "<strong>OPC (Optical Proximity Correction)</strong>는 빛의 회절로 인해 모서리가 둥글어지거나(Corner Rounding) 선폭이 수축하는 광학 왜곡 현상을 역계산하여 마스크 모서리에 세리프(Serif)를 달아 보정하는 필수 기술입니다.",
            "<strong>OAI (Off-Axis Illumination)</strong>는 빛을 수직이 아닌 비스듬한 경사각으로 입사시켜 0차 회절광과 1차 회절광의 렌즈 입사 간섭을 극대화함으로써 미세 패턴 해상도를 대폭 향상시키는 조명 기법입니다.",
            "<strong>MPT (Multi-Patterning Technology)</strong>는 단일 노광 한계를 돌파하기 위해 다중 노광/식각(LELE)이나 화학 증착 스페이서를 마스크로 활용해 1회 노광 대비 피치를 절반/4분의 1로 쪼개는 자가정렬 패턴화(SADP/SAQP) 기술입니다."
        ],
        "svg_title": "📊 [미세화 3대 RET 기술] OPC 패턴 보정 & SADP (스페이서 자가정렬 4단계)",
        "svg": """<svg viewBox="0 0 780 350" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="350" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="25" y="30" width="340" height="290" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="40" y="55" fill="#38bdf8" font-size="12" font-weight="800">1. OPC (Optical Proximity Correction)</text>
  <text x="40" y="80" fill="#cbd5e1" font-size="10.5">• 마스크 설계 형상 vs 웨이퍼 전사 결과</text>
  <rect x="40" y="95" width="80" height="60" fill="#64748b"/>
  <text x="50" y="130" fill="#ffffff" font-size="9.5">단순 사각 마스크</text>
  <text x="130" y="130" fill="#f87171" font-size="14" font-weight="900">➔</text>
  <ellipse cx="180" cy="125" rx="35" ry="25" fill="#ef4444" opacity="0.6"/>
  <text x="155" y="128" fill="#ffffff" font-size="9">라운딩 왜곡</text>
  <path d="M 40 190 L 50 190 L 50 180 L 100 180 L 100 190 L 110 190 L 110 230 L 100 230 L 100 240 L 50 240 L 50 230 L 40 230 Z" fill="#38bdf8"/>
  <text x="45" y="213" fill="#0f172a" font-size="9.5" font-weight="800">OPC 보정 마스크</text>
  <text x="130" y="213" fill="#34d399" font-size="14" font-weight="900">➔</text>
  <rect x="155" y="185" width="60" height="50" rx="3" fill="#10b981" opacity="0.8"/>
  <text x="165" y="213" fill="#ffffff" font-size="9.5" font-weight="700">목표 직사각 달성</text>
  <text x="40" y="275" fill="#fbbf24" font-size="10">• 세리프(Serif), 라인 엔드 보정, 해머헤드 적용</text>

  <rect x="385" y="30" width="370" height="290" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="400" y="55" fill="#38bdf8" font-size="12" font-weight="800">2. SADP (Self-Aligned Double Patterning)</text>
  <text x="400" y="75" fill="#cbd5e1" font-size="10.5">희생막 코어 양쪽에 스페이서를 증착하여 피치를 1/2로 분할</text>
  <rect x="420" y="95" width="50" height="25" fill="#94a3b8"/>
  <text x="480" y="112" fill="#cbd5e1" font-size="10">① 1차 노광/식각으로 코어(Core Mandrel) 형성</text>
  <rect x="420" y="135" width="50" height="25" fill="#94a3b8"/>
  <rect x="408" y="135" width="12" height="25" fill="#38bdf8"/>
  <rect x="470" y="135" width="12" height="25" fill="#38bdf8"/>
  <text x="490" y="152" fill="#cbd5e1" font-size="10">② 측벽에 얇은 스페이서 증착/에치백</text>
  <rect x="408" y="175" width="12" height="25" fill="#38bdf8"/>
  <rect x="470" y="175" width="12" height="25" fill="#38bdf8"/>
  <text x="490" y="192" fill="#cbd5e1" font-size="10">③ 코어 제거 ➔ 스페이서만 마스크로 남음</text>
  <rect x="408" y="215" width="12" height="25" fill="#10b981"/>
  <rect x="470" y="215" width="12" height="25" fill="#10b981"/>
  <text x="490" y="232" fill="#34d399" font-size="10" font-weight="700">④ 하부막 식각 ➔ 피치 1/2 (Pitch Halving 달성!)</text>
  <text x="400" y="275" fill="#fbbf24" font-size="10">※ 오버레이(Overlay) 에러에 독립적인 강력한 미세화 기법</text>
</svg>""",
        "lecture": r"""<h3>1. 광학 근접 보정(OPC)의 핵심 알고리즘</h3>
<p>패턴 선폭이 빛 파장보다 작아지면 회절로 인해 인접 패턴 간의 빛 간섭이 발생합니다. 직선 끝단이 오그라들거나(Line-end shortening) 모서리가 둥글어집니다. 이를 방지하기 위해 마스크 모서리에 돌기를 달아주는 세리프(Serif), 패턴 간격을 조절하는 바이어싱(Biasing)을 전산 시뮬레이션(Model-based OPC)으로 계산하여 마스크에 선반영합니다.</p>
<h3>2. SADP / SAQP의 자가 정렬(Self-Aligned) 원리</h3>
<p>LELE(노광-식각-노광-식각)는 두 번째 노광 시 마스크를 맞추는 오버레이 오차(Overlay Error)로 인해 패턴이 어긋나는 한계가 있습니다. 반면 SADP는 1차 패턴의 측벽에 원자층 단위로 균일하게 증착되는 CVD 박막(스페이서)을 형성한 뒤 코어를 파내므로, 노광 장비의 정렬 정밀도와 상관없이 완벽하게 대칭인 1/2 피치 패턴을 만듭니다. 이를 두 번 반복한 것이 SAQP(피치 1/4)입니다.</p>"""
    },

    # 7. 식각 1) 건식/습식 식각의 차이점
    {
        "id": "q-07",
        "num": "07",
        "badge": "⭐ 최신 질문 (식각 1/3)",
        "title": "식각 1) 건식/습식 식각의 차이점 (Dry vs Wet Etching)",
        "summary": [
            "<strong>습식 식각(Wet Etch)</strong>은 액체 화학 용액(HF, H₃PO₄ 등)을 이용해 반응 속도가 빠르고 선택비(Selectivity)가 매우 우수하지만, 모든 방향으로 깎이는 등방성(Isotropic) 특성 때문에 미세 패턴 형성이 불가능합니다.",
            "<strong>건식 식각(Dry Etch / RIE)</strong>은 플라즈마 상태의 가스를 이용해 전기장으로 가속된 이온 충돌을 결합하여 수직 비등방성(Anisotropic) 패턴을 완벽히 구현하므로 모든 첨단 반도체의 주력 공정입니다.",
            "습식 식각은 패턴 형성이 아닌 박막 전면 제거(Strip), 식각 후 잔여물 세정(Clean), 자연 산화막 제거(Native Oxide Removal) 등의 용도로 제한적으로 특화되어 공존합니다."
        ],
        "svg_title": "📊 [건식 vs 습식 식각] 식각 단면 프로파일, 선택비 및 언더컷(Undercut) 비교",
        "svg": """<svg viewBox="0 0 780 340" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="340" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="25" y="30" width="350" height="280" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
  <text x="40" y="55" fill="#f59e0b" font-size="12.5" font-weight="800">1. 습식 식각 (Wet Etch: 화학 용액)</text>
  <text x="40" y="78" fill="#cbd5e1" font-size="11">• 화학 반응 ➔ 100% 등방성 (모든 방향 균일)</text>
  <text x="40" y="98" fill="#34d399" font-size="11">• 장점: 높은 선택비 (>100:1), 하부막 손상 없음</text>
  <text x="40" y="118" fill="#f87171" font-size="11">• 치명적 단점: 마스크 밑 파고듦 (언더컷 발생)</text>
  <rect x="60" y="140" width="120" height="18" fill="#64748b"/>
  <rect x="200" y="140" width="120" height="18" fill="#64748b"/>
  <text x="135" y="153" fill="#ffffff" font-size="9.5">마스크</text>
  <path d="M 60 158 Q 120 220 180 220 Q 240 220 320 158" fill="none" stroke="#f59e0b" stroke-width="3"/>
  <text x="145" y="195" fill="#f87171" font-size="11" font-weight="700">언더컷 (Undercut)</text>
  <text x="40" y="275" fill="#cbd5e1" font-size="10.5">※ 미세 선폭 전사 불가능 ➔ 세정/Strip 전용</text>

  <rect x="405" y="30" width="350" height="280" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="420" y="55" fill="#38bdf8" font-size="12.5" font-weight="800">2. 건식 식각 (Dry Etch / RIE: 플라즈마)</text>
  <text x="420" y="78" fill="#cbd5e1" font-size="11">• 이온 직진 가속 + 라디칼 화학 반응</text>
  <text x="420" y="98" fill="#38bdf8" font-size="11">• 장점: 완벽한 수직 비등방성 (수직벽 유지)</text>
  <text x="420" y="118" fill="#f87171" font-size="11">• 단점: 물리 충돌 손상(Damage), 상대적 낮은 선택비</text>
  <rect x="440" y="140" width="120" height="18" fill="#64748b"/>
  <rect x="580" y="140" width="120" height="18" fill="#64748b"/>
  <text x="515" y="153" fill="#ffffff" font-size="9.5">마스크</text>
  <path d="M 560 158 L 560 230 L 580 230 L 580 158" fill="none" stroke="#38bdf8" stroke-width="3"/>
  <text x="530" y="200" fill="#38bdf8" font-size="11" font-weight="700">수직 프로파일</text>
  <text x="420" y="275" fill="#34d399" font-size="10.5">※ 수직벽 구현으로 나노미터급 초미세 패턴 전담!</text>
</svg>""",
        "lecture": r"""<h3>1. 건식 식각과 습식 식각의 비교 스펙트럼</h3>
<p>두 식각 방식의 차이는 식각제의 상태(액체 vs 기체 플라즈마)와 방향성(등방성 vs 비등방성)에 있습니다.</p>
<ul>
  <li><strong>선택비(Selectivity)</strong>: 목표 식각막과 하부 막(또는 마스크)의 식각 속도 비입니다. 습식은 화학 결합의 특이성을 이용하므로 선택비가 수백 대 1에 달하지만, 건식 식각은 물리적 이온 충돌이 동반되므로 마스크나 하부막도 함께 깎여 선택비 제어가 까다롭습니다.</li>
  <li><strong>언더컷(Undercut)과 바이어스(Bias)</strong>: 습식 식각은 마스크 하부로 약 1:1 비율로 파고들어가 패턴 선폭이 무너집니다. 나노 스케일에서는 비등방성 건식 식각(RIE)만이 유일한 해결책입니다.</li>
</ul>"""
    },

    # 8. 식각 2) 등방성 식각 vs 비등방성 식각
    {
        "id": "q-08",
        "num": "08",
        "badge": "⭐ 최신 질문 (식각 2/3)",
        "title": "식각 2) 등방성 식각 vs 비등방성 식각 (Isotropic vs Anisotropic)",
        "summary": [
            "<strong>등방성 식각(Isotropic)</strong>은 수평과 수직 방향 식각 속도가 동일하여 식각 단면이 둥글게 파이며 마스크 밑단이 잘려나가는 언더컷(Undercut)을 유발합니다.",
            "<strong>비등방성 식각(Anisotropic)</strong>은 수직 방향 식각 속도가 수평 방향 속도보다 압도적으로 빨라 마스크 패턴과 동일한 각도(90° 수직 프로파일)를 유지합니다.",
            "비등방성을 달성하는 핵심 메커니즘은 <strong>'이온의 수직 충돌 에너지'</strong>와 플라즈마 반응 가스에서 형성되는 <strong>'측벽 보호막(Passivation Polymer Layer)'</strong>의 상호작용입니다."
        ],
        "svg_title": "📊 [비등방성 식각 구현 원리] 이온 충돌 + 측벽 패시베이션 폴리머 메커니즘",
        "svg": """<svg viewBox="0 0 780 330" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="330" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <text x="30" y="45" fill="#38bdf8" font-size="12" font-weight="800">측벽 보호막(Side Passivation) 기반 고이방성 식각</text>
  <rect x="150" y="70" width="180" height="25" fill="#64748b"/>
  <rect x="450" y="70" width="180" height="25" fill="#64748b"/>
  <text x="220" y="87" fill="#ffffff" font-size="11" font-weight="700">포토레지스트 마스크</text>
  <text x="520" y="87" fill="#ffffff" font-size="11" font-weight="700">포토레지스트 마스크</text>

  <path d="M 50 95 L 330 95 L 330 240 L 450 240 L 450 95 L 730 95 L 730 280 L 50 280 Z" fill="#1e293b" stroke="#334155"/>
  <rect x="330" y="95" width="8" height="145" fill="#f59e0b"/>
  <rect x="442" y="95" width="8" height="145" fill="#f59e0b"/>
  <text x="210" y="170" fill="#f59e0b" font-size="11" font-weight="700">측벽 보호막 (CFx 폴리머) ➔</text>
  <text x="460" y="170" fill="#f59e0b" font-size="11" font-weight="700"> 측벽 에칭 차단!</text>

  <line x1="390" y1="60" x2="390" y2="230" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4,3"/>
  <polygon points="386,225 390,237 394,225" fill="#38bdf8"/>
  <text x="350" y="45" fill="#38bdf8" font-size="11" font-weight="800">가속된 양이온 (Ar+, CF₃+)</text>
  <text x="340" y="258" fill="#34d399" font-size="10.5" font-weight="700">바닥 보호막은 이온 충돌로 파괴 ➔ 수직 식각 계속 진행!</text>
</svg>""",
        "lecture": r"""<h3>1. 비등방성 계수(Anisotropy Factor)의 정의</h3>
<div class="formula-box">$$A_f = 1 - \frac{R_L}{R_V}$$</div>
<p>여기서 $R_L$은 수평(Lateral) 식각 속도, $R_V$는 수직(Vertical) 식각 속도입니다. $R_L = R_V$이면 $A_f = 0$(완전 등방성), $R_L = 0$이면 $A_f = 1$(완전 비등방성)입니다.</p>
<h3>2. 측벽 보호막(Passivation) 메커니즘</h3>
<p>식각 가스에 탄화불소 가스를 혼합하면 표면에 얇은 테플론 계열 폴리머($\text{CF}_x$)가 증착됩니다. 수직 방향 바닥면은 수직 입사하는 고에너지 이온의 물리적 스퍼터링으로 폴리머가 즉시 벗겨져 식각이 진행되지만, 수직 측벽은 이온 충돌이 없어 폴리머가 남아 라디칼의 측면 공격을 완벽히 방어합니다.</p>"""
    },

    # 9. 식각 3) 플라즈마의 역할
    {
        "id": "q-09",
        "num": "09",
        "badge": "⭐ 최신 질문 (식각 3/3)",
        "title": "식각 3) 식각 공정에서 플라즈마의 역할 (라디칼 vs 이온 충돌 RIE)",
        "summary": [
            "<strong>플라즈마(Plasma)</strong>는 중성 가스를 고주파(RF) 전력으로 해리시켜 <strong>라디칼(Radical: 화학종)</strong>과 <strong>양이온(Positive Ion: 물리종)</strong>을 동시에 생성하는 핵심 매개체입니다.",
            "<strong>라디칼(Radical)</strong>은 반응성이 매우 높아 화학적 반응으로 결합하여 휘발성 가스를 배출(선택비 담당)하지만 방향성이 없고, <strong>양이온(Ion)</strong>은 캐소드 음전위 쉬스(Sheath) 전계에 의해 수직 가속 충돌하여 결합을 파괴(비등방성 담당)합니다.",
            "이 두 성분이 결합된 <strong>반응성 이온 식각(RIE: Reactive Ion Etching)</strong>은 순수 화학 반응이나 물리 스퍼터링 단독 속도의 수십 배에 달하는 '시너지 화학-물리 효과'로 고속 고선택비 수직 식각을 구현합니다."
        ],
        "svg_title": "📊 [RIE 플라즈마 시너지] 플라즈마 쉬스(Sheath), 라디칼 반응 & 이온 충돌 메커니즘",
        "svg": """<svg viewBox="0 0 780 340" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="340" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="25" y="30" width="360" height="280" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="40" y="55" fill="#38bdf8" font-size="12" font-weight="800">플라즈마 글로우 & 음전위 쉬스(Sheath)</text>
  <rect x="40" y="70" width="330" height="100" fill="rgba(147, 51, 234, 0.2)" rx="4"/>
  <text x="110" y="115" fill="#c084fc" font-size="12" font-weight="800">벌크 플라즈마 (라디칼 + 이온 + 전자)</text>
  <rect x="40" y="170" width="330" height="40" fill="rgba(56, 189, 248, 0.15)"/>
  <text x="70" y="195" fill="#38bdf8" font-size="11" font-weight="700">플라즈마 쉬스 (강력한 하향 수직 전계 E ⬇)</text>
  <rect x="40" y="210" width="330" height="40" fill="#334155"/>
  <text x="130" y="235" fill="#ffffff" font-size="11" font-weight="700">웨이퍼 척 (RF 바이어스, 음전위 형성)</text>
  <text x="40" y="280" fill="#f87171" font-size="10.5">※ 전자는 가벼워 먼저 빠져나가 벌크는 (+), 척은 (-) 셀프 바이어스</text>

  <rect x="405" y="30" width="350" height="280" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="420" y="55" fill="#38bdf8" font-size="12" font-weight="800">화학 + 물리 시너지 (Ion-Assisted Etching)</text>
  <circle cx="450" cy="90" r="12" fill="#38bdf8"/>
  <text x="475" y="95" fill="#38bdf8" font-size="11" font-weight="700">양이온 (Ion): 표면 결합 파괴, 비등방성 부여</text>
  <circle cx="450" cy="130" r="12" fill="#f59e0b"/>
  <text x="475" y="135" fill="#f59e0b" font-size="11" font-weight="700">라디칼 (Radical): 자발 화학반응, 휘발 가스 배출</text>

  <rect x="420" y="160" width="320" height="120" rx="6" fill="#1e293b"/>
  <text x="430" y="180" fill="#10b981" font-size="11" font-weight="700">Coburn-Winters 실험의 결론</text>
  <text x="430" y="200" fill="#cbd5e1" font-size="10">• XeF₂ 가스만 주입 ➔ 식각 속도 매우 느림</text>
  <text x="430" y="220" fill="#cbd5e1" font-size="10">• Ar⁺ 이온 빔만 조사 ➔ 스퍼터링 속도 보통</text>
  <text x="430" y="240" fill="#fbbf24" font-size="10.5" font-weight="700">• 둘 동시 인가 ➔ 단독 합계의 10배 폭발적 속도!</text>
  <text x="430" y="265" fill="#38bdf8" font-size="10">➔ 이온이 표면을 활성화시키면 라디칼이 낚아챔</text>
</svg>""",
        "lecture": r"""<h3>1. 플라즈마 쉬스(Plasma Sheath)와 자기 바이어스(Self-bias)</h3>
<p>플라즈마 내부에서 전자는 이온보다 질량이 수만 배 가벼워 속도가 훨씬 빠릅니다. 따라서 전극 벽면으로 전자가 먼저 도달하여 벽면은 음(-)의 전하로 대전되고, 벌크 플라즈마는 양(+)의 전위를 띱니다. 이 전위차로 인해 경계면에 쉬스(Sheath)라는 강한 전기장 영역이 형성되며, 양이온이 웨이퍼를 향해 직각으로 강력하게 가속 충돌합니다.</p>
<h3>2. RIE 시너지 (Ion-Assisted Chemical Etching)</h3>
<p>실리콘 식각 시 불소/염소 라디칼이 흡착되어 층을 형성합니다. 실온에서 이 결합은 자발 탈착되기 어렵지만, 수직 입사하는 이온이 충돌 에너지를 전달하면 휘발성 가스로 순간 증발하며 폭발적인 식각 속도를 냅니다.</p>"""
    },

    # 10. 이온주입 1) 장비 구동 원리
    {
        "id": "q-10",
        "num": "10",
        "badge": "⭐ 최신 질문 (이온주입 1/4)",
        "title": "이온주입 1) 장비 구동 원리 (이온원, 질량분석기, 가속관, 정전 척)",
        "summary": [
            "<strong>이온주입기(Ion Implanter)</strong>는 기체 소스를 플라즈마로 이온화한 후, 전자기장으로 원하는 단일 동위원소만 정밀 선별하여 고전압으로 웨이퍼에 강제 박아 넣는 장비입니다.",
            "<strong>질량 분석 자석(Mass Analyzer Magnet)</strong>은 로렌츠 힘($r = \frac{mv}{qB}$) 원리를 이용하여 질량 대 전하비($m/q$)에 따른 궤적 반경 차이로 원치 않는 불순물 분자를 100% 걸러냅니다.",
            "가속관(Accelerator)의 인가 전압은 침투 깊이(Energy)를 결정하고, 빔 전류의 적분값(Faraday Cup)은 주입 도즈량(Dose)을 1% 이내 오차로 초정밀 제어합니다."
        ],
        "svg_title": "📊 [이온주입기 장비 5대 모듈] 이온원 ➔ 질량분석 ➔ 가속기 ➔ 스캐너 ➔ 엔드스테이션",
        "svg": """<svg viewBox="0 0 780 330" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="330" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="25" y="60" width="110" height="180" rx="6" fill="#1e293b" stroke="#38bdf8"/>
  <text x="35" y="85" fill="#38bdf8" font-size="11" font-weight="800">① 이온원</text>
  <text x="35" y="105" fill="#94a3b8" font-size="9.5">(Ion Source)</text>
  <text x="35" y="130" fill="#cbd5e1" font-size="9">BF₃, PH₃ 가스</text>
  <text x="35" y="150" fill="#f59e0b" font-size="9">아크 방전 분해</text>
  <circle cx="80" cy="190" r="12" fill="#ef4444"/>
  <text x="65" y="195" fill="#ffffff" font-size="10">B+, F+</text>

  <path d="M 145 130 Q 185 80 235 80 L 235 150 Q 185 150 145 150 Z" fill="#334155" stroke="#f59e0b"/>
  <text x="160" y="110" fill="#f59e0b" font-size="11" font-weight="800">② 분석 자석</text>
  <text x="155" y="175" fill="#cbd5e1" font-size="9">B¹¹+만 90° 편향</text>
  <text x="155" y="190" fill="#f87171" font-size="9">(F+, P+ 걸러냄)</text>

  <rect x="250" y="60" width="130" height="90" rx="6" fill="#1e293b" stroke="#10b981"/>
  <text x="260" y="85" fill="#10b981" font-size="11" font-weight="800">③ 가속관</text>
  <text x="260" y="105" fill="#94a3b8" font-size="9.5">초고전압 인가</text>
  <text x="260" y="125" fill="#34d399" font-size="9">0.5keV ~ 3MeV</text>
  <text x="260" y="140" fill="#cbd5e1" font-size="9">➔ 깊이(Rp) 결정</text>

  <rect x="400" y="60" width="120" height="90" rx="6" fill="#1e293b" stroke="#8b5cf6"/>
  <text x="410" y="85" fill="#a78bfa" font-size="11" font-weight="800">④ 스캐너</text>
  <text x="410" y="105" fill="#cbd5e1" font-size="9">정전 편향판</text>
  <text x="410" y="125" fill="#cbd5e1" font-size="9">X-Y 고속 스캔</text>
  <text x="410" y="140" fill="#cbd5e1" font-size="9">웨이퍼 균일 주입</text>

  <rect x="540" y="40" width="210" height="250" rx="6" fill="#0f172a" stroke="#38bdf8"/>
  <text x="555" y="65" fill="#38bdf8" font-size="12" font-weight="800">⑤ 엔드스테이션 (End Station)</text>
  <rect x="620" y="90" width="12" height="120" fill="#64748b"/>
  <text x="640" y="145" fill="#ffffff" font-size="11" font-weight="700">웨이퍼 (Tilt/Twist 회전)</text>
  <rect x="560" y="120" width="40" height="60" fill="#1e293b" stroke="#f59e0b"/>
  <text x="565" y="145" fill="#f59e0b" font-size="8.5">패러데이</text>
  <text x="568" y="160" fill="#f59e0b" font-size="8.5">컵 (Dose)</text>
  <text x="555" y="240" fill="#34d399" font-size="10.5">Dose = ∫ I dt / (q·A)</text>
  <text x="555" y="265" fill="#94a3b8" font-size="9.5">전하량 적분으로 도즈량 정밀 계측</text>
</svg>""",
        "lecture": r"""<h3>1. 질량 분석 자석의 로렌츠 편향 원리</h3>
<p>이온원에서는 목표 이온 외에도 동위원소나 불소 등 수많은 불순물이 함께 추출됩니다. 자기장($B$) 내부에서 하전 입자가 받는 원심력과 로렌츠 힘의 평형식은 다음과 같습니다:</p>
<div class="formula-box">$$q v B = \frac{m v^2}{r} \implies r = \frac{1}{B} \sqrt{\frac{2 m V_{ext}}{q}}$$</div>
<p>곡률 반경 $r$이 질량 대 전하비($m/q$)의 제곱근에 비례하므로, 자석의 슬릿 위치를 정확히 맞추면 원하는 도펀트 이온만 90도로 꺾여 통과하고 나머지는 벽면에 충돌하여 완벽히 걸러집니다.</p>"""
    },

    # 11. 이온주입 2) Doping Profile의 중요성
    {
        "id": "q-11",
        "num": "11",
        "badge": "⭐ 최신 질문 (이온주입 2/4)",
        "title": "이온주입 2) Doping Profile의 중요성 (투영 사정거리 Rp, 피어슨 분포)",
        "summary": [
            "주입된 이온의 최종 정지 위치는 '원자핵 충돌(Nuclear Stopping: 저에너지, 산란 유발)'과 '전자 구름 마찰(Electronic Stopping: 고에너지, 저항)'의 총 에너지 손실에 의해 결정됩니다.",
            "이온의 깊이별 농도 분포는 <strong>가우시안(Gaussian) 분포</strong>를 따르며, 피크 농도가 나타나는 평균 깊이를 <strong>투영 사정거리(Rp)</strong>, 분포의 폭을 <strong>표준편차(ΔRp, Straggle)</strong>라 합니다.",
            "실제 격자 내부에서는 채널링 효과와 다중 충돌로 인해 깊은 쪽 꼬리가 길어지는 비대칭성이 발생하므로, 왜도(Skewness)와 첨도(Kurtosis)를 반영한 <strong>피어슨(Pearson-IV) 모델</strong>로 정밀 프로파일을 예측합니다."
        ],
        "svg_title": "📊 [이온주입 도핑 프로파일] 가우시안 수식 분포, 사정거리 Rp, 표준편차 ΔRp & 접합깊이",
        "svg": """<svg viewBox="0 0 780 340" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="340" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <line x1="80" y1="270" x2="720" y2="270" stroke="#64748b" stroke-width="1.5"/>
  <line x1="80" y1="50" x2="80" y2="270" stroke="#64748b" stroke-width="1.5"/>
  <text x="660" y="295" fill="#94a3b8" font-size="11">깊이 x (Depth)</text>
  <text x="30" y="60" fill="#94a3b8" font-size="11">농도 C(x)</text>
  <line x1="80" y1="230" x2="720" y2="230" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4"/>
  <text x="620" y="222" fill="#ef4444" font-size="10.5" font-weight="700">기판 배경 농도 (NB)</text>
  <path d="M 80 260 Q 200 250 280 80 Q 360 250 560 260" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="2.5"/>
  <line x1="280" y1="80" x2="280" y2="270" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2,2"/>
  <text x="260" y="295" fill="#f59e0b" font-size="12" font-weight="800">Rp (투영 사정거리)</text>
  <text x="240" y="70" fill="#38bdf8" font-size="11" font-weight="800">피크 농도 (Cp)</text>
  <line x1="220" y1="150" x2="340" y2="150" stroke="#10b981" stroke-width="2"/>
  <text x="240" y="142" fill="#10b981" font-size="11" font-weight="700">폭 2·ΔRp (Straggle)</text>
  <circle cx="430" cy="230" r="5" fill="#ef4444"/>
  <line x1="430" y1="230" x2="430" y2="270" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2,2"/>
  <text x="410" y="295" fill="#ef4444" font-size="12" font-weight="800">Xj (접합 깊이)</text>
  <text x="440" y="225" fill="#cbd5e1" font-size="10">C(Xj) = NB 교차점</text>
</svg>""",
        "lecture": r"""<h3>1. 가우시안 도핑 프로파일 수식 유도</h3>
<div class="formula-box">$$C(x) = \frac{\Phi}{\sqrt{2\pi}\Delta R_p} \exp\left( - \frac{(x - R_p)^2}{2 \Delta R_p^2} \right)$$</div>
<ul>
  <li>$\Phi$ (Dose): 주입된 총 이온량 ($/\text{cm}^2$).</li>
  <li>$R_p$ (Projected Range): 평균 투영 사정거리. 주입 에너지($E$)에 비례하여 깊어집니다.</li>
  <li>$\Delta R_p$ (Straggle): 충돌 산란에 의한 표준편차.</li>
  <li>접합 깊이($X_j$): 주입된 불순물 농도와 기판의 본래 배경 농도($N_B$)가 같아져 전기적 p-n 접합을 이루는 깊이 ($C(X_j) = N_B$).</li>
</ul>"""
    },

    # 12. 이온주입 3) Shallow Implantation
    {
        "id": "q-12",
        "num": "12",
        "badge": "⭐ 최신 질문 (이온주입 3/4)",
        "title": "이온주입 3) Shallow Implantation (초얕은 접합 USJ, 채널링 억제, RTA)",
        "summary": [
            "단채널 효과(DIBL, Punchthrough)를 차단하기 위해 소스/드레인 연장 영역(LDD)의 접합 깊이를 10nm 이하로 극소화하는 공정을 <strong>초얕은 접합(USJ: Ultra-Shallow Junction)</strong>이라 합니다.",
            "<strong>채널링(Channeling) 현상</strong>은 단결정 실리콘의 원자 기둥 사이 빈 공간(격자 터널)으로 이온이 충돌 없이 비정상적으로 깊게 관통하는 현상입니다.",
            "채널링을 막기 위해 웨이퍼를 7° 기울여 쏘는 <strong>틸트(Tilt/Twist)</strong> 공정이나, 무거운 Ge/Si 이온을 먼저 때려 표면을 비정질화하는 <strong>PAI (Pre-Amorphization Implantation)</strong> 기술이 필수적으로 적용됩니다."
        ],
        "svg_title": "📊 [채널링 억제 메커니즘] 단결정 격자 채널링 vs PAI 비정질화 차단 비교",
        "svg": """<svg viewBox="0 0 780 330" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="330" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="25" y="30" width="350" height="280" rx="8" fill="#0f172a" stroke="#f87171" stroke-width="1.2"/>
  <text x="40" y="55" fill="#f87171" font-size="12" font-weight="800">1. 채널링 현상 (Channeling ➔ 깊은 침투 실패)</text>
  <circle cx="80" cy="100" r="8" fill="#64748b"/><circle cx="160" cy="100" r="8" fill="#64748b"/><circle cx="240" cy="100" r="8" fill="#64748b"/>
  <circle cx="80" cy="160" r="8" fill="#64748b"/><circle cx="160" cy="160" r="8" fill="#64748b"/><circle cx="240" cy="160" r="8" fill="#64748b"/>
  <circle cx="80" cy="220" r="8" fill="#64748b"/><circle cx="160" cy="220" r="8" fill="#64748b"/><circle cx="240" cy="220" r="8" fill="#64748b"/>
  <line x1="120" y1="70" x2="120" y2="250" stroke="#ef4444" stroke-width="2.5"/>
  <polygon points="116,245 120,257 124,245" fill="#ef4444"/>
  <text x="135" y="190" fill="#f87171" font-size="10.5" font-weight="700">격자 터널 관통!</text>
  <text x="40" y="285" fill="#cbd5e1" font-size="10.5">원자와 충돌하지 않고 깊숙이 들어가 USJ 붕괴</text>

  <rect x="405" y="30" width="350" height="280" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.2"/>
  <text x="420" y="55" fill="#34d399" font-size="12" font-weight="800">2. 해결책: PAI (비정질화 선행 주입) + USJ</text>
  <rect x="420" y="80" width="320" height="80" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-dasharray="2,2"/>
  <text x="440" y="105" fill="#38bdf8" font-size="11" font-weight="700">Ge/Si 사전 주입 ➔ 표면 비정질화(Amorphous)</text>
  <path d="M 520 70 L 530 110 L 515 130 L 540 145" fill="none" stroke="#f59e0b" stroke-width="2.5"/>
  <circle cx="540" cy="145" r="4" fill="#f59e0b"/>
  <text x="555" y="135" fill="#f59e0b" font-size="10.5" font-weight="700">무작위 충돌 정지</text>
  <line x1="420" y1="160" x2="740" y2="160" stroke="#10b981" stroke-width="2"/>
  <text x="430" y="185" fill="#10b981" font-size="11" font-weight="700">USJ 초얕은 접합 완성 (Xj < 10nm 사수!)</text>
  <text x="420" y="285" fill="#cbd5e1" font-size="10.5">이후 레이저 어닐링(LSA)으로 결정 격자만 복구!</text>
</svg>""",
        "lecture": r"""<h3>1. 붕소(Boron)의 채널링 취약성과 PAI 공정</h3>
<p>p형 도펀트인 붕소($^{11}\text{B}$)는 원자 질량이 매우 작아 충돌 단면적이 좁기 때문에 단결정 격자의 터널을 따라 쉽게 깊은 곳까지 침투합니다. 이를 해결하기 위해 무거운 게르마늄이나 실리콘 이온을 먼저 주입하여 단결정 격자를 깨부수어 표면을 비정질 상태로 바꿉니다. 그 후 붕소를 주입하면 무작위 핵 충돌에 의해 10nm 이하의 극도로 얕은 깊이에서 모두 정지하게 됩니다.</p>"""
    },

    # 13. 이온주입 4) Dose 와 Doping 농도의 차이 및 측정법
    {
        "id": "q-13",
        "num": "13",
        "badge": "⭐ 최신 질문 (이온주입 4/4)",
        "title": "이온주입 4) Dose 와 Doping 농도의 차이 및 측정법 (Dose vs Conc, SIMS)",
        "summary": [
            "<strong>도즈량(Dose, Φ)</strong>은 단위 '면적'당 주입된 총 이온 수($[\\text{cm}^{-2}]$)이며, <strong>도핑 농도(Concentration, C)</strong>는 단위 '부피'당 존재하는 불순물 원자 밀도($[\\text{cm}^{-3}]$)입니다.",
            "도즈량은 주입 장비의 패러데이 컵(Faraday Cup)에 흐르는 빔 전류를 시간 적분하여 인시츄(In-situ)로 실시간 계측합니다.",
            "깊이별 실제 도핑 농도 프로파일 C(x)는 1차 이온 빔으로 표면을 나노 단위로 깎아내며 튀어나오는 2차 이온을 질량 분석하는 <strong>SIMS (이차이온질량분석기)</strong>를 통해 절대 계측합니다."
        ],
        "svg_title": "📊 [Dose vs Concentration 개념 & SIMS 원리] 면적 밀도와 3차원 부피 농도",
        "svg": """<svg viewBox="0 0 780 330" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="330" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="25" y="30" width="350" height="280" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="40" y="55" fill="#38bdf8" font-size="12" font-weight="800">1. Dose(면적) vs Doping 농도(부피)</text>
  <rect x="40" y="75" width="140" height="85" fill="#1e293b" stroke="#38bdf8"/>
  <text x="50" y="95" fill="#38bdf8" font-size="11" font-weight="700">도즈량 (Dose, Φ)</text>
  <text x="50" y="115" fill="#cbd5e1" font-size="10">단위: [ atoms / cm² ]</text>
  <text x="50" y="135" fill="#94a3b8" font-size="9.5">2차원 면적당 총 투입량</text>
  <rect x="200" y="75" width="160" height="85" fill="#1e293b" stroke="#f59e0b"/>
  <text x="210" y="95" fill="#f59e0b" font-size="11" font-weight="700">도핑 농도 (C(x))</text>
  <text x="210" y="115" fill="#cbd5e1" font-size="10">단위: [ atoms / cm³ ]</text>
  <text x="210" y="135" fill="#94a3b8" font-size="9.5">3차원 공간 부피당 밀도</text>
  <rect x="40" y="180" width="320" height="110" rx="6" fill="#1e293b"/>
  <text x="50" y="205" fill="#10b981" font-size="11" font-weight="700">수학적 적분 관계</text>
  <text x="50" y="230" fill="#f1f5f9" font-size="11">Φ = ∫₀^∞ C(x) dx</text>
  <text x="50" y="255" fill="#cbd5e1" font-size="10">• 농도 곡선 C(x) 아래 면적을 전부 적분하면 Dose!</text>

  <rect x="405" y="30" width="350" height="280" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="420" y="55" fill="#38bdf8" font-size="12" font-weight="800">2. SIMS (Secondary Ion Mass Spectrometry)</text>
  <text x="420" y="80" fill="#cbd5e1" font-size="10.5">깊이별 불순물 절대 농도 측정 표준 장비</text>
  <line x1="450" y1="100" x2="520" y2="160" stroke="#f59e0b" stroke-width="2.5"/>
  <text x="430" y="115" fill="#f59e0b" font-size="10">1차 이온 빔 (Cs+, O₂+)</text>
  <rect x="480" y="160" width="220" height="50" fill="#334155"/>
  <text x="550" y="190" fill="#ffffff" font-size="10">웨이퍼 표면 스퍼터링</text>
  <line x1="530" y1="160" x2="620" y2="110" stroke="#38bdf8" stroke-width="2" stroke-dasharray="2,2"/>
  <text x="610" y="105" fill="#38bdf8" font-size="10">튀어나온 2차 이온 ➔</text>
  <rect x="630" y="115" width="110" height="50" fill="#1e293b" stroke="#38bdf8"/>
  <text x="640" y="135" fill="#38bdf8" font-size="9.5">질량 분석기 검출</text>
  <text x="640" y="152" fill="#cbd5e1" font-size="8.5">농도 C(x) 프로파일 완성</text>
  <text x="420" y="250" fill="#34d399" font-size="10.5">※ 감도: 10¹⁴ atoms/cm³ (ppm~ppb 단위 검출 가능)</text>
</svg>""",
        "lecture": r"""<h3>1. 단위 차이와 면적 적분의 물리적 의미</h3>
<p>Dose는 단위 면적에 몇 개의 이온이 투하되었는지를 나타내는 양($\text{cm}^{-2}$)이고, 실리콘 내부로 파고들며 퍼져 형성되는 실제 입체 밀도가 Concentration($\text{cm}^{-3}$)입니다. 따라서 깊이 $x$에 따른 농도 $C(x)$를 0부터 무한대까지 적분하면 총 도즈량 $\Phi$가 됩니다.</p>
<h3>2. 전기적 측정(SRP)과 물리적 측정(SIMS)의 차이</h3>
<ul>
  <li><strong>SIMS</strong>: 이온화 여부(활성화)와 무관하게 격자 틈새에 박혀있는 원자까지 포함한 '물리적 총 원자 수'를 측정합니다.</li>
  <li><strong>SRP / 홀 효과 측정</strong>: 열처리를 통해 실리콘 격자 자리를 치환하여 자유 전자나 정공을 내놓는 '전기적으로 활성화된 캐리어 농도'만을 측정합니다.</li>
</ul>"""
    },

    # 14. 금속 1) Al, Cu, W 의 차이점
    {
        "id": "q-14",
        "num": "14",
        "badge": "⭐ 최신 질문 (금속 1/3)",
        "title": "금속 1) Al, Cu, W 배선의 특성과 차이점 (비저항, 다마신, 플러그)",
        "summary": [
            "<strong>알루미늄(Al)</strong>은 식각이 쉬워 과거 주력 배선이었으나 비저항($2.7\,\mu\Omega\cdot\text{cm}$)이 높고 일렉트로마이그레이션(EM)에 취약하여 도태되었습니다.",
            "<strong>구리(Cu)</strong>는 초저비저항($1.7\,\mu\Omega\cdot\text{cm}$)과 뛰어난 EM 내성으로 현대 고속 다층 배선(Interconnect)의 표준이지만, 건식 식각이 불가능하여 <strong>다마신(Damascene) 공정</strong>이 필수입니다.",
            "<strong>텅스텐(W)</strong>은 비저항($5.6\,\mu\Omega\cdot\text{cm}$)은 높지만 고온 내구성과 CVD 단차 도포성이 완벽하여 트랜지스터 단자와 제1금속 배선을 연결하는 수직 <strong>콘택트 플러그(Contact Plug)</strong>를 전담합니다."
        ],
        "svg_title": "📊 [반도체 3대 금속 배치도] 트랜지스터 상부 텅스텐 플러그 & 구리 다마신 배선 구조",
        "svg": """<svg viewBox="0 0 780 340" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="340" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="30" y="30" width="370" height="280" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="45" y="55" fill="#38bdf8" font-size="12" font-weight="800">BEOL 금속 배선 단면 배치도</text>
  <rect x="80" y="70" width="260" height="35" fill="#d97706" stroke="#b45309" stroke-width="1.5"/>
  <text x="140" y="92" fill="#ffffff" font-size="11" font-weight="800">Metal 2 : 구리 (Cu 다마신 배선)</text>
  <rect x="180" y="105" width="50" height="35" fill="#d97706"/>
  <text x="188" y="127" fill="#ffffff" font-size="10">Cu Via</text>
  <rect x="80" y="140" width="260" height="35" fill="#d97706" stroke="#b45309" stroke-width="1.5"/>
  <text x="140" y="162" fill="#ffffff" font-size="11" font-weight="800">Metal 1 : 구리 (Cu 다마신 배선)</text>
  <rect x="120" y="175" width="35" height="55" fill="#94a3b8" stroke="#475569"/>
  <rect x="260" y="175" width="35" height="55" fill="#94a3b8" stroke="#475569"/>
  <text x="95" y="205" fill="#38bdf8" font-size="10" font-weight="700">W 플러그</text>
  <text x="240" y="205" fill="#38bdf8" font-size="10" font-weight="700">W 플러그</text>
  <rect x="60" y="230" width="300" height="50" fill="#1e293b"/>
  <rect x="175" y="230" width="60" height="20" fill="#f59e0b"/>
  <text x="185" y="244" fill="#0f172a" font-size="10" font-weight="800">Gate</text>
  <text x="80" y="260" fill="#34d399" font-size="9.5">Source (NiSi)</text>
  <text x="270" y="260" fill="#34d399" font-size="9.5">Drain (NiSi)</text>

  <rect x="420" y="30" width="335" height="280" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="435" y="55" fill="#38bdf8" font-size="12" font-weight="800">3대 금속 물성 및 적용처 비교</text>
  <rect x="435" y="70" width="305" height="65" rx="4" fill="#1e293b"/>
  <text x="445" y="90" fill="#f87171" font-size="11" font-weight="700">Al (알루미늄) : 2.7 μΩ·cm</text>
  <text x="445" y="108" fill="#cbd5e1" font-size="10">• 식각 가능하나 RC 지연 심각 및 EM 취약</text>
  <text x="445" y="124" fill="#94a3b8" font-size="9.5">• 최상부 패드(Pad) 전극에 제한적 사용</text>
  <rect x="435" y="145" width="305" height="65" rx="4" fill="#1e293b"/>
  <text x="445" y="165" fill="#f59e0b" font-size="11" font-weight="700">Cu (구리) : 1.7 μΩ·cm (최저 저항)</text>
  <text x="445" y="183" fill="#cbd5e1" font-size="10">• 식각 불가 ➔ 듀얼 다마신 공정 필수</text>
  <text x="445" y="199" fill="#34d399" font-size="9.5">• 중·상층 수평 신호 배선 100% 점유</text>
  <rect x="435" y="220" width="305" height="75" rx="4" fill="#1e293b"/>
  <text x="445" y="240" fill="#38bdf8" font-size="11" font-weight="700">W (텅스텐) : 5.6 μΩ·cm (고융점 3422℃)</text>
  <text x="445" y="258" fill="#cbd5e1" font-size="10">• WF₆ CVD 증착으로 수직 깊은 홀 100% 충진</text>
  <text x="445" y="274" fill="#38bdf8" font-size="9.5">• 소자 직상부 수직 콘택트 플러그 전담</text>
</svg>""",
        "lecture": r"""<h3>1. 구리(Cu) 다마신(Damascene) 공정의 필연성</h3>
<p>구리는 저항이 매우 낮아 신호 지연($RC$ 딜레이)을 줄이는 꿈의 배선이지만, 휘발성 반응 부산물을 만들지 않아 플라즈마로 식각할 수 없습니다. 따라서 절연막에 배선 트렌치를 먼저 파고, 구리 확산 방지막(Ta/TaN)을 깐 뒤 전기도금으로 구리를 가득 채우고, 튀어나온 여분을 CMP로 갈아내는 다마신 기술이 개발되었습니다.</p>
<h3>2. 텅스텐(W) 플러그의 역할</h3>
<p>트랜지스터 소스/드레인과 연결되는 수직 구멍은 종횡비가 매우 큽니다. 스퍼터링으로 구리를 넣으면 입구가 먼저 막혀 내부에 빈 공간(Void)이 생깁니다. 텅스텐은 CVD 기상 반응을 통해 바닥부터 균일하게 차올라 결함 없는 완벽한 수직 전도 기둥을 만듭니다.</p>"""
    },

    # 15. 금속 2) 일렉트로마이그레이션
    {
        "id": "q-15",
        "num": "15",
        "badge": "⭐ 최신 질문 (금속 2/3)",
        "title": "금속 2) 일렉트로마이그레이션 (Electromigration, Black's Eq, Void)",
        "summary": [
            "<strong>일렉트로마이그레이션(EM)</strong>은 미세 배선에 초고밀도 직류 전류가 흐를 때 고속 주행하는 전자들의 운동량(Electron Wind Force)에 의해 금속 원자가 밀려 이동하는 신뢰성 결함 현상입니다.",
            "원자가 쓸려나간 상류에는 빈 구멍인 <strong>보이드(Void: 단선 Open 유발)</strong>가 형성되고, 원자가 밀려 쌓인 하류에는 돌기인 <strong>힐록(Hillock: 인접 배선 쇼트 Short 유발)</strong>이 발생합니다.",
            "배선의 평균 고장 시간(MTTF)은 <strong>블랙의 공식</strong>을 따르며, 구리(Cu)는 알루미늄 대비 활성화 에너지가 높아 EM 수명이 100배 이상 우수합니다."
        ],
        "svg_title": "📊 [일렉트로마이그레이션 파괴 메커니즘] 전자 바람(Electron Wind), 보이드(단선) & 힐록(쇼트)",
        "svg": """<svg viewBox="0 0 780 330" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="330" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="30" y="30" width="720" height="150" rx="8" fill="#0f172a" stroke="#334155"/>
  <text x="45" y="55" fill="#38bdf8" font-size="12" font-weight="800">금속 원자 이동 & 보이드(Void) / 힐록(Hillock) 형성 모식도</text>
  <rect x="60" y="80" width="660" height="50" fill="#d97706" opacity="0.8"/>
  <line x1="80" y1="70" x2="680" y2="70" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="320" y="65" fill="#38bdf8" font-size="11" font-weight="800">전자 이동 방향 (Electron Wind ➔➔➔)</text>
  <ellipse cx="200" cy="105" rx="25" ry="20" fill="#0b1120" stroke="#ef4444" stroke-width="2"/>
  <text x="165" y="110" fill="#f87171" font-size="11" font-weight="800">보이드 (Void)</text>
  <text x="145" y="150" fill="#f87171" font-size="10">원자 유실 ➔ 저항 증가 및 단선(Open)</text>
  <polygon points="530,80 560,40 590,80" fill="#d97706" stroke="#fbbf24" stroke-width="2"/>
  <text x="535" y="32" fill="#fbbf24" font-size="11" font-weight="800">힐록 (Hillock)</text>
  <text x="510" y="150" fill="#fbbf24" font-size="10">원자 응집 돌기 ➔ 인접선 단락(Short)</text>

  <rect x="30" y="195" width="720" height="115" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
  <text x="45" y="220" fill="#38bdf8" font-size="13" font-weight="800">블랙의 공식 (Black's Equation)</text>
  <text x="45" y="248" fill="#f1f5f9" font-size="14" font-weight="700">MTTF = ( A / J^n ) · exp( Ea / kB·T )   (n ≈ 2)</text>
  <text x="45" y="272" fill="#cbd5e1" font-size="10.5">• 전류 밀도(J)가 2배 증가하면 수명(MTTF)은 1/4로 추락 (제곱 반비례!)</text>
  <text x="45" y="292" fill="#34d399" font-size="10.5">• 활성화 에너지(Ea): Al (0.5~0.7 eV) vs Cu (0.9~1.2 eV) ➔ Cu 도입으로 신뢰성 비약적 향상</text>
</svg>""",
        "lecture": r"""<h3>1. 전자 바람 힘(Electron Wind Force)의 물리</h3>
<p>금속 내부의 원자는 전계에 의한 정전기력과 주행하는 전도 전자들이 원자핵 격자와 충돌하며 전달하는 운동량인 전자 바람 힘($F_{wind}$)을 동시에 받습니다. 고밀도 전류 환경에서는 전자 충돌량이 정전기력보다 수백 배 압도적으로 커서 금속 이온들이 양극 쪽으로 물리적으로 표류(Drift)하게 됩니다.</p>
<h3>2. 배선 설계 가이드라인 (Design Rule)</h3>
<p>반도체 칩 설계 시 각 메탈 레이어마다 허용 가능한 최대 전류 밀도($J_{max}$) 한계치를 엄격히 지정합니다. 전원선처럼 항상 한 방향으로 대전류가 흐르는 배선은 폭을 넓히거나 복수 개의 비아(Multiple Via)를 병렬 배치하여 전류를 분산시킵니다.</p>"""
    },

    # 16. 금속 3) Metal-Silicon Junction
    {
        "id": "q-16",
        "num": "16",
        "badge": "⭐ 최신 질문 (금속 3/3)",
        "title": "금속 3) Metal-Silicon Junction (쇼트키 접합 vs 오믹 접합, 실리사이드)",
        "summary": [
            "금속과 실리콘이 접촉하면 일함수 차이로 인해 에너지 장벽($\Phi_B$)이 형성되며, 저농도 반도체와 접합 시 한 방향으로만 전류가 흐르는 정류성 <strong>쇼트키 접합(Schottky Junction)</strong>이 형성됩니다.",
            "트랜지스터 단자에 필수적인 <strong>오믹 접합(Ohmic Junction)</strong>은 접합부 실리콘을 고농도로 축퇴 도핑하여 공핍층 폭을 $1\sim 2\,\text{nm}$로 줄임으로써 전자가 장벽을 통과하는 <strong>양자 터널링(Field Emission)</strong>을 유도해 만듭니다.",
            "현대 공정은 금속과 실리콘 계면에 니켈(Ni)이나 코발트(Co)를 반응시켜 자가 정렬 규화물인 <strong>살리사이드(Salicide: NiSi)</strong>를 형성하여 접촉 저항을 극소화합니다."
        ],
        "svg_title": "📊 [Metal-Si 접합 에너지 밴드도] 쇼트키 정류 장벽 vs 초박막 터널링 오믹 콘택트",
        "svg": """<svg viewBox="0 0 780 340" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="340" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="25" y="30" width="350" height="280" rx="8" fill="#0f172a" stroke="#f87171" stroke-width="1.2"/>
  <text x="40" y="55" fill="#f87171" font-size="12" font-weight="800">1. 쇼트키 접합 (Schottky: 저농도 N-Si 접촉)</text>
  <text x="40" y="78" fill="#cbd5e1" font-size="10.5">• 두꺼운 공핍층 장벽 ➔ 전자의 이동 차단</text>
  <rect x="40" y="95" width="100" height="130" fill="#334155"/>
  <text x="65" y="160" fill="#38bdf8" font-size="12" font-weight="800">Metal (금속)</text>
  <path d="M 140 120 Q 180 120 280 180" fill="none" stroke="#ef4444" stroke-width="3"/>
  <text x="160" y="110" fill="#f87171" font-size="11" font-weight="700">쇼트키 장벽 (ΦB)</text>
  <line x1="140" y1="180" x2="330" y2="180" stroke="#64748b" stroke-dasharray="2,2"/>
  <text x="230" y="175" fill="#94a3b8" font-size="9.5">페르미 준위 Ef</text>
  <text x="40" y="250" fill="#f87171" font-size="11" font-weight="700">➔ 비선형 정류 특성 (다이오드 작동)</text>
  <text x="40" y="270" fill="#cbd5e1" font-size="10">단자 콘택트로는 절대 사용 불가!</text>

  <rect x="405" y="30" width="350" height="280" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.2"/>
  <text x="420" y="55" fill="#34d399" font-size="12" font-weight="800">2. 오믹 접합 (Ohmic: 초고농도 N+ Si 접촉)</text>
  <text x="420" y="78" fill="#cbd5e1" font-size="10.5">• 극도로 얇은 공핍층 ➔ 양자역학적 터널링</text>
  <rect x="420" y="95" width="100" height="130" fill="#334155"/>
  <text x="445" y="160" fill="#38bdf8" font-size="12" font-weight="800">Metal (NiSi)</text>
  <path d="M 520 120 Q 535 120 550 180 L 710 180" fill="none" stroke="#10b981" stroke-width="3"/>
  <line x1="490" y1="140" x2="560" y2="140" stroke="#38bdf8" stroke-width="2.5"/>
  <polygon points="555,136 565,140 555,144" fill="#38bdf8"/>
  <text x="568" y="145" fill="#38bdf8" font-size="10.5" font-weight="800">터널링 관통!</text>
  <text x="525" y="210" fill="#fbbf24" font-size="9.5">초박막 공핍폭 (Wdep < 2nm)</text>
  <text x="420" y="250" fill="#34d399" font-size="11" font-weight="700">➔ 완벽한 양방향 선형 저항 (I ∝ V)</text>
  <text x="420" y="270" fill="#cbd5e1" font-size="10">전압 강하 제로 ➔ 이상적 콘택트 전극 달성</text>
</svg>""",
        "lecture": r"""<h3>1. 오믹 콘택트의 3가지 전도 기구</h3>
<ul>
  <li><strong>열전자 방출 (Thermionic Emission)</strong>: 저농도 도핑 시 열에너지를 얻은 소수 전자만 장벽을 넘어감 (쇼트키 정류 거동).</li>
  <li><strong>열-전계 방출 (Thermionic Field Emission)</strong>: 중농도 도핑 시 장벽 중간 높이에서 터널링 발생.</li>
  <li><strong>전계 방출 (Field Emission / Tunneling)</strong>: 도핑 농도가 $10^{20}\,\text{cm}^{-3}$ 이상이면 공핍층 두께가 전자 파동함수 크기 수준($< 2\,\text{nm}$)으로 얇아져 전자가 장벽을 무저항으로 뚫고 지나가는 순수 양자 터널링이 일어나 이상적인 선형 오믹 접합이 완성됩니다.</li>
</ul>"""
    },

    # 17. 패키징 1) HBM
    {
        "id": "q-17",
        "num": "17",
        "badge": "⭐ 최신 질문 (패키징 1/4)",
        "title": "패키징 1) HBM, HBM, HBM... (TSV, 2.5D 실리콘 인터포저)",
        "summary": [
            "<strong>HBM(고대역폭 메모리)</strong>은 초거대 AI 모델의 메모리 월(Memory Wall) 병목을 깨기 위해 여러 개의 DRAM 다이를 수직 적층하고 수천 개의 <strong>TSV(실리콘 관통 전극)</strong>로 뚫어 병렬 연결한 초고속 메모리입니다.",
            "기존 PCB 기판으로는 감당할 수 없는 초미세 배선을 연결하기 위해 GPU와 HBM을 <strong>2.5D 실리콘 인터포저(Silicon Interposer)</strong> 위에 올려 마이크로 범프로 결합합니다.",
            "HBM3E/HBM4로 진화하며 12단/16단 적층과 1024-bit를 넘어 2048-bit 인터페이스로 확장 중이며, 단일 패키지에서 초당 1.5~2.0 TB 이상의 경이로운 데이터 대역폭을 뿜어냅니다."
        ],
        "svg_title": "📊 [2.5D HBM 첨단 패키징 구조] GPU + 실리콘 인터포저 + 수직 적층 DRAM & TSV",
        "svg": """<svg viewBox="0 0 780 340" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="340" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="50" y="70" width="220" height="60" rx="4" fill="#10b981" stroke="#059669" stroke-width="2"/>
  <text x="110" y="105" fill="#ffffff" font-size="14" font-weight="900">AI GPU / SoC</text>
  <rect x="350" y="40" width="240" height="22" rx="2" fill="#38bdf8"/>
  <text x="430" y="56" fill="#0f172a" font-size="10" font-weight="800">DRAM Die 4 (Top)</text>
  <rect x="350" y="65" width="240" height="22" rx="2" fill="#38bdf8"/>
  <text x="430" y="81" fill="#0f172a" font-size="10" font-weight="800">DRAM Die 3</text>
  <rect x="350" y="90" width="240" height="22" rx="2" fill="#38bdf8"/>
  <text x="430" y="106" fill="#0f172a" font-size="10" font-weight="800">DRAM Die 2</text>
  <rect x="350" y="115" width="240" height="22" rx="2" fill="#0284c7"/>
  <text x="420" y="131" fill="#ffffff" font-size="10" font-weight="800">Base Logic Die (Buffer)</text>
  <line x1="390" y1="40" x2="390" y2="137" stroke="#f59e0b" stroke-width="3"/>
  <line x1="470" y1="40" x2="470" y2="137" stroke="#f59e0b" stroke-width="3"/>
  <line x1="550" y1="40" x2="550" y2="137" stroke="#f59e0b" stroke-width="3"/>
  <text x="600" y="90" fill="#f59e0b" font-size="11" font-weight="700">TSV 관통전극</text>
  <circle cx="80" cy="140" r="3" fill="#cbd5e1"/><circle cx="120" cy="140" r="3" fill="#cbd5e1"/>
  <circle cx="160" cy="140" r="3" fill="#cbd5e1"/><circle cx="200" cy="140" r="3" fill="#cbd5e1"/>
  <circle cx="390" cy="145" r="3" fill="#cbd5e1"/><circle cx="470" cy="145" r="3" fill="#cbd5e1"/>
  <text x="240" y="145" fill="#cbd5e1" font-size="9.5">마이크로 범프</text>
  <rect x="30" y="150" width="720" height="30" rx="3" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="40" y="170" fill="#38bdf8" font-size="11" font-weight="800">2.5D 실리콘 인터포저 (초미세 배선 1024-bit 초고속 데이터 고속도로)</text>
  <rect x="30" y="210" width="720" height="40" rx="4" fill="#0f172a" stroke="#64748b"/>
  <text x="320" y="235" fill="#94a3b8" font-size="12" font-weight="700">패키지 기판 (PCB Substrate)</text>
  <circle cx="100" cy="270" r="10" fill="#64748b"/><circle cx="220" cy="270" r="10" fill="#64748b"/>
  <circle cx="340" cy="270" r="10" fill="#64748b"/><circle cx="460" cy="270" r="10" fill="#64748b"/>
  <circle cx="580" cy="270" r="10" fill="#64748b"/><circle cx="680" cy="270" r="10" fill="#64748b"/>
  <text x="310" y="305" fill="#cbd5e1" font-size="11">BGA 솔더 볼 (메인보드 연결)</text>
</svg>""",
        "lecture": r"""<h3>1. 폰 노이만 병목과 메모리 월(Memory Wall)</h3>
<p>아무리 GPU의 연산 코어가 빨라도, 기존 GDDR 메모리는 인쇄회로기판(PCB)의 배선 핀 수 한계로 인해 데이터가 전송되는 병목이 심각했습니다. HBM은 칩 두께를 $30\sim 50\,\mu\text{m}$로 얇게 갈아내고 구멍을 뚫은 뒤 수천 가닥의 TSV로 1024-bit 이상의 버스를 직결하여 데이터 전송 폭을 수십 배로 넓혔습니다.</p>
<h3>2. 베이스 로직 다이(Base Die)의 핵심 기능</h3>
<p>HBM 스택의 가장 하단에는 단순 메모리가 아닌 연산 및 테스트 제어 로직을 담당하는 베이스 다이가 위치합니다. 각 적층 DRAM 셀의 불량 비트를 검사하여 여분의 셀로 대체하는 리페어(Repair) 기능과 인터포저 통신 인터페이스를 총괄합니다.</p>"""
    },

    # 18. 패키징 2) 패키징 열 전달
    {
        "id": "q-18",
        "num": "18",
        "badge": "⭐ 최신 질문 (패키징 2/4)",
        "title": "패키징 2) 패키징 열 전달 (Thermal Dissipation, TIM, 핫스팟 제어)",
        "summary": [
            "HBM 적층 및 고성능 AI 반도체는 손톱만 한 면적에서 700W 이상의 막대한 전력을 소모하므로, 열을 밖으로 빠르게 배출하지 못하면 칩 온도가 100℃를 넘어 열폭주(Thermal Throttling)가 발생합니다.",
            "<strong>TIM (Thermal Interface Material: 열 계면 소재)</strong>은 칩 표면과 금속 방열판(Lid) 사이의 미세 공기 틈새를 채워 열 저항을 극소화하는 핵심 소재입니다.",
            "HBM 내부 칩 사이를 채우는 <strong>MR-MUF(Molded Underfill)</strong>는 에폭시 몰딩 컴파운드에 실리카 열전도 필러를 고밀도로 분산시켜 기존 NCF(필름 접착) 대비 열 방출 능력을 2.5배 개선했습니다."
        ],
        "svg_title": "📊 [패키징 열 전달 저항 모델] 칩 ➔ TIM ➔ 히트스프레더 ➔ 방열판 열 경로",
        "svg": """<svg viewBox="0 0 780 330" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="330" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="40" y="30" width="700" height="40" rx="4" fill="#475569" stroke="#94a3b8"/>
  <text x="250" y="55" fill="#ffffff" font-size="13" font-weight="800">금속 방열판 / 히트스프레더 (Cu / Vapor Chamber)</text>
  <rect x="60" y="70" width="660" height="18" fill="#f59e0b" opacity="0.9"/>
  <text x="260" y="84" fill="#0f172a" font-size="11" font-weight="900">TIM 1 (열전도율 높은 페이스트 / 인듐 액체금속)</text>
  <line x1="200" y1="180" x2="200" y2="90" stroke="#ef4444" stroke-width="3"/>
  <polygon points="196,95 200,85 204,95" fill="#ef4444"/>
  <line x1="500" y1="180" x2="500" y2="90" stroke="#ef4444" stroke-width="3"/>
  <polygon points="496,95 500,85 504,95" fill="#ef4444"/>
  <text x="300" y="130" fill="#ef4444" font-size="12" font-weight="800">상부 수직 방열 경로 (Heat Flow ⬆⬆⬆)</text>
  <rect x="100" y="150" width="220" height="45" rx="3" fill="#10b981"/>
  <text x="160" y="177" fill="#ffffff" font-size="12" font-weight="800">GPU 다이 (Hotspot)</text>
  <rect x="400" y="150" width="220" height="45" rx="3" fill="#38bdf8"/>
  <text x="440" y="177" fill="#0f172a" font-size="12" font-weight="800">HBM 3D 적층 다이</text>
  <rect x="40" y="215" width="700" height="95" rx="6" fill="#0f172a" stroke="#334155"/>
  <text x="55" y="238" fill="#38bdf8" font-size="12" font-weight="800">열 저항 공식 : θ_JA = ( Tj - Ta ) / Power</text>
  <text x="55" y="260" fill="#cbd5e1" font-size="11">• 접합 온도(Tj)를 85~105℃ 이하로 유지하기 위해 전체 열 저항(θ)을 극소화해야 함</text>
  <text x="55" y="280" fill="#34d399" font-size="11">• HBM 적층 갭 충진재: NCF(필름) ➔ MR-MUF(액상 에폭시+고밀도 필러) 전환으로 열전도율 2.5배 확보</text>
</svg>""",
        "lecture": r"""<h3>1. 푸리에 열전도 법칙과 열 계면 소재(TIM)의 역할</h3>
<p>열 유속 방정식은 $q = -k \nabla T$ 입니다. 금속 방열판과 실리콘 표면은 눈으로 보기에 매끄러워 보여도 미시적으로는 거친 요철이 있어 접촉 시 공기 층이 형성되어 엄청난 열 저항 벽을 만듭니다. 열전도율이 우수한 실리콘 젤/액체 금속 TIM을 채워 열을 수직으로 탈출시킵니다.</p>"""
    },

    # 19. 패키징 3) Warpage
    {
        "id": "q-19",
        "num": "19",
        "badge": "⭐ 최신 질문 (패키징 3/4)",
        "title": "패키징 3) Warpage (열팽창계수 CTE 불일치, 휨 현상, 박리 방지)",
        "summary": [
            "<strong>워피지(Warpage)</strong>는 고온 리플로우 공정(260℃)을 거쳐 상온으로 냉각될 때, 패키지를 구성하는 이종 재료 간의 <strong>열팽창계수(CTE) 불일치</strong>로 인해 패키지 기판이 오목(Smile)하거나 볼록(Frown)하게 휘어지는 현상입니다.",
            "실리콘 칩($\text{CTE} \approx 2.6\,\text{ppm/K}$)과 유기 PCB 기판($\text{CTE} \approx 15\,\text{ppm/K}$)의 극심한 팽창 차이가 주원인입니다.",
            "워피지가 발생하면 솔더 볼이 접촉하지 않는 <strong>오픈(Open)</strong>, 인접 볼끼리 들러붙는 <strong>쇼트(Short)</strong>, 칩 내부 층간이 뜯겨나가는 <strong>박리(Delamination)</strong>가 발생하므로 EMC 수지 물성 최적화와 스티프너(Stiffener) 링 장착으로 억제합니다."
        ],
        "svg_title": "📊 [Warpage 메커니즘 & 불량] CTE 차이에 따른 오목(Smile)/볼록(Frown) 휨과 솔더 불량",
        "svg": """<svg viewBox="0 0 780 330" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="330" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="25" y="30" width="350" height="280" rx="8" fill="#0f172a" stroke="#f87171" stroke-width="1.2"/>
  <text x="40" y="55" fill="#f87171" font-size="12" font-weight="800">1. 스마일 휨 (Smile Warpage: 기판 수축 우세)</text>
  <path d="M 60 120 Q 200 170 340 120" fill="none" stroke="#ef4444" stroke-width="6"/>
  <text x="140" y="115" fill="#ffffff" font-size="11" font-weight="700">실리콘 칩 (낮은 CTE)</text>
  <path d="M 60 140 Q 200 190 340 140" fill="none" stroke="#38bdf8" stroke-width="4"/>
  <text x="140" y="170" fill="#38bdf8" font-size="10">PCB 기판 (높은 CTE: 더 많이 수축)</text>
  <circle cx="70" cy="165" r="7" fill="#ef4444"/>
  <text x="85" y="170" fill="#f87171" font-size="10" font-weight="700">양 끝단 뜸 ➔ 오픈 (Open 단선)</text>
  <ellipse cx="200" cy="195" rx="14" ry="7" fill="#f59e0b"/>
  <text x="160" y="220" fill="#f59e0b" font-size="10" font-weight="700">중앙 눌림 ➔ 쇼트 (Bridge 단락)</text>
  <text x="40" y="275" fill="#cbd5e1" font-size="10.5">상온 냉각 시 바이메탈 현상으로 위로 말려 올라감</text>

  <rect x="405" y="30" width="350" height="280" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.2"/>
  <text x="420" y="55" fill="#34d399" font-size="12" font-weight="800">2. 워피지 제어 핵심 기술</text>
  <path d="M 440 150 Q 580 100 720 150" fill="none" stroke="#f59e0b" stroke-width="5"/>
  <text x="520" y="135" fill="#f59e0b" font-size="11" font-weight="700">볼록 휨 (Frown / Cry Warpage)</text>
  <rect x="420" y="175" width="320" height="115" rx="6" fill="#1e293b"/>
  <text x="435" y="198" fill="#34d399" font-size="11" font-weight="700">워피지 억제 3대 솔루션</text>
  <text x="435" y="220" fill="#cbd5e1" font-size="10">• 1. EMC 물성 매칭: 저수축성 및 실리콘과 유사한 CTE 튜닝</text>
  <text x="435" y="240" fill="#cbd5e1" font-size="10">• 2. 스티프너(Stiffener) 링: 기판 외곽에 금속 보강 프레임 부착</text>
  <text x="435" y="260" fill="#cbd5e1" font-size="10">• 3. 대칭적 적층(Balanced Stack-up): 위아래 배선층 수 대칭 설계</text>
</svg>""",
        "lecture": r"""<h3>1. 바이메탈 효과와 열팽창계수(CTE) 미스매치</h3>
<p>패키지를 구성하는 대표 재료들의 CTE는 다음과 같습니다: 실리콘 다이($2.6\,\text{ppm/K}$), 구리($17\,\text{ppm/K}$), 유기 PCB 기판($14\sim 17\,\text{ppm/K}$), 에폭시 몰딩 컴파운드(EMC: $8\sim 15\,\text{ppm/K}$). 솔더를 녹여 접합하는 260℃ 고온에서는 평평하게 붙어 있다가 상온으로 냉각되는 과정에서 수축률 차이로 인해 극심한 내부 응력과 휨이 발생합니다.</p>"""
    },

    # 20. 패키징 4) 하이브리드 본딩
    {
        "id": "q-20",
        "num": "20",
        "badge": "⭐ 최신 질문 (패키징 4/4)",
        "title": "패키징 4) 하이브리드 본딩 (Hybrid Bonding, Cu-Cu 직접 접합, 범프리스)",
        "summary": [
            "<strong>하이브리드 본딩(Hybrid Bonding / Direct Bond Interconnect)</strong>은 솔더 범프(Solder Bump)를 완전히 없애고, 절연체(SiO₂)와 금속(Cu) 패드를 한 평면으로 연마한 뒤 다이와 다이를 원자 단위로 직접 접합하는 차세대 3D 패키징 기술입니다.",
            "1단계로 상온에서 유전체 간의 분자 결합(Si-O-Si 친수성 본딩)을 형성하고, 2단계로 300~400℃ 열처리 시 열팽창 계수가 큰 구리(Cu)가 부풀어 오르며 <strong>Cu-Cu 고체 원자 확산(Atomic Diffusion)</strong>으로 금속 결합을 완성합니다.",
            "범프 공간이 사라져 연결 배선 피치를 <strong>1㎛ 이하</strong>로 극소화하고, 기생 저항과 커패시턴스를 90% 이상 절감하여 HBM4 및 3D 로직 적층의 최종 종착지로 도입되고 있습니다."
        ],
        "svg_title": "📊 [마이크로 범프 vs 하이브리드 본딩] 범프리스 Cu-Cu 원자 확산 접합 단면 비교",
        "svg": """<svg viewBox="0 0 780 340" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="340" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <rect x="25" y="30" width="350" height="280" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
  <text x="40" y="55" fill="#f59e0b" font-size="12" font-weight="800">1. 전통 마이크로 범프 (Micro-Bump)</text>
  <text x="40" y="78" fill="#cbd5e1" font-size="10.5">• 솔더 볼 높이 존재 (두께 수십 μm)</text>
  <text x="40" y="98" fill="#f87171" font-size="10.5">• 피치 축소 한계: 10μm 이하 시 쇼트 위험</text>
  <rect x="60" y="115" width="280" height="30" fill="#334155"/>
  <text x="170" y="135" fill="#ffffff" font-size="10">상부 칩</text>
  <circle cx="120" cy="165" r="14" fill="#64748b"/>
  <circle cx="200" cy="165" r="14" fill="#64748b"/>
  <circle cx="280" cy="165" r="14" fill="#64748b"/>
  <text x="140" y="170" fill="#f59e0b" font-size="10" font-weight="700">솔더 범프</text>
  <rect x="60" y="185" width="280" height="30" fill="#334155"/>
  <text x="170" y="205" fill="#ffffff" font-size="10">하부 칩</text>
  <text x="40" y="250" fill="#cbd5e1" font-size="10.5">• 큰 기생 인덕턴스 및 높은 열 저항</text>
  <text x="40" y="270" fill="#f87171" font-size="10.5">• HBM 16단 이상 적층 시 높이 규격 초과</text>

  <rect x="405" y="30" width="350" height="280" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.2"/>
  <text x="420" y="55" fill="#34d399" font-size="12" font-weight="800">2. 하이브리드 본딩 (Cu-Cu 직접 접합)</text>
  <text x="420" y="78" fill="#cbd5e1" font-size="10.5">• 범프 제로 (Bumpless)! 두께 0μm</text>
  <text x="420" y="98" fill="#38bdf8" font-size="10.5">• 서브마이크론 피치 (< 1μm) 구현 가능</text>
  <rect x="430" y="115" width="300" height="40" fill="#334155"/>
  <rect x="470" y="140" width="30" height="15" fill="#d97706"/>
  <rect x="560" y="140" width="30" height="15" fill="#d97706"/>
  <rect x="650" y="140" width="30" height="15" fill="#d97706"/>
  <line x1="430" y1="155" x2="730" y2="155" stroke="#34d399" stroke-width="2"/>
  <rect x="470" y="155" width="30" height="15" fill="#d97706"/>
  <rect x="560" y="155" width="30" height="15" fill="#d97706"/>
  <rect x="650" y="155" width="30" height="15" fill="#d97706"/>
  <rect x="430" y="155" width="300" height="40" fill="#334155" opacity="0.8"/>
  <text x="480" y="180" fill="#34d399" font-size="10.5" font-weight="700">Cu-Cu 원자 확산 + SiO₂-SiO₂ 분자 결합</text>
  <text x="420" y="245" fill="#38bdf8" font-size="11" font-weight="800">• 접촉 저항 90% 급감, 신호 지연 0</text>
  <text x="420" y="265" fill="#38bdf8" font-size="11" font-weight="800">• 두께 축소로 HBM 16단/20단 무제한 적층 가능</text>
  <text x="420" y="285" fill="#34d399" font-size="10.5">※ AMD 3D V-Cache, TSMC SoIC 상용화 완료</text>
</svg>""",
        "lecture": r"""<h3>1. 2단계 본딩 시퀀스 (Dual Damascene & Anneal)</h3>
<ol>
  <li><strong>CMP 초정밀 평탄화</strong>: 유전체 표면과 구리 패드를 화학기계적 연마(CMP)로 표면 거칠기 $0.5\,\text{nm}$ 이하로 평탄화합니다.</li>
  <li><strong>상온 친수성 유전체 본딩</strong>: 플라즈마 활성화 후 상온에서 유전체 표면끼리 먼저 맞닿으면 실란 결합($\text{Si}-\text{O}-\text{Si}$)에 의해 결합이 형성됩니다.</li>
  <li><strong>고온 Cu 열팽창 및 원자 확산 결합</strong>: 300~350℃로 가열하면 구리의 열팽창계수가 산화막보다 훨씬 커서 오목했던 구리 패드가 팽창하여 서로 강력하게 밀착하고, 구리 원자가 계면을 넘어 상호 확산하여 완벽한 단일 금속 결정립을 형성합니다.</li>
</ol>"""
    }
]

def update_index_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. 신규 20개 nav-item 생성
    new_nav_items = []
    for item in TOPICS_20:
        nav_html = f'      <li class="nav-item"><a href="#{item["id"]}" class="nav-link"><span class="nav-num">{item["num"]}</span><span class="nav-text">{item["title"]}</span></a></li>'
        new_nav_items.append(nav_html)
    new_nav_block = "\n".join(new_nav_items) + "\n"

    def shift_nav(match):
        old_num = int(match.group(1))
        new_num = old_num + 20
        new_str = f"{new_num:02d}"
        text = match.group(3)
        return f'<li class="nav-item"><a href="#q-{new_str}" class="nav-link"><span class="nav-num">{new_str}</span><span class="nav-text">{text}</span></a></li>'

    nav_list_pattern = re.compile(r'(<ul class="nav-list" id="navList">)(.*?)(</ul>)', re.DOTALL)
    nav_match = nav_list_pattern.search(html)
    if not nav_match:
        print(f"Error: Could not find navList in {file_path}")
        return

    old_nav_content = nav_match.group(2)
    shifted_nav_content = re.sub(
        r'<li class="nav-item"><a href="#q-(\d\d)" class="nav-link"><span class="nav-num">(\d\d)</span><span class="nav-text">(.*?)</span></a></li>',
        shift_nav,
        old_nav_content
    )
    new_full_nav = nav_match.group(1) + "\n" + new_nav_block + shifted_nav_content + nav_match.group(3)
    html = html[:nav_match.start()] + new_full_nav + html[nav_match.end():]

    # 2. 본문 섹션 시프트 (34부터 1까지 거꾸로)
    for old_n in range(34, 0, -1):
        new_n = old_n + 20
        old_str = f"{old_n:02d}"
        new_str = f"{new_n:02d}"
        html = re.sub(
            rf'<section class="([^"]*?)" id="q-{old_str}">',
            rf'<section class="\1" id="q-{new_str}">',
            html
        )
        html = re.sub(
            rf'<span class="topic-badge">Q {old_str}</span>',
            rf'<span class="topic-badge">Q {new_str}</span>',
            html
        )

    # 3. 신규 20개 섹션 HTML 블록 생성
    new_sections = []
    for item in TOPICS_20:
        summary_lis = "\n".join([f"          <li>{s}</li>" for s in item["summary"]])
        sec_html = f"""
    <!-- Q {item['num']} : {item['title']} -->
    <section class="topic-section latest-card-highlight" id="{item['id']}">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q {item['num']}</span>
          <span class="latest-tag">{item['badge']}</span>
          <h2 class="topic-title">{item['title']}</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">면접 대비 3~4줄 핵심 요약</span>
        <ul class="summary-list">
{summary_lis}
        </ul>
      </div>
      <div class="lecture-content">
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            {item['svg_title']}
          </div>
          {item['svg']}
        </div>
        {item['lecture']}
      </div>
    </section>
"""
        new_sections.append(sec_html)

    new_sections_block = "\n".join(new_sections)

    main_header_end = html.find("</header>")
    if main_header_end != -1:
        insert_pos = main_header_end + len("</header>")
        html = html[:insert_pos] + "\n" + new_sections_block + html[insert_pos:]
        print(f"Successfully inserted 20 sections into {file_path}")
    else:
        print(f"Error: Could not find </header> in {file_path}")
        return

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    update_index_html(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_index_html(r"C:\Work\반도체3\index.html")
    print("Done updating both index.html files!")
