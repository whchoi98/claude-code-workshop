# Slide 57: 도구 테스트

**Part 3: TOOL USE**

## Code Blocks

### testing

```python
# 1. 단위 테스트 (pytest)
import pytest
from unittest.mock import patch

def test_get_weather():
    result = get_weather(location="Seoul")
    assert "temp" in result
    assert isinstance(result["temp"], (int, float))

def test_get_weather_invalid():
    with pytest.raises(ValueError):
        get_weather(location="")

# 2. mock으로 외부 의존성 격리
@patch("requests.get")
def test_get_weather_api_call(mock_get):
    mock_get.return_value.json.return_value = {
        "temp": 22, "condition": "sunny"
    }
    mock_get.return_value.status_code = 200

    result = get_weather(location="Seoul")
    assert result["temp"] == 22
    mock_get.assert_called_once()

# 3. 도구 스키마 검증
def test_tool_schemas():
    for tool in TOOLS:
        assert "name" in tool
        assert "description" in tool
        assert "input_schema" in tool
        assert tool["input_schema"]["type"] == "object"
        # JSON Schema 자체 검증
        from jsonschema import Draft7Validator
        Draft7Validator.check_schema(tool["input_schema"])

# 4. 통합 테스트 (mock Claude)
from unittest.mock import MagicMock

def test_agent_flow():
    mock_client = MagicMock()

    # 첫 번째 응답: tool_use
    first = MagicMock()
    first.stop_reason = "tool_use"
    first.content = [MagicMock(
        type="tool_use", id="t1",
        name="get_weather", input={"location": "Seoul"}
    )]

    # 두 번째 응답: text
    second = MagicMock()
    second.stop_reason = "end_turn"
    second.content = [MagicMock(type="text", text="22도 맑음")]

    mock_client.messages.create.side_effect = [first, second]

    # agent 실행
    result = run_agent("서울 날씨", client=mock_client)
    assert "22도" in result

# 5. 도구 응답 시간 모니터링
def test_tool_performance():
    start = time.time()
    result = get_weather("Seoul")
    elapsed = time.time() - start
    assert elapsed < 1.0, f"Too slow: {elapsed}s"
```

## Speaker Notes

도구 테스트로 안정적인 도구를 보장합니다.
1번 단위 테스트는 pytest로 작성합니다.
정상 케이스와 예외 케이스 모두 다룹니다.
get_weather의 정상 결과 형식과 잘못된 입력 시 ValueError를 검증합니다.
2번 mock으로 외부 의존성을 격리합니다.
requests.get을 patch해 실제 API 호출 없이 테스트할 수 있습니다.
mock_get.return_value로 응답을 시뮬레이션하고 assert_called_once로 호출 여부를 확인합니다.
3번 도구 스키마 검증은 자동화 가능합니다.
모든 TOOLS의 필드 존재와 input_schema의 type, JSON Schema 자체 유효성을 검사합니다.
Draft7Validator.check_schema로 schema가 valid JSON Schema인지 확인합니다.
4번 통합 테스트는 Claude를 mock합니다.
MagicMock으로 tool_use 응답과 end_turn 응답을 순차적으로 반환하게 설정합니다.
side_effect에 응답 리스트를 두면 호출마다 다음 응답이 사용됩니다.
agent 흐름이 의도대로 동작하는지 검증할 수 있습니다.
5번 도구 응답 시간 모니터링은 성능 회귀를 방지합니다.
특정 임계치를 정해 그보다 느리면 테스트가 실패하게 합니다.
CI에서 자동 실행하면 성능 저하를 즉시 감지합니다.
