/*
 * ScheduledExecutorService class
 */

import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

class Main {
  public static void main(String[] args) {
    var service = Init.run();

    /**
     * Instance
     */
    _schedule.run(service);
    _scheduleAtFixedRate.run(service);
    _shutdown.run(service);
  }

}

class Init {
  static ScheduledExecutorService run() {
    return Executors.newScheduledThreadPool(1);
  }
}

class _schedule {
  static void run(ScheduledExecutorService service) {
    // run after 2 seconds
    service.schedule(
        () -> System.out.println("hey!"),
        2,
        TimeUnit.SECONDS);
  }
}

class _scheduleAtFixedRate {
  static void run(ScheduledExecutorService service) {
    // cronjob
    // run the first task right await, and then every 5 seconds
    // if any task throws an exception, the future tasks are suppressed
    service.scheduleAtFixedRate(
        () -> System.out.println("periodically!"),
        0,
        5,
        TimeUnit.SECONDS);
  }
}

class _shutdown {
  static void run(ScheduledExecutorService service) {
    // the executor service must be closed otherwise it will hang
    // the shutdown hook finishes gracefully the ongoing tasks
    // when shutdown is called, it receives no more new tasks
    service.shutdown();
  }
}
