// Interface

// Function: No input -> Void

class Main {
  public static void main(String[] args) {
    Runnable r1 = () -> System.out.println("Hello, World!");
    Runnable r2 = new Runnable() {
      @Override
      public void run() {
        System.out.println("Hello, World!");
      }
    };

    r1.run();
    r2.run();
  }
}
