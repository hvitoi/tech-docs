import java.util.NoSuchElementException;
import java.util.Optional;

class Main {
  public static void main(String[] args) {
    // Static methods
    _empty(); // -> Optional
    _of(); // -> Optional
    _ofNullable(); // -> Optional

    // Instance methods
    _get(); // -> T
    _orElse(); // -> T
    _orElseGet(); // -> T
    _orElseThrow(); // -> T

    _isPresent(); // -> bool
    _isEmpty(); // -> bool
    _ifPresent(); // -> void

    _filter(); // -> Optional
    _map(); // -> Optional
  }

  static void _empty() {
    var opt = Optional.<String>empty();
  }

  static void _of() {
    var opt = Optional.of("henry");
    // var opt = Optional.of(null); // fails! Use ofNullable instead
  }

  static void _ofNullable() {
    var opt = Optional.ofNullable("henry");
    var opt2 = Optional.<String>ofNullable(null);
  }

  static void _get() {
    var opt = Optional.of("hey");
    try {
      var value = opt.get();
    } catch (NoSuchElementException e) {
      // throw when there is not value in the optional
      e.printStackTrace();
    }
  }

  static void _orElse() {
    // similar to .get() but sets a default value if none is found

    // Null or Empty
    var opt = Optional.<String>empty();
    var opt2 = Optional.<String>ofNullable(null);

    var name = opt.orElse("john");
  }

  static void _orElseGet() {
    // similar to .orElse() but receives an a supplier as argument to be used in
    // case the value is null/empty

    // Null or Empty
    var opt = Optional.<String>empty();
    var opt2 = Optional.<String>ofNullable(null);

    var name = opt.orElseGet(() -> "john");
  }

  static void _orElseThrow() {
    // Null or Empty
    var opt = Optional.<String>empty();
    var opt2 = Optional.<String>ofNullable(null);

    // throw error if the value is null/empty
    try {
      var name1 = opt.orElseThrow(); // throws NoSuchElementException by default
      var name2 = opt.orElseThrow(IllegalArgumentException::new);
    } catch (Exception e) {
    }
  }

  static void _isPresent() {
    var opt = Optional.empty();
    if (opt.isPresent()) { // false
    }
  }

  static void _isEmpty() {
    var opt = Optional.empty();
    if (opt.isEmpty()) { // true
    }
  }

  static void _ifPresent() {
    // Execute the lambda only if there is a value
    var msg1 = Optional.of("hey");
    var msg2 = Optional.empty();

    // Accepts a consumer (does not return any value)
    // msg1.ifPresent(s -> System.out.println(s.length()));
    msg2.ifPresent(System.out::println); // I won't run

  }

  static void _filter() {
    // returns the Optional unchanged if the predicate matches, otherwise returns an
    // empty Optional
    var opt = Optional
        .of(8)
        .filter(el -> el % 2 == 0);
  }

  static void _map() {
    // Apply the map only if a value is present
    Object obj = "Hey";
    var result = Optional.of(obj)
        .filter(String.class::isInstance) // verify if it's an instance of String
        .map(String.class::cast) // cast to string (redundant here)
        .map(s -> s + ", how are you doing?")
        .map(s -> s + " Great!");
  }
}
