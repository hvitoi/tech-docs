import java.util.NoSuchElementException;
import java.util.Optional;

class Main {
  public static void main(String[] args) {
    // Static methods
    _empty();
    _of();
    _ofNullable();

    // Instance methods
    _isPresent();
    _isEmpty();
    _ifPresent();
    _orElse();
    _orElseGet();
    _orElseThrow();
    _get();
    _filter();
    _map();

  }

  static void _empty() {
    var opt = Optional.empty(); // opt.isPresent() == false
  }

  static void _of() {
    var opt = Optional.of("henry"); // opt.isPresent() == true
  }

  static void _ofNullable() {
    var opt = Optional.ofNullable("henry");
    var opt2 = Optional.ofNullable(null);
  }

  static void _isPresent() {
    var opt = Optional.empty();
    if (opt.isPresent()) {
      // do something ..
    }
  }

  static void _isEmpty() {
    var opt = Optional.empty();
    if (opt.isEmpty()) {
      // do something ..
    }
  }

  static void _ifPresent() {
    // Execute the lambda only if there is a value
    var msg1 = Optional.of("Hey!");
    var msg2 = Optional.empty();

    // msg1.ifPresent(s -> System.out.println(s.length()));
    msg2.ifPresent(System.out::println); // I won't run

  }

  static void _orElse() {
    Optional<String> opt = Optional.ofNullable(null);
    String name = opt.orElse("john"); // similar to .get() but sets a default value if none is found
  }

  static void _orElseGet() {
    Optional<String> opt = Optional.ofNullable(null);
    String name = opt.orElseGet(() -> "john"); // similar to .orElse() but receives an expression as argument
  }

  static void _orElseThrow() {
    Optional<String> opt = Optional.ofNullable(null);

    try {
      String name = opt.orElseThrow(IllegalArgumentException::new); // throw error if null is found
      String name2 = opt.orElseThrow(); // throws NoSuchElementException if empty Optional is found (java 10+)
    } catch (Exception e) {
    }
  }

  static void _get() {
    Optional<String> opt = Optional.of("henry");

    try {
      String name = opt.get();
    } catch (NoSuchElementException e) {
    }
  }

  static void _filter() {
    String str = "hi";

    // empty string will also be considered as Empty Optional
    Optional<String> opt = Optional.ofNullable(str).filter(s -> !s.isEmpty());
  }

  static void _map() {
    String str = Optional.ofNullable("hi")
        .filter(String.class::isInstance) // verify if it's an instance of String
        .map(String.class::cast) // cast to string (redundant here)
        .map(s -> s + ", how are you doing?")
        .map(s -> s + " Great!")
        .orElse("default message");
  }
}
