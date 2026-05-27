# Slide 37: Proxy basics

**Part 3: NETWORK & SECURITY**

## Code Blocks

### Proxy env

```bash
# 1. 환경변수 표준 (모든 사내 PC 공통)
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080
export NO_PROXY=localhost,127.0.0.1,.company.com,169.254.169.254

# 2. Windows (관리자 PowerShell)
[Environment]::SetEnvironmentVariable(
  'HTTPS_PROXY', 'http://proxy.company.com:8080', 'Machine')

# 3. GPO로 일괄 배포 (Windows)
# Computer Configuration → Preferences →
#   Windows Settings → Environment

# 4. Claude Code의 자동 인식
# Node.js 표준 환경변수를 그대로 사용
# 별도 Claude Code 설정 불필요

# 5. 검증
$ claude doctor
  Network:
    api.anthropic.com via proxy.company.com:8080  ✓ (250 ms)
    Outbound HTTPS allowed                         ✓
    Proxy: http://proxy.company.com:8080           ✓
```

## Speaker Notes

사내 프록시 통과 설정입니다.
환경변수 표준을 모든 사내 PC에 공통으로 적용합니다.
1단계 환경변수를 설정합니다.
HTTP_PROXY와 HTTPS_PROXY를 사내 프록시 주소로 지정합니다.
NO_PROXY로 예외 도메인을 명시합니다.
localhost, 사내 도메인, 그리고 AWS 메타데이터 IP 169.254.169.254를 반드시 포함합니다.
2단계 Windows는 관리자 PowerShell에서 Machine 스코프로 설정합니다.
3단계 GPO로 일괄 배포할 수 있습니다.
Computer Configuration의 Preferences에서 Environment를 설정합니다.
4단계 Claude Code는 Node.js 표준 환경변수를 그대로 사용하므로 별도 설정이 불필요합니다.
5단계 claude doctor로 검증합니다.
Network 섹션에서 api.anthropic.com이 프록시를 통해 정상 도달하는지 확인합니다.
