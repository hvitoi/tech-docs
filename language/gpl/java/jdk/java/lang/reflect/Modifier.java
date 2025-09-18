import java.lang.reflect.Modifier;

class Main {
  public static void main(String[] args) {
    ClassGetModifiers.run();

    // Static methods
    _isAbstract();
    _isPublic();

  }

  static void _isAbstract() {
    Class clazz = new Person().getClass();
    int personModifiers = clazz.getModifiers();

    boolean isAbstract = Modifier.isAbstract(personModifiers); // false
    // System.out.println(isAbstract);
  }

  static void _isPublic() {
    Class clazz = new Person().getClass();
    int personModifiers = clazz.getModifiers();

    boolean isPublic = Modifier.isPublic(personModifiers); // true
    // System.out.println(isPublic);
  }
}

class ClassGetModifiers {
  static void run() {
    Class clazz = new Person().getClass();
    int personModifiers = clazz.getModifiers(); // 1
  }
}

class Person {
  private String name;
  private int age;
}
