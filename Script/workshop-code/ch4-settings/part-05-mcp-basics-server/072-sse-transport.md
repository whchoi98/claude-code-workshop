# Slide 72: SSE transport

**Part 5: MCP 기본과 공식 서버**

## Code Blocks

### sse

```bash
# settings.json
{
  "mcpServers": {
    "events-stream": {
      "type": "sse",
      "url": "https://mcp-events.company.com/sse",
      "headers": {
        "Authorization": "Bearer ${SSE_TOKEN}"
      }
    }
  }
}

# 동작 흐름
1. Claude Code가 SSE 연결 시작 (long-lived HTTP)
2. 서버가 'data:' 라인으로 이벤트 스트림 전송
3. 양방향 메시지 교환 가능
4. 연결 유지 (재연결 자동)

# 적합 시나리오
- 진행 상황 실시간 보고 (배포, 빌드 등)
- 외부 이벤트 푸시 (Slack 새 메시지, CI 결과)
- 장기 실행 작업의 중간 결과
- 양방향 대화형 워크플로

# vs HTTP
- HTTP: 1요청 1응답 (짧은 작업)
- SSE: 1연결 N이벤트 (긴 작업, 푸시)
```

## Speaker Notes

SSE 통신 방식을 자세히 살펴봅니다.
settings.json 예시는 단순합니다.
type을 sse로 명시하고 url과 인증 헤더만 추가합니다.
동작 흐름은 HTTP와 다릅니다.
Claude Code가 SSE 연결을 시작합니다.
long-lived HTTP 연결입니다.
서버가 data 라인으로 이벤트 스트림을 전송합니다.
양방향 메시지 교환이 가능하며 연결이 끊기면 자동 재연결됩니다.
적합 시나리오를 봅니다.
진행 상황 실시간 보고에 적합합니다.
배포, 빌드, 데이터 처리 같은 긴 작업의 단계별 보고에 사용합니다.
외부 이벤트 푸시도 가능합니다.
Slack 새 메시지, CI 결과 같은 비동기 이벤트를 받을 수 있습니다.
장기 실행 작업의 중간 결과를 받거나 양방향 대화형 워크플로를 구현할 수 있습니다.
HTTP와 비교하면 차이가 분명합니다.
HTTP는 1요청 1응답으로 짧은 작업에 적합하고 SSE는 1연결 N이벤트로 긴 작업과 푸시에 적합합니다.
