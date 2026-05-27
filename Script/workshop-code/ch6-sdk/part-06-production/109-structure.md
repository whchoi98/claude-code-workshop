# Slide 109: 구조화 로깅

**Part 6: PRODUCTION 운영**

## Code Blocks

### logging

```python
# 1. structlog 설정
import structlog, logging

structlog.configure(
    processors=[
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.dict_tracebacks,
        structlog.processors.JSONRenderer(),
    ],
)

logger = structlog.get_logger()
logger = logger.bind(service="claude-api", env="production")

# 2. 호출 로깅
def call_claude(user_id, prompt):
    request_id = generate_request_id()
    log = logger.bind(user_id=user_id, request_id=request_id)
    log.info("claude_call_start", prompt_length=len(prompt))

    start = time.time()
    try:
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        )
        log.info("claude_call_success",
            model=response.model,
            stop_reason=response.stop_reason,
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            duration_ms=int((time.time() - start) * 1000),
        )
        return response
    except Exception as e:
        log.error("claude_call_failure",
            error_type=type(e).__name__,
            error_message=str(e),
        )
        raise

# 3. 출력 예시 (JSON 한 줄)
# {"event":"claude_call_success","level":"info",
#  "timestamp":"2026-05-25T10:30:00Z",
#  "user_id":"user_1","request_id":"req_xyz",
#  "model":"claude-sonnet-4-5","stop_reason":"end_turn",
#  "input_tokens":120,"output_tokens":450,"duration_ms":2350}

# 4. 로그 분석 (jq)
# 평균 응답 시간
$ cat app.log | jq -s 'map(.duration_ms) | add / length'

# 에러율
$ cat app.log | jq -rs '[.[] | select(.level == "error")] | length'

# 5. PII 마스킹
import re
def mask_pii(text):
    text = re.sub(r'[\w.-]+@[\w.-]+', '[EMAIL]', text)
    text = re.sub(r'\b\d{3}-\d{4}-\d{4}\b', '[PHONE]', text)
    return text

log.info("call_start", prompt_masked=mask_pii(prompt))
```

## Speaker Notes

구조화 로깅은 운영의 핵심입니다.
structlog 라이브러리로 JSON 형식 로그를 생성합니다.
processors 체인으로 log_level, TimeStamper, JSONRenderer를 연결합니다.
logger.bind로 service와 env 같은 글로벌 컨텍스트를 추가합니다.
call_claude 함수에서 user_id와 request_id를 bind한 새 log를 만듭니다.
claude_call_start, claude_call_success, claude_call_failure 이벤트로 호출 생명주기를 추적합니다.
출력은 JSON 한 줄로 통일되어 검색과 분석이 쉽습니다.
jq로 평균 응답 시간이나 에러율을 한 줄로 계산할 수 있습니다.
PII 마스킹은 매우 중요합니다.
mask_pii 함수로 이메일과 전화번호를 placeholder로 치환해 로그에 PII가 노출되지 않게 합니다.
GDPR이나 개인정보보호법 같은 규제 준수에 필수입니다.
