/*
 * Runtime class
 */

class Main {
  public static void main(String[] args) {
    /*
     * Static
     */
    _getRuntime();

    /*
     * Instance
     */
    _availableProcessors();

  }

  static void _getRuntime() {
    Runtime.getRuntime();
  }

  static void _availableProcessors() {
    var runtime = Runtime.getRuntime();
    runtime.availableProcessors();
  }
}
