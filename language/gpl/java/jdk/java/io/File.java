import java.io.File;
import java.nio.file.Path;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _toPath();
    _getParentFile();
    _mkdirs();
  }

  static void _new() {
    // scoped to the root project path
    File file = new File("sample.json");
  }

  static void _toPath() {
    var file = new File("sample.json");
    Path path = file.toPath(); // the relative path of the file
  }

  static void _getParentFile() {
    var file = new File("sample.json");

    // the same filename but at a parent directory
    File parentFile = file.getParentFile();
  }

  static void _mkdirs() {
    var file = new File("sample.json");
    // create parent directories as needed to create the file
    file.mkdirs();
  }
}
