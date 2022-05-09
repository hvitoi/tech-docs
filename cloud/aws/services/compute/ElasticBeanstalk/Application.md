# AWS::ElasticBeanstalk::Application

- `Elastic Beanstalk` is a developer-centric view of deploying an app on AWS
- It's a managed service that manages components such as EC2, ASG, ELB, RDS together! Bundled as a single interface
- `Application`: collection of beanstalk components

```yaml
Type: AWS::ElasticBeanstalk::Application
Properties:
  ApplicationName: String
  Description: String
  ResourceLifecycleConfig: ApplicationResourceLifecycleConfig
```

## ResourceLifecycleConfig

- Specifies an application resource lifecycle configuration to prevent your application from accumulating too many versions.
