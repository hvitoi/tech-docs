import java.util.function.BiFunction;

// Two Inputs (different type) -> One Output
// T: first param type, U: second param type, R: return type

class Main {
  public static void main(String[] args) {
    // Static methods
    BiFunctionNew.run();

    // Instance methods
    BiFunctionApply.run();
  }
}

class BiFunctionNew {
  static void run() {

    BiFunction<String, Integer, String> fn = (num, cha) -> num.toString() + cha;
  }
}

class BiFunctionApply {
  static void run() {
    String myCha = "zz";
    Integer myNum = 99;

    BiFunction<String, Integer, String> fn = (cha, num) -> cha + num.toString();

    String res = fn.apply(myCha, myNum); // "zz99"
    System.out.println(res);
  }
}
