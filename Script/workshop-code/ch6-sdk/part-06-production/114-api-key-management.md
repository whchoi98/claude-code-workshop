# Slide 114: API key 관리

**Part 6: PRODUCTION 운영**

## Code Blocks

### API key

```python
# 절대 금지: 평문 하드코딩, .env 커밋, 로그 출력, 메신저 공유

# 1. AWS Secrets Manager (권장)
import boto3, json
from functools import lru_cache

@lru_cache(maxsize=1)
def get_anthropic_key():
    sm = boto3.client("secretsmanager")
    response = sm.get_secret_value(SecretId="prod/anthropic/api-key")
    return json.loads(response["SecretString"])["api_key"]

import anthropic
client = anthropic.Anthropic(api_key=get_anthropic_key())

# 2. HashiCorp Vault
import hvac
def get_from_vault(path):
    vault = hvac.Client(url="https://vault.company.com")
    vault.token = os.getenv("VAULT_TOKEN")
    response = vault.secrets.kv.v2.read_secret_version(path=path)
    return response["data"]["data"]["api_key"]

# 3. Kubernetes Secret (secret.yaml)
# apiVersion: v1
# kind: Secret
# metadata: {name: anthropic-credentials}
# type: Opaque
# data:
#   api-key: <base64-encoded>

# Pod env
# env:
#   - name: ANTHROPIC_API_KEY
#     valueFrom:
#       secretKeyRef:
#         name: anthropic-credentials
#         key: api-key

# 4. 자동 회전 (90일 주기)
def rotate_anthropic_key():
    new_key = create_new_anthropic_key()   # 가상 (수동 발급 후 자동화)
    sm = boto3.client("secretsmanager")
    sm.update_secret(
        SecretId="prod/anthropic/api-key",
        SecretString=json.dumps({"api_key": new_key}),
    )
    invalidate_cache_for_all_services()
    schedule_old_key_revocation()  # 24시간 후

# 5. 서비스별 분리
# - 각 서비스가 별도 key 사용
# - metadata로 호출 추적
# - 노출 시 영향 범위 최소화

SERVICE_KEYS = {
    "api": "prod/anthropic/api-service",
    "batch": "prod/anthropic/batch-job",
    "research": "prod/anthropic/research",
}
```

## Speaker Notes

API key 보안 관리입니다.
절대 금지 사항이 있습니다.
평문 하드코딩, .env 파일을 git 커밋, 로그에 출력, Slack이나 이메일 공유는 절대 안 됩니다.
AWS Secrets Manager 사용 패턴이 권장됩니다.
boto3 secretsmanager client로 get_secret_value를 호출합니다.
lru_cache로 매 호출마다 Secrets Manager에 접근하지 않도록 캐싱합니다.
Anthropic 인스턴스 생성 시 api_key 인자로 전달합니다.
HashiCorp Vault도 유사한 패턴입니다.
hvac client로 KV v2 secret을 읽어옵니다.
Kubernetes Secret이 K8s 환경에서 표준입니다.
secret.yaml에 base64로 encoded api-key를 저장합니다.
Pod 정의에서 env의 valueFrom secretKeyRef로 환경변수로 주입합니다.
자동 회전은 90일 주기가 일반적입니다.
rotate_anthropic_key 함수에서 4단계로 진행합니다.
새 key 발급, Secrets Manager 업데이트, 모든 서비스의 캐시 무효화, 24시간 후 이전 key 무효화입니다.
서비스별 분리도 중요합니다.
각 서비스별 별도 key를 발급하면 노출 시 영향 범위를 최소화할 수 있습니다.
