# -*- coding: utf-8 -*-
"""
insert_soi_cj_cdep_q01.py
사용자 질문: "soi기술로 body와 s/d분리해 기생cap을 없앤다 에서 기생cap은 접합cap이야 depletion region cap이야"
대시보드 최상단 Q01로 신규 추가하고, 기존 80개 질문을 Q02~Q81로 시프트 (총 81개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (소자 커패시턴스 개념 정립 · SOI 물리)",
    "title": "SOI에서 Body와 S/D를 분리해 없애는 기생 커패시턴스는 접합Cap(Cj)일까, 공핍영역Cap(Cdep)일까?",
    "nav_title": "SOI로 없애는 기생Cap은 접합Cap(Cj)일까 공핍Cap(Cdep)일까?",
    "summary": [
        "<strong>1. 질문의 핵심 결론: '구조적 명칭은 접합 커패시턴스(Cj), 물리적 본질은 공핍 커패시턴스(Cdep)'</strong>: 'Body와 S/D를 분리한다'는 문맥에서 지칭하는 대상은 <strong>소스/드레인과 기판(바디) 사이의 '접합 커패시턴스(Junction Capacitance, $C_j$)'</strong>입니다. 그런데 <strong>접합 커패시턴스의 물리적 메커니즘 자체가 바로 P-N 접합면의 공핍 영역(Depletion Region)에 의해 생기는 공핍 커패시턴스($C_{dep,pn} = \\frac{\\epsilon_{si} A}{W_{dep}}$)</strong>이므로 둘은 다른 것이 아니라 '이름'과 '물리적 실체'의 관계입니다.",
        "<strong>2. 벌크 vs SOI의 결정적 차이 (바닥면 P-N 접합의 소멸)</strong>: 벌크 Si에서는 S/D 바닥 전체가 P형 기판과 맞닿아 거대한 $N^+-P$ 접합 공핍층($C_{j,bottom}$)이 형성됩니다. 반면 <strong>SOI는 S/D 밑바닥에 두꺼운 매립 산화막(BOX: Buried Oxide, $\\text{SiO}_2$)이 깔려 바디와 물리적으로 완전 격리되므로, P-N 접합면 자체가 아예 사라져 $C_j$가 원천 소멸</strong>됩니다.",
        "<strong>3. 게이트 아래 채널 공핍 커패시턴스($C_{dep,ch}$)와의 명확한 구분</strong>: 반도체 교재에서 기호로 $C_{dep}$라고 쓸 때는 게이트 산화막 아래 채널의 공핍 용량을 뜻하는 경우가 많습니다. 문장에서 'Body와 S/D를 분리'한다고 명시했으므로 <strong>타깃은 명백히 S/D 접합 커패시턴스($C_j$)</strong>입니다.",
        "<strong>4. FD-SOI의 2중 혜택</strong>: FD-SOI에서는 S/D 바닥의 접합 커패시턴스($C_j$)를 100% 없애는 동시에, 바디 박막화로 게이트 아래 채널의 공핍 커패시턴스($C_{dep,ch}$)까지 0에 가깝게 소멸시켜 <strong>RC 지연 대폭 단축(속도 20~30% 향상) 및 $SS \\approx 60\\text{mV/dec}$ 복원을 동시 달성</strong>합니다."
    ],
    "svg_title": "📊 [커패시터 구조 해부도] (A) 벌크 Cj vs SOI BOX 절연 단면 | (B) Cj와 Cdep의 물리적 관계도 | (C) MOSFET 2대 기생 커패시턴스 구분",
    "svg": """<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Bulk vs SOI S/D Junction Capacitance Elimination -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 벌크 vs SOI 소스/드레인 하부 비교</text>

    <!-- Sub-case 1: Bulk MOSFET -->
    <g transform="translate(15, 42)">
      <rect width="270" height="135" rx="5" fill="#1e293b" stroke="#ef4444"/>
      <text x="10" y="16" fill="#f87171" font-size="9" font-weight="800">1. 벌크(Bulk) MOSFET: 거대한 C_j 존재</text>
      <!-- Gate -->
      <rect x="90" y="25" width="90" height="10" fill="#64748b" rx="1"/>
      <text x="122" y="33" fill="#fff" font-size="7">Gate</text>
      <!-- S / D -->
      <rect x="25" y="35" width="55" height="35" fill="#f59e0b" rx="2"/>
      <text x="35" y="55" fill="#000" font-size="7.5" font-weight="800">Source (N+)</text>
      <rect x="190" y="35" width="55" height="35" fill="#f59e0b" rx="2"/>
      <text x="202" y="55" fill="#000" font-size="7.5" font-weight="800">Drain (N+)</text>
      <!-- P-Substrate -->
      <rect x="25" y="70" width="220" height="55" fill="#047857" opacity="0.3"/>
      <!-- S/D Bottom Junction Depletion Layer -->
      <rect x="25" y="68" width="55" height="12" fill="#ef4444" opacity="0.6"/>
      <rect x="190" y="68" width="55" height="12" fill="#ef4444" opacity="0.6"/>
      <text x="90" y="60" fill="#ef4444" font-size="8" font-weight="800">P-N 접합 공핍층</text>
      <text x="10" y="95" fill="#fca5a5" font-size="8">• S/D 바닥 전체가 P기판과 접촉 ➔ P-N 접합 형성!</text>
      <text x="10" y="110" fill="#fde047" font-size="8.5" font-weight="800">★ C_j = ε_si · A / W_dep (거대한 기생 커패시턴스)</text>
      <text x="10" y="125" fill="#cbd5e1" font-size="7.5">➔ 신호 충방전 지연(RC Delay) 유발 및 소비전력 증가</text>
    </g>

    <!-- Sub-case 2: SOI MOSFET -->
    <g transform="translate(15, 188)">
      <rect width="270" height="140" rx="5" fill="#1e293b" stroke="#10b981"/>
      <text x="10" y="16" fill="#34d399" font-size="9" font-weight="800">2. SOI MOSFET: S/D 바닥 접합 자체 소멸!</text>
      <!-- Gate -->
      <rect x="90" y="25" width="90" height="10" fill="#38bdf8" rx="1"/>
      <text x="122" y="33" fill="#000" font-size="7">Gate</text>
      <!-- S / D touching BOX directly -->
      <rect x="25" y="35" width="55" height="20" fill="#f59e0b" rx="1"/>
      <text x="35" y="48" fill="#000" font-size="7.5" font-weight="800">Source (N+)</text>
      <rect x="190" y="35" width="55" height="20" fill="#f59e0b" rx="1"/>
      <text x="202" y="48" fill="#000" font-size="7.5" font-weight="800">Drain (N+)</text>
      <rect x="80" y="35" width="110" height="20" fill="#10b981" opacity="0.4"/>
      <text x="115" y="48" fill="#fff" font-size="7.5">Body</text>
      <!-- Buried Oxide (BOX) Layer -->
      <rect x="25" y="55" width="220" height="40" fill="#334155" stroke="#38bdf8" stroke-dasharray="2,2"/>
      <text x="45" y="78" fill="#38bdf8" font-size="9" font-weight="800">매립 산화막 (Buried Oxide, SiO₂)</text>
      <!-- Silicon Substrate below BOX -->
      <rect x="25" y="95" width="220" height="15" fill="#1e293b"/>
      <text x="10" y="118" fill="#a7f3d0" font-size="8">★ S/D 바닥이 BOX와 닿아 P-N 접합면 원천 소멸!</text>
      <text x="10" y="132" fill="#fde047" font-size="8">• C_j 100% 제거! 두꺼운 BOX 산화막 용량(C_BOX) 대체</text>
    </g>

    <!-- Summary Box -->
    <rect x="15" y="338" width="270" height="68" rx="6" fill="#0b1329" stroke="#334155"/>
    <text x="22" y="358" fill="#38bdf8" font-size="8.8" font-weight="800">구조적 판정 결과:</text>
    <text x="22" y="375" fill="#cbd5e1" font-size="8">• "Body와 S/D 분리"의 대상 = <strong>소스/드레인 접합Cap (Cj)</strong></text>
    <text x="22" y="392" fill="#fde047" font-size="8">• S/D-Body P-N 접합 계면 자체가 소멸하는 것임!</text>
  </g>

  <!-- PANEL B: The Relation between Cj and Cdep (Venn / Hierarchy) -->
  <g transform="translate(340, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) Cj와 Cdep의 관계: '이름' vs '물리 실체'</text>

    <!-- Venn / Relationship Diagram -->
    <g transform="translate(15, 42)">
      <rect width="280" height="180" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="20" fill="#fde047" font-size="9.5" font-weight="800">💡 두 개념의 포함 관계와 본질</text>

      <!-- Outer Box: Depletion Capacitance (Physics) -->
      <rect x="20" y="34" width="240" height="132" rx="5" fill="#0b1329" stroke="#38bdf8" stroke-dasharray="3,2"/>
      <text x="30" y="50" fill="#38bdf8" font-size="8.5" font-weight="800">공핍 커패시턴스 (Depletion Capacitance, C_dep) [물리 원리]</text>
      <text x="30" y="64" fill="#94a3b8" font-size="7.5">: 공간 전하 공핍층에 전하가 쌓여 발생하는 모든 정전용량</text>

      <!-- Inner Box 1: Junction Capacitance -->
      <rect x="30" y="74" width="220" height="42" rx="4" fill="#047857" opacity="0.6" stroke="#10b981"/>
      <text x="40" y="90" fill="#a7f3d0" font-size="8.5" font-weight="800">① P-N 접합 커패시턴스 (C_j = C_dep,pn)</text>
      <text x="40" y="105" fill="#fff" font-size="7.5">➔ S/D와 Body 접합부의 공핍층 용량! (SOI가 없애는 것)</text>

      <!-- Inner Box 2: Gate Channel Depletion Cap -->
      <rect x="30" y="120" width="220" height="40" rx="4" fill="#1e293b" stroke="#a855f7"/>
      <text x="40" y="136" fill="#c084fc" font-size="8.5" font-weight="800">② 채널 공핍 커패시턴스 (C_dep,ch)</text>
      <text x="40" y="150" fill="#cbd5e1" font-size="7.5">➔ Gate 산화막 아래 채널의 공핍층 용량 (SS 결정)</text>
    </g>

    <!-- Clear Explanation Text Box -->
    <g transform="translate(15, 232)">
      <rect width="280" height="174" rx="6" fill="#0b1329" stroke="#334155"/>
      <text x="12" y="18" fill="#34d399" font-size="9" font-weight="800">★ 엔지니어의 명쾌한 정리 기준:</text>
      <text x="12" y="38" fill="#cbd5e1" font-size="8.5">Q. "Cj인가, Cdep인가?"</text>
      <text x="12" y="56" fill="#fde047" font-size="8.5" font-weight="700">A. "구조적으로는 Cj이고, 물리적으로는 Cdep이다!"</text>
      
      <text x="12" y="78" fill="#cbd5e1" font-size="8">• S/D-Body 사이의 P-N 접합면에 생기므로</text>
      <text x="20" y="92" fill="#38bdf8" font-size="8">➔ 부르는 **이름은 접합 커패시턴스(Cj)**입니다.</text>

      <text x="12" y="112" fill="#cbd5e1" font-size="8">• 하지만 P-N 접합면의 유전체가 바로 '공핍층'이므로</text>
      <text x="20" y="126" fill="#34d399" font-size="8">➔ 그 **물리적 메커니즘은 공핍 커패시턴스(Cdep)**입니다.</text>

      <text x="12" y="146" fill="#fca5a5" font-size="7.8">⚠️ 단, 게이트 아래 채널의 C_dep,ch와 혼동하지 않기 위해</text>
      <text x="12" y="158" fill="#fca5a5" font-size="7.8">    회로/소자에서는 **'Junction Capacitance (Cj)'**로 명명합니다.</text>
    </g>
  </g>

  <!-- PANEL C: Circuit Benefit & FD-SOI Dual Elimination -->
  <g transform="translate(670, 20)">
    <rect width="290" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) 회로 속도 향상 &amp; FD-SOI 2중 제거</text>

    <!-- Circuit Speed Boost -->
    <g transform="translate(15, 42)">
      <rect width="260" height="135" rx="6" fill="#1e293b" stroke="#f59e0b"/>
      <text x="12" y="18" fill="#fde047" font-size="9" font-weight="800">1. C_j 제거가 가져오는 RC 딜레이 단축</text>
      <text x="12" y="38" fill="#ffffff" font-size="9">τ_delay = R_on · C_total</text>
      <text x="12" y="56" fill="#cbd5e1" font-size="8">C_total = C_gate + C_interconnect + C_j</text>
      <text x="12" y="74" fill="#cbd5e1" font-size="8">• 벌크에서는 S/D 바닥 C_j가 전체의 30~40% 차지!</text>
      <text x="12" y="90" fill="#fde047" font-size="8.5" font-weight="700">➔ SOI에서 C_j 제거 시 C_total 급감!</text>
      <text x="12" y="108" fill="#34d399" font-size="8.5" font-weight="800">★ 스위칭 속도 20~30% 폭등 &amp; 동적 전력(fCV²) 급감</text>
      <text x="12" y="124" fill="#bae6fd" font-size="7.5">• 기생 바이폴라 래치업(Latch-up) 원천 방지</text>
    </g>

    <!-- FD-SOI Dual Benefit -->
    <g transform="translate(15, 188)">
      <rect width="260" height="140" rx="6" fill="#1e293b" stroke="#10b981"/>
      <text x="12" y="18" fill="#34d399" font-size="9.5" font-weight="800">2. FD-SOI의 위대한 2중 제거 (C_j + C_dep)</text>
      <text x="12" y="38" fill="#cbd5e1" font-size="8">FD-SOI(완전공핍형)는 두 가지 기생 용량을 동시 박멸:</text>
      
      <text x="12" y="58" fill="#38bdf8" font-size="8.5" font-weight="700">[혜택 1] S/D 바닥 C_j 소멸:</text>
      <text x="20" y="72" fill="#cbd5e1" font-size="7.8">S/D와 BOX 접촉으로 기생 접합 정전용량 90% 제거</text>

      <text x="12" y="90" fill="#a7f3d0" font-size="8.5" font-weight="700">[혜택 2] 채널 C_dep,ch 극소화:</text>
      <text x="20" y="104" fill="#cbd5e1" font-size="7.8">바디 박막화(T_si &lt; W_dep)로 바디 완전 공핍화 달성</text>
      <text x="20" y="118" fill="#fde047" font-size="8" font-weight="800">➔ SS ≈ 60 mV/dec 달성으로 누설전류 차단!</text>
    </g>

    <!-- Conclusion Box -->
    <rect x="15" y="338" width="260" height="68" rx="6" fill="#0b1329" stroke="#334155"/>
    <text x="20" y="358" fill="#fbbf24" font-size="8.5" font-weight="800">핵심 결론 요약:</text>
    <text x="20" y="375" fill="#cbd5e1" font-size="8">• "Body-S/D 분리" 문맥의 주인공은 **C_j**!</text>
    <text x="20" y="392" fill="#a7f3d0" font-size="8">• C_j의 물리적 작동 원리가 바로 **C_dep**!</text>
  </g>
