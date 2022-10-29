# AWS::Logs::MetricFilter

- Metric filter
- Trigger alarms

```yaml
Type: AWS::Logs::MetricFilter
Properties:
  FilterPattern: String
  LogGroupName: String
  MetricTransformations:
    - MetricTransformation
```

- **Agents**

- _Log Agent_

  - A `log agent` must be installed with the role allowed to send logs to cloudwatch
  - Gather metrics every `5 min`. - If `detailed monitoring` is enabled, metrics is gathered every 1 min
  - Log config is defined in `/etc/awslogs/awslogs.conf`
  - Cloudwatch region is defined in `/etc/awslogs/awscli.conf`

  ```sh
  yum install -y awslogs
  ```

- _Unified Agent_

  - The `unified agent` is a newer version of the log agent
    - It can collect additional system-level metrics (RAM, CPU, Disk IO, netstat, processes, swap, etc)

- **Instance Recovery**

  - Recovery an EC2 instance based on metric
  - After recovery, the new instance gets:
    - Same Private, Public, Elastic IP
    - Same Metadata
    - Placement group
    - ...
