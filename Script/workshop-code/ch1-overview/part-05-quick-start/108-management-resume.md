# Slide 108: 세션 관리 /resume

**Part 5: QUICK START**

## Code Blocks

### resume

```bash
# 1. 사용 가능한 세션 목록
$ claude --list-sessions
sess_abc123  | ~/projects/my-app    | 2026-05-24 10:30 | 23 messages
sess_def456  | ~/projects/api-svc   | 2026-05-23 18:15 | 41 messages
sess_ghi789  | ~/projects/my-app    | 2026-05-23 09:00 | 89 messages

# 2. 특정 세션 재개
$ claude -r sess_abc123
> [Resumed session sess_abc123]
> [Loaded 23 messages, context 24% used]

# 3. REPL 내부에서
> /resume sess_abc123

# 4. 세션 검색
$ claude --search-sessions "pagination"
sess_abc123  | matched: "cursor-based pagination", "Link header"

# 5. 세션 삭제 (오래된 정리)
$ claude --delete-session sess_ghi789
```

## Speaker Notes

세션 관리 명령을 살펴봅니다.
claude --list-sessions로 모든 세션 목록을 볼 수 있습니다.
세션 ID, 작업 디렉토리, 마지막 활동 시간, 메시지 수가 표시됩니다.
특정 세션을 재개하려면 claude -r 다음에 세션 ID를 지정합니다.
재개하면 이전 메시지와 컨텍스트가 복원되어 그 시점부터 작업을 이어갈 수 있습니다.
REPL 내부에서도 /resume 명령으로 다른 세션으로 전환 가능합니다.
--search-sessions로 키워드 검색이 가능해 "pagination" 같은 단어를 포함한 세션을 빠르게 찾을 수 있습니다.
오래된 세션은 --delete-session으로 정리할 수 있습니다.
디스크 공간 절약과 검색 성능 향상에 도움이 됩니다.
