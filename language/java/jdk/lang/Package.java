import java.util.Arrays;
import java.util.List;

class Main {
  public static void main(String[] args) {

    // Instance methods
    PackageGetName.run();

  }
}

class PackageGetName {
  static void run() {
    Class clazz = new Person().getClass();
    Package pkg = clazz.getPackage();

    String packageName = pkg.getName();
  }
}

public class Person {
  private String name;
  private int age;
}
