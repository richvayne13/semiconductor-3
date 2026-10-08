import os
import re

def update_html():
    file_path = r"C:\Work\반도체3\result\261007_v1.0\index.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. New Q01 nav-item
    new_nav_item = """      <li class="nav-item"><a href="#q-01" class="nav-link"><span class="nav-num">01</span><span class="nav-text">cox가 증가하면 vt는 왜 감소해?</span></a></li>\n"""

    # 2. New Q01 Section with SVG
    new_q01_section = """    <!-- Q 01 : cox가 증가하면 vt는 왜 감소해? -->
    <section class="topic-section latest-card-highlight" id="q-01">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q 01</span>
          <span class="latest-tag">⭐ 가장 최근 질문 (1번 배치)</span>
          <h2 class="topic-title">cox가 증가하면 vt는 왜 감소해?</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">면접 대비 3~4줄 핵심 요약</span>
        <ul class="summary-list">
          <li><strong>"문턱전압 공식($V_{th} = V_{FB} + 2\\phi_F + \\frac{Q_{dep}}{C_{ox}}$)에서, 채널을 형성하기 전 기판 공핍층 전하($Q_{dep}$)를 형성하는 데 소모되는 산화막 전압 강하가 $V_{ox} = \\frac{Q_{dep}}{C_{ox}}$이기 때문입니다."</strong></li>
          <li><strong>"산화막 커패시턴스($C_{ox} = \\frac{\\epsilon_{ox}}{T_{ox}}$)가 커질수록 커패시터의 전하 충전 능력이 극대화되어, 동일한 공핍 전하($Q_{dep}$)를 유도하는 데 필요한 산화막 전압 비용($V_{ox}$)이 획기적으로 줄어듭니다."</strong></li>
          <li><strong>"결과적으로 게이트 전압이 산화막에서 쓸데없이 허비되지 않고 실리콘 표면 밴드를 휘는 데($2\\phi_F$) 거의 1:1로 다이렉트 전달되므로, 더 낮은 게이트 전압만으로도 즉시 채널이 턴온(Vt 감소)됩니다."</strong></li>
        </ul>
      </div>
      <div class="lecture-content">
        <!-- SVG 그래픽 다이어그램: Cox 증가와 Vt 감소 메커니즘 -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [전압 분배 비교] 두꺼운 산화막(산화막 전압 낭비 커서 Vt 높음) vs 얇은 산화막(Cox 극대화로 직결 전달, Vt 낮음)
          </div>
          <svg viewBox="0 0 780 410" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <defs>
              <linearGradient id="gateGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#475569"/>
                <stop offset="100%" stop-color="#334155"/>
              </linearGradient>
              <linearGradient id="oxThickGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#f59e0b"/>
                <stop offset="100%" stop-color="#d97706"/>
              </linearGradient>
              <linearGradient id="oxThinGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#10b981"/>
                <stop offset="100%" stop-color="#059669"/>
              </linearGradient>
              <linearGradient id="siSubGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#1e293b"/>
                <stop offset="100%" stop-color="#0f172a"/>
              </linearGradient>
            </defs>

            <!-- Background -->
            <rect width="780" height="410" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
            <line x1="390" y1="20" x2="390" y2="390" stroke="#334155" stroke-dasharray="4 4" stroke-width="1.5"/>

            <!-- ================= LEFT: THICK OXIDE (Low Cox) ================= -->
            <text x="30" y="38" fill="#f59e0b" font-size="13" font-weight="800">⚠️ [1] 두꺼운 산화막 (T_ox 큼 ➔ C_ox 작음 ➔ V_t 높음)</text>
            
            <!-- Gate Electrode Left -->
            <rect x="50" y="60" width="290" height="30" rx="4" fill="url(#gateGrad)" stroke="#64748b" stroke-width="1"/>
            <text x="165" y="80" fill="#f8fafc" font-size="11.5" font-weight="700">게이트 (Gate)</text>

            <!-- Thick Oxide Layer -->
            <rect x="50" y="90" width="290" height="45" fill="url(#oxThickGrad)" stroke="#b45309" stroke-width="1.2"/>
            <text x="115" y="118" fill="#ffffff" font-size="12" font-weight="800">두꺼운 산화막 (T_ox 두꺼움)</text>

            <!-- Silicon Substrate -->
            <rect x="50" y="135" width="290" height="110" rx="4" fill="url(#siSubGrad)" stroke="#334155" stroke-width="1.2"/>
            <text x="130" y="170" fill="#94a3b8" font-size="11" font-weight="600">P-기판 (실리콘 채널 표면)</text>
            <!-- Depletion charge -->
            <rect x="70" y="185" width="250" height="45" rx="4" fill="rgba(239, 68, 68, 0.15)" stroke="#f43f5e" stroke-dasharray="3 3"/>
            <text x="100" y="212" fill="#fca5a5" font-size="11" font-weight="700">공핍 전하 Q_dep (고정 음이온 ⊖⊖⊖)</text>

            <!-- Voltage Breakdown Bar Left -->
            <rect x="50" y="260" width="290" height="130" rx="6" fill="rgba(245, 158, 11, 0.08)" stroke="#f59e0b" stroke-width="1"/>
            <text x="60" y="282" fill="#f59e0b" font-size="12" font-weight="800">🔋 게이트 인가 전압 분배 (V_t ≈ 0.8 V):</text>
            
            <!-- Big Vox loss -->
            <rect x="60" y="295" width="160" height="24" rx="4" fill="#f43f5e"/>
            <text x="70" y="311" fill="#ffffff" font-size="11" font-weight="700">V_ox = Q_dep / C_ox (0.5V 낭비!)</text>

            <!-- Small surface potential -->
            <rect x="225" y="295" width="100" height="24" rx="4" fill="#3b82f6"/>
            <text x="235" y="311" fill="#ffffff" font-size="11" font-weight="700">2φ_F (0.3V)</text>

            <text x="60" y="342" fill="#cbd5e1" font-size="10.5">• C_ox가 작아 Q_dep를 유도하는 데 큰 전압(V_ox) 낭비</text>
            <text x="60" y="360" fill="#cbd5e1" font-size="10.5">• 실리콘에 전압이 잘 전달되지 않아 채널 턴온 둔감</text>
            <text x="60" y="378" fill="#f87171" font-size="11" font-weight="700">➔ 결론: 문턱전압(V_t)이 높아짐 (구동력 저하)</text>


            <!-- ================= RIGHT: THIN OXIDE (High Cox) ================= -->
            <text x="420" y="38" fill="#10b981" font-size="13" font-weight="800">✅ [2] 얇은 산화막 (T_ox 얇음 ➔ C_ox 폭증 ➔ V_t 감소)</text>
            
            <!-- Gate Electrode Right -->
            <rect x="440" y="60" width="290" height="30" rx="4" fill="url(#gateGrad)" stroke="#64748b" stroke-width="1"/>
            <text x="555" y="80" fill="#f8fafc" font-size="11.5" font-weight="700">게이트 (Gate)</text>

            <!-- Thin Oxide Layer (Ultra thin) -->
            <rect x="440" y="90" width="290" height="15" fill="url(#oxThinGrad)" stroke="#047857" stroke-width="1.2"/>
            <text x="505" y="102" fill="#ffffff" font-size="10.5" font-weight="800">얇은 산화막 (T_ox 극소화 ➔ C_ox 폭증!)</text>

            <!-- Silicon Substrate Right -->
            <rect x="440" y="105" width="290" height="140" rx="4" fill="url(#siSubGrad)" stroke="#334155" stroke-width="1.2"/>
            <text x="520" y="145" fill="#94a3b8" font-size="11" font-weight="600">P-기판 (실리콘 채널 표면)</text>
            <!-- Inversion channel formed easily -->
            <rect x="460" y="155" width="250" height="20" rx="3" fill="#38bdf8"/>
            <text x="495" y="169" fill="#042f2e" font-size="11" font-weight="800">⚡ 전자 반전층(채널) 손쉽게 형성!</text>
            <rect x="460" y="180" width="250" height="45" rx="4" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-dasharray="3 3"/>
            <text x="490" y="207" fill="#6ee7b7" font-size="11" font-weight="700">공핍 전하 Q_dep (작은 전압으로도 완전 보상)</text>

            <!-- Voltage Breakdown Bar Right -->
            <rect x="440" y="260" width="290" height="130" rx="6" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1"/>
            <text x="450" y="282" fill="#10b981" font-size="12" font-weight="800">⚡ 게이트 인가 전압 분배 (V_t ≈ 0.4 V 급감!):</text>
            
            <!-- Tiny Vox loss -->
            <rect x="450" y="295" width="55" height="24" rx="4" fill="#10b981"/>
            <text x="455" y="311" fill="#ffffff" font-size="9.5" font-weight="700">V_ox (0.1V)</text>

            <!-- Full surface potential -->
            <rect x="510" y="295" width="100" height="24" rx="4" fill="#3b82f6"/>
            <text x="520" y="311" fill="#ffffff" font-size="11" font-weight="700">2φ_F (0.3V)</text>

            <text x="450" y="342" fill="#cbd5e1" font-size="10.5">• C_ox가 극대화되어 V_ox = Q_dep / C_ox 전압 손실 80% 절감</text>
            <text x="450" y="360" fill="#cbd5e1" font-size="10.5">• 게이트 전압이 산화막 통과 후 표면에 1:1 다이렉트 전달</text>
            <text x="450" y="378" fill="#34d399" font-size="11" font-weight="700">➔ 결론: 문턱전압(V_t)이 대폭 감소! (고속 저전력 동작)</text>
          </svg>
        </div>

        <h3>1. 문턱전압($V_{th}$)의 수식적 정의와 $C_{ox}$의 위치</h3>
        <p>MOSFET에서 문턱전압($V_{th}$)은 실리콘 표면이 강반전(Strong Inversion, 표면 전위 $\phi_s = 2\phi_F$)에 도달하여 전도 채널이 형성되는 데 필요한 최소 게이트 전압입니다:</p>
        <div class="formula-box">
          $$V_{th} = V_{FB} + 2\phi_F + \mathbf{V_{ox}} = V_{FB} + 2\phi_F + \frac{|Q_{dep}|}{\mathbf{C_{ox}}}$$
        </div>
        <p>여기서 공핍 전하량 $|Q_{dep}| = \sqrt{2q \epsilon_{si} N_A (2\phi_F)}$를 대입하면 전체 문턱전압 공식이 완성됩니다:</p>
        <div class="formula-box">
          $$V_{th} = V_{FB} + 2\phi_F + \frac{\sqrt{2q \epsilon_{si} N_A (2\phi_F)}}{\mathbf{C_{ox}}}$$
        </div>
        <p>수식에서 명확히 드러나듯, <strong>$C_{ox}$는 분모에 위치</strong>합니다. 따라서 산화막 두께($T_{ox}$)가 얇아져 $C_{ox} = \epsilon_{ox}/T_{ox}$가 증가할수록, 산화막 전압 강하 항인 $\frac{Q_{dep}}{C_{ox}}$가 줄어들어 **전체 문턱전압($V_{th}$)은 수학적·물리적으로 감소**할 수밖에 없습니다.</p>

        <h3>2. 물리적 메커니즘: 산화막 전압 강하($V_{ox}$)의 절감</h3>
        <p>게이트 전압을 인가하여 채널을 열려면 두 가지 단계를 거쳐야 합니다:</p>
        <ol style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>1단계 (공핍 전하 $Q_{dep}$ 보상)</strong>: 기판 표면의 다수 캐리어(정공)를 밀어내어 고정된 음이온($B^-$)으로 이루어진 공핍층을 먼저 파놓아야 합니다. 게이트 전극에는 이 음전하와 짝을 이루는 양전하($+Q_{dep}$)가 충전되어야 합니다.</li>
          <li><strong>2단계 (반전층 형성)</strong>: 공핍층이 최대치($W_{dep,max}$)에 달한 후, 비로소 자유 전자들이 표면에 모여 전류가 흐르는 채널이 열립니다($2\phi_F$).</li>
        </ol>
        <p>기본 커패시터 물리 법칙은 <strong>$Q = C \cdot V \implies V = Q / C$</strong>입니다:</p>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>$C_{ox}$가 작을 때 (두꺼운 산화막)</strong>: 커패시터 용량이 작으므로, 필요한 전하량($Q_{dep}$)을 게이트에 끌어모으려면 산화막 양단에 **엄청나게 큰 전압($V_{ox}$)을 쓸데없이 지불(낭비)**해야 합니다.</li>
          <li><strong>$C_{ox}$가 클 때 (얇은 산화막)</strong>: 커패시터 용량이 크기 때문에, **극히 미미한 전압($V_{ox}$)만 걸어주어도 필요한 공핍 전하($Q_{dep}$)가 순식간에 충전**됩니다. 산화막에서 허비되는 통행세($V_{ox}$)가 사라지므로 문턱전압($V_{th}$)이 극적으로 낮아집니다.</li>
        </ul>

        <h3>3. 정전기적 전압 분배(Voltage Divider) 관점</h3>
        <p>게이트에 가한 전압($V_G$)은 산화막 커패시터($C_{ox}$)와 실리콘 공핍 커패시터($C_{dep}$)가 직렬로 연결된 회로에 분배됩니다:</p>
        <div class="formula-box">
          $$\Delta \phi_s = \Delta V_G \cdot \left(\frac{C_{ox}}{C_{ox} + C_{dep}}\right) = \Delta V_G \cdot \left(\frac{1}{1 + \frac{C_{dep}}{\mathbf{C_{ox}}}}\right)$$
        </div>
        <p>$C_{ox}$가 $C_{dep}$보다 압도적으로 커지면 분배비는 거의 <strong>1 (100%)</strong>에 수렴합니다. 즉, <strong>게이트 전압이 산화막에서 손실되지 않고 실리콘 표면 전위($\phi_s$)로 온전히 직결 전달</strong>되므로, 표면 밴드를 $2\phi_F$까지 휘어 채널을 오픈하는 데 필요한 게이트 전압($V_{th}$)이 낮아집니다.</p>

        <h3>4. 직관적 마스터 비유: '물통의 밑면적'과 '귓속말'</h3>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>물통 비유</strong>:
            <br>- 공핍 전하량($Q_{dep}$)은 채워야 할 '물의 양(리터)'이고, $C_{ox}$는 물통의 '밑면적', $V_{ox}$는 '수위(높이)'입니다.
            <br>- 좁은 물통($C_{ox}$ 작음): 정해진 양의 물을 채우려면 수위(전압)가 한참 높이 치솟아야 합니다 $\rightarrow$ $V_{th}$ 높음.
            <br>- 넓은 대형 물통($C_{ox}$ 큼): 얕은 수위(낮은 전압)만으로도 필요한 물의 양을 단숨에 채웁니다 $\rightarrow$ <strong>$V_{th}$ 낮음</strong>.
          </li>
          <li><strong>확성기 vs 귓속말 비유</strong>:
            <br>- 산화막이 두꺼운 것은 먼 거리에서 확성기로 채널을 부르는 것과 같아 큰 목소리(높은 전압)가 필요합니다.
            <br>- 산화막이 얇아 $C_{ox}$가 큰 것은 게이트가 실리콘 바로 귓가에 밀착한 것과 같아, <strong>작은 속삭임(낮은 전압)만으로도 즉각 반응하여 채널이 켜집니다</strong>.
          </li>
        </ul>
      </div>
    </section>
"""

    # 3. Renumber existing nav-items (01 -> 02, ..., 25 -> 26)
    nav_pattern = r'(<ul class="nav-list" id="navList">)([\s\S]*?)(</ul>)'
    match = re.search(nav_pattern, html)
    if match:
        old_nav_items = match.group(2)
        shifted_nav = old_nav_items
        for i in range(25, 0, -1):
            old_str = f'<span class="nav-num">{i:02d}</span>'
            new_str = f'<span class="nav-num">{i+1:02d}</span>'
            shifted_nav = shifted_nav.replace(old_str, new_str)
            old_href = f'href="#q-{i:02d}"'
            new_href = f'href="#q-{i+1:02d}"'
            shifted_nav = shifted_nav.replace(old_href, new_href)
        
        updated_nav_list = match.group(1) + "\n" + new_nav_item + shifted_nav + match.group(3)
        html = html[:match.start()] + updated_nav_list + html[match.end():]

    # 4. Renumber existing sections (q-01 -> q-02, ..., q-25 -> q-26)
    for i in range(25, 0, -1):
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
        r"""<p class="main-desc">질문자님께서 질문하신 문장 그대로 좌측 탭 제목과 본문 제목을 구성하였습니다. 최상단에는 가장 최근 질문인 <strong>'cox가 증가하면 vt는 왜 감소해?'</strong>가 1번으로 위치합니다.</p>""",
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
