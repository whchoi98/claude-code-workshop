# Slide 27: temperature와 top_p

**Part 2: MESSAGES API 심화**

## Code Blocks

### temperature

```python
# 1. temperature (0.0 ~ 1.0, 기본 1.0)
# - 0.0: 결정적, 거의 같은 응답
# - 1.0: 창의적, 다양한 응답
# - 매번 동일한 결과 필요하면 0.0

# 결정적 응답 (분류, 데이터 추출)
client.messages.create(
    temperature=0.0,
    messages=[{
        "role": "user",
        "content": "다음을 yes/no로만 답: 이 코드 안전한가?"
    }],
    ...
)

# 창의적 응답 (글쓰기, 브레인스토밍)
client.messages.create(
    temperature=1.0,
    messages=[{
        "role": "user",
        "content": "이 제품 이름 10가지 제안"
    }],
    ...
)

# 2. top_p (nucleus sampling, 0.0 ~ 1.0, 기본 1.0)
# - 누적 확률 p 이내의 토큰만 고려
# - 0.5: 매우 좁은 선택
# - 1.0: 모든 가능성

# 권장: temperature 또는 top_p 중 하나만 조정

# 3. 결정적이지 않은 이유
# temperature 0.0이라도 약간의 변동 가능
# 하드웨어, 배치 등의 영향

# 4. 실전 패턴
# 분류, 추출
TEMP_DETERMINISTIC = 0.0

# 분석, 요약
TEMP_BALANCED = 0.5

# 글쓰기, 브레인스토밍
TEMP_CREATIVE = 1.0

# 5. 사용 가이드
TASKS = {
    "classification":   {"temperature": 0.0},
    "extraction":       {"temperature": 0.0},
    "summarization":    {"temperature": 0.3},
    "code_review":      {"temperature": 0.3},
    "code_generation":  {"temperature": 0.5},
    "creative_writing": {"temperature": 1.0},
}

def call_for(task: str, prompt: str):
    params = TASKS[task]
    return client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
        **params,
    )
```

## Speaker Notes

temperature와 top_p로 응답 다양성을 조절합니다.
1번 temperature는 0.0에서 1.0 사이이고 기본은 1.0입니다.
0.0은 결정적이라 거의 같은 응답이 나오고 1.0은 창의적이라 다양한 응답이 나옵니다.
매번 동일한 결과가 필요하면 0.0을 사용합니다.
결정적 응답이 필요한 분류나 데이터 추출에는 0.0을 사용합니다.
창의적 응답이 필요한 글쓰기나 브레인스토밍에는 1.0을 사용합니다.
2번 top_p는 nucleus sampling으로 누적 확률 p 이내의 토큰만 고려합니다.
0.5는 매우 좁은 선택, 1.0은 모든 가능성을 고려합니다.
temperature와 top_p 둘 중 하나만 조정하는 것이 권장됩니다.
3번 결정적이지 않은 이유는 temperature 0.0이라도 약간의 변동이 있을 수 있기 때문입니다.
하드웨어와 배치 처리의 영향입니다.
4번 실전 패턴 3가지를 정리합니다.
결정적은 0.0, 균형은 0.5, 창의는 1.0입니다.
5번 사용 가이드를 TASKS dict로 관리하면 용도별 일관성을 유지할 수 있습니다.
call_for 함수로 task 이름만 주면 적절한 temperature가 자동 적용됩니다.
