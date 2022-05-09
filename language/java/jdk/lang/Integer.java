import java.math.BigDecimal;

class Main {
  public static void main(String[] args) {

    // Static Methods
    IntegerCompare.run();
    IntegerParseInt.run();
    IntegerValueOf.run();
    IntegerSum.run();

  }
}

class IntegerCompare {
  static void run() {

    Integer ref1 = 30;
    Integer ref2 = 30;
    Integer ref3 = 20;

    Integer.compare(ref1, ref2); // 0: equal
    Integer.compare(ref2, ref3); // +1: 1st > 2nd
    Integer.compare(ref3, ref2); // -1: 1st < 2nd

  }
}

class IntegerParseInt {
  static void run() {

    Integer parsedInt = Integer.parseInt("3279"); // String -> Integer

  }
}

class IntegerValueOf {
  static void run() {

    Integer ref1 = 30; // boxing from int
    Integer ref2 = Integer.valueOf(30); // boxing from int
    Integer ref3 = Integer.valueOf("20"); // boxing from str

  }
}

class IntegerSum {
  static void run() {

    int sum = Integer.sum(1, 1);

  }
}
