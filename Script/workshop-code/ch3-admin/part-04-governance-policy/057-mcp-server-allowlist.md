# Slide 57: MCP server allowlist

**Part 4: GOVERNANCE & POLICY**

## Code Blocks

### MCP Policy

```bash
# managed-settings.json에 MCP 통제 추가
{
  "mcpPolicy": {
    "mode": "allowlist",
    "allowedServers": [
      "jira-internal",
      "confluence-internal",
      "gitlab-internal",
      "filesystem",
      "github"
    ],
    "deniedServers": [
      "any-untrusted-server"
    ],
    "requireApproval": [
      "shell",
      "browser"
    ]
  }
}

# 효과
- 사용자가 .claude/settings.json에 추가한
  MCP 서버 중 allowlist에 없으면 무시
- deniedServers에 명시된 서버는 차단
- requireApproval은 매번 사용자 확인

# 사내 MCP 서버 사전 등록 (자동 설정)
{
  "mcpServers": { ... 사내 표준 서버들 ... }
}
이를 managed-settings에 함께 포함하면 모든 PC에 자동 등록
```

## Speaker Notes

MCP 서버 화이트리스트로 거버넌스를 강화합니다.
managed-settings.json에 mcpPolicy 섹션을 추가합니다.
mode를 allowlist로 설정하면 명시된 서버만 사용 가능합니다.
allowedServers에 jira-internal, confluence-internal, gitlab-internal, filesystem, github 같은 사내 표준 서버를 명시합니다.
deniedServers에는 신뢰되지 않은 외부 서버를 명시 차단합니다.
requireApproval에는 shell이나 browser처럼 강력한 서버를 두어 매번 사용자 확인을 받게 합니다.
효과는 명확합니다.
사용자가 .claude/settings.json에 추가한 MCP 서버 중 allowlist에 없으면 무시됩니다.
deniedServers에 명시된 서버는 차단됩니다.
requireApproval은 매번 사용자 확인이 필요합니다.
사내 MCP 서버를 사전 등록하면 모든 PC에 자동으로 사내 표준 서버가 적용됩니다.
mcpServers 섹션을 managed-settings에 함께 포함하면 됩니다.
