# C

## Compilers

- **GCC**: Unix/Linux/Mac
  - <https://gcc.gnu.org/>
- **MinGW**: Windows
  - <http://www.mingw.org/>
- **Clang**
  - Frontend for LLVM. Generates IR code

## Build System

- **CMake**
  - Build-generator tool
  - Generates the file needed by the build tool

```shell
brew install cmake
pacman -S cmake
```

## Language Server

- **clangd**
  - <https://clangd.llvm.org/>
  - It is based on the Clang C++ compiler, and is part of the LLVM project
  - Uses the configuration defined in the `.clangd` file
  - Installed in vscode via `llvm-vs-code-extensions.vscode-clangd` extension
- **ccls**
  - <https://github.com/MaskRay/ccls>

## Debugging

- **CodeLLDB**: A native debugger powered by LLDB
  - vscode extension: `vadimcn.vscode-lldb`
  - LLDB is available in clang
