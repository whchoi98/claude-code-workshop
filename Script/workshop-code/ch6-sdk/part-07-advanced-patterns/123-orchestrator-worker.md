# Slide 123: Orchestrator-Worker 패턴

**Part 7: 고급 패턴**

## Code Blocks

### orchestrator

```python
# orchestrator.py
from anthropic import AsyncAnthropic
import asyncio, json

client = AsyncAnthropic()

# Orchestrator: 작업 분할
async def plan_tasks(user_request: str) -> list:
    response = await client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system="""당신은 작업 분할 전문가입니다.
        사용자 요청을 분석해 병렬 처리 가능한 sub-task들로 나누세요.
        응답은 JSON 배열: [{"id": int, "description": str}]""",
        messages=[{"role": "user", "content": user_request}],
    )
    text = response.content[0].text
    # JSON 추출
    start = text.find("[")
    end = text.rfind("]") + 1
    return json.loads(text[start:end])

# Worker: 개별 작업 수행
async def execute_task(task: dict) -> dict:
    response = await client.messages.create(
        model="claude-haiku-4-5",   # worker는 저비용 모델
        max_tokens=1024,
        system="당신은 task 실행 전문가입니다. 정확하고 간결하게.",
        messages=[{
            "role": "user",
            "content": f"Task {task['id']}: {task['description']}"
        }],
    )
    return {
        "id": task["id"],
        "description": task["description"],
        "result": response.content[0].text,
    }

# Synthesizer: 결과 종합
async def synthesize_results(user_request: str, results: list) -> str:
    response = await client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        system="""당신은 결과 종합 전문가입니다.
        여러 sub-task 결과를 받아 사용자에게 통합 응답을 작성합니다.""",
        messages=[{
            "role": "user",
            "content": f"""원 요청: {user_request}

Sub-task 결과들:
{json.dumps(results, ensure_ascii=False, indent=2)}

종합 응답을 작성해 주세요."""
        }],
    )
    return response.content[0].text

# 메인 흐름
async def orchestrate(user_request: str) -> str:
    # 1. 계획
    tasks = await plan_tasks(user_request)
    print(f"Plan: {len(tasks)} tasks")

    # 2. 병렬 실행
    results = await asyncio.gather(*[execute_task(t) for t in tasks])

    # 3. 종합
    final = await synthesize_results(user_request, results)
    return final

# 사용
result = asyncio.run(orchestrate(
    "한국 IT 산업 트렌드를 5가지 관점에서 분석해 주세요"
))
```

## Speaker Notes

Orchestrator-Worker 패턴은 계획과 실행을 분리합니다.
plan_tasks 함수가 Orchestrator 역할입니다.
Sonnet 모델로 사용자 요청을 받아 병렬 처리 가능한 sub-task들로 분할합니다.
JSON 배열 형식으로 응답을 받아 파싱합니다.
execute_task 함수는 Worker 역할입니다.
Haiku 모델로 비용을 절감하면서 개별 task를 수행합니다.
각 worker는 자기 task에만 집중합니다.
synthesize_results는 Synthesizer 역할입니다.
Sonnet 모델로 원 요청과 모든 sub-task 결과를 받아 통합 응답을 작성합니다.
orchestrate 함수가 전체 흐름을 조정합니다.
plan_tasks로 작업 분할, asyncio.gather로 모든 worker 병렬 실행, synthesize_results로 종합 응답 생성입니다.
사용 예시는 한국 IT 산업 트렌드 5가지 관점 분석 같은 복합 요청입니다.
5가지 관점을 5개 worker가 동시에 분석한 후 종합되어 더 깊이있고 빠른 응답이 됩니다.
Orchestrator가 비용 큰 Sonnet, Worker가 저비용 Haiku로 비용도 최적화됩니다.
