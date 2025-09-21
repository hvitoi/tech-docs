import java.util.Comparator;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();
    _comparing();
  }

  static void _new() {
    // Anonymous class
    var comparator1 = new Comparator<String>() {
      @Override
      public int compare(String a, String b) {
        return a.compareTo(b);
      }
    };

    // Lambda
    Comparator<Integer> comparator2 = (a, b) -> Integer.compare(a, b);

  }

  static void _comparing() {
    // It's a factory method
    // You specify just what field will be used to compare
    var comparator1 = Comparator.comparing(Person::getAge);
    var comparator2 = Comparator.comparing((Person p) -> p.getAge()); // same
  }
}

class Person {
  String name;
  int age;

  public Person(String name, int age) {
    this.name = name;
    this.age = age;
  }

  public String getName() {
    return name;
  }

  public int getAge() {
    return age;
  }

}
