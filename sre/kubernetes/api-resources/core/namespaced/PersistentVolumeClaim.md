# PersistentVolumeClaim (pvc)

- It's the action of requesting a storage volume (so that it can be attached to a pod)
- The PVC can request a volume from
  - A preexisting **PV** that satisfies the matching criteria
  - A defined **SC**, so that it dynamically creates the PV under the hood

## PVC Phases

- `Pending`: no match to any PV or the SC has not created the PV yet (the case of WaitForFirstConsumer)
- `Bound`: bound to a PV

## Claim from PV

- It finds an existing PV that satisfies the claim
- If there are multiple matches for the claim, you can use labels to bind to the desired volume
- A small PVC will match to a big PV if it doesn't find a better option
- There is a `1 to 1 relationship between PV and PVC`
- PVC must exist in the same namespace of the pod

- **Matching Criteria**
  - Sufficient Capacity
  - Access Modes
  - Volume Modes
  - Storage Class
  - Selector

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  resources:
    requests:
      storage: 30Mi # it can match with bigger PVs
  accessModes:
    - ReadWriteOnce
```

## Claim from SC

- Define the storage volume provisioner (SC)
- This way, the PV is created automatically by the StorageClass

- `standard`: static provisioning
- `manual`: static provisioning
- `storage-class-name`: dynamic provisioning

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  storageClassName: ebs-sc
  resources:
    requests:
      storage: 2Gi
  accessModes:
    - ReadWriteOnce
```

## Properties

### spec.resources

- Represents the minimum resources the volume should have

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  resources:
    requests:
      storage: 30Mi
```

### spec.storageClassName

- Defines `dynamic provisioning` of volumes by means of an StorageClass (SC)
- When a VPC is created, a PV is then provisioned automatically on the cloud on the fly

```shell
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  storageClassName: ebs-sc
  resources:
    requests:
      storage: 4Gi
```

### spec.accessModes (bypass)

- Bypass to `pv.spec.accessModes`

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  resources:
    requests:
      storage: 30Mi
  accessModes:
    - ReadWriteOnce
```
