# Slide 72: 스트림 에러 처리

**Part 4: STREAMING**

## Code Blocks

### stream errors

```python
# 1. 스트림 중간에 에러 발생
from anthropic import APIError

async def safe_stream(prompt, websocket):
    try:
        async with client.messages.stream(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            async for text in stream.text_stream:
                await websocket.send_json({
                    "type": "text",
                    "text": text,
                })

            final = await stream.get_final_message()
            await websocket.send_json({
                "type": "done",
                "usage": final.usage.model_dump(),
            })

    except APIError as e:
        await websocket.send_json({
            "type": "error",
            "message": f"API error: {e.message}",
        })

    except Exception as e:
        await websocket.send_json({
            "type": "error",
            "message": f"Unexpected: {type(e).__name__}",
        })

# 2. 재시도 with backoff
import asyncio
from anthropic import RateLimitError, APIConnectionError

async def stream_with_retry(prompt, websocket, max_retries=3):
    for attempt in range(max_retries):
        try:
            await safe_stream(prompt, websocket)
            return    # 성공
        except RateLimitError as e:
            wait = int(e.response.headers.get("retry-after", "60"))
            await websocket.send_json({
                "type": "retry",
                "wait": wait,
                "attempt": attempt + 1,
            })
            await asyncio.sleep(wait)
        except APIConnectionError:
            await asyncio.sleep(2 ** attempt)

    await websocket.send_json({
        "type": "error",
        "message": "Max retries exceeded",
    })

# 3. 부분 응답 처리
async def stream_with_partial_save(prompt, db):
    accumulated = ""
    try:
        async with client.messages.stream(...) as stream:
            async for text in stream.text_stream:
                accumulated += text
                # 5초마다 부분 저장
                if len(accumulated) % 100 == 0:
                    await db.save_partial(accumulated)

    except Exception as e:
        # 에러 발생 시에도 부분 응답 보존
        await db.save_with_error(accumulated, str(e))
        raise
```

## Speaker Notes

스트림 에러 처리로 도중 실패에 대응합니다.
1번 스트림 중간에 에러가 발생할 수 있습니다.
safe_stream 함수에서 try except로 감싸고 APIError와 일반 Exception을 구분 처리합니다.
websocket으로 type error 메시지를 보내 클라이언트에 알립니다.
2번 재시도 with backoff 패턴입니다.
stream_with_retry는 max_retries만큼 반복하면서 RateLimitError와 APIConnectionError를 처리합니다.
RateLimit는 retry-after 헤더를 존중하고 클라이언트에 type retry로 대기 시간을 알립니다.
ConnectionError는 exponential backoff로 2의 attempt 제곱 초만큼 대기합니다.
3번 부분 응답 처리는 중요한 데이터 보호 패턴입니다.
stream_with_partial_save에서 accumulated에 청크를 누적하면서 일정 길이마다 DB에 부분 저장합니다.
예외 발생 시에도 finally 블록처럼 동작해 지금까지의 응답을 보존합니다.
5분 이상 걸리는 긴 응답에서 네트워크 끊김이 발생해도 데이터 손실을 최소화합니다.
Claude의 답변이 길 때 특히 유용한 패턴입니다.
