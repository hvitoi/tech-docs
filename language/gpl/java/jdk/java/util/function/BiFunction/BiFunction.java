import java.util.function.BiFunction;

// 2 inputs -> 1 output

class Main {
  public static void main(String[] args) {
    _new();

    // Instance methods
    _apply();
  }

  static void _new() {
    BiFunction<String, Integer, String> fn = (num, cha) -> num.toString() + cha;
  }

  static void _apply() {
    String myCha = "zz";
    Integer myNum = 99;

    BiFunction<String, Integer, String> fn = (cha, num) -> cha + num.toString();

    String res = fn.apply(myCha, myNum); // "zz99"
    System.out.println(res);
  }
}
