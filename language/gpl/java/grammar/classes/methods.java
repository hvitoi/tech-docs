class Main {
  public static void main(String[] args) {
    Hello.sayHello();
    Hello.sayHello("Henry");
  }
}

// Overload is when a method assumes more forms depending on its signature
// Overload do not consider the method return type or the method visibility
// Overload takes into account only the parameters and their types
class Hello {
  static void sayHello() {
    System.out.println("Hello!");
  }

  static void sayHello(String name) {
    System.out.println("Hello, " + name + "!");
  }
}
