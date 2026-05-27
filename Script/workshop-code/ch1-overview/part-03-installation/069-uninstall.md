# Slide 69: Uninstall

**Part 3: INSTALLATION**

## Code Blocks

### uninstall

```bash
# 1. 설치 방식별 제거

# npm으로 설치한 경우
npm uninstall -g @anthropic-ai/claude-code

# brew로 설치한 경우
brew uninstall --cask claude-code

# native install.sh로 설치한 경우
rm -f ~/.claude/bin/claude
# PATH에서 ~/.claude/bin 제거 (~/.bashrc 편집)

# Windows MSI로 설치한 경우
# 제어판 > 프로그램 추가/제거 > Claude Code 제거

# 2. 사용자 설정/세션 클린업 (선택)
rm -rf ~/.claude/sessions     # 세션 기록 삭제
rm -rf ~/.claude/logs         # 로그 삭제
rm -f  ~/.claude/settings.json # 설정 삭제 (주의)

# 3. 모든 흔적 완전 제거
rm -rf ~/.claude              # 모든 데이터 삭제
```

## Speaker Notes

제거 절차도 알아두면 좋습니다.
우선 설치 방식별로 적절한 제거 명령을 사용합니다.
npm으로 설치했다면 npm uninstall -g, brew라면 brew uninstall --cask, native install.sh라면 ~/.claude/bin/claude 파일을 삭제하고 PATH 설정을 제거합니다.
Windows MSI는 제어판의 프로그램 추가/제거 메뉴를 사용합니다.
패키지 제거만으로는 사용자 데이터가 남아 있을 수 있는데, 세션 기록은 ~/.claude/sessions, 로그는 ~/.claude/logs, 설정은 ~/.claude/settings.json에 저장됩니다.
필요에 따라 부분적으로 또는 전체적으로 ~/.claude 디렉토리를 삭제할 수 있습니다.
settings.json에는 MCP 설정과 권한 규칙이 들어 있어 한 번 삭제하면 복구하기 번거로우므로 백업 후 진행하시기 바랍니다.
