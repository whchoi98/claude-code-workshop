# Slide 133: Lab 1 / First settings.json

**Part 9: RECAP & 4 LABS**

## Code Blocks

### Lab 1

```bash
# 1. 사용자 전역 settings 디렉토리
$ mkdir -p ~/.claude

# 2. settings.json 작성
$ cat > ~/.claude/settings.json <<'EOF'
{
  "permissions": {
    "allow": [
      "Read", "Grep", "Glob",
      "Bash(npm test:*)", "Bash(npm run lint)",
      "Bash(git diff:*)", "Bash(git log:*)", "Bash(git status)"
    ],
    "ask": ["Edit", "Write", "Bash(git push:*)"],
    "deny": [
      "Bash(rm -rf:*)", "Bash(curl:*)",
      "Read(**/.env*)", "Read(**/.ssh/**)"
    ]
  },
  "model": "claude-sonnet-4-5",
  "modelAlias": {
    "fast": "claude-haiku-4-5",
    "smart": "claude-opus-4-5"
  },
  "theme": "dark",
  "outputStyle": "concise",
  "editor": {
    "tabWidth": 2,
    "preferredQuotes": "single"
  }
}
EOF

# 3. 검증
$ claude doctor
# Settings 섹션 확인 - 모든 설정이 인식되어야 함

# 4. 실제 사용 테스트
$ claude
> /permissions
> /model fast    # 모델 전환 테스트
```

## Speaker Notes

Lab 1은 첫 settings.json 작성 실습입니다.
약 20분 소요됩니다.
5단계 흐름으로 진행됩니다.
1단계 사용자 전역 디렉토리 ~/.claude를 생성합니다.
2단계 settings.json을 작성합니다.
permissions에 allow는 안전한 도구들, ask는 변경 도구들, deny는 위험 명령들을 명시합니다.
model을 Sonnet으로 기본 지정하고 fast와 smart 별명을 등록합니다.
3단계 model alias를 설정합니다.
fast는 Haiku로, smart는 Opus로 매핑합니다.
4단계 theme과 editor 선호를 추가합니다.
dark 테마, concise 출력 스타일, tab width 2와 single quotes를 명시합니다.
5단계 claude doctor로 검증합니다.
Settings 섹션에서 모든 설정이 정상 인식되는지 확인합니다.
실제 사용 테스트로 /permissions와 /model fast를 시도해 봅니다.
본인의 첫 개인화된 Claude Code 환경이 완성됩니다.
