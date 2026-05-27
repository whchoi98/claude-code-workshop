# Slide 132: Prompt 압축

**Part 7: 고급 패턴**

## Code Blocks

### compression

```python
# 큰 prompt를 의미 보존하면서 짧게 만들기

# 1. 단순 압축 (Haiku로)
async def compress_prompt(long_text: str, target_ratio: float = 0.3):
    response = await client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=int(len(long_text) * target_ratio),
        system=f"""다음 텍스트를 핵심 의미를 모두 보존하면서
        {int(target_ratio*100)}% 길이로 압축. 중요 정보 손실 없이.""",
        messages=[{"role": "user", "content": long_text}],
    )
    return response.content[0].text

# 사용
long_doc = open("contract.txt").read()   # 50KB
compressed = await compress_prompt(long_doc, target_ratio=0.3)  # 15KB

# 압축본으로 분석 (저비용)
response = client.messages.create(
    model="claude-sonnet-4-5",
    messages=[{"role": "user", "content": f"분석: {compressed}"}],
    ...
)

# 2. 구조화 압축 (정보 추출)
async def extract_structured(long_text: str):
    response = await client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=2048,
        system="""다음에서 구조화된 정보 추출 (JSON):
        {
          "key_points": [...],
          "entities": [...],
          "dates": [...],
          "amounts": [...]
        }""",
        messages=[{"role": "user", "content": long_text}],
    )
    return json.loads(response.content[0].text)

# 추출된 정보만으로 작업 진행
structured = await extract_structured(big_document)
# 원본 50KB -> 구조화 5KB

# 3. RAG 패턴 (관련 부분만)
def find_relevant_chunks(question: str, document: str, top_k: int = 5):
    chunks = split_into_chunks(document, chunk_size=500)

    question_emb = embed(question)
    chunk_embs = [embed(c) for c in chunks]

    # cosine similarity로 top-k 선택
    scores = [cosine_sim(question_emb, e) for e in chunk_embs]
    indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    return [chunks[i] for i in indices[:top_k]]

# 사용
relevant = find_relevant_chunks(question, big_document)
context = "\n".join(relevant)
response = client.messages.create(
    messages=[{"role": "user",
        "content": f"문서:\n{context}\n\n질문: {question}"}],
    ...
)

# 4. 효과 측정
# 원본: 100K 토큰 input
# 압축 후: 30K 토큰 input
# 절감: 70% (Sonnet 기준 $0.21 -> $0.06)
```

## Speaker Notes

Prompt 압축으로 입력 토큰을 절감합니다.
큰 prompt를 의미 보존하면서 짧게 만드는 패턴입니다.
첫째, 단순 압축은 Haiku로 합니다.
compress_prompt 함수에서 target_ratio 30 퍼센트로 압축합니다.
max_tokens를 원본 길이의 30 퍼센트로 제한합니다.
50KB 문서를 15KB로 압축한 후 Sonnet으로 분석하면 입력 비용을 70 퍼센트 절감합니다.
둘째, 구조화 압축은 정보 추출 패턴입니다.
JSON 형식으로 key_points, entities, dates, amounts를 추출합니다.
50KB 원본이 5KB 구조화 데이터가 됩니다.
분석에 필요한 정보만 추출하므로 의미 손실 없이 크게 압축됩니다.
셋째, RAG 패턴은 관련 부분만 사용합니다.
find_relevant_chunks에서 질문과 청크들의 임베딩 유사도를 계산해 top_k만 선택합니다.
질문에 직접 관련된 부분만 컨텍스트로 사용합니다.
넷째, 효과 측정입니다.
원본 100K 토큰이 압축 후 30K로 줄면 70 퍼센트 절감입니다.
Sonnet 기준 0.21달러가 0.06달러가 됩니다.
Claude의 200K 윈도우를 활용하더라도 의미있는 정보만 담는 것이 비용과 품질 모두에 유리합니다.
응답 속도도 빨라지는 부가 효과가 있습니다.
