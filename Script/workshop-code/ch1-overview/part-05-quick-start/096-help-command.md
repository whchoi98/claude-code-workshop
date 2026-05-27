# Slide 96: /help 명령

**Part 5: QUICK START**

## Code Blocks

### /help

```
> /help

Available commands:

Session
  /clear          Clear context and start fresh
  /compact        Summarize older messages
  /status         Show session info and usage

Configuration
  /init           Initialize CLAUDE.md
  /memory         Open CLAUDE.md in editor
  /model <name>   Switch model (sonnet, opus, haiku)
  /cost           Show token usage and cost

Auth
  /login          Sign in
  /logout         Sign out

Tools
  /tools          List available tools
  /mcp            List MCP servers

Other
  /exit, /quit    End session
  /help           Show this help
```

## Speaker Notes

/help 명령으로 표시되는 전체 명령 목록입니다.
크게 네 그룹으로 정리되는데, Session 그룹은 컨텍스트 제어 명령으로 /clear, /compact, /status가 있습니다.
Configuration 그룹은 /init, /memory, /model, /cost로 동작을 설정합니다.
Auth 그룹은 /login과 /logout입니다.
Tools 그룹은 /tools로 현재 사용 가능한 도구 목록, /mcp로 설정된 MCP 서버 목록을 확인합니다.
/exit이나 /quit으로 세션을 종료할 수 있습니다.
모든 명령은 슬래시로 시작하며 자동완성도 지원됩니다.
새로운 사용자가 가장 먼저 익혀야 할 명령들입니다.
