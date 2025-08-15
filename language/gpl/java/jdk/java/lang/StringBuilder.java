class Main {
  public static void main(String[] args) {
    // Static Methods
    _new();

    // Instance methods
    _append();
    _toString();
  }

  static void _new() {
    StringBuilder builder = new StringBuilder("hey");
  }

  static void _append() {
    StringBuilder builder = new StringBuilder("hey");
    builder.append(" there!");
    System.out.println(builder.toString());
  }

  static void _toString() {
    StringBuilder builder = new StringBuilder("hey");
    builder.append(" there!");
    System.out.println(builder.toString());
  }
}
