import java.util.Optional;

class Main {
  public static void main(String[] args) {
    // Static methods
    SystemOutPrintln.run();
    SystemCurrentTimeMillis.run();
    SystemGetenv.run();
  }
}

class SystemOutPrintln {
  static void run() {
    // "out" is a static attribute
    // "println" is a non-static method
    System.out.println("Hello World!");

  }
}

class SystemCurrentTimeMillis {
  static void run() {
    // the difference, measured in milliseconds, between the current time and
    // midnight, January 1, 1970 UTC.
    Long msSinceEpoch = System.currentTimeMillis();

  }
}

class SystemGetenv {
  static void run() {
    System.getenv("JAVA_HOME"); // environment variable

    try {
      String ENV_VAR1 = Optional.ofNullable(System.getenv("ENV_VAR1")).orElseThrow(
          () -> new IllegalArgumentException("ENV_VAR1 is not set in the environment"));
    } catch (IllegalArgumentException e) {
    }

  }
}