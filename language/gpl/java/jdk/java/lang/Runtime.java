class Main {
  public static void main(String[] args) {
    // Static methods
    _getRuntime();

    // Instance methods
    _availableProcessors();
  }

  static void _getRuntime() {
    var runtime = Runtime.getRuntime();
  }

  static void _availableProcessors() {
    var runtime = Runtime.getRuntime();
    int processorsCount = runtime.availableProcessors();
  }
}
