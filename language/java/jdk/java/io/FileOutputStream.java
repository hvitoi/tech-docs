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
      FileOutputStream fileOutputStream = new FileOutputStream("file.txt");
      return fileOutputStream;
    } catch (FileNotFoundException e) {
      return null;
    }
  }

  static void _write() {
    FileOutputStream fileOutputStream = _new();
    try {
      fileOutputStream.write(1234567890); // write binary to a file
      fileOutputStream.close();
    } catch (IOException e) {
    }
  }

  static void _close() {
    FileOutputStream fileOutputStream = _new();
    try {
      fileOutputStream.write(1234567890); // write binary to a file
      fileOutputStream.close();
    } catch (IOException e) {
    }
  }
}
