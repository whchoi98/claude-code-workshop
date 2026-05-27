# Slide 36: PDF 입력

**Part 2: MESSAGES API 심화**

## Code Blocks

### PDF input

```bash
# 1. PDF를 직접 입력 (텍스트 + 이미지)
import base64

with open("contract.pdf", "rb") as f:
    pdf_data = base64.standard_b64encode(f.read()).decode()

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": [
            {"type": "document", "source": {
                "type": "base64",
                "media_type": "application/pdf",
                "data": pdf_data,
            }},
            {"type": "text", "text":
                "이 계약서의 핵심 조항 5가지와 위험 요소 분석"
            },
        ],
    }],
)

# 2. URL 기반 PDF
{"type": "document", "source": {
    "type": "url",
    "url": "https://example.com/report.pdf",
}}

# 3. 텍스트 추출만 (file_id 활용)
file = client.files.create(
    file=open("doc.pdf", "rb"),
    purpose="user_data",
)

response = client.messages.create(
    messages=[{
        "role": "user",
        "content": [
            {"type": "document", "source": {
                "type": "file",
                "file_id": file.id,
            }},
            {"type": "text", "text": "요약해줘"},
        ],
    }],
    ...
)

# 4. PDF + Caching (큰 문서)
client.messages.create(
    messages=[{
        "role": "user",
        "content": [
            {
                "type": "document",
                "source": {"type": "base64", ...},
                "cache_control": {"type": "ephemeral"},
            },
            {"type": "text", "text": "Q1: ..."},
        ],
    }],
    ...
)

# 5. PDF 크기 제한
# - 최대 32MB
# - 100 페이지 권장 (그 이상은 청크 분할)
# - 첫 호출은 처리 시간이 더 길 수 있음

# 6. 활용 사례
# - 계약서 분석
# - 연구 논문 요약
# - 재무 보고서 데이터 추출
# - 매뉴얼 Q&A
```

## Speaker Notes

PDF 입력으로 문서를 직접 분석할 수 있습니다.
1번 PDF를 base64로 인코딩해 document block에 전달합니다.
media_type은 application/pdf로 명시합니다.
Claude가 텍스트와 이미지 모두를 함께 처리합니다.
2번 URL 기반 PDF도 지원됩니다.
source type을 url로 두고 외부 PDF URL을 명시합니다.
3번 텍스트 추출만 필요한 경우 file_id 활용도 가능합니다.
client.files.create로 파일을 업로드하고 file_id를 source에 전달합니다.
자주 참조하는 문서를 한 번만 업로드해 재사용할 때 효과적입니다.
4번 PDF에 caching을 적용하면 큰 문서를 효율적으로 다룰 수 있습니다.
같은 PDF에 여러 질문을 할 때 caching으로 비용을 크게 줄입니다.
5번 PDF 크기 제한은 최대 32MB이고 100 페이지가 권장됩니다.
그 이상은 청크 분할이 필요합니다.
첫 호출은 처리 시간이 더 길 수 있습니다.
6번 활용 사례는 계약서 분석, 연구 논문 요약, 재무 보고서 데이터 추출, 매뉴얼 Q&A 등입니다.
