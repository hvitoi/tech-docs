# env

- Takes a command name as argument and will run the first executable by that name it finds in the directories listed in the environment variable `$PATH`

```shell
env

# run command with additional environment variables
env MOZ_ENABLE_WAYLAND=1 firefox
```

## Env on scripts

- This will call `env`, which then goes through `PATH` to find a program called `bash`
- This makes it work regardless of where bash is installed

```bash
#!/usr/bin/env bash
echo hi
```
