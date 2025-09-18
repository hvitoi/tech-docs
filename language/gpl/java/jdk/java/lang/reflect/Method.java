import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

class Main {
  public static void main(String[] args) {
    ClassGetDeclaredMethods.run();
    ClassGetDeclaredMethod.run();
    ClassGetMethods.run();
    ClassGetMethod.run();

    // Instance methods
    _getName();
    _invoke();
    // _getType();
    // _setAccessible();
    // _set();
    // _get();
    // _getBoolean();

  }

  static void _getName() {
    Class clazz = new Person().getClass();
    Method[] methods = clazz.getDeclaredMethods();

    for (Method method : methods) {
      String methodName = method.getName();
      System.out.println(methodName);
    }
  }

  static void _invoke() {
    Person person = new Person();
    Class clazz = person.getClass();

    try {
      Method method = clazz.getDeclaredMethod("printName");
      try {
        method.invoke(person);
      } catch (IllegalAccessException | InvocationTargetException e) {
        e.printStackTrace();
      }
      // method.invoke(person, arg1, arg2);
      // String name = (String) method.invoke(person);
    } catch (NoSuchMethodException e) {
    }
  }
}

class ClassGetDeclaredMethods {
  static void run() {
    Class clazz = new Person().getClass();

    // get only public methods of the class
    Method[] methods = clazz.getDeclaredMethods();
  }
}

class ClassGetDeclaredMethod {
  static void run() {
    Class clazz = new Person().getClass();

    try {
      Method method1 = clazz.getDeclaredMethod("printName"); // get method with 0 args
      Method method2 = clazz.getDeclaredMethod("printName", String.class); // get method with 1 string arg
    } catch (NoSuchMethodException e) {
    }

  }
}

class ClassGetMethods {
  static void run() {
    Class clazz = new Person().getClass();

    // return only the public methods in both the class and all superclasses
    Method[] methods = clazz.getMethods();
    // "equals", "notifyAll", "hashCode", "toString", "printName"
  }
}

class ClassGetMethod {
  static void run() {
    Class clazz = new Person().getClass();

    // return a single public method by its name
    try {
      Method method1 = clazz.getMethod("printName"); // get method with 0 args
      Method method2 = clazz.getMethod("printName", String.class); // get method with 1 string arg
    } catch (NoSuchMethodException e) {
    }

  }
}

class Person {
  private String name;
  private int age;

  public void printName() {
    System.out.println(this.name);
  }

  public void printName(String dummyString) {
    System.out.println(this.name);
  }
}
