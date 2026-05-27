# Slide 108: Command with arguments

**Part 7: CUSTOM SLASH COMMANDS**

## Code Blocks

### arguments

```bash
# .claude/commands/fix-issue.md
다음 GitHub Issue 번호의 문제를 수정해 주세요: #$ARGUMENTS

작업 절차:
1. gh issue view $ARGUMENTS 로 issue 내용 확인
2. 관련 파일을 Grep으로 탐색
3. 문제 원인 파악
4. 수정 사항 적용
5. 테스트 작성 또는 갱신
6. PR 생성 시 "Closes #$ARGUMENTS" 명시

# 호출 예시
> /fix-issue 1234
# $ARGUMENTS가 "1234"로 치환됨

# 결과적으로 Claude가 받는 프롬프트
"다음 GitHub Issue 번호의 문제를 수정해 주세요: #1234
 작업 절차: 1. gh issue view 1234 로 issue 내용 확인 ..."

# 여러 인자
> /fix-issue 1234 high
# $ARGUMENTS = "1234 high" (전체가 한 문자열로)

# 더 정교한 처리는 명령 내부에서 prompting
"인자가 두 부분이면 첫째는 issue 번호,
 둘째는 우선순위로 처리해 주세요."

# 빈 호출
> /fix-issue
# $ARGUMENTS = "" (빈 문자열)
# 명령 내부에서 처리 방법 안내
```

## Speaker Notes

인자가 있는 명령 작성법입니다.
$ARGUMENTS 변수에 호출 시 입력된 인자가 들어갑니다.
fix-issue.md 예시를 봅니다.
명령 본문에 $ARGUMENTS를 여러 위치에 사용합니다.
GitHub issue 번호로 활용되며 작업 절차에도 포함됩니다.
호출 예시는 /fix-issue 1234입니다.
$ARGUMENTS가 1234 문자열로 치환됩니다.
결과적으로 Claude는 1234로 채워진 완전한 프롬프트를 받습니다.
여러 인자도 가능합니다.
공백으로 구분된 모든 인자가 한 문자열로 들어옵니다.
/fix-issue 1234 high는 $ARGUMENTS가 1234 high가 됩니다.
더 정교한 처리는 명령 내부에서 prompting으로 합니다.
예를 들어 인자가 두 부분이면 첫째는 issue 번호, 둘째는 우선순위로 처리해 달라고 안내할 수 있습니다.
빈 호출도 가능합니다.
인자 없이 호출하면 $ARGUMENTS가 빈 문자열이 됩니다.
명령 내부에서 적절히 처리하면 됩니다.
