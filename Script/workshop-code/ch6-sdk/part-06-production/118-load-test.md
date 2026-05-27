# Slide 118: 부하 테스트

**Part 6: PRODUCTION 운영**

## Code Blocks

### load test

```python
# locustfile.py - Claude API 부하 테스트
from locust import HttpUser, task, between
import random

class ClaudeAppUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.prompts = [
            "Python list comprehension 설명",
            "JavaScript 비동기 처리",
            "Rust ownership 개념",
            "Go의 goroutine",
        ]

    @task(10)
    def chat_call(self):
        prompt = random.choice(self.prompts)
        with self.client.post(
            "/chat",
            json={"prompt": prompt},
            timeout=60,
            catch_response=True,
            name="POST /chat",
        ) as response:
            if response.status_code == 200:
                response.success()
                data = response.json()
                if data.get("usage", {}).get("output_tokens", 0) < 10:
                    response.failure("Response too short")
            elif response.status_code == 429:
                response.failure("Rate limited")
            else:
                response.failure(f"Status {response.status_code}")

    @task(1)
    def stream_call(self):
        with self.client.post(
            "/chat/stream",
            json={"prompt": "Write a haiku"},
            stream=True,
            timeout=60,
            catch_response=True,
            name="POST /chat/stream",
        ) as response:
            chunks = sum(1 for line in response.iter_lines()
                         if line.startswith(b"data: "))
            if chunks > 0:
                response.success()
            else:
                response.failure("No chunks")

# 실행
# $ locust -f locustfile.py --host=http://localhost:8000
# Web UI: http://localhost:8089
# Headless: --users 10 --spawn-rate 1 --run-time 5m --headless

# 성능 목표
# - p95 latency < 5초
# - 에러율 < 1%
# - throughput 10 RPS 유지
# - 50명 동시 사용자 처리

# 결과 분석
# - rate limit 도달 빈도
# - 에러별 발생률
# - 응답 시간 분포 (p50, p95, p99)
# - 비용 추정 (분당 호출 * 평균 비용)
```

## Speaker Notes

부하 테스트는 Locust 도구를 사용합니다.
locustfile.py에 HttpUser 클래스를 정의합니다.
wait_time을 1-3초 사이 랜덤으로 두어 실제 사용자처럼 시뮬레이션합니다.
on_start에서 각 사용자 시작 시 prompt 목록을 준비합니다.
@task 데코레이터로 부하 패턴을 정의합니다.
chat_call은 가중치 10으로 일반 호출, stream_call은 가중치 1로 스트리밍 호출입니다.
10대 1 비율로 호출됩니다.
catch_response=True로 응답을 분석할 수 있습니다.
200 응답은 success, 429는 rate limit failure로 분류합니다.
output_tokens가 10 미만이면 응답이 너무 짧다고 failure로 처리합니다.
stream_call은 stream=True로 청크 단위 응답을 받습니다.
청크 수를 카운트하고 0보다 크면 success입니다.
실행은 locust -f locustfile.py로 Web UI에서 인터랙티브하게 진행하거나 headless 모드로 자동화할 수 있습니다.
성능 목표 4가지를 정의합니다.
p95 latency 5초 미만, 에러율 1퍼센트 미만, throughput 10 RPS 유지, 50명 동시 사용자 처리입니다.
부하 테스트 결과로 rate limit 도달, 에러 분포, 응답 시간 분포, 비용 추정을 분석합니다.
프로덕션 배포 전 capacity 검증에 필수입니다.
