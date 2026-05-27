# Slide 162: Import Syntax

**Part 8: CLAUDE.md & MEMORY**

## Code Blocks

### @import

```bash
# CLAUDE.md 안에 다른 마크다운 파일을 임포트

# Project: my-app

@./docs/architecture.md
@./docs/coding-style.md
@./.claude/local.md

# 또는 사내 표준
@/etc/claude/team-rules.md
@~/.claude/personal-style.md

## Specific Project Notes
- 이 프로젝트만의 특수 사정...

# 효과:
#  - 큰 CLAUDE.md를 여러 파일로 분할 관리
#  - 사내 표준 파일을 여러 프로젝트가 공유
#  - 임포트는 재귀적으로 처리 (단, 순환 참조 방지)
```

## Speaker Notes

CLAUDE.md 안에서 다른 마크다운 파일을 임포트할 수 있습니다.
@ 기호 다음에 경로를 적으면 그 파일의 내용이 CLAUDE.md에 포함됩니다.
큰 CLAUDE.md를 여러 파일로 분할해 관리할 수 있고, 사내 표준 파일을 만들어 여러 프로젝트가 동일한 내용을 공유할 수 있으며, 임포트가 재귀적으로 처리되어 임포트된 파일이 또 다른 파일을 임포트할 수 있습니다.
