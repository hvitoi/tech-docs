import java.util.concurrent.TimeUnit;

class Main {
  public static void main(String[] args) {
    // Static fields
    _SECONDS();
    _DAYS();

    // Instance methods
    _sleep();
  }

  static void _SECONDS() {
    var seconds = TimeUnit.SECONDS;
  }

  static void _DAYS() {
    var days = TimeUnit.DAYS;
  }

  static void _sleep() {
    try {
      var timeUnit = TimeUnit.SECONDS;
      timeUnit.sleep(5);
    } catch (InterruptedException e) {
    }
  }
}
