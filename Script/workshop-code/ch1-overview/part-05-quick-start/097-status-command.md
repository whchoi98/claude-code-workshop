# Slide 97: /status 명령

**Part 5: QUICK START**

## Code Blocks

### /status

```
> /status

Session
  ID:              sess_abc123
  Started:         2026-05-24 09:32 (5m ago)
  Working dir:     ~/projects/my-app
  CLAUDE.md:       loaded (450 lines)

Auth
  Method:          OAuth (Claude Max)
  User:            user@example.com

Model
  Default:         claude-sonnet-4-5
  Small/fast:      claude-haiku-4-5 (subagents)

Permissions
  allow rules:     5
  ask rules:       2
  deny rules:      3

Usage (this session)
  Input tokens:    12,403
  Output tokens:   3,210
  Context used:    8% of 200K
```

## Speaker Notes

/status 명령은 현재 세션의 종합 상태를 한 번에 보여 줍니다.
Session 섹션은 세션 ID, 시작 시간, 작업 디렉토리, CLAUDE.md 로드 여부를 표시합니다.
Auth 섹션은 인증 방식과 사용자 이메일, Model 섹션은 기본 모델과 Subagent용 빠른 모델을 표시합니다.
Permissions 섹션은 현재 적용 중인 권한 규칙 개수를 카테고리별로 보여 주고, Usage 섹션은 이번 세션의 토큰 사용량과 컨텍스트 윈도우 사용률을 표시합니다.
컨텍스트가 70%를 넘어가면 /compact를 고려하라는 안내가 함께 표시됩니다.
작업 중에 한 번씩 /status를 실행해 상태를 점검하는 습관을 들이면 좋습니다.
