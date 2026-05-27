# Slide 39: Internal CA cert

**Part 3: NETWORK & SECURITY**

## Code Blocks

### CA Certs

```bash
# 시나리오: 사내 프록시가 TLS를 가로채 사내 CA로 재서명

# 1. 사내 CA 인증서 파일 확보
# 보통 IT팀에서 제공 (company-ca.crt 또는 .pem)

# 2. Node.js 환경변수 설정
export NODE_EXTRA_CA_CERTS=/etc/ssl/company-ca.crt
# 또는 Windows
$env:NODE_EXTRA_CA_CERTS = "C:\Certs\company-ca.crt"

# 3. 시스템 trust store에도 추가 (옵션, 권장)
# macOS
$ sudo security add-trusted-cert -d -r trustRoot \
    -k /Library/Keychains/System.keychain company-ca.crt

# Linux (Ubuntu/Debian)
$ sudo cp company-ca.crt /usr/local/share/ca-certificates/
$ sudo update-ca-certificates

# Windows
certutil -addstore -f "ROOT" company-ca.crt

# 4. 검증
$ claude doctor
  TLS:
    Custom CA: /etc/ssl/company-ca.crt        ✓
    Verify peer: enabled                       ✓
    Handshake: TLS 1.3, ECDHE-ECDSA           ✓
```

## Speaker Notes

사내 CA 인증서 설정을 살펴봅니다.
사내 프록시가 TLS를 가로채 사내 CA로 재서명하는 환경에 대응합니다.
1단계 사내 CA 인증서 파일을 IT팀에서 받습니다.
company-ca.crt 또는 .pem 파일 형태입니다.
2단계 Node.js 환경변수를 설정합니다.
NODE_EXTRA_CA_CERTS에 인증서 경로를 지정합니다.
Windows는 PowerShell에서 $env로 설정합니다.
3단계 시스템 trust store에도 추가하는 것을 권장합니다.
macOS는 security 명령으로 System keychain에 추가합니다.
Linux는 인증서를 ca-certificates 디렉토리에 두고 update-ca-certificates를 실행합니다.
Windows는 certutil로 ROOT 저장소에 추가합니다.
4단계 claude doctor로 검증합니다.
TLS 섹션에서 Custom CA가 인식되고 peer verify가 enabled되며 handshake가 정상인지 확인합니다.
중요한 점은 절대 TLS 검증을 비활성화하지 말라는 것입니다.
인증서를 명시적으로 추가하는 방식을 사용합니다.
