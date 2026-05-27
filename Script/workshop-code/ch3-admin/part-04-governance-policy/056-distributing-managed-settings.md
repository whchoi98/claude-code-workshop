# Slide 56: Distributing managed-settings

**Part 4: GOVERNANCE & POLICY**

## Code Blocks

### Distribution

```bash
# 1. Windows GPO (도메인 환경)
# Group Policy Editor:
# Computer Configuration → Preferences →
#   Windows Settings → Files
# Source: \\fileserver\Configs\managed-settings-L2.json
# Destination: C:\ProgramData\Claude\managed-settings.json
# Action: Replace
# Targeting: 개발팀 그룹

# 2. macOS Jamf Configuration Profile
# Custom Settings Payload
# Preference Domain: com.anthropic.claude
# Property List: managed-settings.json 내용

# 3. Linux Ansible
- name: Deploy managed-settings
  hosts: developers
  become: yes
  tasks:
    - name: Copy config
      copy:
        src: managed-settings-L2.json
        dest: /etc/claude/managed-settings.json
        owner: root
        mode: '0644'
    - name: Verify
      command: claude doctor

# 4. 그룹별 다른 파일 배포 가능
# L1: managed-settings-readonly.json
# L2: managed-settings-standard.json
# L3: managed-settings-developer.json
```

## Speaker Notes

managed-settings를 사내 PC에 배포하는 방법입니다.
Windows GPO 도메인 환경은 Group Policy Editor에서 Computer Configuration의 Preferences Windows Settings Files를 사용합니다.
Source는 파일서버 공유 경로의 managed-settings 파일이고 Destination은 PC의 ProgramData Claude 디렉토리입니다.
Action을 Replace로 설정하고 Targeting으로 개발팀 그룹을 지정합니다.
macOS는 Jamf Configuration Profile의 Custom Settings Payload를 사용합니다.
Preference Domain을 com.anthropic.claude로 설정하고 Property List에 managed-settings 내용을 넣습니다.
Linux는 Ansible playbook으로 처리합니다.
developers 그룹에 copy 태스크로 파일을 배포하고 root 소유로 mode 0644로 설정합니다.
command 태스크로 doctor를 실행해 적용을 검증합니다.
그룹별 다른 파일을 배포할 수 있습니다.
L1은 readonly, L2는 standard, L3는 developer로 차등 적용합니다.
