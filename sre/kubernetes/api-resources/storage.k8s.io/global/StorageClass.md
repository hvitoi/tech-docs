# Storageclass (sc)

- `Storage Class` provisions volumes dynamically when a PVC claims it

- **Dynamic Provisioning**

  - Automatically creates the storage needed (locally or on cloud providers)
  - Differently from `Static Provisioning` where the storage must be in place beforehand
  - With `StorageClasses` a provisioner is defined (E.g., google storage) that automatically provisions storage
  - When claiming a storage (with PVC associated with a SC), the PV is created automatically

- **Reclaim Policy**

  - `Retain` (default): Cloud storage resource is kept when pvc is deleted
  - `Delete`: Cloud storage resource is deleted when pvc is deleted
  - `Recycle`: Cloud storage resource can be reused by other pvcs

- **Volume Binding Mode**

  - `Immediate` (default): SC creates a PV after PVC is created
  - `WaitForFirstConsumer`: SC creates a PV after PVC is created AND the pod initializes. Until then the PVC remains in Pending state. This way the PV is provisioned in the same region of the pod

- **Allow Volume Expansion**
  - ... expands the storage automatically

## Local

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: storage-class-name
provisioner: kubernetes.io/no-provisioner
reclaimPolicy: Retain
volumeBindingMode: WaitForFirstConsumer
```

## GCP

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: storage-class-name
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-standard # pd-ssd
  replication-type: none # regional-pd
```

## AWS

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: storage-class-name
provisioner: kubernetes.io/aws-ebs
parameters:
  type: io1
  iopsPerGB: "10"
  fsType: ext4
```

## Azure

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
