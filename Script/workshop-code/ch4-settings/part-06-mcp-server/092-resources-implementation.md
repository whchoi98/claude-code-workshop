# Slide 92: Resources implementation

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### resources

```python
// src/resources/wiki.ts
import {
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

export function setupWikiResources(server: Server) {
  // 1. 사용 가능한 리소스 목록
  server.setRequestHandler(ListResourcesRequestSchema, async () => ({
    resources: [
      {
        uri: "wiki://onboarding",
        name: "Onboarding Guide",
        description: "신입 사원 온보딩 가이드",
        mimeType: "text/markdown",
      },
      {
        uri: "wiki://architecture",
        name: "System Architecture",
        description: "사내 시스템 아키텍처 문서",
        mimeType: "text/markdown",
      },
    ],
  }));

  // 2. 리소스 콘텐츠 반환
  server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
    const { uri } = request.params;

    // 사내 wiki API 호출
    const docName = uri.replace("wiki://", "");
    const response = await fetch(
      `https://wiki.company.com/api/pages/${docName}`,
      { headers: { "Authorization": `Bearer ${process.env.WIKI_TOKEN}` } }
    );

    const markdown = await response.text();
    return {
      contents: [{
        uri,
        mimeType: "text/markdown",
        text: markdown,
      }],
    };
  });
}
```

## Speaker Notes

Resources 등록 방법입니다.
Resources는 읽기 전용 데이터를 노출하는 primitive입니다.
ListResourcesRequestSchema와 ReadResourceRequestSchema를 import합니다.
첫째, 사용 가능한 리소스 목록을 반환합니다.
각 리소스는 uri, name, description, mimeType을 가집니다.
uri는 wiki:// 같은 사용자 정의 스킴을 사용합니다.
예시는 onboarding 가이드와 architecture 문서입니다.
둘째, 리소스 콘텐츠를 반환합니다.
ReadResourceRequestSchema 핸들러에서 uri를 받습니다.
uri에서 wiki:// 접두사를 제거해 문서 이름을 추출합니다.
사내 wiki API를 호출해 markdown 콘텐츠를 가져옵니다.
contents 배열에 uri, mimeType, text를 담아 반환합니다.
Claude Code가 이 콘텐츠를 메인 컨텍스트에 자동으로 포함시킵니다.
Resources는 자주 참조하는 사내 문서나 정책을 노출하는 데 적합합니다.
