# AWS::InspectorV2::CisScanConfiguration

- `Security Assessments` for EC2 instances!
- Spot `vulnerabilities` with the OS AMI
- Spot `unintended network access`

- The **Inspector Agent** must be installed in the EC2 instance

![Inspector](.images/inspector.png)

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html>

```yaml
Type: AWS::InspectorV2::CisScanConfiguration
Properties:
  ScanName: String
  Schedule:
    Schedule
  SecurityLevel: String
  Tags:
    Key: Value
  Targets:
    CisTargets
```
