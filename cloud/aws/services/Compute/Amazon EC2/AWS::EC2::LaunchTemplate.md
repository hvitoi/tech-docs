# AWS::EC2::LaunchTemplate

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html>

```yaml
Type: AWS::EC2::LaunchTemplate
Properties:
  LaunchTemplateData:
    LaunchTemplateData
  LaunchTemplateName: String
  TagSpecifications:
    - LaunchTemplateTagSpecification
  VersionDescription: String
```

### LaunchTemplateData

```yaml
BlockDeviceMappings:
  - BlockDeviceMapping
CapacityReservationSpecification:
  CapacityReservationSpecification
CpuOptions:
  CpuOptions
CreditSpecification:
  CreditSpecification
DisableApiStop: Boolean
DisableApiTermination: Boolean
EbsOptimized: Boolean
ElasticGpuSpecifications:
  - ElasticGpuSpecification
ElasticInferenceAccelerators:
  - LaunchTemplateElasticInferenceAccelerator
EnclaveOptions:
  EnclaveOptions
HibernationOptions:
  HibernationOptions
IamInstanceProfile:
  IamInstanceProfile
ImageId: String
InstanceInitiatedShutdownBehavior: String
InstanceMarketOptions:
  InstanceMarketOptions
InstanceRequirements:
  InstanceRequirements
InstanceType: String
KernelId: String
KeyName: String
LicenseSpecifications:
  - LicenseSpecification
MaintenanceOptions:
  MaintenanceOptions
MetadataOptions:
  MetadataOptions
Monitoring:
  Monitoring
NetworkInterfaces:
  - NetworkInterface
Placement:
  Placement
PrivateDnsNameOptions:
  PrivateDnsNameOptions
RamDiskId: String
SecurityGroupIds:
  - String
SecurityGroups:
  - String
TagSpecifications:
  - TagSpecification
UserData: String
```
