class Main {

  public static void main(String[] args) {
    // Static Fields
    _TRUE();
    _FALSE();

    // Instance methods
    _booleanValue();

  }

  static void _TRUE() {
    Boolean myTrue1 = Boolean.TRUE;
    boolean myTrue2 = true;
  }

  static void _FALSE() {
    Boolean myFalse1 = Boolean.FALSE;
    boolean myFalse2 = false;
  }

  static void _booleanValue() {
    Boolean myTrue = Boolean.TRUE;
    myTrue.booleanValue(); // true

    Boolean myFalse = Boolean.FALSE;
    myFalse.booleanValue(); // false
  }
}
