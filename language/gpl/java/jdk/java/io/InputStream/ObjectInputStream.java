import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.ObjectInputStream;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _readObject();
    // _close();
  }

  static ObjectInputStream _new() {
    try {
      var fileInput = new FileInputStream("file.txt");
      var objectInput = new ObjectInputStream(fileInput);
      return objectInput;
    } catch (FileNotFoundException e) { // for FileInputStream
      // e.printStackTrace();
      return null;
    } catch (IOException e) {
      e.printStackTrace();
      return null;
    }
  }

  static void _readObject() {

    try (var objectInput = _new()) { // try-with-resources ensures closing
      if (objectInput == null) {
        return;
      }
      Object obj = objectInput.readObject();
      System.out.println("Read object: " + obj);
    } catch (IOException | ClassNotFoundException e) {
      e.printStackTrace();
    }
  }

  static void _close() {
    var objectInput = _new();
    if (objectInput == null) {
      return;
    }
    try {
      objectInput.close();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
