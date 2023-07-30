# Rust

- No garbage collector (fast runtime)
- Memory safety

## Crate

- It's a package, a project, a library
- `main.rs` and `lib.rs` are the crates' root
- Each crate can have several modules (a file or a directory)

## Modules

- Each file in Rust (except main.rs and lib.rs) corresponds to one `module`
- A module can be a `file` or a `directory` containing a `mod.rs`
  - Modules are a directory allows submodules

## Expressions vs. Statements

- `Expression`
  - Evaluate to a value
  - Does not change state
  - Semicolon cannot be placed (otherwise the return is an empty unit)
- `Statement`
  - Perform actions, but do not return value
  - Does change state! E.g., assign variables
  - Semicolon is mandatory
