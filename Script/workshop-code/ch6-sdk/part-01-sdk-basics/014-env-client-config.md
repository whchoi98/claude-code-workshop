# Slide 14: 환경별 클라이언트 설정

**Part 1: SDK 기본**

## Code Blocks

### env config

```python
# config.py - 환경별 설정
import os
from anthropic import Anthropic, AnthropicBedrock

def get_client():
    env = os.getenv("ENV", "dev")

    if env == "dev":
        # 개발: Direct + 짧은 timeout
        return Anthropic(
            timeout=30.0,
            max_retries=1,
        )
    elif env == "staging":
        # Staging: Bedrock + 중간 timeout
        return AnthropicBedrock(
            aws_region=os.getenv("AWS_REGION", "us-east-1"),
            timeout=60.0,
            max_retries=2,
        )
    elif env == "prod":
        # Prod: Bedrock + 긴 timeout + 많은 재시도
        return AnthropicBedrock(
            aws_region=os.getenv("AWS_REGION", "us-east-1"),
            timeout=120.0,
            max_retries=5,
        )
    else:
        raise ValueError(f"Unknown env: {env}")

def get_model() -> str:
    env = os.getenv("ENV", "dev")
    if env == "prod":
        return "us.anthropic.claude-sonnet-4-5-20250514-v1:0"
    return "claude-sonnet-4-5"

# 사용
client = get_client()
model = get_model()

message = client.messages.create(
    model=model,
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hi"}],
)

# 또는 클래스 기반
class ClaudeClient:
    def __init__(self):
        self.client = get_client()
        self.model = get_model()

    def chat(self, prompt: str, **kwargs) -> str:
        message = self.client.messages.create(
            model=self.model,
            max_tokens=kwargs.get("max_tokens", 1024),
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text
```

## Speaker Notes

환경별 클라이언트 설정 패턴입니다.
config.py에 get_client 함수를 정의합니다.
ENV 환경변수에 따라 다른 클라이언트를 반환합니다.
dev는 Anthropic Direct로 짧은 timeout과 1회 재시도입니다.
staging은 Bedrock으로 60초 timeout과 2회 재시도입니다.
prod는 Bedrock으로 120초 timeout과 5회 재시도로 강건합니다.
get_model 함수는 환경별 적절한 모델 ID를 반환합니다.
prod는 cross-region inference profile을 사용하고 dev와 staging은 단순 ID를 사용합니다.
사용은 client와 model을 한 번 얻은 후 messages.create에 전달합니다.
또는 클래스 기반 ClaudeClient 패턴이 더 깔끔합니다.
__init__에서 client와 model을 초기화하고 chat 메서드로 단순화된 인터페이스를 제공합니다.
kwargs로 max_tokens 같은 옵션을 전달 가능합니다.
이 패턴으로 환경 분리와 코드 재사용이 동시에 가능합니다.
