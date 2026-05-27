# Slide 116: 단위 테스트

**Part 6: PRODUCTION 운영**

## Code Blocks

### unit tests

```python
import pytest
from unittest.mock import MagicMock, patch
from anthropic import RateLimitError

# 1. 함수 로직 테스트 (Claude mock)
@patch("my_module.Anthropic")
def test_call_claude_success(mock_anthropic):
    mock_response = MagicMock()
    mock_response.content = [MagicMock(type="text", text="Hello!")]
    mock_response.usage.input_tokens = 10
    mock_response.usage.output_tokens = 5
    mock_response.stop_reason = "end_turn"

    mock_client = MagicMock()
    mock_client.messages.create.return_value = mock_response
    mock_anthropic.return_value = mock_client

    from my_module import call_claude
    result = call_claude("Hi")
    assert result == "Hello!"
    mock_client.messages.create.assert_called_once()

# 2. 에러 처리 테스트 (시퀀스)
@patch("my_module.Anthropic")
def test_rate_limit_retry(mock_anthropic):
    mock_client = MagicMock()
    error = RateLimitError(
        message="Rate limited",
        response=MagicMock(headers={"retry-after": "1"}),
        body=None,
    )
    mock_client.messages.create.side_effect = [
        error,    # 첫 호출 실패
        MagicMock(content=[MagicMock(type="text", text="OK")]),  # 재시도 성공
    ]
    mock_anthropic.return_value = mock_client

    from my_module import call_claude_with_retry
    result = call_claude_with_retry("Hi")
    assert result == "OK"
    assert mock_client.messages.create.call_count == 2

# 3. 입력 검증 테스트
def test_validate_empty():
    from my_module import validate_prompt
    with pytest.raises(ValueError, match="Empty"):
        validate_prompt("")

def test_validate_too_long():
    from my_module import validate_prompt
    with pytest.raises(ValueError, match="too long"):
        validate_prompt("x" * 100_000)

# 4. fixture
@pytest.fixture
def mock_claude():
    with patch("my_module.Anthropic") as m:
        mock_client = MagicMock()
        m.return_value = mock_client
        yield mock_client

def test_with_fixture(mock_claude):
    mock_claude.messages.create.return_value = MagicMock(
        content=[MagicMock(type="text", text="test")],
    )
    from my_module import call_claude
    assert call_claude("Hi") == "test"

# 5. 비용 계산
def test_cost_calculation():
    from my_module import calculate_cost
    r = MagicMock(model="claude-sonnet-4-5",
        usage=MagicMock(input_tokens=1000, output_tokens=500,
                        cache_read_input_tokens=0,
                        cache_creation_input_tokens=0))
    assert abs(calculate_cost(r) - 0.0105) < 1e-6
```

## Speaker Notes

단위 테스트는 pytest와 mock으로 작성합니다.
함수 로직 테스트에서 Claude를 mock합니다.
mock_response에 content, usage, stop_reason을 설정합니다.
messages.create의 return_value를 mock_response로 두면 실제 API 호출 없이 테스트 가능합니다.
검증은 결과 값과 호출 인자 모두 확인합니다.
call_args.kwargs로 어떤 인자로 호출됐는지 검사합니다.
에러 처리 테스트는 side_effect로 시퀀스를 정의합니다.
첫 호출은 RateLimitError를 raise하고 두 번째는 성공 응답을 반환합니다.
call_count로 재시도가 발생했는지 검증합니다.
입력 검증 테스트는 pytest.raises로 예외 발생을 확인합니다.
match 인자로 에러 메시지도 검증할 수 있습니다.
fixture로 공통 설정을 재사용합니다.
mock_claude fixture는 모든 테스트에서 mock된 client를 제공합니다.
yield로 테스트 종료 후 자동 cleanup이 가능합니다.
비용 계산 테스트로 단순 로직을 검증합니다.
MagicMock으로 response를 구성하고 calculate_cost가 정확한 값을 반환하는지 확인합니다.
단위 테스트는 Claude API를 호출하지 않으므로 빠르고 비용이 없습니다.
