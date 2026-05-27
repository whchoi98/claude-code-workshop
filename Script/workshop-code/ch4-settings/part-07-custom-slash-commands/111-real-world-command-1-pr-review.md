# Slide 111: Real-world command 1: PR review

**Part 7: CUSTOM SLASH COMMANDS**

## Code Blocks

### review-pr

```bash
# .claude/commands/review-pr.md
---
description: PR 자동 종합 리뷰 (코드 + 보안 + 테스트)
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash(gh pr:*)
  - Bash(git diff:*)
model: claude-sonnet-4-5
---

PR #$ARGUMENTS 를 종합 리뷰해 주세요.

# 절차
1. gh pr view $ARGUMENTS 로 PR 정보 가져오기
2. gh pr diff $ARGUMENTS 로 변경 내용 분석
3. 다음 4가지 관점에서 검토:

## 1. 코드 품질
- 가독성, 명명, 구조
- 중복 코드, 복잡도
- SOLID 원칙 위반

## 2. 보안
- OWASP Top 10
- 시크릿 노출
- 입력 검증 부재

## 3. 테스트
- 커버리지 (변경 부분에 새 테스트가 있는가)
- 엣지 케이스 누락
- 통합 테스트 필요성

## 4. 운영
- 성능 영향
- 의존성 변경
- 마이그레이션 필요성

# 출력 형식
각 섹션을 분리하고, 우선순위 (Critical / Important / Suggestion)
로 정리. 직접적인 수정 제안 코드 블록 포함.
```

## Speaker Notes

실전 명령 첫 번째는 PR 종합 리뷰입니다.
frontmatter에 description, allowed-tools, model을 명시합니다.
allowed-tools에 Read, Grep, Glob과 함께 gh pr 명령과 git diff 명령을 허용합니다.
명령 본문은 4가지 관점의 종합 리뷰 절차입니다.
절차 1단계는 gh pr view로 PR 정보 가져오기, 2단계는 gh pr diff로 변경 내용 분석입니다.
3단계가 핵심으로 4가지 관점 검토입니다.
첫째, 코드 품질로 가독성, 명명, 구조, 중복, SOLID 원칙을 봅니다.
둘째, 보안으로 OWASP Top 10, 시크릿 노출, 입력 검증을 점검합니다.
셋째, 테스트로 커버리지, 엣지 케이스, 통합 테스트 필요성을 봅니다.
넷째, 운영으로 성능 영향, 의존성 변경, 마이그레이션을 검토합니다.
출력 형식도 명시합니다.
각 섹션을 분리하고 우선순위로 정리하며 직접적인 수정 제안 코드 블록을 포함하도록 합니다.
호출은 /review-pr 1234처럼 간단합니다.
