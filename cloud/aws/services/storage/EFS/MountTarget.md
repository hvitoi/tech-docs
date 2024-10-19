# AWS::EFS::MountTarget

```shell
# EFS mount helper
yum install -y "amazon-efs-utils"
mount "fs-a7fe24dc:/" "./my-shared-dir" \
  -t "efs" \
  -o "tls" \

# NFS client
sudo mount "fs-a7fe24dc.efs.us-east-2.amazonaws.com:/" "./my-shared-dir" \
  -t "nfs4" \
  -o "nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport"
```

## Properties

- <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html>

```yaml
Type: AWS::EFS::MountTarget
Properties:
  FileSystemId: String
  IpAddress: String
  SecurityGroups:
    - String
  SubnetId: String
```
