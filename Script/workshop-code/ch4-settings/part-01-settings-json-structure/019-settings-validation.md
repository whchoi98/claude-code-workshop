# Slide 19: Settings validation

**Part 1: settings.json 구조**

## Code Blocks

### Validation

```bash
# 1. claude doctor로 모든 설정 검증
$ claude doctor

Settings:
  Resolved: ~/.claude/settings.json + .claude/settings.json
  Permissions: 12 allow, 3 ask, 5 deny rules                      ✓
  Hooks: 2 PreToolUse, 1 PostToolUse                              ✓
  MCP servers: filesystem (stdio), github (stdio)                 ✓
  Telemetry: enabled, endpoint: https://otel.company.com:4318     ✓

# 2. JSON 문법 오류 시 직접 확인
$ jq . ~/.claude/settings.json
# JSON parse error 메시지로 라인 번호 표시

# 3. 권한 충돌 확인
> /permissions
# 현재 적용된 모든 권한 규칙 표시
# 각 규칙이 어느 계층에서 왔는지 함께 표시

# 4. Hooks 동작 확인
$ claude --debug
# hook 실행 시 stderr에 로그 출력
# 어느 hook이 어떤 입력을 받고 어떤 결과를 냈는지

# 5. MCP 서버 연결 확인
> /mcp
# 등록된 MCP 서버 목록과 연결 상태
```

## Speaker Notes

Settings 검증과 디버깅 방법입니다.
1단계 claude doctor로 모든 설정을 종합 검증합니다.
Settings 섹션에 resolved된 파일 경로, permissions 규칙 수, hooks 수, MCP 서버 상태, telemetry 설정이 모두 표시됩니다.
각 항목 옆 OK 표시로 정상 동작을 확인합니다.
2단계 JSON 문법 오류 시 jq 명령으로 직접 확인합니다.
파싱 에러 메시지에 라인 번호가 표시되어 빠르게 수정할 수 있습니다.
3단계 권한 충돌 확인입니다.
/permissions 명령으로 현재 적용된 모든 권한 규칙을 표시합니다.
각 규칙이 어느 계층에서 왔는지 함께 표시되어 디버깅이 쉽습니다.
4단계 Hooks 동작 확인은 --debug 옵션입니다.
hook 실행 시 stderr에 로그가 출력되어 어떤 입력을 받고 어떤 결과를 냈는지 추적할 수 있습니다.
5단계 MCP 서버 연결 확인은 /mcp 명령입니다.
등록된 MCP 서버 목록과 연결 상태를 표시합니다.
