# Chapter 3: Admin Setup

설치, OS, 사내망 통합

코드 블록 슬라이드: 57개

[← 워크샵 메인](../README.md)

## 파트 목록

## Part 1: DEPLOYMENT STRATEGY
Slides 6-20 (15 slides)

  - [Slide 8: Internal mirror setup](./part-01-deployment-strategy/008-internal-mirror-setup.md)
  - [Slide 10: Native installer mass deployment](./part-01-deployment-strategy/010-native-installer-mass-deployment.md)
  - [Slide 11: Windows MSI deployment](./part-01-deployment-strategy/011-windows-msi-deployment.md)
  - [Slide 12: Docker enterprise image](./part-01-deployment-strategy/012-docker-enterprise-image.md)
  - [Slide 13: Version pinning](./part-01-deployment-strategy/013-version-pinning.md)
  - [Slide 15: Offline air-gapped](./part-01-deployment-strategy/015-offline-air-gapped.md)
  - [Slide 18: Cost forecasting](./part-01-deployment-strategy/018-cost-forecasting.md)

## Part 2: CREDENTIALS MANAGEMENT
Slides 21-35 (15 slides)

  - [Slide 24: Bedrock model access](./part-02-credentials-management/024-bedrock-model-access.md)
  - [Slide 25: IAM policy](./part-02-credentials-management/025-iam-policy.md)
  - [Slide 26: Bedrock env config](./part-02-credentials-management/026-bedrock-env-config.md)
  - [Slide 27: Bedrock SSO integration](./part-02-credentials-management/027-bedrock-sso-integration.md)
  - [Slide 28: Vertex AI setup](./part-02-credentials-management/028-vertex-ai-setup.md)
  - [Slide 29: OAuth Pro/Max](./part-02-credentials-management/029-oauth-pro-max.md)
  - [Slide 31: PrivateLink/VPC Endpoint](./part-02-credentials-management/031-privatelink-vpc-endpoint.md)
  - [Slide 34: Lab environment credentials](./part-02-credentials-management/034-lab-environment-credentials.md)

## Part 3: NETWORK & SECURITY
Slides 36-50 (15 slides)

  - [Slide 37: Proxy basics](./part-03-network-security/037-proxy-basics.md)
  - [Slide 38: Authenticated proxy](./part-03-network-security/038-authenticated-proxy.md)
  - [Slide 39: Internal CA cert](./part-03-network-security/039-internal-ca-cert.md)
  - [Slide 41: Internal DNS](./part-03-network-security/041-internal-dns.md)
  - [Slide 44: Outbound traffic inspection](./part-03-network-security/044-outbound-traffic-inspection.md)
  - [Slide 45: Hooks for DLP](./part-03-network-security/045-hooks-for-dlp.md)
  - [Slide 46: Internal MCP server](./part-03-network-security/046-internal-mcp-server.md)
  - [Slide 47: Network troubleshooting](./part-03-network-security/047-network-troubleshooting.md)

## Part 4: GOVERNANCE & POLICY
Slides 51-65 (15 slides)

  - [Slide 52: Settings hierarchy](./part-04-governance-policy/052-settings-hierarchy.md)
  - [Slide 53: managed-settings.json sample](./part-04-governance-policy/053-managed-settings-json-sample.md)
  - [Slide 54: Permission patterns](./part-04-governance-policy/054-permission-patterns.md)
  - [Slide 56: Distributing managed-settings](./part-04-governance-policy/056-distributing-managed-settings.md)
  - [Slide 57: MCP server allowlist](./part-04-governance-policy/057-mcp-server-allowlist.md)
  - [Slide 58: Hooks for governance](./part-04-governance-policy/058-hooks-for-governance.md)
  - [Slide 59: Audit log hook example](./part-04-governance-policy/059-audit-log-hook-example.md)
  - [Slide 60: User policy banner](./part-04-governance-policy/060-user-policy-banner.md)

## Part 5: MONITORING & COST CONTROL
Slides 66-80 (15 slides)

  - [Slide 68: OTel configuration](./part-05-monitoring-cost-control/068-otel-configuration.md)
  - [Slide 70: /cost command](./part-05-monitoring-cost-control/070-cost-command.md)
  - [Slide 71: Cost dashboard](./part-05-monitoring-cost-control/071-cost-dashboard.md)
  - [Slide 72: Cost Explorer](./part-05-monitoring-cost-control/072-cost-explorer.md)
  - [Slide 73: Budget alarms](./part-05-monitoring-cost-control/073-budget-alarms.md)
  - [Slide 74: Automatic throttling](./part-05-monitoring-cost-control/074-automatic-throttling.md)
  - [Slide 75: Per-user tracking](./part-05-monitoring-cost-control/075-per-user-tracking.md)
  - [Slide 77: Token efficiency tips](./part-05-monitoring-cost-control/077-token-efficiency-tips.md)

## Part 6: SSO & IDENTITY INTEGRATION
Slides 81-95 (15 slides)

  - [Slide 84: IAM Identity Center deep dive](./part-06-sso-identity-integration/084-iam-identity-center-deep-dive.md)
  - [Slide 85: Okta integration](./part-06-sso-identity-integration/085-okta-integration.md)
  - [Slide 86: Azure AD integration](./part-06-sso-identity-integration/086-azure-ad-integration.md)
  - [Slide 87: Google Workspace integration](./part-06-sso-identity-integration/087-google-workspace-integration.md)
  - [Slide 89: MFA enforcement](./part-06-sso-identity-integration/089-mfa-enforcement.md)
  - [Slide 90: JIT provisioning](./part-06-sso-identity-integration/090-jit-provisioning.md)
  - [Slide 91: SCIM provisioning](./part-06-sso-identity-integration/091-scim-provisioning.md)
  - [Slide 93: Offboarding](./part-06-sso-identity-integration/093-offboarding.md)
  - [Slide 94: Audit identity events](./part-06-sso-identity-integration/094-audit-identity-events.md)

## Part 7: AUDIT & COMPLIANCE
Slides 96-105 (10 slides)

  - [Slide 97: CloudTrail integration](./part-07-audit-compliance/097-cloudtrail-integration.md)
  - [Slide 102: Audit report automation](./part-07-audit-compliance/102-audit-report-automation.md)

## Part 8: TROUBLESHOOTING
Slides 106-110 (5 slides)

  - [Slide 107: Auth troubleshooting](./part-08-troubleshooting/107-auth-troubleshooting.md)
  - [Slide 108: Network troubleshooting](./part-08-troubleshooting/108-network-troubleshooting.md)

## Part 9: RECAP & 3 LABS
Slides 111-120 (10 slides)

  - [Slide 113: Lab 1 / Internal mirror](./part-09-recap-labs/113-lab-1-internal-mirror.md)
  - [Slide 114: Lab 2 / Bedrock SSO](./part-09-recap-labs/114-lab-2-bedrock-sso.md)
  - [Slide 115: Lab 3 / Governance](./part-09-recap-labs/115-lab-3-governance.md)
  - [Slide 116: FAQ](./part-09-recap-labs/116-faq.md)
  - [Slide 119: References](./part-09-recap-labs/119-references.md)
