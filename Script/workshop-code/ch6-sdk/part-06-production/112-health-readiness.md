# Slide 112: 헬스체크와 readiness

**Part 6: PRODUCTION 운영**

## Code Blocks

### health check

```python
# 1. FastAPI 엔드포인트
from fastapi import FastAPI, HTTPException

app = FastAPI()

# /health: liveness probe (간단, <50ms)
@app.get("/health")
async def health():
    return {"status": "ok"}

# /ready: readiness probe (의존성 확인, <1s)
@app.get("/ready")
async def ready():
    checks = {}

    # Anthropic API 응답 확인 (tiny 호출)
    try:
        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=10,
            messages=[{"role": "user", "content": "ping"}],
            timeout=5.0,
        )
        checks["anthropic"] = "ok"
    except Exception as e:
        checks["anthropic"] = f"fail: {e}"

    # DB와 Redis
    try:
        db.execute("SELECT 1")
        checks["database"] = "ok"
    except Exception as e:
        checks["database"] = f"fail: {e}"

    try:
        redis_client.ping()
        checks["redis"] = "ok"
    except Exception as e:
        checks["redis"] = f"fail: {e}"

    if all(v == "ok" for v in checks.values()):
        return {"status": "ready", "checks": checks}
    raise HTTPException(status_code=503, detail={
        "status": "not_ready", "checks": checks,
    })

# 2. K8s probe 설정 (deployment.yaml)
# livenessProbe:
#   httpGet: {path: /health, port: 8000}
#   initialDelaySeconds: 10
#   periodSeconds: 30
# readinessProbe:
#   httpGet: {path: /ready, port: 8000}
#   initialDelaySeconds: 5
#   periodSeconds: 10
#   timeoutSeconds: 10

# 3. ALB health check (AWS)
# 30초 간격, 2회 실패 시 unhealthy
# Auto-scaling 결정에 사용

# 4. Anthropic 상태 페이지 통합
import requests
def check_anthropic_status():
    r = requests.get("https://status.anthropic.com/api/v2/status.json",
                     timeout=5)
    return r.json()["status"]["indicator"] == "none"
```

## Speaker Notes

헬스체크와 readiness 패턴입니다.
FastAPI에서 두 엔드포인트를 분리합니다.
/health는 liveness probe로 간단합니다.
status ok만 반환하는 50밀리초 미만 응답입니다.
/ready는 readiness probe로 의존성을 확인합니다.
Anthropic API, database, redis 같은 외부 의존성을 점검합니다.
Anthropic API 확인은 가장 작은 모델 Haiku로 tiny 호출을 합니다.
max_tokens 10으로 비용을 최소화합니다.
모든 체크 통과해야 ready 응답이고 하나라도 실패 시 503 not_ready를 반환합니다.
K8s probe 설정 예시입니다.
livenessProbe는 30초 간격으로 /health를 호출합니다.
readinessProbe는 10초 간격으로 /ready를 호출합니다.
timeoutSeconds 차이로 readiness가 더 긴 응답을 허용합니다.
ALB나 ELB health check도 동일한 패턴입니다.
2회 실패 시 unhealthy 표시되고 Auto-scaling 결정에 사용됩니다.
Anthropic API 자체 상태 확인은 status.anthropic.com을 활용합니다.
incidents 발생 시 우리 readiness도 false로 만들어 traffic을 차단할 수 있습니다.
