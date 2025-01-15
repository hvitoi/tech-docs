# clang

```shell
# Compiles into a binary "main.out"
clang++ main.cpp
```

## -o

- Output filename

```shell
clang \
  -o main.out \
  main.c # The source file to compile
```

## -g

- Generate source-level debug information
- This includes debugging symbols

```shell
clang \
  -g \
  main.c
```
