# AWS::Bedrock::Guardrail

- Control the interaction between the users and the Foundation Model (FM)
- E.g., filter undesirable and harmful content
- It's also useful to avoid hallucination (ground checking)

- Options
  - `Content filters`
  - `Denied topics`
  - `Word filters`
  - `Sensitive information filters`
  - `Contextual grounding check`

- Guardrails can then be applied to FMs

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-guardrail.html>

```yaml
Type: AWS::Bedrock::Guardrail
Properties:
  BlockedInputMessaging: String
  BlockedOutputsMessaging: String
  ContentPolicyConfig:
    ContentPolicyConfig
  ContextualGroundingPolicyConfig:
    ContextualGroundingPolicyConfig
  Description: String
  KmsKeyArn: String
  Name: String
  SensitiveInformationPolicyConfig:
    SensitiveInformationPolicyConfig
  Tags:
    - Tag
  TopicPolicyConfig:
    TopicPolicyConfig
  WordPolicyConfig:
    WordPolicyConfig
```
