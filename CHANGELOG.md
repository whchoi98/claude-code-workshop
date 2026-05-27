# Changelog

[![English](https://img.shields.io/badge/lang-English-blue.svg)](#english)
[![Korean](https://img.shields.io/badge/lang-%ED%95%9C%EA%B5%AD%EC%96%B4-red.svg)](#한국어)

---

# English

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-05-25

### Added

- Publish the initial Claude Code Deep Dive Workshop release as a PDF-centric distribution of the three-day, 850-slide curriculum.
- Distribute Chapter 1 (Overview, 200 slides) as `PDF/ClaudeCode_Ch1_20260525.pdf`.
- Distribute Chapter 2 (Agents & Subagents, 110 slides) as `PDF/ClaudeCode_Ch2_20260525.pdf`.
- Distribute Chapter 3 (Admin Setup, 120 slides) as `PDF/ClaudeCode_Ch3_20260525.pdf`.
- Distribute Chapter 4 (Settings, 140 slides) as `PDF/ClaudeCode_Ch4_20260525.pdf`.
- Distribute Chapter 5 (CLI Reference, 130 slides) as `PDF/ClaudeCode_Ch5_20260525..pdf`.
- Distribute Chapter 6 (Agent SDK, 150 slides) as `PDF/ClaudeCode_Ch6_20260525.pdf`.
- Add the extracted code snippet archive under `Script/workshop-code/`, totaling 502 markdown files across six chapter folders and 53 part folders.
- Include 108 snippets under `ch1-overview` across 10 parts covering installation, IDE integration, and CLAUDE.md authoring.
- Include 53 snippets under `ch2-agents` across 9 parts covering subagent definition, the Task tool, and five production patterns.
- Include 57 snippets under `ch3-admin` across 9 parts covering deployment, credentials, network security, governance, SSO, and audit logging.
- Include 86 snippets under `ch4-settings` across 9 parts covering `settings.json`, permissions, hooks, MCP, and custom slash commands.
- Include 86 snippets under `ch5-cli` across 8 parts covering the `claude` CLI, headless mode, output formats, and CI/CD integration.
- Include 112 snippets under `ch6-sdk` across 8 parts covering SDK basics, the Messages API, tool use, streaming, MCP integration, and production patterns.
- Provide Python and TypeScript samples side by side across the Agent SDK material.
- Cover three authentication paths in all SDK examples: Anthropic Direct, Amazon Bedrock, and Vertex AI.
- Embed a single-sentence Korean speaker note in every extracted snippet markdown file.
- Apply a consistent design system — 16:9 ratio, Black/Navy theme (`#161D26`), accent color (`#FF9900`) — across all six chapter PDFs.
- Add `Script/workshop-code-README.md` and `Script/workshop-code/README.md` as navigation guides for the snippet archive.

[Unreleased]: https://github.com/<your-org>/claude-code-workshop/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/<your-org>/claude-code-workshop/releases/tag/v1.0.0

---

# 한국어

이 프로젝트의 모든 주요 변경 사항은 이 파일에 기록됩니다.
이 문서는 [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)를 기반으로 하며, [Semantic Versioning](https://semver.org/spec/v2.0.0.html)을 따릅니다.

## [Unreleased]

## [1.0.0] - 2026-05-25

### Added

- 3일 850 슬라이드 분량의 Claude Code Deep Dive Workshop 커리큘럼을 PDF 중심 배포 형태로 최초 공개.
- Chapter 1 (Overview, 200 슬라이드) `PDF/ClaudeCode_Ch1_20260525.pdf` 로 배포.
- Chapter 2 (Agents & Subagents, 110 슬라이드) `PDF/ClaudeCode_Ch2_20260525.pdf` 로 배포.
- Chapter 3 (Admin Setup, 120 슬라이드) `PDF/ClaudeCode_Ch3_20260525.pdf` 로 배포.
- Chapter 4 (Settings, 140 슬라이드) `PDF/ClaudeCode_Ch4_20260525.pdf` 로 배포.
- Chapter 5 (CLI Reference, 130 슬라이드) `PDF/ClaudeCode_Ch5_20260525..pdf` 로 배포.
- Chapter 6 (Agent SDK, 150 슬라이드) `PDF/ClaudeCode_Ch6_20260525.pdf` 로 배포.
- 6개 챕터 폴더와 53개 파트 폴더에 걸친 총 502개 마크다운 파일로 구성된 코드 스니펫 아카이브를 `Script/workshop-code/` 아래에 추가.
- `ch1-overview` 10개 파트에 설치, IDE 통합, CLAUDE.md 작성을 다루는 108개 스니펫 포함.
- `ch2-agents` 9개 파트에 서브에이전트 정의, Task 도구, 5가지 실전 패턴을 다루는 53개 스니펫 포함.
- `ch3-admin` 9개 파트에 배포, 자격 증명, 네트워크 보안, 거버넌스, SSO, 감사 로그를 다루는 57개 스니펫 포함.
- `ch4-settings` 9개 파트에 `settings.json`, Permissions, Hooks, MCP, 커스텀 Slash 명령을 다루는 86개 스니펫 포함.
- `ch5-cli` 8개 파트에 `claude` CLI, Headless 모드, 출력 포맷, CI/CD 통합을 다루는 86개 스니펫 포함.
- `ch6-sdk` 8개 파트에 SDK 기초, Messages API, Tool Use, Streaming, MCP 통합, 프로덕션 패턴을 다루는 112개 스니펫 포함.
- Agent SDK 자료 전반에 Python과 TypeScript 예제 동등 제공.
- 모든 SDK 예제에 Anthropic Direct, Amazon Bedrock, Vertex AI 등 3가지 인증 경로 적용.
- 모든 추출 스니펫 마크다운 파일에 단문화된 한국어 발표자 노트 포함.
- 16:9 비율, Black/Navy 테마(`#161D26`), 액센트 컬러(`#FF9900`)로 구성된 일관된 디자인 시스템을 6개 챕터 PDF 전체에 일관 적용.
- 스니펫 아카이브 탐색을 돕는 `Script/workshop-code-README.md` 와 `Script/workshop-code/README.md` 추가.

[Unreleased]: https://github.com/<your-org>/claude-code-workshop/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/<your-org>/claude-code-workshop/releases/tag/v1.0.0
