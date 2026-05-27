# Slide 84: Multi-server orchestration

**Part 5: MCP 기본과 공식 서버**

## Code Blocks

### orchestration

```bash
# 실전 시나리오: GitHub + JIRA + Slack 통합 워크플로

# 사용자 요청
> 이번 주 머지된 PR을 분석해서 관련 JIRA 티켓 상태를 업데이트하고
  완료 사항을 #engineering 채널에 요약 게시해줘

# Claude의 동작 (멀티 MCP 자동 조율)
1. GitHub MCP
   → search_pull_requests(query: 'is:merged merged:>=2026-05-19')
   → 결과: 23개 PR

2. 각 PR에서 JIRA 티켓 키 추출 (커밋 메시지의 PROJ-123)

3. JIRA MCP
   → 각 티켓 get_issue로 상태 확인
   → transition_issue로 'Done' 상태로 변경
   → add_comment로 머지된 PR 링크 추가

4. Slack MCP
   → send_message(channel: '#engineering', text: '...')
   → 메시지 내용: 머지된 PR 수, 관련 티켓 목록, 주요 변경사항

# 결과
- 23개 PR 자동 분석
- 18개 JIRA 티켓 Done 처리
- Slack에 깔끔한 요약 게시
- 사람 개입 없이 5분 내 완료
```

## Speaker Notes

멀티 MCP 서버 오케스트레이션 실전 시나리오입니다.
GitHub, JIRA, Slack 세 서버를 함께 활용하는 워크플로입니다.
사용자가 한 가지 요청을 합니다.
이번 주 머지된 PR을 분석해서 관련 JIRA 티켓 상태를 업데이트하고 완료 사항을 Slack 채널에 요약 게시해 달라는 요청입니다.
Claude가 자동으로 세 서버를 조율합니다.
1단계 GitHub MCP의 search_pull_requests로 머지된 PR을 검색합니다.
2단계 각 PR의 커밋 메시지에서 PROJ-123 형식의 JIRA 티켓 키를 추출합니다.
3단계 JIRA MCP에서 get_issue로 상태를 확인하고 transition_issue로 Done 상태로 변경합니다.
add_comment로 머지된 PR 링크를 추가합니다.
4단계 Slack MCP의 send_message로 engineering 채널에 요약을 게시합니다.
결과적으로 23개 PR 자동 분석, 18개 JIRA 티켓 Done 처리, Slack 요약 게시가 사람 개입 없이 5분 내 완료됩니다.
복잡한 워크플로를 자연어 한 줄로 자동화하는 강력한 패턴입니다.
