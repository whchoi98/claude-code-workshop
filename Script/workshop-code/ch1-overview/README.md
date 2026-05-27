# Chapter 1: Overview

Claude Code 전반 이해

코드 블록 슬라이드: 108개

[← 워크샵 메인](../README.md)

## 파트 목록

## Part 1: WHAT IS CLAUDE CODE
Slides 9-30 (22 slides)

  - [Slide 21: Case 1 디버깅](./part-01-what-is-claude-code/021-case-1.md)
  - [Slide 22: Case 2 리팩토링](./part-01-what-is-claude-code/022-case-2.md)
  - [Slide 23: Case 3 신기능 개발](./part-01-what-is-claude-code/023-case-3.md)
  - [Slide 24: Case 4 코드베이스 학습](./part-01-what-is-claude-code/024-case-4-learning.md)
  - [Slide 25: Case 5 테스트 작성](./part-01-what-is-claude-code/025-case-5-test.md)

## Part 2: ARCHITECTURE
Slides 31-48 (18 slides)

  - [Slide 35: Client Layer - Agent SDK](./part-02-architecture/035-client-layer-agent-sdk.md)
  - [Slide 39: Tool System Overview](./part-02-architecture/039-tool-system-overview.md)
  - [Slide 42: Permission Model](./part-02-architecture/042-permission-model.md)

## Part 3: INSTALLATION
Slides 49-70 (22 slides)

  - [Slide 52: npm Install on macOS/Linux](./part-03-installation/052-npm-install-on-macos-linux.md)
  - [Slide 53: npm Install on Ubuntu/Debian](./part-03-installation/053-npm-install-on-ubuntu-debian.md)
  - [Slide 54: npm Install on RHEL/Fedora](./part-03-installation/054-npm-install-on-rhel-fedora.md)
  - [Slide 55: npm Install on Windows](./part-03-installation/055-npm-install-on-windows.md)
  - [Slide 56: Native Installer macOS](./part-03-installation/056-native-installer-macos.md)
  - [Slide 57: Native Installer Linux](./part-03-installation/057-native-installer-linux.md)
  - [Slide 58: Native Installer Windows](./part-03-installation/058-native-installer-windows.md)
  - [Slide 59: Node Manager nvm](./part-03-installation/059-node-manager-nvm.md)
  - [Slide 60: Node Manager fnm](./part-03-installation/060-node-manager-fnm.md)
  - [Slide 61: Node Manager Volta](./part-03-installation/061-node-manager-volta.md)
  - [Slide 62: Docker Container Setup](./part-03-installation/062-docker-container-setup.md)
  - [Slide 63: Docker Custom Image](./part-03-installation/063-docker-custom-image.md)
  - [Slide 64: WSL2 Setup](./part-03-installation/064-wsl2-setup.md)
  - [Slide 65: Devcontainer Setup](./part-03-installation/065-devcontainer-setup.md)
  - [Slide 66: Installation Verification](./part-03-installation/066-installation-verification.md)
  - [Slide 67: claude doctor](./part-03-installation/067-claude-doctor.md)
  - [Slide 68: Upgrade](./part-03-installation/068-upgrade.md)
  - [Slide 69: Uninstall](./part-03-installation/069-uninstall.md)

## Part 4: AUTHENTICATION
Slides 71-88 (18 slides)

  - [Slide 72: Auth Method 1: OAuth](./part-04-authentication/072-auth-method-1-oauth.md)
  - [Slide 74: OAuth: 사용량 모니터링](./part-04-authentication/074-oauth-use-monitoring.md)
  - [Slide 75: Auth Method 2: Anthropic API Key](./part-04-authentication/075-auth-method-2-anthropic-api-key.md)
  - [Slide 77: API Key 환경변수](./part-04-authentication/077-api-key-env.md)
  - [Slide 79: Auth Method 3: AWS Bedrock](./part-04-authentication/079-auth-method-3-aws-bedrock.md)
  - [Slide 82: Bedrock IAM Policy](./part-04-authentication/082-bedrock-iam-policy.md)
  - [Slide 84: Auth Method 4: Vertex AI](./part-04-authentication/084-auth-method-4-vertex-ai.md)
  - [Slide 85: Vertex GCP 설정](./part-04-authentication/085-vertex-gcp-config.md)
  - [Slide 86: Vertex 자격증명 (ADC)](./part-04-authentication/086-vertex-adc.md)
  - [Slide 88: /login /logout](./part-04-authentication/088-login-logout.md)

