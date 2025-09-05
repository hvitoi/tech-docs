# Abstract Syntax Tree (AST)

- An AST (Abstract Syntax Tree) is a tree representation of the structure of source code.
  - `Abstract`: it doesn’t include every detail of the syntax (like parentheses, commas, or whitespace).
  - `Syntax Tree`: it represents the grammatical structure of code.

- It’s the data structure compilers, interpreters, and many tools use to reason about code.

```txt
2 + 3 * 4

      (+)
     /   \
   (2)   (*)
        /   \
      (3)   (4)
```
