# Slide 61: Jenkins / Credentials

**Part 4: CI/CD 통합**

## Code Blocks

### credentials

```
// 1. Jenkins UI에서 credentials 등록
// Manage Jenkins → Credentials → System → Global credentials
// Kind: Secret text
// ID: anthropic-api-key
// Secret: sk-ant-api03-...

// 2. environment 블록으로 주입
pipeline {
    environment {
        // Secret text 타입
        ANTHROPIC_API_KEY = credentials('anthropic-api-key')

        // Username/Password 타입 (자동 분할)
        // DB_CREDENTIALS_USR, DB_CREDENTIALS_PSW 자동 생성
        DB_CREDENTIALS = credentials('db-prod')

        // File 타입
        AWS_CONFIG = credentials('aws-config-file')
    }
}

// 3. withCredentials로 스코프 한정
pipeline {
    stages {
        stage('Sensitive') {
            steps {
                withCredentials([
                    string(credentialsId: 'anthropic-api-key',
                           variable: 'ANTHROPIC_API_KEY')
                ]) {
                    sh '''
                        claude -p "..." --output-format json
                    '''
                }
                // 블록 밖에서는 ANTHROPIC_API_KEY 노출 안 됨
            }
        }
    }
}

// 4. AWS Bedrock 사용 시 (IAM Role)
pipeline {
    environment {
        CLAUDE_CODE_USE_BEDROCK = '1'
        AWS_REGION = 'us-east-1'
    }
    options {
        // EC2 instance role 자동 사용 또는
        // AWS Credentials 플러그인
        withAWS(role: 'arn:aws:iam::123:role/jenkins-claude') { ... }
    }
}
```

## Speaker Notes

Jenkins Credentials로 시크릿을 안전하게 관리합니다.
1번 Jenkins UI에서 credentials를 등록합니다.
Manage Jenkins의 Credentials 메뉴에서 Secret text 타입으로 추가합니다.
ID는 anthropic-api-key처럼 의미있는 이름으로 명시합니다.
2번 environment 블록으로 주입합니다.
credentials 함수에 ID를 전달하면 해당 시크릿을 환경변수로 사용 가능합니다.
Username과 Password 타입은 USR과 PSW 접미사로 자동 분할됩니다.
File 타입은 임시 파일 경로를 받아 파일로 사용 가능합니다.
3번 withCredentials는 스코프를 한정합니다.
특정 stage나 step 안에서만 환경변수가 노출됩니다.
블록 밖에서는 보이지 않으므로 시크릿 노출 범위를 최소화할 수 있습니다.
4번 AWS Bedrock 사용 시 IAM Role 패턴이 권장됩니다.
CLAUDE_CODE_USE_BEDROCK을 1로 설정하고 AWS Credentials 플러그인의 withAWS로 role을 assume 합니다.
API key를 저장할 필요가 없어 보안이 강화됩니다.
