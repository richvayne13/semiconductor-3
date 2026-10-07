import os
import re

def update_html():
    file_path = r"C:\Work\반도체3\result\261007_v1.0\index.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. New Q01 nav-item
    new_nav_item = """      <li class="nav-item"><a href="#q-01" class="nav-link"><span class="nav-num">01</span><span class="nav-text">표면쪽 농도를 감소시키면 drain side 높은 전계를 낮추는 메커니즘</span></a></li>
"""
    
    # 2. New Q01 Section with SVG
    new_q01_section = """    <!-- Q 01 : 표면쪽 농도를 감소시키면 drain side의 높은 전계를 낮추는 메커니즘이 뭐야? -->
    <section class="topic-section latest-card-highlight" id="q-01">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q 01</span>
          <span class="latest-tag">⭐ 가장 최근 질문 (1번 배치)</span>
          <h2 class="topic-title">표면쪽 농도를 감소시키면 drain side의 높은 전계를 낮추는 메커니즘이 뭐야?</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">면접 대비 3~4줄 핵심 요약</span>
        <ul class="summary-list">
          <li><strong>"표면 쪽 불순물 농도($N$)를 낮추면 푸아송 방정식($\\frac{d\\mathcal{E}}{dx} = \\frac{qN}{\\epsilon}$)에 의해 공간 전하 밀도($\\rho$)가 줄어들어 전기장의 공간적 기울기가 완만해집니다."</strong></li>
          <li><strong>"도핑 농도가 낮아진 만큼 표면 접합부의 공핍층 폭($W_{dep} \\propto 1/\\sqrt{N}$)이 넓게 확장되므로, 동일한 드레인 전압 강하가 긴 거리에 걸쳐 분산되어 최고 전계 피크($\\mathcal{E}_{max}$)가 급격히 낮아집니다."</strong></li>
          <li><strong>"결과적으로 드레인 코너 표면에 집중되던 수평 및 수직 전계의 집중(Field Crowding)이 해소되어 핫 캐리어 주입(HCI)과 GIDL 누설을 동시에 억제하게 됩니다."</strong></li>
        </ul>
      </div>
      <div class="lecture-content">
        <!-- SVG 그래픽 다이어그램: 표면 농도 감소와 전계 피크 완화 -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [전기장 프로파일 비교] 표면 고농도(급격한 피크) vs 표면 농도 감소(완만한 전계 분산)
          </div>
          <svg viewBox="0 0 760 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <defs>
              <linearGradient id="q1HighDop" x1="0%" y1="100%" x2="0%" y2="0%">
                <stop offset="0%" stop-color="rgba(244, 63, 94, 0.1)"/>
                <stop offset="100%" stop-color="rgba(244, 63, 94, 0.45)"/>
              </linearGradient>
              <linearGradient id="q1LowDop" x1="0%" y1="100%" x2="0%" y2="0%">
                <stop offset="0%" stop-color="rgba(16, 185, 129, 0.1)"/>
                <stop offset="100%" stop-color="rgba(16, 185, 129, 0.45)"/>
              </linearGradient>
            </defs>
            <rect width="760" height="360" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
            <line x1="60" y1="310" x2="710" y2="310" stroke="#334155" stroke-width="1.5"/>
            <line x1="60" y1="310" x2="60" y2="30" stroke="#334155" stroke-width="1.5"/>
            <text x="60" y="22" fill="#94a3b8" font-size="11.5" font-family="'JetBrains Mono', monospace">전기장 세기 (E) ▲</text>
            <text x="640" y="332" fill="#94a3b8" font-size="11.5" font-family="'JetBrains Mono', monospace">드레인 접합 거리 (x) ►</text>

            <!-- 고농도 표면: 좁은 밑변, 치솟는 피크 -->
            <path d="M 270 310 L 360 55 L 410 310 Z" fill="url(#q1HighDop)" stroke="#f43f5e" stroke-width="3"/>
            <circle cx="360" cy="55" r="5" fill="#f43f5e"/>
            <text x="370" y="60" fill="#f43f5e" font-size="13" font-weight="800">E_max (고농도 표면: 공간 전하 밀도 ρ 높아 피크 폭증!)</text>

            <!-- 표면 농도 감소: 넓은 밑변, 완만한 피크 -->
            <path d="M 200 310 L 340 180 L 520 310 Z" fill="url(#q1LowDop)" stroke="#10b981" stroke-width="3"/>
            <circle cx="340" cy="180" r="5" fill="#10b981"/>
            <text x="350" y="185" fill="#10b981" font-size="13" font-weight="800">E_max (표면 농도 감소: 공핍층 W_dep 확장으로 피크 절반 완화!)</text>

            <!-- 면적 일정 주석 -->
            <rect x="520" y="85" width="210" height="60" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#0284c7" stroke-width="1.5"/>
            <text x="532" y="107" fill="#38bdf8" font-size="12" font-weight="700">💡 면적(전압 강하 ΔV)은 동일!</text>
            <text x="532" y="127" fill="#cbd5e1" font-size="11">밑변이 2~3배 넓어져 높이가 낮아짐</text>
          </svg>
        </div>

        <h3>1. 푸아송 방정식(Poisson's Equation)과 공간 전하 밀도</h3>
        <p>전기장의 공간적 기울기는 공간 전하 밀도($\\rho = qN$)에 비례합니다:</p>
        <div class="formula-box">
          $$\\frac{d\\mathcal{E}}{dx} = \\frac{\\rho(x)}{\\epsilon_{si}} = \\frac{q \\cdot \\mathbf{N_{surface}}}{\\epsilon_{si}}$$
        </div>
        <p>표면 농도($N_{surface}$)가 낮아지면 전하 밀도가 희박해져 전기장 그래프의 기울기가 완만해집니다.</p>

        <h3>2. 공핍층 폭($W_{dep}$) 확장과 삼각형 면적 법칙</h3>
        <div class="formula-box">
          $$\\Delta V = \\int \\mathcal{E}(x) dx \\approx \\frac{1}{2} \\cdot \\mathcal{E}_{max} \\cdot \\mathbf{W_{dep}} = \\text{일정 (드레인 전압)}$$
        </div>
        <p>공핍층 폭 공식($W_{dep} \\propto 1/\\sqrt{N}$)에 따라 농도가 낮아지면 밑변($W_{dep}$)이 2~3배로 넓어지므로, 같은 전압 면적을 채우기 위해 삼각형 높이인 최대 전계 피크($\\mathcal{E}_{max}$)가 절반 이하로 자동 하강합니다.</p>

        <h3>3. 2차원 전계 집중(Field Crowding) 해소</h3>
        <p>드레인 표면 코너는 게이트 수직 전계와 드레인 수평 전계가 교차하는 지점입니다. 표면 농도를 낮추면 얇게 달라붙어 있던 전기력선이 넓은 체적으로 부드럽게 퍼져나가며 국소 전계 집중이 완벽히 해소됩니다.</p>
      </div>
    </section>
"""

    # Renumber existing nav-items (01 -> 02, etc.)
    # We will find the nav-list block and replace it
    nav_pattern = r'(<ul class="nav-list" id="navList">)([\s\S]*?)(</ul>)'
    match = re.search(nav_pattern, html)
    if match:
        old_nav_items = match.group(2)
        # Shift numbers
        # First remove any old latest tag on Q01
        shifted_nav = old_nav_items
        for i in range(22, 0, -1):
            old_str = f'<span class="nav-num">{i:02d}</span>'
            new_str = f'<span class="nav-num">{i+1:02d}</span>'
            shifted_nav = shifted_nav.replace(old_str, new_str)
            # and replace href
            old_href = f'href="#q-{i:02d}"'
            new_href = f'href="#q-{i+1:02d}"'
            shifted_nav = shifted_nav.replace(old_href, new_href)
        
        updated_nav_list = match.group(1) + "\n" + new_nav_item + shifted_nav + match.group(3)
        html = html[:match.start()] + updated_nav_list + html[match.end():]

    # Renumber existing sections (q-01 -> q-02, etc.)
    # First find all section IDs and badges
    for i in range(22, 0, -1):
        old_id = f'id="q-{i:02d}"'
        new_id = f'id="q-{i+1:02d}"'
        html = html.replace(old_id, new_id)
        
        old_badge = f'<span class="topic-badge">Q {i:02d}</span>'
        new_badge = f'<span class="topic-badge">Q {i+1:02d}</span>'
        html = html.replace(old_badge, new_badge)

    # Remove latest-card-highlight and latest-tag from old Q01 (now Q02)
    html = html.replace('section class="topic-section latest-card-highlight" id="q-02"', 'section class="topic-section" id="q-02"')
    html = html.replace('<span class="latest-tag">⭐ 가장 최근 질문 (1번 배치)</span>\n          <h2 class="topic-title">gidl에서', '<h2 class="topic-title">gidl에서')

    # Insert new Q01 section right after header.main-header
    header_end_tag = '</header>'
    idx = html.find(header_end_tag)
    if idx != -1:
        insert_pos = idx + len(header_end_tag)
        html = html[:insert_pos] + "\n\n" + new_q01_section + html[insert_pos:]

    # Write to result
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {file_path}")

    # Copy to root
    root_path = r"C:\Work\반도체3\index.html"
    with open(root_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {root_path}")

if __name__ == "__main__":
    update_html()
