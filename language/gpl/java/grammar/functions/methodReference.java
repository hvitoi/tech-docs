import java.util.stream.Stream;

// converts a method into a lambda

/*
 * object::instanceMethod
 * Class::instanceMethod
 * Class::staticMethod
 * Class::new (constructor reference)
 */

class Main {
  public static void main(String[] args) {

    Stream
        .of("Henrique", "Abrantes", "Vitoi")
        .map(String::length) // class::instanceMethod - el -> el.length()
        .forEach(System.out::println); // object::instanceMethod - el -> System.out.println(el)
  }
}
