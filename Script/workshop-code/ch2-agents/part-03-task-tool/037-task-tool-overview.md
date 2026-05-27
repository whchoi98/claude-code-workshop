# Slide 37: Task tool overview

**Part 3: TASK 도구와 디스패치**

## Code Blocks

### Task call

```bash
# Task 호출 형식 (메인의 tool_use 블록)
Task(
  subagent_type="code-reviewer",
  description="Review the recent commit",
  prompt="""
  최근 커밋 ${SHA}의 변경사항을 검토해 주세요.
  특히 인증 관련 변경에 주목하세요.
  
  관련 파일:
  - src/auth/middleware.js
  - src/auth/jwt.js
  """
)

# 반환 형식 (Subagent의 결과)
{ "summary": "...", "issues": [...], "tokens_used": 5234 }
```

## Speaker Notes

Task 도구의 전체 개요를 살펴봅니다.
Task는 메인 에이전트가 Subagent를 호출하는 유일한 메커니즘입니다.
호출 시 세 가지 핵심 인자를 전달합니다.
subagent_type은 호출할 Subagent의 name 필드 값입니다.
description은 작업의 짧은 라벨로 로그나 UI에 표시됩니다.
prompt는 Subagent에게 전달할 실제 지시 내용입니다.
Subagent의 시스템 프롬프트는 자동 적용되므로 prompt에는 작업 컨텍스트만 적으면 됩니다.
Subagent 실행이 끝나면 결과가 메인에 반환됩니다.
반환 형식은 summary와 issues 같은 구조화된 결과, 그리고 사용된 토큰 수 등의 메타데이터를 포함합니다.
이 결과를 메인이 받아 사용자에게 보고하거나 다음 작업으로 이어갑니다.
