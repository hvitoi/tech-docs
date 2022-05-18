import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class Main {
  public static void main(String[] args) {

    /**
     * Static
     */
    ExecutorServiceNew.run();

    /**
     * Instance
     */
    ExecutorServiceSubmit.run();
  }

}

class ExecutorServiceNew {
  static ExecutorService run() {
    ExecutorService service = Executors.newCachedThreadPool();
    return service;

  }

}

class ExecutorServiceSubmit {
  static void run() {
    ExecutorService service = ExecutorServiceNew.run();

    // submit a task to be run in the thread (Runnable or Callable)

    service.submit(() -> {
      Thread.sleep(5000);
      System.out.println("I finished executing after 5 seconds.");
      return null;
    });

    service.submit(() -> {
      Thread.sleep(10000);
      System.out.println("I finished executing after 10 seconds.");
      return null;
    });

  }

}
