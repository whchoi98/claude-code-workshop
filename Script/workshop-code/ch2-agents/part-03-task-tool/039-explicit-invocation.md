# Slide 39: Explicit invocation

**Part 3: TASK 도구와 디스패치**

## Code Blocks

### explicit calls

```bash
# 방법 1: 자연어로 지정
> code-reviewer 에이전트를 사용해서 이 PR을 검토해 줘.

> security-scanner로 의존성 취약점을 검사해 줘.

# 방법 2: /agents 슬래시 명령으로 목록 확인 후 선택
> /agents
Available agents:
  - code-reviewer
  - test-writer
  - security-scanner
  - docs-writer

> code-reviewer 사용

# 방법 3: 메인 프롬프트에서 직접 지시
> [Use code-reviewer subagent]
> 최근 commit을 리뷰해 줘.
```

## Speaker Notes

명시적 호출 방법을 살펴봅니다.
3가지 방법이 있습니다.
첫 번째 방법은 자연어로 지정하는 것입니다.
code-reviewer 에이전트를 사용해서 이 PR을 검토해 달라는 식으로 에이전트 이름을 직접 언급합니다.
두 번째 방법은 슬래시 명령 /agents로 등록된 에이전트 목록을 먼저 확인하는 것입니다.
프로젝트와 사용자 디렉토리에서 모든 등록된 에이전트가 표시됩니다.
원하는 이름을 선택해 사용한다고 말합니다.
세 번째 방법은 메인 프롬프트에서 직접 지시하는 것입니다.
Use code-reviewer subagent 같은 명시적 키워드로 메인에게 강제할 수 있습니다.
명시적 호출은 자동 디스패치보다 우선합니다.
예측 가능한 동작이 필요할 때 사용합니다.
