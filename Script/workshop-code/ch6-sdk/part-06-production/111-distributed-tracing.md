# Slide 111: 분산 트레이싱

**Part 6: PRODUCTION 운영**

## Code Blocks

### tracing

```python
# 1. OpenTelemetry 설치
# pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(OTLPSpanExporter(endpoint="http://otel:4317"))
)
tracer = trace.get_tracer("claude-app")

# 2. Claude 호출 트레이싱
def call_claude_traced(user_id, prompt):
    with tracer.start_as_current_span("claude_call") as span:
        span.set_attribute("user.id", user_id)
        span.set_attribute("prompt.length", len(prompt))

        try:
            with tracer.start_as_current_span("messages.create") as api_span:
                response = client.messages.create(
                    model="claude-sonnet-4-5",
                    max_tokens=1024,
                    messages=[{"role": "user", "content": prompt}],
                )
                api_span.set_attribute("model", response.model)
                api_span.set_attribute("input_tokens", response.usage.input_tokens)
                api_span.set_attribute("output_tokens", response.usage.output_tokens)

            with tracer.start_as_current_span("postprocess"):
                result = process_response(response)

            span.set_status(trace.Status(trace.StatusCode.OK))
            return result
        except Exception as e:
            span.record_exception(e)
            span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))
            raise

# 3. 트레이스 컨텍스트 전파 (자동)
# HTTP 호출 시 trace-id가 헤더에 자동 전파
# 마이크로서비스 간 호출 추적 가능

# 4. Sentry / Jaeger UI
# - 호출 흐름 시각화
# - 어디서 오래 걸리는지 빠르게 파악
# - 에러 발생 위치 추적

# 5. 비용 효율 sampling (1% 일반, 100% 에러)
from opentelemetry.sdk.trace.sampling import (
    ParentBased, TraceIdRatioBased,
)
sampler = ParentBased(root=TraceIdRatioBased(0.01))
trace.set_tracer_provider(TracerProvider(sampler=sampler))
```

## Speaker Notes

분산 트레이싱은 OpenTelemetry를 사용합니다.
1번 OpenTelemetry 설치와 설정입니다.
opentelemetry-api, sdk, exporter-otlp 세 패키지를 설치합니다.
TracerProvider를 설정하고 BatchSpanProcessor로 OTLP exporter를 연결합니다.
endpoint는 사내 OTel collector의 gRPC 주소입니다.
2번 Claude 호출 트레이싱은 with tracer.start_as_current_span으로 합니다.
claude_call이라는 부모 span을 시작합니다.
user.id와 prompt.length 같은 속성을 설정합니다.
내부에 messages.create span을 중첩해 API 호출만 측정합니다.
response 정보를 속성으로 추가합니다.
postprocess span으로 응답 후처리 시간을 별도 추적합니다.
성공 시 OK status, 실패 시 ERROR status와 예외를 기록합니다.
3번 트레이스 컨텍스트 전파는 자동입니다.
HTTP 호출 시 trace-id가 헤더에 자동 전파되어 마이크로서비스 간 호출이 한 트레이스로 연결됩니다.
4번 Sentry나 Jaeger UI로 시각화하면 호출 흐름과 병목, 에러를 즉시 파악할 수 있습니다.
5번 비용 효율적 sampling이 중요합니다.
100 퍼센트 트레이싱은 비용이 큽니다.
일반 호출은 1 퍼센트, 에러는 100 퍼센트 sampling이 일반적입니다.
