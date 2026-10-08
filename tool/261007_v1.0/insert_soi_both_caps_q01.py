import os
import re

def update_html():
    file_path = r"C:\Work\반도체3\result\261007_v1.0\index.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. New Q01 nav-item
    new_nav_item = """      <li class="nav-item"><a href="#q-01" class="nav-link"><span class="nav-num">01</span><span class="nav-text">soi는 기생접합커패시턴스를 줄여줘 공핍커패시턴스를 줄여줘?</span></a></li>\n"""

    # 2. New Q01 Section with SVG
    new_q01_section = """    <!-- Q 01 : soi는 기생접합커패시턴스를 줄여줘 공핍커패시턴스를 줄여줘? -->
    <section class="topic-section latest-card-highlight" id="q-01">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q 01</span>
          <span class="latest-tag">⭐ 가장 최근 질문 (1번 배치)</span>
          <h2 class="topic-title">soi는 기생접합커패시턴스를 줄여줘 공핍커패시턴스를 줄여줘?</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">면접 대비 3~4줄 핵심 요약</span>
        <ul class="summary-list">
          <li><strong>"결론부터 말씀드리면, SOI(특히 FD-SOI)는 기생 접합 커패시턴스($C_j$)와 공핍 커패시턴스($C_{dep}$) 둘 다 획기적으로 줄여줍니다."</strong></li>
          <li><strong>"소스/드레인 바닥면에서는 저유전율 매몰 산화막(BOX) 덕분에 기생 접합 커패시턴스($C_j$)가 70~80% 급감하여 회로의 동작 속도(RC Delay)가 20~30% 대폭 향상됩니다."</strong></li>
          <li><strong>"게이트 아래 채널 영역에서는 실리콘 박막이 5~7nm로 극도로 얇아 완전 공핍(Fully Depleted)되므로 공핍 커패시턴스($C_{dep}$)가 거의 0에 수렴하여, 이상적인 서브스레숄드 스윙($SS \\approx 60\\,\\text{mV/dec}$)을 달성합니다."</strong></li>
        </ul>
      </div>
      <div class="lecture-content">
        <!-- SVG 그래픽 다이어그램: SOI의 C_j 및 C_dep 동시 절감 메커니즘 -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [FD-SOI 소자 단면] 위치별 커패시턴스 동시 절감 메커니즘 (S/D 바닥 C_j 80% 절감 + 채널 C_dep ≈ 0 극소화)
          </div>
          <svg viewBox="0 0 780 430" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <defs>
              <linearGradient id="soiBothGate" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#475569"/>
                <stop offset="100%" stop-color="#334155"/>
              </linearGradient>
              <linearGradient id="soiBothBox" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#0284c7"/>
                <stop offset="100%" stop-color="#38bdf8"/>
              </linearGradient>
            </defs>

            <!-- Background Canvas -->
            <rect width="780" height="430" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

            <!-- Upper Half: FD-SOI Device Cross-section -->
            <!-- Base Substrate -->
            <rect x="50" y="160" width="680" height="70" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
            <text x="325" y="200" fill="#64748b" font-size="11" font-weight="600">하부 실리콘 지지 기판 (Base Substrate)</text>

            <!-- BOX Layer -->
            <rect x="50" y="115" width="680" height="45" fill="url(#soiBothBox)" stroke="#0284c7" stroke-width="1.5"/>
            <text x="270" y="142" fill="#ffffff" font-size="12" font-weight="800">🛡️ 매몰 산화막 (BOX Layer, SiO₂)</text>

            <!-- Source & Drain -->
            <rect x="50" y="55" width="160" height="60" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
            <text x="95" y="90" fill="#34d399" font-size="12" font-weight="800">Source (N⁺)</text>

            <rect x="570" y="55" width="160" height="60" fill="#1e293b" stroke="#10b981" stroke-width="1.5"/>
            <text x="615" y="90" fill="#34d399" font-size="12" font-weight="800">Drain (N⁺)</text>

            <!-- Ultra-thin Channel (5~7nm) -->
            <rect x="210" y="85" width="360" height="30" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-dasharray="3 3"/>
            <text x="290" y="105" fill="#38bdf8" font-size="11" font-weight="800">초박막 실리콘 채널 (T_si ≈ 6nm, Fully Depleted)</text>

            <!-- Gate -->
            <rect x="290" y="40" width="200" height="22" fill="url(#soiBothGate)" stroke="#94a3b8" stroke-width="1"/>
            <rect x="290" y="62" width="200" height="4" fill="#f59e0b"/>
            <text x="375" y="55" fill="#ffffff" font-size="11" font-weight="700">Gate</text>
            <text x="365" y="75" fill="#f59e0b" font-size="9" font-weight="800">C_ox</text>

            <!-- Red Callouts for C_j reduction on Source/Drain bottoms -->
            <path d="M 130 115 L 130 135" stroke="#f43f5e" stroke-width="2.5" marker-end="url(#arrowRed)"/>
            <rect x="55" y="120" width="150" height="22" rx="4" fill="rgba(244, 63, 94, 0.3)" stroke="#f43f5e"/>
            <text x="65" y="135" fill="#fecaca" font-size="10" font-weight="800">C_j 80% 급감! (속도↑)</text>

            <path d="M 650 115 L 650 135" stroke="#f43f5e" stroke-width="2.5"/>
            <rect x="575" y="120" width="150" height="22" rx="4" fill="rgba(244, 63, 94, 0.3)" stroke="#f43f5e"/>
            <text x="585" y="135" fill="#fecaca" font-size="10" font-weight="800">C_j 80% 급감! (속도↑)</text>


            <!-- Lower Half: Detailed Dual Effect Breakdown Cards -->
            <!-- Card 1: 기생 접합 커패시턴스 C_j 절감 -->
            <rect x="50" y="245" width="330" height="170" rx="6" fill="rgba(244, 63, 94, 0.08)" stroke="#f43f5e" stroke-width="1.2"/>
            <text x="65" y="270" fill="#f43f5e" font-size="12.5" font-weight="800">① 기생 접합 커패시턴스 (C_j) 절감</text>
            <text x="65" y="292" fill="#cbd5e1" font-size="11">• <strong>적용 부위</strong>: 소스 / 드레인 바닥면</text>
            <text x="65" y="312" fill="#cbd5e1" font-size="10.5">• <strong>원리</strong>: 바닥이 실리콘 대신 두껍고 유전율 낮은</text>
            <text x="75" y="330" fill="#fca5a5" font-size="10.5">매몰 산화막(BOX)에 닿음 (C_j = ε_ox·A / T_BOX)</text>
            <text x="65" y="352" fill="#cbd5e1" font-size="10.5">• <strong>결과</strong>: 기생 정전용량 <strong>70~80% 대폭 감소</strong></text>
            <text x="65" y="375" fill="#10b981" font-size="11" font-weight="800">➔ 회로 스위칭 동작 속도(Speed) 20~30% 향상!</text>
            <text x="75" y="395" fill="#cbd5e1" font-size="10.5">동적 충방전 소비 전력(P = C_j · V² · f) 급감</text>

            <!-- Card 2: 공핍 커패시턴스 C_dep 절감 -->
            <rect x="400" y="245" width="330" height="170" rx="6" fill="rgba(56, 189, 248, 0.08)" stroke="#38bdf8" stroke-width="1.2"/>
            <text x="415" y="270" fill="#38bdf8" font-size="12.5" font-weight="800">② 공핍 커패시턴스 (C_dep) 절감</text>
            <text x="415" y="292" fill="#cbd5e1" font-size="11">• <strong>적용 부위</strong>: 게이트 아래 채널 실리콘</text>
            <text x="415" y="312" fill="#cbd5e1" font-size="10.5">• <strong>원리</strong>: 실리콘 박막이 6nm로 극도로 얇아 채널 전체가</text>
            <text x="425" y="330" fill="#93c5fd" font-size="10.5">완전 공핍(Fully Depleted)되어 C_dep ≈ 0 수렴</text>
            <text x="415" y="352" fill="#cbd5e1" font-size="10.5">• <strong>결과</strong>: 바디 팩터 m = 1 + C_dep/C_ox ➔ <strong>1.0 달성</strong></text>
            <text x="415" y="375" fill="#38bdf8" font-size="11" font-weight="800">➔ 서브스레숄드 스윙 SS ≈ 60 mV/dec 극한 달성!</text>
            <text x="425" y="395" fill="#cbd5e1" font-size="10.5">스위칭 칼날화로 저전압·초저누설(I_off 차단) 완성</text>
          </svg>
        </div>

        <h3>1. 결론: "SOI는 둘 다 획기적으로 줄여줍니다!"</h3>
        <p>반도체 엔지니어링 관점에서 <strong>SOI(특히 Fully Depleted SOI, FD-SOI)의 가장 위대한 점은 소자의 서로 다른 두 위치에서 발생하는 두 커패시턴스를 동시에 박멸한다는 것</strong>입니다.</p>
        <p>어느 하나만 줄이는 것이 아니라, <strong>S/D에서는 기생 접합 커패시턴스($C_j$)를 줄이고, 채널에서는 공핍 커패시턴스($C_{dep}$)를 줄여</strong> 각기 다른 치명적인 장점을 제공합니다.</p>

        <h3>2. 두 커패시턴스 절감 메커니즘 정밀 비교</h3>
        <table class="data-table">
          <thead>
            <tr>
              <th>구분</th>
              <th>① 기생 접합 커패시턴스 ($C_j$) 절감</th>
              <th>② 공핍 커패시턴스 ($C_{dep}$) 절감</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>절감 부위</strong></td>
              <td><strong>소스(Source) 및 드레인(Drain) 바닥면</strong></td>
              <td><strong>게이트 산화막 바로 아래 채널(Channel)</strong></td>
            </tr>
            <tr>
              <td><strong>벌크 소자의 문제</strong></td>
              <td>S/D 바닥이 실리콘 기판($\kappa_{si} \approx 11.9$)과 접합하여 거대한 기생 정전용량 형성</td>
              <td>기판이 두꺼워 게이트 전압 인가 시 깊은 공핍층 형성 ($C_{dep} > 0$)</td>
            </tr>
            <tr>
              <td><strong>SOI의 절감 원리</strong></td>
              <td>바닥에 유전율 낮고 두꺼운 매몰 산화막(BOX, $\kappa_{ox} \approx 3.9$)이 맞닿음</td>
              <td>실리콘 박막이 5~7nm로 극도로 얇아 채널 전체가 100% 완전 공핍(Fully Depleted)</td>
            </tr>
            <tr>
              <td><strong>수식적 변화</strong></td>
              <td>$$C_j = \frac{\epsilon_{ox} A}{T_{BOX}} \ll \frac{\epsilon_{si} A}{W_{dep}} \quad (\mathbf{80\% \text{ 급감}})$$</td>
              <td>$$C_{dep} \approx 0 \implies m = 1 + \frac{C_{dep}}{C_{ox}} \approx \mathbf{1.0}$$</td>
            </tr>
            <tr>
              <td><strong>최종 효과</strong></td>
              <td>
                • $RC$ 지연 감소로 **동작 속도 20~30% 향상**<br>
                • 동적 충방전 전력($P = C_j V^2 f$) 절감
              </td>
              <td>
                • 서브스레숄드 스윙 **$SS \approx 60\,\text{mV/dec}$ 이론적 한계 달성**<br>
                • 오프 누설($I_{off}$) 차단 및 문턱전압 롤오프 방어
              </td>
            </tr>
          </tbody>
        </table>

        <h3>3. 직관적인 일타 마스터 비유: '자동차 경량화'와 '칼날 스위치'</h3>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>기생 접합 커패시턴스($C_j$) 절감 = '자동차 휠의 무게를 80% 깎아낸 경량화'</strong>:
            <br>- 바퀴(드레인)를 굴릴 때마다 회로가 짊어져야 했던 무거운 기생 짐($C_j$)을 덜어내어, <strong>차가 시속 20~30% 더 빠르게 가속(초고속 동작)</strong>하고 기름(충방전 전력)을 덜 먹습니다.
          </li>
          <li><strong>공핍 커패시턴스($C_{dep}$) 절감 = '헐렁한 고무 스위치를 칼날 스위치로 교체'</strong>:
            <br>- 게이트가 채널을 켤 때 쓸데없이 기판 내부로 힘을 낭비하던 고무 탄성($C_{dep}$)을 0으로 만들어, <strong>살짝만 눌러도 즉시 딸깍하고 켜지고 꺼지는 칼날 같은 스위칭($SS = 60$)</strong>을 완성합니다.
          </li>
        </ul>
      </div>
    </section>
"""

    # 3. Renumber existing nav-items (01 -> 02, ..., 28 -> 29)
    nav_pattern = r'(<ul class="nav-list" id="navList">)([\s\S]*?)(</ul>)'
    match = re.search(nav_pattern, html)
    if match:
        old_nav_items = match.group(2)
        shifted_nav = old_nav_items
        for i in range(28, 0, -1):
            old_str = f'<span class="nav-num">{i:02d}</span>'
            new_str = f'<span class="nav-num">{i+1:02d}</span>'
            shifted_nav = shifted_nav.replace(old_str, new_str)
            old_href = f'href="#q-{i:02d}"'
            new_href = f'href="#q-{i+1:02d}"'
            shifted_nav = shifted_nav.replace(old_href, new_href)
        
        updated_nav_list = match.group(1) + "\n" + new_nav_item + shifted_nav + match.group(3)
        html = html[:match.start()] + updated_nav_list + html[match.end():]

    # 4. Renumber existing sections (q-01 -> q-02, ..., q-28 -> q-29)
    for i in range(28, 0, -1):
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
        r"""<p class="main-desc">질문자님께서 질문하신 문장 그대로 좌측 탭 제목과 본문 제목을 구성하였습니다. 최상단에는 가장 최근 질문인 <strong>'soi는 기생접합커패시턴스를 줄여줘 공핍커패시턴스를 줄여줘?'</strong>가 1번으로 위치합니다.</p>""",
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
