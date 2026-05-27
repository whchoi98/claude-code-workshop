# Slide 100: HTTP server mode

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### http server

```python
// src/http-server.ts - HTTP 모드 진입점
import express from "express";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import {
  SSEServerTransport
} from "@modelcontextprotocol/sdk/server/sse.js";
import { setupServer } from "./server.js";

const app = express();
app.use(express.json());

const mcpServer = new Server({...}, {...});
setupServer(mcpServer);

// SSE endpoint
app.get("/sse", async (req, res) => {
  // 인증
  const auth = req.headers.authorization;
  if (!auth?.startsWith("Bearer ")) {
    return res.status(401).json({ error: "Unauthorized" });
  }

  const transport = new SSEServerTransport("/messages", res);
  await mcpServer.connect(transport);
});

// Messages endpoint
app.post("/messages", express.raw({ type: "application/json" }),
  async (req, res) => {
    // 처리...
  }
);

// Health check
app.get("/health", (req, res) => res.json({ status: "ok" }));

const port = process.env.PORT || 8080;
app.listen(port, () => {
  console.error(`MCP HTTP server on :${port}`);
});
```

## Speaker Notes

HTTP 서버 모드로 배포하는 패턴입니다.
stdio 모드 외에 HTTP/SSE 모드도 지원해야 원격 사용자가 접근할 수 있습니다.
Express 프레임워크를 사용합니다.
SSEServerTransport를 SDK에서 import합니다.
MCP 서버 인스턴스를 생성하고 setupServer로 도구 등록까지 합니다.
SSE endpoint를 정의합니다.
/sse 경로로 GET 요청을 받습니다.
Authorization 헤더의 Bearer 토큰을 검증합니다.
유효하지 않으면 401을 반환합니다.
SSEServerTransport를 생성하고 mcpServer에 connect합니다.
Messages endpoint도 POST /messages로 정의합니다.
Claude Code가 메시지를 보낼 때 이 경로를 사용합니다.
/health endpoint는 단순 OK를 반환합니다.
Kubernetes나 로드밸런서의 헬스체크에 사용됩니다.
PORT 환경변수로 포트를 설정하고 listen합니다.
이 패턴으로 사내 서버에 한 번 배포하면 모든 사용자가 같은 서버를 사용할 수 있습니다.
