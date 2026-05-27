# Slide 34: 멀티 메시지 구조

**Part 2: MESSAGES API 심화**

## Code Blocks

### content blocks

```bash
# 1. content가 string인 경우
{"role": "user", "content": "Hello"}

# 2. content가 ContentBlock 배열인 경우
{
    "role": "user",
    "content": [
        {"type": "text", "text": "다음 이미지 분석:"},
        {"type": "image", "source": {
            "type": "base64",
            "media_type": "image/jpeg",
            "data": "...",
        }},
        {"type": "text", "text": "포함된 객체를 나열"},
    ],
}

# 3. ContentBlock 타입들
# - text: 일반 텍스트
# - image: 이미지 (base64 또는 URL)
# - document: PDF 같은 문서
# - tool_use: 모델의 도구 호출 (응답에서만)
# - tool_result: 도구 호출 결과

# 4. 텍스트와 이미지 결합
import base64

with open("diagram.png", "rb") as f:
    image_data = base64.standard_b64encode(f.read()).decode()

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {"type": "image", "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": image_data,
            }},
            {"type": "text", "text": "이 다이어그램 설명"},
        ],
    }],
)

# 5. URL 기반 이미지
{"type": "image", "source": {
    "type": "url",
    "url": "https://example.com/image.jpg",
}}

# 6. 응답의 content 처리
for block in response.content:
    if block.type == "text":
        print(block.text)
    elif block.type == "tool_use":
        print(f"Tool: {block.name}")
        print(f"Input: {block.input}")
```

## Speaker Notes

멀티 메시지 구조에서 content는 string 또는 ContentBlock 배열입니다.
1번 단순 텍스트는 string으로 충분합니다.
2번 복잡한 경우 ContentBlock 배열로 작성합니다.
text와 image 같은 type별 객체를 배열에 둡니다.
3번 ContentBlock 타입은 5가지입니다.
text는 일반 텍스트, image는 이미지, document는 PDF, tool_use는 모델의 도구 호출이며 응답에서만 나타납니다.
tool_result는 도구 호출 결과입니다.
4번 텍스트와 이미지 결합 패턴입니다.
base64로 인코딩한 이미지 데이터와 텍스트 질문을 함께 전달합니다.
media_type을 정확히 명시해야 합니다.
image png, image jpeg, image gif, image webp가 지원됩니다.
5번 URL 기반 이미지도 지원됩니다.
source type을 url로 두고 외부 URL을 명시합니다.
6번 응답의 content 처리는 type 확인 후 분기합니다.
text 타입은 .text, tool_use 타입은 .name과 .input에 접근합니다.
TypeScript는 instanceof나 type narrowing을 사용합니다.
