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

    /**
     * Instance
     */
    _get.run(scheduledFuture);
    _getDelay.run(scheduledFuture);
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

class _get {
  static void run(ScheduledFuture<String> scheduledFuture) {
    try {
      scheduledFuture.get();
    } catch (InterruptedException | ExecutionException e) {
    }
  }
}

class _getDelay {
  static void run(ScheduledFuture<String> scheduledFuture) {
    // how many seconds until it is executed
    scheduledFuture.getDelay(TimeUnit.MILLISECONDS);
  }
}
