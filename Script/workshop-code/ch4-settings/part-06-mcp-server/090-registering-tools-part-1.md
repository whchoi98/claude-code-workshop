# Slide 90: Registering tools (part 1)

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### tool def

```python
// src/tools/employee.ts
import { z } from "zod";

// 입력 스키마 (Zod로 검증)
export const getEmployeeSchema = z.object({
  employee_id: z.string().describe("사원 ID (예: emp_12345)"),
});

// 도구 메타데이터
export const getEmployeeTool = {
  name: "get_employee",
  description: "사원 ID로 사원 정보 조회",
  inputSchema: {
    type: "object",
    properties: {
      employee_id: {
        type: "string",
        description: "사원 ID (예: emp_12345)",
      },
    },
    required: ["employee_id"],
  },
};

// 도구 핸들러 (실제 로직)
export async function handleGetEmployee(args: unknown) {
  // 입력 검증
  const { employee_id } = getEmployeeSchema.parse(args);

  // 사내 API 호출 (예시)
  const response = await fetch(
    `https://hr-api.company.com/employees/${employee_id}`,
    { headers: { "Authorization": `Bearer ${process.env.HR_TOKEN}` } }
  );

  if (!response.ok) throw new Error(`HR API error: ${response.status}`);

  const employee = await response.json();
  return employee;
}
```

## Speaker Notes

Tools 등록의 첫 단계는 도구 정의입니다.
예시는 사원 정보 조회 도구입니다.
먼저 zod로 입력 스키마를 정의합니다.
employee_id를 문자열로 요구하며 describe로 설명을 추가합니다.
zod 스키마는 런타임 입력 검증에 사용됩니다.
다음 도구 메타데이터를 정의합니다.
name은 get_employee, description은 도구 설명입니다.
inputSchema는 JSON Schema 형식으로 작성합니다.
MCP 프로토콜이 이 형식을 표준으로 사용합니다.
properties에 각 인자의 타입과 설명을 명시하고 required 배열에 필수 인자를 나열합니다.
핸들러 함수에서 실제 로직을 작성합니다.
args를 unknown으로 받아 zod 스키마로 parse합니다.
파싱 실패 시 자동으로 에러가 던져집니다.
사내 HR API를 호출하며 환경변수 HR_TOKEN으로 인증합니다.
실패 시 에러를 던지고 성공 시 JSON 데이터를 반환합니다.
