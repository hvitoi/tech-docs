import java.time.Duration;

class Main {
  public static void main(String[] args) {

    // Static methods
    DurationOfMillis.run();

  }
}

class DurationOfMillis {
  static void run() {
    // 5 seconds
    Duration duration = Duration.ofMillis(5000);
  }
}
