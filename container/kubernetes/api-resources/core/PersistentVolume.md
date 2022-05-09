# Persistent Volume

- `Storage Requirements`
  - Storage doesn't depend on the pod lifecycle
  - Storage must be available on all nodes! (the pod can restarted and be scheduled to another node)
  - Storage needs to survive even if the cluster crashes
- It takes a space from the actual physical storage
  - E.g., Local Disk, NFS server, cloud storage
- The `PV` is an `interface` with the actual storage
- Persistent Volumes are not namespaced

- **Local Volumes**
  - Violates the 2nd and 3rd requirements for data persistence: it's tied to 1 node, does not survive in cluster crashes
  - For DB persistence, it's not recommended to use local Volume!
- **Remote Volumes**
  - Remote storage server

## PV phases

- `Available`: not yet bound to any PVC
- `Bound`: bound to a PVC
- `Released`: data still intact, but cannot be bound to any other PVC.

## Access Modes

- `ReadOnlyMany`: multiple nodes can read-only the volume
- `ReadWriteOnce`: can read and write by only one node
- `ReadWriteMany`: multiple nodes can read and write to the volume

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-name
spec:
  capacity:
    storage: 50Mi
  accessModes:
    - ReadOnlyMany
    - ReadWriteOnce
    - ReadWriteMany
  hostPath:
    path: /tmp/data
```

## PV Reclaim Policy

- `Retain` (default): PV cannot be reused by any other PVC. It will remain until manually deleted
- `Delete`: Delete automatically as soon as the claim is deleted
- `Recycle`: Data will be scrubbed before making it available to other PVC

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-name
spec:
  capacity:
    storage: 50Mi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /tmp/data
  persistentVolumeReclaimPolicy: Retain
```

## Volume Mode

- `Filesystem` (default)

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-name
spec:
  capacity:
    storage: 50Mi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /tmp/data
  volumeMode: Filesystem
```

## Node Affinity

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-name
spec:
  capacity:
    storage: 50Mi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /tmp/data
  nodeAffinity:
    required:
      nodeSelectorTerms:
        - matchExpressions:
            - key: kubernetes.io/hostname
              operator: In
              values:
                - node01
```

## Storage Sources

### local

- Local storage devices mounted on nodes.

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-name
spec:
  capacity:
    storage: 100Gi
  accessModes:
    - ReadWriteOnce
  local:
    path: /mnt/disks/sdd1
  #storageClassName: local-storage
```

### hostPath

- Take a slice of the host HDD and make it a PV
- For single node testing only; will not work in a multi-node cluster (consider using local volume instead)

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-name
spec:
  capacity:
    storage: 50Mi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /tmp/data # path in the host machine
```

### nfs

- Network File System (NFS) storage

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-name
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  nfs: # nfs parameters
    path: /dir/path/on/nfs/server
    server: nfs-server-ip-address
  mountOptions:
    - hard
    - nfsvers=4.0
  #storageClassName: slow
```

### awsElasticBlockStore

- AWS Elastic Block Store (EBS)

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-name
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  awsElasticBlockStore:
    volumeID: <volume-id>
    fsType: ext4
```

### gcePersistentDisk

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-name
  labels:
    failure-domain.beta.kubernetes.io/zone: us-central1-a__us-central1-b
spec:
  capacity:
    storage: 400Gi
  accessModes:
    - ReadWriteOnce
  gcePersistentDisk:
    pdName: my-data-disk
    fsType: ext4
```
