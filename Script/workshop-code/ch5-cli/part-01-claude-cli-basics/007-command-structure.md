# Slide 7: Command structure

**Part 1: claude 명령 기본**

## Code Blocks

### invocations

```bash
# 방식 1: 대화형 (interactive)
$ claude
> 이 코드를 리뷰해 줘
> ...

# 방식 2: Headless (single prompt)
$ claude -p "이 디렉토리의 README.md 요약해 줘"
# 한 번 응답 후 즉시 종료

# 방식 3: Pipe (stdin)
$ cat report.md | claude -p "이 보고서의 핵심 3가지 정리"
$ git diff | claude -p "이 변경사항을 한 줄로 요약"

# 방식 4: Redirect (stdout)
$ claude -p "Python 정렬 알고리즘 5개 비교" > comparison.md
$ claude -p "README 초안 작성" | tee README.md

# 조합 예시
$ tail -100 app.log | claude -p \
    "이 로그에서 에러를 찾고 원인 분석" \
    --output-format json > analysis.json

# 다중 명령
$ for dir in src/*/; do
    claude -p "$dir 폴더의 코드 품질 평가" > "reports/$(basename $dir).md"
  done
```

## Speaker Notes

claude 명령의 4가지 호출 방식입니다.
방식 1은 대화형입니다.
인자 없이 claude만 입력하면 대화 세션이 시작됩니다.
Day 1과 2에서 주로 다룬 방식입니다.
방식 2는 Headless입니다.
-p 또는 --print 플래그와 프롬프트를 함께 전달하면 한 번 응답 후 즉시 종료됩니다.
스크립트와 자동화에 핵심적인 방식입니다.
방식 3은 pipe입니다.
다른 명령의 stdout을 claude의 stdin으로 전달합니다.
cat이나 git diff 같은 명령의 출력을 그대로 분석 입력으로 사용합니다.
방식 4는 redirect입니다.
claude의 응답을 파일로 저장하거나 다른 명령에 파이프합니다.
tee를 사용하면 파일 저장과 화면 출력을 동시에 할 수 있습니다.
조합과 다중 명령으로 강력한 자동화가 가능합니다.
