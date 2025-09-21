import java.util.Objects;

class Main {
  public static void main(String[] args) {
    // Instance methods
    _getClass();
    _toString();
    _equals();
  }

  static void _getClass() {
    var p = new Person("Henry", 30);
    var clazz = p.getClass(); // get class at runtime
  }

  static void _toString() {
    var p = new Person("Henry", 30);
    System.out.println(p.toString()); // Person@3911c2a7 (unless overridden)
    System.out.println(p); // no need to call .toString() - it's done automatically
  }

  static void _equals() {
    var p1 = new Person("Henry", 30);
    var p2 = new Person("Henry", 30);
    p1.equals(p2); // Uses the user-define equal implementation
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
    return String.format("Person{name='%s', number=%d]", name, age);
  }

  @Override
  public boolean equals(Object obj) {
    if (this == obj)
      return true; // same object
    if (obj == null || getClass() != obj.getClass())
      return false;
    Person other = (Person) obj;
    return age == other.age && Objects.equals(name, other.name);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, age);
  }
}
