class Main {

  public static void main(String[] args) {

    // Static methods
    _new();

    // Instance methods
    _value();

  }

  static void _new() {
    boolean myTrue = true;
    boolean myFalse = false;
  }

  static void _value() {
    Boolean myTrue = Boolean.TRUE;
    Boolean myFalse = Boolean.FALSE;

    myTrue.booleanValue(); // true
    myFalse.booleanValue(); // false
  }
}
