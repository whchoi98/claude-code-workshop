# Slide 119: Bash basics

**Part 6: CORE CAPABILITIES**

## Code Blocks

### Bash sync

```bash
# Bash 도구 - 동기 실행 기본
Bash(
  command: "npm test -- user.test.js",
  description: "사용자 테스트 실행",   # 필수
  timeout: 60000,                       # ms, 기본 120초, 최대 600초
)

# 다중 명령은 && / || / ; 로
Bash(command: "cd src && npm install && npm run build")

# 표준 출력과 표준 에러 모두 수집
- stdout: 명령 정상 출력
- stderr: 에러 출력
- exit_code: 0이 정상, 비0이 실패

# 안전 권장사항
- 절대 경로 사용 권장 (cd 의존도 줄이기)
- 위험 명령 (rm -rf, sudo, curl|sh) 자동 차단됨
- 파일 변경은 Bash 대신 Edit/Write 사용
```

## Speaker Notes

Bash 도구는 셸 명령을 실행하는 도구입니다.
command 인자에 실행할 명령을, description 인자에 명령의 목적을 자연어로 기술합니다.
description은 필수이며 권한 승인 화면에 표시되어 사용자가 의도를 파악할 수 있게 해 줍니다.
timeout은 밀리초 단위이며 기본 120초, 최대 600초까지 지정 가능합니다.
다중 명령은 &&, ||, 세미콜론으로 연결할 수 있습니다.
stdout과 stderr를 모두 수집하며 exit_code로 성공 여부를 판단합니다.
안전 권장사항으로 절대 경로 사용을 권장하며, rm -rf, sudo, curl pipe sh 같은 위험 명령은 자동으로 차단됩니다.
파일 변경은 Bash 대신 Edit이나 Write 도구를 사용하는 것이 안전합니다.
