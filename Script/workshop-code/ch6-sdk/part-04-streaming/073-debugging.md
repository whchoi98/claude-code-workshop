# Slide 73: 스트림 디버깅

**Part 4: STREAMING**

## Code Blocks

### debugging

```python
# 1. 이벤트 로깅
import json
import logging

logger = logging.getLogger("stream")

async def log_stream_events(stream):
    event_counts = {}
    start = time.time()

    async for event in stream:
        # 이벤트별 카운트
        event_counts[event.type] = event_counts.get(event.type, 0) + 1

        # 상세 로그 (개발 시)
        logger.debug(json.dumps({
            "event": event.type,
            "elapsed_ms": int((time.time() - start) * 1000),
        }))

        yield event

    # 종료 후 통계
    logger.info(f"Stream completed: {event_counts}, "
                f"{int((time.time() - start) * 1000)}ms")

# 2. 첫 토큰 시간 (TTFT) 측정
async def measure_ttft(stream):
    start = time.time()
    first_token_time = None

    async for event in stream:
        if event.type == "content_block_delta":
            if event.delta.type == "text_delta":
                if first_token_time is None:
                    first_token_time = time.time()
                    ttft_ms = int((first_token_time - start) * 1000)
                    print(f"TTFT: {ttft_ms}ms")
        yield event

# 3. 토큰 처리 속도 (tokens/second)
async def measure_throughput(stream):
    token_count = 0
    first_token_time = None

    async for event in stream:
        if event.type == "content_block_delta":
            if event.delta.type == "text_delta":
                token_count += 1    # 근사치
                if first_token_time is None:
                    first_token_time = time.time()
        yield event

    if first_token_time:
        elapsed = time.time() - first_token_time
        tps = token_count / elapsed if elapsed > 0 else 0
        print(f"~{tps:.1f} tokens/s")

# 4. CloudWatch / Datadog 메트릭
def send_metric(name, value):
    cloudwatch.put_metric_data(
        Namespace="ClaudeStream",
        MetricData=[{
            "MetricName": name,
            "Value": value,
            "Timestamp": datetime.utcnow(),
        }]
    )

# 사용
async def monitored_stream(prompt):
    async with client.messages.stream(...) as stream:
        wrapped = measure_ttft(measure_throughput(stream))
        async for event in wrapped:
            # ... 정상 처리 ...
            pass
```

## Speaker Notes

스트림 디버깅을 위한 관측과 로깅 패턴입니다.
1번 이벤트 로깅은 각 이벤트의 타입과 elapsed 시간을 기록합니다.
log_stream_events는 generator 함수로 yield 패턴을 사용해 원본 스트림을 wrapping합니다.
event_counts에 타입별 발생 횟수를 누적하고 종료 후 통계를 출력합니다.
2번 TTFT 즉 Time To First Token 측정이 중요합니다.
사용자 경험 메트릭의 핵심입니다.
첫 text_delta 이벤트의 시간을 기록해 응답 시작까지의 지연을 측정합니다.
일반적으로 300에서 800 밀리초가 기대됩니다.
3번 토큰 처리 속도는 tokens per second로 측정합니다.
delta 이벤트 카운트를 elapsed로 나눠 계산합니다.
Sonnet은 약 50 tokens/s, Haiku는 100 tokens/s 정도입니다.
4번 CloudWatch나 Datadog로 메트릭 전송이 운영에 필수입니다.
send_metric 함수로 TTFT와 throughput을 외부 모니터링에 보냅니다.
monitored_stream에서 wrapping function을 중첩해 여러 측정을 동시에 합니다.
대시보드에서 추세를 보고 성능 회귀를 즉시 감지할 수 있습니다.
