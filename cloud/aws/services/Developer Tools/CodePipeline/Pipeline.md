# AWS::CodePipeline::Pipeline

- Orchestrate the whole `Code` -> `Build` -> `Test` -> `Deploy` -> `Provision`

![CodePipeline](.images/codepipeline.png)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html>

```yaml
Type: AWS::CodePipeline::Pipeline
Properties:
  ArtifactStore:
    ArtifactStore
  ArtifactStores:
    - ArtifactStoreMap
  DisableInboundStageTransitions:
    - StageTransition
  ExecutionMode: String
  Name: String
  PipelineType: String
  RestartExecutionOnUpdate: Boolean
  RoleArn: String
  Stages:
    - StageDeclaration
  Tags:
    - Tag
  Triggers:
    - PipelineTriggerDeclaration
  Variables:
    - VariableDeclaration
```
