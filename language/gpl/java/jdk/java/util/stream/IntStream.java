import java.util.stream.IntStream;

class Main {
  public static void main(String[] args) {
    // Static methods
    _rangeClosed();
  }

  static void _rangeClosed() {
    IntStream stream = IntStream.rangeClosed(1, 5);
  }
}
