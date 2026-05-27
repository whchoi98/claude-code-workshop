# Slide 35: 이미지 메시지 (Vision)

**Part 2: MESSAGES API 심화**

## Code Blocks

### vision

```python
# 1. 단일 이미지 분석
import base64

def encode_image(path: str) -> tuple[str, str]:
    with open(path, "rb") as f:
        data = base64.standard_b64encode(f.read()).decode()
    ext = path.split(".")[-1].lower()
    mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg",
            "png": "image/png", "gif": "image/gif",
            "webp": "image/webp"}[ext]
    return data, mime

data, mime = encode_image("chart.png")

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {"type": "image", "source": {
                "type": "base64",
                "media_type": mime,
                "data": data,
            }},
            {"type": "text", "text": "이 차트의 핵심 인사이트"},
        ],
    }],
)
print(response.content[0].text)

# 2. 여러 이미지 비교
content = []
for path in ["v1.png", "v2.png", "v3.png"]:
    data, mime = encode_image(path)
    content.append({
        "type": "image",
        "source": {"type": "base64", "media_type": mime, "data": data},
    })
content.append({
    "type": "text",
    "text": "이 3개 버전의 차이점과 개선점",
})

response = client.messages.create(
    messages=[{"role": "user", "content": content}],
    ...
)

# 3. 활용 사례
# - 차트/그래프 데이터 추출
# - 다이어그램 코드 변환 (Mermaid)
# - UI 스크린샷 분석
# - 손글씨 OCR
# - 이미지 캡셔닝
# - 의료 영상 분석 (전문가 검토 보조)

# 4. 이미지 크기 제한
# - 최대 5MB 또는 1.15MP
# - 너무 큰 이미지는 자동 다운샘플링
# - 4K 이미지는 미리 1080p로 줄이면 토큰 절약
```

## Speaker Notes

이미지 메시지로 Vision 기능을 활용합니다.
1번 단일 이미지 분석은 base64 인코딩 후 image content block에 전달합니다.
encode_image 함수에서 파일 확장자로 media_type을 결정합니다.
jpg, jpeg, png, gif, webp가 지원됩니다.
텍스트 질문과 함께 보내면 이미지를 분석해 응답합니다.
2번 여러 이미지 비교도 가능합니다.
content 배열에 image block을 여러 개 추가하고 마지막에 비교 질문을 둡니다.
v1, v2, v3 같은 버전 비교나 before after 분석에 유용합니다.
3번 활용 사례는 다양합니다.
차트와 그래프에서 데이터 추출, 다이어그램을 Mermaid 코드로 변환, UI 스크린샷 분석, 손글씨 OCR, 이미지 캡셔닝, 의료 영상 분석 보조 등이 가능합니다.
4번 이미지 크기 제한이 있습니다.
최대 5MB 또는 1.15 메가픽셀입니다.
너무 큰 이미지는 자동 다운샘플링됩니다.
4K 이미지는 미리 1080p로 줄이면 토큰을 절약할 수 있습니다.
