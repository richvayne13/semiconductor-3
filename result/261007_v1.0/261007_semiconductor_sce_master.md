# [보고서] 반도체 소자 물리 & 단채널 효과(SCE) Q&A 백과사전 (사용자 질문 탭 순)

- **작성일자**: 2026년 10월 9일
- **저장경로**: `C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md`
- **배포 대시보드**: [C:\Work\반도체3\index.html](file:///C:/Work/반도체3/index.html)
- **온라인 라이브 서비스**: [https://richvayne13.github.io/semiconductor-3/](https://richvayne13.github.io/semiconductor-3/)

---

## 1. 개요 및 목적
본 보고서와 대시보드는 **사용자께서 직접 질문하신 문장 그대로 좌측 내비게이션 탭의 제목으로 구성**하고, **가장 최근에 질문하신 순서(역순/최신순)로 1번부터 30번까지 배치**하여 맞춤형 학습 및 면접 대비가 가능하도록 구축되었습니다.

각 질문 섹션은 항상 **[💡 면접 대비 3~4줄 핵심 요약]**이 선행되고, 이어지는 **[📘 세부 마스터 강의 노트]**에서 심층 물리 수식과 직관적인 고품질 SVG 시각 다이어그램을 다룹니다.

---

## 2. 사용자 질문 기반 목차 (최신순 34대 Q&A)

| 순번 | 좌측 탭 제목 (사용자 실제 질문) | 주요 핵심 키워드 |
| :---: | :--- | :--- |
| **Q 01** | **웨이퍼 제조 1) 초크랄스키 기법 (300mm 웨이퍼)** ⭐ [최신 1번] | 고순도 Si 융액(1420℃), 대시 네킹(Dash Necking: 3~5mm 무전위화), 숄더/직동(Body), MCZ(Magnetic CZ: 0.3T 전자기장으로 열대류 억제 & 산소 제어), 와이어소 절단/CMP |
| **Q 02** | **웨이퍼 제조 2) 기판 도핑 (P- / P+ / N- / N+)** | 전자의 높은 이동도($\mu_n \approx 3\mu_p$) 기반 NMOS 우선 설계 ➔ P- 기판 표준화, 래치업(Latch-up) 방지를 위한 P/P+ 에피 웨이퍼, 웰(Well) 격리 |
| **Q 03** | **웨이퍼 제조 3) 도핑 농도와 면저항의 관계** | 면저항 공식($R_s = \rho/t = 1/qN\mu t$), 4-Point Probe 측정 원리, 고농도 도핑 시 이온화 불순물 산란에 의한 이동도 저하(비선형성), 살리사이드(Salicide) & Raised S/D |
| **Q 04** | **웨이퍼 제조 4) 웨이퍼 결정 단면에 따른 특성 변화** | (100) 최저 원자밀도 & 최소 계면트랩($D_{it}$) ➔ 평면 NMOS 표준, (110) 정공 이동도 2배 우수 ➔ 3D FinFET 수직 측면 활용, 이방성 식각(Anisotropic Etch) 응용 |
| **Q 05** | **petdc는 무슨 공정 말하는 걸까?** | 팹(FAB) 5대 단위 공정 모듈 (P: Photo, E: Etch, T: Thin Film, D: Diffusion, C: CMP/Clean), 순환 루프, PECVD 오타 구별 |
| **Q 06** | **soi는 기생접합커패시턴스를 줄여줘 공핍커패시턴스를 줄여줘?** | **둘 다 획기적으로 절감!** (S/D 바닥 $C_j$ 80% 절감 ➔ 속도 30% 향상 + 채널 $C_{dep} \approx 0$ 극소화 ➔ $SS \approx 60\,\text{mV/dec}$) |
| **Q 07** | **기생접합커패시턴스와 공핍커패시턴스는 같은말이야?** | 물리적 원리($C=\epsilon/W_{dep}$) 일치 vs 소자 위치 차이(채널 표면 $C_{dep}$ vs S/D p-n 접합 $C_j$), SS vs RC 지연 |
| **Q 08** | **soi기술도입이유** | 매몰 산화막(BOX), 지하 펀치스루 원천 봉쇄, 접합 커패시턴스($C_j$) 80% 절감, $SS \approx 60\,\text{mV/dec}$, 래치업/소프트에러 박멸 |
| **Q 09** | **cox가 증가하면 vt는 왜 감소해?** | 문턱전압 수식 분모 위치, $V_{ox} = Q_{dep}/C_{ox}$, 전하 충전 효율, 전압 분배기($C_{ox} \gg C_{dep}$), 물통/확성기 비유 |
| **Q 10** | **halo implant에서 모서리 도핑 농도 높여놓으면 depletion이 가로막히는 로직** | 전하 중성 원리($Q^+=Q^-$), 전기력선 가우스 종단(Termination), 음전하 방패벽, 푸아송 적분, $W_{dep} \propto 1/\sqrt{N_A}$ |
| **Q 11** | **halo implant가 punchthrough 개선하는 메커니즘** | 헤일로($P^+$ Pocket), 공핍층 폭 압축($W_{dep} \propto 1/\sqrt{N_A}$), Depletion Merge 방지, Quad-Tilt, RSCE |
| **Q 12** | **표면쪽 농도를 감소시키면 drain side 높은 전계를 낮추는 메커니즘** | 푸아송 방정식($\frac{d\mathcal{E}}{dx} = \frac{qN}{\epsilon}$), 공간 전하 밀도($\rho$), 공핍층 폭($W_{dep} \propto 1/\sqrt{N}$) 확장, 삼각형 면적 법칙, Field Crowding 해소 |
| **Q 13** | **gidl에서 밴드간터널링이 뭐야?** | BTBT, 밴드 휨, 터널링 거리($d_{tunnel}$), EHP 생성, 양자역학적 관통, 온도 무관 |
| **Q 14** | **gate spacer가 핫캐리어와 gidl 억제하는 메커니즘** | 2단계 자기정렬 마스크, LDD 형성, $E_{lateral,max}$ 완화, $N^+$ 오버랩 차단 |
| **Q 15** | **ldd가 dibl에 좋은 점 설명** | 초얕은 접합($X_j$), $N^+$ 물리적 거리 격리, Charge Sharing 면적 극소화 |
| **Q 16** | **ldd로 dibl, gidl 둘 다 막을 수 있나?** | GIDL 직접 방어, DIBL 부분 개선 및 Halo 도핑과의 필수 공조 듀오 |
| **Q 17** | **shallow junction depth profile은 뭐야?** | 접합 깊이($X_j$), Sub-keV 저에너지 주입, 레이저 어닐링(LSA), Raised S/D |
| **Q 18** | **ldd한다고 어떻게 수평전기장피크를 낮추는 건데?** | $E \approx \Delta V / \Delta x$, 삼각형 넓이 법칙, 공핍층 밑변($W_{dep}$) 확장, 완만한 미끄럼틀 |
| **Q 19** | **ldd는 뭘 개선하기 위한 거야?** | HCI 억제(최우선), GIDL 억제, 드레인 항복전압($BV$) 개선, 직렬저항 트레이드오프 |
| **Q 20** | **ionization 발생하면 SS 특성 저하시키는 메커니즘** | 충격 이온화 정공 $\rightarrow$ $I_{sub} R_{sub}$ 기판 전위 상승 $\rightarrow$ 기생 BJT 턴온, 계면트랩($N_{it}$) |
| **Q 21** | **hot carrier injection이 뭐야?** | 핀치오프 초고전계, 충격 이온화, 산화막 주입($3.2\,\text{eV}$), $\Delta V_{th} > 0$ 노화 |
| **Q 22** | **gidl이 뭐야?** | 오버랩 영역 초고수직전계, BTBT 터널링, V자형 누설 곡선, DRAM 리텐션 타임 파괴 |
| **Q 23** | **depletion cap 줄이는 방법이 왜 shallow junction이야?** | $C = \epsilon A / d$, 3차원 박스에서 측면 공핍 면적($P \times X_j$) 축소, RC 지연 개선 |
| **Q 24** | **high-k는 dibl, punchthrough 둘 다 공통해결법이지?** | DIBL(표면)은 특효약, Punchthrough(지하 벌크)는 해결 불가 (PTS/FD-SOI 필요) |
| **Q 25** | **dibl 개선방법 중 high-k 메커니즘이 뭐야?** | 물리적 두께 유지로 터널링 차단, EOT 축소, $C_G \gg C_D$ 전압 분배, $\lambda$ 축소 |
| **Q 26** | **dibl 포텐셜 베리어는 소스-채널이야, 소스-바디야?** | 소스-채널 장벽(DIBL, 표면) vs 소스-바디 장벽(Punchthrough, 지하) 명확한 구분 |
| **Q 27** | **채널 감싸는 면적 증가할수록 dibl 유리한 메커니즘** | 전기력선 차폐(Shielding), $C_G \gg C_D$, 스케일 길이($\lambda$) 축소, 사각지대 박멸 |
| **Q 28** | **3d dram dual gate는 finfet이랑 다른 맥락이지?** | 다층 적층 공정 한계 극복, 저온 IGZO 이동도($I_{on}$) 2배 보상, 상/하 독립 제어 |
| **Q 29** | **punchthrough가 뭐야?** | 기판 지하 공핍층 결합(Merge), 전위 장벽 붕괴, 게이트 통제권 무력화, $V_{PT} \propto L^2$ |
| **Q 30** | **subthreshold current가 뭐야?** | 약반전 영역 확산(Diffusion) 전류, 볼츠만 열에너지, $SS \ge 60\,\text{mV/dec}$, 오프 누설 |
| **Q 31** | **vt 작아지면 좋은 거 아닌가?** | $I_{on}$ 증가 속도 장점 vs 서브스레숄드 누설 지수함수 폭증 및 수율 괴멸 위험 |
| **Q 32** | **채널에 음이온으로 charge 형성된다는 게 무슨 말이야?** | 정공(+) 쫓겨나고 고정 억셉터 붕소 음이온($B^-$)만 남은 공핍층, 빈 의자 비유 |
| **Q 33** | **S/D-Body 공핍층 침범으로 charge sharing되는 게 vt roll off야?** | Yau 모델, S/D이 공핍 음이온 숙제를 분담하여 게이트 필요 전압($Q_{B,eff}$) 감소 |
| **Q 34** | **vt roll off와 dibl을 알려줘** | 기하학적 전하 분할(정적) vs 드레인 전계 침투(동적 바이어스), 구동력 저하 오해 교정 |

---

## 3. 실행 및 열람
- **로컬 대시보드 파일**: [C:\Work\반도체3\index.html](file:///C:/Work/반도체3/index.html)
- **온라인 라이브 주소**: [https://richvayne13.github.io/semiconductor-3/](https://richvayne13.github.io/semiconductor-3/)
- **원클릭 배포 스크립트**: [C:\Work\반도체3\tool\261007_v1.0\deploy.bat](file:///C:/Work/반도체3/tool/261007_v1.0/deploy.bat)
