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
    /**
     * Static
     */
    _new.run();
    _completedFuture.run();
    _supplyAsync.run();

    _allOf.run();
    _join.run();

    /**
     * Instance
     */
    _complete.run();
    _completeExceptionally.run();
    _get.run();
    _handle.run();

    _thenApply.run();
    _thenAccept.run();
    _thenRun.run();

    _thenCompose.run();
    _thenCombine.run();
    _thenAcceptBoth.run();
  }
}

class _new {
  static void run() {
    // CompletableFuture implements the Future interface
    var task = new CompletableFuture<>();
  }
}

class _completedFuture {
  static void run() {
    // complete Future (with a constant)
    var task = CompletableFuture.completedFuture("Hello");
  }
}

class _supplyAsync {
  static void run() {
    Supplier<String> supplier = () -> "Hello";
    // complete Future (with a supplier)
    var task = CompletableFuture.supplyAsync(supplier);
  }
}

class _allOf {
  static void run() {
    var task1 = CompletableFuture.completedFuture("Hello");
    var task2 = CompletableFuture.completedFuture("Beautiful");
    var task3 = CompletableFuture.completedFuture("World");

    // This new CompletableFuture waits for all tasks to be completed
    // With this we cannot access the results of each task (returns Void)
    var combinedFuture = CompletableFuture.allOf(task1, task2, task3);
  }
}

class _join {
  static void run() {
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
}

class _complete {
  static void run() {
    var task = new CompletableFuture<>();
    task.complete("Hello"); // mark the task as complete right away
  }
}

class _completeExceptionally {
  static void run() {
    var task = new CompletableFuture<>();

    // Complete it with an exception
    task.completeExceptionally(
        new RuntimeException("Calculation failed!"));

    // task.get(); // ExecutionException
  }
}

class _get {
  static void run() {
    var task = CompletableFuture.completedFuture("Hello");

    try {
      task.get(); // will wait for the result to be ready
    } catch (InterruptedException e) {
    } catch (ExecutionException e) {
    }
  }
}

class _handle {
  static void run() {
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
}

class _thenApply {
  static void run() {
    var task = CompletableFuture.completedFuture("Hello");

    // Process future result with a function
    Function<String, String> fn = s -> s + " World";
    var taskFunction = task.thenApply(fn);

    // thenApply() runs in the calling thread
    // thenApplyAsync() runs in a new thread using the common fork/join pool
    // implementation of Executor ForkJoinPool.commonPool()
  }
}

class _thenAccept {
  static void run() {
    var task = CompletableFuture.completedFuture("Hello");

    // Consume future result with a consumer
    Consumer<String> consumer = s -> System.out.println("Result: " + s);
    var taskConsumer = task.thenAccept(consumer);
  }
}

class _thenRun {
  static void run() {
    var task = CompletableFuture.completedFuture("Hello");

    // Run something after future result is complete
    Runnable runnable = () -> System.out.println("Computation finished.");
    var taskRun = task.thenRun(runnable);
  }
}

class _thenCompose {
  static void run() {
    var task = CompletableFuture.completedFuture("Hello");

    var taskComposite = task
        .thenCompose(s -> CompletableFuture.supplyAsync(() -> s + " World"));
  }
}

class _thenCombine {
  static void run() {
    var task1 = CompletableFuture.completedFuture("Hello");
    var task2 = CompletableFuture.completedFuture("World");

    var taskCombination = task1
        .thenCombine(task2, (s1, s2) -> s1 + s2);
  }
}

class _thenAcceptBoth {
  static void run() {
    var task1 = CompletableFuture.completedFuture("Hello");
    var task2 = CompletableFuture.completedFuture("World");

    var taskCombination = task1
        .thenAcceptBoth(task2,
            (s1, s2) -> System.out.println(s1 + s2));
  }
}
