# -*- coding: utf-8 -*-
"""
insert_memory_system_role_q01.py
사용자 질문:
"메모리가 시스템에서 어떤 역할을 하는지 설명해라"

대시보드 최상단 Q01로 신규 추가하고, 기존 91개 질문을 Q02~Q92로 시프트 (총 92개 질문 백과사전).
"""

import sys
import re

NEW_TOPIC = {
    "id": "q-01",
    "num": "01",
    "badge": "⭐ 최신 질문 (컴퓨터 구조 & 시스템 아키텍처 · 메모리의 시스템적 역할과 계층 구조)",
    "title": "메모리가 시스템에서 어떤 역할을 하는가? (폰 노이만 구조, 계층 구조, 메모리 월, HBM)",
    "nav_title": "메모리가 시스템에서 하는 역할과 계층 구조",
    "summary": [
        "<strong>1. 폰 노이만 구조의 실행 무대 (프로그램 내장 방식)</strong>: CPU가 '두뇌(작업자)'라면 메모리는 '작업대(책상)와 창고'입니다. 컴퓨터의 모든 명령어(Code)와 데이터는 실행되기 위해 반드시 메모리에 적재(Load)되어야 하며, 프로세스의 상태와 컨텍스트를 실시간으로 지탱하는 실행의 절대적 무대입니다.",
        "<strong>2. 속도-용량-비용 격차를 해소하는 메모리 계층 구조(Memory Hierarchy)</strong>: 초고속 CPU(GHz, 서브 나노초)와 저속 보조기억장치(SSD/HDD, 마이크로~밀리초) 사이의 10만 배 속도 격차를 완충하기 위해 `레지스터 ➔ SRAM 캐시(L1~L3) ➔ 메인 메모리(DRAM/HBM) ➔ 스토리지(NAND SSD)`로 이어지는 피라미드 계층을 형성하여 비용 대비 성능을 극대화합니다.",
        "<strong>3. 시스템 안정성과 자원 추상화 (가상 메모리 Virtual Memory)</strong>: 물리적 DRAM 용량의 한계를 극복하고 멀티태스킹 환경에서 프로그램들이 서로의 영역을 침범하지 못하도록 독립된 가상 주소 공간(Paging)을 제공하고 메모리 보호(Protection)를 수행합니다.",
        "<strong>4. AI 시대의 패러다임 전환과 메모리 월(Memory Wall)</strong>: 프로세서 연산 속도가 메모리 대역폭보다 수십 배 빠르게 발전하면서 데이터 병목(Memory Wall)이 발생했습니다. 이를 극복하기 위해 수천 개 TSV로 초광대역을 공급하는 <strong>HBM(High Bandwidth Memory)</strong>과 메모리 내부에서 직접 연산하는 <strong>PIM(Processing-In-Memory)</strong>으로 메모리의 역할이 '단순 저장소'에서 '컴퓨팅의 핵심 동반자'로 진화하고 있습니다."
    ],
    "svg_title": "📊 [메모리의 시스템적 역할 종합 다이어그램] (A) 폰 노이만 구조와 데이터 흐름 | (B) 메모리 계층 구조(Hierarchy) 피라미드 | (C) AI 시대 메모리 월과 HBM 혁신",
    "svg": r"""<svg viewBox="0 0 980 460" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
  <rect width="980" height="460" rx="12" fill="#0b1120" stroke="#1e293b" stroke-width="1.5"/>

  <!-- PANEL A: Von Neumann Architecture & Memory Role -->
  <g transform="translate(20, 20)">
    <rect width="300" height="420" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
    <text x="16" y="26" fill="#38bdf8" font-size="12" font-weight="800">■ (A) 폰 노이만 구조와 메모리의 역할</text>

    <!-- Architecture Diagram -->
    <g transform="translate(15, 42)">
      <rect width="270" height="235" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="18" fill="#fde047" font-size="8.8" font-weight="800">1. 컴퓨터 3대 핵심 블록의 협업</text>

      <!-- CPU Box -->
      <rect x="15" y="32" width="105" height="75" rx="4" fill="#0284c7" opacity="0.3" stroke="#38bdf8"/>
      <text x="35" y="50" fill="#38bdf8" font-size="9" font-weight="900">CPU / GPU</text>
      <text x="25" y="65" fill="#cbd5e1" font-size="7">• 연산장치 (ALU)</text>
      <text x="25" y="78" fill="#cbd5e1" font-size="7">• 제어장치 (CU)</text>
      <text x="25" y="91" fill="#fde047" font-size="7.2" font-weight="800">[두뇌 / 작업자]</text>

      <!-- Main Memory Box -->
      <rect x="150" y="32" width="105" height="75" rx="4" fill="#10b981" opacity="0.3" stroke="#10b981"/>
      <text x="165" y="50" fill="#34d399" font-size="9" font-weight="900">주기억장치 (DRAM)</text>
      <text x="160" y="65" fill="#cbd5e1" font-size="7">• 프로그램 코드 적재</text>
      <text x="160" y="78" fill="#cbd5e1" font-size="7">• 활성 데이터 버퍼</text>
      <text x="160" y="91" fill="#fde047" font-size="7.2" font-weight="800">[작업대 / 책상]</text>

      <!-- Bidirectional Bus -->
      <path d="M 120 62 L 150 62" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrowYellow)"/>
      <path d="M 150 75 L 120 75" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrowYellow)"/>
      <text x="112" y="55" fill="#fbbf24" font-size="6.8" font-weight="800">시스템 버스</text>

      <!-- Storage Box below -->
      <rect x="15" y="125" width="240" height="45" rx="4" fill="#6366f1" opacity="0.25" stroke="#818cf8"/>
      <text x="25" y="142" fill="#a5b4fc" font-size="8.5" font-weight="800">보조기억장치 (NAND Flash SSD / HDD) [대형 창고 / 서가]</text>
      <text x="25" y="157" fill="#cbd5e1" font-size="7.2">• 비휘발성 영구 보존 | 대용량 파일·OS 이미지 보관 | 수 ms 속도</text>

      <!-- Data load arrow from storage to memory -->
      <path d="M 200 125 L 200 107" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="145" y="120" fill="#38bdf8" font-size="6.8" font-weight="800">프로그램 로드(Load)</text>

      <!-- Explanation inside card -->
      <text x="12" y="188" fill="#fde047" font-size="7.8" font-weight="800">★ 왜 메모리가 필수적인가?</text>
      <text x="12" y="202" fill="#cbd5e1" font-size="7.2">• CPU는 너무 빠르고(GHz), SSD는 너무 느림(10만 배 차이!)</text>
      <text x="12" y="215" fill="#cbd5e1" font-size="7.2">• CPU가 SSD에서 직접 읽으면 99.9%의 시간을 멍하니 대기함</text>
      <text x="12" y="228" fill="#34d399" font-size="7.5" font-weight="800">➔ 중간에 고속 작업대(DRAM)를 두어 CPU 속도와 보조를 맞춤!</text>
    </g>

    <!-- Bottom summary box -->
    <rect x="15" y="295" width="270" height="112" rx="6" fill="#0b1329" stroke="#38bdf8"/>
    <text x="22" y="315" fill="#38bdf8" font-size="9" font-weight="800">💡 책상과 서가의 비유:</text>
    <text x="22" y="333" fill="#cbd5e1" font-size="7.8">• <strong>CPU</strong>: 일을 하는 사람 (두뇌)</text>
    <text x="22" y="348" fill="#34d399" font-size="7.8">• <strong>메모리(DRAM)</strong>: 지금 펼쳐놓고 일하는 <strong>'책상'</strong></text>
    <text x="22" y="364" fill="#cbd5e1" font-size="7.8">• <strong>스토리지(SSD)</strong>: 책들을 꽂아두는 저 멀리 <strong>'서가/창고'</strong></text>
    <text x="22" y="380" fill="#fde047" font-size="8" font-weight="800">➔ 책상이 넓고 빨라야 서가에 안 가고 바로바로 작업 가능!</text>
    <text x="22" y="396" fill="#a5f3fc" font-size="7.5">이 역할을 체계화한 것이 (B)의 '메모리 계층 구조'입니다.</text>
  </g>

  <!-- PANEL B: Memory Hierarchy Pyramid -->
  <g transform="translate(340, 20)">
    <rect width="310" height="420" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1.2"/>
    <text x="16" y="26" fill="#34d399" font-size="12" font-weight="800">■ (B) 메모리 계층 구조 (Memory Hierarchy)</text>

    <!-- Pyramid Graphic -->
    <g transform="translate(15, 42)">
      <rect width="280" height="235" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="12" y="16" fill="#fde047" font-size="8.8" font-weight="800">속도 vs 용량 vs 단가의 최적화 피라미드</text>

      <!-- Level 1: Registers -->
      <polygon points="140,26 100,56 180,56" fill="#ef4444" opacity="0.85"/>
      <text x="123" y="47" fill="#fff" font-size="7" font-weight="900">레지스터</text>

      <!-- Level 2: SRAM Cache -->
      <polygon points="100,58 180,58 210,95 70,95" fill="#f59e0b" opacity="0.85"/>
      <text x="110" y="78" fill="#000" font-size="7.5" font-weight="900">SRAM 캐시 (L1~L3)</text>

      <!-- Level 3: Main Memory DRAM -->
      <polygon points="70,97 210,97 240,145 40,145" fill="#10b981" opacity="0.85"/>
      <text x="100" y="122" fill="#000" font-size="8" font-weight="900">주기억장치 (DRAM / HBM)</text>

      <!-- Level 4: Storage NAND SSD -->
      <polygon points="40,147 240,147 270,200 10,200" fill="#3b82f6" opacity="0.85"/>
      <text x="92" y="176" fill="#fff" font-size="8" font-weight="900">보조기억장치 (NAND Flash SSD)</text>

      <!-- Side indicators -->
      <!-- Left side: Speed & Cost -->
      <path d="M 20 195 L 20 35" stroke="#ef4444" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="8" y="28" fill="#ef4444" font-size="6.5" font-weight="800">속도↑ 단가↑</text>

      <!-- Right side: Capacity -->
      <path d="M 260 35 L 260 195" stroke="#38bdf8" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
      <text x="245" y="208" fill="#38bdf8" font-size="6.5" font-weight="800">용량↑ (TB)</text>

      <!-- Latency numbers -->
      <text x="185" y="45" fill="#fca5a5" font-size="6.5">&lt; 1 ns (ps급)</text>
      <text x="215" y="80" fill="#fde047" font-size="6.5">1 ~ 10 ns</text>
      <text x="238" y="125" fill="#a7f3d0" font-size="6.5">50 ~ 100 ns</text>
      <text x="220" y="185" fill="#93c5fd" font-size="6.5">수십 μs ~ ms</text>
    </g>

    <!-- Hierarchy Details Box -->
    <g transform="translate(15, 288)">
      <rect width="280" height="118" rx="6" fill="#0b1329" stroke="#10b981"/>
      <text x="10" y="18" fill="#34d399" font-size="8.8" font-weight="800">★ 계층 구조가 존재하는 근본 이유</text>
      <text x="10" y="34" fill="#cbd5e1" font-size="7.5">• 모든 메모리를 초고속 SRAM으로 만들면? ➔ 컴퓨터 수억 원!</text>
      <text x="10" y="48" fill="#cbd5e1" font-size="7.5">• 모든 메모리를 저렴한 SSD로 통일하면? ➔ 컴퓨터 거북이 둔갑!</text>
      <text x="10" y="64" fill="#fde047" font-size="7.8" font-weight="800">• 지역성의 원리(Locality of Reference):</text>
      <text x="18" y="78" fill="#cbd5e1" font-size="7.2">자주 쓰는 데이터 10%가 전체 실행의 90%를 차지함</text>
      <text x="18" y="92" fill="#a7f3d0" font-size="7.2">➔ 작은 초고속 캐시와 적당한 DRAM만으로 최고 가성비 실현!</text>
      <text x="10" y="108" fill="#38bdf8" font-size="7.5" font-weight="800">➔ 이것이 현대 모든 컴퓨터가 계층 구조를 채택한 비결입니다.</text>
    </g>
  </g>

  <!-- PANEL C: Modern AI Paradigm: Memory Wall & HBM -->
  <g transform="translate(670, 20)">
    <rect width="290" height="420" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="14" y="26" fill="#fbbf24" font-size="11.5" font-weight="800">■ (C) AI 시대의 병목: 메모리 월(Memory Wall)</text>

    <!-- Memory Wall Graph -->
    <g transform="translate(15, 42)">
      <rect width="260" height="175" rx="6" fill="#1e293b" stroke="#334155"/>
      <text x="10" y="16" fill="#f87171" font-size="8.8" font-weight="800">연산 속도 vs 메모리 대역폭의 격차</text>

      <!-- Axes -->
      <line x1="25" y1="120" x2="235" y2="120" stroke="#94a3b8" stroke-width="1"/>
      <line x1="25" y1="120" x2="25" y2="25" stroke="#94a3b8" stroke-width="1"/>
      <text x="215" y="132" fill="#94a3b8" font-size="6.5">연도 (Year)</text>
      <text x="15" y="22" fill="#94a3b8" font-size="6.5">성능</text>

      <!-- Processor curve (exponential, red) -->
      <path d="M 25 110 Q 120 90 230 30" stroke="#ef4444" stroke-width="2.2" fill="none"/>
      <text x="135" y="42" fill="#f87171" font-size="7.5" font-weight="800">GPU/CPU 연산 성능 (연 60%↑)</text>

      <!-- Memory bandwidth curve (slow, blue) -->
      <path d="M 25 115 Q 120 108 230 85" stroke="#38bdf8" stroke-width="2" fill="none"/>
      <text x="145" y="98" fill="#38bdf8" font-size="7.5" font-weight="800">메모리 대역폭 (연 10%↑)</text>

      <!-- Gap shading (Memory Wall) -->
      <polygon points="150,75 230,30 230,85 150,100" fill="#fbbf24" opacity="0.25"/>
      <text x="160" y="72" fill="#fde047" font-size="8" font-weight="900">메모리 월 (Memory Wall!)</text>

      <text x="10" y="142" fill="#cbd5e1" font-size="7.2">• GPU는 초당 1,000조 번 계산할 수 있는데,</text>
      <text x="10" y="154" fill="#cbd5e1" font-size="7.2">• 메모리가 데이터를 제때 못 주어 GPU가 놀고 있음!</text>
      <text x="10" y="166" fill="#fca5a5" font-size="7.5" font-weight="800">➔ 이것이 바로 '메모리 병목(Memory Bottleneck)'</text>
    </g>

    <!-- Revolutionary Solutions: HBM & PIM -->
    <g transform="translate(15, 228)">
      <rect width="260" height="178" rx="6" fill="#0b1329" stroke="#f59e0b"/>
      <text x="10" y="18" fill="#fbbf24" font-size="8.8" font-weight="800">★ 메모리의 패러다임 전환: HBM과 PIM</text>

      <text x="10" y="36" fill="#34d399" font-size="8" font-weight="800">1. HBM (고대역폭 메모리):</text>
      <text x="18" y="50" fill="#cbd5e1" font-size="7.2">• DRAM 8~16단을 수직 TSV로 관통 적층</text>
      <text x="18" y="62" fill="#cbd5e1" font-size="7.2">• 1024~2048개 버스선으로 대역폭 1.2~3.3 TB/s 폭포수</text>
      <text x="18" y="74" fill="#a7f3d0" font-size="7.2">➔ AI 가속기(NVIDIA H100/B200)의 필수 심장!</text>

      <text x="10" y="94" fill="#38bdf8" font-size="8" font-weight="800">2. PIM (Processing-In-Memory):</text>
      <text x="18" y="108" fill="#cbd5e1" font-size="7.2">• 데이터를 CPU로 보낼 필요 없이 메모리 내부에서 직접 연산!</text>
      <text x="18" y="120" fill="#cbd5e1" font-size="7.2">• 데이터 이동 전력 소모 80% 절감</text>

      <rect x="8" y="132" width="244" height="36" rx="3" fill="#1e293b" stroke="#10b981"/>
      <text x="14" y="148" fill="#34d399" font-size="7.8" font-weight="800">🚀 미래 메모리의 역할 재정의:</text>
      <text x="14" y="160" fill="#cbd5e1" font-size="7.2">'단순 데이터 저장소' ➔ '컴퓨팅의 핵심 동반자'로 도약!</text>
    </g>
  </g>

  <!-- Arrow marker definition -->
  <defs>
    <marker id="arrowYellow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#f59e0b" />
    </marker>
    <marker id="arrowBlue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#38bdf8" />
    </marker>
    <marker id="arrowRed" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="#ef4444" />
    </marker>
  </defs>
</svg>""",
    "lecture": r"""
        <!-- Section 1: Core Role in Von Neumann Architecture -->
        <div style="margin-top:24px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#38bdf8; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            1. 폰 노이만 컴퓨터 구조에서 메모리의 본질적 역할: "실행의 무대"
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            현대 모든 컴퓨터의 기반인 <strong>폰 노이만 아키텍처(Von Neumann Architecture)</strong>의 핵심은 <strong>'프로그램 내장 방식(Stored-Program Concept)'</strong>입니다.
            즉, 연산 장치(CPU/GPU)가 작동하려면 실행해야 할 명령어(코드)와 데이터가 반드시 **메모리에 미리 적재(Load)**되어 있어야만 합니다.
          </p>

          <div style="background:#0f172a; border-left:4px solid #38bdf8; padding:16px 20px; border-radius:0 8px 8px 0; margin-bottom:18px;">
            <h4 style="color:#38bdf8; font-size:1.05rem; font-weight:800; margin-bottom:8px;">🏢 시스템 3대 요소의 완벽한 일상 비유</h4>
            <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:18px;">
              <li><strong>CPU (두뇌 / 작업자)</strong>: 손과 머리가 엄청나게 빨라 1초에 수십억 번의 계산을 해치우는 천재 작업자입니다.</li>
              <li><strong>메모리 DRAM (작업대 / 책상)</strong>: 작업자가 지금 당장 손을 뻗어 읽고 쓸 수 있도록 문서와 도구를 펼쳐놓은 **넓고 빠른 책상**입니다.</li>
              <li><strong>스토리지 SSD/HDD (창고 / 문서 보관소)</strong>: 전원이 꺼져도 책을 영구 보존하지만, 저 멀리 지하에 있어 가지러 갔다 오는 데 한참 걸리는 **대형 창고**입니다.</li>
            </ul>
          </div>
          <p style="font-size:0.92rem; line-height:1.7; color:#cbd5e1;">
            만약 메모리가 없다면, 초고속 CPU는 데이터를 가져오기 위해 매번 저 먼 지하 창고(SSD)까지 왕복해야 하므로 **99.99%의 시간을 멍하니 기다리는 데 낭비**하게 됩니다. 
            따라서 메모리는 **초고속 CPU와 저속 스토리지 사이의 극심한 속도 격차를 메워주는 핵심 가교(Bridge)**입니다.
          </p>
        </div>

        <!-- Section 2: 4 Core Functions of Memory in a System -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#34d399; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            2. 시스템 관점에서 메모리가 수행하는 4대 핵심 기능
          </h3>

          <!-- Function 1 -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:14px; border-left:4px solid #38bdf8;">
            <h4 style="color:#38bdf8; font-size:1.02rem; font-weight:800; margin-bottom:6px;">
              ① 속도 버퍼링 (Speed Bridging & Decoupling)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              CPU는 나노초 이하($< 1\,\text{ns}$)의 클록 주기로 동작하지만, NAND 플래시 SSD는 마이크로초($\mu\text{s}$), HDD는 밀리초($\text{ms}$) 단위로 동작합니다.
              메모리(DRAM)는 수십 나노초($50\sim 80\,\text{ns}$) 수준의 고속으로 CPU의 연산 요청에 즉각 응답하여 **프로세서가 쉬지 않고 최고 속도로 풀가동되도록 완충**합니다.
            </p>
          </div>

          <!-- Function 2 -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:14px; border-left:4px solid #facc15;">
            <h4 style="color:#facc15; font-size:1.02rem; font-weight:800; margin-bottom:6px;">
              ② 프로세스 실행 공간 및 컨텍스트 보존 (Execution Workspace)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              운영체제(OS) 커널, 실행 중인 애플리케이션의 **코드 영역(Code), 전역 변수(Data), 동적 할당 공간(Heap), 함수 호출 및 지역 변수(Stack)** 등 프로세스의 모든 상태와 문맥(Context)이 실시간으로 살아 숨 쉬는 유일한 물리적 공간입니다.
            </p>
          </div>

          <!-- Function 3 -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:14px; border-left:4px solid #10b981;">
            <h4 style="color:#10b981; font-size:1.02rem; font-weight:800; margin-bottom:6px;">
              ③ 가상 메모리(Virtual Memory)를 통한 자원 보호 및 추상화
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              실제 물리 DRAM 용량이 16GB에 불과하더라도, 메모리 관리 장치(MMU)와 페이징(Paging) 기법을 통해 각 프로그램에 4GB 이상의 독립된 가상 주소 공간을 부여합니다.
              이를 통해 **프로그램끼리 서로의 메모리를 침범해 다운되는 것을 완벽히 방지(Memory Protection)**하고, 멀티태스킹의 안정성을 담보합니다.
            </p>
          </div>

          <!-- Function 4 -->
          <div style="background:#1e293b; border-radius:8px; padding:16px 20px; margin-bottom:14px; border-left:4px solid #ef4444;">
            <h4 style="color:#f87171; font-size:1.02rem; font-weight:800; margin-bottom:6px;">
              ④ 데이터 영속성(Persistence)과 비휘발성 보관 (Storage)
            </h4>
            <p style="color:#cbd5e1; font-size:0.9rem; line-height:1.7;">
              DRAM이 전원이 켜져 있을 때의 활성 작업대 역할을 한다면, 비휘발성 메모리(NAND Flash)는 컴퓨터가 꺼져도 사용자의 소중한 파일, 데이터베이스, 사진, OS 이미지를 10년 이상 안전하게 영구 보존하는 금고 역할을 수행합니다.
            </p>
          </div>
        </div>

        <!-- Section 3: Memory Hierarchy -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#fbbf24; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            3. 메모리 계층 구조(Memory Hierarchy): 최적의 비용 대비 성능
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            컴퓨터는 단 하나의 만능 메모리를 쓸 수 없습니다. <strong>빠른 메모리는 비싸고 면적을 많이 차지하며, 싼 메모리는 느리기 때문</strong>입니다. 
            이를 해결하기 위해 인류는 피라미드 형태의 계층 구조를 구축했습니다.
          </p>

          <div style="overflow-x:auto; margin-bottom:16px;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#0f172a; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1e293b; color:#38bdf8; text-align:left;">
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">계층</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">소재 및 소자</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">지연 시간 (Latency)</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">대표 용량</th>
                  <th style="padding:10px 14px; border-bottom:2px solid #334155;">주요 시스템 역할</th>
                </tr>
              </thead>
              <tbody style="color:#cbd5e1; line-height:1.6;">
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#ef4444;">1. 레지스터 (Register)</td>
                  <td style="padding:10px 14px;">플립플롭 (Flip-Flop)</td>
                  <td style="padding:10px 14px; font-weight:800; color:#ef4444;">&lt; 0.5 ns (1 사이클)</td>
                  <td style="padding:10px 14px;">수 KB</td>
                  <td style="padding:10px 14px;">CPU 내부 ALU 직속 피연산자 보관</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#f59e0b;">2. 캐시 메모리 (SRAM)</td>
                  <td style="padding:10px 14px;">6T-SRAM</td>
                  <td style="padding:10px 14px; font-weight:800; color:#f59e0b;">1 ~ 10 ns (L1~L3)</td>
                  <td style="padding:10px 14px;">수 MB ~ 수십 MB</td>
                  <td style="padding:10px 14px;">자주 쓰는 데이터 임시 보관 (캐싱)</td>
                </tr>
                <tr style="border-bottom:1px solid #1e293b;">
                  <td style="padding:10px 14px; font-weight:700; color:#10b981;">3. 메인 메모리 (DRAM)</td>
                  <td style="padding:10px 14px;">1T-1C DRAM / HBM</td>
                  <td style="padding:10px 14px; font-weight:800; color:#10b981;">50 ~ 100 ns</td>
                  <td style="padding:10px 14px;">16GB ~ 수 TB</td>
                  <td style="padding:10px 14px;">OS 및 실행 프로그램의 메인 작업대</td>
                </tr>
                <tr>
                  <td style="padding:10px 14px; font-weight:700; color:#3b82f6;">4. 보조기억장치 (SSD)</td>
                  <td style="padding:10px 14px;">3D NAND Flash</td>
                  <td style="padding:10px 14px; font-weight:800; color:#3b82f6;">10 ~ 100 μs</td>
                  <td style="padding:10px 14px;">수 TB ~ 수십 TB</td>
                  <td style="padding:10px 14px;">비휘발성 대용량 영구 저장 창고</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Section 4: Modern AI Paradigm and Memory Wall -->
        <div style="margin-top:28px;">
          <h3 style="font-size:1.25rem; font-weight:800; color:#ef4444; margin-bottom:12px; border-bottom:1px solid #334155; padding-bottom:8px;">
            4. AI 시대의 혁명: 메모리 월(Memory Wall)과 HBM / PIM
          </h3>
          <p style="font-size:0.95rem; line-height:1.75; color:#e2e8f0; margin-bottom:12px;">
            최근 생성형 AI(ChatGPT 등)와 LLM의 등장으로 메모리의 위상은 완전히 달라졌습니다.
          </p>
          <div style="background:#0f172a; border-left:4px solid #f59e0b; padding:16px 20px; border-radius:0 8px 8px 0;">
            <ul style="color:#cbd5e1; font-size:0.92rem; line-height:1.8; padding-left:18px;">
              <li><strong>메모리 월(Memory Wall) 병목</strong>: GPU의 연산 속도는 매년 수십%씩 폭증하는데, 기존 메모리가 데이터를 실어나르는 대역폭(Bandwidth)은 그 속도를 따라가지 못해 최첨단 GPU가 데이터를 기다리며 멍하니 노는 병목이 발생했습니다.</li>
              <li><strong>HBM(High Bandwidth Memory)의 구원</strong>: DRAM 칩을 8~16단으로 얇게 깎아 수천 개의 TSV 관통전극으로 수직 연결하여 **초당 1~3.3 TB의 쓰나미 같은 데이터 대역폭**을 공급함으로써 AI 연산의 심장으로 등극했습니다.</li>
              <li><strong>PIM(Processing-In-Memory)의 미래</strong>: 메모리가 단순히 데이터를 저장하는 수동적 창고를 넘어, **메모리 내부에서 직접 덧셈과 곱셈 연산을 수행**하여 데이터 이동 전력을 80% 줄이는 미래 컴퓨팅의 혁신을 이끌고 있습니다.</li>
            </ul>
          </div>
        </div>
    """
}

def update_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Step 1: Shift existing 91 topics (q-91 down to q-01) by +1 (q-XX -> q-(XX+1))
    for old_n in range(91, 0, -1):
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

    # Step 4: Update header description to 92 questions
    html = re.sub(
        r"최상단에는 '.*?'이 위치하며, 총 \d+개 질문으로 구성되어 있습니다\.",
        r"최상단에는 '메모리가 시스템에서 하는 역할과 계층 구조'이 위치하며, 총 92개 질문으로 구성되어 있습니다.",
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully updated {file_path}")

if __name__ == "__main__":
    update_file(r"C:\Work\반도체3\result\261007_v1.0\index.html")
    update_file(r"C:\Work\반도체3\index.html")
    print("Done adding Q01 Memory System Role topic!")
