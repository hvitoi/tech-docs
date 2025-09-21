class Main {
  public static void main(String[] args) {
    assert (1 == 0);
    // Don't use asserting for production error handling
    // By default, assertions are disabled, you need to enable them with
    // java -ea Main
  }
}
