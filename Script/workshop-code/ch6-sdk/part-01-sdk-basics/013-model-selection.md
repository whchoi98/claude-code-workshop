# Slide 13: 모델 선택

**Part 1: SDK 기본**

## Code Blocks

### models

```python
# Anthropic Direct
client.messages.create(
    model="claude-sonnet-4-5",     # 기본, 균형
    # model="claude-haiku-4-5",     # 빠르고 저렴
    # model="claude-opus-4-5",      # 최고 성능
    ...
)

# AWS Bedrock (region prefix + 버전)
client.messages.create(
    model="us.anthropic.claude-sonnet-4-5-20250514-v1:0",
    # cross-region inference 권장
    # us. : 미국, eu. : 유럽, apac. : 아시아-태평양
    ...
)

# GCP Vertex AI (@ 기호로 버전)
client.messages.create(
    model="claude-sonnet-4-5@20250514",
    ...
)

# 모델 선택 가이드
+----------------+--------+----------+----------+--------+
| 모델           | 속도   | 비용     | 품질     | 권장   |
+----------------+--------+----------+----------+--------+
| Haiku 4.5      | 빠름   | 1x       | 일반     | 분류   |
| Sonnet 4.5     | 보통   | 3x       | 우수     | 기본   |
| Opus 4.5       | 느림   | 15x      | 최고     | 핵심   |
+----------------+--------+----------+----------+--------+

# 동적 선택 패턴
def pick_model(complexity: str) -> str:
    return {
        "trivial":  "claude-haiku-4-5",
        "standard": "claude-sonnet-4-5",
        "critical": "claude-opus-4-5",
    }[complexity]

# 사용
model = pick_model("standard")
message = client.messages.create(model=model, ...)

# 비용 추적
print(f"Model: {message.model}")
print(f"Input:  {message.usage.input_tokens}")
print(f"Output: {message.usage.output_tokens}")
```

## Speaker Notes

모델 선택과 경로별 ID 형식입니다.
Anthropic Direct는 단순한 이름입니다.
claude-sonnet-4-5가 기본이고 haiku와 opus도 있습니다.
AWS Bedrock은 region prefix와 버전 suffix가 포함됩니다.
us, eu, apac 같은 prefix로 cross-region inference를 활용합니다.
GCP Vertex AI는 at 기호로 버전이 분리됩니다.
모델 선택 가이드 표를 봅니다.
Haiku 4.5는 빠르고 저렴해 분류 같은 작업에 적합합니다.
Sonnet 4.5는 균형 잡힌 모델로 기본 선택입니다.
Opus 4.5는 최고 성능이지만 15배 비싸므로 핵심 작업에만 사용합니다.
동적 선택 패턴이 권장됩니다.
complexity 인자로 trivial, standard, critical을 받아 적절한 모델을 반환하는 함수를 만들 수 있습니다.
비용 추적은 message.model로 실제 사용된 모델을 확인하고 usage로 토큰 수를 확인합니다.
이 두 정보를 로그하면 모델별 비용 분석이 가능합니다.
