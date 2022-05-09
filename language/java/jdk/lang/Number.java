import java.math.BigDecimal;

class Main {
  public static void main(String[] args) {

    // Number Implementations
    NumberImplementations.run();

    // Instance methods
    NumberByteValue.run();
    NumberShortValue.run();
    NumberIntValue.run();
    NumberLongValue.run();

    NumberDoubleValue.run();
    NumberFloatValue.run();
  }
}

class NumberImplementations {
  static void run() {

    byte myByte = 120;
    byte byteSizeBytes = Byte.BYTES; // 1 byte
    byte byteMinValue = Byte.MIN_VALUE; // -128
    byte byteMaxValue = Byte.MAX_VALUE; // +127

    short myShort = 3209;
    short shortSizeBytes = Short.BYTES; // 2 bytes
    short minShortValue = Short.MIN_VALUE; // - 32_768
    short maxShortValue = Short.MAX_VALUE; // + 32_767

    int myInt = 1_000;
    int myIntDivided = 5 / 3; // floors the value
    int intSizeBytes = Integer.BYTES; // 4 bytes
    int intMinValue = Integer.MIN_VALUE; // -2_147_483_648
    int intMaxValue = Integer.MAX_VALUE; // +2_147_483_648: overflows with +1

    long myLong = 2_147_483_648L;
    long longSizeBytes = Long.BYTES; // 8 bytes
    long longMinValue = Long.MIN_VALUE; // -9_223_372_036_854_775_808
    long longMaxValue = Long.MAX_VALUE; // 9_223_372_036_854_775_807

    float myFloat = 5000f;
    float myFloatDivided = 5f / 3f; // less precise
    float floatSizeBytes = Float.BYTES; // 4 bytes
    float floatMinValue = Float.MIN_VALUE; // 1.4 E-45
    float floatMaxValue = Float.MAX_VALUE; // 3.4028235 E+38

    double myDouble = 3_000_000.4_567_890d;
    double myDoubleDivided = 5.00 / 3.00; // more precise
    double doubleSizeBytes = Double.BYTES; // 8 bytes
    double doubleMinValue = Double.MIN_VALUE; // 4.9 E-324
    double doubleMaxValue = Double.MAX_VALUE; // 1.7976931348623157 E+308

  }
}

class NumberByteValue {
  static void run() {
    Number number = 29;
    byte byteValue = number.byteValue();
  }
}

class NumberShortValue {
  static void run() {
    Number number = 29;
    short shortValue = number.shortValue();
  }
}

class NumberIntValue {
  static void run() {
    Number number = 29;
    int intValue = number.intValue();
  }
}

class NumberLongValue {
  static void run() {
    Number number = 29;
    long longValue = number.longValue();
  }
}

class NumberFloatValue {
  static void run() {
    Number number = 29;
    float floatValue = number.floatValue();
  }
}

class NumberDoubleValue {
  static void run() {
    Number number = 29;
    double doubleValue = number.doubleValue();
  }
}
