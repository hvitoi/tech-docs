import java.io.PrintStream;
import java.util.Optional;
import java.util.Properties;

class Main {
  public static void main(String[] args) {
    // Static methods
    _out();
    _currentTimeMillis();
    _getenv();
    _getProperties();
  }

  static void _out() {
    // Returns the "stdout" PrintStream
    PrintStream stdout = System.out;
    stdout.println("");
  }

  static void _currentTimeMillis() {
    // the difference, measured in milliseconds, between the current time and
    // midnight, January 1, 1970 UTC.
    Long msSinceEpoch = System.currentTimeMillis();
  }

  static void _getenv() {
    String envHome = System.getenv("HOME"); // environment variable

    try {
      String foo = Optional
          .ofNullable(System.getenv("HOME"))
          .orElseThrow(() -> new IllegalArgumentException("This env is not set"));
    } catch (IllegalArgumentException e) {
      e.printStackTrace();
    }
  }

  static void _getProperties() {
    // Get JVM properties
    Properties properties = System.getProperties();
  }
}
