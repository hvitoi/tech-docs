class Main {

  public static void main(String[] args) {
    _boolean();
    _byte();
    _char();

    _short();
    _int();
    _long();

    _float();
    _double();

    boxing();
  }

  static void _boolean() {
    boolean foo1 = true;
    boolean foo2 = false;
  }

  static void _byte() {
    byte foo = 120;
    var a = Byte.BYTES; // 1 byte
    var b = Byte.MIN_VALUE; // -128
    var c = Byte.MAX_VALUE; // +127
  }

  static void _char() {
    // Stores a single Unicode character
    // 1 byte
    char foo = 'a';
  }

  static void _short() {
    // Rarely used today
    short foo = 3209;
    var a = Short.BYTES; // 2 bytes
    var b = Short.MIN_VALUE; // - 32_768
    var c = Short.MAX_VALUE; // + 32_767
  }

  static void _int() {
    int foo1 = 1_000;
    int foo2 = 5 / 3; // floors the value

    var a = Integer.BYTES; // 4 bytes
    var b = Integer.MIN_VALUE; // -2_147_483_648
    var c = Integer.MAX_VALUE; // +2_147_483_648: overflows with +1
  }

  static void _long() {
    long foo = 2_147_483_648L;

    var a = Long.BYTES; // 8 bytes
    var b = Long.MIN_VALUE; // -9_223_372_036_854_775_808
    var c = Long.MAX_VALUE; // 9_223_372_036_854_775_807
  }

  static void _float() {
    // ~ 6 or 7 decimal digits
    float foo1 = 3.14f;
    float foo2 = 5f / 3f; // less precise

    var a = Float.BYTES; // 4 bytes
    var b = Float.MIN_VALUE; // 1.4 E-45
    var c = Float.MAX_VALUE; // 3.4028235 E+38
  }

  static void _double() {
    // 15 decimal digits
    double foo1 = 3_000_000.4_567_890d;
    double foo2 = 5.00 / 3.00; // more precise

    var a = Double.BYTES; // 8 bytes
    var b = Double.MIN_VALUE; // 4.9 E-324
    var c = Double.MAX_VALUE; // 1.7976931348623157 E+308
  }

  static void boxing() {
    /*
     * Autoboxing in Java is the automatic conversion that the compiler
     * does between primitive types and their corresponding wrapper classes
     */

    Integer wrapper = 41; // autoboxing
    int primitive = wrapper; // unboxing

    // Collections can't hold primitive types, only Object
    // Autoboxing automatically casts it to the correct Object type

  }
}
