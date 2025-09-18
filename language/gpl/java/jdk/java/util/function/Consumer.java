import java.util.function.Consumer;

// One Input -> Void

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();
  }

  static void _new() {
    Consumer<String> consumer1 = s -> System.out.println(s); // new syntax
    Consumer<String> consumer2 = new MyConsumerClass(); // older way to create consumers
  }
}

class MyConsumerClass implements Consumer<String> {
  @Override
  public void accept(String str) {
    System.out.println(str);
  }
}
