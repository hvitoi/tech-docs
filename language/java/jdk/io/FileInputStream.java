import java.io.FileNotFoundException;
import java.io.FileInputStream;
import java.io.IOException;

class Main {
  public static void main(String[] args) {
    // Static methods
    FileInputStreamNew.run();

    // Instance methods
    FileInputStreamRead.run();
    FileInputStreamClose.run();

  }
}

class FileInputStreamNew {
  static FileInputStream run() {
    try {
      FileInputStream fileInputStream = new FileInputStream("file.txt");
      return fileInputStream;
    } catch (FileNotFoundException e) {
      return null;
    }
  }
}

class FileInputStreamRead {
  static void run() {

    FileInputStream fileInputStream = FileInputStreamNew.run();
    try {
      int binaryData = fileInputStream.read();
      fileInputStream.close();
    } catch (IOException e) {
    }

  }
}

class FileInputStreamClose {
  static void run() {

    FileInputStream fileInputStream = FileInputStreamNew.run();
    try {
      int binaryData = fileInputStream.read();
      fileInputStream.close();
    } catch (IOException e) {
    }

  }
}
