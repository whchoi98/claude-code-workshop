# Slide 119: 배포 전략

**Part 6: PRODUCTION 운영**

## Code Blocks

### deployment

```python
# 1. Canary Deployment (K8s + Istio)
# apiVersion: networking.istio.io/v1
# kind: VirtualService
# spec:
#   http:
#     - route:
#         - destination: {host: claude-app, subset: v1}
#           weight: 95
#         - destination: {host: claude-app, subset: v2}
#           weight: 5

# 2. Feature Flag로 새 모델 점진 도입
import ldclient
ldclient.set_config({"sdk_key": "..."})
flag_client = ldclient.get()

def get_model_for_user(user_id):
    user = {"key": user_id}
    if flag_client.variation("use-opus", user, default=False):
        return "claude-opus-4-5"
    return "claude-sonnet-4-5"

# 사용
model = get_model_for_user(user_id)
response = client.messages.create(model=model, ...)

# 3. A/B 테스트 (모델 비교)
def ab_test_call(user_id, prompt):
    bucket = hash(user_id) % 100
    if bucket < 50:
        model = "claude-sonnet-4-5"
        bucket_name = "control"
    else:
        model = "claude-opus-4-5"
        bucket_name = "experiment"

    response = client.messages.create(model=model, ...)
    record_ab_metric(user_id, bucket_name,
                     duration=response.duration_ms,
                     cost=calculate_cost(response))

# 4. Rollback Plan
# - kubectl rollout undo deployment/claude-app
# - Feature flag로 즉시 0%
# - DB schema는 backward compatible
# - 이전 deployment 즉시 복구 가능

# 5. 배포 후 모니터링 (1시간 집중)
# 추적 메트릭:
# - 에러율 변화 (배포 전후 비교)
# - p95 응답 시간 변화
# - 비용 변화 (시간당)
# - 사용자 피드백 (Slack)
# - 예외 발생 패턴

# 6. 점진 확대 시나리오
# Day 1: 5% canary
# Day 2: 25%로 확대 (메트릭 OK 시)
# Day 3-4: 50%
# Day 5+: 100%
# 문제 시: 즉시 rollback
```

## Speaker Notes

배포 전략의 4가지 핵심 패턴입니다.
Canary Deployment 패턴입니다.
5 퍼센트 traffic만 새 버전으로 라우팅하고 메트릭이 좋으면 25 퍼센트, 100 퍼센트로 점진 확대합니다.
문제 발생 시 즉시 rollback합니다.
K8s + Istio의 VirtualService 예시에서 weight 95와 5로 트래픽 비율을 명시합니다.
Feature Flag로 새 모델 점진 도입을 합니다.
LaunchDarkly 같은 도구를 사용해 코드 배포 없이 사용자 비율을 조정합니다.
get_model_for_user 함수에서 flag variation으로 use-opus를 확인하고 결과에 따라 모델을 선택합니다.
10 퍼센트 사용자부터 시작해 점진 확대하고 문제 시 즉시 0 퍼센트로 변경 가능합니다.
A/B 테스트는 두 모델을 동시 운영해 비교합니다.
user_id의 hash로 50/50 분할하고 control과 experiment 그룹으로 분류합니다.
각 그룹의 응답 시간, 비용, 사용자 만족도를 기록해 비교 분석합니다.
Rollback Plan을 준비합니다.
kubectl rollout undo로 이전 버전으로 즉시 복구하거나 Feature flag로 0 퍼센트 전환합니다.
DB schema는 backward compatible하게 유지합니다.
배포 후 모니터링을 1시간 동안 집중 수행합니다.
에러율, 응답 시간, 비용, 사용자 피드백, 예외 패턴 모두 추적합니다.
