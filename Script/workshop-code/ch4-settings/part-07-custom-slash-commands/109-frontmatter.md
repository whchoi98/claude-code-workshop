# Slide 109: Frontmatter

**Part 7: CUSTOM SLASH COMMANDS**

## Code Blocks

### frontmatter

```bash
# .claude/commands/security-review.md
---
description: 보안 관점 코드 리뷰 (취약점, secret, OWASP Top 10)
allowed-tools:
  - Read
  - Grep
  - Glob
model: claude-opus-4-5      # 보안 분석은 Opus 권장
disable-model-invocation: false
---

다음 git diff를 보안 관점에서 검토해 주세요: $ARGUMENTS

검토 항목:
1. OWASP Top 10 패턴 검사
2. 시크릿 또는 자격증명 노출 여부
3. SQL injection 가능성
4. XSS 취약점
5. 권한 우회 가능성

# Frontmatter 필드 설명
description:    /commands 목록에 표시되는 설명
allowed-tools:  이 명령 실행 중 허용되는 도구 (보안 강화)
model:          이 명령에 강제로 사용할 모델
disable-model-invocation: true면 사용자 모델 선택 비활성
argument-hint:  인자 형식 힌트 (자동완성에 도움)

# 사용 예시 (목록 표시 시)
> /
  /review            - PR 자동 리뷰
  /security-review   - 보안 관점 코드 리뷰 (취약점, ...)
  /deploy            - 표준 배포 절차
```

## Speaker Notes

Frontmatter는 명령 메타데이터를 정의합니다.
security-review.md 예시를 봅니다.
YAML frontmatter는 파일 상단에 세 줄짜리 대시로 둘러쌉니다.
description은 /commands 목록에 표시되는 설명입니다.
allowed-tools는 이 명령 실행 중 허용되는 도구를 명시합니다.
Read, Grep, Glob만 허용해 보안을 강화할 수 있습니다.
model은 이 명령에 강제로 사용할 모델을 지정합니다.
보안 분석은 Opus가 권장됩니다.
disable-model-invocation을 true로 하면 사용자가 다른 모델로 전환할 수 없게 합니다.
중요한 명령에 모델을 강제하는 패턴입니다.
argument-hint는 인자 형식 힌트로 자동완성에 도움됩니다.
사용 예시를 봅니다.
슬래시만 입력하면 description이 함께 표시되어 사용자가 명령을 쉽게 발견할 수 있습니다.
