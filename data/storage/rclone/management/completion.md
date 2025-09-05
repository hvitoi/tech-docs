# completion

- Generate auto-complete for a given shell

```shell
# Write auto-complete script to stdout
# This needs to be sourced by the shell
rclone completion fish -
```

```fish
# rclone.fish
if command -q rclone
    eval $(rclone completion fish -)
end
```
