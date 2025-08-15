import java.util.stream.IntStream;

class Main {
  public static void main(String[] args) {

    /**
     * Static
     */
    IntStreamRangeClosed.run();

  }
}

class IntStreamRangeClosed {
  static void run() {
    IntStream stream = IntStream.rangeClosed(1, 5);
  }
}
