/*
 * TimeUnit class
 */

import java.util.concurrent.TimeUnit;

class Main {
  public static void main(String[] args) {
    /*
     * Static
     */
    Init.run();

    /*
     * Instance
     */
    _sleep.run();
  }
}

class Init {
  static void run() {
    var seconds = TimeUnit.SECONDS;
    var days = TimeUnit.DAYS;
  }
}

class _sleep {
  static void run() {
    try {
      var timeUnit = TimeUnit.SECONDS;
      timeUnit.sleep(5);
    } catch (InterruptedException e) {
    }
  }
}
