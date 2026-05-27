# Slide 105: Retry TypeScript

**Part 6: PRODUCTION 운영**

## Code Blocks

### retry TS

```python
// 1. p-retry 라이브러리 활용
import pRetry, { AbortError } from "p-retry";
import Anthropic, {
  APIConnectionError, APIConnectionTimeoutError,
  RateLimitError, AuthenticationError,
} from "@anthropic-ai/sdk";

const client = new Anthropic();

async function callClaude(prompt: string): Promise<string> {
  const message = await client.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    messages: [{ role: "user", content: prompt }],
  });
  return message.content[0].type === "text" ? message.content[0].text : "";
}

const result = await pRetry(
  () => callClaude("Hello"),
  {
    retries: 3,
    factor: 2,
    minTimeout: 1000,
    maxTimeout: 60_000,
    onFailedAttempt: error => {
      console.warn(`Attempt ${error.attemptNumber} failed`);
      if (error instanceof AuthenticationError) {
        throw new AbortError("Authentication failed");
      }
    },
  }
);

// 2. 수동 구현 (generic)
async function retryWithBackoff<T>(
  fn: () => Promise<T>,
  options: { maxRetries?: number; baseDelay?: number } = {}
): Promise<T> {
  const { maxRetries = 3, baseDelay = 2000 } = options;

  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await fn();
    } catch (err) {
      if (err instanceof AuthenticationError) throw err;
      if (err instanceof RateLimitError) {
        const retryAfter = parseInt(
          err.headers?.["retry-after"] ?? "60"
        );
        await new Promise(r => setTimeout(r, retryAfter * 1000));
      } else if (
        err instanceof APIConnectionError ||
        err instanceof APIConnectionTimeoutError
      ) {
        const delay = baseDelay * Math.pow(2, attempt) + Math.random() * 1000;
        await new Promise(r => setTimeout(r, delay));
      } else {
        throw err;
      }
    }
  }
  throw new Error("Max retries exceeded");
}
```

## Speaker Notes

TypeScript에서 Retry 패턴입니다.
1번 p-retry 라이브러리를 사용합니다.
pRetry 함수에 callback을 전달하면 자동 재시도가 됩니다.
retries 3, factor 2 exponential, minTimeout 1초, maxTimeout 1분으로 설정합니다.
onFailedAttempt callback에서 시도 정보를 로깅하고 permanent 에러 시 AbortError를 throw해서 재시도를 중단합니다.
2번 수동 구현은 generic 함수로 작성합니다.
retryWithBackoff는 모든 async 함수에 적용 가능합니다.
for 루프에서 maxRetries만큼 시도합니다.
AuthenticationError는 즉시 throw로 재시도 안 합니다.
RateLimitError는 retry-after 헤더를 사용합니다.
APIConnectionError류는 exponential backoff와 jitter를 적용합니다.
알 수 없는 에러는 즉시 throw해서 의도하지 않은 동작을 방지합니다.
TypeScript의 type guard로 안전하게 에러를 분기 처리합니다.
