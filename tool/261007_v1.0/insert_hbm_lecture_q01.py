# -*- coding: utf-8 -*-
"""
insert_hbm_lecture_q01.py
유튜브 '칩쟁이 HBM 총 정리 (개념, 특징, 공정방법, 이슈, 성능)' 영상을
대시보드 최상단 Q01로 신규 추가하고, 기존 54개 질문을 Q02~Q55로 시프트 (총 55개 질문 백과사전).
"""

import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (유튜브 칩쟁이 강의 특강)",
    "title": "HBM 총 정리 (개념, 특징, 공정방법, 이슈, 성능 - 칩쟁이 특강)",
    "summary": [
        "<strong>HBM(High Bandwidth Memory)</strong>은 수평 배선의 물리적 한계(선폭 20㎛, 평면 그래프 병목)를 극복하기 위해 DRAM 다이를 수직 적층하고 수천 개의 TSV로 직결하여 1024-bit 이상의 초광대역 버스를 구현한 메모리입니다.",
        "제조 공정은 <strong>2.5D 실리콘 인터포저(선폭 < 1㎛)</strong> 위 실장 방식과 스택 본딩 기술이 핵심이며, 삼성전자의 TC-NCF(필름 압착) 대비 SK하이닉스의 MR-MUF(리플로우 + 고방열 액상 에폭시)가 더미 마이크로 범프 2배 확보 및 방열 특성에서 우위를 점하고 있습니다.",
        "현재의 3대 기술 난제는 <strong>발열(Heat), 워피지(Warpage 휨), 복합 수율 및 TSV 칩 면적 페널티(Cost)</strong>이며, 차세대 HBM4에서는 범프를 없애고 구리 원자를 직접 맞붙이는 '하이브리드 본딩(Hybrid Bonding)'으로의 전환이 예고되어 있습니다.",
        "HBM은 1GB당 가격이 일반 DRAM 대비 약 4배($10.6 vs $2.9)에 달하여, 전체 DRAM 생산량의 5% 비중으로 전체 매출의 21%를 독식하는 초고수익 핵심 제품입니다."
    ],
    "svg_title": "📊 [칩쟁이 HBM 특강 총괄도] 2.5D 인터포저 구조 & TC-NCF vs MR-MUF vs 하이브리드 본딩",
    "svg": """<svg viewBox="0 0 780 370" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="780" height="370" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
  <!-- Left: 2.5D Package Architecture -->
  <rect x="25" y="30" width="360" height="310" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
  <text x="40" y="55" fill="#38bdf8" font-size="12" font-weight="800">1. 2.5D HBM 아키텍처 (인터포저 & TSV)</text>
  <!-- GPU -->
  <rect x="40" y="75" width="110" height="65" rx="4" fill="#10b981"/>
  <text x="65" y="112" fill="#ffffff" font-size="12" font-weight="900">AI GPU</text>
  <!-- HBM 4 Stack -->
  <rect x="180" y="70" width="180" height="15" fill="#38bdf8"/>
  <rect x="180" y="88" width="180" height="15" fill="#38bdf8"/>
  <rect x="180" y="106" width="180" height="15" fill="#38bdf8"/>
  <rect x="180" y="124" width="180" height="16" fill="#0284c7"/>
  <text x="220" y="100" fill="#0f172a" font-size="10" font-weight="800">DRAM Core Stack</text>
  <text x="210" y="136" fill="#ffffff" font-size="9" font-weight="700">Base Logic Die (Buffer)</text>
  <!-- TSV Lines -->
  <line x1="210" y1="70" x2="210" y2="135" stroke="#f59e0b" stroke-width="2"/>
  <line x1="330" y1="70" x2="330" y2="135" stroke="#f59e0b" stroke-width="2"/>
  <!-- Interposer -->
  <rect x="40" y="155" width="320" height="25" fill="#334155" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="50" y="172" fill="#38bdf8" font-size="10.5" font-weight="800">2.5D 실리콘 인터포저 (선폭 < 1μm, 1024-bit 버스)</text>
  <!-- PCB Substrate -->
  <rect x="40" y="200" width="320" height="35" fill="#1e293b"/>
  <text x="140" y="222" fill="#94a3b8" font-size="11" font-weight="700">패키지 기판 (PCB)</text>
  <text x="40" y="265" fill="#cbd5e1" font-size="10.5">• 대역폭(Bandwidth) = 클록 × 버스 폭 × 2</text>
  <text x="40" y="285" fill="#34d399" font-size="10.5">• GDDR6(32-bit) ➔ HBM3(1024-bit, 819GB/s)</text>
  <text x="40" y="305" fill="#fbbf24" font-size="10.5">• HBM4: 2048-bit 버스 확장 (대역폭 2배 추가)</text>

  <!-- Right: 3 Stack Bonding Technologies -->
  <rect x="400" y="30" width="355" height="310" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1.2"/>
  <text x="415" y="55" fill="#38bdf8" font-size="12" font-weight="800">2. 스택 본딩 3대 공정 방식 비교</text>

  <rect x="415" y="70" width="325" height="75" rx="4" fill="#1e293b"/>
  <text x="425" y="90" fill="#f87171" font-size="11" font-weight="700">① TC-NCF (삼성전자 주력 방식)</text>
  <text x="425" y="108" fill="#cbd5e1" font-size="10">• 층마다 비전도성 필름(NCF) 깔고 열압착(TC) 반복</text>
  <text x="425" y="124" fill="#34d399" font-size="9.5">➔ 장점: 워피지(휨) 제어 유리 / 단점: 속도 느림, 방열 불리</text>

  <rect x="415" y="155" width="325" height="85" rx="4" fill="#1e293b"/>
  <text x="425" y="175" fill="#f59e0b" font-size="11" font-weight="700">② MR-MUF (SK하이닉스 주력 방식)</text>
  <text x="425" y="193" fill="#cbd5e1" font-size="10">• 리플로우 일괄 융착 후 액상 에폭시(MUF) 모세관 충진</text>
  <text x="425" y="210" fill="#cbd5e1" font-size="9.5">• 더미 마이크로 범프 2배 확보로 방열 압도적 우수</text>
  <text x="425" y="226" fill="#fbbf24" font-size="9.5">➔ HBM3/3E 독점 납품의 핵심 원동력</text>

  <rect x="415" y="250" width="325" height="75" rx="4" fill="#1e293b"/>
  <text x="425" y="270" fill="#38bdf8" font-size="11" font-weight="700">③ 하이브리드 본딩 (HBM4 이후 차세대)</text>
  <text x="425" y="288" fill="#cbd5e1" font-size="10">• 범프리스(Bumpless) Cu-Cu 직접 원자 결합 + SiO₂ 본딩</text>
  <text x="425" y="306" fill="#38bdf8" font-size="9.5">➔ 두께 한계 돌파, 16단/20단 무제한 적층 가능</text>
</svg>""",
    "lecture": r"""<h3>1. 대역폭(Bandwidth)과 레이턴시(Latency)의 본질적 구분</h3>
<p>유튜브 강의에서 설명하는 가장 직관적인 비유는 <strong>수도꼭지와 수도관</strong>입니다:</p>
<ul>
  <li><strong>레이턴시 (Latency / 지연 시간)</strong>: 수도꼭지를 딱 틀었을 때 물이 파이프를 타고 이동하여 처음 쏟아져 나오기까지 걸리는 시간입니다 (예: LoL 북미 서버 접속 시 거리 때문에 발생하는 150ms 핑).</li>
  <li><strong>대역폭 (Bandwidth)</strong>: 물이 나오기 시작한 뒤 초당 쏟아지는 물의 부피(수도관의 직경)입니다. HBM은 레이턴시가 짧은 것이 아니라 한 번에 데이터를 콸콸 쏟아붓는 수도관 굵기(대역폭)가 압도적인 메모리입니다.</li>
</ul>
<h3>2. PCB의 물리적 한계와 실리콘 인터포저의 필연성</h3>
<p>DRAM 대역폭 공식은 $\text{Bandwidth} = \text{Clock} \times \text{Bus Width} \times 2$ 입니다. 클록을 높이면 고주파 저항 손실로 발열이 폭증하므로 버스 폭을 늘려야 합니다. 그러나 일반 PCB는 선폭이 약 $20\,\mu\text{m}$에 달해 1024가닥의 버스를 깔면 배선 폭만 $20\,\text{mm}$가 넘어 칩 크기($11\,\text{mm} \times 11\,\text{mm}$)를 초과합니다. 이를 해결하기 위해 반도체 공정으로 선폭을 <strong>$1\,\mu\text{m}$ 이하</strong>로 줄인 <strong>2.5D 실리콘 인터포저</strong>가 도입되었습니다.</p>
<h3>3. TC-NCF vs MR-MUF vs 하이브리드 본딩의 진실</h3>
<ul>
  <li><strong>삼성전자 TC-NCF</strong>: 층마다 필름을 깔고 열과 압력으로 눌러 본딩하므로 휨(Warpage) 억제에는 유리하지만, 열전도도가 낮은 필름 특성과 더미 범프 수 부족으로 방열에 취약합니다.</li>
  <li><strong>SK하이닉스 MR-MUF</strong>: 스택 전체를 가적층 후 리플로우로 일괄 솔더 접합하고, 고열전도 실리카 필러가 든 액상 에폭시를 진공 압력으로 주입합니다. 열을 빼내는 더미 마이크로 범프를 2배 이상 배치할 수 있어 <strong>방열 특성이 압도적</strong>입니다.</li>
  <li><strong>차세대 하이브리드 본딩</strong>: 마이크로 범프(솔더 높이)를 완전히 제거하고 화학기계적 연마(CMP)로 구리가 살짝 오목하게 파이게 한 뒤, 열처리 시 구리의 높은 열팽창계수($17\,\text{ppm}$)를 이용해 Cu-Cu 원자 확산 직접 결합을 완성합니다.</li>
</ul>"""
}

