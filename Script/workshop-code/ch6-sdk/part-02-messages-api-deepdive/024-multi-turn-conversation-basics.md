# Slide 24: 멀티턴 대화 기본

**Part 2: MESSAGES API 심화**

## Code Blocks

### multi-turn

```python
# 1. 단순 멀티턴 (메시지 누적)
messages = []

def chat(user_input: str) -> str:
    messages.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=messages,
    )

    assistant_text = response.content[0].text
    messages.append({
        "role": "assistant",
        "content": response.content,    # 전체 content 보존
    })
    return assistant_text

# 사용
print(chat("Python 데코레이터 설명"))
print(chat("그 예시를 더 보여줘"))
print(chat("@property와 무엇이 다른가"))

# 2. 클래스 기반 대화 관리
class Conversation:
    def __init__(self, system: str = None):
        self.system = system
        self.messages = []

    def send(self, user_input: str) -> str:
        self.messages.append({
            "role": "user",
            "content": user_input,
        })

        kwargs = {
            "model": "claude-sonnet-4-5",
            "max_tokens": 1024,
            "messages": self.messages,
        }
        if self.system:
            kwargs["system"] = self.system

        response = client.messages.create(**kwargs)

        self.messages.append({
            "role": "assistant",
            "content": response.content,
        })
        return response.content[0].text

    def reset(self):
        self.messages = []

# 사용
conv = Conversation(system="당신은 코드 멘토")
print(conv.send("Python 리스트 컴프리헨션"))
print(conv.send("성능은 어떤가"))
```

## Speaker Notes

멀티턴 대화 기본 패턴입니다.
1번 단순 멀티턴은 messages 배열에 누적하는 방식입니다.
chat 함수에서 user 메시지를 추가하고 호출 후 assistant 응답을 추가합니다.
response.content를 그대로 보존해 다음 호출 시 context로 사용합니다.
사용은 chat 함수를 여러 번 호출하면 대화가 자연스럽게 이어집니다.
2번 클래스 기반 대화 관리가 더 깔끔합니다.
Conversation 클래스에 system과 messages를 멤버로 둡니다.
send 메서드에서 user 메시지 추가, claude 호출, assistant 메시지 추가를 한 번에 처리합니다.
system이 있으면 kwargs에 추가하는 조건부 패턴을 사용합니다.
reset 메서드로 새 대화를 시작할 수 있습니다.
사용은 인스턴스를 만들고 send를 여러 번 호출합니다.
클래스 기반은 상태 관리가 자연스럽고 여러 대화를 동시에 다룰 수 있습니다.
웹 앱에서 사용자별 Conversation 인스턴스를 유지하는 패턴이 일반적입니다.
