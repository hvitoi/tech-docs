import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;

class Main {
  public static void main(String[] args) {
    // Instance methods
    _getName();
    _newInstance();
  }

  static void _getName() {
    Constructor<?>[] constructors = Person.class.getConstructors();

    for (var constructor : constructors) {
      String name = constructor.getName();
    }
  }

  static void _newInstance() {
    // get first constructor (no args)
    Constructor<?> constructor = Person.class.getConstructors()[0];

    // Instantiate a new object with the constructor
    try {
      Person p = (Person) constructor.newInstance();
    } catch (InstantiationException | IllegalAccessException | IllegalArgumentException | InvocationTargetException e) {
      e.printStackTrace();
    }
  }
}

class Person {
  private String name;

  public Person() {
  }

  public Person(String name) {
    this.name = name;
  }
}
