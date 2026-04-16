# Setup

## IAM Role: AgentSpace

- <https://docs.aws.amazon.com/devopsagent/latest/userguide/getting-started-with-aws-devops-agent-cli-onboarding-guide.html>
- It's role grants to the `Agent Space` access to `AWS resources` in this account (the same account in which the AgentSpace is deployed). You can add access to resources in `secondary AWS accounts` when setting up the capabilities of this Agent Space.

```shell
# Create Role
cat > trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "aidevops.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<ACCOUNT_ID>"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:aidevops:<REGION>:<ACCOUNT_ID>:agentspace/*"
        }
      }
    }
  ]
}
EOF

aws iam create-role \
  --role-name DevOpsAgentRole-AgentSpace \
  --assume-role-policy-document file://trust-policy.json

# Get Role ARN
aws iam get-role --role-name DevOpsAgentRole-AgentSpace --query 'Role.Arn' --output text

# Attach Managed Policy
aws iam attach-role-policy \
  --role-name DevOpsAgentRole-AgentSpace \
  --policy-arn arn:aws:iam::aws:policy/AIDevOpsAgentAccessPolicy

# Attach Inline Policy
cat > inline-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCreateServiceLinkedRoles",
      "Effect": "Allow",
      "Action": [
        "iam:CreateServiceLinkedRole"
      ],
      "Resource": [
        "arn:aws:iam::<ACCOUNT_ID>:role/aws-service-role/resource-explorer-2.amazonaws.com/AWSServiceRoleForResourceExplorer"
      ]
    }
  ]
}
EOF

aws iam put-role-policy \
  --role-name DevOpsAgentRole-AgentSpace \
  --policy-name AllowCreateServiceLinkedRoles \
  --policy-document file://inline-policy.json
```

## IAM Role: WebApp (Operator)

- This role grants to the `WebApp` access to this `AgentSpace`

```shell
# Create role
cat > trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "aidevops.amazonaws.com"
      },
      "Action": [
        "sts:AssumeRole",
        "sts:TagSession"
      ],
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<ACCOUNT_ID>"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:aidevops:<REGION>:<ACCOUNT_ID>:agentspace/*"
        }
      }
    }
  ]
}
EOF

aws iam create-role \
  --role-name DevOpsAgentRole-WebappAdmin \
  --assume-role-policy-document file://trust-policy.json

# Get Role ARN
aws iam get-role --role-name DevOpsAgentRole-WebappAdmin --query 'Role.Arn' --output text

# Attach managed policy
aws iam attach-role-policy \
  --role-name DevOpsAgentRole-WebappAdmin \
  --policy-arn arn:aws:iam::aws:policy/AIDevOpsOperatorAppAccessPolicy
```

## IAM Role: AgentSpace (Source Account) - OPTIONAL

- Create this role in an external account if you need your Agent Space in the monitoring account to access other accounts

```shell
# Create Role
cat > trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "aidevops.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<MONITORING_ACCOUNT_ID>",
          "sts:ExternalId": "arn:aws:aidevops:<REGION>:<MONITORING_ACCOUNT_ID>:agentspace/<AGENT_SPACE_ID>"
        }
      }
    }
  ]
}
EOF

aws iam create-role \
  --role-name DevOpsAgentCrossAccountRole \
  --assume-role-policy-document file://trust-policy.json

# Get Role ARN
aws iam get-role --role-name DevOpsAgentCrossAccountRole --query 'Role.Arn' --output text

# Attach Managed Policy
aws iam attach-role-policy \
  --role-name DevOpsAgentCrossAccountRole \
  --policy-arn arn:aws:iam::aws:policy/AIDevOpsAgentAccessPolicy

# Attach Inline Policy
cat > inline-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCreateServiceLinkedRoles",
      "Effect": "Allow",
      "Action": [
        "iam:CreateServiceLinkedRole"
      ],
      "Resource": [
        "arn:aws:iam::<EXTERNAL_ACCOUNT_ID>:role/aws-service-role/resource-explorer-2.amazonaws.com/AWSServiceRoleForResourceExplorer"
      ]
    }
  ]
}
EOF

aws iam put-role-policy \
  --role-name DevOpsAgentCrossAccountRole \
  --policy-name AllowCreateServiceLinkedRoles \
  --policy-document file://inline-policy.json
```

## Create AgentSpace

```shell
aws devops-agent create-agent-space \
  --name "MyAgentSpace" \
  --description "AgentSpace for monitoring my application"

aws devops-agent list-agent-spaces
```

- On the first setup on an account, your user role will need you will permissions to
- This is done via `aws iam create-service-linked-role --aws-service-name aidevops.amazonaws.com` and it's executed automatically when creating the first agent space on that account

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aidevops:*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:CreateServiceLinkedRole"
      ],
      "Resource": "arn:aws:iam::*:role/aws-service-role/aidevops.amazonaws.com/AWSServiceRoleForAIDevOps"
    }
  ]
}
```

## Associate Services

```shell
# Associate with the built-in service "Aws" (an AWS Account)
aws devops-agent associate-service \
  --agent-space-id MyAgentSpace \
  --service-id aws \
  --configuration '{
    "aws": {
      "assumableRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/DevOpsAgentRole-AgentSpace",
      "accountId": "<ACCOUNT_ID>",
      "accountType": "monitor"
    }
  }'

```

```shell
# Associate the external account (optional) - requires creating a role in the external account
aws devops-agent associate-service \
  --agent-space-id MyAgentSpace \
  --service-id aws \
  --configuration '{
    "sourceAws": {
      "accountId": "<EXTERNAL_ACCOUNT_ID>",
      "accountType": "source",
      "assumableRoleArn": "arn:aws:iam::<EXTERNAL_ACCOUNT_ID>:role/DevOpsAgentCrossAccountRole"
    }
  }'
```

## Enable Operator App

```shell
aws devops-agent enable-operator-app \
  --agent-space-id MyAgentSpace \
  --auth-flow iam \
  --operator-app-role-arn "arn:aws:iam::<MONITORING_ACCOUNT_ID>:role/DevOpsAgentRole-WebappAdmin"
```
