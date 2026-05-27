# Slide 125: 에이전트 간 통신

**Part 7: 고급 패턴**

## Code Blocks

### communication

```python
# 1. Shared state (Redis)
import redis, json
from anthropic import AsyncAnthropic

r = redis.Redis(decode_responses=True)
client = AsyncAnthropic()

async def agent_writer(session_id: str, task: str):
    """Agent 1: 작성"""
    response = await client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        messages=[{"role": "user", "content": f"작성: {task}"}],
    )
    draft = response.content[0].text
    r.set(f"session:{session_id}:draft", draft)
    r.set(f"session:{session_id}:status", "writer_done")
    return draft

async def agent_critic(session_id: str):
    """Agent 2: 검토"""
    # 다른 agent의 결과 가져오기
    draft = r.get(f"session:{session_id}:draft")

    response = await client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system="당신은 비평 전문가입니다. 개선점 3가지를 지적하세요.",
        messages=[{"role": "user", "content": draft}],
    )
    feedback = response.content[0].text
    r.set(f"session:{session_id}:feedback", feedback)
    r.set(f"session:{session_id}:status", "critic_done")
    return feedback

# 2. Pub/Sub으로 이벤트
def publish_event(channel: str, event: dict):
    r.publish(channel, json.dumps(event))

async def coordinator():
    """다른 agent의 이벤트를 구독"""
    pubsub = r.pubsub()
    pubsub.subscribe("agent_events")

    for message in pubsub.listen():
        if message["type"] != "message": continue
        event = json.loads(message["data"])
        if event["type"] == "task_complete":
            # 다음 단계 시작
            handle_task_complete(event)

# 3. Message Queue (Celery)
from celery import Celery
app = Celery("agents", broker="redis://localhost:6379")

@app.task
def run_writer_agent(session_id, task):
    # ... agent_writer 로직 ...
    pass

@app.task
def run_critic_agent(session_id):
    # ... agent_critic 로직 ...
    pass

# 사용 (chain으로 순차 실행)
from celery import chain
result = chain(
    run_writer_agent.s("sess_1", "한국 음식 소개 글"),
    run_critic_agent.s("sess_1"),
).apply_async()

# 4. 직접 SDK 호출 chain (단순)
async def multi_agent_chain(session_id, task):
    draft = await agent_writer(session_id, task)
    feedback = await agent_critic(session_id)

    # 피드백을 반영한 재작성
    final = await client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        messages=[{
            "role": "user",
            "content": f"원본:\n{draft}\n\n피드백:\n{feedback}\n\n수정 작성",
        }],
    )
    return final.content[0].text
```

## Speaker Notes

에이전트 간 통신 패턴입니다.
첫째, Shared state를 Redis로 구현합니다.
각 에이전트는 자기 결과를 session 키 아래 저장합니다.
다른 에이전트는 r.get으로 결과를 읽어 사용합니다.
status 키로 진행 상황도 함께 추적합니다.
둘째, Pub/Sub으로 이벤트 기반 통신을 합니다.
publish_event 함수로 채널에 이벤트를 발행합니다.
coordinator는 채널을 구독하고 이벤트 타입에 따라 다음 단계를 시작합니다.
비동기 협업이 가능합니다.
셋째, Message Queue로 Celery를 사용합니다.
각 에이전트를 Celery task로 정의하면 분산 환경에서 처리 가능합니다.
chain으로 순차 실행을 만들 수 있습니다.
넷째, 단순한 경우는 직접 SDK 호출 chain입니다.
multi_agent_chain 함수에서 writer 호출, critic 호출, 피드백 반영 재작성을 순차 진행합니다.
작은 협업은 이 방식이 가장 단순하고 디버깅이 쉽습니다.
대규모는 Celery 같은 큐 시스템을 사용합니다.
복잡도와 규모에 맞는 패턴을 선택하시기 바랍니다.
