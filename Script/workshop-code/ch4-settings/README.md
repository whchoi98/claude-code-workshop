# Chapter 4: Settings

settings.json, slash, hooks

코드 블록 슬라이드: 86개

[← 워크샵 메인](../README.md)

## 파트 목록

## Part 1: settings.json 구조
Slides 6-20 (15 slides)

  - [Slide 7: 3-tier hierarchy](./part-01-settings-json-structure/007-3-tier-hierarchy.md)
  - [Slide 8: Full options overview](./part-01-settings-json-structure/008-full-options-overview.md)
  - [Slide 9: permissions deep dive](./part-01-settings-json-structure/009-permissions-deep-dive.md)
  - [Slide 10: model field](./part-01-settings-json-structure/010-model-field.md)
  - [Slide 11: hooks options overview](./part-01-settings-json-structure/011-hooks-options-overview.md)
  - [Slide 12: mcpServers options](./part-01-settings-json-structure/012-mcpservers-options.md)
  - [Slide 13: telemetry & theme](./part-01-settings-json-structure/013-telemetry-theme.md)
  - [Slide 15: Personal user example](./part-01-settings-json-structure/015-personal-user-example.md)
  - [Slide 16: Team project example](./part-01-settings-json-structure/016-team-project-example.md)
  - [Slide 17: Org standard example](./part-01-settings-json-structure/017-org-standard-example.md)
  - [Slide 18: settings.local.json](./part-01-settings-json-structure/018-settings-local-json.md)
  - [Slide 19: Settings validation](./part-01-settings-json-structure/019-settings-validation.md)

## Part 2: PERMISSIONS 심화
Slides 21-35 (15 slides)

  - [Slide 23: Pattern syntax](./part-02-permissions-deepdive/023-pattern-syntax.md)
  - [Slide 24: Bash patterns deep](./part-02-permissions-deepdive/024-bash-patterns-deep.md)
  - [Slide 25: Path glob patterns](./part-02-permissions-deepdive/025-path-glob-patterns.md)
  - [Slide 26: Specificity rules](./part-02-permissions-deepdive/026-specificity-rules.md)
  - [Slide 27: /permissions command](./part-02-permissions-deepdive/027-permissions-command.md)
  - [Slide 29: Granular permissions](./part-02-permissions-deepdive/029-granular-permissions.md)
  - [Slide 30: Sensitive data protection](./part-02-permissions-deepdive/030-sensitive-data-protection.md)
  - [Slide 31: additionalDirectories](./part-02-permissions-deepdive/031-additionaldirectories.md)
  - [Slide 32: Approval flow](./part-02-permissions-deepdive/032-approval-flow.md)

## Part 3: HOOKS 4가지 시점
Slides 36-50 (15 slides)

  - [Slide 37: Hook structure](./part-03-hooks-4/037-hook-structure.md)
  - [Slide 38: Hook input format](./part-03-hooks-4/038-hook-input-format.md)
  - [Slide 39: Hook output format](./part-03-hooks-4/039-hook-output-format.md)
  - [Slide 41: PreToolUse example](./part-03-hooks-4/041-pretooluse-example.md)
  - [Slide 43: PostToolUse example](./part-03-hooks-4/043-posttooluse-example.md)
  - [Slide 45: SessionStart example](./part-03-hooks-4/045-sessionstart-example.md)
  - [Slide 47: Stop example](./part-03-hooks-4/047-stop-example.md)
  - [Slide 48: Hook chaining](./part-03-hooks-4/048-hook-chaining.md)
  - [Slide 49: Hook debugging](./part-03-hooks-4/049-hook-debugging.md)

## Part 4: HOOKS 실전 패턴
Slides 51-65 (15 slides)

  - [Slide 53: Pattern 1 / Auto Lint - settings](./part-04-hooks-practical/053-pattern-1-auto-lint-settings.md)
  - [Slide 54: Pattern 1 / Auto Lint - script](./part-04-hooks-practical/054-pattern-1-auto-lint-script.md)
  - [Slide 56: Pattern 2 / DLP - script](./part-04-hooks-practical/056-pattern-2-dlp-script.md)
  - [Slide 57: Pattern 3 / Audit - design](./part-04-hooks-practical/057-pattern-3-audit-design.md)
  - [Slide 58: Pattern 3 / Audit - script](./part-04-hooks-practical/058-pattern-3-audit-script.md)
  - [Slide 60: Pattern 4 / Slack - script](./part-04-hooks-practical/060-pattern-4-slack-script.md)
  - [Slide 61: Pattern 5 / Auto Format combined](./part-04-hooks-practical/061-pattern-5-auto-format-combined.md)
  - [Slide 62: Combining patterns](./part-04-hooks-practical/062-combining-patterns.md)

