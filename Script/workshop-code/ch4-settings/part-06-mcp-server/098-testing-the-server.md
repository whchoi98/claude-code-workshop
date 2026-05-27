# Slide 98: Testing the server

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### tests

```python
// tests/employee.test.ts
import { describe, it, expect, vi } from "vitest";
import {
  handleGetEmployee, getEmployeeSchema
} from "../src/tools/employee";

describe("getEmployeeSchema", () => {
  it("유효한 employee_id 통과", () => {
    expect(() => getEmployeeSchema.parse({
      employee_id: "emp_12345"
    })).not.toThrow();
  });

  it("빈 employee_id 거부", () => {
    expect(() => getEmployeeSchema.parse({
      employee_id: ""
    })).toThrow();
  });
});

describe("handleGetEmployee", () => {
  it("정상 조회 시 employee 객체 반환", async () => {
    // fetch mock
    global.fetch = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({ id: "emp_1", name: "Alice" }),
    });

    const result = await handleGetEmployee(
      { employee_id: "emp_1" },
      { headers: { authorization: "Bearer test" } }
    );

    expect(result.name).toBe("Alice");
  });
});

// 실행
// $ npm test
```

## Speaker Notes

서버 테스트 패턴입니다.
vitest를 사용한 단위 테스트 예시입니다.
employee 스키마 검증 테스트를 봅니다.
유효한 employee_id로 parse가 통과하는지 확인합니다.
빈 문자열로 parse 시 throw되는지 확인합니다.
두 케이스가 정상 동작해야 입력 검증이 올바른 것입니다.
handleGetEmployee 핸들러 테스트를 봅니다.
global.fetch를 vi.fn으로 mock합니다.
실제 외부 API 호출 없이 응답을 시뮬레이션합니다.
mock된 응답은 ok true와 json 함수를 반환합니다.
핸들러를 호출하고 result.name이 Alice인지 검증합니다.
외부 의존성을 mock하면 빠르고 결정적인 테스트가 가능합니다.
CI에서 npm test로 실행되며 매 PR마다 자동 검증됩니다.
테스트가 충분하면 리팩토링이나 새 기능 추가가 안전합니다.
