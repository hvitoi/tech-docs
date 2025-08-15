/*
 * Runnable interface
 */

class Main {
  public static void main(String[] args) {
    Runnable r1 = () -> System.out.println("Computation finished.");
    Runnable r2 = new MyRunner();
  }
}

// Defines a function!

class MyRunner implements Runnable {
  @Override
  public void run() {
    System.out.println("I will run!");
  }
}
