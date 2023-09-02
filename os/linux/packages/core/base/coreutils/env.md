# env

```shell
# List an environment variables
env

# run a command but set an env first
env MOZ_ENABLE_WAYLAND=1 firefox
```

## Env on scripts

- This will call `env`, which then goes through `PATH` to find a program called `bash`
- This makes it work regardless of where bash is installed

```bash
#!/usr/bin/env bash
echo hi
```
