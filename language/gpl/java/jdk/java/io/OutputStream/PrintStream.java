import java.io.PrintStream;

class Main {

  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _println();
    _printf();
  }

  static void _new() {
    PrintStream stdout = System.out;
  }

  static void _println() {
    PrintStream stdout = System.out;
    stdout.println("a");
  }

  static void _printf() {
    PrintStream stdout = System.out;
    var name = "Henry";
    stdout.printf("Hello, %s!", name);
  }

}
