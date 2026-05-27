# Slide 42: Permission Model

**Part 2: ARCHITECTURE**

## Code Blocks

### settings.json

```bash
# settings.json
{
  "permissions": {
    "allow": [
      "Read(**)",
      "Bash(npm test:*)",
      "Bash(git status)",
      "Bash(git diff:*)"
    ],
    "ask": [
      "Edit(**)",
      "Write(**)"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(sudo:*)",
      "Bash(curl * | sh)"
    ]
  }
}
```

## Speaker Notes

권한 모델은 Claude Code의 안전성을 보장하는 핵심 메커니즘입니다.
settings.json의 permissions 섹션에서 세 가지 규칙을 정의할 수 있는데, allow는 자동으로 허용할 도구 호출, ask는 사용자 확인을 요구할 도구, deny는 거부할 도구입니다.
화면 예시처럼 글롭 패턴을 사용해 세밀하게 지정할 수 있는데, Read 도구는 모든 파일에 대해 자동 허용하고, Bash 도구는 npm test나 git 명령만 자동 허용하며, Edit과 Write는 매번 확인을 받고, rm -rf나 sudo, curl pipe sh 같은 위험 명령은 명시적으로 거부합니다.
이 규칙은 사용자별, 프로젝트별, 엔터프라이즈 정책별로 계층적으로 적용됩니다.