## Part 5: QUICK START
Slides 89-110 (22 slides)

  - [Slide 91: 대화형 REPL 입문](./part-05-quick-start/091-conversation-repl.md)
  - [Slide 95: /init 명령](./part-05-quick-start/095-init-command.md)
  - [Slide 96: /help 명령](./part-05-quick-start/096-help-command.md)
  - [Slide 97: /status 명령](./part-05-quick-start/097-status-command.md)
  - [Slide 98: /clear 명령](./part-05-quick-start/098-clear-command.md)
  - [Slide 99: 시나리오 1 디버깅 (문제 정의)](./part-05-quick-start/099-1-definition.md)
  - [Slide 100: 시나리오 1 디버깅 (작업 흐름)](./part-05-quick-start/100-1-task.md)
  - [Slide 101: 시나리오 1 디버깅 (도구 호출)](./part-05-quick-start/101-1-tool-call.md)
  - [Slide 102: 시나리오 2 기능 추가 (문제 정의)](./part-05-quick-start/102-2-definition.md)
  - [Slide 103: 시나리오 2 기능 추가 (Plan 모드)](./part-05-quick-start/103-2-plan.md)
  - [Slide 104: 시나리오 2 기능 추가 (실행)](./part-05-quick-start/104-execution.md)
  - [Slide 105: 시나리오 3 리팩토링](./part-05-quick-start/105-refactor.md)
  - [Slide 107: Plan 모드 활성화 상세](./part-05-quick-start/107-plan.md)
  - [Slide 108: 세션 관리 /resume](./part-05-quick-start/108-management-resume.md)
  - [Slide 109: 세션 관리 --continue](./part-05-quick-start/109-management-continue.md)

## Part 6: CORE CAPABILITIES
Slides 111-138 (28 slides)

  - [Slide 112: Read tool basics](./part-06-core-capabilities/112-read-tool-basics.md)
  - [Slide 113: Read multimodal](./part-06-core-capabilities/113-read-multimodal.md)
  - [Slide 114: Read line range](./part-06-core-capabilities/114-read-line-range.md)
  - [Slide 115: Edit Find Replace](./part-06-core-capabilities/115-edit-find-replace.md)
  - [Slide 116: Edit Multi-file](./part-06-core-capabilities/116-edit-multi-file.md)
  - [Slide 117: Write](./part-06-core-capabilities/117-write.md)
  - [Slide 118: NotebookEdit](./part-06-core-capabilities/118-notebookedit.md)
  - [Slide 119: Bash basics](./part-06-core-capabilities/119-bash-basics.md)
  - [Slide 120: Bash background](./part-06-core-capabilities/120-bash-background.md)
  - [Slide 122: Grep basics](./part-06-core-capabilities/122-grep-basics.md)
  - [Slide 123: Grep regex](./part-06-core-capabilities/123-grep-regex.md)
  - [Slide 124: Glob](./part-06-core-capabilities/124-glob.md)
  - [Slide 125: WebSearch](./part-06-core-capabilities/125-websearch.md)
  - [Slide 126: WebFetch](./part-06-core-capabilities/126-webfetch.md)
  - [Slide 128: Git workflow](./part-06-core-capabilities/128-git-workflow.md)
  - [Slide 129: Git commit message](./part-06-core-capabilities/129-git-commit-message.md)
  - [Slide 130: Git PR creation](./part-06-core-capabilities/130-git-pr-creation.md)
  - [Slide 133: allow/deny patterns](./part-06-core-capabilities/133-allow-deny-patterns.md)
  - [Slide 134: ask mode](./part-06-core-capabilities/134-ask-mode.md)
  - [Slide 135: Auto-accept mode](./part-06-core-capabilities/135-auto-accept-mode.md)
  - [Slide 136: Yolo mode](./part-06-core-capabilities/136-yolo-mode.md)

