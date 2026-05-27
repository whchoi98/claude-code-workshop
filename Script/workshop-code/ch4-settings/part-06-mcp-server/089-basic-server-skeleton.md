# Slide 89: Basic server skeleton

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### skeleton

```python
// src/index.ts
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "company-mcp-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
      resources: {},
      prompts: {},
    },
  }
);

// 도구 등록은 다음 슬라이드에서

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Company MCP Server running on stdio");
}

main().catch((err) => {
  console.error("Server error:", err);
  process.exit(1);
});

// 실행
// $ npm run build && npm start
// 또는 개발 시: $ npm run dev
```

## Speaker Notes

기본 서버 스켈레톤입니다.
MCP SDK의 Server 클래스와 StdioServerTransport를 import합니다.
Server 인스턴스를 생성하면서 두 객체를 전달합니다.
첫 번째 객체는 서버 메타데이터로 name과 version을 명시합니다.
두 번째 객체는 capabilities로 제공할 기능을 선언합니다.
tools, resources, prompts 3가지 모두 빈 객체로 선언해 둡니다.
실제 도구 등록은 다음 슬라이드에서 다룹니다.
main 함수에서 StdioServerTransport를 생성하고 server.connect로 연결합니다.
중요한 점은 console.log가 아닌 console.error를 사용한다는 것입니다.
stdio 방식에서 stdout은 JSON-RPC 메시지 전용이므로 로그는 stderr로 보내야 합니다.
실행은 npm run build로 컴파일 후 npm start로 가능합니다.
개발 중에는 npm run dev로 watch 모드를 사용합니다.
