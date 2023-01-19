/*
 * Class class
 */

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.stream.Stream;

class Main {
  public static void main(String[] args) {

    // Static methods
    _forName.run();

    // Instance methods
    _getName.run();
    _getCanonicalName.run();
    _getSimpleName.run();
    _getPackage.run();
    _getSuperclass.run();
    _getInterfaces.run();
    _getModifiers.run();

    _getDeclaredFields.run();
    _getDeclaredField.run();
    _getFields.run();
    _getField.run();

    _getDeclaredMethods.run();
    _getDeclaredMethod.run();
    _getMethods.run();
    _getMethod.run();

    _getConstructors.run();

  }
}

class _forName {
  static void run() {
    try {
      Class.forName("Person"); // FQN: e.g., com.hvitoi.Person
    } catch (ClassNotFoundException e) {
    }

  }
}

class _getName {
  static void run() {
    // Get class from an instance
    var person = new Person();
    var clazz = person.getClass();
    clazz.getName(); // DQN: e.g., com.hvitoi.Person
  }
}

class _getCanonicalName {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    String classCanonicalName = clazz.getCanonicalName(); // com.hvitoi.Person
  }
}

class _getSimpleName {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    String classSimpleName = clazz.getSimpleName(); // Person

  }
}

class _getDeclaredFields {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    Field[] fields = clazz.getDeclaredFields();

    Stream.of(fields).anyMatch(e -> e.getType() == Integer.class); // check if any of the fields is an integer
  }
}

class _getDeclaredField {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    try {
      Field field = clazz.getDeclaredField("name");
    } catch (NoSuchFieldException e) {
    }

  }
}

class _getFields {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    // return only the public fields in both the class and all superclasses
    Field[] fields = clazz.getFields();
  }
}

class _getField {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    try {
      // return a single public field by its name
      Field field = clazz.getField("name");
    } catch (NoSuchFieldException e) {
    }
  }
}

class _getDeclaredMethods {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    Method[] methods = clazz.getDeclaredMethods();
  }
}

class _getDeclaredMethod {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    try {
      Method method = clazz.getDeclaredMethod("printName"); // public void Person.printName()
    } catch (NoSuchMethodException e) {
    }

  }
}

class _getMethods {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    // return only the public methods in both the class and all superclasses
    Method[] methods = clazz.getMethods();
    // "equals", "notifyAll", "hashCode", "toString", "printName"
  }
}

class _getMethod {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    // return a single public method by its name
    try {
      Method method = clazz.getMethod("printName"); // public void Person.printName()
    } catch (NoSuchMethodException e) {
    }

  }
}

class _getPackage {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    Package classPackage = clazz.getPackage();
  }
}

class _getSuperclass {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    Class<?> superClass = clazz.getSuperclass(); // class java.lang.Object
  }
}

class _getInterfaces {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    // Get interfaces that a class explicitly declares as implemented
    Class<?>[] classInterfaces = clazz.getInterfaces(); // list containing interface Printable
    // System.out.println(classInterfaces[0]);
  }
}

class _getConstructors {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    Constructor<?>[] constructors = clazz.getConstructors(); // list containing public Person() constructor
    // System.out.println(constructors[0]);
  }
}

class _getModifiers {
  static void run() {
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