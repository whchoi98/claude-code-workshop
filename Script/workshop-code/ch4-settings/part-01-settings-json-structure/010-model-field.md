# Slide 10: model field

**Part 1: settings.json 구조**

## Code Blocks

### model

```bash
{
  "model": "claude-sonnet-4-5",

  "modelAlias": {
    "fast": "claude-haiku-4-5",
    "smart": "claude-opus-4-5",
    "default": "claude-sonnet-4-5"
  }
}

# 사용 방법
# 1. 기본 모델: model 필드 값 사용
# 2. 명시 호출: > /model smart  → Opus 사용
# 3. Subagent에서 사용:
#    .claude/agents/my-agent.md frontmatter에
#    model: smart

# 비용 통제 패턴
# managed-settings에서 model 강제:
{
  "model": "claude-sonnet-4-5",
  "modelAlias": {
    "smart": "claude-sonnet-4-5"  # smart도 sonnet으로
  }
}
# 사용자가 smart를 호출해도 Sonnet 사용

# 모델 차단
# managed-settings deny:
{
  "deniedModels": ["claude-opus-4-5"]
}
```

## Speaker Notes

model 옵션과 별명 시스템을 살펴봅니다.
model 필드에 기본 모델을 명시합니다.
claude-sonnet-4-5 같은 정확한 모델 ID를 지정합니다.
modelAlias에 사용자 친화적 별명을 등록할 수 있습니다.
fast는 Haiku, smart는 Opus, default는 Sonnet 같은 식으로 설정합니다.
사용 방법은 세 가지입니다.
기본 모델은 model 필드 값을 사용합니다.
명시 호출은 /model smart 명령으로 Opus를 사용합니다.
Subagent에서는 frontmatter의 model 필드에 별명을 적습니다.
비용 통제 패턴이 있습니다.
managed-settings에서 modelAlias로 smart도 Sonnet으로 매핑하면 사용자가 smart를 호출해도 Sonnet이 사용됩니다.
또는 deniedModels로 Opus를 명시 차단할 수도 있습니다.
