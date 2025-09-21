class Main {

  public static void main(String[] args) {
    _new();

    // Instance methods
    _booleanValue();

  }

  static void _new() {
    Boolean myTrue1 = Boolean.TRUE;
    Boolean myFalse1 = Boolean.FALSE;

    boolean myTrue2 = true;
    boolean myFalse2 = false;

  }

  static void _booleanValue() {
    Boolean myTrue = Boolean.TRUE;
    myTrue.booleanValue(); // true

    Boolean myFalse = Boolean.FALSE;
    myFalse.booleanValue(); // false
  }
}