## Part 5: MCP 기본과 공식 서버
Slides 66-85 (20 slides)

  - [Slide 68: MCP primitives](./part-05-mcp-basics-server/068-mcp-primitives.md)
  - [Slide 69: 3 transport methods](./part-05-mcp-basics-server/069-3-transport-methods.md)
  - [Slide 70: stdio transport details](./part-05-mcp-basics-server/070-stdio-transport-details.md)
  - [Slide 71: HTTP transport](./part-05-mcp-basics-server/071-http-transport.md)
  - [Slide 72: SSE transport](./part-05-mcp-basics-server/072-sse-transport.md)
  - [Slide 73: Official server: filesystem](./part-05-mcp-basics-server/073-official-server-filesystem.md)
  - [Slide 74: Official server: github](./part-05-mcp-basics-server/074-official-server-github.md)
  - [Slide 75: Official server: slack](./part-05-mcp-basics-server/075-official-server-slack.md)
  - [Slide 76: Official server: postgres](./part-05-mcp-basics-server/076-official-server-postgres.md)
  - [Slide 77: Official server: jira](./part-05-mcp-basics-server/077-official-server-jira.md)
  - [Slide 78: /mcp command](./part-05-mcp-basics-server/078-mcp-command.md)
  - [Slide 84: Multi-server orchestration](./part-05-mcp-basics-server/084-multi-server-orchestration.md)

## Part 6: MCP 사내 서버 구축
Slides 86-105 (20 slides)

  - [Slide 88: SDK setup](./part-06-mcp-server/088-sdk-setup.md)
  - [Slide 89: Basic server skeleton](./part-06-mcp-server/089-basic-server-skeleton.md)
  - [Slide 90: Registering tools (part 1)](./part-06-mcp-server/090-registering-tools-part-1.md)
  - [Slide 91: Registering tools (part 2)](./part-06-mcp-server/091-registering-tools-part-2.md)
  - [Slide 92: Resources implementation](./part-06-mcp-server/092-resources-implementation.md)
  - [Slide 93: Prompts implementation](./part-06-mcp-server/093-prompts-implementation.md)
  - [Slide 94: Input validation](./part-06-mcp-server/094-input-validation.md)
  - [Slide 95: Authentication](./part-06-mcp-server/095-authentication.md)
  - [Slide 96: Error handling](./part-06-mcp-server/096-error-handling.md)
  - [Slide 97: Logging](./part-06-mcp-server/097-logging.md)
  - [Slide 98: Testing the server](./part-06-mcp-server/098-testing-the-server.md)
  - [Slide 99: Docker packaging](./part-06-mcp-server/099-docker-packaging.md)
  - [Slide 100: HTTP server mode](./part-06-mcp-server/100-http-server-mode.md)
  - [Slide 101: Deployment to Kubernetes](./part-06-mcp-server/101-deployment-to-kubernetes.md)
  - [Slide 102: Real-world example](./part-06-mcp-server/102-real-world-example.md)
  - [Slide 104: Versioning and updates](./part-06-mcp-server/104-versioning-and-updates.md)

## Part 7: CUSTOM SLASH COMMANDS
Slides 106-120 (15 slides)

  - [Slide 107: Command basics](./part-07-custom-slash-commands/107-command-basics.md)
  - [Slide 108: Command with arguments](./part-07-custom-slash-commands/108-command-with-arguments.md)
  - [Slide 109: Frontmatter](./part-07-custom-slash-commands/109-frontmatter.md)
  - [Slide 110: Tool restriction in commands](./part-07-custom-slash-commands/110-tool-restriction-in-commands.md)
  - [Slide 111: Real-world command 1: PR review](./part-07-custom-slash-commands/111-real-world-command-1-pr-review.md)
  - [Slide 112: Real-world command 2: Deployment](./part-07-custom-slash-commands/112-real-world-command-2-deployment.md)
  - [Slide 113: Real-world command 3: Debugging](./part-07-custom-slash-commands/113-real-world-command-3-debugging.md)
  - [Slide 114: Real-world command 4: Sprint summary](./part-07-custom-slash-commands/114-real-world-command-4-sprint-summary.md)
  - [Slide 115: Real-world command 5: Translate](./part-07-custom-slash-commands/115-real-world-command-5-translate.md)
  - [Slide 116: Team library](./part-07-custom-slash-commands/116-team-library.md)

## Part 8: INTEGRATION & TROUBLESHOOTING
Slides 121-130 (10 slides)

  - [Slide 122: 4-mechanism integration](./part-08-integration-troubleshooting/122-4-mechanism-integration.md)
  - [Slide 125: Troubleshooting: Hooks not firing](./part-08-integration-troubleshooting/125-troubleshooting-hooks-not-firing.md)
  - [Slide 126: Troubleshooting: MCP connection](./part-08-integration-troubleshooting/126-troubleshooting-mcp-connection.md)
  - [Slide 127: Troubleshooting: Permission denied](./part-08-integration-troubleshooting/127-troubleshooting-permission-denied.md)

## Part 9: RECAP & 4 LABS
Slides 131-140 (10 slides)

  - [Slide 133: Lab 1 / First settings.json](./part-09-recap-labs/133-lab-1-first-settings-json.md)
  - [Slide 134: Lab 2 / PreToolUse Hook](./part-09-recap-labs/134-lab-2-pretooluse-hook.md)
  - [Slide 135: Lab 3 / Custom MCP server](./part-09-recap-labs/135-lab-3-custom-mcp-server.md)
  - [Slide 136: Lab 4 / Custom Slash Command](./part-09-recap-labs/136-lab-4-custom-slash-command.md)
  - [Slide 137: FAQ](./part-09-recap-labs/137-faq.md)
  - [Slide 139: References](./part-09-recap-labs/139-references.md)
