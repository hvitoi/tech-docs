import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _read();
    _close();

  }

  static FileInputStream _new() {
    try {
      FileInputStream fileInputStream = new FileInputStream("file.txt");
      return fileInputStream;
    } catch (FileNotFoundException e) {
      return null;
    }
  }

  static void _read() {
    FileInputStream fileInputStream = _new();
    try {
      int binaryData = fileInputStream.read();
      fileInputStream.close();
    } catch (IOException e) {
    }
  }

  static void _close() {
    FileInputStream fileInputStream = _new();
    try {
      int binaryData = fileInputStream.read();
      fileInputStream.close();
    } catch (IOException e) {
    }
  }
}
