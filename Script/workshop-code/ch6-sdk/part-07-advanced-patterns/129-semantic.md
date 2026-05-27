# Slide 129: Semantic 캐시

**Part 7: 고급 패턴**

## Code Blocks

### semantic cache

```python
# 의미가 유사한 prompt를 캐시 hit으로 처리
# "Python list comprehension 설명" ~= "파이썬 리스트 컴프리헨션 알려줘"

# 1. 임베딩 생성 (Voyage AI 또는 OpenAI)
import voyageai
vo = voyageai.Client()

def embed(text: str) -> list:
    result = vo.embed([text], model="voyage-3", input_type="query")
    return result.embeddings[0]

# 2. Vector DB (Pinecone, Qdrant, pgvector 등)
import pinecone
pinecone.init(api_key=os.getenv("PINECONE_KEY"))
index = pinecone.Index("claude-cache")

def cache_set(prompt: str, response: str):
    vec = embed(prompt)
    index.upsert([(
        hashlib.md5(prompt.encode()).hexdigest(),
        vec,
        {"prompt": prompt, "response": response}
    )])

def cache_get(prompt: str, similarity_threshold: float = 0.95):
    vec = embed(prompt)
    results = index.query(vector=vec, top_k=1, include_metadata=True)
    if results.matches and results.matches[0].score >= similarity_threshold:
        return results.matches[0].metadata["response"]
    return None

# 3. 통합 사용
def smart_call_with_semantic(prompt):
    # Layer 1: 정확 캐시 (생략)

    # Layer 2: Semantic 캐시
    cached = cache_get(prompt, similarity_threshold=0.95)
    if cached:
        log_cache_hit("L2_semantic")
        return cached

    # 호출
    response = client.messages.create(...)
    text = response.content[0].text

    # 캐시 저장
    cache_set(prompt, text)
    return text

# 4. 효과
# - "Python list comprehension" 첫 호출: API 호출
# - "파이썬 리스트 컴프리헨션" 재호출: 캐시 hit (0.96 유사도)
# - 30~50% hit rate 일반 (도메인 따라)

# 5. 주의사항
# - 한국어/영어 의미 매칭 가능하려면 multilingual 임베딩
# - 너무 낮은 threshold (0.85)는 잘못된 매칭 발생
# - 너무 높은 (0.99)은 hit rate 낮음
# - 0.95 정도가 일반적 sweet spot

# 6. pgvector 대안 (sqlalchemy)
from pgvector.sqlalchemy import Vector

class Cache(Base):
    __tablename__ = "claude_cache"
    id = Column(Integer, primary_key=True)
    prompt = Column(Text)
    response = Column(Text)
    embedding = Column(Vector(1024))   # voyage-3 dimension

# 유사도 검색
similar = session.query(Cache).order_by(
    Cache.embedding.l2_distance(query_vec)
).limit(1).first()
```

## Speaker Notes

Semantic 캐시는 의미 기반 매칭입니다.
정확히 같지 않아도 의미가 유사한 prompt를 캐시 hit으로 처리합니다.
Python list comprehension 설명과 파이썬 리스트 컴프리헨션 알려줘 같은 표현이 매칭됩니다.
구현은 3단계입니다.
첫째, 임베딩 생성입니다.
Voyage AI나 OpenAI 같은 임베딩 모델을 사용합니다.
voyage-3는 다국어 지원이 우수합니다.
둘째, Vector DB에 저장합니다.
Pinecone, Qdrant, pgvector 같은 옵션이 있습니다.
upsert로 키, 벡터, 메타데이터를 저장합니다.
query로 가장 유사한 결과를 찾습니다.
셋째, 통합 사용입니다.
Layer 2로 semantic 검색을 시도하고 0.95 이상 유사도면 캐시된 응답을 사용합니다.
miss면 실제 호출 후 캐시에 저장합니다.
효과는 30에서 50 퍼센트 hit rate가 일반적입니다.
주의사항이 있습니다.
한국어 영어 매칭은 multilingual 임베딩이 필요합니다.
threshold가 너무 낮으면 잘못된 매칭, 너무 높으면 hit rate 저하입니다.
0.95 정도가 sweet spot입니다.
pgvector는 PostgreSQL 확장으로 별도 DB 없이 사용 가능한 대안입니다.
