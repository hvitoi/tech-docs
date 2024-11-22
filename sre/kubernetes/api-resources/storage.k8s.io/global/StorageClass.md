# StorageClass (sc)

- Storage Class (`SC`) **provisions volumes dynamically** (represented by a `PV`) whenever a `PVC` is created

- What is **Dynamic Provisioning**?
  - Automatically creates the storage needed (locally or on cloud providers)
  - Differently from `Static Provisioning` (with static PVs) where the storage must be in place beforehand
  - With `StorageClasses` a provisioner is defined (E.g., google storage) that automatically provisions storage
  - When claiming a storage (with PVC associated with a SC), the PV is created automatically

## Properties

### allowVolumeExpansion

- Expands the storage automatically

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: my-sc
provisioner: kubernetes.io/no-provisioner
allowVolumeExpansion: true
```

### volumeBindingMode

- **Immediate** (default)
  - SC creates a PV as soon as the PVC is created

- **WaitForFirstConsumer**
  - SC creates a PV as soon as the PVC is created AND the pod initializes
  - Before the pod initializes the PVC remains in `Pending` state
  - This way the PV is provisioned in the same region of the pod

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: my-sc
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
```

### spec.allowedTopologies

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: ebs-sc
provisioner: ebs.csi.aws.com
volumeBindingMode: WaitForFirstConsumer
parameters:
  csi.storage.k8s.io/fstype: xfs
  type: io1
  iopsPerGB: "50"
  encrypted: "true"
allowedTopologies:
  - matchLabelExpressions:
    - key: topology.kubernetes.io/zone
      values:
        - us-east-2c
```

### provisioner

#### kubernetes.io/no-provisioner

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: my-sc
provisioner: kubernetes.io/no-provisioner
```

#### kubernetes.io/gce-pd

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: my-sc
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-standard # pd-ssd
  replication-type: none # regional-pd
```

#### kubernetes.io/aws-ebs

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: my-sc
provisioner: kubernetes.io/aws-ebs
parameters:
  type: io1
  iopsPerGB: "10"
  fsType: ext4
```

#### kubernetes.io/azure-disk

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: managed
provisioner: kubernetes.io/azure-disk # Disk PV can only be attached to one pod at a time
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
parameters:
  kind: Managed # Shared (default), Managed, Dedicated
  storageaccounttype: StandardSSD_LRS # Premium_LRS, Standard_LRS
  cachingmode: ReadOnly
```

#### kubernetes.io/azure-file

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: azurefile # /usr/share/nginx/html to serve pages
provisioner: kubernetes.io/azure-file # File Shares can be attached to multiple pods at the same time
reclaimPolicy: Delete
volumeBindingMode: Immediate
allowVolumeExpansion: true
parameters:
  skuName: Standard_LRS
mountOptions:
  - dir_mode=0777
  - file_mode=0777
  - uid=0
  - gid=0
  - mfsymlinks
  - cache=strict
  - actimeo=30
```

#### ebs.csi.aws.com

- Requires the [EBS CSI Driver](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html) installed on the cluster
- By default when creating an EKS cluster only a `kubernetes.io/aws-ebs` storage class is created

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: ebs-sc
provisioner: ebs.csi.aws.com
volumeBindingMode: WaitForFirstConsumer
parameters:
  csi.storage.k8s.io/fstype: xfs
  type: io1
  iopsPerGB: "50"
  encrypted: "true"
  # fstype: ntfs # for windows
allowedTopologies:
  - matchLabelExpressions:
    - key: topology.kubernetes.io/zone
      values:
        - us-east-2c
```

### reclaimPolicy (bypass)

- Bypassed to `pv.spec.persistentVolumeReclaimPolicy`

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: my-sc
provisioner: kubernetes.io/no-provisioner
reclaimPolicy: Retain
```
