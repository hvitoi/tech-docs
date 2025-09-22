import java.util.function.UnaryOperator;

// One Input -> One Output (of the same type)

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();
  }

  static void _new() {
    UnaryOperator<String> fn = s -> s.toUpperCase();
  }
}
