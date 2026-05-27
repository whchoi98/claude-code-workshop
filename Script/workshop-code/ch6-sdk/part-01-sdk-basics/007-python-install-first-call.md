# Slide 7: Python 설치와 첫 호출

**Part 1: SDK 기본**

## Code Blocks

### Python first call

```python
# 1. 설치
$ pip install anthropic

# 또는 uv (더 빠름)
$ uv add anthropic

# requirements.txt
anthropic>=0.40.0

# 2. 환경변수 설정
$ export ANTHROPIC_API_KEY="sk-ant-api03-..."

# 3. 첫 호출 (Hello World)
# hello.py
from anthropic import Anthropic

client = Anthropic()    # API key를 환경변수에서 자동 읽음

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

print(message.content[0].text)
print(f"Tokens used: {message.usage.output_tokens}")

# 실행
$ python hello.py
# 출력:
# Hello! It's nice to meet you...
# Tokens used: 28

# 4. API key 명시적 전달
client = Anthropic(api_key="sk-ant-...")
# 또는 .env 파일과 python-dotenv

# 5. 타임아웃과 재시도 옵션
client = Anthropic(
    timeout=60.0,
    max_retries=3,
)
```

## Speaker Notes

Python SDK 설치와 첫 호출입니다.
1단계 설치는 pip install anthropic 한 줄입니다.
또는 uv add anthropic으로 더 빠르게 설치할 수 있습니다.
requirements.txt에는 버전 제약을 명시합니다.
2단계 환경변수 설정입니다.
ANTHROPIC_API_KEY를 export합니다.
3단계 첫 호출은 5줄입니다.
from anthropic import Anthropic으로 import하고 client = Anthropic으로 인스턴스를 만듭니다.
API key는 환경변수에서 자동으로 읽습니다.
client.messages.create로 호출하면서 model, max_tokens, messages를 명시합니다.
messages는 dict의 list로 role과 content를 갖습니다.
응답은 message 객체로 받고 content[0].text로 텍스트를 추출합니다.
usage.output_tokens로 토큰 사용량도 확인 가능합니다.
4단계 API key 명시적 전달도 가능합니다.
5단계 타임아웃과 재시도 옵션을 클라이언트 생성 시 명시할 수 있습니다.
