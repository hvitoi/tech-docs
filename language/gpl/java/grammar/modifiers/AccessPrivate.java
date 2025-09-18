class Main {
  public static void main(String[] args) {
  }
}

class Person {

  // private attribute
  private String firstName;
  private String lastName;

  // private constructor
  private Person() {
  }

  // private method
  private void sayHello() {
    System.out.println("Hello"); // can only be invoked in this own class
  }

  /**
   *
   * * Encapsulation
   */

  // private attributes are accessed externally by getters and setters

  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }

  public String getLastName() {
    return lastName;
  }

  public void setLastName(String lastName) {
    this.lastName = lastName;
  }

}
