class Main {

  // A field is a variable declared inside a class or interface, but outside any
  // method or constructor.
  public static void main(String[] args) {
    var person = new Person();
    person.setFirstName("Henrique"); // set private attribute
    person.lastName = "Boss"; // set public attribute
  }
}

class Person {
  private String firstName; // only the own class can access
  public String lastName; // anyone can access
  protected String motherName; // only own class and child classes can access
  int age;
  boolean isHappy = true; // default value
  char favoriteLetter;
  Pet pet = new Pet(); // default value

  // ---

  public String getFirstName() {
    return firstName;
  }

  public void setFirstName(String firstName) {
    this.firstName = firstName;
  }

}

class Pet {
  String name;
  String type;
}
