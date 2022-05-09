import java.util.NoSuchElementException;
import java.util.Optional;

class Main {
  public static void main(String[] args) {
    // Static methods
    OptionalEmpty.run();
    OptionalOf.run();
    OptionalOfNullable.run();

    // Instance methods
    OptionalIsPresent.run();
    OptionalIsEmpty.run();
    OptionalIfPresent.run();
    OptionalOrElse.run();
    OptionalOrElseGet.run();
    OptionalOrElseThrow.run();
    OptionalGet.run();
    OptionalFilter.run();
    OptionalMap.run();
  }
}

class OptionalEmpty {
  static void run() {
    Optional<String> opt = Optional.empty(); // opt.isPresent() == false
  }
}

class OptionalOf {
  static void run() {
    Optional<String> opt = Optional.of("henry"); // opt.isPresent() == true
  }
}

class OptionalOfNullable {
  static void run() {
    Optional<String> opt = Optional.ofNullable("henry");
    Optional<String> opt2 = Optional.ofNullable(null);
  }
}

class OptionalIsPresent {
  static void run() {
    Optional<String> opt = Optional.empty();
    if (opt.isPresent()) {
      // do something ..
    }
  }
}

class OptionalIsEmpty {
  static void run() {
    Optional<String> opt = Optional.empty();
    if (opt.isEmpty()) {
      // do something ..
    }
  }
}

class OptionalIfPresent {
  static void run() {
    Optional<String> opt = Optional.empty();
    opt.ifPresent(name -> System.out.println(name.length()));
  }
}

class OptionalOrElse {
  static void run() {
    Optional<String> opt = Optional.ofNullable(null);
    String name = opt.orElse("john"); // similar to .get() but sets a default value if none is found
  }
}

class OptionalOrElseGet {
  static void run() {
    Optional<String> opt = Optional.ofNullable(null);
    String name = opt.orElseGet(() -> "john"); // similar to .orElse() but receives an expression as argument
  }
}

class OptionalOrElseThrow {
  static void run() {
    Optional<String> opt = Optional.ofNullable(null);

    try {
      String name = opt.orElseThrow(IllegalArgumentException::new); // throw error if null is found
      String name2 = opt.orElseThrow(); // throws NoSuchElementException if empty Optional is found (java 10+)
    } catch (Exception e) {
    }
  }
}

class OptionalGet {
  static void run() {
    Optional<String> opt = Optional.of("henry");

    try {
      String name = opt.get();
    } catch (NoSuchElementException e) {
    }
  }

}

class OptionalFilter {
  static void run() {
    String str = "hi";

    // empty string will also be considered as Empty Optional
    Optional<String> opt = Optional.ofNullable(str).filter(s -> !s.isEmpty());
  }
}

class OptionalMap {
  static void run() {
    String str = Optional.ofNullable("hi")
        .filter(String.class::isInstance) // verify if it's an instance of String
        .map(String.class::cast) // cast to string (redundant here)
        .map(s -> s + ", how are you doing?")
        .map(s -> s + " Great!")
        .orElse("default message");
  }

}