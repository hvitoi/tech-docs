# Well Architected Framework

- <https://aws.amazon.com/architecture/well-architected/>

## 5 Pillars

### Operational Excellence

- Run and monitor systems to deliver business value
- Continuously improve processes and procedures

- **Design Principles**
  - `IaC`
  - `Documentation`
  - `Frequent, small, reversible changes`
  - `Refine operations procedures frequently` and ensure the team is familiar with it
  - `Anticipate failure`
  - `Learn from all operational failures`

![Operational Excellence](.images/well-architected-tool-operational-excellence.png)

### Security

- Protect `information`, `systems` and `assets` while delivering business value
- `Risk assessments` and `mitigation strategies`

- **Design Principles**
  - `Implement a strong identity foundation`: centralize privileges and reduce long-term credentials - Principle of least privilege
  - `Enable traceability`: integrate logs and metrics with systems
  - `Apply security at all layers`: edge network, vpc, subnet, lb, OS, app
  - `Automate security best practices`
  - `Protect data in transit and at rest`
  - `Keep people away from data`
  - `Prepare for security events`: increase speed for detection, investigation and recovery

![Security](.images/well-architected-tool-security.png)

### Reliability

- System `recover` from infrastructure or service disruptions
- `Dynamically scale` to meet demand and `mitigate disruptions`

- **Design Principles**
  - `Test recovery procedures`: simulate different failures to recreate scenarios
  - `Automatically recover from failure`: anticipate and remediate failures
  - `Scale horizontally to aggregate system availability`
  - `Stop guessing capacity`: use autoscaling
  - `Manage change in automation`: use automation to make infrastructure

![Reliability](.images/well-architected-tool-reliability.png)

### Performance Efficiency

- Use computing resource efficiently
- Maintain that efficiency as demand changes

- **Design Principles**
  - `Democratize advanced technologies`
  - `Go global in minutes`
  - `Use serverless architectures`
  - `Experiment more often`
  - `Mechanical sympathy`: be aware of all AWS services

![Performance Efficiency](.images/well-architected-tool-reliability-performance-efficiency.png)

### Cost Optimization

- Deliver business value at the `lowest price`

- **Design Principles**
  - `Adopt a consumption mode`: pay only for what you use
  - `Measure overall efficiency`: use cloudwatch
  - `Stop spending money on data center operations`: move to cloud and stop worrying about infrastructure
  - `Analyze and attribute expensitures`: use tags to track cost of each application
  - `Use managed and application level services to reduce cost of ownership`: prefer serverless

![Cost Optimization](.images/well-architected-tool-cost-optimization.png)

## Architecture Use Cases

### Stateless Web App

![Stateless Web App](.images/architecture-statelessapp.png)

### Stateful (E-commerce)

![Stateful E-commerce](.images/architecture-ecommerce.png)

### Stateful (Blog)

![Stateful Blog](.images/architecture-blog.png)

### To Do List Mobile App

![Todo List](.images/architecture-todolist.png)

### Serverless Blogs

![Serverless Blog](.images/architecture-serverless-blog.png)

### Microservices

![Microservices](.images/architecture-microservices.png)

### Distributing paid content

![Distributing Paid Content](.images/architecture-paid-content.png)

### Software Updates Offloading

![Software Updates Offloading](.images/software-updates-offloading.png)

### Big Data Ingestion Pipeline

![Big Data Ingestion Pipeline](.images/big-data-ingestion-pipeline.png)

### Lambda, SNS, SQS

![Lambda, SNS, SQS](.images/architecture-lambda-sns-sqs.png)

### S3 Events

![S3 Events](.images/architecture-s3-events.png)

### Caching Strategies

![Caching Strategies](.images/architecture-caching-strategies.png)

### Network Security

![Network ALB](.images/architecture-network-alb.png)
![Network NLB](.images/architecture-network-nlb.png)
![Network NLB](.images/architecture-network-cloudfront.png)

### High Performance Computing (HPC)
