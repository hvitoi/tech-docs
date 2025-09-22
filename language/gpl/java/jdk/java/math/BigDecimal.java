import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.RoundingMode;
import java.util.Random;

// Unscaled value: an arbitrary precision integer
// Scale: a 32-bit integer representing the number of digits to the right of the decimal point

// Example: 3.14 -> unscaled value: 314 -> scale: 2

class Main {
  public static void main(String[] args) {
    _new();

    // Static Fields
    _ONE();
    _ZERO();

    // Static Methods
    _valueOf();

    // Instance methods
    _add();
    _compareTo();
    _multiply();
    _setScale();

  }

  static void _new() {
    var a = new BigDecimal("0.1");
    var b = new BigDecimal(new char[] { '3', '.', '1', '6', '1', '5' });
    var c = new BigDecimal(42);
    var d = new BigDecimal(123412345678901L);
    var e = new BigDecimal(0.1d); // 0.1 does not have an exact representation in double
    var f = new BigDecimal(BigInteger.probablePrime(100, new Random()));
  }

  static void _ONE() {
    var one = BigDecimal.ONE;
  }

  static void _ZERO() {
    var zero = BigDecimal.ZERO;
  }

  static void _valueOf() {
    var a = BigDecimal.valueOf(123412345678901L);
    var b = BigDecimal.valueOf(123412345678901L, 2);
    var c = BigDecimal.valueOf(0.1d);
  }

  static void _add() {
    var num1 = BigDecimal.ONE;
    var num2 = BigDecimal.ONE;

    var res = num1.add(num2);
  }

  static void _compareTo() {
    var num1 = BigDecimal.ONE;
    var num2 = BigDecimal.ONE;

    int res = num1.compareTo(num2); // 0: the same, 1: greater, -1: lesser
  }

  static void _multiply() {
    var num1 = BigDecimal.ONE;
    var num2 = BigDecimal.ONE;

    var res = num1.multiply(num2);
  }

  static void _setScale() {
    var num = BigDecimal.ONE;

    var res = num.setScale(2, RoundingMode.HALF_UP); // transform to 1.00
  }
}
