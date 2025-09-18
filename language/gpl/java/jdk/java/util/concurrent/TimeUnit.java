/*
 * TimeUnit class
 */

import java.util.concurrent.TimeUnit;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _sleep();
  }

  static void _new() {
    var seconds = TimeUnit.SECONDS;
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
