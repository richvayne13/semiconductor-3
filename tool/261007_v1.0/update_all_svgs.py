import os

def update_all_svgs():
    html_file = r"C:\Work\반도체3\result\261007_v1.0\index.html"
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. DIBL SVG Diagram
    dibl_svg = """
        <!-- SVG 그래픽 다이어그램: DIBL 에너지 장벽 강하 -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [에너지 밴드 다이어그램] 드레인 전압(V_D) 증가에 따른 소스-채널 전위 장벽 강하(DIBL)
          </div>
          <svg viewBox="0 0 760 360" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <defs>
              <linearGradient id="barrierNorm" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#94a3b8"/>
                <stop offset="100%" stop-color="#64748b"/>
              </linearGradient>
              <linearGradient id="barrierLow" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#f43f5e"/>
                <stop offset="100%" stop-color="#f59e0b"/>
              </linearGradient>
              <filter id="glow-dibl" x="-20%" y="-20%" width="140%" height="140%">
                <feGaussianBlur stdDeviation="3" result="blur" />
                <feComposite in="SourceGraphic" in2="blur" operator="over" />
              </filter>
              <marker id="arr-dibl-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#f43f5e"/>
              </marker>
              <marker id="arr-dibl-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981"/>
              </marker>
            </defs>

            <!-- 배경 & 축 -->
            <rect width="760" height="360" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
            <line x1="55" y1="310" x2="715" y2="310" stroke="#334155" stroke-width="1.5"/>
            <line x1="55" y1="310" x2="55" y2="30" stroke="#334155" stroke-width="1.5"/>
            <text x="55" y="22" fill="#94a3b8" font-size="11.5" font-family="'JetBrains Mono', monospace">전도대 에너지 (E_C) ▲</text>
            <text x="650" y="332" fill="#94a3b8" font-size="11.5" font-family="'JetBrains Mono', monospace">채널 위치 (x) ►</text>

            <!-- 영역 구분선 및 레이블 -->
            <line x1="200" y1="40" x2="200" y2="310" stroke="#1e293b" stroke-dasharray="4 4" stroke-width="1.2"/>
            <line x1="540" y1="40" x2="540" y2="310" stroke="#1e293b" stroke-dasharray="4 4" stroke-width="1.2"/>
            <text x="95" y="55" fill="#38bdf8" font-size="13" font-weight="700">[ 소스 (Source) ]</text>
            <text x="335" y="55" fill="#e2e8f0" font-size="13" font-weight="700">[ 채널 (Channel) ]</text>
            <text x="590" y="55" fill="#38bdf8" font-size="13" font-weight="700">[ 드레인 (Drain) ]</text>

            <!-- 정상 상태 (낮은 V_D) 밴드 프로파일 -->
            <path d="M 60 210 L 200 210 Q 370 70 540 210 L 710 210" fill="none" stroke="#64748b" stroke-width="2.5" stroke-dasharray="5 4"/>
            <text x="385" y="95" fill="#94a3b8" font-size="11.5">낮은 V_D (정상 장벽 높이)</text>

            <!-- 높은 V_D 인가 시 (DIBL 발생) 밴드 프로파일 -->
            <path d="M 60 210 L 200 210 Q 350 145 540 290 L 710 290" fill="none" stroke="url(#barrierLow)" stroke-width="3.8" filter="url(#glow-dibl)"/>
            <text x="365" y="140" fill="#f43f5e" font-size="12" font-weight="700">높은 V_D (DIBL로 깎인 장벽!)</text>

            <!-- 장벽 강하 ΔVth 표시 -->
            <line x1="330" y1="102" x2="330" y2="152" stroke="#f59e0b" stroke-width="2" marker-end="url(#arr-dibl-red)" marker-start="url(#arr-dibl-red)"/>
            <text x="250" y="132" fill="#f59e0b" font-size="12" font-weight="800">장벽 강하 (ΔΦ_B)</text>

            <!-- 소스 전자들이 쏟아져 넘어가는 모습 -->
            <circle cx="130" cy="195" r="5.5" fill="#10b981"/>
            <circle cx="150" cy="195" r="5.5" fill="#10b981"/>
            <circle cx="170" cy="195" r="5.5" fill="#10b981"/>
            <path d="M 180 190 Q 250 145 370 170 Q 470 210 560 280" fill="none" stroke="#10b981" stroke-width="2.5" stroke-dasharray="4 3" marker-end="url(#arr-dibl-green)"/>
            <text x="440" y="210" fill="#10b981" font-size="12" font-weight="700">전자가 장벽을 넘어 폭주 (누설 I_off 폭증!)</text>
          </svg>
        </div>
    """

    # 2. LDD Electric Field SVG Diagram
    ldd_svg = """
        <!-- SVG 그래픽 다이어그램: LDD 전계 피크 완화 -->
        <div style="background:#090d1a; border:1px solid #1e293b; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 6px 20px rgba(0,0,0,0.4);">
          <div style="font-size:0.95rem; font-weight:700; color:#38bdf8; margin-bottom:14px; display:flex; align-items:center; gap:8px;">
            📊 [전기장 프로파일 비교] LDD 적용 전(수직 절벽) vs LDD 적용 후(완만한 미끄럼틀)
          </div>
          <svg viewBox="0 0 760 340" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" style="display:block; overflow:visible;">
            <defs>
              <linearGradient id="efieldNoLDD" x1="0%" y1="100%" x2="0%" y2="0%">
                <stop offset="0%" stop-color="rgba(244, 63, 94, 0.1)"/>
                <stop offset="100%" stop-color="rgba(244, 63, 94, 0.4)"/>
              </linearGradient>
              <linearGradient id="efieldLDD" x1="0%" y1="100%" x2="0%" y2="0%">
                <stop offset="0%" stop-color="rgba(16, 185, 129, 0.1)"/>
                <stop offset="100%" stop-color="rgba(16, 185, 129, 0.4)"/>
              </linearGradient>
            </defs>

            <!-- 배경 & 축 -->
            <rect width="760" height="340" rx="10" fill="#0b1120" stroke="#1e293b" stroke-width="1.2"/>
            <line x1="60" y1="290" x2="710" y2="290" stroke="#334155" stroke-width="1.5"/>
            <line x1="60" y1="290" x2="60" y2="30" stroke="#334155" stroke-width="1.5"/>
            <text x="60" y="22" fill="#94a3b8" font-size="11.5" font-family="'JetBrains Mono', monospace">수평 전기장 (E_lateral) ▲</text>
            <text x="645" y="312" fill="#94a3b8" font-size="11.5" font-family="'JetBrains Mono', monospace">드레인 접합 거리 (x) ►</text>

            <!-- No LDD: 좁은 밑변, 살인적인 피크 -->
            <path d="M 280 290 L 370 50 L 410 290 Z" fill="url(#efieldNoLDD)" stroke="#f43f5e" stroke-width="3"/>
            <circle cx="370" cy="50" r="5" fill="#f43f5e"/>
            <text x="380" y="55" fill="#f43f5e" font-size="13" font-weight="800">E_max (No LDD: 핫 캐리어 폭증!)</text>

            <!-- LDD 적용: 넓은 밑변, 절반으로 떨어진 피크 -->
            <path d="M 220 290 L 350 170 L 510 290 Z" fill="url(#efieldLDD)" stroke="#10b981" stroke-width="3"/>
            <circle cx="350" cy="170" r="5" fill="#10b981"/>
            <text x="360" y="175" fill="#10b981" font-size="13" font-weight="800">E_max (LDD: 피크 50% 이상 완화!)</text>

            <!-- 동일 면적 (적분 전압 ΔV) 강조 주석 -->
            <rect x="520" y="80" width="210" height="60" rx="8" fill="rgba(15, 23, 42, 0.9)" stroke="#0284c7" stroke-width="1.5"/>
            <text x="532" y="102" fill="#38bdf8" font-size="12" font-weight="700">💡 면적(적분 전압 ΔV)은 동일!</text>
            <text x="532" y="122" fill="#cbd5e1" font-size="11">밑변(W_dep)이 넓어져 피크가 완화됨</text>
          </svg>
        </div>
    """

    # Replace DIBL ascii diagram in Q22 and Q03
    old_dibl_diagram = """        <div class="diagram-box">
[에너지 밴드 관점의 DIBL 현상]

      소스 (N⁺)      소스-채널 장벽 (원래 높이) ───┐
        ●●● (전자)    DIBL로 깎인 장벽 ───────┼──┐
                                               │  │
                                               │  └──► 드레인 (V_D 인가로 낮아짐)
      * 드레인이 소스 앞의 문턱을 강제로 깎아내려 전자가 채널로 마구 쏟아져 들어감!</div>"""

    if old_dibl_diagram in content:
        content = content.replace(old_dibl_diagram, dibl_svg)
        print("Replaced DIBL text diagram with SVG!")

    # Replace LDD ascii diagram in Q06 and Q02
    old_ldd_diagram = """        <div class="diagram-box">
[전기장 프로파일 비교: 수직 절벽에서 완만한 미끄럼틀로!]

   전기장 (E) ▲
              │         ▲ [No LDD] 밑변 좁음 ──► 피크(E_max) 폭증!
              │        ╱ ╲
              │       ╱   ▲ [LDD 적용] 밑변(W_dep)을 넓혀 피크를 절반으로 완화!
              │      ╱   ╱ ╲
              └─────┴───┴───┴────────────────────────► 거리 (x)</div>"""

    if old_ldd_diagram in content:
        content = content.replace(old_ldd_diagram, ldd_svg)
        print("Replaced LDD text diagram with SVG!")

    # Write back
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    root_file = r"C:\Work\반도체3\index.html"
    with open(root_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated all SVGs in index.html and root!")

if __name__ == "__main__":
    update_all_svgs()
