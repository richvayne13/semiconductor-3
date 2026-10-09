import os
import re

def update_html():
    file_path = r"C:\Work\반도체3\result\261007_v1.0\index.html"
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. New Q01 nav-item
    new_nav_item = """      <li class="nav-item"><a href="#q-01" class="nav-link"><span class="nav-num">01</span><span class="nav-text">petdc는 무슨 공정 말하는 걸까?</span></a></li>\n"""

    # 2. New Q01 Section with SVG
    new_q01_section = """    <!-- Q 01 : petdc는 무슨 공정 말하는 걸까? -->
    <section class="topic-section latest-card-highlight" id="q-01">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q 01</span>
          <span class="latest-tag">⭐ 가장 최근 질문 (1번 배치)</span>
          <h2 class="topic-title">petdc는 무슨 공정 말하는 걸까?</h2>
        </div>
      </div>
      <div class="interview-summary-card">
        <span class="summary-tag">면접 대비 3~4줄 핵심 요약</span>
        <ul class="summary-list">
          <li><strong>"반도체 팹(FAB) 실무와 양산 기술에서 'PETDC'는 반도체 전공정을 구성하는 '5대 핵심 단위 공정 모듈'의 영문 첫 글자를 조합한 현업 약어입니다."</strong></li>
          <li><strong>"P(Photo: 노광/패터닝), E(Etch: 식각), T(Thin Film: 박막 증착), D(Diffusion: 확산/이온주입/열처리), C(CMP/Cleaning: 평탄화 및 세정)의 5개 엔지니어링 파트로 나뉩니다."</strong></li>
          <li><strong>"교과서의 '8대 공정'을 팹 장비군과 라인 운영 체계에 맞춰 5대 단위 모듈로 묶은 현업 표준 분류 체계이며, 웨이퍼에 박막을 깔고(T) 패턴을 그리고(P) 깎아내며(E) 씻어내고(C) 불순물을 주입(D)하는 수백 회의 순환 루프로 반도체가 완성됩니다."</strong></li>
        </ul>
      </div>
      <div class="lecture-content">
        <!-- SVG 그래픽 다이어그램: 반도체 5대 핵심 공정 모듈 P-E-T-D-C 순환 루프 -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [반도체 팹 5대 단위 모듈] P-E-T-D-C 아키텍처 및 웨이퍼 제조 순환 루프(Cycle)
          </div>
          <svg viewBox="0 0 780 440" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <defs>
              <linearGradient id="pGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#3b82f6"/>
                <stop offset="100%" stop-color="#1d4ed8"/>
              </linearGradient>
              <linearGradient id="eGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ef4444"/>
                <stop offset="100%" stop-color="#b91c1c"/>
              </linearGradient>
              <linearGradient id="tGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#10b981"/>
                <stop offset="100%" stop-color="#047857"/>
              </linearGradient>
              <linearGradient id="dGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#f59e0b"/>
                <stop offset="100%" stop-color="#b45309"/>
              </linearGradient>
              <linearGradient id="cGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#8b5cf6"/>
                <stop offset="100%" stop-color="#6d28d9"/>
              </linearGradient>
            </defs>

            <!-- Background Canvas -->
            <rect width="780" height="440" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

            <!-- Top Title Box -->
            <rect x="230" y="20" width="320" height="35" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.2"/>
            <text x="245" y="43" fill="#38bdf8" font-size="13" font-weight="800">🏭 FAB 양산기술 5대 공정 모듈 (P·E·T·D·C)</text>

            <!-- 5 Process Cards in a Flow Row -->
            <!-- 1. P Card -->
            <rect x="25" y="75" width="135" height="185" rx="8" fill="rgba(59, 130, 246, 0.08)" stroke="#3b82f6" stroke-width="1.5"/>
            <rect x="25" y="75" width="135" height="34" rx="8" fill="url(#pGrad)"/>
            <text x="42" y="98" fill="#ffffff" font-size="14" font-weight="900">P : Photo</text>
            <text x="35" y="128" fill="#93c5fd" font-size="11" font-weight="700">📷 포토 공정</text>
            <text x="35" y="148" fill="#cbd5e1" font-size="10">• 노광 (Lithography)</text>
            <text x="35" y="165" fill="#cbd5e1" font-size="10">• PR 도포 / 베이크</text>
            <text x="35" y="182" fill="#cbd5e1" font-size="10">• EUV / ArFi 노광</text>
            <text x="35" y="199" fill="#cbd5e1" font-size="10">• 현상 (Develop)</text>
            <text x="35" y="222" fill="#60a5fa" font-size="10" font-weight="700">"회로 패턴 전사"</text>
            <text x="35" y="245" fill="#94a3b8" font-size="9">(공정의 꽃, 고난도)</text>

            <!-- Arrow 1 -->
            <path d="M 163 165 L 175 165" stroke="#475569" stroke-width="2"/>

            <!-- 2. E Card -->
            <rect x="175" y="75" width="135" height="185" rx="8" fill="rgba(239, 68, 68, 0.08)" stroke="#ef4444" stroke-width="1.5"/>
            <rect x="175" y="75" width="135" height="34" rx="8" fill="url(#eGrad)"/>
            <text x="195" y="98" fill="#ffffff" font-size="14" font-weight="900">E : Etch</text>
            <text x="185" y="128" fill="#fca5a5" font-size="11" font-weight="700">⚡ 식각 공정</text>
            <text x="185" y="148" fill="#cbd5e1" font-size="10">• 건식 식각 (Dry)</text>
            <text x="185" y="165" fill="#cbd5e1" font-size="10">• 플라즈마 RIE</text>
            <text x="185" y="182" fill="#cbd5e1" font-size="10">• 습식 식각 (Wet)</text>
            <text x="185" y="199" fill="#cbd5e1" font-size="10">• PR 스트립</text>
            <text x="185" y="222" fill="#f87171" font-size="10" font-weight="700">"불필요 막질 깎기"</text>
            <text x="185" y="245" fill="#94a3b8" font-size="9">(고선택비·비등방성)</text>

            <!-- Arrow 2 -->
            <path d="M 313 165 L 325 165" stroke="#475569" stroke-width="2"/>

            <!-- 3. T Card -->
            <rect x="325" y="75" width="135" height="185" rx="8" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1.5"/>
            <rect x="325" y="75" width="135" height="34" rx="8" fill="url(#tGrad)"/>
            <text x="335" y="98" fill="#ffffff" font-size="13.5" font-weight="900">T : Thin Film</text>
            <text x="335" y="128" fill="#6ee7b7" font-size="11" font-weight="700">🥞 박막 증착</text>
            <text x="335" y="148" fill="#cbd5e1" font-size="10">• CVD (화학 증착)</text>
            <text x="335" y="165" fill="#cbd5e1" font-size="10">• ALD (원자층 증착)</text>
            <text x="335" y="182" fill="#cbd5e1" font-size="10">• PVD (스퍼터링)</text>
            <text x="335" y="199" fill="#cbd5e1" font-size="10">• 절연막/금속막</text>
            <text x="335" y="222" fill="#34d399" font-size="10" font-weight="700">"박막 층층이 적층"</text>
            <text x="335" y="245" fill="#94a3b8" font-size="9">(두께 균일도·Step)</text>

            <!-- Arrow 3 -->
            <path d="M 463 165 L 475 165" stroke="#475569" stroke-width="2"/>

            <!-- 4. D Card -->
            <rect x="475" y="75" width="135" height="185" rx="8" fill="rgba(245, 158, 11, 0.08)" stroke="#f59e0b" stroke-width="1.5"/>
            <rect x="475" y="75" width="135" height="34" rx="8" fill="url(#dGrad)"/>
            <text x="483" y="98" fill="#ffffff" font-size="13.5" font-weight="900">D : Diffusion</text>
            <text x="485" y="128" fill="#fcd34d" font-size="11" font-weight="700">♨️ 확산/이온주입</text>
            <text x="485" y="148" fill="#cbd5e1" font-size="10">• 이온주입 (Implant)</text>
            <text x="485" y="165" fill="#cbd5e1" font-size="10">• 열산화 (Oxidation)</text>
            <text x="485" y="182" fill="#cbd5e1" font-size="10">• 어닐링 (RTA)</text>
            <text x="485" y="199" fill="#cbd5e1" font-size="10">• 도펀트 활성화</text>
            <text x="485" y="222" fill="#fbbf24" font-size="10" font-weight="700">"전기적 성질 부여"</text>
            <text x="485" y="245" fill="#94a3b8" font-size="9">(P/N 도핑·접합 형성)</text>

            <!-- Arrow 4 -->
            <path d="M 613 165 L 625 165" stroke="#475569" stroke-width="2"/>

            <!-- 5. C Card -->
            <rect x="625" y="75" width="130" height="185" rx="8" fill="rgba(139, 92, 246, 0.08)" stroke="#8b5cf6" stroke-width="1.5"/>
            <rect x="625" y="75" width="130" height="34" rx="8" fill="url(#cGrad)"/>
            <text x="635" y="98" fill="#ffffff" font-size="13" font-weight="900">C : CMP/Clean</text>
            <text x="635" y="128" fill="#c4b5fd" font-size="11" font-weight="700">🧼 평탄화/세정</text>
            <text x="635" y="148" fill="#cbd5e1" font-size="10">• 화학기계연마(CMP)</text>
            <text x="635" y="165" fill="#cbd5e1" font-size="10">• 웨이퍼 표면 평탄화</text>
            <text x="635" y="182" fill="#cbd5e1" font-size="10">• 습식 세정 (Wet)</text>
            <text x="635" y="199" fill="#cbd5e1" font-size="10">• 파티클 오염 제거</text>
            <text x="635" y="222" fill="#a78bfa" font-size="10" font-weight="700">"표면 갈고 씻기"</text>
            <text x="635" y="245" fill="#94a3b8" font-size="9">(포토 초점 심도 사수)</text>


            <!-- Lower Section: Why PETDC? Explanation Cards -->
            <rect x="25" y="280" width="730" height="140" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#334155" stroke-width="1.2"/>
            <text x="40" y="306" fill="#38bdf8" font-size="12.5" font-weight="800">💡 왜 교과서의 '8대 공정' 대신 현업에서는 'PETDC 5대 공정'으로 부를까?</text>
            
            <text x="40" y="330" fill="#cbd5e1" font-size="11">• <strong>1) 장비군 및 공정 기술 조직 일치</strong>: 팹(FAB)의 엔지니어 팀은 포토팀(P), 식각팀(E), 박막팀(T), 디퓨전팀(D), CMP/세정팀(C)으로 운영됨</text>
            <text x="40" y="352" fill="#cbd5e1" font-size="11">• <strong>2) 무한 순환 루프(Cycle)</strong>: 반도체는 1회 통과가 아니라 [박막(T) ➔ 포토(P) ➔ 식각(E) ➔ 세정/CMP(C) ➔ 이온주입(D)]을 수백 회 반복하여 완성</text>
            <text x="40" y="374" fill="#cbd5e1" font-size="11">• <strong>3) 장비/기술 오타 주의</strong>: 간혹 <strong>PECVD</strong>(플라즈마 화학기상증착)를 잘못 표기한 오타인 경우도 있으므로 문맥에 맞게 판단 필수</text>
            <text x="40" y="398" fill="#10b981" font-size="11.5" font-weight="800">➔ 결론: "PETDC = 삼성전자 / SK하이닉스 팹 현업에서 분류하는 5대 단위 핵심 공정 모듈!"</text>
          </svg>
        </div>

        <h3>1. 'PETDC'의 실체: 반도체 팹(FAB) 5대 핵심 공정 모듈</h3>
        <p>반도체 취업 준비나 현업 엔지니어들 사이에서 쓰이는 <strong>'PETDC'</strong>는 반도체 전공정을 이루는 <strong>5대 단위 공정(Unit Process Module)</strong>의 머리글자를 모은 현업 약어입니다:</p>
        
        <table class="data-table">
          <thead>
            <tr>
              <th>약어</th>
              <th>공정명 (Full Name)</th>
              <th>주요 역할 및 핵심 장비/기술</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>P</strong></td>
              <td><strong>Photo (포토 공정, Photolithography)</strong></td>
              <td>웨이퍼 위에 감광액(PR)을 바르고 빛(EUV, ArFi)을 쪼여 회로 설계 패턴을 그리는 공정</td>
            </tr>
            <tr>
              <td><strong>E</strong></td>
              <td><strong>Etch (식각 공정, Etching)</strong></td>
              <td>포토로 전사된 PR 패턴을 마스크 삼아, 불필요한 막질을 플라즈마(건식 RIE)로 깎아내는 공정</td>
            </tr>
            <tr>
              <td><strong>T</strong></td>
              <td><strong>Thin Film (박막 공정, Deposition)</strong></td>
              <td>웨이퍼 표면에 절연막이나 전도성 금속막을 CVD, ALD, PVD 기술로 균일하게 덮는 공정</td>
            </tr>
            <tr>
              <td><strong>D</strong></td>
              <td><strong>Diffusion (확산 / 이온주입 / 열처리)</strong></td>
              <td>웨이퍼에 불순물(도펀트)을 주입(Implant)하고 고온 Furnace/RTA로 열처리하여 p/n 접합을 만드는 공정</td>
            </tr>
            <tr>
              <td><strong>C</strong></td>
              <td><strong>CMP / Cleaning (화학기계연마 & 세정)</strong></td>
              <td>단차가 생긴 표면을 평탄화(CMP)하고, 화학 케미컬로 미세 파티클과 유기 오염물을 씻어내는 공정</td>
            </tr>
          </tbody>
        </table>

        <h3>2. 왜 교과서의 '8대 공정' 대신 현업은 'PETDC'로 나눌까?</h3>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>팹(FAB) 조직 체계와의 1:1 매칭</strong>:
            <br>삼성전자 메모리사업부, SK하이닉스 양산기술(PE) 및 공정기술 조직은 전공정 부서를 <strong>'Photo 기술팀, Etch 기술팀, Thin Film 기술팀, Diffusion 기술팀, CMP/세정 기술팀'</strong>의 5개 모듈 단위로 편성하여 장비를 운영합니다.
          </li>
          <li><strong>수백 회의 무한 순환 루프(Cycle)</strong>:
            <br>반도체는 1번 훑고 지나가는 일방통행이 아닙니다.
            <br><strong>[박막 증착(T) ➔ 포토 패터닝(P) ➔ 식각(E) ➔ 세정/CMP(C) ➔ 이온주입(D)]</strong>의 단위 사이클을 40~70회 이상 끊임없이 반복하여 수십 층의 3차원 트랜지스터와 배선을 빌드업합니다.
          </li>
        </ul>

        <h3>3. 혹시 장비/공정 이름 오타일 가능성: PECVD</h3>
        <p>만약 현업 조직이나 모듈 분류를 묻는 맥락이 아니라 개별 박막 장비를 이야기하는 맥락이었다면, 플라즈마를 이용해 저온에서 박막을 증착하는 <strong>PECVD (Plasma Enhanced Chemical Vapor Deposition)</strong>를 'PETDC'로 잘못 기재했거나 오인했을 가능성도 있습니다.</p>

        <h3>4. 직관적 마스터 비유: '아파트 건축 5대 전담반'</h3>
        <ul style="margin-left: 20px; line-height: 1.8; color: var(--text-sub);">
          <li><strong>T (Thin Film)</strong>: 바닥에 콘크리트 슬래브를 붓고 벽면을 세우는 <strong>'골조 적층반'</strong></li>
          <li><strong>P (Photo)</strong>: 콘크리트 위에 먹줄을 튕겨 방과 기둥의 위치를 정밀하게 그리는 <strong>'설계 도면 도안반'</strong></li>
          <li><strong>E (Etch)</strong>: 도면대로 문과 창문 구멍을 정밀하게 뚫어내는 <strong>'천공 및 조각반'</strong></li>
          <li><strong>C (CMP/Clean)</strong>: 울퉁불퉁한 콘크리트 표면을 매끄럽게 갈아내고 분진을 물청소하는 <strong>'미장 및 청소반'</strong></li>
          <li><strong>D (Diffusion)</strong>: 벽 속에 전선과 배관을 매립하여 전기가 통하게 만드는 <strong>'전기 배선 시공반'</strong></li>
          <li>이 5개 반이 한 층을 끝내면, 바로 다음 층으로 올라가 똑같은 작업을 100번 반복하여 100층짜리 초고층 빌딩(V-NAND / 첨단 DRAM)을 완성하는 것입니다!</li>
        </ul>
      </div>
    </section>
"""

    # 3. Renumber existing nav-items (01 -> 02, ..., 29 -> 30)
    nav_pattern = r'(<ul class="nav-list" id="navList">)([\s\S]*?)(</ul>)'
    match = re.search(nav_pattern, html)
    if match:
        old_nav_items = match.group(2)
        shifted_nav = old_nav_items
        for i in range(29, 0, -1):
            old_str = f'<span class="nav-num">{i:02d}</span>'
            new_str = f'<span class="nav-num">{i+1:02d}</span>'
            shifted_nav = shifted_nav.replace(old_str, new_str)
            old_href = f'href="#q-{i:02d}"'
            new_href = f'href="#q-{i+1:02d}"'
            shifted_nav = shifted_nav.replace(old_href, new_href)
        
        updated_nav_list = match.group(1) + "\n" + new_nav_item + shifted_nav + match.group(3)
        html = html[:match.start()] + updated_nav_list + html[match.end():]

    # 4. Renumber existing sections (q-01 -> q-02, ..., q-29 -> q-30)
    for i in range(29, 0, -1):
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
        r"""<p class="main-desc">질문자님께서 질문하신 문장 그대로 좌측 탭 제목과 본문 제목을 구성하였습니다. 최상단에는 가장 최근 질문인 <strong>'petdc는 무슨 공정 말하는 걸까?'</strong>가 1번으로 위치합니다.</p>""",
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
