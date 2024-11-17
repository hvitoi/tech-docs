# PersistentVolumeClaim (pvc)

- It's the action of `finding a PV that satifies the claim` and `use it`
- If there are multiple matches for the claim, you can use labels to bind to the desired volume
- A small PVC will match to a big PV if it doesn't find a better option
- There is a `1 to 1 relationship between PV and PVC`
- PVC must exist in the same namespace of the pod

## Matching Criteria

- Sufficient Capacity
- Access Modes
- Volume Modes
- Storage Class
- Selector

## PVC States

- `Pending`: no match to any PV
- `Bound`: bound to a PV

## Claim from PV

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myclaim
  namespace: default
spec:
  resources:
    requests:
      storage: 30Mi # it can match with bigger PVs
  accessModes:
    - ReadWriteOnce
```

## Claim from SC

- Assign a storage provisioner to the volume claim
- This way, the PV is created automatically by the StorageClass

- `standard`: static provisioning
- `manual`: static provisioning
- `storage-class-name`: dynamic provisioning

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-name
spec:
  resources:
    requests:
      storage: 2Gi
  accessModes:
    - ReadWriteOnce
  storageClassName: google-storage
```
