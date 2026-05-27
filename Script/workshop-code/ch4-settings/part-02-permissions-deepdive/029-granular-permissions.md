# Slide 29: Granular permissions

**Part 2: PERMISSIONS 심화**

## Code Blocks

### Role-based

```bash
# 시나리오: 신입 개발자 vs 시니어 개발자

# 신입 개발자 (보수적)
{
  "permissions": {
    "allow": [
      "Read(src/**)", "Read(tests/**)", "Read(docs/**)",
      "Grep", "Glob",
      "Bash(npm test:*)", "Bash(npm run lint)"
    ],
    "ask": [
      "Edit(src/**)", "Edit(tests/**)",
      "Write(**)", "Bash(git commit:*)"
    ],
    "deny": [
      "Edit(.github/**)",  # CI 설정 변경 금지
      "Edit(scripts/**)",   # 빌드 스크립트 변경 금지
      "Bash(npm run deploy:*)",
      "Bash(git push:*)"
    ]
  }
}

# 시니어 개발자 (관대)
{
  "permissions": {
    "allow": [
      "Read", "Grep", "Glob",
      "Edit(src/**)", "Edit(tests/**)", "Edit(docs/**)",
      "Bash(npm:*)", "Bash(git:*)"
    ],
    "ask": ["Write(**)", "Bash(git push:*)"],
    "deny": ["Bash(rm -rf:*)", "Bash(sudo:*)"]
  }
}
```

## Speaker Notes

역할별 차등 권한 설계를 살펴봅니다.
신입 개발자와 시니어 개발자에게 다른 권한을 부여하는 예시입니다.
신입 개발자는 보수적인 권한을 가집니다.
allow에 Read 도구와 안전한 빌드 명령만 자동 허용합니다.
ask에 Edit과 Write를 두어 모든 변경 작업을 확인 받습니다.
deny에 .github 디렉토리, scripts 디렉토리, deploy 명령, git push를 명시 차단합니다.
CI 설정이나 빌드 스크립트 같은 중요 파일을 보호합니다.
시니어 개발자는 관대한 권한을 가집니다.
allow에 Read와 Edit 도구를 광범위 허용합니다.
Bash npm 별과 git 별로 거의 모든 npm과 git 명령을 자동 허용합니다.
ask에는 Write와 git push만 두어 영향이 큰 작업만 확인 받습니다.
deny는 rm -rf와 sudo 같은 명백한 위험만 차단합니다.
승급 시 권한이 자연스럽게 확대되는 경로를 설계할 수 있습니다.
