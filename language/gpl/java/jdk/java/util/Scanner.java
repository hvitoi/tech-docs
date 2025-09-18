import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _nextLine();
  }

  static void _new() {
    var scanner = new Scanner(System.in);
  }

  static void _nextLine() {
    // Read from stdin
    var scanner = new Scanner(System.in);
    var input = scanner.nextLine();
    System.out.println("You typed: " + input);
  }
}
