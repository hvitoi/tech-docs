import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

class Main {
  public static void main(String[] args) {
    var executor = Executors.newCachedThreadPool();

    // Instance methods
    _submit(executor);
    _execute(executor);
  }

  static void _submit(ExecutorService executor) {
    // submit a task to be run in the thread
    // Takes a Runnable task (Runnable or Callable) which returns back a value
    // Returns a Future can be used to get the result

    Future<?> result = executor.submit(() -> {
      try {
        Thread.sleep(1000);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
      System.out.println("I finished executing after 1 second.");
    });

    Future<?> result2 = executor.submit(() -> {
      try {
        Thread.sleep(2000);
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
      System.out.println("I finished executing after 2 seconds.");
    });
  }

  static void _execute(ExecutorService executor) {
    // Just like "submit", but ignores the result
    // Therefore it accepts only Runnable functions
    Runnable fn = () -> System.out.println("lol!");
    executor.execute(fn);
  }

}
