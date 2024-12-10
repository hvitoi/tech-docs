# AWS::EC2::SpotFleet

- A Spot Fleet request contains the configuration information to launch a `fleet of instances`
- The Spot Fleet `request` can include multiple `launch specifications`

## Spot Instance

- It's a type of EC2 instance that uses `spare capacity available` at a significantly reduced cost compared to On-Demand Instances.
- Good for batch jobs, data analysis, image processing, distributed workloads

### Pricing

- Up to `90% cheaper` than On-Demand Instances
- The pricing fluctuates based on supply and demand for capacity.

### Interruption

- AWS may interrupt your Spot Instance when the capacity is no longer available or when the Spot price exceeds the price you've set as your maximum (if specified).
- Spot Instances rely on spare capacity in AWS regions. If the capacity demand increases, `AWS can reclaim Spot Instances` with a `two-minute warning`
- The 2-minutes warnings is sent via `EventBridge`

## Spot Block

- Designed not to be interrupted
- When you cancel the spot request, the associated instances are not terminated
- If a request is pesistent, it's opened again after the instance is interrupted

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-spotfleet.html>

```yaml
Type: AWS::EC2::SpotFleet
Properties:
  SpotFleetRequestConfigData:
    SpotFleetRequestConfigData
```

### SpotFleetRequestConfigData

```yaml
AllocationStrategy: String
Context: String
ExcessCapacityTerminationPolicy: String
IamFleetRole: String
InstanceInterruptionBehavior: String
InstancePoolsToUseCount: Integer
LaunchSpecifications:
  - SpotFleetLaunchSpecification
LaunchTemplateConfigs:
  - LaunchTemplateConfig
LoadBalancersConfig:
  LoadBalancersConfig
OnDemandAllocationStrategy: String
OnDemandMaxTotalPrice: String
OnDemandTargetCapacity: Integer
ReplaceUnhealthyInstances: Boolean
SpotMaintenanceStrategies:
  SpotMaintenanceStrategies
SpotMaxTotalPrice: String
SpotPrice: String
TagSpecifications:
  - SpotFleetTagSpecification
TargetCapacity: Integer
TargetCapacityUnitType: String
TerminateInstancesWithExpiration: Boolean
Type: String
ValidFrom: String
ValidUntil: String

```

#### AllocationStrategy

- **lowestPrice**: launches instances from the `Spot Instance pools` with the lowest price
- **diversified**: launches instances from all the `Spot Instance pools` that you specify
- **capacityOptimized**: launches instances from `Spot Instance pools` with optimal capacity for the number of instances that are launching

#### TargetCapacity

- Define `number` of instances and `max cost per spot instance`
- When the price is higher you get 2min grace period to stop or terminate the instance

#### Type

- `request`: once interrupted won't launch again
- `maintain`: once interrupted will claim again
