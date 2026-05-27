# Slide 127: Troubleshooting: Permission denied

**Part 8: INTEGRATION & TROUBLESHOOTING**

## Code Blocks

### perm debug

```bash
# 증상: Edit 도구가 권한 거부됨

# 1. /permissions로 확인
> /permissions Edit(src/api/user.js)
→ DENY (matched by 'Edit(src/api/secure/**)'
        from managed-settings.json)

# 2. 어느 계층 deny인지 확인
managed-settings.json: 조직 강제 → root만 수정 가능
.claude/settings.json: 팀 공유 → PR로 수정
~/.claude/settings.json: 개인 → 직접 수정 가능

# 3. 의도된 차단이라면
# 권한이 있는 사람에게 요청하거나
# 다른 디렉토리에서 작업

# 4. 의도되지 않은 차단이라면 수정
# 예시: 너무 광범위한 deny 패턴
"deny": ["Edit(src/**/secure*)"]  # 의도

# 실제로는 src/api/user.js에 매칭 안 되어야 하는데
# 패턴 오타나 잘못된 글롭으로 매칭됨

# 5. 수정 후 검증
> /permissions Edit(src/api/user.js)
→ ALLOW (matched by 'Edit(src/**)' from project settings)

# 6. 다른 일반 원인
- additionalDirectories에 추가 필요
- 절대 경로 매칭 문제
- managed-settings의 deny가 너무 광범위
```

## Speaker Notes

권한 거부 오류 진단입니다.
Edit 도구가 권한 거부되는 증상입니다.
1단계 /permissions 명령으로 확인합니다.
특정 호출이 어느 규칙에 매칭되어 DENY되는지 정확히 표시됩니다.
어느 settings 파일의 어떤 규칙인지까지 알 수 있습니다.
2단계 어느 계층의 deny인지 확인합니다.
managed-settings는 조직 강제로 root만 수정 가능합니다.
.claude/settings.json은 팀 공유로 PR로 수정합니다.
~/.claude/settings.json은 개인용으로 직접 수정 가능합니다.
3단계 의도된 차단이라면 권한이 있는 사람에게 요청하거나 다른 디렉토리에서 작업합니다.
4단계 의도되지 않은 차단이라면 패턴을 수정합니다.
너무 광범위한 deny 패턴이 흔한 원인입니다.
secure 같은 키워드가 의도와 다르게 매칭될 수 있습니다.
5단계 수정 후 다시 /permissions로 검증합니다.
6단계 다른 일반 원인은 additionalDirectories 필요, 절대 경로 매칭 문제, managed-settings의 광범위 deny입니다.
