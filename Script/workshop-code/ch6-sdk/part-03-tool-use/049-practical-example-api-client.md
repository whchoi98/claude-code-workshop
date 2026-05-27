# Slide 49: 실전 예시 / API 클라이언트

**Part 3: TOOL USE**

## Code Blocks

### API client

```python
import requests
from anthropic import Anthropic

client = Anthropic()

# 도구: GitHub API 통합
TOOLS = [
    {
        "name": "get_repo_issues",
        "description": "GitHub 저장소의 이슈 목록 조회",
        "input_schema": {
            "type": "object",
            "properties": {
                "owner": {"type": "string"},
                "repo": {"type": "string"},
                "state": {"type": "string", "enum": ["open", "closed", "all"]},
                "labels": {"type": "string", "description": "콤마 구분"},
            },
            "required": ["owner", "repo"],
        },
    },
    {
        "name": "create_issue",
        "description": "GitHub 이슈 생성",
        "input_schema": {
            "type": "object",
            "properties": {
                "owner": {"type": "string"},
                "repo": {"type": "string"},
                "title": {"type": "string"},
                "body": {"type": "string"},
                "labels": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["owner", "repo", "title"],
        },
    },
]

GH_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"Bearer {GH_TOKEN}",
           "Accept": "application/vnd.github+json"}

def get_repo_issues(owner, repo, state="open", labels=None):
    params = {"state": state}
    if labels:
        params["labels"] = labels
    r = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/issues",
        headers=HEADERS, params=params, timeout=10,
    )
    r.raise_for_status()
    return [{
        "number": i["number"],
        "title": i["title"],
        "labels": [l["name"] for l in i["labels"]],
    } for i in r.json()[:20]]

def create_issue(owner, repo, title, body="", labels=None):
    r = requests.post(
        f"https://api.github.com/repos/{owner}/{repo}/issues",
        headers=HEADERS,
        json={"title": title, "body": body, "labels": labels or []},
        timeout=10,
    )
    r.raise_for_status()
    return {"number": r.json()["number"], "url": r.json()["html_url"]}

FUNCS = {"get_repo_issues": get_repo_issues, "create_issue": create_issue}
```

## Speaker Notes

실전 예시 API 클라이언트 통합입니다.
requests 라이브러리로 GitHub API와 Claude를 연결합니다.
도구 2개를 정의합니다.
get_repo_issues는 저장소의 이슈 목록을 가져오고 state와 labels로 필터링 가능합니다.
state는 enum으로 open, closed, all 중 하나입니다.
create_issue는 새 이슈를 생성하고 title, body, labels를 받습니다.
GH_TOKEN 환경변수로 인증합니다.
GITHUB_TOKEN은 PAT 또는 GitHub App token입니다.
HEADERS에 Authorization과 Accept를 명시합니다.
get_repo_issues 구현은 GET 요청으로 이슈 목록을 가져옵니다.
params로 state와 labels를 전달합니다.
response에서 number, title, labels만 추출해 토큰을 절약합니다.
timeout 10초로 안정성을 확보합니다.
create_issue 구현은 POST 요청입니다.
json body에 title, body, labels를 전달합니다.
응답에서 issue number와 URL만 반환합니다.
FUNCS dict로 매핑하면 Claude가 자연어로 GitHub와 상호작용할 수 있게 됩니다.
예를 들어 open 상태인 bug 라벨 이슈를 보여줘 같은 명령이 가능합니다.