</svg>""",
    "lecture": r"""
        <!-- Section 1: Direct Clear Answer -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 단도직입 결론: 접합 커패시턴스(Cj)인가, 공핍 커패시턴스(Cdep)인가?
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            질문자님께서 질문하신 문장 <em>"SOI 기술로 body와 S/D를 분리해 기생 cap을 없앤다"</em>에서 말하는 기생 커패시턴스는:
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:18px;">
            <h4 style="color:#38bdf8; font-size:1.05rem; font-weight:800; margin-bottom:8px;">🎯 핵심 판정: "구조적 이름은 접합 커패시턴스(Cj)이고, 물리적 실체는 공핍 커패시턴스(Cdep)입니다!"</h4>
            <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:18px;">
              <li><strong>구조적 명칭 관점</strong>: 소스($N^+$)와 드레인($N^+$)이 바디(P-기판)와 맞닿는 경계면을 분리하므로, <strong>'소스/드레인 접합 커패시턴스(Source/Drain Junction Capacitance, $C_j$)'</strong>를 지칭합니다.</li>
              <li><strong>물리적 메커니즘 관점</strong>: P-N 접합 커패시턴스($C_j$)라는 것의 물리적 정체 자체가 바로 <strong>'P-N 접합면에 형성된 공핍 영역(Depletion Region)에 의해 생기는 공핍 커패시턴스($C_{dep,pn} = \frac{\epsilon_{si} A}{W_{dep}}$)'</strong>입니다.</li>
              <li>따라서 두 개념은 대립되는 배타적 개념이 아니라, <strong>"소자 구조에서 부르는 이름은 접합 커패시턴스($C_j$)이고, 그 커패시턴스가 생기는 물리학적 원리가 바로 공핍 영역(Depletion Region)의 공핍 커패시턴스($C_{dep}$)"</strong>인 것입니다!</li>
            </ul>
          </div>
        </div>

        <!-- Section 2: Why Bulk has Huge Cj and How SOI Eliminates it -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 벌크(Bulk) Si의 비극과 SOI가 $C_j$를 없애는 물리적 메커니즘
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            이해를 돕기 위해 기존 벌크 트랜지스터와 SOI 트랜지스터의 소스/드레인 바닥면을 비교해 보겠습니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#f87171; margin:14px 0 8px;">■ 벌크(Bulk) MOSFET : 거대한 S/D 바닥 접합 커패시턴스</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:10px;">
            벌크 웨이퍼에서는 $N^+$로 고농도 도핑된 소스와 드레인이 P형 실리콘 기판(바디) 위에 직접 만들어집니다.<br>
            따라서 소스/드레인의 <strong>밑바닥 전체($A_{bottom}$)와 측면($A_{sw}$)이 기판 실리콘과 광범위하게 맞닿아 거대한 P-N 접합을 형성</strong>합니다:
            $$C_{j,bulk} = C_{j,bottom} + C_{j,sw} = \frac{\epsilon_{si} A_{bottom}}{W_{dep,bottom}} + \frac{\epsilon_{si} A_{sw}}{W_{dep,sw}}$$
            이 접합 공핍 커패시턴스는 트랜지스터가 0에서 1로 스위칭할 때마다 매번 전하를 채우고 비워야 하므로, <strong>전체 칩 신호 지연(RC Delay)의 30~40%를 차지하는 주범</strong>이자 전력 낭비의 온상입니다.
          </p>

          <h4 style="font-size:1rem; font-weight:700; color:#34d399; margin:14px 0 8px;">■ SOI (Silicon-On-Insulator) : P-N 접합면 자체를 물리적으로 소멸!</h4>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1; margin-bottom:12px;">
            SOI 웨이퍼는 실리콘 기판 위에 두꺼운 **매립 산화막(BOX: Buried Oxide, $\text{SiO}_2$, 수십~수백 nm)**이 깔려 있고, 그 위에 얇은 실리콘 박막이 얹혀 있는 구조입니다.<br>
            소스를 만들 때 실리콘 박막 바닥까지 도펀트를 주입하면, **소스/드레인의 밑바닥이 기판 실리콘이 아니라 절연체인 BOX 산화막과 직접 맞닿게 됩니다!**
          </p>
          <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.75; padding-left:20px; margin-bottom:12px;">
            <li>소스/드레인 밑바닥에 실리콘 바디가 없으므로 <strong>P-N 접합면 자체가 물리적으로 존재하지 않습니다 (접합 소멸!)</strong>.</li>
            <li>P-N 접합 공핍층($\epsilon_{si}=11.7$, 얇은 $W_{dep}$) 대신, <strong>유전율이 3배나 낮고 두께가 훨씬 두꺼운 산화막($\epsilon_{ox}=3.9, t_{BOX} \gg W_{dep}$)</strong>이 바닥을 받치게 됩니다:
              $$C_{BOX} = \frac{\epsilon_{ox} A_{bottom}}{t_{BOX}} \ll C_{j,bottom}$$
            </li>
            <li>그 결과 S/D 하부의 기생 커패시턴스가 <strong>기존 벌크 대비 90% 이상 격감(사실상 제거)</strong>됩니다.</li>
          </ul>
        </div>

        <!-- Section 3: The Source of Confusion - Gate Channel Depletion Cap -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 질문자님께서 헷갈리셨던 이유: '채널 공핍 커패시턴스($C_{dep,ch}$)'와의 용어 혼선
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            질문자님께서 <em>"이게 접합 cap인가, depletion cap인가?"</em> 고민하셨던 이유는 반도체 교재에서 **두 가지 서로 다른 위치의 커패시턴스를 모두 '공핍(Depletion)'이라는 단어로 부르기 때문**입니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #f59e0b; padding:14px 18px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#fbbf24; font-size:1rem; font-weight:700; margin-bottom:8px;">💡 반도체 엔지니어가 명확히 구별해야 하는 2대 공핍 커패시턴스</h4>
            <ol style="color:#cbd5e1; font-size:0.9rem; line-height:1.8; padding-left:18px;">
              <li><strong>① 소스/드레인 접합 공핍 커패시턴스 ($C_j = C_{dep,pn}$)</strong>
                <br>• 위치: **소스/드레인과 바디(기판) 사이의 P-N 접합면**
                <br>• 영향: 회로의 스위칭 속도(RC 딜레이) 및 동적 전력 소모($f C V^2$) 결정
                <br>• <strong>★ SOI가 Body와 S/D를 분리해서 없애는 바로 그 주인공!</strong>
              </li>
              <li><strong>② 게이트 채널 공핍 커패시턴스 ($C_{dep,ch}$)</strong>
                <br>• 위치: **게이트 산화막 바로 아래 채널 표면에 형성되는 수직 공핍층**
                <br>• 영향: 게이트 전압 분배 및 서브스레시홀드 스윙($SS = 60(1 + C_{dep,ch}/C_{ox})$) 결정
                <br>• (S/D와 바디 사이가 아니라 게이트와 채널 사이의 커패시턴스임)
              </li>
            </ol>
          </div>

          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1;">
            문장에서 <strong>"body와 s/d를 분리해"</strong>라고 명확히 주어와 목적어를 지정했으므로, 게이트 아래 채널($C_{dep,ch}$)이 아니라 **소스/드레인과 바디 사이의 '접합 커패시턴스($C_j$)'**를 말하는 것임이 100% 명백합니다.
          </p>
        </div>

        <!-- Section 4: FD-SOI Dual Revolution -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#ef4444; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. FD-SOI의 위대한 혁신: $C_j$와 채널 $C_{dep,ch}$의 동시 박멸
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            더욱 놀라운 사실은 최신 **FD-SOI (Fully Depleted SOI, 완전공핍형 SOI)** 기술은 이 두 가지 기생 커패시턴스를 **동시에 둘 다 없애버린다**는 점입니다:
          </p>
          <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:22px; margin-bottom:14px;">
            <li><strong>동시 혜택 1 ($C_j$ 박멸)</strong>: S/D 바닥이 BOX 산화막에 닿아 소스/드레인 접합 커패시턴스($C_j$)를 없애 **회로 동작 속도를 20~30% 폭등**시킵니다.</li>
            <li><strong>동시 혜택 2 ($C_{dep,ch}$ 박멸)</strong>: 바디 실리콘 박막 두께($T_{si}$)를 $5\sim6\,\text{nm}$로 극도로 얇게 깎아 채널 전체를 완전 공핍화(Fully Depleted)시킴으로써, 게이트 아래 채널 공핍 커패시턴스($C_{dep,ch}$)까지 0에 가깝게 만들어 **서브스레시홀드 스윙을 이상치인 $SS \approx 60\,\text{mV/dec}$로 복원**하고 누설전류를 잡습니다.</li>
          </ul>
        </div>

        <!-- Section 5: Summary Table -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.15rem; font-weight:800; color:#e2e8f0; margin-bottom:12px;">
            5. 핵심 요약 비교 정리표
          </h3>
          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">질문 항목</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">명칭 및 물리적 분류</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">형성 위치</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">SOI 기술의 제거 메커니즘</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#38bdf8;">문장의 직접적 타깃</td>
                  <td style="padding:10px 14px; color:#34d399; font-weight:700;">접합 커패시턴스 ($C_j$)</td>
                  <td style="padding:10px 14px;">소스/드레인($N^+$) ↔ 바디($P$) 계면</td>
                  <td style="padding:10px 14px;">S/D 하부에 BOX 산화막을 깔아 <strong>P-N 접합면 자체를 물리적으로 소멸</strong></td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#f59e0b;">$C_j$의 물리적 본질</td>
                  <td style="padding:10px 14px;">공핍 커패시턴스 ($C_{dep,pn}$)</td>
                  <td style="padding:10px 14px;">P-N 접합의 역방향 공핍층 공간 전하</td>
                  <td style="padding:10px 14px;">접합이 사라지므로 <strong>공핍 영역 전하 변조 메커니즘도 함께 소멸</strong></td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#c084fc;">채널 공핍 커패시턴스</td>
                  <td style="padding:10px 14px;">채널 $C_{dep,ch}$ (SS 결정 인자)</td>
                  <td style="padding:10px 14px;">게이트 산화막 직하부 채널 영역</td>
                  <td style="padding:10px 14px;">FD-SOI에서 바디 박막화($T_{si} < W_{dep}$)를 통해 <strong>$C_{dep,ch} \approx 0$화 동시 달성</strong></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 80 topics (q-80 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(80, 0, -1):
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

    # Step 4: Update header description to 81 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 'SOI로 없애는 기생Cap은 접합Cap(Cj)일까 공핍Cap(Cdep)일까?'이 위치하며, 총 81개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 SOI Cj vs Cdep topic!")
