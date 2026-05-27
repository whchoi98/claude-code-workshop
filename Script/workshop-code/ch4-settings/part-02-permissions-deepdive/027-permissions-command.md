# Slide 27: /permissions command

**Part 2: PERMISSIONS 심화**

## Code Blocks

### /permissions

```bash
# 1. 모든 권한 규칙 표시
> /permissions

Current effective permissions:

ALLOW (12 rules):
  ✓ Read                              [managed-settings.json]
  ✓ Grep                              [managed-settings.json]
  ✓ Glob                              [managed-settings.json]
  ✓ Bash(npm test:*)                  [.claude/settings.json]
  ✓ Bash(git diff:*)                  [.claude/settings.json]
  ✓ Edit(docs/**)                     [.claude/settings.json]
  ...

ASK (3 rules):
  ? Edit(src/**)                      [.claude/settings.json]
  ? Write(**)                         [.claude/settings.json]
  ? Bash(git push:*)                  [.claude/settings.json]

DENY (5 rules):
  ✗ Bash(rm -rf:*)                    [managed-settings.json]
  ✗ Bash(curl:*)                      [managed-settings.json]
  ✗ Read(**/.env*)                    [managed-settings.json]
  ...

# 2. 특정 도구 확인
> /permissions Bash(rm -rf foo)
  → DENY (matched by 'Bash(rm -rf:*)' from managed-settings.json)
```

## Speaker Notes

/permissions 명령으로 권한을 실시간으로 확인하고 디버깅할 수 있습니다.
인자 없이 호출하면 현재 적용된 모든 권한 규칙이 표시됩니다.
ALLOW, ASK, DENY 카테고리별로 분류되고 각 규칙 옆에는 어느 settings 파일에서 왔는지 표시됩니다.
managed-settings.json에서 온 규칙과 .claude/settings.json에서 온 규칙이 명확히 구분됩니다.
특정 도구 호출 결과를 미리 확인할 수도 있습니다.
예를 들어 /permissions 뒤에 Bash 괄호 rm -rf foo 형태로 명령하면 그 호출이 어떤 결과가 될지 표시됩니다.
DENY 결과와 함께 어느 규칙이 매칭되어 차단되는지, 그 규칙이 어느 settings에서 왔는지까지 알려줍니다.
권한 디버깅에 매우 유용한 명령입니다.
