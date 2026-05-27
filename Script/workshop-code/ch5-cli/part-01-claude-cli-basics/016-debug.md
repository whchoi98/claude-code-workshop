# Slide 16: 디버깅 옵션

**Part 1: claude 명령 기본**

## Code Blocks

### debug

```bash
# 1. --debug : 상세 디버그 로그
$ claude -p "..." --debug 2> debug.log
# stderr에 모든 내부 동작 로그
# Tool 호출, MCP 통신, 모델 응답까지 추적

# 2. --verbose : 사용자 향 상세 출력
$ claude doctor --verbose
# 환경 정보, 설정 파일 위치, MCP 연결 상태
# 환경변수 현재 값까지 모두 표시

# 3. claude doctor : 종합 진단
$ claude doctor

Claude Code v1.2.0
✓ Node.js v20.10.0
✓ Settings: ~/.claude/settings.json (valid)
✓ Authentication: API key (sk-ant-...)
✓ MCP servers: 3 connected
✓ Network: api.anthropic.com reachable
✗ Disk space: 92% used (warning)

# 4. 환경변수 확인
$ env | grep -i claude
$ env | grep -i anthropic

# 5. 버전 정보
$ claude --version
claude-code 1.2.0 (build 2026.05.20)

# 6. 일반 디버깅 흐름
1. claude doctor      # 기본 진단
2. claude --version   # 버전 확인
3. --debug 재실행      # 상세 로그
4. /mcp logs <server> # MCP 문제
5. Slack #claude 문의  # 에스컬레이션
```

## Speaker Notes

디버깅 옵션 3가지를 정리합니다.
첫째, --debug는 상세 디버그 로그입니다.
stderr에 모든 내부 동작 로그가 출력됩니다.
Tool 호출, MCP 통신, 모델 응답까지 추적됩니다.
2 리다이렉트로 파일에 저장하는 것이 일반적입니다.
둘째, --verbose는 사용자 향 상세 출력입니다.
주로 claude doctor와 함께 사용합니다.
환경 정보, 설정 파일 위치, MCP 연결 상태, 환경변수 값까지 모두 표시합니다.
셋째, claude doctor는 종합 진단 명령입니다.
Node.js 버전, settings 파일 유효성, 인증 상태, MCP 서버 연결, 네트워크 도달성, 디스크 공간까지 한 번에 확인합니다.
각 항목에 체크 표시나 X 표시로 정상 여부를 보여줍니다.
일반 디버깅 흐름은 5단계입니다.
claude doctor로 기본 진단, --version으로 버전 확인, --debug 재실행으로 상세 로그, /mcp logs로 MCP 문제 확인, 그래도 안 되면 사내 Slack에 에스컬레이션합니다.
