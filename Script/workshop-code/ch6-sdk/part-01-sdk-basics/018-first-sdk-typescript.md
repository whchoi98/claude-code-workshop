# Slide 18: 첫 SDK 앱 TypeScript

**Part 1: SDK 기본**

## Code Blocks

### API server

```python
// app.ts - Claude 기반 API 서버
import express from "express";
import Anthropic, { APIError } from "@anthropic-ai/sdk";

const app = express();
app.use(express.json());

const client = new Anthropic();

interface ChatRequest {
  prompt: string;
  model?: string;
  max_tokens?: number;
}

app.post("/chat", async (req, res) => {
  const { prompt, model = "claude-sonnet-4-5",
          max_tokens = 1024 } = req.body as ChatRequest;

  if (!prompt) {
    return res.status(400).json({ error: "prompt required" });
  }

  try {
    const message = await client.messages.create({
      model,
      max_tokens,
      messages: [{ role: "user", content: prompt }],
    });

    const text = message.content[0].type === "text"
      ? message.content[0].text : "";

    res.json({
      text,
      usage: message.usage,
      model: message.model,
    });

  } catch (err) {
    if (err instanceof APIError) {
      res.status(err.status ?? 500).json({
        error: err.message,
      });
    } else {
      res.status(500).json({ error: "internal error" });
    }
  }
});

app.get("/health", (_, res) => res.json({ ok: true }));

const port = process.env.PORT ?? 3000;
app.listen(port, () => console.log(`API on :${port}`));

// 사용
// $ curl -X POST http://localhost:3000/chat \
//     -d '{"prompt":"Hello"}' \
//     -H "content-type: application/json"
```

## Speaker Notes

TypeScript로 만든 첫 Express API 서버 예시입니다.
express와 Anthropic SDK를 import합니다.
app.use(express.json)으로 JSON body parsing을 활성화합니다.
client는 모듈 레벨에서 한 번만 생성합니다.
ChatRequest interface로 입력 타입을 정의합니다.
prompt는 필수, model과 max_tokens는 선택입니다.
POST /chat 엔드포인트에서 req.body를 destructuring하면서 기본값을 명시합니다.
prompt가 없으면 400을 반환합니다.
await client.messages.create로 Claude를 호출합니다.
content[0]의 type narrowing으로 text를 안전하게 추출합니다.
응답에 text, usage, model을 포함시킵니다.
catch에서 APIError는 그 status를 사용하고 일반 에러는 500으로 처리합니다.
/health 엔드포인트는 헬스체크용입니다.
app.listen으로 서버를 시작합니다.
사용은 curl로 POST 요청을 보내면 됩니다.
실용적인 API 서버가 완성됩니다.
