# Slide 126: Troubleshooting: MCP connection

**Part 8: INTEGRATION & TROUBLESHOOTING**

## Code Blocks

### mcp debug

```bash
# 증상: /mcp 명령에서 jira 서버가 'Failed'

# 진단 절차

# 1. /mcp로 상태 확인
> /mcp
  jira    [http]   ✗ Failed
    Error: 401 Unauthorized
    Last attempt: 2 minutes ago

# 2. 토큰 확인
$ echo $JIRA_TOKEN   # 환경변수 설정 여부
$ # 토큰 만료 여부 (API 직접 호출로 확인)
$ curl -H "Authorization: Bearer $JIRA_TOKEN" \
       "https://jira.atlassian.com/api/myself"
# 401이면 토큰 만료, 200이면 정상

# 3. 로그 확인
> /mcp logs jira
# 최근 stderr 출력

# 4. 재연결
> /mcp reconnect jira

# 5. settings.json 검증
$ jq . .claude/settings.json
# JSON 문법 오류 확인

# 6. 일반 원인
- 환경변수 미설정 또는 만료
- URL 오타
- 네트워크/방화벽 차단
- 서버 측 문제 (curl로 직접 확인)
- npm 패키지 버전 호환 안 됨

# 7. stdio 서버는 프로세스 확인
$ ps aux | grep mcp
# 자식 프로세스가 살아있는가?
```

## Speaker Notes

MCP 서버 연결 실패 진단 절차입니다.
jira 서버가 Failed로 표시되는 증상입니다.
1단계 /mcp로 상태를 확인합니다.
에러 메시지와 마지막 시도 시각이 표시됩니다.
2단계 토큰을 확인합니다.
환경변수 설정 여부를 echo로 확인하고 curl로 직접 API 호출해 토큰 유효성을 검증합니다.
401이면 토큰 만료, 200이면 토큰은 정상이고 다른 문제입니다.
3단계 로그를 확인합니다.
/mcp logs jira 명령으로 최근 stderr 출력을 봅니다.
4단계 재연결을 시도합니다.
/mcp reconnect jira로 다시 연결합니다.
5단계 settings.json을 검증합니다.
jq로 JSON 문법 오류를 체크합니다.
6단계 일반 원인입니다.
환경변수 미설정이나 만료, URL 오타, 네트워크와 방화벽 차단, 서버 측 문제, npm 패키지 버전 호환 문제 같은 원인들이 있습니다.
7단계 stdio 서버는 프로세스를 확인합니다.
ps aux로 자식 프로세스가 살아 있는지 확인합니다.
