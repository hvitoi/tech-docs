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
    ObjectOutputStreamNew.run();

    // Instance methods
    ObjectOutputStreamWriteObject.run();
    ObjectOutputStreamFlush.run();
    ObjectOutputStreamClose.run();

  }
}

class ObjectOutputStreamNew {
  static ObjectOutputStream run() {
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
}

class ObjectOutputStreamWriteObject {
  static void run() {
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

class ObjectOutputStreamFlush {
  static void run() {
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

class ObjectOutputStreamClose {
  static void run() {
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