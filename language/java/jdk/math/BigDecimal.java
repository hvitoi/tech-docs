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
    BigDecimalAttributes.run();

    // Static Methods
    BigDecimalNew.run();
    BigDecimalValueOf.run();

    // Instance methods
    BigDecimalAdd.run();
    BigDecimalCompareTo.run();
    BigDecimalMultiply.run();
    BigDecimalSetScale.run();

  }
}

class BigDecimalAttributes {
  static void run() {
    BigDecimal one = BigDecimal.ONE;
    BigDecimal zero = BigDecimal.ZERO;
  }
}

class BigDecimalNew {
  static void run() {
    BigDecimal bdFromString = new BigDecimal("0.1");
    BigDecimal bdFromCharArray = new BigDecimal(new char[] { '3', '.', '1', '6', '1', '5' });
    BigDecimal bdFromInt = new BigDecimal(42);
    BigDecimal bdFromLong = new BigDecimal(123412345678901L);
    BigDecimal bdFromDouble = new BigDecimal(0.1d); // 0.1 does not have an exact representation in double
    BigDecimal bdFromBigInteger = new BigDecimal(BigInteger.probablePrime(100, new Random()));
  }
}

class BigDecimalValueOf {
  static void run() {
    BigDecimal bdFromLong1 = BigDecimal.valueOf(123412345678901L);
    BigDecimal bdFromLong2 = BigDecimal.valueOf(123412345678901L, 2);
    BigDecimal bdFromDouble = BigDecimal.valueOf(0.1d);
  }
}

class BigDecimalAdd {
  static void run() {
    BigDecimal num1 = BigDecimal.ONE;
    BigDecimal num2 = BigDecimal.ONE;

    BigDecimal res = num1.add(num2);
  }

}

class BigDecimalCompareTo {
  static void run() {
    BigDecimal num1 = BigDecimal.ONE;
    BigDecimal num2 = BigDecimal.ONE;
    int res = num1.compareTo(num2); // 0: the same, 1: greater, -1: lesser
  }

}

class BigDecimalMultiply {
  static void run() {
    BigDecimal num1 = BigDecimal.ONE;
    BigDecimal num2 = BigDecimal.ONE;

    BigDecimal res = num1.multiply(num2); // does not change the original value
  }

}

class BigDecimalSetScale {
  static void run() {
    BigDecimal num = BigDecimal.ONE;

    BigDecimal res = num.setScale(2, RoundingMode.HALF_UP); // transform to 1.00
  }

}
