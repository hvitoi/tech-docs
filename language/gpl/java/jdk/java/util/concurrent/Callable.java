// Interface

// Function: 0 input -> 1 output

import java.util.concurrent.Callable;

class Main {
  public static void main(String[] args) {

    Callable<Integer> c1 = () -> 1 + 1;
    Callable<Integer> c2 = new Callable<Integer>() {
      @Override
      public Integer call() {
        return 1 + 1;
      }
    };

    try {
      c1.call();
      c2.call();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
