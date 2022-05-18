import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class Main {
  public static void main(String[] args) {

    /**
     * Static
     */
    ExecutorsNewCachedThreadPool.run();
    ExecutorsNewFixedThreadPool.run();
  }

}

class ExecutorsNewCachedThreadPool {
  static void run() {
    ExecutorService service1 = Executors.newCachedThreadPool();
    service1.submit(() -> {
      Thread.sleep(5000);
      System.out.println("I finished executing after 5 seconds.");
      return null;
    });

    //

    ExecutorService service2 = Executors.newCachedThreadPool();
    service2.submit(() -> {
      Thread.sleep(10000);
      System.out.println("I finished executing after 10 seconds.");
      return null;
    });

  }

}

class ExecutorsNewFixedThreadPool {
  static void run() {
    // if a thread terminates due to a failure in the task, then a new thread with
    // the task in created to replace it
    ExecutorService service = Executors.newFixedThreadPool(3);
  }

}
