# Slide 97: MCP 환경변수

**Part 6: 환경변수와 설정**

## Code Blocks

### MCP env

```bash
# 1. MCP 서버 자격증명 (settings.json에서 참조)
# ~/.claude/settings.json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GH_TOKEN}"
      }
    },
    "slack": {
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}"
      }
    },
    "postgres": {
      "env": {
        "POSTGRES_URL": "${DATABASE_URL}"
      }
    }
  }
}

# 2. 셸 환경변수로 주입
export GH_TOKEN=ghp_...
export SLACK_BOT_TOKEN=xoxb-...
export DATABASE_URL=postgres://...

# 3. .env 파일 사용 (dotenv-cli)
# .env
GH_TOKEN=ghp_xxx
SLACK_BOT_TOKEN=xoxb-yyy

# 명령 실행
$ dotenv -e .env claude -p "..."

# 4. 사내 secret manager 통합
# AWS Secrets Manager
$ export GH_TOKEN=$(aws secretsmanager get-secret-value \
    --secret-id github-token --query SecretString --output text)
$ claude -p "..."

# HashiCorp Vault
$ export GH_TOKEN=$(vault kv get -field=token secret/github)

# 1Password CLI
$ export GH_TOKEN=$(op read "op://Engineering/GitHub/token")

# 5. CI/CD에서 (GitHub Actions)
# Secrets로 등록 후
env:
  GH_TOKEN: ${{ secrets.GH_TOKEN }}
  SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}

# 6. 디버깅
$ claude /mcp logs github   # 토큰 인식 확인
```

## Speaker Notes

MCP 환경변수로 서버별 자격증명을 주입합니다.
1번 settings.json에서 환경변수 참조 패턴입니다.
mcpServers의 각 서버 env 블록에 달러 괄호로 환경변수를 참조합니다.
GitHub는 GITHUB_PERSONAL_ACCESS_TOKEN, Slack은 SLACK_BOT_TOKEN, Postgres는 POSTGRES_URL이 표준입니다.
2번 셸 환경변수로 직접 export합니다.
3번 .env 파일 사용 패턴은 dotenv-cli를 활용합니다.
dotenv -e .env claude로 실행하면 .env 파일의 변수를 자동 주입합니다.
4번 사내 secret manager 통합이 권장됩니다.
AWS Secrets Manager, HashiCorp Vault, 1Password CLI 같은 도구로 안전하게 가져옵니다.
5번 CI/CD에서는 secrets로 등록 후 env 블록에서 참조합니다.
6번 디버깅은 claude /mcp logs로 토큰이 정상 인식되었는지 확인할 수 있습니다.
401 같은 인증 에러가 나면 환경변수가 제대로 전달되었는지 가장 먼저 확인해야 합니다.
