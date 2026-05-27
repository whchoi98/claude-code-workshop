# Slide 138: Lab 1 / 첫 SDK 호출

**Part 8: RECAP & 4 LABS**

## Code Blocks

### Lab 1

```python
# 1. 환경 설정
$ python -m venv venv && source venv/bin/activate
$ pip install anthropic

# 또는 TypeScript
$ npm init -y
$ npm install @anthropic-ai/sdk
$ npm install --save-dev typescript tsx

# 2. API key 설정
$ export ANTHROPIC_API_KEY="sk-ant-..."

# 3. 첫 호출 (Python)
# hello.py
from anthropic import Anthropic
client = Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.content[0].text)
print(f"Tokens: {response.usage.output_tokens}")

# 4. 첫 호출 (TypeScript)
// hello.ts
import Anthropic from "@anthropic-ai/sdk";
const client = new Anthropic();

const message = await client.messages.create({
  model: "claude-sonnet-4-5",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello!" }],
});
console.log(message.content[0].type === "text"
  ? message.content[0].text : "");

# 5. 다양한 호출 패턴 연습
# - 시스템 프롬프트 추가
# - max_tokens 조정 (10, 1024, 4000)
# - temperature 비교 (0.0 vs 1.0)
# - 다른 모델 (Haiku vs Sonnet vs Opus)

# 6. 비용 측정
# - 5회 호출 후 총 토큰
# - 모델별 비용 비교
# - count_tokens로 사전 추정

# 7. 에러 처리 연습
# - 잘못된 모델 ID -> BadRequestError
# - API key 제거 -> AuthenticationError
# - 큰 max_tokens (>4096 for haiku) -> 잘림 확인

# 8. 도움말 탐색
# - dir(client.messages)
# - help(client.messages.create)
# - 공식 문서: docs.anthropic.com
```

## Speaker Notes

Lab 1은 첫 SDK 호출 실습입니다.
약 20분 소요됩니다.
환경 설정부터 다양한 호출 패턴까지 익힙니다.
1번 환경 설정은 Python 또는 TypeScript 중 본인이 익숙한 언어를 선택합니다.
Python은 venv와 pip, TypeScript는 npm으로 설정합니다.
2번 API key를 환경변수로 설정합니다.
3번 첫 호출 Python 예시를 직접 실행해 봅니다.
4번 같은 작업을 TypeScript로도 시도해 봅니다.
5번 다양한 호출 패턴을 연습합니다.
시스템 프롬프트, max_tokens 조정, temperature 비교, 다른 모델 사용입니다.
6번 비용 측정으로 토큰 사용량을 추적합니다.
5회 호출 후 총 토큰을 계산하고 모델별 비용을 비교합니다.
count_tokens로 사전 추정하는 패턴도 익힙니다.
7번 에러 처리 연습입니다.
잘못된 모델 ID로 BadRequestError를 발생시키고 API key 제거로 AuthenticationError를 발생시킵니다.
실제 에러를 경험해 보는 것이 중요합니다.
8번 도움말 탐색으로 SDK의 다른 기능들을 발견하는 습관을 들입니다.
