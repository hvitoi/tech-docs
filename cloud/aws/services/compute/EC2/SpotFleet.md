# AWS::EC2::SpotFleet

- A Spot Fleet request contains the configuration information to launch a `fleet of instances`
- The Spot Fleet `request` can include multiple `launch specifications`

- **Spot Instance**
  - Cheap (up to 90% discount)
  - Less reliable
  - Good for batch jobs, data analysis, image processing, distributed workloads
- **Spot Block**
  - Designed not to be interrupted
  - When you cancel the spot request, the associated instances are not terminated
  - If a request is pesistent, it's opened again after the instance is interrupted

```yaml
Type: AWS::EC2::SpotFleet
Properties:
  SpotFleetRequestConfigData: SpotFleetRequestConfigData
```

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
LoadBalancersConfig: LoadBalancersConfig
OnDemandAllocationStrategy: String
OnDemandMaxTotalPrice: String
OnDemandTargetCapacity: Integer
ReplaceUnhealthyInstances: Boolean
SpotMaintenanceStrategies: SpotMaintenanceStrategies
SpotMaxTotalPrice: String
SpotPrice: String
TargetCapacity: Integer
TerminateInstancesWithExpiration: Boolean
Type: String
ValidFrom: String
ValidUntil: String
```

## SpotFleetRequestConfigData

### AllocationStrategy

- **lowestPrice**: launches instances from the `Spot Instance pools` with the lowest price
- **diversified**: launches instances from all the `Spot Instance pools` that you specify
- **capacityOptimized**: launches instances from `Spot Instance pools` with optimal capacity for the number of instances that are launching

### TargetCapacity

- Define `number` of instances and `max cost per spot instance`
- When the price is higher you get 2min grace period to stop or terminate the instance

### Type

- `request`: once interrupted won't launch again
- `maintain`: once interrupted will claim again
