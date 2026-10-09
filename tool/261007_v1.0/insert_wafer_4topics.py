import os
import re

def update_html():
    file_path = r"C:\Work\반도체3\result\261007_v1.0\index.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. New Q01~Q04 nav-items
    new_nav_items = """      <li class="nav-item"><a href="#q-01" class="nav-link"><span class="nav-num">01</span><span class="nav-text">웨이퍼 제조 1) 초크랄스키 기법 (300mm 웨이퍼)</span></a></li>
      <li class="nav-item"><a href="#q-02" class="nav-link"><span class="nav-num">02</span><span class="nav-text">웨이퍼 제조 2) 기판 도핑 (P- / P+ / N- / N+)</span></a></li>
      <li class="nav-item"><a href="#q-03" class="nav-link"><span class="nav-num">03</span><span class="nav-text">웨이퍼 제조 3) 도핑 농도와 면저항의 관계</span></a></li>
      <li class="nav-item"><a href="#q-04" class="nav-link"><span class="nav-num">04</span><span class="nav-text">웨이퍼 제조 4) 웨이퍼 결정 단면에 따른 특성 변화</span></a></li>
"""

    # 2. Four new sections with inline SVGs
    new_sections = """    <!-- Q 01 : 웨이퍼 제조 1) 초크랄스키 기법 (300mm 웨이퍼) -->
    <section class="topic-section latest-card-highlight" id="q-01">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q 01</span>
          <span class="latest-tag">⭐ 가장 최근 질문 (웨이퍼 1/4)</span>
          <h2 class="topic-title">웨이퍼 제조 1) 초크랄스키 기법 (300mm 웨이퍼)</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">면접 대비 3~4줄 핵심 요약</span>
        <ul class="summary-list">
          <li><strong>"초크랄스키(CZ: Czochralski) 기법은 고순도 폴리실리콘 용융액(1420℃)에 종자 결정(Seed)을 담근 뒤, 회전시키며 서서히 인상(Pulling)하여 원통형 단결정 잉곳(Ingot)을 성장시키는 핵심 공정입니다."</strong></li>
          <li><strong>"초기 직경을 3~5mm로 가늘게 뽑는 '네킹(Dash Necking)' 공정을 통해 열충격 전위(Dislocation)를 밖으로 배출시켜 결함 제로의 무전위 단결정을 확보합니다."</strong></li>
          <li><strong>"현대 300mm 대구경 웨이퍼는 열대류에 의한 산소 오염과 도펀트 불균일을 막기 위해 강력한 자기장을 인가하는 MCZ(Magnetic CZ) 기술을 필수로 적용합니다."</strong></li>
        </ul>
      </div>
      <div class="lecture-content">
        <!-- SVG 그래픽 다이어그램: 초크랄스키(CZ) 성장 공정 4단계 -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [초크랄스키 잉곳 성장 메커니즘] 네킹(무전위화) ➔ 숄더 ➔ 직동(Body 300mm) ➔ 테일 분리
          </div>
          <svg viewBox="0 0 780 430" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <defs>
              <linearGradient id="czMelt" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#ea580c"/>
                <stop offset="100%" stop-color="#9a3412"/>
              </linearGradient>
              <linearGradient id="czIngot" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#94a3b8"/>
                <stop offset="50%" stop-color="#cbd5e1"/>
                <stop offset="100%" stop-color="#64748b"/>
              </linearGradient>
            </defs>

            <rect width="780" height="430" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

            <!-- Left: CZ Furnace Chamber Diagram -->
            <rect x="30" y="30" width="360" height="370" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
            <text x="45" y="55" fill="#38bdf8" font-size="12" font-weight="800">CZ 장비 챔버 & 잉곳 인상 모식도</text>

            <!-- Pulling Rod -->
            <rect x="195" y="65" width="10" height="60" fill="#64748b"/>
            <text x="215" y="85" fill="#38bdf8" font-size="10" font-weight="700">인상축 (Pulling ↻)</text>

            <!-- Ingot Shape -->
            <!-- Seed & Necking -->
            <rect x="198" y="125" width="4" height="20" fill="#cbd5e1"/>
            <text x="80" y="138" fill="#f59e0b" font-size="10.5" font-weight="700">① 네킹 (3~5mm, 무전위화) ──►</text>
            <!-- Shoulder -->
            <polygon points="198,145 202,145 270,185 130,185" fill="url(#czIngot)"/>
            <text x="50" y="170" fill="#cbd5e1" font-size="10">② 어깨 형성 (Shoulder) ──►</text>
            <!-- Body (300mm Ingot) -->
            <rect x="130" y="185" width="140" height="100" fill="url(#czIngot)" stroke="#475569"/>
            <text x="145" y="235" fill="#0f172a" font-size="13" font-weight="900">300mm Ingot (직동)</text>
            <!-- Tail/End Cone into Melt -->
            <polygon points="130,285 270,285 220,310 180,310" fill="url(#czIngot)"/>

            <!-- Quartz Crucible & Melt -->
            <path d="M 80 305 Q 80 380 200 380 Q 320 380 320 305 Z" fill="url(#czMelt)" stroke="#f97316" stroke-width="1.5"/>
            <text x="145" y="350" fill="#ffffff" font-size="12" font-weight="800">실리콘 융액 (1420℃)</text>
            <text x="145" y="368" fill="#fed7aa" font-size="9.5">석영 도가니 (Crucible ↺)</text>

            <!-- Heater Coils -->
            <rect x="60" y="300" width="12" height="75" rx="3" fill="#ef4444"/>
            <rect x="328" y="300" width="12" height="75" rx="3" fill="#ef4444"/>
            <text x="345" y="342" fill="#ef4444" font-size="10" font-weight="700">흑연 히터</text>


            <!-- Right: 4 Core Growth Steps & 300mm Key Technology -->
            <!-- Step Card 1: Dash Necking -->
            <rect x="410" y="30" width="340" height="85" rx="6" fill="rgba(56, 189, 248, 0.08)" stroke="#38bdf8" stroke-width="1"/>
            <text x="425" y="52" fill="#38bdf8" font-size="12" font-weight="800">1. 대시 네킹(Dash Necking) 기술</text>
            <text x="425" y="72" fill="#cbd5e1" font-size="10.5">• 1420℃ 융액 접촉 시 극심한 열충격으로 전위(결함) 발생</text>
            <text x="425" y="90" fill="#cbd5e1" font-size="10.5">• 직경을 3~5mm로 가늘게 뽑아 전위를 표면 밖으로 밀어냄</text>
            <text x="425" y="106" fill="#34d399" font-size="10" font-weight="700">➔ 결함이 전혀 없는 무전위(Dislocation-free) 단결정 달성!</text>

            <!-- Step Card 2: Shoulder & Body -->
            <rect x="410" y="125" width="340" height="85" rx="6" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1"/>
            <text x="425" y="147" fill="#10b981" font-size="12" font-weight="800">2. 숄더(Shoulder) & 바디(Body) 성장</text>
            <text x="425" y="167" fill="#cbd5e1" font-size="10.5">• 인상 속도를 줄여 목표 직경(300mm, 12인치)까지 확장</text>
            <text x="425" y="185" fill="#cbd5e1" font-size="10.5">• 회전 속도와 온도 밸런스로 길이 2m, 중량 200kg 성장</text>
            <text x="425" y="201" fill="#38bdf8" font-size="10" font-weight="700">➔ 초정밀 직경 편차 제어 (오차 ±0.5mm 이내)</text>

            <!-- Step Card 3: MCZ (Magnetic CZ) for 300mm -->
            <rect x="410" y="220" width="340" height="95" rx="6" fill="rgba(245, 158, 11, 0.08)" stroke="#f59e0b" stroke-width="1"/>
            <text x="425" y="242" fill="#f59e0b" font-size="12" font-weight="800">3. 300mm 대구경 필수: MCZ (Magnetic CZ)</text>
            <text x="425" y="262" fill="#cbd5e1" font-size="10.5">• 거대 도가니 내부의 난류 열대류(Thermal Convection) 억제</text>
            <text x="425" y="280" fill="#cbd5e1" font-size="10.5">• 도가니(SiO₂) 용출 산소 농도 제어 및 도펀트 균일도 사수</text>
            <text x="425" y="298" fill="#fbbf24" font-size="10" font-weight="700">➔ 0.3 Tesla 초전도 자기장 인가로 융액 거동 완벽 통제</text>

            <!-- Step Card 4: Slicing to Prime Wafer -->
            <rect x="410" y="325" width="340" height="75" rx="6" fill="rgba(139, 92, 246, 0.08)" stroke="#8b5cf6" stroke-width="1"/>
            <text x="425" y="347" fill="#a78bfa" font-size="12" font-weight="800">4. 후가공 (Slicing ➔ CMP ➔ Prime Wafer)</text>
            <text x="425" y="367" fill="#cbd5e1" font-size="10.5">• 다이아몬드 와이어 소 절단 ➔ 에지 모따기(Bevel) ➔ 양면 랩핑</text>
            <text x="425" y="385" fill="#e2e8f0" font-size="10.5">• 최종 CMP 경면 연마로 표면 거칠기 0.1nm 수준 거울 완성</text>
          </svg>
        </div>

        <h3>1. 초크랄스키(CZ: Czochralski) 공정의 4단계 성장 프로세스</h3>
        <ol style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>용융 및 시드 접촉 (Melting & Seeding)</strong>: 고순도 폴리실리콘(11N)을 석영 도가니에서 1420℃로 녹인 뒤, 원하는 결정 방향(&lt;100&gt; 등)의 종자 결정(Seed)을 융액 표면에 접촉시킵니다.</li>
          <li><strong>대시 네킹 (Dash Necking - 무전위화)</strong>: 열충격으로 발생한 전위 결함이 결정을 따라 내려오는 것을 막기 위해, 직경을 3~5mm로 가늘고 빠르게 인상하여 결함을 결정 밖으로 밀어내 소멸시킵니다.</li>
          <li><strong>숄더 및 직동 성장 (Shoulder & Body Growth)</strong>: 인상 속도를 줄여 목표 구경(300mm)으로 직경을 넓힌 후, 컴퓨터 비전으로 직경을 실시간 감시하며 길이 2m 이상의 원통형 잉곳을 만듭니다.</li>
          <li><strong>테일링 (Tailing / Crown Out)</strong>: 잉곳 분리 시 급격한 온도 변화로 전위가 역주입되는 것을 방지하기 위해 직경을 뾰족하게 줄여가며 융액에서 떼어냅니다.</li>
        </ol>

        <h3>2. 300mm 대구경화의 핵심 난제와 MCZ(Magnetic CZ) 기술</h3>
        <p>웨이퍼 구경이 200mm에서 300mm로 커지면서 융액량이 수백 kg으로 증가하여 극심한 열대류 난류가 발생합니다. 이로 인해 도가니(SiO₂)에서 녹아 나온 산소가 불균일하게 섞이고 도펀트 농도가 흔들리는 문제가 생깁니다. 이를 해결하기 위해 <strong>강력한 자기장(0.2~0.4 T)을 인가해 전도성 실리콘 융액의 대류를 물리적으로 묶어두는 MCZ 기술</strong>이 300mm 양산의 표준입니다.</p>
      </div>
    </section>


    <!-- Q 02 : 웨이퍼 제조 2) 기판 도핑 (P- / P+ / N- / N+) -->
    <section class="topic-section" id="q-02">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q 02</span>
          <h2 class="topic-title">웨이퍼 제조 2) 기판 도핑 (P- / P+ / N- / N+)</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">면접 대비 3~4줄 핵심 요약</span>
        <ul class="summary-list">
          <li><strong>"웨이퍼 기판 도핑은 잉곳 성장 시 융액에 3족(붕소: P형) 또는 5족(인/비소: N형) 불순물을 미량 첨가하여 기본 전기 전도 특성을 결정하는 작업입니다."</strong></li>
          <li><strong>"현대 고성능 CMOS는 전자의 이동도($\mu_n$)가 정공보다 3배 빨라 전체 회로 속도를 좌우하는 NMOS를 기판에 직접 형성하기 위해 'P- 기판'을 주류 표준으로 사용합니다."</strong></li>
          <li><strong>"첨단 미세 공정에서는 래치업(Latch-up)을 원천 차단하기 위해 고농도 P+ 기판 위에 고순도 저농도 P- 에피 실리콘을 얇게 올린 'P/P+ Epi 웨이퍼'를 채택합니다."</strong></li>
        </ul>
      </div>
      <div class="lecture-content">
        <!-- SVG 그래픽 다이어그램: P/P+ Epi 웨이퍼 및 도핑 스펙트럼 -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [웨이퍼 도핑 분류 & 구조] P/P+ 에피택셜 웨이퍼 (래치업 차단 + 소자 고성능화)
          </div>
          <svg viewBox="0 0 780 380" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <rect width="780" height="380" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

            <!-- Left: P/P+ Epi Wafer Structure -->
            <rect x="40" y="40" width="340" height="300" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
            <text x="60" y="70" fill="#38bdf8" font-size="13" font-weight="800">첨단 로직의 표준: P/P⁺ 에피 웨이퍼</text>

            <!-- Thin Epi Layer P- -->
            <rect x="60" y="90" width="300" height="50" rx="4" fill="rgba(56, 189, 248, 0.25)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="75" y="112" fill="#ffffff" font-size="12" font-weight="800">상부 P⁻ 에피층 (Epitaxial Layer, ~5μm)</text>
            <text x="75" y="128" fill="#bae6fd" font-size="10">저농도 (N_A ≈ 10¹⁵ cm⁻³) ➔ 접합용량 C_j 극소화 & 정밀 Vt</text>

            <!-- Bulk Substrate P+ -->
            <rect x="60" y="145" width="300" height="155" rx="4" fill="rgba(139, 92, 246, 0.25)" stroke="#8b5cf6" stroke-width="1.5"/>
            <text x="75" y="180" fill="#ffffff" font-size="13" font-weight="800">하부 P⁺ 고농도 기판 (Substrate, ~770μm)</text>
            <text x="75" y="202" fill="#ddd6fe" font-size="10.5">• 고농도 (N_A ≈ 10¹⁹ cm⁻³, 붕소 초과 도핑)</text>
            <text x="75" y="222" fill="#ddd6fe" font-size="10.5">• 기판 저항 R_sub ≈ 0 수준 극소화</text>
            <text x="75" y="245" fill="#f43f5e" font-size="11" font-weight="800">🛡️ 래치업(Latch-up) 완전 방어벽!</text>
            <text x="75" y="265" fill="#cbd5e1" font-size="10">기판 노이즈 전하 즉각 접지 배출</text>

            <!-- Right: 4 Wafer Types Matrix -->
            <rect x="410" y="40" width="330" height="300" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
            <text x="430" y="70" fill="#10b981" font-size="13" font-weight="800">기판 도핑 4대 분류 체계</text>

            <rect x="430" y="90" width="290" height="50" rx="6" fill="#1e293b" stroke="#38bdf8"/>
            <text x="445" y="110" fill="#38bdf8" font-size="11.5" font-weight="800">1. P⁻ 기판 (저농도, 1~100 Ω·cm)</text>
            <text x="445" y="128" fill="#cbd5e1" font-size="10">표준 CMOS 기판. NMOS를 기판에 바로 형성 (전자 이동도↑)</text>

            <rect x="430" y="148" width="290" height="50" rx="6" fill="#1e293b" stroke="#8b5cf6"/>
            <text x="445" y="168" fill="#a78bfa" font-size="11.5" font-weight="800">2. P⁺ 기판 (고농도, 0.001~0.01 Ω·cm)</text>
            <text x="445" y="186" fill="#cbd5e1" font-size="10">Epi 웨이퍼의 지지 기판. 래치업 방지 및 노이즈 차폐</text>

            <rect x="430" y="206" width="290" height="50" rx="6" fill="#1e293b" stroke="#10b981"/>
            <text x="445" y="226" fill="#34d399" font-size="11.5" font-weight="800">3. N⁻ 기판 (저농도)</text>
            <text x="445" y="244" fill="#cbd5e1" font-size="10">고전압 바이폴라, 파워 소자, 고감도 이미지센서(CIS)</text>

            <rect x="430" y="264" width="290" height="50" rx="6" fill="#1e293b" stroke="#f59e0b"/>
            <text x="445" y="284" fill="#fbbf24" font-size="11.5" font-weight="800">4. N⁺ 기판 (고농도)</text>
            <text x="445" y="302" fill="#cbd5e1" font-size="10">Power MOSFET 수직 전류 도통용 저저항 드레인 기판</text>
          </svg>
        </div>

        <h3>1. 왜 현대 표준 CMOS는 'P- 기판'을 주류로 쓸까?</h3>
        <p>실리콘에서 전자의 이동도($\mu_n \approx 1400\,\text{cm}^2/\text{V}\cdot\text{s}$)는 정공($\mu_p \approx 450$)보다 약 3배 빠릅니다. 따라서 트랜지스터의 구동 전류($I_{on}$)와 스위칭 속도는 NMOS가 지배합니다. P- 기판을 사용하면 고성능 NMOS를 기판에 바로 만들고, 상대적으로 느린 PMOS는 N-Well을 파서 형성하므로 공정이 단순해지고 전체 칩 동작 속도가 극대화됩니다.</p>

        <h3>2. 고농도 P+ 위에 저농도 P-를 올리는 'P/P+ Epi 웨이퍼'의 존재 이유</h3>
        <p>벌크 실리콘의 치명적인 고질병은 NMOS와 PMOS 사이의 기생 BJT가 턴온되어 칩이 타버리는 <strong>래치업(Latch-up)</strong>입니다. 하부에 고농도 $P^+$ 기판을 깔아두면 기판 저항($R_{sub}$)이 거의 0으로 떨어져 기생 트랜지스터의 베이스-에미터 전압이 걸리지 않아 래치업이 완벽히 차단됩니다. 동시에 상부에는 깨끗한 저농도 $P^-$ 에피층을 형성하여 소자의 정전용량($C_j$)을 낮추고 항복 전압을 확보합니다.</p>
      </div>
    </section>


    <!-- Q 03 : 웨이퍼 제조 3) 도핑 농도와 면저항의 관계 -->
    <section class="topic-section" id="q-03">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q 03</span>
          <h2 class="topic-title">웨이퍼 제조 3) 도핑 농도와 면저항의 관계</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">면접 대비 3~4줄 핵심 요약</span>
        <ul class="summary-list">
          <li><strong>"면저항($R_s = \frac{\rho}{t} = \frac{1}{q N \mu t}$)은 도핑 농도($N$)가 증가할수록 캐리어 밀도가 늘어나 기본적으로 반비례하며 급격히 감소합니다."</strong></li>
          <li><strong>"그러나 고농도 영역($N > 10^{18}\,\text{cm}^{-3}$)에서는 이온화 불순물 산란(Ionized Impurity Scattering)으로 이동도($\mu$)가 저하되어 저항 감소율이 점차 둔화되는 비선형성을 보입니다."</strong></li>
          <li><strong>"단채널 효과를 막기 위해 접합 깊이($X_j$)를 극도로 얕게 만드는 초미세 공정에서는 두께($t$) 감소로 인해 면저항($R_s$)이 폭증하므로, 이를 보상하기 위해 살리사이드(Salicide) 및 Raised S/D 기술을 적용합니다."</strong></li>
        </ul>
      </div>
      <div class="lecture-content">
        <!-- SVG 그래픽 다이어그램: 도핑 농도 vs 비저항/면저항 및 4-Point Probe -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [도핑 농도와 면저항 역학] Irvin 커브 비선형성 & 4-Point Probe 측정 원리
          </div>
          <svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

            <!-- Left: Resistivity vs Doping Concentration Graph -->
            <rect x="40" y="30" width="340" height="300" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
            <text x="55" y="55" fill="#38bdf8" font-size="12" font-weight="800">비저항(ρ) vs 도핑 농도(N) (Irvin 커브)</text>

            <!-- Graph axes -->
            <line x1="75" y1="280" x2="350" y2="280" stroke="#475569" stroke-width="1.5"/>
            <line x1="75" y1="280" x2="75" y2="75" stroke="#475569" stroke-width="1.5"/>
            <text x="75" y="70" fill="#94a3b8" font-size="10">비저항 ρ (Ω·cm) ▲</text>
            <text x="250" y="298" fill="#94a3b8" font-size="10">도핑 농도 N (cm⁻³) ►</text>

            <!-- Inverse curve -->
            <path d="M 85 90 Q 130 230 340 270" fill="none" stroke="#f43f5e" stroke-width="3"/>
            <text x="145" y="145" fill="#f43f5e" font-size="11" font-weight="800">ρ ∝ 1 / (q · N · μ)</text>

            <!-- Mobility scattering note -->
            <rect x="180" y="170" width="180" height="65" rx="5" fill="rgba(244, 63, 94, 0.15)" stroke="#f43f5e"/>
            <text x="190" y="190" fill="#fca5a5" font-size="10" font-weight="700">⚠️ 고농도 이동도 저하:</text>
            <text x="190" y="208" fill="#cbd5e1" font-size="9.5">이온화 불순물 산란으로</text>
            <text x="190" y="222" fill="#cbd5e1" font-size="9.5">저항 감소 기울기 완만해짐</text>


            <!-- Right: 4-Point Probe & Sheet Resistance Formula -->
            <rect x="400" y="30" width="345" height="300" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
            <text x="415" y="55" fill="#10b981" font-size="12" font-weight="800">면저항(R_s) 정의 & 4-Point Probe 측정</text>

            <!-- Formula box -->
            <rect x="415" y="75" width="315" height="60" rx="6" fill="#1e293b" stroke="#10b981"/>
            <text x="430" y="100" fill="#34d399" font-size="13" font-weight="900">R_s = ρ / t = 1 / (q · N · μ · t)  [Ω/sq]</text>
            <text x="430" y="122" fill="#cbd5e1" font-size="10">단위: 오옴 퍼 스퀘어 (정사각형 면적당 저항)</text>

            <!-- 4-Point Probe Diagram -->
            <rect x="415" y="150" width="315" height="165" rx="6" fill="rgba(16, 185, 129, 0.08)" stroke="#334155"/>
            <text x="430" y="172" fill="#38bdf8" font-size="11" font-weight="700">4탐침법 (접촉 저항 배제 정밀 측정)</text>

            <!-- 4 probes -->
            <line x1="470" y1="185" x2="470" y2="235" stroke="#94a3b8" stroke-width="3"/>
            <line x1="520" y1="185" x2="520" y2="235" stroke="#f59e0b" stroke-width="3"/>
            <line x1="570" y1="185" x2="570" y2="235" stroke="#f59e0b" stroke-width="3"/>
            <line x1="620" y1="185" x2="620" y2="235" stroke="#94a3b8" stroke-width="3"/>

            <!-- Current outer loop -->
            <path d="M 470 185 Q 545 150 620 185" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3 3"/>
            <text x="525" y="165" fill="#94a3b8" font-size="10">전류 I 공급</text>

            <!-- Voltage inner meter -->
            <path d="M 520 185 Q 545 170 570 185" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="535" y="180" fill="#f59e0b" font-size="10">전압 V 측정</text>

            <!-- Wafer sample -->
            <rect x="445" y="235" width="255" height="25" fill="#334155" stroke="#64748b"/>
            <text x="530" y="252" fill="#ffffff" font-size="10.5" font-weight="700">웨이퍼 박막 (두께 t)</text>

            <text x="430" y="285" fill="#10b981" font-size="11" font-weight="800">R_s = (π / ln 2) · (V / I) ≈ 4.532 · (V / I)</text>
            <text x="430" y="303" fill="#cbd5e1" font-size="9.5">외곽에서 전류(I)를 흘리고 안쪽에서 전압(V)만 측정</text>
          </svg>
        </div>

        <h3>1. 도핑 농도($N$)와 비저항($\rho$), 면저항($R_s$)의 수학적 관계</h3>
        <p>반도체 재료의 고유 비저항($\rho$)은 캐리어 농도($n, p$)와 전하량($q$), 이동도($\mu$)의 곱에 반비례합니다:</p>
        <div class="formula-box">
          $$\rho = \frac{1}{\sigma} = \frac{1}{q(n\mu_n + p\mu_p)} \approx \frac{1}{q \cdot N \cdot \mu(N)}$$
        </div>
        <p>웨이퍼 표면이나 박막처럼 두께($t$) 또는 접합 깊이($X_j$)가 정해진 2차원 층에서는 면저항($R_s$, Sheet Resistance)을 사용합니다:</p>
        <div class="formula-box">
          $$R = \rho \frac{L}{W \cdot t} = \left(\frac{\rho}{t}\right) \frac{L}{W} = \mathbf{R_s} \left(\frac{L}{W}\right) \implies \mathbf{R_s = \frac{\rho}{t} = \frac{1}{q \cdot N \cdot \mu \cdot t} \quad [\Omega/\text{sq}]}$$
        </div>

        <h3>2. 고농도 영역에서의 비선형성 (이온화 불순물 산란)</h3>
        <p>도핑 농도($N$)를 10배 올린다고 해서 면저항이 정확히 1/10로 떨어지지 않습니다. $N > 10^{18}\,\text{cm}^{-3}$ 이상에서는 전자가 격자 속을 이동할 때 수많은 이온화 도펀트들과 부딪히는 <strong>이온화 불순물 산란(Ionized Impurity Scattering)</strong>이 극심해져 이동도($\mu$)가 급감하기 때문입니다. 따라서 고농도로 갈수록 저항 감소율이 완만해집니다.</p>

        <h3>3. 초미세 접합에서의 면저항 폭증 난제와 살리사이드(Salicide)</h3>
        <p>단채널 효과를 막기 위해 S/D 접합 깊이($X_j$)를 수십 나노미터로 극도로 얕게(Ultra-Shallow Junction) 만들면, 분모의 두께($t$)가 너무 얇아져 **면저항($R_s$)과 기생 직렬 저항이 폭증**하여 구동 전류가 깎입니다. 이를 해결하기 위해 소스/드레인 표면에 전도성이 극히 뛰어난 전이금속 실리사이드(CoSi₂, NiSi 등)를 형성하는 <strong>살리사이드(Salicide)</strong> 기술과 위로 덧살을 올리는 <strong>Raised S/D</strong> 기술을 필수 적용합니다.</p>
      </div>
    </section>


    <!-- Q 04 : 웨이퍼 제조 4) 웨이퍼 결정 단면에 따른 특성 변화 -->
    <section class="topic-section" id="q-04">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q 04</span>
          <h2 class="topic-title">웨이퍼 제조 4) 웨이퍼 결정 단면에 따른 특성 변화</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">면접 대비 3~4줄 핵심 요약</span>
        <ul class="summary-list">
          <li><strong>"실리콘 단결정의 밀러 지수(&lt;100&gt;, &lt;110&gt;, &lt;111&gt;)에 따라 원자 표면 밀도와 댕글링 본드(Dangling Bond) 수가 달라져 산화막 품질, 캐리어 이동도, 습식 식각 속도가 완전히 달라집니다."</strong></li>
          <li><strong>"전자 이동도($\mu_n$)는 원자 밀도가 낮고 계면 트랩($D_{it}$)이 가장 적은 (100) 면에서 최대이므로 평면 CMOS 웨이퍼의 표준으로 사용됩니다."</strong></li>
          <li><strong>"반면 정공 이동도($\mu_p$)는 (110) 면에서 (100)보다 2배 이상 빠르므로, 3차원 FinFET에서는 핀의 양 측벽을 (110) 면으로 정렬하여 취약했던 PMOS 성능을 극대화합니다."</strong></li>
        </ul>
      </div>
      <div class="lecture-content">
        <!-- SVG 그래픽 다이어그램: 결정면별 원자 밀도, 이동도, FinFET 적용 -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [실리콘 결정면 비교] (100) vs (110) vs (111) 특성 차이 및 3D FinFET 측벽 활용
          </div>
          <svg viewBox="0 0 780 390" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <rect width="780" height="390" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

            <!-- 3 Columns for 3 Crystal Planes -->
            <!-- Plane (100) -->
            <rect x="30" y="30" width="225" height="210" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5"/>
            <rect x="30" y="30" width="225" height="32" rx="6" fill="#0284c7"/>
            <text x="75" y="52" fill="#ffffff" font-size="13" font-weight="900">실리콘 (100) 면</text>
            <text x="45" y="80" fill="#cbd5e1" font-size="11">• 원자 밀도: 6.78 × 10¹⁴ (최저)</text>
            <text x="45" y="100" fill="#cbd5e1" font-size="11">• 댕글링 본드: 가장 적음</text>
            <text x="45" y="120" fill="#38bdf8" font-size="11" font-weight="700">• 계면 트랩 Dit: 극소 (최우수!)</text>
            <text x="45" y="142" fill="#34d399" font-size="11.5" font-weight="800">⚡ 전자 이동도(μ_n): 최대!</text>
            <text x="45" y="162" fill="#f87171" font-size="10.5">• 정공 이동도(μ_p): 낮음</text>
            <text x="45" y="185" fill="#fcd34d" font-size="11" font-weight="800">📌 평면 CMOS 표준 웨이퍼</text>
            <text x="45" y="202" fill="#94a3b8" font-size="9.5">산화막 품질 우수, 노이즈 극소</text>

            <!-- Plane (110) -->
            <rect x="275" y="30" width="230" height="210" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
            <rect x="275" y="30" width="230" height="32" rx="6" fill="#059669"/>
            <text x="320" y="52" fill="#ffffff" font-size="13" font-weight="900">실리콘 (110) 면</text>
            <text x="290" y="80" fill="#cbd5e1" font-size="11">• 원자 밀도: 9.60 × 10¹⁴ (중간)</text>
            <text x="290" y="100" fill="#cbd5e1" font-size="11">• 댕글링 본드: 중간 수준</text>
            <text x="290" y="120" fill="#cbd5e1" font-size="11">• 계면 트랩 Dit: 중간</text>
            <text x="290" y="142" fill="#94a3b8" font-size="10.5">• 전자 이동도(μ_n): 중간</text>
            <text x="290" y="162" fill="#34d399" font-size="11.5" font-weight="800">⚡ 정공 이동도(μ_p): 압도적 1위!</text>
            <text x="290" y="185" fill="#38bdf8" font-size="11" font-weight="800">📌 FinFET 핀 측벽(Sidewall)</text>
            <text x="290" y="202" fill="#94a3b8" font-size="9.5">취약한 PMOS 성능 2배 급상승!</text>

            <!-- Plane (111) -->
            <rect x="525" y="30" width="225" height="210" rx="6" fill="#0f172a" stroke="#8b5cf6" stroke-width="1.5"/>
            <rect x="525" y="30" width="225" height="32" rx="6" fill="#7c3aed"/>
            <text x="570" y="52" fill="#ffffff" font-size="13" font-weight="900">실리콘 (111) 면</text>
            <text x="540" y="80" fill="#cbd5e1" font-size="11">• 원자 밀도: 15.7 × 10¹⁴ (최고)</text>
            <text x="540" y="100" fill="#cbd5e1" font-size="11">• 댕글링 본드: 가장 많음</text>
            <text x="540" y="120" fill="#f87171" font-size="11">• 계면 트랩 Dit: 가장 높음 (나쁨)</text>
            <text x="540" y="142" fill="#94a3b8" font-size="10.5">• 캐리어 이동도: 상대적 열세</text>
            <text x="540" y="165" fill="#f59e0b" font-size="11.5" font-weight="800">⚡ 습식 식각 속도 100배 느림!</text>
            <text x="540" y="185" fill="#a78bfa" font-size="11" font-weight="800">📌 MEMS 비등방성 에칭</text>
            <text x="540" y="202" fill="#94a3b8" font-size="9.5">KOH 식각 저지면, 태양전지 피라미드</text>


            <!-- Bottom: 3D FinFET Crystal Engineering Spotlight -->
            <rect x="30" y="255" width="720" height="115" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#334155" stroke-width="1.2"/>
            <text x="45" y="280" fill="#38bdf8" font-size="12.5" font-weight="800">💡 3차원 FinFET 시대의 결정 단면 공학 (Crystal Engineering):</text>
            
            <text x="45" y="304" fill="#cbd5e1" font-size="11">• 평면 구조는 바닥면 (100) 하나만 쓰므로 PMOS가 NMOS보다 전류가 1/3로 약해 사이즈를 2배 이상 키워야 했음</text>
            <text x="45" y="325" fill="#cbd5e1" font-size="11">• 3D FinFET은 핀을 깎아 세우면서 <strong>상단면은 (100)</strong>, <strong>수직 측벽 2개 면은 (110)</strong>이 됨</text>
            <text x="45" y="347" fill="#10b981" font-size="11.5" font-weight="800">➔ 측벽 (110) 면에서 정공 이동도가 2배 폭증하여, 별도 면적 증가 없이도 PMOS 구동력이 NMOS에 맞먹게 대폭 개선됨!</text>
          </svg>
        </div>

        <h3>1. 결정 방향에 따른 3대 물리 특성 비교</h3>
        <table class="data-table">
          <thead>
            <tr>
              <th>결정면</th>
              <th>원자 표면 밀도</th>
              <th>계면 산화막 트랩 ($D_{it}$)</th>
              <th>전자 이동도 ($\mu_n$)</th>
              <th>정공 이동도 ($\mu_p$)</th>
              <th>주요 적용 분야</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>(100)</strong></td>
              <td>$6.78 \times 10^{14}\,\text{cm}^{-2}$ (최저)</td>
              <td><strong>가장 적음 (최우수)</strong></td>
              <td><strong>최고 (1위)</strong></td>
              <td>낮음</td>
              <td><strong>표준 평면 CMOS 웨이퍼</strong> (MOSFET 표준)</td>
            </tr>
            <tr>
              <td><strong>(110)</strong></td>
              <td>$9.60 \times 10^{14}\,\text{cm}^{-2}$ (중간)</td>
              <td>중간</td>
              <td>중간</td>
              <td><strong>압도적 최고 (1위)</strong></td>
              <td><strong>FinFET / GAA 핀 측벽</strong> (PMOS 성능 극대화)</td>
            </tr>
            <tr>
              <td><strong>(111)</strong></td>
              <td>$15.7 \times 10^{14}\,\text{cm}^{-2}$ (최고)</td>
              <td>가장 많음 (불리)</td>
              <td>낮음</td>
              <td>중간</td>
              <td>바이폴라 소자, <strong>MEMS 비등방 식각 저지면</strong></td>
            </tr>
          </tbody>
        </table>

        <h3>2. 3D FinFET에서 결정 방향(110)이 일으킨 기적</h3>
        <p>전통적인 평면 트랜지스터에서는 PMOS의 정공 이동도가 NMOS 전자의 1/3에 불과하여, 동일한 온전류를 맞추기 위해 PMOS 게이트 폭($W$)을 2~3배 넓혀야만 했습니다. 그러나 <strong>3차원 FinFET 구조</strong>에서는 핀(Fin)의 높이($H_{fin}$)가 높아지면서 채널 면적의 80% 이상이 <strong>핀의 양 측벽(Sidewall)</strong>에 형성됩니다.</p>
        <p>이 측벽이 바로 <strong>정공 이동도가 2배 이상 빠른 (110) 결정면</strong>입니다! 그 결과 FinFET에서는 별도의 레이아웃 면적 낭비 없이도 PMOS의 구동 능력이 비약적으로 상승하여 고속 저전력 동작의 결정적 발판이 되었습니다.</p>
      </div>
    </section>
"""

    # 3. Renumber existing nav-items (01 -> 05, ..., 30 -> 34)
    nav_pattern = r'(<ul class="nav-list" id="navList">)([\s\S]*?)(</ul>)'
    match = re.search(nav_pattern, html)
    if match:
        old_nav_items = match.group(2)
        shifted_nav = old_nav_items
        for i in range(30, 0, -1):
            old_str = f'<span class="nav-num">{i:02d}</span>'
            new_str = f'<span class="nav-num">{i+4:02d}</span>'
            shifted_nav = shifted_nav.replace(old_str, new_str)
            old_href = f'href="#q-{i:02d}"'
            new_href = f'href="#q-{i+4:02d}"'
            shifted_nav = shifted_nav.replace(old_href, new_href)
        
        updated_nav_list = match.group(1) + "\n" + new_nav_items + shifted_nav + match.group(3)
        html = html[:match.start()] + updated_nav_list + html[match.end():]

    # 4. Renumber existing sections (q-01 -> q-05, ..., q-30 -> q-34)
    for i in range(30, 0, -1):
        old_id = f'id="q-{i:02d}"'
        new_id = f'id="q-{i+4:02d}"'
        html = html.replace(old_id, new_id)
        
        old_badge = f'<span class="topic-badge">Q {i:02d}</span>'
        new_badge = f'<span class="topic-badge">Q {i+4:02d}</span>'
        html = html.replace(old_badge, new_badge)

    # 5. Remove latest-card-highlight and latest-tag from old Q01 (now Q05)
    html = html.replace('<section class="topic-section latest-card-highlight" id="q-05">', '<section class="topic-section" id="q-05">')
    html = html.replace("""          <span class="topic-badge">Q 05</span>\n          <span class="latest-tag">⭐ 가장 최근 질문 (1번 배치)</span>""", """          <span class="topic-badge">Q 05</span>""")

    # 6. Update main header description
    html = re.sub(
        r'<p class="main-desc">[\s\S]*?</p>',
        r"""<p class="main-desc">질문자님께서 질문하신 문장 그대로 좌측 탭 제목과 본문 제목을 구성하였습니다. 최상단에는 가장 최근 질문인 <strong>'웨이퍼 제조 4대 핵심 주제 (초크랄스키, 기판 도핑, 면저항, 결정 단면)'</strong>가 1~4번으로 위치합니다.</p>""",
        html,
        count=1
    )

    # 7. Insert new sections right after header.main-header
    header_end_tag = '</header>'
    idx = html.find(header_end_tag)
    if idx != -1:
        insert_pos = idx + len(header_end_tag)
        html = html[:insert_pos] + "\n\n" + new_sections + html[insert_pos:]

    # 8. Write to result
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

    # 9. Copy to root
    root_path = r"C:\Work\반도체3\index.html"
    with open(root_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Successfully updated {root_path}")

if __name__ == "__main__":
    update_html()
