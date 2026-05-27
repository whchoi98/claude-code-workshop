# Slide 46: 출력 파일 분할

**Part 3: 출력 형식과 파싱 심화**

## Code Blocks

### split output

```bash
# 시나리오: 한 응답에서 여러 파일을 추출

# 1. 도구 호출별 결과 저장
$ claude -p "src/의 모든 .js 파일을 분석. \
  각 파일별 분석 결과를 JSON으로 출력" \
  --output-format stream-json | \
    while IFS= read -r line; do
      TYPE=$(echo "$line" | jq -r '.type')
      if [ "$TYPE" = "tool_result" ]; then
        FILE=$(echo "$line" | jq -r '.tool_use_id')
        echo "$line" | jq '.content' > "results/$FILE.json"
      fi
    done

# 2. 응답 안의 코드 블록 추출
$ claude -p "Python 정렬 알고리즘 5개. \
  각각을 별도 함수로" --output-format json | \
    jq -r '.result' | \
    awk '/```python/{p=1; n++; next}
         /```/{p=0; next}
         p{print > "alg_" n ".py"}'

# 3. 섹션별 파일 분할 (마크다운)
$ claude -p "API 문서 작성. ## 섹션 단위로 구성" \
    --output-format json | jq -r '.result' | \
    awk '/^## /{f=tolower($2); gsub(/ /,"_",f); f="docs/"f".md"}
         f{print > f}'

# 4. JSON 응답을 여러 파일로 (jq)
$ echo '[{"id":1,"data":"..."},{"id":2,"data":"..."}]' | \
    jq -c '.[]' | \
    while IFS= read -r obj; do
      ID=$(echo "$obj" | jq -r '.id')
      echo "$obj" > "items/$ID.json"
    done

# 5. zip으로 묶기
$ zip -r analysis-results.zip results/ docs/
```

## Speaker Notes

출력 파일 분할 패턴입니다.
한 응답에서 여러 파일을 추출하는 시나리오입니다.
1번 도구 호출별 결과 저장입니다.
stream-json으로 호출하고 type이 tool_result인 이벤트를 잡아 각각 별도 파일에 저장합니다.
2번 응답 안의 코드 블록 추출은 awk로 처리합니다.
백틱 세 개로 시작하는 라인을 만나면 새 파일에 출력 시작, 끝나면 종료합니다.
파일명에 카운터를 사용해 알고리즘 1, 2, 3 같은 형식으로 분할합니다.
3번 섹션별 마크다운 분할입니다.
## 으로 시작하는 라인의 두 번째 단어를 파일명으로 사용합니다.
공백은 언더스코어로 바꾸고 소문자로 변환합니다.
4번 JSON 배열을 여러 파일로 분할합니다.
jq -c로 한 줄씩 출력하고 각 객체를 ID 기준 파일로 저장합니다.
5번 zip으로 묶어 다운로드 가능한 단일 파일로 만듭니다.
결과 배포 시 유용합니다.
