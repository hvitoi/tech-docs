import java.util.ArrayList;
import java.util.List;

class Main {
  public static void main(String[] args) {
    System.out.println("Total: " + Person.getTotal());

    for (var p : Person.people) {
      System.out.println(p);
    }
  }
}

// static attributes or methods belong to the class (and not to the instance)
class Person {

  // instance fields
  private String firstName;
  private String lastName;
  private int age;

  // static fields
  static int total;
  static List<Person> people = new ArrayList<>();

  // constructor
  public Person(String firstName, String lastName, int age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    total++;
  }

  // static block to initialize some data
  static {
    people.add(new Person("Henry", "Doe", 14));
    people.add(new Person("Albert", "Doe", 15));
    people.add(new Person("John", "Doe", 16));
  }

  // static methods
  public static int getTotal() {
    return total;
  }

  // toString override for printing
  @Override
  public String toString() {
    return firstName + " " + lastName + " (" + age + ")";
  }

}
