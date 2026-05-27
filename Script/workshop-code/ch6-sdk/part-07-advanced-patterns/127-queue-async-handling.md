# Slide 127: 큐 기반 비동기 처리

**Part 7: 고급 패턴**

## Code Blocks

### queue patterns

```python
# 시나리오: 큰 작업을 사용자에게 즉시 응답하고 백그라운드에서 처리

# 1. FastAPI + Celery 패턴
from fastapi import FastAPI, BackgroundTasks
from tasks import analyze_document

app = FastAPI()

# 동기 API: 즉시 응답, 백그라운드에서 처리
@app.post("/analyze")
async def submit_analysis(doc_id: int):
    task = analyze_document.delay(doc_id)
    return {
        "task_id": task.id,
        "status": "queued",
        "check_url": f"/tasks/{task.id}",
    }

# 진행 상황 확인 endpoint
@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    from celery.result import AsyncResult
    result = AsyncResult(task_id)

    return {
        "task_id": task_id,
        "status": result.status,
        "info": result.info,
        "result": result.result if result.ready() else None,
    }

# 2. 우선순위 큐 (다중 worker)
# routes.py - task별 큐 라우팅
app.conf.task_routes = {
    "tasks.critical_*": {"queue": "high"},
    "tasks.normal_*":   {"queue": "default"},
    "tasks.bulk_*":     {"queue": "low"},
}

# Worker 시작 (queue별)
# $ celery -A tasks worker -Q high -c 8       # 우선순위 큐
# $ celery -A tasks worker -Q default -c 4
# $ celery -A tasks worker -Q low -c 2        # 배치 처리

# 3. Rate limit이 있는 task
@app.task(rate_limit="10/m")    # 분당 10개
def expensive_claude_call(prompt):
    return client.messages.create(...)

# 4. Chord 패턴 (병렬 후 합산)
from celery import chord

job = chord(
    [analyze_document.s(id) for id in doc_ids],  # 병렬
    summarize_results.s()                          # 종합
)
result = job.apply_async()

# 5. Webhook으로 완료 알림
@app.task
def analyze_and_notify(doc_id, callback_url):
    result = perform_analysis(doc_id)
    requests.post(callback_url, json={
        "doc_id": doc_id,
        "result": result,
    })

# 사용자 측 (curl 또는 fetch)
# POST /analyze {doc_id: 123, callback_url: "https://..."}
# 즉시 응답: task_id
# 처리 완료 후 webhook으로 결과 전송
```

## Speaker Notes

큐 기반 비동기 처리로 사용자 응답과 분리합니다.
FastAPI와 Celery 패턴이 표준입니다.
동기 API submit_analysis는 task.delay로 큐에 등록만 하고 task_id를 즉시 반환합니다.
status queued와 check_url을 함께 응답해 클라이언트가 추적 가능하게 합니다.
get_task_status endpoint에서 AsyncResult로 진행 상황을 조회합니다.
status, info, result를 모두 반환합니다.
우선순위 큐는 task_routes로 정의합니다.
critical은 high 큐, normal은 default 큐, bulk는 low 큐로 라우팅합니다.
Worker도 -Q 옵션으로 특정 큐만 처리하게 시작합니다.
high 큐는 concurrency 8로 빠르게 처리하고 low 큐는 2로 천천히 처리합니다.
Rate limit이 있는 task는 rate_limit 옵션을 명시합니다.
분당 10개로 제한해 Anthropic rate limit 도달을 방지합니다.
Chord 패턴은 병렬 후 합산입니다.
여러 task를 병렬로 실행하고 모두 완료되면 summary task가 실행됩니다.
Webhook으로 완료 알림하는 패턴도 일반적입니다.
analyze_and_notify task가 처리 완료 후 callback_url로 결과를 POST합니다.
사용자는 polling 없이 결과를 받을 수 있습니다.
