import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

class Main {
  public static void main(String[] args) {
    // Instance methods
    _getName();
    _invoke();
  }

  static void _getName() {
    Method method = Person.class.getDeclaredMethods()[0]; // first method
    String methodName = method.getName(); // printName method (the one without args)
  }

  static void _invoke() {
    var p = new Person();
    Method method = p.getClass().getDeclaredMethods()[0];

    try {
      method.invoke(p);
      // method.invoke(p, "foo"); // with args
    } catch (IllegalAccessException | InvocationTargetException e) {
      e.printStackTrace();
    }

  }
}

class Person {

  public void printName() {
    //
  }

  public void printName(String dummyString) {
    //
  }
}
