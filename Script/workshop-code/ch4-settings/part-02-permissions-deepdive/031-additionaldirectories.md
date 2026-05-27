# Slide 31: additionalDirectories

**Part 2: PERMISSIONS 심화**

## Code Blocks

### additionalDirs

```bash
# 기본 동작
Claude Code는 현재 작업 디렉토리(cwd) 외부 접근을 차단합니다.
홈 디렉토리나 시스템 디렉토리는 기본적으로 못 들어갑니다.

# 외부 디렉토리 허용 방법
{
  "permissions": {
    "additionalDirectories": [
      "/Users/me/shared-libs",
      "/Users/me/personal-notes",
      "~/.config/myapp"
    ],
    "allow": [
      "Read(/Users/me/shared-libs/**)",
      "Read(/Users/me/personal-notes/**)"
    ]
  }
}

# 주의 사항
1. additionalDirectories로 추가만 가능하지 권한이 자동 부여 X
2. allow에도 명시적으로 경로 패턴 추가 필요
3. 절대 경로 또는 홈 디렉토리 expansion (~) 가능

# 보안 권장
- 가능한 한 좁은 디렉토리만 추가
- /Users/me 같은 홈 전체는 절대 피하기
- 추가 후 deny 패턴으로 민감 파일 명시 차단
```

## Speaker Notes

additionalDirectories는 프로젝트 외부 접근을 허용하는 옵션입니다.
기본 동작을 먼저 이해해야 합니다.
Claude Code는 현재 작업 디렉토리, 즉 cwd 외부 접근을 차단합니다.
홈 디렉토리나 시스템 디렉토리는 기본적으로 들어갈 수 없습니다.
외부 디렉토리를 허용하려면 additionalDirectories에 명시합니다.
예시처럼 shared-libs나 personal-notes 디렉토리를 추가합니다.
중요한 점은 additionalDirectories만으로는 부족하다는 것입니다.
allow에도 그 경로 패턴을 명시적으로 추가해야 합니다.
additionalDirectories는 접근 가능한 영역을 확장하는 것일 뿐이고 실제 권한은 별도로 부여해야 합니다.
절대 경로나 홈 디렉토리 expansion 물결표를 사용할 수 있습니다.
보안 권장 사항은 명확합니다.
가능한 한 좁은 디렉토리만 추가하시고 홈 전체 같은 광범위 추가는 피하시기 바랍니다.
추가 후 deny 패턴으로 민감 파일을 명시 차단합니다.
