# Slide 30: Sensitive data protection

**Part 2: PERMISSIONS 심화**

## Code Blocks

### sensitive deny

```bash
# 반드시 deny에 포함해야 할 패턴들

# 1. 자격증명 파일
"Read(**/.env*)",
"Read(**/.env.local)",
"Read(**/credentials)",
"Read(**/.aws/credentials)",
"Read(**/.aws/config)",

# 2. SSH와 GPG 키
"Read(**/.ssh/**)",
"Read(**/id_rsa)", "Read(**/id_ed25519)",
"Read(**/.gnupg/**)",

# 3. 클라우드 자격증명
"Read(**/.kube/config)",
"Read(**/gcloud/**)",

# 4. 사내 시크릿
"Read(**/secrets/**)",
"Read(**/secret*)",
"Read(**/private_key*)",
"Read(**/*.pem)", "Read(**/*.key)",

# 5. 위험 시스템 경로
"Read(/etc/shadow)",
"Read(/etc/sudoers)",
"Read(/proc/**)",
"Edit(/etc/**)",

# 6. 데이터베이스 덤프
"Read(**/*.sql.gz)",
"Read(**/backup/**)"
```

## Speaker Notes

민감 데이터 보호를 위해 반드시 deny에 포함해야 할 패턴들입니다.
첫째, 자격증명 파일입니다.
.env, .env.local, credentials, .aws의 credentials와 config 파일을 차단합니다.
둘째, SSH와 GPG 키입니다.
.ssh 디렉토리 전체, id_rsa, id_ed25519, .gnupg 디렉토리를 차단합니다.
셋째, 클라우드 자격증명입니다.
.kube의 config, gcloud 디렉토리를 차단합니다.
넷째, 사내 시크릿입니다.
secrets 디렉토리 전체, private_key 파일, .pem과 .key 파일을 차단합니다.
다섯째, 위험 시스템 경로입니다.
/etc/shadow, /etc/sudoers, /proc 디렉토리 읽기와 /etc 디렉토리 쓰기를 차단합니다.
여섯째, 데이터베이스 덤프와 백업 파일입니다.
이 패턴들을 managed-settings에 명시하면 조직 전체가 보호됩니다.
