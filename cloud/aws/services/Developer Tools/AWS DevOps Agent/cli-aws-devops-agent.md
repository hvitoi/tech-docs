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

## get-agent-space

```shell
AGENT_ID=
aws devops-agent get-agent-space \
  --agent-space-id $AGENT_ID
```

## enable-operator-app

- Authentication flows can use `IAM`, `IAM Identity Center (IDC)`, or an `external identity provider (IdP)`.

```shell
aws devops-agent enable-operator-app \
  --agent-space-id MyAgentSpace \
  --auth-flow iam \
  --operator-app-role-arn "arn:aws:iam::<MONITORING_ACCOUNT_ID>:role/DevOpsAgentRole-WebappAdmin"
```

## associate-service

- Creates an **AWS::DevOpsAgent::Service** and a **AWS::DevOpsAgent::Association** (if not the built-in services "aws" and "sourceaws")
- The `service-id` is either "Aws", "SourceAws", or the uuid of the AWS::DevOpsAgent::Service resource
- Built-in services do not need to you register the service beforehand

```shell
# aws - monitor
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

# aws - source
aws devops-agent associate-service \
  --agent-space-id <AGENT_SPACE_ID> \
  --service-id aws \
  --configuration '{
    "sourceAws": {
      "accountId": "<EXTERNAL_ACCOUNT_ID>",
      "accountType": "source",
      "assumableRoleArn": "arn:aws:iam::<EXTERNAL_ACCOUNT_ID>:role/DevOpsAgentCrossAccountRole"
    }
  }'
```

## list-associations

- List associations for an agent space

```shell
AGENT_ID=
aws devops-agent list-associations \
  --agent-space-id $AGENT_ID
```

## register-service

```shell
aws devops-agent register-service \
  --service servicenow \
  --service-details  '{
    "servicenow": {
      "instanceUrl": "<SERVICENOW_INSTANCE_URL>",
      "authorizationConfig": {
        "oAuthClientCredentials": {
            "clientName": "<SERVICENOW_CLIENT_NAME>",
            "clientId": "<SERVICENOW_CLIENT_ID>",
            "clientSecret": "<SERVICENOW_CLIENT_SECRET>"
        }
      }
    }
  }'
```

```shell
aws devops-agent associate-service \
  --agent-space-id <AGENT_SPACE_ID> \
  --service-id <SERVICE_ID> \
  --configuration '{
    "servicenow": {
      "instanceUrl": "<SERVICENOW_INSTANCE_URL>"
    }
  }'
```

## list-services

- List **AWS::DevOpsAgent::Service** resources

```shell
aws devops-agent list-services
```
