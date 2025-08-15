class Main {
  public static void main(String[] args) {

    // Static methods
    _new();
    _printStackTrace();
    _getStackTrace();
  }

  static void _new() {
    Exception e = new Exception();
  }

  static void _printStackTrace() {
    Exception e = new Exception();
    e.printStackTrace();
  }

  static void _getStackTrace() {
    Exception e = new Exception();
    e.getStackTrace();
  }
}
