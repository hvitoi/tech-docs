import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

class Main {
  public static void main(String[] args) {
    // Static methods
    FileOutputStreamNew.run();

    // Instance methods
    FileOutputStreamWrite.run();
    FileOutputStreamClose.run();

  }
}

class FileOutputStreamNew {
  static FileOutputStream run() {
    try {
      FileOutputStream fileOutputStream = new FileOutputStream("file.txt");
      return fileOutputStream;
    } catch (FileNotFoundException e) {
      return null;
    }
  }
}

class FileOutputStreamWrite {
  static void run() {

    FileOutputStream fileOutputStream = FileOutputStreamNew.run();
    try {
      fileOutputStream.write(1234567890); // write binary to a file
      fileOutputStream.close();
    } catch (IOException e) {
    }

  }
}

class FileOutputStreamClose {
  static void run() {

    FileOutputStream fileOutputStream = FileOutputStreamNew.run();
    try {
      fileOutputStream.write(1234567890); // write binary to a file
      fileOutputStream.close();
    } catch (IOException e) {
    }

  }
}
