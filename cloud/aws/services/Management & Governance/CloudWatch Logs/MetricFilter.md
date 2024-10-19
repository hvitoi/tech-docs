# AWS::Logs::MetricFilter

- Metric filter
- Trigger alarms

## Agents

- **Log Agent**
  - A `log agent` must be installed with the role allowed to send logs to cloudwatch
  - Gather metrics every `5 min`. - If `detailed monitoring` is enabled, metrics is gathered every 1 min
  - Log config is defined in `/etc/awslogs/awslogs.conf`
  - Cloudwatch region is defined in `/etc/awslogs/awscli.conf`

  ```shell
  yum install -y awslogs
  ```

- **Unified Agent**
  - The `unified agent` is a newer version of the log agent
    - It can collect additional system-level metrics (RAM, CPU, Disk IO, netstat, processes, swap, etc)

## Instance Recovery

- Recovery an EC2 instance based on metric
- After recovery, the new instance gets:
  - Same Private, Public, Elastic IP
  - Same Metadata
  - Placement group
  - ...

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html>

```yaml
Type: AWS::Logs::MetricFilter
Properties:
  FilterName: String
  FilterPattern: String
  LogGroupName: String
  MetricTransformations:
    - MetricTransformation
```
