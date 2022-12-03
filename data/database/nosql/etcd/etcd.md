# etcd

- It's a highly available `key-value` `distributed` database
- Listens on port **2379**

## Install

```shell
wget "https://github.com/etcd-io/etcd/releases/download/v3.5.0/etcd-v3.5.0-linux-amd64.tar.gz"
tar -xzvf "etcd-v3.5.0-linux-amd64.tar.gz"
./etcd
```

## etcdctl v2

- Control client for etcd
- Version 2 is used by default unless v3 is specified

```shell
# set key-value
etcdctl set "key" "value"

# get key-value
etcdctl get "key"
```

```shell
etcdctl backup
etcdctl cluster-health
etcdctl mk
etcdctl mkdir
etcdctl set
```

## etcdctl v3

- Set etcdctl v3: `export ETCDCTL_API=3`

```shell
etcdctl snapshot save
etcdctl endpoint health
etcdctl get
etcdctl put
```

## Snapshots

```shell
# save snapshot
ETCDCTL_api=3 etcdctl \
  snapshot save "snapshot.db"

# status of snapshot
ETCDCTL_api=3 etcdctl \
  snapshot status "snapshot.db"

# restore snapshot
ETCDCTL_api=3 etcdctl \
  snapshot restore "snapshot.db" \
    --data-dir "/var/lib/etcd-from-backup"
```

- After the restore is performed, you must update the `etcd.service`

```conf
ExecStart=/usr/local/bin/etcd \\
  ... \\
  --data-dir=/var/lib/etcd-from-backup
```

```shell
# Restart etcd with the newer snapshot data
systemctl daemon-reload
systemctl restart etcd
```
