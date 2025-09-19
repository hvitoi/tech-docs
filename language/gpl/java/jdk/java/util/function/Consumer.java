import java.util.function.Consumer;

// One Input -> Void

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();
  }

  static void _new() {
    Consumer<String> consumer1 = System.out::println; // new syntax
    Consumer<String> consumer2 = (el) -> System.out.println(el); // with lambdas
    Consumer<String> consumer3 = new MyConsumer(); // consumer class (legacy)
  }
}

class MyConsumer implements Consumer<String> {
  @Override
  public void accept(String str) {
    System.out.println(str);
  }
}
