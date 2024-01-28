import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _writeObject();
    _flush();
    _close();
  }

  static ObjectOutputStream _new() {
    try {
      FileOutputStream fileOutputStream = new FileOutputStream("file.txt"); // save to file
      ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream); // save obj to file
      return objectOutputStream;
    } catch (FileNotFoundException e) { // for FileOutputStream
      return null;
    } catch (IOException e) { // for ObjectOutputStream
      return null;
    }
  }

  static void _writeObject() {
    ObjectOutputStream objectOutputStream = ObjectOutputStreamNew.run();

    // Object -> Serialize -> File
    Person p1 = new Person("Joe", 20);
    try {
      objectOutputStream.writeObject(p1);
      objectOutputStream.flush();
      objectOutputStream.close();
    } catch (IOException e) {
    }

  }

  static void _flush() {
    ObjectOutputStream objectOutputStream = ObjectOutputStreamNew.run();

    // Object -> Serialize -> File
    Person p1 = new Person("Joe", 20);
    try {
      objectOutputStream.writeObject(p1);
      objectOutputStream.flush();
      objectOutputStream.close();
    } catch (IOException e) {
    }
  }

  static void _close() {
    ObjectOutputStream objectOutputStream = ObjectOutputStreamNew.run();

    // Object -> Serialize -> File
    Person p1 = new Person("Joe", 20);
    try {
      objectOutputStream.writeObject(p1);
      objectOutputStream.flush();
      objectOutputStream.close();
    } catch (IOException e) {
    }
  }
}

class Person implements Serializable {

  static String country = "ITALY"; // won't be serialized
  transient Integer height; // won't be serialized
  private String name;
  private Integer age;

  Person(String name, Integer age) {
    this.name = name;
    this.age = age;
  }
}
