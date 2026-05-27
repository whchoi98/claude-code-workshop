# Slide 9: permissions deep dive

**Part 1: settings.json 구조**

## Code Blocks

### permissions

```json
{
  "permissions": {
    "allow": [
      "Read", "Grep", "Glob",
      "Bash(npm test:*)",
      "Bash(npm run lint)",
      "Bash(git diff:*)",
      "Read(src/**)",
      "Edit(docs/**)"
    ],
    "ask": [
      "Edit(src/**)",
      "Write(**)",
      "Bash(git push:*)",
      "Bash(git commit:*)"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(curl:*)",
      "Bash(* > /etc/*)",
      "Read(**/.env*)",
      "Read(**/secrets/**)"
    ],
    "additionalDirectories": [
      "/Users/me/shared-libs"
    ]
  }
}
```

## Speaker Notes

permissions 옵션을 자세히 살펴봅니다.
deny는 강제 차단입니다.
rm -rf 같은 위험 명령, curl 같은 외부 다운로드, 시스템 파일 쓰기, 환경 파일 읽기 등을 명시 차단합니다.
allow는 자동 허용입니다.
Read, Grep, Glob 같은 안전한 읽기 도구, npm test나 lint, git diff 같은 안전한 명령을 자동 실행 허용합니다.
ask는 사용자 확인을 받습니다.
Edit이나 Write 같은 변경 작업, git push나 commit 같은 외부 영향 명령을 사용자 확인 후 실행합니다.
additionalDirectories는 프로젝트 외부 디렉토리 접근을 허용합니다.
공유 라이브러리 디렉토리 같은 경우 명시 추가합니다.
