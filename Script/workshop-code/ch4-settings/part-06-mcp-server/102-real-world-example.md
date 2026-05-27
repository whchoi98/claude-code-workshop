# Slide 102: Real-world example

**Part 6: MCP 사내 서버 구축**

## Code Blocks

### real example

```bash
# settings.json (사용자 측)
{
  "mcpServers": {
    "company-wiki": {
      "type": "sse",
      "url": "https://mcp.company.com/sse",
      "headers": {
        "Authorization": "Bearer ${COMPANY_MCP_TOKEN}"
      }
    }
  }
}

# 사용 예시
> 우리 회사의 코딩 컨벤션 문서를 찾아서 요약해줘

# Claude의 동작
1. company-wiki MCP의 search_documents 도구 호출
   → query: "coding convention"
2. 결과 받음:
   - "engineering/coding-style.md"
   - "frontend/react-guidelines.md"
   - "backend/python-pep8-strict.md"
3. 각 문서를 read_document로 가져옴
4. 요약 응답:
   "우리 회사 코딩 컨벤션은 다음과 같습니다:
    - JavaScript: ESLint Airbnb config 사용
    - Python: PEP 8 + 사내 추가 규칙 5가지
    - React: Hooks 우선, class component 금지
    ..."

# 운영 메트릭 (3개월 운영 후)
- 일 평균 호출: 4,200건
- p99 응답 시간: 180ms
- 사용자: 230명
- 만족도: 4.6 / 5.0
```

## Speaker Notes

실전 예시로 회사 위키 검색 MCP 서버를 봅니다.
사용자 측 settings.json에 company-wiki 서버를 등록합니다.
sse 방식으로 mcp.company.com에 연결하며 Bearer 토큰으로 인증합니다.
사용 예시는 자연스럽습니다.
사용자가 회사 코딩 컨벤션 문서를 찾아서 요약해 달라고 요청합니다.
Claude가 자동으로 동작합니다.
1단계 search_documents 도구를 coding convention 쿼리로 호출합니다.
2단계 관련 문서 목록을 받습니다.
engineering, frontend, backend 영역의 문서들이 발견됩니다.
3단계 각 문서를 read_document로 가져옵니다.
4단계 요약 응답을 생성합니다.
JavaScript, Python, React 각각의 컨벤션을 종합해 사용자에게 전달합니다.
3개월 운영 후 메트릭이 인상적입니다.
일 평균 4200건 호출, p99 응답 시간 180ms, 사용자 230명, 만족도 4.6점입니다.
사내 MCP 서버가 일상 도구로 자리잡은 사례입니다.
