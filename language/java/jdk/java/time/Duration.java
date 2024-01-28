import java.time.Duration;

class Main {
  public static void main(String[] args) {

    // Static methods
    _ofMillis();
    _ofSeconds();

  }

  static void _ofMillis() {
    // 5 seconds
    Duration duration = Duration.ofMillis(5000);
  }

  static void _ofSeconds() {
    Duration duration = Duration.ofSeconds(5.1);
  }
}
