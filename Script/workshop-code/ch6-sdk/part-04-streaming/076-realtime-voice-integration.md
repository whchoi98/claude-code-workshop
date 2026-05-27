# Slide 76: 실시간 음성 통합

**Part 4: STREAMING**

## Code Blocks

### voice streaming

```python
# 시나리오: Claude 응답을 실시간으로 음성으로 변환

# 1. ElevenLabs streaming TTS
from elevenlabs import generate, stream
import anthropic

claude = anthropic.AsyncAnthropic()

async def stream_to_voice(prompt):
    # 텍스트 청크를 모아서 문장 단위로 TTS
    buffer = ""
    sentence_endings = [".", "!", "?", "\n"]

    async with claude.messages.stream(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        async for text in stream.text_stream:
            buffer += text

            # 문장 끝 감지
            for ending in sentence_endings:
                if ending in buffer:
                    idx = buffer.rindex(ending)
                    sentence = buffer[:idx+1]
                    buffer = buffer[idx+1:]

                    # 문장을 음성으로 변환 후 재생
                    audio = generate(
                        text=sentence,
                        voice="Bella",
                        stream=True,
                    )
                    stream(audio)
                    break

        # 마지막 buffer 처리
        if buffer.strip():
            audio = generate(text=buffer, voice="Bella", stream=True)
            stream(audio)

# 2. 효과
# - 사용자 음성 입력 (STT)
# - Claude 응답을 점진적으로 받음 (스트림)
# - 문장 단위로 즉시 음성 합성 (스트림 TTS)
# - 전체 응답을 기다리지 않고 듣기 시작
# - 자연스러운 대화 경험

# 3. 응답 시간 비교
# 전통: STT (1s) + Claude (5s) + TTS (3s) = 9s 대기
# 통합: STT (1s) + 첫 문장 (1s) + 점진 재생 = 2s 후 듣기 시작

# 4. 대화형 음성 비서
# 마이크 입력 -> STT (실시간)
#             -> Claude (스트림)
#             -> TTS (스트림)
#             -> 스피커 출력 (실시간)

# 5. 통합 라이브러리
# - LiveKit + Anthropic
# - OpenAI Realtime API 같은 패턴
# - Vapi, Retell 같은 음성 봇 플랫폼
```

## Speaker Notes

실시간 음성 통합으로 자연스러운 대화 인터페이스를 만듭니다.
Claude 응답을 실시간으로 음성으로 변환하는 시나리오입니다.
1번 ElevenLabs streaming TTS와 결합 예시입니다.
stream_to_voice 함수에서 buffer에 청크를 누적합니다.
문장 끝 마침표, 느낌표, 물음표, 개행을 감지해 완성된 문장을 분리합니다.
rindex로 마지막 문장 끝 위치를 찾고 buffer에서 분리합니다.
분리된 문장을 ElevenLabs로 즉시 음성 합성하고 재생합니다.
마지막 buffer 처리로 남은 텍스트도 음성으로 변환합니다.
2번 효과는 매우 강력합니다.
사용자 음성 입력을 STT로 받고 Claude 응답을 스트림으로 받습니다.
문장 단위로 즉시 음성 합성하고 전체 응답을 기다리지 않고 듣기 시작합니다.
자연스러운 대화 경험이 가능합니다.
3번 응답 시간 비교가 인상적입니다.
전통적 방식은 STT 1초, Claude 5초, TTS 3초 합산 9초 대기입니다.
통합 방식은 STT 1초 후 첫 문장 1초로 2초 후 듣기 시작합니다.
4.5배 빠른 응답입니다.
4번 대화형 음성 비서의 일반적 흐름을 보여줍니다.
5번 통합 라이브러리로 LiveKit, OpenAI Realtime API 패턴, Vapi, Retell 같은 음성 봇 플랫폼을 활용할 수 있습니다.
