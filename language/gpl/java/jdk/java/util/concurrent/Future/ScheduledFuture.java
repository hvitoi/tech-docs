import java.util.concurrent.ExecutionException;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

class Main {
  public static void main(String[] args) {
    var scheduledFuture = Executors
        .newScheduledThreadPool(1)
        .schedule(() -> "hey", 2, TimeUnit.SECONDS);

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
