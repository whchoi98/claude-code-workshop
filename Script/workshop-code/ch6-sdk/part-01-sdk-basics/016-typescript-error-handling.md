# Slide 16: TypeScript 에러 처리

**Part 1: SDK 기본**

## Code Blocks

### TS errors

```python
// TypeScript 에러 클래스
import Anthropic, {
  APIError,
  APIConnectionError,
  APIConnectionTimeoutError,
  AuthenticationError,
  BadRequestError,
  PermissionDeniedError,
  NotFoundError,
  RateLimitError,
  APIStatusError,
} from "@anthropic-ai/sdk";

const client = new Anthropic();

try {
  const message = await client.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hi" }],
  });
  console.log(message.content[0].type === "text"
    ? message.content[0].text : "");

} catch (err) {
  if (err instanceof AuthenticationError) {
    console.error("인증 실패:", err.message);
  } else if (err instanceof RateLimitError) {
    const retryAfter = parseInt(
      err.headers?.["retry-after"] ?? "60"
    );
    console.log(`Rate limited, retry in ${retryAfter}s`);
    await new Promise(r => setTimeout(r, retryAfter * 1000));
  } else if (err instanceof APIConnectionError) {
    console.error("Connection failed:", err.message);
  } else if (err instanceof APIConnectionTimeoutError) {
    console.error("Timeout:", err.message);
  } else if (err instanceof BadRequestError) {
    console.error("Bad request:", err.message);
  } else if (err instanceof APIStatusError) {
    console.error(`Status ${err.status}: ${err.message}`);
  } else if (err instanceof APIError) {
    console.error("API error:", err.message);
  } else {
    throw err;    // 알 수 없는 에러는 re-throw
  }
}

// 헬퍼 함수 패턴
async function safeCallClaude<T>(
  fn: () => Promise<T>
): Promise<T | null> {
  try {
    return await fn();
  } catch (err) {
    if (err instanceof RateLimitError) {
      // retry 로직
    }
    return null;
  }
}
```

## Speaker Notes

TypeScript 에러 처리는 try catch와 instanceof 타입 가드를 결합합니다.
import에서 에러 클래스들을 함께 가져옵니다.
Python과 같은 계층 구조입니다.
catch 블록에서 err을 받고 instanceof로 구체적인 타입을 확인합니다.
AuthenticationError는 메시지 출력 후 중단합니다.
RateLimitError는 headers의 retry-after를 파싱하고 setTimeout으로 대기 후 재시도합니다.
APIConnectionError와 APIConnectionTimeoutError는 별도로 구분됩니다.
BadRequestError는 인자 문제로 디버깅 필요합니다.
APIStatusError는 status 코드를 함께 출력해 서버 에러를 추적합니다.
마지막에 APIError로 catch-all을 두고 알 수 없는 에러는 throw err로 re-throw합니다.
헬퍼 함수 패턴도 권장됩니다.
safeCallClaude로 모든 호출을 래핑하면 에러 처리 로직을 한 곳에서 관리할 수 있습니다.
Generic T로 모든 반환 타입을 지원합니다.
