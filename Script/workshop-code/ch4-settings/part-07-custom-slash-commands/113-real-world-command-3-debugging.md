# Slide 113: Real-world command 3: Debugging

**Part 7: CUSTOM SLASH COMMANDS**

## Code Blocks

### debug-error

```bash
# .claude/commands/debug-error.md
---
description: 에러 로그 분석과 원인 추적
argument-hint: <error message or file path>
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash(git log:*)
  - Bash(git blame:*)
---

다음 에러를 분석하고 원인을 추적해 주세요:

$ARGUMENTS

# 분석 절차
1. 에러 메시지에서 키워드 추출 (함수명, 파일명, 라인)

2. 관련 코드 위치 탐색
   - Grep으로 함수명 검색
   - 호출 체인 추적 (caller 찾기)

3. 최근 변경 이력 확인
   - git log --all -p --grep="<관련 키워드>"
   - git blame 으로 해당 라인 변경자와 시점

4. 가능성 있는 원인 3가지 가설 제시
   - 입력 검증 부재
   - race condition
   - null/undefined 처리 누락
   - 외부 의존성 변경
   - 기타

5. 각 가설별 검증 방법 제시
   - 어떤 로그를 추가하면 확인 가능한가
   - 어떤 테스트 케이스가 재현하는가

6. 즉시 적용 가능한 수정 제안
   - 핫픽스 (임시)
   - 근본 수정 (장기)

# 호출 예시
> /debug-error "TypeError: Cannot read property 'id' of undefined at user.js:42"
```

## Speaker Notes

실전 명령 세 번째는 에러 디버깅입니다.
frontmatter에 description, argument-hint, allowed-tools를 명시합니다.
디버깅에 필요한 Read, Grep, Glob, git log, git blame만 허용합니다.
명령 본문은 6단계 분석 절차입니다.
1단계 에러 메시지에서 함수명, 파일명, 라인을 키워드로 추출합니다.
2단계 관련 코드 위치를 Grep으로 탐색하고 호출 체인을 추적합니다.
3단계 최근 변경 이력을 git log와 git blame으로 확인합니다.
4단계 가능성 있는 원인 3가지 가설을 제시합니다.
입력 검증 부재, race condition, null 처리 누락, 외부 의존성 변경 같은 일반적 원인들입니다.
5단계 각 가설별 검증 방법을 제시합니다.
어떤 로그를 추가하면 확인 가능한지, 어떤 테스트 케이스가 재현하는지 안내합니다.
6단계 즉시 적용 가능한 수정 제안을 합니다.
핫픽스로 임시 조치, 근본 수정으로 장기 해결을 모두 제시합니다.
호출은 에러 메시지를 인자로 전달하면 됩니다.
