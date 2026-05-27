# Slide 177: Pattern 6 Headless

**Part 9: WORKFLOW PATTERNS**

## Code Blocks

### HEADLESS

```bash
# 기본 헤드리스 사용
$ claude -p "package.json에서 outdated 패키지 알려줘"

# 결과를 파일로 저장
$ claude -p "이 프로젝트의 의존성 분석" > deps-report.md

# 다른 명령과 파이프
$ git log --oneline -20 | claude -p "지난 20개 커밋의 영향도 요약"

# JSON 출력으로 후처리
$ claude -p "사용된 환경변수 목록" --output-format json | jq '.envvars'

# 도구 제한 + 비밀번호 없는 자동화
$ claude -p "코드베이스의 보안 이슈 스캔" \
    --allowed-tools "Read,Grep,Glob" \
    --output-format json

# 모델 지정으로 비용 절감
$ claude -p "간단한 변환 작업" --model haiku
```

## Speaker Notes

Pattern 6 Headless Automation은 -p 플래그를 활용한 비대화형 자동화입니다.
기본 사용은 claude -p에 프롬프트를 전달하면 한 번의 응답 후 종료됩니다.
결과를 파일로 저장하거나, git 같은 다른 명령의 출력을 파이프로 받거나, JSON 출력을 jq로 후처리하는 다양한 활용이 가능합니다.
allowed-tools 플래그로 도구를 제한하면 자동화 환경에서도 안전성을 보장할 수 있고, --model haiku처럼 가벼운 모델을 지정하면 비용을 크게 절감할 수 있습니다.
셸 스크립트와 cron, GitHub Actions에 통합하면 강력한 자동화가 가능합니다.
