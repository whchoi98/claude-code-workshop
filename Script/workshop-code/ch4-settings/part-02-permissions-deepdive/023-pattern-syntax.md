# Slide 23: Pattern syntax

**Part 2: PERMISSIONS 심화**

## Code Blocks

### syntax

```bash
# 1. 도구 이름만 - 도구 전체 허용
"Read", "Grep", "Glob", "Edit", "Write"

# 2. 경로 글롭 - 도구 + 경로 제한
"Read(src/**)"           # src 하위 모든 파일
"Read(**/*.md)"          # 모든 .md 파일
"Edit(docs/**)"          # docs 디렉토리만
"Read(src/**, tests/**)" # 여러 경로 콤마 구분

# 3. Bash 명령 패턴
"Bash(npm test:*)"       # npm test로 시작하는 모든 명령
"Bash(npm test)"         # 정확히 'npm test'만
"Bash(git diff:*)"       # git diff 변형들
"Bash(git status)"       # 정확한 명령

# 4. 다중 명령 패턴
"Bash(npm test:*, npm run lint, npm run build)"

# 5. 부정 (deny에서 의미)
"Read(**/.env*)"         # .env 파일 차단
"Bash(*sudo*)"           # sudo 포함 명령 차단
"Read(/etc/**)"          # 시스템 디렉토리 차단

# 6. 와일드카드 (주의)
"Bash(*)"                # 모든 Bash 허용 (위험!)
"Edit(*)"                # 모든 Edit 허용 (주의)
```

## Speaker Notes

패턴 문법의 다양한 표현 방법을 정리합니다.
첫째, 도구 이름만 적으면 해당 도구 전체가 적용됩니다.
Read, Grep, Glob, Edit, Write 같은 형태입니다.
둘째, 경로 글롭으로 도구와 경로를 함께 제한합니다.
Read 괄호 src 별별은 src 하위 모든 파일을 의미합니다.
별별dot md는 모든 마크다운 파일에 적용됩니다.
셋째, Bash 명령 패턴입니다.
npm test 콜론 별은 npm test로 시작하는 모든 명령을 허용합니다.
콜론 없이 정확한 명령만 적으면 그것만 허용됩니다.
넷째, 다중 명령 패턴입니다.
괄호 안에 콤마로 여러 명령을 묶을 수 있습니다.
다섯째, 부정 표현은 주로 deny에서 사용됩니다.
환경 파일 차단, sudo 포함 명령 차단, 시스템 디렉토리 차단 같은 패턴입니다.
여섯째, 와일드카드는 주의가 필요합니다.
Bash 별은 모든 Bash 호출을 허용하므로 매우 위험합니다.
