import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Supplier;

class Main {
  public static void main(String[] args) {
    _new();

    // Static methods
    _completedFuture(); // -> CompletableFuture<T>
    _supplyAsync(); // -> CompletableFuture<T>
    _allOf(); // -> CompletableFuture<Void>

    // Instance methods
    _get(); // -> T (result)
    _join(); // -> T (result)
    _complete(); // -> boolean
    _completeExceptionally(); // -> boolean
    _handle(); // -> CompletableFuture
    _thenApply(); // -> CompletableFuture
    _thenAccept(); // -> CompletableFuture
    _thenRun(); // -> CompletableFuture
    _thenCompose(); // -> CompletableFuture
    _thenCombine(); // -> CompletableFuture
    _thenAcceptBoth(); // -> CompletableFuture
  }

  static void _new() {
    // CompletableFuture implements the Future interface
    var task = new CompletableFuture<String>();
  }

  static void _completedFuture() {
    // complete Future (with a constant)
    var task = CompletableFuture.completedFuture("Hello");
  }

  static void _supplyAsync() {
    // complete Future (with the value from a supplier)
    Supplier<String> supplier = () -> "Hello";
    var task = CompletableFuture.supplyAsync(supplier);
  }

  static void _allOf() {
    var task1 = CompletableFuture.completedFuture("Hello");
    var task2 = CompletableFuture.completedFuture("Beautiful");
    var task3 = CompletableFuture.completedFuture("World");

    // Waits for all tasks to be completed
    // With this we cannot access the results of each task (returns Void)
    var combinedFuture = CompletableFuture.allOf(task1, task2, task3);
  }

  static void _get() {
    var task = CompletableFuture.completedFuture("Hello");

    try {
      task.get(); // will wait for the result to be ready
    } catch (InterruptedException | ExecutionException e) {
      e.printStackTrace();
    }

  }

  static void _join() {
    var task = CompletableFuture.completedFuture("Hello");

    // Gets the result of each task (similar to the get())
    // Differently from get() it throws an unchecked exception in case the Future
    // does not complete normally.
    task.join();
  }

  static void _complete() {
    var task = new CompletableFuture<String>();
    task.complete("Hello"); // mark the task as complete right away
  }

  static void _completeExceptionally() {
    var task = new CompletableFuture<String>();
    // Complete it with an exception
    task.completeExceptionally(
        new RuntimeException("Calculation failed!"));

    // task.get(); // ExecutionException
  }

  static void _handle() {
    CompletableFuture<String> task = CompletableFuture.supplyAsync(() -> {
      throw new RuntimeException("Computation error!");
    });

    // Handle result (set a default result) in case of exception
    var taskHandled = task.handle((s, t) -> s != null ? s : "Hello, Stranger!");
  }

  static void _thenApply() {
    var task = CompletableFuture.completedFuture("Hello");

    // Process future result with a function
    Function<String, String> fn = s -> s + " World";
    var taskFunction = task.thenApply(fn);

    // thenApply() runs in the calling thread
    // thenApplyAsync() runs in a new thread using the common fork/join pool
    // implementation of Executor ForkJoinPool.commonPool()
  }

  static void _thenAccept() {
    var task = CompletableFuture.completedFuture("Hello");

    // Consume future result with a consumer
    Consumer<String> consumer = s -> System.out.println("Result: " + s);
    var taskConsumer = task.thenAccept(consumer);
  }

  static void _thenRun() {
    var task = CompletableFuture.completedFuture("Hello");

    // Run something after future result is complete
    Runnable runnable = () -> System.out.println("Computation finished.");
    var taskRun = task.thenRun(runnable);
  }

  static void _thenCompose() {
    var task = CompletableFuture.completedFuture("Hello");
    var taskComposite = task
        .thenCompose(s -> CompletableFuture.supplyAsync(() -> s + " World"));
  }

  static void _thenCombine() {
    var task1 = CompletableFuture.completedFuture("Hello");
    var task2 = CompletableFuture.completedFuture("World");

    var taskCombination = task1
        .thenCombine(task2, (s1, s2) -> s1 + s2);
  }

  static void _thenAcceptBoth() {
    var task1 = CompletableFuture.completedFuture("Hello");
    var task2 = CompletableFuture.completedFuture("World");

    var taskCombination = task1
        .thenAcceptBoth(task2,
            (s1, s2) -> System.out.println(s1 + s2));
  }
}
