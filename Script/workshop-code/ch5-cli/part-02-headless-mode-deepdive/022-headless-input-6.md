# Slide 22: Headless 입력 방식 6종

**Part 2: HEADLESS 모드 심화**

## Code Blocks

### input methods

```bash
# 1. 인자 (가장 단순)
$ claude -p "이 디렉토리 분석"

# 2. stdin pipe
$ cat report.md | claude -p "이 보고서 핵심 추출"

# 3. heredoc (큰 텍스트)
$ claude -p "$(cat <<'EOF'
다음 코드를 리뷰해 주세요:
- 가독성
- 성능
- 보안
EOF
)"

# 4. 리다이렉트로 출력
$ claude -p "주간 보고서 작성" > weekly.md
$ claude -p "..." 2> debug.log     # stderr만
$ claude -p "..." &> all.log       # 둘 다

# 5. 결합: 다른 명령의 결과를 컨텍스트로
$ (echo "## 최근 commit"; git log -10 --oneline) | \
    claude -p "이 commit 패턴 분석"

# 6. 다중 명령 (순차)
$ claude -p "코드 분석" > analysis.md && \
  claude -p "$(cat analysis.md) 기반 개선안" > improvements.md

# 7. xargs로 일괄 처리 (병렬 X)
$ find . -name "*.py" | \
    xargs -I{} claude -p "{} 분석" > all-analysis.txt

# 8. GNU parallel로 병렬 처리
$ find . -name "*.py" | \
    parallel -j 4 'claude -p "{} 분석" > "reports/{/.}.md"'
```

## Speaker Notes

Headless 입력 방식 6종 + 추가 패턴을 정리합니다.
첫째, 인자 방식은 가장 단순합니다.
둘째, stdin pipe는 cat 같은 명령의 출력을 그대로 전달합니다.
셋째, heredoc은 큰 텍스트나 여러 줄 프롬프트에 적합합니다.
bash의 cat heredoc 구문을 활용합니다.
넷째, 리다이렉트로 출력을 저장합니다.
stdout만, stderr만, 둘 다 같은 다양한 옵션이 있습니다.
다섯째, 결합 패턴입니다.
여러 명령의 결과를 한 prompt에 합쳐 컨텍스트로 사용합니다.
여섯째, 다중 명령 순차 실행입니다.
첫 결과를 다음 명령의 입력으로 연결할 수 있습니다.
추가로 xargs는 일괄 처리이지만 순차 실행이고, GNU parallel을 사용하면 병렬 처리가 가능합니다.
-j 4는 동시 4개 작업을 의미합니다.
