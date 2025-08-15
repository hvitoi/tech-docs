/*
 * ExecutorService class
 */

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class Main {
  public static void main(String[] args) {
    var executorService = Init.run();
    /**
     * Instance
     */
    _submit.run(executorService);
    _execute.run(executorService);
  }

}

class Init {
  static ExecutorService run() {
    return Executors.newCachedThreadPool();
  }
}

class _submit {
  static void run(ExecutorService executorService) {
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
}

class _execute {
  static void run(ExecutorService executorService) {
    // Returns nil so that the result is lost
    // Takes a Callable task which does not return a value
    executorService.execute(() -> System.out.println("lol!"));
  }
}
