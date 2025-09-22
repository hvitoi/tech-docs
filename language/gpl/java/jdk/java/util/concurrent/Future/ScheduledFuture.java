/*
 * ScheduledFuture class
 */

import java.util.concurrent.ExecutionException;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

class Main {
  public static void main(String[] args) {
    var scheduledFuture = Init.run();

    // Instance methods
    _get(scheduledFuture);
    _getDelay(scheduledFuture);
  }

  static void _get(ScheduledFuture<String> scheduledFuture) {
    try {
      scheduledFuture.get();
    } catch (InterruptedException | ExecutionException e) {
    }
  }

  static void _getDelay(ScheduledFuture<String> scheduledFuture) {
    // how many seconds until it is executed
    scheduledFuture.getDelay(TimeUnit.MILLISECONDS);
  }

}

class Init {
  static ScheduledFuture<String> run() {
    var service = Executors.newScheduledThreadPool(1);
    var scheduledFuture = service.schedule(() -> "hey", 2, TimeUnit.SECONDS);
    service.shutdown();
    return scheduledFuture;
  }
}
