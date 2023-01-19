/*
 * Runtime class
 */

class Main {
  public static void main(String[] args) {
    /*
     * Static
     */
    _getRuntime.run();

    /*
     * Instance
     */
    _availableProcessors.run();

  }
}

class _getRuntime {
  static void run() {
    Runtime.getRuntime();
  }
}

class _availableProcessors {
  static void run() {
    var runtime = Runtime.getRuntime();
    runtime.availableProcessors();
  }
}
