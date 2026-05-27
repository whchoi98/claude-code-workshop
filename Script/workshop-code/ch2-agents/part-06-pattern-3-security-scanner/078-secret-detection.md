# Slide 78: Secret detection

**Part 6: PATTERN 3 / SECURITY SCANNER**

## Code Blocks

### secret patterns

```bash
# 에이전트가 검색하는 시크릿 패턴

# AWS
AKIA[0-9A-Z]{16}                    # Access Key
aws_secret_access_key\s*=\s*['"]    # Secret Key

# Google Cloud
AIza[0-9A-Za-z\-_]{35}              # API Key
service_account[\s\S]*?private_key  # JSON SA

# GitHub
ghp_[0-9a-zA-Z]{36}                  # Personal Token
gho_[0-9a-zA-Z]{36}                  # OAuth Token

# Generic
api[-_]?key\s*=\s*['"][^'"]{20,}    # 일반 API key
password\s*=\s*['"][^'"]+['"]       # password

# 추가 점검
- .env 파일 git 추적 여부
- 과거 커밋의 시크릿 (git log -p)
- .gitignore 누락 위험
```

## Speaker Notes

시크릿 탐지 능력을 자세히 살펴봅니다.
에이전트가 검색하는 시크릿 패턴이 광범위합니다.
AWS는 AKIA로 시작하는 16자 Access Key와 secret access key 패턴을 검색합니다.
Google Cloud는 AIza로 시작하는 35자 API Key와 service account private key를 검색합니다.
GitHub는 ghp underscore로 시작하는 Personal Token과 gho underscore OAuth Token을 검색합니다.
범용 패턴도 검사합니다.
api key 변수에 20자 이상의 값이 들어있는 경우, password 변수에 값이 들어있는 경우 등입니다.
추가 점검 사항도 있습니다.
.env 파일이 실수로 git에 추적되고 있는지 확인합니다.
과거 커밋의 시크릿도 점검합니다.
git log -p로 이력을 검색해 이미 커밋된 시크릿을 발견합니다.
.gitignore 누락 위험도 함께 보고합니다.
