# Pass By Reference vs. Pass By Value

- In C++ you can have a function with the following signature

```c++
void printList(list<int> &theList) {
  ...
}
```

This means that the variables theList is `passed by reference`, and it can be directly manipulated in memory.
If `&` in not specified it is instead treated as `pass by value`, in which the whole object is copied.

## Reference vs. Pointer

| Feature            | Reference Version                                | Pointer Version                                       |
| -                  | -                                                | -                                                     |
| How it’s passed    | By reference (alias to the original object).     | By pointer (memory address of the object).            |
| Syntax in function | Use the argument directly.                       | Must dereference *arg to access the object.           |
| Memory Safety      | Cannot be null (references are always valid).    | Can be null (requires explicit null-checks).          |
| Reassignment       | Cannot reassign the reference to another object. | Pointer can be reassigned to point to another object. |
| Performance        | No overhead of copying or dereferencing.         | Small overhead due to dereferencing.                  |

## Usage

- Reference operator is not available in C. It's a feature of C++
- C was designed to be simpler and more minimalistic, and references as an abstraction over pointers were introduced later in C++ for better syntax and safer memory handling.
- C relies on pointers for indirect referencing and memory manipulation.

```c++
int x = 10;

int &ref = x;   // ref is a reference to x
int *ptr = &x;  // ptr now holds the address of x
```
