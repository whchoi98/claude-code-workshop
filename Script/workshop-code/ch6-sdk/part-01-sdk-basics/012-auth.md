# Slide 12: 인증 옵션

**Part 1: SDK 기본**

## Code Blocks

### 3 paths

```python
# 1. Anthropic Direct (기본)
from anthropic import Anthropic
client = Anthropic()    # ANTHROPIC_API_KEY 환경변수 자동

# TypeScript
import Anthropic from "@anthropic-ai/sdk";
const client = new Anthropic();

# 2. AWS Bedrock 경로
# Python
from anthropic import AnthropicBedrock
client = AnthropicBedrock(
    aws_region="us-east-1",
    # AWS 자격증명은 boto3 chain 자동 사용
    # 환경변수, ~/.aws/credentials, EC2 role 등
)
# 또는 명시
client = AnthropicBedrock(
    aws_access_key="AKIA...",
    aws_secret_key="...",
    aws_session_token="...",  # 임시 자격증명
    aws_region="us-east-1",
)

# TypeScript
import AnthropicBedrock from "@anthropic-ai/bedrock-sdk";
const client = new AnthropicBedrock({
  awsRegion: "us-east-1",
});

# 3. GCP Vertex AI 경로
# Python
from anthropic import AnthropicVertex
client = AnthropicVertex(
    project_id="my-gcp-project",
    region="us-central1",
)

# TypeScript
import AnthropicVertex from "@anthropic-ai/vertex-sdk";
const client = new AnthropicVertex({
  projectId: "my-gcp-project",
  region: "us-central1",
});

# 4. 모든 클라이언트가 동일한 messages API 제공
# 코드의 99%가 동일하게 동작
message = client.messages.create(
    model="...",    # 모델 ID만 경로별로 다름
    ...
)

# 5. 환경변수만으로 경로 전환
# ANTHROPIC_API_KEY      → Direct
# CLAUDE_CODE_USE_BEDROCK=1 + AWS_REGION → Bedrock
```

## Speaker Notes

인증 옵션 3가지 경로별 클라이언트입니다.
1번 Anthropic Direct가 가장 기본입니다.
from anthropic import Anthropic으로 import하고 인스턴스를 만듭니다.
ANTHROPIC_API_KEY 환경변수가 자동 사용됩니다.
TypeScript도 동일한 패턴입니다.
2번 AWS Bedrock 경로는 AnthropicBedrock 클라이언트를 사용합니다.
aws_region을 명시하고 AWS 자격증명은 boto3 chain이 자동 사용합니다.
환경변수, AWS credentials 파일, EC2 role 등에서 자동 로드됩니다.
또는 access_key, secret_key, session_token을 명시적으로 전달할 수도 있습니다.
TypeScript는 별도 패키지 @anthropic-ai/bedrock-sdk를 사용합니다.
3번 GCP Vertex AI 경로는 AnthropicVertex 클라이언트입니다.
project_id와 region을 명시합니다.
GOOGLE_APPLICATION_CREDENTIALS 환경변수로 service account 인증이 자동 처리됩니다.
4번 모든 클라이언트가 동일한 messages API를 제공합니다.
코드의 99 퍼센트가 동일하게 동작하고 모델 ID만 경로별로 다릅니다.
경로 전환이 매우 쉽습니다.
5번 환경변수만으로 경로 전환도 가능합니다.
