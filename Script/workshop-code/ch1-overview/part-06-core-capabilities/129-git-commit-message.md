# Slide 129: Git commit message

**Part 6: CORE CAPABILITIES**

## Code Blocks

### Commit message

```bash
# Claude의 커밋 메시지 작성 패턴

# 1. 변경 분석
git diff --staged
# → 어떤 파일이 어떻게 바뀌었는지 분석

# 2. Conventional Commits 형식 생성
feat(users): add pagination with cursor-based navigation

- Add page/limit query parameters with sensible defaults
- Implement Link header for next/prev navigation
- Update tests for new pagination behavior

# 3. 커밋 실행
git commit -m "$(cat <<'EOF'
feat(users): add pagination with cursor-based navigation
...
EOF
)"

# 권장: Co-authored-by Claude 추가 (투명성)
# Co-Authored-By: Claude <noreply@anthropic.com>
```

## Speaker Notes

Claude의 커밋 메시지 자동 작성 패턴을 살펴봅니다.
1단계 git diff staged로 어떤 파일이 어떻게 바뀌었는지 분석합니다.
2단계 Conventional Commits 형식으로 메시지를 생성합니다.
첫 줄에는 feat, fix, docs, refactor 같은 type과 함께 변경 범위와 한 줄 요약을 작성합니다.
본문에는 변경 사항의 세부 내용을 bullet point로 정리합니다.
3단계 git commit 명령으로 커밋을 실행합니다.
권장 사항은 커밋 메시지에 Co-authored-by Claude 라인을 추가해 투명성을 확보하는 것입니다.
