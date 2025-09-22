import java.util.function.BinaryOperator;
import java.util.stream.Stream;

// 2 inputs -> 1 output (of the same type)

class Main {
  public static void main(String[] args) {
    _new();
  }

  static void _new() {
    BinaryOperator<Integer> fn = (sum, num) -> sum + num;
    Integer res = Stream
        .of(1, 2, 3, 4)
        .reduce(0, fn); // 10
  }
}
