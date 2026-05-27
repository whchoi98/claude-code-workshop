# Slide 78: /mcp command

**Part 5: MCP 기본과 공식 서버**

## Code Blocks

### /mcp

```bash
# 1. 현재 연결된 MCP 서버 목록
> /mcp

Connected MCP Servers:

  filesystem        [stdio]  ✓ Connected
    Tools: 5 (read_file, write_file, ...)
    Status: ready

  github            [stdio]  ✓ Connected
    Tools: 12 (create_issue, search_code, ...)
    Status: ready

  jira              [http]   ✗ Failed
    Error: 401 Unauthorized
    Last attempt: 2 minutes ago

  slack             [stdio]  ⚠ Disconnected
    Reason: Process exited (code 1)

# 2. 특정 서버 도구 목록
> /mcp tools github
  - create_issue(owner, repo, title, body)
  - create_pull_request(...)
  - merge_pull_request(...)
  - ...

# 3. 특정 서버 재연결
> /mcp reconnect jira

# 4. 디버깅 정보
> /mcp logs github
# 최근 stderr 출력 표시
```

## Speaker Notes

/mcp 명령은 MCP 서버 상태를 확인하고 관리하는 도구입니다.
첫째, 인자 없이 호출하면 현재 연결된 모든 MCP 서버 목록이 표시됩니다.
각 서버의 통신 방식 stdio/http/sse가 대괄호로 표시되고 연결 상태가 체크 표시나 X 표시로 나타납니다.
filesystem과 github는 정상 연결, jira는 401 인증 실패, slack은 프로세스 종료로 끊긴 상태가 보입니다.
각 서버의 도구 수와 상태도 함께 표시됩니다.
둘째, 특정 서버의 도구 목록을 볼 수 있습니다.
/mcp tools github 형태로 명령하면 GitHub MCP가 제공하는 모든 도구의 시그니처가 표시됩니다.
셋째, 특정 서버 재연결이 가능합니다.
/mcp reconnect jira로 jira 서버를 다시 연결합니다.
토큰을 새로 발급받은 후나 일시적 네트워크 문제 해결 후 유용합니다.
넷째, 디버깅 정보를 볼 수 있습니다.
/mcp logs github로 최근 stderr 출력을 확인합니다.
어떤 에러가 발생했는지 추적할 수 있습니다.
