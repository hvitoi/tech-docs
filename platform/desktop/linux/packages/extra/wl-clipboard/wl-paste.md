# wl-paste

- primary buffer: where middle click pastes from
- clipboard buffer: standard clipboard

```shell
# paste from clipboard buffer
wl-paste

# watches for changes in the primary buffer and clears it
wl-paste -p --watch wl-copy -p ''
```
