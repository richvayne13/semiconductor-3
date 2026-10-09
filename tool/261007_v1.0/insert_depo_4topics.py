# -*- coding: utf-8 -*-
"""
insert_depo_4topics.py
'6. 증착 - 기체 상태의 원자로부터 박막을 형성하는 공정'
1) APCVD, LPCVD, ALD, PECVD
2) Uniformity, Uniformity, Uniformity
3) 박막 두께는 어떻게 계측할까?
4) 열 예산

위 4대 주제를 신규 Q01~Q04로 최상단에 추가하고, 기존 55개 질문을 Q05~Q59로 시프트 (총 59개 질문 백과사전).
"""

import sys
import re

DEPO_TOPICS = [
    {
        "id": "q-01",
        "num": "01",
        "badge": "⭐ 최신 질문 (증착 공정 1/4)",
        "is_latest": True,
        "title": "증착 1) APCVD, LPCVD, ALD, PECVD (화학기상증착과 원자층증착의 원리 및 특성 비교)",
        "nav_title": "증착 1) APCVD, LPCVD, ALD, PECVD",
        "summary": [
            "<strong>CVD(Chemical Vapor Deposition)</strong>는 기체 상태 전구체(Precursor)를 챔버에 주입하여 웨이퍼 표면에서 화학 반응을 통해 고체 박막을 형성하는 공정이며, 에너지원(열/플라즈마)과 압력(대기압/저압)에 따라 특성이 나뉩니다.",
            "<strong>LPCVD(저압 CVD, 0.1~1 Torr)</strong>는 긴 평균자유행로(MFP)로 표면 반응 제어(Surface reaction limited) 영역에서 동작하여 우수한 단차 도포성(Step Coverage)과 고품질 박막을 형성하지만, 600~900℃의 고온이 필요합니다.",
            "<strong>PECVD(플라즈마 CVD, 1~5 Torr)</strong>는 RF 플라즈마의 전자가 반응 가스를 분해(라디칼 형성)하여 활성화 에너지를 제공하므로 200~400℃ 저온에서도 증착이 가능해, 알루미늄/구리 금속 배선 후공정(BEOL)의 층간 절연막(IMD) 형성에 필수적입니다.",
            "<strong>ALD(원자층 증착)</strong>는 전구체와 반응 가스를 교대로 주입하는 표면 자기포화 반응(Self-limiting reaction)을 통해 1사이클당 약 0.1nm 두께를 원자 단위로 정밀 제어하며, 100%에 가까운 완벽한 3D 단차 도포성을 제공합니다."
        ],
        "svg_title": "📊 [박막 증착 4대 핵심 기술 메커니즘] APCVD vs LPCVD vs PECVD vs ALD 비교",
        "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  
  <!-- Left: CVD 3 Types Comparison -->
  <rect x="20" y="25" width="365" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="50" fill="#38bdf8" font-size="12.5" font-weight="800">1. CVD 3대 기술 특성 비교 (에너지원 & 압력)</text>
  
  <rect x="35" y="65" width="335" height="75" rx="5" fill="#1e293b"/>
  <text x="45" y="85" fill="#f87171" font-size="11" font-weight="700">① APCVD (대기압, 760 Torr / 350~450℃)</text>
  <text x="45" y="103" fill="#cbd5e1" font-size="10">• 증착 속도 빠름, 설비 단순 / 기상 반응 파티클 多</text>
  <text x="45" y="120" fill="#94a3b8" font-size="9.5">➔ 단차 도포성 불량, 두께 균일도 낮음 (초기 후막용)</text>

  <rect x="35" y="150" width="335" height="85" rx="5" fill="#1e293b"/>
  <text x="45" y="170" fill="#f59e0b" font-size="11" font-weight="700">② LPCVD (저압, 0.1~1 Torr / 600~900℃)</text>
  <text x="45" y="188" fill="#cbd5e1" font-size="10">• 평균자유행로(MFP) 큼 ➔ 표면 반응 제한 영역</text>
  <text x="45" y="205" fill="#34d399" font-size="10">• 고밀도 치밀한 막질, 우수한 Step Coverage</text>
  <text x="45" y="222" fill="#fbbf24" font-size="9.5">➔ Poly-Si, Si₃N₄, HTO 절연막 표준 / 고온 단점</text>

  <rect x="35" y="245" width="335" height="85" rx="5" fill="#1e293b"/>
  <text x="45" y="265" fill="#38bdf8" font-size="11" font-weight="700">③ PECVD (저압, 1~5 Torr / 200~400℃ 저온!)</text>
  <text x="45" y="283" fill="#cbd5e1" font-size="10">• RF 플라즈마 전자가 가스 해리 ➔ 라디칼 반응</text>
  <text x="45" y="300" fill="#34d399" font-size="10">• 열 예산(Thermal Budget) 대폭 절감 가능</text>
  <text x="45" y="317" fill="#38bdf8" font-size="9.5">➔ BEOL 금속 배선 층간절연막(IMD) & 패시베이션</text>

  <!-- Right: ALD 4-Step Cycle -->
  <rect x="400" y="25" width="360" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
  <text x="415" y="50" fill="#10b981" font-size="12.5" font-weight="800">2. ALD 원자층 증착 4단계 사이클 (자기포화 반응)</text>

  <rect x="415" y="65" width="160" height="115" rx="4" fill="#1e293b"/>
  <text x="425" y="85" fill="#38bdf8" font-size="10.5" font-weight="700">[Step 1] 전구체 주입</text>
  <text x="425" y="103" fill="#cbd5e1" font-size="9.5">• Source 가스 공급</text>
  <text x="425" y="119" fill="#34d399" font-size="9.5">• 기판 표면 화학 흡착</text>
  <text x="425" y="135" fill="#fbbf24" font-size="9">• 자기제한(Self-Limiting)</text>
  <text x="425" y="150" fill="#cbd5e1" font-size="8.5">단원자층 흡착 후 반응 정지</text>

  <rect x="585" y="65" width="160" height="115" rx="4" fill="#1e293b"/>
  <text x="595" y="85" fill="#f59e0b" font-size="10.5" font-weight="700">[Step 2] 퍼지(Purge)</text>
  <text x="595" y="103" fill="#cbd5e1" font-size="9.5">• 불활성 가스(Ar, N₂)</text>
  <text x="595" y="119" fill="#cbd5e1" font-size="9.5">• 미반응 잉여 전구체</text>
  <text x="595" y="135" fill="#cbd5e1" font-size="9.5">• 물리흡착 분자 배출</text>
  <text x="595" y="150" fill="#94a3b8" font-size="8.5">기상 반응 원천 차단</text>

  <rect x="415" y="190" width="160" height="115" rx="4" fill="#1e293b"/>
  <text x="425" y="210" fill="#10b981" font-size="10.5" font-weight="700">[Step 3] 반응제 주입</text>
  <text x="425" y="228" fill="#cbd5e1" font-size="9.5">• Reactant 가스(H₂O, O₃)</text>
  <text x="425" y="244" fill="#34d399" font-size="9.5">• 표면 흡착 분자와 반응</text>
  <text x="425" y="260" fill="#10b981" font-size="9.5">• 1 Monolayer 형성</text>
  <text x="425" y="275" fill="#cbd5e1" font-size="8.5">원하는 고체 박막 생성</text>

  <rect x="585" y="190" width="160" height="115" rx="4" fill="#1e293b"/>
  <text x="595" y="210" fill="#a855f7" font-size="10.5" font-weight="700">[Step 4] 2차 퍼지</text>
  <text x="595" y="228" fill="#cbd5e1" font-size="9.5">• 반응 부산물(Byproduct)</text>
  <text x="595" y="244" fill="#cbd5e1" font-size="9.5">• 잔류 반응제 완전 배출</text>
  <text x="595" y="260" fill="#a855f7" font-size="9.5">• 1 Cycle = ~0.1 nm</text>
  <text x="595" y="275" fill="#cbd5e1" font-size="8.5">다음 사이클 준비 완료</text>

  <text x="415" y="325" fill="#34d399" font-size="10.5" font-weight="700">★ ALD 핵심: 100% Conformal Step Coverage & 디지털 두께 제어</text>
</svg>""",
        "lecture": r"""<h3>1. 화학기상증착(CVD)의 기본 원리와 2대 율속 단계</h3>
<p>CVD는 기체 상태의 반응 가스(전구체)를 주입하여 웨이퍼 표면에서의 화학 반응을 통해 고체 박막을 성장시키는 공정입니다. 반응 속도는 온도와 압력에 따라 다음 두 가지 영역으로 나뉩니다:</p>
<ul>
  <li><strong>질량 수송 제한 영역 (Mass Transport Limited, 고온 영역)</strong>: 반응 가스가 웨이퍼 표면으로 공급(확산)되는 속도가 표면 화학 반응 속도보다 느려 공급량이 전체 증착 속도를 결정합니다. 유량 제어가 필수적이며 단차 도포성이 불리합니다 (APCVD의 전형적 거동).</li>
  <li><strong>표면 반응 제한 영역 (Surface Reaction Limited, 저온/저압 영역)</strong>: 웨이퍼 표면에서의 화학 흡착 및 반응 속도가 가스 공급 속도보다 느려 반응 속도가 아레니우스 식($\text{Rate} \propto \exp(-E_a/kT)$)에 의해 온도의 지배를 받습니다. 가스 분자가 표면 전체에 균일하게 퍼진 뒤 천천히 반응하므로 단차 도포성(Step Coverage)이 월등히 우수합니다 (LPCVD의 거동).</li>
</ul>

<h3>2. 4대 증착 공정(APCVD, LPCVD, PECVD, ALD) 종합 비교</h3>
<div class="data-table-wrap">
  <table class="data-table">
    <thead>
      <tr>
        <th>공정 구분</th>
        <th>압력 영역</th>
        <th>공정 온도</th>
        <th>에너지원</th>
        <th>단차 도포성</th>
        <th>증착 속도</th>
        <th>주요 반도체 응용처</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>APCVD</strong></td>
        <td>대기압 (760 Torr)</td>
        <td>350 ~ 450℃</td>
        <td>열 에너지</td>
        <td>불량 (Poor)</td>
        <td>매우 빠름 (>100nm/min)</td>
        <td>초기 두꺼운 절연막, BPSG/PSG 후막</td>
      </tr>
      <tr>
        <td><strong>LPCVD</strong></td>
        <td>저압 (0.1 ~ 1 Torr)</td>
        <td>600 ~ 900℃</td>
        <td>열 에너지</td>
        <td>우수 (Good)</td>
        <td>보통 (5~20nm/min)</td>
        <td>Poly-Si 게이트, Si₃N₄ 하드마스크, HTO</td>
      </tr>
      <tr>
        <td><strong>PECVD</strong></td>
        <td>저압 (1 ~ 5 Torr)</td>
        <td>200 ~ 400℃</td>
        <td>RF 플라즈마 전자</td>
        <td>보통 (Moderate)</td>
        <td>빠름 (50~100nm/min)</td>
        <td>BEOL 금속 배선 층간절연막(IMD), SiN 패시베이션</td>
      </tr>
      <tr>
        <td><strong>ALD</strong></td>
        <td>저압 (0.1 ~ 10 Torr)</td>
        <td>150 ~ 350℃</td>
        <td>표면 화학 결합</td>
        <td>완벽 (100% Conformal)</td>
        <td>극히 느림 (~0.1nm/cycle)</td>
        <td>High-k 게이트 유전막, 3D NAND 채널홀, FinFET/GAA</td>
      </tr>
    </tbody>
  </table>
</div>

<h3>3. PECVD: 열 에너지를 플라즈마로 대체하여 '저온 증착'을 실현한 원리</h3>
<p>LPCVD의 고온(>600℃)은 이미 형성된 소스/드레인 접합과 금속 배선(Cu의 경우 400℃ 초과 시 열화)을 파괴합니다. PECVD는 <strong>RF(13.56MHz) 전력을 인가하여 가벼운 전자를 고에너지로 가속</strong>시킵니다. 이 전자가 반응 분자와 충돌하여 고온 없이도 반응성이 극히 높은 <strong>라디칼(Radical)</strong>을 생성합니다. 따라서 기판 온도는 200~400℃의 저온을 유지하면서도 화학 반응을 완벽하게 일으킬 수 있어 <strong>후공정(BEOL) 배선의 표준</strong>으로 자리 잡았습니다.</p>

<h3>4. ALD(원자층 증착): 원자 단위 제어와 자기제한 반응(Self-Limiting Reaction)</h3>
<p>ALD는 반응 기체를 동시에 챔버에 넣지 않고 4단계 사이클로 분리합니다:</p>
<ol>
  <li><strong>1단계 (전구체 주입)</strong>: 기판 표면의 활성 사이트와 화학 흡착(Chemisorption)합니다. 표면 사이트가 모두 채워지면 더 이상 반응하지 않는 <strong>자기포화 현상(Self-Limiting)</strong>이 일어나 단원자층만 정확히 남습니다.</li>
  <li><strong>2단계 (퍼지)</strong>: 미반응 잔류 가스를 비활성 기체(Ar/N₂)로 완전 배출합니다.</li>
  <li><strong>3단계 (반응제 주입)</strong>: 흡착된 전구체와 반응제를 결합시켜 1원자층의 고체 박막을 완성합니다.</li>
  <li><strong>4단계 (2차 퍼지)</strong>: 반응 부산물(Byproduct)을 배출합니다.</li>
</ol>
<p>이 4단계를 1사이클로 하여 사이클 수만큼 두께가 정비례하므로 <strong>수 $\text{\AA}$ 단위의 디지털 두께 제어</strong>와 <strong>종횡비 70:1 이상의 입체 구조에서도 100% 완벽한 Step Coverage</strong>를 보장합니다.</p>"""
    },
    {
        "id": "q-02",
        "num": "02",
        "badge": "⭐ 최신 질문 (증착 공정 2/4)",
        "is_latest": False,
        "title": "증착 2) Uniformity, Uniformity, Uniformity (균일도의 절대적 중요성과 3대 차원)",
        "nav_title": "증착 2) Uniformity, Uniformity, Uniformity",
        "summary": [
            "박막 두께가 수 나노미터(nm) 단위로 초미세화됨에 따라 0.1nm의 두께 편차만으로도 문턱전압($V_{th} \propto 1/C_{ox}$), 커패시턴스($C$), 배선 저항($R$)이 요동쳐 칩 동작 마진이 붕괴되므로 <strong>균일도(Uniformity)</strong>는 수율의 알파이자 오메가입니다.",
            "균일도는 <strong>① 웨이퍼 내 균일도(WIW, Within-Wafer)</strong>, <strong>② 웨이퍼 간/배치 간 균일도(WTW, Wafer-to-Wafer)</strong>, <strong>③ 미세 3차원 패턴의 단차 도포성(Step Coverage)</strong>이라는 3대 차원으로 철저하게 관리됩니다.",
            "수학적으로 균일도는 $\\text{Non-Uniformity} = \\frac{T_{max} - T_{min}}{2 \\times T_{mean}} \\times 100\\%$로 정의되며, 최선단 공정에서는 웨이퍼 전면에서 1% 미만의 극단적인 균일도를 목표로 합니다.",
            "고종횡비(Aspect Ratio > 70:1) 구조인 3D NAND 채널 홀과 DRAM 커패시터에서는 기착 확률(Sticking Coefficient)이 크면 패턴 입구가 먼저 막히는 핀치오프(Pinch-off)로 내부에 보이드(Void)가 생기므로 완벽한 Step Coverage 기술이 필수적입니다."
        ],
        "svg_title": "📊 [박막 균일도(Uniformity) 3대 차원 및 단차 도포성] WIW, WTW, Step Coverage & Void 방지",
        "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: WIW 300mm Wafer Uniformity -->
  <rect x="20" y="25" width="235" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="50" fill="#38bdf8" font-size="12" font-weight="800">1. WIW (웨이퍼 내 균일도)</text>
  <!-- Wafer circle -->
  <circle cx="137" cy="140" r="70" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <circle cx="137" cy="140" r="50" fill="#0f172a" stroke="#0284c7" stroke-width="1.5" stroke-dasharray="3,3"/>
  <circle cx="137" cy="140" r="25" fill="#0369a1" opacity="0.4"/>
  <text x="110" y="145" fill="#38bdf8" font-size="10" font-weight="700">Center: Tc</text>
  <text x="145" y="90" fill="#f87171" font-size="9.5" font-weight="700">Edge: Te</text>
  <rect x="30" y="225" width="215" height="105" rx="4" fill="#1e293b"/>
  <text x="40" y="245" fill="#fbbf24" font-size="10.5" font-weight="700">공식: Non-Uniformity (%)</text>
  <text x="40" y="265" fill="#34d399" font-size="11" font-weight="700">NU = (Tmax - Tmin) / (2×Tavg)</text>
  <text x="40" y="285" fill="#cbd5e1" font-size="9.5">• 300mm 전면 ±1% 이내 관리</text>
  <text x="40" y="302" fill="#cbd5e1" font-size="9.5">• 샤워헤드 & 에지 링 제어</text>
  <text x="40" y="318" fill="#94a3b8" font-size="9">• 온도/가스 유량 구역별 보정</text>

  <!-- Center: Step Coverage Definition -->
  <rect x="270" y="25" width="240" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
  <text x="285" y="50" fill="#f59e0b" font-size="12" font-weight="800">2. 3D 단차 도포성 (Step Coverage)</text>
  <!-- Trench Diagram -->
  <path d="M 290 80 L 335 80 L 335 180 L 445 180 L 445 80 L 490 80" fill="none" stroke="#64748b" stroke-width="3"/>
  <!-- Thin film conformal -->
  <path d="M 290 92 L 347 92 L 347 168 L 433 168 L 433 92 L 490 92" fill="none" stroke="#38bdf8" stroke-width="6"/>
  <text x="390" y="88" fill="#38bdf8" font-size="10" font-weight="700">Top: T_top</text>
  <text x="440" y="135" fill="#34d399" font-size="10" font-weight="700">Side: T_side</text>
  <text x="350" y="163" fill="#fbbf24" font-size="10" font-weight="700">Bottom: T_bot</text>
  <rect x="280" y="200" width="220" height="130" rx="4" fill="#1e293b"/>
  <text x="290" y="220" fill="#f59e0b" font-size="10.5" font-weight="700">단차 도포성 지표</text>
  <text x="290" y="238" fill="#34d399" font-size="10.5">• S/C = (T_bottom / T_top) × 100%</text>
  <text x="290" y="256" fill="#cbd5e1" font-size="9.5">• 측벽비 = T_side / T_top</text>
  <text x="290" y="275" fill="#f87171" font-size="9.5">• 입구 돌출(Overhang) ➔ 보이드 유발</text>
  <text x="290" y="293" fill="#cbd5e1" font-size="9.5">• 고종횡비(A/R > 70:1) 채널 홀에서</text>
  <text x="290" y="311" fill="#38bdf8" font-size="9.5">  ALD가 100% 달성하는 핵심 원천</text>

  <!-- Right: Defect vs Conformal comparison -->
  <rect x="525" y="25" width="235" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
  <text x="540" y="50" fill="#10b981" font-size="12" font-weight="800">3. 불량(Void) vs 완벽 증착</text>
  
  <rect x="535" y="65" width="215" height="125" rx="4" fill="#1e293b"/>
  <text x="545" y="83" fill="#f87171" font-size="10.5" font-weight="700">[Pinch-off 결함: PVD / APCVD]</text>
  <!-- Pinch off sketch -->
  <path d="M 550 95 L 580 95 L 580 145 L 630 145 L 630 95 L 660 95" fill="none" stroke="#64748b" stroke-width="2"/>
  <!-- Overhang touching -->
  <circle cx="583" cy="100" r="8" fill="#f87171" opacity="0.6"/>
  <circle cx="627" cy="100" r="8" fill="#f87171" opacity="0.6"/>
  <ellipse cx="605" cy="130" rx="14" ry="10" fill="#ef4444" opacity="0.4"/>
  <text x="590" y="133" fill="#ffffff" font-size="8.5" font-weight="800">Void 발생</text>
  <text x="545" y="165" fill="#cbd5e1" font-size="9">• 기착확률 큼 ➔ 입구 막힘</text>
  <text x="545" y="179" fill="#f87171" font-size="9">• 내부 구멍(Void/Seam) ➔ 신뢰성 파괴</text>

  <rect x="535" y="200" width="215" height="130" rx="4" fill="#1e293b"/>
  <text x="545" y="218" fill="#34d399" font-size="10.5" font-weight="700">[완벽 단차도포: ALD / LPCVD]</text>
  <text x="545" y="238" fill="#cbd5e1" font-size="9.5">• 자기포화 반응으로 입구 과증착 차단</text>
  <text x="545" y="255" fill="#34d399" font-size="9.5">• 바닥/측벽 두께 동일 (S/C ≈ 100%)</text>
  <text x="545" y="273" fill="#cbd5e1" font-size="9.5">• 3D NAND 수직 적층 & FinFET 필수</text>
  <text x="545" y="295" fill="#fbbf24" font-size="10" font-weight="700">WTW: 챔버 컨디셔닝 & APC 피드백</text>
  <text x="545" y="313" fill="#94a3b8" font-size="8.5">➔ 1년 365일 로트 간 균일 재현성 유지</text>
</svg>""",
        "lecture": r"""<h3>1. 왜 강사는 "Uniformity, Uniformity, Uniformity"를 세 번이나 외쳤는가?</h3>
<p>반도체 공정에서 균일도(Uniformity)는 단순한 품질 관리 지표가 아니라 <strong>수율(Yield)과 직결되는 절대적 생존 조건</strong>입니다. 그 이유는 다음과 같습니다:</p>
<ul>
  <li><strong>소자 파라미터 산포 폭발 방지</strong>: 게이트 유전막 두께($t_{ox}$)가 1nm 수준인 최선단 소자에서 0.1nm의 불균일은 $C_{ox} = \epsilon/t_{ox}$ 공식에 의해 커패시턴스를 10% 변화시키고, 문턱전압($V_{th}$)을 수십 mV 이동시킵니다. 이는 동작 주파수 저하와 오프 누설 전류 폭증을 부릅니다.</li>
  <li><strong>후속 식각(Etch) 공정 마진 붕괴 방지</strong>: 증착된 막질의 두께가 웨이퍼 영역마다 다르면, 식각 공정 시 얇은 영역은 이미 다 깎여 하부 기판이 손상(Over-etch Punch-through)되는 반면, 두꺼운 영역은 식각이 덜 끝나 잔류물(Under-etch Residue)이 남아 배선 단락(Short)을 일으킵니다.</li>
</ul>

<h3>2. 균일도의 3대 핵심 차원</h3>
<ol>
  <li><strong>WIW (Within-Wafer Uniformity, 웨이퍼 내 균일도)</strong>:
    <p>직경 300mm(12인치) 대구경 웨이퍼 표면 전체에서 중심부(Center)와 외곽부(Edge)의 두께 차이를 관리합니다. 가스 공급 샤워헤드의 홀 밀도 분배, 웨이퍼 에지 링(Edge Ring)을 통한 가스 배기 균형, 척(Chuck) 히터의 멀티존(Multi-zone) 독립 온도 제어로 중심-외곽 편차를 극소화합니다.</p>
  </li>
  <li><strong>WTW (Wafer-to-Wafer Uniformity, 웨이퍼 간 균일도) & Lot-to-Lot</strong>:
    <p>1개 카세트(25장) 내의 첫 번째 웨이퍼와 마지막 웨이퍼, 그리고 수천 장을 생산하는 동안 배치 간 두께가 일정해야 합니다. 챔버 내부 벽면에 증착 부산물이 쌓여 열전달이나 플라즈마 임피던스가 변하는 <strong>챔버 드리프트(Chamber Drift)</strong>를 막기 위해 인시츄 클리닝(In-situ Clean)과 고급 공정 제어(APC, Advanced Process Control) 피드백 알고리즘을 사용합니다.</p>
  </li>
  <li><strong>3D 단차 도포성 (Step Coverage, 구조 내 균일도)</strong>:
    <p>평면뿐만 아니라 깊게 파인 트렌치(Trench)나 비아 홀(Via Hole)의 상단(Top), 측벽(Sidewall), 바닥(Bottom) 간 두께 비율입니다.
    $$\text{Step Coverage (S/C)} = \frac{t_{\text{bottom}}}{t_{\text{top}}} \times 100\%$$
    3D NAND의 채널 홀처럼 깊이가 수십 $\mu\text{m}$이고 종횡비(Aspect Ratio)가 70:1 이상인 구조에서는 S/C가 95% 이상 나오지 않으면 신뢰성이 파괴됩니다.</p>
  </li>
</ol>

<h3>3. 기착 확률(Sticking Coefficient)과 보이드(Void) 발생 메커니즘</h3>
<p>가스 분자가 표면에 닿았을 때 달라붙는 확률을 <strong>기착 확률($S_c$)</strong>이라고 합니다:</p>
<ul>
  <li><strong>PVD 및 APCVD ($S_c \approx 1$)</strong>: 분자가 표면에 부딪히자마자 즉시 달라붙으므로, 노출이 많은 패턴 입구 모서리에 먼저 막이 두껍게 쌓이는 <strong>돌출(Overhang) 현상</strong>이 발생합니다. 그 결과 입구가 먼저 닫히는 핀치오프(Pinch-off)가 발생하여 내부에 텅 빈 공간인 <strong>보이드(Void)나 이음매(Seam)</strong>가 갇히게 됩니다.</li>
  <li><strong>ALD ($S_c \rightarrow 0$, 포화 후 반응)</strong>: 표면 흡착이 자기제한적으로 포화될 때까지 분자가 패턴 바닥 깊숙한 곳까지 자유롭게 튕겨 들어가(Knudsen Diffusion) 흡착되므로 보이드가 전혀 없는 100% Conformal 증착이 가능합니다.</li>
</ul>"""
    },
    {
        "id": "q-03",
        "num": "03",
        "badge": "⭐ 최신 질문 (증착 공정 3/4)",
        "is_latest": False,
        "title": "증착 3) 박막 두께는 어떻게 계측할까? (엘립소메트리 Ellipsometry, 광학 간섭계, X선 계측)",
        "nav_title": "증착 3) 박막 두께는 어떻게 계측할까?",
        "summary": [
            "양산 팹(FAB)의 박막 두께 계측은 웨이퍼를 손상시키지 않고 초고속으로 전수 검사할 수 있는 비파괴 광학 방식인 <strong>분광 엘립소메트리(Spectroscopic Ellipsometry, SE)</strong>와 <strong>반사율 분광 간섭계(Spectroscopic Reflectometry, SR)</strong>가 표준입니다.",
            "<strong>엘립소메트리(Ellipsometry)</strong>는 편광된 빛이 박막에 비스듬히 입사하여 반사될 때의 진폭비 각도($\\Psi$)와 위상차 각도($\\Delta$) 변화($\\rho = \\tan\\Psi e^{i\\Delta}$)를 측정하여, 두께($d$)와 복소 굴절률($n, k$)을 $\\text{\\AA}$ 단위(단원자층) 극초정밀도로 역산해 냅니다.",
            "<strong>반사 분광 간섭계(Reflectometry)</strong>는 수직 입사광이 박막 표면과 하부 계면에서 반사되어 나타나는 간섭 파형 주기($2nd = m\\lambda$)를 측정하여 수십 nm 이상의 투명 절연막 두께를 고속으로 측정합니다.",
            "불투명한 금속 박막은 형광 X선 방출량을 측정하는 <strong>XRF</strong>나 <strong>XRR</strong>을 활용하며, 모든 광학 계측기의 절대 표준(Calibration Standard)은 집속이온빔(FIB)으로 자른 단면의 원자 격자를 직접 촬영하는 <strong>TEM(투과전자현미경)</strong>으로 교정합니다."
        ],
        "svg_title": "📊 [박막 두께 계측 3대 핵심 기술 원리] 엘립소메트리 vs 반사 분광계 vs TEM 격자 관측",
        "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: Ellipsometry -->
  <rect x="20" y="25" width="365" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="50" fill="#38bdf8" font-size="12.5" font-weight="800">1. 분광 엘립소메트리 (Ellipsometry: 최고 정밀도)</text>
  <!-- Optical schematic -->
  <circle cx="50" cy="85" r="10" fill="#fbbf24"/>
  <text x="42" y="89" fill="#0f172a" font-size="9" font-weight="800">광원</text>
  <!-- Polarizer -->
  <line x1="65" y1="90" x2="110" y2="120" stroke="#fbbf24" stroke-width="2"/>
  <rect x="110" y="110" width="12" height="25" fill="#38bdf8" rx="2"/>
  <text x="95" y="105" fill="#38bdf8" font-size="9">편광기 (선형편광)</text>
  <!-- Beam to wafer -->
  <line x1="122" y1="123" x2="185" y2="175" stroke="#38bdf8" stroke-width="2.5"/>
  <!-- Wafer sample -->
  <rect x="140" y="175" width="90" height="25" fill="#1e293b" stroke="#64748b"/>
  <rect x="140" y="170" width="90" height="6" fill="#0284c7" opacity="0.8"/>
  <text x="155" y="192" fill="#94a3b8" font-size="9">Si 기판</text>
  <text x="150" y="166" fill="#38bdf8" font-size="8.5" font-weight="700">박막 (d, n, k)</text>
  <!-- Reflected beam (Elliptical) -->
  <line x1="185" y1="175" x2="250" y2="120" stroke="#a855f7" stroke-width="2.5"/>
  <ellipse cx="220" cy="145" rx="5" ry="12" fill="none" stroke="#a855f7" stroke-width="1.5" transform="rotate(-35 220 145)"/>
  <text x="235" y="135" fill="#a855f7" font-size="9">타원편광 반사</text>
  <!-- Analyzer & Detector -->
  <rect x="250" y="110" width="12" height="25" fill="#10b981" rx="2"/>
  <rect x="275" y="95" width="25" height="20" fill="#334155" rx="3"/>
  <text x="278" y="108" fill="#10b981" font-size="8.5">검광기</text>

  <!-- Math formula card -->
  <rect x="35" y="210" width="335" height="120" rx="4" fill="#1e293b"/>
  <text x="45" y="230" fill="#fbbf24" font-size="10.5" font-weight="700">핵심 측정 원리 공식: ρ = rp / rs</text>
  <text x="45" y="250" fill="#34d399" font-size="11" font-weight="700">ρ = tan(Ψ) · exp( i · Δ )</text>
  <text x="45" y="270" fill="#cbd5e1" font-size="9.5">• Ψ (Psi): p편광과 s편광의 진폭 감쇠비</text>
  <text x="45" y="287" fill="#cbd5e1" font-size="9.5">• Δ (Delta): p편광과 s편광의 위상차 변화</text>
  <text x="45" y="305" fill="#38bdf8" font-size="9.5">• 굴절률(n), 흡수계수(k), 두께(d) 동시 도출</text>
  <text x="45" y="322" fill="#fbbf24" font-size="9">➔ Å 단위 초박막(Gate High-k 등) 양산 표준</text>

  <!-- Right: Reflectometry & TEM -->
  <rect x="400" y="25" width="360" height="320" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
  <text x="415" y="50" fill="#f59e0b" font-size="12.5" font-weight="800">2. 반사 간섭계(SR) & TEM 교정 캘리브레이션</text>

  <!-- Reflectometry Box -->
  <rect x="415" y="65" width="330" height="125" rx="5" fill="#1e293b"/>
  <text x="425" y="85" fill="#f59e0b" font-size="11" font-weight="700">① 반사 분광 간섭계 (Reflectometry: 고속 측정)</text>
  <text x="425" y="105" fill="#cbd5e1" font-size="10">• 수직 입사광의 상부 반사파(r₁)와 하부 반사파(r₂) 간섭</text>
  <text x="425" y="125" fill="#34d399" font-size="10.5" font-weight="700">• 광로차 조건: 2 · n · d = m · λ (보강/상쇄)</text>
  <text x="425" y="145" fill="#cbd5e1" font-size="9.5">• 간섭 줄무늬 피크 간격으로 수십 nm~수 μm 두께 연산</text>
  <text x="425" y="163" fill="#fbbf24" font-size="9.5">➔ 광학계 단순, 측정 속도 극히 빠름 (초당 수십 포인트)</text>
  <text x="425" y="179" fill="#94a3b8" font-size="8.5">(단점: 단일 투명 박막에 한정, 극초박막 < 5nm 오차 큼)</text>

  <!-- TEM & X-ray Box -->
  <rect x="415" y="200" width="330" height="130" rx="5" fill="#1e293b"/>
  <text x="425" y="220" fill="#10b981" font-size="11" font-weight="700">② 금속막 계측(XRF/XRR) & 기준 TEM</text>
  <text x="425" y="240" fill="#38bdf8" font-size="10">• XRF (X-선 형광): 불투명 금속 박막 두께/조성 분석</text>
  <text x="425" y="258" fill="#38bdf8" font-size="10">• XRR (X-선 반사율): 임계각 간섭으로 밀도/두께 측정</text>
  <text x="425" y="278" fill="#10b981" font-size="10.5" font-weight="700">• HR-TEM (원자 격자 직접 관측 / 절대 표준)</text>
  <text x="425" y="296" fill="#cbd5e1" font-size="9.5">- FIB로 시편 절단 후 원자 격자(Lattice Fringe) 계수</text>
  <text x="425" y="313" fill="#34d399" font-size="9.5">- 광학 엘립소메트리 모델의 피팅 기준 표준(Golden Sample)</text>
</svg>""",
        "lecture": r"""<h3>1. 박막 두께 계측의 핵심 과제: 비파괴(Non-Destructive) & 인라인(In-Line)</h3>
<p>양산 반도체 웨이퍼는 한 장에 수천만 원에 달하므로, 두께를 재기 위해 웨이퍼를 자를 수는 없습니다. 따라서 <strong>빛(광학)이나 X-선을 쏘아 반사되는 신호를 분석하는 비파괴 계측</strong>이 팹(FAB) 내에 100% 인라인으로 도입되어 있습니다.</p>

<h3>2. 분광 엘립소메트리(Spectroscopic Ellipsometry, SE)의 심층 원리</h3>
<p>엘립소메트리는 반도체 박막 계측의 꽃이라 불리는 최고 정밀도 비파괴 계측기입니다.</p>
<ol>
  <li><strong>원리</strong>: 특정한 편광 상태(예: 선형 편광)의 빛을 브루스터 각(Brewster angle) 부근의 큰 입사각(약 70°)으로 박막에 입사시킵니다. 빛이 박막 표면과 하부 기판 계면에서 반사될 때, 입사면에 평행한 p-편광과 수직인 s-편광의 반사율 및 위상이 달라져 <strong>타원 편광(Elliptical polarization)</strong>으로 변환됩니다.</li>
  <li><strong>측정 파라미터 ($\Psi, \Delta$)</strong>:
    $$\rho = \frac{r_p}{r_s} = \tan(\Psi) \exp(i\Delta)$$
    여기서 $\tan(\Psi)$는 두 편광 성분의 진폭 반사율 비이며, $\Delta$는 반사 과정에서 발생한 위상차(Phase shift)입니다.</li>
  <li><strong>독보적 장점</strong>: 빛의 세기(Intensity) 자체를 재는 것이 아니라 <strong>진폭비와 위상차의 상대적 변화</strong>를 측정하므로 광원의 밝기 변동에 영향을 받지 않아 잡음에 매우 강합니다. 또한 위상차 $\Delta$는 박막 두께가 $0.1\,\text{nm}$만 변해도 민감하게 반응하므로 <strong>단원자층($\text{\AA}$) 수준의 극초박막 두께와 복소 굴절률($n, k$)</strong>을 동시에 역산할 수 있습니다.</li>
</ol>

<h3>3. 반사 분광 간섭계(Spectroscopic Reflectometry, SR)</h3>
<p>빛을 박막 표면에 수직($90^\circ$)으로 쏘아 반사되어 돌아오는 빛의 스펙트럼 강도를 분석합니다.</p>
<ul>
  <li>박막 윗면에서 반사된 빛과 아랫면(실리콘 기판 계면)에서 반사된 빛 사이에는 $2nd$ (왕복 광로차)만큼의 경로 차이가 발생합니다.</li>
  <li>파장($\lambda$)에 따라 보강 간섭($2nd = m\lambda$)과 상쇄 간섭이 번갈아 나타나며, 파장에 따른 반사율 그래프에서 <strong>간섭 피크의 개수와 간격</strong>을 세어 두께 $d$를 빠르게 계산합니다.</li>
  <li>측정 속도가 초당 수십 지점으로 매우 빠르지만, 박막 두께가 5nm 이하로 얇아지면 간섭 피크가 나타나지 않아 측정이 불가능해집니다.</li>
</ul>

<h3>4. 불투명 금속막 및 최종 검증 표준(TEM)</h3>
<ul>
  <li><strong>금속 박막 (Cu, W, Co 등)</strong>: 빛이 침투하지 못하고 전반사되므로 광학 계측이 불가능합니다. 따라서 고에너지 X-선을 쏘아 원자 고유의 특성 X선 방출량을 세는 <strong>XRF(X-ray Fluorescence)</strong>나, 저각도 X선 반사의 간섭 패턴을 보는 <strong>XRR</strong>을 사용하며, 4-Point Probe 면저항($R_s = \rho/t$)으로 간접 역산합니다.</li>
  <li><strong>TEM(투과전자현미경)</strong>: FIB(집속이온빔)로 웨이퍼의 특정 다이를 파괴적으로 얇게 절단한 뒤, 투과전자현미경으로 실리콘 원자 격자 줄무늬(Lattice Fringe)를 직접 세어 박막 두께를 잽니다. 이것이 광학 엘립소메트리 측정 모델을 보정(Calibration)하는 <strong>절대 표준(Golden Reference)</strong> 역할을 합니다.</li>
</ul>"""
    },
    {
        "id": "q-04",
        "num": "04",
        "badge": "⭐ 최신 질문 (증착 공정 4/4)",
        "is_latest": False,
        "title": "증착 4) 열 예산 (박막 증착과 Thermal Budget: FEOL/BEOL 열화 방지 및 저온화 기술)",
        "nav_title": "증착 4) 열 예산",
        "summary": [
            "<strong>열 예산(Thermal Budget, $\\int T(t) dt$)</strong>은 웨이퍼가 전체 제조 공정 동안 노출될 수 있는 열적 에너지(온도×시간)의 허용 상한량이며, 이미 제작된 하부 패턴이 열에 의해 파괴되지 않도록 후속 증착 공정은 열 예산을 엄격하게 준수해야 합니다.",
            "<strong>FEOL(전공정 트랜지스터 단계)</strong>에서는 정밀하게 주입된 소스/드레인의 초얕은 접합(USJ)과 헤일로(Halo) 도펀트가 고온에서 재확산(Dopant Out-diffusion)되어 단채널 효과(SCE) 방어선이 무너지므로 고온 증착이 금지됩니다.",
            "<strong>BEOL(후공정 금속 배선 단계)</strong>에서는 구리(Cu) 배선의 마이그레이션 방지, 배리어 메탈 보호, 저유전율(Low-k) 층간 절연막의 열분해 파괴를 방지하기 위해 챔버 온도를 <strong>무조건 400℃ 이하</strong>로 강력하게 봉쇄합니다.",
            "따라서 반도체 증착 기술의 발전사는 고온 열 에너지를 쓰던 LPCVD(600~900℃)에서 RF 플라즈마 전자로 반응을 유도하는 PECVD(200~400℃), 나아가 초저온(150~250℃)에서 원자층을 쌓는 PEALD로 진화해 온 <strong>'열 예산 절감의 역사'</strong>입니다."
        ],
        "svg_title": "📊 [공정 단계별 열 예산 한계 및 증착 저온화 로드맵] FEOL vs BEOL 400℃ 상한선",
        "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: Temperature Ceiling by Process Stage -->
  <rect x="20" y="25" width="365" height="320" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.2"/>
  <text x="35" y="50" fill="#f87171" font-size="12.5" font-weight="800">1. 반도체 공정 단계별 열 예산 허용 온도 상한선</text>

  <!-- Bar 1: Well & Isolation -->
  <rect x="40" y="75" width="325" height="42" rx="4" fill="#1e293b"/>
  <rect x="40" y="75" width="310" height="42" rx="4" fill="#ef4444" opacity="0.3"/>
  <text x="50" y="93" fill="#ffffff" font-size="10.5" font-weight="700">① 기판 웰(Well) & STI 매립 (1000 ~ 1100℃)</text>
  <text x="50" y="109" fill="#fca5a5" font-size="9.5">• 소자 구조 형성 전 단계 ➔ 최고온 퍼니스 열처리 허용</text>

  <!-- Bar 2: Gate & USJ -->
  <rect x="40" y="125" width="325" height="42" rx="4" fill="#1e293b"/>
  <rect x="40" y="125" width="230" height="42" rx="4" fill="#f59e0b" opacity="0.3"/>
  <text x="50" y="143" fill="#ffffff" font-size="10.5" font-weight="700">② 게이트 산화막 & USJ 활성화 (600 ~ 800℃)</text>
  <text x="50" y="159" fill="#fcd34d" font-size="9.5">• 초얕은 접합(USJ) 번짐 방지 ➔ RTA 스파이크 열처리 적용</text>

  <!-- Bar 3: Salicide -->
  <rect x="40" y="175" width="325" height="42" rx="4" fill="#1e293b"/>
  <rect x="40" y="175" width="160" height="42" rx="4" fill="#eab308" opacity="0.3"/>
  <text x="50" y="193" fill="#ffffff" font-size="10.5" font-weight="700">③ 살리사이드(NiSi) 형성 (450 ~ 500℃)</text>
  <text x="50" y="209" fill="#fef08a" font-size="9.5">• 500℃ 초과 시 NiSi₂ 고저항 상전이 & 응집(Agglomeration) 파괴</text>

  <!-- Bar 4: BEOL Metal Wiring LIMIT -->
  <rect x="40" y="225" width="325" height="52" rx="4" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
  <rect x="40" y="225" width="120" height="52" rx="4" fill="#0284c7" opacity="0.5"/>
  <text x="50" y="245" fill="#38bdf8" font-size="11" font-weight="800">④ BEOL 금속 배선 공정 (★ 400℃ 절대 상한선)</text>
  <text x="50" y="262" fill="#bae6fd" font-size="9.5">• Cu 배선 마이그레이션 & Low-k 절연막 분해 방지</text>

  <rect x="40" y="288" width="325" height="45" rx="4" fill="#0b1120" stroke="#f87171" stroke-width="1"/>
  <text x="50" y="306" fill="#f87171" font-size="10" font-weight="700">⚠️ 열 예산 초과 시: 확산 길이 L = 2√(Dt) 지수함수 폭증</text>
  <text x="50" y="322" fill="#cbd5e1" font-size="9">➔ 트랜지스터 숏채널 효과(DIBL, Punchthrough) 즉각 발발</text>

  <!-- Right: Deposition Evolution Solution -->
  <rect x="400" y="25" width="360" height="320" rx="8" fill="#0f172a" stroke="#34d399" stroke-width="1.2"/>
  <text x="415" y="50" fill="#34d399" font-size="12.5" font-weight="800">2. 열 예산 극복을 위한 증착 기술의 진화</text>

  <rect x="415" y="65" width="330" height="75" rx="5" fill="#1e293b"/>
  <text x="425" y="85" fill="#f87171" font-size="11" font-weight="700">[과거] 열 화학 LPCVD (600 ~ 900℃)</text>
  <text x="425" y="103" fill="#cbd5e1" font-size="10">• 오직 기판 열 에너지로만 반응 가스 해리</text>
  <text x="425" y="120" fill="#fca5a5" font-size="9.5">➔ 하부 접합 및 금속 배선 열화로 현대 선단 공정 적용 불가</text>

  <rect x="415" y="150" width="330" height="85" rx="5" fill="#1e293b"/>
  <text x="425" y="170" fill="#38bdf8" font-size="11" font-weight="700">[도약] 플라즈마 PECVD (200 ~ 400℃)</text>
  <text x="425" y="188" fill="#cbd5e1" font-size="10">• RF 플라즈마 고에너지 전자가 라디칼 생성</text>
  <text x="425" y="205" fill="#34d399" font-size="10">• 400℃ 이하에서 고속 산화막/질화막 증착 성공</text>
  <text x="425" y="222" fill="#38bdf8" font-size="9.5">➔ BEOL 금속 배선 층간 절연막(IMD) 양산 도입</text>

  <rect x="415" y="245" width="330" height="85" rx="5" fill="#1e293b"/>
  <text x="425" y="265" fill="#10b981" font-size="11" font-weight="700">[현재 & 미래] PEALD (100 ~ 250℃ 초저온)</text>
  <text x="425" y="283" fill="#cbd5e1" font-size="10">• 플라즈마 직접 반응으로 초저온 단원자층 증착</text>
  <text x="425" y="300" fill="#34d399" font-size="10">• 열 예산 거의 소모 없이 100% 단차 도포성 확보</text>
  <text x="425" y="317" fill="#fbbf24" font-size="9.5">➔ 3D FinFET, GAA 나노시트, 첨단 HBM 패키징 필수</text>
</svg>""",
        "lecture": r"""<h3>1. 열 예산(Thermal Budget)의 본질적 의미와 물리 법칙</h3>
<p>열 예산은 반도체 칩이 제작되는 전체 공정 라이프사이클 동안 받는 <strong>열의 총 누적량</strong>을 의미하며, 수학적으로는 $\int T(t) dt$로 표현됩니다. 온도가 높을수록, 고온 노출 시간이 길수록 열 예산은 기하급수적으로 소모됩니다.</p>
<p>이것이 무서운 이유는 <strong>Fick의 확산 제2법칙</strong> 때문입니다:</p>
$$\frac{\partial C}{\partial t} = D(T) \frac{\partial^2 C}{\partial x^2}, \quad D(T) = D_0 \exp\left(-\frac{E_a}{k_B T}\right)$$
<p>확산 계수 $D(T)$는 온도 $T$의 <strong>지수함수(Exponential)</strong>로 비례합니다. 즉, 온도가 100℃만 올라가도 도펀트가 움직이는 확산 속도는 수십~수백 배 폭증하여, 확산 침투 거리 $L = 2\sqrt{Dt}$가 급격히 늘어납니다.</p>

<h3>2. 공정 단계별 허용 온도(Ceiling)와 물리적 파괴 메커니즘</h3>
<ol>
  <li><strong>FEOL (트랜지스터 형성 초기)</strong>:
    <p>기판 웰(Well) 형성과 STI 트렌치 매립 단계에서는 아직 미세 패턴이 없으므로 1,000℃ 이상의 고온 열처리가 허용됩니다.</p>
  </li>
  <li><strong>초얕은 접합(USJ) 및 헤일로(Halo) 형성 후 (한계: 600~700℃)</strong>:
    <p>단채널 효과(SCE)를 막기 위해 기판 표면 $10\,\text{nm}$ 미만으로 정밀하게 얕게 도핑해 둔 $N^+$ 소스/드레인과 채널 모서리의 $P^+$ 헤일로 도펀트가 고온 증착 챔버에 들어가면 <strong>채널 내부로 옆으로 번져버립니다(Lateral Straggle)</strong>. 이로 인해 실효 채널 길이($L_{eff}$)가 급감하고 DIBL과 펀치스루가 즉각 재발합니다.</p>
  </li>
  <li><strong>살리사이드(Salicide: NiSi) 형성 후 (한계: 450~500℃)</strong>:
    <p>콘택 저항을 낮추기 위해 접합 표면에 형성한 니켈 실리사이드(NiSi)는 500℃를 넘으면 고저항 상인 $\text{NiSi}_2$로 변하거나 얇은 막이 덩어리로 뭉쳐 찢어지는 <strong>응집 현상(Agglomeration)</strong>이 발생하여 소자가 파괴됩니다.</p>
  </li>
  <li><strong>BEOL 금속 배선 단계 (한계: 400℃ Hard Limit)</strong>:
    <p>구리(Cu)는 녹는점이 낮아 400℃를 넘으면 원자가 이동하여 보이드(단선)를 만들고, Cu 확산 방지용 질화막 배리어가 파괴되어 실리콘으로 침투합니다. 또한 배선 간 기생 커패시턴스를 줄이기 위해 도입된 <strong>Low-k 유전막(SiCOH)의 메틸기($-\text{CH}_3$)가 열분해되어 다공성 구조가 붕괴</strong>되므로 400℃ 초과는 절대 금기입니다.</p>
  </li>
</ol>

<h3>3. 증착 공정의 역사: 열 예산을 줄이기 위한 기술적 진화</h3>
<p>따라서 반도체 증착 기술은 열 예산의 상한선이 낮아지는 흐름에 맞춰 진화해 왔습니다:</p>
<ul>
  <li><strong>LPCVD (고온의 한계)</strong>: 고온(600~900℃)에서만 반응 가스가 분해되므로 후반부 공정에는 쓸 수 없습니다.</li>
  <li><strong>PECVD (플라즈마 혁신, 200~400℃)</strong>: 열 대신 <strong>RF 플라즈마의 고에너지 전자</strong>가 기체 분자를 때려 반응성 높은 라디칼을 만듦으로써, 기판을 가열하지 않고도 200~400℃ 저온에서 고속 증착을 가능하게 하여 BEOL 배선 절연막 형성을 성공시켰습니다.</li>
  <li><strong>PEALD (초저온 원자층 증착, 100~250℃)</strong>: 열 에너지가 전혀 없는 상온~200℃ 수준에서도 플라즈마 라디칼을 반응제로 사용하여 원자층 단위의 고밀도 박막을 완벽한 Step Coverage로 형성합니다. FinFET, GAA 3D 트랜지스터 및 첨단 HBM 패키징 공정의 핵심입니다.</li>
</ul>"""
    }
]

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 55 topics (q-55 down to q-01) by +4 (q-XX -> q-(XX+4))
    # We must go from 55 down to 1
    for old_n in range(55, 0, -1):
        new_n = old_n + 4
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

    # For old Q 01 (now Q 05), remove 'latest-card-highlight' from section class
    html = re.sub(
        r'<section class="topic-section latest-card-highlight" id="q-05">',
        r'<section class="topic-section" id="q-05">',
        html
    )

    # Step 2: Build new nav-items for Q 01 ~ Q 04
    new_nav_items = ""
    for t in DEPO_TOPICS:
        new_nav_items += f'      <li class="nav-item"><a href="#{t["id"]}" class="nav-link"><span class="nav-num">{t["num"]}</span><span class="nav-text">{t["title"]}</span></a></li>\n'

    nav_list_pos = html.find('<ul class="nav-list" id="navList">')
    if nav_list_pos != -1:
        insert_nav = nav_list_pos + len('<ul class="nav-list" id="navList">\n')
        html = html[:insert_nav] + new_nav_items + html[insert_nav:]
    else:
        print("Error: navList not found")

    # Step 3: Build new sections for Q 01 ~ Q 04
    new_sections_html = ""
    for t in DEPO_TOPICS:
        highlight_class = " latest-card-highlight" if t["is_latest"] else ""
        latest_tag_html = f'\n          <span class="latest-tag">{t["badge"]}</span>'
        summary_lis = "\n".join([f"          <li>{s}</li>" for s in t["summary"]])

        sec = f"""
    <!-- Q {t['num']} : {t['title']} -->
    <section class="topic-section{highlight_class}" id="{t['id']}">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q {t['num']}</span>{latest_tag_html}
          <h2 class="topic-title">{t['title']}</h2>
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
            {t['svg_title']}
          </div>
          {t['svg']}
        </div>
        {t['lecture']}
      </div>
    </section>
"""
        new_sections_html += sec

    main_header_end = html.find("</header>")
    if main_header_end != -1:
        insert_sec = main_header_end + len("</header>")
        html = html[:insert_sec] + "\n" + new_sections_html + html[insert_sec:]
    else:
        print("Error: </header> not found")

    # Step 4: Update header description text
    old_desc = '최상단에는 가장 최근 질문인 <strong>\'반도체 제조 단위 공정 20대 핵심 주제 (산화, 노광, 식각, 이온주입, 금속 배선, 첨단 패키징 HBM)\'</strong>가 1~20번으로 위치합니다.'
    new_desc = '최상단에는 가장 최근 질문인 <strong>\'증착 공정 4대 핵심 주제 (APCVD/LPCVD/ALD/PECVD, 균일도 Uniformity, 박막 두께 계측, 열 예산)\'</strong> 및 HBM 특강이 최신 1~5번으로 위치하며, 총 59개 질문으로 구성되어 있습니다.'
    if old_desc in html:
        html = html.replace(old_desc, new_desc)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding 4 deposition topics!")
