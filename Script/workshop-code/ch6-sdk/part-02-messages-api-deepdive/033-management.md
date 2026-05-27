# Slide 33: 컨텍스트 윈도우 관리

**Part 2: MESSAGES API 심화**

## Code Blocks

### context window

```python
# 1. 컨텍스트 윈도우 한계
# - claude-sonnet-4-5: 200K input tokens
# - claude-opus-4-5: 200K
# - claude-haiku-4-5: 200K

# 2. 토큰 1개 ≈
# - 영어 단어 0.75개
# - 한글 글자 1-2개
# - 코드 줄 0.5-2 토큰

# 3. 컨텍스트 절약 전략

# 전략 A: 입력 압축
def compress_messages(messages, threshold=180_000):
    while True:
        count = client.messages.count_tokens(
            model="claude-sonnet-4-5",
            messages=messages,
        )
        if count.input_tokens < threshold:
            return messages

        # 오래된 메시지 요약 후 교체
        old = messages[:-10]
        recent = messages[-10:]
        summary = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": f"다음을 요약: {old}"
            }],
        )
        messages = [
            {"role": "user", "content": f"이전 요약: {summary.content[0].text}"},
            *recent,
        ]

# 전략 B: 청크 분할
def chunk_input(text, max_chunk=50_000):
    chunks = []
    for i in range(0, len(text), max_chunk):
        chunks.append(text[i:i+max_chunk])
    return chunks

# 각 청크를 별도로 처리하고 통합
chunks = chunk_input(huge_document)
results = []
for chunk in chunks:
    r = client.messages.create(
        messages=[{"role": "user", "content": f"분석: {chunk}"}],
        ...
    )
    results.append(r.content[0].text)

# 통합
final = client.messages.create(
    messages=[{"role": "user", "content":
        f"다음 분석들 통합: {' '.join(results)}"
    }],
    ...
)

# 전략 C: 관련 부분만 선택 (RAG)
relevant_docs = vector_search(query, top_k=10)
context = "\n".join(relevant_docs)
```

## Speaker Notes

컨텍스트 윈도우 관리는 200K 토큰을 효과적으로 활용하는 것입니다.
1번 한계는 모든 claude 4.5 모델이 200K input입니다.
2번 토큰 1개의 대략적 크기는 영어 단어 0.75개, 한글 1-2자, 코드 0.5-2 토큰입니다.
3번 컨텍스트 절약 전략 3가지를 소개합니다.
전략 A는 입력 압축입니다.
compress_messages 함수에서 토큰 수를 측정해 한계 90 퍼센트인 180000에 도달하면 오래된 메시지를 요약합니다.
비용이 싼 Haiku로 요약을 만들고 최근 10개 메시지와 함께 사용합니다.
전략 B는 청크 분할입니다.
큰 문서를 50000 글자 단위로 나누고 각각 분석한 후 결과를 통합합니다.
각 청크는 컨텍스트에 충분히 들어가고 최종 통합은 결과들의 요약만 처리합니다.
전략 C는 RAG 패턴입니다.
vector_search로 관련 문서 top 10만 선택해 컨텍스트로 사용합니다.
질문에 직접 관련된 정보만 포함시켜 정확도와 비용 모두 개선합니다.
이 3가지 전략을 조합하면 200K를 넘는 데이터도 효과적으로 처리할 수 있습니다.
