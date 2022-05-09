class Person {

  // protected attribute
  protected String firstName;
  protected String lastName;

  // protected constructor
  protected Person() {
  }

  // protected method
  protected void sayHello() {
    System.out.println("Hello"); // can only be invoked in this class or its children
  }

}