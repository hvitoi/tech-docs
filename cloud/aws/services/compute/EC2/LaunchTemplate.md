# AWS::EC2::LaunchTemplate

```yaml
Type: AWS::EC2::LaunchTemplate
Properties:
  LaunchTemplateData: LaunchTemplateData
  LaunchTemplateName: String
  TagSpecifications:
    - LaunchTemplateTagSpecification
```

```yaml
BlockDeviceMappings:
  - BlockDeviceMapping
CapacityReservationSpecification: CapacityReservationSpecification
CpuOptions: CpuOptions
CreditSpecification: CreditSpecification
DisableApiTermination: Boolean
EbsOptimized: Boolean
ElasticGpuSpecifications:
  - ElasticGpuSpecification
ElasticInferenceAccelerators:
  - LaunchTemplateElasticInferenceAccelerator
EnclaveOptions: EnclaveOptions
HibernationOptions: HibernationOptions
IamInstanceProfile: IamInstanceProfile
ImageId: String
InstanceInitiatedShutdownBehavior: String
InstanceMarketOptions: InstanceMarketOptions
InstanceType: String
KernelId: String
KeyName: String
LicenseSpecifications:
  - LicenseSpecification
MetadataOptions: MetadataOptions
Monitoring: Monitoring
NetworkInterfaces:
  - NetworkInterface
Placement: Placement
RamDiskId: String
SecurityGroupIds:
  - String
SecurityGroups:
  - String
TagSpecifications:
  - TagSpecification
UserData: String
```
