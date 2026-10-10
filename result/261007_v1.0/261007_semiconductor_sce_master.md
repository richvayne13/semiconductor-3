# [보고서] 반도체 소자 물리 & 단채널 효과(SCE) Q&A 백과사전 (사용자 질문 탭 순)

- **작성일자**: 2026년 10월 9일
- **저장경로**: `C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md`
- **배포 대시보드**: [C:\Work\반도체3\index.html](file:///C:/Work/반도체3/index.html)
- **온라인 라이브 서비스**: [https://richvayne13.github.io/semiconductor-3/](https://richvayne13.github.io/semiconductor-3/)

---

## 1. 개요 및 목적
본 보고서와 대시보드는 **사용자께서 직접 질문하신 문장 그대로 좌측 내비게이션 탭의 제목으로 구성**하고, **가장 최근에 질문하신 순서(역순/최신순)로 1번부터 77번까지 배치**하여 맞춤형 학습 및 면접 대비가 가능하도록 구축되었습니다.

각 질문 섹션은 항상 **[💡 면접 대비 3~4줄 핵심 요약]**이 선행되고, 이어지는 **[📘 세부 마스터 강의 노트]**에서 심층 물리 수식과 직관적인 고품질 SVG 시각 다이어그램을 다룹니다.

---

## 2. 사용자 질문 기반 목차 (최신순 91대 Q&A)

| 순번 | 좌측 탭 제목 (사용자 실제 질문) | 주요 핵심 키워드 |
| :---: | :--- | :--- |
| **Q 01** | **유전율은 전하를 품는 능력인데, 왜 이게 높아야 좋을까? (게이트 장악력, 터널링 차단, DRAM 축소)** ⭐ [최신 1번] | "무조건 높아야 좋은 것은 아니다!" (배선 IMD는 Low-k 필수 vs 게이트/DRAM은 High-k 필수), High-k가 필수적인 3대 이유: ① 게이트 채널 지배력($C_{ox}$) 극대화로 낮은 $V_{GS}$에서도 막대한 구동 전류($I_{on}$) 유치 및 DIBL 차단, ② 두께와 정전용량의 분리(디커플링): 물리적 두께($t_{phys}$)를 $3.5\text{nm}$로 두껍게 세워 양자 터널링 누설전류를 차단하면서도 전기적 $EOT$를 $0.55\text{nm}$로 축소하는 마법, ③ 초미세 DRAM 1T-1C 셀에서 좁쌀만 한 바닥 면적에도 데이터 유실을 막는 최소 $25\,\text{fF}$ 전하 보존 |
| **Q 02** | **유전율(Permittivity, ε)이란 무엇인가? 유전율이 높다는 것의 물리적 의미와 반도체 응용** | '전기(電)를 유도(誘)하여 품는 정도', 외부 전기장 하에서 전기적 분극(Polarization, $P$)을 일으켜 전기 에너지를 저장하고 외부 전계를 완화(스크리닝)하는 능력, 유전율이 높다는 것의 3대 본질: ① 분극력 극대화(전기적 스펀지/에어백), ② 전하 저장 용량($C = \epsilon A/d$) 비례 폭증, ③ 쿨롱 힘($F \propto 1/\epsilon$) 약화(전하 간 상호작용 차폐), 반도체 FEOL의 High-k($\text{HfO}_2$, EOT 1nm 이하 축소로 $C_{ox} \uparrow$ 및 터널링 차단) vs BEOL의 Low-k($\text{SiCOH}$, RC 지연 및 누화 노이즈 차단) 양대 전략 비교 |
| **Q 03** | **MOS Cap의 동작 특성 완전 정복 (축적·평탄대·공핍·반전 4대 영역, 에너지 밴드, C-V 거동)** | 표면 전위($\psi_s$)에 따른 4대 동작 영역: ① 축적($\psi_s < 0$, 정공 결집, $C=C_{ox}$), ② 평탄대($\psi_s=0$, 밴드 휨 제로, $C_{FB}$), ③ 공핍($0<\psi_s<2\phi_B$, 정공 퇴출 및 공핍층 확장으로 $C$ 지속 하강), ④ 반전($\psi_s \ge 2\phi_B$, 전자 반전층 형성, $W_{dep,max}$ 고정), 반전 영역 C-V 3대 주파수 분기: 저주파(LF, $C_{ox}$ 복원) vs 고주파(HF, $C_{min}$ 정체) vs 깊은 공핍(Deep Depletion, $C$ 급락), 실무 C-V 진단 파라미터($t_{ox}, V_{FB}, Q_f, N_A, D_{it}$) 추출 원리 해부 |
| **Q 04** | **MOS Cap(모스 커패시터)과 MOSFET의 본질적 차이 (구조, 반전층 공급원, C-V 거동 비교)** | 2단자 수동 정전용량 소자(수평 직류 전류 $I_{DS}=0$) vs 4단자 능동 스위치/증폭기(게이트 전압으로 $I_{DS}$ On/Off 제어), 반전층 캐리어 공급원의 결정적 차이: 열 생성(Thermal EHP Generation, $\tau \sim \text{ms}$)에 의존하는 MOS Cap vs 소스/드레인($N^+$) 전자 저수지에서 피코초($\text{ps}$) 단위로 즉각 공급하는 MOSFET, C-V 특성 곡선 고주파(HF) 반전층 분기: 소수캐리어가 못 따라와 $C_{min}$에 정체되는 MOS Cap vs S/D 직접 공급으로 $C_{ox}$로 100% 완전 회복하는 MOSFET, FAB 공정 진단($t_{ox}, V_{FB}, D_{it}, N_A$ 역산) vs 고성능 CMOS 로직 컴퓨팅 응용 비교 |
| **Q 05** | **PD-SOI에서 채널 아래 쌓인 정공(양전하)은 왜 Vt를 낮출까? (바디 전위 상승과 장벽 붕괴 로직)** | 드레인 핀치오프 강전계 충격 이온화(Impact Ionization)로 생성된 정공($h^+$)들이 BOX 절연벽과 접합 장벽에 갇혀 중성 바디에 누적(플로팅 바디 효과), 바디 전위 양(+)으로 부유 상승($V_{BS} > 0$), Vt 하강 3대 로직: ① 바디 효과 공식 역전($V_{th} = V_{th0} + \gamma [\sqrt{2\phi_F - V_{BS}} - \sqrt{2\phi_F}]$, 순방향 바디 바이어스로 루트 항 축소), ② 소스-채널 전위 장벽 강하(Potential Barrier Lowering, 전자 주입 용이), ③ 게이트가 치워야 할 공간 공핍 전하($|Q_{dep}| = \sqrt{2\epsilon q N_A (2\phi_F - V_B)}$) 축소로 산화막 전압 강하($V_{ox}$) 절감, 치명적 킹크 효과(Kink Effect)와 $I_D$ 급증 및 이력 현상(Hysteresis), 중성 바디를 원천 소멸시킨 5~7nm 극박막 FD-SOI로의 진화 |
| **Q 06** | **공유 영역을 제외해 공핍층이 작아져서 Depletion Cap이 커진 건가? (질문자 직관 검증)** | 질문자님의 물리적 직관 100% 완벽 검증, 소스/드레인이 가로채어 sharing하는 양쪽 귀퉁이 공핍 영역을 제외하면 게이트 순수 전하가 사다리꼴로 축소, $L$ 기준 평균 환산 실효 공핍 깊이 $W_{dep,eff}$가 얕아짐(Thinning), 평행판 공식($C = \epsilon/d$)에서 두께($d = W_{dep,eff}$) 감소로 $C_{dep,eff}$ 상승 메커니즘, 핵심 구분: '총 전하량($Q_{B,eff}$)'은 사다리꼴 축소로 감소($V_{th}$ 롤오프) vs '단위 면적당 커패시턴스($C_{dep,eff}$)'는 실효 두께 축소로 증가($SS$ 악화), 현실에서 $C_{dep}$가 커지는 또 다른 핵심 요인(펀치스루 억제용 고농도 Halo 도핑 $W_{dep} \propto 1/\sqrt{N_A}$에 의한 물리적 두께 압축)과의 2대 시너지, 3차원 FinFET/GAA 무도핑 채널 도입 배경 |
| **Q 07** | **2차원 전하 분할(Charge Sharing)과 실효 두께 축소(Thinning) 상세** | 야우(Yau)의 사다리꼴 전하 분할 기하 모델, S/D 4분원 접합 침범으로 게이트 유효 전하 $Q_{B,eff} = Q_{B,1D}(1 - \Delta L/2L)$ 축소, 게이트 면적($W \times L$) 기준 평균 환산 두께 $W_{dep,eff} = W_{dep}(1 - \Delta L/2L)$ 얇아짐(Thinning)의 수학적 유도, 분모 감소로 유효 $C_{dep,eff} = \frac{\epsilon}{W_{dep,eff}}$ 가파른 상승 및 $SS = 60(1 + C_{dep,eff}/C_{ox})$ 악화 메커니즘 |
| **Q 08** | **Body가 얇아지면 왜 Cdep가 작아질까? (C=dQ/dV 본질, BOX 직렬)** | 평행판 공식($C = \epsilon/d$) 오해 해소, 커패시턴스의 물리적 정의($C = dQ/d\psi$), 얇은 바디에서 100% 완전 공핍화 시 공핍 전하량 한계 고정($Q_{dep} = qN_A T_{body}$)으로 전하 변조 소멸($dQ/d\psi \approx 0$), 두껍고 저유전율인 매립 산화막(BOX)과의 직렬 연결($1/C_{eff} = T_{si}/\epsilon_{si} + t_{BOX}/\epsilon_{ox}$)로 등가 용량 급감, 무도핑 채널($N_A \approx 0$) 실현으로 $C_{dep} \approx 0$ 및 $SS \approx 60\,\text{mV/dec}$ 복원 |
| **Q 09** | **공핍 커패시턴스의 구성 (S/D 접합Cap 외에 채널, 측벽, 폴리 공핍)** | MOSFET 내부 공핍 커패시턴스 3대 영역 해부: ① 게이트 직하부 채널 표면 공핍층($C_{dep,ch}$, $C_{ox}$와 직렬 연결되어 $SS$ 및 $V_{th}$ 결정), ② 소스/드레인 접합 공핍층($C_j$, 바닥면 $C_{j,bot}$과 측벽면 $C_{j,sw}$의 병렬 접지 부하, RC 딜레이 지배), ③ 폴리실리콘 게이트 내부 공핍층($C_{poly}$, EOT 손실의 원인), 반도체 업계의 공핍Cap 박멸 기술(SOI, FinFET/GAA 무도핑 채널, HKMG 금속 게이트) |
| **Q 10** | **SOI에서 부분공핍(PD)과 완전공핍(FD)이 뜻하는 것은? (원리, FBE, Kink)** | 실리콘 박막 두께($T_{si}$)와 최대 공핍층 폭($W_{dep,max}$)의 비교 기준, PD-SOI($T_{si} > W_{dep}$)의 하부 중성 영역(Neutral Body) 잔류 및 정공 축적으로 인한 플로팅 바디 효과(FBE)와 킹크(Kink) 왜곡, FD-SOI($T_{si} < W_{dep}$, 5~7nm)의 바디 100% 완전 공핍화로 FBE 원천 박멸, $C_{dep} \approx 0$화로 $SS \approx 60\,\text{mV/dec}$ 복원, 무도핑 채널(Undoped) 실현 및 백 바이어스(Back Bias) 동적 튜닝 혁신 |
| **Q 11** | **SOI로 없애는 기생Cap은 접합Cap(Cj)일까 공핍Cap(Cdep)일까?** | 'Body와 S/D 분리' 문맥의 구조적 대상은 소스/드레인 접합 커패시턴스($C_j$), 그러나 $C_j$의 물리적 작동 메커니즘 자체가 P-N 접합 공핍 영역의 $C_{dep,pn}$임 (이름=Cj, 물리실체=Cdep), S/D 바닥이 BOX 산화막에 닿아 P-N 접합면 자체를 물리적으로 소멸시켜 기생 용량 90% 제거(속도 20~30% 향상), 게이트 아래 채널 $C_{dep,ch}$(SS 인자)와의 명확한 구분 및 FD-SOI의 2중 제거 혜택 |
| **Q 12** | **Body Thickness(바디 두께)가 얇아져야 하는 이유 (스케일 길이, 누설 차단)** | 스케일 길이 공식($\lambda = \sqrt{\frac{\epsilon_{si}}{2\epsilon_{ox}} t_{ox} T_{body}}$)에서 $t_{ox}$ 터널링 한계 봉착 시 $L \ge 3\lambda$ 만족을 위한 유일한 $T_{body}$ 축소 필연성, 벌크 게이트 사각지대 지하 펀치스루 누설 경로의 기하학적 원천 박멸, 완전 공핍화(FD)로 $C_{dep} \approx 0$ 및 $SS \approx 60\,\text{mV/dec}$ 이상치 복원, 무도핑 채널(Undoped) 실현으로 쿨롱 산란 제거($\mu \uparrow$) 및 무작위 도펀트 요동(RDF) 편차 0% 박멸 |
| **Q 13** | **채널이 짧아지면 공핍 커패시턴스가 왜 올라갈까? (Cdep 증가 원리)** | 펀치스루 억제용 고농도 도핑($N_A \uparrow$, Halo) ➔ $W_{dep} \propto 1/\sqrt{N_A}$ 축소로 $C_{dep} \propto \sqrt{N_A}$ 직접 상승, 2차원 전하 분할(Charge Sharing)로 실효 두께($W_{dep,eff}$) 왜곡 축소 및 유효 $C_{dep}$ 상승, $SS = 60(1 + C_{dep}/C_{ox})$ 악화 및 $I_{off}$ 누설전류 폭발, FinFET/GAA 무도핑 채널 도입 배경 |
| **Q 14** | **IMD 정의, 스페이서 피치분할(SADP), HBM TIM 미세공기 충진** | IMD(Inter-Metal Dielectric) vs ILD(M1과 소자 분리) 및 Low-k(SiCOH) RC 딜레이 개선, SADP(자가정렬 스페이서 피치 분할) 5단계(Mandrel ➔ ALD 스페이서 ➔ 에치백 ➔ 코어 스트립 ➔ 피치 1/2 분할) 및 오버레이 에러 제로, HBM 16단 패키지 상단 TIM1 위치 및 계면 미세 요철(Micro-roughness) 사이 단열 공기($k=0.026$) 100% 배출 충진(Air Displacement)으로 접촉 열저항($R_{th}$) 극소화 |
| **Q 15** | **하이브리드 본딩의 원리 (동일평면 연마, SiO2결합, Cu열팽창)** | CMP 초평탄화 및 의도적 Cu 디싱(2~5nm), 상온 친수성 SiO₂ 수소결합 ➔ Si-O-Si 공유결합, Cu 열팽창계수(CTE 17 vs 0.5) 30배 차이로 틈새 채움, 고온 Cu-Cu 고상 원자확산 및 단일 결정립 성장(Grain Growth), 무범프 3D 패키징 |
| **Q 16** | **완만한 도핑의 Cj 감소 원리와 PAI(사전 비정질화) 기술**  | 경사 접합($\rho = qax$) 전하 중성으로 $W_{dep} \propto a^{-1/3}$ 확장 및 $C_j \downarrow$, PAI(Pre-Amorphization Implantation) 무거운 Ge 사전 주입으로 표면 비정질화(a-Si), 붕소(B) 채널링 원천 차단, SPER 고상 에피 재결정화, USJ 초얕은 접합 |
| **Q 17** | **이온화 불순물 산란이란 무엇인가? (쿨롱 편향과 이동도 저하)**  | 고정 전하 이온($P^+, B^-$) 쿨롱 인력/척력 궤적 굴절, 브룩스-헤링 공식($\mu_{ii} \propto T^{3/2}/N_I$), $\sigma = qN\mu$에서 $N$ 증가 시 $\mu$ 급락으로 저항 감소율 둔화(어빈 곡선 포화), 살리사이드(Salicide) 필수성 |
| **Q 18** | **언더컷(Undercut)이란 무엇인가? (원리, 문제점, GAA 응용)**  | 마스크 하부 수평 침식 식각, 등방성 식각($R_L > 0$), CD 선폭 손실 및 패턴 붕괴(Collapse), RIE 및 측벽 보호막(Passivation) 방어, 3nm GAA 나노시트 선택적 SiGe 수평 식각(이너 스페이서 형성) |
| **Q 19** | **면저항의 도핑농도와 캐리어밀도는 P기판과 정공(p)을 뜻할까?**  | P기판 잴 때는 붕소(NA)와 정공(p) 100% 일치, N형(NMOS S/D 등) 잴 때는 비소/인(ND)과 전자(n), 보편 공식 $\sigma = q(n\mu_n + p\mu_p)$, 완전 이온화($p \approx N_A, n \approx N_D$), 영역별 측정 실무 |
| **Q 20** | **P- 에피층 저농도 도핑으로 Cj 낮추는 메커니즘 (Wdep 반비례)**  | 질문 알고리즘 100% 일치 ($N_A \downarrow \implies W_{dep} \uparrow \implies C_j \downarrow$), 전하 중성 조건($Q^+=Q^-$), 평행판 커패시터 모델($C_j = \epsilon_s/W_{dep}$), RC 지연 단축, P/P+ 에피 웨이퍼(상부 속도 + 하부 래치업 방어) |
| **Q 21** | **네킹공정을 통해 열충격 전위를 밖으로 배출시키는 원리 (사선 소멸)**  | Dash Necking, {111} 슬립면 54.7° 사선 전파, 2~3mm 직경 극소화로 자유 표면(Free Surface) 충돌 및 소멸, 1420℃ 열충격 극복, 무전위 단결정 잉곳, 윌리엄 대시 |
| **Q 22** | **MR-MUF에서 EMC는 원래 NCF에서 뭐였고 뭘 대체한 거야?**  | NCF(고체 비전도성 필름) 완전 대체, 2중 공정(NCF 언더필+외벽 일반 EMC)을 단일 액상 EMC로 통합(Molded Underfill), 고밀도 세라믹 필러(열전도도 2.5배 향상), 방열 더미 범프 수직 고속도로, HBM3E 열 관리 |
| **Q 23** | **USJ가 줄이는 기생 커패시턴스는 Cj인가 Cdep인가? (접합 vs 공핍 구분)**  | S/D 측면 접합($C_{j,sw} \propto X_j$) 및 오버랩($C_{ov}$) 100% 직접 감소, 채널 공핍 커패시턴스($C_{dep}=\epsilon_{si}/W_{dep,ch}$)는 불변, 전하 분할(Charge Sharing 침범) 원천 차단 vs FD-SOI의 동시 절감 비교 |
| **Q 24** | **TIM은 열폭주를 줄이는 핵심 소재인데 뭐의 줄인말이야?**  | Thermal Interface Material(열 계면 재료), 미세 표면 거칠기(공기 단열벽 $k=0.026$ 제거), 접촉 열저항($R_{th}$) 극소화, 계층별 TIM1(다이-IHS 인듐솔더) vs TIM2(IHS-쿨러 그리스), 차세대 700W+ AI가속기 방열 |
| **Q 25** | **HBM에서 16단 적층과 2048-bit, 대역폭, 버스선 개념 완전 정복**  | 16-High 수직 적층(30㎛ 칩 박막화+TSV 엘리베이터), 2048-bit(2048차선 고속도로), 물리적 버스선(인터포저 구리선 2048가닥), 대역폭(차선수×속도 총전송량 3.3TB/s 폭포수), GDDR(32차선 과속) 대비 압도적 저발열/초고용량 |
| **Q 26** | **공핍층 폭은 줄이는 게 좋은 거야 넓히는 게 좋은 거야?**  | 위치별 트레이드오프 (S/D 바닥: 넓혀야 $C_j \downarrow$, HCI/내압 개선 vs 채널 수평: 좁혀야 펀치스루/DIBL 방어 vs 게이트 수직: 얕아야 게이트 통제력 $\lambda$ 강화 및 $SS \approx 60\text{mV}$ 달성) |
| **Q 27** | **반도체 INTERCONNECT 고속다층배선 구조와 원리**  | 3차원 피라미드 계층(Local M1~M3 ➔ Semi-Global M4~M8 ➔ Global Top Metal), 인터커넥트 병목 $\tau=RC$, Cu 듀얼 다마신, Low-k 절연막, 후면 전력 공급망(BSPDN) |
| **Q 28** | **도핑농도를 완만하게 하면 공핍층 넓어져 Cj 감소하는 로직**  | 전하 중성 조건($Q^+=Q^-$), 경사 접합($\rho=qax$), 푸아송 유도 $W_{dep} = [12\epsilon_s (V_{bi}-V)/(qa)]^{1/3}$, 평행판 모델 $C_j = \epsilon_s A / W_{dep}$ 반비례 감소, S/D LDD RC 지연 개선 |
| **Q 29** | **채널농도를 올리면 전자이동도는 왜 떨어져?**  | 이온화 불순물 쿨롱 척력 산란($B^-$), 수직 유효 전계($\mathcal{E}_{eff} \propto \sqrt{N_A}$) 증가로 산화막-실리콘 계면 표면 거칠기 산란 폭증($\mu_{sr} \propto \mathcal{E}_{eff}^{-2}$), 마티센의 법칙, 구동 전류 $I_{on}$ 저하, FinFET/GAA 무도핑 채널 |
| **Q 30** | **공핍전하량이 채널 부근 농도에 의해 결정된다는 게 무슨 뜻이야?**  | NMOS 기판은 P형 실리콘($N_A$), 정공 퇴출 후 남겨진 고정 붕소 음이온($B^-$) 공간 전하 $Q_{dep}$, $|Q_{dep}| = \sqrt{2q\epsilon_s N_A (2\phi_B)}$, 게이트의 전하 중화 숙제, $V_{th} = V_{FB} + 2\phi_B + |Q_{dep}|/C_{ox}$ |
| **Q 31** | **면저항은 도핑농도가 커지면 캐리어밀도가 커져 감소하는 이유?**  | 완전 이온화(Complete Ionization), 캐리어 밀도 $n \approx N$, 미시적 옴의 법칙 $J = \sigma \mathcal{E}$, 전도도 $\sigma = q N \mu$, 면저항 $R_s = \frac{1}{q N \mu t}$ 반비례, 이온화 불순물 산란과 Irvin Curve, Salicide/Raised S/D |
| **Q 32** | **doping profile이 왜중요해?** | 공간적 농도 분포 $C(x)$, 접합 깊이($X_j$)와 급준도(nm/dec), Retrograde 웰(표면 이동도+지하 펀치스루 방어), 기생 $C_j$ 경사 접합, LDD 전계 피크 완화, 축퇴 도핑 오믹 터널링 |
| **Q 33** | **증착 1) APCVD, LPCVD, ALD, PECVD (화학기상증착과 원자층증착의 원리 및 특성 비교)**  | CVD 율속 단계(질량수송 vs 표면반응), LPCVD(고온 치밀), PECVD(RF 플라즈마 라디칼, 200~400℃ 저온 BEOL), ALD(자기제한반응, 1사이클 ~0.1nm, 100% Conformal) |
| **Q 34** | **증착 2) Uniformity, Uniformity, Uniformity (균일도의 절대적 중요성과 3대 차원)** | 균일도 3대 차원(WIW 300mm 에지링, WTW 챔버 APC 피드백, 3D 단차도포성 S/C), 기착확률(Sc)과 Overhang 핀치오프 보이드(Void) 방지 |
| **Q 35** | **증착 3) 박막 두께는 어떻게 계측할까? (엘립소메트리 Ellipsometry, 광학 간섭계, X선 계측)** | 분광 엘립소메트리(SE: ρ = tanΨ exp(iΔ) 비파괴 Å단위 초정밀 역산), 반사 간섭계(2nd=mλ 고속), XRF/XRR(금속막), HR-TEM(원자격자 절대표준) |
| **Q 36** | **증착 4) 열 예산 (박막 증착과 Thermal Budget: FEOL/BEOL 열화 방지 및 저온화 기술)** | ∫T dt, Fick 2법칙 D(T)∝exp(-Ea/kT), USJ 도펀트 재확산(DIBL 유발), NiSi 응집(500℃ 한계), BEOL Cu/Low-k 400℃ Hard Limit, PEALD 초저온 진화 |
| **Q 37** | **HBM 총 정리 (개념, 특징, 공정방법, 이슈, 성능 - 칩쟁이 특강)** | 대역폭(수도관) vs 레이턴시, 2.5D 인터포저, 1024-bit 버스, TC-NCF vs MR-MUF(더미범프 2배 방열), 하이브리드 본딩, 1b DRAM 코어다이 |
| **Q 38** | **산화 1) 건식/습식 산화의 차이점 (Dry vs Wet Oxidation)**  | 건식($O_2$: 치밀, 낮은 $D_{it}$, 게이트 절연막) vs 습식($H_2O$: 초고속, 부생성물 $H_2$ 다공성, 후막 마스킹), $0.44 t_{ox}$ Si 기판 침식 |
| **Q 39** | **산화 2) 열 예산 (Thermal Budget)** | $\int T(t) dt$, 고온 누적량, 도펀트 비의도적 재확산 및 USJ 붕괴 방지, 퍼니스 퇴출 ➔ RTA 스파이크 ➔ LSA(레이저 어닐링) |
| **Q 40** | **산화 3) 표면 반응속도 vs. 확산 속도 (Deal-Grove 모델)** | $x_o^2 + Ax_o = B(t+\tau)$, 초기 선형(Linear: 표면 화학 반응 속도 $k_s$ 지배) vs 후막 포물선(Parabolic: 산소 확산 계수 $D_{eff}$ 지배) |
| **Q 41** | **노광 1) 광학계 기본 수식 (Rayleigh 분해능과 초점심도)** | 레일리 식($R = k_1 \frac{\lambda}{\text{NA}}$, $\text{DOF} = k_2 \frac{\lambda}{\text{NA}^2}$), NA 증가 시 DOF 제곱 급감 트레이드오프, ArFi 액침 & EUV 파장 단축 |
| **Q 42** | **노광 2) EUV 관련 핵심 현안 (13.5nm, 반사 광학계, 펠리클, 스토캐스틱)** | 13.5nm 전물질 흡수, Mo/Si 다층 반사경(68% 한계), LPP 주석 플라즈마 광원, CNT 펠리클 내열성, 포톤 샷 노이즈(스토캐스틱 결함), High-NA |
| **Q 43** | **노광 3) 리소그래피 미세화 기법 (OPC, OAI, MPT: LELE, SADP)** | OPC(세리프 왜곡 보정), OAI(변형 조명), MPT(자가정렬 스페이서 피치 분할 SADP/SAQP, 오버레이 에러 극복) |
| **Q 44** | **식각 1) 건식/습식 식각의 차이점 (Dry vs Wet Etching)** | 습식(화학액, 등방성, 고선택비, 언더컷 ➔ 세정/Strip 전용) vs 건식(플라즈마 RIE, 비등방성 수직벽, 손상/선택비 제어 ➔ 미세 패턴) |
| **Q 45** | **식각 2) 등방성 식각 vs 비등방성 식각 (Isotropic vs Anisotropic)** | 비등방성 계수($A_f = 1 - R_L/R_V$), 수직 이온 충돌(Bombardment) + 탄화불소 측벽 보호막(Passivation Polymer) 메커니즘 |
| **Q 46** | **식각 3) 식각 공정에서 플라즈마의 역할 (라디칼 vs 이온 충돌 RIE)** | 라디칼(화학적 자발 반응, 선택비) + 이온(쉬스 전계 수직 가속 충돌, 물리 결합 파괴), Coburn-Winters 시너지(10배 고속 비등방성) |
| **Q 47** | **이온주입 1) 장비 구동 원리 (이온원, 질량분석기, 가속관, 정전 척)** | 이온원 방전, 질량 분석 자석 로렌츠 편향($r \propto \sqrt{m/q}$ 단일 동위원소 선별), 고전압 가속관(깊이 결정), 패러데이 컵 도즈량($\Phi$) 적분 |
| **Q 48** | **이온주입 2) Doping Profile의 중요성 (투영 사정거리 Rp, 피어슨 분포)** | 핵 저지능 vs 전자 저지능, 가우시안 수식 프로파일($R_p$: 평균 사정거리, $\Delta R_p$: 분산 폭, $X_j$: 접합 깊이), Pearson-IV 비대칭 꼬리 모델 |
| **Q 49** | **이온주입 3) Shallow Implantation (초얕은 접합 USJ, 채널링 억제, RTA)** | 채널링(격자 터널 관통 현상), 7° Tilt/Twist 주입, PAI(Ge/Si 선행 주입으로 표면 비정질화) ➔ 채널링 차단, 밀리초 LSA 급속 열처리 |
| **Q 50** | **이온주입 4) Dose 와 Doping 농도의 차이 및 측정법 (Dose vs Conc, SIMS)** | 도즈량($\Phi$: 단위면적당 총량 $[\text{cm}^{-2}]$, 패러데이 컵) vs 농도($C(x)$: 단위부피당 밀도 $[\text{cm}^{-3}]$, SIMS 스퍼터링 질량분석) |
| **Q 51** | **금속 1) Al, Cu, W 배선의 특성과 차이점 (비저항, 다마신, 플러그)** | Al($2.7\,\mu\Omega\cdot\text{cm}$, 식각 용이, 과거 배선), Cu($1.7\,\mu\Omega\cdot\text{cm}$, 최저 저항, 다마신 공정 필수), W($5.6\,\mu\Omega\cdot\text{cm}$, CVD 완벽 단차 도포성, 수직 콘택트 플러그) |
| **Q 52** | **금속 2) 일렉트로마이그레이션 (Electromigration, Black's Eq, Void)** | 전자 바람(Electron Wind) 운동량 충돌, 상류 보이드(Void 단선) vs 하류 힐록(Hillock 쇼트), 블랙 공식($\text{MTTF} \propto J^{-2}\exp(E_a/kT)$) |
| **Q 53** | **금속 3) Metal-Silicon Junction (쇼트키 접합 vs 오믹 접합, 실리사이드)** | 쇼트키 장벽($\Phi_B$, 정류성 다이오드) vs 터널링 오믹 콘택트(축퇴 도핑 $N > 10^{20}$, $W_{dep} < 2\,\text{nm}$ 양자 터널링), 살리사이드(NiSi) |
| **Q 54** | **패키징 1) HBM, HBM, HBM... (TSV, 2.5D 실리콘 인터포저)** | 메모리 월 병목 타파, 수천 개 TSV 관통전극 기반 8~16단 DRAM 수직 적층, 2.5D 실리콘 인터포저, 1024-bit 버스, 대역폭 $> 1.5\,\text{TB/s}$ |
| **Q 55** | **패키징 2) 패키징 열 전달 (Thermal Dissipation, TIM, 핫스팟 제어)** | 700W 초고발열, TIM(방열 페이스트/액체금속) 열 저항 극소화, HBM MR-MUF(에폭시+고열전도 필러) 갭필, 핫스팟 방열판 탈출 |
| **Q 56** | **패키징 3) Warpage (열팽창계수 CTE 불일치, 휨 현상, 박리 방지)** | 실리콘($2.6\,\text{ppm}$) vs 기판($15\,\text{ppm}$) CTE 불일치, 리플로우 냉각 시 바이메탈 휨(Smile/Frown), 솔더 오픈/쇼트 방지용 EMC 및 스티프너 링 |
| **Q 57** | **패키징 4) 하이브리드 본딩 (Hybrid Bonding, Cu-Cu 직접 접합, 범프리스)** | 범프 제로(Bumpless), 유전체($\text{SiO}_2$) 친수성 결합 + Cu-Cu 원자 확산 직접 결합, 피치 $< 1\,\mu\text{m}$, 접촉 저항 90% 절감, HBM4 16단 필수 |
| **Q 58** | **웨이퍼 제조 1) 초크랄스키 기법 (300mm 웨이퍼)** | 고순도 Si 융액(1420℃), 대시 네킹(Dash Necking: 3~5mm 무전위화), 숄더/직동(Body), MCZ(Magnetic CZ: 0.3T 전자기장으로 열대류 억제 & 산소 제어), 와이어소 절단/CMP |
| **Q 59** | **웨이퍼 제조 2) 기판 도핑 (P- / P+ / N- / N+)** | 전자의 높은 이동도($\mu_n \approx 3\mu_p$) 기반 NMOS 우선 설계 ➔ P- 기판 표준화, 래치업(Latch-up) 방지를 위한 P/P+ 에피 웨이퍼, 웰(Well) 격리 |
| **Q 60** | **웨이퍼 제조 3) 도핑 농도와 면저항의 관계** | 면저항 공식($R_s = \rho/t = 1/qN\mu t$), 4-Point Probe 측정 원리, 고농도 도핑 시 이온화 불순물 산란에 의한 이동도 저하(비선형성), 살리사이드(Salicide) & Raised S/D |
| **Q 61** | **웨이퍼 제조 4) 웨이퍼 결정 단면에 따른 특성 변화** | (100) 최저 원자밀도 & 최소 계면트랩($D_{it}$) ➔ 평면 NMOS 표준, (110) 정공 이동도 2배 우수 ➔ 3D FinFET 수직 측면 활용, 이방성 식각(Anisotropic Etch) 응용 |
| **Q 62** | **petdc는 무슨 공정 말하는 걸까?** | 팹(FAB) 5대 단위 공정 모듈 (P: Photo, E: Etch, T: Thin Film, D: Diffusion, C: CMP/Clean), 순환 루프, PECVD 오타 구별 |
| **Q 63** | **soi는 기생접합커패시턴스를 줄여줘 공핍커패시턴스를 줄여줘?** | **둘 다 획기적으로 절감!** (S/D 바닥 $C_j$ 80% 절감 ➔ 속도 30% 향상 + 채널 $C_{dep} \approx 0$ 극소화 ➔ $SS \approx 60\,\text{mV/dec}$) |
| **Q 64** | **기생접합커패시턴스와 공핍커패시턴스는 같은말이야?** | 물리적 원리($C=\epsilon/W_{dep}$) 일치 vs 소자 위치 차이(채널 표면 $C_{dep}$ vs S/D p-n 접합 $C_j$), SS vs RC 지연 |
| **Q 65** | **soi기술도입이유** | 매몰 산화막(BOX), 지하 펀치스루 원천 봉쇄, 접합 커패시턴스($C_j$) 80% 절감, $SS \approx 60\,\text{mV/dec}$, 래치업/소프트에러 박멸 |
| **Q 66** | **cox가 증가하면 vt는 왜 감소해?** | 문턱전압 수식 분모 위치, $V_{ox} = Q_{dep}/C_{ox}$, 전하 충전 효율, 전압 분배기($C_{ox} \gg C_{dep}$), 물통/확성기 비유 |
| **Q 67** | **halo implant에서 모서리 도핑 농도 높여놓으면 depletion이 가로막히는 로직** | 전하 중성 원리($Q^+=Q^-$), 전기력선 가우스 종단(Termination), 음전하 방패벽, 푸아송 적분, $W_{dep} \propto 1/\sqrt{N_A}$ |
| **Q 68** | **halo implant가 punchthrough 개선하는 메커니즘** | 헤일로($P^+$ Pocket), 공핍층 폭 압축($W_{dep} \propto 1/\sqrt{N_A}$), Depletion Merge 방지, Quad-Tilt, RSCE |
| **Q 69** | **표면쪽 농도를 감소시키면 drain side 높은 전계를 낮추는 메커니즘** | 푸아송 방정식($\frac{d\mathcal{E}}{dx} = \frac{qN}{\epsilon}$), 공간 전하 밀도($\rho$), 공핍층 폭($W_{dep} \propto 1/\sqrt{N}$) 확장, 삼각형 면적 법칙, Field Crowding 해소 |
| **Q 70** | **gidl에서 밴드간터널링이 뭐야?** | BTBT, 밴드 휨, 터널링 거리($d_{tunnel}$), EHP 생성, 양자역학적 관통, 온도 무관 |
| **Q 71** | **gate spacer가 핫캐리어와 gidl 억제하는 메커니즘** | 2단계 자기정렬 마스크, LDD 형성, $E_{lateral,max}$ 완화, $N^+$ 오버랩 차단 |
| **Q 72** | **ldd가 dibl에 좋은 점 설명** | 초얕은 접합($X_j$), $N^+$ 물리적 거리 격리, Charge Sharing 면적 극소화 |
| **Q 73** | **ldd로 dibl, gidl 둘 다 막을 수 있나?** | GIDL 직접 방어, DIBL 부분 개선 및 Halo 도핑과의 필수 공조 듀오 |
| **Q 74** | **shallow junction depth profile은 뭐야?** | 접합 깊이($X_j$), Sub-keV 저에너지 주입, 레이저 어닐링(LSA), Raised S/D |
| **Q 75** | **ldd한다고 어떻게 수평전기장피크를 낮추는 건데?** | $E \approx \Delta V / \Delta x$, 삼각형 넓이 법칙, 공핍층 밑변($W_{dep}$) 확장, 완만한 미끄럼틀 |
| **Q 76** | **ldd는 뭘 개선하기 위한 거야?** | HCI 억제(최우선), GIDL 억제, 드레인 항복전압($BV$) 개선, 직렬저항 트레이드오프 |
| **Q 77** | **ionization 발생하면 SS 특성 저하시키는 메커니즘** | 충격 이온화 정공 $\rightarrow$ $I_{sub} R_{sub}$ 기판 전위 상승 $\rightarrow$ 기생 BJT 턴온, 계면트랩($N_{it}$) |
| **Q 78** | **hot carrier injection이 뭐야?** | 핀치오프 초고전계, 충격 이온화, 산화막 주입($3.2\,\text{eV}$), $\Delta V_{th} > 0$ 노화 |
| **Q 79** | **gidl이 뭐야?** | 오버랩 영역 초고수직전계, BTBT 터널링, V자형 누설 곡선, DRAM 리텐션 타임 파괴 |
| **Q 80** | **depletion cap 줄이는 방법이 왜 shallow junction이야?** | $C = \epsilon A / d$, 3차원 박스에서 측면 공핍 면적($P \times X_j$) 축소, RC 지연 개선 |
| **Q 81** | **high-k는 dibl, punchthrough 둘 다 공통해결법이지?** | DIBL(표면)은 특효약, Punchthrough(지하 벌크)는 해결 불가 (PTS/FD-SOI 필요) |
| **Q 82** | **dibl 개선방법 중 high-k 메커니즘이 뭐야?** | 물리적 두께 유지로 터널링 차단, EOT 축소, $C_G \gg C_D$ 전압 분배, $\lambda$ 축소 |
| **Q 83** | **dibl 포텐셜 베리어는 소스-채널이야, 소스-바디야?** | 소스-채널 장벽(DIBL, 표면) vs 소스-바디 장벽(Punchthrough, 지하) 명확한 구분 |
| **Q 84** | **채널 감싸는 면적 증가할수록 dibl 유리한 메커니즘** | 전기력선 차폐(Shielding), $C_G \gg C_D$, 스케일 길이($\lambda$) 축소, 사각지대 박멸 |
| **Q 85** | **3d dram dual gate는 finfet이랑 다른 맥락이지?** | 다층 적층 공정 한계 극복, 저온 IGZO 이동도($I_{on}$) 2배 보상, 상/하 독립 제어 |
| **Q 86** | **punchthrough가 뭐야?** | 기판 지하 공핍층 결합(Merge), 전위 장벽 붕괴, 게이트 통제권 무력화, $V_{PT} \propto L^2$ |
| **Q 87** | **subthreshold current가 뭐야?** | 약반전 영역 확산(Diffusion) 전류, 볼츠만 열에너지, $SS \ge 60\,\text{mV/dec}$, 오프 누설 |
| **Q 88** | **vt 작아지면 좋은 거 아닌가?** | $I_{on}$ 증가 속도 장점 vs 서브스레숄드 누설 지수함수 폭증 및 수율 괴멸 위험 |
| **Q 89** | **채널에 음이온으로 charge 형성된다는 게 무슨 말이야?** | 정공(+) 쫓겨나고 고정 억셉터 붕소 음이온($B^-$)만 남은 공핍층, 빈 의자 비유 |
| **Q 90** | **S/D-Body 공핍층 침범으로 charge sharing되는 게 vt roll off야?** | Yau 모델, S/D이 공핍 음이온 숙제를 분담하여 게이트 필요 전압($Q_{B,eff}$) 감소 |
| **Q 91** | **vt roll off와 dibl을 알려줘** | 기하학적 전하 분할(정적) vs 드레인 전계 침투(동적 바이어스), 구동력 저하 오해 교정 |

---

## 3. 실행 및 열람
- **로컬 대시보드 파일**: [C:\Work\반도체3\index.html](file:///C:/Work/반도체3/index.html)
- **온라인 라이브 주소**: [https://richvayne13.github.io/semiconductor-3/](https://richvayne13.github.io/semiconductor-3/)
- **원클릭 배포 스크립트**: [C:\Work\반도체3\tool\261007_v1.0\deploy.bat](file:///C:/Work/반도체3/tool/261007_v1.0/deploy.bat)