def update_files(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. nav-item 시프트: 54부터 1까지 거꾸로 시프트 (q-XX -> q-(XX+1))
    for old_n in range(54, 0, -1):
        new_n = old_n + 1
        old_str = f"{old_n:02d}"
        new_str = f"{new_n:02d}"
        html = re.sub(
            rf'<li class="nav-item"><a href="#q-{old_str}" class="nav-link"><span class="nav-num">{old_str}</span><span class="nav-text">(.*?)</span></a></li>',
            rf'<li class="nav-item"><a href="#q-{new_str}" class="nav-link"><span class="nav-num">{new_str}</span><span class="nav-text">\1</span></a></li>',
            html
        )
        html = re.sub(
            rf'<section class="([^"]*?)" id="q-{old_str}">',
            rf'<section class="\1" id="q-{new_str}">',
            html
        )
        html = re.sub(
            rf'<span class="topic-badge">Q {old_str}</span>',
            rf'<span class="topic-badge">Q {new_str}</span>',
            html
        )

    # 2. 신규 Q01 nav-item 추가
    new_nav_item = f'      <li class="nav-item"><a href="#{NEW_TOPIC["id"]}" class="nav-link"><span class="nav-num">{NEW_TOPIC["num"]}</span><span class="nav-text">{NEW_TOPIC["title"]}</span></a></li>\n'
    nav_list_pos = html.find('<ul class="nav-list" id="navList">')
    if nav_list_pos != -1:
        insert_nav = nav_list_pos + len('<ul class="nav-list" id="navList">\n')
        html = html[:insert_nav] + new_nav_item + html[insert_nav:]

    # 3. 신규 Q01 섹션 추가
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
        <span class="summary-tag">강의 핵심 4대 요약 포인트</span>
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

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {file_path}")

if __name__ == "__main__":
    update_files(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_files(r"C:\Work\반도체3\index.html")
    print("Done!")
