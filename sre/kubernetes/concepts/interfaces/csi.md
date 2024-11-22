# Container Storage Interface (CSI)

- CNI allows multiple storage solutions be compatible with Kubernetes
- Allows any container orchestration tool to work with any storage vendor with supported plugin
- It defines a set of RPCs called by the container orchestrator and must be implemented by the storage drivers

- `CreateVolume`: Call (provision new volume) -> Should (provision new volume on the storage)
- `DeleteVolume`: Call (delete volume) -> Should (decommission a volume)
- `ControllerPublishVolume`: Call (place workload that uses volume onto a node) -> Should (make volume available on a node)

## CSI Snapshotter

- <https://github.com/kubernetes-csi/external-snapshotter>
- The `CSI snapshotter` is part of Kubernetes implementation of `Container Storage Interface` (CSI) and implements both the `volume snapshot` and the `volume group snapshot` feature.

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: csi-aws-vsc
driver: ebs.csi.aws.com
deletionPolicy: Delete
```

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: ebs-volume-snapshot
spec:
  volumeSnapshotClassName: csi-aws-vsc
  source:
    persistentVolumeClaimName: ebs-claim
```

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: ebs-snapshot-restored-claim
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: ebs-sc
  resources:
    requests:
      storage: 4Gi
  dataSource:
    name: ebs-volume-snapshot
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
```
