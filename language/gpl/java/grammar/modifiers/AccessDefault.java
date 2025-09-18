class Main {
  public static void main(String[] args) {
  }
}

class Person {

  // package private attribute
  String firstName;
  String lastName;
  String address;

  // package private constructor
  Person() {
  }

  // package private method
  void sayHello() {
    System.out.println("Hello");
  }

}
