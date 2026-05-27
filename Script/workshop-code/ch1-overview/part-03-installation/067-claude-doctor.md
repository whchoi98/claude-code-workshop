# Slide 67: claude doctor

**Part 3: INSTALLATION**

## Code Blocks

### claude doctor

```bash
$ claude doctor

  Claude Code Doctor

  System
    OS                macOS 14.6 (arm64)            OK
    Node              v20.10.0                       OK
    Disk free         12.3 GB                        OK
    RAM               16 GB                          OK

  Network
    api.anthropic.com  reachable (43 ms)             OK
    Outbound HTTPS     allowed                        OK
    Proxy              none detected                  OK

  Auth
    Credentials       ANTHROPIC_API_KEY (env)         OK
    Token valid       yes (Pro plan)                  OK

  Config
    Settings file     ~/.claude/settings.json         OK
    CLAUDE.md         not found (project root)        i
    MCP servers       2 configured                    OK

  Issues: 0 errors, 1 info
```

## Speaker Notes

claude doctor는 환경 자가 진단을 수행하는 강력한 명령입니다.
출력은 4개 섹션으로 구성됩니다.
System은 OS, Node, 디스크, RAM 같은 시스템 사양을 확인합니다.
Network는 api.anthropic.com 도달 가능성, HTTPS 통신 허용, 프록시 감지를 확인합니다.
Auth는 자격증명 위치와 유효성, 활성 플랜을 확인합니다.
Config는 settings.json 위치, CLAUDE.md 존재, MCP 서버 설정을 확인합니다.
각 항목 옆에는 정상, 오류, 또는 안내 정보 아이콘이 표시됩니다.
진단 결과 요약에 에러 수가 표시되며, --verbose 플래그로 더 자세한 출력을 받을 수 있습니다.
설치 후 가장 먼저 실행해 보고 문제가 있을 때 가장 먼저 다시 실행하는 것이 좋습니다.
