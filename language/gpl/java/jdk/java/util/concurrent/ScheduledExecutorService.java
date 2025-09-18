/*
 * ScheduledExecutorService class
 */

import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

class Main {
  public static void main(String[] args) {
    var service = Executors.newScheduledThreadPool(1);

    // Instance methods
    _schedule(service);
    _scheduleAtFixedRate(service);
    _shutdown(service);
  }

  static void _schedule(ScheduledExecutorService service) {
    // run after 2 seconds
    service.schedule(
        () -> System.out.println("hey!"),
        2,
        TimeUnit.SECONDS);
  }

  static void _scheduleAtFixedRate(ScheduledExecutorService service) {
    // cronjob
    // run the first task right await, and then every 5 seconds
    // if any task throws an exception, the future tasks are suppressed
    service.scheduleAtFixedRate(
        () -> System.out.println("periodically!"),
        0,
        5,
        TimeUnit.SECONDS);
  }

  static void _shutdown(ScheduledExecutorService service) {
    // the executor service must be closed otherwise it will hang
    // the shutdown hook finishes gracefully the ongoing tasks
    // when shutdown is called, it receives no more new tasks
    service.shutdown();
  }

}
