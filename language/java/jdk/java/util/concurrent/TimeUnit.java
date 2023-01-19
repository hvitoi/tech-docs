/*
 * TimeUnit class
 */

import java.util.concurrent.TimeUnit;

class Main {
  public static void main(String[] args) {
    _sleep.run();
  }
}

class _sleep {
  static void run() {
    try {
      TimeUnit.SECONDS.sleep(5);
    } catch (InterruptedException e) {
    }
  }
}
