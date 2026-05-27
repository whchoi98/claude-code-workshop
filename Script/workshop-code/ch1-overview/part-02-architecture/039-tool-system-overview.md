# Slide 39: Tool System Overview

**Part 2: ARCHITECTURE**

## Code Blocks

### TOOL CALL CYCLE

```
Tool Call Flow

  1. Claude 응답 → tool_use 블록 (name, input)
  2. Tool Router → 도구 식별 → 권한 검사
  3. Permission Layer → allow / ask / deny 결정
  4. Tool Executor → 실제 도구 실행 (Read/Edit/Bash/...)
  5. 결과 → tool_result → 다음 Claude 호출의 컨텍스트로

Built-in Tools
  Read · Edit · Write · NotebookEdit · Bash · Grep · Glob ·
  WebSearch · WebFetch · TodoWrite · Task (subagent dispatch)

MCP Tools
  외부 서버가 제공하는 도구를 동일한 인터페이스로 호출
```

## Speaker Notes

도구 시스템의 전체 개요를 살펴봅니다.
Tool Call Flow는 5단계로 동작합니다.
1단계 Claude가 응답으로 tool_use 블록을 생성합니다.
2단계 Tool Router가 도구를 식별하고 권한 검사를 시작합니다.
3단계 Permission Layer가 allow, ask, deny 중 하나의 결정을 내립니다.
4단계 Tool Executor가 실제 도구를 실행합니다.
5단계 실행 결과가 tool_result로 다음 Claude 호출의 컨텍스트로 전달됩니다.
내장 도구는 Read, Edit, Write, NotebookEdit, Bash, Grep, Glob, WebSearch, WebFetch, TodoWrite, Task 등 11가지 이상이며, MCP 도구는 외부 서버가 제공하는 도구를 동일한 인터페이스로 호출할 수 있게 해 줍니다.
