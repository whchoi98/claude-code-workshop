# Slide 73: Official server: filesystem

**Part 5: MCP 기본과 공식 서버**

## Code Blocks

### filesystem

```bash
# 1. settings.json 등록
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/me/Documents",
        "/Users/me/Code",
        "/Users/me/Notes"
      ]
    }
  }
}

# 2. 제공되는 도구
- read_file(path)              - 파일 읽기
- write_file(path, content)    - 파일 쓰기
- list_directory(path)          - 디렉토리 목록
- search_files(path, pattern)   - 파일 검색
- move_file(source, dest)      - 파일 이동

# 3. 사용 예시 (Claude에게)
> ~/Documents의 모든 .md 파일을 요약해 줘

# Claude가 자동으로 사용
1. list_directory(~/Documents) 호출
2. .md 파일 필터링
3. 각각 read_file 호출
4. 요약 응답

# 4. 보안 주의
- 권한 부여한 디렉토리 외 접근 불가
- 다른 사용자 디렉토리는 명시 안 하면 막힘
```

## Speaker Notes

첫 번째 공식 서버는 filesystem입니다.
로컬 파일 시스템 접근을 제공하는 가장 기본적인 서버입니다.
settings.json 등록 방법을 봅니다.
npx로 @modelcontextprotocol/server-filesystem 패키지를 실행합니다.
args에 접근 허용할 디렉토리 경로들을 나열합니다.
Documents, Code, Notes 같은 자주 사용하는 디렉토리를 등록합니다.
제공되는 도구는 5가지입니다.
read_file로 파일 읽기, write_file로 쓰기, list_directory로 목록 조회, search_files로 검색, move_file로 이동입니다.
사용 예시를 봅니다.
Documents의 모든 .md 파일을 요약해 달라고 요청하면 Claude가 자동으로 list_directory를 호출하고 .md 파일을 필터링한 후 각각 read_file로 내용을 읽고 요약합니다.
보안 측면에서 권한 부여한 디렉토리 외에는 접근할 수 없습니다.
다른 사용자 디렉토리는 명시하지 않으면 차단됩니다.
