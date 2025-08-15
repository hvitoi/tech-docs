import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.RoundingMode;
import java.util.Random;

// Unscaled value: an arbitrary precision integer
// Scale: a 32-bit integer representing the number of digits to the right of the decimal point

// Example: 3.14 -> unscaled value: 314 -> scale: 2

class Main {
  public static void main(String[] args) {
    // Static Attributes
    _attributes();

    // Static Methods
    _new();
    _valueOf();

    // Instance methods
    _add();
    _compareTo();
    _multiply();
    _setScale();

  }

  static void _attributes() {
    BigDecimal one = BigDecimal.ONE;
    BigDecimal zero = BigDecimal.ZERO;
  }

  static void _new() {
    BigDecimal bdFromString = new BigDecimal("0.1");
    BigDecimal bdFromCharArray = new BigDecimal(new char[] { '3', '.', '1', '6', '1', '5' });
    BigDecimal bdFromInt = new BigDecimal(42);
    BigDecimal bdFromLong = new BigDecimal(123412345678901L);
    BigDecimal bdFromDouble = new BigDecimal(0.1d); // 0.1 does not have an exact representation in double
    BigDecimal bdFromBigInteger = new BigDecimal(BigInteger.probablePrime(100, new Random()));
  }

  static void _valueOf() {
    BigDecimal bdFromLong1 = BigDecimal.valueOf(123412345678901L);
    BigDecimal bdFromLong2 = BigDecimal.valueOf(123412345678901L, 2);
    BigDecimal bdFromDouble = BigDecimal.valueOf(0.1d);
  }

  static void _add() {
    BigDecimal num1 = BigDecimal.ONE;
    BigDecimal num2 = BigDecimal.ONE;

    BigDecimal res = num1.add(num2);
  }

  static void _compareTo() {
    BigDecimal num1 = BigDecimal.ONE;
    BigDecimal num2 = BigDecimal.ONE;
    int res = num1.compareTo(num2); // 0: the same, 1: greater, -1: lesser
  }

  static void _multiply() {
    BigDecimal num1 = BigDecimal.ONE;
    BigDecimal num2 = BigDecimal.ONE;

    BigDecimal res = num1.multiply(num2); // does not change the original value
  }

  static void _setScale() {
    BigDecimal num = BigDecimal.ONE;

    BigDecimal res = num.setScale(2, RoundingMode.HALF_UP); // transform to 1.00
  }
}
