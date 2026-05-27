# Slide 94: Input validation

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### validation

```python
// src/tools/tickets.ts
import { z } from "zod";

// 강력한 스키마 정의
export const searchTicketsSchema = z.object({
  query: z.string()
    .min(3, "쿼리는 최소 3자 이상")
    .max(200, "쿼리는 최대 200자")
    .refine(
      (s) => !/<script|javascript:|eval\(/i.test(s),
      "위험한 패턴 감지"
    ),
  status: z.enum(["open", "in_progress", "closed"]).optional(),
  priority: z.enum(["low", "medium", "high", "critical"]).optional(),
  limit: z.number().int().min(1).max(100).default(20),
});

export async function handleSearchTickets(args: unknown) {
  // 입력 검증 (실패 시 ZodError throw)
  const params = searchTicketsSchema.parse(args);

  // SQL injection 방지: parameterized query 사용
  const tickets = await db.query(
    `SELECT id, title, status FROM tickets
     WHERE title LIKE ? AND status = ?
     LIMIT ?`,
    [`%${params.query}%`, params.status ?? "open", params.limit]
  );

  // 출력 마스킹 (민감 정보 제거)
  return tickets.map((t) => ({
    id: t.id,
    title: t.title,
    status: t.status,
    // assignee_email은 의도적으로 제외
  }));
}
```

## Speaker Notes

입력 검증 패턴을 살펴봅니다.
Zod로 안전한 처리를 구현합니다.
강력한 스키마 정의 예시입니다.
query는 문자열로 최소 3자, 최대 200자입니다.
refine으로 사용자 정의 검증을 추가합니다.
script 태그나 javascript 콜론, eval 같은 위험 패턴을 감지합니다.
status와 priority는 enum으로 허용 값을 제한합니다.
limit은 정수로 1-100 범위, 기본 20으로 설정합니다.
parse 호출 시 검증이 실패하면 ZodError가 자동으로 던져집니다.
SDK가 이를 받아 적절한 에러 응답으로 변환합니다.
SQL injection 방지를 위해 parameterized query를 사용합니다.
문자열 결합이 아닌 ? 플레이스홀더와 매개변수 배열을 사용합니다.
출력 마스킹도 중요합니다.
응답에서 assignee_email 같은 민감 정보를 의도적으로 제거합니다.
필요한 정보만 노출하는 것이 보안 원칙입니다.
