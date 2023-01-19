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
  }

}

class Init {
  static ExecutorService run() {
    return Executors.newCachedThreadPool();
  }
}

class _submit {
  static void run(ExecutorService executorService) {
    // submit a task to be run in the thread (Runnable or Callable)
    executorService.submit(() -> {
      Thread.sleep(5000);
      System.out.println("I finished executing after 5 seconds.");
      return null;
    });

    executorService.submit(() -> {
      Thread.sleep(10000);
      System.out.println("I finished executing after 10 seconds.");
      return null;
    });
  }
}
