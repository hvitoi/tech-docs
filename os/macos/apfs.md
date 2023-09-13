# Apple Filesystem

- Replaces `HFS+` (MacOS Extended)

## Chracteristics

- **Space sharing**

  - Volumes inside of a container share free space
  - However, `reserved` and `quota` sizes that also be defined

- **Cloning**

  - Cloning a file happens instantly and takes no additional space
  - This is possible due to `Copy-On-Write` (COW)
  - Only new changes are stored
  - That open possibilities for `Snapshots`
  - `Time Machine` is used to manage snapshots

- **Atomic safe-save**

  - Guarantees atomic save even for document bundles (documents that are actually folders with multiple files)

## Container Roles

- **Data**
  - Sealed: no
  - FileVault: yes
  - Encrypted: yes
  - Size: ~15 GB
- **System**
  - Sealed: yes
  - FileVault: yes
  - Encrypted: no
  - Size: ~9 GB
  - Snapshot is taken from it
- **Preboot**
  - Sealed: no
  - FileVault: no
  - Size: ~2 GB
- **VM**
  - Sealed: no
  - FileVault: no
  - Size: ~20 KB
- **Recovery**
  - Sealed: no
  - FileVault: no
  - Size: ~1 GB

## Recovery Keys

- `Personal Recovery Key` (PRK)
  - Alphanumeric string generated at the time of encryption
- `Institutional recovery key` (IRK)
  - Pre-made recovery key that can be installed on a system prior to encryption
