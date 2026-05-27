# Slide 59: Jenkins / Jenkinsfile 기본

**Part 4: CI/CD 통합**

## Code Blocks

### Jenkinsfile

```python
// Jenkinsfile
pipeline {
    agent {
        docker {
            image 'node:20-alpine'
            args '-v /var/lib/jenkins/.npm:/root/.npm'
        }
    }

    environment {
        ANTHROPIC_API_KEY = credentials('anthropic-api-key')
        CLAUDE_MAX_TURNS = '15'
    }

    options {
        timeout(time: 10, unit: 'MINUTES')
        ansiColor('xterm')
    }

    stages {
        stage('Setup') {
            steps {
                sh 'npm install -g @anthropic-ai/claude-code'
                sh 'claude --version'
            }
        }

        stage('Review') {
            when {
                anyOf {
                    branch 'main'
                    changeRequest()
                }
            }
            steps {
                script {
                    def review = sh(
                        script: '''
                            claude -p "PR 변경 사항 리뷰" \
                              --max-turns $CLAUDE_MAX_TURNS \
                              --output-format json | jq -r '.result'
                        ''',
                        returnStdout: true
                    ).trim()
                    writeFile file: 'review.md', text: review
                }
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'review.md',
                                 fingerprint: true
            }
        }
    }

    post {
        success { echo '✓ Review completed' }
        failure { echo '✗ Review failed' }
        always { cleanWs() }
    }
}
```

## Speaker Notes

Jenkins Jenkinsfile 기본 구조입니다.
Declarative Pipeline 문법을 사용합니다.
agent 블록에 docker로 node:20-alpine 이미지를 명시합니다.
args로 npm 캐시를 호스트와 공유해 빌드 속도를 높입니다.
environment에 credentials 함수로 시크릿을 안전하게 주입합니다.
anthropic-api-key는 Jenkins Credentials 매니저에 등록된 ID입니다.
options로 timeout 10분과 컬러 출력을 활성화합니다.
stages 안에 Setup, Review, Archive 3단계가 있습니다.
Setup에서 claude-code를 설치하고 버전을 확인합니다.
Review는 when 블록으로 main 브랜치이거나 PR일 때만 실행됩니다.
sh의 returnStdout true로 결과를 변수에 받고 writeFile로 파일에 저장합니다.
Archive에서 archiveArtifacts로 결과를 Jenkins에 보존합니다.
post 블록은 stage 후 항상 실행되는 후처리입니다.
success, failure, always 조건에 따라 다른 동작을 정의할 수 있습니다.
