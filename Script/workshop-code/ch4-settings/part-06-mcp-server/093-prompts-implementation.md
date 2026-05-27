# Slide 93: Prompts implementation

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### prompts

```python
// src/prompts/standard.ts
import {
  ListPromptsRequestSchema,
  GetPromptRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

export function setupPrompts(server: Server) {
  // 1. 프롬프트 목록
  server.setRequestHandler(ListPromptsRequestSchema, async () => ({
    prompts: [
      {
        name: "incident-response",
        description: "장애 대응 표준 절차",
        arguments: [
          { name: "service", description: "장애 서비스명", required: true },
          { name: "severity", description: "심각도 (P0~P4)", required: true },
        ],
      },
      {
        name: "code-review-checklist",
        description: "사내 표준 코드 리뷰 체크리스트",
        arguments: [
          { name: "pr_url", description: "PR URL", required: true },
        ],
      },
    ],
  }));

  // 2. 프롬프트 콘텐츠
  server.setRequestHandler(GetPromptRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;

    if (name === "incident-response") {
      return {
        messages: [{
          role: "user",
          content: { type: "text", text:
`다음 장애를 대응해 주세요:
- 서비스: ${args?.service}
- 심각도: ${args?.severity}

표준 절차:
1. 장애 영향 범위 확인
2. 임시 조치 검토
3. 근본 원인 분석
4. 영구 조치 계획` },
        }],
      };
    }
    throw new Error(`Unknown prompt: ${name}`);
  });
}
```

## Speaker Notes

Prompts 등록 방법입니다.
Prompts는 재사용 가능한 프롬프트 템플릿입니다.
ListPromptsRequestSchema와 GetPromptRequestSchema를 사용합니다.
첫째, 프롬프트 목록을 반환합니다.
각 프롬프트는 name, description, arguments를 가집니다.
incident-response는 장애 대응 표준 절차로 service와 severity 인자를 받습니다.
code-review-checklist는 사내 표준 코드 리뷰로 pr_url 인자를 받습니다.
각 인자에 required 필드로 필수 여부를 명시합니다.
둘째, 프롬프트 콘텐츠를 반환합니다.
name과 arguments를 받아 적절한 메시지를 생성합니다.
incident-response의 경우 service와 severity 값을 템플릿에 삽입합니다.
표준 절차 4단계를 포함한 프롬프트가 자동 생성됩니다.
사용자는 /mcp prompts incident-response 같은 명령으로 호출할 수 있습니다.
팀 표준 프롬프트를 한 곳에서 관리하는 패턴입니다.
