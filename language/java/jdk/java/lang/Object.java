class Main {
  public static void main(String[] args) {

    // Instance methods
    _equals();
    _getClass();
    _toString();
  }

  static void _equals() {
    Object a = "Hey";
    Object b = "Hey";

    a.equals(b); // true
  }

  static void _getClass() {
    Object a = "Hey";

    // get the class type at runtime
    Class clazz = a.getClass(); // class java.lang.String
  }

  static void _toString() {
    Object p = new Person(1, "Henry");

    p.toString(); // Person@3911c2a7 (unless overridden)

    System.out.println(p.toString());
    System.out.println(p); // no need to call .toString() - it's done automatically
  }
}

class Person {
  int number;
  String name;

  public Person(int number, String name) {
    this.number = number;
    this.name = name;
  }

  @Override
  public String toString() {
    return "Person [name=" + name + ", number=" + number + "]";
  }
}
