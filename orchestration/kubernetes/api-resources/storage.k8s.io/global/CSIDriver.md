# CSIDriver (csidrivers)

```yaml
apiVersion: storage.k8s.io/v1
kind: CSIDriver
metadata:
  name: ebs.csi.aws.com
spec:
  fsGroupPolicy: ReadWriteOnceWithFSType
  volumeLifecycleModes:
    - Persistent
  attachRequired: true
  podInfoOnMount: false
  requiresRepublish: false
  seLinuxMount: false
  storageCapacity: false
```
