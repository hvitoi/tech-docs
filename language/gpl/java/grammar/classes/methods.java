class Main {
  public static void main(String[] args) {
    Greetings.sayHello();
    Greetings.sayHello("Henry");

    System.out.println(new Greetings().toString());
  }
}

class Greetings {

  /*
   * Method Overload
   *
   * It's when a method assumes more forms depending on its signature
   * It does not consider the method return type or the method visibility
   * It takes into account only the parameters and their types
   */
  static void sayHello() {
    System.out.println("Hello!");
  }

  static void sayHello(String name) {
    // System.out.println("Hello, " + name + "!");
    System.out.printf("Hello, %s!\n", name);
  }

  /*
   * Method Override
   *
   * Allows Polymorphism. That is: assuming a different
   * behavior from the super class
   */
  @Override // Ensures that you are overriding the method (and not creating a new one)
  public String toString() {
    return super.toString() + " xD";
  }
}
