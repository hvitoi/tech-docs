import java.util.function.Predicate;

// One Input -> Boolean

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();
  }

  static void _new() {
    Predicate<String> startsWithS = str -> str.startsWith("S"); // true or false
  }
}
