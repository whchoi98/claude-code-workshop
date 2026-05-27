# Slide 26: Specificity rules

**Part 2: PERMISSIONS 심화**

## Code Blocks

### specificity

```bash
# 시나리오: 두 규칙이 모두 매칭될 때

# 예시 1: allow와 deny 충돌
allow: "Bash(*)"            # 모든 Bash 허용
deny:  "Bash(rm -rf:*)"     # rm -rf 차단
→ 결과: rm -rf는 차단 (deny가 더 구체적이고 deny 우선)

# 예시 2: 두 allow 충돌
allow: "Read(**)"           # 모두 허용
allow: "Read(src/**)"       # src만 명시
→ 결과: 둘 다 적용 (allow끼리는 더 관대한 쪽 적용)

# 예시 3: allow와 ask 충돌
allow: "Edit(docs/**)"       # docs는 자동
ask:   "Edit(**)"            # 일반 Edit은 확인
→ 결과: docs는 자동, 다른 경로는 ask

# 일반 규칙 (3가지)
1. deny > ask > allow (deny가 최우선)
2. 더 구체적인 패턴 > 일반 패턴
3. 더 상위 계층 > 하위 계층 (managed > project > user)

# 디버깅: /permissions 명령으로 어느 규칙이 적용되었는지 확인
```

## Speaker Notes

두 패턴이 모두 매칭될 때 어느 것이 이기는지 살펴봅니다.
예시 1은 allow와 deny 충돌입니다.
allow Bash 별로 모든 Bash 허용하고 deny Bash rm -rf 콜론 별로 rm 차단합니다.
결과적으로 rm -rf는 차단됩니다.
deny가 더 구체적이고 deny가 항상 우선이기 때문입니다.
예시 2는 두 allow 충돌입니다.
Read 별별로 모두 허용하고 Read src 별별로 src만 명시합니다.
결과적으로 둘 다 적용됩니다.
allow끼리는 더 관대한 쪽이 적용됩니다.
예시 3은 allow와 ask 충돌입니다.
Edit docs 별별은 자동 허용, Edit 별별은 ask 확인입니다.
결과적으로 docs는 자동, 다른 경로는 ask가 적용됩니다.
구체적인 패턴이 더 우선됩니다.
일반 규칙 3가지를 기억하세요.
deny 최우선, 구체 우선, 상위 계층 우선입니다.
디버깅은 /permissions 명령을 사용합니다.
