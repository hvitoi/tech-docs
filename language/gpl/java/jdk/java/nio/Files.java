import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.nio.file.StandardOpenOption;

class Main {
  public static void main(String[] args) {
    // Static methods
    _write();
    _copy();
    _readString();
  }

  static void _write() {
    var file = new File("/tmp/file.txt");
    try {
      Files.write(file.toPath(), "abc".getBytes(), StandardOpenOption.APPEND);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  static void _copy() {
    var file = new File("/tmp/file.txt");
    var newPath = Path.of("/tmp/foo/file.txt");
    // copy file from file into newPath
    try {
      Files.copy(file.toPath(), newPath, StandardCopyOption.REPLACE_EXISTING);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  static void _readString() {
    // Read string out of a text file
    var filePath = Path.of("/tmp/file.txt");
    try {
      var s = Files.readString(filePath);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

}
