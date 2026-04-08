# aws devops-agent

## create-agent-space

- Creates an **AWS::DevOpsAgent::AgentSpace**

```shell
aws devops-agent create-agent-space \
  --name "MyAgentSpace" \
  --description "AgentSpace for monitoring my application"

```

## list-agent-spaces

```shell
aws devops-agent list-agent-spaces
```

## associate-service

- Creates an **AWS::DevOpsAgent::Service** and a **AWS::DevOpsAgent::Association** (if not the built-in services "aws" and "sourceaws")
- The `service-id` is either "Aws", "SourceAws", or the uuid of the AWS::DevOpsAgent::Service resource

```shell
aws devops-agent associate-service \
  --agent-space-id "MyAgentSpace" \
  --service-id aws \
  --configuration '{
    "aws": {
      "assumableRoleArn": "arn:aws:iam::<MONITORING_ACCOUNT_ID>:role/DevOpsAgentRole-AgentSpace",
      "accountId": "<MONITORING_ACCOUNT_ID>",
      "accountType": "monitor"
    }
  }'
```

## enable-operator-app

- Authentication flows can use `IAM`, `IAM Identity Center (IDC)`, or an `external identity provider (IdP)`.

```shell
aws devops-agent enable-operator-app \
  --agent-space-id MyAgentSpace \
  --auth-flow iam \
  --operator-app-role-arn "arn:aws:iam::<MONITORING_ACCOUNT_ID>:role/DevOpsAgentRole-WebappAdmin"
```
