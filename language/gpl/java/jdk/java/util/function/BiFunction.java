import java.util.function.BiFunction;

// Two Inputs (different type) -> One Output
// T: first param type, U: second param type, R: return type

class Main {
  public static void main(String[] args) {
    // Static methods
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
