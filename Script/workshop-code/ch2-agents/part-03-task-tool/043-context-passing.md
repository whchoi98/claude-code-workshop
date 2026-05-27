# Slide 43: Context passing

**Part 3: TASK 도구와 디스패치**

## Code Blocks

### context pass

```bash
# Subagent는 메인 컨텍스트를 자동으로 받지 않음
# 필요한 정보를 prompt에 명시적으로 담아 전달해야 함

# 좋은 예시 (충분한 컨텍스트)
Task(
  subagent_type="code-reviewer",
  prompt=f"""
  작업: 다음 PR diff를 검토해 주세요.
  
  변경 요약: 사용자 인증 미들웨어에 JWT 검증 추가
  관련 파일: src/auth/middleware.js, tests/auth.test.js
  
  PR diff:
  ${diff_content}
  
  특별 주의 사항: HS256 vs RS256 알고리즘 선택 적절성
  """
)

# 피해야 할 예시 (정보 부족)
Task(subagent_type="code-reviewer", prompt="PR 리뷰해 줘")
```

## Speaker Notes

Subagent에 컨텍스트를 전달하는 방법을 설명합니다.
중요한 점은 Subagent가 메인 컨텍스트를 자동으로 받지 않는다는 것입니다.
메인이 prompt에 필요한 정보를 명시적으로 담아 전달해야 합니다.
좋은 예시를 보면 작업 목표, 변경 요약, 관련 파일 목록, 실제 diff 내용, 특별 주의 사항을 모두 포함합니다.
Subagent는 이 정보만으로 충분히 작업을 수행할 수 있습니다.
반면 피해야 할 예시는 PR 리뷰해 달라는 한 줄짜리 prompt입니다.
Subagent는 어떤 PR인지 알 수 없으므로 추측이나 오류가 발생합니다.
핵심 원칙은 Subagent가 처음 일을 시작하는 사람처럼 모든 정보가 필요하다는 것입니다.
메인의 대화 이력은 따라가지 않으니 명시적으로 전달하시기 바랍니다.
