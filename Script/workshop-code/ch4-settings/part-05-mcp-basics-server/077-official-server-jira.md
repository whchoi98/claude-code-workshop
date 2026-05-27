# Slide 77: Official server: jira

**Part 5: MCP 기본과 공식 서버**

## Code Blocks

### jira

```bash
# 1. API 토큰 발급
# https://id.atlassian.com/manage-profile/security/api-tokens
# Create API Token

# 2. settings.json 등록
{
  "mcpServers": {
    "jira": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-jira"],
      "env": {
        "JIRA_URL": "https://company.atlassian.net",
        "JIRA_EMAIL": "user@company.com",
        "JIRA_API_TOKEN": "${JIRA_TOKEN}"
      }
    }
  }
}

# 3. 제공되는 도구
- create_issue(project, summary, description)
- get_issue(issue_key)
- update_issue(issue_key, fields)
- search_issues(jql_query)
- add_comment(issue_key, body)
- transition_issue(issue_key, status)
- list_projects()

# 4. 사용 예시
> PROJ-123 티켓 상태를 In Review로 변경해줘
> 이번 스프린트의 모든 high 우선순위 버그를 찾아줘
> 이 PR 내용으로 JIRA 티켓 생성해줘
> 진행 중인 내 티켓들을 요약해줘

# 5. JQL (JIRA Query Language) 지원
# 복잡한 검색도 자연어로 가능
```

## Speaker Notes

다섯 번째 공식 서버는 jira입니다.
JIRA 통합 서버입니다.
사용 절차를 봅니다.
1단계 API 토큰을 발급합니다.
Atlassian의 manage-profile에서 Create API Token으로 만듭니다.
2단계 settings.json에 등록합니다.
env에 JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN을 주입합니다.
3단계 제공되는 도구는 풍부합니다.
create_issue, get_issue, update_issue로 티켓 CRUD가 가능합니다.
search_issues는 JQL 쿼리를 받아 복잡한 검색을 합니다.
add_comment로 댓글 추가, transition_issue로 상태 전환, list_projects로 프로젝트 목록 조회가 가능합니다.
4단계 사용 예시는 다양합니다.
티켓 상태 변경, 스프린트 버그 찾기, PR 내용으로 티켓 생성, 내 티켓 요약 같은 작업입니다.
5단계 JQL을 자연어로 사용 가능합니다.
Claude가 자연어 요청을 JQL로 변환해서 검색합니다.
