# Apple Filesystem

- Replaces `HFS+` (MacOS Extended)

## Space sharing

- Volumes inside of a container share free space
- However, `reserved` and `quota` sizes that also be defined

## Cloning

- Cloning a file happens instantly and takes no additional space
- This is possible due to `Copy-On-Write` (COW)
- Only new changes are stored
- That open possibilities for `Snapshots`
- `Time Machine` is used to manage snapshots

## Atomic safe-save

- Guarantees atomic save even for document bundles (documents that are actually folders with multiple files)
