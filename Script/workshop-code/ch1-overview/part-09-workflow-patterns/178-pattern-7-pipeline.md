# Slide 178: Pattern 7 Pipeline

**Part 9: WORKFLOW PATTERNS**

## Code Blocks

### PIPELINE

```bash
# 1. 단순 파이프
$ git log --since="1 week ago" --pretty=format:"%h %s" \
   | claude -p "지난 주 변경 사항을 카테고리별로 분류해 줘"

# 2. 여러 단계 파이프
$ find . -name "*.test.ts" \
   | claude -p "이 테스트 파일 목록에서 누락된 도메인 찾기" \
   | grep -i "missing"

# 3. JSON 파이프 (구조화 데이터)
$ aws ec2 describe-instances --output json \
   | claude -p "비용 최적화 제안" --output-format json \
   | tee optimization-report.json

# 4. 로그 분석 자동화
$ tail -1000 /var/log/app.log \
   | claude -p "이 로그에서 ERROR 패턴과 빈도를 정리해" \
   > daily-error-report.md
```

## Speaker Notes

Pattern 7 Pipeline은 Claude를 Unix 파이프라인의 한 단계로 통합하는 패턴입니다.
첫째 git log 출력을 받아 카테고리별로 분류, 둘째 find 결과를 받아 누락된 도메인 찾기 후 grep으로 필터링, 셋째 AWS describe-instances JSON을 받아 비용 최적화 제안을 JSON으로 출력해 다음 단계에서 활용, 넷째 로그 파일의 ERROR 패턴 자동 분석 등 다양한 패턴이 가능합니다.
stdin과 stdout만 활용하므로 다른 명령과의 조합이 무한합니다.
