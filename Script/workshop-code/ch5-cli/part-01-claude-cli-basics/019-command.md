# Slide 19: 명령 조합 패턴

**Part 1: claude 명령 기본**

## Code Blocks

### patterns

```bash
# 패턴 1: 빠른 일회성 분석
$ claude -p "이 파일의 핵심 아이디어 3가지"

# 패턴 2: pipe로 다른 명령 결과 분석
$ git log --since="1 week ago" --oneline | \
    claude -p "이번 주 작업 카테고리별 분류"

# 패턴 3: JSON 출력 후 jq 파싱
$ claude -p "README 요약" --output-format json | \
    jq -r '.result' > summary.md

# 패턴 4: 안전한 CI 설정
$ claude -p "PR 변경 사항 요약" \
    --allowed-tools "Read,Bash(gh pr:*)" \
    --max-turns 10 \
    --output-format json | \
    jq -r '.result'

# 패턴 5: 환경변수로 동적 프롬프트
$ PR_NUM=$(gh pr list --json number -q '.[0].number')
$ claude -p "PR #$PR_NUM 리뷰" --output-format json

# 패턴 6: 다단계 세션
$ S=$(claude -p "분석" --output-format json | \
      jq -r '.session_id')
$ claude --continue "$S" -p "수정안 제시"
$ claude --continue "$S" -p "테스트 작성"

# 패턴 7: 병렬 처리
$ for f in src/*.js; do
    claude -p "$f 분석" > "reports/$(basename $f).md" &
  done
$ wait    # 모든 작업 완료 대기
```

## Speaker Notes

명령 조합 패턴 7가지입니다.
패턴 1은 빠른 일회성 분석입니다.
프롬프트만 주고 즉시 결과를 받습니다.
패턴 2는 pipe로 다른 명령 결과를 분석합니다.
git log 출력을 그대로 분석 입력으로 사용합니다.
패턴 3은 JSON 출력 후 jq 파싱입니다.
구조화 데이터에서 result만 추출해 파일에 저장합니다.
패턴 4는 안전한 CI 설정입니다.
allowed-tools를 좁히고 max-turns로 무한 루프를 방지하며 JSON으로 출력합니다.
패턴 5는 환경변수로 동적 프롬프트입니다.
PR 번호를 동적으로 가져와 프롬프트에 포함시킵니다.
패턴 6은 다단계 세션입니다.
첫 분석 후 같은 session_id로 수정안과 테스트 작성을 순차 진행합니다.
패턴 7은 병렬 처리입니다.
여러 파일을 백그라운드로 분석하고 wait로 완료를 대기합니다.
7가지 패턴이 대부분의 실전 활용에 충분합니다.
