# Slide 117: 통합 테스트

**Part 6: PRODUCTION 운영**

## Code Blocks

### integration

```python
import pytest, os
from anthropic import Anthropic, BadRequestError

# 환경변수로 통합 테스트 활성화
INTEGRATION = os.getenv("RUN_INTEGRATION_TESTS") == "1"
pytestmark = pytest.mark.skipif(
    not INTEGRATION,
    reason="Set RUN_INTEGRATION_TESTS=1 to run"
)

@pytest.fixture(scope="module")
def real_client():
    api_key = os.getenv("ANTHROPIC_API_KEY_TEST")
    assert api_key, "Set ANTHROPIC_API_KEY_TEST"
    return Anthropic(api_key=api_key)

# 1. 기본 호출 (Haiku로 비용 절감)
def test_real_call(real_client):
    response = real_client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=50,
        messages=[{"role": "user", "content": "Reply 'pong'"}],
    )
    assert response.stop_reason in ["end_turn", "max_tokens"]
    text = response.content[0].text
    assert "pong" in text.lower()

# 2. Tool Use
def test_real_tool_use(real_client):
    tools = [{
        "name": "get_time",
        "description": "Get current time",
        "input_schema": {"type": "object", "properties": {}},
    }]
    response = real_client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=200,
        tools=tools,
        tool_choice={"type": "tool", "name": "get_time"},
        messages=[{"role": "user", "content": "What time?"}],
    )
    assert response.stop_reason == "tool_use"
    tool_blocks = [b for b in response.content if b.type == "tool_use"]
    assert len(tool_blocks) == 1
    assert tool_blocks[0].name == "get_time"

# 3. Streaming
def test_real_streaming(real_client):
    chunks = []
    with real_client.messages.stream(
        model="claude-haiku-4-5",
        max_tokens=100,
        messages=[{"role": "user", "content": "Count 1 to 5"}],
    ) as stream:
        for text in stream.text_stream:
            chunks.append(text)
    assert len(chunks) > 1
    full = "".join(chunks)
    for n in ["1", "2", "3", "4", "5"]:
        assert n in full

# 4. 에러 시나리오
def test_invalid_model(real_client):
    with pytest.raises(BadRequestError):
        real_client.messages.create(
            model="claude-nonexistent",
            max_tokens=10,
            messages=[{"role": "user", "content": "Hi"}],
        )

# 5. 비용 통제
# - Haiku만 사용 (1x 단가)
# - max_tokens 작게 (50-200)
# - 회당 비용: <$0.001
# - 매일 100회 = $0.1
```

## Speaker Notes

통합 테스트는 실제 API 호출을 포함합니다.
환경변수로 통합 테스트를 활성화합니다.
RUN_INTEGRATION_TESTS가 1일 때만 실행되므로 일반 단위 테스트와 분리됩니다.
pytestmark.skipif로 전체 모듈을 조건부 실행합니다.
real_client fixture는 module scope로 두어 한 번만 생성합니다.
별도의 테스트용 API key를 사용해 운영 key와 분리합니다.
기본 호출 통합 테스트는 Haiku 모델로 비용을 절감합니다.
max_tokens 50으로 짧게, pong이 응답에 포함되는지 검증합니다.
Tool Use 통합 테스트는 도구 정의와 tool_choice를 명시해 강제 호출을 만듭니다.
stop_reason이 tool_use이고 호출된 도구 이름이 정확한지 확인합니다.
Streaming 통합 테스트는 실제로 청크가 여러 개 도착하는지 검증합니다.
청크 수가 1보다 크고 모든 숫자가 포함되는지 확인합니다.
에러 시나리오로 잘못된 모델 ID를 사용해 BadRequestError 발생을 확인합니다.
비용 통제가 중요합니다.
통합 테스트는 Haiku만 사용하고 max_tokens를 작게 유지합니다.
회당 비용 0.001 달러 미만이고 매일 100회 실행해도 0.1 달러로 통제됩니다.
CI에서 매일 자동 실행하면 API 변화나 회귀를 즉시 감지할 수 있습니다.
