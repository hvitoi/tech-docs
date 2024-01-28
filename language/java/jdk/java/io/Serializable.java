import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

class Main {
  public static void main(String[] args) {
  }
}

class Person implements Serializable {

  /**
   * The JVM associates a version (long) number with each serializable class.
   * We use it to verify that the saved and loaded objects have the same
   * attributes, and thus are compatible on serialization.
   * If a serializable class doesn't declare a serialVersionUID, the JVM will
   * generate one automatically
   */

  private static final long serialVersionUID = 1L;

  // static attributes belongs to the class and won't be serialized
  static String country = "ITALY";

  // transient attributes belongs to the object but won't be serialized
  transient Integer height;

  private String name;
  private Integer age;
  private Address address; // must be serializable or NotSerializableException

  Person(String name, Integer age) {
    this.name = name;
    this.age = age;
  }

  public Address getAddress() {
    return address;
  }

  public void setAddress(Address address) {
    this.address = address;
  }

  // Custom Serialization
  private void writeObject(ObjectOutputStream oos) throws IOException {
    oos.defaultWriteObject();
    oos.writeObject(address.getHouseNumber());
  }

  // Custom Deserialization
  private void readObject(ObjectInputStream ois) throws ClassNotFoundException, IOException {
    ois.defaultReadObject();
    Integer houseNumber = (Integer) ois.readObject();
    Address a = new Address();
    a.setHouseNumber(houseNumber);
    this.setAddress(a);
  }

}

class Address {
  private Integer houseNumber;

  public Integer getHouseNumber() {
    return houseNumber;
  }

  public void setHouseNumber(Integer houseNumber) {
    this.houseNumber = houseNumber;
  }

}
