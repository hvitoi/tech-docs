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
      var fileInput = new FileInputStream("file.txt");
      return fileInput;
    } catch (FileNotFoundException e) {
      // e.printStackTrace();
      return null;
    }
  }

  static void _read() {
    // try-with-resources automatically closes stream
    try (var fileInput = _new()) {
      if (fileInput == null) {
        return;
      }
      int binaryData = fileInput.read();
      System.out.println("Read byte: " + binaryData);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  static void _close() {
    try {
      var fileInput = _new();
      if (fileInput == null) {
        return;
      }
      fileInput.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
