import java.util.function.BinaryOperator;
import java.util.stream.Stream;

// Two Inputs (same type) -> One Output

class Main {
  public static void main(String[] args) {

    // Static methods
    BinaryOperatorNew.run();

  }
}

class BinaryOperatorNew {
  static void run() {
    BinaryOperator<Integer> fn = (Integer sum, Integer num) -> sum + num;
    BinaryOperator<Integer> fn2 = (sum, num) -> sum + num; // types can be omitted

    Integer res = Stream.of(1, 2, 3, 4).reduce(0, fn); // 10
  }
}
