import java.util.Optional;
import java.util.Properties;

class Main {
  public static void main(String[] args) {
    // Static methods
    _println();
    _currentTimeMillis();
    _getenv();
    _getProperties();
  }

  static void _println() {
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
    System.getenv("JAVA_HOME"); // environment variable

    try {
      String ENV_VAR1 = Optional.ofNullable(System.getenv("ENV_VAR1")).orElseThrow(
          () -> new IllegalArgumentException("ENV_VAR1 is not set in the environment"));
    } catch (IllegalArgumentException e) {
    }

  }

  static void _getProperties() {
    // Get JVM properties

    var properties = System.getProperties();

    System.out.println(properties);

  }
}
