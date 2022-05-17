class Main {
  public static void main(String[] args) {
    // Static methods
    RunnableNew.run();

  }
}

class RunnableNew {
  static void run() {
    // No args
    Runnable runnable = () -> System.out.println("Computation finished.");
  }
}
