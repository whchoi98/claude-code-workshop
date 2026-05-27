# Claude Code Deep Dive Workshop

[![License: Proprietary](https://img.shields.io/badge/license-Proprietary-blue.svg)](#license)
[![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)](./PDF)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](./CHANGELOG.md)
[![English](https://img.shields.io/badge/lang-English-blue.svg)](#english)
[![Korean](https://img.shields.io/badge/lang-%ED%95%9C%EA%B5%AD%EC%96%B4-red.svg)](#한국어)

A 3-day Claude Code curriculum delivered as six rendered PDF chapters and 502 extracted code snippets.
6개 챕터 PDF와 502개 추출 코드 스니펫으로 제공되는 3일간의 Claude Code 커리큘럼입니다.

---

# English

## Overview

Claude Code Deep Dive Workshop is a Korean-language technical curriculum delivered as ready-to-present PDF slide decks and a searchable archive of every code example used in the workshop. The repository contains six chapter PDFs covering 850 slides in total, paired with 502 markdown files that extract each code-bearing slide into a standalone, grep-friendly snippet with Korean speaker notes. All slide artifacts follow a consistent design system for visual identity.

## Features

- **Six rendered PDF chapters** — 850 slides total covering Overview, Agents & Subagents, Admin Setup, Settings, CLI Reference, and the Agent SDK.
- **502 extracted code snippets** — Each code-bearing slide is exported as a numbered markdown file under `Script/workshop-code/`, organized by chapter and part for fast lookup.
- **Bilingual coverage in code** — Python and TypeScript samples appear side by side across SDK material, with three authentication paths (Anthropic Direct, Amazon Bedrock, Vertex AI).
- **Korean speaker notes per snippet** — Every extracted markdown file embeds the original Korean speaker script alongside the code.
- **Self-contained — no build step required** — PDFs and markdown ship pre-rendered; consumers only need a PDF viewer and a text editor.

## Prerequisites

- A PDF viewer to read the chapter decks under `PDF/`.
- A text editor or GitHub viewer to read markdown snippets under `Script/workshop-code/`.
- `grep` and `find` (or any equivalent search tool) to locate snippets by keyword or file name.
- `git` to clone the repository.

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-org>/claude-code-workshop.git
cd claude-code-workshop

# 2. Open the PDF for a given chapter (example: Chapter 1)
xdg-open PDF/ClaudeCode_Ch1_20260525.pdf    # Linux
# open  PDF/ClaudeCode_Ch1_20260525.pdf       # macOS

# 3. Browse extracted code snippets
ls Script/workshop-code/ch6-sdk/part-06-production/
```

## Usage

```bash
# Find Python retry patterns
grep -rn "tenacity" Script/workshop-code/

# Find hook examples across all chapters
grep -rn "PreToolUse" Script/workshop-code/

# Find authentication-related snippets by file name
find Script/workshop-code/ -name "*auth*"

# List all snippets in a specific part
ls Script/workshop-code/ch6-sdk/part-01-sdk-basics/
# → 007-python-install-first-call.md
# → 008-typescript-install-first-call.md
# → ...

# Open a single snippet
cat Script/workshop-code/ch6-sdk/part-06-production/104-retry-python.md
```

## Project Structure

```
claude-code-workshop/
├── README.md                                  # This file
├── CHANGELOG.md                               # Per-version change history
├── PDF/                                       # Rendered chapter decks (final artifacts)
│   ├── ClaudeCode_Ch1_20260525.pdf            # Ch.1 Overview, 200 slides
│   ├── ClaudeCode_Ch2_20260525.pdf            # Ch.2 Agents & Subagents, 110 slides
│   ├── ClaudeCode_Ch3_20260525.pdf            # Ch.3 Admin Setup, 120 slides
│   ├── ClaudeCode_Ch4_20260525.pdf            # Ch.4 Settings, 140 slides
│   ├── ClaudeCode_Ch5_20260525..pdf           # Ch.5 CLI Reference, 130 slides
│   └── ClaudeCode_Ch6_20260525.pdf            # Ch.6 Agent SDK, 150 slides
└── Script/
    ├── workshop-code-README.md                # Top-level guide for the snippet archive
    └── workshop-code/                         # 502 extracted code snippets
        ├── README.md
        ├── ch1-overview/                      # 10 parts, 108 snippets
        ├── ch2-agents/                        #  9 parts,  53 snippets
        ├── ch3-admin/                         #  9 parts,  57 snippets
        ├── ch4-settings/                      #  9 parts,  86 snippets
        ├── ch5-cli/                           #  8 parts,  86 snippets
        └── ch6-sdk/                           #  8 parts, 112 snippets
```

Each snippet file is named `NNN-meaningful-slug.md`, where `NNN` is the slide number. The markdown body contains the slide title, the full code block, and the Korean speaker note.

## Contributing

Contributions are welcome. Follow this flow:

1. **Fork** the repository on GitHub.
2. **Branch** from `main`: `git checkout -b fix/your-change`.
3. **Commit** using [Conventional Commits](https://www.conventionalcommits.org):
   - `feat: add ch6-sdk multi-agent orchestration snippet`
   - `fix: correct retry backoff in 104-retry-python.md`
   - `docs: clarify directory layout in README`
4. **Push** to your fork: `git push origin fix/your-change`.
5. **Open a Pull Request** referencing the relevant issue and describing the change.

For changes that affect snippet content, please cite the source slide number in the commit body so reviewers can cross-reference the PDF.

## License

This project is distributed under **Proprietary** terms. Internal use, private delivery to customers, and modification for internal training are permitted; external redistribution and commercial resale are prohibited.

## Contact

- Maintainer: **Choi WooHyung** — Principal Solutions Architect
- Email: whchoi@amazon.com
- LinkedIn: [linkedin.com/in/woohyungchoi](https://linkedin.com/in/woohyungchoi)
- Issues: open an issue on the repository hosting this project.

---

# 한국어

## 개요

Claude Code Deep Dive Workshop은 발표 가능한 PDF 슬라이드 자료와 워크샵에서 사용된 모든 코드 예제를 검색 가능한 형태로 함께 제공하는 한국어 기술 커리큘럼입니다. 저장소에는 총 850 슬라이드 분량의 6개 챕터 PDF와, 코드를 포함한 슬라이드를 각각 독립된 마크다운 파일로 추출한 502개의 스니펫이 함께 들어 있습니다. 추출된 각 파일에는 한국어 발표자 노트가 포함되어 있으며, 모든 슬라이드 자료는 일관된 디자인 시스템을 따라 시각 정체성을 유지합니다.

## 주요 기능

- **6개 챕터 PDF 산출물** — Overview, Agents & Subagents, Admin Setup, Settings, CLI Reference, Agent SDK 총 850 슬라이드.
- **502개 추출 코드 스니펫** — 코드를 포함하는 모든 슬라이드가 `Script/workshop-code/` 아래에 챕터·파트 단위로 번호가 매겨진 마크다운으로 정리되어 빠른 검색이 가능합니다.
- **코드 수준의 이중 언어 지원** — SDK 자료 전반에 Python과 TypeScript 예제가 나란히 제공되며, 3가지 인증 경로(Anthropic Direct, Amazon Bedrock, Vertex AI)를 모두 다룹니다.
- **스니펫별 한국어 발표자 노트** — 추출된 모든 마크다운 파일에 코드와 함께 원본 한국어 발표 스크립트가 포함됩니다.
- **빌드 단계 없는 즉시 활용** — PDF와 마크다운이 사전 렌더링되어 제공되므로 PDF 뷰어와 텍스트 에디터만 있으면 바로 사용할 수 있습니다.

## 사전 요구 사항

- `PDF/` 아래 챕터 PDF를 열어볼 수 있는 PDF 뷰어.
- `Script/workshop-code/` 아래 마크다운을 확인할 수 있는 텍스트 에디터 또는 GitHub 웹 뷰어.
- 키워드나 파일명으로 스니펫을 찾기 위한 `grep`, `find` (또는 동등한 검색 도구).
- 저장소 클론에 사용할 `git`.

## 설치 방법

```bash
# 1. 저장소 클론
git clone https://github.com/<your-org>/claude-code-workshop.git
cd claude-code-workshop

# 2. 원하는 챕터 PDF 열기 (예: Chapter 1)
xdg-open PDF/ClaudeCode_Ch1_20260525.pdf    # Linux
# open  PDF/ClaudeCode_Ch1_20260525.pdf       # macOS

# 3. 추출된 코드 스니펫 탐색
ls Script/workshop-code/ch6-sdk/part-06-production/
```

## 사용법

```bash
# Python retry 패턴 찾기
grep -rn "tenacity" Script/workshop-code/

# 전체 챕터에서 Hook 예제 찾기
grep -rn "PreToolUse" Script/workshop-code/

# 인증 관련 스니펫을 파일명으로 찾기
find Script/workshop-code/ -name "*auth*"

# 특정 파트의 스니펫 목록 확인
ls Script/workshop-code/ch6-sdk/part-01-sdk-basics/
# → 007-python-install-first-call.md
# → 008-typescript-install-first-call.md
# → ...

# 단일 스니펫 열기
cat Script/workshop-code/ch6-sdk/part-06-production/104-retry-python.md
```

## 프로젝트 구조

```
claude-code-workshop/
├── README.md                                  # 이 파일
├── CHANGELOG.md                               # 버전별 변경 사항
├── PDF/                                       # 렌더링된 챕터 산출물
│   ├── ClaudeCode_Ch1_20260525.pdf            # Ch.1 Overview, 200 슬라이드
│   ├── ClaudeCode_Ch2_20260525.pdf            # Ch.2 Agents & Subagents, 110 슬라이드
│   ├── ClaudeCode_Ch3_20260525.pdf            # Ch.3 Admin Setup, 120 슬라이드
│   ├── ClaudeCode_Ch4_20260525.pdf            # Ch.4 Settings, 140 슬라이드
│   ├── ClaudeCode_Ch5_20260525..pdf           # Ch.5 CLI Reference, 130 슬라이드
│   └── ClaudeCode_Ch6_20260525.pdf            # Ch.6 Agent SDK, 150 슬라이드
└── Script/
    ├── workshop-code-README.md                # 스니펫 아카이브 최상위 가이드
    └── workshop-code/                         # 추출된 502개 코드 스니펫
        ├── README.md
        ├── ch1-overview/                      # 10개 파트, 108개 스니펫
        ├── ch2-agents/                        #  9개 파트,  53개 스니펫
        ├── ch3-admin/                         #  9개 파트,  57개 스니펫
        ├── ch4-settings/                      #  9개 파트,  86개 스니펫
        ├── ch5-cli/                           #  8개 파트,  86개 스니펫
        └── ch6-sdk/                           #  8개 파트, 112개 스니펫
```

각 스니펫 파일은 `NNN-의미있는-슬러그.md` 형식이며, `NNN`은 슬라이드 번호입니다. 마크다운 본문에는 슬라이드 제목, 전체 코드 블록, 한국어 발표자 노트가 포함됩니다.

## 기여 방법

기여를 환영합니다. 아래 순서를 따라 주세요.

1. GitHub에서 저장소를 **포크(Fork)** 합니다.
2. `main`에서 새 **브랜치(Branch)** 를 생성합니다: `git checkout -b fix/your-change`.
3. [Conventional Commits](https://www.conventionalcommits.org) 형식으로 **커밋(Commit)** 합니다.
   - `feat: ch6-sdk 멀티 에이전트 오케스트레이션 스니펫 추가`
   - `fix: 104-retry-python.md의 retry backoff 수정`
   - `docs: README의 디렉토리 구조 설명 명확화`
4. 포크된 저장소에 **푸시(Push)** 합니다: `git push origin fix/your-change`.
5. 관련 이슈를 참조하고 변경 사항을 설명하며 **Pull Request** 를 엽니다.

스니펫 내용이 변경되는 경우, 리뷰어가 PDF와 대조할 수 있도록 커밋 본문에 원본 슬라이드 번호를 명시해 주세요.

## 라이선스

이 프로젝트는 **Proprietary** 조건으로 배포됩니다. 내부 활용, 고객사 대상 비공개 발표, 사내 교육 목적의 수정은 허용되며, 외부 공개 재배포와 상업적 재판매는 금지됩니다.

## 연락처

- 메인테이너: **최우형(Choi WooHyung)** — Principal Solutions Architect
- 이메일: whchoi@amazon.com
- LinkedIn: [linkedin.com/in/woohyungchoi](https://linkedin.com/in/woohyungchoi)
- 이슈: 이 프로젝트가 호스팅된 저장소에 이슈를 등록해 주세요.
