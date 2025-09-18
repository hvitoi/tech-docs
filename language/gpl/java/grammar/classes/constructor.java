class Main {
  public static void main(String[] args) {
    // Instantiation
    var person1 = new Person();
    var person2 = new Person("Henry", "Boss");
  }
}

class Person {
  private String firstName;
  private String lastName;

  // Default Constructor
  public Person() {
  }

  // Constructor with Parameters
  public Person(String firstName, String lastName) { // overload
    this.firstName = firstName;
    this.lastName = lastName;
  }

}
