# Slide 13: 권한 옵션

**Part 1: claude 명령 기본**

## Code Blocks

### permissions

```bash
# 1. --allowed-tools : 화이트리스트 방식
$ claude -p "이 디렉토리 분석" \
    --allowed-tools Read,Grep,Glob

# 2. --disallowed-tools : 블랙리스트 방식
$ claude -p "..." \
    --disallowed-tools Write,Edit,Bash

# 3. 명령 패턴 (Bash 세분화)
$ claude -p "..." \
    --allowed-tools "Read,Grep,Bash(git diff:*)"

# 4. settings.json과 결합
# settings.json의 deny는 항상 우선
# allowed-tools는 settings의 allow에 추가됨

# 5. 위험한 옵션: --dangerously-skip-permissions
$ claude -p "..." --dangerously-skip-permissions
# 모든 권한 확인 우회 (CI/CD에서만 사용)
# 실수로 prod 환경에 사용하면 큰 사고

# 6. 조합 패턴 (CI 환경)
$ claude -p "PR 리뷰만 작성" \
    --allowed-tools "Read,Grep,Glob,Bash(gh pr:*),Bash(git diff:*)" \
    --disallowed-tools "Write,Edit,Bash(git push:*)" \
    --max-turns 20

# Permissions 우선순위
# deny > 명시 disallowed > 명시 allowed > settings allow
```

## Speaker Notes

권한 옵션을 살펴봅니다.
첫째, --allowed-tools는 화이트리스트 방식입니다.
명시한 도구만 허용됩니다.
안전한 도구만 사용해야 할 때 유용합니다.
둘째, --disallowed-tools는 블랙리스트 방식입니다.
명시한 도구는 차단하고 나머지는 허용합니다.
셋째, Bash 명령은 패턴으로 세분화할 수 있습니다.
Bash 괄호 git diff 콜론 별 형태로 git diff 시작 명령만 허용 가능합니다.
넷째, settings.json과 결합됩니다.
settings의 deny는 항상 우선되고 명시한 allowed-tools는 settings의 allow에 추가됩니다.
다섯째, --dangerously-skip-permissions는 위험한 옵션입니다.
모든 권한 확인을 우회하므로 CI/CD에서만 사용해야 합니다.
실수로 prod 환경에 사용하면 큰 사고가 발생합니다.
여섯째, 조합 패턴입니다.
CI 환경에서 PR 리뷰만 하도록 allowed와 disallowed를 동시 명시하고 max-turns로 무한 루프를 방지합니다.
권한 우선순위는 deny가 최우선이고 명시 disallowed, 명시 allowed, settings allow 순서입니다.
