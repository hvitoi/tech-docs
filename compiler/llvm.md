# LLVM (Low Level Virtual Machine)

- LLVM is a set of `compiler` and `toolchain technologies`
- Allows creating `frontends` for any programming language
- Allows creating `backends` for any instruction set architecture
- It is designed around a language independent `Intermediate Representation (IR)`

## Steps

- `Frontend`

  1. Source Code
  1. Lexical Analysis (AST)
  1. IR Code

- `Middle`

  1. IR code optimization

- `Backend`\*

  1. IR code
  1. Machine code

## Bulding LLVM

### Lexer

- Scans the source code and breaks into a collection of tokens
- **Tokens**
  - `Identifier`: x, color, UP
  - `Keyword`: if, while, return
  - `Separator`: }, (, ;
  - `Operator`: +, <, =
  - `Literal`: true, 6.02e23, "music"

### AST (Abstract Syntax Tree)

- Tree to represent to `structure of the code` and the `relation between the tokens`

### Parser

- Builds the AST

### IR

- Generates the `intermediate representation` code
