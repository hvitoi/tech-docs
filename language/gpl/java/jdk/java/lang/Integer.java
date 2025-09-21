class Main {
  public static void main(String[] args) {
    // Static Methods
    _compare();
    _valueOf();
    _parseInt();
    _sum();
  }

  static void _compare() {
    var num1 = 9;
    var num2 = 8;

    Integer.compare(num1, num1); // 0: equal
    Integer.compare(num1, num2); // +1: 1st > 2nd
    Integer.compare(num2, num1); // -1: 1st < 2nd
  }

  static void _valueOf() {
    Integer num1 = 30; // boxing from int
    var num2 = Integer.valueOf(30); // boxing from int
    var num3 = Integer.valueOf("20"); // boxing from str
  }

  static void _parseInt() {
    var num = Integer.parseInt("3279"); // String -> Integer
  }

  static void _sum() {
    // Sums 2 numbers
    int sum = Integer.sum(1, 2);
  }
}
