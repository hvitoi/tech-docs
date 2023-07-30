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

## Scopes

- Range within an item (e.g., variable) is valid
- `Global Scope`: accessible throughout the entire program
- `Local Scope`: accessible only within a function or block

## Memory Allocation

- `Stack Memory`
  - LIFO
  - Must have known and fixed size
  - It's faster than allocating to heap, because the new data is always on the top (constant time access)

```rust
fn main() {
  let x = 42;
  let y = 10;
  let z = add_numbers(x, y);
}

fn add_numbers(a: i32, b: i32) -> i32 {
  let c = a + b;
  c
}
// Stack level 0 (main): x, y, z
// Stack level 1 (add_numbers): a, b, c
```

- `Heap Memory`

  - Allocate types with unknown sizes (e.g., arrays, strings)
  - Allocating and accessing is slower (using pointers)
  - The pointer to the value, however, is still pushed to the stack (pointer is fixed size)

## Ownership

- `Owner` of a value
  - It's the variable or data structure that holds it
  - It's responsible for allocating and freeing the memory used to store that data
- **Rules**
  1. Each value has an `owner`
  1. There can be `only one owner` at a time
  1. When the owner goes out of scope, the value is dropped

```rust
{
  let s = "hello"; // s is alloc'ed

}
// s is freed
```

- **Ownership drop**
  - Values within `stack memory` are always copied (the value itself or the pointer)
  - When we are talking about dynamic size values (e.g., arrays), only the pointer is copied, however the actual value in the heap is the same. When that happens,
  - When a pointer is copied, the first pointer `ownership is dropped`, because there can't be 2 owners at the same time

```rust
// Copy
let x = 5;
let y = x; // x and y are independent, no ownership is dropped

// Move
let s1 = String::from("hello");
let s2 = s1; // s1 ownership is dropped (s1 is dropped)
let s3 = s2.clone(); // force copy (both ownerships are kept)
```

- **Ownership guarantees**
  - Prevents `dangling pointers`
  - Prevents `double-free` (trying to free a memory that has already been freed)
  - Prevents `memory leaks` (not freeing memory that should have been freed)
