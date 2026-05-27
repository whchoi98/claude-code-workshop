# Slide 38: 대화 저장과 로드

**Part 2: MESSAGES API 심화**

## Code Blocks

### storage

```python
# 1. JSON 파일 저장
import json
from pathlib import Path

def save_conversation(messages: list, filename: str):
    # ContentBlock을 직렬화 가능한 dict로
    serializable = []
    for m in messages:
        if isinstance(m.get("content"), list):
            content = [
                {"type": b.type, **(
                    {"text": b.text} if b.type == "text"
                    else b.model_dump()
                )}
                for b in m["content"]
            ]
        else:
            content = m["content"]
        serializable.append({
            "role": m["role"],
            "content": content,
        })

    Path(filename).write_text(
        json.dumps(serializable, ensure_ascii=False, indent=2)
    )

def load_conversation(filename: str) -> list:
    return json.loads(Path(filename).read_text())

# 2. SQLAlchemy 모델
from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True)
    user_id = Column(String, index=True)
    title = Column(String)
    messages = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

# 사용
session.add(Conversation(
    user_id="user_1",
    title="Python tutoring",
    messages=messages,
))
session.commit()

# 3. 대화 검색
def search_conversations(user_id: str, query: str):
    return session.query(Conversation).filter(
        Conversation.user_id == user_id,
        Conversation.messages.cast(String).ilike(f"%{query}%"),
    ).order_by(Conversation.updated_at.desc()).all()

# 4. 대화 분기 (fork)
def fork_conversation(conv_id: int, at_message_index: int):
    original = session.query(Conversation).get(conv_id)
    new_messages = original.messages[:at_message_index]
    fork = Conversation(
        user_id=original.user_id,
        title=f"{original.title} (forked)",
        messages=new_messages,
    )
    session.add(fork)
    session.commit()
```

## Speaker Notes

대화 저장과 로드 패턴입니다.
1번 JSON 파일 저장은 간단한 방식입니다.
save_conversation 함수에서 ContentBlock을 직렬화 가능한 dict로 변환합니다.
list 타입 content는 각 block을 type별로 변환하고 string content는 그대로 사용합니다.
load_conversation으로 다시 읽을 수 있습니다.
2번 SQLAlchemy 모델로 영구 DB 저장이 가능합니다.
Conversation 클래스에 user_id, title, messages JSON, created_at, updated_at을 정의합니다.
user_id에 index를 두어 사용자별 조회를 빠르게 합니다.
session.add와 commit으로 저장합니다.
3번 대화 검색은 query로 구현합니다.
messages를 cast해서 String으로 변환하고 ilike로 키워드 검색합니다.
4번 대화 분기 fork 패턴이 강력합니다.
원본 대화의 특정 시점까지만 복사해서 새 분기를 만듭니다.
at_message_index까지의 메시지로 새 Conversation을 만들고 commit합니다.
같은 컨텍스트에서 다른 방향으로 대화를 진행할 때 유용합니다.
Claude.ai의 분기 기능과 유사한 패턴입니다.
