# Slide 68: 청크 후처리

**Part 4: STREAMING**

## Code Blocks

### chunk processing

```python
# 시나리오: 응답이 들어오는 동안 점진적으로 분석/변환

# 1. Markdown 실시간 렌더링
import markdown

class StreamingMarkdown:
    def __init__(self):
        self.buffer = ""
        self.md = markdown.Markdown()

    def add_chunk(self, chunk):
        self.buffer += chunk
        # 단락 끝마다 렌더링
        if "\n\n" in self.buffer:
            parts = self.buffer.split("\n\n")
            self.buffer = parts[-1]    # 마지막 미완성 단락은 보관
            for p in parts[:-1]:
                html = self.md.convert(p)
                yield html

sm = StreamingMarkdown()
with client.messages.stream(...) as stream:
    for text in stream.text_stream:
        for html in sm.add_chunk(text):
            print(html)

# 2. 코드 블록 감지 (점진적)
class StreamingCodeBlock:
    def __init__(self):
        self.buffer = ""
        self.in_code = False
        self.code = ""
        self.lang = ""

    def feed(self, chunk):
        self.buffer += chunk
        # 코드 블록 시작 감지
        if not self.in_code and "```" in self.buffer:
            idx = self.buffer.index("```")
            yield ("text", self.buffer[:idx])
            self.in_code = True
            # 언어 ID 추출
            rest = self.buffer[idx+3:]
            self.buffer = rest
        elif self.in_code and "```" in self.buffer:
            idx = self.buffer.index("```")
            self.code += self.buffer[:idx]
            yield ("code", self.code, self.lang)
            self.code = ""
            self.lang = ""
            self.in_code = False
            self.buffer = self.buffer[idx+3:]

# 3. JSON 점진적 파싱 (json-stream)
import json_stream

# 큰 JSON 응답에서 점진적으로 객체 추출
# stream 응답이 JSON 배열일 때 각 요소를 즉시 처리

# 4. 이벤트 기반 트리거
KEYWORDS = ["ERROR", "WARNING", "TODO"]

def watch_for_keywords(stream):
    buffer = ""
    for chunk in stream.text_stream:
        buffer += chunk
        for kw in KEYWORDS:
            if kw in buffer:
                send_alert(f"Found: {kw}")
                buffer = buffer[buffer.index(kw)+len(kw):]
        yield chunk
```

## Speaker Notes

청크 후처리로 응답이 들어오는 동안 점진적으로 분석합니다.
1번 Markdown 실시간 렌더링이 일반적입니다.
StreamingMarkdown 클래스에서 buffer에 청크를 누적합니다.
단락 구분자인 두 개 연속 개행을 만나면 그 전까지의 단락들을 HTML로 변환합니다.
마지막 미완성 단락은 다음 청크와 결합되도록 보관합니다.
2번 코드 블록 감지는 점진적으로 처리합니다.
백틱 세 개를 감지해 코드 블록 시작과 종료를 추적합니다.
언어 ID 추출과 코드 누적, 종료 시 emit하는 패턴입니다.
시작이면 text, 종료면 code 타입으로 yield합니다.
3번 JSON 점진적 파싱은 json-stream 라이브러리를 활용합니다.
큰 JSON 응답이 배열인 경우 각 요소가 도착하는 대로 즉시 처리할 수 있습니다.
전체 응답을 기다리지 않아도 됩니다.
4번 이벤트 기반 트리거는 특정 키워드 감시입니다.
ERROR, WARNING, TODO 같은 키워드가 감지되면 즉시 alert을 보내고 그 이후 텍스트는 buffer에서 제거합니다.
모니터링이나 알람 시스템에 활용됩니다.
청크 후처리로 응답 완료를 기다리지 않고 즉시 반응할 수 있습니다.
