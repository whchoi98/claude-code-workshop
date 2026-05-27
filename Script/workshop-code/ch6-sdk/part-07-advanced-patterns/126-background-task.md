# Slide 126: 백그라운드 작업

**Part 7: 고급 패턴**

## Code Blocks

### celery

```python
# 1. Celery 설정
# pip install celery[redis]

# tasks.py
from celery import Celery
from anthropic import Anthropic

app = Celery("claude_tasks", broker="redis://localhost:6379/0",
             backend="redis://localhost:6379/1")

@app.task(bind=True, max_retries=3)
def analyze_document(self, document_id: int):
    try:
        client = Anthropic()
        doc = fetch_document(document_id)

        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2048,
            messages=[{"role": "user", "content": f"분석: {doc}"}],
        )

        save_analysis(document_id, response.content[0].text)
        return {"id": document_id, "status": "done"}

    except Exception as e:
        # Celery 자동 재시도
        raise self.retry(exc=e, countdown=60 * (2 ** self.request.retries))

# 2. 호출 (즉시 반환, 백그라운드 실행)
result = analyze_document.delay(doc_id=123)
# result.id = task ID
# result.get(timeout=60) = 결과 대기 (blocking)
# result.status = "PENDING" | "STARTED" | "SUCCESS" | "FAILURE"

# 3. Worker 실행
# $ celery -A tasks worker --loglevel=info --concurrency=4

# 4. 진행 상황 추적
@app.task(bind=True)
def long_analysis(self, doc_ids: list):
    total = len(doc_ids)
    for i, doc_id in enumerate(doc_ids):
        # 진행률 업데이트
        self.update_state(
            state="PROGRESS",
            meta={"current": i, "total": total, "percent": i*100//total},
        )
        analyze_one(doc_id)

    return {"status": "done", "count": total}

# 클라이언트에서 진행률 확인
task = long_analysis.delay([1, 2, 3, ..., 100])
while not task.ready():
    info = task.info or {}
    print(f"Progress: {info.get('percent', 0)}%")
    time.sleep(2)

# 5. 스케줄링 (Celery Beat)
from celery.schedules import crontab

app.conf.beat_schedule = {
    "daily-report": {
        "task": "tasks.generate_daily_report",
        "schedule": crontab(hour=9, minute=0),   # 매일 오전 9시
    },
    "every-5-min": {
        "task": "tasks.health_check",
        "schedule": 300.0,   # 5분마다
    },
}

# 시작: celery -A tasks beat
```

## Speaker Notes

백그라운드 작업은 Celery와 Redis Queue로 구현합니다.
Celery 설정에 broker와 backend를 redis로 명시합니다.
@app.task 데코레이터로 함수를 task로 등록합니다.
bind=True로 self 접근이 가능해지고 max_retries=3으로 자동 재시도 횟수를 명시합니다.
analyze_document task에서 예외 발생 시 self.retry로 exponential backoff와 함께 재시도합니다.
호출은 .delay() 메서드로 즉시 반환됩니다.
실제 처리는 worker에서 백그라운드로 수행됩니다.
result.get(timeout=60)으로 결과를 대기하거나 result.status로 현재 상태를 확인할 수 있습니다.
Worker는 celery -A tasks worker 명령으로 실행합니다.
concurrency 4로 동시 4개 task를 처리할 수 있습니다.
진행 상황 추적은 self.update_state로 합니다.
PROGRESS 상태와 함께 current, total, percent를 meta로 전달합니다.
클라이언트에서 task.info로 진행률을 실시간 확인할 수 있습니다.
스케줄링은 Celery Beat을 사용합니다.
beat_schedule에 crontab 또는 초 단위 간격으로 정기 task를 정의합니다.
매일 오전 9시 보고서나 5분마다 헬스체크 같은 패턴이 일반적입니다.
