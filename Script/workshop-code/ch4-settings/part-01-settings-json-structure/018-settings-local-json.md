# Slide 18: settings.local.json

**Part 1: settings.json 구조**

## Code Blocks

### local override

```bash
# .gitignore에 추가
.claude/settings.local.json

# .claude/settings.local.json (개인 오버라이드)
{
  "permissions": {
    "allow": [
      "Bash(npm run dev:*)",
      "Read(/Users/me/notes/**)"
    ]
  },
  "mcpServers": {
    "my-personal-jira": {
      "command": "npx",
      "args": ["-y", "@my-org/jira-mcp"],
      "env": { "JIRA_TOKEN": "my-personal-token" }
    }
  }
}

# 효과
- 팀 설정은 그대로 유지
- 본인만의 권한과 MCP 추가 가능
- 다른 팀원에게 영향 없음
```

## Speaker Notes

settings.local.json은 프로젝트별 개인 오버라이드 파일입니다.
프로젝트의 .claude/ 디렉토리에 있지만 Git에는 커밋하지 않습니다.
.gitignore에 .claude/settings.local.json을 추가해야 합니다.
사용 시나리오는 본인만의 프로젝트별 설정을 덮어쓸 때입니다.
예시를 봅니다.
permissions의 allow에 npm run dev 명령이나 개인 notes 디렉토리 접근을 추가합니다.
mcpServers에 개인 토큰으로 인증되는 my-personal-jira 서버를 추가합니다.
효과는 명확합니다.
팀 .claude/settings.json은 그대로 유지됩니다.
본인만의 권한과 MCP를 추가할 수 있습니다.
다른 팀원에게 영향이 없습니다.
조직 표준은 지키되 개인 워크플로에 맞춰 확장하는 패턴입니다.
