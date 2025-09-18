class Main {
  public static void main(String[] args) {

    // Instantiate Child Class with Child Type
    Developer a1 = new Developer("Henry");
    a1.dummyMethod(); // child method
    a1.awesomeMethod(); // child method
    a1.awesomeMethod(99); // child method

    // Instantiate Child Class with Super Type
    Employee a2 = new Developer("Maria"); // Polymorphism
    a2.dummyMethod(); // child method (event though it's the Employee super class type)
    // a2.awesomeMethod(); // method inexistent
    // a2.awesomeMethod(99); // method inexistent
  }
}

class Employee {
  private String firstName;

  // ---

  protected Employee(String firstName) {
    this.setFirstName(firstName);
    System.out.println(this.getFirstName() + "(Super Class): Constructor");
  }

  // ---

  protected String getFirstName() {
    return firstName;
  }

  protected void setFirstName(String firstName) {
    this.firstName = firstName;
  }

  // ---

  public void dummyMethod() {
    System.out.println(this.getFirstName() + " (Super Class): Dummy Method");
  }

}

// In Java there is no multiple inheritance!
class Developer extends Employee {

  public Developer(String firstName) {
    super(firstName);
    System.out.println(super.getFirstName() + "(Child Class): Constructor");
  }
  // ---

  // Polymorphism: Overrides the dummyMethod of the super class
  @Override // assure that you are overriding the method (and not creating a new one)
  public void dummyMethod() {
    System.out.println(super.getFirstName() + "(Child Class): Dummy Method");
  }

  // ---

  // Polymorphism: same method with different parameters
  public void awesomeMethod() {
    System.out.println(super.getFirstName() + "(Child Class): Awesome Method - 0 param");
  }

  public void awesomeMethod(int uselessNumber) {
    System.out.println(super.getFirstName() + "(Child Class): Awesome Method - 1 param");
  }

}
