import java.util.Optional;
import java.util.Properties;

class Main {
  public static void main(String[] args) {
    // Static methods
    _out_println();
    _currentTimeMillis();
    _getenv();
    _getProperties();
  }

  static void _out_println() {
    // "out" is a static attribute
    // "println" is a non-static method
    System.out.println("Hello World!");
  }

  static void _currentTimeMillis() {
    // the difference, measured in milliseconds, between the current time and
    // midnight, January 1, 1970 UTC.
    Long msSinceEpoch = System.currentTimeMillis();
  }

  static void _getenv() {
    System.getenv("HOME"); // environment variable

    try {
      String foo = Optional.ofNullable(System.getenv("FOO")).orElseThrow(
          () -> new IllegalArgumentException("FOO is not set in the environment"));
    } catch (IllegalArgumentException e) {
    }

  }

  static void _getProperties() {
    // Get JVM properties
    Properties properties = System.getProperties();
  }
}
