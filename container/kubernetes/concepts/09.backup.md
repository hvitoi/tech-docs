# Backup

## Resources Config

- Resources config are stored in `etcd`
- Other solutions help automatizing the backup process (`Velero`)

```shell
# Store a backup of all resources
kubectl get "all" \
  --all-namespaces \
  -o "yaml" \
  > "all-resources.yaml"
```

## Etcd backup

- Etcd holds the database on the master node at the `/var/lib/etcd` (default)
- Etcd also comes with a built-in `snapshot` solution
- All the commands with the `etcdcli` must have the certificate parameters

```shell
ETCDCTL_api=3 etcdctl \
  snapshot save "snapshot.db" \
    --endpoints "https://127.0.0.1:2379" \
    --cacert "/etc/etcd/ca.crt" \
    --cert "/etc/etcd/etcd-server.crt"  \
    --key "/etc/etcd/etcd-server.key"
```

### Saving snapshot

```shell
# save snapshot
ETCDCTL_api=3 etcdctl \
  snapshot save "snapshot.db"

# status of snapshot
ETCDCTL_api=3 etcdctl \
  snapshot status "snapshot.db"
```

### Restoring snapshot

```shell
# stop kube-apiserver service
systemctl stop "kube-apiserver"

# restore snapshot
ETCDCTL_api=3 etcdctl \
  snapshot restore "snapshot.db" \
    --data-dir "/var/lib/etcd-from-backup"
```

- When etcd restore from a backup, it initializes a new cluster configuration
- That's why a new data directory is needed
- After the restore is performed, you must update the `etcd.service` or the volume mapping of the yaml in `/etc/kubernetes/manifests`

```conf
ExecStart=/usr/local/bin/etcd \\
  ... \\
  --data-dir=/var/lib/etcd-from-backup
```

```shell
# Restart etcd with the newer snapshot data
systemctl daemon-reload
systemctl restart etcd

# start back the kube-apiserver service
systemctl start kube-apiserver
```
