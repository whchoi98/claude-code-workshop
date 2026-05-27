# Slide 8: TypeScript 설치와 첫 호출

**Part 1: SDK 기본**

## Code Blocks

### TS first call

```python
# 1. 설치
$ npm install @anthropic-ai/sdk
# 또는 pnpm/yarn
$ pnpm add @anthropic-ai/sdk
$ yarn add @anthropic-ai/sdk

# package.json
{
  "dependencies": {
    "@anthropic-ai/sdk": "^0.30.0"
  }
}

# 2. 환경변수 설정 (동일)
$ export ANTHROPIC_API_KEY="sk-ant-api03-..."

# 3. 첫 호출 (Hello World)
# hello.ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();    // API key 자동 로드

const message = await client.messages.create({
  model: "claude-sonnet-4-5",
  max_tokens: 1024,
  messages: [
    { role: "user", content: "Hello, Claude!" }
  ],
});

// content는 ContentBlock[]
console.log(message.content[0].type === "text"
  ? message.content[0].text
  : "");
console.log(`Tokens: ${message.usage.output_tokens}`);

# 실행
$ npx tsx hello.ts
# 또는 컴파일 후 node hello.js

# 4. 명시적 API key
const client = new Anthropic({
  apiKey: "sk-ant-...",
  timeout: 60_000,           // ms
  maxRetries: 3,
});

# 5. CommonJS도 지원
const Anthropic = require("@anthropic-ai/sdk");
```

## Speaker Notes

TypeScript SDK 설치와 첫 호출입니다.
1단계 설치는 npm install @anthropic-ai/sdk 입니다.
pnpm과 yarn도 지원됩니다.
package.json에 dependencies로 명시됩니다.
2단계 환경변수 설정은 Python과 동일합니다.
3단계 첫 호출입니다.
import Anthropic from @anthropic-ai/sdk로 ES Module 형식을 사용합니다.
new Anthropic으로 인스턴스를 만들고 API key는 환경변수에서 자동 로드됩니다.
await로 비동기 호출하며 messages.create의 인자 구조는 Python과 동일합니다.
TypeScript의 차이는 content가 ContentBlock 배열이라는 점입니다.
type 필드로 분기해 text 타입인 경우에만 .text 속성에 접근합니다.
타입 안전성을 위한 패턴입니다.
usage.output_tokens는 동일합니다.
실행은 npx tsx로 즉시 실행하거나 컴파일 후 node로 실행합니다.
4단계 명시적 API key는 객체로 전달합니다.
timeout은 밀리초 단위로 ms 사용에 주의합니다.
5단계 CommonJS도 지원하지만 ESM을 권장합니다.