## Part 7: IDE INTEGRATION
Slides 139-152 (14 slides)

  - [Slide 140: VS Code install](./part-07-ide-integration/140-vs-code-install.md)
  - [Slide 142: VS Code commands](./part-07-ide-integration/142-vs-code-commands.md)
  - [Slide 143: VS Code selection context](./part-07-ide-integration/143-vs-code-selection-context.md)
  - [Slide 145: JetBrains install](./part-07-ide-integration/145-jetbrains-install.md)
  - [Slide 148: External editor Vim](./part-07-ide-integration/148-external-editor-vim.md)
  - [Slide 149: Emacs/Neovim](./part-07-ide-integration/149-emacs-neovim.md)

## Part 8: CLAUDE.md & MEMORY
Slides 153-168 (16 slides)

  - [Slide 154: Memory Hierarchy](./part-08-claudemd-memory/154-memory-hierarchy.md)
  - [Slide 155: Project Memory](./part-08-claudemd-memory/155-project-memory.md)
  - [Slide 156: User Memory](./part-08-claudemd-memory/156-user-memory.md)
  - [Slide 157: Local Memory](./part-08-claudemd-memory/157-local-memory.md)
  - [Slide 158: Enterprise Memory](./part-08-claudemd-memory/158-enterprise-memory.md)
  - [Slide 159: /init Command](./part-08-claudemd-memory/159-init-command.md)
  - [Slide 160: /memory Edit Command](./part-08-claudemd-memory/160-memory-edit-command.md)
  - [Slide 161: # Quick Add Shorthand](./part-08-claudemd-memory/161-quick-add-shorthand.md)
  - [Slide 162: Import Syntax](./part-08-claudemd-memory/162-import-syntax.md)
  - [Slide 163: Nested Import Priority](./part-08-claudemd-memory/163-nested-import-priority.md)
  - [Slide 167: Example - Python Project](./part-08-claudemd-memory/167-example-python-project.md)
  - [Slide 168: Example - Monorepo](./part-08-claudemd-memory/168-example-monorepo.md)

## Part 9: WORKFLOW PATTERNS
Slides 169-186 (18 slides)

  - [Slide 171: Pattern 1 Example](./part-09-workflow-patterns/171-pattern-1-example.md)
  - [Slide 172: Pattern 2 TDD](./part-09-workflow-patterns/172-pattern-2-tdd.md)
  - [Slide 173: Pattern 3 Code Review](./part-09-workflow-patterns/173-pattern-3-code-review.md)
  - [Slide 174: Pattern 4 Multi-Agent](./part-09-workflow-patterns/174-pattern-4-multi-agent.md)
  - [Slide 175: Pattern 5 Visual](./part-09-workflow-patterns/175-pattern-5-visual.md)
  - [Slide 177: Pattern 6 Headless](./part-09-workflow-patterns/177-pattern-6-headless.md)
  - [Slide 178: Pattern 7 Pipeline](./part-09-workflow-patterns/178-pattern-7-pipeline.md)
  - [Slide 179: Pattern 7 JSON Output](./part-09-workflow-patterns/179-pattern-7-json-output.md)
  - [Slide 180: Pattern 8 CI/CD](./part-09-workflow-patterns/180-pattern-8-ci-cd.md)
  - [Slide 181: Cost Management](./part-09-workflow-patterns/181-cost-management.md)
  - [Slide 185: Combining Patterns](./part-09-workflow-patterns/185-combining-patterns.md)

## Part 10: RECAP & LABS
Slides 187-200 (14 slides)

  - [Slide 189: FAQ](./part-10-recap-labs/189-faq.md)
  - [Slide 191: Lab 1](./part-10-recap-labs/191-lab-1.md)
  - [Slide 192: Lab 2](./part-10-recap-labs/192-lab-2.md)
  - [Slide 193: Lab 3](./part-10-recap-labs/193-lab-3.md)
  - [Slide 194: Lab 4](./part-10-recap-labs/194-lab-4.md)
  - [Slide 195: Lab 5](./part-10-recap-labs/195-lab-5.md)
  - [Slide 199: References](./part-10-recap-labs/199-references.md)
