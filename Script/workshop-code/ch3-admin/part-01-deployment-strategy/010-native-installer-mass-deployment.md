# Slide 10: Native installer mass deployment

**Part 1: DEPLOYMENT STRATEGY**

## Code Blocks

### Mass deploy

```bash
# macOS - MDM (Jamf Pro 등)
1. claude-code.pkg 다운로드
2. Jamf Pro에 패키지 업로드
3. 정책 생성: 그룹 대상, 사일런트 설치
4. self-service에도 게시

# Linux - Ansible playbook
# install_claude.yml
- hosts: developers
  become: yes
  tasks:
    - name: Download installer
      get_url:
        url: https://claude.ai/install.sh
        dest: /tmp/claude_install.sh
        mode: '0755'
    - name: Run installer
      shell: /tmp/claude_install.sh
      environment:
        CLAUDE_INSTALL_PATH: /opt/claude

    - name: Verify
      command: claude --version

# Ansible 실행
$ ansible-playbook -i hosts install_claude.yml
```

## Speaker Notes

Native Installer를 대량 배포하는 방법입니다.
macOS는 Jamf Pro 같은 MDM 도구를 사용합니다.
1단계 claude-code.pkg 파일을 다운로드합니다.
2단계 Jamf Pro에 패키지를 업로드합니다.
3단계 정책을 생성해 대상 그룹과 사일런트 설치를 지정합니다.
4단계 self-service 카탈로그에도 게시해 사용자가 필요할 때 직접 설치할 수 있게 합니다.
Linux는 Ansible playbook으로 처리합니다.
developers 호스트 그룹을 대상으로 합니다.
get_url 태스크로 install.sh를 다운로드합니다.
shell 태스크로 설치를 실행합니다.
환경변수로 설치 경로를 통제할 수 있습니다.
verify 태스크로 설치 결과를 확인합니다.
ansible-playbook 명령으로 일괄 실행하면 수백 대 서버에 일관되게 배포됩니다.
