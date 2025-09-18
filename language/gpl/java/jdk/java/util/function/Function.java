import java.util.function.Function;

// One Input -> One Output

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _apply();
    _andThen();
  }

  static void _new() {
    Function<String, Integer> fn = (word) -> word.length();
  }

  static void _apply() {
    Function<String, Integer> fn = (word) -> word.length();
    Integer res = fn.apply("henrique"); // 8

  }

  static void _andThen() {
    Function<String, Integer> fn1 = x -> x.length();
    Function<Integer, Integer> fn2 = x -> x * 2;

    Function<String, Integer> compositeFn = fn1.andThen(fn2);
    Integer res = compositeFn.apply("henrique"); // 16

  }
}
