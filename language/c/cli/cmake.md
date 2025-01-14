# cmake

- Generate the file `compile_commands.json`
- By default clang tries to read this file from the root of the project
  - Or manually set it with the flag `--compile-commands-dir=build/debug`

```shell
# Generate the build file into "build/debug" folder
cmake -H. -B "build/debug" -DCMAKE_EXPORT_COMPILE_COMMANDS=1
```
