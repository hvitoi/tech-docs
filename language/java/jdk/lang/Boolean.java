class Main {
  public static void main(String[] args) {

    // Static methods
    BooleanNew.run();

    // Instance methods
    BooleanBooleanValue.run();

  }
}

class BooleanNew {
  static void run() {
    boolean myTrue = true;
    boolean myFalse = false;
  }
}

class BooleanBooleanValue {
  static void run() {
    Boolean myTrue = Boolean.TRUE;
    Boolean myFalse = Boolean.FALSE;

    myTrue.booleanValue(); // true
    myFalse.booleanValue(); // false
  }
}