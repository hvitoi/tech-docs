/*
 * Callable interface
 */

import java.util.concurrent.Callable;

class Main {
  public static void main(String[] args) {
  }
}

class MyCaller implements Callable<Void> {
  @Override
  public Void call() throws Exception {
    System.out.println("do something");
    return null;
  }
}
