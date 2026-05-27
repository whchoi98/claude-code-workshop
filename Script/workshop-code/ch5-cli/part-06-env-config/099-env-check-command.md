# Slide 99: 환경변수 점검 명령

**Part 6: 환경변수와 설정**

## Code Blocks

### inspect

```bash
# 1. 종합 진단
$ claude doctor

Claude Code v1.2.0
✓ Node.js v20.10.0
✓ Settings: ~/.claude/settings.json (valid)
✓ Authentication:
  - Type: AWS Bedrock
  - Region: us-east-1
  - Profile: production
✓ Network:
  - HTTPS_PROXY: http://proxy.company.com:8080
  - NO_PROXY: localhost,.company.com
  - CA: /etc/ssl/certs/company-ca.pem
✓ MCP servers: 5 connected
  - github: ✓
  - slack: ✓
  - jira: ✓ (auth via env)
  - postgres: ✓
  - filesystem: ✓
⚠ Log level: debug (운영에서는 info 권장)
✗ Disk space: 92% used

# 2. 상세 모드
$ claude doctor --verbose

# Settings 전체 출력 + 환경변수 값 + 모든 MCP 도구 목록

# 3. 환경변수만 확인
$ env | grep -i claude
$ env | grep -i anthropic
$ env | grep -i aws
$ env | grep -i proxy

# 4. 한 번에 모두 출력
$ env | grep -iE 'claude|anthropic|aws|gcp|proxy|ca_cert'

# 5. settings 파일 위치 확인
$ claude doctor --verbose | grep -i settings
$ ls -la ~/.claude/

# 6. 디버그 모드로 환경변수 로딩 확인
$ CLAUDE_CODE_LOG_LEVEL=debug claude --version 2>&1 | \
    grep -i 'loading'

# 7. 트러블슈팅 체크리스트
- export가 셸에 적용됐는지 (.bashrc, .zshrc 확인)
- 새 터미널에서도 환경변수가 보이는지
- direnv 사용 시 direnv allow 했는지
- /etc/environment의 시스템 전역 변수
- CI에서는 secrets로 등록했는지
```

## Speaker Notes

환경변수 점검 명령들입니다.
1번 claude doctor는 종합 진단입니다.
Node.js 버전, Settings 파일 유효성, Authentication 정보, Network 설정, MCP 서버 상태, 로그 레벨, 디스크 공간까지 한눈에 보여줍니다.
2번 --verbose 옵션은 상세 모드입니다.
Settings 전체와 환경변수 값, 모든 MCP 도구 목록까지 출력합니다.
3번 환경변수만 확인하려면 env 명령에 grep으로 필터링합니다.
claude, anthropic, aws, proxy 같은 키워드별로 확인합니다.
4번 한 번에 모두 출력하려면 grep의 -E 옵션으로 여러 패턴을 OR로 매칭합니다.
5번 settings 파일 위치 확인은 doctor의 verbose 출력이나 ls 명령으로 합니다.
6번 디버그 모드로 환경변수 로딩 과정을 추적할 수 있습니다.
7번 트러블슈팅 체크리스트가 중요합니다.
export가 셸에 적용됐는지 .bashrc나 .zshrc 확인, 새 터미널에서 보이는지, direnv allow 했는지, 시스템 전역 변수 위치, CI secrets 등록 여부를 단계별로 확인합니다.
