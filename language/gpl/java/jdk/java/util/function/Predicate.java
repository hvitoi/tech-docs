import java.util.function.Predicate;

// 1 input -> 1 output (boolean)

class Main {
  public static void main(String[] args) {
    _new();
  }

  static void _new() {
    Predicate<String> startsWithS = str -> str.startsWith("S"); // true or false
  }
}
