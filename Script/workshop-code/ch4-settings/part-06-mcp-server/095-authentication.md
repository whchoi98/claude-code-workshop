# Slide 95: Authentication

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### auth

```python
// src/auth.ts
import jwt from "jsonwebtoken";

export interface AuthContext {
  userId: string;
  email: string;
  groups: string[];
  permissions: string[];
}

const JWT_SECRET = process.env.JWT_SECRET || "";

// MCP 요청에서 인증 정보 추출
export function authenticate(request: any): AuthContext {
  // stdio: 환경변수에서 토큰 (개발용)
  const token = process.env.MCP_AUTH_TOKEN ||
                request.params?.auth?.token;

  if (!token) {
    throw new Error("Authentication required");
  }

  try {
    const decoded = jwt.verify(token, JWT_SECRET) as any;
    return {
      userId: decoded.sub,
      email: decoded.email,
      groups: decoded.groups || [],
      permissions: decoded.permissions || [],
    };
  } catch (err) {
    throw new Error("Invalid or expired token");
  }
}

// 권한 검사
export function requirePermission(ctx: AuthContext, perm: string) {
  if (!ctx.permissions.includes(perm)) {
    throw new Error(`Permission denied: ${perm}`);
  }
}

// 도구 핸들러에서 사용
export async function handleGetEmployee(args: unknown, request: any) {
  const ctx = authenticate(request);
  requirePermission(ctx, "hr:read");
  // ... 실제 로직
}
```

## Speaker Notes

서버 인증 구현입니다.
AuthContext 인터페이스를 정의합니다.
userId, email, groups, permissions를 포함합니다.
authenticate 함수에서 요청에서 토큰을 추출합니다.
stdio 방식은 환경변수에서, http/sse 방식은 request params에서 토큰을 받습니다.
토큰이 없으면 즉시 에러를 던집니다.
jsonwebtoken 라이브러리로 JWT를 검증합니다.
verify 성공 시 decoded 페이로드에서 사용자 정보를 추출해 AuthContext로 반환합니다.
실패 시 invalid 또는 expired 에러를 던집니다.
requirePermission 함수로 권한 검사를 합니다.
AuthContext의 permissions 배열에 특정 권한이 있는지 확인합니다.
없으면 Permission denied 에러를 던집니다.
도구 핸들러에서 사용 패턴을 봅니다.
먼저 authenticate를 호출해 인증하고 requirePermission으로 도구별 권한을 검사합니다.
그 후 실제 로직을 실행합니다.
각 도구가 자체 권한을 명시적으로 요구하므로 보안이 강화됩니다.
