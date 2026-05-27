# Slide 53: 에이전트 패턴

**Part 3: TOOL USE**

## Code Blocks

### agent pattern

```python
# 1. 단순 에이전트 (1 task 완료)
def simple_agent(task: str, tools, funcs, max_iters=15):
    messages = [{"role": "user", "content": task}]

    for _ in range(max_iters):
        r = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=2048,
            tools=tools,
            messages=messages,
        )
        messages.append({"role": "assistant", "content": r.content})

        if r.stop_reason != "tool_use":
            return "".join(b.text for b in r.content if b.type=="text")

        results = []
        for b in r.content:
            if b.type == "tool_use":
                out = funcs[b.name](**b.input)
                results.append({
                    "type":"tool_result",
                    "tool_use_id":b.id,
                    "content":json.dumps(out),
                })
        messages.append({"role":"user", "content":results})

    return "Max iterations reached"

# 2. 사용 예시
TOOLS = [READ_TOOL, WRITE_TOOL, LIST_TOOL, SHELL_TOOL]
result = simple_agent(
    "src/ 디렉토리의 Python 파일들을 분석하고 README.md 작성",
    TOOLS, FUNCS,
)

# 3. 점진적 결과 보고 (callback)
def agent_with_callback(task, tools, funcs, on_progress):
    messages = [{"role": "user", "content": task}]
    iter_count = 0

    while True:
        r = client.messages.create(...)
        iter_count += 1

        # 진행 상황 알림
        for b in r.content:
            if b.type == "tool_use":
                on_progress({
                    "iteration": iter_count,
                    "tool": b.name,
                    "input": b.input,
                })
            elif b.type == "text":
                on_progress({
                    "iteration": iter_count,
                    "thinking": b.text,
                })

        # ... 위와 동일한 로직 ...

# 사용
def progress(info):
    if "tool" in info:
        print(f"[{info['iteration']}] 도구: {info['tool']}")
    elif "thinking" in info:
        print(f"[{info['iteration']}] 생각: {info['thinking'][:60]}...")

agent_with_callback(task, TOOLS, FUNCS, progress)
```

## Speaker Notes

에이전트 패턴은 Tool Use 기반의 자율 동작 구현입니다.
1번 단순 에이전트는 한 task를 완료하는 패턴입니다.
simple_agent 함수에서 task를 시작으로 max_iters까지 반복합니다.
각 iteration에서 messages.create를 호출하고 응답을 처리합니다.
stop_reason이 tool_use면 도구를 실행하고 결과를 다음 호출에 전달합니다.
stop_reason이 end_turn 등이면 최종 응답을 추출해 반환합니다.
max_iters에 도달하면 강제 종료해 무한 루프를 방지합니다.
2번 사용 예시는 매우 강력합니다.
READ, WRITE, LIST, SHELL 도구를 주고 src 디렉토리 분석 후 README 작성 같은 복합 작업을 한 줄로 요청합니다.
Claude가 자율적으로 도구를 사용해 작업을 완성합니다.
3번 점진적 결과 보고는 callback 패턴입니다.
각 iteration의 도구 호출과 생각 과정을 callback으로 보고합니다.
on_progress 함수에서 tool 정보와 thinking 텍스트를 받아 UI에 표시할 수 있습니다.
사용 시 progress 함수를 정의해 콘솔이나 UI에 출력하면 사용자가 에이전트의 작업 진행을 실시간으로 볼 수 있습니다.
CLI에서 Headless 모드와 비슷한 사용자 경험을 SDK에서 직접 구현할 수 있습니다.
