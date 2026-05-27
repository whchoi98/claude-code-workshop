# Slide 23: 시스템 프롬프트

**Part 2: MESSAGES API 심화**

## Code Blocks

### system prompt

```bash
# 1. 단순 시스템 프롬프트
message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    system="당신은 친절한 한국어 도우미입니다.",
    messages=[{"role": "user", "content": "안녕"}],
)

# 2. 긴 시스템 프롬프트 (파일에서 로드)
with open("prompts/code_reviewer.md") as f:
    system_prompt = f.read()

message = client.messages.create(
    system=system_prompt,
    ...
)

# 3. 시스템 프롬프트 구성 베스트 프랙티스
SYSTEM_PROMPT = """
# 역할
당신은 시니어 백엔드 엔지니어입니다.

# 전문성
- 분산 시스템
- Python, Go, Rust
- AWS, K8s

# 톤
- 정확하고 간결하게
- 기술 용어 사용
- 예시 코드 포함

# 제약
- 추측 금지 (모르면 모른다고)
- 보안 위험 발견 시 명시
- 영문 응답 (기술 토론 시)
"""

# 4. 시스템 프롬프트 vs user 메시지
# system: 역할, 톤, 제약, 컨텍스트 (변하지 않는 것)
# user:   실제 질문, 작업 (매번 다른 것)

# 5. 시스템 프롬프트는 캐시 대상
# 같은 시스템 프롬프트 사용 시 caching으로 비용 절감 가능
# (다음 슬라이드에서 다룸)

# 6. 멀티 파트 시스템 (배열 형식)
client.messages.create(
    system=[
        {"type": "text", "text": "역할: ..."},
        {"type": "text", "text": "제약: ...",
         "cache_control": {"type": "ephemeral"}},
    ],
    ...
)
```

## Speaker Notes

시스템 프롬프트는 system 매개변수로 전달합니다.
1번 단순 시스템 프롬프트는 문자열로 명시합니다.
2번 긴 시스템 프롬프트는 파일에서 로드합니다.
프롬프트 엔지니어링 결과물을 별도 파일로 관리하는 것이 권장됩니다.
3번 구성 베스트 프랙티스는 5개 섹션으로 구조화합니다.
역할, 전문성, 톤, 제약, 예시 같은 구조가 효과적입니다.
Markdown 헤더로 구분하면 모델이 인식하기 좋습니다.
4번 system 매개변수와 user 메시지의 차이를 명확히 이해해야 합니다.
system은 역할, 톤, 제약, 컨텍스트 같이 변하지 않는 것을 둡니다.
user는 실제 질문이나 작업 같이 매번 다른 것을 둡니다.
5번 시스템 프롬프트는 캐시 대상입니다.
같은 시스템 프롬프트 사용 시 caching으로 비용을 절감할 수 있습니다.
다음 슬라이드에서 자세히 다룹니다.
6번 멀티 파트 시스템은 배열 형식으로 cache_control을 명시할 수 있습니다.
캐시할 부분과 동적 부분을 분리하는 패턴입니다.
