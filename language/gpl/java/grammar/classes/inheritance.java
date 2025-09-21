class Main {
  public static void main(String[] args) {

    Developer a1 = new Developer("Henry");
    a1.makeCoffee(); // child method
    a1.code(); // child method
    a1.code(99); // child method

    Employee a2 = new Developer("Maria"); // implicit casting
    a2.makeCoffee(); // child method (even though it's the Employee super class type)
    // a2.code(); // method inexistent
    // a2.code(99); // method inexistent
  }
}

class Employee {
  private String name;

  protected Employee(String name) {
    this.setName(name);
    System.out.println(this.getName() + "(Super Class): Constructor");
  }

  protected String getName() {
    return name;
  }

  protected void setName(String name) {
    this.name = name;
  }

  public void makeCoffee() {
    System.out.println(this.getName() + " (Super Class): makeCoffee Method");
  }

}

// In Java there is no multiple inheritance!
class Developer extends Employee {

  public Developer(String name) {
    super(name);
    System.out.println(super.getName() + "(Child Class): Constructor");
  }

  // Polymorphism: Overrides the method of the super class
  @Override // assure that you are overriding the method (and not creating a new one)
  public void makeCoffee() {
    System.out.println(super.getName() + "(Child Class): Dummy Method");
  }

  // Polymorphism: Overloads the method with different parameters
  public void code() {
    System.out.println(super.getName() + "(Child Class): Awesome Method - 0 param");
  }

  public void code(int uselessNumber) {
    System.out.println(super.getName() + "(Child Class): Awesome Method - 1 param");
  }

}
