# Slide 70: stdio transport details

**Part 5: MCP 기본과 공식 서버**

## Code Blocks

### stdio

```bash
# settings.json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/me/Documents",
        "/Users/me/Projects"
      ],
      "env": {
        "LOG_LEVEL": "info"
      }
    }
  }
}

# 동작 흐름
1. Claude Code 시작 시 npx 명령 실행
2. MCP 서버가 자식 프로세스로 시작됨
3. stdin/stdout으로 JSON-RPC 메시지 교환
4. Claude Code 종료 시 자식 프로세스도 종료

# 장점
- 가장 빠른 응답 (네트워크 X)
- 별도 인프라 불필요
- 자격증명을 환경변수로 안전 전달

# 단점
- 같은 머신에서만 동작
- 서버 재사용 불가 (각 Claude 인스턴스마다 별도)
- 자원 소비 (각 서버마다 프로세스)
```

## Speaker Notes

stdio 통신 방식을 자세히 살펴봅니다.
settings.json 예시를 봅니다.
command에 실행할 명령을 명시합니다.
npx를 사용하면 npm 패키지를 즉시 실행할 수 있어 편리합니다.
args에 npx 인자를 배열로 전달합니다.
-y는 자동 yes, 그 다음에 패키지 이름과 패키지 인자들이 옵니다.
filesystem 서버의 경우 접근 허용할 디렉토리 목록을 인자로 받습니다.
env에 환경변수를 주입할 수 있습니다.
동작 흐름을 봅니다.
Claude Code 시작 시 npx 명령을 실행합니다.
MCP 서버가 자식 프로세스로 시작되고 stdin과 stdout으로 JSON-RPC 메시지를 교환합니다.
Claude Code 종료 시 자식 프로세스도 종료됩니다.
장점은 가장 빠른 응답, 별도 인프라 불필요, 환경변수로 안전한 자격증명 전달입니다.
단점은 같은 머신에서만 동작, 서버 재사용 불가, 자원 소비입니다.
