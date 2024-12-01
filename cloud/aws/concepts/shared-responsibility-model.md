# Shared Responsibility Model

- <https://aws.amazon.com/compliance/shared-responsibility-model/>

![Shared Responsibility](.images/shared-responsibility.png)

## Responsibilities

- **AWS Responsibility**
  - Protect infrastructure
  - Managed services (s3, dynamo, rds, etc)

- **Customer Responsibility**
  - EC2: manage the OS, firewall, network config, IAM
  - Encrypt application data

- **Shared Controls**
  - Patch Management
  - Configuration Management
  - Awareness & Training
