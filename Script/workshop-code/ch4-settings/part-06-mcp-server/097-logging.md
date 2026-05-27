# Slide 97: Logging

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### logging

```python
// src/logger.ts
import pino from "pino";

export const logger = pino({
  level: process.env.LOG_LEVEL || "info",
  formatters: {
    level: (label) => ({ level: label }),
  },
  base: {
    service: "company-mcp-server",
    version: process.env.npm_package_version,
  },
});

// 도구 핸들러에서 구조화 로깅
export async function handleSearchTickets(args: unknown, req: any) {
  const startTime = Date.now();
  const ctx = authenticate(req);

  logger.info({
    user_id: ctx.userId,
    tool: "search_tickets",
    args: { ...args, sensitive_removed: true },
  }, "Tool invocation");

  try {
    const result = await /* 실제 로직 */;

    logger.info({
      user_id: ctx.userId,
      tool: "search_tickets",
      duration_ms: Date.now() - startTime,
      result_count: result.length,
    }, "Tool success");

    return result;
  } catch (err) {
    logger.error({
      user_id: ctx.userId,
      tool: "search_tickets",
      error: err instanceof Error ? err.message : String(err),
      duration_ms: Date.now() - startTime,
    }, "Tool failed");
    throw err;
  }
}
```

## Speaker Notes

로깅과 관측 가능성을 다룹니다.
pino 라이브러리를 사용해 구조화 로깅을 구현합니다.
logger 인스턴스를 생성하면서 메타데이터를 base 필드에 추가합니다.
service 이름과 version이 모든 로그에 자동 포함됩니다.
도구 핸들러에서 구조화 로깅 패턴을 봅니다.
시작 시점에 user_id, tool 이름, args를 로그합니다.
args에서 민감 정보는 sensitive_removed로 표시해 제거합니다.
성공 시 duration_ms와 result_count를 함께 로그합니다.
실패 시 에러 메시지와 duration_ms를 error 레벨로 로그합니다.
모든 로그는 JSON 형식으로 출력되어 ELK나 Datadog 같은 도구로 쉽게 수집됩니다.
pino는 stderr로 출력하므로 stdio 통신을 방해하지 않습니다.
Docker 컨테이너 환경에서는 stdout으로도 보낼 수 있습니다.
운영 환경에서 이런 구조화 로깅이 트러블슈팅의 핵심입니다.
