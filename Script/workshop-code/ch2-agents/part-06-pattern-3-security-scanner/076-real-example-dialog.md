# Slide 76: Real example dialog

**Part 6: PATTERN 3 / SECURITY SCANNER**

## Code Blocks

### security demo

```bash
> 방금 머지된 PR #245의 보안 점검을 해 주세요.

[메인] security-scanner를 호출합니다.
       → Task(security-scanner, "PR #245 보안 점검")

[sec ] PR diff 분석 중...
        Bash: git diff main..245 → 12 files changed

        의존성 점검 중...
        Bash: npm audit → 3 vulnerabilities found

        코드 분석 중...
        Read+Grep: SQL 패턴, eval, exec, innerHTML

        시크릿 검사 중...
        Grep: API_KEY|TOKEN|PASSWORD patterns

## Security Report

### Critical (2)
- [SQL Injection] src/api/users.js:78 (CWE-89)
  외부 input이 query 문자열에 직접 삽입.
  수정안: parameterized query 사용

- [Secret Leak] src/config/aws.js:12 (CWE-798)
  AKIA로 시작하는 AWS 키 하드코딩.
  수정안: 환경변수로 이동

### High (1)
- [Outdated Dep] lodash 4.17.19 → 4.17.21
  CVE-2021-23337 (Prototype Pollution)

[메인] Critical 2건, High 1건 발견. 머지 차단 권장.
```

## Speaker Notes

Security Scanner의 실전 대화 예시입니다.
사용자가 방금 머지된 PR 245의 보안 점검을 요청합니다.
메인은 security-scanner를 호출합니다.
에이전트가 단계별로 분석합니다.
첫 단계로 PR diff를 분석해 12개 파일이 변경되었음을 확인합니다.
두 번째로 npm audit으로 의존성을 점검해 3개의 취약점을 발견합니다.
세 번째로 코드 분석을 진행합니다.
SQL 패턴, eval, exec, innerHTML 같은 위험 패턴을 Grep으로 검색합니다.
네 번째로 시크릿 검사를 합니다.
API_KEY, TOKEN, PASSWORD 패턴을 검색합니다.
결과를 보고합니다.
Critical 2건이 발견됩니다.
SQL Injection이 src/api/users.js 78번 라인에서 발견됩니다.
CWE-89 분류이며 parameterized query 사용을 권장합니다.
Secret Leak이 src/config/aws.js 12번 라인에서 발견됩니다.
AKIA로 시작하는 AWS 키 하드코딩으로 환경변수 이동을 권장합니다.
High 1건은 lodash 버전 업그레이드 권장입니다.
메인은 머지 차단을 권장합니다.
