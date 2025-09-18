class Main {
  public static void main(String[] args) {
    // Instance methods
    _toString();
    _equals();
    _getClass();
  }

  static void _toString() {
    var p = new Person("Henry", 30);
    System.out.println(p.toString()); // Person@3911c2a7 (unless overridden)
    System.out.println(p); // no need to call .toString() - it's done automatically
  }

  static void _equals() {
    var a = "Hey";
    var b = "Hey";
    a.equals(b); // true
  }

  static void _getClass() {
    var a = "Hey";
    var clazz = a.getClass(); // get class at runtime
    System.out.println(clazz);
  }

}

class Person {
  String name;
  int age;

  public Person(String name, int age) {
    this.name = name;
    this.age = age;
  }

  @Override
  public String toString() {
    return "Person [name=" + name + ", number=" + age + "]";
  }
}
