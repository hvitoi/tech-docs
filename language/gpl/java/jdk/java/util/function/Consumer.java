import java.util.function.Consumer;

// 1 input -> 0 output (void)

class Main {
  public static void main(String[] args) {
    _new();
  }

  static void _new() {
    Consumer<String> consumer1 = System.out::println; // new syntax
    Consumer<String> consumer2 = (String el) -> System.out.println(el); // with lambdas
    Consumer<String> consumer3 = new Consumer<String>() { // consumer class (legacy)
      @Override
      public void accept(String str) {
        System.out.println(str);
      }
    };
  }
}
