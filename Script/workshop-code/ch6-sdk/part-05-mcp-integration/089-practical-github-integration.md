# Slide 89: 실전 / GitHub 통합

**Part 5: MCP SDK 통합**

## Code Blocks

### GitHub MCP

```python
# pr_automation.py - GitHub MCP를 SDK로 활용
import os
import anthropic

client = anthropic.Anthropic()

def analyze_pr(repo_owner: str, repo_name: str, pr_number: int):
    response = client.beta.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=2048,
        mcp_servers=[{
            "type": "url",
            "url": "https://mcp.github.com/mcp",
            "name": "github",
            "authorization_token": os.getenv("GITHUB_TOKEN"),
        }],
        # 권한 좁힘 - 읽기만
        tools=[
            {"name": "github__get_pull_request"},
            {"name": "github__get_pull_request_files"},
            {"name": "github__get_pull_request_comments"},
            {"name": "github__list_commits"},
        ],
        system="""당신은 시니어 코드 리뷰어입니다.
        PR을 분석하고 마크다운 보고서를 작성합니다.
        - 코드 품질
        - 보안 위험
        - 테스트 커버리지
        - 개선 제안""",
        messages=[{
            "role": "user",
            "content": f"{repo_owner}/{repo_name} 저장소의 PR #{pr_number}를 분석해 주세요.",
        }],
        betas=["mcp-client-2025-04-04"],
    )

    # 결과 추출
    review_text = "".join(
        b.text for b in response.content if b.type == "text"
    )

    # MCP 도구 사용 통계
    tools_called = sum(
        1 for b in response.content if b.type == "mcp_tool_use"
    )

    return {
        "review": review_text,
        "tools_called": tools_called,
        "tokens": response.usage.model_dump(),
    }

# 사용
result = analyze_pr("anthropics", "claude-code", 123)
print(result["review"])
print(f"MCP 도구 호출: {result['tools_called']}회")
print(f"토큰 사용: {result['tokens']}")

# 효과
# - 직접 GitHub API 코드 작성 안 함
# - Claude가 자동으로 적절한 도구 선택
# - PR diff, 코멘트, 커밋 등을 자율적으로 조회
# - 종합 분석 후 보고서 생성
```

## Speaker Notes

실전 GitHub MCP 통합 예시입니다.
analyze_pr 함수에서 PR 분석을 자동화합니다.
mcp_servers에 GitHub MCP를 명시합니다.
tools 매개변수로 권한을 좁혀 읽기 전용 도구만 허용합니다.
get_pull_request, get_files, get_comments, list_commits 네 도구만 사용 가능합니다.
create_issue 같은 쓰기 도구는 차단됩니다.
system prompt에 시니어 코드 리뷰어 역할과 분석 관점 4가지를 명시합니다.
user 메시지에 PR 정보만 전달하면 Claude가 자율적으로 도구를 선택해 호출합니다.
betas에 mcp-client를 명시해 beta 기능을 활성화합니다.
결과 추출은 text 블록을 join해 리뷰 텍스트로 만듭니다.
MCP 도구 호출 횟수와 토큰 사용량을 통계로 반환합니다.
사용은 함수 한 번 호출이면 됩니다.
효과가 놀랍습니다.
직접 GitHub API 코드를 작성하지 않습니다.
Claude가 자동으로 적절한 도구를 선택해서 호출합니다.
PR diff, 코멘트, 커밋 등을 자율적으로 조회한 후 종합 분석 보고서를 생성합니다.
MCP 통합이 자동화 코드를 얼마나 단순화하는지 보여주는 예시입니다.
