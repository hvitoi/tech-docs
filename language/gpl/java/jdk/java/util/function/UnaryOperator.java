import java.util.function.UnaryOperator;

// One Input -> One Output

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();
  }

  static void _new() {
    UnaryOperator<String> fn = (String s) -> s.toUpperCase();
    UnaryOperator<String> fn2 = s -> s.toUpperCase(); // types can be omitted
  }
}
