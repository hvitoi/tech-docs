import java.lang.reflect.Modifier;
import java.util.Arrays;
import java.util.List;

class Main {
  public static void main(String[] args) {
    ClassGetModifiers.run();

    // Static methods
    ModifierIsPublic.run();
    ModifierIsAbstract.run();

  }
}

class ClassGetModifiers {
  static void run() {
    Class clazz = new Person().getClass();
    int personModifiers = clazz.getModifiers(); // 1
  }
}

class ModifierIsAbstract {
  static void run() {
    Class clazz = new Person().getClass();
    int personModifiers = clazz.getModifiers();

    boolean isAbstract = Modifier.isAbstract(personModifiers); // false
    // System.out.println(isAbstract);

  }
}

class ModifierIsPublic {
  static void run() {
    Class clazz = new Person().getClass();
    int personModifiers = clazz.getModifiers();

    boolean isPublic = Modifier.isPublic(personModifiers); // true
    // System.out.println(isPublic);

  }
}

public class Person {
  private String name;
  private int age;
}
