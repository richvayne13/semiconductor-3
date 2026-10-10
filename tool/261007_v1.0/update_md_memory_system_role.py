# -*- coding: utf-8 -*-
import re

md_path = r"C:\Work\반도체3\result\261007_v1.0\261007_semiconductor_sce_master.md"

with open(md_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update title / count
content = re.sub(
    r"## 2\. 사용자 질문 기반 목차 \(최신순 \d+대 Q&A\)",
    r"## 2. 사용자 질문 기반 목차 (최신순 92대 Q&A)",
    content
)

# Shift existing Q 01 ~ Q 91 to Q 02 ~ Q 92
for old_n in range(91, 0, -1):
    new_n = old_n + 1
    old_str = f"Q {old_n:02d}"
    new_str = f"Q {new_n:02d}"
    content = re.sub(
        rf"\|\s*\*\*{old_str}\*\*\s*\|",
        f"| **{new_str}** |",
        content
    )

# Remove ⭐ [최신 1번] from old Q 01 (now Q 02)
content = content.replace("⭐ [최신 1번] |", "|")

# Define new Q 01 row
new_q01_row = (
    "| **Q 01** | **메모리가 시스템에서 어떤 역할을 하는가? (폰 노이만 구조, 계층 구조, 메모리 월, HBM)** ⭐ [최신 1번] | "
    "폰 노이만 프로그램 내장 방식의 실행 무대(책상과 창고의 비유), "
    "10만 배의 속도-용량-비용 격차를 완충하는 4단계 메모리 계층 구조(레지스터 ➔ SRAM 캐시 ➔ DRAM/HBM ➔ NAND Flash SSD), "
    "가상 메모리(Virtual Memory)를 통한 메모리 보호 및 자원 추상화, "
    "AI 시대의 폰 노이만 병목인 '메모리 월(Memory Wall)'과 HBM 초광대역 대역폭(1.2~3.3 TB/s) 및 PIM(Processing-In-Memory) 연산 패러다임 혁신 |\n"
)

# Insert new Q 01 right after header row
header_divider = "| :---: | :--- | :--- |\n"
pos = content.find(header_divider)
if pos != -1:
    insert_pos = pos + len(header_divider)
    content = content[:insert_pos] + new_q01_row + content[insert_pos:]

with open(md_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully updated {md_path}")
