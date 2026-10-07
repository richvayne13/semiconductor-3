import os
import re

def update_html():
    file_path = r"C:\Work\반도체3\result\261007_v1.0\index.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. New Q01 nav-item
    new_nav_item = """      <li class="nav-item"><a href="#q-01" class="nav-link"><span class="nav-num">01</span><span class="nav-text">halo implant가 punchthrough 개선하는 메커니즘</span></a></li>\n"""

    # 2. New Q01 Section with SVG
    new_q01_section = """    <!-- Q 01 : halo implant가 punchthrough 개선하는 메커니즘 -->
    <section class="topic-section latest-card-highlight" id="q-01">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q 01</span>
          <span class="latest-tag">⭐ 가장 최근 질문 (1번 배치)</span>
          <h2 class="topic-title">halo implant가 punchthrough 개선하는 메커니즘</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">면접 대비 3~4줄 핵심 요약</span>
        <ul class="summary-list">
          <li><strong>"헤일로 이온 주입(Halo / Pocket Implant)은 소스/드레인 접합부 하단 및 코너 기판 영역에 웰과 동일한 타입의 고농도 불순물($P^+$)을 국소적으로 주입하는 공정입니다."</strong></li>
          <li><strong>"공핍층 폭 공식($W_{dep} \propto 1/\\sqrt{N_A}$)에 따라 국소 도핑 농도($N_A$)가 대폭 증가하면서, 드레인 고전압 인가 시 기판 지하 벌크로 확장되는 공핍층 폭을 물리적으로 강력하게 압축·차단합니다."</strong></li>
          <li><strong>"이로 인해 소스와 드레인 공핍층이 기판 지하에서 서로 맞닿아 전위 장벽이 붕괴되는 '공핍층 결합(Merge)'을 원천 봉쇄하여, 게이트 통제를 벗어난 대량 지하 누설 전류인 펀치스루(Punchthrough)를 완벽히 억제합니다."</strong></li>
        </ul>
      </div>
      <div class="lecture-content">
        <!-- SVG 그래픽 다이어그램: Halo Implant의 펀치스루 차단 메커니즘 -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [소자 단면 비교] Halo 미적용(공핍층 결합 펀치스루 폭주) vs Halo 적용(공핍층 압축 및 장벽 수호)
          </div>
          <svg viewBox="0 0 780 410" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <defs>
              <!-- Gradient definitions -->
              <linearGradient id="depNoHaloGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="rgba(239, 68, 68, 0.25)"/>
                <stop offset="50%" stop-color="rgba(239, 68, 68, 0.45)"/>
                <stop offset="100%" stop-color="rgba(239, 68, 68, 0.25)"/>
              </linearGradient>
              <linearGradient id="depHaloGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="rgba(14, 165, 233, 0.2)"/>
                <stop offset="100%" stop-color="rgba(14, 165, 233, 0.05)"/>
              </linearGradient>
              <linearGradient id="haloPocketGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#8b5cf6"/>
                <stop offset="100%" stop-color="#6366f1"/>
              </linearGradient>
            </defs>

            <!-- Base Canvas -->
            <rect width="780" height="410" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

            <!-- Divider Line -->
            <line x1="390" y1="20" x2="390" y2="390" stroke="#334155" stroke-dasharray="4 4" stroke-width="1.5"/>

            <!-- ================= LEFT: WITHOUT HALO ================= -->
            <text x="30" y="38" fill="#f43f5e" font-size="13" font-weight="800">❌ [1] Halo 미적용 (저농도 기판 P-Sub, N_A 낮음)</text>
            
            <!-- Silicon Substrate Left -->
            <rect x="25" y="55" width="340" height="230" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
            <text x="35" y="270" fill="#64748b" font-size="11" font-weight="600">P-기판 (저농도 N_A)</text>

            <!-- Source N+ (Left) -->
            <rect x="25" y="55" width="70" height="55" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.2"/>
            <text x="42" y="88" fill="#38bdf8" font-size="11.5" font-weight="700">Source</text>
            <text x="45" y="102" fill="#94a3b8" font-size="9">(N⁺)</text>

            <!-- Drain N+ (Left) -->
            <rect x="295" y="55" width="70" height="55" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.2"/>
            <text x="314" y="88" fill="#38bdf8" font-size="11.5" font-weight="700">Drain</text>
            <text x="313" y="102" fill="#f43f5e" font-size="9">(V_D=High)</text>

            <!-- Gate Left -->
            <rect x="130" y="35" width="130" height="20" fill="#334155" stroke="#94a3b8" stroke-width="1"/>
            <rect x="130" y="51" width="130" height="4" fill="#38bdf8"/>
            <text x="175" y="49" fill="#f8fafc" font-size="11" font-weight="700">Gate</text>

            <!-- Merged Depletion Region (Left) -->
            <path d="M 95 110 Q 195 200 295 110 L 295 55 L 365 55 L 365 140 Q 200 240 25 140 L 25 55 L 95 55 Z" fill="url(#depNoHaloGrad)" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3 3"/>
            <text x="120" y="145" fill="#f43f5e" font-size="11" font-weight="800">공핍층 결합 발생! (Merge)</text>

            <!-- Punchthrough Leakage Current Path (Left) -->
            <path d="M 75 110 Q 195 175 315 110" fill="none" stroke="#f43f5e" stroke-width="3"/>
            <polygon points="315,110 302,104 306,113" fill="#f43f5e"/>
            <text x="110" y="195" fill="#fecaca" font-size="11" font-weight="800">⚡ 지하 펀치스루 누설 전류 (I_PT)</text>
            <text x="105" y="210" fill="#f87171" font-size="10">게이트 통제 불능! (장벽 붕괴)</text>

            <!-- Explanation Box Left -->
            <rect x="25" y="295" width="340" height="95" rx="6" fill="rgba(244, 63, 94, 0.08)" stroke="#f43f5e" stroke-width="1"/>
            <text x="35" y="316" fill="#f43f5e" font-size="11" font-weight="700">⚠️ 문제 메커니즘:</text>
            <text x="35" y="334" fill="#cbd5e1" font-size="10.5">• 기판 농도(N_A)가 낮아 드레인 공핍층이 지하로 길게 확장</text>
            <text x="35" y="352" fill="#cbd5e1" font-size="10.5">• 소스-드레인 공핍층 결합으로 지하 전위 장벽 소멸</text>
            <text x="35" y="370" fill="#f87171" font-size="10.5">• 게이트가 꺼져도 지하로 전자가 쏟아져 대량 오프 누설 발생</text>


            <!-- ================= RIGHT: WITH HALO IMPLANT ================= -->
            <text x="415" y="38" fill="#10b981" font-size="13" font-weight="800">✅ [2] Halo(Pocket) 적용 (국소 고농도 P⁺ 주머니 방어벽)</text>
            
            <!-- Silicon Substrate Right -->
            <rect x="415" y="55" width="340" height="230" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
            <text x="425" y="270" fill="#64748b" font-size="11" font-weight="600">P-기판 (저농도 N_A)</text>

            <!-- Source N+ (Right) -->
            <rect x="415" y="55" width="70" height="55" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.2"/>
            <text x="432" y="88" fill="#38bdf8" font-size="11.5" font-weight="700">Source</text>
            <text x="435" y="102" fill="#94a3b8" font-size="9">(N⁺)</text>

            <!-- Drain N+ (Right) -->
            <rect x="685" y="55" width="70" height="55" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.2"/>
            <text x="704" y="88" fill="#38bdf8" font-size="11.5" font-weight="700">Drain</text>
            <text x="703" y="102" fill="#f43f5e" font-size="9">(V_D=High)</text>

            <!-- Gate Right -->
            <rect x="520" y="35" width="130" height="20" fill="#334155" stroke="#94a3b8" stroke-width="1"/>
            <rect x="520" y="51" width="130" height="4" fill="#38bdf8"/>
            <text x="565" y="49" fill="#f8fafc" font-size="11" font-weight="700">Gate</text>

            <!-- Halo Pockets (Purple/Violet) -->
            <!-- Source side Halo -->
            <path d="M 470 110 Q 500 135 505 85 L 485 55 L 485 110 Z" fill="url(#haloPocketGrad)" stroke="#a78bfa" stroke-width="1.5"/>
            <!-- Drain side Halo -->
            <path d="M 695 110 Q 665 135 660 85 L 685 55 L 685 110 Z" fill="url(#haloPocketGrad)" stroke="#a78bfa" stroke-width="1.5"/>
            <text x="635" y="145" fill="#a78bfa" font-size="10.5" font-weight="700">Halo (P⁺)</text>
            <text x="465" y="145" fill="#a78bfa" font-size="10.5" font-weight="700">Halo (P⁺)</text>

            <!-- Narrow Depletion Regions (Right) -->
            <path d="M 485 55 Q 515 115 485 125 L 415 125 L 415 55 Z" fill="url(#depHaloGrad)" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="2 2"/>
            <path d="M 685 55 Q 645 115 685 130 L 755 130 L 755 55 Z" fill="url(#depHaloGrad)" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="2 2"/>

            <!-- Robust Barrier Zone -->
            <rect x="525" y="105" width="120" height="50" rx="6" fill="rgba(16, 185, 129, 0.12)" stroke="#10b981" stroke-width="1.2"/>
            <text x="545" y="125" fill="#34d399" font-size="11" font-weight="800">🛡️ 견고한 장벽 유지</text>
            <text x="535" y="143" fill="#cbd5e1" font-size="9.5">공핍층 결합 완벽 차단! (I_PT=0)</text>

            <!-- Explanation Box Right -->
            <rect x="415" y="295" width="340" height="95" rx="6" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1"/>
            <text x="425" y="316" fill="#10b981" font-size="11" font-weight="700">💡 차단 메커니즘 (해결책):</text>
            <text x="425" y="334" fill="#cbd5e1" font-size="10.5">• 접합 코너에 국소 고농도 P⁺ 포켓 형성 (W_dep ∝ 1/√N_A)</text>
            <text x="425" y="352" fill="#cbd5e1" font-size="10.5">• 드레인 공핍층 확장을 1/5 수준으로 강력 압축하여 격리</text>
            <text x="425" y="370" fill="#34d399" font-size="10.5">• 지하 전위 장벽을 사수하여 펀치스루 원천 봉쇄!</text>
          </svg>
        </div>

        <h3>1. 펀치스루(Punchthrough)의 근본 원인과 지하 누설 경로</h3>
        <p>채널 길이가 서브 미크론(Sub-micron) 이하로 짧아질 때, 드레인 전압($V_D$)을 높이면 드레인 접합부에서 기판 벌크 방향으로 확장되는 <strong>역방향 바이어스 공핍층</strong>이 기판 지하 깊은 곳을 통해 소스 접합부 공핍층과 물리적으로 맞닿게 됩니다(<strong>Depletion Region Merge</strong>).</p>
        <p>공핍층이 결합하는 순간, 소스-기판 접합부에 형성되어 전자의 이동을 가로막고 있던 <strong>내장 전위 장벽(Built-in Potential Barrier)이 지하에서 완전히 붕괴</strong>합니다. 표면 채널은 게이트 전압($V_G$)으로 끌 수 있지만, 게이트 정전기 통제력이 미치지 못하는 깊은 지하 벌크를 통해 소스의 전자가 드레인으로 제어 불능 상태로 쏟아져 들어가는 현상이 바로 <strong>펀치스루(Punchthrough)</strong>입니다.</p>

        <h3>2. 헤일로(Pocket) 도핑에 의한 공핍층 폭 압축 공식</h3>
        <p>p-n 접합부에서 역방향 전압 인가 시 기판 쪽으로 침투하는 공핍층의 폭($W_{dep}$)은 기판의 도핑 농도($N_A$)에 반비례합니다:</p>
        <div class="formula-box">
          $$W_{dep} = \sqrt{\frac{2\epsilon_{si}(V_{bi} + V_R)}{q \cdot \mathbf{N_A}}} \quad \propto \quad \frac{1}{\sqrt{\mathbf{N_A}}}$$
        </div>
        <p>기판 전체가 저농도($N_A \approx 10^{15}\,\text{cm}^{-3}$)일 때는 $W_{dep}$가 매우 길어져 드레인 공핍층이 쉽게 소스까지 닿습니다. 그러나 소스/드레인 접합 하단 및 코너에 <strong>헤일로 이온 주입($P^+$ Pocket, $N_A \approx 10^{18}\,\text{cm}^{-3}$)</strong>을 적용하면:</p>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li>국소 영역의 <strong>$N_A$가 100~1,000배 증가</strong>합니다.</li>
          <li>공핍층 폭($W_{dep}$)은 <strong>$1/\sqrt{1000} \approx 1/30$ 수준으로 극단적으로 얇게 압축</strong>됩니다.</li>
          <li>드레인에 고전압이 걸려도 공핍층이 헤일로 주머니 바깥으로 뻗어나가지 못하고 갇히므로, <strong>소스 공핍층과의 결합이 물리적으로 완벽히 차단</strong>됩니다.</li>
        </ul>

        <h3>3. 전면 고농도 도핑 대비 '국소 헤일로(Pocket)'만의 결정적 강점</h3>
        <p>펀치스루를 막기 위해 기판 전체(Well 전체)의 도핑 농도를 균일하게 높이면 심각한 부작용이 발생합니다:</p>
        <div class="formula-box">
          $$\mu = \frac{\mu_0}{1 + (N_A / N_{ref})^\alpha} \quad (\text{이온화 불순물 산란}), \quad V_{th} = V_{FB} + 2\phi_F + \frac{\sqrt{2q\epsilon N_A (2\phi_F)}}{C_{ox}}$$
        </div>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>이동도 저하 방지</strong>: 채널 표면 전체의 농도를 높이면 이온화 불순물 산란(Ionized Impurity Scattering)에 의해 전자 이동도($\mu$)와 온전류($I_{on}$)가 급감합니다. 헤일로는 접합부 코너에만 국소적으로 치고 빠지므로 채널 중심부의 표면 이동도를 온전히 보존합니다.</li>
          <li><strong>문턱전압($V_{th}$) 급상승 억제</strong>: 전체 기판 도핑 시 $V_{th}$가 과도하게 치솟는 문제를 방지합니다.</li>
          <li><strong>접합 정전용량($C_j$) 최소화</strong>: S/D 바닥면 전체가 아닌 코너 측면에만 한정 형성하므로 바닥면 기생 접합 커패시턴스 증가를 최소화하여 동작 속도(RC Delay)를 확보합니다.</li>
        </ul>

        <h3>4. 실제 반도체 양산 공정과 수반 현상 (RSCE)</h3>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>경사 회전 이온 주입 (Quad-Tilt Implant)</strong>: 게이트 패턴 형성 후, 게이트 밑바닥 코너와 LDD 하부로 도펀트가 파고들 수 있도록 웨이퍼를 20°~45° 기울이고 4방향 90°씩 회전(Quad-rotation)시키며 이온을 주입합니다. (NMOS: $B^+$, $BF_2^+$, $In^+$ / PMOS: $As^+$, $P^+$)</li>
          <li><strong>역 단채널 효과 (RSCE, Reverse Short Channel Effect)</strong>: 채널 길이가 줄어들 때, 소스 측 헤일로와 드레인 측 헤일로가 서로 가까워져 채널 중심부까지 유효 도핑 농도가 높아지면서 <strong>단채널에서 일시적으로 $V_{th}$가 오히려 증가하는 현상</strong>이 발생합니다. 이는 단채널의 $V_{th}$ 롤오프를 보상하는 훌륭한 안전판 역할을 합니다.</li>
        </ul>
      </div>
    </section>
"""

    # 3. Renumber existing nav-items (01 -> 02, ..., 23 -> 24)
    nav_pattern = r'(<ul class="nav-list" id="navList">)([\s\S]*?)(</ul>)'
    match = re.search(nav_pattern, html)
    if match:
        old_nav_items = match.group(2)
        shifted_nav = old_nav_items
        for i in range(23, 0, -1):
            old_str = f'<span class="nav-num">{i:02d}</span>'
            new_str = f'<span class="nav-num">{i+1:02d}</span>'
            shifted_nav = shifted_nav.replace(old_str, new_str)
            old_href = f'href="#q-{i:02d}"'
            new_href = f'href="#q-{i+1:02d}"'
            shifted_nav = shifted_nav.replace(old_href, new_href)
        
        updated_nav_list = match.group(1) + "\n" + new_nav_item + shifted_nav + match.group(3)
        html = html[:match.start()] + updated_nav_list + html[match.end():]

    # 4. Renumber existing sections (q-01 -> q-02, ..., q-23 -> q-24)
    for i in range(23, 0, -1):
        old_id = f'id="q-{i:02d}"'
        new_id = f'id="q-{i+1:02d}"'
        html = html.replace(old_id, new_id)
        
        old_badge = f'<span class="topic-badge">Q {i:02d}</span>'
        new_badge = f'<span class="topic-badge">Q {i+1:02d}</span>'
        html = html.replace(old_badge, new_badge)

    # 5. Remove latest-card-highlight and latest-tag from old Q01 (now Q02)
    html = html.replace('<section class="topic-section latest-card-highlight" id="q-02">', '<section class="topic-section" id="q-02">')
    html = html.replace("""          <span class="topic-badge">Q 02</span>\n          <span class="latest-tag">⭐ 가장 최근 질문 (1번 배치)</span>""", """          <span class="topic-badge">Q 02</span>""")

    # 6. Update main header description
    html = re.sub(
        r'<p class="main-desc">[\s\S]*?</p>',
        r"""<p class="main-desc">질문자님께서 질문하신 문장 그대로 좌측 탭 제목과 본문 제목을 구성하였습니다. 최상단에는 가장 최근 질문인 <strong>'halo implant가 punchthrough 개선하는 메커니즘'</strong>이 1번으로 위치합니다.</p>""",
        html,
        count=1
    )

    # 7. Insert new Q01 section right after header.main-header
    header_end_tag = '</header>'
    idx = html.find(header_end_tag)
    if idx != -1:
        insert_pos = idx + len(header_end_tag)
        html = html[:insert_pos] + "\n\n" + new_q01_section + html[insert_pos:]

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
