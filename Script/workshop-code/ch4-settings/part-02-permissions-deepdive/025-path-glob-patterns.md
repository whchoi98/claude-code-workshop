# Slide 25: Path glob patterns

**Part 2: PERMISSIONS 심화**

## Code Blocks

### glob patterns

```bash
# 1. 단일 디렉토리
"Read(src/**)"              # src 하위 모든
"Read(src/api/**)"          # src/api 하위만
"Read(./README.md)"         # 정확한 파일

# 2. 파일 확장자 패턴
"Read(**/*.md)"             # 모든 마크다운
"Edit(**/*.{js,ts})"        # JS와 TS 파일
"Read(**/*.{yaml,yml})"     # YAML 파일

# 3. 여러 경로 조합
"Read(src/**, tests/**, docs/**)"
"Edit(src/**)"               # 작성은 src만

# 4. 제외 패턴 (deny와 조합)
allow: "Read(**)"
deny:  "Read(**/.env*)"      # .env 파일은 제외
deny:  "Read(**/node_modules/**)"

# 5. 절대 경로
"Read(/Users/me/shared/**)"  # 홈 외부 디렉토리
"Read(/etc/claude/**)"       # 시스템 디렉토리 (특별)

# 6. 현재 프로젝트 외부 접근
# settings.json의 additionalDirectories
{
  "permissions": {
    "additionalDirectories": ["/Users/me/shared-libs"],
    "allow": ["Read(/Users/me/shared-libs/**)"]
  }
}
```

## Speaker Notes

경로 글롭 패턴 작성법을 자세히 봅니다.
첫째, 단일 디렉토리 패턴입니다.
src 별별은 src 하위 모든 것을, src api 별별은 src/api 하위만 의미합니다.
특정 파일은 점 슬래시 파일명으로 명시할 수 있습니다.
둘째, 파일 확장자 패턴입니다.
별별 점md는 모든 마크다운 파일, 별별 점js,ts 중괄호는 JS와 TS 파일에 동시 적용됩니다.
셋째, 여러 경로 조합입니다.
괄호 안에 콤마로 여러 경로를 묶을 수 있습니다.
넷째, 제외 패턴은 deny와 조합해서 만듭니다.
allow에 Read 별별로 모두 허용한 후 deny에 환경 파일이나 node_modules를 차단합니다.
다섯째, 절대 경로도 사용 가능합니다.
Users me shared 별별은 홈 외부 디렉토리에 접근할 때 사용합니다.
여섯째, 현재 프로젝트 외부 접근입니다.
additionalDirectories에 디렉토리를 명시한 후 allow에 그 경로를 추가합니다.
