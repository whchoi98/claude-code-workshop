# Slide 174: Pattern 4 Multi-Agent

**Part 9: WORKFLOW PATTERNS**

## Code Blocks

### SUBAGENTS

```bash
> 대규모 마이그레이션 작업을 Subagents로 분할해 주세요.

Main Claude:
  ✓ 작업 분석: 47개 파일을 5개 영역으로 분할
  ✓ Subagent 1: src/api/* (10 files) - api-migrator
  ✓ Subagent 2: src/services/* (12 files) - service-migrator
  ✓ Subagent 3: src/components/* (15 files) - ui-migrator
  ✓ Subagent 4: tests/* (8 files) - test-migrator
  ✓ Subagent 5: docs/* (2 files) - doc-updater

  병렬 실행:
    Subagent 1-4 동시 진행 (각각 격리된 컨텍스트)
    Subagent 5는 1-4 완료 후 실행 (의존성)

  ✓ 모든 결과 취합 후 통합 PR 생성

# Chapter 2에서 Subagents 시스템을 깊이 다룹니다.
```

## Speaker Notes

Pattern 4 Multi-Agent는 Subagents를 활용한 병렬 처리입니다.
Chapter 2에서 깊이 다루지만 여기서는 맛보기로 살펴봅니다.
47개 파일의 대규모 마이그레이션 작업이 있을 때, Main Claude가 작업을 5개 영역으로 분할하고 각 영역에 전문 Subagent를 할당합니다.
api-migrator, service-migrator, ui-migrator, test-migrator는 동시에 병렬 실행되며 각각 격리된 컨텍스트를 가집니다.
doc-updater는 다른 작업이 완료된 후 실행되어 일관된 문서를 만듭니다.
병렬 처리로 시간이 크게 단축되며, 격리된 컨텍스트로 안전성도 보장됩니다.
