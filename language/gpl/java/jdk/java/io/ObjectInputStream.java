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
    _readObject();
    _close();

  }

  static ObjectInputStream _new() {
    try {
      FileInputStream fileInputStream = new FileInputStream("file.txt");
      ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);
      return objectInputStream;
    } catch (FileNotFoundException e) { // for FileInputStream
      return null;
    } catch (IOException e) { // for ObjectInputStream
      return null;
    }
  }

  static void _readObject() {
    ObjectInputStream objectInputStream = ObjectInputStreamNew.run();
    try {
      Person p2 = (Person) objectInputStream.readObject(); // Person [age=20, height=null, name=Joe]
      objectInputStream.close();
    } catch (IOException e) {
    } catch (ClassNotFoundException e) {
    }
  }

  static void _close() {
    ObjectInputStream objectInputStream = ObjectInputStreamNew.run();
    try {
      Person p2 = (Person) objectInputStream.readObject(); // Person [age=20, height=null, name=Joe]
      objectInputStream.close();
    } catch (IOException e) {
    } catch (ClassNotFoundException e) {
    }
  }
}

class Person {

  private String name;
  private Integer age;
  transient Integer height;

}
