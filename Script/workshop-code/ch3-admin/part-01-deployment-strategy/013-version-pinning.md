# Slide 13: Version pinning

**Part 1: DEPLOYMENT STRATEGY**

## Code Blocks

### Version Control

```bash
# 1. npm 설치 시 특정 버전 고정
$ npm install -g @anthropic-ai/claude-code@1.5.0

# 2. 자동 업데이트 체크 비활성화 (모든 사용자)
# 사내 표준 환경변수로 강제
$ export CLAUDE_DISABLE_UPDATE_CHECK=1

# 3. managed-settings.json (관리자만 수정 가능)
{
  "updateChecker": {
    "enabled": false,
    "notifyOnUpdate": false
  },
  "fixedVersion": "1.5.0"
}

# 4. 새 버전 검증 후 일괄 롤아웃 (Ansible 예시)
- name: Update Claude Code to 1.6.0
  hosts: developers
  tasks:
    - name: Install new version
      npm:
        name: '@anthropic-ai/claude-code'
        version: '1.6.0'
        global: yes

# 5. 검증 절차: dev → staging → production 그룹별 단계 배포
```

## Speaker Notes

버전 고정과 통제 방법입니다.
자동 업데이트를 차단하고 검증된 버전만 사용하는 패턴입니다.
1단계 npm 설치 시 특정 버전을 명시합니다.
@1.5.0 같은 형태로 정확히 지정합니다.
2단계 자동 업데이트 체크를 비활성화합니다.
CLAUDE_DISABLE_UPDATE_CHECK 환경변수를 1로 설정합니다.
3단계 managed-settings.json으로 강제합니다.
관리자만 수정할 수 있는 이 설정 파일에 updateChecker를 비활성화하고 fixedVersion을 명시합니다.
4단계 새 버전이 검증되면 Ansible로 일괄 롤아웃합니다.
npm 모듈로 글로벌 설치를 자동화합니다.
5단계 검증 절차는 dev, staging, production 그룹별 단계 배포로 진행합니다.
문제 발견 시 빠르게 롤백할 수 있도록 단계를 명확히 합니다.
