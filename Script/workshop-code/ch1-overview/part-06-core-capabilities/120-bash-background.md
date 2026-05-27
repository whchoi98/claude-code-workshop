# Slide 120: Bash background

**Part 6: CORE CAPABILITIES**

## Code Blocks

### Bash async

```bash
# 백그라운드 실행 - run_in_background: true
Bash(
  command: "npm run dev",
  description: "개발 서버 시작",
  run_in_background: true,
)
# → shell_id 반환, 즉시 다음 작업 계속

# 출력 확인 - BashOutput 도구
BashOutput(bash_id: "shell-123", filter: "ERROR")
# → 누적된 출력을 가져옴

# 종료 - KillShell 도구
KillShell(shell_id: "shell-123")

# 활용 패턴
- 개발 서버 (npm run dev / docker compose up)
- 파일 워치 (vite, webpack)
- 로그 tail 모니터링
- 장시간 빌드 작업
```

## Speaker Notes

장시간 실행되거나 무한 루프인 명령은 백그라운드로 실행해야 합니다.
Bash 호출 시 run_in_background를 true로 설정하면 명령이 백그라운드로 시작되고 shell_id가 반환되며 Claude는 즉시 다음 작업을 진행할 수 있습니다.
백그라운드 명령의 출력은 BashOutput 도구로 폴링할 수 있는데, bash_id로 식별하고 filter 옵션으로 특정 패턴만 추출할 수 있습니다.
명령을 강제 종료할 때는 KillShell 도구를 사용합니다.
활용 패턴은 개발 서버 시작, 파일 워치 모드 빌드, 로그 tail 모니터링, 장시간 빌드 작업 같은 시나리오입니다.
이 기능이 있어 Claude Code가 풀스택 개발 워크플로를 자동화할 수 있습니다.
