class Main {
  public static void main(String[] args) {

    // Instantiation
    Person person1 = new Person();
    Person person2 = new Person();
    Person person3 = person1;

    // References
    System.out.println(person1 == person2); // false
    System.out.println(person1 == person3); // true

    // addresses to instances (objects) take the form Person@e056f20
  }
}

class Person {
  private String firstName;
  private String lastName;
}
