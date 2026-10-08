import os
import re

def update_html():
    file_path = r"C:\Work\반도체3\result\261007_v1.0\index.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. New Q01 nav-item
    new_nav_item = """      <li class="nav-item"><a href="#q-01" class="nav-link"><span class="nav-num">01</span><span class="nav-text">halo implant에서 모서리 도핑 농도 높여놓으면 depletion이 가로막히는 로직</span></a></li>\n"""

    # 2. New Q01 Section with SVG
    new_q01_section = """    <!-- Q 01 : halo implant에서 모서리 도핑 농도 높여놓으면 depletion이 가로막히는 로직 -->
    <section class="topic-section latest-card-highlight" id="q-01">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q 01</span>
          <span class="latest-tag">⭐ 가장 최근 질문 (1번 배치)</span>
          <h2 class="topic-title">halo implant에서 모서리 도핑 농도 높여놓으면 depletion이 가로막히는 로직</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">면접 대비 3~4줄 핵심 요약</span>
        <ul class="summary-list">
          <li><strong>"전하 중성 원리($Q^+ = Q^-$)에 의해, 드레인 양이온($N^+$)에서 뿜어져 나오는 전기력선은 기판 쪽 음이온($B^-$)을 만나야만 종단(Terminate)되어 전기장이 0으로 소멸하고 공핍층 전진이 멈춥니다."</strong></li>
          <li><strong>"모서리에 헤일로($P^+$)를 고농도로 도핑해 두면 억셉터 음전하 밀도가 100~1,000배 밀집되어, 인가된 드레인 전압을 단 10~20nm의 극도로 얇은 거리 안에서 모두 상쇄(소화)하는 '단단한 전하 방패벽'이 형성됩니다."</strong></li>
          <li><strong>"푸아송 방정식($\\frac{d\\mathcal{E}}{dx} = \\frac{qN_A}{\\epsilon}$)에 의해 전기장 감쇄율이 수직에 가깝게 가파르게 꺾이며, 공핍층 폭 공식($W_{dep} \\propto 1/\\sqrt{N_A}$)에 따라 공핍층 경계면이 모서리 벽면에서 더 이상 전진하지 못하고 물리적으로 가로막히게 됩니다."</strong></li>
        </ul>
      </div>
      <div class="lecture-content">
        <!-- SVG 그래픽 다이어그램: 전기력선 종단과 공핍층 가로막힘(정지) 메커니즘 -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [전기력선 종단 원리] 저농도 기판(전기력선 관통 & 공핍층 침투) vs 헤일로 고농도(음전하 방패에 막혀 공핍층 정지)
          </div>
          <svg viewBox="0 0 780 420" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <defs>
              <linearGradient id="q1DrainGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#0284c7"/>
                <stop offset="100%" stop-color="#38bdf8"/>
              </linearGradient>
              <linearGradient id="q1HaloWallGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#7c3aed"/>
                <stop offset="100%" stop-color="#a855f7"/>
              </linearGradient>
              <linearGradient id="q1DepDeep" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="rgba(239, 68, 68, 0.25)"/>
                <stop offset="100%" stop-color="rgba(239, 68, 68, 0.05)"/>
              </linearGradient>
            </defs>

            <!-- Background -->
            <rect width="780" height="420" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
            <line x1="390" y1="20" x2="390" y2="400" stroke="#334155" stroke-dasharray="4 4" stroke-width="1.5"/>

            <!-- ================= LEFT: LOW DOPING (No Halo) ================= -->
            <text x="30" y="38" fill="#f43f5e" font-size="13" font-weight="800">❌ [1] 저농도 모서리 (음전하 밀도 희박, N_A 낮음)</text>
            
            <!-- Drain Box -->
            <rect x="30" y="60" width="85" height="180" rx="6" fill="url(#q1DrainGrad)" stroke="#38bdf8" stroke-width="1.2"/>
            <text x="45" y="85" fill="#ffffff" font-size="12" font-weight="800">드레인 (N⁺)</text>
            <text x="40" y="105" fill="#e0f2fe" font-size="10">고정 양전하 (+)</text>
            <!-- Donor plus symbols -->
            <text x="50" y="135" fill="#ffffff" font-size="18" font-weight="900">⊕ ⊕</text>
            <text x="50" y="165" fill="#ffffff" font-size="18" font-weight="900">⊕ ⊕</text>
            <text x="50" y="195" fill="#ffffff" font-size="18" font-weight="900">⊕ ⊕</text>

            <!-- Depletion Region extending far -->
            <rect x="115" y="60" width="240" height="180" rx="4" fill="url(#q1DepDeep)" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3 3"/>
            <text x="140" y="85" fill="#f87171" font-size="11" font-weight="700">공핍층(Depletion) 길게 확장 ──►</text>

            <!-- Sparse Acceptor minus symbols -->
            <circle cx="160" cy="130" r="12" fill="#1e293b" stroke="#64748b"/>
            <text x="154" y="136" fill="#94a3b8" font-size="16" font-weight="900">⊖</text>
            <circle cx="240" cy="170" r="12" fill="#1e293b" stroke="#64748b"/>
            <text x="234" y="176" fill="#94a3b8" font-size="16" font-weight="900">⊖</text>
            <circle cx="320" cy="120" r="12" fill="#1e293b" stroke="#64748b"/>
            <text x="314" y="126" fill="#94a3b8" font-size="16" font-weight="900">⊖</text>

            <!-- Long Electric field lines penetrating -->
            <path d="M 115 130 L 310 120" stroke="#f43f5e" stroke-width="2.5" marker-end="url(#arrowRed)"/>
            <path d="M 115 160 L 230 170" stroke="#f43f5e" stroke-width="2.5"/>
            <line x1="115" y1="190" x2="350" y2="190" stroke="#f43f5e" stroke-width="2.5"/>
            <text x="135" y="225" fill="#fca5a5" font-size="11" font-weight="700">전기력선이 끝없이 소스 쪽으로 질주!</text>

            <!-- Explanation box Left -->
            <rect x="30" y="260" width="330" height="135" rx="6" fill="rgba(244, 63, 94, 0.08)" stroke="#f43f5e" stroke-width="1"/>
            <text x="40" y="282" fill="#f43f5e" font-size="11.5" font-weight="700">⚠️ 왜 공핍층이 안 멈추는가?</text>
            <text x="40" y="303" fill="#cbd5e1" font-size="10.5">• 전기력선은 음전하(⊖)를 만나야만 소멸함</text>
            <text x="40" y="322" fill="#cbd5e1" font-size="10.5">• 기판 농도가 낮아 음이온(B⁻)이 듬성듬성 있음</text>
            <text x="40" y="341" fill="#cbd5e1" font-size="10.5">• 드레인 전하량을 채우기 위해 공핍층이 100nm 이상</text>
            <text x="40" y="360" fill="#f87171" font-size="10.5">• 끝없이 파고들어 소스와 충돌 (펀치스루 발생!)</text>


            <!-- ================= RIGHT: HIGH HALO DOPING ================= -->
            <text x="420" y="38" fill="#10b981" font-size="13" font-weight="800">✅ [2] 헤일로 고농도 모서리 (빽빽한 음전하 방패벽!)</text>
            
            <!-- Drain Box -->
            <rect x="420" y="60" width="85" height="180" rx="6" fill="url(#q1DrainGrad)" stroke="#38bdf8" stroke-width="1.2"/>
            <text x="435" y="85" fill="#ffffff" font-size="12" font-weight="800">드레인 (N⁺)</text>
            <text x="430" y="105" fill="#e0f2fe" font-size="10">고정 양전하 (+)</text>
            <text x="440" y="135" fill="#ffffff" font-size="18" font-weight="900">⊕ ⊕</text>
            <text x="440" y="165" fill="#ffffff" font-size="18" font-weight="900">⊕ ⊕</text>
            <text x="440" y="195" fill="#ffffff" font-size="18" font-weight="900">⊕ ⊕</text>

            <!-- Dense Halo Wall (Shield) -->
            <rect x="505" y="60" width="65" height="180" rx="4" fill="url(#q1HaloWallGrad)" stroke="#a855f7" stroke-width="1.5"/>
            <text x="510" y="82" fill="#ede9fe" font-size="10.5" font-weight="800">Halo (P⁺)</text>
            
            <!-- Ultra dense negative ions -->
            <text x="515" y="115" fill="#ffffff" font-size="15" font-weight="900">⊖ ⊖</text>
            <text x="515" y="140" fill="#ffffff" font-size="15" font-weight="900">⊖ ⊖</text>
            <text x="515" y="165" fill="#ffffff" font-size="15" font-weight="900">⊖ ⊖</text>
            <text x="515" y="190" fill="#ffffff" font-size="15" font-weight="900">⊖ ⊖</text>
            <text x="515" y="215" fill="#ffffff" font-size="15" font-weight="900">⊖ ⊖</text>

            <!-- Short electric field lines absorbed immediately -->
            <path d="M 505 110 L 525 110" stroke="#fbbf24" stroke-width="3"/>
            <polygon points="525,110 520,106 520,114" fill="#fbbf24"/>
            <path d="M 505 135 L 525 135" stroke="#fbbf24" stroke-width="3"/>
            <polygon points="525,135 520,131 520,139" fill="#fbbf24"/>
            <path d="M 505 160 L 525 160" stroke="#fbbf24" stroke-width="3"/>
            <polygon points="525,160 520,156 520,164" fill="#fbbf24"/>
            <path d="M 505 185 L 525 185" stroke="#fbbf24" stroke-width="3"/>
            <polygon points="525,185 520,181 520,189" fill="#fbbf24"/>

            <!-- STOP Wall Barrier -->
            <rect x="575" y="75" width="180" height="150" rx="6" fill="rgba(16, 185, 129, 0.12)" stroke="#10b981" stroke-width="1.5"/>
            <text x="590" y="105" fill="#34d399" font-size="12" font-weight="800">🛑 공핍층 전진 불가 (STOP!)</text>
            <text x="590" y="130" fill="#cbd5e1" font-size="11">• 전기력선 전원 종단 (E = 0)</text>
            <text x="590" y="152" fill="#cbd5e1" font-size="11">• 15nm 벽면에서 완전 정지!</text>
            <text x="590" y="174" fill="#38bdf8" font-size="11" font-weight="700">W_dep ∝ 1/√N_A (1/10 압축)</text>
            <text x="590" y="200" fill="#34d399" font-size="11" font-weight="800">🛡️ 지하 P-Sub 완벽 수호</text>

            <!-- Explanation box Right -->
            <rect x="420" y="260" width="335" height="135" rx="6" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1"/>
            <text x="430" y="282" fill="#10b981" font-size="11.5" font-weight="700">💡 공핍층이 가로막히는 물리 로직:</text>
            <text x="430" y="303" fill="#cbd5e1" font-size="10.5">• 전하 중성 법칙: Q⁺(드레인) = Q⁻(헤일로 음이온)</text>
            <text x="430" y="322" fill="#cbd5e1" font-size="10.5">• 음전하가 빽빽하여 단 15nm 두께로 Q⁺ 전량 상쇄</text>
            <text x="430" y="341" fill="#cbd5e1" font-size="10.5">• 푸아송 적분 완료: 드레인 전압(V_D)이 코앞에서 전액 소진</text>
            <text x="430" y="360" fill="#34d399" font-size="10.5">• 전기장이 0이 되므로 공핍층이 더 나아갈 구동력 소멸!</text>
          </svg>
        </div>

        <h3>1. 전하 중성 원리(Charge Neutrality)와 '필요 체적'의 법칙</h3>
        <p>드레인에 역방향 전압($V_D$)을 걸면 드레인 측 $N^+$ 영역에서는 전자가 빠져나가 고정된 양이온($\text{Donor } N_D^+$)이 남고, 기판 쪽에서는 정공이 밀려나 고정된 음이온($\text{Acceptor } N_A^-$)이 남습니다.</p>
        <div class="formula-box">
          $$Q_{\text{depletion}}^+ = Q_{\text{depletion}}^- \implies q \cdot N_D \cdot W_{dep,n} = q \cdot \mathbf{N_A} \cdot \mathbf{W_{dep,p}}$$
        </div>
        <p>기판 쪽으로 공핍층이 파고드는 거리($W_{dep,p}$)는 다음 공식으로 결정됩니다:</p>
        <div class="formula-box">
          $$W_{dep,p} = \left(\frac{N_D}{\mathbf{N_A}}\right) \cdot W_{dep,n}$$
        </div>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>저농도 모서리 ($N_A = 10^{15}\,\text{cm}^{-3}$)</strong>: 드레인의 막대한 양전하($N_D \approx 10^{20}$)를 상쇄할 음전하를 모으려면 실리콘을 깊고 넓게 파고들어야 하므로, 공핍층이 소스 코앞까지 수백 나노미터를 침투합니다.</li>
          <li><strong>헤일로 고농도 모서리 ($N_A = 10^{18}\,\text{cm}^{-3}$)</strong>: 모서리 체적 안에 음전하($B^-$)가 1,000배 빽빽하게 깔려 있습니다. 따라서 <strong>단 10~20nm의 얇은 껍질 두께만으로도 드레인 양전하를 100% 완벽히 상쇄</strong>하므로, 공핍층이 더 이상 깊이 파고들 물리적 이유가 사라져 그 자리에서 정지합니다.</li>
        </ul>

        <h3>2. 가우스 법칙(Gauss's Law)과 전기력선 종단(Termination) 로직</h3>
        <p>전기력선(Electric Flux Line, $\mathcal{D}$)은 양전하에서 출발하여 음전하에서만 끝납니다($\nabla \cdot \mathcal{D} = \rho$).</p>
        <div class="formula-box">
          $$\frac{d\mathcal{E}}{dx} = \frac{\rho(x)}{\epsilon_{si}} = \frac{q \cdot \mathbf{N_A}}{\epsilon_{si}}$$
        </div>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li>전기장의 감쇄 기울기($d\mathcal{E}/dx$)는 <strong>도핑 농도 $N_A$에 직접 비례</strong>합니다.</li>
          <li>헤일로 모서리의 높은 $N_A$는 전기력선에 있어 <strong>'초고밀도 흡수 방탄벽'</strong>과 같습니다. 드레인에서 출발한 모든 전기력선이 모서리 벽면에 닿자마자 대기하고 있던 $B^-$ 이온들과 1:1로 결합하여 <strong>빛의 속도로 종단(Terminate)</strong>됩니다.</li>
          <li>전기력선이 남김없이 종단되면 전기장($\mathcal{E}$)은 즉시 $0\,\text{V/cm}$이 되며, 전계가 0인 지점이 바로 <strong>'공핍층의 끝 경계면(Depletion Edge)'</strong>이 되므로 공핍층은 벽면에 가로막혀 멈추게 됩니다.</li>
        </ul>

        <h3>3. 푸아송 적분과 전압 소진 거리 ($W_{dep} \propto 1/\sqrt{N_A}$)</h3>
        <p>인가된 드레인 전압($V_D + V_{bi}$)은 전기장 아래의 적분 면적으로 모두 소진되어야 공핍층이 멈춥니다:</p>
        <div class="formula-box">
          $$V_D + V_{bi} = \int_{0}^{W_{dep}} \mathcal{E}(x) dx \approx \frac{q \cdot \mathbf{N_A}}{2\epsilon_{si}} W_{dep,p}^2 \implies \mathbf{W_{dep,p} = \sqrt{\frac{2\epsilon_{si}(V_D + V_{bi})}{q \cdot N_A}}}$$
        </div>
        <p>헤일로를 통해 모서리 농도($N_A$)를 100배 올리면 전압 흡수 효율이 극대화되어, 공핍층 필요 폭($W_{dep}$)은 $\sqrt{100} = 10$배, 즉 <strong>1/10 수준으로 압축</strong>되어 모서리 입구에서 전압이 100% 소진되고 차단됩니다.</p>

        <h3>4. 직관적 마스터 비유: '세금 징수관'과 '부자 마을'</h3>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>세금 징수관 (드레인 전압 $V_D$)</strong>: "나는 1,000억 원의 음전하 세금을 걷을 때까지 앞으로 계속 진격하겠다!"</li>
          <li><strong>저농도 기판 (가난한 빈민촌)</strong>: 집집마다 가진 돈(음이온)이 100원뿐이라, 징수관이 세금을 다 채우기 위해 옆 동네(소스)까지 끝없이 쳐들어갑니다 $\rightarrow$ <strong>펀치스루 붕괴</strong>.</li>
          <li><strong>헤일로 고농도 모서리 (재벌 마을)</strong>: 마을 입구 3개 저택에서 1,000억 원을 한 번에 다 내어줍니다. 징수관은 마을 골목 안쪽(지하 기판)으로 더 들어갈 필요가 없어 <strong>입구에서 즉시 발길을 돌리고 멈춥니다</strong> $\rightarrow$ <strong>공핍층 완전 가로막힘!</strong></li>
        </ul>
      </div>
    </section>
"""

    # 3. Renumber existing nav-items (01 -> 02, ..., 24 -> 25)
    nav_pattern = r'(<ul class="nav-list" id="navList">)([\s\S]*?)(</ul>)'
    match = re.search(nav_pattern, html)
    if match:
        old_nav_items = match.group(2)
        shifted_nav = old_nav_items
        for i in range(24, 0, -1):
            old_str = f'<span class="nav-num">{i:02d}</span>'
            new_str = f'<span class="nav-num">{i+1:02d}</span>'
            shifted_nav = shifted_nav.replace(old_str, new_str)
            old_href = f'href="#q-{i:02d}"'
            new_href = f'href="#q-{i+1:02d}"'
            shifted_nav = shifted_nav.replace(old_href, new_href)
        
        updated_nav_list = match.group(1) + "\n" + new_nav_item + shifted_nav + match.group(3)
        html = html[:match.start()] + updated_nav_list + html[match.end():]

    # 4. Renumber existing sections (q-01 -> q-02, ..., q-24 -> q-25)
    for i in range(24, 0, -1):
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
        r"""<p class="main-desc">질문자님께서 질문하신 문장 그대로 좌측 탭 제목과 본문 제목을 구성하였습니다. 최상단에는 가장 최근 질문인 <strong>'halo implant에서 모서리 도핑 농도 높여놓으면 depletion이 가로막히는 로직'</strong>이 1번으로 위치합니다.</p>""",
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
