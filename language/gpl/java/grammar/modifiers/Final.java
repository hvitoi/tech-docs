class Main {
  public static void main(String[] args) {
  }
}

// class cannot be modified
final class Person {

  // final attributes (do not change)
  final String firstName = "Henry"; // must be initialized
  final String lastName = "Boss"; // must be initialized

  // final method
  final void sayHello() {
    System.out.println("Hello");
  }

}
