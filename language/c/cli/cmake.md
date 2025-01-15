# cmake

- CMake configuration `CMakeLists.txt`
- Upon running `Cmake` a set of `Makefiles` are created in the `build directory`

```shell
mkdir build
cd build
cmake .. # build the previous dir (the project root) in the current dir (the build dir)
make # run the auto-generated make file
```

## -S

- Explicitly specify a source directory
- Usually the project's root

```shell
cmake -S "." -B "build"
cmake -B "build" # same, uses the current directory by default
```

## -B

- Explicitly specify a build directory.

```shell
cmake -S "." -B "build"
```

## -D

- Create or update a cmake cache entry

```shell
cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=1
```
