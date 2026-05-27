# Slide 96: Error handling

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### errors

```python
// src/errors.ts
import { ErrorCode, McpError } from "@modelcontextprotocol/sdk/types.js";

// 표준 MCP 에러
export class AuthError extends McpError {
  constructor(message: string) {
    super(ErrorCode.InvalidRequest, message);
  }
}

export class PermissionError extends McpError {
  constructor(perm: string) {
    super(ErrorCode.InvalidRequest, `Permission denied: ${perm}`);
  }
}

export class NotFoundError extends McpError {
  constructor(resource: string) {
    super(ErrorCode.InvalidParams, `Not found: ${resource}`);
  }
}

// 도구 핸들러에서 사용
export async function handleGetEmployee(args: unknown, request: any) {
  try {
    const ctx = authenticate(request);
    requirePermission(ctx, "hr:read");
    const { employee_id } = getEmployeeSchema.parse(args);

    const response = await fetch(`...${employee_id}`);
    if (response.status === 404) {
      throw new NotFoundError(`Employee: ${employee_id}`);
    }
    if (response.status === 401) {
      throw new AuthError("HR API authentication failed");
    }

    return await response.json();
  } catch (err) {
    if (err instanceof McpError) throw err;  // re-throw

    // 예상 못 한 에러는 로그만
    console.error("Unexpected:", err);
    throw new McpError(
      ErrorCode.InternalError,
      "Internal server error"
    );
  }
}
```

## Speaker Notes

에러 처리 패턴입니다.
MCP SDK의 McpError 클래스와 ErrorCode를 사용합니다.
사용자 정의 에러 클래스를 정의합니다.
AuthError는 인증 실패, PermissionError는 권한 부족, NotFoundError는 자원 없음입니다.
각각 적절한 ErrorCode와 메시지를 부모 클래스에 전달합니다.
도구 핸들러에서 try-catch로 에러를 처리합니다.
인증, 권한, 입력 검증을 순차 수행합니다.
fetch 응답의 status에 따라 적절한 에러를 던집니다.
404는 NotFoundError, 401은 AuthError로 변환합니다.
외부 catch에서 McpError instanceof 체크를 합니다.
이미 McpError이면 그대로 re-throw해 SDK가 처리하게 합니다.
예상하지 못한 에러는 console.error로 로그를 남기고 InternalError로 변환합니다.
내부 에러 상세를 클라이언트에 노출하지 않는 것이 보안 원칙입니다.
사용자는 적절한 에러 메시지만 받고 디버깅 정보는 서버 로그에만 남습니다.
