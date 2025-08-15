import java.util.Arrays;
import java.util.List;

class Main {
  public static void main(String[] args) {

    // Instance methods
    _getName();
  }

  static void _getName() {
    Class clazz = new Person().getClass();
    Package pkg = clazz.getPackage();

    String packageName = pkg.getName();
  }
}

public class Person {
  private String name;
  private int age;
}
