import os
import re

def update_html():
    file_path = r"C:\Work\반도체3\result\261007_v1.0\index.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. New Q01 nav-item
    new_nav_item = """      <li class="nav-item"><a href="#q-01" class="nav-link"><span class="nav-num">01</span><span class="nav-text">기생접합커패시턴스와 공핍커패시턴스는 같은말이야?</span></a></li>\n"""

    # 2. New Q01 Section with SVG
    new_q01_section = """    <!-- Q 01 : 기생접합커패시턴스와 공핍커패시턴스는 같은말이야? -->
    <section class="topic-section latest-card-highlight" id="q-01">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q 01</span>
          <span class="latest-tag">⭐ 가장 최근 질문 (1번 배치)</span>
          <h2 class="topic-title">기생접합커패시턴스와 공핍커패시턴스는 같은말이야?</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">면접 대비 3~4줄 핵심 요약</span>
        <ul class="summary-list">
          <li><strong>"물리적 동작 원리($C = \\frac{\\epsilon A}{W_{dep}}$) 관점에서는 기생 접합 커패시턴스($C_j$)도 공핍 커패시턴스($C_{dep}$)의 일종이므로 본질적으로 같은 물리 현상입니다."</strong></li>
          <li><strong>"하지만 MOSFET 소자 관점에서는 발생하는 위치와 역할에 따라 엄격히 구분됩니다. 공핍 커패시턴스($C_{dep}$)는 주로 '게이트 아래 채널 표면'에 생겨 문턱전압($V_{th}$)과 서브스레숄드 스윙($SS$)을 결정하는 성분을 의미합니다."</strong></li>
          <li><strong>"반면 기생 접합 커패시턴스($C_j$)는 '소스/드레인과 기판(Body) 사이의 p-n 접합면'에 원치 않게 생겨 회로의 스위칭 속도(RC Delay)를 저하시키고 충방전 전력을 소모시키는 기생 성분을 뜻하므로 완전히 같은 말로 혼용할 수는 없습니다."</strong></li>
        </ul>
      </div>
      <div class="lecture-content">
        <!-- SVG 그래픽 다이어그램: 공핍 커패시턴스 vs 기생 접합 커패시턴스 비교 -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [개념 맵 & 소자 위치 비교] 공핍 커패시턴스(물리적 총칭) vs 기생 접합 커패시턴스(S/D p-n 접합)
          </div>
          <svg viewBox="0 0 780 430" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <defs>
              <linearGradient id="capGateGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#475569"/>
                <stop offset="100%" stop-color="#334155"/>
              </linearGradient>
              <linearGradient id="capCdepGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="rgba(56, 189, 248, 0.25)"/>
                <stop offset="100%" stop-color="rgba(56, 189, 248, 0.05)"/>
              </linearGradient>
              <linearGradient id="capCjGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="rgba(244, 63, 94, 0.25)"/>
                <stop offset="100%" stop-color="rgba(244, 63, 94, 0.05)"/>
              </linearGradient>
            </defs>

            <!-- Base Background -->
            <rect width="780" height="430" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

            <!-- MOSFET Structure (Upper Half) -->
            <rect x="50" y="50" width="680" height="180" rx="6" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
            <text x="70" y="215" fill="#64748b" font-size="11" font-weight="600">P-기판 (Body)</text>

            <!-- Source & Drain -->
            <rect x="50" y="50" width="160" height="65" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.2"/>
            <text x="95" y="88" fill="#38bdf8" font-size="12" font-weight="800">Source (N⁺)</text>

            <rect x="570" y="50" width="160" height="65" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.2"/>
            <text x="615" y="88" fill="#38bdf8" font-size="12" font-weight="800">Drain (N⁺)</text>

            <!-- Gate -->
            <rect x="270" y="30" width="240" height="20" fill="url(#capGateGrad)" stroke="#94a3b8" stroke-width="1"/>
            <rect x="270" y="47" width="240" height="5" fill="#f59e0b"/>
            <text x="375" y="44" fill="#ffffff" font-size="11" font-weight="700">Gate</text>
            <text x="365" y="60" fill="#f59e0b" font-size="9.5" font-weight="800">산화막 (C_ox)</text>

            <!-- Location 1: Channel Depletion Capacitance C_dep -->
            <rect x="270" y="52" width="240" height="60" fill="url(#capCdepGrad)" stroke="#38bdf8" stroke-dasharray="3 3"/>
            <text x="305" y="85" fill="#38bdf8" font-size="11.5" font-weight="800">① 채널 표면 공핍 커패시턴스 (C_dep)</text>
            <text x="325" y="102" fill="#93c5fd" font-size="10">위치: 게이트 산화막 바로 아래 채널 표면</text>

            <!-- Location 2: Parasitic Junction Capacitance C_j -->
            <!-- Source bottom/side C_sb -->
            <path d="M 50 115 L 210 115 L 210 50 L 225 50 L 225 128 L 50 128 Z" fill="url(#capCjGrad)" stroke="#f43f5e" stroke-dasharray="3 3"/>
            <text x="65" y="145" fill="#f43f5e" font-size="11" font-weight="800">② 기생 접합 커패시턴스 (C_sb)</text>

            <!-- Drain bottom/side C_db -->
            <path d="M 555 50 L 570 50 L 570 115 L 730 115 L 730 128 L 555 128 Z" fill="url(#capCjGrad)" stroke="#f43f5e" stroke-dasharray="3 3"/>
            <text x="560" y="145" fill="#f43f5e" font-size="11" font-weight="800">② 기생 접합 커패시턴스 (C_db)</text>
            <text x="565" y="162" fill="#fca5a5" font-size="9.5">위치: 드레인/소스 p-n 접합면</text>


            <!-- Lower Half: Conceptual Distinction Cards -->
            <!-- Left Card: C_dep -->
            <rect x="50" y="245" width="330" height="170" rx="6" fill="rgba(56, 189, 248, 0.08)" stroke="#38bdf8" stroke-width="1.2"/>
            <text x="65" y="270" fill="#38bdf8" font-size="13" font-weight="800">📘 공핍 커패시턴스 (C_dep / C_d)</text>
            <text x="65" y="292" fill="#e2e8f0" font-size="11" font-weight="700">• 개념적 범주: 물리적 메커니즘을 뜻하는 상위 개념</text>
            <text x="65" y="312" fill="#cbd5e1" font-size="10.5">• MOSFET에서의 주 위치: 게이트 바로 아래 실리콘 표면</text>
            <text x="65" y="332" fill="#cbd5e1" font-size="10.5">• 소자에 미치는 영향:</text>
            <text x="75" y="352" fill="#93c5fd" font-size="10.5">- 서브스레숄드 스윙 결정: SS = 60 × (1 + C_dep / C_ox)</text>
            <text x="75" y="372" fill="#93c5fd" font-size="10.5">- 문턱전압(V_th) 및 기판 효과(Body Effect) 결정</text>
            <text x="65" y="398" fill="#38bdf8" font-size="11" font-weight="700">➔ "소자의 정전기적 게이트 통제력과 직결!"</text>

            <!-- Right Card: C_j -->
            <rect x="400" y="245" width="330" height="170" rx="6" fill="rgba(244, 63, 94, 0.08)" stroke="#f43f5e" stroke-width="1.2"/>
            <text x="415" y="270" fill="#f43f5e" font-size="13" font-weight="800">⚠️ 기생 접합 커패시턴스 (C_j = C_db, C_sb)</text>
            <text x="415" y="292" fill="#e2e8f0" font-size="11" font-weight="700">• 개념적 범주: 회로 관점의 '기생(불필요)' 하위 성분</text>
            <text x="415" y="312" fill="#cbd5e1" font-size="10.5">• MOSFET에서의 주 위치: 소스/드레인과 기판(Body) 접합면</text>
            <text x="415" y="332" fill="#cbd5e1" font-size="10.5">• 소자에 미치는 영향:</text>
            <text x="425" y="352" fill="#fca5a5" font-size="10.5">- 출력단 RC 지연 유발: 회로 동작 속도 20~30% 저하</text>
            <text x="425" y="372" fill="#fca5a5" font-size="10.5">- 동적 충방전 전력 낭비: P = C_j · V² · f</text>
            <text x="415" y="398" fill="#f43f5e" font-size="11" font-weight="700">➔ "회로 동작 속도를 갉아먹는 불필요한 군더더기!"</text>
          </svg>
        </div>

        <h3>1. 물리적 본질: "물리 원리는 100% 동일하다"</h3>
        <p>반도체 물리 관점에서 두 커패시턴스는 모두 <strong>'공핍층(Depletion Region)이 전하 없는 절연체 역할을 하여 발생하는 정전용량'</strong>이라는 동일한 물리 공식을 따릅니다:</p>
        <div class="formula-box">
          $$C = \frac{dQ}{dV} = \frac{\epsilon_{si} \cdot A}{W_{dep}}$$
        </div>
        <p>따라서 <strong>"기생 접합 커패시턴스($C_j$)는 공핍 커패시턴스($C_{dep}$)라는 거대한 물리적 범주 안에 포함되는 한 종류(부분집합)"</strong>입니다.</p>

        <h3>2. 소자/회로 관점의 결정적 차이: "위치와 역할이 완전히 다르다"</h3>
        <p>MOSFET을 다룰 때 엔지니어들이 두 단어를 구분해서 쓰는 이유는 <strong>발생하는 위치와 소자에 미치는 영향</strong>이 전혀 다르기 때문입니다:</p>

        <table class="data-table">
          <thead>
            <tr>
              <th>구분</th>
              <th>공핍 커패시턴스 ($C_{dep}$ / $C_d$)</th>
              <th>기생 접합 커패시턴스 ($C_j$ / $C_{db}$, $C_{sb}$)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>발생 위치</strong></td>
              <td><strong>게이트 산화막 바로 아래 채널 표면</strong></td>
              <td><strong>소스 및 드레인과 기판(Body) 사이의 접합면</strong></td>
            </tr>
            <tr>
              <td><strong>개념적 성격</strong></td>
              <td>소자 물리학적 기본 특성 파라미터</td>
              <td>회로 설계 관점의 불필요한 '기생 성분(Parasitic)'</td>
            </tr>
            <tr>
              <td><strong>주요 영향</strong></td>
              <td>
                • 서브스레숄드 스윙: $SS = 60 \cdot (1 + C_{dep}/C_{ox})$<br>
                • 문턱전압($V_{th}$) 및 바디 효과 계수($\gamma$) 결정
              </td>
              <td>
                • 출력단 $RC$ 스위칭 지연(Delay) 유발<br>
                • 동적 소비 전력($P = C_j V^2 f$) 낭비
              </td>
            </tr>
            <tr>
              <td><strong>엔지니어의 목표</strong></td>
              <td>$SS \rightarrow 60$ 달성을 위해 $C_{dep}$ 축소 (FD-SOI 도입 등)</td>
              <td>동작 속도 확보를 위해 $C_j$ 극소화 (Shallow Junction, SOI 등)</td>
            </tr>
          </tbody>
        </table>

        <h3>3. 단어의 뉘앙스 분해: 왜 '기생'과 '접합'이 붙었을까?</h3>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>'기생(Parasitic)'</strong>: 우리가 원해서 넣은 소자가 아니라, 소스/드레인을 만들다 보니 어쩔 수 없이 덤으로 딸려와서 <strong>회로 성능을 갉아먹는 성분</strong>이라는 뜻입니다.</li>
          <li><strong>'접합(Junction)'</strong>: 채널 표면이 아니라 소스/드레인과 기판이 만나는 <strong>p-n 역방향 접합 다이오드 면</strong>에서 생긴다는 구체적인 위치를 뜻합니다.</li>
        </ul>

        <h3>4. 직관적 마스터 비유: '스프링'과 '신발에 묻은 진흙'</h3>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>공핍 커패시턴스 ($C_{dep}$) = '스위치의 내부 스프링'</strong>:
            <br>- 게이트가 채널을 누를 때 버티는 저항력입니다.
            <br>- 이 스프링($C_{dep}$)이 너무 뻣뻣하면 게이트가 스위치를 켜는 데 힘($SS$ 저하)이 듭니다.
          </li>
          <li><strong>기생 접합 커패시턴스 ($C_j$) = '달리기 선수의 신발에 묻은 무거운 진흙'</strong>:
            <br>- 스위치 자체의 동작과는 상관없이, 선수가 달릴 때(드레인이 출력 전압을 바꿀 때)마다 다리를 무겁게 붙잡아 속도를 늦추는 거추장스러운 방해물입니다.
          </li>
        </ul>
      </div>
    </section>
"""

    # 3. Renumber existing nav-items (01 -> 02, ..., 27 -> 28)
    nav_pattern = r'(<ul class="nav-list" id="navList">)([\s\S]*?)(</ul>)'
    match = re.search(nav_pattern, html)
    if match:
        old_nav_items = match.group(2)
        shifted_nav = old_nav_items
        for i in range(27, 0, -1):
            old_str = f'<span class="nav-num">{i:02d}</span>'
            new_str = f'<span class="nav-num">{i+1:02d}</span>'
            shifted_nav = shifted_nav.replace(old_str, new_str)
            old_href = f'href="#q-{i:02d}"'
            new_href = f'href="#q-{i+1:02d}"'
            shifted_nav = shifted_nav.replace(old_href, new_href)
        
        updated_nav_list = match.group(1) + "\n" + new_nav_item + shifted_nav + match.group(3)
        html = html[:match.start()] + updated_nav_list + html[match.end():]

    # 4. Renumber existing sections (q-01 -> q-02, ..., q-27 -> q-28)
    for i in range(27, 0, -1):
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
        r"""<p class="main-desc">질문자님께서 질문하신 문장 그대로 좌측 탭 제목과 본문 제목을 구성하였습니다. 최상단에는 가장 최근 질문인 <strong>'기생접합커패시턴스와 공핍커패시턴스는 같은말이야?'</strong>가 1번으로 위치합니다.</p>""",
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
