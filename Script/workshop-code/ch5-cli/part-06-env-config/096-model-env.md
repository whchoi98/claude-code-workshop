# Slide 96: 모델 환경변수

**Part 6: 환경변수와 설정**

## Code Blocks

### model env

```bash
# 1. 기본 모델 (settings.json도 가능)
export ANTHROPIC_MODEL=claude-sonnet-4-5

# 2. 모델별 사용 패턴
# 환경변수 우선순위
# --model 옵션 > ANTHROPIC_MODEL > settings.json model > default

# 3. settings.json의 modelAlias 활용
# ~/.claude/settings.json
{
  "modelAlias": {
    "fast": "claude-haiku-4-5",
    "smart": "claude-opus-4-5",
    "review": "claude-sonnet-4-5",
    "translate": "claude-haiku-4-5"
  }
}

# 사용 시
$ claude -p "..." --model fast
$ claude -p "..." --model smart

# 4. 모델 ID 표 (2026년 기준)
# Anthropic Direct
# - claude-sonnet-4-5 (기본)
# - claude-haiku-4-5 (저비용)
# - claude-opus-4-5 (최고 성능)

# AWS Bedrock
# - us.anthropic.claude-sonnet-4-5-20250514-v1:0
# - us.anthropic.claude-haiku-4-5-20251017-v1:0
# - us.anthropic.claude-opus-4-5-20250629-v1:0
# (cross-region inference profile 권장)

# GCP Vertex AI
# - claude-sonnet-4-5@20250514
# - claude-haiku-4-5@20251017
# - claude-opus-4-5@20250629

# 5. 모델 확인
$ claude doctor | grep -i model
$ claude -p "현재 사용 중인 모델은?" \
    --output-format json | jq -r '.model'
```

## Speaker Notes

모델 환경변수와 별명 시스템입니다.
1번 ANTHROPIC_MODEL로 기본 모델을 명시합니다.
settings.json에서도 가능합니다.
2번 모델 선택 우선순위는 명확합니다.
--model 옵션, ANTHROPIC_MODEL 환경변수, settings의 model, 기본값 순입니다.
3번 settings.json의 modelAlias 활용이 권장됩니다.
예시처럼 fast, smart, review, translate 같은 의미있는 별명을 정의합니다.
사용 시 --model fast처럼 별명을 직접 사용할 수 있어 가독성이 높습니다.
4번 모델 ID 표를 경로별로 정리합니다.
Anthropic Direct는 단순한 이름입니다.
AWS Bedrock은 region prefix와 버전 suffix가 포함됩니다.
cross-region inference profile 사용이 권장됩니다.
GCP Vertex AI는 at 기호로 버전이 분리됩니다.
5번 모델 확인은 두 가지 방법이 있습니다.
claude doctor에서 grep model로 현재 설정을 확인하고 claude -p로 직접 물어볼 수도 있습니다.
JSON 응답의 .model 필드에 사용된 모델 ID가 포함됩니다.
