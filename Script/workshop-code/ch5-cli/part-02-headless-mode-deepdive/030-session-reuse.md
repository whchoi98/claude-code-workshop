# Slide 30: 세션 재사용

**Part 2: HEADLESS 모드 심화**

## Code Blocks

### session reuse

```bash
# --resume : 마지막 세션 자동 복귀
$ claude --resume
> 그 다음 단계는?  # 이전 컨텍스트 그대로

# --resume과 -p 조합
$ claude --resume -p "그 다음은?"

# --continue <session_id> : 특정 세션 명시
$ claude --continue ses_abc123 -p "추가 분석"

# 세션 ID 추출
$ S=$(claude -p "초기 분석" --output-format json \
      | jq -r '.session_id')
$ echo "Session: $S"

# 다단계 자동화 예시
# Step 1: 코드 분석
S=$(claude -p "src/ 디렉토리 종합 분석" \
    --allowed-tools "Read,Grep,Glob" \
    --output-format json | jq -r '.session_id')

# Step 2: 같은 컨텍스트에서 개선안
claude --continue "$S" -p "이제 구체적인 개선안 5개" \
    --max-turns 10 > improvements.md

# Step 3: 우선순위 선정
claude --continue "$S" -p "위 5개 중 ROI 높은 3개 선정" \
    > priorities.md

# Step 4: 구현 가이드
claude --continue "$S" -p "선정된 3개의 구체적 구현 가이드" \
    --allowed-tools "Read,Write" \
    --max-turns 20

# 세션 만료
# 약 30분간 활동 없으면 자동 만료
# 만료 후 --continue는 새 세션 시작
```

## Speaker Notes

세션 재사용 옵션 두 가지를 살펴봅니다.
--resume은 마지막 세션 자동 복귀입니다.
인자 없이 사용하면 대화형으로, -p와 함께 사용하면 Headless로 이어집니다.
--continue session_id는 특정 세션을 명시적으로 이어갑니다.
여러 세션을 동시 관리할 때 필요합니다.
세션 ID는 JSON 출력에서 jq로 추출합니다.
다단계 자동화의 핵심 패턴입니다.
Step 1에서 코드 분석을 하고 session_id를 변수로 저장합니다.
Step 2에서 같은 컨텍스트에서 개선안 5개를 받습니다.
Step 3에서 위 5개 중 ROI 높은 3개를 선정합니다.
Step 4에서 선정된 3개의 구체적 구현 가이드를 작성합니다.
각 단계가 이전 단계의 컨텍스트를 모두 기억하고 있어 자연스러운 흐름이 됩니다.
세션은 약 30분간 활동이 없으면 자동 만료됩니다.
만료 후 --continue는 새 세션을 시작합니다.
