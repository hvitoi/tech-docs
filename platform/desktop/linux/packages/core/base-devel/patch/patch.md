# patch

- Given that `changes.diff` is created with from `file1.txt` to `file2.txt`
- `Hunk` is a modification

```shell
# Modify file1.txt with the changes
patch < changes.diff

# Revert a patch applied
patch -R < changes.diff

patch -Np1 <$t2_patch
```

## Rejects

- If a file fails to be patched (conflicts), it is created a `.rej` (with the lines failed to patch) and a `.orig` with the original file before the partial changes
- Some hunks can still be patched successfully, in this case a file will be partially patched
