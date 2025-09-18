import java.util.function.Supplier;

// Void -> One Output

class Main {
  public static void main(String[] args) {
    // Static methods
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
