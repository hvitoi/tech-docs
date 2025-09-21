class Main {

  // A field is a variable declared inside of a class, but outside any
  // method or constructor (not a local variable).
  public static void main(String[] args) {
    var person = new Person();
    person.setFirstName("Henrique"); // set private field
    person.lastName = "Boss"; // set public field
  }
}

class Person {
  /**
   * Access modifiers
   * private < package private < protected < public
   */

  // Private
  // Accessible within the same class
  private String firstName; // only the own class can access

  // Package Private (default)
  // Accessible within the same package
  // When no access modifier is explicitly defined
  int age;

  // Protected
  // Accessible within the same package or by child classes (even if in different
  // packages)
  protected String motherName;

  // Public
  // Accessible from anywhere
  // The filename must follow the same class name
  public String lastName; // anyone can access

  /*
   * Default values
   */
  boolean isHappy = true;

  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }

}
