# Slide 115: Edit Find Replace

**Part 6: CORE CAPABILITIES**

## Code Blocks

### Edit tool

```bash
# Edit 도구의 기본 형태
Edit(
  file_path: "src/services/user.js",
  old_str: "return user;",
  new_str: "if (!user) throw new NotFoundError();\n  return user;"
)

# 핵심 규칙
- old_str은 파일에서 유일해야 함 (중복 시 에러)
- 들여쓰기까지 정확히 일치해야 함
- 충분한 컨텍스트 포함 권장 (앞뒤 2-3줄)
- replace_all: true 옵션으로 모든 일치 수정 가능

# 잘못된 예
Edit(old_str: "return user", new_str: "...")
# → 같은 줄이 여러 곳에 있다면 에러

# 올바른 예
Edit(
  old_str: "  if (id) {\n    user = await User.find(id);\n    return user;\n  }",
  new_str: "..."
)
```

## Speaker Notes

Edit 도구는 파일의 일부를 정밀하게 수정하는 도구입니다.
Find and Replace 방식으로 동작하는데, old_str에 현재 내용, new_str에 새 내용을 지정합니다.
핵심 규칙은 old_str이 파일 내에서 유일해야 한다는 것입니다.
같은 문자열이 여러 곳에 있으면 어디를 수정해야 할지 모호하므로 오류를 반환합니다.
들여쓰기와 공백까지 정확히 일치해야 하므로, 충분한 컨텍스트를 포함하는 것이 권장됩니다.
보통 앞뒤 2-3줄을 포함합니다.
모든 일치를 한 번에 수정하고 싶다면 replace_all 옵션을 true로 설정합니다.
Edit 도구는 원자적으로 적용되므로 부분 적용 같은 중간 상태가 발생하지 않습니다.
