# Slide 61: Node Manager Volta

**Part 3: INSTALLATION**

## Code Blocks

### Volta

```bash
# 1. Volta 설치
curl https://get.volta.sh | bash
# 또는 Windows: winget install Volta.Volta

# 2. Node 설치 + 기본 설정
volta install node@20
volta install npm@10

# 3. 프로젝트별 도구 고정 (package.json에 자동 기록)
cd my-project
volta pin node@20
volta pin npm@10

# 4. 패키지 도구도 함께 관리
volta install @anthropic-ai/claude-code
# /home/user/.volta/bin/claude

# 5. 검증
volta list
claude --version
```

## Speaker Notes

Volta는 Node뿐만 아니라 JavaScript 도구 전체를 관리하는 매니저입니다.
1단계 get.volta.sh 스크립트나 WinGet으로 설치합니다.
2단계 volta install node@20 명령으로 Node 20을 설치합니다.
3단계 프로젝트 디렉토리에서 volta pin 명령을 사용하면 해당 프로젝트의 package.json에 사용할 Node와 npm 버전이 자동으로 기록됩니다.
협업하는 동료가 같은 프로젝트에 진입하면 Volta가 자동으로 동일한 버전을 사용합니다.
4단계 npm 글로벌 패키지인 Claude Code도 volta install로 관리하면 PATH 같은 환경 설정 문제 없이 깔끔하게 설치됩니다.
macOS, Linux, Windows 모두 동일하게 동작하며 cross-platform 일관성이 뛰어납니다.
