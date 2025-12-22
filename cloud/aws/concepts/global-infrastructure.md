# Infrastructure

- <https://aws.amazon.com/about-aws/global-infrastructure/regions_az/>
- `AWS` was launched for public in 2004
- First services were SQS, S3 and EC2

## Partition

- A completely independent aws infrastructure

- aws
- aws-ch
- aws-us-gov
- aws-eu (coming soon)

## Regions

- A `cluster of data` centers in a `geographic area`

- Things to consider before choosing a region
  - `Data compliance`: data governance & legal requirements
  - `Proximity`: reduces latency
  - `Available services`: not all servies are available in all regions
  - `Pricing`: prices vary from region to region

- Examples
  - `us-east-1` (Northern Virginia)
  - `eu-west-3` (Paris)
  - `sa-east-1` (São Paulo)
  - `ap-southeast-2` (Sydney)

## Availability Zones

- Each region has some availability zones
  - Usually 3, min 2, max 6
- The `AZ` is a (one or more) discrete data center with `redundant power`, `networking` and `connectivity`
- The AZ is designed to be independent (good for cases of failure)
- Different `AZ` within a region are connect with `high bandwidth` and `ultra-low latency network`

- Example (ap-southeast-2)
  - ap-southeast2a
  - ap-southeast2b
  - ap-southeast2c

## Points of Presence (Edge Locations)

- It's like a region, but limited.
- It offers a way to serve content to the end user with the higher proximity possible (and lower latency)
- It's used for `caching`

## Service Types

- **Zonal services**
  - `Control plane`: Regional
  - `Data plane`: Zonal
  - RDS, EC2, EBS
- **Regional services**
  - `Control plane`: Regional
  - `Data plane`: Regional
  - S3, SQS, DynamoDB
- **Global services**
  - `Control plane`: Single Region
  - `Data plane`: Globally Distributed
  - IAM (cp in us-east-1), CloudFront, Route 53, Global Accelerator, WAF

## Services

- Documentation: <https://docs.aws.amazon.com/>
- CloudFormation Definition: <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html>
