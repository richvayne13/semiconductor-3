# -*- coding: utf-8 -*-
"""
insert_plasma_loss_q01.py
사용자 질문:
"[질문1] Plasma의 생성에 대해서는 충분히 잘 들었습니다. 반대로, Plasma의 소멸에 대해서도 설명하실 수 있나요.
Plasma의 발생 원리도 중요하지만, Plasma의 Density와 생성된 Plasma를 유지하기 위해서는 Plasma의 소멸 메커니즘에 대한 이해도 중요합니다. 일반적으로 Plasma의 소멸은 양이온의 중성화, 전자의 Loss로 설명할 수 있습니다. Plasma 내 양이온은 Cathode와 충돌했을 때, 혹은 Chamber 외부에서 Recombination이 일어나면서 중성기체로 돌아가게 되죠. 전자의 경우, 양이온과 충돌하지 못 하게 되면 Anode로 들어가면서 전자 Loss가 발생하게 됩니다. 양이온과 전자의 Loss가 높으면 높을수록, 앞서 설명드렸던 글로우 방전을 일으키기 어렵기 때문에 Plasma의 Density가 낮아지거나 완전히 소멸하게 됩니다.

여기서 전자가 양이온이아니라 기체원자와 충돌하지못해서 anode로 들어가면 전자loss가발생하는거지?"

기존 103개 질문을 Q02~Q104로 시프트하고, 최상단 Q01에 신규 등록 (총 104개 질문 백과사전 완성).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (플라즈마 물리 & 소멸 메커니즘 · 전자 손실의 실체와 벽면 재결합 원리 완전 교정)",
    "title": "플라즈마의 소멸(Loss) 메커니즘과 전자 손실의 실체: '기체 원자 충돌 미흡' vs '양이온 재결합' 오류 교정 및 벽면 손실(Wall Loss) 완전 해부",
    "nav_title": "플라즈마 소멸 메커니즘: 전자 손실과 벽면 재결합의 실체",
    "summary": [
        "<strong>1. 사용자 지적의 정확성 (100% 오류 교정)</strong>: 사용자님의 지적이 100% 정확합니다! 원문의 <em>'전자가 양이온과 충돌하지 못하면'</em>은 명백한 물리적 개념 오류이며, 정확하게는 <strong>'전자가 중성 기체 원자(Neutral Gas Atom)와 이온화 충돌을 통해 증식하지 못하고 Anode(양극)나 벽면으로 빠져나갈 때' 전자 Loss가 발생</strong>하는 것입니다.",
        "<strong>2. 전자와 양이온이 충돌하면 손실을 막는 게 아니라 '오히려 소멸'</strong>: 전자가 양이온($\\text{Ar}^+$)과 충돌하는 것은 플라즈마 생성이 아니라, 둘이 합쳐져 중성 원자로 돌아가는 <strong>'체적 재결합(Volume Recombination: $e^- + \\text{Ar}^+ \\rightarrow \\text{Ar}$)'</strong>으로 전자가 소멸하는 과정입니다. 따라서 '양이온과 충돌하지 못해서 Loss가 난다'는 서술은 물리적 인과관계가 정반대로 기술된 것입니다.",
        "<strong>3. 반도체 플라즈마의 밀도 특성: 중성 원자가 99.99% 압도</strong>: 반도체 저온 플라즈마(Weakly Ionized Plasma)는 이온화율이 $10^{-6} \\sim 10^{-4}$에 불과하여, 챔버 내 입자의 99.99% 이상이 중성 기체($\\text{Ar}$)입니다. 전자가 날아가다 마주치는 상대는 사실상 전부 중성 기체 원자이며, 이들과 충분히 충돌하여 2차 전자를 쏟아내야 플라즈마가 유지됩니다.",
        "<strong>4. 플라즈마 소멸의 2대 축: 벽면 손실(Wall Loss) vs 체적 손실(Volume Loss)</strong>: 플라즈마의 실제 소멸은 99% 이상 <strong>'벽면 손실(Surface Recombination)'</strong>에서 일어납니다. 가벼운 전자는 Anode나 접지 벽면으로 빨려 들어가 흡수되고, 무거운 양이온은 Cathode나 벽면으로 끌려가 표면 전자를 받아 중성화(Neutralization)되어 중성 기체로 환원됩니다.",
        "<strong>5. 글로우 방전 정상 상태의 본질 (생성률 = 소멸률 평형)</strong>: 플라즈마가 유지되려면 $\\text{Generation Rate (전자-기체 이온화)} = \\text{Loss Rate (벽면 전극 흡수)}$의 균형이 성립해야 합니다. 압력이 너무 낮아 평균자유행로(MFP)가 길어지면 전자가 기체와 부딪치지도 못하고 Anode로 탈출(Loss 폭증)하여 플라즈마가 즉시 꺼지게 됩니다."
    ],
    "svg_title": "📊 [플라즈마 소멸 메커니즘 및 전자 손실(Loss) 종합 해부 다이어그램] (A) 전자 손실의 진짜 원인 (중성 기체 충돌 미흡 vs Anode 흡수) | (B) 원문 오류 교정: 전자-양이온 충돌은 '체적 재결합(소멸)' | (C) 플라즈마 소멸 2대 경로 (벽면 손실 vs 체적 손실)",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: True Electron Loss Mechanism -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 전자 손실(Electron Loss)의 실체</text>

    <!-- Visual Chamber Cross-section -->
    <g transform="translate(15, 40)">
      <rect width="270" height="210" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 플라즈마 생성(유지) vs 손실(Loss)</text>

      <!-- Cathode (Top) -->
      <rect x="15" y="28" width="240" height="20" rx="3" fill="#450a0a" stroke="#ef4444"/>
      <text x="75" y="42" fill="#fca5a5" font-size="7.5" font-weight="800">Cathode (음극, -Vdc / RF 주입)</text>

      <!-- Case 1: Healthy Ionization (Left) -->
      <g transform="translate(20, 56)">
        <rect width="110" height="110" rx="4" fill="#0b1329" stroke="#10b981"/>
        <text x="8" y="14" fill="#34d399" font-size="7" font-weight="800">정상: 이온화 충돌 (유지)</text>
        <circle cx="20" cy="35" r="5" fill="#38bdf8"/>
        <text x="18" y="38" fill="#0f172a" font-size="6" font-weight="900">e⁻</text>
        <path d="M 26 35 L 50 50" stroke="#38bdf8" stroke-width="1.5" marker-end="url(#arrowCyan)"/>
        <!-- Gas Atom Ar -->
        <circle cx="58" cy="55" r="9" fill="#64748b"/>
        <text x="52" y="58" fill="#f8fafc" font-size="6.5" font-weight="800">Ar</text>
        <!-- Collision products -->
        <path d="M 68 55 L 90 42" stroke="#38bdf8" stroke-width="1.2" marker-end="url(#arrowCyan)"/>
        <path d="M 68 55 L 90 68" stroke="#38bdf8" stroke-width="1.2" marker-end="url(#arrowCyan)"/>
        <text x="25" y="86" fill="#fde047" font-size="6.5" font-weight="800">e⁻ + Ar ➔ Ar⁺ + 2e⁻</text>
        <text x="18" y="100" fill="#a7f3d0" font-size="6.2">전자 증식 (Avalanche)!</text>
      </g>

      <!-- Case 2: Electron Loss to Anode (Right) -->
      <g transform="translate(140, 56)">
        <rect width="110" height="110" rx="4" fill="#0b1329" stroke="#ef4444"/>
        <text x="8" y="14" fill="#f87171" font-size="7" font-weight="800">손실: 충돌 없이 흡수 (Loss)</text>
        <circle cx="20" cy="35" r="5" fill="#38bdf8"/>
        <text x="18" y="38" fill="#0f172a" font-size="6" font-weight="900">e⁻</text>
        <!-- Fly straight through without collision -->
        <path d="M 26 35 L 55 75 L 55 105" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,2" marker-end="url(#arrowRed)"/>
        <text x="10" y="58" fill="#94a3b8" font-size="6">기체 원자(Ar)와</text>
        <text x="10" y="69" fill="#f87171" font-size="6.2" font-weight="800">충돌하지 못하고 직행!</text>
        <text x="10" y="94" fill="#ef4444" font-size="6.5" font-weight="800">Anode로 흡수 소멸!</text>
      </g>

      <!-- Anode (Bottom) -->
      <rect x="15" y="174" width="240" height="22" rx="3" fill="#14532d" stroke="#22c55e"/>
      <text x="75" y="189" fill="#86efac" font-size="7.5" font-weight="800">Anode (양극 / 접지 챔버 벽면, 0V)</text>
    </g>

    <!-- Takeaway Box -->
    <g transform="translate(15, 260)">
      <rect width="270" height="145" rx="5" fill="#0b1329" stroke="#38bdf8"/>
      <text x="12" y="18" fill="#38bdf8" font-size="8.8" font-weight="800">💡 사용자 지적 100% 확인</text>
      <text x="12" y="36" fill="#cbd5e1" font-size="7.5">• 전자가 마주쳐야 할 대상은 <strong>중성 기체 원자(Ar)</strong>!</text>
      <text x="12" y="52" fill="#cbd5e1" font-size="7.5">• 기체와 충돌하여 새 전자를 불리지 못하고</text>
      <text x="16" y="66" fill="#f87171" font-size="7.8" font-weight="800">  양극(Anode)으로 도망쳐 흡수되는 것이 전자 Loss!</text>
      <text x="12" y="86" fill="#fde047" font-size="7.5" font-weight="800">• 압력이 낮을수록(MFP 길수록) 충돌 기회 박탈</text>
      <text x="16" y="100" fill="#cbd5e1" font-size="7.2">➔ 전자가 그냥 Anode로 쑥 빠져나가 방전 꺼짐</text>
      <text x="12" y="122" fill="#34d399" font-size="7.5" font-weight="800">➔ "기체원자와 충돌 못해서 Loss" 질문이 완벽히 맞음!</text>
    </g>
  </g>

  <!-- PANEL B: Error Correction: Electron-Ion Collision -->
  <g transform="translate(335, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#ef4444" stroke-width="1.2"/>
    <text x="16" y="26" fill="#f87171" font-size="12" font-weight="800">■ (B) 원문 오류 교정: 전자-양이온 충돌</text>

    <!-- Inversion Analysis Box -->
    <g transform="translate(15, 40)">
      <rect width="280" height="205" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">2. '전자와 양이온의 충돌'은 왜 오류인가?</text>

      <!-- Recombination Box -->
      <g transform="translate(10, 26)">
        <rect width="260" height="75" rx="4" fill="#0b1329" stroke="#ef4444"/>
        <text x="10" y="16" fill="#f87171" font-size="7.8" font-weight="800">❌ 전자와 양이온이 충돌하면? ➔ '소멸(재결합)'!</text>
        <text x="16" y="32" fill="#fde047" font-size="7.2" font-weight="800">e⁻ + Ar⁺ ➔ Ar + hν (체적 재결합, Recombination)</text>
        <text x="16" y="46" fill="#cbd5e1" font-size="7">• 전자가 양이온을 만나면 둘 다 사라져 중성 기체 환원!</text>
        <text x="16" y="58" fill="#cbd5e1" font-size="7">• 즉, 양이온 충돌은 전자를 살리는 게 아니라</text>
        <text x="16" y="70" fill="#f87171" font-size="7" font-weight="800">   오히려 전자가 소멸되는 또 다른 Loss 메커니즘!</text>
      </g>

      <!-- Density Comparison Box -->
      <g transform="translate(10, 110)">
        <rect width="260" height="85" rx="4" fill="#0b1329" stroke="#10b981"/>
        <text x="10" y="16" fill="#34d399" font-size="7.8" font-weight="800">📊 반도체 플라즈마 입자 밀도비 (Weakly Ionized)</text>
        <text x="16" y="32" fill="#cbd5e1" font-size="7.2">• 중성 기체 원자 밀도 : $n_g \sim 10^{15}\,\text{cm}^{-3}$ (99.99%)</text>
        <text x="16" y="46" fill="#cbd5e1" font-size="7.2">• 양이온/전자 밀도 : $n_e \sim 10^{10}\,\text{cm}^{-3}$ (0.01% 이하)</text>
        <text x="16" y="60" fill="#fde047" font-size="7.2" font-weight="800">➔ 중성 기체가 양이온보다 100,000배 압도적으로 많음!</text>
        <text x="16" y="74" fill="#cbd5e1" font-size="6.8">• 전자가 양이온과 마주칠 확률은 사실상 거의 제로(0)!</text>
      </g>
    </g>

    <!-- Why Original Text Had a Mistake -->
    <g transform="translate(15, 260)">
      <rect width="280" height="145" rx="5" fill="#0b1329" stroke="#ef4444"/>
      <text x="12" y="18" fill="#f87171" font-size="8.8" font-weight="800">⚠️ 원문 작성자의 명백한 착각/말실수</text>
      <text x="12" y="38" fill="#cbd5e1" font-size="7.5">• 원문: <em>"양이온과 충돌하지 못하게 되면 Anode로..."</em></text>
      <text x="12" y="56" fill="#fde047" font-size="7.8" font-weight="800">➔ 작성자가 '기체 원자(중성 가스)'와 '양이온'을</text>
      <text x="18" y="70" fill="#fde047" font-size="7.8" font-weight="800">   용어상 혼동하여 잘못 말한 것입니다!</text>
      <text x="12" y="90" fill="#cbd5e1" font-size="7.2">• 전자가 양이온을 중성화하기 위해 부딪치는 것은</text>
      <text x="16" y="102" fill="#cbd5e1" font-size="7.2">  벽면(Wall)에서 일어나는 현상이지 비행 중 충돌이 아님.</text>
      <text x="12" y="122" fill="#38bdf8" font-size="7.5" font-weight="800">결론: 사용자님의 지적이 물리적으로 100% 참(True)!</text>
    </g>
  </g>

  <!-- PANEL C: Complete Plasma Loss Mechanisms -->
  <g transform="translate(660, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (C) 플라즈마 소멸 2대 실제 경로</text>

    <!-- Breakdown of Loss mechanisms -->
    <g transform="translate(15, 40)">
      <rect width="270" height="235" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">소멸 경로의 물리적 분류</text>

      <!-- Pathway 1: Wall Loss (Dominant) -->
      <g transform="translate(10, 26)">
        <rect width="250" height="92" rx="4" fill="#0b1329" stroke="#38bdf8"/>
        <text x="8" y="14" fill="#38bdf8" font-size="7.5" font-weight="800">1. 벽면/전극 표면 손실 (Wall Loss) ★ [99% 이상 지배]</text>
        <text x="12" y="28" fill="#cbd5e1" font-size="6.8">• <strong>전자 손실</strong>: 가벼운 전자가 빠른 확산으로</text>
        <text x="16" y="40" fill="#cbd5e1" font-size="6.8">  Anode(양극) 및 접지 챔버 벽면에 흡수되어 소멸</text>
        <text x="12" y="54" fill="#cbd5e1" font-size="6.8">• <strong>양이온 손실</strong>: 무거운 양이온이 음극 쉬스 전계로</text>
        <text x="16" y="66" fill="#cbd5e1" font-size="6.8">  Cathode 및 벽면에 충돌 ➔ 전자를 받아 중성화</text>
        <text x="12" y="80" fill="#fde047" font-size="7" font-weight="800">➔ 벽면이 전자-이온의 거대한 '재결합 무덤' 역할!</text>
      </g>

      <!-- Pathway 2: Volume Recombination -->
      <g transform="translate(10, 126)">
        <rect width="250" height="95" rx="4" fill="#0b1329" stroke="#f59e0b"/>
        <text x="8" y="14" fill="#fbbf24" font-size="7.5" font-weight="800">2. 체적 재결합 (Volume Recombination) [저압서 극소]</text>
        <text x="12" y="28" fill="#cbd5e1" font-size="6.8">• 기체 공간 내에서 전자와 양이온이 직접 충돌</text>
        <text x="12" y="40" fill="#fde047" font-size="6.8" font-weight="800">➔ $e^- + \text{Ar}^+ \rightarrow \text{Ar} + h\nu$ (빛 방출 후 중성화)</text>
        <text x="12" y="54" fill="#cbd5e1" font-size="6.8">• 저압(mTorr) 공정에서는 운동량/에너지 보존을 위한</text>
        <text x="16" y="66" fill="#cbd5e1" font-size="6.8">  3체 충돌 확률이 낮아 거의 일어나지 않음</text>
        <text x="12" y="80" fill="#94a3b8" font-size="6.8">➔ 반도체 챔버 소멸의 본체는 99% '벽면 손실'!</text>
      </g>
    </g>

    <!-- Steady State Balance Box -->
    <g transform="translate(15, 285)">
      <rect width="270" height="120" rx="6" fill="#0b1329" stroke="#10b981"/>
      <text x="12" y="16" fill="#34d399" font-size="8.8" font-weight="800">⚖️ 정상 상태(Steady-State) 유지 조건</text>
      <text x="12" y="36" fill="#fde047" font-size="7.8" font-weight="800">생성률 (Generation) = 소멸률 (Loss)</text>
      <text x="12" y="54" fill="#cbd5e1" font-size="7">• 전자-기체 이온화 속도 = 벽면 흡수 + 재결합 속도</text>
      <text x="12" y="72" fill="#cbd5e1" font-size="7">• 생성률 &gt; 소멸률 ➔ 플라즈마 밀도 상승</text>
      <text x="12" y="90" fill="#f87171" font-size="7">• 소멸률 &gt; 생성률 (압력 급감, 벽면 흡수 폭증)</text>
      <text x="16" y="104" fill="#f87171" font-size="7.2" font-weight="800">➔ 글로우 방전 유지 불가 ➔ 플라즈마 소멸 (Off)!</text>
    </g>
  </g>

  <!-- Markers -->
  <defs>
    <marker id="arrowCyan" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#38bdf8" />
    </marker>
    <marker id="arrowRed" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#ef4444" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- SECTION 1: Error Correction and Fact Check -->
        <div style="margin-top:20px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 사용자 질문 팩트 체크: "기체 원자와 충돌하지 못해서 Anode로 들어가 Loss가 나는 건가요?"
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            <strong>사용자님의 지적이 100% 정확하고 날카롭습니다!</strong><br>
            제시해 주신 질문 원문의 <em>"전자의 경우, 양이온과 충돌하지 못하게 되면 Anode로 들어가면서 전자 Loss가 발생하게 됩니다"</em>라는 문장은 <strong>명백한 개념적 오류(또는 용어의 혼동)</strong>입니다.
          </p>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
            <div style="background:#0f172a; border-left:4px solid #ef4444; padding:16px 18px; border-radius:0 8px 8px 0;">
              <h4 style="color:#f87171; font-size:0.95rem; font-weight:800; margin-bottom:6px;">
                ❌ 원문 서술의 치명적 오류
              </h4>
              <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
                <em>"전자가 양이온과 충돌하지 못해서 Loss가 난다?"</em><br>
                ➔ <strong>물리적으로 완전히 틀린 인과관계입니다!</strong><br>
                전자가 날아가다 양이온($\text{Ar}^+$)과 충돌하면, 이온화 증식이 일어나는 것이 아니라 전자와 양이온이 합쳐져 중성 원자로 돌아가는 <strong>'체적 재결합(Volume Recombination: $e^- + \text{Ar}^+ \rightarrow \text{Ar}$)'</strong>이 일어납니다. 즉, 양이온과의 충돌은 전자를 유지시키는 것이 아니라 <strong>오히려 전자가 소멸되는 또 다른 Loss 메커니즘</strong>입니다!
              </p>
            </div>
            <div style="background:#0f172a; border-left:4px solid #10b981; padding:16px 18px; border-radius:0 8px 8px 0;">
              <h4 style="color:#34d399; font-size:0.95rem; font-weight:800; margin-bottom:6px;">
                ✔ 올바른 물리적 실체 (사용자님의 생각 일치)
              </h4>
              <p style="color:#cbd5e1; font-size:0.88rem; line-height:1.7; margin:0;">
                <em>"전자가 중성 기체 원자와 충돌하지 못해서 Loss가 난다!"</em><br>
                ➔ <strong>100% 완벽한 정답입니다!</strong><br>
                전자가 전기장에서 가속되면서 <strong>중성 기체 원자($\text{Ar}$)</strong>와 쾅 부딪쳐야 <strong>'이온화 충돌($e^- + \text{Ar} \rightarrow \text{Ar}^+ + 2e^-$)'</strong>을 일으켜 새 전자를 복제(증식)할 수 있습니다.
                그런데 기체와 충돌하지 못하고 그냥 <strong>Anode(양극)나 벽면으로 쑥 빨려 들어가 흡수(Wall Loss)</strong>되어 버리면 전자가 영구 손실되는 것입니다.
              </p>
            </div>
          </div>

          <div style="background:#1e293b; padding:14px 18px; border-radius:8px; margin-bottom:18px;">
            <p style="color:#fde047; font-size:0.9rem; line-height:1.7; margin:0;">
              💡 <strong>작성자의 의도 추정</strong>: 질문 텍스트를 작성한 사람은 <em>'중성 기체 원자(Neutral Gas Atom)'</em>라고 적었어야 할 자리에 무심코 <em>'양이온'</em>이라는 단어를 잘못 썼거나, 양이온과의 재결합 개념을 뒤섞어 오기한 것입니다. 사용자님의 물리적 직관이 완전히 옳았습니다.
            </p>
          </div>
        </div>

        <!-- SECTION 2: Why Colliding with Gas Atom is the Key -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fde047; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 반도체 플라즈마의 밀도 법칙: 왜 전자는 기체 원자하고만 부딪칠까?
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            반도체 공정에서 사용하는 플라즈마는 핵융합 플라즈마와 달리 **'약전리 플라즈마(Weakly Ionized Plasma)'** 또는 **'저온 플라즈마(Cold Plasma)'**입니다:
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:16px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:800; margin-bottom:8px;">
              입자 밀도의 압도적 불균형: 10만 배의 차이
            </h4>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.85; padding-left:20px; margin:0;">
              <li><strong>중성 기체 원자 밀도 ($n_g$)</strong>: 약 $10^{14} \sim 10^{16}\,\text{cm}^{-3}$ (전체 챔버 입자의 **99.99% 이상**)</li>
              <li><strong>전자 및 양이온 밀도 ($n_e, n_i$)</strong>: 약 $10^{9} \sim 10^{11}\,\text{cm}^{-3}$ (전체의 **0.01% 미만**)</li>
              <li><strong>이온화도 (Ionization Degree)</strong>: $\alpha = \frac{n_i}{n_g + n_i} \approx 10^{-6} \sim 10^{-4}$ ($0.0001\% \sim 0.01\%$)</li>
            </ul>
          </div>

          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:14px;">
            챔버 안에는 <strong>중성 기체 원자가 이온보다 10만 배에서 100만 배나 압도적으로 빽빽하게 가득 차 있습니다.</strong>
            따라서 전자가 방전 공간을 날아가다 마주치는 대상은 확률적으로 99.999%가 **중성 기체 원자($\text{Ar}$)**입니다.
            전자가 날아가는 동안 양이온과 마주쳐 충돌할 확률은 사실상 거의 존재하지 않습니다.
          </p>
        </div>

        <!-- SECTION 3: The True Plasma Loss Mechanisms -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#10b981; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 플라즈마 소멸(Loss)의 2대 메커니즘 완전 해부
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            플라즈마가 소멸되는 진짜 물리적 메커니즘은 공간에 따라 **'표면(벽면) 손실'**과 **'체적 손실'**의 두 가지로 정확히 분류됩니다:
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#38bdf8; font-size:1rem; font-weight:800; margin-bottom:6px;">
              경로 ① 벽면/전극 표면 손실 (Wall Loss / Surface Recombination) ★ [99% 이상 지배!]
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              저압 반도체 장비에서 플라즈마가 소멸하는 현상의 99% 이상은 챔버의 전극과 금속 내벽(Wall)에서 일어납니다:
              <br>• <strong>전자 손실 (Electron Loss)</strong>: 전자는 질량이 매우 가벼워 열속도($v_{th,e} = \sqrt{8kT_e/\pi m_e}$)가 이온보다 수백 배 빠릅니다. 전자는 양극(Anode) 또는 접지된 챔버 금속 벽면(Grounded Chamber Wall)으로 광속으로 도달하여 **전극의 도선 회로로 흘러 들어가 영구 흡수(Loss)**됩니다.
              <br>• <strong>양이온 손실 (Ion Loss)</strong>: 양이온은 음극(Cathode)이나 벽면 쉬스(Sheath) 전계에 이끌려 **보옴 속도($u_B = \sqrt{kT_e/M}$)**로 벽면에 충돌합니다. 벽면에 부딪힌 양이온은 금속 표면의 자유전자를 하나 낚아채어 **중성 원자(Neutral Atom)로 환원(중성화)**된 뒤 진공 펌프로 배출됩니다.
              <br>➔ 즉, <strong>챔버 벽면 전체가 전자와 양이온이 만나 소멸하는 거대한 '표면 재결합 무덤'</strong>인 것입니다!
            </p>
          </div>

          <div style="background:#0f172a; border-left:4px solid #fbbf24; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:14px;">
            <h4 style="color:#fbbf24; font-size:1rem; font-weight:800; margin-bottom:6px;">
              경로 ② 체적 손실 (Volume Loss / Volume Recombination) [저압에서는 극히 미미]
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              벽면이 아니라 플라즈마 기체 공간 한가운데서 전자와 양이온이 직접 만나 결합하는 현상입니다:
              <br>• <strong>방사 재결합 (Radiative Recombination)</strong>: $e^- + \text{Ar}^+ \rightarrow \text{Ar} + h\nu$ (에너지를 빛으로 방출하며 결합)
              <br>• <strong>3체 재결합 (Three-body Recombination)</strong>: $e^- + e^- + \text{Ar}^+ \rightarrow \text{Ar} + e^-$ (세 입자가 동시에 충돌하여 잉여 에너지 분산)
              <br>➔ 그러나 반도체 공정(수 mTorr ~ 수백 mTorr)은 기체 밀도가 낮아 3개 입자가 한 번에 만날 확률이 극히 희박합니다. 따라서 <strong>기체 공간 내에서의 체적 재결합은 1% 미만이며, 소멸의 본체는 전적으로 벽면 손실(Wall Loss)</strong>입니다.
            </p>
          </div>
        </div>

        <!-- SECTION 4: Steady-State Glow Discharge Balance -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. 글로우 방전 유지의 절대 법칙: 생성률(Generation) = 소멸률(Loss) 평형
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            플라즈마가 꺼지지 않고 일정한 밀도(Density)를 유지(Steady-state)하기 위한 지배 방정식은 다음과 같습니다:
          </p>

          <div style="background:#1e293b; padding:16px 20px; border-radius:8px; margin-bottom:16px;">
            <div style="text-align:center; font-size:1.15rem; font-weight:800; color:#38bdf8; margin-bottom:10px;">
              $$\frac{dn_e}{dt} = G - L = n_e n_g K_{iz} - \frac{n_e}{\tau_{loss}} = 0$$
            </div>
            <ul style="color:#cbd5e1; font-size:0.9rem; line-height:1.85; padding-left:20px; margin:0;">
              <li><strong>$G$ (생성률, Generation Rate)</strong>: 전자와 중성 기체 원자의 이온화 충돌로 초당 생겨나는 전자 수 ($n_e \cdot n_g \cdot K_{iz}$)</li>
              <li><strong>$L$ (손실률, Loss Rate)</strong>: 확산에 의해 Anode/벽면으로 빠져나가 소멸하는 초당 전자 수 ($n_e / \tau_{loss}$)</li>
              <li><strong>방전 유지 조건 ($G = L$)</strong>: 초당 만들어지는 전자 수가 벽면으로 빠져나가는 전자 수와 정확히 같아야 플라즈마 밀도가 유지됩니다.</li>
            </ul>
          </div>

          <div style="background:#0f172a; border-left:4px solid #ef4444; padding:16px 20px; border-radius:0 8px 8px 0;">
            <h4 style="color:#f87171; font-size:1rem; font-weight:800; margin-bottom:6px;">
              왜 전자가 기체와 충돌하지 못하면 플라즈마가 꺼질까? (파센 법칙의 좌측 한계)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7; margin:0;">
              챔버 압력이 너무 낮거나 전극 간격이 너무 좁으면 전자의 **평균자유행로(Mean Free Path, $\lambda_{mfp} \propto 1/P$)**가 챔버 크기보다 길어집니다.
              그러면 음극에서 튀어나온 전자가 기체 원자와 충돌해 이온화를 일으키기도 전에 **그냥 곧장 Anode 전극으로 날아가 흡수(Loss 폭증)**되어 버립니다.
              <br>생성률($G$)이 바닥나고 손실률($L$)이 압도하므로, 연쇄 증식(Avalanche)이 불가능해져 <strong>플라즈마는 즉시 소멸(Extinction, 방전 꺼짐)</strong>하게 됩니다!
            </p>
          </div>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 103 topics (q-103 down to q-01) by +1
    for old_n in range(103, 0, -1):
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

    # Step 4: Update header description to 104 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 '플라즈마 소멸 메커니즘: 전자 손실과 벽면 재결합의 실체(Q01)'가 위치하며, 총 104개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Plasma Loss topic!")
