import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.nio.file.StandardOpenOption;

class Main {
  public static void main(String[] args) throws IOException {
    /**
     * Static
     */
    _copy();
    _write();
  }

  static void _copy() throws IOException {

    File file = new File("file");
    Path newPath = Path.of("/");

    // copy file from path1 to path2
    Files.copy(file.toPath(), newPath, StandardCopyOption.REPLACE_EXISTING);
  }

  static void _write() throws IOException {

    File file = new File("file");

    // write to a file
    Files.write(file.toPath(), "abc".getBytes(), StandardOpenOption.APPEND);
  }
}
