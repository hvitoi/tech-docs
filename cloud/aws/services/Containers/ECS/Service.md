# AWS::ECS::Service

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html>

```yaml
Type: AWS::ECS::Service
Properties:
  CapacityProviderStrategy:
    - CapacityProviderStrategyItem
  Cluster: String
  DeploymentConfiguration:
    DeploymentConfiguration
  DeploymentController:
    DeploymentController
  DesiredCount: Integer
  EnableECSManagedTags: Boolean
  EnableExecuteCommand: Boolean
  HealthCheckGracePeriodSeconds: Integer
  LaunchType: String
  LoadBalancers:
    - LoadBalancer
  NetworkConfiguration:
    NetworkConfiguration
  PlacementConstraints:
    - PlacementConstraint
  PlacementStrategies:
    - PlacementStrategy
  PlatformVersion: String
  PropagateTags: String
  Role: String
  SchedulingStrategy: String
  ServiceConnectConfiguration:
    ServiceConnectConfiguration
  ServiceName: String
  ServiceRegistries:
    - ServiceRegistry
  Tags:
    - Tag
  TaskDefinition: String
  VolumeConfigurations:
    - ServiceVolumeConfiguration
```

### DeploymentConfiguration

- **Rolling Updates**
- Control how many tasks can started and stopped and in which order
- E.g., `Min Healthy Instances` (100%), `Max Healthy Instances` (150%)
