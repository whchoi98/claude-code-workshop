# Chapter 2: Agents & Subagents

에이전트와 서브에이전트

코드 블록 슬라이드: 53개

[← 워크샵 메인](../README.md)

## 파트 목록

## Part 1: SUBAGENTS 개념과 원리
Slides 6-20 (15 slides)

  - [Slide 10: Context isolation](./part-01-subagents-concepts/010-context-isolation.md)
  - [Slide 13: Tool permission isolation](./part-01-subagents-concepts/013-tool-permission-isolation.md)
  - [Slide 18: Cost & latency](./part-01-subagents-concepts/018-cost-latency.md)

## Part 2: SUBAGENT 정의 방법
Slides 21-35 (15 slides)

  - [Slide 22: Directory structure](./part-02-subagent-definition/022-directory-structure.md)
  - [Slide 24: YAML frontmatter structure](./part-02-subagent-definition/024-yaml-frontmatter-structure.md)
  - [Slide 26: description field](./part-02-subagent-definition/026-description-field.md)
  - [Slide 27: tools field](./part-02-subagent-definition/027-tools-field.md)
  - [Slide 30: Good description comparison](./part-02-subagent-definition/030-good-description-comparison.md)
  - [Slide 31: Example code-reviewer](./part-02-subagent-definition/031-example-code-reviewer.md)
  - [Slide 32: Example test-writer](./part-02-subagent-definition/032-example-test-writer.md)
  - [Slide 33: Example docs-writer](./part-02-subagent-definition/033-example-docs-writer.md)
  - [Slide 34: Permission inheritance](./part-02-subagent-definition/034-permission-inheritance.md)

## Part 3: TASK 도구와 디스패치
Slides 36-50 (15 slides)

  - [Slide 37: Task tool overview](./part-03-task-tool/037-task-tool-overview.md)
  - [Slide 38: Auto dispatch](./part-03-task-tool/038-auto-dispatch.md)
  - [Slide 39: Explicit invocation](./part-03-task-tool/039-explicit-invocation.md)
  - [Slide 41: Parallel example](./part-03-task-tool/041-parallel-example.md)
  - [Slide 43: Context passing](./part-03-task-tool/043-context-passing.md)
  - [Slide 45: Cost tracking](./part-03-task-tool/045-cost-tracking.md)
  - [Slide 47: Auto dispatch real example](./part-03-task-tool/047-auto-dispatch-real-example.md)
  - [Slide 48: Explicit dispatch real example](./part-03-task-tool/048-explicit-dispatch-real-example.md)

## Part 4: PATTERN 1 / CODE REVIEWER
Slides 51-62 (12 slides)

  - [Slide 53: Agent definition full](./part-04-pattern-1-code-reviewer/053-agent-definition-full.md)
  - [Slide 54: System prompt deep dive](./part-04-pattern-1-code-reviewer/054-system-prompt-deep-dive.md)
  - [Slide 55: Invocation interactive](./part-04-pattern-1-code-reviewer/055-invocation-interactive.md)
  - [Slide 56: Invocation headless](./part-04-pattern-1-code-reviewer/056-invocation-headless.md)
  - [Slide 57: GitHub Actions integration](./part-04-pattern-1-code-reviewer/057-github-actions-integration.md)
  - [Slide 59: Multi-agent collaboration](./part-04-pattern-1-code-reviewer/059-multi-agent-collaboration.md)

## Part 5: PATTERN 2 / TESTER
Slides 63-72 (10 slides)

  - [Slide 64: Agent definition](./part-05-pattern-2-tester/064-agent-definition.md)
  - [Slide 65: Coverage workflow](./part-05-pattern-2-tester/065-coverage-workflow.md)
  - [Slide 67: Real dialog](./part-05-pattern-2-tester/067-real-dialog.md)
  - [Slide 71: CI Integration](./part-05-pattern-2-tester/071-ci-integration.md)

## Part 6: PATTERN 3 / SECURITY SCANNER
Slides 73-82 (10 slides)

  - [Slide 74: Agent definition](./part-06-pattern-3-security-scanner/074-agent-definition.md)
  - [Slide 76: Real example dialog](./part-06-pattern-3-security-scanner/076-real-example-dialog.md)
  - [Slide 77: Dependency scanning](./part-06-pattern-3-security-scanner/077-dependency-scanning.md)
  - [Slide 78: Secret detection](./part-06-pattern-3-security-scanner/078-secret-detection.md)
  - [Slide 79: Pre-commit hook integration](./part-06-pattern-3-security-scanner/079-pre-commit-hook-integration.md)

## Part 7: PATTERN 4 / DOCS WRITER
Slides 83-92 (10 slides)

  - [Slide 84: Agent definition](./part-07-pattern-4-docs-writer/084-agent-definition.md)
  - [Slide 85: README generation](./part-07-pattern-4-docs-writer/085-readme-generation.md)
  - [Slide 86: API doc generation](./part-07-pattern-4-docs-writer/086-api-doc-generation.md)
  - [Slide 87: ADR generation](./part-07-pattern-4-docs-writer/087-adr-generation.md)
  - [Slide 88: Multilingual docs](./part-07-pattern-4-docs-writer/088-multilingual-docs.md)
  - [Slide 89: Changelog automation](./part-07-pattern-4-docs-writer/089-changelog-automation.md)
  - [Slide 90: CI integration](./part-07-pattern-4-docs-writer/090-ci-integration.md)

## Part 8: PATTERN 5 / MIGRATION BOT
Slides 93-100 (8 slides)

  - [Slide 94: Agent definition](./part-08-pattern-5-migration-bot/094-agent-definition.md)
  - [Slide 95: Lib upgrade scenario](./part-08-pattern-5-migration-bot/095-lib-upgrade-scenario.md)
  - [Slide 96: Import path migration](./part-08-pattern-5-migration-bot/096-import-path-migration.md)
  - [Slide 97: API deprecation](./part-08-pattern-5-migration-bot/097-api-deprecation.md)
  - [Slide 99: Cost efficiency](./part-08-pattern-5-migration-bot/099-cost-efficiency.md)

## Part 9: RECAP & LABS
Slides 101-110 (10 slides)

  - [Slide 103: Lab 1](./part-09-recap-labs/103-lab-1.md)
  - [Slide 104: Lab 2](./part-09-recap-labs/104-lab-2.md)
  - [Slide 105: Lab 3](./part-09-recap-labs/105-lab-3.md)
  - [Slide 106: Lab 4](./part-09-recap-labs/106-lab-4.md)
  - [Slide 107: FAQ](./part-09-recap-labs/107-faq.md)
  - [Slide 109: References](./part-09-recap-labs/109-references.md)
