# Slide 66: React SSE 클라이언트

**Part 4: STREAMING**

## Code Blocks

### React client

```python
// Chat.tsx - React SSE 클라이언트
import { useState } from "react";

export function Chat() {
  const [text, setText] = useState("");
  const [isStreaming, setIsStreaming] = useState(false);

  async function sendMessage(prompt: string) {
    setText("");
    setIsStreaming(true);

    const response = await fetch("/chat/stream", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });

    const reader = response.body!.getReader();
    const decoder = new TextDecoder();
    let buffer = "";

    while (true) {
      const { value, done } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });

      // SSE line 단위 처리
      const lines = buffer.split("\n\n");
      buffer = lines.pop() || "";

      for (const line of lines) {
        if (!line.startsWith("data: ")) continue;
        const json = JSON.parse(line.slice(6));

        if (json.type === "text") {
          // 점진적으로 텍스트 추가
          setText(prev => prev + json.text);
        } else if (json.type === "done") {
          console.log("Done, tokens:", json.usage);
          setIsStreaming(false);
        }
      }
    }
  }

  return (
    <div>
      <textarea onKeyDown={e => {
        if (e.key === "Enter" && !e.shiftKey) {
          e.preventDefault();
          sendMessage(e.currentTarget.value);
        }
      }} />
      <div className="response">
        {text}
        {isStreaming && <span className="cursor">▊</span>}
      </div>
    </div>
  );
}

// 효과
// - 첫 토큰 0.3초 후 표시
// - 타이핑 효과로 사용자 인지 지연 감소
// - 응답 도중 사용자가 중단 가능 (다음 슬라이드)
```

## Speaker Notes

React SSE 클라이언트로 브라우저에서 스트림을 수신합니다.
useState로 text와 isStreaming 상태를 관리합니다.
sendMessage 함수에서 fetch로 POST 요청을 보냅니다.
body의 getReader로 ReadableStream Reader를 얻습니다.
TextDecoder로 UTF-8 디코딩합니다.
while 루프에서 reader.read를 반복 호출하며 chunk를 받습니다.
done이 true면 종료합니다.
buffer에 누적하고 split으로 SSE 메시지를 분리합니다.
빈 줄 두 개가 메시지 구분자입니다.
각 라인에서 data:로 시작하는 부분만 파싱합니다.
slice 6으로 data: 접두사를 제거하고 JSON.parse 합니다.
type이 text면 setText prev plus json.text로 점진적으로 추가합니다.
type이 done이면 토큰 사용량을 로그하고 isStreaming을 false로 설정합니다.
UI는 textarea와 응답 영역으로 구성됩니다.
Enter 키 입력으로 메시지를 보내고 응답이 점진적으로 표시됩니다.
isStreaming일 때 깜빡이는 커서 효과를 추가하면 ChatGPT 같은 경험이 완성됩니다.
첫 토큰이 0.3초 후 표시되어 인지 지연이 크게 감소합니다.
