# Access modifiers

- Define how `classes`, `variables` and `methods` can be accessed from other parts of the program

1. `protected`: visible to classes in the same package + children classes
1. `public`: visible to classes in all packages

public > protected > package-private > private

## Classes

### public

- Accessible from `anywhere`
- The filename must follow the same class name
- Allowed for top-level classes

```java
public class MyClass {
  }
```

### protected

- Accessible within the `same package` or `different packages when it's a subclass`

```java
public class Outer {
  protected class Inner {
  }
}
```

### package-private (default)

- Accessible within the `same package`
- Allowed for top-level classes

```java
class MyClass {
}
```

### private

- Accessible within the `same class`

```java
public class Outer {
  private class Inner {
  }
}
```
