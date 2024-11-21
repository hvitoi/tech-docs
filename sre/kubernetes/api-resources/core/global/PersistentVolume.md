# PersistentVolume (pv)

- `Storage Requirements`
  - Storage does not depend on the pod lifecycle
  - Storage does not depend on a node (it must be available on all nodes, pods can restart and spawn in another node)
  - Storage must be independent from the cluster (it needs to survive even if the cluster crashes)

- A PV represents a space from the actual physical storage
  - E.g., Local Disk, NFS server, cloud storage
- The `PV` is an `interface` with the actual storage

- **Local Volumes** violates the 2nd and 3rd requirements for data persistence: it's tied to 1 node, does not survive in cluster crashes. It's bad for DB persistence.

## PV Phases

- PV phases are not affected by the pods/deployments. It is affected by PVCs
  - If a pod is deleted or recreated, the PV does not transition to other phase (it is independent from the pod lifecycle)

- **Available**
  - Not yet claimed by any PVC
- **Bound**
  - Claimed and bound to a PVC
- **Released**
  - Claimed by a PVC, but already released
  - Data still intact, but cannot be bound to any other PVC

## Properties

### spec.volumeMode

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

### spec.persistentVolumeReclaimPolicy

- **Delete** (default)
  - Cloud storage resource (and the PV) is deleted as soon as the PVC is deleted
- **Retain**
  - Cloud storage resource (and the PV) is kept when PVC is deleted
  - The PV cannot be reused by any other PVC
- **Recycle**
  - Cloud storage resource (and the PV) is kept when PVC is deleted
  - The PV can be reused by other PVCs

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

### spec.accessModes

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

### spec.nodeAffinity

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

### Storage Sources

#### spec.local

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

#### spec.hostPath

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

#### spec.nfs

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

#### spec.awsElasticBlockStore

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

#### spec.gcePersistentDisk

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
