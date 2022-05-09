import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.stream.Stream;

class Main {
  public static void main(String[] args) {

    // Static methods
    ClassForName.run();

    // Instance methods
    ClassGetName.run();
    ClassGetCanonicalName.run();
    ClassGetSimpleName.run();
    ClassGetPackage.run();
    ClassGetSuperclass.run();
    ClassGetInterfaces.run();
    ClassGetModifiers.run();

    ClassGetDeclaredFields.run();
    ClassGetDeclaredField.run();
    ClassGetFields.run();
    ClassGetField.run();

    ClassGetDeclaredMethods.run();
    ClassGetDeclaredMethod.run();
    ClassGetMethods.run();
    ClassGetMethod.run();

    ClassGetConstructors.run();

  }
}

class ClassForName {
  static void run() {
    try {
      Class<?> clazz = Class.forName("Person"); // FQN: e.g., com.hvitoi.Person
    } catch (ClassNotFoundException e) {
    }

  }
}

class ClassGetName {
  static void run() {
    // Get class from an instance
    Person person = new Person();
    Class<?> clazz = person.getClass();
    String className = clazz.getName(); // DQN: e.g., com.hvitoi.Person
  }
}

class ClassGetCanonicalName {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    String classCanonicalName = clazz.getCanonicalName(); // com.hvitoi.Person
  }
}

class ClassGetSimpleName {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    String classSimpleName = clazz.getSimpleName(); // Person

  }
}

class ClassGetDeclaredFields {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    Field[] fields = clazz.getDeclaredFields();

    Stream.of(fields).anyMatch(e -> e.getType() == Integer.class); // check if any of the fields is an integer
  }
}

class ClassGetDeclaredField {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    try {
      Field field = clazz.getDeclaredField("name");
    } catch (NoSuchFieldException e) {
    }

  }
}

class ClassGetFields {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    // return only the public fields in both the class and all superclasses
    Field[] fields = clazz.getFields();
  }
}

class ClassGetField {
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

class ClassGetDeclaredMethods {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    Method[] methods = clazz.getDeclaredMethods();
  }
}

class ClassGetDeclaredMethod {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    try {
      Method method = clazz.getDeclaredMethod("printName"); // public void Person.printName()
    } catch (NoSuchMethodException e) {
    }

  }
}

class ClassGetMethods {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    // return only the public methods in both the class and all superclasses
    Method[] methods = clazz.getMethods();
    // "equals", "notifyAll", "hashCode", "toString", "printName"
  }
}

class ClassGetMethod {
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

class ClassGetPackage {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    Package classPackage = clazz.getPackage();
  }
}

class ClassGetSuperclass {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();
    Class<?> superClass = clazz.getSuperclass(); // class java.lang.Object
  }
}

class ClassGetInterfaces {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    // Get interfaces that a class explicitly declares as implemented
    Class<?>[] classInterfaces = clazz.getInterfaces(); // list containing interface Printable
    // System.out.println(classInterfaces[0]);
  }
}

class ClassGetConstructors {
  static void run() {
    Person person = new Person();
    Class<?> clazz = person.getClass();

    Constructor<?>[] constructors = clazz.getConstructors(); // list containing public Person() constructor
    // System.out.println(constructors[0]);
  }
}

class ClassGetModifiers {
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