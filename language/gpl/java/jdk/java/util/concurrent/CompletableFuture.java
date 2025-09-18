/*
 * CompletableFuture class
 */

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();
    _completedFuture();
    _supplyAsync();

    _allOf();
    _join();

    // Instance methods
    _complete();
    _completeExceptionally();
    _get();
    _handle();

    _thenApply();
    _thenAccept();
    _thenRun();

    _thenCompose();
    _thenCombine();
    _thenAcceptBoth();
  }

  static void _new() {
    // CompletableFuture implements the Future interface
    var task = new CompletableFuture<>();
  }

  static void _completedFuture() {
    // complete Future (with a constant)
    var task = CompletableFuture.completedFuture("Hello");
  }

  static void _supplyAsync() {
    Supplier<String> supplier = () -> "Hello";
    // complete Future (with a supplier)
    var task = CompletableFuture.supplyAsync(supplier);
  }

  static void _allOf() {
    var task1 = CompletableFuture.completedFuture("Hello");
    var task2 = CompletableFuture.completedFuture("Beautiful");
    var task3 = CompletableFuture.completedFuture("World");

    // This new CompletableFuture waits for all tasks to be completed
    // With this we cannot access the results of each task (returns Void)
    var combinedFuture = CompletableFuture.allOf(task1, task2, task3);
  }

  static void _join() {
    var task1 = CompletableFuture.completedFuture("Hello");
    var task2 = CompletableFuture.completedFuture("Beautiful");
    var task3 = CompletableFuture.completedFuture("World");

    // Gets the result of each task (similar to the get())
    // Differently from get() it throws an unchecked exception in case the Future
    // does not complete normally.
    var combined = Stream.of(task1, task2, task3)
        .map(CompletableFuture::join)
        .collect(Collectors.joining(" "));
  }

  static void _complete() {
    var task = new CompletableFuture<>();
    task.complete("Hello"); // mark the task as complete right away
  }

  static void _completeExceptionally() {
    var task = new CompletableFuture<>();

    // Complete it with an exception
    task.completeExceptionally(
        new RuntimeException("Calculation failed!"));

    // task.get(); // ExecutionException
  }

  static void _get() {
    var task = CompletableFuture.completedFuture("Hello");

    try {
      task.get(); // will wait for the result to be ready
    } catch (InterruptedException e) {
    } catch (ExecutionException e) {
    }
  }

  static void _handle() {
    String name = null;
    var task = CompletableFuture.supplyAsync(() -> {
      if (name == null) {
        throw new RuntimeException("Computation error!");
      }
      return "Hello, " + name;
    });

    // ...

    // Handle result (set a default result) in case of exception
    task.handle((s, t) -> s != null ? s : "Hello, Stranger!");
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
