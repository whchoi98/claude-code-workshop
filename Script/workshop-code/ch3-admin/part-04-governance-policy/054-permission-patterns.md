# Slide 54: Permission patterns

**Part 4: GOVERNANCE & POLICY**

## Code Blocks

### Patterns

```bash
# 1. 도구 이름만 (전체 허용)
"Read", "Grep", "Glob"

# 2. 경로 글롭 패턴
"Read(src/**)"           # src 디렉토리만 읽기 가능
"Edit(docs/**)"          # docs만 편집 가능
"Read(**/*.md)"          # 모든 .md 파일만 읽기

# 3. Bash 명령 패턴
"Bash(npm test:*)"       # npm test 시작하는 모든 명령
"Bash(git diff:*)"       # git diff 변형들
"Bash(npm run lint)"     # 정확히 이 명령만

# 4. 부정 (deny에서만 의미)
"Read(**/.env*)"         # .env 파일 차단
"Read(**/credentials/**)"  # credentials 디렉토리 전체 차단
"Bash(*sudo*)"           # sudo 포함 명령 모두 차단

# 5. 와일드카드 주의
"Bash(*)"  # 모든 Bash 허용 (위험)
"Edit(*)"  # 모든 Edit 허용 (주의)

# 6. 우선순위
# 더 구체적인 패턴이 일반 패턴보다 우선
# allow Bash(npm test:*) + deny Bash(npm:*) → npm test만 허용
```

## Speaker Notes

권한 패턴 작성법을 자세히 살펴봅니다.
6가지 패턴 유형이 있습니다.
첫째, 도구 이름만 적으면 해당 도구 전체를 허용합니다.
둘째, 경로 글롭 패턴입니다.
Read 괄호 src 별별은 src 디렉토리만 읽을 수 있게 합니다.
별별dot md는 모든 마크다운 파일에 적용됩니다.
셋째, Bash 명령 패턴입니다.
Bash npm test 콜론 별은 npm test로 시작하는 모든 명령을 허용합니다.
Bash npm run lint는 정확히 이 명령만 허용합니다.
넷째, 부정 패턴은 deny에서 주로 의미가 있습니다.
환경 파일이나 credentials 디렉토리, sudo 포함 명령을 차단합니다.
다섯째, 와일드카드는 주의가 필요합니다.
Bash 별이나 Edit 별은 모든 호출을 허용하므로 위험합니다.
여섯째, 우선순위는 더 구체적인 패턴이 일반 패턴보다 우선합니다.
allow npm test 콜론 별과 deny npm 콜론 별을 함께 두면 npm test만 허용됩니다.
