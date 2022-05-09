class Main {
  public static void main(String[] args) {

    // Instance methods
    ObjectEquals.run();
    ObjectGetClass.run();
    ObjectToString.run();
  }
}

class ObjectEquals {
  static void run() {
    Object a = "Hey";
    Object b = "Hey";

    a.equals(b); // true

  }
}

class ObjectGetClass {
  static void run() {
    Object a = "Hey";

    // get the class type at runtime
    Class clazz = a.getClass(); // class java.lang.String
  }
}

class ObjectToString {
  static void run() {
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