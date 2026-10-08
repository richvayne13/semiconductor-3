import os
import re

def update_html():
    file_path = r"C:\Work\반도체3\result\261007_v1.0\index.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. New Q01 nav-item
    new_nav_item = """      <li class="nav-item"><a href="#q-01" class="nav-link"><span class="nav-num">01</span><span class="nav-text">soi기술도입이유</span></a></li>\n"""

    # 2. New Q01 Section with SVG
    new_q01_section = """    <!-- Q 01 : soi기술도입이유 -->
    <section class="topic-section latest-card-highlight" id="q-01">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q 01</span>
          <span class="latest-tag">⭐ 가장 최근 질문 (1번 배치)</span>
          <h2 class="topic-title">soi기술도입이유</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">면접 대비 3~4줄 핵심 요약</span>
        <ul class="summary-list">
          <li><strong>"기판과 활성 소자 사이에 매몰 절연막(BOX: Buried Oxide)을 삽입하여, 드레인 공핍층이 기판 지하 깊은 곳을 통해 소스로 결합하는 지하 펀치스루(Punchthrough) 누설 경로를 물리적으로 원천 차단하기 위해 도입되었습니다."</strong></li>
          <li><strong>"소스/드레인 바닥면이 실리콘 기판 대신 유전율이 낮은 산화막($SiO_2$)과 맞닿으므로 기생 접합 커패시턴스($C_j$)가 70~80% 급감하여, 스위칭 동작 속도(RC Delay)가 20~30% 빨라지고 충방전 소비 전력이 대폭 절감됩니다."</strong></li>
          <li><strong>"특히 박막형 FD-SOI는 기판 공핍 전하($Q_{dep}$)가 거의 없어 이상적인 서브스레숄드 스윙($SS \\approx 60\\,\\text{mV/dec}$)을 달성하며, 기생 래치업(Latch-up) 및 방사선 소프트 에러를 완벽히 박멸합니다."</strong></li>
        </ul>
      </div>
      <div class="lecture-content">
        <!-- SVG 그래픽 다이어그램: Bulk Si vs SOI 구조 비교 및 4대 도입 이유 -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [소자 구조 비교] 벌크 실리콘(지하 펀치스루 & 거대 기생용량 C_j) vs SOI(BOX 절연막으로 지하 통로 절단 & C_j 80% 급감)
          </div>
          <svg viewBox="0 0 780 420" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <defs>
              <linearGradient id="soiGateGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#475569"/>
                <stop offset="100%" stop-color="#334155"/>
              </linearGradient>
              <linearGradient id="soiBoxGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#0284c7"/>
                <stop offset="100%" stop-color="#38bdf8"/>
              </linearGradient>
              <linearGradient id="soiLeakGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="rgba(244, 63, 94, 0.3)"/>
                <stop offset="100%" stop-color="rgba(244, 63, 94, 0.05)"/>
              </linearGradient>
            </defs>

            <!-- Background -->
            <rect width="780" height="420" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
            <line x1="390" y1="20" x2="390" y2="400" stroke="#334155" stroke-dasharray="4 4" stroke-width="1.5"/>

            <!-- ================= LEFT: BULK SILICON ================= -->
            <text x="30" y="38" fill="#f43f5e" font-size="13" font-weight="800">❌ [1] 기존 벌크 실리콘 (Bulk Si)</text>
            
            <!-- Substrate Bulk -->
            <rect x="30" y="60" width="330" height="200" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
            <text x="40" y="245" fill="#64748b" font-size="11" font-weight="600">두꺼운 P-기판 실리콘 벌크 (연결됨)</text>

            <!-- Gate -->
            <rect x="135" y="42" width="120" height="18" fill="url(#soiGateGrad)" stroke="#94a3b8" stroke-width="1"/>
            <rect x="135" y="58" width="120" height="4" fill="#f59e0b"/>
            <text x="180" y="55" fill="#ffffff" font-size="10.5" font-weight="700">Gate</text>

            <!-- Source & Drain -->
            <rect x="30" y="60" width="85" height="55" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.2"/>
            <text x="50" y="92" fill="#38bdf8" font-size="11.5" font-weight="800">Source (N⁺)</text>
            
            <rect x="275" y="60" width="85" height="55" fill="#1e293b" stroke="#0ea5e9" stroke-width="1.2"/>
            <text x="295" y="92" fill="#38bdf8" font-size="11.5" font-weight="800">Drain (N⁺)</text>

            <!-- Huge Bottom Junction Capacitance C_j -->
            <rect x="30" y="115" width="85" height="12" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-dasharray="2 2"/>
            <rect x="275" y="115" width="85" height="12" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-dasharray="2 2"/>
            <text x="35" y="142" fill="#fca5a5" font-size="10" font-weight="700">거대한 접합 정전용량 C_j (느림!)</text>

            <!-- Deep Bulk Leakage (Punchthrough) -->
            <path d="M 115 105 Q 195 185 275 105" fill="none" stroke="#f43f5e" stroke-width="3" stroke-dasharray="4 3"/>
            <polygon points="275,105 262,99 266,108" fill="#f43f5e"/>
            <text x="110" y="175" fill="#f87171" font-size="11" font-weight="800">⚡ 지하 펀치스루 누설 통로 개방!</text>
            <text x="125" y="195" fill="#fca5a5" font-size="10">게이트 제어권 밖 (오프 누설 폭증)</text>

            <!-- Explanation Box Left -->
            <rect x="30" y="275" width="330" height="125" rx="6" fill="rgba(244, 63, 94, 0.08)" stroke="#f43f5e" stroke-width="1"/>
            <text x="40" y="296" fill="#f43f5e" font-size="11.5" font-weight="700">⚠️ 벌크 실리콘의 한계:</text>
            <text x="40" y="316" fill="#cbd5e1" font-size="10.5">• 소스-드레인 아래에 두꺼운 기판이 있어 지하 누설 통로 존재</text>
            <text x="40" y="334" fill="#cbd5e1" font-size="10.5">• 바닥면 p-n 접합 면적이 넓어 접합 커패시턴스(C_j) 거대함</text>
            <text x="40" y="352" fill="#cbd5e1" font-size="10.5">• 인접 소자와 기판을 공유하여 기생 래치업(Latch-up) 위험</text>
            <text x="40" y="370" fill="#f87171" font-size="10.5">• 방사선 충돌 시 지하 벌크에 막대한 전하 축적 (소프트 에러)</text>


            <!-- ================= RIGHT: SOI (Silicon-On-Insulator) ================= -->
            <text x="420" y="38" fill="#10b981" font-size="13" font-weight="800">✅ [2] SOI 구조 (Silicon-On-Insulator)</text>
            
            <!-- Support Wafer Bottom -->
            <rect x="420" y="160" width="330" height="100" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
            <text x="510" y="215" fill="#64748b" font-size="11" font-weight="600">하부 지지 기판 (Base Substrate)</text>

            <!-- Buried Oxide (BOX Layer) -->
            <rect x="420" y="115" width="330" height="45" fill="url(#soiBoxGrad)" stroke="#0284c7" stroke-width="1.5"/>
            <text x="480" y="142" fill="#ffffff" font-size="12" font-weight="800">🛡️ 매몰 절연막 (BOX: Buried Oxide, SiO₂)</text>

            <!-- Ultra-thin Top Si Layer -->
            <rect x="420" y="60" width="330" height="55" fill="#1e293b" stroke="#334155" stroke-width="1.2"/>

            <!-- Gate Right -->
            <rect x="525" y="42" width="120" height="18" fill="url(#soiGateGrad)" stroke="#94a3b8" stroke-width="1"/>
            <rect x="525" y="58" width="120" height="4" fill="#10b981"/>
            <text x="570" y="55" fill="#ffffff" font-size="10.5" font-weight="700">Gate</text>

            <!-- Source & Drain touching BOX -->
            <rect x="420" y="60" width="85" height="55" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
            <text x="440" y="92" fill="#34d399" font-size="11.5" font-weight="800">Source (N⁺)</text>
            
            <rect x="665" y="60" width="85" height="55" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
            <text x="685" y="92" fill="#34d399" font-size="11.5" font-weight="800">Drain (N⁺)</text>

            <!-- Channel in Ultra-thin Si -->
            <text x="540" y="92" fill="#38bdf8" font-size="11" font-weight="700">초박막 채널</text>

            <!-- Blocking punchthrough -->
            <line x1="505" y1="135" x2="665" y2="135" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="4 2"/>
            <circle cx="585" cy="135" r="14" fill="#dc2626"/>
            <text x="579" y="140" fill="#ffffff" font-size="14" font-weight="900">✕</text>
            <text x="495" y="105" fill="#10b981" font-size="10.5" font-weight="800">지하 통로 원천 절단! (누설 = 0)</text>

            <!-- Explanation Box Right -->
            <rect x="420" y="275" width="330" height="125" rx="6" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1"/>
            <text x="430" y="296" fill="#10b981" font-size="11.5" font-weight="700">💡 SOI 도입 4대 핵심 이점:</text>
            <text x="430" y="316" fill="#cbd5e1" font-size="10.5">• ① 지하 벌크가 없어 펀치스루(Punchthrough) 물리적 박멸</text>
            <text x="430" y="334" fill="#cbd5e1" font-size="10.5">• ② S/D 바닥이 산화막에 닿아 기생용량(C_j) 80% 급감 ➔ 초고속</text>
            <text x="430" y="352" fill="#cbd5e1" font-size="10.5">• ③ 공핍 커패시턴스 소멸로 이상적 서브스레숄드 스윙(SS ≈ 60)</text>
            <text x="430" y="370" fill="#34d399" font-size="10.5">• ④ 완전한 소자 격리로 래치업 및 방사선 에러 100% 차단</text>
          </svg>
        </div>

        <h3>1. SOI(Silicon-On-Insulator)의 구조적 본질</h3>
        <p>기존 벌크(Bulk) 실리콘 웨이퍼는 트랜지스터의 활성 영역(소스, 드레인, 채널)이 두꺼운 실리콘 기판 본체와 물리적으로 이어져 있습니다. 반면 <strong>SOI 웨이퍼</strong>는 실리콘 기판 위에 두꺼운 <strong>매몰 산화막(BOX: Buried Oxide, 주로 $SiO_2$)</strong>을 형성하고, 그 위에 얇은 단결정 실리콘 박막(Top Si film)을 얹은 샌드위치 구조입니다.</p>

        <h3>2. SOI 기술 도입의 4대 핵심 이유 (소자물리 관점)</h3>
        
        <h4>① 지하 펀치스루(Punchthrough) 원천 봉쇄 (단채널 효과 극복)</h4>
        <p>미세화가 진행될수록 드레인 전계가 기판 지하 깊은 곳(Bulk)으로 침투하여 소스 공핍층과 결합하는 <strong>펀치스루</strong>가 발생합니다. SOI 구조에서는 소스/드레인/채널 하부에 두꺼운 절연체인 BOX가 깔려 있어, 전자가 누설될 수 있는 <strong>'기판 지하 통로 자체가 물리적으로 존재하지 않습니다.'</strong> 따라서 단채널에서도 극도의 오프 누설 억제 능력을 발휘합니다.</p>

        <h4>② 접합 정전용량($C_j$) 극소화 ➔ 동작 속도 향상 & 저전력화</h4>
        <p>벌크 소자에서는 소스/드레인 바닥면 전체가 p-n 접합을 이루어 거대한 기생 접합 커패시턴스를 가집니다:</p>
        <div class="formula-box">
          $$C_{j,\text{bulk}} = \frac{\epsilon_{si} \cdot A}{W_{dep}} \quad (\epsilon_{si} \approx 11.9) \quad \gg \quad C_{j,\text{SOI}} = \frac{\epsilon_{ox} \cdot A}{T_{BOX}} \quad (\epsilon_{ox} \approx 3.9)$$
        </div>
        <p>실리콘 대비 유전율이 3배 낮고 두께($T_{BOX}$)가 훨씬 두꺼운 절연막이 바닥을 받치고 있으므로, <strong>기생 접합 커패시턴스가 70~80% 급감</strong>합니다. 이에 따라 회로의 스위칭 지연 시간($\tau = R C_j$)이 단축되어 **동작 속도가 20~30% 향상**되고, 동적 소비 전력($P = C V^2 f$)이 대폭 절감됩니다.</p>

        <h4>③ 이상적인 서브스레숄드 스윙 ($SS \rightarrow 60\,\text{mV/dec}$) 달성</h4>
        <p>서브스레숄드 스윙 공식은 바디 팩터 $m$에 의해 결정됩니다:</p>
        <div class="formula-box">
          $$SS = 2.3 \frac{kT}{q} \left(1 + \frac{C_{dep}}{C_{ox}}\right) \approx 60 \cdot \mathbf{m} \quad [\text{mV/dec}]$$
        </div>
        <p>벌크 소자는 기판 공핍 커패시턴스($C_{dep}$)로 인해 $m \approx 1.2\sim1.4$ ($SS \approx 70\sim90\,\text{mV/dec}$) 수준입니다. 그러나 실리콘 두께가 극도로 얇은 <strong>FD-SOI(Fully Depleted SOI)</strong>는 채널 전체가 게이트에 의해 완전히 공핍되어 실리콘 내부 전하가 고정되므로, $C_{dep} \approx 0$에 수렴하여 <strong>$m \approx 1.0$ ($SS \approx 60\,\text{mV/dec}$의 이론적 한계치)</strong>에 도달합니다. 스위칭이 칼같이 날카로워져 낮은 $V_{th}$에서도 누설 전류가 발생하지 않습니다.</p>

        <h4>④ 기생 래치업(Latch-up) 및 소프트 에러(Soft Error) 완전 박멸</h4>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>래치업 박멸</strong>: 벌크 CMOS에서 인접한 NMOS와 PMOS 사이에 필연적으로 생기던 기생 싸이리스터(p-n-p-n 구조)가 BOX 절연막에 의해 완전히 분리되므로 래치업 현상이 원천 불가능합니다.</li>
          <li><strong>소프트 에러 내성</strong>: 우주 방사선(알파 입자, 중성자)이 실리콘 기판 깊은 곳에 충돌해도, 절연막 덕분에 전하가 채널로 유입되지 않아 메모리 비트 반전 오류가 수백 배 감소합니다.</li>
        </ul>

        <h3>3. 직관적인 일타 비유: '지하실 절단 방수포'와 '모래주머니 제거'</h3>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>방수 매트리스 비유 (펀치스루 박멸)</strong>:
            <br>- 벌크 실리콘은 흙바닥에 지은 집이라 비(드레인 전압)가 오면 지하 흙 속으로 물(누설 전류)이 스며들어 옆방(소스)으로 샙니다.
            <br>- SOI는 바닥 전체에 두꺼운 방수 고무 매트(BOX)를 깔아 지하실 경로 자체를 절단해 버렸으므로 누설이 물리적으로 0이 됩니다.
          </li>
          <li><strong>모래주머니 제거 비유 (C_j 극소화)</strong>:
            <br>- 소스/드레인이 밑바닥에 주렁주렁 달고 있던 무거운 모래주머니(거대한 실리콘 접합 커패시턴스)를 절연막으로 떼어내어, 발걸음(스위칭 속도)이 30% 날아갈 듯 가벼워진 육상 선수와 같습니다.
          </li>
        </ul>
      </div>
    </section>
"""

    # 3. Renumber existing nav-items (01 -> 02, ..., 26 -> 27)
    nav_pattern = r'(<ul class="nav-list" id="navList">)([\s\S]*?)(</ul>)'
    match = re.search(nav_pattern, html)
    if match:
        old_nav_items = match.group(2)
        shifted_nav = old_nav_items
        for i in range(26, 0, -1):
            old_str = f'<span class="nav-num">{i:02d}</span>'
            new_str = f'<span class="nav-num">{i+1:02d}</span>'
            shifted_nav = shifted_nav.replace(old_str, new_str)
            old_href = f'href="#q-{i:02d}"'
            new_href = f'href="#q-{i+1:02d}"'
            shifted_nav = shifted_nav.replace(old_href, new_href)
        
        updated_nav_list = match.group(1) + "\n" + new_nav_item + shifted_nav + match.group(3)
        html = html[:match.start()] + updated_nav_list + html[match.end():]

    # 4. Renumber existing sections (q-01 -> q-02, ..., q-26 -> q-27)
    for i in range(26, 0, -1):
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
        r"""<p class="main-desc">질문자님께서 질문하신 문장 그대로 좌측 탭 제목과 본문 제목을 구성하였습니다. 최상단에는 가장 최근 질문인 <strong>'soi기술도입이유'</strong>가 1번으로 위치합니다.</p>""",
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
