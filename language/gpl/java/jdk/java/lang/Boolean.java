class Main {

  public static void main(String[] args) {

    // Static methods
    _new();

    // Instance methods
    _booleanValue();

  }

  static void _new() {
    boolean myTrue = true;
    boolean myFalse = false;

    Boolean myTrue2 = Boolean.TRUE;
    Boolean myFalse2 = Boolean.FALSE;
  }

  static void _booleanValue() {
    Boolean myTrue = Boolean.TRUE;
    myTrue.booleanValue(); // true

    Boolean myFalse = Boolean.FALSE;
    myFalse.booleanValue(); // false
  }
}
