import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _write();
    _close();
  }

  static FileOutputStream _new() {
    try {
      return new FileOutputStream("file.txt");
    } catch (FileNotFoundException e) {
      e.printStackTrace();
      return null;
    }
  }

  static void _write() {
    try (var outputStream = _new()) { // auto-closable
      outputStream.write(1234567890); // write binary to a file
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  static void _close() {
    var fileOutputStream = _new();
    try {
      fileOutputStream.close();
    } catch (IOException e) {
      e.printStackTrace();
    }

  }
}
