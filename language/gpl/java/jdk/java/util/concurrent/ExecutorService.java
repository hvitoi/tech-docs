/*
 * ExecutorService class
 */

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class Main {
  public static void main(String[] args) {
    var executorService = Executors.newCachedThreadPool();

    // Instance methods
    _submit(executorService);
    _execute(executorService);
  }

  static void _submit(ExecutorService executorService) {
    // submit a task to be run in the thread
    // Takes a Runnable task which returns back a value
    // Returns a Future can be used to get the result
    executorService.submit(() -> {
      Thread.sleep(1000);
      System.out.println("I finished executing after 1 second.");
      return null;
    });

    executorService.submit(() -> {
      Thread.sleep(2000);
      System.out.println("I finished executing after 2 seconds.");
      return null;
    });
  }

  static void _execute(ExecutorService executorService) {
    // Returns nil so that the result is lost
    // Takes a Callable task which does not return a value
    executorService.execute(() -> System.out.println("lol!"));
  }

}
