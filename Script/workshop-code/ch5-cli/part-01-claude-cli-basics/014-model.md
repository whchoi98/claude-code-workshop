# Slide 14: 모델 옵션

**Part 1: claude 명령 기본**

## Code Blocks

### model

```bash
# 1. --model : 모델 선택
$ claude -p "..." --model claude-sonnet-4-5    # 기본
$ claude -p "..." --model claude-haiku-4-5     # 빠르고 저렴
$ claude -p "..." --model claude-opus-4-5      # 최고 성능

# settings.json의 modelAlias 사용 가능
$ claude -p "..." --model fast    # → Haiku
$ claude -p "..." --model smart   # → Opus

# 2. --max-turns : 최대 도구 호출 횟수
$ claude -p "프로젝트 전체 분석" --max-turns 10
# 도구를 10회 호출하면 종료 (무한 루프 방지)
# 기본값: 30, 권장: 작업 복잡도에 맞춰 조정

# 3. --max-tokens : 응답 토큰 제한
$ claude -p "이 코드 한 줄 평" --max-tokens 200
# 응답이 200 토큰을 넘으면 잘림
# 짧은 응답을 강제할 때 유용

# 4. 비용 절감 패턴
# - 간단한 작업: Haiku (10x 저렴)
# - 표준 작업: Sonnet (기본, 균형)
# - 복잡한 분석: Opus (10x 비싸지만 정확)

# 5. CI 환경 권장 설정
$ claude -p "..." \
    --model claude-haiku-4-5 \
    --max-turns 20 \
    --max-tokens 4000 \
    --output-format json
```

## Speaker Notes

모델 옵션을 살펴봅니다.
첫째, --model로 모델을 선택합니다.
claude-sonnet-4-5가 기본이고 haiku는 빠르고 저렴하며 opus는 최고 성능입니다.
settings.json의 modelAlias를 사용해 fast, smart 같은 별명도 사용 가능합니다.
둘째, --max-turns는 최대 도구 호출 횟수입니다.
도구를 명시한 횟수만큼 호출하면 종료합니다.
무한 루프나 의도하지 않은 폭주를 방지합니다.
기본값은 30이고 작업 복잡도에 맞춰 조정합니다.
셋째, --max-tokens는 응답 토큰 제한입니다.
짧은 응답을 강제할 때 유용합니다.
넷째, 비용 절감 패턴입니다.
간단한 작업은 Haiku로 10배 절감하고 표준 작업은 Sonnet, 복잡한 분석은 Opus를 사용합니다.
다섯째, CI 환경 권장 설정입니다.
Haiku, max-turns 20, max-tokens 4000, output-format json 조합이 비용과 안정성의 균형점입니다.
