// Runtime stack / Call stack
class Main {

  public static void main(String[] args) {
    System.out.println("main: start");
    Main.method1();
    System.out.println("main: end");
  }

  static void method1() {
    System.out.println("method 1: start");
    method2();
    System.out.println("method 1: end");
  }

  static void method2() {
    System.out.println("method 2: start");
    int lol = 3 / 0; // show the callstack with the exact line where the exception happened
    System.out.println("method 2: end");
  }

}
