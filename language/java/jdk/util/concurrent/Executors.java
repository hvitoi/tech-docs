import java.util.concurrent.Executors;

class Main {
  public static void main(String[] args) {

    // Static methods
    ExecutorsNewCachedThreadPool.run();
  }

}

class ExecutorsNewCachedThreadPool {
  static void run() {
    Executors.newCachedThreadPool().submit(() -> {
      Thread.sleep(5000);
      System.out.println("I finished executing after 5 seconds.");
      return null;
    });

    Executors.newCachedThreadPool().submit(() -> {
      Thread.sleep(10000);
      System.out.println("I finished executing after 10 seconds.");
      return null;
    });

  }

}
