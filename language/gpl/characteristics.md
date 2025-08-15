# Programming language paradigms

## Interpreted

- The core functionalities are usually shells over C libraries

- Examples
  - Python
  - Ruby
  - Javascript
  - PHP

## Compiled

- The core functionalities are written using its own language

- Examples
  - C
  - C++
  - Rust
  - Java
  - Go

## Procedural

- List of instructions to be executed
- C, Unix shell

## Declarative

- Describe the problem to be solved
- The underlying engine will decide what procedures are going to be run according to what you declared
- SQL

## Object-oriented

- Objects that have internal state
- Provide methods that query or modify this internal state
- Java, Smalltalk (mandatory)
- C++, Python (optional)

## Functional

- Decompose problems into a set of functions
- `Deterministic`: same inputs equal to same inputs always
- `Side effects`: action that modifies the internal state (e.g., change object) or any external state (e.g., write to database)
- `Pure function`: deterministic & no side effects
- Pure functions are encouraged in functional programming
