# Slide 11: Windows MSI deployment

**Part 1: DEPLOYMENT STRATEGY**

## Code Blocks

### GPO / Intune

```bash
# 1. MSI 다운로드 및 검증
$ Invoke-WebRequest \
    -Uri https://claude.ai/download/windows.msi \
    -OutFile \\fileserver\Software\ClaudeCode\claude.msi
$ Get-FileHash claude.msi  # SHA256 확인

# 2. GPO 생성 (Group Policy Management Console)
# Computer Configuration → Policies → Software Settings
#   → Software Installation → New → Package
#     UNC path: \\fileserver\Software\ClaudeCode\claude.msi
#     Deployment: Assigned

# 3. 또는 Intune (modern, 클라우드 기반)
# Apps → Add → Windows app (Win32)
# .intunewin 패키지 생성 후 업로드
# Assignment: Required for 그룹

# 4. 사용자 PC 부팅 시 자동 설치
# 사용자 작업 없이 백그라운드 진행

# 5. 사일런트 옵션 (수동 설치 시)
$ msiexec /i claude.msi /quiet /norestart
```

## Speaker Notes

Windows 환경에서의 MSI 대량 배포입니다.
도메인 환경의 일괄 설치를 살펴봅니다.
1단계 MSI를 다운로드하고 SHA256 해시로 무결성을 검증합니다.
사내 파일 서버의 공유 경로에 배치합니다.
2단계 GPO를 생성합니다.
Group Policy Management Console에서 Computer Configuration의 Software Settings를 통해 패키지를 등록합니다.
Deployment를 Assigned로 설정하면 부팅 시 자동 설치됩니다.
3단계 또는 더 현대적인 Intune을 사용할 수 있습니다.
Windows app으로 등록하고 .intunewin 패키지로 변환 후 업로드합니다.
Required 어사인먼트로 강제 설치됩니다.
4단계 사용자 PC 부팅 시 자동 설치되며 사용자 작업이 필요 없습니다.
5단계 수동 설치 시에는 msiexec 명령에 /quiet와 /norestart 옵션을 줍니다.
