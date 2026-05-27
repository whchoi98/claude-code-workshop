# Slide 91: Registering tools (part 2)

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### register

```python
// src/server.ts
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import {
  ListToolsRequestSchema,
  CallToolRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import {
  getEmployeeTool, handleGetEmployee
} from "./tools/employee.js";
import {
  searchTicketsTool, handleSearchTickets
} from "./tools/tickets.js";

export function setupServer(server: Server) {
  // 1. tools 목록 응답
  server.setRequestHandler(ListToolsRequestSchema, async () => ({
    tools: [
      getEmployeeTool,
      searchTicketsTool,
      // ... 다른 도구들
    ],
  }));

  // 2. tool 호출 처리
  server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;

    switch (name) {
      case "get_employee":
        return { content: [{
          type: "text",
          text: JSON.stringify(await handleGetEmployee(args), null, 2)
        }]};
      case "search_tickets":
        return { content: [{
          type: "text",
          text: JSON.stringify(await handleSearchTickets(args), null, 2)
        }]};
      default:
        throw new Error(`Unknown tool: ${name}`);
    }
  });
}
```

## Speaker Notes

도구를 서버에 등록하는 방법입니다.
SDK의 ListToolsRequestSchema와 CallToolRequestSchema를 import합니다.
각 도구 파일에서 메타데이터와 핸들러를 import합니다.
setupServer 함수에서 두 가지 요청 핸들러를 등록합니다.
첫째, ListToolsRequestSchema 핸들러입니다.
클라이언트가 도구 목록을 요청하면 모든 도구의 메타데이터를 배열로 반환합니다.
둘째, CallToolRequestSchema 핸들러입니다.
클라이언트가 특정 도구를 호출하면 name으로 분기해 적절한 핸들러를 실행합니다.
switch 문으로 각 도구 이름에 매핑된 핸들러를 호출합니다.
응답은 content 배열 형식이며 type이 text인 객체에 결과를 JSON 문자열로 담습니다.
정의되지 않은 도구가 호출되면 에러를 던집니다.
이 패턴으로 새 도구를 추가할 때 switch 문에 case만 추가하면 됩니다.
