# Slide 24: Bash patterns deep

**Part 2: PERMISSIONS 심화**

## Code Blocks

### Bash patterns

```bash
# 1. 정확 매칭 (가장 안전)
"Bash(npm test)"           # 'npm test' 이 명령만
"Bash(git status)"          # 'git status' 이 명령만

# 2. 접두사 매칭 (':*' 사용)
"Bash(npm test:*)"          # 'npm test --watch' 등 모두
"Bash(git diff:*)"          # 'git diff', 'git diff HEAD~1' 등

# 3. 부분 패턴 (정규식 비슷)
"Bash(* > /tmp/*)"          # /tmp로의 리디렉션만
"Bash(*sudo*)"              # sudo 포함 명령 (deny에서)

# 4. 자주 쓰는 안전한 패턴 (allow)
"Bash(npm test:*)",
"Bash(npm run lint)",
"Bash(npm run build)",
"Bash(npm run dev:*)",
"Bash(git status)",
"Bash(git diff:*)",
"Bash(git log:*)",
"Bash(git show:*)",
"Bash(ls:*)",
"Bash(pwd)"

# 5. 위험 패턴 (deny에 추가)
"Bash(rm -rf:*)",
"Bash(rm -f:*)",
"Bash(sudo:*)",
"Bash(chmod:*)",
"Bash(* > /etc/*)",
"Bash(curl:*)", "Bash(wget:*)"
```

## Speaker Notes

Bash 패턴을 더 깊이 살펴봅니다.
첫째, 정확 매칭이 가장 안전합니다.
Bash 괄호 npm test는 정확히 npm test 이 명령만 허용합니다.
둘째, 접두사 매칭은 콜론 별을 사용합니다.
npm test 콜론 별은 npm test --watch나 npm test path 같은 변형을 모두 허용합니다.
셋째, 부분 패턴은 정규식과 비슷합니다.
별 > /tmp/별은 /tmp 디렉토리로의 리디렉션만 허용합니다.
별 sudo 별은 sudo가 포함된 모든 명령에 매칭됩니다.
넷째, 자주 쓰는 안전한 패턴들을 allow에 추가합니다.
npm test, lint, build, dev, git의 status, diff, log, show 같은 읽기 전용 명령이 안전합니다.
다섯째, 위험 패턴들을 deny에 추가합니다.
rm -rf, sudo, chmod, 시스템 디렉토리 쓰기, curl과 wget 같은 외부 다운로드를 차단합니다.
