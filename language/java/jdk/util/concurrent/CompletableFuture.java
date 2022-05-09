import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
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
    CompletableFutureNew.run();
    CompletableFutureCompletedFuture.run();
    CompletableFutureSupplyAsync.run();

    CompletableFutureAllOf.run();
    CompletableFutureJoin.run();

    /**
     * Instance
     */
    CompletableFutureComplete.run();
    CompletableFutureGet.run();
    CompletableFutureHandle.run();
    CompletableFutureCompleteExceptionally.run();

    CompletableFutureThenApply.run();
    CompletableFutureThenAccept.run();
    CompletableFutureThenRun.run();

    CompletableFutureThenCompose.run();
    CompletableFutureThenCombine.run();
    CompletableFutureThenAcceptBoth.run();

  }

}

class CompletableFutureNew {
  static void run() {
    // CompletableFuture implements the Future interface
    Future<String> task = new CompletableFuture<>();
  }
}

class CompletableFutureCompletedFuture {
  static void run() {
    // complete Future (with a constant)
    Future<String> task = CompletableFuture.completedFuture("Hello");
  }
}

class CompletableFutureSupplyAsync {
  static void run() {
    Supplier<String> supplier = () -> "Hello";
    // complete Future (with a supplier)
    Future<String> task = CompletableFuture.supplyAsync(supplier);
  }
}

class CompletableFutureAllOf {
  static void run() {
    CompletableFuture<String> task1 = CompletableFuture.completedFuture("Hello");
    CompletableFuture<String> task2 = CompletableFuture.completedFuture("Beautiful");
    CompletableFuture<String> task3 = CompletableFuture.completedFuture("World");

    // This new CompletableFuture waits for all tasks to be completed
    // With this we cannot access the results of each task (returns Void)
    CompletableFuture<Void> combinedFuture = CompletableFuture.allOf(task1, task2, task3);

  }
}

class CompletableFutureJoin {
  static void run() {
    CompletableFuture<String> task1 = CompletableFuture.completedFuture("Hello");
    CompletableFuture<String> task2 = CompletableFuture.completedFuture("Beautiful");
    CompletableFuture<String> task3 = CompletableFuture.completedFuture("World");

    // Gets the result of each task (similar to the get())
    // Differently from get() it throws an unchecked exception in case the Future
    // does not complete normally.
    String combined = Stream.of(task1, task2, task3)
        .map(CompletableFuture::join)
        .collect(Collectors.joining(" "));

  }
}

class CompletableFutureComplete {
  static void run() {
    CompletableFuture<String> task = new CompletableFuture<>();
    task.complete("Hello"); // mark the task as complete right away
  }

}

class CompletableFutureCompleteExceptionally {
  static void run() {
    CompletableFuture<String> task = new CompletableFuture<>();

    // Complete it with an exception
    task.completeExceptionally(
        new RuntimeException("Calculation failed!"));

    // task.get(); // ExecutionException
  }

}

class CompletableFutureGet {
  static void run() {
    Future<String> task = CompletableFuture.completedFuture("Hello");

    try {
      task.get(); // will wait for the result to be ready
    } catch (InterruptedException e) {
    } catch (ExecutionException e) {
    }

  }

}

class CompletableFutureHandle {
  static void run() {
    String name = null;
    CompletableFuture<String> task = CompletableFuture.supplyAsync(() -> {
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

class CompletableFutureThenApply {
  static void run() {
    CompletableFuture<String> task = CompletableFuture.completedFuture("Hello");

    // Process future result with a function
    Function<String, String> fn = s -> s + " World";
    CompletableFuture<String> taskFunction = task.thenApply(fn);

    // thenApply() runs in the calling thread
    // thenApplyAsync() runs in a new thread using the common fork/join pool
    // implementation of Executor ForkJoinPool.commonPool()

  }
}

class CompletableFutureThenAccept {
  static void run() {
    CompletableFuture<String> task = CompletableFuture.completedFuture("Hello");

    // Consume future result with a consumer
    Consumer<String> consumer = s -> System.out.println("Result: " + s);
    CompletableFuture<Void> taskConsumer = task.thenAccept(consumer);
  }
}

class CompletableFutureThenRun {
  static void run() {
    CompletableFuture<String> task = CompletableFuture.completedFuture("Hello");

    // Run something after future result is complete
    Runnable runnable = () -> System.out.println("Computation finished.");
    CompletableFuture<Void> taskRun = task.thenRun(runnable);

  }
}

class CompletableFutureThenCompose {
  static void run() {
    CompletableFuture<String> task = CompletableFuture.completedFuture("Hello");

    CompletableFuture<String> taskComposite = task
        .thenCompose(s -> CompletableFuture.supplyAsync(() -> s + " World"));

  }
}

class CompletableFutureThenCombine {
  static void run() {
    CompletableFuture<String> task1 = CompletableFuture.completedFuture("Hello");
    CompletableFuture<String> task2 = CompletableFuture.completedFuture("World");

    CompletableFuture<String> taskCombination = task1
        .thenCombine(task2, (s1, s2) -> s1 + s2);

  }
}

class CompletableFutureThenAcceptBoth {
  static void run() {
    CompletableFuture<String> task1 = CompletableFuture.completedFuture("Hello");
    CompletableFuture<String> task2 = CompletableFuture.completedFuture("World");

    CompletableFuture<Void> taskCombination = task1
        .thenAcceptBoth(task2,
            (s1, s2) -> System.out.println(s1 + s2));
  }
}
