# Slide 35: Client Layer - Agent SDK

**Part 2: ARCHITECTURE**

## Code Blocks

### PYTHON SDK

```python
# Python SDK 예시
from claude_agent_sdk import ClaudeAgent

agent = ClaudeAgent(
    cwd="/path/to/repo",
    allowed_tools=["Read", "Edit", "Bash"],
    model="claude-sonnet-4-5",
)

result = agent.run(
    "사용자 모델에 deleted_at 컬럼을 추가하고 마이그레이션을 생성해 주세요."
)

print(result.summary)
print(result.modified_files)
```

## Speaker Notes

세 번째 클라이언트 계층은 Agent SDK입니다.
Claude Code의 모든 기능을 Python 또는 TypeScript 코드에서 프로그래매틱하게 호출할 수 있게 해 줍니다.
화면 코드는 Python SDK 예시입니다.
ClaudeAgent 객체를 만들 때 작업 디렉토리, 허용 도구 목록, 사용할 모델을 지정합니다.
그 후 run 메서드에 자연어 명령을 전달하면 Claude Code와 동일하게 자율 작업을 수행하고, 결과로 변경된 파일 목록과 요약을 받을 수 있습니다.
비동기 호출과 스트리밍 응답을 지원하므로 백엔드 서비스나 자동화 파이프라인에 통합하기 좋습니다.
Chapter 6에서 SDK 전체를 자세히 다룹니다.
