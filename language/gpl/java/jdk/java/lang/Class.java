import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.stream.Stream;

class Main {
  public static void main(String[] args) {

    // Static methods
    _forName();

    // Instance methods
    _getName();
    _getCanonicalName();
    _getSimpleName();
    _getPackage();
    _getSuperclass();
    _getInterfaces();
    _getModifiers();

    _getDeclaredFields();
    _getDeclaredField();
    _getFields();
    _getField();

    _getDeclaredMethods();
    _getDeclaredMethod();
    _getMethods();
    _getMethod();

    _getConstructors();

  }

  static void _forName() {
    try {
      // returns the class associated with a given name
      Class clazz = Class.forName("Person");
      // System.out.println(clazz.getName());
    } catch (ClassNotFoundException e) {
    }
  }

  static void _getName() {
    var person = new Person();
    var clazz = person.getClass();
    clazz.getName(); // DQN: e.g., com.hvitoi.Person
  }

  static void _getCanonicalName() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    String classCanonicalName = clazz.getCanonicalName(); // com.hvitoi.Person
  }

  static void _getSimpleName() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    String classSimpleName = clazz.getSimpleName(); // Person
  }

  static void _getDeclaredFields() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    Field[] fields = clazz.getDeclaredFields();

    Stream.of(fields).anyMatch(e -> e.getType() == Integer.class); // check if any of the fields is an integer
  }

  static void _getDeclaredField() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    try {
      Field field = clazz.getDeclaredField("name");
    } catch (NoSuchFieldException e) {
    }
  }

  static void _getFields() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    // return only the public fields in both the class and all superclasses
    Field[] fields = clazz.getFields();
  }

  static void _getField() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    try {
      // return a single public field by its name
      Field field = clazz.getField("name");
    } catch (NoSuchFieldException e) {
    }
  }

  static void _getDeclaredMethods() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    Method[] methods = clazz.getDeclaredMethods();
  }

  static void _getDeclaredMethod() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    try {
      Method method = clazz.getDeclaredMethod("printName"); // public void Person.printName()
    } catch (NoSuchMethodException e) {
    }
  }

  static void _getMethods() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    // return only the public methods in both the class and all superclasses
    Method[] methods = clazz.getMethods();
    // "equals", "notifyAll", "hashCode", "toString", "printName"
  }

  static void _getMethod() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    // return a single public method by its name
    try {
      Method method = clazz.getMethod("printName"); // public void Person.printName()
    } catch (NoSuchMethodException e) {
    }
  }

  static void _getPackage() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    Package classPackage = clazz.getPackage();
  }

  static void _getSuperclass() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    Class<?> superClass = clazz.getSuperclass(); // class java.lang.Object
  }

  static void _getInterfaces() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    // Get interfaces that a class explicitly declares as implemented
    Class<?>[] classInterfaces = clazz.getInterfaces(); // list containing interface Printable
    // System.out.println(classInterfaces[0]);
  }

  static void _getConstructors() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    Constructor<?>[] constructors = clazz.getConstructors(); // list containing public Person() constructor
    // System.out.println(constructors[0]);
  }

  static void _getModifiers() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    int personModifiers = clazz.getModifiers(); // 1
  }
}

class Person implements Printable {
  private String name;
  private Integer age;

  @Override
  public void printName() {
    System.out.println(this.name + ": " + this.age.toString());
  }

}

interface Printable {
  void printName();
}
