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
SPACE_ID=
aws devops-agent get-agent-space \
  --agent-space-id $SPACE_ID
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
- Does not list `aws` or `sourceaws` services, it's an association directly ("built-in" services)

```shell
aws devops-agent list-services
```

## associate-service

- Creates an **AWS::DevOpsAgent::Service** and a **AWS::DevOpsAgent::Association** (if not the built-in services "aws" and "sourceaws")
- The `service-id` is either "Aws", "SourceAws", or the uuid of the AWS::DevOpsAgent::Service resource
- Built-in services do not need to you register the service beforehand
- Your role needs a PassRole permission for passing `arn:aws:iam::<ACCOUNT_ID>:role/DevOpsAgentRole-AgentSpace` to the DevOps Agent

```shell
# aws (self aws account)
aws devops-agent associate-service \
  --agent-space-id "MyAgentSpace" \
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
# aws (external aws account)
aws devops-agent associate-service \
  --agent-space-id "MyAgentSpace" \
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
SPACE_ID=
aws devops-agent list-associations \
  --agent-space-id $SPACE_ID
```

## enable-operator-app

- Authentication flows can use `IAM`, `IAM Identity Center (IDC)`, or an `external identity provider (IdP)`.
- Your role needs a PassRole permission for passing `arn:aws:iam::<ACCOUNT_ID>:role/DevOpsAgentRole-WebappAdmin` to the DevOps Agent

```shell
aws devops-agent enable-operator-app \
  --agent-space-id MyAgentSpace \
  --auth-flow iam \
  --operator-app-role-arn "arn:aws:iam::<ACCOUNT_ID>:role/DevOpsAgentRole-WebappAdmin"
```

## list-private-connections

```shell
aws devops-agent list-private-connections
```

- Does **not** return subnets or security groups — those are on the underlying VPC Lattice Resource Gateway
- To see subnets/SGs, use the `resourceGatewayId` from the output and run:

```shell
aws vpc-lattice get-resource-gateway \
  --resource-gateway-identifier <RESOURCE_GATEWAY_ARN>
```

```shell
NAME=
aws devops-agent describe-private-connection \
  --name $NAME
```

## create-private-connection

```shell
aws devops-agent create-private-connection \
    --name prometheus-mcp \
    --mode '{
      "serviceManaged": {
        "hostAddress": "prometheus-mcp.example.com",
        "vpcId": "vpc-00000000000000000",
        "subnetIds": [
          "subnet-00000000000000001",
          "subnet-00000000000000002",
          "subnet-00000000000000003"
        ],
        "securityGroupIds": ["sg-00000000000000000"],
        "portRanges": ["443"]
      }
    }'
```
