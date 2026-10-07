import os

def update_index_with_svgs():
    html_file = r"C:\Work\반도체3\result\261007_v1.0\index.html"
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. BTBT SVG Diagram
    btbt_svg = """
        <!-- SVG 그래픽 다이어그램: BTBT 터널링 실체 -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [에너지 밴드 다이어그램] 초고전계 하의 밴드 간 터널링(BTBT) 및 캐리어 분리
          </div>
          <svg viewBox="0 0 760 380" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <defs>
              <linearGradient id="ecGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#38bdf8"/>
                <stop offset="100%" stop-color="#0284c7"/>
              </linearGradient>
              <linearGradient id="evGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#f43f5e"/>
                <stop offset="100%" stop-color="#be123c"/>
              </linearGradient>
              <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
                <feGaussianBlur stdDeviation="3.5" result="blur" />
                <feComposite in="SourceGraphic" in2="blur" operator="over" />
              </filter>
              <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/>
              </marker>
              <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#38bdf8"/>
              </marker>
              <marker id="arrow-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#f43f5e"/>
              </marker>
              <marker id="arrow-amber" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#f59e0b"/>
              </marker>
            </defs>

            <!-- 배경 그리드 & 축 -->
            <rect width="760" height="380" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
            <line x1="55" y1="330" x2="715" y2="330" stroke="#334155" stroke-width="1.5"/>
            <line x1="55" y1="330" x2="55" y2="35" stroke="#334155" stroke-width="1.5"/>
            <text x="55" y="24" fill="#94a3b8" font-size="11.5" font-family="'JetBrains Mono', monospace">에너지 (E) ▲</text>
            <text x="655" y="352" fill="#94a3b8" font-size="11.5" font-family="'JetBrains Mono', monospace">위치 (x) ►</text>

            <!-- 영역 표시 -->
            <text x="90" y="52" fill="#64748b" font-size="11" font-weight="600">[ 게이트 절연막 표면 ]</text>
            <text x="580" y="52" fill="#64748b" font-size="11" font-weight="600">[ N⁺ 드레인 전극 방향 ]</text>

            <!-- 전도대 (Ec) 곡선 -->
            <path d="M 70 70 C 160 75, 230 190, 340 240 L 700 255" fill="none" stroke="url(#ecGrad)" stroke-width="3.5" filter="url(#glow)"/>
            <text x="75" y="62" fill="#38bdf8" font-size="13.5" font-weight="700">전도대 (E_C)</text>

            <!-- 가전자대 (Ev) 곡선 -->
            <path d="M 70 180 C 160 185, 230 300, 340 350 L 700 365" fill="none" stroke="url(#evGrad)" stroke-width="3.5" filter="url(#glow)"/>
            <text x="75" y="198" fill="#f43f5e" font-size="13.5" font-weight="700">가전자대 (E_V)</text>

            <!-- 밴드갭 표시 (Eg = 1.12 eV) -->
            <line x1="140" y1="80" x2="140" y2="185" stroke="#94a3b8" stroke-dasharray="3 3" stroke-width="1.2"/>
            <circle cx="140" cy="80" r="3" fill="#38bdf8"/>
            <circle cx="140" cy="185" r="3" fill="#f43f5e"/>
            <text x="148" y="136" fill="#cbd5e1" font-size="11" font-weight="600">밴드갭 E_g = 1.12 eV</text>

            <!-- BTBT 터널링 화살표 (수평 순간이동) -->
            <line x1="165" y1="188" x2="265" y2="188" stroke="#f59e0b" stroke-width="3" stroke-dasharray="5 3" marker-end="url(#arrow-amber)"/>

            <!-- 터널링 장벽 거리 d_tunnel -->
            <line x1="170" y1="210" x2="260" y2="210" stroke="#38bdf8" stroke-width="1.5"/>
            <line x1="170" y1="205" x2="170" y2="215" stroke="#38bdf8" stroke-width="1.5"/>
            <line x1="260" y1="205" x2="260" y2="215" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="175" y="226" fill="#38bdf8" font-size="10.5" font-weight="700">d_tunnel ≤ 3~5 nm</text>

            <!-- 전자(e-) 방출 및 드레인 유입 -->
            <circle cx="265" cy="188" r="7" fill="#10b981" stroke="#ffffff" stroke-width="2" filter="url(#glow)"/>
            <text x="259" y="192" fill="#ffffff" font-size="10" font-weight="800">e⁻</text>
            <path d="M 280 192 Q 350 225 460 246" fill="none" stroke="#10b981" stroke-width="2.2" stroke-dasharray="4 3" marker-end="url(#arrow-green)"/>
            <text x="472" y="242" fill="#10b981" font-size="12" font-weight="700">전자 드레인 유입 ➔ GIDL 누설 전류 (I_D)</text>

            <!-- 정공(h+) 방출 및 기판 이동 -->
            <circle cx="165" cy="188" r="7" fill="#f43f5e" stroke="#ffffff" stroke-width="2" filter="url(#glow)"/>
            <text x="160" y="192" fill="#ffffff" font-size="10" font-weight="800">h⁺</text>
            <path d="M 150 192 Q 115 220 80 235" fill="none" stroke="#f43f5e" stroke-width="2.2" stroke-dasharray="4 3" marker-end="url(#arrow-red)"/>
            <text x="60" y="255" fill="#f43f5e" font-size="11.5" font-weight="700">정공 기판 배출 (I_sub)</text>

            <!-- 터널링 설명 박스 -->
            <rect x="235" y="110" width="250" height="52" rx="8" fill="rgba(15, 23, 42, 0.92)" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="248" y="131" fill="#f59e0b" font-size="12" font-weight="700">⚡ 양자역학적 BTBT 터널링</text>
            <text x="248" y="148" fill="#e2e8f0" font-size="10.5">금지대 장벽을 파동으로 뚫고 통과!</text>

            <!-- 전기장 기울기 표시 -->
            <path d="M 210 65 L 285 95" fill="none" stroke="#e2e8f0" stroke-width="1.8" marker-end="url(#arrow-blue)"/>
            <text x="295" y="85" fill="#38bdf8" font-size="11" font-weight="600">초고전계 (E > 1 MV/cm)</text>
            <text x="295" y="100" fill="#94a3b8" font-size="10">가파른 밴드 휨 (Slope = -qE)</text>
          </svg>
        </div>
    """

    # Replace the text diagram in Q01
    old_q1_diagram = """        <div class="diagram-box">
[에너지 밴드 다이어그램: BTBT 터널링의 실체]

    전도대 (E_C) ──┐
                   │  ◄── 가파른 밴드 휨 (초고전계)
                   │
    ───────────────┼────────► [터널링 순간이동!] ──┐ E_C
    가전자대 (E_V) ─┘                               └── 전도대로 전자가 뚫고 나옴!
                   ◄── d_tunnel ──►                   (전자-정공 쌍 EHP 생성)
                   (터널링 거리가 3~5nm로 얇아짐)</div>"""

    if old_q1_diagram in content:
        content = content.replace(old_q1_diagram, btbt_svg)
        print("Replaced Q01 BTBT diagram successfully!")
    else:
        print("Could not find exact Q01 diagram text, searching for diagram-box in Q01...")

    # Write back
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # Copy to root
    root_file = r"C:\Work\반도체3\index.html"
    with open(root_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated root index.html")

if __name__ == "__main__":
    update_index_with_svgs()
