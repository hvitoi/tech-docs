class Main {
  public static void main(String[] args) {
  }
}

// static attributes or methods belong to the class (and not to the instance)
class Person {

  // static attributes
  static int total;

  // static procedures
  static {
    people.add(new Person("Henry", "Doe", 14));
    people.add(new Person("Albert", "Doe", 14));
    people.add(new Person("John", "Doe", 14));
  }

  // static method
  public static int getTotal() {
    return Person.total;
  }

  // static method
  public static void setTotal(int total) {
    Person.total = total;
  }

}
