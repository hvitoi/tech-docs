class Main {
  public static void main(String[] args) {
    // Static Methods
    _new();

    // Instance methods
    _append();
    _toString();
  }

  static void _new() {
    var sb = new StringBuilder();
    var sb2 = new StringBuilder("Hey!"); // define initial value
  }

  static void _append() {
    var myStr = new StringBuilder()
        .append("Hello")
        .append(" World!")
        .toString();
  }

  static void _toString() {
    var myStr = new StringBuilder()
        .append("Hello")
        .append(" World!")
        .toString();
  }
}
