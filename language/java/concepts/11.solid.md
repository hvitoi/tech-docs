# SOLID

- **Cohesion**

  - Every class should have only one responsibility
  - The class separate concerns so that you don't have to modify it often
  - It doesn't grow forever
  - Classes are small and limited scope

- **Decoupling**

  - Changes to classes do not affect the main class
  - To decouple, always code to `interfaces`!
  - Interfaces are stable
  - `Efferent coupling`: shows who a given class depends on
  - `Afferent coupling`: shows who depends on a given class

- **Encapsulation**
  - Hide the behavior inside of a class. It's `abstraction`!
  - `Unappropriated intimacy` is when a class knows a lot about another class
  - `Tell, Don't Ask`
  - What the method does? Must be explicit in its name
  - How is does it? You should not know! It must be hidden (encapsulated)
  - A DAO is a good example of encapsulated class
  - Well encapsulated classes do not propagate changes
  - `Demeter Law`: avoid chaining methods
    - bad: fature.getCliente().marcaComoInadimplente();
    - good: fature.marcaClienteComoInadimplente(); (encapsulated)

## Single Responsability Principle (SRP)

- "There should never be more than one reason for a class to change."
- It's basically `cohesion`

## Open–closed Principle (OCP)

- "Software entities ... should be `open for extension`, but `closed for modification`."
- The behavior of the class is changed based on the a polymorphic parameter you pass on the constructor. This way the class code remains untouched
- The parameter passed on the constructor must have an interface
- That's `decoupling`, because the changes do not affect the main class

## Liskov Substitution principle (LSP)

- "Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it."
- `Design by contract`
- The child class cannot narrow the conditions of the parent class
  - It can extend, but never narrow
- Favor `Composition` over `Inheritance`

## Interface Segregation principle

- "Many client-specific interfaces are better than one general-purpose interface."

## Dependency Inversion principle (DIP)

- "Depend upon `abstractions`, [not] concretions."
- A class must depend always on a more stable class
- Try to depend always on abstraction
- Programing OO is thinking always about abstraction
