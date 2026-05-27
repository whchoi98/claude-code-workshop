# Slide 98: 디렉토리와 캐시 환경변수

**Part 6: 환경변수와 설정**

## Code Blocks

### dir env

```bash
# 1. 설정 디렉토리
export CLAUDE_CODE_HOME=~/.claude
# 기본값: ~/.claude
# 안에 들어가는 것: settings.json, glossary.md, sessions/

# 2. 세션 디렉토리
export CLAUDE_CODE_SESSIONS_DIR=~/.claude/sessions
# 세션별 메타데이터와 컨텍스트 저장

# 3. 캐시 디렉토리
export CLAUDE_CODE_CACHE_DIR=~/.cache/claude
# 모델 응답 캐시, MCP 결과 캐시

# 4. 로그 디렉토리
export CLAUDE_CODE_LOG_DIR=/var/log/claude
# 모든 로그 파일 저장 위치

# 5. 사내 표준 위치 (관리자 권장)
# /opt/claude/    : 시스템 전역 도구
# /etc/claude/    : 시스템 전역 설정 (managed-settings)
# /var/log/claude/ : 시스템 로그
# /var/cache/claude/ : 시스템 캐시

# 6. 캐시 정리
$ rm -rf $CLAUDE_CODE_CACHE_DIR
# 또는
$ claude cache clear

# 7. 캐시 비활성화 (디버깅 시)
export CLAUDE_CODE_DISABLE_CACHE=1

# 8. 임시 디렉토리
export TMPDIR=/var/tmp/claude
# claude가 사용하는 임시 파일 위치
# 기본값: /tmp 또는 시스템 기본

# 9. 디렉토리 권한 (보안)
$ chmod 700 ~/.claude      # 본인만 접근
$ chmod 600 ~/.claude/settings.json    # 본인만 읽기/쓰기

# 10. 디렉토리 백업
$ tar czf claude-backup.tar.gz ~/.claude
# settings, glossary 등 백업
```

## Speaker Notes

디렉토리와 캐시 환경변수로 저장 위치를 커스터마이즈합니다.
1번 CLAUDE_CODE_HOME으로 설정 디렉토리를 명시합니다.
기본값은 홈 디렉토리의 .claude이고 settings.json, glossary.md, sessions 디렉토리가 들어 있습니다.
2번 CLAUDE_CODE_SESSIONS_DIR로 세션 디렉토리를 별도 위치로 분리할 수 있습니다.
3번 CLAUDE_CODE_CACHE_DIR로 캐시 디렉토리를 명시합니다.
모델 응답 캐시와 MCP 결과 캐시가 저장됩니다.
4번 CLAUDE_CODE_LOG_DIR로 로그 디렉토리를 분리합니다.
5번 사내 표준 위치는 시스템 전역 도구는 /opt, 설정은 /etc, 로그는 /var/log, 캐시는 /var/cache에 두는 것이 권장됩니다.
6번 캐시 정리는 rm으로 직접 삭제하거나 claude cache clear 명령을 사용합니다.
7번 CLAUDE_CODE_DISABLE_CACHE를 1로 설정하면 캐시를 사용하지 않습니다.
디버깅 시 유용합니다.
8번 TMPDIR로 임시 파일 위치를 명시할 수 있습니다.
9번 디렉토리 권한은 보안상 chmod 700, 파일은 600으로 본인만 접근하게 설정합니다.
10번 디렉토리 백업은 tar로 압축해 보관할 수 있습니다.
