import java.lang.reflect.Constructor;

class Main {
  public static void main(String[] args) {
    _getConstructors();
    _getConstructor();

    // Instance methods
    _getName();
    _newInstance();
  }

  static void _getConstructors() {
    Class clazz = new Person().getClass();

    // List containing public Person() constructor
    Constructor[] constructors = clazz.getConstructors();
  }

  static void _getConstructor() {
    Class clazz = new Person().getClass();

    // NoSuchMethodException is thrown is the constructor is not found
    // Constructor constructor1 = clazz.getConstructor(); // get constructor with no
    // args
    // Constructor constructor2 = clazz.getConstructor(String.class); // get
    // constructor with string arg
  }

  static void _getName() {
    Class clazz = new Person().getClass();
    Constructor[] constructors = clazz.getConstructors();

    for (Constructor constructor : constructors) {
      String constructorName = constructor.getName();
      System.out.println(constructorName);
    }
  }

  static void _newInstance() {
    Class clazz = new Person().getClass();
    Constructor constructor = clazz.getConstructors()[0]; // get first constructor (no args)

    // Instantiate a new object from an constructor
    // Person newPerson = (Person) constructor.newInstance();
  }
}

class Person {
  private String name;
  private int age;

  public Person() {
  }

  public Person(String name) {
    this.name = name;
  }
}
