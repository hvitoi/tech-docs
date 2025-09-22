import java.util.function.Supplier;

// 0 input -> 1 output

class Main {
  public static void main(String[] args) {
    _new();

    // Instance methods
    _get();
  }

  static void _new() {
    // Supplier of results
    Supplier<String> supplier = () -> "Hello";

  }

  static void _get() {
    Supplier<String> supplier = () -> "Hello";
    String res = supplier.get(); // hello
  }
}
