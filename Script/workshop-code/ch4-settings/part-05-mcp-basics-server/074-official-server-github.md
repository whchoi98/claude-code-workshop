# Slide 74: Official server: github

**Part 5: MCP 기본과 공식 서버**

## Code Blocks

### github

```bash
# 1. 토큰 발급
# https://github.com/settings/tokens → Generate new token
# 권한: repo (read+write), workflow, read:org

# 2. settings.json 등록
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GH_TOKEN}"
      }
    }
  }
}

# 3. 제공되는 주요 도구
- create_issue(owner, repo, title, body)
- create_pull_request(owner, repo, title, head, base)
- get_pull_request(owner, repo, pr_number)
- merge_pull_request(owner, repo, pr_number)
- search_code(query)
- search_issues(query)
- get_file_contents(owner, repo, path)
- create_or_update_file(owner, repo, path, content)

# 4. 사용 예시
> 우리 organization의 모든 open PR을 요약해 줘
> 이 코드 변경사항으로 PR을 만들어 줘

# 5. 인증 옵션
- PAT (Personal Access Token) - 개인용
- GitHub App - 조직용 (SSO 통합 가능)
```

## Speaker Notes

두 번째 공식 서버는 github입니다.
GitHub 통합을 위한 강력한 서버입니다.
사용 절차를 봅니다.
1단계 토큰을 발급합니다.
GitHub Settings의 Developer settings에서 Personal Access Token을 생성합니다.
권한은 repo, workflow, read:org를 부여합니다.
2단계 settings.json에 등록합니다.
npx로 server-github 패키지를 실행하고 env에 토큰을 주입합니다.
3단계 제공되는 주요 도구를 살펴봅니다.
create_issue, create_pull_request, get_pull_request, merge_pull_request 같은 PR과 Issue 관리 도구가 있습니다.
search_code와 search_issues로 검색이 가능하며 get_file_contents로 파일 내용을 가져올 수 있습니다.
create_or_update_file로 파일을 직접 수정할 수도 있습니다.
4단계 사용 예시입니다.
organization의 모든 open PR을 요약해 달라거나 코드 변경사항으로 PR을 만들어 달라고 요청할 수 있습니다.
5단계 인증 옵션입니다.
PAT는 개인용, GitHub App은 조직용으로 SSO 통합이 가능합니다.
