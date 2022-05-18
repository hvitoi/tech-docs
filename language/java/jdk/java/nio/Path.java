import java.nio.file.Path;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    PathOf.run();

  }
}

class PathOf {
  static void run() {
    Path path = Path.of("/");
  }
}
