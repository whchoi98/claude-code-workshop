# Slide 10: 비동기 클라이언트 (TypeScript)

**Part 1: SDK 기본**

## Code Blocks

### TS async

```python
// 1. TypeScript는 기본이 비동기
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const message = await client.messages.create({
  model: "claude-sonnet-4-5",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hi" }],
});

// 2. 동시 호출 (Promise.all)
const prompts = [
  "Python을 한 줄로 설명",
  "JavaScript를 한 줄로 설명",
  "Rust를 한 줄로 설명",
];

const tasks = prompts.map(prompt =>
  client.messages.create({
    model: "claude-haiku-4-5",
    max_tokens: 200,
    messages: [{ role: "user", content: prompt }],
  })
);

const results = await Promise.all(tasks);
results.forEach(r => {
  if (r.content[0].type === "text") {
    console.log(r.content[0].text);
  }
});

// 3. 제한된 동시성 (p-limit)
import pLimit from "p-limit";

const limit = pLimit(3);    // 최대 3개 동시

const tasksLimited = prompts.map(prompt =>
  limit(() => client.messages.create({
    model: "claude-haiku-4-5",
    max_tokens: 200,
    messages: [{ role: "user", content: prompt }],
  }))
);

const results2 = await Promise.all(tasksLimited);

// 4. 순차 처리 (의도적으로)
for (const prompt of prompts) {
  const r = await client.messages.create({...});
  // 한 번에 하나씩
}
```

## Speaker Notes

TypeScript 비동기 패턴입니다.
1번 TypeScript는 기본이 비동기입니다.
await 키워드로 messages.create를 호출하면 Promise가 반환됩니다.
2번 동시 호출은 Promise.all로 합니다.
prompts 배열을 map으로 task 배열로 변환하고 Promise.all로 모두 완료를 기다립니다.
결과 forEach로 처리하며 type narrowing으로 text 타입을 안전하게 사용합니다.
3번 제한된 동시성은 p-limit 라이브러리로 구현합니다.
pLimit 3을 만들고 각 호출을 limit으로 감쌉니다.
최대 3개만 동시 실행되고 나머지는 대기합니다.
Python의 Semaphore와 동일한 효과입니다.
4번 순차 처리는 for of 루프로 의도적으로 사용합니다.
한 호출이 끝나야 다음이 시작됩니다.
이전 결과를 다음 호출에 사용해야 할 때 필요한 패턴입니다.
