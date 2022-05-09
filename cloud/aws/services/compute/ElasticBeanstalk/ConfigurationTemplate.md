# AWS::ElasticBeanstalk::ConfigurationTemplate

```yaml
Type: AWS::ElasticBeanstalk::ConfigurationTemplate
Properties:
  ApplicationName: String
  Description: String
  EnvironmentId: String
  OptionSettings:
    - ConfigurationOptionSetting
  PlatformArn: String
  SolutionStackName: String
  SourceConfiguration: SourceConfiguration
```

## SolutionStackName

- The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, `64bit Amazon Linux 2013.09 running Tomcat 7 Java 7`.

- Go
- Java SE
- Java With Tomcat
- .NET (Linux or Windows)
- Node.JS
- PHP
- Ruby
- Packer Builder
- Single Container Docker
- Multi-Container Docker
