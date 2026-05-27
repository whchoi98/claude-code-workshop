# Slide 71: 백프레셔

**Part 4: STREAMING**

## Code Blocks

### backpressure

```python
# 문제: 클라이언트가 빠르게 보내는 청크를 처리 못함
# 해결: 백프레셔로 적절히 throttling

# 1. 큐 기반 버퍼링
import asyncio

class BackpressureQueue:
    def __init__(self, max_size=100):
        self.queue = asyncio.Queue(maxsize=max_size)
        self.full_count = 0

    async def put(self, item):
        if self.queue.full():
            self.full_count += 1
            print(f"Queue full! Slowing down ({self.full_count}x)")
            await asyncio.sleep(0.1)    # 잠시 대기
        await self.queue.put(item)

    async def get(self):
        return await self.queue.get()

# 2. 스트림에서 활용
async def producer(stream, queue):
    async for event in stream:
        if event.type == "content_block_delta":
            await queue.put(event.delta.text)
    await queue.put(None)    # 종료 signal

async def consumer(queue, websocket):
    while True:
        text = await queue.get()
        if text is None: break
        await websocket.send_json({"type": "text", "text": text})

async def main():
    queue = BackpressureQueue(max_size=50)
    async with client.messages.stream(...) as stream:
        await asyncio.gather(
            producer(stream, queue),
            consumer(queue, websocket),
        )

# 3. 청크 배칭 (전송 효율)
class ChunkBatcher:
    def __init__(self, batch_size=10, flush_ms=100):
        self.batch = []
        self.batch_size = batch_size
        self.flush_ms = flush_ms
        self.last_flush = time.time()

    async def add(self, text, sender):
        self.batch.append(text)
        elapsed = (time.time() - self.last_flush) * 1000
        if len(self.batch) >= self.batch_size or elapsed > self.flush_ms:
            await sender("".join(self.batch))
            self.batch = []
            self.last_flush = time.time()

# 4. nginx 같은 프록시 설정
# X-Accel-Buffering: no    # 버퍼링 비활성
# proxy_buffering off;      # nginx config
# proxy_cache off;           # nginx config
```

## Speaker Notes

백프레셔는 느린 클라이언트에 대응하는 패턴입니다.
문제는 클라이언트가 처리 못하는 속도로 청크가 도착하는 경우입니다.
1번 큐 기반 버퍼링이 표준 해법입니다.
BackpressureQueue 클래스에서 asyncio.Queue를 max_size로 제한합니다.
큐가 가득 차면 짧게 대기하고 카운터를 증가시켜 발생 빈도를 추적합니다.
2번 스트림에서 producer consumer 패턴을 적용합니다.
producer는 스트림에서 이벤트를 받아 queue에 넣고 consumer는 queue에서 꺼내 websocket으로 전송합니다.
둘이 독립적으로 동작하므로 속도 차이를 큐가 흡수합니다.
3번 청크 배칭은 전송 효율을 높입니다.
ChunkBatcher 클래스에서 batch_size나 flush_ms 조건이 만족되면 일괄 전송합니다.
작은 청크 100개를 보내는 것보다 큰 청크 10개를 보내는 것이 네트워크 효율이 좋습니다.
단 너무 큰 배치는 응답 지연을 늘리므로 100ms 정도가 일반적입니다.
4번 인프라 설정도 중요합니다.
nginx 같은 프록시의 buffering을 끄지 않으면 청크들이 모두 모인 후 한 번에 전송됩니다.
X-Accel-Buffering no 헤더와 nginx config의 proxy_buffering off가 필수입니다.
