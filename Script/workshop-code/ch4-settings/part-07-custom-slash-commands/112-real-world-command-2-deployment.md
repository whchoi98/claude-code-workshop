# Slide 112: Real-world command 2: Deployment

**Part 7: CUSTOM SLASH COMMANDS**

## Code Blocks

### deploy

```bash
# .claude/commands/deploy.md
---
description: 표준 배포 절차 (dev/staging/prod)
argument-hint: <env>
allowed-tools:
  - Read
  - Bash(git status)
  - Bash(git log:*)
  - Bash(npm test)
  - Bash(npm run build)
  - Bash(npm run deploy:*)
  - Bash(curl https://hooks.slack.com/*)
model: claude-sonnet-4-5
---

$ARGUMENTS 환경에 배포를 진행해 주세요.

# 사전 점검
1. git status가 깨끗한가? (dirty면 중단)
2. 마지막 커밋이 main에 있는가?
3. 다음 명령 모두 통과 확인:
   - npm test
   - npm run build
   - npm run lint

# 배포 절차
1. 배포 전 Slack #deploys 채널에 시작 알림
   curl -X POST $SLACK_HOOK \
     -d '{"text":"🚀 Deploying to $ARGUMENTS"}'

2. npm run deploy:$ARGUMENTS 실행

3. 배포 완료 후 health check
   curl https://$ARGUMENTS.company.com/health
   응답이 200 OK가 아니면 즉시 rollback 안내

4. Slack에 완료 알림
   curl -X POST $SLACK_HOOK \
     -d '{"text":"✅ Deployed to $ARGUMENTS"}'

5. 최종 보고: 배포된 commit hash, 환경, 시간

# 주의
- prod 배포는 사용자 확인 필수
```

## Speaker Notes

실전 명령 두 번째는 표준 배포 절차입니다.
frontmatter에 argument-hint로 env 인자를 받음을 명시합니다.
allowed-tools에 배포에 필요한 정확한 명령만 명시합니다.
git status, git log, npm test, build, deploy, Slack hook curl까지 좁게 허용합니다.
명령 본문은 사전 점검과 배포 절차로 구성됩니다.
사전 점검 3가지는 git 상태 깨끗함, 마지막 커밋이 main에 있음, 모든 테스트와 빌드 통과입니다.
배포 절차는 5단계입니다.
1단계 Slack에 시작 알림을 보냅니다.
2단계 npm run deploy 명령을 환경에 맞춰 실행합니다.
3단계 health check로 200 OK 응답을 확인하고 실패 시 즉시 rollback 안내합니다.
4단계 Slack에 완료 알림을 보냅니다.
5단계 최종 보고로 배포 commit hash, 환경, 시간을 요약합니다.
주의 사항으로 prod 배포는 사용자 확인이 필수임을 명시합니다.
호출은 /deploy staging이나 /deploy prod 같은 형태입니다.
