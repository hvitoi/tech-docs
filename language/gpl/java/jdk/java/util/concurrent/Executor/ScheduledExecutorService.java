import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

class Main {
  public static void main(String[] args) {
    var executor = Executors.newScheduledThreadPool(1);

    // Instance methods
    _schedule(executor);
    _scheduleAtFixedRate(executor);
    _shutdown(executor);
  }

  static void _schedule(ScheduledExecutorService executor) {
    // run after 2 seconds
    executor.schedule(
        () -> System.out.println("hey!"),
        2,
        TimeUnit.SECONDS);
  }

  static void _scheduleAtFixedRate(ScheduledExecutorService executor) {
    // cronjob
    // run the first task right await, and then every 5 seconds
    // if any task throws an exception, the future tasks are suppressed
    executor.scheduleAtFixedRate(
        () -> System.out.println("periodically!"),
        0,
        5,
        TimeUnit.SECONDS);
  }

  static void _shutdown(ScheduledExecutorService executor) {
    // the executor service must be closed otherwise it will hang
    // the shutdown hook finishes gracefully the ongoing tasks
    // when shutdown is called, it receives no more new tasks
  }

}
