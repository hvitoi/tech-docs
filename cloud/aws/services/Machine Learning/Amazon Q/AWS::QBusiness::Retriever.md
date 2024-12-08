# AWS::QBusiness::Retriever

- A retriever is an index from which data can be get in real time
- The selection of the retriever influences on the available data sources
- Supported data sources:
  - S3
  - Web crawler
  - Upload
  - etc

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-qbusiness-retriever.html>

```yaml
Type: AWS::QBusiness::Retriever
Properties:
  ApplicationId: String
  Configuration:
    RetrieverConfiguration
  DisplayName: String
  RoleArn: String
  Tags:
    - Tag
  Type: String
```
