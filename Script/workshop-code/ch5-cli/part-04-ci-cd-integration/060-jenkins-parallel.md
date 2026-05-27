# Slide 60: Jenkins / Parallel

**Part 4: CI/CD 통합**

## Code Blocks

### parallel

```
// 병렬 분석 패턴
pipeline {
    agent any
    environment {
        ANTHROPIC_API_KEY = credentials('anthropic-api-key')
    }
    stages {
        stage('Setup') {
            steps {
                sh 'npm install -g @anthropic-ai/claude-code'
            }
        }

        stage('Parallel Analysis') {
            parallel {
                stage('Security') {
                    steps {
                        sh '''
                            claude -p "보안 관점 코드 분석" \
                              --allowed-tools "Read,Grep,Glob" \
                              --output-format json \
                              > security.json
                        '''
                    }
                }
                stage('Performance') {
                    steps {
                        sh '''
                            claude -p "성능 관점 분석" \
                              --output-format json \
                              > performance.json
                        '''
                    }
                }
                stage('Documentation') {
                    steps {
                        sh '''
                            claude -p "문서화 검토" \
                              --output-format json \
                              > docs.json
                        '''
                    }
                }
            }
        }

        stage('Aggregate') {
            steps {
                sh '''
                    jq -s '...' security.json performance.json \
                       docs.json > final-report.json
                '''
                archiveArtifacts artifacts: 'final-report.json'
            }
        }
    }
}
```

## Speaker Notes

Jenkins 병렬 실행 패턴입니다.
stage 안에 parallel 블록을 두면 그 안의 stage들이 동시 실행됩니다.
Setup에서 claude-code 설치 후 Parallel Analysis stage가 실행됩니다.
Security, Performance, Documentation 세 stage가 동시에 실행됩니다.
각 stage는 다른 관점의 분석을 수행하고 결과를 별도 JSON 파일에 저장합니다.
Security는 Read, Grep, Glob 도구만 허용해 안전합니다.
각 분석이 독립적이므로 한 stage가 실패해도 나머지는 계속됩니다.
모든 병렬 stage 완료 후 Aggregate stage가 시작됩니다.
jq -s로 3개 JSON을 합쳐 통합 보고서 final-report.json을 생성합니다.
archiveArtifacts로 Jenkins에 보존하면 다운로드 가능합니다.
총 실행 시간이 3개 순차 실행 대비 약 1/3로 단축됩니다.
