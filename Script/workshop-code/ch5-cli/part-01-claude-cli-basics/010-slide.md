# Slide 10: 동작 모드 옵션

**Part 1: claude 명령 기본**

## Code Blocks

### -p 옵션

```bash
# 1. 대화형 (인자 없음)
$ claude
> 이 코드 리뷰해 줘
> 추가로 보안 관점에서도 봐 줘
> /exit

# 2. Headless 단일 응답
$ claude -p "현재 디렉토리 구조 분석"
# 응답 후 종료. 추가 대화 불가.

# 3. Headless 다회 도구 호출
$ claude -p "README.md를 읽고 요약해서 SUMMARY.md에 저장"
# Claude가 Read와 Write를 자동으로 호출
# 모든 작업 완료 후 종료

# 4. -p 와 --print 동일
$ claude -p "..."
$ claude --print "..."

# 5. 표준입력과 함께
$ git diff | claude -p "이 변경의 위험도 평가"
# stdin이 있으면 그것을 컨텍스트로 사용

# 6. 표준입력과 -p 동시
$ git log --oneline -20 | claude -p \
    "이 커밋 목록을 분류해 줘"

# 주의: 대화형에서는 stdin 사용 못 함
# Claude가 사용자 입력으로 stdin을 기대하기 때문
```

## Speaker Notes

동작 모드 옵션을 자세히 살펴봅니다.
-p 또는 --print 플래그 유무가 핵심 차이입니다.
인자 없이 claude만 실행하면 대화형 세션이 시작됩니다.
사용자가 /exit으로 종료할 때까지 계속됩니다.
-p와 프롬프트를 함께 전달하면 Headless 단일 응답 모드입니다.
응답이 끝나면 자동 종료됩니다.
추가 대화는 불가능합니다.
Headless에서도 다회 도구 호출이 가능합니다.
README 읽기와 SUMMARY 쓰기 같은 다단계 작업이 한 호출에서 모두 수행됩니다.
-p와 --print는 동일한 플래그입니다.
stdin을 함께 사용할 수도 있습니다.
git diff 출력을 pipe로 전달하면 그것을 컨텍스트로 사용합니다.
주의할 점은 대화형에서는 stdin을 사용할 수 없다는 것입니다.
Claude가 사용자 입력으로 stdin을 기대하기 때문입니다.
