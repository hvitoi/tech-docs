import java.io.File;
import java.nio.file.Path;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    _new();

    /**
     * Instance
     */
    _toPath();
    _getParentFile();
    _mkdirs();
  }

  static File _new() {
    File file = new File("src/main/resources/sample.json"); // scoped to the root project path
    return file;
  }

  static void _toPath() {
    File file = _new();
    Path path = file.toPath();
  }

  static void _getParentFile() {
    File file = _new();

    // the same filename but at a parent directory
    File parentFile = file.getParentFile();
  }

  static void _mkdirs() {
    File file = _new();
    // create parent directories as needed to create the file
    file.mkdirs();
  }
}
