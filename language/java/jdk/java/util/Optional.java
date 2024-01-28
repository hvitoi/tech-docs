import java.util.NoSuchElementException;
import java.util.Optional;

class Main {
  public static void main(String[] args) {
    // Static methods
    empty();
    of();
    ofNullable();

    // Instance methods
    isPresent();
    isEmpty();
    ifPresent();
    orElse();
    orElseGet();
    orElseThrow();
    get();
    filter();
    map();

  }

  static void empty() {
    Optional<String> opt = Optional.empty(); // opt.isPresent() == false
  }

  static void of() {
    Optional<String> opt = Optional.of("henry"); // opt.isPresent() == true
  }

  static void ofNullable() {
    Optional<String> opt = Optional.ofNullable("henry");
    Optional<String> opt2 = Optional.ofNullable(null);
  }

  static void isPresent() {
    Optional<String> opt = Optional.empty();
    if (opt.isPresent()) {
      // do something ..
    }
  }

  static void isEmpty() {
    Optional<String> opt = Optional.empty();
    if (opt.isEmpty()) {
      // do something ..
    }
  }

  static void ifPresent() {
    Optional<String> opt = Optional.empty();
    opt.ifPresent(name -> System.out.println(name.length()));
  }

  static void orElse() {
    Optional<String> opt = Optional.ofNullable(null);
    String name = opt.orElse("john"); // similar to .get() but sets a default value if none is found
  }

  static void orElseGet() {
    Optional<String> opt = Optional.ofNullable(null);
    String name = opt.orElseGet(() -> "john"); // similar to .orElse() but receives an expression as argument
  }

  static void orElseThrow() {
    Optional<String> opt = Optional.ofNullable(null);

    try {
      String name = opt.orElseThrow(IllegalArgumentException::new); // throw error if null is found
      String name2 = opt.orElseThrow(); // throws NoSuchElementException if empty Optional is found (java 10+)
    } catch (Exception e) {
    }
  }

  static void get() {
    Optional<String> opt = Optional.of("henry");

    try {
      String name = opt.get();
    } catch (NoSuchElementException e) {
    }
  }

  static void filter() {
    String str = "hi";

    // empty string will also be considered as Empty Optional
    Optional<String> opt = Optional.ofNullable(str).filter(s -> !s.isEmpty());
  }

  static void map() {
    String str = Optional.ofNullable("hi")
        .filter(String.class::isInstance) // verify if it's an instance of String
        .map(String.class::cast) // cast to string (redundant here)
        .map(s -> s + ", how are you doing?")
        .map(s -> s + " Great!")
        .orElse("default message");
  }
}
