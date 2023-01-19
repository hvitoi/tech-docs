/*
 * Executors class
 */

import java.util.concurrent.Executors;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    _newCachedThreadPool.run();
    _newFixedThreadPool.run();
  }
}

class _newCachedThreadPool {
  static void run() {
    var executorService1 = Executors.newCachedThreadPool();
    executorService1.submit(() -> {
      Thread.sleep(5000);
      System.out.println("I finished executing after 5 seconds.");
      return null;
    });

    //

    var executorService2 = Executors.newCachedThreadPool();
    executorService2.submit(() -> {
      Thread.sleep(10000);
      System.out.println("I finished executing after 10 seconds.");
      return null;
    });
  }
}

class _newFixedThreadPool {
  static void run() {
    // if a thread terminates due to a failure in the task, then a new thread with
    // the task in created to replace it
    var executorService = Executors.newFixedThreadPool(3);
  }
}
