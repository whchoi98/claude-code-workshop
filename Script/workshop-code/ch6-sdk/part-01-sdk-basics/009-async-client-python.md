# Slide 9: 비동기 클라이언트 (Python)

**Part 1: SDK 기본**

## Code Blocks

### Python async

```python
# 1. AsyncAnthropic으로 비동기 처리
import asyncio
from anthropic import AsyncAnthropic

async def main():
    client = AsyncAnthropic()

    message = await client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": "Hi"}],
    )
    print(message.content[0].text)

asyncio.run(main())

# 2. 동시 호출 (asyncio.gather)
async def multiple_calls():
    client = AsyncAnthropic()

    # 5개를 동시에 호출
    tasks = [
        client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=200,
            messages=[{"role": "user", "content": q}],
        )
        for q in [
            "Python을 한 줄로 설명",
            "JavaScript를 한 줄로 설명",
            "Rust를 한 줄로 설명",
            "Go를 한 줄로 설명",
            "TypeScript를 한 줄로 설명",
        ]
    ]
    results = await asyncio.gather(*tasks)
    for r in results:
        print(r.content[0].text)

asyncio.run(multiple_calls())

# 3. 제한된 동시성 (Semaphore)
async def rate_limited():
    client = AsyncAnthropic()
    sem = asyncio.Semaphore(3)    # 최대 3개 동시

    async def call(prompt):
        async with sem:
            return await client.messages.create(
                model="claude-haiku-4-5",
                max_tokens=200,
                messages=[{"role": "user", "content": prompt}],
            )

    tasks = [call(p) for p in PROMPTS]
    return await asyncio.gather(*tasks)
```

## Speaker Notes

Python 비동기 클라이언트입니다.
1번 AsyncAnthropic으로 비동기 처리를 합니다.
async def 함수 안에서 await client.messages.create로 호출합니다.
asyncio.run으로 이벤트 루프를 시작합니다.
2번 동시 호출은 asyncio.gather로 합니다.
5개의 task를 동시에 시작하고 모두 완료될 때까지 기다립니다.
for 루프로 task를 만들고 unpacking으로 gather에 전달합니다.
결과는 task 순서대로 받습니다.
Haiku를 사용해 비용을 절감합니다.
3번 제한된 동시성은 Semaphore로 구현합니다.
최대 3개 동시 호출로 rate limit을 방지합니다.
async with sem으로 컨텍스트 매니저 패턴을 사용합니다.
3개가 동시 실행되고 하나가 완료되면 다음이 시작됩니다.
대량 처리 시 필수 패턴입니다.
동기 클라이언트로는 5개 호출이 순차로 약 5초 걸린다면 비동기는 1초로 줄어듭니다.
