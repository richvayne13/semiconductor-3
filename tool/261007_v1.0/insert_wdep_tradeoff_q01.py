# -*- coding: utf-8 -*-
"""
insert_wdep_tradeoff_q01.py
사용자 질문: "공핍층폭은 줄이는게좋은거야 넓히는게좋은거야"
대시보드 최상단 Q01로 신규 추가하고, 기존 65개 질문을 Q02~Q66으로 시프트 (총 66개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 물리 & 공핍층 딜레마)",
    "title": "공핍층 폭은 줄이는 게 좋은 거야 넓히는 게 좋은 거야? (위치별 트레이드오프)",
    "nav_title": "공핍층 폭은 줄이는 게 좋은 거야 넓히는 게 좋은 거야?",
    "summary": [
        "결론부터 말하면 <strong>'소자의 어느 위치에 있는 공핍층인가'에 따라 정반대</strong>이며, 이는 반도체 소자 공학에서 가장 흥미롭고 치열한 <strong>핵심 트레이드오프(양면성)</strong>입니다.",
        "<strong>① 소스/드레인(S/D) 접합부: ➔ '넓힐수록(Wdep ↑)' 좋습니다!</strong> 기생 접합 커패시턴스($C_j = \\frac{\\epsilon_s A}{W_{dep}}$)가 줄어들어 RC 스위칭 속도가 빨라지고, 최대 전계($\\mathcal{E}_{max} \\approx \\frac{2V}{W_{dep}}$)가 완화되어 핫캐리어(HCI)와 애벌랜치 항복 전압($BV$)이 개선됩니다.",
        "<strong>② 채널 수평 방향 (드레인 ➔ 소스 침범): ➔ '줄일수록(Wdep ↓)' 좋습니다!</strong> 드레인 공핍층이 채널 쪽으로 너무 넓게 퍼지면 소스 공핍층과 맞닿아 <strong>지하 펀치스루(Punchthrough) 및 DIBL</strong>이 발생하므로, 헤일로(Halo, $P^+$) 도핑으로 억지로 압축해야 합니다.",
        "<strong>③ 게이트 하부 수직 방향: ➔ '줄일수록(Wdep ↓)' 좋습니다!</strong> 수직 공핍층이 얇을수록 게이트의 정전기적 제어력(스케일 길이 $\\lambda$)이 강해지고 서브스레숄드 스윙($SS$)이 개선되므로, 최신 FinFET 및 GAA는 실리콘 바디를 수 nm로 깎아 <strong>수직 공핍층을 강제로 극한까지 축소</strong>시켰습니다."
    ],
    "svg_title": "📊 [공핍층 폭 Wdep의 위치별 트레이드오프] 넓혀야 하는 부위(S/D) vs 줄여야 하는 부위(채널/게이트하부)",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>

  <!-- Left: MOSFET Cross-Section with Depletion Region Annotations -->
  <rect x="20" y="25" width="375" height="320" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="35" y="48" fill="#38bdf8" font-size="12" font-weight="800">1. MOSFET 내 공핍층의 3대 핵심 영역 비교</text>

  <!-- Gate Stack -->
  <rect x="135" y="65" width="145" height="25" fill="#334155" rx="3" stroke="#94a3b8"/>
  <text x="165" y="82" fill="#ffffff" font-size="11" font-weight="700">게이트 전극</text>
  <rect x="135" y="90" width="145" height="6" fill="#38bdf8"/>

  <!-- Substrate -->
  <rect x="40" y="96" width="335" height="150" rx="4" fill="#1e293b"/>
  <text x="50" y="235" fill="#94a3b8" font-size="9.5">P형 기판 (Substrate)</text>

  <!-- Source / Drain -->
  <rect x="45" y="96" width="65" height="50" fill="#0284c7" opacity="0.6" rx="2"/>
  <text x="55" y="125" fill="#ffffff" font-size="10" font-weight="800">소스 N⁺</text>

  <rect x="305" y="96" width="65" height="50" fill="#0284c7" opacity="0.6" rx="2"/>
  <text x="312" y="125" fill="#ffffff" font-size="10" font-weight="800">드레인 N⁺</text>

  <!-- Depletion 1: S/D Junction Bottom (Widen is good!) -->
  <path d="M 45 146 Q 77 175 110 146" fill="none" stroke="#10b981" stroke-width="2.5" stroke-dasharray="3,3"/>
  <path d="M 305 146 Q 337 175 370 146" fill="none" stroke="#10b981" stroke-width="2.5" stroke-dasharray="3,3"/>
  <text x="45" y="185" fill="#10b981" font-size="9.5" font-weight="700">① S/D 바닥 접합: [넓혀라! W ↑]</text>
  <text x="45" y="198" fill="#cbd5e1" font-size="8.5">➔ Cj = ε/W 감소 (RC 지연 개선)</text>

  <!-- Depletion 2: Lateral Drain into Channel (Narrow is good!) -->
  <path d="M 270 96 Q 260 120 305 140" fill="none" stroke="#ef4444" stroke-width="2.5"/>
  <text x="180" y="120" fill="#ef4444" font-size="9.5" font-weight="800">② 채널 침범:</text>
  <text x="180" y="133" fill="#ef4444" font-size="9" font-weight="700">[줄여라! W ↓]</text>
  <text x="155" y="148" fill="#fca5a5" font-size="8.5">펀치스루/DIBL 방어</text>

  <!-- Depletion 3: Gate Vertical Depletion (Narrow is good!) -->
  <rect x="135" y="96" width="145" height="25" fill="#fbbf24" opacity="0.2" stroke="#fbbf24" stroke-dasharray="2,2"/>
  <text x="145" y="112" fill="#fbbf24" font-size="9" font-weight="800">③ 게이트 하부 수직 Wdep:</text>
  <text x="145" y="165" fill="#fbbf24" font-size="9.5" font-weight="700">[줄여라! W ↓] (게이트 장악력 λ 강화)</text>

  <!-- Bottom Summary card -->
  <rect x="35" y="255" width="345" height="75" rx="4" fill="#1e293b"/>
  <text x="45" y="273" fill="#fbbf24" font-size="10" font-weight="700">★ 엔지니어의 딜레마 해결책</text>
  <text x="45" y="290" fill="#cbd5e1" font-size="9">• S/D 쪽은 LDD 완만 도핑으로 공핍층 확장 ➔ Cj 감소</text>
  <text x="45" y="306" fill="#cbd5e1" font-size="9">• 채널 모서리는 Halo 고농도로 공핍층 압축 ➔ 펀치 차단</text>
  <text x="45" y="322" fill="#34d399" font-size="9">• FinFET/GAA: 바디 두께(Tsi) 자체를 줄여 수직 Wdep 박멸</text>

  <!-- Right: Detailed Trade-off Matrix Table -->
  <rect x="410" y="25" width="350" height="320" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
  <text x="425" y="48" fill="#10b981" font-size="12" font-weight="800">2. 공핍층 폭(Wdep) 양면성 종합 판정표</text>

  <rect x="425" y="60" width="320" height="120" rx="4" fill="#1e293b"/>
  <text x="435" y="80" fill="#34d399" font-size="11" font-weight="700">[CASE 1] 공핍층 폭을 '넓혀야' 좋은 경우 (W ↑)</text>
  <text x="435" y="100" fill="#38bdf8" font-size="10" font-weight="700">1) 기생 접합 커패시턴스 극소화 (Cj ↓)</text>
  <text x="445" y="115" fill="#cbd5e1" font-size="9">• Cj = ε·A / Wdep ➔ 고주파 스위칭 속도 극대화</text>
  <text x="435" y="133" fill="#f59e0b" font-size="10" font-weight="700">2) 전계 완화 및 항복 전압(BV) 상승</text>
  <text x="445" y="148" fill="#cbd5e1" font-size="9">• E_max ≈ 2V / Wdep ➔ 핫캐리어(HCI) & GIDL 억제</text>
  <text x="435" y="166" fill="#10b981" font-size="9.5">• 포토다이오드: 수광 영역 확장 ➔ 광 변환 효율 증가</text>

  <rect x="425" y="190" width="320" height="145" rx="4" fill="#1e293b"/>
  <text x="435" y="210" fill="#ef4444" font-size="11" font-weight="700">[CASE 2] 공핍층 폭을 '줄여야' 좋은 경우 (W ↓)</text>
  <text x="435" y="230" fill="#f87171" font-size="10" font-weight="700">1) 지하 펀치스루(Punchthrough) 원천 봉쇄</text>
  <text x="445" y="246" fill="#cbd5e1" font-size="9">• 드레인 공핍층이 소스에 닿지 못하게 가로막아야 함</text>
  <text x="435" y="264" fill="#fbbf24" font-size="10" font-weight="700">2) DIBL(드레인 유도 장벽 강하) 차단</text>
  <text x="445" y="280" fill="#cbd5e1" font-size="9">• 채널로 드레인 전계 침투 억제 ➔ 오프 누설 전류 사수</text>
  <text x="435" y="298" fill="#38bdf8" font-size="10" font-weight="700">3) 게이트 정전기적 통제력(스케일 길이 λ) 극대화</text>
  <text x="445" y="315" fill="#cbd5e1" font-size="9">• 수직 Wdep 얕을수록 서브스레숄드 스윙(SS ≈ 60mV) 달성</text>
</svg>""",
    "lecture": r"""<h3>1. 본질적 질문: 공핍층 폭($W_{dep}$)은 줄이는 게 좋은가, 넓히는 게 좋은가?</h3>
<p>이 질문은 반도체 소자 물리학에서 <strong>가장 핵심적인 트레이드오프(Trade-off, 양면성)</strong>를 찌르는 질문입니다. 결론부터 말씀드리면 다음과 같습니다:</p>
<blockquote>
  <strong>"소자의 어느 부위인가, 그리고 속도를 원하느냐 누설을 막길 원하느냐에 따라 정반대입니다!"</strong>
</blockquote>

---

<h3>2. 공핍층 폭을 '넓힐수록(Wdep ↑)' 무조건 좋은 부위와 이유</h3>

<h4>① 소스/드레인(S/D) 바닥 p-n 접합부 $\rightarrow$ 고속 스위칭과 내압 확보</h4>
<ul>
  <li><strong>기생 커패시턴스($C_j$) 극소화</strong>:
    $$C_j = \frac{\epsilon_s \cdot A}{W_{dep}}$$
    접합 커패시턴스는 공핍층 폭($W_{dep}$)에 반비례합니다. 공핍층 폭이 넓어질수록 평행판 커패시터의 극판 거리가 멀어지는 것과 같으므로 <strong>$C_j$가 뚝 떨어집니다</strong>. 이는 인버터 회로의 충방전 RC 지연($\tau \approx R C_j$)을 획기적으로 줄여 소자의 최고 동작 클록 주파수($f_{max}$)를 끌어올립니다.</li>
  <li><strong>최대 전계($\mathcal{E}_{max}$) 완화와 소자 신뢰성</strong>:
    $$\mathcal{E}_{max} \approx \frac{2(V_{bi} - V)}{W_{dep}}$$
    공핍층 폭($W_{dep}$)이 넓어지면 전압이 완만하게 떨어져 <strong>드레인 모서리의 초고전계 피크가 분산</strong>됩니다. 그 결과 전자들이 과도하게 가속되어 게이트 산화막을 파괴하는 <strong>핫 캐리어 인젝션(HCI)</strong>, 밴드간 터널링 누설인 <strong>GIDL</strong>, 그리고 항복 전압(Breakdown Voltage, $BV$)이 획기적으로 개선됩니다. (이것이 소스/드레인에 완만한 농도의 LDD를 넣는 이유입니다.)</li>
</ul>

<h4>② 광다이오드 (Photodiode / CMOS 이미지 센서)</h4>
<p>빛(광자)을 쬐어 전자-정공 쌍(EHP)을 생성하고 이를 전기로 바꾸는 공간이 바로 공핍층입니다. 따라서 빛을 감지하는 이미지 센서나 포토다이오드에서는 **빛을 최대한 많이 흡수하기 위해 공핍층을 수 마이크로미터 이상으로 넓게(PIN 구조)** 만듭니다.</p>

---

<h3>3. 공핍층 폭을 '줄일수록(Wdep ↓)' 무조건 좋은 부위와 이유</h3>

<h4>① 채널 수평 방향 (드레인에서 소스로 뻗어 나오는 공핍층) $\rightarrow$ 단채널 효과 방어</h4>
<ul>
  <li><strong>지하 펀치스루(Punchthrough) 원천 봉쇄</strong>:
    드레인에 역방향 전압이 걸리면 드레인 공핍층이 채널을 향해 수평으로 뻗어 나갑니다. 만약 채널 부근의 공핍층 폭이 너무 넓으면, <strong>드레인 공핍층이 소스 공핍층과 물리적으로 맞닿아 결합(Merge)</strong>해 버립니다. 이 순간 전위 장벽이 붕괴되어 전류가 억제되지 않고 쏟아져 나오는 '지하 펀치스루'가 발생합니다.</li>
  <li><strong>DIBL (드레인 유도 장벽 강하) 차단</strong>:
    공핍층이 채널 안쪽으로 파고들면 드레인 전계가 소스-채널 장벽을 깎아내려 문턱전압이 붕괴(Vt Roll-off)됩니다. 따라서 <strong>채널 모서리의 공핍층은 무조건 좁고 단단하게 압축($W_{dep} \downarrow$)</strong>해야 합니다. (이것이 채널 모서리에 고농도 $P^+$ 헤일로 도핑을 하는 이유입니다.)</li>
</ul>

<h4>② 게이트 하부 채널 수직 방향 깊이 $\rightarrow$ 게이트 장악력 극대화</h4>
<ul>
  <li><strong>스케일 길이(Scale Length, $\lambda$) 축소</strong>:
    단채널 효과를 판가름하는 특성 스케일 길이는 대략 다음과 같습니다:
    $$\lambda \approx \sqrt{\frac{\epsilon_{si}}{\epsilon_{ox}} t_{ox} W_{dep,max}}$$
    $\lambda$가 작을수록 게이트가 드레인보다 채널을 완벽하게 통제할 수 있습니다. 즉, <strong>게이트 아래의 수직 공핍층 깊이($W_{dep}$)가 얕을수록 드레인 전계의 지하 침투를 막고 게이트의 통제력이 압도적</strong>으로 강해집니다.</li>
  <li><strong>서브스레숄드 스윙 (SS) 최적화</strong>:
    $$SS \approx 60 \left( 1 + \frac{C_{dep}}{C_{ox}} \right) = 60 \left( 1 + \frac{\epsilon_{si}/W_{dep}}{\epsilon_{ox}/t_{ox}} \right) \quad [\text{mV/dec}]$$
    수직 공핍층을 완전히 없애거나 극소화하면 $C_{dep} \approx 0$이 되어 이상적인 한계치인 $60\,\text{mV/dec}$에 도달합니다.</li>
</ul>

---

<h3>4. 최신 반도체 공학자들의 '천재적인 절충안'</h3>
<p>한쪽은 넓혀야 하고 다른 쪽은 줄여야 하는 이 치명적인 딜레마를 반도체 공학자들은 다음과 같이 정교하게 해결했습니다:</p>
<ol>
  <li><strong>LDD + Halo 복합 도핑 (평면 MOSFET의 해법)</strong>:
    <ul>
      <li><strong>LDD (저농도 $N^-$)</strong>: 드레인 접합 바닥 쪽은 도핑을 완만하게 펴서 **공핍층을 넓혀($W_{dep} \uparrow$) $C_j$를 깎고 전계를 완화**시킵니다.</li>
      <li><strong>Halo (고농도 $P^+$ Pocket)</strong>: 채널 쪽으로 파고드는 모서리만 고농도로 도핑해 **공핍층을 강제로 압축($W_{dep} \downarrow$)하여 펀치스루를 차단**합니다.</li>
    </ul>
  </li>
  <li><strong>FinFET과 GAA 나노시트 (3차원 혁명)</strong>:
    실리콘 바디 두께($T_{si}$) 자체를 수 나노미터로 극도로 얇게 깎아버렸습니다. 물리적으로 실리콘 자체가 얇기 때문에 <strong>수직 공핍층 폭은 애초에 커질 수가 없어($W_{dep} \le T_{si}$) 게이트 통제력이 극대화</strong>되고, 벌크 기판이 없어 지하 펀치스루가 원천 소멸되었습니다.</li>
</ol>"""
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 65 topics (q-65 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(65, 0, -1):
        new_n = old_n + 1
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

    # For old Q 01 (now Q 02), remove 'latest-card-highlight' from section class
    html = re.sub(
        r'<section class="topic-section latest-card-highlight" id="q-02">',
        r'<section class="topic-section" id="q-02">',
        html
    )

    # Step 2: Build new nav-item for Q 01
    new_nav_item = f'      <li class="nav-item"><a href="#{NEW_TOPIC["id"]}" class="nav-link"><span class="nav-num">{NEW_TOPIC["num"]}</span><span class="nav-text">{NEW_TOPIC["nav_title"]}</span></a></li>\n'
    nav_list_pos = html.find('<ul class="nav-list" id="navList">')
    if nav_list_pos != -1:
        insert_nav = nav_list_pos + len('<ul class="nav-list" id="navList">\n')
        html = html[:insert_nav] + new_nav_item + html[insert_nav:]

    # Step 3: Build new section for Q 01
    summary_lis = "\n".join([f"          <li>{s}</li>" for s in NEW_TOPIC["summary"]])
    new_section_html = f"""
    <!-- Q 01 : {NEW_TOPIC['title']} -->
    <section class="topic-section latest-card-highlight" id="{NEW_TOPIC['id']}">
      <div class="topic-header">
        <div class="topic-title-wrap">
          <span class="topic-badge">Q 01</span>
          <span class="latest-tag">{NEW_TOPIC['badge']}</span>
          <h2 class="topic-title">{NEW_TOPIC['title']}</h2>
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
            {NEW_TOPIC['svg_title']}
          </div>
          {NEW_TOPIC['svg']}
        </div>
        {NEW_TOPIC['lecture']}
      </div>
    </section>
"""

    main_header_end = html.find("</header>")
    if main_header_end != -1:
        insert_sec = main_header_end + len("</header>")
        html = html[:insert_sec] + "\n" + new_section_html + html[insert_sec:]

    # Step 4: Update header description
    old_desc_part = "총 65개 질문으로 구성되어 있습니다."
    new_desc_part = "최상단에는 '공핍층 폭 축소 vs 확장의 위치별 트레이드오프' 및 '반도체 INTERCONNECT 다층배선'이 위치하며, 총 66개 질문으로 구성되어 있습니다."
    if old_desc_part in html:
        html = html.replace(old_desc_part, new_desc_part)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Wdep tradeoff topic!")
