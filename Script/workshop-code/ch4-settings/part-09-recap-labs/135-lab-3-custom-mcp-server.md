# Slide 135: Lab 3 / Custom MCP server

**Part 9: RECAP & 4 LABS**

## Code Blocks

### Lab 3

```python
# 1. 프로젝트 생성
$ mkdir my-mcp && cd my-mcp
$ npm init -y
$ npm install @modelcontextprotocol/sdk
$ npm install -D typescript @types/node tsx

# 2. src/index.ts 작성 (간단한 사내 도구)
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { ListToolsRequestSchema, CallToolRequestSchema }
  from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  { name: "my-mcp", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [{
    name: "company_random_fact",
    description: "사내 trivia 무작위 반환",
    inputSchema: { type: "object", properties: {} },
  }],
}));

server.setRequestHandler(CallToolRequestSchema, async (req) => {
  const facts = [
    "우리 회사는 2010년에 설립되었습니다.",
    "코드 리뷰는 24시간 내에 첫 응답을 줍니다.",
    "Friday는 No Meeting Day입니다.",
  ];
  return { content: [{
    type: "text",
    text: facts[Math.floor(Math.random() * facts.length)]
  }]};
});

const transport = new StdioServerTransport();
await server.connect(transport);

# 3. settings.json에 등록 후 사용
> 사내 trivia 하나 알려줘
```

## Speaker Notes

Lab 3는 사내 MCP 서버 작성 실습입니다.
약 30분 소요됩니다.
간단한 예제로 전 과정을 경험합니다.
1단계 프로젝트를 생성합니다.
npm init 후 MCP SDK와 TypeScript 의존성을 설치합니다.
2단계 src/index.ts를 작성합니다.
Server와 StdioServerTransport, 요청 스키마들을 import합니다.
Server 인스턴스를 만들고 tools capabilities를 선언합니다.
ListToolsRequestSchema 핸들러에 company_random_fact 도구를 등록합니다.
CallToolRequestSchema 핸들러에 도구 호출 로직을 작성합니다.
사내 trivia 배열에서 무작위로 하나를 반환하는 간단한 구현입니다.
StdioServerTransport로 연결합니다.
3단계 settings.json에 등록합니다.
mcpServers에 my-mcp 항목을 추가하고 command와 args를 명시합니다.
4단계 사용 테스트입니다.
Claude에게 사내 trivia를 요청하면 MCP 도구가 호출되어 응답합니다.
첫 MCP 서버를 직접 작성하고 동작하는 것을 보는 강력한 경험입니다.
