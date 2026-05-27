# Claude Code Deep Dive Workshop - Code Samples

3일간의 Claude Code 워크샵에서 사용된 **코드 블록과 발표자 노트**를 챕터/파트별로 정리한 자료입니다. 코드가 포함된 슬라이드만 추출되어, 실제로 활용 가능한 코드 스니펫에 빠르게 접근할 수 있습니다.

## 파일 명명 규칙

각 슬라이드 마크다운 파일은 **슬라이드 번호 + 의미 있는 제목 슬러그** 형식입니다:

```
007-python-install-first-call.md        # Slide 7: Python 설치와 첫 호출
044-tool-cycle-implementation.md         # Slide 44: 호출 사이클 구현
082-mcp-servers-parameter.md             # Slide 82: mcp_servers 매개변수
103-error-classify.md                    # Slide 103: 에러 분류와 대응
104-retry-python.md                      # Slide 104: Retry / Python
```

번호로 정렬 순서를 유지하면서 제목으로 내용을 즉시 파악할 수 있습니다.

## 통계

| Chapter | 전체 슬라이드 | 코드 슬라이드 | 코드 블록 | 폴더 |
|---------|---------------|---------------|-----------|------|
| Ch.1 Overview          | 200 | 108 | 108 | [ch1-overview](./ch1-overview/) |
| Ch.2 Agents & Subagents | 110 |  53 |  53 | [ch2-agents](./ch2-agents/) |
| Ch.3 Admin Setup       | 120 |  57 |  57 | [ch3-admin](./ch3-admin/) |
| Ch.4 Settings          | 140 |  86 |  86 | [ch4-settings](./ch4-settings/) |
| Ch.5 CLI Reference     | 130 |  86 |  86 | [ch5-cli](./ch5-cli/) |
| Ch.6 Agent SDK         | 150 | 112 | 112 | [ch6-sdk](./ch6-sdk/) |
| **합계**                | **850** | **502** | **502** | |

## 폴더 구조

```
workshop-code/
├── README.md
├── ch1-overview/
│   ├── README.md
│   ├── part-01-what-is-claude-code/
│   │   ├── README.md
│   │   ├── 009-claude-code-install.md
│   │   └── ...
│   └── ...
├── ch6-sdk/
│   ├── part-01-sdk-basics/
│   │   ├── 007-python-install-first-call.md
│   │   ├── 008-typescript-install-first-call.md
│   │   └── ...
│   ├── part-06-production/
│   │   ├── 103-error-classify.md
│   │   ├── 104-retry-python.md
│   │   └── ...
│   └── ...
```

각 슬라이드 마크다운에는 다음이 포함됩니다:

- 슬라이드 번호와 원본 한국어 제목
- 소속 파트 정보
- 모든 코드 블록 (Python/TypeScript/bash/JSON/YAML 등 언어 자동 감지)
- 발표자 노트 (한국어 단문)

## 활용 방법

### 1. GitHub에서 직접 탐색
GitHub에 푸시하면 마크다운이 자동 렌더링되어 코드 하이라이팅과 함께 표시됩니다.
파일명만 봐도 어떤 내용인지 알 수 있어 탐색이 효율적입니다.

### 2. 파일명으로 검색
```bash
# Python retry 패턴 찾기
ls workshop-code/ch6-sdk/part-06-production/ | grep retry

# 인증 관련 파일 찾기
find workshop-code/ -name "*auth*"

# Hooks 예시 파일 찾기
find workshop-code/ -name "*hook*"
```

### 3. 내용 검색
```bash
grep -rn "tenacity" workshop-code/
grep -rn "PreToolUse" workshop-code/
grep -rn "mcp_servers" workshop-code/
```

## 라이선스

발표자: Choi WooHyung (Prin. Solutions Architect, AWS Korea)
연락: whchoi@amazon.com / https://linkedin.com/in/woohyungchoi
