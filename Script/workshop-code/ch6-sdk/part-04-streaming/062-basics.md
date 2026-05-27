# Slide 62: 스트리밍 기본

**Part 4: STREAMING**

## Code Blocks

### streaming basic

```python
# 1. 가장 단순한 스트리밍 (Python)
import anthropic

client = anthropic.Anthropic()

with client.messages.stream(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "긴 글 작성"}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

# 결과: 텍스트가 토큰 단위로 점진적으로 출력
# 사용자는 응답이 끝날 때까지 기다리지 않음

# 2. 최종 메시지 추출
with client.messages.stream(...) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

    # 스트림 종료 후 최종 message 객체 얻음
    final_message = stream.get_final_message()
    print(f"\nTokens: {final_message.usage.output_tokens}")

# 3. TypeScript 버전
import Anthropic from "@anthropic-ai/sdk";
const client = new Anthropic();

const stream = client.messages.stream({
  model: "claude-sonnet-4-5",
  max_tokens: 1024,
  messages: [{ role: "user", content: "긴 글 작성" }],
});

for await (const event of stream) {
  if (event.type === "content_block_delta" &&
      event.delta.type === "text_delta") {
    process.stdout.write(event.delta.text);
  }
}

const finalMessage = await stream.finalMessage();
console.log(`\nTokens: ${finalMessage.usage.output_tokens}`);

# 4. 비교: 일반 호출 vs 스트림
# 일반:  사용자 5초 대기 -> 전체 응답 한 번에
# 스트림: 0.3초 후 첫 토큰 -> 점진 표시 -> 5초 완료
# 인지된 응답 시간: 5초 -> 0.3초 (15배 개선)
```

## Speaker Notes

스트리밍 기본 사용법입니다.
1번 가장 단순한 스트리밍은 Python에서 with 문과 stream 메서드를 사용합니다.
stream.text_stream을 for로 순회하면 텍스트가 토큰 단위로 점진적으로 전달됩니다.
print의 end와 flush 옵션으로 즉시 출력합니다.
2번 최종 메시지 추출은 스트림 종료 후 get_final_message로 합니다.
전체 응답의 토큰 사용량과 메타데이터를 얻을 수 있습니다.
3번 TypeScript 버전은 비슷한 패턴입니다.
client.messages.stream으로 스트림을 만들고 for await로 이벤트를 순회합니다.
event.type을 확인해 content_block_delta의 text_delta인 경우만 출력합니다.
finalMessage는 await으로 받습니다.
4번 비교가 인상적입니다.
일반 호출은 5초 대기 후 한 번에 응답이 옵니다.
스트리밍은 0.3초 후 첫 토큰이 도착하고 점진적으로 표시되며 5초에 완료됩니다.
인지된 응답 시간이 5초에서 0.3초로 15배 개선됩니다.
사용자 경험에 미치는 영향이 매우 큽니다.
