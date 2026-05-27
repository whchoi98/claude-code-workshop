# Slide 38: Auto dispatch

**Part 3: TASK 도구와 디스패치**

## Code Blocks

### auto dispatch

```bash
# 사용자 요청
> 최근 PR의 보안 이슈를 점검해 줘.

# 메인의 자동 디스패치 (사용자가 별도 지정 안 함)
- 모든 Subagent의 description 검토
- "보안" 키워드가 description에 있는 security-scanner 선택
- Task(subagent_type="security-scanner", ...)
- 사용자는 어떤 에이전트가 호출되었는지 결과와 함께 안내받음

# 잘 작동하려면
- description이 구체적이고 사용 시점 명시
- 에이전트끼리 description 영역이 명확히 구분됨
```

## Speaker Notes

자동 디스패치 메커니즘을 살펴봅니다.
4단계 흐름으로 동작합니다.
첫째, 사용자 요청을 메인이 수신합니다.
둘째, 메인이 모든 등록된 Subagent의 description을 검색합니다.
셋째, 가장 적합한 Subagent를 선택합니다.
넷째, Task 도구를 통해 자동으로 호출합니다.
예시로 사용자가 최근 PR의 보안 이슈를 점검해 달라고 요청한 상황입니다.
메인은 모든 Subagent의 description을 검토하고 보안 키워드가 있는 security-scanner를 자동 선택합니다.
Task 도구로 호출하고 결과를 받아 사용자에게 보고합니다.
사용자는 어떤 에이전트가 호출되었는지 결과와 함께 안내받습니다.
자동 디스패치가 잘 작동하려면 두 가지가 중요합니다.
description이 구체적이고 사용 시점이 명시되어야 합니다.
에이전트끼리 description 영역이 명확히 구분되어야 합니다.
