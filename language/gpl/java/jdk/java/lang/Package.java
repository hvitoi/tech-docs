class Main {
  public static void main(String[] args) {
    // Instance methods
    _getName();
  }

  static void _getName() {
    var pkg = "hello".getClass().getPackage();
    String packageName = pkg.getName();
  }
}
