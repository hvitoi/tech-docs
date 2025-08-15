import java.math.BigDecimal;

class Main {
  public static void main(String[] args) {

    // Static Methods
    _compare();
    _parseInt();
    _valueOf();
    _sum();
  }

  static void _compare() {

    Integer ref1 = 30;
    Integer ref2 = 30;
    Integer ref3 = 20;

    Integer.compare(ref1, ref2); // 0: equal
    Integer.compare(ref2, ref3); // +1: 1st > 2nd
    Integer.compare(ref3, ref2); // -1: 1st < 2nd
  }

  static void _parseInt() {
    Integer parsedInt = Integer.parseInt("3279"); // String -> Integer
  }

  static void _valueOf() {
    Integer ref1 = 30; // boxing from int
    Integer ref2 = Integer.valueOf(30); // boxing from int
    Integer ref3 = Integer.valueOf("20"); // boxing from str
  }

  static void _sum() {
    int sum = Integer.sum(1, 1);
  }
}
