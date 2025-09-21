class Main {
  public static void main(String[] args) {
    _new();

    // Instance methods
    _printStackTrace();
    _getStackTrace();
  }

  static void _new() {
    Exception e = new Exception();
  }

  static void _printStackTrace() {
    var e = new Exception();
    // e.printStackTrace();
  }

  static void _getStackTrace() {
    var e = new Exception();
    var stackTrace = e.getStackTrace();

    // for (var el : stackTrace) {
    // System.out.println(el);
    // }
  }
}
